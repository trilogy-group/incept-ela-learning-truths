# read:inceptbench

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "inceptbench",
 "coverage": {
  "read": [
   "inceptbench-main (2.6.6, newest despite the name): AGENTS.md, CONTRIBUTING.md, README.md, docs/ (diffed against the other copies; internals/math-verifier.md, maintainers/release.md diff)",
   "inceptbench-main/src/inceptbench/prompts/: question/_base_evaluation.txt, closed_ended_evaluation.txt, ela_evaluation.txt, math_evaluation.txt, sat_rw_evaluation.txt, sat_math_evaluation.txt (diff), social_studies_evaluation.txt, match_evaluation.txt, sequence_evaluation.txt, dbq/leq/saq_evaluation.txt; article/evaluation.txt, social_studies_evaluation.txt, decomposition.txt; mcq_set and quiz evaluation (sections); fiction/nonfiction/other evaluation (outline plus scoring sections); stimulus_promise_extraction.txt",
   "inceptbench-main/src/inceptbench code docstrings and comments: evaluators/guards.py (all 14 guards), evaluators/question.py (stem-redundancy cue, detectors, wiki context), evaluators/base.py (interest relevance), evaluators/mcq_set.py, models/base.py (score bounds), config/tier_scoring.py, config/constants.py, golden/runner.py, decomposer/anchor_slicer.py, tools/factual_accuracy_audit.py, tools/stimulus_reference_detector.py, tools/variety_check.py, llm/baml_native_evaluator.py",
   "inceptbench-main/src/inceptbench/golden/golden_dataset.json (parsed for ids, labels and metadata only; compared across the three copies)",
   "inceptbench-main/tests/ (module docstrings of every issue, rule and guard test; test_evaluator_prompt_rules_962.py golden-102 history; fixtures/fake_stimulus_questions.json structure)",
   "inceptbench-main/.github/workflows/quality-gates.yml, .agents/ READMEs and skills, scripts/ docstrings",
   "inceptbench-main/website/Incept Pedagogy & Learning Science Overview.md; website/content/english/pages/ (answer-verification, reading-question-qc, ti-question-qa, text-content-evaluator, math-content-evaluator, release-notes, edubench, direct-instruction, certifications)",
   "inceptbench-latest (2.6.3): every prompt, guards.py, runner, golden set, tests and README diffed against main and the old copy; sat_rw/sat_math overlays read",
   "inceptbench (2.5.3, branch wire-ap-evaluator-context): CLAUDE.md, README.md, releases/v1.3.0.md, releases/v1.4.0.md, docs/legacy/EVALUATORS.md (beyond the used lines), docs/legacy README/USAGE/INPUT_OUTPUT/MAINTAINERS (scanned), plans/01 and 02, scripts/AUTOMATIC_REGENERATION_SUMMARY.txt, scripts/REEVALUATION_GUIDE.md (scanned), scores/summary.txt and */results.txt, old src/inceptbench/prompts and inceptbench_new/prompts (diffed), src/inceptbench/agents/localization_guidelines.json, localization_evaluator.py, simple_content_qc.py (system prompt), content_evaluator.py (header), evaluators/base.py AP context block, submodules/EduBench/README.md, submodules/reading-question-qc/qc_pipeline/README.md and config/prompts.json, packages/incept-eval/README.md (outline)",
   "inceptbench git history: all 144 commit messages read; deleted docs/EVALUATOR_VARIANCE_FIX.md (591 lines) recovered with git show e5be84f^"
  ],
  "skipped": [
   "src/inceptbench/curricula/**/*.md in all copies (0.08-16 MB standards dumps: data, not findings)",
   ".env and .env.bak.e1 files (credentials; never opened)",
   "venv/, logs/, node_modules, baml_client/ (generated code), api_router, deploy/publishing/cloud-run docs (operational)",
   "website themes/layouts HTML, blog posts and author pages (placeholders), benchmarks/*.md (1-byte files)",
   "scores/*/sets/* raw/converted/scores data, submodules/EduBench data, code, README_zh.md (duplicate) and distribution-radar.pdf (figure)",
   "Already-used docs (AP_EVALUATION.md = internals/ap-evaluation.md, MATH_VERIFIER.md, user_guides/api.md, examples.md): only diffed across copies, not mined again",
   "agents/edubench_evaluator.py (163 KB legacy code) and object_counter.py beyond a grep",
   "Git objects missing from the iCloud copy (e.g. tree of commit 715eadc): its message was read, its diff could not be"
  ],
  "notes": "Folder names mislead: inceptbench-main is the newest (2.6.6, single commit, 1 Jun 2026), inceptbench-latest is 2.6.3 (single commit, 22 May 2026), and inceptbench is 2.5.3 on unmerged branch wire-ap-evaluator-context (29 Apr 2026) and is the only copy with history. What changed: 2.5.3 to 2.6.3 moved subject rules out of the domain-general base into overlays (ELA, math, SAT, social studies); added the zero-knowledge leak probe, the override clause and eight must-fail copy-task audits (SIG-1 to SIG-8); added guards.py (deterministic overrides of judge rationalizations); replaced keyword stimulus checks with model-extracted 'promises' verified in code; replaced verbatim decomposition with anchor slicing; grew the gold set to 106 (adds 101-108, drops 038 and 046) and counted errored items as misses. 2.6.3 to 2.6.6 added schema/format agnosticism (renderer and JSON-shape rules removed, SPR format guard disabled), SIG-9 and SIG-10, the missing-word ban, instance-to-category and phenomenon-diagram carve-outs, the DBQ topic-match rule, SAT inference-verifiability, vocabulary-in-context and synthesis rules, 14 guards, and a gold set of 104 (drops 007, 055, 071, 073, 074, 097; adds 109-112; relabels 102 INFERIOR to ACCEPTABLE). The AP work in the oldest copy (unified curriculum record carrying assessment boundaries, misconceptions, expanded objectives and textbook-cited evidence atoms; course IDs rebased by content match) is absent from both later copies. The deterministic overall-score table from the variance fix was reverted (commit 9f8acd5) to clamping the model's number within bands, and the base-versus-overlay contradiction on missing difficulty definitions still exists in 2.6.6. Uncertainty policies conflict across judges (question judge: pass; localization: fail; sequence: middle score; skipped audit: cap below top) - relevant to truth 9. Gold pass thresholds disagree (0.95 in the dataset file, 0.98 runner default, 0.99 in CI). Commit-message citations give the repo .git path plus commit hash and message line numbers."
 },
 "candidates": [
  {
   "statement": "A question meant to test subject knowledge fails if a reader with none of that knowledge can reach the answer from the given material alone - by paraphrase, by reading a label or arrow, or by everyday inference - even when the answer word itself never appears.",
   "kind": "adopted rule",
   "found_by": "Disagreement reports (issues 972, 976, 977) showed the judge passing items whose stimulus already stated the answer, and excusing one because a technical word was missing from the passage; a zero-knowledge role-play probe and a ban on that 'missing-word' defense were added between 2.5.3 and 2.6.6.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt",
     "lines": "125",
     "quote": "Discriminator: after fully absorbing the stimulus, is grade-level `{request.subject}` reasoning **still required** to pick the answer? If the cognitive demand collapses to \"look and report\" or \"match restated description to its conventional name\", it is a leak. → `educational_accuracy`"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt",
     "lines": "110",
     "quote": "It is an evaluation error to claim an item is NOT a mechanism-naming leak simply because the literal answer word does not appear in the stimulus."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_evaluator_prompt_rules_976.py",
     "lines": "4-6",
     "quote": "Root cause: evaluator performed the zero-knowledge counterfactual probe but rationalized past a connect-the-paragraphs leak by claiming a missing technical word (\"pipes\") in the stimulus meant subject knowledge was still required."
    }
   ],
   "against": "The probe is skipped for reading/ELA items (_base_evaluation.txt L102) and must pass premise visualizations and data-interpretation tasks (L120: \"the targeted skill IS reading / interpreting / measuring the stimulus\"); it over-fired on instance-to-category classification (test_evaluator_prompt_rules_972.py L4-10) and on phenomenon diagrams (test_evaluator_prompt_rules_977.py L4-6).",
   "adds_to_existing": [
    5,
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge an item by the operation a student must actually perform to answer it, not by the verb in its stem or the name of the skill it claims to test.",
   "kind": "adopted rule",
   "found_by": "Items whose 'evaluate/explain/justify' stems reduced to text matching, and items that described a skill instead of exercising it (synonym questions labelled as meaning-in-context), were passing.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt",
     "lines": "114",
     "quote": "Verbs like *evaluate / claim / analyze / explain / justify* in the question stem do **not** rescue the item — they describe the cover, not the actual cognitive demand."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt",
     "lines": "80-81",
     "quote": "Items must exercise the targeted SAT R&W substandard, not describe the substandard in the abstract."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_evaluator_prompt_rules_969.py",
     "lines": "5-7",
     "quote": "Items that use a foundational everyday word and a direct synonym answer test synonym recognition rather than determining meaning in context, and should fail `curriculum_alignment`."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Wording that adds reading load without adding demand is a flaw: stacked analysis instructions, topics from the standard padded into the stem, and clauses that give no path to the answer.",
   "kind": "adopted rule",
   "found_by": "Generated stems padded with unrelated topics from the standard (issue 482) and 'First X. Then, based on X, Y.' stems with adult-register passages passed at 0.95 ACCEPTABLE (issues 411-415).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt",
     "lines": "152",
     "quote": "This commonly occurs when generation tries to \"cover\" as much of the standard as possible by inserting unrelated topics into the stem."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_evaluator_prompt_rules_411_418.py",
     "lines": "9-11",
     "quote": "G6 ELA items with \"First X. Then, based on X, Y.\" stems and adult-register passages were passing evaluation at 0.95 ACCEPTABLE despite real grade-band problems."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "96",
     "quote": "Being in the same broad curriculum standard does not make a clause connected — the clause must provide information *necessary* to answering this specific question."
    }
   ],
   "against": "_base_evaluation.txt L151: \"Do NOT flag for legitimate multi-step prompts where each step actually drives a different decision.\" L156 exempts first steps that identify a closed grammatical category.",
   "adds_to_existing": [
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every wrong option must survive elimination by a student who lacks the tested knowledge: no simple negations of what the stem asks for, no options off the stem's topic, and no combination options.",
   "kind": "adopted rule",
   "found_by": "Items whose distractors were plain opposites passed the distractor metrics (issue 460); off-topic distractors made a 'hard' item trivial (issue 981); a combination-option rule was added for multi-select items (commit c8c082c).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_evaluator_prompt_rules_460.py",
     "lines": "3-5",
     "quote": "The distractor_quality and reveals_misconceptions metrics were passing items whose incorrect options were simply the logical negation/opposite of the correct answers (e.g., \"good land\" vs \"poor land\", \"near people\" vs \"no people\")."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "601",
     "quote": "Students can eliminate them by topical mismatch alone without subject knowledge."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit c8c082c message)",
     "lines": "9",
     "quote": "- Add MSQ combination-option rule: \\\"Both A and B\\\" style options → distractor_quality=0.0"
    }
   ],
   "against": "The deterministic negation guard fires only when ALL correct answers align with the stem's direction and ALL distractors oppose it (guards.py L962-974).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "The key must not stand out by form: it should not be the only option that repeats a distinctive word, name or number from the stem or its category label, and it should not differ from the others in length, grammar or tone.",
   "kind": "adopted rule",
   "found_by": "Keys were telegraphed by being the only option repeating the stem's region name (a deterministic guard and audit SIG-10 were added in 2.6.6); matching items echoed their own category labels and sorted by syntax.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/social_studies_evaluation.txt",
     "lines": "16",
     "quote": "When the stem names a region and the correct answer is the only option that also names that region, students can identify the correct answer by simple keyword matching rather than subject knowledge."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/match_evaluation.txt",
     "lines": "411",
     "quote": "- **Syntactic giveaway pattern**: Items in the same category share a distinctive grammatical structure that items in other categories do not — allowing a student to sort by syntax alone."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt",
     "lines": "73-75",
     "quote": "A student should not be able to identify the key from the task line alone. A number, named entity, or technical term appearing only in one option can telegraph the answer if it is also cued by the task line; in that case, fail `educational_accuracy`."
    }
   ],
   "against": "sat_rw_evaluation.txt L75-76: \"Ordinary topic-word overlap is acceptable.\"; match_evaluation.txt L379 treats a single label echo as borderline (\"keep 1.0 unless it is the dominant word in the label\").",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make wrong options diagnostic: at least one should match a known misconception while the key matches none, and when a skill has several named parts, different options should miss different parts.",
   "kind": "adopted rule",
   "found_by": "Published misconceptions in the curriculum data never reached the judge until the unified record was wired in; a 'monotonous failure modes' rule was added (issue 372) and then scoped because it over-fired on single-skill items in the gold suite.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/src/inceptbench/evaluators/base.py",
     "lines": "600",
     "quote": "A high-quality MCQ should have at least one distractor that targets one of these misconceptions, and the correct answer must NOT match any of them."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "600",
     "quote": "In that narrow case, if every distractor violates the same sub-criterion the question loses diagnostic value → `distractor_quality = 0.0`."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_evaluator_prompt_rules_371_382.py",
     "lines": "25-26",
     "quote": "does not over-fire on single-skill items (avoids golden-suite regression)."
    }
   ],
   "against": "The misconception guidance exists only on the unmerged branch in the oldest copy and is absent from 2.6.3 and 2.6.6; closed_ended_evaluation.txt L600 says that for single-skill standards, distractors sharing a failure category are \"NORMAL good design, not a flaw.\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When a stem asks for two steps but the options answer only the last one, the options give the first step away.",
   "kind": "adopted rule",
   "found_by": "Issue 382 (partial-question giveaway) added to the closed-ended rubric and pinned by a prompt-rule test.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "603",
     "quote": "If the stem asks the student to do two things (e.g., \"First identify the sentence with the error, then choose the correction\"), but the answer options only correspond to ONE of the source items, the identification step is given away by the option set."
    }
   ],
   "against": "_base_evaluation.txt L156: do not fire \"when the answer options' text references the first step's output\" because the student commits to both steps in one choice.",
   "adds_to_existing": [
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before reading the key of an open-response item, list what students at that level might reasonably answer; if two or more correct answers are missing from the accepted set, the item has no single answer.",
   "kind": "adopted rule",
   "found_by": "Over-broad fill-in blanks were being excused because the keyed answer was the exact curriculum term; a mechanical blind-completion check was added and pinned by a regression test.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "442",
     "quote": "1. Read the stem WITHOUT looking at the accepted-answer list."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "445",
     "quote": "4. If TWO OR MORE of your completions are factually correct, grammatically fit, AND are NOT in the accepted-answer set, this is a **concrete, unambiguous violation**: the question does not have a single correct answer."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "449",
     "quote": "Example of violation (topic-agnostic): Stem: \"A person who writes books is called a _____.\" Accepted answers: only \"author\". A student could also correctly answer \"writer\" because the stem's description fits that just as well."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    6,
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check a fill-in item by putting the key into the blank and reading the whole sentence for grammar and sense.",
   "kind": "adopted rule",
   "found_by": "Keys that produced double determiners (e.g. 'a(n) an adverb') passed until a deterministic guard was added in 2.6.x.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "248",
     "quote": "For fill-in-the-blank: mentally insert the correct answer into the blank and read the COMPLETE resulting sentence aloud."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/evaluators/guards.py",
     "lines": "282-283",
     "quote": "Detect ungrammatical double-determiner patterns in ELA fill-in-the-blank questions (e.g. ``a(n) an adverb``) and override factual_accuracy."
    }
   ],
   "against": "closed_ended_evaluation.txt L250: the shorthand \"a(n) _____\" is not an error (\"\"a(n) adverb\" should resolve to \"an adverb\"\").",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "In a comparison item, the keyed explanation must name a cause that differs between the things compared; a cause that applied to both explains nothing about the difference.",
   "kind": "adopted rule",
   "found_by": "One of eight copy-task audits (SIG-5) added for issue 962 from flagged items.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "116",
     "quote": "If the correct answer's causal explanation applies equally to both subjects, it explains the general direction of change for all subjects — not the specific comparative difference."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When the skill is working with a medium itself (reading a map or graph, listening), the item must present that medium; when the skill is reasoning about content, a text version is acceptable - ask whether the missing medium makes the item unanswerable or only less authentic.",
   "kind": "adopted rule",
   "found_by": "Items swapped a standard's named medium for another (SIG-6, issue 962) while other items were failed for lacking media their skill did not need; a medium-perception pre-check was added.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "134",
     "quote": "A structurally different medium (e.g., a data table) trains a different cognitive operation even when it conveys the same information."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "403",
     "quote": "The distinction: does the absence of the actual medium make the question *unanswerable*, or merely *less authentic*? If the student can fully exercise the target skill using the text provided, the format is acceptable."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    64
   ],
   "name_bearing_source": false
  },
  {
   "statement": "An item may only require knowledge the targeted standard teaches; any further fact or principle needed to answer must be given in the item.",
   "kind": "adopted rule",
   "found_by": "Audits SIG-3 and SIG-9 were added after items required facts or tool mechanics outside the standard; essay rubrics fail prompts whose rubric needs evidence the course does not provide.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "76",
     "quote": "That fact must be provided in the stem; students should not be required to supply it from outside knowledge."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "190",
     "quote": "Testing the physics of the tool rather than its application is outside the standard's scope."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/leq_evaluation.txt",
     "lines": "22",
     "quote": "- Score 0.0: Rubric is unachievable (e.g., requires evidence that doesn't exist in the curriculum)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    20
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Alignment holds only if the answer choices make claims about the standard's named target and its specific focus; sharing a broad topic, period or type of evidence is not enough.",
   "kind": "adopted rule",
   "found_by": "Issue 1004: content on other sub-topics scored curriculum_alignment 1.0 because the rubric failed only 'completely different subject/topic'; issue 984: well-made documents on the wrong topic passed; SIG-2 targets the 'inference-chain' rationalization.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_evaluator_prompt_rules_1004.py",
     "lines": "8-10",
     "quote": "Root cause: the DBQ evaluation prompt used \"completely different subject/topic\" as the failure threshold, allowing the evaluator to rationalize that gender roles vs religion/labor were \"same general subject domain\" and therefore pass."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "53",
     "quote": "The distinction that matters: the answer options must make claims **about the standard's named target**, not about a *different* subject that can be *inferred using* the same evidence. The evidence type and the cognitive target are not the same thing."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/dbq_evaluation.txt",
     "lines": "29",
     "quote": "A DBQ whose prompt and documents address a DIFFERENT specific analytical focus or sub-topic than what the standard explicitly requires, even within the same broad historical period or unit."
    }
   ],
   "against": "The general question rule stays lenient: _base_evaluation.txt L163 \"PASS if: the question exercises the standard's named skill, OR any prerequisite/component/application within the same subject domain and grade-level topic.\"",
   "adds_to_existing": [
    58,
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A judge told to pass whenever reasonable evaluators could disagree talks itself past real faults; known fault patterns need narrow checks that fail by default and override that stance.",
   "kind": "adopted rule",
   "found_by": "Leaks and misalignments rationalized under the default-pass stance led to the override clause and must-fail audits (2.6.3); separately, making borderline difficulty and distractor calls pass by default dropped the gold-set pass rate to 94%, below the 98% bar, and was reverted.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt",
     "lines": "5",
     "quote": "If reasonable evaluators could disagree, the metric passes."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "10",
     "quote": "These audits override the base-prompt default-PASS stance; the \"reasonable evaluators could disagree\" carve-out does NOT apply."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 2750903 message)",
     "lines": "3-7",
     "quote": "Per golden dataset regression test (94% pass rate, below 98% threshold): - difficulty_alignment: restore 'use general definitions + judgment' when no curriculum definitions available (revert pass-by-default added in PR #268) - distractor_quality: remove 'borderline default to 1.0' paragraph (revert PR #268 change that made evaluator too lenient on ambiguous distractor flaws)"
    }
   ],
   "against": "Default-pass remains the rule elsewhere: closed_ended_evaluation.txt L687 \"When uncertain, default to PASS\"; article/evaluation.txt L881 chooses 1.0 when two runs could disagree.",
   "adds_to_existing": [
    32,
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write each targeted check as a copy task: the judge copies the exact text the rule applies to into named fields and then answers yes or no, so the verdict follows from what was copied, and a missing audit counts as a failure.",
   "kind": "adopted rule",
   "found_by": "Free-form judgments kept rationalizing past the same defects, so eight copy-task audits (issue 962) and standard-triggered ELA audits were added.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "12",
     "quote": "Each audit is a **copy task** — fill the fields by copying exact text from the question content. The failure condition then follows from what you copied, with no room for reinterpretation."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/ela_evaluation.txt",
     "lines": "5",
     "quote": "Skipping the audit is itself a failure of the metric: if the audit is missing, score that metric `0.0`. The audit must use real values from the content, not boilerplate."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/match_evaluation.txt",
     "lines": "395",
     "quote": "You MUST produce the per-category pattern table above before assigning a score. Claiming \"no patterns found\" without the table is not acceptable."
    }
   ],
   "against": "Audits did not stabilise every case: a planted must-fail gold item still 'may vary between INFERIOR and ACCEPTABLE/SUPERIOR across runs' (test_evaluator_prompt_rules_962.py L216-217).",
   "adds_to_existing": [
    31,
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a judge excuses a known fault, write its excuses into the rubric as invalid and require any override to quote the narrow exception it relies on.",
   "kind": "measured",
   "found_by": "On two flagged real-world items a soft cue gave inconsistent verdicts on identical defects; after listing the disallowed rationalizations and requiring quoted overrides, re-runs flagged both.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 0a22a5b message)",
     "lines": "5-7",
     "quote": "The LLM rationalized one case as \"common formatting style\" and on a second run cropped the stem to its first sentence and claimed the options weren't present, when in fact the full A/B/C/D answer list was inline."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 0a22a5b message)",
     "lines": "17-18",
     "quote": "- Require any override to cite which narrow false-positive case applies and quote the supporting stem text."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "599",
     "quote": "A distractor that satisfies the question's stated requirements just as well as the keyed answer is a fail, not a \"less effective\" alternative → `distractor_quality = 0.0`."
    }
   ],
   "against": "Measured on two items only.",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Scan a judge's written reasoning in code for faults it admits and then excuses with a reason the rubric does not allow, and overturn those passes.",
   "kind": "adopted rule",
   "found_by": "Judges wrote 'quite implausible' or 'factual error' yet scored 1.0, or admitted a sub-topic mismatch but passed it as 'same general subject domain' (issue 1004); four rationalization guards were added by 2.6.6.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/evaluators/guards.py",
     "lines": "489-491",
     "quote": "The evaluator may internally admit a distractor is implausible (\"quite implausible\", \"somewhat silly\") but invent a non-rubric excuse to score 1.0 anyway."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_evaluator_prompt_rules_1004.py",
     "lines": "13-15",
     "quote": "added a deterministic guard to catch evaluator self-rationalization when it admits a sub-topic mismatch but dismisses it as \"same general subject domain\""
    }
   ],
   "against": "guards.py L671-674: \"Admission keywords are kept narrow on purpose: broader cues like \"causal\" or \"mechanism\" trigger far too often on factually-correct explanations that merely mention causation, so the guard requires an explicit admission phrase.\"",
   "adds_to_existing": [
    67,
    39
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Tell the judge explicitly when part of the material could not be delivered, such as a picture that failed to load, and forbid it from describing or citing anything it was not given.",
   "kind": "adopted rule",
   "found_by": "Issue 339: the judge graded pictures that had failed to download (fix verified at 99/100 on the gold set); judges also claimed programmatic findings that did not exist.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 4e52d17 message)",
     "lines": "1-3",
     "quote": "fix(article-eval): prevent stimulus_quality hallucination when images fail to download (#339) Fixes #339. Merging into fix/article-eval-quality-2026-04-24. Golden dataset: 99/100 (99.0%)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/article/evaluation.txt",
     "lines": "644",
     "quote": "> - NOT describe specific visual details you have not actually seen"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt",
     "lines": "135",
     "quote": "If you have not been given a deterministic finding in the input, you must not claim one exists."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    30
   ],
   "name_bearing_source": false
  },
  {
   "statement": "If the curriculum data or content split a judge depends on cannot be obtained, fail the evaluation loudly; silent fallbacks produced verdicts with no curriculum context and no sign that anything was wrong.",
   "kind": "adopted rule",
   "found_by": "Every curriculum error path returned empty context silently (commit 101e555); failed decomposition silently flattened content into a single prompt (issue 192).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 101e555 message)",
     "lines": "8-9",
     "quote": "The result: evaluations ran without curriculum context with no signal that anything was wrong."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_decomposition_loud_failure.py",
     "lines": "1-2",
     "quote": "Tests that decomposition failures propagate loudly instead of silently flattening content into a single evaluation prompt."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_curriculum_loud_failures.py",
     "lines": "1-2",
     "quote": "Tests that curriculum API errors propagate loudly through the evaluator pipeline instead of being silently swallowed into an empty context."
    }
   ],
   "against": "The AP path stays fail-closed and returns empty context on a course mismatch (commit 082d3a3 line 35: \"Course mismatch still returns \"\" with COURSE_MISMATCH_FAIL_CLOSED log.\"); the fact audit fails open when no reference passages are found (commit 8aedb57 line 22: \"Fail-open: if no Wikipedia passages retrieved, skip audit (score=1.0)\").",
   "adds_to_existing": [
    36,
    33
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a check cannot run, the item must not keep a perfect rating: fall back to a simpler check rather than to a pass, and cap and annotate the result.",
   "kind": "adopted rule",
   "found_by": "GH 858: a skipped fact audit silently preserved perfect scores; an outage of the model-based stimulus check would have let 'Look at the chart' with no chart pass.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_factual_audit_skipped_scoring.py",
     "lines": "44",
     "quote": "Auditor error skip on a perfect item must downgrade overall to ACCEPTABLE."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_stimulus_llm_failure_fallback.py",
     "lines": "4-8",
     "quote": "When `_extract_stimulus_promises_llm` exhausts its retries and returns None, the detector must still flag a mismatch if the regex fast-path saw a real visual reference and no actual stimulus is present. Otherwise an LLM outage silently disables the entire mismatch detector and \"Look at the chart\" with no chart attached gets a free pass."
    }
   ],
   "against": "test_factual_audit_skipped_scoring.py L75: \"Legitimate data-unavailable skip preserves score but adds a caveat.\"",
   "adds_to_existing": [
    36,
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "State every scoring rule once and keep rubric layers and scoring code in agreement; contradictions between them showed up as run-to-run flips and as a rating band that no rule defined.",
   "kind": "measured",
   "found_by": "Two runs on the same 690 items disagreed on 38 ratings (5.5%); 9 of the 27 metric flips came from one base-versus-overlay contradiction on missing difficulty definitions, and a prompt/code mismatch left a band decided only by the model's free number.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/EVALUATOR_VARIANCE_FIX.md (deleted in commit e5be84f; read with git show e5be84f^:docs/EVALUATOR_VARIANCE_FIX.md)",
     "lines": "29",
     "quote": "| `difficulty_alignment` | 9 | Base prompt and overlay prompt **contradicted each other** on what to do when no difficulty definitions exist |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/EVALUATOR_VARIANCE_FIX.md (deleted in commit e5be84f; read with git show e5be84f^:docs/EVALUATOR_VARIANCE_FIX.md)",
     "lines": "40",
     "quote": "This meant ACCEPTABLE only existed when ALL metrics pass but the LLM gave less than 0.99 — a pure \"vibes-based\" category with no definition. 78/690 questions (11%) landed there randomly."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit d9d4441 message)",
     "lines": "10-12",
     "quote": "- Make the \"Unnatural interjections in the stem\" rule body byte-identical across _base_evaluation.txt and closed_ended_evaluation.txt to prevent drift between the two concatenated prompts."
    }
   ],
   "against": "The contradiction survives in 2.6.6: _base_evaluation.txt L170 \"If no definitions provided: `difficulty_alignment = 1.0`\" versus closed_ended_evaluation.txt L547 \"Use the general definitions above (Easy/Medium/Hard) as your baseline\", because the aligning fix was reverted (commit 2750903).",
   "adds_to_existing": [
    34,
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Independent fact checkers catch largely different errors, so let either one fail an item rather than trusting a single checker.",
   "kind": "measured",
   "found_by": "Comparing the main judge with a separately prompted fact audit on the same item set: 16 confirmed errors only the audit caught, 6 only the main judge caught, zero overlap; the audit was then merged as min(main, audit).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/EVALUATOR_VARIANCE_FIX.md (deleted in commit e5be84f; read with git show e5be84f^:docs/EVALUATOR_VARIANCE_FIX.md)",
     "lines": "407-409",
     "quote": "- GPT audit caught **16 confirmed factual errors** that Gemini completely missed - Gemini caught **6 different factual errors** that the GPT audit missed - **Zero overlap** — the two models detect entirely different kinds of errors"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/tools/factual_accuracy_audit.py",
     "lines": "13-15",
     "quote": "The audit result is **merged** into the main evaluator's ``factual_accuracy`` score via ``min(main, audit)`` — if either the main evaluator or the audit catches a factual error, the question fails."
    }
   ],
   "against": "EVALUATOR_VARIANCE_FIX.md L402: \"The audit added additional variance on top of Gemini's baseline 5.5%.\" The audit runs only for social studies in code (config/constants.py L22-26).",
   "adds_to_existing": [
    65
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Pasting reference passages into a general judge's prompt made it worse at catching factual errors and less consistent; keep reference text for a narrow fact check.",
   "kind": "measured",
   "found_by": "Experiment: the reference-grounded main judge caught 3 of 22 factual errors versus 6 of 22 without, and rating flips rose from 5.5% to 7.0%; in 2.6.6 reference injection into the main judge is opt-in only.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/EVALUATOR_VARIANCE_FIX.md (deleted in commit e5be84f; read with git show e5be84f^:docs/EVALUATOR_VARIANCE_FIX.md)",
     "lines": "422",
     "quote": "**Finding**: **Wikipedia-grounded Gemini performed WORSE** — caught only 3/22 factual errors (down from 6/22 baseline) and increased variance to 7.0% (up from 5.5%). Gemini apparently got confused by the additional context rather than using it for cross-referencing."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/evaluators/question.py",
     "lines": "1079",
     "quote": "use_wiki = os.environ.get(\"EVALUATOR_USE_WIKIPEDIA\", \"\").strip().lower() in ("
    }
   ],
   "against": "The unmerged AP branch adds up to 30 textbook-cited facts per standard to every judge prompt with no measured comparison (inceptbench/src/inceptbench/evaluators/base.py L617-631).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A judge must not fail a fact because it cannot recall it; fail only when it can state the error and a well-documented correction, and a student would come away believing something substantively wrong.",
   "kind": "adopted rule",
   "found_by": "Fact-metric flips (8 of 27 run-to-run metric flips) and false failures on real documents and simplified attributions led to a three-gate correction test.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/tools/factual_accuracy_audit.py",
     "lines": "125",
     "quote": "Absence of recall is not absence of fact."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/tools/factual_accuracy_audit.py",
     "lines": "147-148",
     "quote": "If you cannot clearly articulate what wrong belief the student would form, the error fails Gate 3 and you must score 1.0."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/EVALUATOR_VARIANCE_FIX.md (deleted in commit e5be84f; read with git show e5be84f^:docs/EVALUATOR_VARIANCE_FIX.md)",
     "lines": "108",
     "quote": "The audit used a rigorous 3-gate system that reduced false positives. The main evaluator would sometimes flag borderline factual issues that the audit would correctly pass."
    }
   ],
   "against": "sat_rw_evaluation.txt L19-21 still requires failing invented studies, fake quotations and named people presented as real, which a judge can only spot from its own knowledge.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Treat every claim an item's explanation makes about the item (that a statement is in the text, that an option is right) as something to verify against the item itself; judges otherwise accept the explanation's description of itself.",
   "kind": "adopted rule",
   "found_by": "Issue 967: an explanation wrongly called a distractor 'a fact stated explicitly in the text' and the judge accepted it, scoring factual accuracy 1.0.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_evaluator_prompt_rules_967.py",
     "lines": "10",
     "quote": "The evaluator accepted the explanation's self-characterization without checking."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt",
     "lines": "34-36",
     "quote": "**Rule:** When an explanation claims a distractor is \"a fact stated explicitly in the text\" or \"explicitly stated,\" you MUST verify whether the *specific claim made in that distractor* is literally present in the stimulus."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/ela_evaluation.txt",
     "lines": "83",
     "quote": "Do NOT use `answer_explanation` as your sole source of truth — the explanation may be absent, wrong, or misleading."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    43,
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Explanations, hints and feedback must refer to the options, values and key actually in the item; any mismatch is an accuracy failure.",
   "kind": "adopted rule",
   "found_by": "Generated support text discussed values that were not among the item's options.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "260-261",
     "quote": "- **FIELD MISMATCH**: Explanations, hints, feedback templates, or `additional_details` describe distractors, answers, or values that do NOT match the actual options or correct answer - Example: `additional_details` discusses choosing between \"7 riyals\" and \"14 riyals\" but actual options are 28, 70, 30, 35"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "271",
     "quote": "**CRITICAL - Supporting Text Fields**: You MUST treat explanations, hints, feedback templates, and diagnostic notes (`additional_details` fields) as part of the content."
    }
   ],
   "against": "closed_ended_evaluation.txt L272: when code verification says the answer is correct, the mismatch counts under clarity, not accuracy.",
   "adds_to_existing": [
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge only what changes the student's experience; never fail an item for how its data is stored (field names, nesting, lists versus strings).",
   "kind": "adopted rule",
   "found_by": "The judge misread a valid list of equivalent answers as several blanks (issue 390) and failed items for unfamiliar shapes; 2.6.6 added a schema-agnosticism rule and disabled a renderer-format guard.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt",
     "lines": "20",
     "quote": "If the same question, asked of a student, would have the same pedagogical experience regardless of how the JSON is structured, the schema is irrelevant."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_issue_390_fillin_accepted_answers.py",
     "lines": "3-6",
     "quote": "The evaluator incorrectly flags FILL_IN questions where accepted_answers contains multiple single-element lists (e.g. [[\"3\"], [\"3/1\"], [\"6/2\"]]) as having multiple blanks, when in fact this is the valid platform format for multiple equivalent answers to a single blank (list[answer_set][blank_index])."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/evaluators/guards.py",
     "lines": "1919-1921",
     "quote": "Renderer / UI schema compliance is a platform concern, not a question-quality concern, so InceptBench no longer scores on it"
    }
   ],
   "against": "2.6.3 still failed items on field placement (inceptbench-latest sat_rw_evaluation.txt L27: \"The `question` field must contain only the student-facing task line, not the passage.\"); options duplicated in the stem are still penalised because students see them twice (question.py L700-701).",
   "adds_to_existing": [
    30,
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a model splits material into parts, have it mark where each part starts and ends and cut the original in code; asked to copy the parts, it paraphrased pictures, tables and diagrams into words.",
   "kind": "adopted rule",
   "found_by": "The decomposer turned images, inline SVG and tables into text descriptions, so the downstream judge found no stimulus and failed items that had one; anchor slicing replaced verbatim copying between 2.5.3 and 2.6.3.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/decomposer/anchor_slicer.py",
     "lines": "6-9",
     "quote": "When the decomposer LLM is asked to \"extract verbatim text\" of a child node, it routinely paraphrases rich stimuli — `<img src=\"...\">` becomes \"[Image: ...]\", `<svg>` blocks become text descriptions, `<table>` becomes a bulleted list."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/decomposer/anchor_slicer.py",
     "lines": "9-11",
     "quote": "The downstream evaluator then runs a programmatic stimulus check on the paraphrased text, finds no real image, and scores `stimulus_quality = 0.0` even though the source had the image inline."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/decomposer/anchor_slicer.py",
     "lines": "15-16",
     "quote": "The decomposer LLM returns short verbatim `start_anchor` / `end_anchor` substrings instead. This module slices the ORIGINAL source buffer between"
    }
   ],
   "against": "anchor_slicer.py L27-28: \"Failure is non-fatal: if anchors don't match, the caller falls back to the LLM's free-text `extracted_content`.\"",
   "adds_to_existing": [
    17,
    30
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Run each automatic check only on the item types it was built for; checks built for one type produced systematic false failures on others.",
   "kind": "adopted rule",
   "found_by": "A fact audit misread ordering positions as date inversions on sequencing items; option-only audits failed numeric free-response items; a guard for document-based essays fired on all question types and destabilised a gold item.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 20bb29e message)",
     "lines": "5-7",
     "quote": "The independent factual audit produces systematic false positives (misreads position indices as date inversions)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/evaluators/guards.py",
     "lines": "2300-2302",
     "quote": "SPR has no answer options, so those audits can mis-fire and force false failures on `curriculum_alignment`, `educational_accuracy`, or"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_evaluator_prompt_rules_962.py",
     "lines": "213-215",
     "quote": "History: previously expected INFERIOR, but consensus variance and the original DBQ curriculum-alignment guard firing on all question types caused intermittent passes."
    }
   ],
   "against": "The variance work later removed the sequence skip from the fact audit and gave it sequence-specific guidance instead (EVALUATOR_VARIANCE_FIX.md L339-341).",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Checks triggered by word lists fire on ordinary uses of those words; require the directive phrasing and filter out narrative or negated uses.",
   "kind": "adopted rule",
   "found_by": "Items containing 'model' or 'figure' were forced to fail stimulus checks; 'figure-eight' collided with 'figure'; narrative 'is looking at a map' was read as an instruction; broad cue words fired on correct explanations.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 20bb29e message)",
     "lines": "10-12",
     "quote": "Sequence questions have no visual stimuli — the mismatch check injected \"MUST score stimulus_quality = 0.0\" for items containing words like \"model\" or \"figure\", overriding correct sequence scores."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/evaluators/question.py",
     "lines": "793-794",
     "quote": "Bare \"figure\" / \"figures\" are intentionally excluded because they collide with content phrases like \"figure-eight\" (#371 bee dance)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/tools/stimulus_reference_detector.py",
     "lines": "940-943",
     "quote": "Narrative/descriptive \"is looking at\" is NOT a directive to the student. Phrases like \"A family is looking at a map\" describe a scenario; they do not instruct the student to consult a visual artifact."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Change a labelled reference case only after checking the item itself, never to make it agree with the judge.",
   "kind": "measured",
   "found_by": "A deliberately wrong-keyed gold item was relabelled top quality because a new judge passed it (bringing the set to 100/100), then relabelled back four days later; another planted must-fail item was later pinned to pass because the judge's verdict on it varied between runs.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 715eadc message)",
     "lines": "4",
     "quote": "- golden-001 (math g3 mcq easy): INFERIOR → SUPERIOR (BAML correctly rates it; no failing metrics)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 3a88a35 message)",
     "lines": "3-7",
     "quote": "golden-001 (grade 3 MCQ on parallel sides) has a labeled answer of B=1 with the explanation \"A triangle has one pair of parallel sides: the bottom side is parallel to itself.\" A triangle has zero pairs of parallel sides, and no standard geometry treats a side as parallel to itself — the correct answer is A=0."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_evaluator_prompt_rules_962.py",
     "lines": "216-218",
     "quote": "item's evaluator score sits on the pass/fail boundary and may vary between INFERIOR and ACCEPTABLE/SUPERIOR across runs. It is pinned to ACCEPTABLE to reflect its typical post-fix behaviour while acknowledging inherent instability."
    }
   ],
   "against": "Relabelling is right when the item was checked: commit 3a88a35 lines 12-14 \"Relabel the expected verdict so the golden suite reflects the actual quality of the item rather than the curator's mistake.\"",
   "adds_to_existing": [
    39,
    37,
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Pin every rule added after a judging failure with a deterministic test that breaks if the rule's text is removed or moved, plus a labelled regression case that exercises it.",
   "kind": "adopted rule",
   "found_by": "Disagreement-report issues (371 to 1004) each got a prompt-string test and several got a gold item; CI runs the gold regression on every pull request.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_evaluator_prompt_rules_371_382.py",
     "lines": "3-5",
     "quote": "The tests check that the relevant guidance string is present in the right prompt file so that edits removing or relocating it are caught deterministically (no LLM)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_evaluator_prompt_rules_1004.py",
     "lines": "15-16",
     "quote": "added golden-112 regression entry."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/.github/workflows/quality-gates.yml",
     "lines": "182",
     "quote": "GOLDEN_PASS_THRESHOLD: ${{ vars.GOLDEN_PASS_THRESHOLD || '0.99' }}"
    }
   ],
   "against": "Thresholds disagree across places: 0.95 in the gold file (golden_dataset.json L4 \"pass_threshold\": 0.95), 0.98 runner default, 0.99 in CI.",
   "adds_to_existing": [
    38,
    60,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Fix a reported judging failure with a general rule, and keep the reported item's details and standard-specific rules out of the general rubric.",
   "kind": "adopted rule",
   "found_by": "Repository rule backed by a test banning item-specific terms from the audits and a test banning substandard-specific rules from the standardized-test overlays (issue 397).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/AGENTS.md",
     "lines": "154",
     "quote": "When fixing an issue, generalize from the reported example. Do not paste the issue's exact example, item text, answer choices, IDs, issue numbers, or attachment-specific content into production prompts, rubrics, evaluators, tests, or code unless the requirement is explicitly about that literal content."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_sat_overlay_no_substandard_rules.py",
     "lines": "6-8",
     "quote": "Substandard-level guidance is owned by the curriculum repo and delivered at runtime through the Curriculum API."
    }
   ],
   "against": "Several audits remain tied to narrow content patterns, e.g. closed_ended_evaluation.txt L63 (\"names a specific wild animal species by its common name\") and L162 (geographic reference lines).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When scoring a judge against labelled cases, count the items it failed to evaluate as misses, not as excluded.",
   "kind": "adopted rule",
   "found_by": "Between 2.5.3 and 2.6.3 the gold runner's pass rate changed from passes over evaluated items to passes over all items.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/golden/runner.py",
     "lines": "350-352",
     "quote": "Count errored items as misses for the release gate. A green golden run should mean enough of the whole dataset passed, not just the subset that completed without provider/runtime errors."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/src/inceptbench/golden/runner.py",
     "lines": "350-351",
     "quote": "evaluated = total - errors pass_rate = (passed / evaluated) if evaluated > 0 else 0.0"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    37
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Spend repeat judgments where a verdict sits near a threshold: re-run borderline items and break disagreements with a third run.",
   "kind": "adopted rule",
   "found_by": "Run-to-run flips concentrated in borderline items; consensus scoring was added for overall scores between 0.75 and 0.90.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/llm/baml_native_evaluator.py",
     "lines": "31-33",
     "quote": "Consensus scoring: for borderline overall scores in this range, run a second BAML call and average. If the two runs disagree on bucket, run a 3rd tiebreaker. CONSENSUS_SCORE_RANGE = (0.75, 0.90)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 9a68759 message)",
     "lines": "12-14",
     "quote": "- Add consensus scoring to call_baml_question: borderline scores (0.75–0.90) trigger a 2nd BAML call; if buckets agree, average; if they disagree, run a 3rd tiebreaker and majority-vote"
    }
   ],
   "against": "A borderline gold item still flipped between runs after consensus (test_evaluator_prompt_rules_962.py L213-217).",
   "adds_to_existing": [
    34,
    65
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Have the judge write its reasoning before its score; a score emitted first stayed put even when the reasoning that followed corrected it.",
   "kind": "adopted rule",
   "found_by": "A judge committed 0.82, its reasoning then concluded 0.92, and the recorded score stayed 0.82 because of output field order.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 30f12a3 message)",
     "lines": "33-34",
     "quote": "- Fixes: LLM committed wrong score 0.82, reasoning self-corrected to 0.92, but JSON score stayed at 0.82 due to field commit order"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt",
     "lines": "311",
     "quote": "**CRITICAL**: Write reasoning BEFORE assigning scores. The score must follow from the reasoning."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Do not show a judge how its verdict will be combined downstream; a note that a stricter audit would be merged in made it fail a labelled passing case in every run.",
   "kind": "measured",
   "found_by": "With the merge description visible in the judge's output schema, a gold pass-case failed in 2 of 2 runs, versus passing 2 of 2 without it.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit b4a9346 message)",
     "lines": "3-6",
     "quote": "The factual_audit field was appearing in the JSON schema sent to Gemini, with a description mentioning 'merged into factual_accuracy via min(main,audit)'. This primed the LLM to be more aggressive about failing factual_accuracy, causing golden-046 to consistently fail (0/2 pass on PR vs 2/2 on main)."
    }
   ],
   "against": "Two runs on one item.",
   "adds_to_existing": [
    30
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Score only the dimensions that apply to the content type; leave a non-applicable dimension out rather than passing or failing it.",
   "kind": "adopted rule",
   "found_by": "Issue 343: instruction-design dimensions were scored on articles they do not apply to; they are now suppressed and nulled in code.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit ee21a33 message)",
     "lines": "18-22",
     "quote": "#343: follows_direct_instruction incorrectly evaluated for SS articles - Add METRIC SUPPRESSION block to social_studies_evaluation.txt prompt - Add post-processing in ArticleEvaluator.evaluate() to null out DI-only metrics (follows_direct_instruction, worked_examples, practice_problems) for any article routed to the SS overlay"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/article/social_studies_evaluation.txt",
     "lines": "55",
     "quote": "**DO NOT evaluate or output scores for the following metrics** — they are not applicable to Social Studies articles and must be **omitted entirely** from your output:"
    }
   ],
   "against": "CONTRIBUTING.md L52 (2.6.6): \"Metrics that don't apply to your type should auto-pass\".",
   "adds_to_existing": [
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Require the judge to cite the text that earns each pass, not only each failure; uniformly perfect scores were rubber-stamping.",
   "kind": "adopted rule",
   "found_by": "Issue 342: uniform perfect scoring on articles.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit ee21a33 message)",
     "lines": "13-16",
     "quote": "#342: uniform perfect scoring / rubber-stamp evaluation - Add POSITIVE EVIDENCE REQUIREMENT: must cite specific text for each 1.0 score - Add ANTI-RUBBER-STAMP CHECKS: mandatory checks for reflection repetition, register shifts, and curriculum element enumeration"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/article/evaluation.txt",
     "lines": "106",
     "quote": "**POSITIVE EVIDENCE REQUIREMENT**: Even when giving a metric a score of 1.0, you MUST cite at least one specific piece of text evidence from the article that justifies the pass — not just the absence of a problem."
    }
   ],
   "against": "The question judge still defaults to pass without positive evidence (_base_evaluation.txt L5).",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a standard lists its elements explicitly, material claiming to teach it must cover each one; a single missing element fails alignment.",
   "kind": "adopted rule",
   "found_by": "Issue 341: articles covering only part of a standard's listed elements passed alignment.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit ee21a33 message)",
     "lines": "8-11",
     "quote": "#341: curriculum_alignment partial coverage - Add COMPLETENESS CHECK: explicitly listed elements in standard must ALL appear - Add PROPORTIONALITY CHECK: 'various groups' requires 3+ representatives - curriculum_alignment = 0.0 if any explicitly required element is entirely absent"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/article/evaluation.txt",
     "lines": "111",
     "quote": "- **curriculum_alignment**: Enumerate the explicit elements listed in the standard and verify EACH one appears in the article."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    58
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When the skill is combining sources or formats, every source given must be needed to reach the answer; a source that only decorates, or one that alone suffices, fails the item.",
   "kind": "adopted rule",
   "found_by": "Integration items carried pictures their own explanations never used, and synthesis items reduced to matching a single note; ELA audits, a deterministic detector and SAT synthesis rules were added (issue 968).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/ela_evaluation.txt",
     "lines": "20",
     "quote": "Integration must demand combining at least two formats to reach the answer."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/evaluators/question.py",
     "lines": "904-907",
     "quote": "if the item carries an image_url but the answer_explanation never references any visual element, the image is decorative and the item fails the integration demand."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt",
     "lines": "100-102",
     "quote": "If the aim is so narrow that only one note is relevant and the student can identify the correct answer by simple keyword matching, the item reduces synthesis to a matching exercise."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5,
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Each claim in a keyed answer must trace to a point the source makes; a claim on ground the source never covered is an error, while naming the category of what the source described is not.",
   "kind": "adopted rule",
   "found_by": "An argument-conclusion audit was added and then narrowed after it over-flagged the category-label summaries the standard expects (issue 418).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/ela_evaluation.txt",
     "lines": "39",
     "quote": "- ANY correct option with a `NONE` claim → `factual_accuracy = 0.0`. \"Pedagogical synthesis\" / \"appropriate inference for hard items\" do NOT rescue genuine domain shifts. They DO rescue category-label synthesis covered by the bullet above — that is the standard's intended skill, not a violation."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_evaluator_prompt_rules_411_418.py",
     "lines": "17-19",
     "quote": "concluding-statement items were failing on `factual_accuracy` because Audit B was over-flagging the exact category-label synthesis the standard expects."
    }
   ],
   "against": "See the over-flagging above: a strict trace-to-source audit misfired on legitimate synthesis until narrowed.",
   "adds_to_existing": [
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A harder version of an item must demand more - different facts or a different structure - rather than reword the easier one; judging items one at a time cannot catch this.",
   "kind": "adopted rule",
   "found_by": "The variance investigation noted the judge cannot detect the same facts rephrased across difficulty levels because items are judged independently; a batch-level recycling check exists only for matching items.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/match_evaluation.txt",
     "lines": "504",
     "quote": "If the majority of items in a Medium question are recycled from its Easy counterpart, set `difficulty_alignment = 0.0` for the Medium question — it is not genuinely harder, just relabelled."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/EVALUATOR_VARIANCE_FIX.md (deleted in commit e5be84f; read with git show e5be84f^:docs/EVALUATOR_VARIANCE_FIX.md)",
     "lines": "288",
     "quote": "8. **Cross-difficulty recycling** — The evaluator still can't detect cross-difficulty item recycling (same facts rephrased across easy/medium/hard) because each question is evaluated independently."
    }
   ],
   "against": "match_evaluation.txt L492: \"This check is only active when you can see multiple difficulty variants for the same substandard in the batch.\"",
   "adds_to_existing": [
    41
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Difficulty comes from what the task demands - reasoning steps and plausible confusions - not from length, number of parts or hard vocabulary; a harder item should let a partly informed student argue for a wrong answer.",
   "kind": "adopted rule",
   "found_by": "Matching and reading rubrics after length, item count and vocabulary were being mistaken for difficulty.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt",
     "lines": "127",
     "quote": "- Length alone is not difficulty."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/match_evaluation.txt",
     "lines": "315",
     "quote": "Hard vocabulary or long item text does not elevate an EASY structure to MEDIUM, but genuine item ambiguity does."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/match_evaluation.txt",
     "lines": "322",
     "quote": "Ask: \"What is the wrong category a partially-knowing student would pick for this item, and why would they pick it?\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "To check an item's labelled level, test it against every level's definition and see which one it fits, instead of starting from its label.",
   "kind": "adopted rule",
   "found_by": "Added to the closed-ended and matching rubrics to stop confirmation bias in difficulty calls.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "544",
     "quote": "This prevents confirmation bias — do not start from the labeled level and try to justify it. Instead, objectively determine which level fits and compare."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/match_evaluation.txt",
     "lines": "333",
     "quote": "This prevents confirmation bias. Do NOT start from the labeled level and try to justify it."
    }
   ],
   "against": "Without written level definitions the layers disagree on whether to judge level at all (_base_evaluation.txt L170 versus closed_ended_evaluation.txt L547).",
   "adds_to_existing": [
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "An argument task needs sources and a prompt that support more than one defensible position.",
   "kind": "adopted rule",
   "found_by": "Document-based and long-essay rubrics.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/dbq_evaluation.txt",
     "lines": "63",
     "quote": "- Score 0.0: All documents point to one obvious conclusion; no real analysis or argumentation is possible"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/leq_evaluation.txt",
     "lines": "58",
     "quote": "- Score 0.0: Only one valid position exists, making the prompt non-argumentative"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Build each part of an open question so a vague, generic answer cannot earn credit and so each part can be scored on its own.",
   "kind": "adopted rule",
   "found_by": "Short-answer rubric.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/saq_evaluation.txt",
     "lines": "41",
     "quote": "- Score 1.0: Parts require specific evidence, examples, or reasoning; generic answers would not earn points"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/saq_evaluation.txt",
     "lines": "36",
     "quote": "- Score 1.0: Has the expected number of parts (check metadata/curriculum context for requirements); each part has a clear task verb; parts are logically connected but independently scorable"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    56,
    69
   ],
   "name_bearing_source": false
  },
  {
   "statement": "An ordering item needs one defensible order: every element must have a clear position (not an ongoing condition with no starting point), the stem must name the ordering rule, and elements must not carry the information that settles the order.",
   "kind": "adopted rule",
   "found_by": "Sequencing rubric added after items mixed gradual processes with events and embedded dates that made ordering trivial.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/sequence_evaluation.txt",
     "lines": "36",
     "quote": "The test: if you cannot name the specific event/law/publication that STARTED this condition → it is an ongoing_state → orderability ≤ 3."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/sequence_evaluation.txt",
     "lines": "176-178",
     "quote": "**Dates-in-items flag:** Items containing explicit years/centuries inline (e.g., \"in 1492\", \"c. 1440 CE\", \"during the 15th century\") reduce the task to date-reading rather than content knowledge."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/sequence_evaluation.txt",
     "lines": "189-190",
     "quote": "Does the question stem make the ordering criterion explicit? Do items avoid forward references that reveal their relative position?"
    }
   ],
   "against": "sequence_evaluation.txt L178-179: dates are fine when \"the specific date is itself the curriculum fact being tested\".",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Scan generated student-facing text for fused words (such as 'themain' or 'tothe') and treat them as failures, since young readers cannot recover them.",
   "kind": "adopted rule",
   "found_by": "A recurring defect in generated text; a mandatory mechanical scan was added to the article and reading rubrics.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/article/evaluation.txt",
     "lines": "759-761",
     "quote": "- **Merged non-word forms** in student-facing text: `themain`, `forclosure`, `becausethe`, `tothe`, `ofthe`, `inthe`, `sentenceending`, etc. - These are serious errors, especially for early-grade content where students may not recognize malformed words - If merged non-words appear ANYWHERE in the student-facing text, set `diction_and_sentence_structure = 0.0`"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/nonfiction_reading/evaluation.txt",
     "lines": "410-411",
     "quote": "- **Merged non-word forms**: `themain`, `thewater`, `becausethe`, `tothe`, `ofthe`, `inthe`, etc. - These are serious errors, especially for early-grade content where students may not recognize malformed words"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep the text students must read within, or only just above, their grade's reading band; flag a sustained adult register rather than a single hard term, unless the hard words are what is being taught.",
   "kind": "adopted rule",
   "found_by": "Issues 411-415: adult-register passages passed at 0.95 ACCEPTABLE; a sustained-register rule was added.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/ela_evaluation.txt",
     "lines": "43-45",
     "quote": "For ELA items targeting grades 3–8, the passage, transcript, or writing samples that the student must read should sit within (or only modestly above) the typical reading band for the target grade."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/ela_evaluation.txt",
     "lines": "53-55",
     "quote": "Do NOT flag because a single domain term appears once; the failure is a sustained register mismatch across the passage."
    }
   ],
   "against": "sat_rw_evaluation.txt L131-132: \"task demand matters more than prose complexity. Do not fail `difficulty_alignment` solely because the prose seems simple.\"",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Do not fail an item as too obvious because it is obvious to an expert; judge it for the learners it targets.",
   "kind": "adopted rule",
   "found_by": "Matching rubric note on diagnostic value.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/match_evaluation.txt",
     "lines": "260",
     "quote": "**NOTE**: A task that feels \"obvious in hindsight\" to an expert is still diagnostically useful if the target student population is learning the concept."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Whether a support such as a picture or diagram helps or gives the answer away depends on the item's purpose: it scaffolds when the idea is new and bypasses the skill in a fluency check.",
   "kind": "adopted rule",
   "found_by": "Scaffolding pictures were being failed as giveaways; an audience-relative rule was added.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "685-686",
     "quote": "- If the purpose is clearly fluency/mastery assessment AND the stimulus allows bypassing the skill → consider failing - If the purpose is conceptual learning OR unclear → accept scaffolding as appropriate"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/math_evaluation.txt",
     "lines": "22-28",
     "quote": "- A countable 3×4 array is APPROPRIATE scaffolding"
    }
   ],
   "against": "closed_ended_evaluation.txt L687: \"When uncertain, default to PASS\".",
   "adds_to_existing": [
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Localized items must be solvable without local cultural knowledge, use at most one region-specific reference, stay in the language of instruction, and fall back to neutral wording when a guardrail cannot be met.",
   "kind": "adopted rule",
   "found_by": "Localization guidelines judged rule by rule; stacked regional props read as caricature.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/src/inceptbench/agents/localization_guidelines.json",
     "lines": "29",
     "quote": "**Universal solvability**: Problems should be solvable without requiring local cultural knowledge."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/src/inceptbench/agents/localization_guidelines.json",
     "lines": "102",
     "quote": "**Regional Reference Limit**: Use at most one explicit, region-specific object or concept."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/legacy/EVALUATORS.md",
     "lines": "244",
     "quote": "These rules reject caricatures (e.g., stacking “camel + dates + desert”) and prevent switching languages unless instruction requires it."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Personalizing an item to a student's interests means naming one of those interests in what the student reads; a thematic hint does not count, and personalization must not sway correctness judgments.",
   "kind": "adopted rule",
   "found_by": "Interest-relevance metric backed by a deterministic literal-mention check.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/evaluators/base.py",
     "lines": "1127-1128",
     "quote": "**Rule:** the content must reference AT LEAST ONE of the listed interests by literally naming it."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/evaluators/base.py",
     "lines": "1135-1136",
     "quote": "No listed interest is literally named. Inferred or thematic connections DO NOT pass"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/evaluators/base.py",
     "lines": "1142-1144",
     "quote": "Do NOT let this metric influence any other metric (factual_accuracy, educational_accuracy, clarity_precision, etc.) — those judge correctness, not engagement."
    }
   ],
   "against": "base.py L1145-1146: a literal mention can still fail \"if it is shoehorned in a way that makes the question incoherent\".",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Test a generator for variety by sending the same request ten times and measuring how different the outputs are; low variety means learners will meet near-repeats.",
   "kind": "adopted rule",
   "found_by": "Benchmark variety check: mean pairwise word-trigram distance across 10 responses, with scores below 0.45 marking the generator as static.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/README.md",
     "lines": "146",
     "quote": "- Sends each provided request 10 times, scores response diversity via trigram Jaccard distance"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/tools/variety_check.py",
     "lines": "500",
     "quote": "is_static = (variety_score < self.threshold) if variety_score is not None else None"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Anchor a judge's grade-level difficulty call to the most similar validated items for that grade rather than to its own sense of the grade.",
   "kind": "adopted rule",
   "found_by": "The bundled reading-question QC pipeline runs its difficulty check only when benchmark items are supplied.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "43",
     "quote": "A set of the 5 most semantically similar validated test questions that are considered benchmarks for the specified grade level"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/submodules/reading-question-qc/qc_pipeline/README.md",
     "lines": "18",
     "quote": "# Include difficulty assessment (requires benchmark questions)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Reconcile a local copy of curriculum data with the published source by matching content, not identifiers; identifiers can be shifted wholesale.",
   "kind": "measured",
   "found_by": "For one course, 224 of 239 local entries matched the canonical source by content, but 218 of those sat at a different identifier (systematically off by one period).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit fb17482 message)",
     "lines": "10-13",
     "quote": "The local APEURO entries were systematically off by one period. Verified by content cross-match: 224 of 239 inceptbench APEURO entries had a strong content match in the curriculum repo, but 218 of those were at a different KC id."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    63,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give a judge only published curriculum data; where the source publishes nothing (no boundaries or misconceptions), leave it empty rather than generate it.",
   "kind": "adopted rule",
   "found_by": "Merging curriculum context for the judge on the AP branch.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 082d3a3 message)",
     "lines": "42-45",
     "quote": "(CB CED has no published boundaries/misconceptions for APEURO; we don't fabricate them)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit fb17482 message)",
     "lines": "5",
     "quote": "Pure data combination — no LLM-generated content."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Open question: when a judge is given reference facts, should a claim the facts do not support fail, or only a claim they contradict?",
   "kind": "open question",
   "found_by": "The two grounding designs in scope disagree: the unmerged AP branch treats unsupported claims as unsupported, while the fact audit and the reference-context path fail only direct contradictions.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/src/inceptbench/evaluators/base.py",
     "lines": "620",
     "quote": "If a claim cannot be supported by an atom listed here, it is unsupported."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/tools/factual_accuracy_audit.py",
     "lines": "212",
     "quote": "3. Score **0.0** ONLY if a passage clearly and directly contradicts"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/evaluators/question.py",
     "lines": "1241",
     "quote": "- Do NOT penalize correct content just because Wikipedia doesn't mention it."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Generated passages must not present invented studies, data, quotations or named people as real; anonymous framing is acceptable only when no specific fact is presented as real.",
   "kind": "adopted rule",
   "found_by": "Standardized-test reading overlay; short-answer and essay rubrics also fail fabricated or unattributed stimuli.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt",
     "lines": "19-23",
     "quote": "Fail `factual_accuracy` for a false, fabricated, or materially misleading claim in the stimulus, key, or explanation. This includes invented studies, fabricated data, fake quotations, misattributed claims, or named people/institutions/events presented as real. Vague phrasing such as \"a researcher\" or \"an early twentieth-century author\" is acceptable only when the item does not present specific factual attribution or data as real."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/saq_evaluation.txt",
     "lines": "68",
     "quote": "- Score 0.0: Stimulus is fabricated/irrelevant/unattributed, OR harmful (wrong, misleading, contradictory, distracting), OR Mode A and stimulus is not core, OR Mode B and no stimulus present"
    }
   ],
   "against": "dbq_evaluation.txt L17 allows fabricated documents with \"pedagogical justification\"; the three-gate test (factual_accuracy_audit.py L114-125) forbids failing a document merely because the judge thinks it does not exist.",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge whether two answers are equivalent by the convention being taught; answers that are equal in general can differ in meaning under the lesson's convention.",
   "kind": "adopted rule",
   "found_by": "An early-grade grouping convention under which two mathematically equal expressions describe different situations.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/math_evaluation.txt",
     "lines": "19",
     "quote": "**Curriculum Context Note**: When curriculum specifies pedagogical distinctions (e.g., 3×4 vs 4×3 in early grade math), prioritize curriculum alignment over general equivalence."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/src/inceptbench/agents/simple_content_qc.py",
     "lines": "129-131",
     "quote": "the equations \"4 x 3 = 12\" and \"3 x 4 = 12\" are NOT both correct (even though they are mathematically equivalent) because they are NOT equivalent within the context of the problem"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    10,
    13
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check submitted content for text addressed to the judge - pre-written scores, dimension-by-dimension self-praise, instructions to pass - and void the whole evaluation when it is found.",
   "kind": "adopted rule",
   "found_by": "An integrity check was added in 2.3.6 to detect prompt injection and score manipulation in submitted content.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/article/evaluation.txt",
     "lines": "62",
     "quote": "**The key test for Category C:** Is this text written to *help a student or teacher understand the content*, or is it written to *convince an evaluator to give high scores*?"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/website/content/english/pages/release-notes.md",
     "lines": "17",
     "quote": "- Added `integrity_check` metric to detect prompt injection and score manipulation attempts in submitted content."
    }
   ],
   "against": "article/evaluation.txt L57-60: genuine explanations in rationale, hint or feedback fields are not violations.",
   "adds_to_existing": [
    12
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Do not fail an item on an ambiguous reading of a picture alone: trust structured measurements over a model's description, which is unreliable on fine positions and nesting.",
   "kind": "adopted rule",
   "found_by": "Two tiers of image evidence were introduced after model descriptions misplaced points on number lines and items inside nested diagrams.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
     "lines": "279",
     "quote": "It can be wrong about exact positions on number lines, placement of items within nested diagrams (Venn diagrams, set diagrams), and fine spatial details."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt",
     "lines": "257",
     "quote": "**Conservative default**: For counting ambiguities (tick marks, shaded squares, number line positions), do NOT fail `factual_accuracy` from image evidence alone unless deterministic checks report explicit FAIL or the contradiction is unambiguous at normal viewing."
    }
   ],
   "against": "The structured analyser also erred: test_issue_363_visual_false_alarms.py L36 \"2x2 labeled layout where old x-only ordering swaps B and C.\"",
   "adds_to_existing": [
    22,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a code check passes, overturn only the judge's failures that cite what the code checked; other failures stand.",
   "kind": "adopted rule",
   "found_by": "Design of the deterministic math-verification guard.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/evaluators/guards.py",
     "lines": "85-90",
     "quote": "If the LLM scored factual_accuracy low (< 0.3) and its reasoning explicitly cites mathematical errors, but precomputed SymPy verification says CORRECT, override factual_accuracy to 1.0. Non-mathematical factual errors (history, biology, etc.) are NEVER silenced by a passing arithmetic check."
    }
   ],
   "against": "docs/internals/math-verifier.md L65: the code verdict depends on a model's extraction, which \"can sometimes misrepresent the problem\".",
   "adds_to_existing": [
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Feedback on a wrong choice must address that specific choice - its error and the likely misconception behind it - and offer a concrete strategy, not generic encouragement.",
   "kind": "adopted rule",
   "found_by": "Explanation QC checks in the bundled reading-question pipeline.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "65",
     "quote": "The feedback must address the particular distractor chosen"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "69",
     "quote": "The feedback must categorize or name the type of thinking error"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "81",
     "quote": "The tip should be specific and actionable, not vague encouragement"
    }
   ],
   "against": "The same rubric requires the feedback to give the answer (prompts.json L77: \"The feedback must either explicitly state the correct answer or clearly guide the student to it\"), which conflicts with truth 1.",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Model judges of educational responses score more generously than human raters and agree with them only moderately.",
   "kind": "external research",
   "found_by": "EduBench (https://arxiv.org/pdf/2505.16160), bundled in scope: one system's outputs averaged 9.05 from a model judge but 7.82 from humans; Kendall's W between model judges and humans was 0.56-0.63.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/submodules/EduBench/README.md",
     "lines": "122",
     "quote": "|                 | DeepSeek V3            | 9.67 | 9.12 | 8.97 | 8.82 | **8.32** | 9.31 | 9.34 | 8.65 | 9.23 | 9.05 |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/submodules/EduBench/README.md",
     "lines": "142",
     "quote": "|                 | DeepSeek V3            | 7.45 | 8.12 | 8.16 | 8.17 | 7.84 | 7.56 | 8.08 | 8.01 | 7.03 | 7.82 |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/submodules/EduBench/README.md",
     "lines": "218",
     "quote": "- **Consistency between humans and models**: The model evaluations do not fully align with human judgments, which may be due to limited understanding of the evaluation criteria by the models."
    }
   ],
   "against": "EduBench README L193: the best and worst systems were the same under human and model judges.",
   "adds_to_existing": [
    44,
    37
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Enforce a standard's boundaries strictly only when the target standard was given; when it was inferred from the content, treat its boundaries as guidance.",
   "kind": "adopted rule",
   "found_by": "Curriculum confidence levels used by every judge prompt; no measurement found.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt",
     "lines": "206",
     "quote": "- **GUARANTEED** (from explicit skills metadata): Assessment boundaries strictly enforced. No exceptions."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt",
     "lines": "208",
     "quote": "- **SOFT** (from content inference): Boundaries are guidance. Only fail for clear, unambiguous violations."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/submodules/reading-question-qc/qc_pipeline/config/prompts.json",
   "lines": "77",
   "quote": "The feedback must either explicitly state the correct answer or clearly guide the student to it"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt",
   "lines": "62",
   "quote": "**Display Timing**: Content is ONLY an \"answer giveaway\" if shown BEFORE the student attempts to answer. Content behind reveal cues, shown after submission, or on-demand is NEVER a giveaway."
  },
  {
   "truth": 3,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
   "lines": "339",
   "quote": "- **Showing the answer or reasoning that leads to it is NOT a failure.** Explicit \"Answer: ...\" is expected."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/mcq_set/evaluation.txt",
   "lines": "310",
   "quote": "- Any question can be answered without the stimulus"
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/evaluators/question.py",
   "lines": "979-983",
   "quote": "Narrative-writing-evaluation items (standards naming engage/orient reader, event sequence, establish context with characters) that ask the student to pick the BEST among multiple long parallel options (drafts/passages of 40+ words each) carry a high risk of containing distractors that a reasonable student could defensibly pick."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/submodules/reading-question-qc/qc_pipeline/config/prompts.json",
   "lines": "21",
   "quote": "Degree-Only Difference**: Differs only in degree/intensity when the passage doesn't clearly establish the distinction"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/mcq_set/evaluation.txt",
   "lines": "372",
   "quote": "- Chi-square probability >= 60% (if provided)"
  },
  {
   "truth": 9,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt",
   "lines": "5",
   "quote": "If reasonable evaluators could disagree, the metric passes."
  },
  {
   "truth": 9,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/src/inceptbench/agents/localization_evaluator.py",
   "lines": "51",
   "quote": "- Return FAIL (score=0) if there is any violation, uncertainty, or missing evidence."
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 2750903 message)",
   "lines": "3",
   "quote": "Per golden dataset regression test (94% pass rate, below 98% threshold):"
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/sequence_evaluation.txt",
   "lines": "111-112",
   "quote": "If you are uncertain of the specific approximate dates for both items → default to sequence_accuracy = 4 (uncertain, not confirmed wrong)."
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/website/content/english/pages/answer-verification.md",
   "lines": "105",
   "quote": "- **●●○○○○○○○○ (0-4)**: Low - manual review recommended"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt",
   "lines": "54-55",
   "quote": "answer choices must be verbatim spans from the stimulus. Ellipses are allowed only for shortening; paraphrased or fabricated options fail `specification_compliance`"
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/src/inceptbench/agents/simple_content_qc.py",
   "lines": "78-79",
   "quote": "The image only needs to reflect the present state of the content as described in the text."
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/legacy/EVALUATORS.md",
   "lines": "140",
   "quote": "1. Task fidelity (25%) - Shows only given info"
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/article/evaluation.txt",
   "lines": "658",
   "quote": "> - Apply **heightened scrutiny** for historical, scientific, or factual inaccuracies"
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/legacy/EVALUATORS.md",
   "lines": "152-153",
   "quote": "- ❌ `quant_count_mismatch` - Wrong counts - ❌ `label_invention` - Invented labels"
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/website/Incept Pedagogy & Learning Science Overview.md",
   "lines": "425",
   "quote": "| **Word Length (Questions / Items)** | 5–10 words per question. | 10–15 words per question. | 15–25 words per question. |"
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/ela_evaluation.txt",
   "lines": "75",
   "quote": "For these questions, **the formatting markup in the answer options IS the substance of the correct answer**, not decoration."
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/evaluators/question.py",
   "lines": "1055-1058",
   "quote": "The stimulus-reference check uses it as a fallback so a recursively decomposed child whose anchor slice missed a sibling-region stimulus is not falsely flagged when the parent article actually carries that image."
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/EVALUATOR_VARIANCE_FIX.md (deleted in commit e5be84f; read with git show e5be84f^:docs/EVALUATOR_VARIANCE_FIX.md)",
   "lines": "21",
   "quote": "**Example**: Both runs have C=0, N=0 (all metrics pass). Run 1: LLM outputs `overall.score = 0.97` → ACCEPTABLE. Run 2: LLM outputs `overall.score = 1.0` → SUPERIOR. Pure randomness."
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/EVALUATOR_VARIANCE_FIX.md (deleted in commit e5be84f; read with git show e5be84f^:docs/EVALUATOR_VARIANCE_FIX.md)",
   "lines": "539",
   "quote": "Baseline was: 38/690 (5.5%) → 55% reduction"
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/src/inceptbench/agents/localization_evaluator.py",
   "lines": "49",
   "quote": "You are a localization quality specialist. Evaluate ONE localization rule at a time."
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 0a22a5b message)",
   "lines": "14-16",
   "quote": "- Inject the raw stem text (capped at 2000 chars) inside the cue block so the LLM cannot crop or deny material that is quoted alongside the instruction that asks it to verify."
  },
  {
   "truth": 33,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/EVALUATOR_VARIANCE_FIX.md (deleted in commit e5be84f; read with git show e5be84f^:docs/EVALUATOR_VARIANCE_FIX.md)",
   "lines": "422",
   "quote": "**Finding**: **Wikipedia-grounded Gemini performed WORSE** — caught only 3/22 factual errors (down from 6/22 baseline) and increased variance to 7.0% (up from 5.5%)."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/EVALUATOR_VARIANCE_FIX.md (deleted in commit e5be84f; read with git show e5be84f^:docs/EVALUATOR_VARIANCE_FIX.md)",
   "lines": "5",
   "quote": "When running InceptBench evaluation **twice on the same 690 Grade 10 questions**, the overall rating (`SUPERIOR` / `ACCEPTABLE` / `INFERIOR`) **disagrees for 38 questions (5.5% variance)**."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/EVALUATOR_VARIANCE_FIX.md (deleted in commit e5be84f; read with git show e5be84f^:docs/EVALUATOR_VARIANCE_FIX.md)",
   "lines": "173",
   "quote": "GPT-5.4-mini at temperature=0.0 had **3x more variance** (15.7%) than Gemini at temperature=1.0 (5.5%)."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/EVALUATOR_VARIANCE_FIX.md (deleted in commit e5be84f; read with git show e5be84f^:docs/EVALUATOR_VARIANCE_FIX.md)",
   "lines": "586",
   "quote": "Top remaining source: `curriculum_alignment` (4 flips). This metric asks whether the question aligns with curriculum standards — a subjective judgment where borderline cases will always have some variance at temperature=1.0."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 2750903 message)",
   "lines": "6-7",
   "quote": "- distractor_quality: remove 'borderline default to 1.0' paragraph (revert PR #268 change that made evaluator too lenient on ambiguous distractor flaws)"
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/EVALUATOR_VARIANCE_FIX.md (deleted in commit e5be84f; read with git show e5be84f^:docs/EVALUATOR_VARIANCE_FIX.md)",
   "lines": "129",
   "quote": "- Added paragraph after the Fail conditions: \"If two reasonable evaluators could disagree on whether distractors are 'plausible enough' or 'parallel enough,' you MUST default to 1.0. Only score 0.0 when the flaw is concrete, specific, and unambiguous.\""
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 596ad44 message)",
   "lines": "3-6",
   "quote": "BAML path was returning raw LLM scores without applying the same score clamping that the default generate_structured() path applies. This caused BAML to over-score borderline ACCEPTABLE/SUPERIOR cases (e.g. golden-089: BAML=1.00 SUPERIOR vs expected ACCEPTABLE)."
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_ela_enforcement_guard.py",
   "lines": "4-5",
   "quote": "The image consistency guard must NOT silently cancel an ELA detector enforcement that deliberately set factual_accuracy to 0.0."
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/scores/summary.txt",
   "lines": "34-35",
   "quote": "NOTE: Issue recommendations are based on the Reading Question QC evaluator, as it is the only production-validated framework."
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/scores/summary.txt",
   "lines": "40-41",
   "quote": "SAT Reading Generation       | 0.654 (65%) | 0.605   | 0.704      | 100.0%   | 82 (3 sets) | 1.4.0 APLIT Quiz Generation        | 0.712 (71%) | 0.823   | 0.602      | 66.7%    | 60 (3 sets) | 1.4.0"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_stimulus_promise_detection.py",
   "lines": "4-6",
   "quote": "The fake-stimulus fixture file holds questions that promise a visual/audio/video/multimedia artifact but only provide a prose description (or ad-hoc text data)."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 715eadc message)",
   "lines": "16",
   "quote": "Golden dataset now: 100/100 expected to pass."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 3a88a35 message)",
   "lines": "11-14",
   "quote": "The new evaluator's 3-gate factual_accuracy system correctly catches this as INFERIOR (score 0.0). Relabel the expected verdict so the golden suite reflects the actual quality of the item rather than the curator's mistake."
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/website/Incept Pedagogy & Learning Science Overview.md",
   "lines": "87",
   "quote": "Each concept begins with clear modeling from the teacher. Students see exactly how to perform the skill before trying it themselves. This is followed by short, guided practice and then independent work where students apply what they’ve learned."
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
   "lines": "442",
   "quote": "1. Read the stem WITHOUT looking at the accepted-answer list."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/submodules/EduBench/README.md",
   "lines": "218",
   "quote": "- **Consistency between humans and models**: The model evaluations do not fully align with human judgments, which may be due to limited understanding of the evaluation criteria by the models."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/EVALUATOR_VARIANCE_FIX.md (deleted in commit e5be84f; read with git show e5be84f^:docs/EVALUATOR_VARIANCE_FIX.md)",
   "lines": "467",
   "quote": "| **difficulty_alignment flip** | 9 | Prompt contradiction (base vs overlay) |"
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/src/inceptbench/agents/simple_content_qc.py",
   "lines": "86-88",
   "quote": "6) Look for any unrendered LaTeX anywhere within the text in the image (e.g., \"\\\\div\", \"\\\\\\\\times\", \"\\\\(\", \"\\\\[\", \"\\\\frac\", etc.). Any occurances of unrendered LaTeX are blocking issues."
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/evaluators/question.py",
   "lines": "700-701",
   "quote": "The student therefore sees the same set of options listed twice. This is a structural authoring defect, not a stylistic choice"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit fb17482 message)",
   "lines": "48-50",
   "quote": "Provenance per record (set during merge, not LLM-derived): ``merge_source`` — inceptbench_native | inceptbench_enriched | inceptbench_propagated | inceptbench_remapped |"
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/tests/test_evaluator_prompt_rules_984.py",
   "lines": "6-7",
   "quote": "Root cause: the DBQ evaluation prompt did not explicitly require the prompt TOPIC to match the requested substandard, only that documents support the analytical task."
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/releases/v1.4.0.md",
   "lines": "46-48",
   "quote": "- Answer verification added 0.0 to average (asymmetric penalty) - Penalty magnitude depended on number of other evaluators - Mathematically flawed: 4 evaluators = 25% penalty, 6 evaluators = 16.7% penalty"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/mcq_set/evaluation.txt",
   "lines": "163",
   "quote": "- `factual_accuracy`: If the provided `factual_accuracy failures` count is > 0 → MCQ set factual_accuracy = 0.0"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
   "lines": "227",
   "quote": "If a rationale misattributes causality, misstates a mechanism, or contains a clearly incorrect fact — even when the evaluator attempts to dismiss it with \"pedagogical sense,\" \"educational context,\" or similar phrasing — that IS a factual_accuracy failure."
  },
  {
   "truth": 59,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/tools/factual_accuracy_audit.py",
   "lines": "139-140",
   "quote": "A few years off within the same period/context is NOT student harm."
  },
  {
   "truth": 59,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt",
   "lines": "133",
   "quote": "- **Passage-based questions**: Other errors elsewhere in a passage do not constitute a stimulus failure; only errors interfering with the targeted task matter."
  },
  {
   "truth": 62,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 0a22a5b message)",
   "lines": "10-13",
   "quote": "- Reframe cue as \"VERIFY AND PENALIZE IF CONFIRMED\": adds an explicit definition of stem redundancy, a narrow false-positive list, and an explicit list of disallowed rationalizations (including the exact \"common formatting style\" wording the LLM previously used)."
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/website/content/english/pages/release-notes.md",
   "lines": "23",
   "quote": "- Fixed substandard matching logic that was incorrectly aligning content to the wrong curriculum standards."
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/stimulus_promise_extraction.txt",
   "lines": "13",
   "quote": "The fact that the content offers a prose description instead of an image does NOT remove the promise — record the illustration, not the description."
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit ee21a33 message)",
   "lines": "24-25",
   "quote": "#344: article text referencing missing/unprovided stimulus not flagged - Add MISSING-PROMISED STIMULUS CHECK to stimulus_quality STEP 1"
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
   "lines": "617",
   "quote": "→ The stimulus must be **critical and integral** to the educational task — not merely non-harmful, engaging, or decorative."
  },
  {
   "truth": 64,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt",
   "lines": "671",
   "quote": "A question is NOT penalized simply because it can be solved from text alone."
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/llm/baml_native_evaluator.py",
   "lines": "31-32",
   "quote": "Consensus scoring: for borderline overall scores in this range, run a second BAML call and average. If the two runs disagree on bucket, run a 3rd tiebreaker."
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/evaluators/question.py",
   "lines": "510-511",
   "quote": "If the LLM ignored that directive, this guard enforces the contract deterministically."
  },
  {
   "truth": 67,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/docs/internals/math-verifier.md",
   "lines": "65",
   "quote": "Rule 2 is deliberately permissive because the extraction step can sometimes misrepresent the problem (wrong equation format, missing variables)."
  },
  {
   "truth": 67,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/evaluators/guards.py",
   "lines": "185-187",
   "quote": "Contradictions remain advisory because visual label extraction is not allowed to overrule the evaluator's direct reasoning after the fact."
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/mcq_set/evaluation.txt",
   "lines": "317",
   "quote": "- Questions test different skills/aspects of the stimulus"
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench-main/src/inceptbench/prompts/question/saq_evaluation.txt",
   "lines": "56",
   "quote": "- Score 1.0: Clear criteria for what earns each point; acceptable answers are well-defined"
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/.git (commit 15b8b5a message)",
   "lines": "31-32",
   "quote": "Golden dataset: 99/100 pass on both default and BAML paths. Zero verdict flips. 1 minor score diff (0.10) on golden-038 (both INFERIOR)."
  }
 ]
}
```
