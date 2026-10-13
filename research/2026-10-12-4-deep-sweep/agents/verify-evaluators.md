# verify:evaluators

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "evaluators: how generated items were judged, calibrated, re-run and failure-analysed (work/evaluator and work/evaluatorML)",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (the recheck quote is on line 8, not 3-8). Numbers hold: build27's full run failed 3 of 100 (report 03:48), and a recheck of the same input file (written 03:20) passed all 3 at 03:57; build17's full run failed 8 and its recheck passed 2. Per-item verdicts show item 040 went pass (1.0, 01:54), fail (02:08), pass (0.98, 02:27), and item 041 went from 1.0 SUPERIOR to failing twice. So 'borderline' has no support (removed), and 'passes can fail' is added. Same method as #34 (send each answer more than once, re-send every known miss after each rebuild). Kept because it adds item-judging evidence from re-runs on unchanged files, plus the step of re-judging before repairing.",
   "statement": "Before repairing an item a judge failed, re-run the judge on the unchanged item, and confirm a repaired item over more than one run: failures often pass a second time with nothing changed, and passes can fail.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build27_full_eval/evaluation_report.md",
     "lines": "9",
     "quote": "- Failed: 3",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build27_fail3_recheck/evaluation_report.md",
     "lines": "8",
     "quote": "- Passed: 3",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build17_fail8_recheck/evaluation_report.md",
     "lines": "8",
     "quote": "- Passed: 2",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build17_target7_eval/evaluation_results.jsonl",
     "lines": "5",
     "quote": "\"id\": \"apush-u1-041-mcq_set-hard\", \"type\": \"mcq_set\", \"difficulty\": \"hard\", \"substandard_id\": \"c_4kog\", \"overall_score\": 1.0, \"weighted_score\": null, \"overall_rating\": \"SUPERIOR\", \"passed\": true",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build17_fail8_recheck/evaluation_results.jsonl",
     "lines": "4",
     "quote": "\"id\": \"apush-u1-041-mcq_set-hard\", \"type\": \"mcq_set\", \"difficulty\": \"hard\", \"substandard_id\": \"c_4kog\", \"overall_score\": 0.8, \"weighted_score\": null, \"overall_rating\": \"INFERIOR\", \"passed\": false",
     "verbatim": true
    }
   ],
   "against": "Full runs judged items in batches of 5 and rechecks one at a time ('- Batch size: 5' in the full-run report, '- Batch size: 1' in the recheck report, line 12 of each), so batching may explain part of the flips. But item 041 also flipped between two one-at-a-time runs of the same file. All the re-runs are one external judge on one unit's items.",
   "general": true,
   "duplicate_of": "34",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The DBQ prompt lists document_authenticity under CRITICAL DIMENSIONS (lines 315-322). The runner whose results these reports summarise blocks only document_count, prompt_structure, factual_accuracy and answer_validity, and passes the rest on an average of 0.70 (benchmark_official.py lines 196-214; evaluation_server.py lines 877-895 is the same rule). The process doc states 0.85 instead. Added the 947-item run, which is starker than LATEST: DBQs passed 186 of 191 while document_authenticity got full marks on 28 of 191 (average 0.15). Correction to found_by: 'pass' in these dimension tables means a full score (generate_evaluation_report.py line 112). So read 'items the judge marked down on document authenticity passed', not 'fabricated documents passed'. #28 (students can't skip lesson checks) does not apply; the nearest existing truth is #59.",
   "statement": "Keep the judge's instructions, the pass rule in code and the written spec as one source: a criterion the judge is told is blocking must actually block.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/official_ap_prompts.py",
     "lines": "315-321",
     "quote": "### CRITICAL DIMENSIONS",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/benchmark_official.py",
     "lines": "213",
     "quote": "# Pass if: no hard failures AND overall score >= 0.70",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/evaluation_20260225_081919_0909a798.md",
     "lines": "34",
     "quote": "| DBQ      |    186 |      5 |      0 |     97.4% |      0.87 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/evaluation_20260225_081919_0909a798.md",
     "lines": "82",
     "quote": "| document_authenticity     |   28 |  163 |     14.7% |      0.15 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
     "lines": "34",
     "quote": "| DBQ      |    109 |      1 |      4 |     99.1% |      0.88 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
     "lines": "75",
     "quote": "| document_authenticity     |    1 |  109 |      0.9% |      0.59 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/EVALUATION_PROCESS.md",
     "lines": "123",
     "quote": "### Pass Threshold: **0.85**",
     "verbatim": true
    }
   ],
   "against": "The API reference marks the same criterion as averaged, so the code may match intent and the prompt's 'critical' label may be the outlier: '| `document_authenticity` | Normal | Authentic sources with attribution |' (docs/EVALUATION_API.md line 543).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. In the MCQ_SET cell (n_rows 12, pass_rate 0.25), curriculum_alignment, distractor_quality and specification_compliance each have zero_rate 1.0, mean 0.0 and zero_kills_overall_rate 0.75. So they were zero on the 3 passing sets as well, yet were ranked LOAD_BEARING at 0.75. That ranking reached NORTH_STAR.md line 37 and the plan's 'Oversample DBQ and MCQ_SET load-bearing criteria' (brain-model plan line 89). Every set-level verdict in the pipeline carries 11 metrics and none of those three (checked on all sets in two rechecks), so the zeros most likely mean 'not scored'. Correction: the pack came from earlier graded rows, so the found_by's 'same judge' should read 'the external judge's set-level verdicts in the pipeline'.",
   "statement": "A criterion that scores zero on every item, including items that pass overall, is not what sinks items; confirm it is actually scored before ranking it as decisive.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-registry.json",
     "lines": "337-343",
     "quote": "\"zero_rate\": 1.0",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-registry.json",
     "lines": "386-387",
     "quote": "\"pass_rate\": 0.25,",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-pack-audit.md",
     "lines": "43",
     "quote": "- Load-bearing: `specification_compliance` 0.750, `curriculum_alignment` 0.750, `distractor_quality` 0.750, `educational_accuracy` 0.5833, `stimulus_quality` 0.3333",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/NORTH_STAR.md",
     "lines": "37",
     "quote": "- MCQ_SET is structurally hard: specification_compliance, curriculum_alignment, distractor_quality, educational_accuracy, and stimulus_quality are all load-bearing.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build27_fail3_recheck/evaluation_results.jsonl",
     "lines": "1",
     "quote": "\"metric_scores\": {\"overall\": 0.9, \"factual_accuracy\": 1.0, \"educational_accuracy\": 1.0, \"localization_quality\": 1.0, \"concept_coverage\": 1.0, \"difficulty_distribution\": 1.0, \"stimulus_quality\": 1.0, \"non_repetitiveness\": 1.0, \"test_preparedness\": 1.0, \"answer_balance\": 1.0, \"integrity_check\": 1.0}",
     "verbatim": true
    }
   ],
   "against": "The audit itself flagged the sample size: '- Caveat: only 12 rows; treat as hard until larger sample.' (2026-05-25-ib-criteria-pack-audit.md line 45).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep",
   "reason": "Quotes verbatim and the numbers hold. 39 of 120 requests failed to generate, and the 49.4% was computed on 81. The 25 Feb report's 61.1% is 33 of 54 with 11 judge errors in the denominator, while its per-type rates drop errors (DBQ: 4 passed, 0 failed, 7 errors, shown as 100.0%). benchmark_official.py also adds generation failures to each type's total (line 395). Passed over returned is never below passed over requested, so the inflation is general. No existing truth covers reporting denominators.",
   "statement": "Report every requested item's fate (passed, failed, never produced, not judged) over one stated denominator; computing the rate only on the items that came back inflates it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN8_REPORT.md",
     "lines": "93-95",
     "quote": "This reduced the sample size from 120 to 81, affecting statistical reliability.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/evaluation_20260225_155759_209babe7.md",
     "lines": "34",
     "quote": "| DBQ      |      4 |      0 |      7 |    100.0% |      0.88 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/benchmark_official.py",
     "lines": "379-382",
     "quote": "# Calculate statistics (generation failures count as 0s)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep",
   "reason": "Quotes verbatim. failure_analyzer.py counts hard_fail_breakdown over every failure ('for f in failures', lines 127-140), so 146 is the number of answer-validity hard-fails among all 280 failures; dividing it by the 153 hard-difficulty failures confuses 'hard-fail' with 'hard'. The 'Expected Impact' figures on each fix (lines 484-541, one added as evidence) have no computation behind them. The '348 failures' given for distractor quality (line 325) exceeds the 280 failed items, so it counts issues. Related to #61 (don't build on a writer's unchecked notes) but about numbers in analyses; not a duplicate.",
   "statement": "Recompute every number in a machine-written analysis from the raw records before acting on it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
     "lines": "40",
     "quote": "- Answer validity appears in 95% (146/153) of hard question failures",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
     "lines": "17",
     "quote": "| Hard | 153 | 765 | 20.0% |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/failure_analyzer.py",
     "lines": "127-140",
     "quote": "analysis['hard_fail_breakdown'][hf] += 1",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
     "lines": "484",
     "quote": "### 1. Implement Answer Validity Hard Gates (Expected Impact: +15-20% pass rate)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep",
   "reason": "Quotes verbatim. The topic table is code-produced (failure_analyzer.py by_topic). The 'students confuse' pitfalls and the 15-25% selection-rate target were written by analysis agents from judge verdicts on generated items; no learner answered any item. Distinct from #44 and #48, which separate machine checks and passed gates from learning.",
   "statement": "Read failure rates of generated items as evidence about the writer and the judge, not about what learners find hard.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
     "lines": "603",
     "quote": "| Spread of Communism after 1900... | 3 | 6 | 50.0% |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
     "lines": "126",
     "quote": "- Students confuse different communist movements (Russian, Chinese, Cuban)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
     "lines": "345",
     "quote": "- Validate distractors represent 15-25% selection rate each",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (the RUN3 quote is on line 102; the router that sends medium MSQ to MCQ is lines 119-121). Correction: the very next run (Run 4) measured MSQ+medium at 71%, then 78% (7/9) and 88% (7/8), so 'the next two runs' should read 'the next three runs'. Match+easy went 15%, 0% (all 6 failed), then 64%. 'Reverse' softened to 'can reverse'. The pipeline-side counterpart of #15 (never adapt on fewer than three observations); not a duplicate.",
   "statement": "Don't route, restrict or drop an item type because of one run's cell rates over a handful of items; such cells can reverse on the next run.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN3_REPORT.md",
     "lines": "102",
     "quote": "| **Medium** | MCQ (83%) | Match (73%) | MSQ (54%) |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "44",
     "quote": "| MSQ | 40% | 71% | 75% |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN5_REPORT.md",
     "lines": "64",
     "quote": "3. **MSQ + Medium: 78%** (7/9) - Good",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN6_REPORT.md",
     "lines": "66",
     "quote": "1. **MSQ + Medium: 88%** (7/8)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "50",
     "quote": "2. **Match + Easy = 0%** - All 6 questions failed",
     "verbatim": true
    }
   ],
   "against": "The writer changed between runs ('The endpoint update broke format compliance:', BENCHMARK_RUN4_REPORT.md line 58), so the reversals mix writer changes with sampling noise; no two runs repeat the same writer and judge.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep",
   "reason": "Quotes verbatim. Run 6 had 39 fill-in items of 116 and Run 7 had 20, and the overall rate went from 50.0% to 62.9%. Holding Run 6's mix with Run 7's per-format rates gives about 59%, so the mix accounts for roughly a quarter to a half of the rise; the rest is the format's own gain (23% to 45%, the against). Run 8 had no match items (line 29), and its figures check out: 40 of 81 (49.4%), or 39 of 59 (66.1%) without fill-in. The same report's 'Would be 58% pass rate without fill-in' (line 115) is wrong.",
   "statement": "Compare runs per item type or on the same mix of types; a shift in the mix moves the overall pass rate by itself.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md",
     "lines": "502",
     "quote": "| Run 6 | 39 | 26 | 28 | 23 | 116 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md",
     "lines": "503",
     "quote": "| Run 7 | 20 | 33 | 34 | 29 | 116 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN8_REPORT.md",
     "lines": "137",
     "quote": "| Pass Rate | 49.4% | **66.1%** |",
     "verbatim": true
    }
   ],
   "against": "The weakest format's own rate also changed between those runs (23% to 45%), so the mix explains only part of the change: '| fill-in | 66% | 50% | **21%** | 25% | 23% | 45% | **38%** |' (BENCHMARK_COMPREHENSIVE_REPORT.md line 107).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "drop",
   "reason": "Quotes verbatim, but the evidence contradicts the claim that verdicts flip on borderline and failing items rather than confident passes. Item 041 scored 1.0 (SUPERIOR) and then failed in the next two runs of the same file; item 040 scored 1.0, failed, then passed. What remains (re-run failures as well as passes) is #34 and candidate 0. The test_server.py design (5 recent passes at 0.9 or more, 20% disagreement allowed) is already attached to #34 as existing evidence.",
   "statement": "Test a judge's repeatability on borderline and failing items, not on confident passes; that is where its verdicts flip.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/test_server.py",
     "lines": "113-117",
     "quote": "\"overall_score\": {\"$gte\": 0.9}  # High-scoring questions",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/test_server.py",
     "lines": "208",
     "quote": "return matches >= total * 0.8  # Allow 20% variance due to LLM",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build27_fail3_recheck/evaluation_report.md",
     "lines": "8",
     "quote": "- Passed: 3",
     "verbatim": true
    }
   ],
   "against": "Item 041 scored 1.0 (SUPERIOR) in one run and failed in the next two runs of the same file (apush_unit1_deterministic_build17_target7_eval/evaluation_results.jsonl line 5; apush_unit1_deterministic_build17_fail8_recheck/evaluation_results.jsonl line 4).",
   "general": false,
   "duplicate_of": "34",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (B1, B2 and the prompt audit's difficulty default). Reworded: the original 'Don't let a check run, or pass by default, only when...' runs the two loopholes together. The local judge has the same hole, added as evidence: a dimension the model leaves out scores 1.0 'Not evaluated' (evaluator.py lines 159-168). Refines #9 (unsure is never a pass) and #38.",
   "statement": "Don't let a check run only when an optional part is present, or pass by default when that part or its definition is missing: leaving the part out then becomes the easiest way to pass.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-pack-audit.md",
     "lines": "63",
     "quote": "- B1: `stimulus_quality` Mode C default-pass when no curriculum `requires_stimulus` flag is present.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-pack-audit.md",
     "lines": "64",
     "quote": "- B2: zero-knowledge educational probe runs only when a stimulus is present.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "27",
     "quote": "- If no difficulty definitions are provided, `difficulty_alignment` defaults to pass.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/core/evaluator.py",
     "lines": "168",
     "quote": "return DimensionScore(score=1.0, reasoning=default_reasoning, issues=[])",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Refinement of the found_by: a consistency check was written (ap_benchmark/core/models.py lines 231-260) but nothing calls it (a search of the folder finds only its definition), so the prompt's 'evaluation ERROR' is never enforced. Extends #9: a contradiction between the reasons and the verdict is an unsure verdict.",
   "statement": "When a judge's reasons and its verdict disagree, treat the verdict as unsure and re-check it; never let the contradiction resolve to a pass.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-pack-audit.md",
     "lines": "65",
     "quote": "- B3: base prompt anti-contradiction self-heal can flip failures to pass if reasoning says correct.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/base.py",
     "lines": "64-66",
     "quote": "3. Inconsistency between issues and scores is an evaluation ERROR",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/core/models.py",
     "lines": "233",
     "quote": "Validate self-consistency: every 0.0 has issues, every issue has 0.0.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The 14.7% (28 of 191) in the 947-item run and 0.9% (1 of 110) in LATEST are full-score rates on document_authenticity, the lowest of every dimension in both runs. The judge's own note asks for authentic documents 'or clearly labeled as adapted/simulated' (LATEST.md line 169), and the pass contract forbids 'fabricated documents presented as real' (line 32, added). Overlaps #17 (quote exactly) but adds attribution and the labelling of constructed text. Added to against: the later repair rules preferred plausible generic attributions to labels.",
   "statement": "Never present invented text as a real document or quotation: quote real sources exactly with full attribution, or label constructed text as adapted or constructed.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/evaluation_20260225_081919_0909a798.md",
     "lines": "82",
     "quote": "| document_authenticity     |   28 |  163 |     14.7% |      0.15 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
     "lines": "169",
     "quote": "This document has no attribution whatsoever and risks misleading students.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/generate_apush_unit1_openapi_poc.py",
     "lines": "136",
     "quote": "Avoid fake verbatim quotations; for uncertain source text, write paraphrased source-style excerpts with clear generic attribution.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-pass-contract-matrix.md",
     "lines": "32",
     "quote": "- fabricated documents presented as real,",
     "verbatim": true
    }
   ],
   "against": "The project's own rules disagree on constructed documents. One spec requires '- ALL documents MUST be authentic historical sources or clearly adapted from authentic sources' (docs/GENERATOR_API_SPEC.md line 294). The pass contract allows '- retrieve or construct real-source-mirroring documents with period-plausible language and attribution; do not invent unsupported facts.' (2026-05-25-ib-pass-contract-matrix.md line 39). The later repair rules say 'Prefer generic but plausible attributions such as 'Spanish colonial account, early 1500s' over fake named precision.' (e2e_pipeline/iterate_repair_to_100.py line 155), with no label that the text is constructed.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, but the '348 failures' figure (COMPREHENSIVE_FAILURE_REPORT.md line 325) was written by an analysis agent from per-issue counts (it exceeds the 280 failed items), so it is replaced by code-produced and judge evidence. In LATEST, distractor quality got full marks on 69 of 221 choice items (31.2%, the lowest of their dimensions). The local rubric fails absurd options (base.py line 97), and a judge rejected one as 'extreme/absurd' (LATEST.md line 176). The external rules ban borderline-correct and opposite options (audit line 40). Adds to #6.",
   "statement": "Build each wrong option from a named misconception or a specific wrong link (wrong time, place, cause or actor); both absurd and near-correct options fail.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
     "lines": "79",
     "quote": "| distractor_quality        |   69 |  152 |     31.2% |      0.35 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
     "lines": "176",
     "quote": "Option A is too easily dismissed as an extreme/absurd distractor.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/base.py",
     "lines": "97",
     "quote": "- FAIL for obviously absurd distractors",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "40",
     "quote": "- Avoid opposite/negation distractors, borderline-correct distractors, and partial-question giveaways.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "39",
     "quote": "- Distractors must be plausible, homogeneous, grammatically parallel, similar in specificity/length, and tied to real misconceptions.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ap-history-ib-expectation-matrix.md",
     "lines": "124",
     "quote": "- Write distractors from wrong period, wrong region, wrong cause, wrong actor, or overgeneralized interpretation.",
     "verbatim": true
    }
   ],
   "against": "One run report advised the opposite for easy items: '- Have obviously wrong distractors (for MCQ)' (docs/reports/BENCHMARK_RUN4_REPORT.md line 326).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "keep",
   "reason": "Quotes verbatim. In Run 6, 35 of 39 fill-in items failed cognitive demand (30 of 39 failed overall), and fill-in averaged 38% across Runs 2-7 (BENCHMARK_COMPREHENSIVE_REPORT.md line 107). The measured rate depends on the rubric version, as the against says. No existing truth covers fitting the task to the objective's verb.",
   "statement": "Make the item demand the thinking the objective's verb names; a format that only asks for a recalled term cannot test an explain-why objective.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_FAILURE_REPORT.md",
     "lines": "132",
     "quote": "- Learning objectives require \"explain how and why\" but questions only test \"what\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN6_REPORT.md",
     "lines": "99",
     "quote": "| **Cognitive Demand** | **35** (90% of fill-in!) |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/GENERATOR_API_SPEC.md",
     "lines": "128",
     "quote": "- Use the action verbs in the objective to guide question construction (e.g., \"Explain\" → requires explanation, \"Compare\" → requires comparison)",
     "verbatim": true
    }
   ],
   "against": "The judge's rubric was later relaxed to accept recall, so the measured failure rate depends on the rubric version: '- Recall and memorization questions ARE ACCEPTABLE' (ap_benchmark/prompts/base.py line 88); fill-in also passed 65.6% in one run (BENCHMARK_RUN2_REPORT.md line 121).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep",
   "reason": "Quotes verbatim. In Run 5, 24 of 39 hard items failed, difficulty alignment being the largest cause (17), and the judge cited scaffolding that made answers predictable (lines 92-114). The later repair rules say the same ('Do not make difficulty depend on obscure wording...', iterate_repair_to_100.py line 216, added). The cause is the judge's reading, not learner data.",
   "statement": "Make a harder item harder by adding reasoning steps, not rarer words or extra context; added scaffolding made hard items easier.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN3_REPORT.md",
     "lines": "80",
     "quote": "- Difficulty adjustment only changes vocabulary complexity, not cognitive demand",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN5_REPORT.md",
     "lines": "114",
     "quote": "**Pattern:** The endpoint adds too much context/scaffolding, which paradoxically makes hard questions easier to answer.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/packages/apush_unit1_pipeline_v0/docs/KNOWN_FAILURES.md",
     "lines": "44",
     "quote": "- Make the medium difficulty come from an APUSH inference, not wording complexity.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py",
     "lines": "216",
     "quote": "Do not make difficulty depend on obscure wording; make it depend on historical reasoning.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep",
   "reason": "Quotes verbatim. Match averaged 51% over Runs 2-7 and never exceeded 55% (BENCHMARK_COMPREHENSIVE_REPORT.md lines 106, 384-387), and the judge's reasons cite the missing extra options. No run tested matching items with extra options, and the judge's own matching rules allowed equal counts (against).",
   "statement": "Give a matching item more answer choices than prompts; with one-to-one pairs the last matches fall out by elimination.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN7_REPORT.md",
     "lines": "58",
     "quote": "- difficulty_alignment: 1:1 matching without distractors reduces difficulty",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN7_REPORT.md",
     "lines": "59",
     "quote": "- distractor_quality: No extra options to create analytical challenge",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md",
     "lines": "391",
     "quote": "- No distractors = simple elimination",
     "verbatim": true
    }
   ],
   "against": "The judge's own matching rules allowed equal counts: '- Equal or greater number of definitions/descriptions' (ap_benchmark/prompts/match.py line 12).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "drop",
   "reason": "Quotes verbatim and 20.0% against 6.5% holds. But the 2,296 evaluations are every evaluation in one evaluation-server log (failure_analyzer.py parses log blocks), not 'the largest run', and other runs in the same sources reverse the order. Run 3 passed 46% of easy and 69% of hard items (BENCHMARK_RUN5_REPORT.md line 28); Run 8 passed 39.4% easy and 64.0% hard; the pipeline's build 2 failed 6 of 34 easy and 4 of 33 hard. Where failures concentrate depends on the writer; measuring per cell is candidates 6 and 7.",
   "statement": "Spend the most checking on the hardest generated items; in the largest run they failed review three times as often as the easiest.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
     "lines": "15",
     "quote": "| Easy | 51 | 779 | 6.5% |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
     "lines": "17",
     "quote": "| Hard | 153 | 765 | 20.0% |",
     "verbatim": true
    }
   ],
   "against": "Smaller runs with other writers showed the reverse: '**Inversion:** Hard questions now outperform easy questions.' (docs/reports/BENCHMARK_RUN8_REPORT.md line 53).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 17,
   "verdict": "keep",
   "reason": "Quotes verbatim (the build 2 quote is on line 16). Under the external judge any zero keeps an item below 0.85 (prompt audit lines 11-15), and the pipeline passes an item only at 0.85 or an acceptable rating (evaluate_generated_openapi_items.py lines 54-60). So build 2's 14 educational_accuracy zeros sit on 14 of its 15 failures. It was the most common zero in every pipeline run read (25 of 32 failures in clean3 round 0). That metric covers more than the zero-knowledge probe, as the found_by says. The mirror of #5 (the text must be needed): here knowledge must be needed. Related to #3.",
   "statement": "When an item tests knowledge rather than reading, check that a reader with no knowledge cannot reach the answer from the source and question alone.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "28",
     "quote": "- Stimulus answer leaks fail `educational_accuracy` when a zero-knowledge student can reach the answer from the stimulus and stem alone.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "41",
     "quote": "- Avoid stimulus leaks: mechanism-naming, connect-the-paragraphs, visual-depicts-answer, and numbered-path mechanism-labeling leaks.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build2_eval/evaluation_report.md",
     "lines": "16",
     "quote": "- Zero metrics: {'concept_coverage': 1, 'difficulty_alignment': 1, 'difficulty_distribution': 3, 'educational_accuracy': 14, 'mastery_learning_alignment': 2, 'non_repetitiveness': 2, 'specification_compliance': 3, 'stimulus_quality': 2, 'test_preparedness': 3}",
     "verbatim": true
    }
   ],
   "against": "The probe only runs when a source is present, so items without one were never checked: '- B2: zero-knowledge educational probe runs only when a stimulus is present.' (2026-05-25-ib-criteria-pack-audit.md line 64).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Correction: the pipeline did pass verdicts to the writer. Its repair prompt carries the judge's reasoning and suggested improvements as 'CLEAN CONTENT REVIEW NOTES', after dropping sentences that contain judge words (iterate_repair_to_100.py lines 264-290, 486-487). So the rule covers the judge's names, scores, labels and raw output (lines 267-268, added), not its verdicts; statement rewritten. The item-side counterpart of #12.",
   "statement": "Nothing a student sees may address the judge (score claims, rubric self-advocacy, instructions to the evaluator), and the writer never sees the judge's names, scores, metric labels or raw output; a failed item's reasons reach it only as plain editorial notes.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "24",
     "quote": "- Integrity check runs first. Never include evaluator-facing score claims, rubric self-advocacy, or instructions to the evaluator.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "110",
     "quote": "- Integrity failure overrides all metrics to zero.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py",
     "lines": "399",
     "quote": "\"\"\"Generator-safe contract: no scoring labels, weights, or judge-facing terms.\"\"\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py",
     "lines": "267-268",
     "quote": "The generator must never see evaluator names, scores, metric labels, or raw judge JSON. It only receives ordinary editorial/historical repair notes.",
     "verbatim": true
    }
   ],
   "against": "none found; no run compares repairs given these notes with repairs given raw verdicts or no notes.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. As written, the rule reproduces the external judge's exploitable default: with no quotable spec the check scores 1.0 (B4, one of the five surfaces cheater runs found). So the statement now adds that such a check is unsure (#9), not passed. The two patterns come from an external post the catalogue cites; the catalogue's path has no person's name. Refines #32 (bounded claims) and #17.",
   "statement": "Let a judge fail an item on a requirement only when it quotes both the requirement and the violating text, make those quotes required fields of its output, and treat a check with no quotable requirement as unsure, not passed.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "26",
     "quote": "- `specification_compliance` only fails when there is a clear explicit spec, a quoted requirement, and quoted violating content.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/PATTERNS_CATALOG.md",
     "lines": "105",
     "quote": "- **P-WWVCD-04** — For judge hallucination, require `evidence_quote` output field + strip write perms from evaluator. Never \"BE STRICT\" in a prompt.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/PATTERNS_CATALOG.md",
     "lines": "107",
     "quote": "- **P-WWVCD-06** — Output schemas enforce evidence fields; empty quotes fail the run.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-pack-audit.md",
     "lines": "66",
     "quote": "- B4: `specification_compliance` defaults to 1.0 without explicit quoted spec and quoted violation.",
     "verbatim": true
    }
   ],
   "against": "The quote rule on its own left a default pass that cheater runs exploited: '- B4: `specification_compliance` defaults to 1.0 without explicit quoted spec and quoted violation.' (2026-05-25-ib-criteria-pack-audit.md line 66). The added clause answers it but is untested.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep",
   "reason": "Quotes verbatim. The prompt relaxed recall on 24 Feb (base.py line 15), after the 24 Feb comparison named cognitive demand the primary driver of failures (line 88, added). Meanwhile the 23 Feb gold set still labels recall-only items as failures (gold_standard.json line 194), and the pre-judge rule still fails 'What year...' stems (rules.py line 45, added). No source records why the prompt changed. Adds 'never to move the pass rate' to #37, #42 and #45.",
   "statement": "Change a judge only to agree better with labelled cases, never to move the pass rate, and re-label the calibration cases whenever a rule changes.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/EVALUATION_PROCESS.md",
     "lines": "158-159",
     "quote": "- Changes to evaluator based on benchmark accuracy, not pass rate",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/base.py",
     "lines": "15",
     "quote": "PROMPT_VERSION = \"2026.02.24.1\"  # Relaxed cognitive demand - recall is OK",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/calibration/gold_standard.json",
     "lines": "194",
     "quote": "\"failure_reason\": \"Recall-only question - just asks for a date without any analysis\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md",
     "lines": "88",
     "quote": "| cognitive_demand | 38 | **PRIMARY DRIVER** |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/hard_fail/rules.py",
     "lines": "45",
     "quote": "r'^what\\s+year\\s+',",
     "verbatim": true
    }
   ],
   "against": "none found; no source records whether the relaxation was tested against labelled cases.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "keep",
   "reason": "Quotes verbatim. The five surfaces come from cheater reports summarised in the audit (the reports themselves live outside this folder). The frozen holdout is planned, not shown to have run. The judge-side counterpart of #38 and #47; not a duplicate.",
   "statement": "Before optimizing items against a judge, attack the judge with a deliberate cheater to find what it passes by default, and keep a frozen holdout to catch gaming.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-pack-audit.md",
     "lines": "61",
     "quote": "Cheater reports identify five exploitable surfaces:",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-pack-audit.md",
     "lines": "69",
     "quote": "Training implication: do not teach exploit text. Teach defensive generation patterns:",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/plans/2026-05-25-ib-criteria-brain-model.md",
     "lines": "98",
     "quote": "- Keep a frozen holdout to detect grader overfit and \"cheater\" behavior.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep",
   "reason": "Quotes verbatim. In Run 4, 15 of 26 curriculum-alignment failures were format mismatches, and the same mismatch also failed factual accuracy because the judge's view lacked the choices. The local prompt's rule that every issue must zero at least one dimension pulls the other way (against). Related to #31 and #30.",
   "statement": "Map each fault to one primary criterion; otherwise one fault fails several criteria and the per-criterion counts mislead.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "30",
     "quote": "- One issue should map to one primary metric. The compiler should label likely failure metric explicitly.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "24",
     "quote": "**15 out of 26 curriculum alignment failures (58%) are due to FORMAT MISMATCH.**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "139-140",
     "quote": "factual_accuracy: \"Cannot verify factual accuracy because the actual",
     "verbatim": true
    }
   ],
   "against": "The local judge prompt allowed one issue to zero several criteria: '2. Every issue MUST result in at least one 0.0 dimension' (ap_benchmark/prompts/base.py line 65).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (curriculum.py lines 95-112: GUARANTEED for an explicit node or substandard id, HARD for a description or instructions, SOFT for content inference). Correction to the against: the gold cases do carry curriculum_info (e.g. gold_standard.json line 12), but the loader drops it, and difficulty too (validator.py lines 81-87). So the effect holds, for a different reason. Related to #33.",
   "statement": "Mark alignment strictly only against an explicit target; when the target had to be inferred from the item, fail only clear mismatches.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/core/curriculum.py",
     "lines": "99",
     "quote": "\"Any deviation from the target standard is a curriculum_alignment FAILURE.\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/core/curriculum.py",
     "lines": "110-111",
     "quote": "\"Curriculum standards are inferred from content. Be conservative in evaluation - \"",
     "verbatim": true
    }
   ],
   "against": "The calibration harness never gave the judge a target. load_gold_standard builds each case without its curriculum_info or difficulty (ap_benchmark/calibration/validator.py lines 81-87), so 'curriculum_info=example.question_dict.get(\"curriculum_info\", \"\"),' (line 117) is always empty, and every calibration case ran in the lenient inferred mode.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep",
   "reason": "Quotes verbatim. The pipeline's own repair rules add that explanations must not contradict option text (iterate_repair_to_100.py line 194, added). Refines #59 by naming where facts hide; not a duplicate.",
   "statement": "Fact-check every field a student can see (explanations, hints, feedback, source details) and check that the key agrees with all of them.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "29",
     "quote": "- Factual claims, answer keys, rationales, feedback, and support fields all count for `factual_accuracy`.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "38",
     "quote": "- The keyed answer must be factually correct and internally consistent with all explanations, hints, feedback, and additional details.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/calibration/gold_standard.json",
     "lines": "460",
     "quote": "\"failure_reason\": \"Factual inconsistency: Question says 1946 (correct), but explanation says 1948 (incorrect)\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py",
     "lines": "194",
     "quote": "Answer explanations must not contradict option text.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 25,
   "verdict": "keep",
   "reason": "Quotes verbatim. The external judge's SAQ rules also ask for parts 'independently scorable, and connected' (prompt audit line 72, added). Contested by the API spec's scaffolding rule (against). Related to #41 and #68 (distinctness) and to #3 (no pre-answering).",
   "statement": "Make each question in a set, and each part of a multi-part question, answerable and scorable on its own; no part may pre-answer another.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/AP_GENERATOR_SPEC.md",
     "lines": "44",
     "quote": "**Rules**: 3-4 questions, different skills, independent answers",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
     "lines": "130",
     "quote": "| Parts (a) and (b) have some potential overlap — a strong answer to (a) could partially pre-answer (b... | 1 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-pass-contract-matrix.md",
     "lines": "127",
     "quote": "- parts that depend on one another in a way that blocks independent scoring,",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "72",
     "quote": "- Parts should be clear, usually labeled, independently scorable, and connected.",
     "verbatim": true
    }
   ],
   "against": "Another spec pulls the other way: '- Parts MUST be scaffolded (build on each other OR test related aspects)' (docs/GENERATOR_API_SPEC.md line 239).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "keep",
   "reason": "Quotes verbatim. The support is thin: one adopted rule and one judge note (count 1). 'Hard to mark' is the reader's gloss; the note says only that the part conflates two concepts. Kept as a standard item-writing rule.",
   "statement": "Ask for one task per part; a part that combines two tasks or two concepts is hard to mark.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/EVALUATION_API.md",
     "lines": "328",
     "quote": "- **NEVER** use compound verbs like \"identify AND describe\" in a single part",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
     "lines": "125",
     "quote": "| Part (c) conflates two distinct concepts — maritime technology development AND navigational skills —... | 1 |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep",
   "reason": "Quotes verbatim. In build 2, mcq_set failed 12 of 19, against 3 failures among the other 81 items. The repair rules later fixed one reasoning move per question (cause or context, comparison or continuity, consequence; iterate_repair_to_100.py lines 202-204, added). Same idea as #68 (a distinct element for each question sharing a source). Kept for the build-order method and the set failure counts. No run isolates the method's effect.",
   "statement": "For questions that share one source, choose the source first, list the distinct reasoning moves it supports, and write each question around a different move.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ap-history-ib-expectation-matrix.md",
     "lines": "122",
     "quote": "- Choose stimulus first, then create distinct child reasoning moves.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-pass-contract-matrix.md",
     "lines": "71",
     "quote": "- build set backwards from stimulus: identify distinct APUSH reasoning moves first, then write each child around a different move.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build2_eval/evaluation_report.md",
     "lines": "14",
     "quote": "- By type: {'dbq': {'total': 21, 'passed': 20, 'failed': 1}, 'leq': {'total': 21, 'passed': 21}, 'mcq': {'total': 21, 'passed': 20, 'failed': 1}, 'mcq_set': {'total': 19, 'passed': 7, 'failed': 12}, 'saq': {'total': 18, 'passed': 17, 'failed': 1}}",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py",
     "lines": "202",
     "quote": "Question 1 must ask for the outside historical cause or context that best explains the stimulus, not what the stimulus says.",
     "verbatim": true
    }
   ],
   "against": "none found; no run isolates the effect of the build order.",
   "general": true,
   "duplicate_of": "68",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (the rules.py quote is on line 64). Added the word-overlap cue that the repair rules target (line 191; also lines 208-209). Added to against: the pipeline's locked key order repeats across sets. Adds to #8.",
   "statement": "Make the right option impossible to spot from surface cues: similar length, grammatical fit with the stem, no absolute words, no 'all/none of the above', and no distinctive word that only the right option shares with the stem or source.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/mcq.py",
     "lines": "13",
     "quote": "- All options should be roughly similar in length",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/mcq.py",
     "lines": "20",
     "quote": "- Answer options should not give away the answer through grammar clues",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/hard_fail/rules.py",
     "lines": "64",
     "quote": "r'all\\s+of\\s+the\\s+above',",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py",
     "lines": "191",
     "quote": "Avoid reusing distinctive nouns, verbs, or historical labels from the stimulus in only the correct option.",
     "verbatim": true
    }
   ],
   "against": "The absolute-language word list also catches ordinary words, so a word filter can fail sound options: \"r'\\b(only|solely|exclusively)\\b',\" (ap_benchmark/hard_fail/rules.py line 38). And the pipeline's fixed key order, 'Use locked answer keys A, C, and B in that order.' (e2e_pipeline/iterate_repair_to_100.py line 201), balances each set but repeats one position pattern across every set, which is itself a surface cue.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 29,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, but 'against: none found' was wrong. The later repair rules forbid option-by-option rationales, so that part moves from the statement to against. The core (show the reasoning; restating is not explaining) is held by the local rubric (base.py lines 100, 103), by the pre-judge rule for trivial explanations (rules.py lines 72-77) and by the gold set.",
   "statement": "An answer explanation must show the reasoning that makes the keyed answer right; restating the answer is not an explanation.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/base.py",
     "lines": "100",
     "quote": "- Does the explanation teach WHY the answer is correct?",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/base.py",
     "lines": "103",
     "quote": "- FAIL if explanation just restates the answer",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/calibration/gold_standard.json",
     "lines": "365",
     "quote": "\"failure_reason\": \"Recall-only asking for date; explanation is just the answer repeated\"",
     "verbatim": true
    }
   ],
   "against": "Whether to explain each wrong option is contested. The local rubric asks '- Does it address why other options are wrong?' (ap_benchmark/prompts/base.py line 101). The later pipeline told the writer 'Prefer one concise explanation of why the keyed answer is correct instead of option-by-option rationales.' (e2e_pipeline/iterate_repair_to_100.py line 194) and '- Do not use option-by-option explanation text; explain only the keyed answer's reasoning.' (line 243).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 30,
   "verdict": "keep",
   "reason": "Quotes verbatim. 510 of 53,790 requests were classed definition_to_assessment, and the failure scenario is at plan line 156. An adopted rule; no run measures it.",
   "statement": "When the learning target is a definition, write a task in which the learner uses the idea; never paste the definition into the question.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/plans/2026-05-25-ap-history-request-expectation-mapping.md",
     "lines": "35",
     "quote": "- Definitional standards must be transformed into assessment tasks, not copied into stems.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ap-history-ib-expectation-matrix.md",
     "lines": "213",
     "quote": "- Definitional text rather than task verb: identify the concept as the content target; require generator to transform it into a reasoning task rather than copy the definition.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/request_expectations/ap_history_request_expectations_summary.md",
     "lines": "8",
     "quote": "- By reasoning mode: {'definition_to_assessment': 510, 'causation': 25695, 'statement_to_assessment': 4515, 'comparison': 5880, 'evidence_source_analysis': 105, 'contextualization': 465, 'continuity_change_over_time': 13320, 'explanation_general': 2910, 'evaluation_argument': 390}",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep",
   "reason": "Quotes verbatim (generator on Gemini, judge on Claude; EVALUATION_PROCESS.md lines 153-159). An adopted rule with no measurement. A special case of #43 (check against something that doesn't assume the answer), kept as added evidence from item judging.",
   "statement": "Judge generated items with a different model from the one that wrote them.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/EVALUATION_PROCESS.md",
     "lines": "5",
     "quote": "It uses Claude API (not the same model as the generator) to ensure impartial evaluation.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/EVALUATION_PROCESS.md",
     "lines": "155-158",
     "quote": "- Evaluator criteria should NOT be influenced by generator output",
     "verbatim": true
    }
   ],
   "against": "none found; no source measures same-model against different-model judging.",
   "general": true,
   "duplicate_of": "43",
   "name_bearing_source": false
  },
  {
   "index": 32,
   "verdict": "keep",
   "reason": "Quotes verbatim. A planned bake-off that never ran (against). Related to #70 and #51; not a duplicate.",
   "statement": "Judge a writing aid (a spec, contract or prompt) by the items it leads to, against a no-aid baseline on the same requests, not by how its own text reads.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/deterministic_compiler/parallel_experiment_note.md",
     "lines": "26",
     "quote": "The winner is not whichever contract sounds better. The winner is whichever path improves downstream InceptBench pass rate, retry count, cost, and failure distribution when feeding the same APUSH/APWH/APEuro benchmark requests into the same generator.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/deterministic_compiler/README.md",
     "lines": "29-31",
     "quote": "1. No helper baseline.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/deterministic_compiler/README.md",
     "lines": "46",
     "quote": "The deterministic compiler wins by measured downstream outcomes, not by sounding clever.",
     "verbatim": true
    }
   ],
   "against": "At planning time the comparison had not run, and no result was found in scope: '- No no-compiler baseline or compiler A/B harness has run.' (plans/2026-05-25-ib-pattern-compiler-prelaunch-revision.md line 61).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 33,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. LEQ passed 100% in all twelve summary reports (200 of 200, 120 of 120) and 21 of 21 in every pipeline build; the pack finds no load-bearing criterion; and the gold set holds no LEQ case. Added a third possibility that the sources show for DBQ: 97.4% passed while document authenticity got full marks on 14.7% (see candidate 1). Added to against: two detailed runs did fail LEQs. The same move as #38 (a check that never fired proves nothing until it catches a planted fault); kept as added evidence.",
   "statement": "When one item format passes a judge almost every time, find out whether the items are good, the judge has nothing it can fail them on, or the pass rule ignores what the judge finds.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/evaluation_20260225_081919_0909a798.md",
     "lines": "33",
     "quote": "| LEQ      |    200 |      0 |      0 |    100.0% |      1.00 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-pack-audit.md",
     "lines": "56",
     "quote": "- No load-bearing criterion in the pack.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
     "lines": "80",
     "quote": "LEQ is comparatively lenient but still needs clean structure.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/evaluation_20260225_081919_0909a798.md",
     "lines": "34",
     "quote": "| DBQ      |    186 |      5 |      0 |     97.4% |      0.87 |",
     "verbatim": true
    }
   ],
   "against": "In two later detailed runs the judge did fail essay prompts: '| LEQ | 8 | 3 | 0 | 72.7% |' (docs/reports/detailed_report_20260226_115508.md line 24) and '| LEQ | 9 | 3 | 0 | 75.0% |' (docs/reports/detailed_report_20260226_124949.md line 24).",
   "general": true,
   "duplicate_of": "38",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/detailed_report_20260226_115508.md",
   "lines": "110",
   "quote": "The answer options (A, B, C, D) are entirely missing from the submission.",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/official_ap_formatters.py",
   "lines": "100-101",
   "quote": "lines.append(\"*No options provided*\")",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/detailed_report_20260226_115508.md",
   "lines": "21",
   "quote": "| MCQ | 0 | 12 | 0 | 0.0% |",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/detailed_report_20260226_124949.md",
   "lines": "21",
   "quote": "| MCQ | 11 | 1 | 0 | 91.7% |",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/base.py",
   "lines": "351",
   "quote": "content = content[:8000] + \"\\n\\n... [truncated for evaluation]\"",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/calibration/validator.py",
   "lines": "81-116",
   "quote": "difficulty=example.question_dict.get(\"difficulty\", \"medium\"),",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/calibration/gold_standard.json",
   "lines": "296-308",
   "quote": "\"failure_reason\": \"Too easy for 'hard' difficulty; requires no analysis\"",
   "ok": true
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/core/evaluator.py",
   "lines": "167-168",
   "quote": "return DimensionScore(score=1.0, reasoning=default_reasoning, issues=[])",
   "ok": true
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/core/evaluator.py",
   "lines": "446",
   "quote": "error_score = DimensionScore(score=0.0, reasoning=f\"Evaluation error: {str(e)}\", issues=[])",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/evaluation_20260225_155759_209babe7.md",
   "lines": "11-14",
   "quote": "| Passed | 33 (61.1%) |",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_repair_loop_clean4/loop_summary.jsonl",
   "lines": "2",
   "quote": "\"api_missing_evaluation\": 1",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/base.py",
   "lines": "28",
   "quote": "**When in doubt, FAIL the question. Missing problems is worse than over-flagging.**",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/base.py",
   "lines": "52-60",
   "quote": "Be THOROUGH. Find every problem.",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports - not ok: a low full-score rate alone does not show the judge's flags were spurious",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
   "lines": "79",
   "quote": "| distractor_quality        |   69 |  152 |     31.2% |      0.35 |",
   "ok": false
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
   "lines": "174-176",
   "quote": "It does not represent a genuine student misconception and therefore weakens distractor quality.\", 'severity': 'minor'",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
   "lines": "118",
   "quote": "| No significant structural or validity issues identified. | 2 |",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
   "lines": "23",
   "quote": "- Default evaluator stance is pass, but mandatory audits in overlays override that leniency.",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/test_server.py",
   "lines": "206",
   "quote": "Some evaluations differ (may be due to LLM variance)",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports - not ok: the zeroed criterion is distractor quality, not a key or a fact (it bears on candidate 1, not #59)",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
   "lines": "155-158",
   "quote": "- **Dimensions:** factual_accuracy=1.0, answer_validity=1.0, stimulus_alignment=1.0, distractor_quality=0.0, skill_alignment=1.0, clarity=1.0",
   "ok": false
  },
  {
   "truth": 59,
   "effect": "supports - not ok: the zeroed criterion is stimulus integration, not a key or a fact",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/evaluation_20260225_081919_0909a798.md",
   "lines": "152-155",
   "quote": "- **Dimensions:** prompt_structure=1.0, historical_specificity=1.0, answerability=1.0, skill_alignment=1.0, stimulus_integration=0.0, scoring_clarity=1.0",
   "ok": false
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
   "lines": "19",
   "quote": "The practical rule for the generator is: **do not aim for “mostly good”; produce a checklist-complete item with no score-zero openings.**",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports - not ok: #28 is about students skipping lesson checks; a writer-side format assertion does not bear on it (it fits #67)",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN4_REPORT.md",
   "lines": "212-217",
   "quote": "assert response.format == \"fill-in\"",
   "ok": false
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/EVALUATION_PROCESS.md",
   "lines": "127",
   "quote": "Hard fails trigger BEFORE the API call, saving time and money.",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN4_REPORT.md",
   "lines": "24",
   "quote": "**15 out of 26 curriculum alignment failures (58%) are due to FORMAT MISMATCH.**",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN2_REPORT.md",
   "lines": "181-187",
   "quote": "**Problem:** Question frames settlement houses as a Gilded Age phenomenon when the curriculum explicitly states they were Progressive Era (1890s-1920s). The Gilded Age ended around 1898.",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
   "lines": "126",
   "quote": "| Minor note: The curriculum context lists the time period as 'late 19th century,' which contradicts t... | 1 |",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN2_REPORT.md",
   "lines": "30",
   "quote": "The dramatic improvement in curriculum alignment (43% → 89%) confirms the endpoint is now properly utilizing the `learning_objective` and `statement` fields provided in requests.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_FAILURE_REPORT.md",
   "lines": "33",
   "quote": "The generator ignores the specific `learning_objective` and `statement` provided in the request. Instead, it produces generic questions about the broad topic area.",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_FAILURE_REPORT.md",
   "lines": "30",
   "quote": "**65 out of 79 failed questions** had curriculum alignment issues. This is the **dominant failure mode**.",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports - not ok: a writer-side scope rule, not a check",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/GENERATOR_API_SPEC.md",
   "lines": "123-124",
   "quote": "- The question MUST NOT require knowledge outside the scope of this fact (except for scaffolding context)",
   "ok": false
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_repair_loop_clean4/loop_summary.jsonl",
   "lines": "2-3",
   "quote": "{\"round\": 2, \"evaluated\": 100, \"passed\": 87, \"failed\": 13, \"pass_rate\": 0.87, \"zero_metrics\": {\"difficulty_alignment\": 2, \"distractor_quality\": 2",
   "ok": true
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
   "lines": "101",
   "quote": "- Parent factual accuracy fails if any child has a factual failure.",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
   "lines": "107",
   "quote": "- Answer balance for MCQ_SET uses structured extraction plus chi-square; p >= 0.60 passes, otherwise fails.",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_repair_loop_clean3/loop_summary.jsonl",
   "lines": "1",
   "quote": "\"failed\": 32, \"pass_rate\": 0.68, \"zero_metrics\": {\"answer_balance\": 15",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/msq.py",
   "lines": "22",
   "quote": "- Each correct answer must be independently correct",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md",
   "lines": "22-27",
   "quote": "| answer_validity | 146 |",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN3_REPORT.md",
   "lines": "63",
   "quote": "- Result: Questions are either too simple (cognitive fail) or too complex (difficulty fail)",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN3_REPORT.md",
   "lines": "346",
   "quote": "**Failed:** cognitive_demand: \"Requires sophisticated analysis of ideological contradictions, exceeding basic comprehension level\"",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/BENCHMARK_RUN5_REPORT.md",
   "lines": "32",
   "quote": "**Key observation:** Run 5 fixed easy difficulty (27% → 68%) but broke hard difficulty (58% → 38%) and cognitive demand (70% → 59%).",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/calibration/validator.py",
   "lines": "4-5",
   "quote": "Ensures >= 95% accuracy to catch evaluator drift over time.",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports - not ok: raw text is kept only when parsing fails; successful verdicts are stored parsed, so this is not keeping every judgment whole",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/benchmark_official.py",
   "lines": "228-231",
   "quote": "\"raw_response\": text if 'text' in dir() else None,",
   "ok": false
  },
  {
   "truth": 50,
   "effect": "supports - not ok: echoing the target standard's id unchanged is not recording an asset's source or hash",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/GENERATOR_API_SPEC.md",
   "lines": "41",
   "quote": "MUST be echoed back unchanged. MUST NOT be transformed or auto-generated.",
   "ok": false
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
   "lines": "108",
   "quote": "- Factual audit can downgrade `factual_accuracy` by merging audit result via min(main, audit).",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/docs/reports/LATEST.md",
   "lines": "124",
   "quote": "| The preamble/stimulus text is somewhat leading and may inadvertently scaffold answers for parts (a) ... | 1 |",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluator/ap_benchmark/prompts/official_ap_prompts.py",
   "lines": "136-139",
   "quote": "- FAIL if questions can be answered without the stimulus",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-pass-contract-matrix.md",
   "lines": "131",
   "quote": "- specify what earns credit without narrowing valid student phrasing too much.",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-ap-history-ib-expectation-matrix.md",
   "lines": "162",
   "quote": "- Expected-response/rubric criteria are specific enough to grade and flexible enough to accept valid variants.",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/deterministic_compiler/package_report.md",
   "lines": "56",
   "quote": "- Test names show coverage for evaluator prompt rules, factual audit gating, stimulus promise/reference detection, stem redundancy, extraneous-topic guards, and MCQ-set behavior.",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md",
   "lines": "97-98",
   "quote": "- Each question should test a distinct aspect of the stimulus.",
   "ok": true
  }
 ]
}
```
