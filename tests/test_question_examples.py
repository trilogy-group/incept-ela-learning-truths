"""Source fidelity and the boundary between reference material and labels."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import question_examples as examples
from example_adapters import extract_static_literals


class SourceCollectionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.cache = self.root / "cache"
        self.destination = self.root / "collection"
        self.config = self.root / "sources.json"
        self.document = {"units": [{"id": "u1", "lessons": [{"id": "lesson-one", "pages": [
            {"id": "reading", "nodes": [{"type": "passage", "paragraphs": ["An authored passage."]}]},
            {"id": "check", "nodes": [{"type": "question", "bank_type": "mcq", "stem": "Which answer fits?",
                                       "options": ["One", "Two"], "answer_index": 1}]}]}]}]}
        self.sources = []
        self.patches = [patch.object(examples, "SOURCE_CONFIG", self.config), patch.object(examples, "DESTINATION", self.destination)]
        for item in self.patches:
            item.start()

    def tearDown(self):
        for item in reversed(self.patches):
            item.stop()
        self.temp.cleanup()

    def source(self, name, document):
        raw = examples.encoded(document)
        commit = ("a" if not self.sources else "b") * 40
        path = self.cache / "repo" / commit / "lesson.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        self.sources.append({"id": name, "cache_repository": "repo", "commit": commit, "path": "lesson.json",
                             "sha256": examples.digest(raw), "as_of": "2026-10-14", "adapter": "renderer"})
        self.config.write_bytes(examples.encoded({"version": 1, "sources": self.sources}))
        return path

    def rows(self):
        return [json.loads(line) for line in (self.destination / "questions.jsonl").read_text().splitlines()]

    def save_rows(self, rows):
        path = self.destination / "questions.jsonl"
        path.write_text("".join(json.dumps(row) + "\n" for row in rows))
        catalog_path = self.destination / "catalog.json"
        catalog = json.loads(catalog_path.read_text())
        catalog["files"]["questions.jsonl"] = examples.digest(path.read_bytes())
        catalog_path.write_bytes(examples.encoded(catalog))

    def test_keeps_source_key_and_full_ordered_context(self):
        self.source("first", self.document)
        examples.collect(self.cache)
        row = self.rows()[0]
        self.assertEqual(row["native"]["answer_index"], 1)
        occurrence = row["occurrences"][0]
        context = json.loads((self.destination / occurrence["context"]).read_text())
        self.assertEqual(examples.at(context, occurrence["context_pointer"])["pages"][0]["nodes"][0]["paragraphs"], ["An authored passage."])
        self.assertEqual(examples.check(self.destination, self.cache)["external_source_comparisons"], 1)

    def test_asset_only_versions_share_row_and_keep_both_occurrences(self):
        self.source("first", self.document)
        second = copy.deepcopy(self.document)
        second["units"][0]["lessons"][0]["pages"][1]["nodes"][0]["audio_path"] = "audio/new.mp3"
        self.source("second", second)
        counts = examples.collect(self.cache)
        self.assertEqual((counts["unique_examples"], counts["source_occurrences"]), (1, 2))
        self.assertEqual(len(self.rows()[0]["occurrences"]), 2)

    def test_changed_authored_answer_is_a_separate_version(self):
        self.source("first", self.document)
        second = copy.deepcopy(self.document)
        second["units"][0]["lessons"][0]["pages"][1]["nodes"][0]["answer_index"] = 0
        self.source("second", second)
        self.assertEqual(examples.collect(self.cache)["unique_examples"], 2)

    def test_corrupt_source_cache_is_rejected_before_writing(self):
        path = self.source("first", self.document)
        path.write_text("{}")
        with self.assertRaisesRegex(ValueError, "source byte hash"):
            examples.collect(self.cache)
        self.assertFalse(self.destination.exists())

    def test_quality_label_cannot_be_smuggled_into_author_examples(self):
        self.source("first", self.document)
        examples.collect(self.cache)
        rows = self.rows()
        rows[0]["quality_label"] = "pass"
        self.save_rows(rows)
        with self.assertRaisesRegex(ValueError, "quality labels"):
            examples.check(self.destination)

    def test_changed_answer_rejected_even_after_rehashing_data_file(self):
        self.source("first", self.document)
        examples.collect(self.cache)
        rows = self.rows()
        rows[0]["native"]["answer_index"] = 0
        self.save_rows(rows)
        with self.assertRaisesRegex(ValueError, "content identity"):
            examples.check(self.destination)

    def test_changed_display_prompt_rejected_even_after_rehashing(self):
        self.source("first", self.document)
        examples.collect(self.cache)
        rows = self.rows()
        rows[0]["prompt"] = "A different prompt."
        self.save_rows(rows)
        with self.assertRaisesRegex(ValueError, "content identity"):
            examples.check(self.destination)

    def test_missing_question_is_not_hidden_by_rehashing(self):
        self.source("first", self.document)
        examples.collect(self.cache)
        self.save_rows([])
        with self.assertRaisesRegex(ValueError, "occurrence count"):
            examples.check(self.destination)

    def test_question_and_embedded_guided_check_are_distinguished(self):
        document = {"units": [{"lessons": [{"pages": [{"nodes": [{"type": "we_do", "question": "Find the evidence.",
                      "search": {"type": "question", "bank_type": "mcq", "stem": "Which line?", "options": ["A", "B"], "answer_index": 0}}]}]}]}]}
        items, _ = examples.extract_renderer(document)
        self.assertEqual([item["role"] for item in items], ["guided_task", "subcheck"])

    def test_vocabulary_assessment_and_ebsr_parts_are_not_dropped(self):
        document = {"units": [{"lessons": [{"pages": [{"nodes": [
            {"type": "vocab", "word": "epic", "say_back_line": "Give an example.", "assessment": {"rubric": "Names a feature."}},
            {"type": "question", "bank_type": "ebsr", "part_a": {"stem": "What happened?", "answer_index": 1},
             "part_b": {"stem": "Which line proves it?", "answer_index": 0}}]}]}]}]}
        items, _ = examples.extract_renderer(document)
        self.assertEqual([item["kind"] for item in items], ["vocabulary_routine", "ebsr", "ebsr_part", "ebsr_part"])

    def test_qti_response_ids_cardinality_values_and_stimuli_survive(self):
        xml = '<qti-assessment-item><qti-response-declaration identifier="R" cardinality="multiple" base-type="identifier"><qti-correct-response><qti-value>A</qti-value><qti-value>B</qti-value></qti-correct-response></qti-response-declaration><qti-assessment-stimulus-ref identifier="s1"/><qti-choice-interaction max-choices="2"><qti-prompt>Pick two.</qti-prompt></qti-choice-interaction></qti-assessment-item>'
        document = {"items": [{"xml": xml}], "stimuli": {"s1": {"xml": "<p>A passage.</p>"}}}
        items, _ = examples.extract(document, "qti-bundle")
        self.assertEqual(items[0]["kind"], "multiple_select")
        response = items[0]["view"]["authored_correct_responses"][0]
        self.assertEqual((response["identifier"], response["cardinality"], response["values"]), ("R", "multiple", ["A", "B"]))
        document["stimuli"] = {}
        with self.assertRaisesRegex(ValueError, "stimulus missing"):
            examples.extract(document, "qti-bundle")

    def test_static_source_calls_are_omitted_not_executed(self):
        parsed = extract_static_literals("const BAD = process.exit(9); const GOOD = [{q: 'A question?', answer: 1}];")
        self.assertEqual([item["name"] for item in parsed["literals"]], ["GOOD"])
        self.assertEqual(parsed["omissions"][0]["name"], "BAD")

    def test_dose_verdict_uses_authored_task_not_closing_feedback(self):
        document = {"pages": [{"id": "dose", "nodes": [{"type": "dose", "goal": "Find evidence.",
                     "explain_ask": "Explain your evidence.", "rebut_ask": "Answer the objection.",
                     "close": "That settles it.", "verdict_task": "Which line gives him away?",
                     "verdict": {"question": "What does it prove?"}}]}]}
        items, _ = examples.extract_animated(document)
        verdict = next(item for item in items if item["pointer"].endswith("/verdict"))
        self.assertEqual(verdict["prompt"], "Which line gives him away?")
        self.assertEqual(verdict["view"]["prompt"], "Which line gives him away?")

    def test_ebsr_same_choice_id_is_bound_to_each_response(self):
        xml = '<qti-assessment-item><qti-choice-interaction response-identifier="A" max-choices="1"><qti-prompt>Part A</qti-prompt><qti-simple-choice identifier="ChoiceA">First</qti-simple-choice></qti-choice-interaction><qti-choice-interaction response-identifier="B" max-choices="1"><qti-prompt>Part B</qti-prompt><qti-simple-choice identifier="ChoiceA">Second</qti-simple-choice></qti-choice-interaction></qti-assessment-item>'
        items, _ = examples.extract({"items": [{"xml": xml}], "stimuli": {}}, "qti-bundle")
        self.assertEqual(items[0]["kind"], "ebsr")
        choices = items[0]["view"]["choices"]
        self.assertEqual([(choice["identifier"], choice["response_identifier"], choice["interaction_index"]) for choice in choices],
                         [("ChoiceA", "A", 0), ("ChoiceA", "B", 1)])

    def test_student_text_redaction_fails_but_vetted_phonetic_syllable_survives(self):
        with patch.object(examples, "scrub", side_effect=lambda value: value.replace("internalperson", "[name]")):
            with self.assertRaisesRegex(ValueError, "learner wording"):
                examples.sanitize({"stem": "internalperson wrote this."})
        with patch.object(examples, "scrub", side_effect=lambda value: value.replace("stan", "[name]")):
            self.assertEqual(examples.sanitize({"text": "Say kon-stan-tih-NO-pul."})[0]["text"], "Say kon-stan-tih-NO-pul.")


if __name__ == "__main__":
    unittest.main()
