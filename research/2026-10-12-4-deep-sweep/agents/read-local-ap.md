# read:local-ap

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "local-ap",
 "coverage": {
  "read": [
   "~/Documents/APinceptbench/README.md and docs/ (all 10 .md files: AP_GENERATOR_SPEC, AP_QUESTION_TYPES_SPEC, CURRICULUM_STANDARDS, EVALUATION_API, EVALUATION_PROCESS, GENERATOR_API_SPEC, GENERATOR_INPUTS, README, SYSTEM_ARCHITECTURE)",
   "~/Documents/APinceptbench/docs/reports/ (all 10 reports: FAILURE, RUN2-RUN8, COMPREHENSIVE, evaluation_20260225)",
   "~/Documents/APinceptbench/ap_benchmark/prompts/official_ap_prompts.py (lines 1-480), prompts/base.py, hard_fail/rules.py, calibration/validator.py, calibration/gold_standard.json (all 25 cases summarized), core/curriculum.py (lines 280-396), benchmark_official.py and evaluation_server.py (pass logic), test_server.py (consistency test)",
   "APinceptbench git history read-only via git show: initial-commit README.md, docs/AP_QUESTION_TYPES_SPEC.md, docs/AP_GENERATOR_SPEC.md, and commit stats of the cleanup commits",
   "~/Documents/APinceptbench/data/curriculum_facts.json and curriculum_relationships.json (first records only)",
   "~/Downloads/unit-1-apush-benchmark.jsonl (first and last record), unit-4-apush-benchmark.jsonl (first record), unit-1-apwh-benchmark.jsonl (first record)",
   "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx (sharedStrings resolved per sheet: Tracker, Work Flow, Master List, Unit 1 Articles header, all nine Unit N Nodes and nine Unit N Relationships sheets tallied; person names ignored)",
   "~/Downloads/Knowledge Schema Generator - AP USH Unit 2.xlsx (Instructions, Configuration, and tallies of Fact Gen, Mapping, Overlay, Consolidation Audit/Output, Supplemental, Refinement, Node Metadata, Relationship Gen Audit); Unit 4 (Instructions, identical); UNIT 7 (consolidation and relationship audits tallied); UNIT 5 and UNIT 6 (sheet lists only)",
   "~/Projects/incept-package-hub/docs/COURSE_PACKAGE_STANDARD.md (the only document there that mentions AP itself); course-packages/courses/g8-reading/review/evidence/case-for-review.md, science-process.md, validation/anti-gaming-blind-solve.json (InceptBench mentions)",
   "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/: README.md, [name]-ap-brainlift.md, [name]-bespoke-mastery-assessments.md, [name]-alphatok-guide.md, pritish-13-criterion-eval-framework.md, [name]-BRI-tiktok-directive.md (all in full); [name]-how-to-write-a-course-brainlift.md (lines 9-82); peter-9-12-social-studies.md and [name]-rethinking-hs-course-design.md (SPOVs, key sections, keyword search)",
   "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/: README.md; validity/00_AUDITS_AND_FIXES.md, 05_LIMITATIONS.md, 02_ITEM_BANK.md (full); 00_BRAINLIFT.md (SPOVs, insights, dropped approaches); 00_CASE_FOR_APPROVAL.md (sections on population and adoption); 06_SOURCES.md (part); 01_PSYCHOMETRIC_DESIGN, 03_SIMULATION_EVIDENCE, 04_CONCURRENT_VALIDITY_PLAN, MAP_PROXY_VALIDITY_CASE (keyword search for findings); reference/CAT_MAP_EXAM_SPEC.md (sections 7, 9.3, 10-12); red-team/README.md, RED_TEAM_FINDINGS.md, RECHECK_FINDINGS.md",
   "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/ (all three files)",
   "~/Projects/grade3-reading/artifacts/wiki-research/hub-review-model.md (full)",
   "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/: BUILD_FACTS.md, feedback_clean.md, qc_sample.json, feedback_wire_report.json (full); package/RED_TEAM_FINDINGS.json (summary and first attacks); g5_analysis_digest.md (headings and keyword search)",
   "Beyond the computed scope, because the user asked to dig into anything AP: ~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/ (review/start-here.md, review/evidence/case-for-review.md, review/evidence/incept-acceptance.json, source/sealed-authoring/README.md, authoring/apush/docs/FULL-COURSE-AUTHORING-STATUS.md, review history notes, prompts/u04.md, lesson-spec.json structure, canonical/unit2/lesson-01.json and assessment-set.json design fields)"
  ],
  "skipped": [
   "APinceptbench/.env, .env.example and .claude/settings.local.json: credential and config files, excluded by the rules",
   "APinceptbench/.venv and __pycache__: environment, not documents",
   "APinceptbench data/*.json beyond the first records, and git-history latest_run_failures.json and run7_failures_archive.json: data dumps",
   "APinceptbench core/orchestrator.py, pipeline.py, evaluator.py, prompt formatters, report generators and ap_benchmark/tests: code with no documented findings beyond the pass logic already read",
   "Downloads unit-N-ap*-benchmark.jsonl beyond one or two records each: data dumps; the records are generation requests with no quality fields",
   "Raw output and source-text sheets of the Knowledge Schema Generator workbooks (Fact Gen, Mapping, Overlay, AMSCO/Heimler/Princeton/Henretta/Exam): data; tallied by column only",
   "Other incept-package-hub hits: the 'AP' matches were 'MAP-' substrings; .worktrees, .claude/worktrees and website/.next are duplicate copies",
   "map-proxy approval-package/ (sign-off, consent, routing spec, approval email, screenshots): organisational; red-team RED_TEAM_RESPONSE, PROTEST_BRIEF, ADDRESS_STATUS and the other RECHECK_* files: responses to findings already read; skill/SKILL.md; validity/figures PNGs",
   "g5_build meeting_clean.md (meeting notes, organisational), approval_clean.md, mapproxy_clean.md and doc_chunks/ (copies of approval and map-proxy documents), lessons/*.json, pp9802_raw_snapshot.json, feedback_authored_772.json, qc_bundle.json (data), [name]_v2_*.json (data with name-bearing filenames), package/G5_*.md (not reached; the red-team JSON was read instead)",
   "team-direction research file 03 is mostly organisational (teams and people); only one design rule from it was used"
  ],
  "notes": "Every file in hs-civics/reference except README.md is named after a person (eight files, not one); every candidate relying on them has name_bearing_source true, and their mentions in 'against' fields are marked name-bearing. The APUSH benchmark .jsonl files are generation requests ({grade, subject, type, difficulty, quantity, skills{lesson_title, substandard_id, substandard_description}}). They have no quality fields, the 'grade' field holds the unit number, and 'substandard_description' holds the learning objective rather than the specific fact. Counts in the spreadsheet-based candidates (overlap 857/1,356, 160 of 2,087 links rejected, 1,163 vs 370 label agreement, comment-category tallies) are my own tallies of the project's columns, not numbers written in the files. Cross-document inconsistencies in the AP benchmark: the pass threshold is 0.85 in its docs and scorer ('fixed, never changes') but 0.70 in the live code. The judge prompt lists critical dimensions that the code doesn't block on. The two reports called 'Run 1' are different run IDs (0.0% and 30.7%). The judge's cognitive-demand rule was relaxed (version 2026.02.24.1) on the same day as the 'recovery' run. Everything was read-only; no mgr or ledger commands were run, because the task forbids writes."
 },
 "candidates": [
  {
   "statement": "Some item formats can only test recall whatever the difficulty setting, so choose the format to fit the thinking the objective asks for and keep recall-only formats away from objectives that ask for explanation.",
   "kind": "measured",
   "found_by": "Across seven benchmark runs a model judge scored generated items. Single-blank fill-in items failed the cognitive-demand check far more often than other formats (38% average pass; 90% failed cognitive demand in one run), and generator changes between runs did not lift them.",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN6_REPORT.md",
     "lines": "105",
     "quote": "**90% of fill-in questions fail cognitive demand.** The format is fundamentally incompatible with AP-level analytical requirements."
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md",
     "lines": "112",
     "quote": "**Root cause:** Fill-in-blank format inherently tests recall. Even with correct curriculum alignment, the question format prevents testing higher-order thinking."
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md",
     "lines": "107",
     "quote": "| fill-in | 66% | 50% | **21%** | 25% | 23% | 45% | **38%** |"
    }
   ],
   "against": "All verdicts came from one model judge whose cognitive-demand rule was relaxed partway through the series: 'PROMPT_VERSION = \"2026.02.24.1\"  # Relaxed cognitive demand - recall is OK' (~/Documents/APinceptbench/ap_benchmark/prompts/base.py line 15). A name-bearing course-design file argues that the line to police is recall versus inference, not format: 'The distinction to enforce is not \"MCQ vs constructed response\" but \"recall vs inference\" — regardless of item format.' (~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/peter-9-12-social-studies.md line 207).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make a harder item demand more reasoning, not harder words or more context in the stem; extra explanation in the stem made items easier.",
   "kind": "measured",
   "found_by": "Generated items were requested at three difficulty levels. The judge repeatedly failed 'hard' items as too easy because the writer raised the vocabulary or added scaffolding instead of reasoning demand; hard items passed 38% in one run.",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_FAILURE_REPORT.md",
     "lines": "211",
     "quote": "- Difficulty should affect cognitive demand, not just vocabulary"
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN3_REPORT.md",
     "lines": "80",
     "quote": "- Difficulty adjustment only changes vocabulary complexity, not cognitive demand"
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN5_REPORT.md",
     "lines": "114",
     "quote": "**Pattern:** The endpoint adds too much context/scaffolding, which paradoxically makes hard questions easier to answer."
    }
   ],
   "against": "The difficulty verdicts were a model judge's opinion, with no learner data, and the pattern swung between runs: '**Key observation:** Run 5 fixed easy difficulty (27% → 68%) but broke hard difficulty (58% → 38%) and cognitive demand (70% → 59%).' (~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN5_REPORT.md line 32).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Treat any difficulty label, whether a writer, a judge or a person assigned it, as a guess until learners have answered the item, and recalibrate it from their responses.",
   "kind": "measured",
   "found_by": "An adaptive test's whole bank of 650 items carried hand-assigned difficulties with no response data, recorded as unknown until field calibration. In the generated-item benchmark, 'hard' items failed more often than 'easy' ones in one run.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/05_LIMITATIONS.md",
     "lines": "11",
     "quote": "This means we do not know how hard any individual item actually is for students."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
     "lines": "39",
     "quote": "the 161–220 figures above are authoring band labels, not measured difficulty."
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN5_REPORT.md",
     "lines": "46",
     "quote": "**Problem:** Hard questions now fail MORE than easy questions. This suggests:"
    }
   ],
   "against": "Simulation suggests a well-built adaptive engine tolerates the guess: 'Simulation 3 shows the engine tolerates this at the expected σ ≈ 0.5–1.0 logits level (reliability ≥ 0.85 maintained) [SIMULATION], but precision is below what it will be post-calibration.' (05_LIMITATIONS.md line 14).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Give the writer the exact statement and objective an item must test, not just its topic, and check that the item tests that statement; a writer given a topic writes generic items about it.",
   "kind": "measured",
   "found_by": "The first benchmark run passed 30.7% of generated items, mainly because the generator ignored the specific objective and statement it was sent. Once it used them, alignment rose from 43.0% to 88.9% and the pass rate to 65.0%. The benchmark request files in Downloads carry only the objective text in 'substandard_description', not the specific fact.",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_FAILURE_REPORT.md",
     "lines": "33",
     "quote": "The generator ignores the specific `learning_objective` and `statement` provided in the request. Instead, it produces generic questions about the broad topic area."
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md",
     "lines": "30",
     "quote": "The dramatic improvement in curriculum alignment (43% → 89%) confirms the endpoint is now properly utilizing the `learning_objective` and `statement` fields provided in requests."
    },
    {
     "path": "~/Documents/APinceptbench/docs/GENERATOR_API_SPEC.md",
     "lines": "123",
     "quote": "- A student who knows this fact MUST be able to answer the question correctly"
    }
   ],
   "against": "Even with the statement, the writer still strayed beyond it: '- Scope expansion beyond provided curriculum (e.g., adding Syria/Libya when curriculum specifies Iraq/Afghanistan only)' (~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md line 60).",
   "adds_to_existing": [
    57,
    58
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check in code that an item has the requested format and all its parts before any judge reads it, and give each kind of fault its own check, because a judge files a structural fault under whichever dimension is nearest.",
   "kind": "measured",
   "found_by": "One generator release returned multiple-choice items when blanks and matching items were requested. The model judge recorded most of this as alignment failures and also failed factual accuracy because parts were missing. In a later 947-item run, the judge filed a stimulus dated outside the item's stated period as a factual error, which is a blocking fail (evaluation_20260225 report line 191). A separate test bank made format compliance a hard gate.",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "24",
     "quote": "**15 out of 26 curriculum alignment failures (58%) are due to FORMAT MISMATCH.**"
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "139-140",
     "quote": "factual_accuracy: \"Cannot verify factual accuracy because the actual answer choices are missing\""
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
     "lines": "245",
     "quote": "| Dim 13: Format compliance | Item structure matches format token (MCQ/MSQ/EBSR/hot-text/sequence/gap-match) | Hard gate |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    67,
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make every check the rubric calls critical block an item on its own; when only some blocked and the rest were averaged, nearly all items passed while most failed a check the rubric called critical.",
   "kind": "measured",
   "found_by": "In a 947-item benchmark, the judge's prompt listed source authenticity and attribution among the critical dimensions for document-based items. The pass code blocked on four other dimensions only and averaged the rest against a 0.70 bar (~/Documents/APinceptbench/benchmark_official.py lines 194-214).",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/evaluation_20260225_081919_0909a798.md",
     "lines": "34",
     "quote": "| DBQ      |    186 |      5 |      0 |     97.4% |      0.87 |"
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/evaluation_20260225_081919_0909a798.md",
     "lines": "82",
     "quote": "| document_authenticity     |   28 |  163 |     14.7% |      0.15 |"
    },
    {
     "path": "~/Documents/APinceptbench/ap_benchmark/prompts/official_ap_prompts.py",
     "lines": "315, 321-323",
     "quote": "- Does each document have proper attribution (author, date, source)?"
    }
   ],
   "against": "The check also accepted simulated documents ('- Are documents historically accurate or properly simulated?', official_ap_prompts.py line 322), and the commonest recorded issue was missing attribution ('- (8x) Document 1 lacks specific attribution (author, date, source)', evaluation report line 63). Part of the failure rate may therefore be attribution format rather than invented sources.",
   "adds_to_existing": [
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check that a rubric's rules can all be met at once; when one rule defined easy items as recall and another failed any item that only tested recall, easy items failed whatever they did.",
   "kind": "measured",
   "found_by": "In one block of context, the judge was told that easy items should test recall and that items must not just test factual recall. In a later run, 26 of 37 easy items failed cognitive demand (~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md line 80).",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/ap_benchmark/core/curriculum.py",
     "lines": "323",
     "quote": "\"easy\": \"Should test basic recall and comprehension of key concepts\","
    },
    {
     "path": "~/Documents/APinceptbench/ap_benchmark/core/curriculum.py",
     "lines": "351",
     "quote": "lines.append(\"  - Questions should test historical thinking, not just factual recall\")"
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN3_REPORT.md",
     "lines": "63",
     "quote": "- Result: Questions are either too simple (cognitive fail) or too complex (difficulty fail)"
    }
   ],
   "against": "The conflict was resolved by relaxing the judge mid-series rather than by fixing the rule ('- Recall and memorization questions ARE ACCEPTABLE', ~/Documents/APinceptbench/ap_benchmark/prompts/base.py line 88), so runs before and after the change are not comparable.",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Derive every count and structural rule from one named source and re-derive it before publishing, because the same quantity stated differently across documents was a recurring and damaging review finding.",
   "kind": "measured",
   "found_by": "Audits and reviews of three course and test packages found counts that disagreed between documents (lessons, items, cohort sizes) and a table that did not sum. One benchmark's own docs stated the item-set rule three ways: exactly 3 questions, 3-4 (AP_GENERATOR_SPEC.md line 44) and 2-3 (GENERATOR_INPUTS.md line 36). A hostile review of another package rated four incompatible enumerations of its core sequence as fatal.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "11",
     "quote": "| 3 | The item-bank source table summed to 520 while claiming 650 | Replaced with the verified 13-file breakdown; the fixtures were counted programmatically and sum to exactly 650 |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "111",
     "quote": "The email says 52 lessons, 745 items and 56 cold passages; the infographic says 47 lessons and 713 graded items; and the “45 instructional tests” are tests, not instruction. The course’s own materials disagree with each other."
    },
    {
     "path": "~/Documents/APinceptbench/docs/EVALUATION_API.md",
     "lines": "286",
     "quote": "- ✅ `questions` - Required, must have **exactly 3** questions"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give a matching item more answers than prompts, or some other guard against elimination, because equal one-to-one lists let the last pairs be solved by elimination.",
   "kind": "measured",
   "found_by": "Matching items never passed more than 55% in any of seven benchmark runs. The judge's recurring reason was equal one-to-one lists with no extra options.",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md",
     "lines": "390",
     "quote": "- 1:1 format eliminates analytical challenge"
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md",
     "lines": "391",
     "quote": "- No distractors = simple elimination"
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN7_REPORT.md",
     "lines": "119-120",
     "quote": "The 1:1 matching format with no distractors makes this more of a medium difficulty question despite being marked as hard"
    }
   ],
   "against": "A shipped platform's guide prescribes the opposite for its match tasks: '- Include 4-6 objects, with no distractor items.' (~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md line 227, name-bearing). The same guide's cloze rule is '- Do include distractor words that are unused.' (line 221).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A fill-in or short-answer item must admit only one answer and say what kind and size of answer is wanted.",
   "kind": "measured",
   "found_by": "After a generator release, fill-in items began failing clarity because blanks allowed several answers at different levels of detail. The run report then set rules for one answer per blank and a stated level of detail.",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "93",
     "quote": "**New clarity failures:** Fill-in blanks are ambiguous about expected answers."
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "260",
     "quote": "1. Each blank should have ONE clear correct answer"
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "261",
     "quote": "2. Specify expected granularity (term, phrase, concept)"
    }
   ],
   "against": "The judge also penalized the obvious fix of listing accepted answers: 'Providing multiple pre-written acceptable answers reduces it to pattern matching rather than requiring critical thinking' (~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN6_REPORT.md lines 115-116).",
   "adds_to_existing": [
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make every option alike in length, grammar and qualification so that none can be chosen or ruled out by its form alone.",
   "kind": "adopted rule",
   "found_by": "A generated-item spec and the rule a review team stated for closed-response items.",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/AP_GENERATOR_SPEC.md",
     "lines": "29",
     "quote": "**Rules**: 4 options, 1 correct, plausible distractors, parallel structure, no absolutes"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
     "lines": "34",
     "quote": "Closed-response items must require the target reasoning and must not be answerable by surface cues, keyword matching, option length, or test-wise elimination."
    }
   ],
   "against": "A fixed word list is blunt. The benchmark's pre-judge regex fails any option containing words such as 'only', 'complete' or 'immediately' (~/Documents/APinceptbench/ap_benchmark/hard_fail/rules.py lines 30-41), while the judge's own rule allows absolutes when accurate: '5. Avoid absolute language (\"always\", \"never\", \"all\", \"none\") unless historically accurate' (official_ap_prompts.py line 34).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Build each wrong option from a named, predictable error and record which error it targets, instead of writing random plausible-but-wrong answers.",
   "kind": "adopted rule",
   "found_by": "A test bank's spec requires each multiple-choice item to have one distractor of each of four named error types and a recorded misconception per wrong option. A generated-item contract requires misconception-based distractors, and the items that passed a benchmark were those whose distractors represented real misconceptions (BENCHMARK_FAILURE_REPORT.md line 227).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md",
     "lines": "356",
     "quote": "`options[i].misconception` field required on all non-key options."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md",
     "lines": "351",
     "quote": "- **Scope error** — true detail presented at wrong granularity"
    },
    {
     "path": "~/Documents/APinceptbench/docs/GENERATOR_API_SPEC.md",
     "lines": "173",
     "quote": "- Distractors MUST represent plausible student misconceptions, not absurd options"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check that every item can be answered by someone who learned the target content and needs nothing beyond it.",
   "kind": "adopted rule",
   "found_by": "A generator contract written after the first benchmark runs, and a judge rubric that fails any part needing obscure knowledge.",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/GENERATOR_API_SPEC.md",
     "lines": "123",
     "quote": "- A student who knows this fact MUST be able to answer the question correctly"
    },
    {
     "path": "~/Documents/APinceptbench/docs/GENERATOR_API_SPEC.md",
     "lines": "124",
     "quote": "- The question MUST NOT require knowledge outside the scope of this fact (except for scaffolding context)"
    },
    {
     "path": "~/Documents/APinceptbench/ap_benchmark/prompts/official_ap_prompts.py",
     "lines": "239",
     "quote": "- FAIL if parts require obscure knowledge"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make each part of a question ask for one thing, and make its declared skill and its scoring guide match what the stem actually asks.",
   "kind": "measured",
   "found_by": "The judge in the 947-item benchmark flagged essay prompts whose declared reasoning type did not match what the prompt asked. The evaluation contract bans compound tasks within one part.",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/evaluation_20260225_081919_0909a798.md",
     "lines": "54",
     "quote": "- (2x) Mismatch between stated reasoning type (causation) and actual prompt structure (..."
    },
    {
     "path": "~/Documents/APinceptbench/docs/EVALUATION_API.md",
     "lines": "328",
     "quote": "- **NEVER** use compound verbs like \"identify AND describe\" in a single part"
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
   "statement": "Keep items that share a source independent, so that no item reveals another's answer and each part can be scored on its own.",
   "kind": "adopted rule",
   "found_by": "Generator and judge rules for item sets that share one stimulus, and for multi-part short-answer items.",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/AP_GENERATOR_SPEC.md",
     "lines": "44",
     "quote": "**Rules**: 3-4 questions, different skills, independent answers"
    },
    {
     "path": "~/Documents/APinceptbench/ap_benchmark/prompts/official_ap_prompts.py",
     "lines": "229",
     "quote": "- Are parts logically connected but independently scorable?"
    }
   ],
   "against": "The same project's generator contract also demands dependence: '- Parts MUST be scaffolded (build on each other OR test related aspects)' (~/Documents/APinceptbench/docs/GENERATOR_API_SPEC.md line 239).",
   "adds_to_existing": [
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge content with a model or person independent of its maker, and change the judge only on its accuracy against labelled cases, never to move the pass rate.",
   "kind": "adopted rule",
   "found_by": "The independence principle the benchmark stated for its model judge.",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/EVALUATION_PROCESS.md",
     "lines": "5",
     "quote": "It uses Claude API (not the same model as the generator) to ensure impartial evaluation."
    },
    {
     "path": "~/Documents/APinceptbench/docs/EVALUATION_PROCESS.md",
     "lines": "158",
     "quote": "- Evaluator criteria should NOT be influenced by generator output"
    },
    {
     "path": "~/Documents/APinceptbench/docs/EVALUATION_PROCESS.md",
     "lines": "159",
     "quote": "- Changes to evaluator based on benchmark accuracy, not pass rate"
    }
   ],
   "against": "The project broke its own rule. The judge's rubric was relaxed mid-series with no recorded accuracy check ('PROMPT_VERSION = \"2026.02.24.1\"  # Relaxed cognitive demand - recall is OK', ap_benchmark/prompts/base.py line 15). The calibration set the judge would be checked against uses a different threshold from the live 0.70 rule ('\"pass_threshold\": 0.85,', ap_benchmark/calibration/gold_standard.json line 4) and holds only 25 multiple-choice and multi-select cases.",
   "adds_to_existing": [
    37,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Does a calibration set built from blatant faults show that a judge will catch the subtle faults that actually occur?",
   "kind": "open question",
   "found_by": "The judge's 25-case calibration set uses blatant faults, such as date-recall questions and gross factual errors. The failures found in live runs were subtler: misdated events and oversimplifications.",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/ap_benchmark/calibration/gold_standard.json",
     "lines": "194",
     "quote": "Recall-only question - just asks for a date without any analysis"
    },
    {
     "path": "~/Documents/APinceptbench/ap_benchmark/calibration/gold_standard.json",
     "lines": "403",
     "quote": "Factual error: Midway was in the Pacific against Japan, not the Atlantic against Germany"
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md",
     "lines": "87",
     "quote": "1. **Temporal confusion** - Misattributing events to wrong time periods"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    37,
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't reroute or redesign on pass rates from a handful of items, and report the count beside every rate, because rates from small groups swung widely between runs.",
   "kind": "measured",
   "found_by": "Run reports set format-routing rules from format-by-difficulty cells of 4 to 15 items. The same cell read 15% in one run (13 items) and 64% two runs later.",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN3_REPORT.md",
     "lines": "35",
     "quote": "1. **Match + Easy = 15%** - Catastrophic failure rate"
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN5_REPORT.md",
     "lines": "58",
     "quote": "| **Match** | 64% | 55% | 38% |"
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN5_REPORT.md",
     "lines": "63",
     "quote": "2. **MCQ + Medium: 83%** (5/6) - Strong"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    15,
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Compare runs format by format and level by level, because a change in the mix of item types moves the overall pass rate without any change in quality.",
   "kind": "measured",
   "found_by": "Removing one weak format moved a run's pass rate from 49.4% to 66.1%. The number of fill-in items per run ranged from 20 to 39, so the overall rate moved with the mix.",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN8_REPORT.md",
     "lines": "137",
     "quote": "| Pass Rate | 49.4% | **66.1%** |"
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md",
     "lines": "502",
     "quote": "| Run 6 | 39 | 26 | 28 | 23 | 116 |"
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md",
     "lines": "503",
     "quote": "| Run 7 | 20 | 33 | 34 | 29 | 116 |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Expect knowledge drafted from several sources to repeat itself, and remove repeats across the whole course before human review, since repeats were still the commonest review note.",
   "kind": "measured",
   "found_by": "These are my own counts from the project's audit columns. In one unit's consolidation audit, 857 of 1,356 drafted facts are marked 'Yes' under 'Overlap Notes'. Human checks of 2,087 generated links across nine units marked 160 'No', and the commonest notes were 'already covered' (23) and 'already mentioned' (17). The pipeline added a redundancy pass before human review.",
   "evidence": [
    {
     "path": "~/Downloads/Knowledge Schema Generator - AP USH Unit 2.xlsx",
     "lines": "sheet '4. Consolidation Audit' (xl/worksheets/sheet10.xml), row 2, column J ('Overlap Notes')",
     "quote": "Yes - Related to AMSCO_2_RP_IVxj; this adds detail to the English focus on land acquisition for agriculture."
    },
    {
     "path": "~/Downloads/Knowledge Schema Generator - AP USH Unit 2.xlsx",
     "lines": "sheet 'Instructions' (xl/worksheets/sheet1.xml), cell B2, step 14",
     "quote": "14. Run step 8 in main.py which will go through the current topic's facts and check for redundancies against previously processed topics in the unit."
    },
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 3 Relationships', rows 14 and 20, column J (Notes; Keep = 'No')",
     "quote": "already covered"
    }
   ],
   "against": "Overlap varies by unit: in the UNIT 7 workbook's '4. All Consolidation Audits' sheet, 109 of 597 rows are marked Yes under 'Overlap Notes' (my count).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check where each generated fact belongs (its scope, its period and the specific standard it serves), not only whether it is true, since misplacement was the commonest human-review note.",
   "kind": "measured",
   "found_by": "This is my keyword tally of the 160 human comments on 1,635 generated knowledge nodes. About 39 concern the wrong unit, period or standard; 30 content already covered elsewhere; 20 length; 13 unclear wording or missing context; and one questions the evidence for a fact. Recorded actions were 49 removals, 48 edits, 14 additions and about 20 moves.",
   "evidence": [
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 1 Nodes', row 10, column M (Comment/Reason); column N reads 'Removed'",
     "quote": "Out of time frame for this course"
    },
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 9 Nodes', rows 109-112, column M; column N reads 'Removed standard mapping'",
     "quote": "Tricky, because these are significant events but they align with the overall learning objective rather than a specific standard"
    },
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 6 Nodes', row 202, column M",
     "quote": "This sentence is true but does not get to the heart of the divisions that occurred in the gilded age."
    }
   ],
   "against": "The tally comes from keywords in free-text comments, not from a coded field, so the categories overlap.",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep each knowledge statement short and about one idea, since over-long generated statements were trimmed and combined ones split during human review.",
   "kind": "measured",
   "found_by": "In human checks of generated knowledge nodes, about 20 of 160 comments record trimming an over-long statement (the original kept as 'og'), and three record splitting one fact into two.",
   "evidence": [
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 3 Nodes', row 151, column M; column N reads 'Edited'",
     "quote": "og (too long) - In 1794, the Whiskey Rebellion occurred when western Pennsylvania farmers protested Alexander Hamilton's excise tax on whiskey;"
    },
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 3 Nodes', rows 152, 155 and 157, column M",
     "quote": "manual add - split the previous fact into two"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When content links two facts, check the stated kind of link (cause, enabling condition or example) on its own, because related facts were often given the wrong kind of link.",
   "kind": "measured",
   "found_by": "These are my counts from human checks of 2,087 model-generated links between knowledge nodes. The rejection rate by stated type ran from 4.2% for 'causes' (6 of 143) to 9.1% for 'exemplifies' (76 of 833).",
   "evidence": [
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 3 Relationships', row 74, column J (type 'enables', Keep 'No')",
     "quote": "The description is an over simplification of the two statements. Locke's ideas didn't necessarily enable the ideological shift--rather it inspired and gave language to republican principles of self governances."
    },
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 1 Relationships', row 134, column J (type 'exemplifies', Keep 'No')",
     "quote": "the trade networks don't exemplify how they adapted to their environments."
    },
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 1 Relationships', row 100, column J (type 'exemplifies', Keep 'No')",
     "quote": "this fits with the source statement but doesn't fit with the target statement"
    }
   ],
   "against": "Most generated links were kept: 160 of 2,087 were marked 'No' (my count from the 'Keep' column).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check a model's labels of which facts are essential against human judgment before they decide what is taught or tested, since they differed on about a quarter of facts, mostly by over-rating.",
   "kind": "measured",
   "found_by": "These are my counts across the nine 'Unit N Nodes' sheets. The generator's essential/supporting label and the human-set level agree on 1,163 nodes and differ on 370; 222 nodes labelled 'essential' were set to 'supporting', and 139 went the other way.",
   "evidence": [
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 1 Nodes', row 1, column D (generator label)",
     "quote": "Classification"
    },
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 1 Nodes', row 1, column L (human-set level)",
     "quote": "Essential/Supporting/Nuanced detail"
    }
   ],
   "against": "Nothing records whether the human level was set before or after the person saw the model's label, so the agreement figure may be inflated.",
   "adds_to_existing": [
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat content produced while a check was out of service as never checked, and replace or re-check all of it before use.",
   "kind": "measured",
   "found_by": "A test bank's quality-check service went down while items were being written. A red team flagged those items, and all 32 were replaced rather than re-trusted.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
     "lines": "313",
     "quote": "The 32 G2 match/sequence items authored during the June-2026 quality-check service outage passed through no trustworthy gate."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/05_LIMITATIONS.md",
     "lines": "77",
     "quote": "The G2 match/sequence items originally authored during the June-2026 quality-check outage were **replaced 2026-07-07** with items quality-scored 1.0 by the healthy-period checker (engine PRs #64/#65; swap table in the engine repo)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    28,
    36
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Report every result as measured, misses included, in every summary: never round a near miss up to a pass or leave the failing metric out.",
   "kind": "measured",
   "found_by": "Adversarial audits of an assessment's validity package found a reliability figure rounded up to meet its target, and the one failing metric missing from every summary table.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "9",
     "quote": "| 1 | Summary tables reported reliability as \"0.930 ✅\" against a ≥0.93 benchmark the underlying reports state as 0.928, below |"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "10",
     "quote": "| 2 | The one failing metric (RMSE 4.12 vs <4.0 target) was omitted from every summary table |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/BUILD_FACTS.md",
     "lines": "28",
     "quote": "Verdicts are **PASS-with-named-gaps**, never bare PASS."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Validate on the production path with the full bank and the full range of learners the claim covers, because a simplified run hid a bias and an error regression.",
   "kind": "measured",
   "found_by": "An assessment's validation ran with a simplified selector and one grade's ability distribution but was described as covering all grades on production code. Re-running it on the real path surfaced a bias and a larger error.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "12",
     "quote": "| 4 | Simulations were G3-scoped (630 items, G3 prior, simplified selector) but described as \"G2–G5, production code\" |"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/05_LIMITATIONS.md",
     "lines": "134",
     "quote": "The initial-run results (r=0.948, rel=0.928, RMSE=4.12 RIT) could not expose production-path effects"
    }
   ],
   "against": "Even the full simulation is not field evidence: 'If the Rasch model is misspecified, all simulation results — including the r=0.967 theta recovery and rel=0.931 reliability — overestimate actual field performance.' (05_LIMITATIONS.md line 97).",
   "adds_to_existing": [
    24,
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Take a baseline from the full current population, one record per learner, on items that discriminate, because a convenience slice and easy items each inflated a baseline.",
   "kind": "measured",
   "found_by": "A learner baseline built from a selected slice of data (repeat records of long-enrolled learners, stale cohorts and a high-achieving import) placed the population at the 72nd percentile; the full current population sat at the 46th. Separately, an 83% accuracy baseline came from items with easy distractors.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "26",
     "quote": "| 1 | Population baseline (206.4 / 72nd pctile) is a biased slice |"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_CASE_FOR_APPROVAL.md",
     "lines": "40",
     "quote": "The old figure was not an arithmetic slip but a compound of three biases we have now quantified"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
     "lines": "86",
     "quote": "The 83% baseline is measured on the wrong test — it comes from the incumbent's easy-distractor items"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Block in code any score or claim that has not been validated yet, rather than relying on disclaimers, because documents drift and code paths don't.",
   "kind": "adopted rule",
   "found_by": "Audits found numbers drifting between an assessment's documents (0.930 vs 0.928), so the team kept its load-bearing claim limits in code. A package standard bars generated views from showing a stronger status than the record holds.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md",
     "lines": "37",
     "quote": "Pre-pilot output is logit ± SE and domain sub-scores; RIT, percentile, and CGP are **blocked in the engine**. Documents can drift; code paths don't."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md",
     "lines": "229",
     "quote": "| Approximate RIT output (200 + 10θ) pre-linking | The transformation's coefficients are exactly what the linking study estimates; emitting the approximation would be the overclaim the design exists to prevent |"
    },
    {
     "path": "~/Projects/incept-package-hub/docs/COURSE_PACKAGE_STANDARD.md",
     "lines": "203",
     "quote": "- generated UI cannot invent a stronger status than the manifest."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Tag every claim about content with the kind of evidence behind it (measured, simulated, decided, derived or asserted), and state what each count does not prove.",
   "kind": "adopted rule",
   "found_by": "Validity and course packages adopted evidence tags and 'does not prove' columns after reviews attacked their unbounded claims.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
     "lines": "256",
     "quote": "- The ≥0.85 threshold is an authoring decision, not an empirically validated cutoff [AUTHORING-DECISION]."
    },
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/docs/FULL-COURSE-AUTHORING-STATUS.md",
     "lines": "15",
     "quote": "| Measure | Complete local inventory | What the count does not prove |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/BUILD_FACTS.md",
     "lines": "31",
     "quote": "7-tag evidence provenance ([Direct-pull]/[Asserted]/[Open]/[AUTHORING-DECISION]/[DERIVED]/[ACADEMIC]/[SIMULATION] as applicable), prove/not-prove pairing."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make only the claims a sample's size can support, set pilot success criteria that size can measure, and recruit learners at both ends of the ability range on purpose, since ordinary use under-samples them.",
   "kind": "adopted rule",
   "found_by": "An assessment's pilot plan limits a roughly 40-learner pilot to usability and red-flag claims, sets kill criteria that can be measured at that size, and commits in advance to recruiting at both extremes, because adaptive selection rarely serves the extreme items.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/README.md",
     "lines": "122",
     "quote": "| Feasibility pilot | ~40 students (1–2 classes) | Usability, engagement, and early item red flags — no calibration claims at this size |"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/04_CONCURRENT_VALIDITY_PLAN.md",
     "lines": "196",
     "quote": "**Success/kill criteria (usage-based — all meaningful at N=40):** session completion ≥ 90%; session duration within the expected 30–60-minute envelope; rapid-guess rate < 10%."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "28",
     "quote": "| 3 | Natural CAT exposure under-samples tail items for calibration |"
    }
   ],
   "against": "Eight learners per extreme is not tail validation: 'is directionally right and statistically decorative; fine for feasibility, but don't let it be read as tail validation.' (~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RED_TEAM_FINDINGS.md line 59).",
   "adds_to_existing": [
    15
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When checking a measure against an established test, keep your measure from acting as practice for that test: counterbalance the order or give it afterwards.",
   "kind": "adopted rule",
   "found_by": "A red team pointed out that giving the new test days before the official one would act as practice on the very test it was being validated against. The plan was redesigned with counterbalanced order and an arm that tests only after the official test.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RED_TEAM_FINDINGS.md",
     "lines": "21",
     "quote": "rehearsal administered days before the real test is a **practice/familiarization intervention on the criterion measure**"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/04_CONCURRENT_VALIDITY_PLAN.md",
     "lines": "65",
     "quote": "All students take both tests (within 2 weeks). Order is counterbalanced to control for practice effects and fatigue:"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Record how long learners take on each item and flag rushed answers, because a disengaged attempt is not evidence of what they know.",
   "kind": "adopted rule",
   "found_by": "An assessment mirrors its reference test's rule of invalidating heavily rushed sessions. A course review found a mastery gate passed at about 20% accuracy by clicking through without reading.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md",
     "lines": "87",
     "quote": "The proxy captures per-item timing silently and flags rushing — so a disengaged student is coached before the official window, and a proxy score carries its own validity flag rather than silent noise."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "97",
     "quote": "Re-engineer the gate to block advancement on genuine misses, require reading or attention, and penalise rapid-guessing, then demonstrate it blocking a real miss in a live walkthrough."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    12
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't put a clock on a test unless speed is what it measures, because a time limit changes what is measured and rewards rapid guessing.",
   "kind": "adopted rule",
   "found_by": "An assessment dropped timed sections because the test it mirrors is untimed. A course position cites a large accuracy penalty under time pressure.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md",
     "lines": "232",
     "quote": "| Timed sections | MAP is an untimed power test; a clock changes the construct and rewards the rapid-guessing MAP penalizes |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
     "lines": "46",
     "quote": "Comprehension is untimed; speed is a different construct; time-pressure triples the on-screen accuracy penalty."
    }
   ],
   "against": "When the real exam is timed, a readiness test may be timed to mirror it: '- Add a timer for the mock exam (to mirror AP-exams) and resolve the multi-part FRQ issue for AP-assessments.' (~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md line 27, name-bearing).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Let learners practise the formats and interactions of the test that counts before it counts, because meeting an interface for the first time on the scored test adds noise to the score.",
   "kind": "adopted rule",
   "found_by": "Learners had practised only single-select items, so they met multi-select and two-part items for the first time on the scored external test.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md",
     "lines": "55",
     "quote": "Alpha students practice on 100% MCQ material; their first multi-select or two-part evidence item is on the scored official MAP. Interface novelty is construct-irrelevant variance (AERA/APA/NCME Standard 1.13)."
    }
   ],
   "against": "The benefit was later bounded: '| 11 | Format-familiarization benefit implied for all six formats | **Bounded** — one-line scope added: strongest for the 3 Reading-2–5-confirmed formats; the other 3 are low-harm additional practice |' (validity/00_AUDITS_AND_FIXES.md line 36). A red team noted that 'if familiarity moves scores at all, it moves the official ones.' (red-team/RED_TEAM_FINDINGS.md line 21).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep test items out of practice and behind access control, and track how often a learner meets the same item again, because items seen before make a test a weaker measure.",
   "kind": "measured",
   "found_by": "An assessment's public test page let anyone harvest the item bank, and repeat sittings shared 29.4% of items on average. A course's learner build keeps all test material and retry-only sources out.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "18",
     "quote": "| 10 | The public no-login test URL allows anonymous farming of the item bank |"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/05_LIMITATIONS.md",
     "lines": "118",
     "quote": "- Item security is weaker: students who take the test multiple times will see repeated items (mean pairwise between-session overlap 29.4%)"
    },
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/review/history/2026-07-27-review-preparation-projections.md",
     "lines": "17-18",
     "quote": "All 120 assessment candidates and 182 assessment/retry-only sources remain out of the learner projection."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "After a wrong answer, teach the failed step and retry on a parallel item that uses different evidence, rather than repeating the same item.",
   "kind": "adopted rule",
   "found_by": "A course's assessment design sends each learner's first failed step to a taught check and then to a parallel retry that uses different evidence.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/assessment-set.json",
     "lines": "26",
     "quote": "Score atomically, record the first failed historical function, teach through its resolved local check, and administer its parallel retry with different evidence before reassessment."
    },
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/review/evidence/incept-acceptance.json",
     "lines": "37",
     "quote": "Unit 1 exposes targeted feedback, correction, and different-evidence retry."
    }
   ],
   "against": "One platform reuses the same item in instruction and review and accepts the cue risk: 'This is a medium-to-low-priority concern, in part because courses typically have a large deck of questions in rotation.' (~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md line 195, name-bearing).",
   "adds_to_existing": [
    4,
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Release independent practice only after the worked model is removed, and base it on material that neither the model nor the guided practice used.",
   "kind": "adopted rule",
   "found_by": "Reviewers found a lesson routine whose model revealed the answer and whose independent step switched to a different skill. A course spec then made independent work release only after the model is removed, and only on material the model had not covered.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/lesson-01.json",
     "lines": "127",
     "quote": "Release only after the worked model and its completed analysis are removed."
    },
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/lesson-01.json",
     "lines": "128",
     "quote": "The model uses a cross-period timeline and the guided task uses an imperial comparison; independent work shifts to a regional matrix that has not been modeled."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
     "lines": "26",
     "quote": "The I-do/we-do/you-do routine is misapplied: I-do reveals the answer instead of modeling thought; we-do is only a hint; you-do sometimes switches to a different skill."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Let taught knowledge recur and build across lessons and in-lesson checks, and keep unseen material for tests and transfer items, because the same overlap is teaching in one place and a leak in the other.",
   "kind": "adopted rule",
   "found_by": "A course review found that keeping every assessment text unrelated to the taught topics also stopped knowledge from building. A later analysis, after five adversarial rounds, found that the same overlap is correct in a knowledge check and a leak in a transfer item.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "45",
     "quote": "***To change this:*** Sequence the learning texts so taught knowledge recurs and compounds, and reserve cold, non-overlapping passages for the test only, where that property belongs."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "43",
     "quote": "by design ensures assessment passages never overlap taught topics so a student “can’t pass on recall.”"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
     "lines": "66",
     "quote": "Whether dose-item overlap is teaching or leaking depends on item class — the same overlap is legitimate in an in-lesson knowledge check and a leak in a comprehension/transfer item"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48,
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Report how many learners actually used and finished the material beside any accuracy figure, because accuracy measured only on finishers, or reach measured by distribution, hides non-use.",
   "kind": "measured",
   "found_by": "Learners on an incumbent course finished a median 12.5% of the intended work, but its sub-skill accuracy was measured only on those who completed items. A test that was distributed in the platform produced 18 results, from at most one real learner.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
     "lines": "72",
     "quote": "the 39–48% sub-skill numbers are measured only on students who *did* complete items, so the 12.5% completion floor is a worse problem than the skill gap."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_CASE_FOR_APPROVAL.md",
     "lines": "152",
     "quote": "an instrument that was distributed in the platform and produced no actionable output went unused (18 results, at most one real student)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    51
   ],
   "name_bearing_source": false
  },
  {
   "statement": "If correcting a wrong answer needs more teaching than the lesson gave, fix the item or where it sits rather than lengthening the feedback.",
   "kind": "adopted rule",
   "found_by": "A teaching-skill rule adopted from a practice framework used by the review team.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
     "lines": "52",
     "quote": "If the feedback needed to correct a response is longer and more complex than the original instruction, the ITEM has crossed the acquisition boundary — fix the item or the placement, not the feedback."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When many learners fail at the same point, treat it as a fault in the instruction and fix it there, keeping remediation for individual slips.",
   "kind": "adopted rule",
   "found_by": "The remediation design in one platform guide, and a course design note.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
     "lines": "291",
     "quote": "If many learners frequently fail at the same point in a course, the instruction itself has failed, not the learner."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/peter-9-12-social-studies.md",
     "lines": "154",
     "quote": "- Quality assurance for the course itself (if students can't pass, the course didn't work)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    60
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Teach every new step before it appears inside a worked example, and check that no lesson leans on an idea not yet taught.",
   "kind": "adopted rule",
   "found_by": "A reviewer finding on a shipped course, recorded as a gradual-release rule.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
     "lines": "54",
     "quote": "Worked examples assemble the known — a novel step must be taught before it appears inside one."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40,
    20
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give every activity a stated rationale: the knowledge it targets, the failure it guards against, why this activity, and when its scaffold comes off.",
   "kind": "adopted rule",
   "found_by": "One of the operating rules a review team attached to its feedback as the standard.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
     "lines": "36",
     "quote": "Any activity needs a rationale: target knowledge type, performance, failure mode it protects against, why this activity, and scaffold retirement condition."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Give each key term one wording and use it verbatim wherever it appears: explanation, check, summary and review.",
   "kind": "adopted rule",
   "found_by": "The design discipline of an incumbent course, recorded in a comparison note.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/03-other-teams-and-alpharead.md",
     "lines": "43",
     "quote": "every key term has ONE wording, propagated verbatim across the video, the CFU, the knowledge organiser, and the FSRS card"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Choose texts for the knowledge sequence, genre balance and quality the course needs, not by a readability score alone.",
   "kind": "adopted rule",
   "found_by": "A course review found texts chosen mainly by a readability measure, which left whole genres out and fell short of the course's own balance target.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "51",
     "quote": "Lexile alone also mishandles poetry and narrative and cannot tell you whether a text is worth reading."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "53",
     "quote": "***To change this:*** Choose texts for a coherent knowledge sequence and a genre balance that includes poetry, drama and more literary work, and judge complexity qualitatively as well as by Lexile."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Build practice up to the length and load of the target performance, because mastering only short pieces does not prepare learners for sustained work.",
   "kind": "adopted rule",
   "found_by": "A course review found every text between 58 and 217 words long, while the target test uses long and paired texts.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "69",
     "quote": "A child can master the whole course one short snippet at a time and never once sustain attention across a multi-passage block."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "71",
     "quote": "***To change this:*** Add longer passages and paired-text sets that build toward test-length and real-world reading."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Award progress or points only for verified learning, never for time spent, navigation, reading or revealing answers.",
   "kind": "adopted rule",
   "found_by": "A course review earned a mastery stamp at about 20% accuracy by clicking through. A later course package awards nothing for time, reading, navigation or answer reveals.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/review/evidence/incept-acceptance.json",
     "lines": "57",
     "quote": "Candidate items, time, reading, voice, reviewer navigation, and answer reveal award 0 XP; production XP integration is not implemented."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "95",
     "quote": "In a hands-on walkthrough one of us earned a stamp on “The Amazing Axolotl” at about 20 percent accuracy by clicking through without reading, then advanced with the passage hidden from view."
    }
   ],
   "against": "Another release ties points to focused time at a successful finish: 'Preview XP is calculated once at a successful lesson finish from whole focused minutes at one XP per minute' (~/Projects/grade3-reading/artifacts/wiki-research/hub-review-model.md lines 329-330).",
   "adds_to_existing": [
    48,
    51
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Build the learner-facing version as a separate projection that leaves out keys, rationales, rubrics, correction routes and test material, rather than hiding them in the page.",
   "kind": "adopted rule",
   "found_by": "A course package generates an answer-safe learner projection, separate from the reviewer corpus, and holds back keys until a response is submitted.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/review/evidence/case-for-review.md",
     "lines": "12-13",
     "quote": "Student projections omit assessment candidates, answer keys, rationales, rubrics, feedback, teacher-only supports, and correction routes."
    },
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/review/evidence/incept-acceptance.json",
     "lines": "81",
     "quote": "Unit 1 withholds independent and checkpoint evidence, excludes keys from student HTML, requires correction before retest, caps candidate attempts, and never unlocks on reviewer action."
    },
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/assessment-set.json",
     "lines": "18",
     "quote": "Withhold keys, rationales, lesson models, correction routes, and retries until the relevant response is submitted."
    }
   ],
   "against": "One platform stores the key in a fixed position and relies on delivery to hide it: 'where 'A' is always the correct answer since options are shuffled at delivery time.' (~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md line 197, name-bearing).",
   "adds_to_existing": [
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Test the learner's whole path at each screen size, because checks that prove page elements exist don't prove a learner can see, hear, answer, recover and finish.",
   "kind": "measured",
   "found_by": "Eight learner-facing defects shipped together behind passing element checks: narration shown as active when it wasn't, progress without a visible reward, overlapping controls, misaligned option letters, a passage below the visible screen and feedback off-screen. The release gate was rebuilt around observed behaviour at mobile and desktop sizes.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/hub-review-model.md",
     "lines": "325-326",
     "quote": "the checks proved that elements existed, but did not prove that a learner could see, understand, hear, correct, complete, and resume the released experience."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/hub-review-model.md",
     "lines": "337",
     "quote": "all run \"at mobile and desktop viewports.\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    46,
    47
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat accessibility as part of validity: an item a learner can't operate, or whose assistive-technology reading gives away the answer, yields an invalid score.",
   "kind": "measured",
   "found_by": "Course and assessment reviews found drag-and-drop items that could not be used by keyboard or assistive technology, and a 12-option item for young learners. A static scan found 192 matching items whose assistive-technology labels announce which bucket is the decoy.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RED_TEAM_FINDINGS.md",
     "lines": "41",
     "quote": "an inaccessible item isn't just bad UX, it's an invalid score."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "103",
     "quote": "An item type that cannot be made accessible is also not a faithful rehearsal of the test."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/BUILD_FACTS.md",
     "lines": "24",
     "quote": "137 items over a 5-option cap driven by hot-text, 161 stimuli leak '###' markdown, 192 match items announce a decoy bucket"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    27
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a written answer can't yet be marked reliably, check in code the part that can be checked (such as the cited evidence) and record the rest without grading it.",
   "kind": "adopted rule",
   "found_by": "A review attacked a written step that could be passed by typing anything. The design split it into an evidence citation checked in code and a justification that is logged but not graded. A course package leaves constructed answers ungraded until a trusted grader and an escalation path to a person exist.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/BUILD_FACTS.md",
     "lines": "35",
     "quote": "\"attempting\"-gameable written step (F4 must log justification as attention evidence, machine-check the citation half)"
    },
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/review/start-here.md",
     "lines": "19",
     "quote": "deterministic checking is limited to candidate MCQ choices; constructed historical reasoning remains ungraded until a trusted rubric grader and human escalation path are approved."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    11,
    29,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Prove a writer actually uses its inputs by sending marked dummy values and checking they come back unchanged.",
   "kind": "adopted rule",
   "found_by": "After a generator ignored the fields it was sent in the first benchmark run, the contract added a compliance test that uses dummy values.",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/GENERATOR_API_SPEC.md",
     "lines": "376",
     "quote": "To verify generator compliance, send this test request:"
    },
    {
     "path": "~/Documents/APinceptbench/docs/GENERATOR_API_SPEC.md",
     "lines": "409",
     "quote": "If any field is missing, renamed, or has a different value, the generator is **non-compliant**."
    },
    {
     "path": "~/Documents/APinceptbench/docs/GENERATOR_API_SPEC.md",
     "lines": "41",
     "quote": "MUST be echoed back unchanged. MUST NOT be transformed or auto-generated."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge generated content on whether it hits its target at the right depth, not on polish, because fluent and readable output was common while on-target output was not.",
   "kind": "measured",
   "found_by": "In the same run, generated items scored 99.1% on clarity while only 43.0% matched their objective. A team position records that a model's knowledge of teaching does not show up in what it generates.",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_FAILURE_REPORT.md",
     "lines": "103",
     "quote": "### 1. Clarity (99.1% pass rate) ✅"
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_FAILURE_REPORT.md",
     "lines": "134",
     "quote": "### 7. Curriculum Alignment (43.0% pass rate) ❌❌"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
     "lines": "61",
     "quote": "A model's pedagogical knowledge does not survive the trip into its generated content"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Anchor content and items to the target exam's released questions and scoring guides as well as to its content outline, because the outline says what is in scope while the released material shows what is valued.",
   "kind": "adopted rule",
   "found_by": "A knowledge-building pipeline drew facts from released exam questions as one of its sources. Two course-design guides tell builders to calibrate items to released exam examples.",
   "evidence": [
    {
     "path": "~/Downloads/Knowledge Schema Generator - AP USH Unit 2.xlsx",
     "lines": "sheet 'Instructions' (xl/worksheets/sheet1.xml), cell B2, step 5",
     "quote": "- Run \"Get Exam Question Inputs\" in the Functions Menu to get the scraped high-alignment MCQs and FRQs from AP Classroom in the \"Exam\" sheet."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
     "lines": "57",
     "quote": "The CED tells you what's in scope; the released materials and rubrics tell you what's actually valued and tested."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-ap-brainlift.md",
     "lines": "217",
     "quote": "- All questions must match CED examples in:"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Design a mastery test to separate learners by breadth, with one item per standard across many standards and items a learner who has mastered the material passes nearly every time, and pick a length where the pass mark is a whole number of allowed errors.",
   "kind": "adopted rule",
   "found_by": "A guide distilled from building one course's mastery test.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-bespoke-mastery-assessments.md",
     "lines": "52",
     "quote": "Discrimination between mastered and non-mastered students is delivered by breadth of coverage (24 items spanning ~24 standards), not by individually tricky items."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-bespoke-mastery-assessments.md",
     "lines": "39",
     "quote": "Given assessments are short, you will likely want to enforce a one-item-per-standard sampling rule."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-bespoke-mastery-assessments.md",
     "lines": "33",
     "quote": "- At a 90% pass threshold, a 30 item form would be more reliable than a 24 item form, but a 28 item form would not be."
    }
   ],
   "against": "A high fixed bar can be out of reach: 'only ~17% of cohort clears 90% today, so a flat wall has no on-ramp.' (~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md line 47).",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Stage a high mastery bar so learners have a way up to it, because a flat bar that only about one learner in six could clear gave most of them no path forward.",
   "kind": "measured",
   "found_by": "A course measured how many of its current learners would clear a flat 90% gate (about 17%) and moved to staged gates.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
     "lines": "47",
     "quote": "Three difficulty bands (not five stages); staged 90% gates (not flat-90%) — only ~17% of cohort clears 90% today, so a flat wall has no on-ramp."
    }
   ],
   "against": "Elsewhere the bar is fixed for all courses: 'This is likely hard-coded school-wide at 90% mastery.' (~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-bespoke-mastery-assessments.md line 46, name-bearing).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When most test items must be written from scratch, fix the test blueprint's slots first and then write items to fill them.",
   "kind": "adopted rule",
   "found_by": "A guide distilled from building one course's mastery test.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-bespoke-mastery-assessments.md",
     "lines": "57",
     "quote": "When most items will be authored from scratch — as is true here — it is vastly more efficient to invert that order: do the sampling first, then author to meet the planned form and bank needs."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Review each stage's output before the next, more expensive stage is built on it: knowledge units before scripts, scripts before media, and approved facts before the links between them.",
   "kind": "adopted rule",
   "found_by": "A knowledge pipeline generates links between facts only after the facts are approved. A platform guide sets a hard checkpoint on knowledge units and asks for script review before media is generated.",
   "evidence": [
    {
     "path": "~/Downloads/Knowledge Schema Generator - AP USH Unit 2.xlsx",
     "lines": "sheet 'Instructions' (xl/worksheets/sheet1.xml), cell B2, step 20",
     "quote": "20. Run step 11 in main.py which is to generate relationships. This will be the very last step after the KS for the unit has been approved."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
     "lines": "89",
     "quote": "The cost of fixing a problem rises sharply once the video has been generated from the script."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
     "lines": "63",
     "quote": "KC errors propagate through every downstream stage, so this is the cheapest place to catch them."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    61
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Before running a whole production pipeline, tune it on a spread of cases that includes every type and the hardest one.",
   "kind": "adopted rule",
   "found_by": "A platform guide's calibration step for video generation.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
     "lines": "103",
     "quote": "- Include the script you think is hardest to generate."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
     "lines": "184",
     "quote": "Each course will need to go through a calibration process where around 10 diverse scripts from the course are used to adjust the prompts in the pipeline as needed."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    47
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Confront the misconceptions learners bring on their own with a direct contrast, but don't raise misconceptions that only poor teaching creates; teach precisely enough to prevent them.",
   "kind": "adopted rule",
   "found_by": "A template for course design documents.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-how-to-write-a-course-brainlift.md",
     "lines": "31",
     "quote": "instinctive misconceptions (intuitive — students arrive with them or generate them naturally) require contrastive treatment in the script; misconceptions caused by poor instruction (artefacts of how the topic is typically taught) should not be surfaced in the script — the script just needs to be precise enough to prevent them."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    62
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Space practice over time and interleave topics, even though learners find it harder than blocked practice.",
   "kind": "external research",
   "found_by": "Cited in a course-design guide: Kornell & Bjork (2008), https://doi.org/10.1111/j.1467-9280.2008.02209.x.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-ap-brainlift.md",
     "lines": "496",
     "quote": "- Link: [https://doi.org/10.1111/j.1467-9280.2008.02209.x](https://doi.org/10.1111/j.1467-9280.2008.02209.x)"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-ap-brainlift.md",
     "lines": "508",
     "quote": "- Interleaving topics rather than blocking them feels harder to students but produces stronger learning and better transfer of knowledge"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    51
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Key corrective feedback to the specific error the learner made, telling them what to look at, rather than giving one generic message for every wrong answer.",
   "kind": "adopted rule",
   "found_by": "One course's lesson spec gives a separate corrective line for each anticipated error type. A review of another course faulted its single generic retry message for every wrong answer (~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md line 15).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/lesson-01.json",
     "lines": "142",
     "quote": "Replace then with a mechanism such as supplied labor, structured diplomacy, or constrained settlement."
    },
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/lesson-01.json",
     "lines": "91",
     "quote": "Ask what the earlier condition made possible, costly, contested, or more likely."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
   "lines": "250",
   "quote": "- Feedback Incorrect: One sentence shown to the student when they answer incorrectly (~15–25 words). Should state the correct answer as concisely as possible. No judgment — just the answer."
  },
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
   "lines": "15",
   "quote": "a wrong answer returns only “Good try, let’s look again,” with no explanation and no correct answer shown."
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/lesson-01.json",
   "lines": "91",
   "quote": "Ask what the earlier condition made possible, costly, contested, or more likely."
  },
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
   "lines": "50",
   "quote": "Hedged language is not politeness, it is load: 'might', 'maybe', 'a little' are excluded because they add processing cost without information."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
   "lines": "26",
   "quote": "I-do reveals the answer instead of modeling thought"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
   "lines": "248",
   "quote": "If the model selects the correct answer in ≥3/5 trials, the item fails — it is answerable from background knowledge alone, not from careful reading of the specific passage."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/incept-package-hub/course-packages/courses/g8-reading/review/evidence/case-for-review.md",
   "lines": "55-56",
   "quote": "The redesign defeats the G8 POC's 98.6%-leak failure."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/g5_analysis_digest.md",
   "lines": "41",
   "quote": "the 120 L.5 vocab seeds LEAK 99.2% and must be re-authored + re-certified, never deployed as-is"
  },
  {
   "truth": 5,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
   "lines": "254",
   "quote": "- Text-dependence ablation uses a language model, which may have different knowledge than a typical G3–G5 student. Items that fail for LLMs may be valid for students (false positives) or vice versa."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
   "lines": "241",
   "quote": "| Dim 9: Answer key defensibility | Correct answer is uniquely defensible from text | Hard gate |"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
   "lines": "47",
   "quote": "79% of correct answers sat at option position A"
  },
  {
   "truth": 9,
   "effect": "counter",
   "path": "~/Documents/APinceptbench/ap_benchmark/prompts/base.py",
   "lines": "28",
   "quote": "**When in doubt, FAIL the question. Missing problems is worse than over-flagging.**"
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
   "lines": "296",
   "quote": "One failure is almost certainly forgetting. Three consecutive failures almost certainly indicate an encoding problem."
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
   "lines": "246",
   "quote": "| Dim 14: EBSR Part B verbatim | Part B options are verbatim passage sentences (EBSR only) | Hard gate |"
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
   "lines": "185",
   "quote": "- Video validation: There is a video validation portal where a human watches newly generated videos and either accepts them or requests a re-generation. This should be done by a subject expert so that any inaccuracies in instruction are picked up."
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
   "lines": "36",
   "quote": "(1) Maps, even stylistic and approximate maps are poor"
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/lesson-01.json",
   "lines": "35",
   "quote": "If source reading, discussion, accessibility support, or correction needs more time, split the lesson rather than compressing the required evidence work."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/BUILD_FACTS.md",
   "lines": "16",
   "quote": "Use the render-truth manifest as the ONE source"
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
   "lines": "28",
   "quote": "The reviewers identify this as a WCAG 2.1 AA contrast failure and unusable by all students."
  },
  {
   "truth": 32,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md",
   "lines": "91",
   "quote": "The discipline: any claim that would embarrass us if checked *was* checked, by an agent instructed to break it."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/test_server.py",
   "lines": "208",
   "quote": "return matches >= total * 0.8  # Allow 20% variance due to LLM"
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/05_LIMITATIONS.md",
   "lines": "61",
   "quote": "The v4 consistency result (r=0.918, LoA [−10.0, +10.0] RIT) is an engine consistency check — explicitly not MAP agreement evidence."
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/benchmark_official.py",
   "lines": "208",
   "quote": "score = dim_data.get(\"score\", 1.0) if isinstance(dim_data, dict) else dim_data"
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/review/evidence/incept-acceptance.json",
   "lines": "37",
   "quote": "Eleven of 28 checks are visibly marked as uncertified fallback routes pending authored replacement."
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/ap_benchmark/calibration/gold_standard.json",
   "lines": "4",
   "quote": "\"pass_threshold\": 0.85,"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/docs/reports/evaluation_20260225_081919_0909a798.md",
   "lines": "33",
   "quote": "| LEQ      |    200 |      0 |      0 |    100.0% |      1.00 |"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/docs/reports/evaluation_20260225_081919_0909a798.md",
   "lines": "100",
   "quote": "| prompt_arguability        |  391 |    0 |    100.0% |      1.00 |"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
   "lines": "97",
   "quote": "then demonstrate it blocking a real miss in a live walkthrough."
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/review/start-here.md",
   "lines": "13",
   "quote": "- seven progressively revealed phases: retrieval, teaching dose, model, guided response, independent response, feedback and different-evidence retry, and checkpoint;"
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
   "lines": "34",
   "quote": "**Relabeled** — now \"internal cross-bank consistency (synthetic),\" explicitly not MAP agreement"
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/incept-package-hub/docs/COURSE_PACKAGE_STANDARD.md",
   "lines": "237",
   "quote": "Warnings remain visible. Human-review requirements do not disappear when the release envelope passes."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/docs/FULL-COURSE-AUTHORING-STATUS.md",
   "lines": "49",
   "quote": "Automated structural, route, source-link, and mutation checks do not substitute for these gates."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/hub-review-model.md",
   "lines": "213-214",
   "quote": "Never describe mechanical validation as human review, certification, runtime verification, or release authorization."
  },
  {
   "truth": 44,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
   "lines": "307",
   "quote": "This instrument's item quality is established **empirically, not editorially** — and that is a design position, not an omission:"
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/ap_benchmark/prompts/base.py",
   "lines": "15",
   "quote": "PROMPT_VERSION = \"2026.02.24.1\"  # Relaxed cognitive demand - recall is OK"
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/ap_benchmark/core/scorer.py",
   "lines": "19",
   "quote": "Pass threshold: 0.85 (fixed, never changes)"
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/benchmark_official.py",
   "lines": "214",
   "quote": "passed = not critical_failed and overall_score >= 0.70"
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/incept-package-hub/docs/COURSE_PACKAGE_STANDARD.md",
   "lines": "156",
   "quote": "Copying an application's stylesheet, rebuilding its shell, or describing an artifact as an approximation never satisfies the presentation declaration, even when the Hub can preserve those bytes exactly."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
   "lines": "35",
   "quote": "Acquisition mastery and durable mastery are different. A same-day lesson gate proves at most 'I can do it now,' not 'I can still do it later under changed conditions.'"
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/review/evidence/case-for-review.md",
   "lines": "10",
   "quote": "The nine assessment sets preserve held-out source use, function-level scoring, correction routes,"
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/assessment-set.json",
   "lines": "67",
   "quote": "Report performance by item and historical function. Do not convert this local sample into an AP score prediction."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Downloads/Knowledge Schema Generator - AP USH Unit 2.xlsx",
   "lines": "sheet '4. Consolidation Audit' (xl/worksheets/sheet10.xml), row 2, column F ('Sources')",
   "quote": "AMSCO, Princeton, Exam"
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-ap-brainlift.md",
   "lines": "592",
   "quote": "- Student preference often conflicts with effective practice"
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
   "lines": "191",
   "quote": "- The trade-off shifts for older students, where the cognitive load of reading along may outweigh the benefit, unless they are in a noisy environment or watching on mute (common on mobile)."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/docs/reports/evaluation_20260225_081919_0909a798.md",
   "lines": "67",
   "quote": "- (3x) Some documents appear to be simulated rather than authentic historical sources"
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md",
   "lines": "60",
   "quote": "- Scope expansion beyond provided curriculum (e.g., adding Syria/Libya when curriculum specifies Iraq/Afghanistan only)"
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN6_REPORT.md",
   "lines": "14-15",
   "quote": "| Avg Score | 0.795 | 0.801 | +0.006 |"
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN3_REPORT.md",
   "lines": "15",
   "quote": "| Avg Score | 0.644 | 0.826 | 0.827 | → stable |"
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RECHECK_FINDINGS.md",
   "lines": "7",
   "quote": "the fix wave introduced a handful of new inconsistencies."
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Downloads/Knowledge Schema Generator - AP USH Unit 2.xlsx",
   "lines": "sheet 'Instructions' (xl/worksheets/sheet1.xml), cell B2, step 20",
   "quote": "20. Run step 11 in main.py which is to generate relationships. This will be the very last step after the KS for the unit has been approved."
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
   "lines": "85",
   "quote": "at least one item is mistagged (a vocabulary item labelled Inference and Evidence), which weakens the claim of full standards alignment."
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Downloads/unit-1-apush-benchmark.jsonl",
   "lines": "1",
   "quote": "{\"grade\":\"1\",\"subject\":\"apush\",\"type\":\"dbq\",\"difficulty\":\"easy\",\"quantity\":1,"
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/docs/EVALUATION_PROCESS.md",
   "lines": "127",
   "quote": "Hard fails trigger BEFORE the API call, saving time and money."
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN5_REPORT.md",
   "lines": "32",
   "quote": "**Key observation:** Run 5 fixed easy difficulty (27% → 68%) but broke hard difficulty (58% → 38%) and cognitive demand (70% → 59%)."
  }
 ]
}
```
