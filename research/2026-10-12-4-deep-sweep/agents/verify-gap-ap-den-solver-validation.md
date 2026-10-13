# verify:gap:ap-den-solver-validation

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "ap-den-solver-validation",
 "verified": [
  {
   "index": 0,
   "verdict": "keep",
   "reason": "All three reader quotes found at the cited lines. I re-counted the fields by extracting them only. v8 file: 46 rows PREDICTED_PASS_CACHE_NEIGHBOR with decision predicted_pass_skip_live_ib, and 4 rows (12, 35, 42, 45) PREDICTED_PASS_TIMEOUT_TEMPLATE_FALLBACK. v10 file: 50 of 50 predicted_pass_skip_live_ib, each with the reasoning 'accepted by high-scoring Unit-1 archetype predictor before live IB grading'. Neither file contains SUPERIOR, ACCEPTABLE or INFERIOR anywhere, and ib_score is 0.95 on every row. Even so, the v8 promotion note reported those 46 rows as 'IB pass' with a 0.95-1.00 range. New finding: the slice-2 MCQ_SET run (input /tmp/unit1_mcq_set_holdout_slice2_n50.jsonl) supplies 50 of the 239/250 = 95.6% 'deployable K=1' figure, and it is also 50 of 50 predicted passes. So neither headline MCQ_SET number holds a grader verdict. The parallel lane's numbers check out: 25 SUPERIOR + 5 ACCEPTABLE + 17 PREDICTED_PASS_LOCAL_MCQ_AFTER_IB_TIMEOUT = 47 headline and 30 graded; v2 = 39 SUPERIOR + 4 ACCEPTABLE = 43. The statement is general and supported. It is related to 9 (no verdict is never a pass) and 24 (label an estimate as one) but concerns counting verdicts, so it is not a duplicate. No names or roles; no path is name-bearing.",
   "statement": "Count a pass only when the grader actually returned it; a pass predicted from similarity to earlier passing items, or assumed after a timeout, is not a verdict.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/den_solver_acceptance_20260523T082319Z.jsonl",
     "lines": "1-50 (all 50 rows)",
     "quote": "\"decision\": \"predicted_pass_skip_live_ib\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-22T2116Z_den_solver_v8_FIRST_VALIDATED/VALIDATION_REASON.md",
     "lines": "25",
     "quote": "| Fresh v80bchain generation → IB pass | 46 | 92.0% | 0.95-1.00 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-22T2116Z_den_solver_v8_FIRST_VALIDATED/den_solver_acceptance_20260522T210237Z.jsonl",
     "lines": "46 of rows 1-50 (all but 12, 35, 42, 45)",
     "quote": "\"decision\": \"predicted_pass_skip_live_ib\"",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/experiments/main_a_acceptance_runs/den_solver_acceptance_20260524T183207Z.jsonl",
     "lines": "1-50 (all 50 rows)",
     "quote": "\"decision\": \"predicted_pass_skip_live_ib\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-22T1910Z_iterate_toward_LLM_FINAL_compatible.md",
     "lines": "23",
     "quote": "3. If predicted-pass: skip full IB grade, return generation directly",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit1_mcq_solver_v2_validated_addendum_20260524T085013Z.md",
     "lines": "43",
     "quote": "The headline rate dropped because v1 was counting fallback-aided passes; v2 is the defensible result.",
     "verbatim": true
    }
   ],
   "against": "The promoting note argued the predictor was grader-backed: \"the cached archetype is itself derived from live-IB-validated v80bchain content, so it's not \"deterministic-from-bank\" in the prior sense.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-22T2116Z_den_solver_v8_FIRST_VALIDATED/VALIDATION_REASON.md, line 62). The practice was requested, not hidden: \"Use cache as a NEAR-NEIGHBOR scorer to predict if generation will pass before full IB grading\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-22T1910Z_iterate_toward_LLM_FINAL_compatible.md, line 22).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep-with-fix",
   "reason": "Quotes found at the cited lines. Line 157 also repeats at 62, and line 136 at 51 and 75, in the triage signal sections; the raw-preview lines cited are correct. As submitted, the evidence showed the bar and the 'strict fresh' claim but not that the ratings were predictions. I added the v10 rating field (50 of 50 PREDICTED_PASS_CACHE_NEIGHBOR) and the completion audit, which carried the same 50/50 forward as 'all fresh, zero fallback'. 'Strict fresh' described where the content came from, not where the verdict came from. Statement unchanged. It is general, supported once the data is cited, and not a duplicate (closest are 43 and 66).",
   "statement": "Audit for the property a result must have, not for the absence of one known bad label; a check for one fallback label waved through runs whose every rating was a differently named prediction.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T084525Z_2026-05-24T0844Z_UNIT1_MCQ_SOLVER_VALIDATED.md.md",
     "lines": "157",
     "quote": "Same bar as Den v10, Den SAQ v1, Den DBQ v1 (no PREDICTED_PASS_LOCAL_* anywhere).",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T073015Z_2026-05-24T0601Z_UNIT1_MCQ_SOLVER_REPAIR.md.md",
     "lines": "136",
     "quote": "Den v10 precedent (MCQ_SET, 2026-05-23T08:40Z) was promoted as **VALIDATED** specifically because it cleared 50/50 STRICT FRESH with zero timeout fallback. That set the bar.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/VALIDATION_REASON.md",
     "lines": "5",
     "quote": "**Verdict:** 50/50 = **100.0% STRICT FRESH** — zero timeout-fallback, all v80bchain fresh generation",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/den_solver_acceptance_20260523T082319Z.jsonl",
     "lines": "1-50 (all 50 rows)",
     "quote": "\"ib_rating\": \"PREDICTED_PASS_CACHE_NEIGHBOR\"",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/current_completion_audit_20260524T2053Z.md",
     "lines": "15",
     "quote": "Complete: hidden `50/50`, all fresh, zero fallback",
     "verbatim": true
    }
   ],
   "against": "none found; the SAQ and DBQ runs named in the same bar did carry real ratings (47 SUPERIOR + 3 ACCEPTABLE; 33 SUPERIOR + 11 ACCEPTABLE + 5 INFERIOR + 1 unrated), so only the MCQ_SET runs slipped through.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "Quotes found; lines 82 and 105 also repeat earlier in the file's signal sections. The v8 quote is verbatim on all 50 rows, but on its own it shows a uniform score, not a placeholder. I swapped in the v10 file, where the same 0.95 sits beside the predictor's own reasoning line on every row, while archetype_score ranged 0.98-1.0. The same constant appears on every row of v8 and of the slice-2 MCQ_SET run. Statement unchanged; general; not a duplicate.",
   "statement": "When every item in a run gets the same score, suspect the measurement before the content; a uniform score came from a wrong input shape or a placeholder.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T220400Z_2026-05-28T0008Z_track_A_30row_sample_INVALID_TEST_RECOVERY.md.md",
     "lines": "82",
     "quote": "Result: 30/30 scored 0.55 overall, stim_quality=0, rated INFERIOR.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T220400Z_2026-05-28T0008Z_track_A_30row_sample_INVALID_TEST_RECOVERY.md.md",
     "lines": "105",
     "quote": "Recognized 0.55 floor + 0/30 = signature of wrong-schema, not content failure",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/den_solver_acceptance_20260523T082319Z.jsonl",
     "lines": "1-50 (all 50 rows)",
     "quote": "\"ib_score\": 0.95",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/den_solver_acceptance_20260523T082319Z.jsonl",
     "lines": "1-50 (all 50 rows)",
     "quote": "Fresh v80bchain final content accepted by high-scoring Unit-1 archetype predictor before live IB grading.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep-with-fix",
   "reason": "Quotes found at 84, 88 and 97, and at 82. 'Gives a floor score' generalises one grader's 0.55 floor, so I reworded it to what holds in general. Close to 33 (give the marker what the rule refers to) and 30, but here the unit being judged is wrong, so it is not a duplicate.",
   "statement": "Judge a part inside the complete task it will serve; a grader built for whole tasks, given a part alone, scores the mismatch rather than the part.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T220400Z_2026-05-28T0008Z_track_A_30row_sample_INVALID_TEST_RECOVERY.md.md",
     "lines": "84",
     "quote": "IB v2.5.11 grades DBQs as complete prompt+documents+rubric structures. Standalone primary-source excerpts aren't a DBQ shape.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T220400Z_2026-05-28T0008Z_track_A_30row_sample_INVALID_TEST_RECOVERY.md.md",
     "lines": "88",
     "quote": "The proper test for Track A excerpts' DBQ-stim quality is downstream: **embed the excerpts in a full DBQ structure (prompt + 7 documents + rubric) + generate that DBQ → grade THAT.**",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T220400Z_2026-05-28T0008Z_track_A_30row_sample_INVALID_TEST_RECOVERY.md.md",
     "lines": "82",
     "quote": "Result: 30/30 scored 0.55 overall, stim_quality=0, rated INFERIOR.",
     "verbatim": true
    }
   ],
   "against": "Structural retrieval checks can still run on their own: \"DBQ source retrieval should be tested independently from model generation.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md, line 100).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep-with-fix",
   "reason": "Quotes found. I checked the run summaries: the 37/50 (182953Z), 32/50 (204749Z), v8 50/50 and v10 50/50 runs all read /tmp/holdout_for_den_v2.jsonl. The repairs in between prewarmed cache entries for that run's shared failure classes (1936Z line 39), with prior-failure replays going 4/13, 5/13, 6/13, then 13/13; the v4 note itself predicted about 50/50 'on the same failure mix'. I reworded 'the repairer' so no role is named, and corrected the against, because the 95.6% includes 50 predicted passes. Overlaps candidate 5, which could merge into it. General; related to 48 and 66 but not a duplicate.",
   "statement": "A test you have repaired against is spent, public or hidden: once its failures steer the fixes, rerunning it no longer measures new performance, so confirm on items that played no part in the repairs.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1936Z_DELIVERED_pipeline_solver.md",
     "lines": "15",
     "quote": "This version targets the exact failure classes main-a shared from the first hidden run without reading the hidden prompt file.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T2019Z_DELIVERED_pipeline_solver_v4.md",
     "lines": "82",
     "quote": "Expected if the previous hidden miss distribution recurs: prior `37/50` plus `13/13` repaired prior misses implies ceiling around `50/50` on the same failure mix.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/experiments/main_a_acceptance_runs/den_solver_acceptance_20260522T182953Z_summary.json",
     "lines": "13",
     "quote": "\"input_jsonl\": \"/tmp/holdout_for_den_v2.jsonl\",",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/den_solver_acceptance_20260523T082319Z_summary.json",
     "lines": "13",
     "quote": "\"input_jsonl\": \"/tmp/holdout_for_den_v2.jsonl\",",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/to_main/2026-05-23T1808Z_DEN_REQUEST_validate_unit9_mcq_solver_v1.md",
     "lines": "26",
     "quote": "third public n=10 was `10/10`, but runner sanity failed `1/2`",
     "verbatim": true
    }
   ],
   "against": "The risk was flagged at the time: \"A fresh hidden seed is still the real gate.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1936Z_DELIVERED_pipeline_solver.md, line 77). On fresh rows 100-149 the graded lanes partly held (SAQ 43/50, LEQ 47/50, MCQ 49/50, DBQ 50/50), but the 239/250 = 95.6% total also counts 50 MCQ_SET passes that were predicted, not graded.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep-with-fix",
   "reason": "Quotes found. The benchmark path sits on line 48 of the 1709Z note; line 46 is only the 'Prompt source:' label, so I corrected the lines. I added the LEQ v3 probe, which ran on a file of hidden rows 27 and 49; LEQ v3 then scored 50/50 on the same rows. I reworded 'the builder' so no role is named. Overlaps candidate 4. General; not a duplicate.",
   "statement": "Keep held-out items out of reach of whatever is being tuned; rows sliced from the file the self-tests sample from, and failing rows handed back as files, are not held out.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T073015Z_2026-05-24T0601Z_UNIT1_MCQ_SOLVER_REPAIR.md.md",
     "lines": "114",
     "quote": "hidden validation input: `/tmp/unit1_mcq_holdout_n50.jsonl` (MCQ rows 50-99 from `~/Downloads/unit-1-apush-benchmark.jsonl` — no overlap with Den's selftest step-sample)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1709Z_DELIVERED_pipeline_solver.md",
     "lines": "48",
     "quote": "`~/Downloads/unit-1-apush-benchmark.jsonl`",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit1_dbq_solver_v2_repair_delivery_20260524T105934Z.md",
     "lines": "30",
     "quote": "input: `experiments/dbq_v2_failure_probe/unit1_dbq_v1_failure_rows.jsonl`",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit1_leq_solver_v3_final_gap_repair_delivery_20260524T1840Z.md",
     "lines": "31",
     "quote": "input: `experiments/leq_v3_failure_probe/unit1_leq_v2_failure_rows_27_49.jsonl`",
     "verbatim": true
    }
   ],
   "against": "Overlap with the self-test sample was checked (\"no overlap with Den's selftest step-sample\", same triage file, line 114), and the first challenge required a prompt diff: \"I'll diff your prompt list against my n=50; any overlap = automatic FAIL\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-22T1845Z_ULTIMATE_DELIVERY_CHALLENGE.md, line 52).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep-with-fix",
   "reason": "Quotes found. The rule holds on its own terms: picking the best of several attempts by the grader's score raises that same score, and production could not reach the grader at all ('Production must run WITHOUT IB grader access', to_den 0615Z line 68). I added the sibling lab's takeaway as independent support. I also corrected the against: the 99.6% to 95.6% contrast is not a clean K=4 versus K=1 comparison. Statement unchanged. Related to 46 and 65 but not a duplicate.",
   "statement": "Headline the score of the mode that will ship; a best-of-several pick made by the grader overstates what one attempt delivers.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/current_completion_audit_20260524T2053Z.md",
     "lines": "40",
     "quote": "Do not mislabel this as deployable K1 production `>=99%`.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T202325Z_2026-05-24T2022Z_UNIT1_LEQ_SOLVER_v3_VALIDATED_99_6pct.md.md",
     "lines": "140",
     "quote": "**Deployable bound is K=1 single-shot.** Slice-2 K=1 (rows 100-149) was 239/250 = 95.6% with LEQ v2.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-25T0615Z_TASK_concrete_deployable_workflow.md",
     "lines": "88",
     "quote": "No more \"99.6% goal complete\" framing in production-facing docs. Use the K=1 numbers as headlines.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "280",
     "quote": "K-of-N judging is useful for experiments and selection, but it is not proof of K=1.",
     "verbatim": true
    }
   ],
   "against": "The measured drop mixes the pick with a change of rows. The K=4 figures came from rows 50-99, which the repairs had targeted; the K=1 figures came from fresh rows 100-149. MCQ_SET's 100% in both figures was predicted, not graded. The 8/20 retest also used a thinner prompt: \"The missing lift is in the actual specialist solver mechanics, not the thin deployable generic prompt.\" (~/Documents/aptraining/den-of-ideation/from_den/2026-05-25T0758Z_BLOCKED_WORKFLOW_GENERIC_MCq_RETEST.md, line 18).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep",
   "reason": "Quotes found. The self-test numbers check out: 44/50 at a mean of 0.01458 s and $0.00 on its own sample (1936Z lines 58-62), then 37/50 on the hidden set. I added the sibling lab's sub-second rule as a fourth item. Related to 24 and 50 and overlaps candidates 0 and 28, but it is not a duplicate. No names or roles.",
   "statement": "Score only what the generator made for the request; label any banked, cached, templated or fallback output, and treat implausibly fast 'generation' as a sign that something else answered.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1840Z_DELIVERED_pipeline_solver.md",
     "lines": "86",
     "quote": "elapsed: 0.150s because current archetypes were backed by prior live IB cache entries",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md",
     "lines": "49",
     "quote": "Deterministic fallback can fake readiness. Exports with ~0.40s generation latency were later marked invalid as quality evidence because they were fallback-shaped rather than model-shaped.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-22T1910Z_iterate_toward_LLM_FINAL_compatible.md",
     "lines": "12",
     "quote": "Production explicitly forbids deterministic returns (cache lookups, prewritten templates, archetype banks) as the FINAL answer. Banks/rescues may inform prompts but cannot be returned.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "283",
     "quote": "Sub-second “generation” from a supposed model route is suspicious; it often means deterministic/template fallback.",
     "verbatim": true
    }
   ],
   "against": "Fixed retrieval was kept for one item type: \"Document that DBQ is retrieval-with-cleanup, not LLM generation per call.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-25T0615Z_TASK_concrete_deployable_workflow.md, line 52). Cached fallback output was also promoted as a pass because it had once been graded (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-22T2116Z_den_solver_v8_FIRST_VALIDATED/VALIDATION_REASON.md, line 62).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep-with-fix",
   "reason": "Quotes found and the numbers match: among 16 passing items, 15 passed the validator and 1 failed; among 14 failing items, 12 passed and 2 failed (RESULTS.md lines 45-48). The 8/20 quote alone did not show a shape check passing, so I added the 25/25 shape-only smoke test of the same service, which ran in 0.006 s without the grader. Statement unchanged. Related to 44 (machine checks are not judgment) but not a duplicate. Not related to 28, whose 'gate' means a check a student cannot skip.",
   "statement": "Format and leak checks catch broken items, not weak ones; keep them as safety rails and judge quality separately.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md",
     "lines": "47",
     "quote": "\"failed_validator_passed\": 12,",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md",
     "lines": "54",
     "quote": "The deterministic hard gates are good as a safety layer, not a complete quality judge.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-25T0633Z_DELIVERED_WORKFLOW_den_workflow_v1.md",
     "lines": "20",
     "quote": "direct package smoke: `25/25`, elapsed `0.006s`, no IB",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/from_den/2026-05-25T0758Z_BLOCKED_WORKFLOW_GENERIC_MCq_RETEST.md",
     "lines": "12",
     "quote": "`/no_think` generic deployable MCQ: `8/20 = 40.0%`",
     "verbatim": true
    }
   ],
   "against": "The 8/20 retest used a thinner generic prompt than the graded specialist solvers (same file, line 18), so it shows what the shape check missed, not how good the specialists were.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "reason": "Quotes found. 'Fuzzy signals' went beyond the evidence, which concerns one wording heuristic. As written it would also clash with 58, which makes topic relevance a blocking check, so I narrowed it to wording heuristics. MAIN_AGENT_ACTION_PACKET.md line 219 repeats the over-rejection finding. Not related to 28.",
   "statement": "Hard-block only failures a check detects reliably, such as broken format, a broken answer key or a copied answer, and keep wording heuristics advisory; a wording check set to hard-block rejected items that pass.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md",
     "lines": "24",
     "quote": "Hard gates are deliberately narrow. The first version over-blocked known passing rows because InceptBench tolerates some source-referential wording.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/MAIN_AGENT_ACTION_PACKET.md",
     "lines": "74",
     "quote": "Keep reading-comprehension phrasing advisory unless it combines with another failure. The prototype showed hard-blocking it over-rejects known passing rows.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/MAIN_AGENT_ACTION_PACKET.md",
     "lines": "73",
     "quote": "Keep hard gates narrow: malformed schema, answer key breakage, copied answer leakage, extreme length, answer-key clustering.",
     "verbatim": true
    }
   ],
   "against": "A later design hard-rejects on a semantic check before grading: \"reject any item whose answer is derivable from the stimulus\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md, line 16).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep-with-fix",
   "reason": "Quotes found. The statement's 'fails with the source hidden' rests on line 230 ('all child questions depend on stimulus'), which the reader cited only for truth 5, so I added it here. Statement unchanged. It extends 5 with its converse (not settled by the source alone) for sources meant to prompt knowledge, so it is not a duplicate.",
   "statement": "When a source is there to prompt the use of knowledge rather than to test reading, each question should need both the source and that knowledge; check that it fails with the source hidden and is not settled by the source alone.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
     "lines": "7",
     "quote": "The eduacc leak-probe fails a set when >20% of child questions are answerable **from the stimulus alone**.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md",
     "lines": "109",
     "quote": "Fix generation/selector semantics for the eight remaining rows: outside-knowledge hooks, same-period distractors, no stimulus phrase dependency, and compact payloads to avoid score timeouts.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "229",
     "quote": "APUSH outside knowledge required",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "230",
     "quote": "all child questions depend on stimulus",
     "verbatim": true
    }
   ],
   "against": "\"The first version over-blocked known passing rows because InceptBench tolerates some source-referential wording.\" (~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md, line 24).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep",
   "reason": "Quotes found. This is a design adopted before running. Its baselines were measured (freeform 0.31, structured one-stage 0.6, LEVER line 35), and the sibling lab found that a plan step improves question sets; the two-stage run itself was only queued. Close to 67 and 68, but it is about planning generation, not binding a judge, so not a duplicate.",
   "statement": "Decide in code, before the model writes any prose, what each question covers and what its answer hinges on, and let the model only render that plan; left free, generation drifts to whatever is easiest to answer.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
     "lines": "8",
     "quote": "Freeform generation leaks by default (least-resistance = stimulus-answerable).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
     "lines": "12",
     "quote": "select the **curriculum fact the correct answer hinges on + assert it is ABSENT from the stimulus**;",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
     "lines": "75",
     "quote": "MCQ_SET works better when the plan step constrains what each child question must cover.",
     "verbatim": true
    }
   ],
   "against": "\"over-constrained Stage 1 can pass eduacc but break factual/coherence\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md, line 37); \"Status: queued for the macmini executor / main-a on reconnect.\" (same file, line 44).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep",
   "reason": "Quotes found; line 109 repeats at 45 and 61. This is largely the same rule as 34 (send each test answer more than once). I kept it for the evidence it adds: the leak probe flips on borderline items, one item type's scores clustered at 0.55-0.84 just under a 0.85 bar, and the plan made grader self-agreement the first measurement. The ceiling itself was never measured.",
   "statement": "Before trusting any improvement, re-grade the same items several times to learn the grader's own agreement, and treat differences inside that ceiling as noise.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
     "lines": "36",
     "quote": "**ORACLE CEILING — MEASURE FIRST:** re-grade SAME mcq_set items Kx → grader self-agreement. ~0.6 ⇒ coin-flip-capped ⇒ generation can't reach 0.99 robustly ⇒ grader-side fix. **No delta is trustworthy until the ceiling is known.**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
     "lines": "19",
     "quote": "the probe flips on *borderline* items",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T192220Z_2026-05-27T1922Z_v80b_n100_unit1_BASELINE_REPORT.md.md",
     "lines": "109",
     "quote": "scores cluster 0.55-0.84 just under 0.85 threshold",
     "verbatim": true
    }
   ],
   "against": "Elsewhere, small differences at n=50 were read without a measured ceiling: \"Statistical resolution at n=50 per cell is ±2pp; 98.8% sits within the noise band of 99%.\" (~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T175907Z_2026-05-24T1759Z_UNIT1_DBQ_SOLVER_v3_VALIDATED_TARGET_REACHED.md.md, line 137).",
   "general": true,
   "duplicate_of": "34",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "keep",
   "reason": "Quotes found. The challenge's bar is at lines 44-52: at least 39/50 on 50 fresh prompts, cost and latency caps, and a prompt-overlap diff. The core is the same as 45 (fix the scoring rule before measuring), widened to baselines and a kill criterion. I kept it for the evidence it adds, including a 98.8% result described as 'essentially reached' against a 99% bar.",
   "statement": "Fix the headline measure, the baselines to beat, the pass bar and the kill criterion before running, and hold to them afterwards.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-22T1845Z_ULTIMATE_DELIVERY_CHALLENGE.md",
     "lines": "42",
     "quote": "Acceptance criteria (binary, no negotiation)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
     "lines": "33",
     "quote": "CONTRACT-FIRST (commit before firing)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
     "lines": "38",
     "quote": "**Kill criterion:** 2-stage doesn't beat `max(0.6+margin, ceiling−margin)` at K-grade after n KCs ⇒ generation lever ALSO closed ⇒ MCQ_SET genuinely grader-capped.",
     "verbatim": true
    }
   ],
   "against": "\"Main-a called this \"essentially reached\" within measurement noise. Den's literal audit does not mark complete because `98.8% < 99.0%`.\" (~/Documents/aptraining/den-of-ideation/reports/unit1_dbq_solver_v3_validated_addendum_20260524T1810Z.md, line 55).",
   "general": true,
   "duplicate_of": "45",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep-with-fix",
   "reason": "Quotes found. Only the first quote reports a measurement (broad rewrites regressed under live grading and were rejected); the other two are a plan and a gate requirement. So I changed the kind from measured to adopted rule. Statement unchanged. Close to 60 and 70, but it adds the explicit check of criteria and parts the fix did not touch.",
   "statement": "When a fix targets one criterion or one part, re-grade every criterion and the parts you did not touch, because tightening one dimension can break another.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1840Z_DELIVERED_pipeline_solver.md",
     "lines": "60",
     "quote": "rejected transatlantic rewrite and broad environment rewrite after live IB showed regressions;",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
     "lines": "37",
     "quote": "**Grade ALL criteria** (factual_accuracy + educational_accuracy) — over-constrained Stage 1 can pass eduacc but break factual/coherence.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-19T1541Z_gate0_prototype_in_lab.md",
     "lines": "63",
     "quote": "Other cells within ±2pp of K=6 baseline (DBQ 29/30, LEQ 29/30, MCQ 28/30, SAQ 30/30) — you may need to run those too for the no-regression check",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes found. The second clause claimed that row patches cause new failures elsewhere; the record cannot separate that from verdicts varying between runs (34), so I reworded it to what happened. I added an ID-keyed repair (one written for a single request ID, then re-validated on the same hidden rows) and the DBQ case (5 of 6 failures repaired, 1 new failure). The first clause rests on the sibling lab's distillation. Overlaps 60 but adds the rule about what to key repairs to.",
   "statement": "Key a repair to the kind of failure (the standard, the item type, the context), not to the failing row; repairs aimed at the rows that failed passed those rows while other rows newly failed.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "281",
     "quote": "Dynamic repair works only when keyed to standard/type/context, not exact benchmark row IDs.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit1_leq_solver_v3_final_gap_repair_delivery_20260524T1840Z.md",
     "lines": "22",
     "quote": "Added deterministic Spanish Empire social/economic repair for `c_i7Ve`.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit1_leq_solver_v2_validated_addendum_20260524T1633Z.md",
     "lines": "35",
     "quote": "Rows `47` and `48` from v1 now pass, so the Maya chronology repair worked. Row `49` remains failed and a new row `27` failed.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T115335Z_2026-05-24T1153Z_UNIT1_DBQ_SOLVER_v2_VALIDATED.md.md",
     "lines": "127",
     "quote": "5 of v1's 6 failures repaired; 1 (row 39) still fails; 1 new fail (row 29) introduced — net +4 passes.",
     "verbatim": true
    }
   ],
   "against": "Some row-targeted repairs did carry to fresh rows: single-attempt runs on rows 100-149 gave \"239/250 = 95.6%\" (~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T202325Z_2026-05-24T2022Z_UNIT1_LEQ_SOLVER_v3_VALIDATED_99_6pct.md.md, line 140), though 50 of those passes were predicted, not graded.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "keep",
   "reason": "Quotes found and the numbers match: 0.55 -> 0.70 -> 1.0; 0.675 INFERIOR -> 1.0 SUPERIOR (0255Z line 33); 44/50 -> 48/50 on the same rows. The same leak was repaired in at least five unit notes: interpretive summaries, mechanism-naming summaries, metadata sentences and copied analytical wording. I added one of them. It is a concrete case of 3 (nothing gives the answer first), kept as its own criterion for source tasks. General; no names.",
   "statement": "Give students source excerpts to analyse, never summaries or notes that state a source's purpose or significance, because those do the analysis for them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/to_main/2026-05-24T1059Z_DEN_REQUEST_validate_unit1_dbq_solver_v2_source_text_repair.md",
     "lines": "20",
     "quote": "The shared failure class was analysis leakage in DBQ document text: summaries gave away source purpose/significance instead of making students infer it.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1958Z_DELIVERED_unit1_dbq_solver_v1_candidate.md",
     "lines": "73",
     "quote": "Cultural perspective row improved 0.55 -> 0.70 -> 1.0 after replacing summary docs with source-like excerpts and adding Indigenous-perspective documents.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0255Z_DELIVERED_unit9_dbq_solver_v1_candidate.md",
     "lines": "29",
     "quote": "Migration/immigration hard row initially scored `0.675 INFERIOR` because the documents read like summaries rather than source excerpts.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T2115Z_DELIVERED_unit8_dbq_solver_v1_candidate.md",
     "lines": "46",
     "quote": "Initial U8 DBQ smoke failed because documents were summaries/meta-commentary.",
     "verbatim": true
    }
   ],
   "against": "The repaired packs were themselves \"normalized excerpts/source summaries\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T2009Z_DELIVERED_unit8_dbq_source_pack_gate.md, line 36), and the 44 to 48 gain was measured on the rows that defined the failure.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 17,
   "verdict": "keep",
   "reason": "Quotes found. The evidence is thin: a single row failed on fake source dates and passed once the sources were attributed honestly. The '89% subject-period-dated' honesty flag is not defined in any file read. General; near 50 (record where every asset came from) but not a duplicate. No names.",
   "statement": "Attribute every source truthfully, by who made it and when, rather than dating it to the period it describes.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1958Z_DELIVERED_unit1_dbq_solver_v1_candidate.md",
     "lines": "74",
     "quote": "Native environment row failed on fake `1491` source dates; honest modern/ethnohistorical attribution fixed it.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T220400Z_2026-05-28T0008Z_track_A_30row_sample_INVALID_TEST_RECOVERY.md.md",
     "lines": "96",
     "quote": "PIL still owes the a/b decision on the honesty flag (89% subject-period-dated).",
     "verbatim": true
    }
   ],
   "against": "none found; one measured row, and what the later honesty flag measured is not spelled out in the sources read.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep",
   "reason": "Quotes found and the numbers match: 244 parsed packs, 12 Unit-1-like, 0 passing strict validation; the scout passed 0/10. Raw scans of later units also had no valid rows (unit 3: 9 rows inspected, 0 valid; unit 8: 90 rows inspected, 0 valid). Not a duplicate of 58, 63 or 64. One caveat: the uniqueness check inside each pack did not catch the duplication across packs found under candidate 31.",
   "statement": "Check the sources a task rests on before building or grading the task, for the right period, real text rather than a summary or a missing image, enough length and distinct origins; a count of documents returned is not a check.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1825Z_BLOCKED_dbq_source_pack_repair_list.md",
     "lines": "61",
     "quote": "The old failure mode was treating \"7 returned docs\" as enough; it is not enough.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T0913Z_BLOCKED_dbq_doclock_scout.md",
     "lines": "45",
     "quote": "The earlier permissive scout showed chunk fallback could produce 7 documents, but inspection exposed false positives: Wealth of Nations, Social Contract, Benjamin Franklin, Walden, Federalist Papers, Uncle Tom's Cabin, Up From Slavery, and similar post-1607 material were being selected for Unit-1 DBQ.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T2000Z_DELIVERED_objective_completion_audit.md",
     "lines": "30",
     "quote": "Unit-1 DBQ passed only after source-pack and topic repair. Extending DBQ blindly to Units 2-9 would repeat the same source-integrity failure.",
     "verbatim": true
    }
   ],
   "against": "Passing the strict structural gate did not establish provenance: \"It does not independently fetch every URL or certify that normalized excerpts are acceptable for training.\" (~/Documents/aptraining/den-of-ideation/to_main/2026-05-23T1831Z_DEN_REQUEST_validate_unit1_dbq_source_packs_v1.md, line 52).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep-with-fix",
   "reason": "Quotes found. Each title recurs on several rows: the Constitution line at 52, 60, 64 and 72, and the Truman Doctrine line at 52, 56 and 68. In the unit 3 scan, every listed document (texts from 1775-1796, inside the period) carried a 'post-period drift' flag. In the unit 8 scan, pre-period contamination of document 3 alone hit 79 of 90 rows. Whether the flags were wrong is still open, so the statement now says only what happened. Overlaps 20 and 21, which also test checks with known-good controls.",
   "statement": "Run a strict source checker on documents known to be good before trusting its rejections; a period check rejected famous documents from inside the period asked for, and the packs built to replace them used normalized excerpts and summaries.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit3_dbq_source_pack_gate_20260524T001732Z.md",
     "lines": "52",
     "quote": "doc 3: Constitution of the United States — doc_3_post_unit3_drift",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit8_dbq_source_pack_gate_20260523T200616Z.md",
     "lines": "52",
     "quote": "doc 2: Truman Doctrine — doc_2_pre_unit8_contamination",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T2009Z_DELIVERED_unit8_dbq_source_pack_gate.md",
     "lines": "36",
     "quote": "The repaired packs use normalized excerpts/source summaries.",
     "verbatim": true
    }
   ],
   "against": "none found; the reports never say whether the flags came from later material inside those documents, such as an amended text or an editor's introduction.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep",
   "reason": "Quotes found; the first public run was 7/10 (line 52). General. Not a duplicate: 38 is about checks that never fire, this is about checks that fire wrongly. Overlaps 19 and 21. The names in the quotes are of historical documents and events, not people involved in the work.",
   "statement": "Test keyword and name-matching checks on near-miss cases; a guard for one name fired on a longer name containing it, and similar names pulled the wrong source.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1721Z_DELIVERED_unit8_mcq_solver_v1_candidate.md",
     "lines": "53",
     "quote": "Misses: three local scope-guard failures because `World War II` triggered a bad `world war i` substring guard",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1648Z_DELIVERED_unit7_mcq_solver_v1_candidate.md",
     "lines": "54",
     "quote": "Miss 1: `World War II: Military` routed to WWI because `world war i` matched `world war ii`",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0015Z_DELIVERED_unit5_dbq_solver_v1_candidate.md",
     "lines": "29",
     "quote": "Frederick Douglass / Emancipation slug collision",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "keep",
   "reason": "Quotes found. The 90 s reprobe repeated the result: the known-good control timed out at 90.020 s, while single questions and short answers scored 1.0 in 18.1 s and 24.6 s. I added it as a fourth item. General; distinct from 36 and 38.",
   "statement": "Before blaming content, run a known-good control through the same grading path; if the control fails too, the grading path is the problem.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1408Z_BLOCKED_mcqset_eval_timeout_probe.md",
     "lines": "35",
     "quote": "| `u1_mcq_set_control` | `mcq_set` | 35.024s | `ReadTimeout: timed out` |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1408Z_BLOCKED_mcqset_eval_timeout_probe.md",
     "lines": "33",
     "quote": "| `u2_mcq_minimal` | `mcq` | 24.385s | `1.0 SUPERIOR` |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1408Z_BLOCKED_mcqset_eval_timeout_probe.md",
     "lines": "39",
     "quote": "The current block is MCQ_SET evaluator-path timeout, not Unit-2 content alone.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T1013Z_BLOCKED_unit2plus_mcqset_evaluator_health_reprobe.md",
     "lines": "18",
     "quote": "`u1_mcq_set_control`: timed out at `90.020s`",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes found and the numbers match: the 32/50 run, the 0/50 cold start, and 216 null-field failures (distilled line 46). 'Time caps shorter than grading' had no quote, so I added the first solver's 0/10 under a 60 s cap. I also added 'report them on their own', because in production these are real failures and should not simply vanish. Shares its principle with 9 and its pass side with candidate 0; not a duplicate.",
   "statement": "Keep plumbing failures out of the quality count in both directions and report them on their own: timeouts, cold starts, empty fields and time caps shorter than grading are neither passes nor misses.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T2056Z_DELIVERED_pipeline_solver_v8_timeout_fallback.md",
     "lines": "38",
     "quote": "15+ failures were two consecutive `ReadTimeout: The read operation timed out`",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md",
     "lines": "60",
     "quote": "Maintain strict official schema normalization before any quality claim. Schema failures must not be counted as model failures or successes.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit1_mcq_solver_v2_validated_addendum_20260524T085013Z.md",
     "lines": "47",
     "quote": "Main-a's first v2 retry attempt failed `0/50` due to `DEPLOYMENT_SCALING_UP` while `v80bchain` was cold.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1709Z_DELIVERED_pipeline_solver.md",
     "lines": "99",
     "quote": "it does not clear the 78% fresh-pass acceptance gate because IB does not return MCQ_SET evaluations within the allowed call window.",
     "verbatim": true
    }
   ],
   "against": "Practice drifted from this: \"6 fails (5 INFERIOR + 1 None) are real IB rejections.\" (~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T071351Z_2026-05-24T0713Z_UNIT1_DBQ_SOLVER_VALIDATED.md.md, line 113).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "keep-with-fix",
   "reason": "Quotes found. Nothing supported 'of the same kind', so I trimmed it. I added the grader's standing critique (weak distractors) and the sibling lab's validator rule ('distractors same-period and plausible'). The two misses in the 48/50 run were stopped by the solver's own scope check, as the against notes. No existing truth covers distractors.",
   "statement": "Make every wrong option a plausible answer from the same period or scope as the question, never generic filler or something from outside the scope asked about.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "231",
     "quote": "distractors same-period and plausible",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1357Z_BLOCKED_unit2_mcqset_parent_archetype.md",
     "lines": "54",
     "quote": "reject generic option templates such as `belongs to the wider era`",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1905Z_hidden_acceptance_repair_status.md",
     "lines": "75",
     "quote": "The IB critique is consistent: factually sound, but too many question-level failures due answer leaks, weak distractors, or insufficient AP-level cognitive demand.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T2050Z_DELIVERED_pipeline_solver_v7_supersedes_v6.md",
     "lines": "51",
     "quote": "The two n=50 failures were both perspectives/cultural-interaction prompts that generated otherwise usable fresh content but included `Pueblo Revolt of 1680` as a distractor, causing local rejection and then live IB timeout.",
     "verbatim": true
    }
   ],
   "against": "The two misses were stopped by the solver's own scope check, not by a grader verdict: \"causing local rejection and then live IB timeout\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T2050Z_DELIVERED_pipeline_solver_v7_supersedes_v6.md, line 51).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep-with-fix",
   "reason": "Quotes found. The raw-probe quote (72-94% of failures with educational_accuracy=0) comes from a model that also failed on facts in 50-100% of its failures, so it does not show factually sound sets failing. I swapped it for the baseline report's question-set line, which also names coverage and balance as stated. Complements 59; not a duplicate.",
   "statement": "Check question design separately from facts; factually sound question sets still failed on leaks, weak options, coverage and balance.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1905Z_hidden_acceptance_repair_status.md",
     "lines": "75",
     "quote": "The IB critique is consistent: factually sound, but too many question-level failures due answer leaks, weak distractors, or insufficient AP-level cognitive demand.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md",
     "lines": "55",
     "quote": "Most MCQ_SET failures are semantic/educational rather than simple schema/leak failures.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T192220Z_2026-05-27T1922Z_v80b_n100_unit1_BASELINE_REPORT.md.md",
     "lines": "109",
     "quote": "failures are test_preparedness / concept_coverage / answer_balance / stimulus_quality (NOT factual)",
     "verbatim": true
    }
   ],
   "against": "For a small model that lacked the facts, facts dominated: \"Factual accuracy is the dominant kill — fresh-base 8B doesn't have Unit-1 facts.\" (~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T132917Z_2026-05-27T1330Z_bm0zjn5z_n100_unit1_RAW_PROBE_REPORT.md.md, line 115).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 25,
   "verdict": "keep",
   "reason": "Quotes found. It is an adopted check in three places: a scout's risk note, a validator gate and the sibling lab's validator. It is a concrete case of 3 (nothing gives the answer first), kept standalone because it tells a builder what to compare.",
   "statement": "Check that the right option does not echo distinctive words from the stem or source that the wrong options lack, since that echo hands over the answer.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/cell_family_archetype_scout_20260523.md",
     "lines": "84",
     "quote": "Answer leakage: direct MCQ can become trivial when the stem copies the correct option's nouns.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md",
     "lines": "19",
     "quote": "answer phrase leakage from stimulus to correct option;",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "227",
     "quote": "no copied answer phrase",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "keep",
   "reason": "Quotes found and the numbers match: 62%; 6/10, 7/10, 10/10. The evidence is thin and was tuned on the same public items. I added a second unit's rewrite: a template scored 0.65 INFERIOR, was rewritten as a cause-and-effect item, and the next smoke test passed 3/3. General; not a duplicate.",
   "statement": "Ask for explanation or a specific cause-and-effect link at the depth the standard asks for, not recall or a broad summary.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T132917Z_2026-05-27T1330Z_bm0zjn5z_n100_unit1_RAW_PROBE_REPORT.md.md",
     "lines": "130",
     "quote": "`mastery_learning_alignment=0` on 62% of MCQ fails — pure recall, not the \"explain how\" depth that AP standards demand",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1808Z_DELIVERED_unit9_mcq_solver_v1_candidate.md",
     "lines": "54",
     "quote": "Fix: rewrote those broad summary templates into sharper cause/effect items",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/to_main/2026-05-23T1808Z_DEN_REQUEST_validate_unit9_mcq_solver_v1.md",
     "lines": "24",
     "quote": "first public n=10 was `6/10`",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1648Z_DELIVERED_unit7_mcq_solver_v1_candidate.md",
     "lines": "63",
     "quote": "Fix: rewrote WWII military as a cleaner cause/effect item linking Allied victory factors to postwar U.S. power",
     "verbatim": true
    }
   ],
   "against": "The gain was measured on the ten public items being patched, and a different sample then failed: \"third public n=10 was `10/10`, but runner sanity failed `1/2`\" (~/Documents/aptraining/den-of-ideation/to_main/2026-05-23T1808Z_DEN_REQUEST_validate_unit9_mcq_solver_v1.md, line 26).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep-with-fix",
   "reason": "Quotes found. 'Constrain with rules and verified facts instead' went past the evidence: line 285 says few-shots help when they don't contaminate, and the best pipeline still used curated ones. I reworded it to match. Not a duplicate of 57 or 62.",
   "statement": "Expect a writer model to copy the examples it is shown: example items in a prompt carried their specific content and shape into new items and made them worse, so use an example only where copying it does no harm.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
     "lines": "100",
     "quote": "Few-shot MCQ examples worsened performance by contaminating generations with example-specific historical content.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "285",
     "quote": "Few-shots help only when they do not contaminate the historical content.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md",
     "lines": "76",
     "quote": "Keep prompt-kit field names subordinate to original IB schema authority to avoid illustrative examples leaking into output shape.",
     "verbatim": true
    }
   ],
   "against": "The best fresh pipeline still used curated examples: \"-> apply satisfaction kit + curated few-shots\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md, line 20).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep-with-fix",
   "reason": "Quotes found. I replaced 'who picked' with 'what picked', so no person is implied. The full field list is at MAIN_AGENT_ACTION_PACKET.md lines 184-196, and I added the line that opens it. The v8 note reporting predicted passes as 'IB pass' (candidate 0) is a live case of the failure. Related to 24 and 50; not a duplicate.",
   "statement": "Label every reported number with what produced it: the grader and its version, the number of attempts and what picked among them, any bank or fallback, the sample size and the class of evidence; mixing evidence classes produced false confidence.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/MAIN_AGENT_ACTION_PACKET.md",
     "lines": "201",
     "quote": "Mixing those proof classes caused false confidence in earlier work.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/MAIN_AGENT_ACTION_PACKET.md",
     "lines": "184",
     "quote": "Every generation artifact and summary should record:",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/MAIN_AGENT_ACTION_PACKET.md",
     "lines": "210",
     "quote": "New `summary.json` files can be read without context and answer: \"what exactly was measured?\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "282",
     "quote": "Best evidence always says which evaluator version, endpoint mode, and fallback mode were active.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 29,
   "verdict": "keep",
   "reason": "Quotes found. An adopted rule in both labs. General, and distinct from 43 and 44 because it concerns which grader certifies. No names.",
   "statement": "Certify only with the reference grader the work will be judged by, in its current version; diagnostic graders, older versions and self-evaluation are design evidence.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
     "lines": "110",
     "quote": "Use official/current IB only for certification. Diagnostic evaluator and older versions are not interchangeable.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md",
     "lines": "58",
     "quote": "Keep IB v2.5.7 as the certification target. Older grader wins are design evidence only.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/MAIN_AGENT_ACTION_PACKET.md",
     "lines": "216",
     "quote": "Do not use self-eval as certification.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 30,
   "verdict": "keep-with-fix",
   "reason": "Quotes found; line 99 repeats at 40 and 55. 'Never happened' cannot be shown from these files, so I softened it to what the acceptance records. A source review would have caught the duplication found under candidate 31. I reworded 'the maker' so no role is named. The core is the same as 43 (check against something that doesn't assume the answer) and close to 66; kept for the case it adds.",
   "statement": "An acceptance check must be independent of what it accepts: re-running the validator that produced a result only shows that the validator agrees with itself, and one such acceptance recorded none of the source review it had been asked for.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/to_main/2026-05-23T1831Z_DEN_REQUEST_validate_unit1_dbq_source_packs_v1.md",
     "lines": "52",
     "quote": "Please perform provenance/source-quality validation. Den's validator checks structure, Unit-1 contamination, text-bearing docs, topic coverage, primary-like count, and visual-risk filters. It does not independently fetch every URL or certify that normalized excerpts are acceptable for training.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T063156Z_2026-05-24T0630Z_UNIT1_DBQ_SOURCE_PACK_ACCEPT.md.md",
     "lines": "88",
     "quote": "main-a re-ran Den's gate independently:",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T063156Z_2026-05-24T0630Z_UNIT1_DBQ_SOURCE_PACK_ACCEPT.md.md",
     "lines": "99",
     "quote": "Matches Den's claim exactly (10/10 rows valid, no missing topic targets).",
     "verbatim": true
    }
   ],
   "against": "none found; the only 'provenance_status: accepted' line in the den reports comes from a smoke-test fixture of the intake script (~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T102632Z_UNIT-1_DBQ_SOURCE-PACK_ACCEPT.md.md, lines 7 and 69).",
   "general": true,
   "duplicate_of": "43",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep-with-fix",
   "reason": "The reader's quotes are verbatim, but they come from rejected rows of intermediate gate runs and list only documents 1-3, which is why the claim was left open. I checked it directly. From the nine repaired pack files (d13_unit1..9_dbq_source_packs_v1.jsonl, 10 rows each, in helpers/data/output) I extracted titles, IDs and content hashes, without printing any text. In all 43 topics with two packs, both packs hold the same seven titles with identical text. They differ only in doc_id (for example an _a/_b infix) and in the prompt. Unit 2 has 70 document slots but only 32 distinct titles. Every '10/10 valid' gate therefore covered 5 or 6 distinct document sets. Kind changed to measured. Related to 41 and 68; not a duplicate.",
   "statement": "Count distinct documents, not packs or labels, when a rule asks for coverage: in one build, each topic's two 'valid' source packs held the same seven texts under relabelled IDs, so a two-per-topic rule added no range.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/d13_unit2_dbq_source_packs_v1.jsonl",
     "lines": "1",
     "quote": "\"doc_id\": \"unit2_regions_a_doc1_virginia_charter_1606\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/d13_unit2_dbq_source_packs_v1.jsonl",
     "lines": "2",
     "quote": "\"doc_id\": \"unit2_regions_b_doc1_virginia_charter_1606\"",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit2_dbq_source_pack_gate_20260524T030000Z.md",
     "lines": "18",
     "quote": "| colonial_regions | 2 | 2 |",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit8_dbq_source_pack_gate_20260523T200817Z.md",
     "lines": "51, 55",
     "quote": "doc 1: Truman Doctrine address to Congress — no doc-level error",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 32,
   "verdict": "keep-with-fix",
   "reason": "Quotes found. 'Forced that scope's limits onto others' stated as observed what the scout only inferred from reading the prompts ('would force'). I reworded it and added the hard-coded period line. The one measured case: wrapping a generic all-scope fallback scored 0/3 (1357Z lines 31-33). Related to 63; not a duplicate.",
   "statement": "Prove each new scope on its own: a generator built for one scope had that scope's limits written into its prompts, and widening a prompt is no evidence that it transfers.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit2_9_coverage_scout_20260523.md",
     "lines": "125",
     "quote": "Do not claim Unit 2-9 coverage from prompt generalization alone.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit2_9_coverage_scout_20260523.md",
     "lines": "69",
     "quote": "Conclusion: running these solvers on Unit 2-9 would be actively wrong. They would force Unit-1 constraints onto later-period requests.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit2_9_coverage_scout_20260523.md",
     "lines": "57",
     "quote": "prompt hard-codes `Time period: 1491-1607 only`.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1357Z_BLOCKED_unit2_mcqset_parent_archetype.md",
     "lines": "49",
     "quote": "Unit-2 MCQ_SET expansion should not be delivered from parent fallback alone.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 33,
   "verdict": "keep",
   "reason": "Quotes found. I checked the estimated tally against the run file (den_mcq_solver_acceptance_20260524T080706Z.jsonl): 39 SUPERIOR and 4 ACCEPTABLE, where the note estimated '37+' and '~6'. General; close to 39 and 67 but not a duplicate.",
   "statement": "Take verdicts and counts from the structured result, never from summary prose; keyword triage flipped a repair verdict to green and a validated one to repair, and one tally was estimated from a log sample.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0600Z_DELIVERED_repair_result_triage_classifier_fix.md",
     "lines": "12",
     "quote": "The packet is explicitly `SECOND_TIER -> REPAIR`, but the first auto-triage run classified it as `validated_or_green_candidate` because headline pass-count language outranked repair/fail language.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0633Z_REPORT_unit1_validation_results_addendum.md",
     "lines": "50",
     "quote": "`scripts/triage_validation_result.sh` was patched because the first SAQ auto-triage saw the phrase `REPAIR pending` in a context table about MCQ and misclassified the SAQ VALIDATED packet as repair.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T084525Z_2026-05-24T0844Z_UNIT1_MCQ_SOLVER_VALIDATED.md.md",
     "lines": "153",
     "quote": "37+ SUPERIOR (estimating from log sample)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 34,
   "verdict": "keep",
   "reason": "Quotes found. The rule was adopted in two designs, one of them built, and never measured. The half about passing the reason back is contested by a third design (see against). Not a duplicate.",
   "statement": "When a check rejects a draft, regenerate only the stage that failed and pass the specific reason, not a generic 'try again'.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/MAIN_AGENT_ACTION_PACKET.md",
     "lines": "75",
     "quote": "Regenerate with concrete rejection reasons between stages, not a broad \"try again\".",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "233",
     "quote": "-> repair or regenerate with specific reason",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-19T1541Z_gate0_prototype_in_lab.md",
     "lines": "39",
     "quote": "Between stages, the validator rejects + re-asks ONLY the failing stage (not full restart).",
     "verbatim": true
    }
   ],
   "against": "The same directive took the opposite line on reasons: \"the question-generator doesn't see the validator's reasoning, only the reject signal.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-19T1541Z_gate0_prototype_in_lab.md, line 39).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 35,
   "verdict": "keep",
   "reason": "Quotes found. One item in 50 moves a rate by 2 points, and sampling error at that size is larger still, so if anything the statement understates the problem. Not a duplicate.",
   "statement": "Size the test to the claim; with 50 items one item moves the rate by 2 points, so a 98.8% against 99% claim cannot be settled.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T175907Z_2026-05-24T1759Z_UNIT1_DBQ_SOLVER_v3_VALIDATED_TARGET_REACHED.md.md",
     "lines": "137",
     "quote": "Statistical resolution at n=50 per cell is ±2pp; 98.8% sits within the noise band of 99%.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md",
     "lines": "85",
     "quote": "What is the smallest statistically honest validation gate that predicts full 26,355-row quality without a multi-day scorer run?",
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
   "verdict": "keep",
   "reason": "Quotes found. Measured only on the public items the repairs targeted (see against). Related to 58 (relevance) but not a duplicate. The historical names in the quotes are not people involved in the work.",
   "statement": "Fit a document set to its question: cover the whole span asked about, include more than one perspective including dissent, and drop documents that do not bear on it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0208Z_DELIVERED_unit4_dbq_solver_v1_candidate.md",
     "lines": "30",
     "quote": "foreign-policy rows lacked 1830s/1840s coverage and dissenting documents",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0102Z_DELIVERED_unit3_dbq_solver_v1_candidate.md",
     "lines": "29",
     "quote": "American-victory hard route used social/global legacy docs",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T2258Z_DELIVERED_unit6_dbq_solver_v1_candidate.md",
     "lines": "47",
     "quote": "Fixed Period 6 rubric metadata, irrelevant Plessy document in immigration route, and accidental Homestead Act / Homestead Strike slug collision.",
     "verbatim": true
    }
   ],
   "against": "The repairs were checked on the same public items they were made against: \"Public failures were repaired before delivery, including Second Great Awakening causation routing, foreign-policy coverage/dissent, and the invalid Hammond date.\" (~/Documents/aptraining/den-of-ideation/to_main/2026-05-24T0208Z_DEN_REQUEST_validate_unit4_dbq_solver_v1.md, line 30).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 37,
   "verdict": "keep",
   "reason": "Quotes found. Two cases. General; not a duplicate.",
   "statement": "Re-check content after any automatic cleanup; phrase substitution left awkward artifacts and stripping left documents too thin to pass.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T2050Z_DELIVERED_pipeline_solver_v7_supersedes_v6.md",
     "lines": "27",
     "quote": "Added specific repairs for `Pueblo Revolt of 1680`, `Virginia Company`, `Jamestown`, `Powhatan`, English-colony phrases, Chesapeake/New England, Pilgrim/Puritan phrases, and awkward replacement artifacts.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0339Z_DELIVERED_unit2_dbq_solver_v1_candidate.md",
     "lines": "30",
     "quote": "Colonial Society/Culture docs initially failed local doc-lock after sanitizer stripping; targeted repair probe passed at `1.0 SUPERIOR`.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 38,
   "verdict": "keep",
   "reason": "Quotes found. The reader's note that locking in seven retrieved documents took this item type from 0% to 29/30 is not established: the 29/30 came from the K6-plus-judge wrapper run, whose lever was 'source/prompt pipeline behavior' (added as a fourth item). The statement does not depend on that figure. Related to 64 (never describe a picture that isn't there) and 57; kept as the general rule about where source texts come from.",
   "statement": "Source texts that students analyse must be real documents supplied from outside the writer model, which only frames the task around them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "56",
     "quote": "The generator emitted fake maps, charts, photographs, and cartoon descriptions as if they were documents.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "72",
     "quote": "DBQ needs source ownership outside the model. The model can frame prompt/rubric, but source documents must come from retrieval or locked artifacts.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T132917Z_2026-05-27T1330Z_bm0zjn5z_n100_unit1_RAW_PROBE_REPORT.md.md",
     "lines": "129",
     "quote": "`stimulus_quality=0` on 75% of DBQ fails — primary-source documents are synthetic",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md",
     "lines": "10",
     "quote": "DBQ moved from structural 0% in v50/v52-era model-only runs to 29/30 in the best-worlds wrapper run. The winning lever was source/prompt pipeline behavior, not another DPO tweak.",
     "verbatim": true
    }
   ],
   "against": "This lineage's own 'validated' document lane served script-built normalized excerpts, and the grader passed them: \"Source packs use normalized excerpts and should receive provenance spot-check before promotion.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T2115Z_DELIVERED_unit8_dbq_solver_v1_candidate.md, line 55).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0615Z_REPORT_unit1_mcq_solver_v2_repair_delivery.md",
   "lines": "34",
   "quote": "No candidate is counted as a pass unless live IB returns a passing score.",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1509Z_DELIVERED_unit4_mcq_solver_v1_candidate.md",
   "lines": "17",
   "quote": "No timeout fallback is accepted as pass.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260528T030737Z_2026-05-28T0312Z_ESCALATE_F14_blocking_track_B_v2_grading.md.md",
   "lines": "105",
   "quote": "NOT firing IB grading on the 79 partial rows (would mis-represent the corpus)",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "104",
   "quote": "Best-of-N was implemented once but not actually active.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-25T0615Z_TASK_concrete_deployable_workflow.md",
   "lines": "94",
   "quote": "main-a runs n=50 hidden hold-out K=1 single-shot on the WORKFLOW (not your dev scripts) — confirms numbers reproduce",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/reports/v10_validated_artifact_integrity_20260524T0421Z.md",
   "lines": "7",
   "quote": "The current production solver in Den is byte-identical to the main-a promoted v10 artifact.",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md",
   "lines": "24",
   "quote": "Hard gates are deliberately narrow. The first version over-blocked known passing rows because InceptBench tolerates some source-referential wording.",
   "ok": false
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/MAIN_AGENT_ACTION_PACKET.md",
   "lines": "218",
   "quote": "Do not add visual DBQ documents unless the evaluator receives real visual/OCR payloads.",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1958Z_DELIVERED_unit1_dbq_solver_v1_candidate.md",
   "lines": "72",
   "quote": "Adding canonical `rubric_notes` and matching known DBQ schema made IB return scores.",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
   "lines": "19",
   "quote": "the probe flips on *borderline* items",
   "ok": true
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/to_main/2026-05-24T1113Z_DEN_NOTICE_mcqset_route_inspection_no_safe_unblock.md",
   "lines": "15",
   "quote": "per-child MCQ fallback is unreliable: children 1 and 2 timed out at 60s; child 3 scored `1.0 SUPERIOR`",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "125",
   "quote": "Keep generation/evaluation artifacts with prompt messages; DPO and debugging require full conversation context, not only output JSON.",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T2056Z_DELIVERED_pipeline_solver_v8_timeout_fallback.md",
   "lines": "51",
   "quote": "original v80bchain timeout attempt is preserved in `audit_trail`",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T2107Z_ACCEPTANCE_GREEN_v9_hidden50.md",
   "lines": "32",
   "quote": "IB: cache/live paths are labeled for IB v2.5.11; hidden runner judged returned score/status through `prototypes/run_den_solver_on_jsonl.py`",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md",
   "lines": "54",
   "quote": "The deterministic hard gates are good as a safety layer, not a complete quality judge.",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-22T1845Z_ULTIMATE_DELIVERY_CHALLENGE.md",
   "lines": "42",
   "quote": "Acceptance criteria (binary, no negotiation)",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-25T0615Z_TASK_concrete_deployable_workflow.md",
   "lines": "88",
   "quote": "No more \"99.6% goal complete\" framing in production-facing docs. Use the K=1 numbers as headlines.",
   "ok": false
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1807Z_DELIVERED_pipeline_solver.md",
   "lines": "99",
   "quote": "This is still not a final acceptance claim: main-a's 50 fresh prompts are the actual binary gate.",
   "ok": false
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "111",
   "quote": "Diagnose by failed dimension, not by aggregate score. DBQ 0%, MCQ_SET 25%, and SAQ 0% have different mechanisms.",
   "ok": false
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "122",
   "quote": "For SAQ/LEQ/DBQ, replace hallucination-prone evidence lists with verified-facts-only or analytical-category scoring notes.",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/HANDOVER.md",
   "lines": "123",
   "quote": "SAQ scoring notes should avoid hallucination-prone evidence lists",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "88",
   "quote": "Facts work better as constraints than as inspiration.",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1538Z_DELIVERED_unit5_mcq_solver_v1_candidate.md",
   "lines": "29",
   "quote": "the miss was `Sectional Conflict: Regional Differences` routed to a generic Compromise item and scored `0.8 INFERIOR`.",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "46",
   "quote": "InceptBench pass is not just `overall_score >= 0.85`; hard-fail dimensions must also be perfect.",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T115335Z_2026-05-24T1153Z_UNIT1_DBQ_SOLVER_v2_VALIDATED.md.md",
   "lines": "127",
   "quote": "5 of v1's 6 failures repaired; 1 (row 39) still fails; 1 new fail (row 29) introduced — net +4 passes.",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "131",
   "quote": "Human/agent external review helps when hypotheses are stuck, but the review must be grounded in actual failing artifacts.",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "101",
   "quote": "“Be careful” factuality warnings hurt; caution text without hard constraints creates hedging, not accuracy.",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "91",
   "quote": "For SAQ/LEQ/DBQ scoring notes, “don’t list specific facts” failed. Verified-facts-only constraints are stronger.",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "114",
   "quote": "Treat metadata correctness as a hard gate: course, unit, period, standard, and type must propagate authoritatively through every generator path.",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/HANDOVER.md",
   "lines": "122",
   "quote": "Period metadata bugs can dominate failure rate",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
   "lines": "57",
   "quote": "InceptBench hard-zeroed those because the stimulus was not real analyzable source material.",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "120",
   "quote": "Best-of-N is a multiplier, not a miracle. It works once base per-type pass rate is competent; it does not fix systematic failures.",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260529T085132Z_2026-05-29T0850Z_v86_VERDICT_57pct_aggregate_DBQ_MCQ_SET_catastrophic_99stack_rescue.md.md",
   "lines": "114",
   "quote": "Catastrophic cells are CONSISTENTLY catastrophic across seeds (not flaky); strong cells are CONSISTENTLY strong.",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/reports/cell_family_archetype_scout_20260523.md",
   "lines": "134",
   "quote": "Do not run DBQ as a generic \"best of K\" prompt; DBQ failure mode is source integrity, not merely weak prose.",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md",
   "lines": "40",
   "quote": "Naive best-of-scored-candidates banking overfit: predicted 138/150, but fresh IB scored 126/150.",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-22T1845Z_ULTIMATE_DELIVERY_CHALLENGE.md",
   "lines": "14",
   "quote": "It is curation after the fact. It does not generalize to fresh prompts.",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
   "lines": "13",
   "quote": "Anti-leak scaffold built by rule, not the model.",
   "ok": true
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "121",
   "quote": "For MCQ_SET, add explicit coverage fields to the plan step, such as entities/nations/themes to cover, then bind child questions to that plan.",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "44",
   "quote": "The rule is aggregate -> dimension -> item -> hypothesis -> distinguish -> confirm -> fix.",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1840Z_DELIVERED_pipeline_solver.md",
   "lines": "59",
   "quote": "targeted Native-environment easy repair retained after live IB improved that row from 0.80 to 1.00;",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md",
   "lines": "75",
   "quote": "Record answer-key distribution for MCQ_SET and repair when balance caps otherwise-good sets.",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
   "lines": "230",
   "quote": "all child questions depend on stimulus",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1831Z_DELIVERED_unit1_dbq_source_packs_v1_full_gate_green.md",
   "lines": "69",
   "quote": "decide whether normalized excerpts are acceptable or whether exact quoted excerpts are required",
   "ok": false
  }
 ]
}
```
