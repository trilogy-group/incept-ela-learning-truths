# verify:social-studies

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "social-studies",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim at the cited lines. The original's 'several times what an independent judge gave the same day's items' rests on the 56% self-graded vs 9.1% external figures. The project itself put part of the 9.1% down to a different batch and JSON parse failures. Its own estimate of the inflation is 10-17%, and on a shared 14-item sample the gap was 29% vs 21%. I narrowed the claim and added the headline disclosure (BENCHMARK_ACHIEVED.md line 10) and CLAUDE_CROSS_EVAL_REPORT.md line 194. Related to 43 and 44 but distinct: it is about keeping the writer and the grader separate.",
   "statement": "Don't let the model that wrote the items be their only grader: its self-grades ran higher than an independent model's (the project put the inflation at 10-17%), and it passed items whose explanations contradicted the key.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/DECISIONS.md",
     "lines": "6",
     "quote": "- Gemini was grading Gemini (self-grading)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/DECISIONS.md",
     "lines": "7",
     "quote": "- Pass rates were inflated by 10-17%",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/CLAUDE_CROSS_EVAL_REPORT.md",
     "lines": "164",
     "quote": "Questions Q36, Q44, and Q46 have explanations that contradict their answer keys. Gemini passed Q36 and Q44 despite this critical flaw.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/CLAUDE_CROSS_EVAL_REPORT.md",
     "lines": "194",
     "quote": "Gemini scores content_accuracy at 1.0 for several questions where the explanation contradicts the answer.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/BENCHMARK_ACHIEVED.md",
     "lines": "10",
     "quote": "**The 95.2% benchmark used Gemini self-evaluation, NOT Claude external evaluation.**",
     "verbatim": true
    }
   ],
   "against": "The larger gap is confounded (HOLISTIC_REVIEW_2026-02-19.md line 202: \"| Feb 17 AM | 56% | Gemini self-grading (meaningless) |\", against 9.1% external): CLAUDE_VS_GEMINI_EVAL.md lines 80-82 put the 9.1% partly down to a different question batch and JSON parsing issues. On the same 14 items the self-grader was only slightly more lenient (CLAUDE_CROSS_EVAL_REPORT.md line 17: \"| Questions Passed | 4/14 (29%) | 3/14 (21%) | 71% |\"), and CLAUDE_MANUAL_REVIEW.md line 10 argued the external judge was too strict. The independent judge was never itself scored against person-labelled items.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. The claim that a later judge version reversed the criterion is not supported: the uniform-difficulty diagnosis (Gate 12b, IB v2.4.0, model_findings.md line 1071) and the progressive change (Gate 13: same model, prompt-only changes) ran back to back. I restated it as: test what a criterion rewards before rebuilding items for it. PLAN-finetune-qwen.md line 520 is verbatim but no longer needed. Distinct from 37 and 45: it is about misreading an outside judge's criterion from its failure messages.",
   "statement": "Before rebuilding items to satisfy a judge's criterion, test what that criterion rewards on controlled examples: a difficulty criterion was read as failing item sets of uniform difficulty, the sets were made progressive, and that criterion's share of set failures rose from 50% to 86% with the same model and prompt-only changes, so the change was reverted.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "1125",
     "quote": "**Why MCQ_SET regressed (-10.8pp):** Generator prompt mandated uniform difficulty → evaluator's difficulty_distribution hard-fails.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "1137",
     "quote": "Gate 13 running immediately after fixes. Same model (sft-v3-14b), same N=100, prompt-only changes.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "1176",
     "quote": "The progressive difficulty change caused `difficulty_distribution` to jump from **50% → 86%** of MCQ_SET failures.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "1176",
     "quote": "The evaluator does NOT want Q1<Q2<Q3 difficulty — it wants all 3 at the SAME stated difficulty level.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md",
     "lines": "17",
     "quote": "The difficulty distribution is narrow; there are no 'Easy' questions present, and over 60% of the quiz sits at the Medium level. This lacks the progression needed for effective differentiation.",
     "verbatim": true
    }
   ],
   "against": "A separate benchmark's judge was read the same way (unit_1/diagnosis.md line 17), so the misreading was shared rather than a one-off. The judge flips verdicts on identical item sets often (python/CLAUDE.md line 101: \"DBQ flips 30%, MCQ_SET 50%\"), so part of the 50%-to-86% shift may be noise.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. The original's '14-50 points with nothing changed' overstated: the 50-point gap compared a 12-item check that skipped the cognitive-demand criterion with the full 116-item run. The measured swings in unchanged types were 14-25 points on 13-24 items. I corrected the numbers and the RUN7_BLUEPRINT line (1005 to 1006). Distinct from 34 (judge noise on the same items) and 15 (student adaptation).",
   "statement": "Don't judge a change from a dozen items: with 13 to 24 items per type, pass rates of item types that hadn't changed swung by 14 to 25 points between runs, and a 12-item check that skipped one criterion scored 100% where the 116-item run scored 50.0%; size samples to the difference you need to see and use unchanged types as the noise floor.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "413",
     "quote": "4. **SAQ improvement (+25pp) is sampling variance.** Only 13 SAQ items in this run. No SAQ-specific changes made. Not a real improvement.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "1260",
     "quote": "4. **MCQ_SET and DBQ high variance**: With 17 and 24 items respectively, a 5-8 item swing produces ±14pp swings. Not statistically meaningful at N=17-24.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "1169",
     "quote": "| SAQ | 50.0% | 40.0% | -10.0pp | Variance (SAQ prompt unchanged) |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/RUN6_ANALYSIS.md",
     "lines": "10",
     "quote": "**Mini benchmark (100%) was misleading.** Comprehensive benchmark revealed cognitive demand collapse.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/RUN6_ANALYSIS.md",
     "lines": "14",
     "quote": "| Run 6 Mini | 12 | 100% | Not evaluated |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/RUN6_ANALYSIS.md",
     "lines": "15",
     "quote": "| Run 6 Comprehensive | 116 | **50.0%** | **51%** |",
     "verbatim": true
    }
   ],
   "against": "The project kept deciding on small samples: winners were declared on 10 items (EXPERIMENT_RESULTS_2026-02-18.md line 15: \"| **Two-Stage Generation** | **100%** (10/10) | ✅ WINNER |\"), and the blueprint kept a 12-question check for iteration (RUN7_BLUEPRINT.md line 1006: \"- 12 questions\"). The 12-item check did not evaluate cognitive demand (RUN6_ANALYSIS.md line 14), so its 100% reflects a missing criterion as well as sample size.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep-with-fix",
   "reason": "Quotes and numbers are verbatim (99.3%, 90.0%, -11pp). 'With no change to the generator' overstated the source, which says only that the drop was 'not a code regression'; I reworded it and added line 249, which gives the second run's mix. Distinct from 49 and 60.",
   "statement": "Compare pass rates only between runs with the same mix of requests: one item type fell from 99.3% to 90.0% when the second run asked only for a unit the first run never requested, and the drop was traced to the test mix, not the code.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
     "lines": "248",
     "quote": "The 99.3% LEQ pass rate (run `fda3ba0f`) had **zero APUSH-5 LEQ** requests.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
     "lines": "249",
     "quote": "The 90.0% LEQ pass rate (run `ee6fb4af`) was **100% APUSH-5 LEQ** requests.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
     "lines": "251",
     "quote": "This is not a code regression but a test distribution change revealing an existing issue with APUSH Unit 5's time period (1844-1877) conflicting with topics like \"Reconstruction\" (1865-1877).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "571",
     "quote": "MCQ apparent regression (-11pp) is explained by sampling variance: Gate 3 included harder MCQ items (APWH, APEURO hard-difficulty).",
     "verbatim": true
    }
   ],
   "against": "A changed mix can also expose a real defect: the 90.0% run revealed a genuine conflict between a unit's period and a topic (IMPROVEMENT_PROPOSALS.md line 251), so the drop was informative even though it was not a regression.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. I tallied all eight REVERTED entries (changelog.md lines 158, 462, 624, 786, 930, 1075, 1433, 1560). Control regression ran from 5.1% to 54.9%, and seven batches gained +3.6 to +4.6 points while one lost 7.1. The original's '5-55%' and 'every batch raised the rate' are corrected to the source values. Distinct from 60 and 70: it is regression testing on items that already passed.",
   "statement": "After every change, re-run a control set of items that already passed: in one improvement loop, seven of eight batches of prompt edits raised the measured pass rate by 3.6 to 4.6 points, yet every batch showed a control regression of 5.1% to 54.9%, over the 3% limit, and all eight were reverted.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/changelog.md",
     "lines": "157",
     "quote": "**Before:** 94.8% | **After:** 87.7% | **Control regression:** 54.9%",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/changelog.md",
     "lines": "462",
     "quote": "**Status:** REVERTED ✗ — control regression 7.1%, improvement +4.6%",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/changelog.md",
     "lines": "624",
     "quote": "**Status:** REVERTED ✗ — control regression 6.9%, improvement +3.6%",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/changelog.md",
     "lines": "1433",
     "quote": "**Status:** REVERTED ✗ — ctrl regression 5.1%",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/agents/retester.md",
     "lines": "39",
     "quote": "- Control group regression > 3% (signs of overfitting/regression), OR",
     "verbatim": true
    }
   ],
   "against": "The judge flips verdicts on identical generations (python/CLAUDE.md line 101: \"The InceptBench evaluator has a **20% rating-flip rate** on identical generations across 4 repeated trials.\"), so control regressions of 5.1% to 9.0% against a 3% limit may be judge noise rather than real regressions. A limit set below the judge's noise reverts every change. Control samples were small (python/CLAUDE.md line 192: \".venv/bin/python -m benchmark.retest --unit 1 --concurrency 30 --control-pct 15\").",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep",
   "reason": "Quotes and numbers are verbatim (89%, 5,219/5,878; 81.9% to 97% on the tuned 28 files). This is a general rule for evaluating generators on held-out material, distinct from 48 (student learning) and 66 (selection bias).",
   "statement": "Confirm a fix on material it was not tuned on, and keep the requests used for evaluation out of anything used to build or tune the generator.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "135",
     "quote": "- **89% (5,219/5,878) prompts identical to training prompts** (500-char fingerprint match)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/CLAUDE.md",
     "lines": "466",
     "quote": "5. Only checkpoint if improvement holds across 2+ units",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/OPTIMIZATION_LOG.md",
     "lines": "42",
     "quote": "**Problem:** Gen 1 winner tested on easy topics. Needed harder topics.",
     "verbatim": true
    }
   ],
   "against": "The 97% headline was measured on the same 28 files the push was tuned against (python/CLAUDE.md line 7: \"raised the 28-file benchmark pass rate from **81.9% to 97%** (reported)\"), so it is not a held-out figure.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep",
   "reason": "Quotes are verbatim, and 70.7%, 94.0%, 43.3% and 100% match CHANGELOG_RELENTLESS.md lines 158-163. Adds a fail-closed rule to 63, which only says to check the labels.",
   "statement": "Never let a missing or unrecognised course or unit label fall back to a default; stop the request instead, because a silent default sent every request for one course through another course's content and skipped its scope rules.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
     "lines": "120",
     "quote": "`parse_substandard(\"KC-4.1.VI+1+D\")` in the generator code doesn't match any of the regex patterns for course detection (USH/WH/EH/MAC/MIC/GOV/HG/EURO prefix). It silently falls through to the default: `{course=\"APUSH\", unit=1}`.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
     "lines": "145",
     "quote": "So `ctx.course` came back as \"APUSH\" for all APWH items. Because `ctx.course != \"APWH\"`, the `_build_apwh_unit_guidance()` function added in commit 2 was **silently skipped** for every APWH request.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
     "lines": "163",
     "quote": "APWH u3 going from 43.3% to 100% with 0 hard-fails is the definitive proof that the KC-prefix routing chain (commits 3+4+2) was the root cause.",
     "verbatim": true
    }
   ],
   "against": "The 70.7%-to-94.0% gain is cumulative over several commits (CHANGELOG_RELENTLESS.md line 139: \"**Pass rate:** APWH 83% -> 94% (+23.3 pp cumulative from baseline 70.7%)\"), so not all of it comes from removing the default.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep",
   "reason": "Quotes are verbatim. 2/50, 30% (6/20) and 75% (6/8) are confirmed; I added line 396 for the 30% baseline. Related to 57 but about retrieval granularity.",
   "statement": "Retrieve source material for an item by its exact topic or objective, not by its broad unit or period; matching only by unit handed the writer the wrong sources.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "407",
     "quote": "1. **Topic mismatch is the root failure cause.** Bank indexed by (course, unit) — 50 entries spanning 30+ years and multiple topics. A \"Failure of Reconstruction\" request had only 2/50 chance of getting Reconstruction documents.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "396",
     "quote": "| DBQ  | 14% (3/22)      | **30% (6/20)**      | +16pp |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "421",
     "quote": "**75%** | 0.944 | +45pp ✅ PASS",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/CHANGELOG.md",
     "lines": "151",
     "quote": "We were doing fuzzy topic-based MongoDB search and sometimes getting irrelevant facts.",
     "verbatim": true
    }
   ],
   "against": "The 75% rests on 8 items (model_findings.md line 421), so the size of the gain is uncertain.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep",
   "reason": "Quotes are verbatim (3/5 and 2/5 zero-score root causes). Overlaps 17 (quote exactly) and 57 (verified facts), but adds that recasting invented sources as paraphrase or 'a historian argues' removed the false attribution, not the false content. I added python/CLAUDE.md line 130 as a second fabrication case.",
   "statement": "Never show students generated text presented as a real person's words or a real document; supply verified sources instead, because recasting invented sources as paraphrase removed the false attribution but not the false content.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "520",
     "quote": "- 3/5 = fabricated stimulus (invented pamphlet, fabricated Locke paraphrase, invented \"New Englanders\" excerpt) — anti-fabrication constraint PARTIALLY effective",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "521",
     "quote": "- 2/5 = \"A historian argues...\" format correct, but factual content of the argument wrong — constraint eliminated format-fabrication but not content-fabrication",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/CLAUDE.md",
     "lines": "591",
     "quote": "- Think: \"What WOULD they have written?\" not \"What DID they write?\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/CLAUDE.md",
     "lines": "130",
     "quote": "Fabricated poem falsely attributed to Wilfred Owen",
     "verbatim": true
    }
   ],
   "against": "The subject spec allowed invented sources (08-AP-SOCIAL-STUDIES-SPEC.md line 152: \"- Primary source excerpts must be authentic or authentically styled\"), and the copyright filter blocks verbatim recall (python/CLAUDE.md line 584: \"The model tries to reproduce actual quotes and triggers copyright filters.\"). Real excerpts therefore have to come from a vetted bank, not from the model.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep",
   "reason": "Quotes are verbatim (7 of 30, 23%; the validator's default return True). I added CLAUDE_CROSS_EVAL_REPORT.md line 194 for 'lenient judges passed it'. Distinct from 59 and 67 as a specific code check.",
   "statement": "Check in code that each explanation endorses the keyed option and no other, and fail the item when the check can't tell; an explanation that contradicts the key misleads like a wrong fact, and lenient judges passed it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/MCQ_BUG_HISTORY.md",
     "lines": "6",
     "quote": "This bug caused 7 out of 30 questions (23%) to fail in Claude cross-evaluation, making it a critical quality blocker.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/MCQ_BUG_HISTORY.md",
     "lines": "80",
     "quote": "return True  # ← WRONG! Should be False to trigger regeneration",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/CLAUDE_CROSS_EVAL_REPORT.md",
     "lines": "197",
     "quote": "- This is functionally equivalent to a factual error",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/CLAUDE_CROSS_EVAL_REPORT.md",
     "lines": "194",
     "quote": "Gemini scores content_accuracy at 1.0 for several questions where the explanation contradicts the answer.",
     "verbatim": true
    }
   ],
   "against": "Pattern checks only catch explicit letter phrases. An explanation can argue for a wrong option without naming it (python/benchmark_runs/analysis_iter1.md line 79: \"The explanation for why D is wrong actually confirms why D could be correct\").",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim (all 'B'; 9/10). The 'spread the key' half duplicates 8, so I restated the candidate around its new part: keep explanation letters in sync with the final option order. I added DECISIONS.md lines 35-36, which describe the desync directly.",
   "statement": "Fix the option order, with the key's position chosen in code, before the explanation is written, or rewrite every letter reference after any later shuffle: shuffling options after the explanation was written left explanations naming the wrong letter, and a writer left to place the key put nearly every key on one letter.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/DECISIONS.md",
     "lines": "35",
     "quote": "- Bug: Explanation generated before shuffle said \"Option A is correct\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/DECISIONS.md",
     "lines": "36",
     "quote": "- After shuffle, answer became \"C\" but explanation still said \"A\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/TECHNICAL-DECISIONS.md",
     "lines": "106",
     "quote": "Fixed answer bias (all answers were \"B\") by shuffling options after generation.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/EXPERIMENT_RESULTS_2026-02-18.md",
     "lines": "118",
     "quote": "- Lower temperature made answer bias worse (9/10 picked \"B\")",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/DECISIONS.md",
     "lines": "49",
     "quote": "- No post-hoc shuffling that can desync answer/explanation",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/EXPERIMENT_RESULTS_2026-02-18.md",
     "lines": "15",
     "quote": "| **Two-Stage Generation** | **100%** (10/10) | ✅ WINNER |",
     "verbatim": true
    }
   ],
   "against": "Each experiment had 10 items. A shuffle done in code with every letter reference rewritten also passed 10 of 10 (EXPERIMENT_RESULTS_2026-02-18.md line 17: \"| **Fixed Position + Shuffle** | **100%** (10/10) | ✅ WINNER |\"), so keeping the explanation and key in sync matters more than the order of the steps.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. The original's 'never related but distinct ideas' fits single-answer parts. It does not fit open 'give one example' parts, which the official guidelines mark with lists of distinct examples (CED line 12660), so I scoped the statement to single-answer parts. Distinct from 10.",
   "statement": "When a part has one intended answer, accept only different wordings of that answer, not related but distinct ideas or a broader or narrower category; mixed lists made marking inconsistent.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/evaluation_audit.md",
     "lines": "69",
     "quote": "4. The accepted answers (popular sovereignty, consent of governed, social contract) are related but distinct concepts, creating grading inconsistency",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter2.md",
     "lines": "40",
     "quote": "Part (a) scoring criteria lists both 'Compromise of 1877' and 'Reconstruction' as acceptable answers, which creates an internal contradiction",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/failures_20260226_172346.md",
     "lines": "79",
     "quote": "- Part (a) scoring accepts 'Martin Luther' or '95 Theses' as equivalent to 'Protestant Reformation,'",
     "verbatim": true
    }
   ],
   "against": "Parts that ask for one example out of many rightly accept several distinct answers, and official scoring guidelines list them (ap-european-history-ced.pdf, pdftotext -layout line 12660: \"Examples that earn this point include the following:\"). The writer instructions pushed for inclusive lists (python/generators/saq.py lines 232-233: \"⛔ SCORING INCLUSIVENESS: If a reasonable AP student could cite evidence X and it's\" / \"factually correct AND relevant to the prompt, it MUST be in the acceptable list.\").",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim (191, 35%). 'Options of telling length' had no evidence, so I added best_practices.md lines 54 and 57 (adopted guidance, not measured). The original 'against' said the ban was later 'enforced in code'; the cited line says only that it lacked enforcement, so I corrected it. The 35% is of 553 generated items, not the 582 requested. Distinct from 3 and 5.",
   "statement": "Check that an item can't be answered from cues inside it: surrounding words that define the answer, extreme words that mark options as false, or options of telling length.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/python/docs/EVALUATION-RESULTS-2026-02-23.md",
     "lines": "34",
     "quote": "**Frequency:** 191 questions (35% of all generated)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/failure_analysis.md",
     "lines": "28",
     "quote": "Question stems provide so much context that students can identify the answer without demonstrating historical thinking skills.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/archive/OPENCLAW_HUMAN_REVIEW.md",
     "lines": "34",
     "quote": "Option A (\"immediate collapse\") is a weak distractor — students could eliminate it by word choice alone",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/best_practices.md",
     "lines": "54",
     "quote": "| Absolute words (always, never, all, none) | Too easily eliminated |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/best_practices.md",
     "lines": "57",
     "quote": "| Options significantly longer/shorter than key | Provides visual cues |",
     "verbatim": true
    }
   ],
   "against": "A word ban is blunt: validation_rules.md line 193 fails a true statement (\"| \"The Civil War resulted in the **complete abolition** of slavery\" | ❌ FAIL: \"complete\" + \"abolition\" |\"). The prompt's banned-word list had no enforcement and absolute language still appeared in 35% of items (improvement_plan_prompts.md line 15: \"| Absolute language | 35% | BANNED WORDS list exists but lacks enforcement mechanism |\"); no rate after enforcement is recorded.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. 'Measure nothing' overstated the cited finding, which is only that misconception-based options beat similarity-based ones, so I softened it. I added the adopted rule (best_practices.md line 28), the non-functioning-distractor note (line 45) and an audit row showing the generated options were not misconception-based. The research claim is as summarised in the project's notes (arXiv:2501.13125); I did not check it against the paper (no network).",
   "statement": "Build each wrong option from a misconception students actually hold, so that some students choose it; options nobody would pick only make the item easier to answer by elimination.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/best_practices.md",
     "lines": "28",
     "quote": "- Each distractor should target a specific student misconception or common error",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/best_practices.md",
     "lines": "45",
     "quote": "- Non-functioning distractors (never selected) indicate poor design",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/best_practices.md",
     "lines": "69",
     "quote": "**Key Finding**: Distractors generated by predicting student choice behavior significantly outperform those generated by similarity-based methods.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/best_practices.md",
     "lines": "395",
     "quote": "- Lee, Y. et al. (2025). Generating Plausible Distractors via Student Choice Prediction. arXiv:2501.13125.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md",
     "lines": "24",
     "quote": "Q1-D (declaring war over the Treaty of Tordesillas) is easily eliminated and does not reflect a realistic student misconception.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/COMPREHENSIVE-AUDIT-2026-02-18.md",
     "lines": "81",
     "quote": "| Distractor Quality | C | Plausible but not misconception-based |",
     "verbatim": true
    }
   ],
   "against": "No student responses were ever collected, so the test of whether a distractor works (best_practices.md line 44: \"- Each should be selected by at least 5% of test-takers\") was never applied; plausibility was judged only by models.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "drop",
   "reason": "Quotes are verbatim, but the only evidence is an automated judge's verdicts on distractors. In ordinary formats a wrong option is necessarily a false statement: for 'which describes the Virginia Plan?', a misdescription is the distractor. The project's own select-all rule demands factually false wrong answers (failure_analysis.md line 119), and nothing shows students were misled. The statement generalises one judge's preference and is not a general truth.",
   "statement": "Make each wrong option wrong as an answer to the question asked, not a false statement of fact; options that asserted invented facts were failed as factual errors that could mislead.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md",
     "lines": "34",
     "quote": "Option B in Question 3 contains a clear factual error: African American Exodusters were not legally barred from settling in Kansas.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/failures_20260226_181058.md",
     "lines": "11",
     "quote": "Option D contains a factual inaccuracy: Germany did not fully seize the Caucasus oil fields.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_3/diagnosis.md",
     "lines": "49",
     "quote": "A factual error is present in Question 3, where a distractor incorrectly describes the Virginia Plan as advocating for a unicameral legislature.",
     "verbatim": true
    }
   ],
   "against": "For select-all items the project's own analysis asked for the opposite (failure_analysis.md line 119: \"4. Wrong answers must be FACTUALLY FALSE statements, not \"distractors\"\"), so the rule depends on the item format.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep",
   "reason": "Quotes are verbatim; this is an adopted item-writing rule. The item with no stem was passed by both judges (CLAUDE_CROSS_EVAL_REPORT.md line 82: \"- **Claude Score:** 0.88 - Pass with minor issues\"), so the check can't be left to judges.",
   "statement": "Write the stem as a complete question that can be understood before the options are read.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/best_practices.md",
     "lines": "381",
     "quote": "- [ ] **Clear stem**: Question understandable without reading options",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/best_practices.md",
     "lines": "159",
     "quote": "**Fix**: Review stems independently before adding options",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/CLAUDE_CROSS_EVAL_REPORT.md",
     "lines": "80",
     "quote": "- ⚠️ Missing question stem (what exactly is being asked?)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "keep-with-fix",
   "reason": "Quotes and numbers are verbatim (86% to 62%; 51% cognitive-demand pass). 'How familiar the material is' had no evidence, so I removed it. I added HANDOFF-finetune-status.md line 69, which says the labels changed but the content didn't.",
   "statement": "Set difficulty by the reasoning an item demands (how many steps, how much synthesis), not by a label: difficulty labels added without different content didn't produce different difficulty, and removing context from hard stems turned them into recall instead of making them harder.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/HANDOFF-finetune-status.md",
     "lines": "69",
     "quote": "**Why it failed:** The difficulty labels were added but content difficulty doesn't vary.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/HANDOFF-finetune-status.md",
     "lines": "71",
     "quote": "**Lesson:** Label injection without content variation teaches nothing. The model needs examples with structurally different question types at each difficulty level.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/RUN6_ANALYSIS.md",
     "lines": "41",
     "quote": "**ACTUAL:** Questions became cognitively shallow recall exercises",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
     "lines": "104",
     "quote": "\"What would X group think?\" pattern is single-step reasoning.",
     "verbatim": true
    }
   ],
   "against": "An earlier lesson in the same project said the reverse (ITERATION_ANALYSIS.md line 181: \"> **Hard questions must require RECALL, not READING.** Scaffolding makes hard questions into medium questions.\"). One review accepted heavy support for weaker students (evaluation_audit.md line 109: \"However, for a practice fill-in, this level of scaffolding might be acceptable for struggling students.\"). The 86%-to-62% drop came from a retrain that also regressed other item types (HANDOFF-finetune-status.md line 70), so it is not a clean test of labels.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 17,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim, and python/CLAUDE.md line 113 is confirmed. The same objective (Inca Empire) drew one failure for leaving it out and another for including it as outside the course, a request no item can satisfy. I reworded the statement so its examples describe the judge's rulings accurately and added the 'easy' DBQ example (unit_1/diagnosis.md line 60). This is the request-side analogue of 39.",
   "statement": "When a request contradicts itself or the course's scope (an objective the judge rules outside the course, a difficulty the task type can't have), or when different generators fail it the same way, fix or reject the request before changing the generator.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "829",
     "quote": "Both models hard-failed at the same DBQ item (item 33) — confirming some eval samples are intrinsically difficult (wrong unit mapping, impossible spec, or IB v2.4.0 edge case).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md",
     "lines": "50",
     "quote": "The question fails to address the specific learning objective requested (Inca Empire) and instead focuses on a different group (Pueblo peoples).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md",
     "lines": "100",
     "quote": "The question targets the wrong curriculum. AP US History focuses on societies in what is now the United States; the Inca Empire is a South American civilization assessed in AP World History.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md",
     "lines": "60",
     "quote": "There is a clear mismatch between the labeled difficulty ('easy') and the actual task complexity.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/CLAUDE.md",
     "lines": "113",
     "quote": "- **4 curriculum alignment** (wrong unit) -- 2 are benchmark data quality issues (unfixable)",
     "verbatim": true
    }
   ],
   "against": "Whether a task type can be 'easy' is the judge's view; a scaffolded short source task could be easy for some students. That a request was impossible is inferred from two models failing the same item, and model_findings.md line 829 itself lists alternatives (wrong unit mapping, impossible spec, or a judge edge case).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep",
   "reason": "Quotes are verbatim. This is a single case, but the mechanism (a writer bends facts to meet a quota) applies to any writer model.",
   "statement": "Let accuracy override any length or span quota in a writer's instructions; when a quota can't be met truthfully, the writer bends the facts to meet it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
     "lines": "18",
     "quote": "\"Use the FULL period or a large subset (minimum 20 years)\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
     "lines": "31",
     "quote": "4. LLM extends to 1850 to meet 20-year minimum → historically inaccurate",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
     "lines": "34",
     "quote": "**Principle:** Historical accuracy > arbitrary length requirements",
     "verbatim": true
    }
   ],
   "against": "One case; the source records the fix as implemented but gives no measured result after it (IMPROVEMENT_PROPOSALS.md line 8: \"**Status:** Implemented\").",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep-with-fix",
   "reason": "Quotes and numbers are verbatim (65% to 61%; 15 examples, 4 failures, 98%). 'Repeatedly made output worse' overstated mixed evidence (examples helped another course), so I restated the candidate around what the evidence shows: rules that grow without pruning, and prohibitions that conflict. Overlaps 62 and 70; the new part is pruning and de-conflicting.",
   "statement": "Treat each rule or example added to a writer's instructions as a change to test, and prune and de-conflict the rules as they grow: a run that only added constraints fell from 65% to 61% and had prohibitions the model couldn't all satisfy, and adding 15 examples to one course's source-based task brought 4 failures where the version without examples passed 98%.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/ITERATION_ANALYSIS.md",
     "lines": "93",
     "quote": "> **More rules ≠ better output.** The LLM has limited attention. Every added constraint dilutes the importance of existing ones.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/ITERATION_ANALYSIS.md",
     "lines": "89",
     "quote": "- Additional rules created conflicting signals",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/VERSION_ANALYSIS.md",
     "lines": "88",
     "quote": "3. **Conflicting DO NOTs** - Model couldn't satisfy all constraints",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/VERSION_ANALYSIS.md",
     "lines": "94",
     "quote": "| Pass Rate | 65% | 61% | -4% |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
     "lines": "186",
     "quote": "APUSH DBQ had 4 failures after adding 15 document examples to prompts.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
     "lines": "225",
     "quote": "| Main | APUSH | 0 | 195.2 | 98% pass |",
     "verbatim": true
    }
   ],
   "against": "Examples helped elsewhere (IMPROVEMENT_PROPOSALS.md line 227: \"| Experiment | APEURO | 31 | 26.6 | 100% pass |\"; VERSION_ANALYSIS.md line 232: \"| Concrete bad examples | **Strong positive** |\"). The run comparisons changed several things at once, and a 4-point drop may be within run-to-run noise.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep",
   "reason": "Quotes are verbatim; the rule was adopted after several runs. Distinct from 62: it contrasts concrete with abstract instructions, not use with avoid.",
   "statement": "Give a writer concrete, checkable constraints that say what the item must make the student do, not abstract labels such as a taxonomy level or 'be specific'.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/RUN7_BLUEPRINT.md",
     "lines": "612",
     "quote": "- Every instruction should be checkable",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/RUN7_BLUEPRINT.md",
     "lines": "637",
     "quote": "- Describe the BEHAVIOR you want, not the classification",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/PROMPT_EVOLUTION.md",
     "lines": "186",
     "quote": "**Why:** Bloom's taxonomy names don't constrain generation behavior.",
     "verbatim": true
    }
   ],
   "against": "The supporting evidence compares whole runs that changed several things at once (RUN7_BLUEPRINT.md line 579: \"- Can't isolate which change caused regression\").",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "keep",
   "reason": "Quotes are verbatim (the saq.py rule spans lines 765-766; the quoted half is on 766). Related to 30 and 33 but distinct: visible text must not point to hidden material.",
   "statement": "Nothing a student or marker sees may refer to the writer's working material that they can't see, such as a research brief or numbered source facts.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter2.md",
     "lines": "42",
     "quote": "Part (a) scoring is problematic: it references 'the brief'",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/archive/OPENCLAW_HUMAN_REVIEW.md",
     "lines": "106",
     "quote": "- Articles reference numbered \"Facts\" from knowledge base that aren't shown in the output",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/generators/saq.py",
     "lines": "765-766",
     "quote": "must be self-contained and readable by someone who ONLY sees the question.",
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
   "reason": "The CED line (pdftotext -layout line 12633) and saq.py line 771 are confirmed verbatim. The official guidelines score each point independently.",
   "statement": "Make each part of a multi-part task answerable and markable on its own, so a slip in one part doesn't cost the others.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/curriculum/ceds/ap-european-history-ced.pdf",
     "lines": "pdftotext -layout output, line 12633",
     "quote": "Each point is earned independently.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/generators/saq.py",
     "lines": "771",
     "quote": "⛔ Parts must be independently scorable — no chaining.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "keep",
   "reason": "Quotes are verbatim. The writer rule's own good example also names the period ('during the seventeenth century', saq.py line 280).",
   "statement": "Name everything a question asks students to relate (both sides of a comparison, the region, the period) so they never have to guess the frame.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/python/docs/EVALUATION-RESULTS-2026-02-23.md",
     "lines": "259",
     "quote": "| **Unclear comparisons** | \"More significant than...\" (than what?) | Complete the comparison |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md",
     "lines": "76",
     "quote": "Part C of the prompt uses the vague descriptor 'southern regions,' which is imprecise.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/generators/saq.py",
     "lines": "282",
     "quote": "RULE: A student should never need to infer WHAT is being compared — name both items.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. The original credited the ban with a 15.9-point rise, but that was on about 20 essay items, within the project's own noise estimate for that size, so I moved the number to 'against'. The statement now covers the defensible part, prompts that admit more than one position, and cites an official two-sided prompt.",
   "statement": "Write argument prompts that leave room for more than one defensible position, such as weighing one cause against another, rather than asking students to confirm a single 'primary cause'.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "1112",
     "quote": "- `specification_compliance` 43% — model uses \"primary cause/primarily responsible\" framing → binary thesis",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "1114",
     "quote": "- Pattern: \"primary cause\" framing generates falsifiable yes/no questions instead of nuanced analytical prompts",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/GENERATOR_STATUS.md",
     "lines": "27",
     "quote": "- Prompts are genuinely arguable — students can take multiple positions",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/curriculum/ceds/ap-european-history-ced.pdf",
     "lines": "pdftotext -layout output, line 12700",
     "quote": "Evaluate whether the Thirty Years’ War was fought primarily for religious or primarily for political reasons.",
     "verbatim": true
    }
   ],
   "against": "Official prompts also use 'primarily' when they pose two alternatives (the CED line above), so the judge's rejection of 'primary cause' framing may be its own preference. The gain after banning the framing (model_findings.md line 1257: \"1. **LEQ fix works**: +15.9pp vs Gate 12b.\") was on 20 essay items (line 1212), within the ±14-point swing the project measured at that size (line 1260). The framing still caused 88% of the remaining essay failures (line 1258).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 25,
   "verdict": "keep",
   "reason": "Quotes are verbatim. The official short-answer example uses a primary source and 'Describe' (CED pdftotext line 12078), and the generator banned both to suit the judge. Related to 37 and 43; it adds the specific failure of trimming real assessment forms to please a judge.",
   "statement": "When a judge rejects task forms that the real assessment uses, check the judge against official items instead of removing those forms from what students get.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/CHANGELOG.md",
     "lines": "20",
     "quote": "**Root cause:** The evaluator treats \"Describe\" and \"Identify\" as recall-level verbs regardless of analytical keywords in the question.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/CHANGELOG.md",
     "lines": "68",
     "quote": "1. **SAQ: No stimulus ever.** Stimulus-based SAQs always fail Part (a) as \"reading comprehension\" instead of \"historical thinking.\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/curriculum/ceds/ap-european-history-ced.pdf",
     "lines": "pdftotext -layout output, line 12078",
     "quote": "(A) Describe the historical situation in Spain reflected in the poster.",
     "verbatim": true
    }
   ],
   "against": "The program forbade changing the judge (03-ARCHITECTURE.md line 41: \"| **Modify the evaluator** | InceptBench is the immutable standard; gaming it is not an option |\"), which left changing the items as the only lever.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "keep",
   "reason": "Quotes are verbatim. Overlaps 37 (score the judge on labelled cases) and 45 (fix the rubric first); it adds the rule that a judge change is justified by agreement with labelled cases, never by pass rate.",
   "statement": "Change a judge's criteria or thresholds only to agree better with labelled cases, never to raise a pass rate.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/python/.claude/skills/monitor-evaluator.md",
     "lines": "46",
     "quote": "- Changes to evaluator should be based on benchmark accuracy, not pass rate",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/CLAUDE_MANUAL_REVIEW.md",
     "lines": "168",
     "quote": "cognitive_threshold = 0.70  # Relaxed from 0.85",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/TEST-FINDINGS-2026-02-17.md",
     "lines": "55",
     "quote": "**Fix:** Updated evaluation prompts to focus on CONTENT quality only,",
     "verbatim": true
    }
   ],
   "against": "Some judge changes fixed real judge bugs rather than lowering the bar (CLAUDE_MANUAL_REVIEW.md line 39: \"**The pass logic is checking `passed = false` even when `score >= 0.85`.**\").",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. The ~14% is of the parallel team's item-set failures, not 14% of all item sets. The truncation case (VALIDATION-REPORT-2026-02-19-COMPREHENSIVE.md line 161) came from the judge being shown a cut-off copy, so it belongs to 30; I replaced it with the judge's own cite-a-snippet method (BENCHMARK-RIGOR-ANALYSIS.md line 26). This applies 17 to judges and complements 32.",
   "statement": "Require a judge to quote the exact words behind each failure, and check in code that those words are in the item.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/workspace/INBOX_FROM_EXTERNAL/2026-04-28T00_first-contact.md",
     "lines": "49",
     "quote": "- We discovered an **InceptBench v2.4.0 false-positive `integrity_check` failure mode** on MCQ_SET (~14% of failures): the eval cites scoring-directive text that doesn't exist in our outputs.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/BENCHMARK-RIGOR-ANALYSIS.md",
     "lines": "26",
     "quote": "2. Identify ALL issues (with IDs, snippets, explanations)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/BENCHMARK-RIGOR-ANALYSIS.md",
     "lines": "27",
     "quote": "3. Score metrics (each 0.0 must cite an issue)",
     "verbatim": true
    }
   ],
   "against": "The 14% comes from a parallel team's runs on its own instance of the judge, not from this project's measurements, and the source file is a recreation of a lost original (line 3).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim (58.8%). 'Score 1.00 but be factually wrong' is a hypothetical in the source ('A question could:'), so I softened 'they pass wrong items' to 'they can'. The literal-title topic check did fail valid items (measured). Related to 10 and 32.",
   "statement": "Don't use keyword, verb or length counts as measures of quality; they can pass wrong items and fail good ones.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/EVALUATION-ANALYSIS.md",
     "lines": "57",
     "quote": "- Score **1.00** but be factually wrong",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/EVALUATION-ANALYSIS.md",
     "lines": "130",
     "quote": "**The 58.8% pass rate is meaningless** because:",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/CONSOLIDATION_2026-02-19.md",
     "lines": "19",
     "quote": "1. **Metaphorical APWH titles** - Topics like \"The Global Tapestry (1200-1450)\" were rejected because validation looked for literal words (\"tapestry\", \"global\") instead of actual historical content (Mongol Empire, Song Dynasty)",
     "verbatim": true
    }
   ],
   "against": "Used as gates rather than as scores, cheap word checks still caught a real cue that appeared in 35% of items (EVALUATION-RESULTS-2026-02-23.md line 34).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 29,
   "verdict": "keep",
   "reason": "Quotes are verbatim (24.53%; top groups of 50, 49 and 32 items share an excerpt opening; 12 duplicates in 62 attempts). The analysed set scored 0.9 or higher (analysis_report.md section 2), so 'high-scoring' holds.",
   "statement": "Check a bank of generated items for repeated sources and stems; a generator keeps returning to the same few well-known passages.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/analysis_report.md",
     "lines": "403",
     "quote": "- Duplicate rate: 24.53%",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/analysis_report.md",
     "lines": "406",
     "quote": "- Count 50: [mcq/apush] Use the excerpt below to answer the question.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/IRONCLAD_BATCH_50.md",
     "lines": "12",
     "quote": "- Duplicates Caught: 12",
     "verbatim": true
    }
   ],
   "against": "The near-duplicate count hashed only the first 200 characters (analysis_report.md line 399: \"- Total unique hashes (first 200 chars): 10382\"), so items sharing a passage but asking different questions were counted as duplicates, and several questions on one source is normal exam practice.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 30,
   "verdict": "keep-with-fix",
   "reason": "All three cells are verbatim and each carries a 'No' verdict. My tally of the verdict columns matches the reader's: 69 'No' and 11 'Partially' of 1,633 facts with a verdict, and 160 'No' plus 4 'Should be deleted' of 2,086 links. Reading the comments on the rejected rows confirms that placement (move to another topic or unit) and repeats dominate, with only a handful of accuracy notes; exact category counts depend on the coding. I dropped 'rather than being false' because the fact verdict column asks whether a fact should be covered, not whether it is true. The path contains a job-role abbreviation but no person's name.",
   "statement": "Review machine-built knowledge for placement, repetition and scope, not only accuracy: most facts and links rejected in review were repeats or belonged to another topic or unit.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 6 Nodes', cell M16",
     "quote": "move to 6.2",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 3 Relationships', cell J14",
     "quote": "already covered",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 1 Nodes', cell M10",
     "quote": "Out of time frame for this course",
     "verbatim": true
    }
   ],
   "against": "The fact verdict column is headed 'Should be covered ?' (sheet 'Unit 1 Nodes', cell K1), so reviewers judged coverage first; few accuracy notes may reflect the review form and its depth rather than accurate facts. Many facts carry only a 'Yes' with no note.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep",
   "reason": "Cells verified: J122 (verdict 'Needs editing'), Unit 8 J6 ('Should be deleted'), J69 (the relation type now reads 'details'). I added Unit 5 J41, another reversed link. These are a pattern, not a rate.",
   "statement": "Check every generated cause-and-effect link for direction, directness and type; links came out reversed, stated an indirect cause as direct, or used the wrong relation.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 6 Relationships', cell J122",
     "quote": "The statements should be reversed since the E. C. Knight Co. decision influenced and changed the scope of the Sherman Antitrust act",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 5 Relationships', cell J41",
     "quote": "more the other way around--because of southern leaders insistence on their right to take slavery to new territories, the Senate balance was important in maintaining that power through new slave states",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 8 Relationships', cell J6",
     "quote": "MAD was more of an indirect cause",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 6 Relationships', cell J69",
     "quote": "This should be \"details,\" not \"exemplifies\"",
     "verbatim": true
    }
   ],
   "against": "These were a minority of link comments (roughly ten of 172); repeats were far more common.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 32,
   "verdict": "keep",
   "reason": "Verified: 437 of 1,194 mapped facts carry 'None' and 757 map to a topic; cell F2 lists the Aztec, Maya and Inca facts removed as out of scope; instruction line 16 is confirmed. Related to 58, applied to extracted knowledge rather than to items.",
   "statement": "Map every fact extracted from source texts to a learning objective, and drop or review the ones that fit none; a large share of textbook-derived facts fit no objective.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Knowledge Schema Generator - AP USH Unit 1.xlsx",
     "lines": "sheet '2. Mapping Output', column D ('Cluster'), e.g. cell D109",
     "quote": "None",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Knowledge Schema Generator - AP USH Unit 1.xlsx",
     "lines": "sheet '6. Fact Refinement Output', cell F2",
     "quote": "3. Out of Scope (Mesoamerican civilizations):",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Knowledge Schema Generator - AP USH Unit 1 - Instructions.csv",
     "lines": "16",
     "quote": "7. In the main.py script, run steps 1 and 2 (generate facts + map facts to curriculum).",
     "verbatim": true
    }
   ],
   "against": "Unmapped facts may still be needed background (the reviews kept asking for added definitions and context), so dropping all of them could remove support students need.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 33,
   "verdict": "keep",
   "reason": "Cells verified. The simplified version had a lower reading grade in 68 of 71 rows (16.1 to 11.9 and 16.6 to 13.9 for the two cited rows). The preference tally is 23 'New' to 7 'Old', with 41 blank. Adds a caution to 23: a sentence split can re-pair ideas.",
   "statement": "Check simplified text by reading it against the original: easier reading-level scores came with sentence splits that changed the meaning, everyday words in place of key terms, and mechanical prose.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'ReadabilityExperiment-dev-inter', cell N13",
     "quote": "In this instance, the sentence split separated \"missionaries\" and \"salvation,\" which led to it only being paired with \"wealth.\" This changes the meaning of the paragraph",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'ReadabilityExperiment-dev-inter', cell N8",
     "quote": "Some of these changes give the flow an overly predictable pattern. That's not always a bad thing, but it can feel very mechanical and repetitive, which is not ideal.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'APUSH Articles-readable-exp', cell M2",
     "quote": "This was pretty solid, but the biggest issue is that specific phrasing from the CED standards were simplified as well (items like \"social diversification\" and \"mobile lifestyles\"). These CED specific terms should stay in the article as much as possible.",
     "verbatim": true
    }
   ],
   "against": "The simplified version was still preferred in most pairs (sheet 'ReadabilityExperiment-dev-inter', column K 'final preference': 23 'New' against 7 'Old'), so on balance simplification helped.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 34,
   "verdict": "keep",
   "reason": "Cells verified; the typos are in the source. In the M28 note the reviewer supplied a real image, and the team then added a copyright-free one. Related to 22 but distinct: prefer authentic images of things students must recognise.",
   "statement": "Use real images of the real places, objects and documents students may need to recognise; generated likenesses don't match what they will actually be shown.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'Articles-readable-exp', cell M12",
     "quote": "When there are historical examples like Angkor Wat or Angkor Tom, why aren't we using actual images? Students will probably have to be able to identify these images on the exam, so why are we relying on AI generated images which often do not resemble fow the image would look in an existing photograph?",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'APUSH Articles', cell M38",
     "quote": "I recommend that you use this famous image illustrating the Anaconda Plan - link",
     "verbatim": true
    }
   ],
   "against": "Real images raise rights questions; one note accepted the generated images where a real one was under copyright (sheet 'APUSH Articles-readable-exp', cell M28: \"If this is copyrighted, the ones you have work.\"), though the same cell records that a copyright-free real image was then added.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 35,
   "verdict": "keep",
   "reason": "Cells verified. Overlaps 21 and 64; it adds a preference for images that carry information over decoration, placed beside their text.",
   "statement": "Prefer pictures that carry information (maps, comparison charts, diagrams) over decorative scenes, and place each one next to the text it supports.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'APUSH Articles', cell M17",
     "quote": "The two images are placed back to back in the article. In addition, if it's possible to replace an image (I would replace image #1) with one that has some information, like a chart comparing the Virginia and New Jersey plans or one that compares the Federalists & Anti-Federalist positions, it would be a better use of space.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'APUSH Articles', cell M34",
     "quote": "This should include a map that shows the Missouri Compromise. I would recommend eliminating the 2 image in favor of it.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'Sheet3', cell A19",
     "quote": "It would be most efficient for the reader to see a chart/table here actually comparing the two movements characteristics",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 36,
   "verdict": "keep-with-fix",
   "reason": "Cells verified. 'Archival' had no support: the M12 note asks for something 'more symbolic' or a different subject, so I reworded the statement. There are only two instances. Related to 19 but broader: portrayals, not slurs.",
   "statement": "Review generated text and images for stereotyped or insensitive portrayals of people, and for atrocities use symbolic images or another subject rather than generated realistic scenes with people in them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'Sheet9', cell C15",
     "quote": "suggests that their performance skills made them stand out. Please rephrase this, as this is a bias that African Americans still face today, limiting roles and spheres of influence.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'APUSH Articles', cell M12",
     "quote": "I don't think we should illustrate a slave ship using AI, at least not with people on it. It could be considered by many to be insensitive. I would create an alternate image that's more symbolic or has to do with something else in the topic.",
     "verbatim": true
    }
   ],
   "against": "Only two instances were recorded and no systematic check existed, so how often this happens is unknown.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 37,
   "verdict": "keep",
   "reason": "Verified: the 'Extra Facts' column is '[]' for all 62 articles in 'Articles-readable-exp' and all 96 in 'APUSH Articles-readable-exp'. 'Missing Facts' is also empty in every row, which suggests the automated check never fired. That adds evidence to 38, but the statement itself (trace each statement to a source) is distinct. H8 and 03-ARCHITECTURE.md line 65 are confirmed.",
   "statement": "Trace every statement in generated text back to a source fact and flag the rest; an automatic 'extra facts' check reported none, while review estimated one or two untraced statements in every article.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'Articles-readable-exp', cell K2 (column K header 'Extra Facts')",
     "quote": "[]",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'APUSH Articles-readable-exp', column K ('Extra Facts'), all 96 article rows",
     "quote": "[]",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'Sheet4', cell H8",
     "quote": "We definitely have more (maybe around 1-2 statement in every article from llm) and some of it seems important as it really ties things together in the article",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/03-ARCHITECTURE.md",
     "lines": "65",
     "quote": "- Every claim in generated questions must trace to a VKB entry",
     "verbatim": true
    }
   ],
   "against": "The same note says some of the added statements were useful connecting text (\"some of it seems important as it really ties things together in the article\"), so a statement with no source is not necessarily wrong.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 38,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim (139, 25%). 'Each wrong option' and 'after the final attempt' went beyond the evidence: the rule asks for at least one wrong option, and timing is not addressed here (it belongs to 1 and 4). The 25% is of 553 generated items, not the 582 requested.",
   "statement": "Give every item an explanation of why the key is right and why the wrong options are wrong, and check in code that it is there: a quarter of generated items had none.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/python/docs/EVALUATION-RESULTS-2026-02-23.md",
     "lines": "104",
     "quote": "**Frequency:** 139 questions (25% of all generated)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/python/docs/EVALUATION-RESULTS-2026-02-23.md",
     "lines": "106",
     "quote": "**Impact:** Students cannot learn from their mistakes without explanations",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/validation_rules.md",
     "lines": "298",
     "quote": "- Must explain why correct answer is correct",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/validation_rules.md",
     "lines": "299",
     "quote": "- Must explain why at least one wrong answer is wrong (for MCQ)",
     "verbatim": true
    }
   ],
   "against": "Explanations are themselves a source of errors (letter mismatches failed 23% of items, per MCQ_BUG_HISTORY.md line 6), so each one needs its own consistency check. The value of explanations is asserted here, not measured.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 39,
   "verdict": "keep",
   "reason": "Quotes are verbatim; the concept_coverage counts of 1, 3 and 6 in units 1-3 are confirmed from the diagnosis headers. Related to 41 and 68 but about covering the parts an objective names.",
   "statement": "Across the items written for one objective, cover each part the objective names rather than going deep on one part.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md",
     "lines": "114",
     "quote": "The quiz omits the 'Caste' (Casta) system entirely.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_3/diagnosis.md",
     "lines": "76",
     "quote": "While the quiz covers the role of women and 'Republican Motherhood' with great depth, it fails the 70% threshold for concept coverage.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/COMPREHENSIVE-TEST-2026-02-17.md",
     "lines": "82",
     "quote": "the question completely fails to address the required sub-topic 'disease'",
     "verbatim": true
    }
   ],
   "against": "The counts were small (1, 3 and 6 coverage failures in units 1-3, per the diagnosis headers), and covering every part across a set can conflict with keeping each item narrow.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 40,
   "verdict": "keep",
   "reason": "Quotes are verbatim. A general fairness rule; related to 58 but about whether an item can be answered, not whether it is on topic.",
   "statement": "Ask only for knowledge the course teaches plus what the item supplies; a part that needs an obscure fact from outside the course can't be answered fairly.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter2.md",
     "lines": "58",
     "quote": "However, Part (c) requires specific knowledge of the Timber Culture Act (1873), which is not a standard APUSH curriculum topic",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/generators/saq.py",
     "lines": "247",
     "quote": "• ALL parts must be answerable using CORE AP curriculum content",
     "verbatim": true
    }
   ],
   "against": "What counts as standard curriculum was judged by a model, not checked against the course framework.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 41,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. The 95.2% headline labelled '340/360' is really 340/357, with 3 errors dropped; 340/360 is 94.4%. The 78.9% is 243/308. The original's '50.6% of all requests' counts 71 never-run pending items as failures, so the fair comparison is 243 of 409 attempted (59.4%). The found_by text is corrected accordingly; the statement keeps no numbers.",
   "statement": "Report pass rates over everything requested, counting a failure to produce an item as a failure, next to any rate that leaves errors out; dropping errors from the denominator raised headline rates.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/BENCHMARK_ACHIEVED.md",
     "lines": "4",
     "quote": "**Pass Rate:** **95.2%** (340/360 questions)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/BENCHMARK_ACHIEVED.md",
     "lines": "28",
     "quote": "| Total Questions | 360 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/BENCHMARK_ACHIEVED.md",
     "lines": "31",
     "quote": "| Errors | 3 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/PARTIAL_RESULTS_SUMMARY.md",
     "lines": "20",
     "quote": "- **Valid Questions Attempted:** 308 (409 - 101 errors)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/PARTIAL_RESULTS_SUMMARY.md",
     "lines": "22",
     "quote": "- **Effective Pass Rate:** 78.9%",
     "verbatim": true
    }
   ],
   "against": "All 101 errors in the 480-item run came from a difficulty the test plan requested but the generator never supported (PARTIAL_RESULTS_SUMMARY.md line 26), so they are a fault in the request more than in the generator. The project excluded infrastructure errors on purpose (CHANGELOG.md line 171: \"- 503 errors from Gemini excluded from pass rate (infrastructure issue, not quality)\"). Reporting both rates covers both cases.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_3/diagnosis.md",
   "lines": "90",
   "quote": "The inclusion of Document 7 (Anderson's 'Crucible of War') constitutes an answer giveaway.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
   "lines": "192",
   "quote": "- Document 7 \"performs analysis for student\" (answer leakage)",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md",
   "lines": "101",
   "quote": "The 'stimulus' is essentially the curriculum fact restated verbatim rather than a primary source, document excerpt, image, or data set",
   "ok": false
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md",
   "lines": "28",
   "quote": "It can be answered entirely from outside knowledge about Portuguese Indian Ocean strategy without any engagement with the stimulus.",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/generators/saq.py",
   "lines": "433",
   "quote": "⛔ STIMULUS INTEGRATION TEST: Cover the stimulus. Can ALL parts be answered",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'Articles-readable-exp', cell M16",
   "quote": "There is a reference to Sumni/Shia in the reflection but they are not mentioned in this reading.",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "635",
   "quote": "DBQ passage_reference: questions aren't explicitly referencing their assigned document.",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md",
   "lines": "10",
   "quote": "There are two defensible correct answers.",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/generators/mcq_set.py",
   "lines": "400",
   "quote": "TEST: \"Could an AP teacher argue this distractor is also correct?\" → if yes, CHANGE IT.",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "528",
   "quote": "**CRITICAL INSIGHT:** MCQ_SET is failing almost entirely because all 3 questions have the same correct answer letter (e.g., A/A/A or B/B/B).",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "615",
   "quote": "- **answer_balance: NOT PRESENT** ← constraint completely fixed this",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/MCQ_BUG_HISTORY.md",
   "lines": "190",
   "quote": "When validation is uncertain, the safe choice is to fail (and regenerate) rather than pass (and ship broken content).",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/FACT_CHECK_RESULTS.md",
   "lines": "42",
   "quote": "- **Analysis:** The knowledge base may lack specific WWI domestic policy facts",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/curriculum/ceds/ap-european-history-ced.pdf",
   "lines": "pdftotext -layout output, line 12638",
   "quote": "Clarity: Exam responses should be considered first drafts and thus may contain",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md",
   "lines": "83",
   "quote": "While Ricci's journals are real, this stimulus is a paraphrase/reconstruction rather than a direct quotation.",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/CLAUDE.md",
   "lines": "130",
   "quote": "Fabricated poem falsely attributed to Wilfred Owen",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'Sheet9', cell C3",
   "quote": "The language here is too simplistic, it should use \"mobile,\" incorporated in the sentence in a natural way, instead of \"moved around\"",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'ReadabilityExperiment-dev-inter', cell L10",
   "quote": "Prefer the term, 'factor' over 'trend' because the exam will use the word 'factor' in questions",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'Sheet9', cell C71",
   "quote": "term typically used here is \"power vacuum\"",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
   "lines": "sheet 'Unit 2 Relationships', cell J103",
   "quote": "change to \"Native American\" from American Indian",
   "ok": false
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
   "lines": "sheet 'Unit 1 Nodes', cell M91",
   "quote": "A short definition of feudalism should be included here.",
   "ok": true
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'Sheet9', cell C43",
   "quote": "Not sure if non-religious/non-Protestant students know what this means.",
   "ok": true
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
   "lines": "sheet 'Unit 7 Nodes', cell M53",
   "quote": "context for the Senate's vote needs to be included for this to make sense",
   "ok": true
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'AP Us Images QC', cell M65",
   "quote": "it lacks clear and distinct visual representations of *both* Latin American and Asian cultural influences as specified by the image caption and topic context.",
   "ok": true
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'Articles-readable-exp', cell M40",
   "quote": "Map of Treaty of Brest-Litovsk is included in gen ai article but it is not mentioned in text",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'AP Us Images QC', cell M35",
   "quote": "Several vehicles visible in the driveways and on the streets are clearly modern car models (e.g., SUVs, modern sedans), which are anachronistic for a 1950s Levittown setting.",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'Articles-readable-exp', cell M39",
   "quote": "Text in image on gen ai article is nonsensical",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'APUSH Articles', cell M36",
   "quote": "The first image should be regenerated. The clothing is far too modern.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/VALIDATION-REPORT-15-45.md",
   "lines": "118",
   "quote": "**Experiments ran in isolation. Production hasn't been tested.**",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/CHANGELOG.md",
   "lines": "78",
   "quote": "The `simple_api.py` transform layer was silently dropping fields before sending to the evaluator, causing failures.",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/ULTIMATE-VALIDATION-REPORT-2026-02-18.md",
   "lines": "195",
   "quote": "| Non-MCQ bypass quality gate | `server.py` | MSQ/fill-in/match/article unvalidated |",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/COMPREHENSIVE-VALIDATION-2026-02-18-1600.md",
   "lines": "65",
   "quote": "FACT_CHECK_ENABLED = False  # EXPERIMENT: Disabled for exp_12_minimal_gates",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/VALIDATION-REPORT-2026-02-19-COMPREHENSIVE.md",
   "lines": "184",
   "quote": "**The evaluator truncates articles to 3000 characters before showing them to Claude!**",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/FINAL_BENCHMARK_RESULTS.md",
   "lines": "40",
   "quote": "**Fix applied:** Match evaluator prompt + field name fix (`text` vs `content`)",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/GENERATOR_STATUS.md",
   "lines": "54",
   "quote": "| Pre-fix | 17.8% | Evaluator couldn't read new format |",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/TEST-FINDINGS-2026-02-17.md",
   "lines": "26",
   "quote": "**Result:** Evaluator saw incomplete content → flagged as \"truncated\"",
   "ok": true
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/SAQ_RALPH_PROMPT.md",
   "lines": "17",
   "quote": "All 12 dimensions score 1.0, but overall score is 0.4-0.6.",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/workspace/INBOX_FROM_EXTERNAL/2026-04-28T00_first-contact.md",
   "lines": "49",
   "quote": "the eval cites scoring-directive text that doesn't exist in our outputs.",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/TECHNICAL-DECISIONS.md",
   "lines": "30",
   "quote": "4. **Evaluation Alignment**: Pass substandard info to evaluation and score 0.0 if off-topic",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/BENCHMARK-RIGOR-ANALYSIS.md",
   "lines": "48",
   "quote": "InceptBench is designed for K-12 Common Core (math/ELA). It doesn't cover:",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/INCEPTBENCH_INTEGRATION_PLAN.md",
   "lines": "24",
   "quote": "DEFAULT_CURRICULUM = \"common_core\"",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/CLAUDE.md",
   "lines": "101",
   "quote": "The InceptBench evaluator has a **20% rating-flip rate** on identical generations across 4 repeated trials.",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/evaluation_audit.md",
   "lines": "237",
   "quote": "The evaluator passed this but failed similar fill-in questions. Inconsistent application.",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/TRAINING_DECISIONS.md",
   "lines": "133",
   "quote": "N=3 is safe under a noisy evaluator (InceptBench alpha 0.37–0.50).",
   "ok": true
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "131",
   "quote": "The dimension tracking code had a Python falsy evaluation bug: `v.get(\"score\") or v.get(\"value\")` drops score=0.0 values (0.0 is falsy).",
   "ok": true
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/MCQ_BUG_HISTORY.md",
   "lines": "176",
   "quote": "### 1. Test the validation function itself",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/BENCHMARK-RIGOR-ANALYSIS.md",
   "lines": "62",
   "quote": "3. **Create human validation set** - 50 gold standard questions (25 good, 25 intentionally bad)",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/EVALUATOR-TEAM-HANDOFF.md",
   "lines": "149",
   "quote": "3. Run against calibration set until it matches expected results",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/evaluation_audit.md",
   "lines": "319",
   "quote": "- **False negatives:** ~10-15% of failed questions (like the Match question above)",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/FACT_CHECK_RESULTS.md",
   "lines": "101",
   "quote": "- **Made-up dates:** No false dates found in test sample",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/URGENT-BUG-STILL-PRESENT.md",
   "lines": "35",
   "quote": "2. **The \"20/20 tests passing\" claim is misleading** - tests may be checking something else",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/PROMPT_EVOLUTION_2026-02-19.md",
   "lines": "5",
   "quote": "**Major Finding: All prompt variants achieved 100% pass rate.**",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/BENCHMARK-RIGOR-ANALYSIS.md",
   "lines": "64",
   "quote": "4. **Add adversarial tests** - wrong answer marked correct, anachronisms, explanation contradictions, factual errors in distractors",
   "ok": true
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
   "lines": "sheet 'Unit 7 Nodes', cell M131",
   "quote": "this agricultural depression may confuse students with the one that comes later.",
   "ok": false
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'Sheet9', cell C55",
   "quote": "section B should go before section A",
   "ok": false
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md",
   "lines": "74",
   "quote": "There is significant overlap between parts (a) and (c).",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md",
   "lines": "42",
   "quote": "The three questions do not adequately cover distinct AP historical thinking skills.",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/MCQ_BUG_HISTORY.md",
   "lines": "203",
   "quote": "- External verification (Claude, not Gemini)",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/archive/OPENCLAW_HUMAN_REVIEW.md",
   "lines": "13",
   "quote": "I read each one as a human reviewer would",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/COMPREHENSIVE-AUDIT-2026-02-18.md",
   "lines": "80",
   "quote": "| Cognitive Demand | C- | Mostly recall, light analysis |",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/GEN5_OPTIMIZATION_REPORT.md",
   "lines": "112",
   "quote": "The 85% first-attempt rate was misleading - it was measuring something other than structural validity.",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/orchestrator/course_checker_blueprint.md",
   "lines": "16",
   "quote": "Evaluator:   InceptBench v2.3.3",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'APUSH Articles', cell M32",
   "quote": "This article is great, but the column F link does not contain any images. The images in the column H link look great.",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/STATISTICAL_ANALYSIS.md",
   "lines": "239",
   "quote": "| Feb 22 | 91.7% | APGOV-only (biased) |",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'APUSH Articles', cell M21",
   "quote": "note that the google doc in H is the old version, the approved version is the s3 in column F",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
   "lines": "175",
   "quote": "15 of 17 factual_accuracy hard-fails came from SAQ scoring notes.",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
   "lines": "183",
   "quote": "**Data:** factual_accuracy hard-fails: 17 -> 2.",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/generators/saq.py",
   "lines": "226",
   "quote": "3. States what does NOT earn the point (e.g., \"just naming X without explaining = 0\")",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/curriculum/ceds/ap-european-history-ced.pdf",
   "lines": "pdftotext -layout output, line 12660",
   "quote": "Examples that earn this point include the following:",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/CHANGELOG.md",
   "lines": "157",
   "quote": "**Decision:** Always prefer verified curriculum facts over LLM-generated research. The LLM should construct questions FROM verified facts, not invent its own.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/TRAINING_DECISIONS.md",
   "lines": "142",
   "quote": "| Prompt engineering for factual_accuracy | No effect | Model uses parametric memory, not prompted context |",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "232",
   "quote": "- The 0.00 failures still occur despite facts injection — hard fails are from document CONTENT quality, not missing facts context",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/TECHNICAL-DECISIONS.md",
   "lines": "21",
   "quote": "Users could select \"Seven Years' War\" but get a question about \"African and European musical traditions\".",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/failure_analysis.md",
   "lines": "324",
   "quote": "- Questions set DURING a time period but not ABOUT the period's key content",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/BENCHMARK-RIGOR-ANALYSIS.md",
   "lines": "44",
   "quote": "Our weighted average could theoretically pass with a factual error if other scores are high.",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md",
   "lines": "35",
   "quote": "A factual error was identified in the third question of the set during the individual question evaluation, which voids the factual accuracy of the quiz as a whole.",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/CLAUDE.md",
   "lines": "455",
   "quote": "**The question is not \"did scores go down?\" but \"WHY did they go down and is the fix addressing the right thing?\"**",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "609",
   "quote": "Gate 3's MCQ failures were about fabricated stimuli. Gate 4's failures are about clarity (ambiguous stems) and factual accuracy in the historian-framing argument.",
   "ok": true
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/CHANGELOG.md",
   "lines": "148",
   "quote": "**Decision:** Flash research stage hallucinated facts that poisoned the compile step. MongoDB verified facts are better.",
   "ok": true
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Knowledge Schema Generator - AP USH Unit 1 - Instructions.csv",
   "lines": "40",
   "quote": "20. Run step 11 in main.py which is to generate relationships. This will be the very last step after the KS for the unit has been approved.",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "1257",
   "quote": "1. **LEQ fix works**: +15.9pp vs Gate 12b. The spec_compliance FORBIDDEN list genuinely helped.",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/VERSION_ANALYSIS.md",
   "lines": "232",
   "quote": "| Concrete bad examples | **Strong positive** |",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/improvement_plan_prompts.md",
   "lines": "39",
   "quote": "- BANNED WORDS has no **detection/rejection mechanism** - it's advisory only",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
   "lines": "41",
   "quote": "Every generated item for these units had content matching the TOPIC but metadata saying the wrong TIME PERIOD. The evaluator saw the mismatch and issued automatic curriculum_alignment hard-fails.",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
   "lines": "43",
   "quote": "**Impact:** 77 curriculum_alignment hard-fails in baseline. This single config error was responsible for the majority of all failures.",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/CHANGELOG.md",
   "lines": "71",
   "quote": "4. **APWH unit correction.** The evaluator returns systematically wrong unit numbers for APWH standards — we fix them before evaluation.",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
   "lines": "54",
   "quote": "The InceptBench evaluator marks decorative SAQ images as INFERIOR (hard-fail on stimulus_quality).",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
   "lines": "62",
   "quote": "the evaluator saw a document declared as \"visual\" with no actual image, triggering a stimulus_quality hard-fail. 17 such failures in the baseline.",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/HANDOFF-finetune-status.md",
   "lines": "64",
   "quote": "**Result:** DBQ scores shifted 0.80-0.82 → 0.84-0.98. Overall 80% → 83.3%.",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md",
   "lines": "124",
   "quote": "Document 3 provides a text description of a painting instead of the image itself.",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'APUSH Articles-readable-exp', cell M45",
   "quote": "There is a map the text references but it is not included in the article.",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/03-ARCHITECTURE.md",
   "lines": "88",
   "quote": "- Political cartoons and images (descriptions for text-based generation)",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/05-OPERATING-PRINCIPLES.md",
   "lines": "48",
   "quote": "| Increase retry count to dilute failures | ❌ Bandaid |",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/03-ARCHITECTURE.md",
   "lines": "94",
   "quote": "- Each retry should address a specific failure mode, not be a random re-roll",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/TRAINING_DECISIONS.md",
   "lines": "133",
   "quote": "**Research:** RBoN (NAACL 2025): Vanilla BoN degrades beyond N~16.",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/PLAN-finetune-qwen.md",
   "lines": "553",
   "quote": "- Score threshold actually correlates with quality (no false positives)",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/MSQ_FIX_RESULTS.md",
   "lines": "100",
   "quote": "1. **Deterministic**: Single-answer MSQs always fail, not dependent on model",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/EXPERIMENT_RESULTS_2026-02-18.md",
   "lines": "104",
   "quote": "- Prompt instruction alone doesn't enforce length",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "953",
   "quote": "Chinese character `绥靖` (\"suí jìng\", appeasement) embedded in English text.",
   "ok": true
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "961",
   "quote": "MCQ_SET hard-fail dimensions cascade: when factual_accuracy fails, educational_accuracy, concept_coverage, localization_quality, difficulty_distribution, non_repetitiveness, test_preparedness, answer_balance, stimulus_quality, and integrity_check all fail together.",
   "ok": true
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/CLAUDE.md",
   "lines": "129",
   "quote": "| apeuro u7 MCQ_SET | factual | One question in set has documented factual error | Per-question independent validation |",
   "ok": true
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/TEST-FINDINGS-2026-02-17.md",
   "lines": "40",
   "quote": "Articles were being evaluated with question criteria (distractor_quality, etc.)",
   "ok": true
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/FRESH_CLAUDE_EVAL_2026-02-17.md",
   "lines": "134",
   "quote": "**Root Cause**: The article evaluator is treating articles as MCQs, expecting \"question stem\" and \"answer options\".",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/CLAUDE.md",
   "lines": "311",
   "quote": "Never batch multiple fixes. Never skip local testing. Always measure before/after.",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "231",
   "quote": "- Cannot measure impact: no A/B control in this run",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/RUN7_BLUEPRINT.md",
   "lines": "579",
   "quote": "- Can't isolate which change caused regression",
   "ok": true
  }
 ]
}
```
