"""Collect authored reference activities as data, with exact source locations.

Source code is never executed. Copies retain intended answers and teaching
scaffolds; they do not contain evaluator verdicts or qualification labels.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import tempfile
import xml.etree.ElementTree as ET

from redact import scrub

ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ROOT / ".local" / "question-examples"
SOURCE_CONFIG = ROOT / "examples" / "sources.json"
VERSION = "authored-examples 0.1"


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def pointer(path):
    return "" if not path else "/" + "/".join(str(x).replace("~", "~0").replace("/", "~1") for x in path)


def at(value, location):
    if location == "":
        return value
    if not location.startswith("/"):
        raise ValueError("invalid JSON pointer")
    for token in location[1:].split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        value = value[int(token)] if isinstance(value, list) else value[token]
    return value


def walk(value, path=()):
    if isinstance(value, dict):
        yield path, value
        for key, child in value.items():
            yield from walk(child, path + (key,))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, path + (index,))


MARKER_KEYS = {"requirement", "accept", "looks_like", "misreadings", "rubric", "expects", "assessment"}
METADATA_KEYS = {"source", "author", "authors", "created_by", "updated_by", "made_by"}


def sanitize(value):
    """Remove internal metadata; never silently change learner wording."""
    changes = []

    def visit(item, path=(), marker=False):
        if isinstance(item, dict):
            result = {}
            for key, child in item.items():
                if key.startswith("_") or key in METADATA_KEYS or (key == "reason" and path and path[-1] == "voiceover"):
                    changes.append({"pointer": pointer(path + (key,)), "action": "metadata-removed"})
                    continue
                result[key] = visit(child, path + (key,), marker or key in MARKER_KEYS)
            return result
        if isinstance(item, list):
            return [visit(child, path + (index,), marker) for index, child in enumerate(item)]
        if isinstance(item, str):
            # This vetted pronunciation contains a syllable that happens to
            # match a local privacy term. Preserve the author's actual text.
            phonetic = "kon-stan-tih-NO-pul"
            protected = item.replace(phonetic, "PHONETICSYLLABLEPLACEHOLDER")
            cleaned = scrub(protected).replace("PHONETICSYLLABLEPLACEHOLDER", phonetic)
            if cleaned != item:
                source_note = "extra" in path and item.startswith("VIDEO (optional, per ")
                if not marker and not source_note:
                    raise ValueError("learner wording needs a privacy review at " + pointer(path))
                changes.append({"pointer": pointer(path), "action": "metadata-text-redacted" if source_note else "marker-text-redacted"})
            if re.search(r"(?:Bearer\s+[A-Za-z0-9_-]{20}|(?:apk_|apikey_)[A-Za-z0-9_-]{16}|[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}|/Users/)", cleaned):
                raise ValueError("private metadata at " + pointer(path))
            return cleaned
        return item

    return visit(value), changes


def semantic(value):
    """Asset hashes/paths do not make a different wording or answer variant."""
    if isinstance(value, dict):
        return {key: semantic(child) for key, child in value.items()
                if not (key.endswith(("_path", "_paths", "_of", "_marks")) or key in {"marks", "voice", "autoplay"})}
    if isinstance(value, list):
        return [semantic(child) for child in value]
    return value


def prompt_of(node):
    for key in ("stem", "q", "question", "prompt", "task", "ask", "instruction", "goal", "line"):
        if isinstance(node.get(key), str) and node[key].strip():
            return node[key]
    return None


def unit(kind, role, path, native, prompt=None, context=()):
    return {"kind": kind, "role": role, "pointer": pointer(path),
            "prompt": prompt if prompt is not None else prompt_of(native),
            "native": native, "context_pointer": pointer(context)}


def extract_renderer(document):
    result = []
    page_nodes = {"speak", "we_do", "think_aloud", "dialogue", "vocab"}
    for path, node in walk(document):
        typ = node.get("type")
        # Root course nodes and nested typed search/knowledge checks both count.
        if typ == "question":
            role = "guided_task" if node.get("mode") == "guided" else "question"
            if "nodes" not in path or path[-2] != "nodes":
                role = "subcheck"
            prompt = prompt_of(node) or prompt_of(node.get("part_a", {}))
            result.append(unit(node.get("bank_type", "question"), role, path, node, prompt))
        elif typ in page_nodes:
            if typ == "speak":
                role = "question" if node.get("assessment") or node.get("mode") == "open" else "recall_task"
                kind = "spoken_response"
            elif typ == "think_aloud":
                kind, role = "worked_example", "model_task"
            elif typ == "vocab":
                if not any(node.get(key) for key in ("routine", "v3", "assessment", "say_back_line")):
                    continue
                kind, role = "vocabulary_routine", "guided_task"
            else:
                kind, role = typ, "guided_task"
            prompt = prompt_of(node)
            if typ == "dialogue":
                prompt = prompt_of(node.get("opening", {})) or prompt_of(node.get("ladder", {}).get("opening", {})) or prompt
            if typ == "vocab":
                prompt = node.get("say_back_line") or node.get("v3", {}).get("type_line") or node.get("word")
            result.append(unit(kind, role, path, node, prompt))
        # Film checks carry question data without type=question.
        elif path and path[-1] == "question" and isinstance(node.get("stem"), str) and node.get("options"):
            result.append(unit("video_mcq", "question", path, node))
        # Author-defined parts inside a teaching task are separate subchecks,
        # not additional independent measurements.
        elif path and any(key in path for key in ("annotations", "blanks")) and isinstance(node.get("ask"), str):
            result.append(unit("annotation_check" if "annotations" in path else "writing_blank", "subcheck", path, node))
        elif path and path[-1] == "evidence" and "sentences" in node and ("correct_index" in node or "correct_indices" in node):
            result.append(unit("evidence_selection", "subcheck", path, node))
        elif path and path[-1] in {"why_check", "hunt", "search"} and prompt_of(node) and typ != "question":
            result.append(unit("guided_check", "subcheck", path, node))
        elif path and path[-1] == "hunt" and "reading_notes" in path and node.get("accept"):
            parent = at(document, pointer(path[:-1]))
            prompt = parent.get("label") or parent.get("title") or parent.get("text")
            result.append(unit("reading_note_recall", "recall_task", path, node, prompt))
        elif path and path[-1] in {"follow_up", "opening", "floor"} and "dialogue" not in path and prompt_of(node):
            # Branches are authored follow-up routes, not tasks everyone sees.
            if any(key in path for key in ("branches", "ladder")):
                result.append(unit("dialogue_follow_up", "subcheck", path, node))
        elif path and path[-1] == "check" and "routine" in path and prompt_of(node):
            result.append(unit("vocabulary_check", "subcheck", path, node))
        elif path and path[-1] in {"part_a", "part_b"} and prompt_of(node):
            result.append(unit("ebsr_part", "subcheck", path, node))
        elif typ == "text" and isinstance(node.get("beats"), list):
            asks = [beat["ask"] for beat in node["beats"] if isinstance(beat, dict) and isinstance(beat.get("ask"), str)]
            has_choices = any(isinstance(beat, dict) and beat.get("choices") for beat in node["beats"])
            if asks and has_choices:
                result.append(unit("reflective_choice", "guided_task", path, node, asks[0]))
        if isinstance(node.get("ladder"), dict):
            for key in ("narrow_question", "who_question", "want_question"):
                text = node["ladder"].get(key)
                if isinstance(text, str) and text.strip():
                    result.append(unit("dialogue_branch_prompt", "subcheck", path + ("ladder", key), text, text))
    # The lesson ancestor gives the complete ordered stimulus and scaffolds.
    for item in result:
        tokens = item["pointer"].split("/")[1:]
        if "lessons" in tokens:
            end = tokens.index("lessons") + 2
        else:
            end = tokens.index("units") + 2 if "units" in tokens else 0
        item["context_pointer"] = "/" + "/".join(tokens[:end]) if end else ""
    return result, []


def extract_animated(document):
    # The original contract extractor remains unchanged and pinned. Split each
    # node into a one-page lesson so later nodes cannot be lost at nodes[0].
    module_path = ROOT / "contract" / "scripts" / "extract_authored.py"
    spec = importlib.util.spec_from_file_location("authored_contract_extractor", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    result, omissions = [], []
    for pi, page in enumerate(document.get("pages", [])):
        for ni, node in enumerate(page.get("nodes", [])):
            base = ("pages", pi, "nodes", ni)
            small = {"pages": [{**page, "nodes": [node]}]}
            try:
                old_items = module.items_of(small)
            except (KeyError, TypeError, ValueError, AttributeError) as error:
                old_items = []
                omissions.append({"pointer": pointer(base), "reason": "contract-adapter-shape", "error_type": type(error).__name__})
            for item in old_items:
                local = item["pointer"].removeprefix("/pages/0/nodes/0")
                location = pointer(base) + local
                native = at(document, location)
                view = item["view"]
                if item["kind"] == "word_web" and isinstance(view.get("prompt"), list):
                    view = {**view, "prompt": [text for text in view["prompt"] if text is not None]}
                if node.get("type") == "dose" and local == "/verdict":
                    view = {**view, "prompt": node.get("verdict_task") or native.get("question")}
                prompt = view.get("stem") or view.get("prompt")
                role = "question"
                if item["kind"] in {"rebuild_choice", "say_back"}:
                    role = "recall_task"
                elif item["kind"] in {"word_web", "evidence_select", "classify"}:
                    role = "guided_task"
                if "/moves/rubrics/" in location:
                    role = "subcheck"
                result.append({**unit(item["kind"], role, base, native, prompt), "pointer": location,
                               "view": view, "operation": item["id"], "context_pointer": pointer(("pages", pi))})
                if node.get("type") == "reading" and node.get("mcqs") and local == "/rubric":
                    result[-1]["exposure_status"] = "retained written alternative; source MCQs replace this check; actual rendering unverified"
            # Quote analysis questions and current task rounds were absent from
            # the original 40-unit contract adapter.
            for relative, child in walk(node):
                if not relative:
                    continue
                if "breakdown" in relative and prompt_of(child):
                    result.append(unit("quote_analysis", "subcheck", base + relative, child, context=("pages", pi)))
                elif any(key in relative for key in ("tasks", "rounds")) and prompt_of(child):
                    result.append(unit("argument_round", "subcheck", base + relative, child, context=("pages", pi)))
                elif "breakdown" in relative and isinstance(child.get("words"), dict):
                    prompts = node.get("unpick_q", [])
                    text = prompts[1] if len(prompts) > 1 else None
                    selected = unit("quote_word_selection", "guided_task", base + relative + ("words",), child["words"], text, context=("pages", pi))
                    selected["view"] = {"source_prompt": text, "word_class_labels": child["words"], "preferred_word_key": None,
                                        "meaning": "The table supplies word classes; it does not specify which word does the most work."}
                    result.append(selected)
            if node.get("type") == "keyword_cards":
                check_node = node.get("check")
                if isinstance(check_node, dict) and prompt_of(check_node):
                    value = unit("cloze", "recall_task", base + ("check",), check_node, context=("pages", pi))
                    value["view"] = {key: check_node.get(key) for key in ("prompt", "before", "after", "correct")}
                    result.append(value)
                else:
                    result.append(unit("keyword_cards", "recall_task", base, node, context=("pages", pi)))
            if node.get("type") == "apply" and not node.get("rubrics"):
                for index, text in enumerate(node.get("stems", [])):
                    if isinstance(text, str):
                        result.append(unit("writing_stem", "model_task", base + ("stems", index), text, text, context=("pages", pi)))
                omissions = [miss for miss in omissions if miss["pointer"] != pointer(base)]
            if node.get("type") == "evaluate" and not node.get("rubric") and node.get("question"):
                result.append(unit("open_prompt", "question", base, node, node["question"], context=("pages", pi)))
                omissions = [miss for miss in omissions if miss["pointer"] != pointer(base)]
            if not old_items and not any(item["pointer"].startswith(pointer(base)) for item in result):
                if any(key in node for key in ("rubric", "task", "check", "mcqs", "verdict")):
                    omissions.append({"pointer": pointer(base), "reason": "unmapped-response-node", "type": node.get("type")})
    record = document.get("record", {})
    if isinstance(record, dict) and isinstance(record.get("confidence"), str):
        result.append(unit("confidence_self_report", "question", ("record", "confidence"), record["confidence"], record["confidence"], context=()))
    return result, omissions


def extract(document, adapter):
    if adapter == "renderer":
        return extract_renderer(document)
    if adapter == "animated":
        return extract_animated(document)
    if adapter == "three-d":
        from example_adapters import extract_three_d, three_d_omissions
        return extract_three_d(document), three_d_omissions(document)
    if adapter == "three-d-literals":
        items = []
        for specification in document["projection"]:
            items.append({**specification, "native": at(document, specification["pointer"])})
        return items, document["parser_omissions"]
    if adapter == "alpha-read":
        items = []
        for li, lesson in enumerate(document["lessons"]):
            for qi, node in enumerate(lesson.get("questions", [])):
                items.append(unit("multiple_select" if sum(bool(choice.get("correct")) for choice in node.get("choices", [])) > 1 else "multiple_choice",
                                  "question", ("lessons", li, "questions", qi), node, node.get("prompt"), context=("lessons", li)))
        return items, []
    if adapter == "qti-bundle":
        items = []
        for index, node in enumerate(document["items"]):
            text = node["xml"]
            if "<!DOCTYPE" in text.upper() or "<!ENTITY" in text.upper():
                raise ValueError("QTI entities are unsupported")
            root = ET.fromstring(text)
            elements = list(root.iter())
            local = lambda element: element.tag.rsplit("}", 1)[-1]
            interactions = [element for element in elements if local(element).endswith("interaction")]
            primary = next((element for element in interactions if local(element) != "qti-choice-interaction"), interactions[0] if interactions else None)
            name = local(primary) if primary is not None else "unknown"
            mapping = {"qti-choice-interaction": "multiple_choice", "qti-match-interaction": "matching",
                       "qti-order-interaction": "sequence", "qti-hottext-interaction": "hot_text"}
            kind = mapping.get(name, "qti_unsupported")
            if len([element for element in interactions if local(element) == "qti-choice-interaction"]) > 1:
                kind = "ebsr"
            if name == "qti-choice-interaction" and primary.get("max-choices") not in {None, "1"}:
                kind = "multiple_select"
            prompts = ["".join(element.itertext()).strip() for element in elements if local(element) == "qti-prompt"]
            responses = []
            for declaration in elements:
                if local(declaration) != "qti-response-declaration":
                    continue
                values = ["".join(value.itertext()).strip() for response in declaration
                          if local(response) == "qti-correct-response" for value in response]
                responses.append({"identifier": declaration.get("identifier"), "cardinality": declaration.get("cardinality"),
                                  "base_type": declaration.get("base-type"), "values": values})
            choices = []
            for interaction_index, interaction in enumerate(interactions):
                sets = [element for element in interaction if local(element) == "qti-simple-match-set"]
                for element in interaction.iter():
                    if local(element) not in {"qti-simple-choice", "qti-simple-associable-choice", "qti-hottext"}:
                        continue
                    set_index = next((index for index, group in enumerate(sets) if element in list(group)), None)
                    choices.append({"identifier": element.get("identifier"), "text": "".join(element.itertext()),
                                    "interaction_index": interaction_index, "response_identifier": interaction.get("response-identifier"),
                                    "match_set_index": set_index})
            view = {"prompts": prompts,
                    "authored_correct_responses": responses,
                    "choices": choices,
                    "stimulus_ids": [element.get("identifier") for element in elements if local(element) == "qti-assessment-stimulus-ref"]}
            missing = set(view["stimulus_ids"]) - set(document["stimuli"])
            if missing:
                raise ValueError("QTI referenced stimulus missing")
            item = unit(kind, "question", ("items", index), node, prompts, context=())
            item["view"] = view
            items.append(item)
        return items, []
    if adapter == "scr-reference":
        entries = document.items() if isinstance(document, dict) else enumerate(document)
        return [unit("scaffolded_short_response", "guided_task", (index,), node, node.get("prompt"), context=(index,))
                for index, node in entries], []
    if adapter == "reading-export":
        return [unit(("multiple_select" if len(node.get("correct", [])) > 1 else "multiple_choice")
                     if node.get("type") == "choice" else {"match": "matching", "order": "sequence", "hottext": "hot_text"}.get(node.get("type"), "unknown"),
                     "question", ("items", index), node,
                     node.get("stem"), context=("items", index))
                for index, node in enumerate(document["items"])], []
    raise ValueError("unknown source adapter")


def identity(item, document):
    context = at(document, item["context_pointer"])
    # Source versions share an occurrence when their task content and lesson
    # identity match. Distinct source locations remain in occurrences[] and
    # retain their full context; no claim of equivalent difficulty follows.
    lesson = context.get("lessonId", context.get("id")) if isinstance(context, dict) else None
    return digest(encoded({"kind": item["kind"], "role": item["role"], "lesson": lesson,
                           "prompt": item["prompt"], "native": semantic(item["native"]),
                           "view": semantic(item.get("view"))}))


def validate_sources(config):
    if config.get("version") != 1 or not isinstance(config.get("sources"), list):
        raise ValueError("invalid example source configuration")
    ids = set()
    for source in config["sources"]:
        if not re.fullmatch(r"[a-z0-9-]+", source["id"]) or source["id"] in ids:
            raise ValueError("invalid or duplicate source id")
        ids.add(source["id"])
        if source.get("commit") is not None and not re.fullmatch(r"[0-9a-f]{40}", source["commit"]):
            raise ValueError("Git source needs an exact commit")
        if not re.fullmatch(r"[0-9a-f]{64}", source["sha256"]) or not source.get("as_of"):
            raise ValueError("source needs a date and byte hash")
        path = Path(source["path"])
        if path.is_absolute() or ".." in path.parts or not path.parts:
            raise ValueError("source path escapes its repository")


def source_document(source, raw):
    if source.get("encoding") == "jsonl":
        return {"items": [json.loads(line) for line in raw.decode().splitlines() if line.strip()]}
    if source.get("encoding") == "static-js":
        from example_adapters import static_three_d_document, extract_three_d_literals
        parsed = static_three_d_document(raw.decode())
        document = parsed["document"]
        document["projection"] = [{key: value for key, value in item.items() if key != "native"}
                                  for item in extract_three_d_literals(raw.decode())]
        for item in document["projection"]:
            if item["pointer"].startswith("/source_lines/"):
                item["context_status"] = "partial static fragment; runtime action target, scene and zone are not reconstructed"
        if source["path"] == "sources/act2-prototype/lesson-data.js":
            for index, node in enumerate(document.get("GUIDED", [])):
                role = "model_task" if not node.get("input") else "guided_task" if node.get("mode", "").startswith("WE DO") else "question"
                document["projection"].append({key: value for key, value in unit("soliloquy_comparison", role, ("GUIDED", index), node, node.get("prompt"), context=()).items() if key != "native"})
            for symbol, kind, role in (("STEMS", "writing_stem", "model_task"), ("CHECK", "paragraph_checklist", "subcheck")):
                for index, text in enumerate(document.get(symbol, [])):
                    document["projection"].append({key: value for key, value in unit(kind, role, (symbol, index), text, text, context=()).items() if key != "native"})
            for index, node in enumerate(document.get("EXITS", [])):
                document["projection"].append({key: value for key, value in unit("closing_task", "recall_task" if index == 0 else "question", ("EXITS", index), node, node[1], context=()).items() if key != "native"})
        document["parser_omissions"] = parsed["omissions"]
        return document
    return json.loads(raw)


def collect(cache_root):
    config = json.loads(SOURCE_CONFIG.read_text())
    validate_sources(config)
    rows, sources, documents = {}, [], {}
    for source in config["sources"]:
        cache = cache_root / source["cache_repository"] / (source["commit"] or "archive") / source["path"]
        raw = cache.read_bytes()
        if digest(raw) != source["sha256"]:
            raise ValueError("cached source byte hash differs: " + source["id"])
        document = source_document(source, raw)
        document, redacted = sanitize(document)
        items, omissions = extract(document, source["adapter"])
        context_path = "contexts/" + source["id"] + ".json"
        documents[context_path] = encoded(document)
        for item in items:
            if at(document, item["pointer"]) != item["native"]:
                raise ValueError("native source pointer mismatch")
            key = identity(item, document)
            occurrence = {"source_id": source["id"], "pointer": item["pointer"],
                          "context_pointer": item["context_pointer"], "context": context_path}
            if item.get("operation"):
                occurrence["operation"] = item["operation"]
            if item.get("exposure_status"):
                occurrence["exposure_status"] = item["exposure_status"]
            if item.get("context_status"):
                occurrence["context_status"] = item["context_status"]
            if source["adapter"] == "qti-bundle":
                occurrence["member_path"] = item["native"]["path"]
                occurrence["member_sha256"] = item["native"]["sha256"]
            if key not in rows:
                rows[key] = {"id": key, "kind": item["kind"], "role": item["role"],
                             "prompt": item["prompt"], "native": item["native"],
                             "intended_answer_status": "author material; not independently validated",
                             "quality_label": None, "occurrences": []}
                if "view" in item:
                    rows[key]["view"] = item["view"]
            # Two operations may share a native node (e.g. argument rebuttal and
            # explanation); identity also includes the exact authored prompt.
            if occurrence in rows[key]["occurrences"]:
                raise ValueError("duplicate source occurrence")
            rows[key]["occurrences"].append(occurrence)
        sources.append({**source, "context": context_path, "context_sha256": digest(documents[context_path]),
                        "occurrences": len(items), "redactions": redacted, "omissions": omissions})
    ordered = sorted(rows.values(), key=lambda row: row["id"])
    documents["questions.jsonl"] = b"".join((json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n").encode() for row in ordered)
    samples = {}
    for row in ordered:
        # These are browsing examples, selected for coverage rather than judged
        # quality. Partial runtime fragments stay in the full collection only.
        if row["prompt"] and any(not occurrence.get("context_status") for occurrence in row["occurrences"]):
            samples.setdefault(row["kind"], {"id": row["id"], "kind": row["kind"], "role": row["role"], "prompt": row["prompt"],
                                            "native": row["native"], "view": row.get("view"), "occurrences": row["occurrences"], "quality_label": None})
    documents["browse.json"] = encoded({"meaning": "One available example per source kind, for browsing; not a best-of selection or quality approval.",
                                        "examples": [samples[kind] for kind in sorted(samples)]})
    counts = {"unique_examples": len(ordered), "source_occurrences": sum(source["occurrences"] for source in sources),
              "by_kind": dict(sorted(Counter(row["kind"] for row in ordered).items())),
              "by_role": dict(sorted(Counter(row["role"] for row in ordered).items())),
              "source_snapshots": len(sources), "omissions": sum(len(source["omissions"]) for source in sources),
              "partial_context_occurrences": sum(bool(item.get("context_status")) for row in ordered for item in row["occurrences"]),
              "browsing_kinds": len(samples)}
    catalog = {"version": VERSION, "source_config_sha256": digest(SOURCE_CONFIG.read_bytes()), "counts": counts,
               "sources": sources, "files": {name: digest(raw) for name, raw in sorted(documents.items())},
               "meaning": "Authored reference activities and version variants, with keys and scaffolds as written. Guided tasks, model tasks and subchecks are not independent mastery questions. No example is an academic gold label.",
               "learner_exposure": "Source context retained; actual rendered and timed exposure is unverified.",
               "duplicates": "Same lesson identity, task content and prompt share one row; all source occurrences and contexts remain. Asset-only differences do not create a new row. Different representations are not semantically merged.",
               "not_collected": config.get("not_collected", [])}
    documents["catalog.json"] = encoded(catalog)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".authored-", dir=DESTINATION.parent))
    try:
        for name, raw in documents.items():
            output = temporary / name
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(raw)
        check(temporary)
        if DESTINATION.is_symlink():
            raise ValueError("example destination must not be a symlink")
        if DESTINATION.exists():
            shutil.rmtree(DESTINATION)
        temporary.rename(DESTINATION)
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)
    return counts


def check(directory=DESTINATION, cache_root=None):
    config = json.loads(SOURCE_CONFIG.read_text())
    validate_sources(config)
    catalog = json.loads((directory / "catalog.json").read_text())
    if catalog["version"] != VERSION or catalog["source_config_sha256"] != digest(SOURCE_CONFIG.read_bytes()):
        raise ValueError("collection source configuration changed")
    for name, expected in catalog["files"].items():
        path = Path(name)
        if path.is_absolute() or ".." in path.parts or digest((directory / path).read_bytes()) != expected:
            raise ValueError("example file hash mismatch")
    rows = [json.loads(line) for line in (directory / "questions.jsonl").read_text().splitlines()]
    if len({row["id"] for row in rows}) != len(rows):
        raise ValueError("duplicate example identities")
    observed = {}
    for row in rows:
        if row["quality_label"] is not None or row["intended_answer_status"] != "author material; not independently validated":
            raise ValueError("authored examples cannot contain quality labels")
        for occurrence in row["occurrences"]:
            observed.setdefault(occurrence["source_id"], []).append((row, occurrence))
    if not set(observed).issubset({source["id"] for source in config["sources"]}):
        raise ValueError("unknown occurrence source")
    comparisons = 0
    if len(catalog["sources"]) != len(config["sources"]):
        raise ValueError("source configuration count differs")
    for source, definition in zip(catalog["sources"], config["sources"]):
        if any(source.get(key) != value for key, value in definition.items()):
            raise ValueError("source provenance differs")
        if source.get("related_context_source") and source["related_context_source"] not in {item["id"] for item in catalog["sources"]}:
            raise ValueError("related source context missing")
        document = json.loads((directory / source["context"]).read_text())
        if cache_root is not None:
            raw = (cache_root / source["cache_repository"] / (source["commit"] or "archive") / source["path"]).read_bytes()
            original = source_document(source, raw)
            if digest(raw) != source["sha256"] or sanitize(original)[0] != document:
                raise ValueError("source comparison differs")
            comparisons += 1
        expected, omissions = extract(document, source["adapter"])
        if source["omissions"] != omissions or len(expected) != source["occurrences"]:
            raise ValueError("source extraction coverage differs")
        found = observed.get(source["id"], [])
        if len(found) != len(expected):
            raise ValueError("source occurrence count differs")
        expected_keys = Counter((identity(item, document), item["pointer"], item["context_pointer"], item.get("operation")) for item in expected)
        expected_map = {(identity(item, document), item["pointer"]): item for item in expected}
        found_keys = Counter((row["id"], item["pointer"], item["context_pointer"], item.get("operation")) for row, item in found)
        if expected_keys != found_keys:
            raise ValueError("source pointer or example identity differs")
        for row, occurrence in found:
            if identity({**row, "context_pointer": occurrence["context_pointer"]}, document) != row["id"]:
                raise ValueError("example content identity differs")
            if semantic(at(document, occurrence["pointer"])) != semantic(row["native"]):
                raise ValueError("source wording or key differs")
            if occurrence["context"] != source["context"]:
                raise ValueError("source context differs")
            matching = expected_map[(row["id"], occurrence["pointer"])]
            if occurrence.get("exposure_status") != matching.get("exposure_status"):
                raise ValueError("source exposure status differs")
            if occurrence.get("context_status") != matching.get("context_status"):
                raise ValueError("source context completeness differs")
            if row.get("view") != matching.get("view"):
                raise ValueError("normalized view differs from source")
    counts = catalog["counts"]
    if counts["unique_examples"] != len(rows) or counts["source_occurrences"] != sum(len(row["occurrences"]) for row in rows):
        raise ValueError("collection counts differ")
    if counts["by_kind"] != dict(Counter(row["kind"] for row in rows)) or counts["by_role"] != dict(Counter(row["role"] for row in rows)):
        raise ValueError("format or role counts differ")
    if counts["partial_context_occurrences"] != sum(bool(item.get("context_status")) for row in rows for item in row["occurrences"]):
        raise ValueError("partial context count differs")
    browse = json.loads((directory / "browse.json").read_text())["examples"]
    by_id = {row["id"]: row for row in rows}
    if len({row["kind"] for row in browse}) != len(browse) or len(browse) != counts["browsing_kinds"]:
        raise ValueError("browsing coverage differs")
    for sample in browse:
        original = by_id[sample["id"]]
        if any(sample[key] != original.get(key) for key in sample):
            raise ValueError("browsing example differs from collection")
        if not any(not occurrence.get("context_status") for occurrence in sample["occurrences"]):
            raise ValueError("partial fragments cannot be standalone browsing examples")
    return {**counts, "external_source_comparisons": comparisons, "quality": "unlabelled author material"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--collect", action="store_true")
    parser.add_argument("--source-cache", type=Path)
    args = parser.parse_args()
    cache = args.source_cache or ROOT / ".local" / "example-sources"
    print(json.dumps(collect(cache) if args.collect else check(cache_root=args.source_cache), indent=2))
