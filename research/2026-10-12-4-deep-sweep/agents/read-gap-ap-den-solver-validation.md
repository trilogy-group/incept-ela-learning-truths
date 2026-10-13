# read:gap:ap-den-solver-validation

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "ap-den-solver-validation",
 "coverage": {
  "read": [
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/ - 152 of 153 files: every delivery, repair, blocked and report note plus STATUS.md (repetitive notes read with blank and command lines stripped)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/ - all 17 requests",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
   "~/Documents/aptraining/den-of-ideation/HANDOVER.md, MAIN_AGENT_ACTION_PACKET.md, CLAUDE.md",
   "~/Documents/aptraining/den-of-ideation/to_main/ - all 53 requests",
   "~/Documents/aptraining/den-of-ideation/from_den/ - the 2 files absent from comms/from_den (2026-05-25T0735Z_DELIVERED_WORKFLOW_HUMAN_CONSOLE.md, 2026-05-25T0758Z_BLOCKED_WORKFLOW_GENERIC_MCq_RETEST.md); the other 110 are copies",
   "~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md and experiments/b0034_k6_baseline_reproduction/REPRODUCTION_REPORT.md (the only .md notes under experiments/)",
   "~/Documents/aptraining/den-of-ideation/reports/: v10_validated_artifact_integrity_20260524T0421Z.md; current_completion_audit_* (10: first and last in full, the other 8 diffed for new lines); current_objective_gate_audit_addendum_* (2); unit1_validation_lane_packet, unit1_validation_execution_runbook, unit1_validation_results_addendum; all 8 *_validated_addendum_*; all 6 *_repair_delivery_*; all 26 *_dbq_source_pack_gate_* (mode, counts, top failures, listed documents); unit2_9_coverage_scout_20260523.md; cell_family_archetype_scout_20260523.md; NEXT_ACTION_POINTER.md",
   "~/Documents/aptraining/den-of-ideation/reports/validation_matrix/*.md (latest.md and first snapshot in full; gate counts of all 28 snapshots)",
   "~/Documents/aptraining/den-of-ideation/reports/validation_triage/*.md (39 files; the raw result preview of every distinct packet read; timestamp duplicates checked)",
   "~/Documents/aptraining/den-of-ideation/reports/validated_evidence_drafts/*.md (18) and reports/repair_bead_drafts/*.md (14): samples in full, the rest checked for lines not already in the triage reports (none new)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md, parallel_ideas_lab_distilled.md, parallel_ideas_lab_structural_takeaways.md (byte-identical to the den-of-ideation copies)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-22T2116Z_den_solver_v8_FIRST_VALIDATED/den_solver_acceptance_20260522T210237Z.jsonl and .../2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/den_solver_acceptance_20260523T082319Z.jsonl - field counts only, no rows printed",
   "Beyond the listed scope, because they explain the counted runs: the two VALIDATION_REASON.md files and the two small den_solver_acceptance_*_summary.json files in those same artifacts/validated folders"
  ],
  "skipped": [
   "comms/from_den/TURN_LOG.md - 243 KB running turn log; logs are excluded by the rules",
   "den-of-ideation reports/monitor/, reports/fireworks_launches/, timestamp-only files, .venv*, prototypes/, scripts/ - excluded by scope",
   "reports/validation_matrix/*.csv and *.jsonl - data dumps; the .md snapshots carry the same states",
   "den-of-ideation/reports files outside the named list (MASTER_SYNTHESIS.md, deployable_workflow_*, mcqset_* probes, main_a_* manifests, den_objective/den_solver_expansion/live_* audits, unit1_leq_solver_v1_delivery, dbq_source_pack_repair_list, u2_9_dbq_coverage_scout, k_12 and ap_social_studies distillations, agentic_development_*, next_training_plan_*, post14_*, mcqset_50_50_*, synapse_meeter_current_intel) - not named for this direction",
   "den-of-ideation/.agent, .agents, .claude, inbox, outbox, to_orch, deployable/ - agent configuration and code, not findings",
   "experiments/ data files (audit JSON, self-test JSONL) - data dumps",
   "comms/from_main, from_cheater and other mailboxes cited by the triage reports (e.g. the stimulus-strip exploit reports) - outside this scope"
  ],
  "notes": "Rating-field counts (ib_rating; solver_result.ib_rating identical). File 1, artifacts/validated/2026-05-22T2116Z_den_solver_v8_FIRST_VALIDATED/den_solver_acceptance_20260522T210237Z.jsonl, 50 rows: PREDICTED_PASS_CACHE_NEIGHBOR 46, PREDICTED_PASS_TIMEOUT_TEMPLATE_FALLBACK 4. File 2, artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/den_solver_acceptance_20260523T082319Z.jsonl, 50 rows: PREDICTED_PASS_CACHE_NEIGHBOR 50. Neither file has a single SUPERIOR, ACCEPTABLE or INFERIOR rating. Related counts: status=pass and passed=true on 50/50 rows in both; ib_score is exactly 0.95 on 50/50 rows in both; final_content_source is v80bchain_fresh_generation 46 + deterministic_timeout_fallback_after_v80b_attempt 4 (file 1) and v80bchain_fresh_generation 50 (file 2); the audit trails hold no grader call outside the prediction stage; file 2's 50 predictions rest on 18 distinct earlier-scored archetype cache keys (archetype_score 0.98-1.0); both summaries give input_jsonl /tmp/holdout_for_den_v2.jsonl, the holdout of the earlier 37/50 run whose failure summary drove the repairs. So the 'validated' 100% anchor of the later 99.6% projection carries no grader verdict. One triage preview (20260525T191103Z_..._v97_proceed_as_built_ack) contains a live API key line; it was not reproduced. No cited path contains a person's name. The home-directory account name in every absolute path was not treated as name-bearing. The two in-scope files with a person's name in the path (to_den/2026-05-28T1615Z_[name]_DIRECTIVE_check_in_with_main_a.md, validation_triage/..._[name]_DELIVERY_unit1_path_to_95pct...) were read and not cited. Training-mechanics content (DPO/SFT plans, v86/v97 verdicts, hyperparameters) was read and excluded. Line numbers were re-checked with grep -n against the original files; triage reports repeat lines, so the raw-preview line is cited."
 },
 "candidates": [
  {
   "statement": "Count a pass only when the grader actually returned it; a pass predicted from similarity to earlier passing items, or assumed after a timeout, is not a verdict.",
   "kind": "measured",
   "found_by": "Both runs promoted as 'validated' 50/50 carry no grader-returned rating. Counting the rating field gives 46 PREDICTED_PASS_CACHE_NEIGHBOR + 4 PREDICTED_PASS_TIMEOUT_TEMPLATE_FALLBACK in one file and 50 PREDICTED_PASS_CACHE_NEIGHBOR in the other, with ib_score exactly 0.95 on all 100 rows. The second run's predictions trace to 18 earlier-scored template entries. The design directive said to skip grading whenever a pass was predicted. In a parallel lane the same practice was caught: headline 47/50 but 30/50 with real grades (17 predicted timeout passes), and the version without the prediction path scored 43/50 with every pass graded.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/den_solver_acceptance_20260523T082319Z.jsonl",
     "lines": "1-50 (all 50 rows)",
     "quote": "\"ib_rating\": \"PREDICTED_PASS_CACHE_NEIGHBOR\""
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-22T1910Z_iterate_toward_LLM_FINAL_compatible.md",
     "lines": "23",
     "quote": "3. If predicted-pass: skip full IB grade, return generation directly"
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit1_mcq_solver_v2_validated_addendum_20260524T085013Z.md",
     "lines": "43",
     "quote": "The headline rate dropped because v1 was counting fallback-aided passes; v2 is the defensible result."
    }
   ],
   "against": "The promoting note argued the predictor was grader-backed: \"the cached archetype is itself derived from live-IB-validated v80bchain content, so it's not \\\"deterministic-from-bank\\\" in the prior sense.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-22T2116Z_den_solver_v8_FIRST_VALIDATED/VALIDATION_REASON.md, line 62).",
   "adds_to_existing": [
    9,
    43,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Audit for the property a result must have, not for the absence of one known bad label; a check for one fallback label waved through runs whose every rating was a differently named prediction.",
   "kind": "measured",
   "found_by": "A later lane was demoted for 17 'PREDICTED_PASS_LOCAL' passes and told to meet the earlier question-set run's 'strict fresh' bar. Every one of that bar run's 50 ratings was PREDICTED_PASS_CACHE_NEIGHBOR, which the 'no PREDICTED_PASS_LOCAL_*' check never matches. 'Strict fresh' described where the content came from, not where the verdict came from. The acceptance criteria in both promoted summaries were min_passed, cost, latency and no_crashes, with nothing about the source of a pass.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T084525Z_2026-05-24T0844Z_UNIT1_MCQ_SOLVER_VALIDATED.md.md",
     "lines": "157",
     "quote": "Same bar as Den v10, Den SAQ v1, Den DBQ v1 (no PREDICTED_PASS_LOCAL_* anywhere)."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T073015Z_2026-05-24T0601Z_UNIT1_MCQ_SOLVER_REPAIR.md.md",
     "lines": "136",
     "quote": "Den v10 precedent (MCQ_SET, 2026-05-23T08:40Z) was promoted as **VALIDATED** specifically because it cleared 50/50 STRICT FRESH with zero timeout fallback. That set the bar."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/VALIDATION_REASON.md",
     "lines": "5",
     "quote": "**Verdict:** 50/50 = **100.0% STRICT FRESH** — zero timeout-fallback, all v80bchain fresh generation"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    43,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When every item in a run gets the same score, suspect the measurement before the content; a uniform score came from a wrong input shape or a placeholder.",
   "kind": "measured",
   "found_by": "30/30 source excerpts sent to the grader outside their task shape all scored 0.55 with stim_quality=0, and the test was declared invalid. In both promoted acceptance files ib_score is 0.95 on 50 of 50 rows, a constant attached to predicted passes rather than a graded score.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T220400Z_2026-05-28T0008Z_track_A_30row_sample_INVALID_TEST_RECOVERY.md.md",
     "lines": "82",
     "quote": "Result: 30/30 scored 0.55 overall, stim_quality=0, rated INFERIOR."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T220400Z_2026-05-28T0008Z_track_A_30row_sample_INVALID_TEST_RECOVERY.md.md",
     "lines": "105",
     "quote": "Recognized 0.55 floor + 0/30 = signature of wrong-schema, not content failure"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-22T2116Z_den_solver_v8_FIRST_VALIDATED/den_solver_acceptance_20260522T210237Z.jsonl",
     "lines": "1-50 (all 50 rows)",
     "quote": "\"ib_score\": 0.95"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Judge a component inside the complete task it will serve; grading a part on its own, as if it were the whole task, gives a floor score that says nothing about the part.",
   "kind": "measured",
   "found_by": "Source excerpts were graded alone as if each were a full document-based task. All 30 floored at 0.55, and the result was voided. The stated fix was to place the excerpts in a full task (prompt, seven documents, marking guide), generate it, and grade that.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T220400Z_2026-05-28T0008Z_track_A_30row_sample_INVALID_TEST_RECOVERY.md.md",
     "lines": "84",
     "quote": "IB v2.5.11 grades DBQs as complete prompt+documents+rubric structures. Standalone primary-source excerpts aren't a DBQ shape."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T220400Z_2026-05-28T0008Z_track_A_30row_sample_INVALID_TEST_RECOVERY.md.md",
     "lines": "88",
     "quote": "The proper test for Track A excerpts' DBQ-stim quality is downstream: **embed the excerpts in a full DBQ structure (prompt + 7 documents + rubric) + generate that DBQ → grade THAT.**"
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T220400Z_2026-05-28T0008Z_track_A_30row_sample_INVALID_TEST_RECOVERY.md.md",
     "lines": "97",
     "quote": "research-first violated: I should have read the IB grader's expected schema for stim_quality grading before designing the test"
    }
   ],
   "against": "Structural retrieval checks can still run on their own: \"DBQ source retrieval should be tested independently from model generation.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md, line 100).",
   "adds_to_existing": [
    30,
    33
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A test you have repaired against is spent, public or hidden; once its failures steer the fixes, rerunning it no longer measures new performance, so confirm on items the repairer never saw.",
   "kind": "measured",
   "found_by": "The first hidden run scored 37/50. Its shared failure summary drove targeted repairs (prior-failure replays 4/13, 5/13, 6/13, then 13/13), and the repairer predicted a ceiling around 50/50 on the same failure mix. Both later 'validated' 50/50 runs used the same holdout file. Item-type lanes were re-validated on the same rows 50-99 after repairs aimed at those rows (30 to 43 to 50/50, 44 to 48 to 49/50, 47 to 48 to 50/50). On fresh rows 100-149, one attempt per item, the stack scored 239/250 = 95.6% and a new failure family appeared. One ten-item public set was patched from 6/10 to 7/10 to 10/10, and a different two-item sample then failed 1/2.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/den_solver_acceptance_20260523T082319Z_summary.json",
     "lines": "13",
     "quote": "\"input_jsonl\": \"/tmp/holdout_for_den_v2.jsonl\","
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1936Z_DELIVERED_pipeline_solver.md",
     "lines": "15",
     "quote": "This version targets the exact failure classes main-a shared from the first hidden run without reading the hidden prompt file."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/to_main/2026-05-23T1808Z_DEN_REQUEST_validate_unit9_mcq_solver_v1.md",
     "lines": "26",
     "quote": "third public n=10 was `10/10`, but runner sanity failed `1/2`"
    }
   ],
   "against": "The repairer flagged the risk itself: \"A fresh hidden seed is still the real gate.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1936Z_DELIVERED_pipeline_solver.md, line 77). The 95.6% on fresh rows shows the repairs partly carried over.",
   "adds_to_existing": [
    48,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep held-out items out of the builder's reach; rows sliced from the file the builder samples its self-tests from, and failing rows handed back as files, are not held out.",
   "kind": "measured",
   "found_by": "Each 'hidden' 50-row set was rows 50-99 of the same benchmark file the solver's self-tests read. Repair probes then ran directly on files of the hidden failure rows (unit1_dbq_v1_failure_rows.jsonl, unit1_leq_v1_failure_rows_47_49.jsonl, unit1_dbq_v2_failure_rows_29_39.jsonl) before re-validation on those same rows.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T073015Z_2026-05-24T0601Z_UNIT1_MCQ_SOLVER_REPAIR.md.md",
     "lines": "114",
     "quote": "hidden validation input: `/tmp/unit1_mcq_holdout_n50.jsonl` (MCQ rows 50-99 from `~/Downloads/unit-1-apush-benchmark.jsonl` — no overlap with Den's selftest step-sample)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1709Z_DELIVERED_pipeline_solver.md",
     "lines": "46-48",
     "quote": "`~/Downloads/unit-1-apush-benchmark.jsonl`"
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit1_dbq_solver_v2_repair_delivery_20260524T105934Z.md",
     "lines": "30",
     "quote": "input: `experiments/dbq_v2_failure_probe/unit1_dbq_v1_failure_rows.jsonl`"
    }
   ],
   "against": "Overlap with the builder's own sample was checked (\"no overlap with Den's selftest step-sample\", same line 114), and the first challenge required a prompt diff: \"I'll diff your prompt list against my n=50; any overlap = automatic FAIL\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-22T1845Z_ULTIMATE_DELIVERY_CHALLENGE.md, line 52).",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Headline the score of the mode that will ship; a best-of-several pick made by the grader overstates what one attempt delivers.",
   "kind": "measured",
   "found_by": "The 'goal complete' figure was 99.6%, with four attempts per item and the grader picking the best. One attempt per item on fresh rows gave 239/250 = 95.6%. The essay lane fell to 48/50, and the short-answer lane was expected near 86% single-shot after 50/50 when picked. A graded retest of the single-shot service scored 8/20 on single questions, and a harder fresh set on the hosted service gave 78.57%. Production could not call the grader at all.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/current_completion_audit_20260524T2053Z.md",
     "lines": "40",
     "quote": "Do not mislabel this as deployable K1 production `>=99%`."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T202325Z_2026-05-24T2022Z_UNIT1_LEQ_SOLVER_v3_VALIDATED_99_6pct.md.md",
     "lines": "140",
     "quote": "**Deployable bound is K=1 single-shot.** Slice-2 K=1 (rows 100-149) was 239/250 = 95.6% with LEQ v2."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-25T0615Z_TASK_concrete_deployable_workflow.md",
     "lines": "88",
     "quote": "No more \"99.6% goal complete\" framing in production-facing docs. Use the K=1 numbers as headlines."
    }
   ],
   "against": "The 8/20 retest used a thinner generic prompt, so it is not a clean comparison: \"The missing lift is in the actual specialist solver mechanics, not the thin deployable generic prompt.\" (~/Documents/aptraining/den-of-ideation/from_den/2026-05-25T0758Z_BLOCKED_WORKFLOW_GENERIC_MCq_RETEST.md, line 18).",
   "adds_to_existing": [
    46,
    65,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Score only what the generator made for the request; label any banked, cached, templated or fallback output, and treat implausibly fast 'generation' as a sign that something else answered.",
   "kind": "measured",
   "found_by": "Template-plus-cache versions scored 44/50 on their own sample at about 0.01 s per item and $0.00, because answers came from earlier-graded entries; they then scored 37/50 on the hidden set. Later-unit 'solvers' were template banks (mean_cost_usd 0.0) patched to 10/10. In a sibling lab, exports at ~0.40 s were voided as quality evidence, and a deployment scaled to zero silently turned model output into fallback output. A contract then banned returning banks as final content.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1840Z_DELIVERED_pipeline_solver.md",
     "lines": "86",
     "quote": "elapsed: 0.150s because current archetypes were backed by prior live IB cache entries"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md",
     "lines": "49",
     "quote": "Deterministic fallback can fake readiness. Exports with ~0.40s generation latency were later marked invalid as quality evidence because they were fallback-shaped rather than model-shaped."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-22T1910Z_iterate_toward_LLM_FINAL_compatible.md",
     "lines": "12",
     "quote": "Production explicitly forbids deterministic returns (cache lookups, prewritten templates, archetype banks) as the FINAL answer. Banks/rescues may inform prompts but cannot be returned."
    }
   ],
   "against": "Fixed retrieval was kept for one item type: \"Document that DBQ is retrieval-with-cleanup, not LLM generation per call.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-25T0615Z_TASK_concrete_deployable_workflow.md, line 52). Cached fallback output was also promoted as a pass because it had once been graded (VALIDATION_REASON.md of the first validated run, line 62).",
   "adds_to_existing": [
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Format and leak checks catch broken items, not weak ones; keep them as safety rails and judge quality separately.",
   "kind": "measured",
   "found_by": "On a scored set, the deterministic validator passed 12 of 14 failing items and wrongly failed 1 of 16 passing ones. A shape-only acceptance passed 25/25 in 0.006 s, while a graded retest of the same service scored 8/20.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md",
     "lines": "47",
     "quote": "\"failed_validator_passed\": 12,"
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md",
     "lines": "54",
     "quote": "The deterministic hard gates are good as a safety layer, not a complete quality judge."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/from_den/2026-05-25T0758Z_BLOCKED_WORKFLOW_GENERIC_MCq_RETEST.md",
     "lines": "12",
     "quote": "`/no_think` generic deployable MCQ: `8/20 = 40.0%`"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    28,
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Hard-block only crisp failures such as broken format, a wrong key or a copied answer, and keep fuzzy signals advisory; hard-blocking a fuzzy wording check rejected items that pass.",
   "kind": "measured",
   "found_by": "The first validator hard-blocked source-referential, reading-style stems and over-blocked known passing items. The split that was kept: hard gates for schema, missing fields, answer leaks, extreme length and key clustering; advisory flags for wording.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md",
     "lines": "24",
     "quote": "Hard gates are deliberately narrow. The first version over-blocked known passing rows because InceptBench tolerates some source-referential wording."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/MAIN_AGENT_ACTION_PACKET.md",
     "lines": "74",
     "quote": "Keep reading-comprehension phrasing advisory unless it combines with another failure. The prototype showed hard-blocking it over-rejects known passing rows."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/MAIN_AGENT_ACTION_PACKET.md",
     "lines": "73",
     "quote": "Keep hard gates narrow: malformed schema, answer key breakage, copied answer leakage, extreme length, answer-key clustering."
    }
   ],
   "against": "A later design hard-rejects on a semantic check before grading: \"reject any item whose answer is derivable from the stimulus\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md, line 16).",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a source is there to prompt the use of knowledge rather than to test reading, each question should need both the source and that knowledge; check that it fails with the source hidden and is not settled by the source alone.",
   "kind": "adopted rule",
   "found_by": "The grader's leak probe failed a whole question set when more than 20% of its questions could be answered from the stimulus alone. The eight sets still failing after known rescues needed outside-knowledge hooks and no dependence on the stimulus's phrasing. The pipeline's validator also required that every question depend on the stimulus.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
     "lines": "7",
     "quote": "The eduacc leak-probe fails a set when >20% of child questions are answerable **from the stimulus alone**."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md",
     "lines": "109",
     "quote": "Fix generation/selector semantics for the eight remaining rows: outside-knowledge hooks, same-period distractors, no stimulus phrase dependency, and compact payloads to avoid score timeouts."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "229",
     "quote": "APUSH outside knowledge required"
    }
   ],
   "against": "\"The first version over-blocked known passing rows because InceptBench tolerates some source-referential wording.\" (~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md, line 24).",
   "adds_to_existing": [
    5,
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Decide in code, before the model writes any prose, what each question covers and what its answer hinges on, and let the model only render that plan; left free, generation drifts to whatever is easiest to answer.",
   "kind": "adopted rule",
   "found_by": "The chosen design committed baselines before running: freeform 0.31 and structured one-stage 0.6 on the target metric. Freeform output 'leaks by default'. Earlier work found question sets better when a plan step fixed each question's coverage. The two-stage run itself was queued, not yet measured.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
     "lines": "8",
     "quote": "Freeform generation leaks by default (least-resistance = stimulus-answerable)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
     "lines": "12",
     "quote": "select the **curriculum fact the correct answer hinges on + assert it is ABSENT from the stimulus**;"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
     "lines": "75",
     "quote": "MCQ_SET works better when the plan step constrains what each child question must cover."
    }
   ],
   "against": "\"over-constrained Stage 1 can pass eduacc but break factual/coherence\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md, line 37); \"Status: queued for the macmini executor / main-a on reconnect.\" (same file, line 44).",
   "adds_to_existing": [
    29,
    67,
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before trusting any improvement, re-grade the same items several times to learn the grader's own agreement, and treat differences inside that ceiling as noise.",
   "kind": "adopted rule",
   "found_by": "One item type's scores clustered at 0.55-0.84, just under the 0.85 pass line, where the probe flips on borderline items. The plan made grader self-agreement the first measurement, since self-agreement near 0.6 would cap any generator.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
     "lines": "36",
     "quote": "**ORACLE CEILING — MEASURE FIRST:** re-grade SAME mcq_set items Kx → grader self-agreement. ~0.6 ⇒ coin-flip-capped ⇒ generation can't reach 0.99 robustly ⇒ grader-side fix. **No delta is trustworthy until the ceiling is known.**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
     "lines": "19",
     "quote": "the probe flips on *borderline* items"
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T192220Z_2026-05-27T1922Z_v80b_n100_unit1_BASELINE_REPORT.md.md",
     "lines": "109",
     "quote": "scores cluster 0.55-0.84 just under 0.85 threshold"
    }
   ],
   "against": "Elsewhere, small differences at n=50 were read without a measured ceiling: \"Statistical resolution at n=50 per cell is ±2pp; 98.8% sits within the noise band of 99%.\" (~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T175907Z_2026-05-24T1759Z_UNIT1_DBQ_SOLVER_v3_VALIDATED_TARGET_REACHED.md.md, line 137).",
   "adds_to_existing": [
    34,
    35
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Fix the headline measure, the baselines to beat, the pass bar and the kill criterion before running, and hold to them afterwards.",
   "kind": "adopted rule",
   "found_by": "The challenge set a binary bar in advance: ≥39/50 on 50 fresh prompts, cost and latency caps, and an overlap diff. The generation plan was written 'contract-first', with baselines and a kill criterion. Later, a 98.8% result was described as having 'essentially reached' a 99% bar.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-22T1845Z_ULTIMATE_DELIVERY_CHALLENGE.md",
     "lines": "42",
     "quote": "Acceptance criteria (binary, no negotiation)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
     "lines": "33",
     "quote": "CONTRACT-FIRST (commit before firing)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
     "lines": "38",
     "quote": "**Kill criterion:** 2-stage doesn't beat `max(0.6+margin, ceiling−margin)` at K-grade after n KCs ⇒ generation lever ALSO closed ⇒ MCQ_SET genuinely grader-capped."
    }
   ],
   "against": "\"Main-a called this \\\"essentially reached\\\" within measurement noise. Den's literal audit does not mark complete because `98.8% < 99.0%`.\" (~/Documents/aptraining/den-of-ideation/reports/unit1_dbq_solver_v3_validated_addendum_20260524T1810Z.md, line 55).",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a fix targets one criterion or one part, re-grade every criterion and the parts you did not touch, because tightening one dimension can break another.",
   "kind": "measured",
   "found_by": "Broad rewrites aimed at failing families regressed under live grading and were reverted, while narrow repairs held (one row went from 0.80 to 1.00). The generation plan requires grading all criteria, because over-constraining for one can break factual accuracy and coherence. The gate required other item types to stay within ±2pp.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1840Z_DELIVERED_pipeline_solver.md",
     "lines": "60",
     "quote": "rejected transatlantic rewrite and broad environment rewrite after live IB showed regressions;"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
     "lines": "37",
     "quote": "**Grade ALL criteria** (factual_accuracy + educational_accuracy) — over-constrained Stage 1 can pass eduacc but break factual/coherence."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-19T1541Z_gate0_prototype_in_lab.md",
     "lines": "63",
     "quote": "Other cells within ±2pp of K=6 baseline (DBQ 29/30, LEQ 29/30, MCQ 28/30, SAQ 30/30) — you may need to run those too for the no-regression check"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    59,
    60,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Repair the class of failure, keyed to what the item is about and how it is built, not the failing row; row-level patches pass their rows while new failures appear elsewhere.",
   "kind": "measured",
   "found_by": "A source-text repair fixed 5 of 6 target rows; one still failed and a new one failed (44/50 to 48/50). An essay repair fixed rows 47 and 48, while row 49 still failed and row 27 newly failed. Several fixes were hand-built routes for one named family, and on fresh rows a new family failed.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "281",
     "quote": "Dynamic repair works only when keyed to standard/type/context, not exact benchmark row IDs."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md",
     "lines": "67",
     "quote": "Add type-specific failure buckets and generalized repair proposals keyed by `substandard_id`, standard description, type, and retrieved sources rather than exact row ID."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit1_leq_solver_v2_validated_addendum_20260524T1633Z.md",
     "lines": "35",
     "quote": "Rows `47` and `48` from v1 now pass, so the Maya chronology repair worked. Row `49` remains failed and a new row `27` failed."
    }
   ],
   "against": "Some row-targeted repairs did carry to fresh rows: single-attempt on rows 100-149 gave \"239/250 = 95.6%\" (~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T202325Z_2026-05-24T2022Z_UNIT1_LEQ_SOLVER_v3_VALIDATED_99_6pct.md.md, line 140).",
   "adds_to_existing": [
    60,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give students source excerpts to analyse, never summaries or notes that state a source's purpose or significance, because those do the analysis for them.",
   "kind": "measured",
   "found_by": "All six hidden failures of the first document-question solver shared 'analysis leakage'. Replacing summaries with excerpts moved single rows from 0.55 to 0.70 to 1.0, and from 0.675 INFERIOR to 1.0. The set went from 44/50 to 48/50, re-scored on the same rows. Leaks also came in through metadata sentences and copied analytical wording.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/to_main/2026-05-24T1059Z_DEN_REQUEST_validate_unit1_dbq_solver_v2_source_text_repair.md",
     "lines": "20",
     "quote": "The shared failure class was analysis leakage in DBQ document text: summaries gave away source purpose/significance instead of making students infer it."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1958Z_DELIVERED_unit1_dbq_solver_v1_candidate.md",
     "lines": "73",
     "quote": "Cultural perspective row improved 0.55 -> 0.70 -> 1.0 after replacing summary docs with source-like excerpts and adding Indigenous-perspective documents."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0255Z_DELIVERED_unit9_dbq_solver_v1_candidate.md",
     "lines": "29",
     "quote": "Migration/immigration hard row initially scored `0.675 INFERIOR` because the documents read like summaries rather than source excerpts."
    }
   ],
   "against": "The repaired packs were themselves \"normalized excerpts/source summaries\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T2009Z_DELIVERED_unit8_dbq_source_pack_gate.md, line 36), and the 44 to 48 gain was measured on the rows that defined the failure.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Attribute every source truthfully, by who made it and when, rather than dating it to the period it describes.",
   "kind": "measured",
   "found_by": "One document set failed on fake period dates for its sources and passed once they were honestly attributed as modern or reconstructed. A later source bundle carried an open honesty flag because 89% of its items were dated by subject period.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1958Z_DELIVERED_unit1_dbq_solver_v1_candidate.md",
     "lines": "74",
     "quote": "Native environment row failed on fake `1491` source dates; honest modern/ethnohistorical attribution fixed it."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T220400Z_2026-05-28T0008Z_track_A_30row_sample_INVALID_TEST_RECOVERY.md.md",
     "lines": "96",
     "quote": "PIL still owes the a/b decision on the honesty flag (89% subject-period-dated)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    17,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check the sources a task rests on before building or grading the task, for the right period, real text rather than a summary or a missing image, enough length and distinct origins; a count of documents returned is not a check.",
   "kind": "measured",
   "found_by": "A permissive scout 'found' seven documents per task by pulling in off-period material, and the strict scout passed 0/10. Of 244 parsed packs, 12 were relevant and 0 valid. The raw pool for every later unit had 0 valid rows. The task type passed only after the source packs were rebuilt first.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1825Z_BLOCKED_dbq_source_pack_repair_list.md",
     "lines": "61",
     "quote": "The old failure mode was treating \"7 returned docs\" as enough; it is not enough."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T0913Z_BLOCKED_dbq_doclock_scout.md",
     "lines": "45",
     "quote": "The earlier permissive scout showed chunk fallback could produce 7 documents, but inspection exposed false positives: Wealth of Nations, Social Contract, Benjamin Franklin, Walden, Federalist Papers, Uncle Tom's Cabin, Up From Slavery, and similar post-1607 material were being selected for Unit-1 DBQ."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T2000Z_DELIVERED_objective_completion_audit.md",
     "lines": "30",
     "quote": "Unit-1 DBQ passed only after source-pack and topic repair. Extending DBQ blindly to Units 2-9 would repeat the same source-integrity failure."
    }
   ],
   "against": "Passing the strict structural gate did not establish provenance: \"It does not independently fetch every URL or certify that normalized excerpts are acceptable for training.\" (~/Documents/aptraining/den-of-ideation/to_main/2026-05-23T1831Z_DEN_REQUEST_validate_unit1_dbq_source_packs_v1.md, line 52).",
   "adds_to_existing": [
    58,
    63,
    64
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Test a strict source checker on known-good material before trusting its rejections; date checks rejected famous in-period documents, and the gaps were then filled with normalized excerpts and summaries.",
   "kind": "open question",
   "found_by": "Raw-pool scans flagged well-known documents from inside the requested period as out of period: a founding document as later 'drift', a 1947 address as 'pre-period contamination'. Every raw row failed, and the repaired packs that replaced them used normalized excerpts and source summaries. The reports do not say whether the flags came from later text inside those documents.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit3_dbq_source_pack_gate_20260524T001732Z.md",
     "lines": "52",
     "quote": "doc 3: Constitution of the United States — doc_3_post_unit3_drift"
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit8_dbq_source_pack_gate_20260523T200616Z.md",
     "lines": "52",
     "quote": "doc 2: Truman Doctrine — doc_2_pre_unit8_contamination"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T2009Z_DELIVERED_unit8_dbq_source_pack_gate.md",
     "lines": "36",
     "quote": "The repaired packs use normalized excerpts/source summaries."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Test keyword and name-matching checks on near-miss cases; a guard for one name fired on a longer name containing it, and similar names pulled the wrong source.",
   "kind": "measured",
   "found_by": "A scope guard for one name fired on a longer name that contains it and failed three valid items (first run 7/10). The same substring overlap routed items to the wrong template, and source keys collided between similarly named documents.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1721Z_DELIVERED_unit8_mcq_solver_v1_candidate.md",
     "lines": "53",
     "quote": "Misses: three local scope-guard failures because `World War II` triggered a bad `world war i` substring guard"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1648Z_DELIVERED_unit7_mcq_solver_v1_candidate.md",
     "lines": "54",
     "quote": "Miss 1: `World War II: Military` routed to WWI because `world war i` matched `world war ii`"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0015Z_DELIVERED_unit5_dbq_solver_v1_candidate.md",
     "lines": "29",
     "quote": "Frederick Douglass / Emancipation slug collision"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before blaming content, run a known-good control through the same grading path; if the control fails too, the grading path is the problem.",
   "kind": "measured",
   "found_by": "Locally valid new question sets kept timing out. A probe with a known-good earlier set as control also timed out (35.024 s, then 90.020 s at a longer cap), while single questions and short answers scored 1.0 in 18-25 s. That placed the block in the grader's set route, not in the content.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1408Z_BLOCKED_mcqset_eval_timeout_probe.md",
     "lines": "35",
     "quote": "| `u1_mcq_set_control` | `mcq_set` | 35.024s | `ReadTimeout: timed out` |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1408Z_BLOCKED_mcqset_eval_timeout_probe.md",
     "lines": "33",
     "quote": "| `u2_mcq_minimal` | `mcq` | 24.385s | `1.0 SUPERIOR` |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1408Z_BLOCKED_mcqset_eval_timeout_probe.md",
     "lines": "39",
     "quote": "The current block is MCQ_SET evaluator-path timeout, not Unit-2 content alone."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    36,
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep plumbing failures out of the quality count in both directions; timeouts, cold starts, empty fields and time caps shorter than grading are neither passes nor misses.",
   "kind": "measured",
   "found_by": "A 32/50 hidden run failed mostly on double read timeouts, with no content returned. A first solver went 0/10 because grading took 80-230 s against a 60 s cap, and a rerun went 0/50 on a cold deployment; in a sibling lab, 216 failures came from a null field. In the other direction, one version returned a template after timeouts and counted it as a pass (4 rows of a 'validated' 50/50), and one tally booked a row with no rating as a grader rejection.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T2056Z_DELIVERED_pipeline_solver_v8_timeout_fallback.md",
     "lines": "38",
     "quote": "15+ failures were two consecutive `ReadTimeout: The read operation timed out`"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md",
     "lines": "60",
     "quote": "Maintain strict official schema normalization before any quality claim. Schema failures must not be counted as model failures or successes."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit1_mcq_solver_v2_validated_addendum_20260524T085013Z.md",
     "lines": "47",
     "quote": "Main-a's first v2 retry attempt failed `0/50` due to `DEPLOYMENT_SCALING_UP` while `v80bchain` was cold."
    }
   ],
   "against": "Practice drifted from this: \"6 fails (5 INFERIOR + 1 None) are real IB rejections.\" (~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T071351Z_2026-05-24T0713Z_UNIT1_DBQ_SOLVER_VALIDATED.md.md, line 113).",
   "adds_to_existing": [
    9,
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make every wrong option a plausible member of the same set as the answer, in the same scope and of the same kind, never filler or something from outside the scope asked about.",
   "kind": "measured",
   "found_by": "A local 50-item run scored 48/50, and both misses were otherwise usable items whose wrong option came from outside the requested period. An older fallback produced generic option wording plus drift into another period. The grader's consistent critique of failing sets included weak distractors.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T2050Z_DELIVERED_pipeline_solver_v7_supersedes_v6.md",
     "lines": "51",
     "quote": "The two n=50 failures were both perspectives/cultural-interaction prompts that generated otherwise usable fresh content but included `Pueblo Revolt of 1680` as a distractor, causing local rejection and then live IB timeout."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1357Z_BLOCKED_unit2_mcqset_parent_archetype.md",
     "lines": "54",
     "quote": "reject generic option templates such as `belongs to the wider era`"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md",
     "lines": "34",
     "quote": "MCQ_SET quality rules became concrete rather than broad-prompted: compact output, APUSH-context child questions, no stimulus phrase matching, no copied answer terms, answer-key balancing, and same-period distractors."
    }
   ],
   "against": "The two misses were stopped by the solver's own scope check, not by a grader verdict: \"causing local rejection and then live IB timeout\" (same file, line 51).",
   "adds_to_existing": [
    58,
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check question design separately from facts; factually sound question sets still failed on leaks, weak options, coverage and balance.",
   "kind": "measured",
   "found_by": "The grader's critique of hidden failures was 'factually sound', failing instead on leaks, distractors and cognitive demand. On a scored set most failures were 'semantic/educational'. One set type scored 0/20 on test preparedness, concept coverage, answer balance and stimulus quality, 'NOT factual'. In a raw model, 72-94% of failures had educational_accuracy=0.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1905Z_hidden_acceptance_repair_status.md",
     "lines": "75",
     "quote": "The IB critique is consistent: factually sound, but too many question-level failures due answer leaks, weak distractors, or insufficient AP-level cognitive demand."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md",
     "lines": "55",
     "quote": "Most MCQ_SET failures are semantic/educational rather than simple schema/leak failures."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T132917Z_2026-05-27T1330Z_bm0zjn5z_n100_unit1_RAW_PROBE_REPORT.md.md",
     "lines": "128",
     "quote": "`educational_accuracy=0` high across cells (72-94% of fails) — grade-level + cognitive-demand mismatch"
    }
   ],
   "against": "For a small model that lacked the facts, facts dominated: \"Factual accuracy is the dominant kill — fresh-base 8B doesn't have Unit-1 facts.\" (~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T132917Z_2026-05-27T1330Z_bm0zjn5z_n100_unit1_RAW_PROBE_REPORT.md.md, line 115).",
   "adds_to_existing": [
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check that the right option does not echo distinctive words from the stem or source that the wrong options lack, since that echo hands over the answer.",
   "kind": "adopted rule",
   "found_by": "Answer leakage was a named failure in the grader's critique, a hard gate in the validator (correct option copying a stimulus phrase) and an overlap penalty in the solver.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/cell_family_archetype_scout_20260523.md",
     "lines": "84",
     "quote": "Answer leakage: direct MCQ can become trivial when the stem copies the correct option's nouns."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md",
     "lines": "19",
     "quote": "answer phrase leakage from stimulus to correct option;"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "227",
     "quote": "no copied answer phrase"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    3,
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Ask for explanation or a specific cause-and-effect link at the depth the standard asks for, not recall or a broad summary.",
   "kind": "measured",
   "found_by": "62% of a raw model's single-question failures scored zero on mastery alignment as 'pure recall'. Broad summary templates scored 6/10, then 7/10, then 10/10 once rewritten as sharper cause-and-effect items, tuned on the same ten items.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T132917Z_2026-05-27T1330Z_bm0zjn5z_n100_unit1_RAW_PROBE_REPORT.md.md",
     "lines": "130",
     "quote": "`mastery_learning_alignment=0` on 62% of MCQ fails — pure recall, not the \"explain how\" depth that AP standards demand"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1808Z_DELIVERED_unit9_mcq_solver_v1_candidate.md",
     "lines": "54",
     "quote": "Fix: rewrote those broad summary templates into sharper cause/effect items"
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/to_main/2026-05-23T1808Z_DEN_REQUEST_validate_unit9_mcq_solver_v1.md",
     "lines": "24",
     "quote": "first public n=10 was `6/10`"
    }
   ],
   "against": "The gain was measured on the ten public items being patched, and a different sample then failed: \"third public n=10 was `10/10`, but runner sanity failed `1/2`\" (same request file, line 26).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Expect a writer model to copy the examples it is shown; example items in a prompt leaked their specific content and shape into new items, so constrain with rules and verified facts instead.",
   "kind": "measured",
   "found_by": "Few-shot single-question examples made performance worse by contaminating new items with the examples' specific content, and illustrative prompt-kit examples leaked into output shape.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
     "lines": "100",
     "quote": "Few-shot MCQ examples worsened performance by contaminating generations with example-specific historical content."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "285",
     "quote": "Few-shots help only when they do not contaminate the historical content."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md",
     "lines": "76",
     "quote": "Keep prompt-kit field names subordinate to original IB schema authority to avoid illustrative examples leaking into output shape."
    }
   ],
   "against": "The best fresh pipeline still used curated examples: \"-> apply satisfaction kit + curated few-shots\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md, line 20).",
   "adds_to_existing": [
    57,
    62
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Label every reported number with what produced it, namely grader and version, attempts and who picked, any bank or fallback, sample size and evidence class; mixed evidence classes produced false confidence.",
   "kind": "adopted rule",
   "found_by": "The project held schema-only, spread-sample, targeted-repair, archived, self-evaluated, older-grader and partial live evidence side by side, and mixing them 'caused false confidence'. A 138/150 retrospective replay was later contradicted by 126/150 on fresh grading, and a predicted-pass run was promoted as graded.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/MAIN_AGENT_ACTION_PACKET.md",
     "lines": "201",
     "quote": "Mixing those proof classes caused false confidence in earlier work."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/MAIN_AGENT_ACTION_PACKET.md",
     "lines": "210",
     "quote": "New `summary.json` files can be read without context and answer: \"what exactly was measured?\""
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "282",
     "quote": "Best evidence always says which evaluator version, endpoint mode, and fallback mode were active."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Certify only with the reference grader the work will be judged by, in its current version; diagnostic graders, older versions and self-evaluation are design evidence.",
   "kind": "adopted rule",
   "found_by": "A 97% result on an older grader version was treated as design evidence only. The evaluation method warned against mixing a diagnostic evaluator with the official one, and the policy on image documents proved sensitive to grader version.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
     "lines": "110",
     "quote": "Use official/current IB only for certification. Diagnostic evaluator and older versions are not interchangeable."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md",
     "lines": "58",
     "quote": "Keep IB v2.5.7 as the certification target. Older grader wins are design evidence only."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/MAIN_AGENT_ACTION_PACKET.md",
     "lines": "216",
     "quote": "Do not use self-eval as certification."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    43,
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "An acceptance check must be independent of the maker; re-running the maker's own validator only shows the validator agrees with itself, and the source review that was asked for never happened.",
   "kind": "measured",
   "found_by": "A provenance and source-quality review was requested because the maker's validator checked structure only. The acceptance re-ran that same validator, reported an exact match (10/10) and accepted, and the packs went on to back a 'validated' 49/50 lane.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/to_main/2026-05-23T1831Z_DEN_REQUEST_validate_unit1_dbq_source_packs_v1.md",
     "lines": "52",
     "quote": "Please perform provenance/source-quality validation. Den's validator checks structure, Unit-1 contamination, text-bearing docs, topic coverage, primary-like count, and visual-risk filters. It does not independently fetch every URL or certify that normalized excerpts are acceptable for training."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T063156Z_2026-05-24T0630Z_UNIT1_DBQ_SOURCE_PACK_ACCEPT.md.md",
     "lines": "88",
     "quote": "main-a re-ran Den's gate independently:"
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T063156Z_2026-05-24T0630Z_UNIT1_DBQ_SOURCE_PACK_ACCEPT.md.md",
     "lines": "99",
     "quote": "Matches Den's claim exactly (10/10 rows valid, no missing topic targets)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    43,
    44,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count distinct sources when a rule asks for coverage; paired packs that list the same documents meet a two-per-topic count without adding range.",
   "kind": "open question",
   "found_by": "The source gates required two valid packs per topic. In the repaired files, both packs for a topic list the same first three documents (rows 3 and 4, rows 7 and 8, rows 1 and 2), so ten 'valid' packs may cover about five distinct sets.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit5_dbq_source_pack_gate_20260523T230245Z.md",
     "lines": "32, 36",
     "quote": "doc 1: Compromise of 1850 fugitive slave provision — no doc-level error"
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit2_dbq_source_pack_gate_20260524T025941Z.md",
     "lines": "31, 35",
     "quote": "doc 1: First Virginia Charter - no doc-level error"
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit8_dbq_source_pack_gate_20260523T200817Z.md",
     "lines": "51, 55",
     "quote": "doc 1: Truman Doctrine address to Congress — no doc-level error"
    }
   ],
   "against": "none found in the sources; the gate reports list only documents 1-3 of each pack, so paired packs may still differ in documents 4-7.",
   "adds_to_existing": [
    41,
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Prove each new scope on its own; a generator tuned for one scope forced that scope's limits onto others, and loosening its prompt is not evidence that it transfers.",
   "kind": "adopted rule",
   "found_by": "The validated solvers hard-coded one period and its banned terms, so running them on other periods would be 'actively wrong'. Wrapping a generic all-scope fallback scored 0/3, with drift back into the first period and generic options.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit2_9_coverage_scout_20260523.md",
     "lines": "125",
     "quote": "Do not claim Unit 2-9 coverage from prompt generalization alone."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/unit2_9_coverage_scout_20260523.md",
     "lines": "69",
     "quote": "Conclusion: running these solvers on Unit 2-9 would be actively wrong. They would force Unit-1 constraints onto later-period requests."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1357Z_BLOCKED_unit2_mcqset_parent_archetype.md",
     "lines": "49",
     "quote": "Unit-2 MCQ_SET expansion should not be delivered from parent fallback alone."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48,
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Take verdicts and counts from the structured result, never from summary prose; keyword triage flipped a repair verdict to green and a validated one to repair, and one tally was estimated from a log sample.",
   "kind": "measured",
   "found_by": "Automated triage of result notes read headline pass-count wording as green on a 'SECOND_TIER -> REPAIR' verdict. It then read a 'REPAIR pending' table row about another lane as a repair verdict on a validated lane. A validation note gave its rating breakdown as an estimate from a log sample.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0600Z_DELIVERED_repair_result_triage_classifier_fix.md",
     "lines": "12",
     "quote": "The packet is explicitly `SECOND_TIER -> REPAIR`, but the first auto-triage run classified it as `validated_or_green_candidate` because headline pass-count language outranked repair/fail language."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0633Z_REPORT_unit1_validation_results_addendum.md",
     "lines": "50",
     "quote": "`scripts/triage_validation_result.sh` was patched because the first SAQ auto-triage saw the phrase `REPAIR pending` in a context table about MCQ and misclassified the SAQ VALIDATED packet as repair."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T084525Z_2026-05-24T0844Z_UNIT1_MCQ_SOLVER_VALIDATED.md.md",
     "lines": "153",
     "quote": "37+ SUPERIOR (estimating from log sample)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    39,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a check rejects a draft, regenerate only the stage that failed and pass the specific reason, not a generic 'try again'.",
   "kind": "adopted rule",
   "found_by": "The staged designs put a deterministic check between stages and re-asked only the failing stage. The production recommendation was to regenerate with concrete rejection reasons. Neither variant was measured.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/MAIN_AGENT_ACTION_PACKET.md",
     "lines": "75",
     "quote": "Regenerate with concrete rejection reasons between stages, not a broad \"try again\"."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "233",
     "quote": "-> repair or regenerate with specific reason"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-19T1541Z_gate0_prototype_in_lab.md",
     "lines": "39",
     "quote": "Between stages, the validator rejects + re-asks ONLY the failing stage (not full restart)."
    }
   ],
   "against": "The same directive took the opposite line on reasons: \"the question-generator doesn't see the validator's reasoning, only the reject signal.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-19T1541Z_gate0_prototype_in_lab.md, line 39).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Size the test to the claim; with 50 items one item moves the rate by 2 points, so a 98.8% against 99% claim cannot be settled.",
   "kind": "open question",
   "found_by": "Pass rates per item type on 50-item sets were averaged into 98.8%, 99.2% and 99.6% projections and compared with a 99% target. The record itself called 98.8% 'within the noise band', and the smallest honest validation gate was left open.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T175907Z_2026-05-24T1759Z_UNIT1_DBQ_SOLVER_v3_VALIDATED_TARGET_REACHED.md.md",
     "lines": "137",
     "quote": "Statistical resolution at n=50 per cell is ±2pp; 98.8% sits within the noise band of 99%."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md",
     "lines": "85",
     "quote": "What is the smallest statistically honest validation gate that predicts full 26,355-row quality without a multi-day scorer run?"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Fit a document set to its question: cover the whole span asked about, include more than one perspective including dissent, and drop documents that do not bear on it.",
   "kind": "measured",
   "found_by": "Public-run failures of document-based tasks were repaired by adding missing decades and dissenting documents, swapping documents about the wrong aspect of the question, and removing an irrelevant document. One row rose from 0.55 to 0.70 to 1.0 after, among other changes, documents from an under-represented perspective were added.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0208Z_DELIVERED_unit4_dbq_solver_v1_candidate.md",
     "lines": "30",
     "quote": "foreign-policy rows lacked 1830s/1840s coverage and dissenting documents"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0102Z_DELIVERED_unit3_dbq_solver_v1_candidate.md",
     "lines": "29",
     "quote": "American-victory hard route used social/global legacy docs"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T2258Z_DELIVERED_unit6_dbq_solver_v1_candidate.md",
     "lines": "47",
     "quote": "Fixed Period 6 rubric metadata, irrelevant Plessy document in immigration route, and accidental Homestead Act / Homestead Strike slug collision."
    }
   ],
   "against": "The repairs were checked on the same public items they were made against: \"Public failures were repaired before delivery, including Second Great Awakening causation routing, foreign-policy coverage/dissent, and the invalid Hammond date.\" (~/Documents/aptraining/den-of-ideation/to_main/2026-05-24T0208Z_DEN_REQUEST_validate_unit4_dbq_solver_v1.md, line 30).",
   "adds_to_existing": [
    58,
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Re-check content after any automatic cleanup; phrase substitution left awkward artifacts and stripping left documents too thin to pass.",
   "kind": "measured",
   "found_by": "A post-generation scope sanitizer needed extra repairs for its own awkward replacement text. One document set failed the length check after the sanitizer stripped leaked sentences, and had to be repaired again.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T2050Z_DELIVERED_pipeline_solver_v7_supersedes_v6.md",
     "lines": "27",
     "quote": "Added specific repairs for `Pueblo Revolt of 1680`, `Virginia Company`, `Jamestown`, `Powhatan`, English-colony phrases, Chesapeake/New England, Pilgrim/Puritan phrases, and awkward replacement artifacts."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0339Z_DELIVERED_unit2_dbq_solver_v1_candidate.md",
     "lines": "30",
     "quote": "Colonial Society/Culture docs initially failed local doc-lock after sanitizer stripping; targeted repair probe passed at `1.0 SUPERIOR`."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Source texts that students analyse must be real documents supplied from outside the writer model, which only frames the task around them.",
   "kind": "measured",
   "found_by": "A generator that wrote its own 'documents' described maps, charts and photographs that did not exist, and the grader zeroed them. Locking in seven retrieved text documents took that item type from 0% to 29/30. In a raw model, synthetic primary sources scored stimulus_quality=0 on 75% of its document-question failures.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "56",
     "quote": "The generator emitted fake maps, charts, photographs, and cartoon descriptions as if they were documents."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
     "lines": "72",
     "quote": "DBQ needs source ownership outside the model. The model can frame prompt/rubric, but source documents must come from retrieval or locked artifacts."
    },
    {
     "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260527T132917Z_2026-05-27T1330Z_bm0zjn5z_n100_unit1_RAW_PROBE_REPORT.md.md",
     "lines": "129",
     "quote": "`stimulus_quality=0` on 75% of DBQ fails — primary-source documents are synthetic"
    }
   ],
   "against": "This lineage's own 'validated' document lane served script-built normalized excerpts, and the grader passed them: \"Source packs use normalized excerpts and should receive provenance spot-check before promotion.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T2115Z_DELIVERED_unit8_dbq_solver_v1_candidate.md, line 55).",
   "adds_to_existing": [
    29,
    57,
    64
   ],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0615Z_REPORT_unit1_mcq_solver_v2_repair_delivery.md",
   "lines": "34",
   "quote": "No candidate is counted as a pass unless live IB returns a passing score."
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1509Z_DELIVERED_unit4_mcq_solver_v1_candidate.md",
   "lines": "17",
   "quote": "No timeout fallback is accepted as pass."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260528T030737Z_2026-05-28T0312Z_ESCALATE_F14_blocking_track_B_v2_grading.md.md",
   "lines": "105",
   "quote": "NOT firing IB grading on the 79 partial rows (would mis-represent the corpus)"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "104",
   "quote": "Best-of-N was implemented once but not actually active."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-25T0615Z_TASK_concrete_deployable_workflow.md",
   "lines": "94",
   "quote": "main-a runs n=50 hidden hold-out K=1 single-shot on the WORKFLOW (not your dev scripts) — confirms numbers reproduce"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/reports/v10_validated_artifact_integrity_20260524T0421Z.md",
   "lines": "7",
   "quote": "The current production solver in Den is byte-identical to the main-a promoted v10 artifact."
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md",
   "lines": "24",
   "quote": "Hard gates are deliberately narrow. The first version over-blocked known passing rows because InceptBench tolerates some source-referential wording."
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/MAIN_AGENT_ACTION_PACKET.md",
   "lines": "218",
   "quote": "Do not add visual DBQ documents unless the evaluator receives real visual/OCR payloads."
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1958Z_DELIVERED_unit1_dbq_solver_v1_candidate.md",
   "lines": "72",
   "quote": "Adding canonical `rubric_notes` and matching known DBQ schema made IB return scores."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
   "lines": "19",
   "quote": "the probe flips on *borderline* items"
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/to_main/2026-05-24T1113Z_DEN_NOTICE_mcqset_route_inspection_no_safe_unblock.md",
   "lines": "15",
   "quote": "per-child MCQ fallback is unreliable: children 1 and 2 timed out at 60s; child 3 scored `1.0 SUPERIOR`"
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "125",
   "quote": "Keep generation/evaluation artifacts with prompt messages; DPO and debugging require full conversation context, not only output JSON."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T2056Z_DELIVERED_pipeline_solver_v8_timeout_fallback.md",
   "lines": "51",
   "quote": "original v80bchain timeout attempt is preserved in `audit_trail`"
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T2107Z_ACCEPTANCE_GREEN_v9_hidden50.md",
   "lines": "32",
   "quote": "IB: cache/live paths are labeled for IB v2.5.11; hidden runner judged returned score/status through `prototypes/run_den_solver_on_jsonl.py`"
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md",
   "lines": "54",
   "quote": "The deterministic hard gates are good as a safety layer, not a complete quality judge."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-22T1845Z_ULTIMATE_DELIVERY_CHALLENGE.md",
   "lines": "42",
   "quote": "Acceptance criteria (binary, no negotiation)"
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-25T0615Z_TASK_concrete_deployable_workflow.md",
   "lines": "88",
   "quote": "No more \"99.6% goal complete\" framing in production-facing docs. Use the K=1 numbers as headlines."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1807Z_DELIVERED_pipeline_solver.md",
   "lines": "99",
   "quote": "This is still not a final acceptance claim: main-a's 50 fresh prompts are the actual binary gate."
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "111",
   "quote": "Diagnose by failed dimension, not by aggregate score. DBQ 0%, MCQ_SET 25%, and SAQ 0% have different mechanisms."
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "122",
   "quote": "For SAQ/LEQ/DBQ, replace hallucination-prone evidence lists with verified-facts-only or analytical-category scoring notes."
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/HANDOVER.md",
   "lines": "123",
   "quote": "SAQ scoring notes should avoid hallucination-prone evidence lists"
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "88",
   "quote": "Facts work better as constraints than as inspiration."
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1538Z_DELIVERED_unit5_mcq_solver_v1_candidate.md",
   "lines": "29",
   "quote": "the miss was `Sectional Conflict: Regional Differences` routed to a generic Compromise item and scored `0.8 INFERIOR`."
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "46",
   "quote": "InceptBench pass is not just `overall_score >= 0.85`; hard-fail dimensions must also be perfect."
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260524T115335Z_2026-05-24T1153Z_UNIT1_DBQ_SOLVER_v2_VALIDATED.md.md",
   "lines": "127",
   "quote": "5 of v1's 6 failures repaired; 1 (row 39) still fails; 1 new fail (row 29) introduced — net +4 passes."
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "131",
   "quote": "Human/agent external review helps when hypotheses are stuck, but the review must be grounded in actual failing artifacts."
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "101",
   "quote": "“Be careful” factuality warnings hurt; caution text without hard constraints creates hedging, not accuracy."
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "91",
   "quote": "For SAQ/LEQ/DBQ scoring notes, “don’t list specific facts” failed. Verified-facts-only constraints are stronger."
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "114",
   "quote": "Treat metadata correctness as a hard gate: course, unit, period, standard, and type must propagate authoritatively through every generator path."
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/HANDOVER.md",
   "lines": "122",
   "quote": "Period metadata bugs can dominate failure rate"
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
   "lines": "57",
   "quote": "InceptBench hard-zeroed those because the stimulus was not real analyzable source material."
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "120",
   "quote": "Best-of-N is a multiplier, not a miracle. It works once base per-type pass rate is competent; it does not fix systematic failures."
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/reports/validation_triage/20260529T085132Z_2026-05-29T0850Z_v86_VERDICT_57pct_aggregate_DBQ_MCQ_SET_catastrophic_99stack_rescue.md.md",
   "lines": "114",
   "quote": "Catastrophic cells are CONSISTENTLY catastrophic across seeds (not flaky); strong cells are CONSISTENTLY strong."
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Documents/aptraining/den-of-ideation/reports/cell_family_archetype_scout_20260523.md",
   "lines": "134",
   "quote": "Do not run DBQ as a generic \"best of K\" prompt; DBQ failure mode is source integrity, not merely weak prose."
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md",
   "lines": "40",
   "quote": "Naive best-of-scored-candidates banking overfit: predicted 138/150, but fresh IB scored 126/150."
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_den/2026-05-22T1845Z_ULTIMATE_DELIVERY_CHALLENGE.md",
   "lines": "14",
   "quote": "It is curation after the fact. It does not generalize to fresh prompts."
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md",
   "lines": "13",
   "quote": "Anti-leak scaffold built by rule, not the model."
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "121",
   "quote": "For MCQ_SET, add explicit coverage fields to the plan step, such as entities/nations/themes to cover, then bind child questions to that plan."
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md",
   "lines": "44",
   "quote": "The rule is aggregate -> dimension -> item -> hypothesis -> distinguish -> confirm -> fix."
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-22T1840Z_DELIVERED_pipeline_solver.md",
   "lines": "59",
   "quote": "targeted Native-environment easy repair retained after live IB improved that row from 0.80 to 1.00;"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md",
   "lines": "75",
   "quote": "Record answer-key distribution for MCQ_SET and repair when balance caps otherwise-good sets."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md",
   "lines": "230",
   "quote": "all child questions depend on stimulus"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-23T1831Z_DELIVERED_unit1_dbq_source_packs_v1_full_gate_green.md",
   "lines": "69",
   "quote": "decide whether normalized excerpts are acceptable or whether exact quoted excerpts are required"
  }
 ]
}
```
