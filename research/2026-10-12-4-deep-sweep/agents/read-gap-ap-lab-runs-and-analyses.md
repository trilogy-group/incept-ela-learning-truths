# read:gap:ap-lab-runs-and-analyses

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "ap-lab-runs-and-analyses",
 "coverage": {
  "read": [
   "~/Documents/aptraining/analyzer/STATUS.md",
   "~/Documents/aptraining/analyzer/reports/ (production_surface_40d.md, run_324d5e51_what_is_really_going_on.md, run_f54d5849_what_is_going_wrong.md)",
   "~/Documents/aptraining/analyzer/.lanes/teaching-benchmark/ (LAUNCH.md, STRATEGY_REPORT.md, TASK.md)",
   "~/Documents/aptraining/analyzer/.agent/MEMORY.md and BRIEFING.md",
   "~/Documents/aptraining/conscience/audit_log/ (all 6 .md)",
   "~/Documents/aptraining/conscience/.agent/MEMORY.md and BRIEFING.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_analyzer/ (2), to_analyzer/ (11), from_conscience/ (8 incl. STATUS.md), to_conscience/ (14)",
   "~/Documents/aptraining/.agent/reports/e2e_v97_live_20260607T100840Z.md",
   "~/.openclaw/workspace-incept/STRATEGY_REPORT.md, memory/2026-05-21.md, memory/ap-benchmark-context.md",
   "~/Documents/aptraining/parallel-ideas-lab/reports/: all 13 per_unit_bench_*.md (incl. rescore and corrected), synapse_checkin_2026_05_27_pipeline_quality_paradox.md, runs_to_commits_40d.md, prepause_decision_log_20260525T082954Z.md, ultimate_v80chain_pipeline_20260525T0945Z.md, unit1_workflow_v2_branch_result_20260525T093757Z.md, handover_observations_training_questions_2026_05_27.md; grep-skimmed LLM_FINAL_ROUTE_STATUS_20260522T185623Z.md, mixmatch_pipeline_insights_20260525.md, deep_repo_extraction_20260525.md, 24H_CARETAKER_STATE_20260521.md; first 60 lines of branch_agent_directive_20260525T082954Z.md",
   "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/ (all 15 .md) and handovers/20260526T064354Z_TYPED_DUCK_COMBO_HANDOVER.md",
   "~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md (all 974 lines; the only .md there)",
   "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md; reports: run_324d5e51_failure_modes.md (head), run_324d5e51_success_patterns.md (full), live_update_decision for 324d5e51, f54d5849, 75cc4abf_failed, ecf7d5c6_failed, 5eb118bd; section headers of 3 failure_modes files; narrative compared across 5 success_patterns files",
   "Snapshot parallel-ideas-lab: WINS_20260514.md, HANDOVER_PARALLEL_IDEAS.md, PIPELINE_WRAPPER_ACTION_PLAN.md, MAIN_AGENT_ACTION_PACKET.md",
   "Snapshot reports: A0F_COMPLETED_RUN_READINESS_20260520.md, B0045_STAGED_MCQSET_INTERIM_20260519.md, K_sweep_99pct_20260519T180652Z.md, OPENAPI_CONFORMANCE_20260520.md, a0f_failure_map_20260519.md (first 150 lines), a0f_validator_probe_20260519.md, pipeline_status_2026-05-18.md, run_73348c1a_orchestrator_contract.md, pil_monitor/ (README, latest, IB_99_SELF_REVIEW_LOOP, 7 inbox messages, 3 snapshots diffed)",
   "Snapshot handoff_from_calibration/*.md (7: two deploy packets, STATUS_UPDATE, XDRAW_MEASUREMENT, CONTRACT, README, INDEX)",
   "Snapshot experiments: all 6 RESULTS.md, goal_runs/RUNNING_SUMMARY.md, failed_export_replay/RUNNING_SUMMARY.md (full), production_all_units/RUNNING_SUMMARY.md (lesson-bearing sections), UNIT1_TO_ALL_UNITS_TRANSFER_PLAN.md, UNIT1_SHOWCASE_CHOICES_20260519.md, official_exports/all_official_generation_audit.md, official_exports/local_eval/local_eval_report.md, 3 SELECTOR_CALIBRATION.md, compatibility_audit.md, all 48 prompt_perfection/runs/*/analysis*.md (pass lines for all, full text for 11)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/request_trace/ (all 4)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/README.md and runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md, system_prompt_mcq_set.md, system_prompt_saq.md, system_prompt_leq.md"
  ],
  "skipped": [
   "parallel-ideas-lab/reports/calibration_handoff_monitor/, the regression_*.md files and the local handoff_from_calibration/ (excluded by the task)",
   "Remaining ~40 variant-calibration-lab run_*_failure_modes.md / run_*_success_patterns.md bodies: machine-generated per-row tables under one fixed title and narrative; one read in full, others checked by headers and narrative comparison",
   "13 zero-byte run_*_ placeholders dated 21 May in variant-calibration-lab/reports, and the zero-byte WINS/HANDOVER/PIPELINE/MAIN_AGENT/README copies in ~/Documents (snapshot copies read instead)",
   "production_all_units/RUNNING_SUMMARY.md per-unit slice logs (about lines 110-228, 470-695, 760-1000, 1032-1820): headers only, because of size (111 KB)",
   "a0f_failure_map_20260519.md beyond line 150 (per-row tables)",
   "All .json/.jsonl artifacts (K_sweep json, typed duck libraries, manifests, score files): data dumps",
   "reports/mcqset_winner_mining_20260521.md (58 KB, dated 21 May, outside the after-21-May window)",
   "Snapshot reports/live_preflight/: contains no .md files",
   "~/.openclaw/workspace-incept/memory/archive/ (excluded); the secrets script path named in memory/2026-05-21.md was not opened",
   "Other .agent files (AGENT, IDENTITY, NORTH_STAR, SOUL) in analyzer/ and conscience/: not in scope"
  ],
  "notes": "Read-only throughout: nothing written, no mgr registration (the task forbids writes). Every cited path starts with the account home directory, which carries the owner's account name; I treated that prefix as not name-bearing and set name_bearing_source false, since no file or folder name below it names a person; quotes naming people were avoided (historical figures appear only as item content). All quotes were checked by exact string match against the files. Caveats: many results are small-n (3-25 items per type) and single-seed, and the sources themselves call several of them directional; rules taken from the rubric-derived writer prompts are marked adopted rules, with the caveat that switching that kit on lowered the pass rate (79.7% vs 85.7%); the variant-calibration-lab pattern reports reuse one title and narrative for every run, so only their tables describe the run they're filed under; the coverage-vs-capacity test was requested repeatedly in to_analyzer but no verdict file exists in from_analyzer."
 },
 "candidates": [
  {
   "statement": "A failure to deliver or to grade an item is not a quality verdict: count it on its own and keep it out of the pass rate's denominator.",
   "kind": "measured",
   "found_by": "Run headlines of 14.6% and 0% were mostly gateway errors, unattempted requests or a broken judge lookup; on the 225 items the judge actually scored the pass rate was 70.2%, and one commit scored 0.0% and 84.3% 26 minutes apart.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/analyzer/reports/run_324d5e51_what_is_really_going_on.md",
     "lines": "4",
     "quote": "**TL;DR:** The headline 14.6 % \"pass rate\" is **meaningless**. The actual model is performing at **70.2 %** on the items that survived two stacked infrastructure failures."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/run_73348c1a_orchestrator_contract.md",
     "lines": "98",
     "quote": "- Schema failures must be counted separately and excluded from quality pass-rate denominators."
    },
    {
     "path": "~/Documents/aptraining/analyzer/reports/production_surface_40d.md",
     "lines": "21",
     "quote": "- **Proof it's not code/model:** the same commit (`bb577e2`) produced a 0.0% run and an 84.3% run **26 minutes apart**."
    }
   ],
   "against": "The lab sometimes counted the other way (\"- MCQ_SET still needs at least `+10` counting score errors as failures.\", ~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md line 874); leaving failures out is only safe if the completion rate is reported beside the pass rate (\"Report four metrics separately:\", run_73348c1a_orchestrator_contract.md line 139).",
   "adds_to_existing": [
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When every item gets the same score (all zeros or one floor value), check the measuring before the content: a misread field, a wrong input shape or a failed lookup.",
   "kind": "measured",
   "found_by": "A per-unit report showed 0.0% for every unit until the scorer was fixed to read the field the judge actually returns (unit 1 then read 60.0%); a 30-item test returned 0.55 for all 30 because the judge was given material in a shape it doesn't grade; a live summary read a verdict field that didn't exist.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/per_unit_bench_corrected_20260527T1009Z.md",
     "lines": "6",
     "quote": "Fix: score now read from ev['overall']['score'] (was ev['score']=None)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_conscience/2026-05-28T0030Z_proactive_log_self_catch_research_first.md",
     "lines": "11",
     "quote": "**Within ~6 minutes**, I recognized this signature as wrong-schema-not-content-fail (the 0.55 floor + 0/30 = grader rejecting \"not a DBQ\" not grading badness of source)."
    },
    {
     "path": "~/Documents/aptraining/.agent/reports/e2e_v97_live_20260607T100840Z.md",
     "lines": "6",
     "quote": "Note: corrected: verdict = overall.score (prior summary read nonexistent overall_pass)."
    }
   ],
   "against": "A uniform zero can also be a real break on the generating side rather than the judge: \"A two-cell code path broke; ~45% aggregate = 3 cells working + 2 cells bugged to zero.\" (~/Documents/aptraining/analyzer/reports/production_surface_40d.md line 24) - still a pipeline fault, not content quality.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Treat a large, sudden score drop as a measurement fault until the judge's inputs and stated reasons have been read; a quiet mismatch in what a label means cut item scores by 10-40 points and looked like a content regression.",
   "kind": "measured",
   "found_by": "A 43-point fall on one item type within 90 minutes traced to a grade field the judge read as a school grade rather than a course unit; the mismatch zeroed accuracy and clarity on correct items in 81 evaluations; earlier a renamed subject had broken the judge's reference lookup.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/analyzer/reports/run_f54d5849_what_is_going_wrong.md",
     "lines": "135",
     "quote": "The MCQ collapse (69 % → 26 %, −43 pp in 90 min) is implausible as a model regression; it is much more likely a **grader-side change to how `grade=\"1\"` is enforced** that fired between the two runs, OR a model output style shift that made the grade-mismatch heuristic trigger more aggressively."
    },
    {
     "path": "~/Documents/aptraining/analyzer/reports/run_f54d5849_what_is_going_wrong.md",
     "lines": "144",
     "quote": "The second one is quieter and therefore more dangerous: it lowers numbers by 10–40 pp on individual items in a way that looks like a model regression."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_analyzer/2026-05-27T1741Z_DIAGNOSIS_data_adequacy_binding_lever.md",
     "lines": "27",
     "quote": "But the **U1 PoC 95% gate is precisely where a silent *partial* curriculum-resolution failure masquerades as factual_accuracy misses** and tanks the gate (or worse, a recovery masks a real miss)."
    }
   ],
   "against": "A detector for this very mismatch had been retired days earlier on a five-item check: \"Confirmed 0/5 random failed-row reasonings cite this.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/handoff_from_calibration/20260520T201911Z_run_0506c1fd_v2_deploy_packet.md line 32).",
   "adds_to_existing": [
    63,
    33
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge a run only once it has finished; an early snapshot can land on a clean window and overstate the pass rate.",
   "kind": "measured",
   "found_by": "A report written from the first 26 minutes of a run gave 48.9% (n=266); the finished run gave 37.0% (n=897) because gateway failures and lower pass rates clustered in later hours; in another run the survivors of a cut-off queue were not a random sample.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/analyzer/reports/run_f54d5849_what_is_going_wrong.md",
     "lines": "13",
     "quote": "**Real pass rate 37.0 % (n = 897, full run).** F1 was a lucky early-window slice; later items pass-rated lower."
    },
    {
     "path": "~/Documents/aptraining/analyzer/reports/run_f54d5849_what_is_going_wrong.md",
     "lines": "61",
     "quote": "A measurement-integrity report got partially fooled by its own measurement window."
    },
    {
     "path": "~/Documents/aptraining/analyzer/reports/run_324d5e51_what_is_really_going_on.md",
     "lines": "54",
     "quote": "The 70.2 % on n=225 is real for *the items that survived*, but the survival itself is not random — it's truncated at the queue's natural drain point."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Don't adopt a change, or a rule for one item type, on a single small run; repeat it on independent draws first, because single-draw winners flipped and small-sample gains halved or vanished.",
   "kind": "measured",
   "found_by": "Per-type gains from one 50-item run proved to be noise on a 90-item multi-seed rerun; the best prompt style for one type changed between a single draw and the three-draw mean; a 3/3 vs 0/3 contrast became 2/3 vs 2/3 on rerun.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md",
     "lines": "75",
     "quote": "- Single-draw conclusions FLIP between draws (e.g., SAQ best-profile changed from `exam_precision` (single-draw) to `tight_alignment` (3-draw mean))."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_analyzer/2026-05-29T0644Z_dream_sequence_sync_06Z.md",
     "lines": "21",
     "quote": "single-seed n=50 Path β ablation showed +10pp lifts (cell-conditional); multi-seed n=90 revealed those were noise."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_4way_verdict_20260526.md",
     "lines": "79",
     "quote": "Per-cell, the 2.5 \"DBQ 3/3 vs 0/3\" was small-N noise — both DBQ cells normalized to 2/3 on 3.5."
    }
   ],
   "against": "The cross-draw packet that enforced this shipped its decisions on two draws, short of the three-draw rule: \"# CROSS-DRAW measurement — Unit 1 n=150 BoN (2 draws)\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/handoff_from_calibration/20260520T234841Z_XDRAW_MEASUREMENT_unit1_n150.md line 1).",
   "adds_to_existing": [
    15,
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Size the sample to the claim: a high pass gate needs enough items per type to tell it from a lower rate, and differences inside the noise floor aren't worth acting on.",
   "kind": "measured",
   "found_by": "Analyses kept asking whether a sample could carry the claim made from it: 45 items per type cannot show 95%, 15-item runs swing by about one item per type, and lifts under one point on 150 items were declared noise.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/analyzer/reports/run_324d5e51_what_is_really_going_on.md",
     "lines": "55",
     "quote": "n=45 per cell is small; 95 % requires <2/45 cell misses, and MCQ_SET alone has 25 misses here."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_14way_verdict_20260526.md",
     "lines": "66",
     "quote": "5. **n=15 noise floor is roughly ±1 row per cell.** Per-cell numbers like \"2/3 vs 0/3\" should be interpreted as directional only."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/handoff_from_calibration/README.md",
     "lines": "67",
     "quote": "- Any packet whose `expected_lift_pp` < 1.0 is below noise floor for n=150 measurements — don't bother."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep an item judged good only after it passes on at least two independent judgings; items banked on one high score failed when re-scored unchanged.",
   "kind": "measured",
   "found_by": "Sets assembled from each item's best past score predicted 138/150 and 145/150 but scored 126/150 and 47/61 when judged afresh, with single items falling from 1.0 to 0.0; requiring repeat passes lifted the fresh trajectory from about 77% to 84.76% and then 85.61%.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md",
     "lines": "320",
     "quote": "- Single-score banking overfits IB noise. Several candidates that previously scored `1.0` failed when rescored unchanged."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md",
     "lines": "578",
     "quote": "- Need a stability gate: a MCQ_SET candidate should pass at least two independent IB scores or pass after serial retry before it is eligible for assembly."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md",
     "lines": "553",
     "quote": "- Prior-score assembly without fresh validation is unreliable. `mixed_step_union_v2` expected `145/150` but fresh-aborted at `47/61`."
    }
   ],
   "against": "An over-strict version removed good items: \"- Clean-pass purity hurt selection. It removed useful candidates with some historical fail evidence but strong fresh behavior.\" (~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md line 767).",
   "adds_to_existing": [
    34,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Picking the best of several drafts helps only where the picker agrees with the final judge; compare its picks with simply taking the first valid draft and drop it if it isn't better.",
   "kind": "measured",
   "found_by": "Choosing among six drafts with a model judge scored 22/25 against 23/25 for a single draft and halved one type's passes; on another set every selection mode, including the model judge, tied simply taking the first valid draft at 13/15.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/BEAD_EVIDENCE_INDEX.md",
     "lines": "57",
     "quote": "- Finding: **K=6 + Gemini-judge gives 22/25 = 88%, WORSE than K=1 (23/25)**. MCQ_SET dropped 4/5 → 2/5. Gemini-judge is not a good MCQ_SET discriminator. **Production: K=1 only.**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pil_monitor/inbox/2026-05-19T1456Z_den_best_of_n_protocol.md",
     "lines": "192",
     "quote": "If judge-selected winners are not reliably better than deterministic filters, do not use Gemini judge. Use the deterministic filter plus stable candidate bank instead."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/unit1_hybrid_showcase_balanced15_after_b0f41b9/selector_calibration_full/SELECTOR_CALIBRATION.md",
     "lines": "10",
     "quote": "| gemini | 15 | 13 | 0.8667 | 0.965333 | 0 |"
    }
   ],
   "against": "The same kind of judge did help another item type, which rose from 22/30 to 28/30: \"- This confirms K=6 + Gemini absolute judge is valuable for MCQ.\" (~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md line 947).",
   "adds_to_existing": [
    65,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Remove drafts that fail code checks before a model ranks the rest; a model ranker let through answer leaks, cut-off options, reversed facts and invented sources.",
   "kind": "measured",
   "found_by": "A branch that let a model judge pick among four drafts kept serving sets with answer leaks, cut-off options and a reversed fact, and was rejected after 3/5 on its final smoke check.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
     "lines": "75",
     "quote": "- Gemini ranking must happen after deterministic local validators remove obvious bad candidates."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
     "lines": "76",
     "quote": "- Do not trust Gemini to catch MCQ_SET answer leaks, truncated options, wrong crop direction, or DBQ source hallucination. Evidence from the rejected branch shows it missed these."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/unit1_workflow_v2_branch_result_20260525T093757Z.md",
     "lines": "81",
     "quote": "- Gemini did not reliably reject these candidates."
    }
   ],
   "against": "Code checks catch only the obvious: \"The visible deterministic rules catch the obvious defects but cannot reliably identify the evaluator's latent concerns without damaging passed controls.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/a0f_validator_probe_20260519.md line 42).",
   "adds_to_existing": [
    67,
    32
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a model chooses among drafts, have it return only which one and serve that draft unchanged from code; a model asked to fit or reshape drafts rewrote them, even when told not to.",
   "kind": "measured",
   "found_by": "A second model asked to fit drafts to the schema rewrote their content with weaker knowledge (23 points below the best run) and kept rewriting under explicit verbatim rules; the fix was a picker that can only output an index, with code serving the chosen draft.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md",
     "lines": "52",
     "quote": "| K=3 + Gemini Flash 3.5 \"reshape\" | -23pp vs PEAK | Gemini regenerated content from scratch (weaker domain knowledge) |"
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md",
     "lines": "54",
     "quote": "| K=3 + Gemini \"structure-only\" | Still regenerating | Schema constraint + token cap overrode \"verbatim\" hard rules |"
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md",
     "lines": "56",
     "quote": "| Current (picker-only, v0.4.0) | TBD — needs IB run | Gemini emits only `{best_index: N}`, Python serves verbatim |"
    }
   ],
   "against": "The picker-only fix went live before its quality was measured (its row reads \"TBD — needs IB run\", same file line 56).",
   "adds_to_existing": [
    29,
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before crediting or blaming a change to the writer's instructions, confirm from the output that it reached the writer for every item type; hidden repair routes and template bypasses ignored it.",
   "kind": "measured",
   "found_by": "A comparison of two instruction sets on the production writer came out reversed because two item types went through repair routes that never saw the instructions; a setting that required live generation was bypassed by a hard-coded template route.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_live_verdict_20260526.md",
     "lines": "25",
     "quote": "The v80bchain balanced15 result (E 14/15 > A 12/15) was a false signal: v80bchain selects deterministic repair routes (`dbq_source_repaired`, `mcq_set_repaired`) before the duck directives reach the model."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/BEAD_EVIDENCE_INDEX.md",
     "lines": "61",
     "quote": "**Duck directives don't reach the model for those cells. Code-port required (pil-6bp.10).**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "2092",
     "quote": "Initial `model_required` env was insufficient because Unit 1 had a hardcoded scored-template bypass before `call_fireworks`."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Record which path produced each item and report fresh output apart from fallbacks and previously approved stock; a pass rate that includes served stock or retries is a different measure from first-attempt quality.",
   "kind": "measured",
   "found_by": "A claimed 500/500 result included 28.8% of items served from a cache of known-good items for the two hardest types; a validated 50/50 included 4 timeout fallbacks (46/50 fresh); an audit warned that a retry stack had quietly redefined the gate.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_analyzer/2026-05-30T0640Z_dream_sequence_2_sync.md",
     "lines": "20",
     "quote": "Layer distribution (final): 71.2% L3 fresh ML + 28.8% L5 cached fallback + **0% exc** (was 9% pre-fix)."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/validated_library_20260525.md",
     "lines": "55",
     "quote": "- 46/50 strict fresh LLM passes = 92.0%."
    },
    {
     "path": "~/Documents/aptraining/conscience/audit_log/2026-05-29T0908Z_CHECKIN_to_main_a.md",
     "lines": "83",
     "quote": "The argument is mathematically correct (K=5 retry on a 95% per-cell base = 99.97%), but it shifts the gate from \"model passes 95% standalone\" to \"stack passes 99% with model as one component.\""
    }
   ],
   "against": "The serving side treated fallback as legitimate for delivery: \"L5 fallback IS the production-correct path for catastrophic cells (degraded mode returning known-good cached items).\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_analyzer/2026-05-29T1840Z_dream_sequence_sync.md line 32) - acceptable for delivery, not as a measure of new content.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When no draft passes, return nothing rather than a filler item; padding gaps with placeholder text produced fake, repeated sources that scored zero.",
   "kind": "measured",
   "found_by": "Fallbacks that padded missing material with placeholder text produced repeated fake documents; in one official run 179 rows of one item type carried the placeholder and that type scored 12/193; a least-bad fallback also leaked a wrong-period item.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "247",
     "quote": "- The generic DBQ fallback padded missing source documents with curriculum facts using `Retrieved APUSH Unit {unit} source N`, which produced fake repetitive documents."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "1851",
     "quote": "- The same placeholder pattern existed in the generic MCQ_SET fallback: 179 generation rows contained `Retrieved APUSH`."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
     "lines": "62",
     "quote": "- If no LLM candidate passes gates, fail closed rather than return a canned final."
    }
   ],
   "against": "Blocking with no fallback turned quality failures into no output at all: \"Lesson: do not hard-reject all deterministic MCQ_SET quality failures unless K is expanded or a fallback candidate policy exists.\" (~/Documents/aptraining/parallel-ideas-lab/reports/24H_CARETAKER_STATE_20260521.md line 29).",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Label every result with how it was produced (full official run, sampled smoke check, local re-score, mixed draws) and never present a sample or a re-score as the official number.",
   "kind": "adopted rule",
   "found_by": "Sampled smoke checks, local re-scores and mixed-draw aggregates were being read as official scores; a run-mode taxonomy was adopted and report scripts were patched to stamp each result's evidence class.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md",
     "lines": "161",
     "quote": "The lab refuses to conflate evidence classes. Every artifact is labeled:"
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md",
     "lines": "167",
     "quote": "- `LIVE_FULL_IB_EXPORT_ANALYSIS` is NOT `LIVE_FULL_IB`; cross-draw `LOCAL_MIX` is NOT board-quality"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/request_trace/2026-05-21T075822Z_2926c4107df0.md",
     "lines": "9",
     "quote": "The trajectory is to operationalize that taxonomy and implement the agreed gates/backlog so future runs do not confuse exploratory local evidence with official live benchmark evidence."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Measure one fixed version per run; a run that spans several deployments, or starts within minutes of a change, is not evidence for any of them.",
   "kind": "measured",
   "found_by": "An official run kept going across several deployments and mixed outputs from old and fixed code, so it was declared invalid and restarted; mapping runs to code showed that runs started within minutes of a change may have hit the previous version.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "241",
     "quote": "- The export is invalid as evidence for the fixed endpoint because it continued through multiple deployments and includes old placeholder generations plus the intermediate DBQ source-gate 502s."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/runs_to_commits_40d.md",
     "lines": "63",
     "quote": "- Render auto-deploys on push; typical deploy-live latency 1-3 min. Runs that fire within ~2 min of a commit push may be reading the prior version."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "2115",
     "quote": "- Important methodology note: deterministic same-build slice `300-349` remains valid only for deterministic/template mode. It cannot be counted as LLM-required proof."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Draw test items from across the whole item set; a gate built from the first item of each type tested one objective per type and proved nothing about the rest.",
   "kind": "measured",
   "found_by": "A 135/135 gate turned out to have tested only the first objective of each type in each unit; widening a 15/15 gate to 30 items dropped it to 20/30 by exposing a second topic cluster; a harness asked for six items per type produced fewer until patched.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "1005",
     "quote": "The completion audit caught an important scope error: the prior 135/135 gate used the replay harness's default `first_per_type` selector. That proves each unit's first benchmark standard per type, not the full benchmark files and not standard diversity across each file."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/goal_runs/RUNNING_SUMMARY.md",
     "lines": "17",
     "quote": "- `official_n30_balanced_20260514T225509Z`: 20/30 = 66.67%; expansion exposed the second APUSH Unit 3 independence-movement cluster."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/goal_runs/official_n30_balanced_after_7e027d7_20260515T011350Z/RESULTS.md",
     "lines": "33",
     "quote": "- Patched the smoke harness selector so `--per-type 6` actually produces 30 rows, balanced 2 easy / 2 medium / 2 hard per type."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check a fix on the items it targeted, then on their neighbours and on a fresh balanced set from the same build; targeted wins repeatedly came with broad regressions.",
   "kind": "measured",
   "found_by": "Versions that fixed their exact blocker items (2/2, 8/8) left the balanced set at 8/15, 12/15 or 35/50; a family regression check caught a previously passing item falling to 0.65 after a neighbouring fix.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
     "lines": "40",
     "quote": "| `0.1.300` | exact MCQ_SET blockers `2/2`, balanced15 effective `8/15 = 53.33%` | Targeted green, broad regression |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "2039",
     "quote": "- Process note: targeted failed-row retests were not sufficient here. The widened family regression gate caught a live breakage in an already-green neighboring row, so future patches should include an affected-family or affected-slice regression gate before claiming a fix is safe."
    },
    {
     "path": "~/.openclaw/workspace-incept/memory/ap-benchmark-context.md",
     "lines": "12",
     "quote": "| benchmark.retest | `python -m benchmark.retest --unit N --concurrency 30` | Retest failures + control, regression check |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    60,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Compare versions on the same items and count which items each one passes; equal totals hid versions that solved different items.",
   "kind": "measured",
   "found_by": "Fourteen prompt recipes run on the same 15 items showed that tied totals hid different solved items, and most pairs traded items rather than one dominating the other.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_14way_verdict_20260526.md",
     "lines": "38",
     "quote": "G and C both hit 12/15. Neither strictly dominates: **G_only=2 (MCQ rows), C_only=2 (MCQ_SET + DBQ rows).** They solve different rows."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_14way_verdict_20260526.md",
     "lines": "64",
     "quote": "4. **Strict dominance is rare.** Only C strictly dominates I (1-0). Every other pair has crossings — recipes trade row classes for row classes."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/combo_tournament_protocol_20260525.md",
     "lines": "15",
     "quote": "5. Promote only after same-row and fresh-row evidence."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Changes that each helped don't simply add up: test the combination itself and remove one change at a time, keeping only those whose removal hurts.",
   "kind": "measured",
   "found_by": "A ranker that scored changes as additive picked a 20-change bundle that lost to the incumbent 73/100 vs 76/100; the bundle combined a primary rule and its own fallback for the same item type.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_search_20260526.md",
     "lines": "19",
     "quote": "It produced `candidate_top_n20_repair_recorded`, which lost the random100 gate **73/100 vs incumbent 76/100** at avg overall `0.8904` vs `0.9094`, while still depending on `dbq_source_repaired` (18/20) and `mcq_set_repaired` (19/20) routes — i.e., not strict-fresh at all."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/handovers/20260526T064354Z_TYPED_DUCK_COMBO_HANDOVER.md",
     "lines": "124",
     "quote": "These do not add cleanly. The first is the primary DBQ policy. The second is fallback style only when real packs are unavailable. Treating them as simultaneous positive ingredients is wrong."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/combo_tournament_protocol_20260525.md",
     "lines": "129",
     "quote": "3. If performance does not drop, remove that duck permanently."
    }
   ],
   "against": "The losing bundle also ran through repair routes that bypassed its instructions (same sentence, typed_recipe_search_20260526.md line 19), so not all of its loss is due to non-additivity.",
   "adds_to_existing": [
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Adding instructions to a writer's prompt can lower quality, so test each addition; extra or irrelevant directives cost passes.",
   "kind": "measured",
   "found_by": "Grounding directives lowered every recipe they were added to at 15 items; dropping one unrelated serving directive lifted one item type from 1/5 to 3/5; a recipe with four fewer directives came within two passes of the best.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_14way_verdict_20260526.md",
     "lines": "62",
     "quote": "3. **Grounding ducks (the new inventory adds) hurt overall.** Despite static_pass and despite intuitive appeal, M/N/O/P all underperform their non-grounded parents. Hypothesis: prompt-attention dilution. Verified by P (lean+grounding) ≤ I (lean), M ≤ C, N ≤ G."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/sweep_n25_final_verdict_20260526.md",
     "lines": "53",
     "quote": "3. **Surprise: dropping `serve_time_single_ib_grade_contract` from G lifts MCQ_SET 1/5 → 3/5.** That directive may be confusing Gemini's MCQ_SET focus. Worth investigating word-level rephrase."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/sweep_n25_final_verdict_20260526.md",
     "lines": "55",
     "quote": "4. **`K_lean_plus_mcq_no_stim` is the budget champion.** 19 ducks, 21/25 = 84%, MCQ_SET 3/5. Only 2 passes behind the champion at 4 fewer ducks. Less prompt = less attention dilution."
    }
   ],
   "against": "One added directive that was predicted to hurt gave the best result: \"1. **`ib_rubric_criterion_alignment` is the breakthrough duck.** Adding it to G yields the unique top recipe at 23/25 with the highest avg score (0.978) AND MCQ_SET 4/5. Predicted at -5 from n=15, actual at +3.\" (~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/sweep_n25_final_verdict_20260526.md line 49).",
   "adds_to_existing": [
    62,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "The right option must not be findable by matching words or close synonyms from the stem, the source or its labels; when it is, change what the question asks rather than swapping in synonyms.",
   "kind": "measured",
   "found_by": "Items failed when the keyed option reused the source's words; swapping in a synonym still failed (0.78), and the item passed (1.0) only once it asked why the idea mattered instead of asking students to name it; a local audit flagged 31 items whose answer copied stem terms.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "109",
     "quote": "- `mcqset_repair_offline_v2`: changed Q2 wording away from \"supremacy\"; score 0.78 because \"taking precedence\" was still treated as a synonym leak for \"supreme.\""
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "110",
     "quote": "- `mcqset_repair_offline_v3`: changed Q2 to ask why the principle mattered historically under the Articles rather than asking students to name/paraphrase the principle. Local IB scored 1.0."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md",
     "lines": "56",
     "quote": "Penalize keyed answers sharing words with labels; otherwise IB sees decorative/source-cued items."
    }
   ],
   "against": "The rubric-derived writer prompt pushed the other way: \"- The stem must reference the stimulus explicitly (\"According to the source...\", \"The passage above suggests...\").\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md line 91); and a warning to the writer alone did not help: \"- Answer-hiding phrasing alone did not improve MCQ_SET.\" (~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md line 807).",
   "adds_to_existing": [
    3,
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make questions need taught knowledge beyond what the given text says, never knowledge beyond what was taught, and let difficulty come from that knowledge rather than from reading load.",
   "kind": "adopted rule",
   "found_by": "Most multiple-choice failures were answers findable by reading the item; rubric-derived prompts required that full marks be earnable from the taught content; validators required difficulty to come from knowledge beyond the source.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
     "lines": "134",
     "quote": "- difficulty must be earned by outside APUSH context, not reading comprehension."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md",
     "lines": "117",
     "quote": "- MCQ misses are mostly educational-accuracy failures: answer can be found by reading, answer leaks, or weak APUSH knowledge demand."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_leq.md",
     "lines": "43",
     "quote": "- Students can earn full marks using ONLY the curriculum (no obscure outside knowledge required)."
    }
   ],
   "against": "The same prompts let the easiest level match the taught statement almost word for word: \"- Easy: direct recall of one curriculum fact; correct answer matches statement nearly verbatim.\" (system_prompt_mcq.md line 96).",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Build wrong options from the same theme, period and category as the right one and of similar length, so the key isn't the only option that touches the topic, while keeping each one clearly wrong.",
   "kind": "measured",
   "found_by": "Items failed when only the keyed option mentioned the topic or when the wrong options came from another domain; replacing them with same-domain alternatives made the items pass (1.0).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/B0045_STAGED_MCQSET_INTERIM_20260519.md",
     "lines": "55",
     "quote": "Gender-role MCQ_SET Q2 fails because only the keyed option visibly signals gender."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "460",
     "quote": "- MCQ_SET `hard-4`: religious-liberty Q3 used treaties/taxes as distractors, making the Virginia Statute too obvious."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md",
     "lines": "82",
     "quote": "- Be in the **same category** as the correct answer (e.g., if correct is a person, distractors are people; if a date, distractors are dates from the same era)."
    }
   ],
   "against": "Same-theme wrong options can turn into defensible second keys: \"| v7 gender same-theme distractor attempt | 1/3 | Regressed badly; reverted. |\" (B0045_STAGED_MCQSET_INTERIM_20260519.md line 41).",
   "adds_to_existing": [
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check the facts in the parts students don't see first (model answers, marking notes, explanations, source dates and attributions); good-looking items failed on errors hidden there.",
   "kind": "measured",
   "found_by": "Failures traced to sample answers, rubric notes, explanation text and source metadata (a document dated after its author's death); replacing a model-written explanation alone lifted one item from 0.33 to 0.97.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pil_monitor/inbox/2026-05-19T1456Z_den_unit1_trap_verifier.md",
     "lines": "17",
     "quote": "Observed LLM-required failures are mostly not structurally bad items. They are good-looking items poisoned by historically wrong teacher-facing metadata:"
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md",
     "lines": "87",
     "quote": "SAQ can have fine prompts but fail because the sample response contains factual errors."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/24H_CARETAKER_STATE_20260521.md",
     "lines": "27",
     "quote": "`ap-apush-1-mcq_set-medium-12` improved from `0.33` to `0.97`"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Use real, verified source texts; when none is available, describe a source by role and period rather than inventing a named author or date.",
   "kind": "measured",
   "found_by": "Model-written sources were fabricated or misdated and scored zero; retrieving vetted sources by objective fixed one slice (0.98); a second judge caught the synthetic-source pattern the main judge passed, and agreement rose from 81.1% to 97.8% once real sources were used.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "88",
     "quote": "- Dynamic DBQ cannot be allowed to invent source documents. It needs retrieved vetted documents or document-bank retrieval by standard. Source retrieval fixed the focused institution DBQ slice: `dynamic_source_gate_dbq_mcqset_v1` DBQ scored 0.98."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pil_monitor/inbox/2026-05-19T1456Z_den_unit1_trap_verifier.md",
     "lines": "58",
     "quote": "Prefer generic-safe attributions over fancy named sources unless the person/date pair is verified."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_conscience/2026-05-29T1840Z_dream_sequence_sync.md",
     "lines": "16",
     "quote": "- **Gemini-vs-IB calibration** 14:55Z: 81.1% overall; DBQ 16.7% (Gemini correctly catches synthetic-source pattern; LEQ/MCQ_SET/SAQ 100%)"
    }
   ],
   "against": "Role-only attributions are a fallback, not a substitute: \"Role-based source descriptions can avoid hallucinated names; use carefully because real source packs are preferable.\" (~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md line 98); \"Generic fabricated documents can reduce obvious fact-check failures, but may conflict with source authenticity expectations.\" (~/Documents/aptraining/parallel-ideas-lab/reports/deep_repo_extraction_20260525.md line 138).",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A real source helps only if it fits the item's exact objective; retrieved but mismatched documents did worse than none.",
   "kind": "measured",
   "found_by": "Locking the writer to retrieved real documents scored 0/30 because retrieval often returned packs that didn't fit the question; prompts named one group while the documents covered another.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/ib_d13_wrapper_eval/RESULTS.md",
     "lines": "24",
     "quote": "- The local v4 retrieval/doc-lock route is not usable as-is: it frequently retrieves irrelevant/misaligned packs, and doc-locking those packs hurts."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/ib_d13_wrapper_eval/RESULTS.md",
     "lines": "15",
     "quote": "| Local v4 D13 doc-lock | `y4axbi4f_d13_doclocked_generations.jsonl` | 0/30 | 0.0% | 0.1283 | 1 | 0 |"
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
     "lines": "106",
     "quote": "- source pack mismatch, e.g. prompt names Africans but documents only cover Native Americans."
    }
   ],
   "against": "Retrieval keyed to the exact objective worked: \"Source retrieval fixed the focused institution DBQ slice: `dynamic_source_gate_dbq_mcqset_v1` DBQ scored 0.98.\" (failed_export_replay/RUNNING_SUMMARY.md line 88).",
   "adds_to_existing": [
    58,
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep editorial text out of the body of a source: summaries, conclusions and notes on its usefulness read as fabricated or as aimed at the marker, so put them in the label or the marking guide.",
   "kind": "measured",
   "found_by": "Source packs that said 'The passage gives enough context for sourcing analysis' were zeroed as gaming; modern summaries inside documents failed factual and source quality; a conclusion-style final document gave away the argument (0.82) and passed (1.0) once rewritten as an evidence inventory.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/unit1_workflow_v2_branch_result_20260525T093757Z.md",
     "lines": "74",
     "quote": "- Local IB treated that as evaluation-gaming and zeroed DBQ."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "284",
     "quote": "- Important negative lesson: adding modern summaries inside DBQ `content` made relevance better but failed factual/stimulus quality because IB treats that as fabricated primary-source text."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "1997",
     "quote": "- Only failure was row 60 DBQ easy (`c_9eQY` Native environment), scoring 0.82 because the environment DBQ's Document 7 gave away the synthesis."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    25,
    12
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give a set of sources for an argument task distinct provenance and opposing views; an accurate but redundant, one-sided or neutral list-like set failed.",
   "kind": "measured",
   "found_by": "An accurate but redundant, one-sided document set failed until replaced with a sequence of opposing sources; documents too neutral and list-like for sourcing failed until rewritten as accounts with distinct provenance.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "448",
     "quote": "- DBQ `medium-7`: individual-liberties document pack was accurate but redundant and one-sided."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "2008",
     "quote": "rows 61-62 DBQ hard/medium failed because the documents were too neutral and list-like for sourcing analysis,"
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
     "lines": "97",
     "quote": "- source-role diversity for demographic/disease prompts;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Count how many distinct items a run produced; a generator serving a few identical items over and over passed many checks but failed each request's specific objective.",
   "kind": "measured",
   "found_by": "A completed run's 216 document-based items held 6 distinct payloads (72 identical) and its 211 sets 13; later decision reports found 4 distinct fingerprints per 45 items.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/A0F_COMPLETED_RUN_READINESS_20260520.md",
     "lines": "44",
     "quote": "| DBQ | 216 | 6 | 72 identical payloads |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/A0F_COMPLETED_RUN_READINESS_20260520.md",
     "lines": "50",
     "quote": "DBQ and MCQ_SET are behaving like static template banks. That can pass many rows, but it is exposed by variety scoring and by substandard-specific alignment failures."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/reports/run_324d5e51_live_update_decision.md",
     "lines": "21",
     "quote": "- MCQ_SET fingerprint uniqueness is below 30%; static stimulus templates are still active."
    }
   ],
   "against": "Variety needs enough samples to measure: \"The small sample showed MCQ_SET duplicate fingerprint `1/2`, so future pre-live diversity smoke should use at least 5 extra DBQ/MCQ_SET samples.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/request_trace/2026-05-21T075822Z_2926c4107df0.md line 27).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Match content to the item's exact objective, not its broad topic or title; an item that passed for one objective failed when reused for a narrower neighbouring one.",
   "kind": "measured",
   "found_by": "Reusing a passed item for a sibling objective failed it; objectives routed by broad title went to the wrong topic's material; in one run 98% of failing document-based items were factually accurate but off the specific objective, and 71 of 98 quality failures in another were alignment failures.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/B0045_STAGED_MCQSET_INTERIM_20260519.md",
     "lines": "25",
     "quote": "3. Regression risk: broad winner reuse can fail a narrower substandard, as seen for gender/family when a labor-oriented passed sibling was reused."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/UNIT1_TO_ALL_UNITS_TRANSFER_PLAN.md",
     "lines": "80",
     "quote": "- Description-specific routes must beat generic lesson-title matches."
    },
    {
     "path": "~/Documents/aptraining/analyzer/reports/run_f54d5849_what_is_going_wrong.md",
     "lines": "20",
     "quote": "Of 125 DBQ failures: **`curriculum_alignment = 0` in 98 % (122 / 125); `factual_accuracy = 0` in only 2 % (3 / 125).**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    58
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat example items given to a writer as a risk: it copies their content and flaws, so vet them and strip examples from other topics down to structure.",
   "kind": "measured",
   "found_by": "The writer copied an example from another period straight into a request; a prompt style built on worked examples scored 83/150 against 113/150 for the best plain style; high-scoring bank items carried leaks and multiple defensible answers.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "71",
     "quote": "The first dynamic smoke copied a bad few-shot-like Gilded Age/Riis MCQ into an APUSH Unit 3 request."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/UNIT1_TO_ALL_UNITS_TRANSFER_PLAN.md",
     "lines": "60",
     "quote": "- Do not trust high-scoring few-shot/pattern rows blindly."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md",
     "lines": "548",
     "quote": "- Primary-source few-shot with long examples: `0/13`; likely overfits to source shape and drifts from the target objective."
    }
   ],
   "against": "Some example-based styles were the best for one type: \"- Exam-writer few-shot MCQ_SET prompts are the best stable MCQ_SET style so far:\" (~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md line 538).",
   "adds_to_existing": [
    57,
    61
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a pick-from-several pipeline fails, check whether any draft passed: if one did, fix the picking; if none did, fix how drafts are written, because more checks only reject.",
   "kind": "measured",
   "found_by": "Failures split into 114 where a passing item existed but wasn't chosen and 45 where none existed; fixing the choosing rescued 9/11 of the first kind and 0/4 of the second; stacking more guards made the writer fill gaps with new failures.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md",
     "lines": "109",
     "quote": "If a passing candidate exists but was not selected, fix retrieval/selector; if none exists, fix generation/data."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md",
     "lines": "107",
     "quote": "- bank_gap rescue rate **0/4 = 0%** (confirmed: parent's fallback can't help; lab mining needed)"
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/LLM_FINAL_ROUTE_STATUS_20260522T185623Z.md",
     "lines": "179",
     "quote": "The new guards caught the previous leaks, but the LLM filled the gap with new failure modes. More generic guard stacking is likely to chase symptoms."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    39,
    65
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before adopting an automatic check, run it on known failures and known passes and report both how many failures it catches and how many good items it would wrongly reject.",
   "kind": "measured",
   "found_by": "A validator suite caught 19 of 102 known failures (0.186) while rejecting 22 known passes; two text detectors were retired because they matched the names of criteria in the judge's narrative rather than failures.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/a0f_validator_probe_20260519.md",
     "lines": "3",
     "quote": "This is a local probe against the A0F export. It measures candidate validators against both failed rows and passed controls."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/a0f_validator_probe_20260519.md",
     "lines": "11",
     "quote": "- False rejects: 22 (0.063)"
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md",
     "lines": "222",
     "quote": "- Both retired; were matching metric NAMES in evaluator narrative, not actual failures."
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
   "statement": "A passed format check says nothing about quality; runs that were fully valid in shape still hid failing items.",
   "kind": "measured",
   "found_by": "A 50/50 shape pass scored 41/50 on quality; schema-valid output for all 26,355 requests was explicitly not a quality result; a preflight with every shape passing still hid a 0.0 and a 0.75.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/24H_CARETAKER_STATE_20260521.md",
     "lines": "54",
     "quote": "A scored `0.1.37` preflight found hidden quality failures despite shape passing"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "1030",
     "quote": "This proves the local candidate can emit schema-compatible content for all 26,355 benchmark rows, but it is not a substitute for IB scoring."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
     "lines": "31",
     "quote": "| `0.1.186` | fresh balanced50 shape `50/50`, score `41/50` | Availability fixed, quality not |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Write a report's narrative from the run's own numbers; templated summary text claimed 95% passing for a run in which every item scored zero.",
   "kind": "measured",
   "found_by": "Comparing the lab's auto-generated pattern reports across runs showed every one carried the same title and the same narrative, including the run in which the judge's lookup failed and every item scored 0.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/reports/run_5eb118bd_success_patterns.md",
     "lines": "93",
     "quote": "Almost everything passes (95%). Pass rows have ~7 documents (matches the live overlay hard rule) and roughly even doc word counts."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/runs_to_commits_40d.md",
     "lines": "41",
     "quote": "| 2026-05-26 19:59 | `5eb118bd` | 673 | 0.0% | `da0bc27` | `0.1.303-llm-final-mcqset-shape-repair` | dbq=0/132 leq=0/135 mcq=0/138 mcq_set=0/132 saq=0/136 |"
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/reports/run_324d5e51_failure_modes.md",
     "lines": "1",
     "quote": "# Run-0133 v2 — failure deep-dive"
    }
   ],
   "against": "The per-run tables in the same report family were computed from each run: \"| dbq | 0/0 | n/a | 0 | n/a |\" (~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/reports/run_5eb118bd_live_update_decision.md line 12).",
   "adds_to_existing": [
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Apply an extra pipeline stage only to the item types it measurably helps; source injection lifted source-based types while the same stages lowered free-response types.",
   "kind": "measured",
   "found_by": "The same retrieval-heavy pipeline added 58.6 and 20.9 points to the two source-based types but cost the essay type 9.6 points and the short-answer type 2.3; a fallback that helped one type regressed two others when applied to all.",
   "evidence": [
    {
     "path": "~/.openclaw/workspace-incept/memory/2026-05-21.md",
     "lines": "16",
     "quote": "- LEQ: Pipeline 90.4% vs Model standalone 100% (-9.6pp)"
    },
    {
     "path": "~/.openclaw/workspace-incept/memory/2026-05-21.md",
     "lines": "23",
     "quote": "MCQ_SET and DBQ must remain in the pipeline because they rely on stimulus/RAG injection (+58.6pp and +20.9pp respectively)."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/BEAD_EVIDENCE_INDEX.md",
     "lines": "66",
     "quote": "- Finding: 19/25 = 76%. DBQ 4/5 (fallback works), but MCQ/MCQ_SET regress. **Use per-KC only, never globally.**"
    }
   ],
   "against": "The lab guide took the opposite general stance: \"**Architectural rule:** raw model is one component; pipeline is the multiplier.\" (~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md line 68).",
   "adds_to_existing": [
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Name why items fail before choosing a fix; fixes layered on without a diagnosis gave no overall lift and added new failures.",
   "kind": "measured",
   "found_by": "Forty days of layered fixes left served quality flat at about 84% and added type-specific regressions, including a fix that crashed the very type it targeted to 12.5%.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/analyzer/reports/production_surface_40d.md",
     "lines": "8",
     "quote": "Every tactic layered on top (anti-static, selector, source-fallback, shape-repair, pubdate-strict) produced **zero aggregate lift** and several **cell-specific regressions**."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md",
     "lines": "129",
     "quote": "Before prompt churn, check whether the failing KC is period-mismapped or criterion-misaligned."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/PIPELINE_WRAPPER_ACTION_PLAN.md",
     "lines": "105",
     "quote": "- Failure-forensics gate before pipeline changes."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    60,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make each part of a multi-part question answerable on its own, give each prompt a single task, and order parts from lower to higher demand.",
   "kind": "adopted rule",
   "found_by": "The writer prompts derived from the judge's rubric listed chained parts, multi-task prompts and all-recall parts among the commonest ways items fail.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_saq.md",
     "lines": "71",
     "quote": "2. **Chained dependencies.** Part b is impossible to answer without first answering part a correctly. Parts should be independent within a shared context."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_leq.md",
     "lines": "76",
     "quote": "4. **Multi-task prompt.** \"Discuss the causes AND consequences AND legacies of X\" — that's three essays. One task per LEQ."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_saq.md",
     "lines": "83",
     "quote": "- [ ] Verb difficulty escalates a → b → c (typical pattern)"
    }
   ],
   "against": "Switching the rubric-derived kit on lowered the pass rate as a whole: \"| v80b K=1 + kit on | 79.7% | run-4c9da828 (FILE2) 2026-05-22 |\" (~/Documents/aptraining/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md line 34), against 85.7% without it, so these rules are untested one by one.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Match a question's thinking demand to what its objective asks; recall questions on analysis objectives, and prompts whose verb doesn't match the named skill, fail.",
   "kind": "adopted rule",
   "found_by": "Rubric-derived prompts named recall-only questions on analysis objectives and skill/verb mismatches as common fail traps; a failing hard item passed after it was rewritten to require synthesis.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md",
     "lines": "115",
     "quote": "7. **Recall-only on a higher-order standard**: standard demands analysis but stem asks \"what year did X happen\". Match cognitive demand to the standard."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_leq.md",
     "lines": "73",
     "quote": "1. **Reasoning skill mismatch.** Prompt is labeled \"comparison\" but actually asks for causation. Match the verb to the skill."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "387",
     "quote": "- Repaired MCQ hard institution item to require synthesis rather than recall."
    }
   ],
   "against": "Same kit caveat: switching the kit on lowered the pass rate to 79.7% from 85.7% (synapse_checkin_2026_05_27_pipeline_quality_paradox.md line 34).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check a set of questions as a whole: no two may test the same fact or share a key, and no key may contradict another's.",
   "kind": "adopted rule",
   "found_by": "Set-level failures (repeated questions, contradictory keys within a set) were named in the rubric-derived prompts and showed up in failure tallies (17 'redundant_questions' tags in one run).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq_set.md",
     "lines": "89",
     "quote": "6. **Inter-question contradictions**: Q1's correct answer says \"X caused Y\", Q3's correct answer says \"Y caused X\". Audit consistency across the set."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq_set.md",
     "lines": "63",
     "quote": "- No two questions have the same correct answer or test the same fact."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/reports/run_324d5e51_failure_modes.md",
     "lines": "18",
     "quote": "| `redundant_questions` | 17 |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    41
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Require a judge to quote the evidence behind each verdict, and discard verdicts that come without one.",
   "kind": "adopted rule",
   "found_by": "The lab's protocol for choosing among drafts made a quoted piece of evidence a required part of every judge verdict.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pil_monitor/inbox/2026-05-19T1456Z_den_best_of_n_protocol.md",
     "lines": "92",
     "quote": "If `evidence_quote` is empty, invalidate the judge result."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pil_monitor/inbox/2026-05-19T1456Z_den_best_of_n_protocol.md",
     "lines": "74",
     "quote": "Only judge surviving candidates. The judge must output evidence:"
    }
   ],
   "against": "No measured result for this rule appears in the sources.",
   "adds_to_existing": [
    16,
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Pin and record the judge's version with every score, and re-grade older results before comparing them; scores from an earlier judge version are design evidence, not current results.",
   "kind": "adopted rule",
   "found_by": "Earlier 90%+ results had been scored by older judge versions that passed different things; a sibling generator's 97% on an older judge was explicitly ruled not comparable.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/HANDOVER_PARALLEL_IDEAS.md",
     "lines": "23",
     "quote": "The parent project has old 90%+ results, but those were on older grader behavior. Do not treat them as current performance unless regraded on the current InceptBench version."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/PIPELINE_WRAPPER_ACTION_PLAN.md",
     "lines": "104",
     "quote": "- Grader-version pinning in every eval artifact."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pipeline_status_2026-05-18.md",
     "lines": "164",
     "quote": "5. Claims from older InceptBench versions should be treated as design evidence, not certified current scores."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    45,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat a gain that comes from exploiting a gap in the judge's rubric as fragile, not as better content.",
   "kind": "adopted rule",
   "found_by": "Leaving the source out of some question types raised pass rates, but the lab tagged it as a rubric blind spot and kept a fallback for when the judge is fixed.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md",
     "lines": "132",
     "quote": "MCQ/SAQ/LEQ no-stimulus may pass current rubrics, but it is a known rubric hole and should be treated as fragile/second-tier unless the product spec allows review-drill shape."
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/sweep_n25_final_verdict_20260526.md",
     "lines": "73",
     "quote": "| `mcq_no_stimulus_can_help` | **rubric_exploit** | If IB patches no-stim blindspot, fall back to C (loses MCQ 5/5, recovers MCQ_SET 3/5) |"
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md",
     "lines": "141",
     "quote": "Different optimization targets (pass judge vs serve educators)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44,
    51
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Refuse to produce kinds of item that have never been checked against the judge rather than ship unvalidated output.",
   "kind": "adopted rule",
   "found_by": "The generator offered only the five item types that had been evaluated and refused the rest because there was no evaluation signal for them.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/README.md",
     "lines": "67",
     "quote": "Unsupported (returns 501): `msq`, `fill-in`, `match`, `sequence`, `article`."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/README.md",
     "lines": "137",
     "quote": "- We have no signal on `msq` / `fill-in` / `match` / `sequence` / `article` from internal eval — gated to 501 to avoid shipping unvalidated outputs."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Give the writer the full description of the objective and the criteria its work will be judged by, not just the topic name.",
   "kind": "measured",
   "found_by": "Adding a directive to align with the judge's rubric criteria produced the best recipe (23/25, mean 0.978) in a 67-recipe sweep; after 98% of document-question failures proved to be alignment misses, the objective's full description was injected into the writer's prompt.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/sweep_n25_final_verdict_20260526.md",
     "lines": "49",
     "quote": "1. **`ib_rubric_criterion_alignment` is the breakthrough duck.** Adding it to G yields the unique top recipe at 23/25 with the highest avg score (0.978) AND MCQ_SET 4/5. Predicted at -5 from n=15, actual at +3."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_analyzer/2026-06-01T1838Z_dream_sequence_sync.md",
     "lines": "28",
     "quote": "injects expanded LO + KC-description text into the DBQ generator prompt directly, so curriculum-alignment signal lands in the input, not just the rubric."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md",
     "lines": "45",
     "quote": "- `assessment_boundaries`: `{{assessment_boundaries}}` (what to assess; what NOT to assess)"
    }
   ],
   "against": "The same directive had been predicted to cost five passes (\"| add_ib_rubric_criterion_alignment | **-5** |\", ~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/sweep_pre_score_analysis_20260526.md line 93); the sweep was one seed of 25 items; the re-measurement of the description injection is not in the sources.",
   "adds_to_existing": [
    33
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When generated content gets facts wrong, first check whether those facts were in the material the writer was given: if absent, fix the material; if present, change how the writer uses it.",
   "kind": "open question",
   "found_by": "A diagnosis split 'not enough data' into missing facts (a bigger writer won't help) and present-but-unused facts (capacity or conditioning is the lever), and proposed checking the failing facts against the source material; the later fix assumed the second case.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_analyzer/2026-05-27T1741Z_DIAGNOSIS_data_adequacy_binding_lever.md",
     "lines": "16",
     "quote": "**The discriminating test (please make the data-adequacy assessment answer THIS, not just row count):** take the off-period hallucination cases (e.g. the 1920s-DBQ-for-Unit-1 sample) and check whether those specific Unit-1 facts are PRESENT in the training corpus."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_analyzer/2026-05-27T1741Z_DIAGNOSIS_data_adequacy_binding_lever.md",
     "lines": "19",
     "quote": "Row-count alone (\"14k = not enough\") cannot tell these apart, and it's the exact spot where \"bigger base\" gets pulled without the binding lever named."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_analyzer/2026-06-01T1838Z_dream_sequence_sync.md",
     "lines": "30",
     "quote": "This addresses §2 coverage-lever side of your 5/27 binding-lever fork: facts ARE in the corpus, but the generator wasn't conditioned on the curriculum context that defines the alignment criterion."
    }
   ],
   "against": "The test was requested again but no verdict file appears: \"Drop verdict at `from_analyzer/<UTC>_COVERAGE_VS_CAPACITY_v4.md`.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_analyzer/2026-05-28T0614Z_dream_sequence_sync_2.md line 39); from_analyzer holds only an acknowledgement and the original diagnosis.",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check an item's stated difficulty against how real students do on it (the share who answer correctly) rather than trusting the writer's or the judge's label.",
   "kind": "open question",
   "found_by": "Two architecture proposals for a teach-then-test loop proposed comparing generated items with real student results, by stated difficulty and by fact taught.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/analyzer/.lanes/teaching-benchmark/STRATEGY_REPORT.md",
     "lines": "33",
     "quote": "- **P-Value & Point-Biserial Mapping:** Store real-world question difficulty (p-value) against generated questions. If a generated \"Medium\" question has a real-world p-value of 0.20 (Hard), we register a `difficulty_misalignment` failure."
    },
    {
     "path": "~/.openclaw/workspace-incept/STRATEGY_REPORT.md",
     "lines": "82",
     "quote": "3. **Benchmarking & Gap Analysis:** The system compares empirical performance against standard benchmark thresholds. If the success rate for a specific `curriculum_fact_id` falls below the threshold (e.g., 70%), it is flagged."
    }
   ],
   "against": "Proposals only; no student data or measured result appears in the sources.",
   "adds_to_existing": [
    44,
    51
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep each rule for an item in one place; instructions that contradicted each other, or a prompt rule that disagreed with a code check, made the writer refuse or were silently overridden.",
   "kind": "measured",
   "found_by": "A kit instruction to refuse without a source corpus that wasn't wired zeroed one item type; a prompt rule demanding four questions clashed with a validator enforcing three and was silently overridden; contradictory period framings made the writer refuse.",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md",
     "lines": "51",
     "quote": "| Satisfaction kit DBQ refusal | 0% on DBQ | `system_prompt_dbq.md` line 135: \"Without D13: refuse\" — we don't wire D13 |"
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md",
     "lines": "91",
     "quote": "\"EXACTLY 4 questions\" conflicted with hardcoded validator at"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/WINS_20260514.md",
     "lines": "152",
     "quote": "- The kit is prepended to the system prompt, then the original service prompt is appended as the hard schema authority. This prevents the kit's illustrative field names from breaking InceptBench JSON shape."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    67
   ],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Documents/aptraining/analyzer/reports/run_f54d5849_what_is_going_wrong.md",
   "lines": "19",
   "quote": "Wrapper sends `grade: \"1\"` for Unit 1; grader reads as 1st grade; zeros `educational_accuracy` and `clarity_precision`."
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/run_73348c1a_orchestrator_contract.md",
   "lines": "57",
   "quote": "- Echo grade as `AP United States History`, not numeric unit values like `\"1\"` or `\"3\"`."
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pipeline_status_2026-05-18.md",
   "lines": "152",
   "quote": "1. Authoritative course/unit propagation is critical."
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/a0f_failure_map_20260519.md",
   "lines": "24",
   "quote": "| quality_fail_standard_alignment | 71 |"
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/WINS_20260514.md",
   "lines": "49",
   "quote": "- Naive best-of-scored-candidates composite predicted `138/150`, but fresh IB scored `126/150`. Conclusion: single-score banking overfits IB noise."
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/PIPELINE_WRAPPER_ACTION_PLAN.md",
   "lines": "255",
   "quote": "Recovery cascade: 1. keep first patch K=1 only; 2. add BoN only in separate bead; 3. require held-out judge before selection."
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/candidate_library_20260525.md",
   "lines": "43",
   "quote": "- It relies on build-time IB oracle selection, which is acceptable for offline banks only if contract and ethics are explicit."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
   "lines": "1948",
   "quote": "the grader showed nondeterminism on repeated MCQ batches."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/prompt_perfection/runs/ib_safe_v2_t0.0_p1.0/analysis.8001.md",
   "lines": "3",
   "quote": "Passed: 106/150 (70.67%)"
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/K_sweep_99pct_20260519T180652Z.md",
   "lines": "48",
   "quote": "| apush/mcq_set | 16/30 (53.3%) | 16/30 (53.3%) | 16/30 (53.3%) | 16/30 (53.3%) | 16/30 (53.3%) | 16/30 (53.3%) |"
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/K_sweep_99pct_20260519T180652Z.md",
   "lines": "47",
   "quote": "| apush/mcq | 6/30 proxy | 9/30 proxy | 17/30 proxy | 21/30 proxy | 26/30 proxy | 28/30 (93.3%) |"
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/handover_observations_training_questions_2026_05_27.md",
   "lines": "25",
   "quote": "synapse learning `cc714738` (K=N transfers format not facts):"
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pil_monitor/inbox/2026-05-19T1456Z_den_best_of_n_protocol.md",
   "lines": "137",
   "quote": "Those need repair layers, not more N."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
   "lines": "81",
   "quote": "- Store enough candidate payload to replay selector mistakes. Prior K-sweep was weakened because full unselected candidate payloads were missing."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/reports/run_324d5e51_live_update_decision.md",
   "lines": "38",
   "quote": "- Do not add broad deterministic filters unless a selector replay proves net lift."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_search_20260526.md",
   "lines": "109",
   "quote": "if a future change broke any of the audit rules, this control would fail to fail — that's the canary."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/PIPELINE_WRAPPER_ACTION_PLAN.md",
   "lines": "60",
   "quote": "| Local validation | known visual-map DBQ is rejected | regex false-positive on legitimate text source; narrow regex | visual-map DBQ passes |"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md",
   "lines": "59",
   "quote": "All children sharing one correct letter is a set-level smell."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
   "lines": "89",
   "quote": "Q2 content was fixed, but answer keys clustered on A/B and scored 0.84."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq_set.md",
   "lines": "84",
   "quote": "Verify every question requires the stimulus by testing the counterfactual"
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md",
   "lines": "116",
   "quote": "8. **Multi-correct**: two options are defensibly correct. Verify with the rationale that only ONE option survives strict reasoning."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/UNIT1_TO_ALL_UNITS_TRANSFER_PLAN.md",
   "lines": "66",
   "quote": "use overly broad \"best explains\" stems with multiple defensible answers."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
   "lines": "2024",
   "quote": "row 336 MCQ_SET easy scored 0.75 because Q2 asked for European disagreement not actually present in the stimulus,"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
   "lines": "105",
   "quote": "- `dynamic_source_gate_mcqset_v2`: MCQ_SET regressed to 0.0 because generated questions referenced phrases not present in the enforced stimulus (`system of checks and balances`, `supreme law of the land`)."
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
   "lines": "98",
   "quote": "- MCQ_SET validator now rejects quoted phrases in child questions/explanations when those phrases are absent from the enforced stimulus."
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/HANDOVER_PARALLEL_IDEAS.md",
   "lines": "52",
   "quote": "the model emits fabricated visual/document promises that InceptBench hard-zeroes."
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/PIPELINE_WRAPPER_ACTION_PLAN.md",
   "lines": "151",
   "quote": "- prose description of a missing visual is invalid,"
  },
  {
   "truth": 64,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq_set.md",
   "lines": "51",
   "quote": "- If image: provide rich descriptive caption (the grader sees text, not image)."
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md",
   "lines": "243",
   "quote": "- Deterministic compression solved grader length but destroyed educational signal / source richness."
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
   "lines": "284",
   "quote": "Context belongs in source labels/rubrics, not document content."
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/24H_CARETAKER_STATE_20260521.md",
   "lines": "29",
   "quote": "Lesson: do not hard-reject all deterministic MCQ_SET quality failures unless K is expanded or a fallback candidate policy exists."
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/WINS_20260514.md",
   "lines": "207",
   "quote": "- Service commit `985f867` changed `/v1/per-question-generator` to one generation only, with MCQ_SET quality checks recorded as advisory metadata instead of blocking responses."
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md",
   "lines": "9",
   "quote": "- External models may be used only for judging/selection; they must not generate AP question content."
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
   "lines": "76",
   "quote": "- Do not trust Gemini to catch MCQ_SET answer leaks, truncated options, wrong crop direction, or DBQ source hallucination. Evidence from the rejected branch shows it missed these."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Documents/aptraining/analyzer/.agent/BRIEFING.md",
   "lines": "28",
   "quote": "Grader (IB v2.5.x) co-evolved with chain — \"sometimes a sycophant of the chain\""
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md",
   "lines": "141",
   "quote": "Different optimization targets (pass judge vs serve educators)"
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Documents/aptraining/analyzer/.agent/MEMORY.md",
   "lines": "44",
   "quote": "3. **Grader co-evolved with chain.** IB v2.5.3 → v2.5.6 → v2.5.7 → v2.5.11 shifts what \"passes\" mean retroactively. No ensemble, no cross-judge calibration. Treat the grader as a variable."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/MAIN_AGENT_ACTION_PACKET.md",
   "lines": "58",
   "quote": "Use current IB v2.5.7 only. Do not compare against v2.5.6/v2.5.3 without regrade."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
   "lines": "249",
   "quote": "The next proof must be a fresh dynamic generation run using the patched pipeline, followed by the prior n=30 regression gate and eventually the full failed-export replay."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/promotion_gate_20260525.md",
   "lines": "47",
   "quote": "- Failed re-validation/cherry-pick artifacts including old Den 50/50 proof and EXPLOIT-003."
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md",
   "lines": "127",
   "quote": "- **SAQ silent regression -4.5pp** — nobody was focused on this; warrants bisect of deploys 0506c1fd→e7e1d980"
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/UNIT1_TO_ALL_UNITS_TRANSFER_PLAN.md",
   "lines": "118",
   "quote": "- Use the same stop rule: if any type drops below 90% in the sample, stop and repair that type before broadening."
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
   "lines": "2054",
   "quote": "This meets the raw 95% slice threshold but fails the methodology/type-floor gate because MCQ_SET is 8/9 = 88.89%."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
   "lines": "80",
   "quote": "- Log every candidate, validation reason, selector score, selected index, model, qtype, row id, and final content hash."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
   "lines": "146",
   "quote": "- Every dynamic run writes `retrieval_manifest.jsonl`, proving per row how many curriculum facts, local constraints, source docs, question-bank examples, and few-shots were used."
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_saq.md",
   "lines": "39",
   "quote": "- Scoring criteria are concrete enough to grade consistently — describe what makes an answer correct, don't dictate the exact answer."
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_saq.md",
   "lines": "73",
   "quote": "4. **Ambiguous scoring.** \"Acceptable answers should be reasonable.\" → Useless. Replace with \"Acceptable answers identify [type of factor] and explain [type of mechanism].\""
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pipeline_status_2026-05-18.md",
   "lines": "154",
   "quote": "3. SAQ scoring notes should avoid hallucination-prone evidence lists."
  },
  {
   "truth": 56,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
   "lines": "209",
   "quote": "SAQ sample responses were too generic to be scorer-facing."
  },
  {
   "truth": 56,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
   "lines": "225",
   "quote": "- SAQ repair now emits concrete scorer-facing examples by topic, such as Jay's Treaty, Neutrality, XYZ, and Quasi-War for foreign-policy differences."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/PIPELINE_WRAPPER_ACTION_PLAN.md",
   "lines": "108",
   "quote": "- Few-shot for format only, not factual hallucination."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md",
   "lines": "55",
   "quote": "**Do NOT fabricate quotes or sources.** If you don't know a verifiable source, drop the stimulus and write a non-stimulus item."
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq_set.md",
   "lines": "74",
   "quote": "- The set fails if ANY single question fails any metric."
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Documents/aptraining/analyzer/reports/production_surface_40d.md",
   "lines": "25",
   "quote": "Pattern: a fix aimed at one cell kills that cell and never repairs the chronically-broken one."
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Documents/aptraining/analyzer/.agent/MEMORY.md",
   "lines": "42",
   "quote": "fewshot_bank = v43soup + v52b + their own outputs."
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md",
   "lines": "809",
   "quote": "- Next MCQ_SET attempt needs stronger content construction, not another wording-only leak warning."
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/WINS_20260514.md",
   "lines": "104",
   "quote": "- The wrong move is another broad instruction."
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pil_monitor/inbox/2026-05-19T1456Z_den_unit1_trap_verifier.md",
   "lines": "25",
   "quote": "These are deterministic trap failures. Retrieval and prompting can reduce them, but a verifier can catch them cheaply."
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pipeline_status_2026-05-18.md",
   "lines": "178",
   "quote": "2. Split schema normalization from content generation so unsupported fields cannot leak."
  },
  {
   "truth": 67,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/a0f_validator_probe_20260519.md",
   "lines": "42",
   "quote": "The visible deterministic rules catch the obvious defects but cannot reliably identify the evaluator's latent concerns without damaging passed controls."
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq_set.md",
   "lines": "86",
   "quote": "3. **Stimulus too thin**: 30-word stimulus + 4 questions = no question can actually require it. Match stimulus depth to set size."
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
   "lines": "171",
   "quote": "- rubric must match prompt scope;"
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
   "lines": "224",
   "quote": "- LEQ repair is topic-specific instead of using a generic regional-economic rubric."
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
   "lines": "23",
   "quote": "The version numbers are not monotonic improvements. Treat every version as a measured hypothesis."
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/.openclaw/workspace-incept/memory/ap-benchmark-context.md",
   "lines": "48",
   "quote": "diagnose → fix one thing → commit → retest → check regression → repeat until 98%"
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/full150_y4axbi4f/RESULTS.md",
   "lines": "12",
   "quote": "After retrying all 25 initial score-error rows with a longer single-row timeout:"
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/WINS_20260514.md",
   "lines": "245",
   "quote": "- Per user direction, the long IB run was stopped and treated as grader instability rather than a pipeline result."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md",
   "lines": "101",
   "quote": "- No metadata in the student-visible fields hinting at the correct answer."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md",
   "lines": "50",
   "quote": "Map labels should be names/regions only; descriptors cause reading-comprehension leaks."
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md",
   "lines": "62",
   "quote": "Pairwise stem cosine catches redundant child questions."
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/B0045_STAGED_MCQSET_INTERIM_20260519.md",
   "lines": "24",
   "quote": "passed rows have balanced distractors, historically accurate content, concise stimulus use, and distinct child-question jobs."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md",
   "lines": "203",
   "quote": "- Real source of (1)/(2) export 81.6% baseline is `/v1/apush-all-units-generator` (every item id starts `apush-all-units-`)."
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md",
   "lines": "76",
   "quote": "- **Rule:** every recommendation requires ≥3-seed evidence before shipping a packet."
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/unit1_workflow_v2_branch_result_20260525T093757Z.md",
   "lines": "74",
   "quote": "- Local IB treated that as evaluation-gaming and zeroed DBQ."
  }
 ]
}
```
