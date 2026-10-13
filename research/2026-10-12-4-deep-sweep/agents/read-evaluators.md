# read:evaluators

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "evaluators: how generated items were judged, calibrated, re-run and failure-analysed (work/evaluator and work/evaluatorML)",
 "coverage": {
  "read": [
   "evaluator/README.md",
   "evaluator/docs/*.md (README, SYSTEM_ARCHITECTURE, EVALUATION_PROCESS, EVALUATION_API: rules and key sections, AP_GENERATOR_SPEC, AP_QUESTION_TYPES_SPEC, CURRICULUM_STANDARDS, GENERATOR_INPUTS, GENERATOR_API_SPEC: rules and key sections)",
   "evaluator/docs/reports: BENCHMARK_FAILURE_REPORT, BENCHMARK_COMPREHENSIVE_REPORT, BENCHMARK_RUN2-RUN8, LATEST, evaluation_20260225_081919_0909a798 (full); the other 11 evaluation_*.md (headers, per-type tables) and 3 detailed_report_20260226_*.md (headers, dimension tables, judge issues)",
   "evaluator/analysis/reports/*.md (COMPREHENSIVE_FAILURE_REPORT in full; the 5 agent findings files, which it repeats), analysis/failure_analyzer.py, analysis/run_analysis_agents.py (agent prompts)",
   "evaluator/ap_benchmark/prompts/*.py (base, official_ap_prompts, official_ap_formatters options handling, mcq, msq, fill_in, match, article)",
   "evaluator/ap_benchmark/core/evaluator.py, scorer.py, curriculum.py (confidence levels); grep of orchestrator.py and pipeline.py for calibration/variance terms",
   "evaluator/ap_benchmark/calibration/gold_standard.json (all 25 cases summarised) and validator.py",
   "evaluator/ap_benchmark/hard_fail/rules.py, checker.py (structure)",
   "evaluator/evaluation_server.py (scoring/pass section), benchmark_official.py (judge call, stats), test_server.py (consistency test), generate_evaluation_report.py (run selection), archive/*.py docstrings, git log",
   "evaluatorML/AGENTS.md, CLAUDE.md, .agent/NORTH_STAR.md, MEMORY.md, LESSONS_LEARNED.md, PATTERNS_CATALOG.md (judge/review sections), KNOWLEDGE_PACK.md (head); grep of the other .agent scaffold files for judge/eval terms",
   "evaluatorML/.agent/memory/analysis: all 5 .md files plus ib-criteria-registry.json and ap-history-benchmark-registry.json",
   "evaluatorML/.agent/memory/plans: ib-criteria-brain-model, ib-pattern-compiler-prelaunch-revision, ap-history-request-expectation-mapping (training-plan skimmed via the others)",
   "evaluatorML/.agent/memory/request_expectations/*.md (6), deterministic_compiler/*.md (README, report, reconciliation, package_report, parallel_experiment_note, package README), packages/apush_unit1_pipeline_v0 README, MANIFEST, docs/KNOWN_FAILURES.md, training_data/*.md",
   "evaluatorML/.agent/memory/e2e_pipeline: all 57 evaluation/generation/loop reports, loop_summary.jsonl files, verdict fields (id, passed, score, zero metrics) of the small evaluation_results.jsonl files for re-run comparison, file timestamps, and scripts: generate_apush_unit1_openapi_poc.py (writer prompt), iterate_repair_to_100.py (clean contract), search_repair_candidates.py (docstring), evaluate_generated_openapi_items.py (pass logic), apply_deterministic_builders.py (header)",
   "evaluatorML/.agent/memory/HANDOFF.md, SHORT_TERM_MEMORY.md, PROMPTS.md, BACKUPS/BEADS pre-migration ledger, beads backup jsonl (filtered for evaluator items)",
   "evaluatorML/synapse-briefs: 18 read in full, all 52 keyword-scanned"
  ],
  "skipped": [
   "evaluator/.env and .env.example (credentials rule)",
   "evaluator/.claude/settings.local.json (tool settings)",
   "evaluator/ap_social_studies_dump.zip, data/curriculum_facts.json, data/curriculum_relationships.json (data dumps)",
   "__pycache__ (compiled)",
   "ap_benchmark/core database/hash/models/orchestrator/pipeline code (infrastructure; grepped only)",
   "evaluatorML/.beads (Dolt database) and BACKUPS tgz",
   "large jsonl: ap_history_ib_contracts_v0.jsonl (409 MB), ap_history_request_expectations.jsonl (167 MB), SFT training jsonl (33 MB), taxonomy json (5.6 MB), exemplar registry, sample jsonl files",
   "zips, *.log, batch_responses/raw_evaluations dumps, generated_content_response.json item dumps, openapi.json",
   "training payload/status JSON and SFT launch details (training mechanics)",
   "plans/2026-05-25-real-beads-migration.md and agent scaffold files SOUL/TOOLS/TWEAKING/HUMAN_GUIDE/GETTING_STARTED/GOGCLI_STARTER/IDENTITY/USER/OPENCLAW, openclaw/, skills/ (agent tooling, grepped only)",
   "synapse-briefs content as evidence (organisational compliance notices; contents name people and an email address)"
  ],
  "notes": "No person-labelled agreement data (judge vs human) exist in either folder; the 25-case gold calibration set has no recorded labeller, covers only single- and multi-select items, and no run of its validator was found. The external judge's criteria pack and cheater reports live in work/aptraining (out of scope) and were used only through the in-scope audit summaries. Many run-to-run pass-rate changes mix writer changes with judge changes; the cleanest judge-variance evidence is the re-runs on unchanged files (content timestamps predate all runs). Several evaluator analysis files are machine-written and contain invented figures; they are cited only as examples of what went wrong or for counts produced by code. Every absolute path sits under the machine's home folder, which contains the account owner's username; I did not treat that shared prefix as name-bearing, and no cited file has a person's name in its path below it. Read-only throughout: no files written and no ledger (mgr) entries made."
 },
 "candidates": [
  {
   "statement": "Before repairing an item the judge failed, re-run the judge on the unchanged item, and confirm a repaired item over more than one run: borderline failures often pass a second time with nothing changed.",
   "kind": "measured",
   "found_by": "In a generation pipeline a 100-item run failed 3 items; re-judging the same unchanged file minutes later passed all 3. In another build, 2 of 8 failures passed when the unchanged file was re-judged, and one item went pass, fail, pass across three runs within an hour (each report names the same input file, whose timestamp predates all the runs).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build27_full_eval/evaluation_report.md",
     "lines": "9",
     "quote": "- Failed: 3"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build27_fail3_recheck/evaluation_report.md",
     "lines": "3-8",
     "quote": "- Passed: 3"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build17_fail8_recheck/evaluation_report.md",
     "lines": "8",
     "quote": "- Passed: 2"
    }
   ],
   "against": "Full runs judged items in batches of 5 and rechecks one at a time ('- Batch size: 5' in the full-run report, '- Batch size: 1' in the recheck report, line 12 of each), so batching may explain part of the flips; one item still flipped between two one-at-a-time runs of the same file.",
   "adds_to_existing": [
    34,
    65,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep the judge's instructions, the pass rule in code and the written spec as one source: a criterion the judge is told is blocking must actually block.",
   "kind": "measured",
   "found_by": "The source-based essay rubric listed document authenticity (line 321) under the judge's critical dimensions, but the server's pass rule gated only four other dimensions and averaged the rest (evaluation_server.py lines 877-895). In the latest run that item type passed 99.1% while document authenticity passed 0.9%, so items with unattributed or fabricated documents passed. The same repo also states two different pass thresholds (0.85 and 0.70).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/official_ap_prompts.py",
     "lines": "315-321",
     "quote": "### CRITICAL DIMENSIONS"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
     "lines": "34",
     "quote": "| DBQ      |    109 |      1 |      4 |     99.1% |      0.88 |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
     "lines": "75",
     "quote": "| document_authenticity     |    1 |  109 |      0.9% |      0.59 |"
    }
   ],
   "against": "The API reference marks the same criterion as averaged, so the code may match intent and the prompt's 'critical' label may be the outlier: '| `document_authenticity` | Normal | Authentic sources with attribution |' (docs/EVALUATION_API.md line 543).",
   "adds_to_existing": [
    28,
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A criterion that scores zero on every item, including items that pass overall, is not what sinks items; confirm it is actually scored before ranking it as decisive.",
   "kind": "measured",
   "found_by": "A criteria-weighting analysis built from 12 graded shared-source sets gave three criteria a zero on all 12 rows while 25% of the rows passed, ranked those three as 'load-bearing', and the ranking was copied into the project's orientation file and training-budget weights. Recorded verdicts for that item type from the same judge carry no such criteria at all (e2e_pipeline/apush_unit1_deterministic_build27_fail3_recheck/evaluation_results.jsonl line 1), so the zeros most likely mean 'not scored'.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-registry.json",
     "lines": "337-343",
     "quote": "\"zero_rate\": 1.0"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-registry.json",
     "lines": "386-387",
     "quote": "\"pass_rate\": 0.25,"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-pack-audit.md",
     "lines": "43",
     "quote": "- Load-bearing: `specification_compliance` 0.750, `curriculum_alignment` 0.750, `distractor_quality` 0.750, `educational_accuracy` 0.5833, `stimulus_quality` 0.3333"
    }
   ],
   "against": "The audit itself flagged the sample size: '- Caveat: only 12 rows; treat as hard until larger sample.' (2026-05-25-ib-criteria-pack-audit.md line 45).",
   "adds_to_existing": [
    9,
    36
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Report every requested item's fate (passed, failed, never produced, not judged) over one stated denominator; computing the rate only on the items that came back inflates it.",
   "kind": "measured",
   "found_by": "One run lost 39 of 120 requested items to generation errors and computed its pass rate on the 81 returned. Another report counted 11 judge errors as non-passes in its headline rate (61.1%) but dropped them from the per-type rates, so a type with 7 errors among 11 items showed 100%. A later runner counted generation failures as zeros.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN8_REPORT.md",
     "lines": "93-95",
     "quote": "This reduced the sample size from 120 to 81, affecting statistical reliability."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/evaluation_20260225_155759_209babe7.md",
     "lines": "34",
     "quote": "| DBQ      |      4 |      0 |      7 |    100.0% |      0.88 |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/benchmark_official.py",
     "lines": "379-382",
     "quote": "# Calculate statistics (generation failures count as 0s)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Recompute every number in a machine-written analysis from the raw records before acting on it.",
   "kind": "measured",
   "found_by": "An automated multi-agent failure analysis claimed one dimension 'appears in 95% (146/153) of hard question failures' by dividing a count taken over all 280 failures by the number of hard-difficulty failures; the same report attached invented 'expected impact' percentages to each recommended fix.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
     "lines": "40",
     "quote": "- Answer validity appears in 95% (146/153) of hard question failures"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
     "lines": "17",
     "quote": "| Hard | 153 | 765 | 20.0% |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/failure_analyzer.py",
     "lines": "127-140",
     "quote": "analysis['hard_fail_breakdown'][hf] += 1"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Read failure rates of generated items as evidence about the writer and the judge, not about what learners find hard.",
   "kind": "measured",
   "found_by": "From topic-level failure rates of generated questions (one topic: 3 failures out of 6 items), an analysis agent wrote what 'students confuse' and set a 15-25% selection-rate target for wrong options, although no learner had answered any item.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
     "lines": "603",
     "quote": "| Spread of Communism after 1900... | 3 | 6 | 50.0% |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
     "lines": "126",
     "quote": "- Students confuse different communist movements (Russian, Chinese, Cuban)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
     "lines": "345",
     "quote": "- Validate distractors represent 15-25% selection rate each"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Don't route, restrict or drop an item type because of one run's cell rates over a handful of items; such cells reverse on the next run.",
   "kind": "measured",
   "found_by": "After one run a report advised moving medium-difficulty multi-select items to single-answer items because that cell passed 54%; the next two runs measured the same cell at 78% (7/9) and 88% (7/8). Another cell went 15%, then 0% (6 items), then 64% over three runs.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN3_REPORT.md",
     "lines": "102-119",
     "quote": "| **Medium** | MCQ (83%) | Match (73%) | MSQ (54%) |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN5_REPORT.md",
     "lines": "64",
     "quote": "3. **MSQ + Medium: 78%** (7/9) - Good"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN6_REPORT.md",
     "lines": "66",
     "quote": "1. **MSQ + Medium: 88%** (7/8)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    15,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Compare runs per item type or on the same mix of types; a shift in the mix moves the overall pass rate by itself.",
   "kind": "measured",
   "found_by": "Between two runs the weakest format fell from 39 to 20 of 116 items while the overall rate rose from 50.0% to 62.9%; a later run had no matching items at all, and leaving out its weakest format alone would have moved its rate from 49.4% to 66.1%.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md",
     "lines": "502",
     "quote": "| Run 6 | 39 | 26 | 28 | 23 | 116 |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md",
     "lines": "503",
     "quote": "| Run 7 | 20 | 33 | 34 | 29 | 116 |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN8_REPORT.md",
     "lines": "137",
     "quote": "| Pass Rate | 49.4% | **66.1%** |"
    }
   ],
   "against": "The weakest format's own rate also changed between those runs (23% to 45%), so the mix explains only part of the change: '| fill-in | 66% | 50% | **21%** | 25% | 23% | 45% | **38%** |' (BENCHMARK_COMPREHENSIVE_REPORT.md line 107).",
   "adds_to_existing": [
    49,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Test a judge's repeatability on borderline and failing items, not on confident passes; that is where its verdicts flip.",
   "kind": "measured",
   "found_by": "The evaluator's consistency test re-scored only recent passing items scoring 0.9 or more and tolerated 20% disagreement, while pipeline re-runs on unchanged files showed flips concentrated among failures (3 of 3 and 2 of 8 failures passed on re-run).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/test_server.py",
     "lines": "113-117",
     "quote": "\"overall_score\": {\"$gte\": 0.9}  # High-scoring questions"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/test_server.py",
     "lines": "208",
     "quote": "return matches >= total * 0.8  # Allow 20% variance due to LLM"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build27_fail3_recheck/evaluation_report.md",
     "lines": "8",
     "quote": "- Passed: 3"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't let a check run, or pass by default, only when an optional part or its definition is present; leaving the part out then becomes the easiest way to pass.",
   "kind": "measured",
   "found_by": "Cheater runs against the external judge found that its source-quality check passes by default when no source is required, its answer-leak probe runs only when a source is present, and its spec check passes without a quoted spec; its difficulty check also passes whenever no difficulty definitions are supplied.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-pack-audit.md",
     "lines": "63",
     "quote": "- B1: `stimulus_quality` Mode C default-pass when no curriculum `requires_stimulus` flag is present."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-pack-audit.md",
     "lines": "64",
     "quote": "- B2: zero-knowledge educational probe runs only when a stimulus is present."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "27",
     "quote": "- If no difficulty definitions are provided, `difficulty_alignment` defaults to pass."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a judge's reasons and its verdict disagree, treat the verdict as unsure and re-check it; never let the contradiction resolve to a pass.",
   "kind": "measured",
   "found_by": "Cheater runs found the external judge's anti-contradiction 'self-heal' can flip a failure to a pass when its reasoning says the item is correct; the local judge prompt declared any issue/score mismatch an evaluation error, but the scoring code never checked for it.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-pack-audit.md",
     "lines": "65",
     "quote": "- B3: base prompt anti-contradiction self-heal can flip failures to pass if reasoning says correct."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/base.py",
     "lines": "64-66",
     "quote": "3. Inconsistency between issues and scores is an evaluation ERROR"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9,
    39
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Never present invented text as a real document or quotation: quote real sources exactly with full attribution, or label constructed text as adapted or constructed.",
   "kind": "measured",
   "found_by": "Unattributed or simulated documents were the most often failed criterion for source-based tasks (document authenticity passed 14.7% in a 947-item run and 0.9% in a later run); the judge called one unlabelled invented account misleading. The pipeline later told the writer to avoid fake verbatim quotations.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/evaluation_20260225_081919_0909a798.md",
     "lines": "82",
     "quote": "| document_authenticity     |   28 |  163 |     14.7% |      0.15 |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
     "lines": "169",
     "quote": "This document has no attribution whatsoever and risks misleading students."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/generate_apush_unit1_openapi_poc.py",
     "lines": "136",
     "quote": "Avoid fake verbatim quotations; for uncertain source text, write paraphrased source-style excerpts with clear generic attribution."
    }
   ],
   "against": "The project's own rules disagree on constructed documents: one spec requires '- ALL documents MUST be authentic historical sources or clearly adapted from authentic sources' (docs/GENERATOR_API_SPEC.md line 294), while the pass contract allows '- retrieve or construct real-source-mirroring documents with period-plausible language and attribution; do not invent unsupported facts.' (2026-05-25-ib-pass-contract-matrix.md line 39).",
   "adds_to_existing": [
    17,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Build each wrong option from a named misconception or a specific wrong link (wrong time, place, cause or actor); both absurd and near-correct options fail.",
   "kind": "measured",
   "found_by": "In the largest failure analysis distractor quality was the most often failed dimension (348 failures); judges rejected options 'no serious student' would pick, and the external judge's rules ban borderline-correct and opposite/negation options.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
     "lines": "325",
     "quote": "## 1. Distractor Quality (348 failures - CRITICAL)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "39-40",
     "quote": "- Distractors must be plausible, homogeneous, grammatically parallel, similar in specificity/length, and tied to real misconceptions."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ap-history-ib-expectation-matrix.md",
     "lines": "124",
     "quote": "- Write distractors from wrong period, wrong region, wrong cause, wrong actor, or overgeneralized interpretation."
    }
   ],
   "against": "One run report advised the opposite for easy items: '- Have obviously wrong distractors (for MCQ)' (docs/reports/BENCHMARK_RUN4_REPORT.md line 326).",
   "adds_to_existing": [
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make the item demand the thinking the objective's verb names; a format that only asks for a recalled term cannot test an explain-why objective.",
   "kind": "measured",
   "found_by": "Generated questions for 'explain how and why' objectives tested only 'what'; in one run 35 of 39 fill-in-the-blank items failed the thinking-demand check, and fill-in averaged 38% pass over six runs.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_FAILURE_REPORT.md",
     "lines": "132",
     "quote": "- Learning objectives require \"explain how and why\" but questions only test \"what\""
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN6_REPORT.md",
     "lines": "99",
     "quote": "| **Cognitive Demand** | **35** (90% of fill-in!) |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/GENERATOR_API_SPEC.md",
     "lines": "128",
     "quote": "- Use the action verbs in the objective to guide question construction (e.g., \"Explain\" → requires explanation, \"Compare\" → requires comparison)"
    }
   ],
   "against": "The judge's rubric was later relaxed to accept recall, so the measured failure rate depends on the rubric version: '- Recall and memorization questions ARE ACCEPTABLE' (ap_benchmark/prompts/base.py line 88); fill-in also passed 65.6% in one run (BENCHMARK_RUN2_REPORT.md line 121).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make a harder item harder by adding reasoning steps, not rarer words or extra context; added scaffolding made hard items easier.",
   "kind": "measured",
   "found_by": "Difficulty settings changed only vocabulary, not the thinking required; in one run 24 of 39 hard items failed, mostly on difficulty alignment, because the writer added context that made the answers predictable.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN3_REPORT.md",
     "lines": "80",
     "quote": "- Difficulty adjustment only changes vocabulary complexity, not cognitive demand"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN5_REPORT.md",
     "lines": "114",
     "quote": "**Pattern:** The endpoint adds too much context/scaffolding, which paradoxically makes hard questions easier to answer."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/packages/apush_unit1_pipeline_v0/docs/KNOWN_FAILURES.md",
     "lines": "44",
     "quote": "- Make the medium difficulty come from an APUSH inference, not wording complexity."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give a matching item more answer choices than prompts; with one-to-one pairs the last matches fall out by elimination.",
   "kind": "measured",
   "found_by": "One-to-one matching items averaged 51% pass over six runs and never exceeded 55%; the judge's reasons cited the missing extra options.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN7_REPORT.md",
     "lines": "58",
     "quote": "- difficulty_alignment: 1:1 matching without distractors reduces difficulty"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN7_REPORT.md",
     "lines": "59",
     "quote": "- distractor_quality: No extra options to create analytical challenge"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md",
     "lines": "391",
     "quote": "- No distractors = simple elimination"
    }
   ],
   "against": "The judge's own matching rules allowed equal counts: '- Equal or greater number of definitions/descriptions' (ap_benchmark/prompts/match.py line 12).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Spend the most checking on the hardest generated items; in the largest run they failed review three times as often as the easiest.",
   "kind": "measured",
   "found_by": "Across 2,296 evaluations, items requested as hard failed 20.0% of the time, against 6.5% for easy and 10.1% for medium.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
     "lines": "15",
     "quote": "| Easy | 51 | 779 | 6.5% |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
     "lines": "17",
     "quote": "| Hard | 153 | 765 | 20.0% |"
    }
   ],
   "against": "Smaller runs with other writers showed the reverse: '**Inversion:** Hard questions now outperform easy questions.' (docs/reports/BENCHMARK_RUN8_REPORT.md line 53).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When an item tests knowledge rather than reading, check that a reader with no knowledge cannot reach the answer from the source and question alone.",
   "kind": "adopted rule",
   "found_by": "The external judge fails items where a zero-knowledge reader can get the answer from the source and stem (paraphrase, mechanism-naming and similar leaks); the check family holding this probe was the most common zero in the pipeline (in one 100-item run it was zero on 14 of the 15 failures).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "28",
     "quote": "- Stimulus answer leaks fail `educational_accuracy` when a zero-knowledge student can reach the answer from the stimulus and stem alone."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "41",
     "quote": "- Avoid stimulus leaks: mechanism-naming, connect-the-paragraphs, visual-depicts-answer, and numbered-path mechanism-labeling leaks."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build2_eval/evaluation_report.md",
     "lines": "9-16",
     "quote": "- Zero metrics: {'concept_coverage': 1, 'difficulty_alignment': 1, 'difficulty_distribution': 3, 'educational_accuracy': 14, 'mastery_learning_alignment': 2, 'non_repetitiveness': 2, 'specification_compliance': 3, 'stimulus_quality': 2, 'test_preparedness': 3}"
    }
   ],
   "against": "The probe only runs when a source is present, so items without one were never checked: '- B2: zero-knowledge educational probe runs only when a stimulus is present.' (2026-05-25-ib-criteria-pack-audit.md line 64).",
   "adds_to_existing": [
    5,
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Nothing a student sees may address the judge (score claims, rubric self-advocacy, instructions to the evaluator), and judge vocabulary and verdicts stay out of the writer's instructions.",
   "kind": "adopted rule",
   "found_by": "The external judge zeroes every metric when an item fails its integrity check, so the pipeline stripped scoring labels and judge-facing terms from the writer's contract and used verdicts only outside the writer to choose between candidates.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "24",
     "quote": "- Integrity check runs first. Never include evaluator-facing score claims, rubric self-advocacy, or instructions to the evaluator."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "110",
     "quote": "- Integrity failure overrides all metrics to zero."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py",
     "lines": "399",
     "quote": "\"\"\"Generator-safe contract: no scoring labels, weights, or judge-facing terms.\"\"\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    12
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Let a judge fail an item on a requirement only when it quotes both the requirement and the violating text, and make those quotes required fields of its output.",
   "kind": "adopted rule",
   "found_by": "The external judge's spec check fails only with a quoted requirement and quoted violating content; the project's reference patterns require an evidence quote from judges, fail runs with empty quotes, and name the rubber-stamp pass and the 'be strict' prompt as failure modes (sources: https://trilogyai.substack.com/p/what-would-vin-claudel-do).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "26",
     "quote": "- `specification_compliance` only fails when there is a clear explicit spec, a quoted requirement, and quoted violating content."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/PATTERNS_CATALOG.md",
     "lines": "105",
     "quote": "- **P-WWVCD-04** — For judge hallucination, require `evidence_quote` output field + strip write perms from evaluator. Never \"BE STRICT\" in a prompt."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/PATTERNS_CATALOG.md",
     "lines": "107",
     "quote": "- **P-WWVCD-06** — Output schemas enforce evidence fields; empty quotes fail the run."
    }
   ],
   "against": "Without a quoted spec the same check passes by default: '- B4: `specification_compliance` defaults to 1.0 without explicit quoted spec and quoted violation.' (2026-05-25-ib-criteria-pack-audit.md line 66).",
   "adds_to_existing": [
    17,
    32,
    33
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Change a judge only to agree better with labelled cases, never to move the pass rate, and re-label the calibration cases whenever a rule changes.",
   "kind": "adopted rule",
   "found_by": "The project's rule ties evaluator changes to benchmark accuracy, not pass rate; yet after runs in which the thinking-demand check was the main cause of failure, the judge prompt was relaxed to accept recall, while the calibration set still labels recall-only items as failures and a pre-judge pattern rule still fails 'What year...' stems, leaving three definitions of one criterion.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/EVALUATION_PROCESS.md",
     "lines": "158-159",
     "quote": "- Changes to evaluator based on benchmark accuracy, not pass rate"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/base.py",
     "lines": "15",
     "quote": "PROMPT_VERSION = \"2026.02.24.1\"  # Relaxed cognitive demand - recall is OK"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/calibration/gold_standard.json",
     "lines": "194",
     "quote": "\"failure_reason\": \"Recall-only question - just asks for a date without any analysis\""
    }
   ],
   "against": "none found; no source records whether the relaxation was tested against labelled cases.",
   "adds_to_existing": [
    37,
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before optimizing items against a judge, attack the judge with a deliberate cheater to find what it passes by default, and keep a frozen holdout to catch gaming.",
   "kind": "adopted rule",
   "found_by": "Cheater runs against the external judge found five exploitable surfaces; the plan then banned teaching exploit text and kept a frozen holdout to detect grader overfit.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-pack-audit.md",
     "lines": "61",
     "quote": "Cheater reports identify five exploitable surfaces:"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-pack-audit.md",
     "lines": "69",
     "quote": "Training implication: do not teach exploit text. Teach defensive generation patterns:"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/plans/2026-05-25-ib-criteria-brain-model.md",
     "lines": "98",
     "quote": "- Keep a frozen holdout to detect grader overfit and \"cheater\" behavior."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Map each fault to one primary criterion; otherwise one fault fails several criteria and the per-criterion counts mislead.",
   "kind": "adopted rule",
   "found_by": "When the writer returned the wrong item format, the judge recorded it as a curriculum-alignment failure (15 of 26 such failures in one run) and also failed factual accuracy because it could not see the answer choices; the external judge's rule maps one issue to one metric.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "30",
     "quote": "- One issue should map to one primary metric. The compiler should label likely failure metric explicitly."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "24",
     "quote": "**15 out of 26 curriculum alignment failures (58%) are due to FORMAT MISMATCH.**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "139-140",
     "quote": "factual_accuracy: \"Cannot verify factual accuracy because the actual"
    }
   ],
   "against": "The local judge prompt allowed one issue to zero several criteria: '2. Every issue MUST result in at least one 0.0 dimension' (ap_benchmark/prompts/base.py line 65).",
   "adds_to_existing": [
    31
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Mark alignment strictly only against an explicit target; when the target had to be inferred from the item, fail only clear mismatches.",
   "kind": "adopted rule",
   "found_by": "The evaluator set confidence levels for the target: with explicit standard metadata any deviation fails alignment; with a target inferred from the content the judge is told to be conservative.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/core/curriculum.py",
     "lines": "99",
     "quote": "\"Any deviation from the target standard is a curriculum_alignment FAILURE.\""
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/core/curriculum.py",
     "lines": "110-111",
     "quote": "\"Curriculum standards are inferred from content. Be conservative in evaluation - \""
    }
   ],
   "against": "The calibration harness passed no target at all, so every calibration case ran in the lenient inferred mode: 'curriculum_info=example.question_dict.get(\"curriculum_info\", \"\"),' (ap_benchmark/calibration/validator.py line 117).",
   "adds_to_existing": [
    33
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Fact-check every field a student can see (explanations, hints, feedback, source details) and check that the key agrees with all of them.",
   "kind": "adopted rule",
   "found_by": "The external judge counts keys, rationales, feedback and support fields toward factual accuracy and requires the key to agree with every explanation and hint; the calibration set includes an item failed only because its explanation contradicted the question's date.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "29",
     "quote": "- Factual claims, answer keys, rationales, feedback, and support fields all count for `factual_accuracy`."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "38",
     "quote": "- The keyed answer must be factually correct and internally consistent with all explanations, hints, feedback, and additional details."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/calibration/gold_standard.json",
     "lines": "460",
     "quote": "\"failure_reason\": \"Factual inconsistency: Question says 1946 (correct), but explanation says 1948 (incorrect)\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make each question in a set, and each part of a multi-part question, answerable and scorable on its own; no part may pre-answer another.",
   "kind": "adopted rule",
   "found_by": "Specs required independent answers for questions sharing a source and independently scorable parts; the judge flagged parts where a strong answer to one would partly answer the next.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/AP_GENERATOR_SPEC.md",
     "lines": "44",
     "quote": "**Rules**: 3-4 questions, different skills, independent answers"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
     "lines": "130",
     "quote": "| Parts (a) and (b) have some potential overlap — a strong answer to (a) could partially pre-answer (b... | 1 |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-pass-contract-matrix.md",
     "lines": "127",
     "quote": "- parts that depend on one another in a way that blocks independent scoring,"
    }
   ],
   "against": "Another spec pulls the other way: '- Parts MUST be scaffolded (build on each other OR test related aspects)' (docs/GENERATOR_API_SPEC.md line 239).",
   "adds_to_existing": [
    41,
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Ask for one task per part; a part that combines two tasks or two concepts is hard to mark.",
   "kind": "adopted rule",
   "found_by": "The API spec bans compound task verbs within one part, and the judge flagged a part that conflated two distinct concepts.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/EVALUATION_API.md",
     "lines": "328",
     "quote": "- **NEVER** use compound verbs like \"identify AND describe\" in a single part"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
     "lines": "125",
     "quote": "| Part (c) conflates two distinct concepts — maritime technology development AND navigational skills —... | 1 |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "For questions that share one source, choose the source first, list the distinct reasoning moves it supports, and write each question around a different move.",
   "kind": "adopted rule",
   "found_by": "Shared-source sets failed far more often than other item types (in one 100-item run 12 of 19 sets failed against 3 failures among the other 81 items); the generation contract adopted this build order and banned redundant questions.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ap-history-ib-expectation-matrix.md",
     "lines": "122",
     "quote": "- Choose stimulus first, then create distinct child reasoning moves."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-pass-contract-matrix.md",
     "lines": "71",
     "quote": "- build set backwards from stimulus: identify distinct APUSH reasoning moves first, then write each child around a different move."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build2_eval/evaluation_report.md",
     "lines": "14",
     "quote": "- By type: {'dbq': {'total': 21, 'passed': 20, 'failed': 1}, 'leq': {'total': 21, 'passed': 21}, 'mcq': {'total': 21, 'passed': 20, 'failed': 1}, 'mcq_set': {'total': 19, 'passed': 7, 'failed': 12}, 'saq': {'total': 18, 'passed': 17, 'failed': 1}}"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    41,
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make the right option impossible to spot from surface cues: similar length, grammatical fit with the stem, no absolute words, no 'all/none of the above'.",
   "kind": "adopted rule",
   "found_by": "The evaluator's item rules require similar option length and no grammar clues, and its pre-judge checks fail items with absolute language or 'all of the above' before the judge is called.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/mcq.py",
     "lines": "13",
     "quote": "- All options should be roughly similar in length"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/mcq.py",
     "lines": "20",
     "quote": "- Answer options should not give away the answer through grammar clues"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/hard_fail/rules.py",
     "lines": "63-64",
     "quote": "r'all\\s+of\\s+the\\s+above',"
    }
   ],
   "against": "The absolute-language word list also catches ordinary words, so a word filter can fail sound options: \"r'\\b(only|solely|exclusively)\\b',\" (ap_benchmark/hard_fail/rules.py line 38).",
   "adds_to_existing": [
    8
   ],
   "name_bearing_source": false
  },
  {
   "statement": "An answer explanation must say why the keyed answer is right and why each wrong option is wrong; restating the answer is not an explanation.",
   "kind": "adopted rule",
   "found_by": "The judge rubric failed explanations that only restated the answer, pre-judge rules failed one-line 'the answer is B' explanations, and calibration items were labelled bad for an explanation that just repeated the answer.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/base.py",
     "lines": "100",
     "quote": "- Does the explanation teach WHY the answer is correct?"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/base.py",
     "lines": "101",
     "quote": "- Does it address why other options are wrong?"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/calibration/gold_standard.json",
     "lines": "365",
     "quote": "\"failure_reason\": \"Recall-only asking for date; explanation is just the answer repeated\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When the learning target is a definition, write a task in which the learner uses the idea; never paste the definition into the question.",
   "kind": "adopted rule",
   "found_by": "Before building generation targets, the plan required definition-style standards to be turned into assessment tasks and listed 'definitional rows become copied stems' as a failure scenario (plan line 156); 510 of 53,790 benchmark requests were classed this way.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/plans/2026-05-25-ap-history-request-expectation-mapping.md",
     "lines": "35",
     "quote": "- Definitional standards must be transformed into assessment tasks, not copied into stems."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ap-history-ib-expectation-matrix.md",
     "lines": "213",
     "quote": "- Definitional text rather than task verb: identify the concept as the content target; require generator to transform it into a reasoning task rather than copy the definition."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/request_expectations/ap_history_request_expectations_summary.md",
     "lines": "8",
     "quote": "- By reasoning mode: {'definition_to_assessment': 510, 'causation': 25695, 'statement_to_assessment': 4515, 'comparison': 5880, 'evidence_source_analysis': 105, 'contextualization': 465, 'continuity_change_over_time': 13320, 'explanation_general': 2910, 'evaluation_argument': 390}"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Judge generated items with a different model from the one that wrote them.",
   "kind": "adopted rule",
   "found_by": "The evaluator was set up as independent of the generator, using a different model family, to keep evaluation impartial and keep its criteria from being shaped by generator output.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/EVALUATION_PROCESS.md",
     "lines": "5",
     "quote": "It uses Claude API (not the same model as the generator) to ensure impartial evaluation."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/EVALUATION_PROCESS.md",
     "lines": "155-158",
     "quote": "- Evaluator criteria should NOT be influenced by generator output"
    }
   ],
   "against": "none found; no source measures same-model against different-model judging.",
   "adds_to_existing": [
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge a writing aid (a spec, contract or prompt) by the items it leads to, against a no-aid baseline on the same requests, not by how its own text reads.",
   "kind": "adopted rule",
   "found_by": "Two ways of producing generation contracts were set up as a bake-off on identical requests and generator settings with a no-helper baseline, to be scored by downstream pass rate, retries and failure mix.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/deterministic_compiler/parallel_experiment_note.md",
     "lines": "26",
     "quote": "The winner is not whichever contract sounds better. The winner is whichever path improves downstream InceptBench pass rate, retry count, cost, and failure distribution when feeding the same APUSH/APWH/APEuro benchmark requests into the same generator."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/deterministic_compiler/README.md",
     "lines": "29-31",
     "quote": "1. No helper baseline."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/deterministic_compiler/README.md",
     "lines": "46",
     "quote": "The deterministic compiler wins by measured downstream outcomes, not by sounding clever."
    }
   ],
   "against": "At planning time the comparison had not run, and no result was found in scope: '- No no-compiler baseline or compiler A/B harness has run.' (plans/2026-05-25-ib-pattern-compiler-prelaunch-revision.md line 61).",
   "adds_to_existing": [
    70,
    51
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When one item format passes a judge almost every time, find out whether the items are good or the judge has nothing it can fail them on.",
   "kind": "open question",
   "found_by": "Essay prompts passed 200 of 200 in one run and 100% in others; the external judge's criteria pack found no criterion that sinks them and its audit calls the format lenient; the calibration set held no case of that format.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/evaluation_20260225_081919_0909a798.md",
     "lines": "33",
     "quote": "| LEQ      |    200 |      0 |      0 |    100.0% |      1.00 |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-pack-audit.md",
     "lines": "56",
     "quote": "- No load-bearing criterion in the pack."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "80",
     "quote": "LEQ is comparatively lenient but still needs clean structure."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/detailed_report_20260226_115508.md",
   "lines": "110",
   "quote": "The answer options (A, B, C, D) are entirely missing from the submission."
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/official_ap_formatters.py",
   "lines": "100-101",
   "quote": "lines.append(\"*No options provided*\")"
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/detailed_report_20260226_115508.md",
   "lines": "21",
   "quote": "| MCQ | 0 | 12 | 0 | 0.0% |"
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/detailed_report_20260226_124949.md",
   "lines": "21",
   "quote": "| MCQ | 11 | 1 | 0 | 91.7% |"
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/base.py",
   "lines": "351",
   "quote": "content = content[:8000] + \"\\n\\n... [truncated for evaluation]\""
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/calibration/validator.py",
   "lines": "81-116",
   "quote": "difficulty=example.question_dict.get(\"difficulty\", \"medium\"),"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/calibration/gold_standard.json",
   "lines": "296-308",
   "quote": "\"failure_reason\": \"Too easy for 'hard' difficulty; requires no analysis\""
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/core/evaluator.py",
   "lines": "167-168",
   "quote": "return DimensionScore(score=1.0, reasoning=default_reasoning, issues=[])"
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/core/evaluator.py",
   "lines": "446",
   "quote": "error_score = DimensionScore(score=0.0, reasoning=f\"Evaluation error: {str(e)}\", issues=[])"
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/evaluation_20260225_155759_209babe7.md",
   "lines": "11-14",
   "quote": "| Passed | 33 (61.1%) |"
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_repair_loop_clean4/loop_summary.jsonl",
   "lines": "2",
   "quote": "\"api_missing_evaluation\": 1"
  },
  {
   "truth": 9,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/base.py",
   "lines": "28",
   "quote": "**When in doubt, FAIL the question. Missing problems is worse than over-flagging.**"
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/base.py",
   "lines": "52-60",
   "quote": "Be THOROUGH. Find every problem."
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
   "lines": "79",
   "quote": "| distractor_quality        |   69 |  152 |     31.2% |      0.35 |"
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
   "lines": "174-176",
   "quote": "It does not represent a genuine student misconception and therefore weakens distractor quality.\", 'severity': 'minor'"
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
   "lines": "118",
   "quote": "| No significant structural or validity issues identified. | 2 |"
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
   "lines": "23",
   "quote": "- Default evaluator stance is pass, but mandatory audits in overlays override that leniency."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/test_server.py",
   "lines": "206",
   "quote": "Some evaluations differ (may be due to LLM variance)"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
   "lines": "155-158",
   "quote": "- **Dimensions:** factual_accuracy=1.0, answer_validity=1.0, stimulus_alignment=1.0, distractor_quality=0.0, skill_alignment=1.0, clarity=1.0"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/evaluation_20260225_081919_0909a798.md",
   "lines": "152-155",
   "quote": "- **Dimensions:** prompt_structure=1.0, historical_specificity=1.0, answerability=1.0, skill_alignment=1.0, stimulus_integration=0.0, scoring_clarity=1.0"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
   "lines": "19",
   "quote": "The practical rule for the generator is: **do not aim for “mostly good”; produce a checklist-complete item with no score-zero openings.**"
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN4_REPORT.md",
   "lines": "212-217",
   "quote": "assert response.format == \"fill-in\""
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/EVALUATION_PROCESS.md",
   "lines": "127",
   "quote": "Hard fails trigger BEFORE the API call, saving time and money."
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN4_REPORT.md",
   "lines": "24",
   "quote": "**15 out of 26 curriculum alignment failures (58%) are due to FORMAT MISMATCH.**"
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN2_REPORT.md",
   "lines": "181-187",
   "quote": "**Problem:** Question frames settlement houses as a Gilded Age phenomenon when the curriculum explicitly states they were Progressive Era (1890s-1920s). The Gilded Age ended around 1898."
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
   "lines": "126",
   "quote": "| Minor note: The curriculum context lists the time period as 'late 19th century,' which contradicts t... | 1 |"
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN2_REPORT.md",
   "lines": "30",
   "quote": "The dramatic improvement in curriculum alignment (43% → 89%) confirms the endpoint is now properly utilizing the `learning_objective` and `statement` fields provided in requests."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_FAILURE_REPORT.md",
   "lines": "33",
   "quote": "The generator ignores the specific `learning_objective` and `statement` provided in the request. Instead, it produces generic questions about the broad topic area."
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_FAILURE_REPORT.md",
   "lines": "30",
   "quote": "**65 out of 79 failed questions** had curriculum alignment issues. This is the **dominant failure mode**."
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/GENERATOR_API_SPEC.md",
   "lines": "123-124",
   "quote": "- The question MUST NOT require knowledge outside the scope of this fact (except for scaffolding context)"
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_repair_loop_clean4/loop_summary.jsonl",
   "lines": "2-3",
   "quote": "{\"round\": 2, \"evaluated\": 100, \"passed\": 87, \"failed\": 13, \"pass_rate\": 0.87, \"zero_metrics\": {\"difficulty_alignment\": 2, \"distractor_quality\": 2"
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
   "lines": "101",
   "quote": "- Parent factual accuracy fails if any child has a factual failure."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
   "lines": "107",
   "quote": "- Answer balance for MCQ_SET uses structured extraction plus chi-square; p >= 0.60 passes, otherwise fails."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_repair_loop_clean3/loop_summary.jsonl",
   "lines": "1",
   "quote": "\"failed\": 32, \"pass_rate\": 0.68, \"zero_metrics\": {\"answer_balance\": 15"
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/msq.py",
   "lines": "22",
   "quote": "- Each correct answer must be independently correct"
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
   "lines": "22-27",
   "quote": "| answer_validity | 146 |"
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN3_REPORT.md",
   "lines": "63",
   "quote": "- Result: Questions are either too simple (cognitive fail) or too complex (difficulty fail)"
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN3_REPORT.md",
   "lines": "346",
   "quote": "**Failed:** cognitive_demand: \"Requires sophisticated analysis of ideological contradictions, exceeding basic comprehension level\""
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN5_REPORT.md",
   "lines": "32",
   "quote": "**Key observation:** Run 5 fixed easy difficulty (27% → 68%) but broke hard difficulty (58% → 38%) and cognitive demand (70% → 59%)."
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/calibration/validator.py",
   "lines": "4-5",
   "quote": "Ensures >= 95% accuracy to catch evaluator drift over time."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/benchmark_official.py",
   "lines": "228-231",
   "quote": "\"raw_response\": text if 'text' in dir() else None,"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/GENERATOR_API_SPEC.md",
   "lines": "41",
   "quote": "MUST be echoed back unchanged. MUST NOT be transformed or auto-generated."
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
   "lines": "108",
   "quote": "- Factual audit can downgrade `factual_accuracy` by merging audit result via min(main, audit)."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
   "lines": "124",
   "quote": "| The preamble/stimulus text is somewhat leading and may inadvertently scaffold answers for parts (a) ... | 1 |"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/official_ap_prompts.py",
   "lines": "136-139",
   "quote": "- FAIL if questions can be answered without the stimulus"
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-pass-contract-matrix.md",
   "lines": "131",
   "quote": "- specify what earns credit without narrowing valid student phrasing too much."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ap-history-ib-expectation-matrix.md",
   "lines": "162",
   "quote": "- Expected-response/rubric criteria are specific enough to grade and flexible enough to accept valid variants."
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/deterministic_compiler/package_report.md",
   "lines": "56",
   "quote": "- Test names show coverage for evaluator prompt rules, factual audit gating, stimulus promise/reference detection, stem redundancy, extraneous-topic guards, and MCQ-set behavior."
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
   "lines": "97-98",
   "quote": "- Each question should test a distinct aspect of the stimulus."
  }
 ]
}
```
