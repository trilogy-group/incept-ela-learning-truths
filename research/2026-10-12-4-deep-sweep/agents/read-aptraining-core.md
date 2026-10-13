# read:aptraining-core

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "aptraining-core",
 "coverage": {
  "read": [
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining top-level .md: AGENTS.md, CLAUDE.md, EXPORT_README.md, RESTART_README.md, THELOOP.md (full), THELOOP_CURRENT_STATE.md",
   "aptraining/handover/ — all 17 documents (full handover, shadow session end, data/quill, oracle x3, compass x4 incl. R42 CoVe spec and R41D stats spec + bugfix, atlas, main session close x3)",
   "aptraining/coordination/ — HANDOVER.md, OWNER.md, RESULTS.md, scripts/SHIP_PRECONDITIONS.md, scripts/SHADOW_DIED.md, clone/CLONE_MAIL.md, clone/results/*.md, .archive/*.md (7), .archive/cloud_directives/*.md (2)",
   "aptraining/agents/ — all 10 NORTH_STAR/README docs (operational only; every learnings/ and state/ folder is empty)",
   "aptraining/memory/ — all 7 files",
   "aptraining/apllm-history/ — README.md; module and function docstrings of main.py, apush_all_units_generator.py, all_units_retrieval.py; runtime_assets/curriculum_facts_bundle_v1/README.md; runtime_assets/ib_satisfaction_kit_v1/failure_mode_index.json (head)",
   "aptraining/artifacts/ — INDEX.md, INCLUSION_CRITERIA.md, MONITORED_PATHS.md; every .md under validated/, second_tier/, quarantine/, pending_review/ (incl. EXPLOIT-002..005, RUBRIC_BLINDSPOTS, FINAL_REPORT); _self_improvement (1), _sla, _cost_ledger; _logs/watcher_replay_dupes .md copies (EXPLOIT-001, EXPLOIT_CATALOG, v87 verdict, calibration status, den deliveries); acceptance summary JSONs; first 3 records only of the two validated acceptance JSONL files",
   "aptraining/helpers/ — README.md; shadow: SHADOW_HANDOFF.md, CHANGELOG.md (scanned), CLAUDE.md (scanned), audits/v35_pressure_test/feedback_v35_within_noise.draft.md, audits/deployments_2026_04_29/STRICT_PRACTICES.md (keys redacted on read), output/analytics.md, output/2026-05-27T2130Z course check, output v93 re-audits (2), output/data_agent_v020_field_test_feedback.md, output/STATUS.md, ib_satisfaction_kit_v1 README + curriculum_context_template + generator_prompts/common_pre_checklist + system_prompt_dbq (scanned) + raw_rubrics/_base_evaluation.txt (full), mcq_evaluation.txt (sections), dbq_evaluation.txt, mcq_set_evaluation.txt/saq/leq (scanned), drafts/C009 + self_heal + poke",
   "helpers/data — .agent/LESSONS_LEARNED.md, .agent/MEMORY.md, .agent/memory/data_quirk_apwh_period_table.md, .agent/memory/feedback_check_score_phase_duration.md; output/postmortem_v89_v90_v91.md, output/forensics/*.md (3), output/ib_pass_criteria_pack/README.md, output/CURRICULUM_DATA_INVENTORY.md, output/curriculum_kc_period_audit.md, output/d13_corpus_v5_inventory.md, output/v93_data_inventory.md, output/99stack_layer4_repair_spec.md, output/fewshot_bank/README.md, output/fact_lookup_for_generation/README.md, output/eval/build_notes.md, output/path_e/path_e_build_notes.md, output/t5_dbq_stem_template.md, output/v18_rebuild_scope.md (parts), d13_atlas_batches drops; scanned v29_curriculum_recipe, q3 plan, d13_dbq_corpus_pipeline_spec, anchor_pool_widening_spec, perfect_dpo audit, v52 build notes, v92_proposal, incept-curriculum README; module docstrings of ~35 data scripts",
   "helpers/serve — module docstrings of all 22 scripts; runs_calibrate_gemini_vs_ib*/calibration_summary.json (2); reports/e2e_v97_live summary.md + summary_corrected.json",
   "aptraining-crystal-copy-20260521 — README, START_HERE_FOR_PARALLEL_AGENT, TASK_PROMPT_FOR_NEW_AGENT, FULL_COPY_MANIFEST; evidence/ (RUN_MODE_TAXONOMY_AND_GATES, LAB_RECONCILIATION, FUTURE_RUN_IMPROVEMENT_BACKLOG); variant-calibration-lab-snapshot/ (KNOWN_ISSUES, RUN_LABEL_POLICY, cross_draw_summary, gemini_selector_calibration_final, next_live_run_prep, run_0506c1fd_v2_final_variety_static, run_afcf4245 failed analysis, trend, system_improvement_status, system_improvement_brainstorm (part), v91 plan, handoff XDRAW measurement, live export analysis (part), HOW_TO_ANALYZE/PIPELINE scanned)",
   "crystal full-copy/parallel-ideas-lab/reports (exist only in snapshot): SELECTOR_CALIBRATION_TAKEAWAYS_20260520, DBQ_GAP_ANALYSIS, dbq_structural_zero, a0f_completed_failure_map_20260520 (part), CANDIDATE_CALIBRATION_AND_149_GATE_20260520, PASS_RATE_RECOVERY_PLAN_20260520 (scanned), IB_A0F_99_RECOVERY_PLAN_20260519 (part), WEEKLY_APUSH_PIL_REPORT_20260520 (part)",
   "crystal full-copy/aptraining-root (exists only in snapshot): achieved.md (part), v38_decision_rules.md, READY_FOR_[name]_2026_05_16T0226Z_GRADER_DOWN.md; scanned HANDOVER_SESSION_END_2026-05-19, MODEL_TRAINER_RESPONSE_2026_05_14, READY_FOR_[name]_2026_05_16T1525Z_FINAL_3SEED_VERDICT; den-of-ideation/reports: MASTER_SYNTHESIS.md (key sections), ap_social_studies_generator_distilled.md, k_12_social_studies_distilled.md; full-copy/aptraining-parent/.agent/memory/auto/research_parallel_team_takeaways.md"
  ],
  "skipped": [
   "Secrets and credentials never opened: aptraining/.aptraining_secrets.env, secrets.env.template, crystal private-runtime/, crystal full-copy/aptraining-parent/.local-secrets and .agent/credentials/synapse_tokens.env",
   "Data dumps: every *.jsonl beyond 3 records, *.json.gz bundles, candidate_bank.json (1.2 MB), system_prompts.json (168 KB), pass/fail exemplar JSONL, criterion_frequency.json, crystal downloads-runs/ (2.1 GB), crystal benchmarks/*.jsonl, crystal runs/, helpers/serve runs_* outputs, all logs (agents/*/logs, artifacts/_logs/*.log, poll and eval logs)",
   "Code bodies (documents and docstrings only): helpers/serve and helpers/data script bodies, coordination/scripts/*.sh, aptraining/parallel-ideas-lab/prototypes (app code only; this folder holds no documents in the current tree), crystal variant-calibration-lab-snapshot/scripts and bon/",
   "helpers/data docstrings: about 120 of 156 scripts are iCloud placeholders and reads stalled (one background extraction hung and was stopped); only about 35 docstrings were extracted",
   "Agent scaffolding with no learning-content findings: helpers/*/.agent (AGENT, KNOWLEDGE_PACK, PATTERNS_CATALOG, TOOLS, SOUL etc.), shadow BOOTSTRAP/AGENTS; the root .agent/ and workspace/ folders are outside this direction's scope",
   "Not reached for time: crystal full-copy/services-ib-generator, most of crystal full-copy/aptraining-root (workspace comms, .agent memory, other READY_FOR_[name] and SCALE_UP files), crystal request_trace/ (4 small files), den-of-ideation ml_learnings_distilled / parallel_ideas_lab_structural_takeaways / agentic_development_* / synapse_meeter reports, crystal parallel-ideas-lab top-level docs (HANDOVER_PARALLEL_IDEAS, WINS_20260514, MAIN_AGENT_ACTION_PACKET, PIPELINE_WRAPPER_ACTION_PLAN), remaining raw rubrics (classifier, math_extraction, stimulus extraction prompts)"
  ],
  "notes": "Every evidence path sits under the account's home folder, whose name is a person's name; no path component below the home folder names a person, so name_bearing_source is false throughout. Quotes keep the source's own markdown (asterisks, backticks) exactly. Key flags: (1) The two 'validated' MCQ_SET solver runs (v8, v10 'STRICT FRESH 50/50') counted rows whose rating is PREDICTED_PASS_CACHE_NEIGHBOR with no live grading stage in the audit trail — I read only the first 3 records of each file, so whether all 50 are predicted is unverified; the later '98% Unit-1' memory may rest on such predicted passes. Both runs used the same /tmp/holdout_for_den_v2.jsonl, and heuristics were 'tuned via iterative repair against hidden hold-out'. (2) The judge calibration that 'met' its 0.95 agreement bar was computed on 90 cached all-pass items (kappa 0.0); the resulting '~97.8% IB correlation' was then reused to justify a cheaper judge. (3) Grader versions moved 2.4.0 -> 2.5.3 -> 2.5.6 -> 2.5.7 -> 2.5.11 (one script targets 2.6.6); pass rates across documents are not comparable. (4) Several of the project's own rules were contradicted by its later practice (fallback items accepted as passes, schema repair and per-criterion patching instead of drop-don't-patch, judge criteria text injected into items' notes, image generation for described documents, per-row 'Repair Unit 1 ...' commits tuned on benchmark rows); these appear under 'against'. (5) The goal-tracking eval set reportedly sampled only units 3/6/8. Model-training mechanics (LR, epochs, LoRA, DPO/SFT recipes, deployments) were excluded. No mgr registration was run because this was a read-only research task."
 },
 "candidates": [
  {
   "statement": "Record the grader's version with every score and compare only scores from the same version; the same items moved 25.92 points when the grader version changed.",
   "kind": "measured",
   "found_by": "The same generated items scored 63.64% under one grader version and 89.56% under the next; a later version cut multiple-choice passes from 100% to 70-80% by tightening one dimension.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/coordination/.archive/CLONE_VERIFY_GRADER.md",
     "lines": "12",
     "quote": "- **+25.92pp swing from grader version alone**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/forensics/mcq_v2.5.6_rubric_tightening.md",
     "lines": "6",
     "quote": "v50 r1/r2/r3 v2.5.6: ~30 mcq rows each (76.7%, 80.0%, 70.0% pass on NEW grader)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_main_session_close/02_CONSOLIDATED_STATE.md",
     "lines": "135",
     "quote": "| ONLY IB v2.5.3 | All historical comparisons require explicit grader-version tagging; some \"regressions\" may be artifacts | `feedback_ib_grader_version_v240_to_v253.md` |"
    }
   ],
   "against": "Pinning the version is necessary but not sufficient: \"Same generations re-scored produce 17pp per-cell variance, ~1-2pp aggregate variance.\" (helpers/shadow/output/analytics.md line 12).",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Re-score identical items several times to find the judge's noise floor, and treat any difference smaller than that floor as no difference.",
   "kind": "measured",
   "found_by": "Re-scoring the same outputs swung per-type pass rates by up to 17 points; deterministic generation still disagreed on 6 of 30 items across seeds; a 'best variant' chosen on one draw flipped on the second.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/analytics.md",
     "lines": "12",
     "quote": "Same generations re-scored produce 17pp per-cell variance, ~1-2pp aggregate variance."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/forensics/mcq_seed_variance_diff.md",
     "lines": "5",
     "quote": "v50 mcq seed σ = 5.09pp at T=0 (should be 0 if deterministic)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/KNOWN_ISSUES.md",
     "lines": "260",
     "quote": "**Symptom**: LEQ exam_precision pass rate was 0.87 on one draw, 0.73 on another. Single-draw \"LEQ exam_precision is best\" claim was wrong."
    }
   ],
   "against": "Aggregates can look steady while item types swing: \"Variance σ < 1pp across seeds — stable, reproducible measurement.\" (crystal full-copy/aptraining-root/achieved.md line 83).",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Decide between two versions item by item on the same items, using the continuous score and a paired test; a pass-rate gain can turn out to be a loss when scored that way.",
   "kind": "measured",
   "found_by": "A +1.77-point pass-rate gain was a -0.88 drop on the continuous score; a +1.33-point 'lift' rested on only 12 of 150 items changing, split 5 against 7 (p = 0.77).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_main_session_close/02_CONSOLIDATED_STATE.md",
     "lines": "137",
     "quote": "| Switch to continuous metric | DBQ \"noise\" revealed as ~all threshold artifact; v36b binary +1.77pp = continuous -0.88 | `feedback_r41d_continuous_metric.md` |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/audits/v35_pressure_test/feedback_v35_within_noise.draft.md",
     "lines": "21",
     "quote": "- Paired McNemar on the same 150 APUSH prompts under the same canonical grader (IB v2.5.3): b=5 (v29-only passes), c=7 (v35-only passes), exact two-sided p = **0.7744**."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/03_R41D_implementation.md",
     "lines": "28",
     "quote": "| M1 | Card, Henderson, Khandelwal, Jia, Mahowald, Jurafsky. *With Little Power Comes Great Responsibility.* EMNLP 2020. | NLP benchmarks routinely under-powered; advocates continuous metrics + paired tests over binary accuracy at small n. Direct fit for our n=30 per cell. |"
    }
   ],
   "against": "Small effects still need many items: \"5. **Power note:** at n=30 per cell and observed SD ≈ 0.15, paired-t detects Δ ≥ ~0.05 with 80% power. Smaller effects need n≥120 per cell — relevant if you want to distinguish CoVe from no-op at 1pp lift.\" (03_R41D_implementation.md line 440).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Before comparing two versions, compare one version with itself; any 'significant' difference in that self-comparison means the measuring setup is broken.",
   "kind": "adopted rule",
   "found_by": "Written into the paired-comparison protocol as the required smoke test before any real comparison is run.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/03_R41D_implementation.md",
     "lines": "449",
     "quote": "4. Smoke test: compare v29 baseline against itself with a different seed run. Expect `per_cell.*.significant_at_alpha == false` everywhere; `mean_diff_overall ≈ 0`. If false-positives appear under self-comparison, the pairing key is wrong — check (row_id, cell) keying."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Regenerate and re-score the baseline under the same conditions as the new version; comparing new output with stored old output made gains look like regressions.",
   "kind": "measured",
   "found_by": "Comparing fresh output against frozen baseline generations reversed the direction of several comparisons once the baseline was regenerated.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_main_session_close/02_CONSOLIDATED_STATE.md",
     "lines": "138",
     "quote": "| Fresh baseline rule | Several \"regressions\" reverse to \"real lifts\" with proper baseline | `feedback_baseline_must_be_fresh_gen.md` |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/coordination/HANDOVER.md",
     "lines": "102",
     "quote": "7. Fresh-gen baseline for continuous comparisons"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Act on a quality number only if it traces to a stored result file from a run that really generated and scored the items; one cited collapse came from a run that took 8 ms on empty prompts.",
   "kind": "measured",
   "found_by": "A 'catastrophic' score drove a strategy pivot but its only result file showed 0/150 in 8 ms with empty prompts; a baseline figure was cited across five-plus memos with no file behind it; a single lucky run was celebrated as a breakthrough.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_main_session_close/01_HANDOVER.md",
     "lines": "66",
     "quote": "- The only v39 summary file shows 0/150 with **8ms elapsed** — eval never actually ran"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_main_session_close/01_HANDOVER.md",
     "lines": "68",
     "quote": "- Eval harness was sending **empty user prompts**, model responded with chatbot fallback"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/THELOOP.md",
     "lines": "753",
     "quote": "1. **Shadow T8 phantom** (2026-05-06T0005Z) — v29 baseline 0.8667 was being cited across 5+ memos including v42/v40h FINAL verdicts; citation trail terminated at \"historical\" with no on-disk file at canonical schema."
    }
   ],
   "against": "A missing file does not prove the claim false: \"**Reality:** the only v39 summary in `workspace/eval/runs/` does show 0/150 with 8ms elapsed — true. But the regression IS real per 0758Z REFRESHER (\"v39 catastrophic, v40 empty outputs, both auto-deleted by Fireworks\").\" (handover/2026-05-01_session_end/SHADOW_HANDOVER.md line 127).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Sort every failed item into infrastructure, format, content or variety failure before computing a pass rate; timeouts, auth errors and unparsed outputs are missing evidence, not bad items.",
   "kind": "measured",
   "found_by": "4,800 authentication failures were recorded as per-item scoring errors; auto-zeroed scoring errors pulled one item type 26.7 points below a parallel run; grader timeouts marked items 0.0 that had already passed.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/.agent/memory/feedback_check_score_phase_duration.md",
     "lines": "29",
     "quote": "The script masked this as per-row scoring errors (`ib_overall=None`, `ib_hard_fails=[\"ib_http_401\"]`) instead of aborting on systemic failure."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/coordination/RESULTS.md",
     "lines": "71",
     "quote": "**mcq_set diverges by -26.7pp** in clone's run — driven by `n_score_err=29/150` in clone's scoring pass, almost certainly concentrated on mcq_set (avg_overall=0.179 implausibly low otherwise; auto-zeroed errors deflate that cell)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/SELECTOR_CALIBRATION_TAKEAWAYS_20260520.md",
     "lines": "28-29",
     "quote": "- Evidence: first calibration smoke marked DBQ as 0.0 because local IB timed out, while existing winner scores showed the same rows passed."
    }
   ],
   "against": "Format failures still count against what is delivered: \"8. OpenAPI shape must be enforced at the boundary.\" (crystal full-copy/parallel-ideas-lab/reports/WEEKLY_APUSH_PIL_REPORT_20260520.md line 498).",
   "adds_to_existing": [
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before crediting a change with a gain, check that the change visibly happens in the outputs; one claimed gain came from a change that appeared in none of 297 outputs.",
   "kind": "measured",
   "found_by": "A new generation mechanism was declared the new best on a +1.33-point lift; a scan found zero of 297 outputs used it, and the lift was within noise.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/audits/v35_pressure_test/feedback_v35_within_noise.draft.md",
     "lines": "22",
     "quote": "- All 297 v35 generations under vanilla `oneshot_generate.py`: zero `[Retrieval=...]`, zero `[IsRel=...]`, zero `[IsSup=...]`, zero `[IsUse=...]`, zero `<paragraph>...</paragraph>`."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_main_session_close/02_CONSOLIDATED_STATE.md",
     "lines": "86",
     "quote": "| **v35 Self-RAG SFT** | 92.26% / 89.33% APUSH on canonical (looked like +1.33pp lift) | **RETRACTED** — McNemar p=0.7744, 0/297 reflection-token emission, mechanism never fired | Self-RAG vocab-extension is non-optional; \"lift\" was grader noise + threshold artifact |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/02_R42_CoVe_DBQ_spec.md",
     "lines": "140",
     "quote": "Log the `stage` (`revise` / `draft_fallback` / `no_block`) per item in the score record so we can quantify how often the verification phase actually fired."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Re-test every claimed improvement yourself on fresh items its author never saw; self-reported results on chosen items overstated pass rates by 10 to 87 points.",
   "kind": "measured",
   "found_by": "A claimed 95.56% fell to 10% on fresh items; other self-tests dropped 100%->64% and 87.5%->0% on an independent hidden set.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/quarantine/2026-05-22T1755Z_den_mcqset_50_50_proof/QUARANTINE_REASON.md",
     "lines": "4-5",
     "quote": "**Independent re-test:** 5/50 = **10.00%** on Unit-1 prompts from e7e1d980 (no overlap with den's 30-prompt training set)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/quarantine/2026-05-22T2120Z_cheater_exploit_003/QUARANTINE_REASON.md",
     "lines": "37",
     "quote": "| Cheater EXPLOIT-003 (phrase-anchor MCQ_SET) | 14/16 = 87.5% | 0/10 partial = 0% (**QUARANTINE**) |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/INCLUSION_CRITERIA.md",
     "lines": "24",
     "quote": "Cherry-picked subsets, single-prompt wins, and self-reported metrics from sub-agents do NOT qualify."
    }
   ],
   "against": "Some drops were modest: \"| Den v2/v3 (cache) | 43/50 = 86% | 37/50 = 74% (second_tier) |\" (same quarantine file, line 33); and the independent re-tests themselves later counted predicted passes (see the predicted-pass candidate).",
   "adds_to_existing": [
    48,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count a pass only when the real judge scored the item actually delivered; a score predicted from similar past items, a cached verdict or a fallback item is not a pass.",
   "kind": "measured",
   "found_by": "A run promoted as '100% strict fresh' has records whose rating is a prediction from cached neighbours with no live grading stage in the audit trail; an earlier '100%' included 4 fallback items; a cache-backed solver's pass rate equalled its cache hit rate.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/VALIDATION_REASON.md",
     "lines": "5",
     "quote": "**Verdict:** 50/50 = **100.0% STRICT FRESH** — zero timeout-fallback, all v80bchain fresh generation"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/den_solver_acceptance_20260523T082319Z.jsonl",
     "lines": "1",
     "quote": "\"ib_score\": 0.95, \"ib_rating\": \"PREDICTED_PASS_CACHE_NEIGHBOR\""
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1830Z_den_solver_v2_online_K_N_with_cache/SECOND_TIER_REASON.md",
     "lines": "39",
     "quote": "Effective behavior: high pass rate ONLY for substandards the cache has seen before; cap_reached for novel substandards. Pass rate ≈ cache hit rate."
    }
   ],
   "against": "The project argued fallback passes were acceptable: \"main-a recommends YES — the cached archetype is itself derived from live-IB-validated v80bchain content, so it's not \"deterministic-from-bank\" in the prior sense.\" (artifacts/validated/2026-05-22T2116Z_den_solver_v8_FIRST_VALIDATED/VALIDATION_REASON.md line 62). Only the first 3 records of each acceptance file were read.",
   "adds_to_existing": [
    24,
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep held-out items truly unseen: never tune repairs against them, never reuse the same set round after round, and keep them out of any cache or pool the generator can consult.",
   "kind": "measured",
   "found_by": "Per-type heuristics were tuned by repeated repair against the hidden set; the same hold-out file fed successive validations; cache hits came from the same earlier pipeline run the hold-out was drawn from.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/memory/project_den_routing_98pct_unit1_2026_05_24.md",
     "lines": "51",
     "quote": "- Per-cell heuristics tuned via iterative repair against hidden hold-out"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/den_solver_acceptance_20260523T082319Z_summary.json",
     "lines": "13",
     "quote": "\"input_jsonl\": \"/tmp/holdout_for_den_v2.jsonl\","
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1830Z_den_solver_v2_online_K_N_with_cache/SECOND_TIER_REASON.md",
     "lines": "50",
     "quote": "37 passes = substandards in cache from prior runs (e7e1d980 pipeline outputs)."
    }
   ],
   "against": "Fresh sets differ in difficulty, so a fresh set must match the target mix: \"Holdout prompts are systematically harder.\" (crystal full-copy/aptraining-root/achieved.md line 69).",
   "adds_to_existing": [
    48,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Calibrate a judge on a sample with known failures as well as passes, and report chance-corrected agreement; 97.8% agreement on an all-pass sample had a kappa of 0 and showed nothing.",
   "kind": "measured",
   "found_by": "A cheaper judge 'met' a 0.95 agreement bar on 90 cached items that had all passed (no true negatives, kappa 0.0), and that figure was then quoted as the judge's correlation; a model labeller gave the top score to 99.6% of items.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/serve/runs_calibrate_gemini_vs_ib_after_swap/calibration_summary.json",
     "lines": "7",
     "quote": "\"kappa\": 0.0,"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/serve/calibrate_gemini_vs_ib.py",
     "lines": "4-5",
     "quote": "Uses the 90 Cheater Layer 1 cached items as the calibration sample (each has authoritative IB v2.5.11 score from build-time)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/analytics.md",
     "lines": "140",
     "quote": "| IsUse 5/4 | 962/4 ⚠ 99.6% degenerate-at-5 (gpt-4o-mini ceiling) |"
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
   "statement": "Make the judge fail an item that leaves out a part its type requires; checks that run only when the part is present let items pass by leaving it out.",
   "kind": "measured",
   "found_by": "A red-team found the judge's toughest checks only ran when a source text was present; stripping the source took a generator from 68% to 100% and a deliberately mid-quality hand-made batch to 30/30, and the same move transferred to short-answer and essay items.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/EXPLOIT-002-stimulus-strip.md",
     "lines": "20-21",
     "quote": "EXPLOIT-002 via v80b lifts **v80b from 68% → 100%** (+32pp) on a 32-item batch."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/RUBRIC_BLINDSPOTS.md",
     "lines": "16-18",
     "quote": "For APUSH MCQs, the curriculum data does **not** carry that flag, so Mode C applies and \"no stimulus = PASS\" — even though every real AP US History MCQ includes a primary-source stimulus."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/pending_review/2026-05-23T000424Z_exploits_EXPLOIT-004-saq-no-stimulus/source_report.md",
     "lines": "5",
     "quote": "**Pass rate**: **34/34 = 100%** on n=34 items (17 distinct APUSH SAQ KCs × 2 variants) via v80bchain (avg overall score **0.994**)"
    }
   ],
   "against": "On fresh items the source-free version passed 90%, not 100% (\"- **n_pass / total**: 45 / 50 = **90.00%**\", second_tier/.../cheater_validation_verdict.md line 3), and source-free items are legitimate for drills: \"- **Stem-only review-drill products**: explicit non-exam-format MCQs (no stimulus) for AP-prep practice apps, where the IB grader rubric matches the product shape.\" (SECOND_TIER_REASON.md line 19); the project's own generator checklist said \"- [ ] If unsure of a source — drop the stimulus, write a non-stimulus item\" (common_pre_checklist.md line 24).",
   "adds_to_existing": [
    33,
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge the task itself, not what the item's own notes or explanation claim about it, and don't let the judge's narrative overturn a failing check; scripted rationales and listed 'features' bought passes.",
   "kind": "measured",
   "found_by": "A rule that flips a 0 to 1 when the judge's written reasoning says 'correct' let a templated explanation steer the verdict; listing two opposing theses in an item's notes earned credit for 'multiple defensible positions'.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/RUBRIC_BLINDSPOTS.md",
     "lines": "51-55",
     "quote": "But because the judge writes reasoning BEFORE the score is applied, a template-driven explanation that prefills the judge's reasoning toward \"content is correct\" will force the score to 1.0 even when the judge's gut would have failed it."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/pending_review/2026-05-23T082229Z_exploits_EXPLOIT-005-leq-no-stimulus/source_report.md",
     "lines": "95-97",
     "quote": "\"Multiple defensible positions\" currently passes if rubric_notes literally lists two opposing thesis sentences."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/apllm-history/runtime_assets/ib_satisfaction_kit_v1/failure_mode_index.json",
     "lines": "13",
     "quote": "\"fix\": \"Don't argue 'this should pass'; just generate content\""
    }
   ],
   "against": "Explanations themselves are allowed: \"Genuine educational explanations in answer/rationale fields are NOT violations.\" (helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt line 29); the project itself wrote the judge's criteria into items' notes: \"- DBQ: rubric_notes = IB DBQ criteria text; additional_details = top-3 misconceptions; image_url = \"[]\"\" (helpers/data/build_u1_maximal_corpus_v6_curriculum_enriched.py line 15).",
   "adds_to_existing": [
    12,
    30
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge how much thinking a task demands from what it actually requires, not from its command verb; swapping in an analytical verb passed with no added demand.",
   "kind": "measured",
   "found_by": "Short-answer items passed the judge's analytical-thinking checks just by opening with 'Explain one way'; the judge also treated 'describe'/'identify' as recall regardless of context.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/pending_review/2026-05-23T000424Z_exploits_EXPLOIT-004-saq-no-stimulus/source_report.md",
     "lines": "27-29",
     "quote": "Using \"Explain ONE way\" hits the analytical sweet spot on the rubric's wording without any actual increase in cognitive demand."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt",
     "lines": "88",
     "quote": "Verbs like *evaluate / claim / analyze / explain / justify* in the question stem do **not** rescue the item — they describe the cover, not the actual cognitive demand."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md",
     "lines": "159",
     "quote": "- “Describe” and “Identify” verbs were treated as recall even when surrounded by analytical language."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    10
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check that a student with no subject knowledge cannot reach the answer from wording alone — by matching the source to an option, naming what the source describes, or ruling out absurd options.",
   "kind": "measured",
   "found_by": "Items whose source paraphrased the keyed option failed half the time (5/10 on this check); the judge's no-knowledge probe was skipped when no source was present, which let weak option sets through.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt",
     "lines": "76",
     "quote": "Working only from the stimulus (including any image-analysis content) and the question stem, attempt to pick the correct answer step by step."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/_logs/watcher_replay_dupes_20260522T2018Z/2026-05-22T201819Z_exploits_EXPLOIT-001-historian-frame-self-leak/source_report.md",
     "lines": "32-34",
     "quote": "1. **Vocabulary / paraphrase leak.** The judge's zero-knowledge counterfactual probe (per `_base_evaluation.txt` Checklist B1) found that the abstract historian claim word-matched one option:"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/RUBRIC_BLINDSPOTS.md",
     "lines": "37-40",
     "quote": "**Patch:** for closed-form history MCQs without a stimulus, add a stem-only variant of the probe that asks \"could a student with no APUSH knowledge eliminate three of these four options purely from common-knowledge / lay-vocabulary reasoning?\"."
    }
   ],
   "against": "The probe does not apply to reading items, where the text is the point: \"- **Skip the probe entirely** when: `request.subject` is ELA / reading / language-arts; the content type is `nonfiction_reading` / `fiction_reading` / `article` (those *are* reading-comprehension by design); or no stimulus is present.\" (_base_evaluation.txt line 80).",
   "adds_to_existing": [
    3,
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Build source-based items from real documents copied verbatim with true attribution and supplied at generation time; never let the writer invent, paraphrase or describe a source.",
   "kind": "measured",
   "found_by": "Generated 'documents' that were invented or described absent artifacts scored 0% on document-based items; supplying real retrieved documents lifted them from 67% to 87.9%, the largest measured gain; an older corpus had real attributions attached to unverified text.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md",
     "lines": "111",
     "quote": "The contrast is the whole story: normal generation without real source injection sits at DBQ 0%; D13 source injection immediately produces non-zero DBQ, but the current naive retrieval/prompting still fails often."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/d13_corpus_v5_inventory.md",
     "lines": "68",
     "quote": "Pipeline-on-v80b uses this and scores **87.9% DBQ** (vs 67% v80b standalone)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/v18_rebuild_scope.md",
     "lines": "15-17",
     "quote": "D8b confirmed plausible-but-fictional content (real attributions, unverified text) — fine for ≤95% but the floor at 99%."
    }
   ],
   "against": "Real sources were necessary but not sufficient: \"The full D13 hot-patch reached only 33.3% and still had 64% `stimulus_quality` zero-rate, so token-overlap + unit bonus is not enough for 97%.\" (dbq_structural_zero.md line 137); the live service generated images from described documents: \"This turns the model's prose description into an actual visual artifact the IB grader can score.\" (apllm-history/main.py lines 532-533); a criteria pack advised \"Use authentic primary-source language patterns, period-correct vocabulary, plausible attribution lines (author/date/source citation).\" (helpers/data/output/ib_pass_criteria_pack/README.md line 23).",
   "adds_to_existing": [
    57,
    17,
    64
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before using a fetched source text, check it is the complete text — not a landing page, a metadata stub, a length-capped excerpt or a page wrapped in library boilerplate.",
   "kind": "measured",
   "found_by": "A fetcher cut every text at exactly 50,000 characters (losing 85-96%) and kept library preambles, rejecting 5 of 6 rows; 109 of 109 links from one library were landing pages; 556 of 648 newly ingested documents were metadata only.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md",
     "lines": "43",
     "quote": "**F-D13-13**: all 6 rows truncated at exactly 50,000 chars, losing 85-96% of fulltext."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/SHADOW_HANDOFF.md",
     "lines": "36",
     "quote": "D13 pipeline broken (322/761 LoC URLs Cloudflare-blocked, 109/109 Gutenberg URLs are landing pages)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/d13_corpus_v5_inventory.md",
     "lines": "28",
     "quote": "- v3 has 648 docs: **92 fulltext + 556 metadata_only** (LoC frequently has metadata but not transcribed fulltext for newer/obscure items)"
    }
   ],
   "against": "Hashing proved the files unchanged but not complete: \"- **D13 U1 SHA256 staging held up.** 8 docs, content-hashed, no re-fetch needed.\" (handover/2026-05-01T1039Z_data_session/HANDOVER.md line 275).",
   "adds_to_existing": [
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "File each source under the period it was created in, not the period it mentions, and check every period label against the source's date in code.",
   "kind": "measured",
   "found_by": "A tagger that filed sources by topic association mislabelled 79% of one unit (mostly later commemorations); a date audit quarantined 211 gross mislabels and still found 23 near-boundary ones.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md",
     "lines": "39",
     "quote": "U4 LoC 96-row topic cluster. **79% era-mistag** (76/96 dates outside 1800-1860, mostly 1904 Louisiana Purchase Expo commemoratives). **F-D13-12** = era-tagger doing semantic-association not date-of-creation."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/2026-05-22T2308Z_v93_phase3_reaudit_VERDICT_ADJUST.md",
     "lines": "28",
     "quote": "- **0 gross anachronisms** (>50-year mismatch) — the 211 gross violations were successfully quarantined."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/2026-05-22T2308Z_v93_phase3_reaudit_VERDICT_ADJUST.md",
     "lines": "29",
     "quote": "- **23 subject-level anachronisms** remain (±20-year or subject-obvious mismatches)."
    }
   ],
   "against": "Later documents about an earlier period were kept by subject: \"- **Commemorative/meta docs** (Brown v. Board 2015–2024, Pearl Harbor 1973–1995 in Unit 7/8) are date-mismatched but **subject-correct**; excluded from the 23 count because the content is about the tagged unit's era.\" (same file, line 42).",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Audit the knowledge base's own labels in code before generating from it; facts sat in units whose period they fall outside, a period table off by one unit made requests contradict themselves, and most of one build's standard IDs were invalid.",
   "kind": "measured",
   "found_by": "A sweep of the curriculum facts flagged 76 facts dated outside their unit's window; a period table produced a prompt whose objective and stated period disagreed; a training build had 77.5% non-canonical standard IDs that passed row-count checks.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/curriculum_kc_period_audit.md",
     "lines": "8",
     "quote": "- **76 KCs** flagged as period-mismatched."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/.agent/memory/data_quirk_apwh_period_table.md",
     "lines": "28",
     "quote": "Concrete observed failure: an apwh/leq Unit 6 prompt had `LEARNING OBJECTIVE: Explain how the development of new technologies changed the world from 1900 to present` paired with `TIME PERIOD: c. 1750 to c. 1900 (STRICT -- nothing outside this range)`."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01_session_end/SHADOW_HANDOVER.md",
     "lines": "59",
     "quote": "| Non-canonical KC IDs | 77.5% (803/1036) use opaque hashes (`c_4EvW`, `s_saxW`); only 14% match `KC-X.Y.Z+N` |"
    }
   ],
   "against": "Automated flags still need human review: \"- `suggested_unit` is best-effort: the unit whose window contains the parsed date range. Manual review still required before any data-side fix.\" (curriculum_kc_period_audit.md line 69).",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Reconcile each knowledge source against the official framework, course by course, before choosing one, and key every standard by course plus ID; two sources for one course had IDs shifted by a period and almost no overlap.",
   "kind": "measured",
   "found_by": "A content comparison found one source's IDs off by one period for a whole course, and for another course 39% of one source and 99.8% of the other had no match; the same ID recurs across courses.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_oracle_session/HANDOVER.md",
     "lines": "343",
     "quote": "InceptBench APEURO IDs off by one period vs CB CED. Curriculum repo IDs match official CB CED."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_oracle_session/HANDOVER.md",
     "lines": "345",
     "quote": "39% of curriculum has no IB match; 99.8% of IB has no curriculum match."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/apllm-history/runtime_assets/curriculum_facts_bundle_v1/README.md",
     "lines": "51",
     "quote": "# Same node_id can exist in multiple courses (e.g. KC-1.1.I.A in APUSH + APEURO)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Audit a source pool's coverage against the curriculum's topics before generating from it; a large pool held one or zero sources for several required topics and leaned heavily on one kind of voice.",
   "kind": "measured",
   "found_by": "Topic scans of a thousand-document source corpus found required topics with one or zero documents, whole units with no documents, and 37% of one unit drawn from a single elite collection.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md",
     "lines": "38",
     "quote": "Slavery/labor = 1 row, Jamestown = 1 row (critical under-rep)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md",
     "lines": "41",
     "quote": "ADST oral histories = 46 rows / 37% (elite foreign-policy skew confirmed)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/d13_corpus_v5_inventory.md",
     "lines": "8",
     "quote": "v3 ingest added **648 new docs** across Units 1/2/4/6/9 (the units missing or sparse in v2), bringing the combined v2+v3 corpus to **1,385 docs / 5.8M chars**."
    }
   ],
   "against": "Coverage counts themselves can mislead: \"False-positive rate documented per-tick (e.g., \"gilded age / labor\" cluster on U6 had 21/34 false-positives = foreign antitrust).\" (atlas HANDOVER.md line 128) and \"## Per-unit aggregate (across all sources, deduplication NOT applied — caveat)\" (helpers/data/output/v93_data_inventory.md line 24).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep every fact in an item — stem, options, sample answers and marking notes — inside the period, region and parts the request names, and check dates in code.",
   "kind": "measured",
   "found_by": "In a 1,080-item run, 41 items were out of period, 21 had sample-answer errors and named anachronism families recurred; marking notes cited a region outside the prompt, and sample answers skipped parts the prompt required.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/next_live_run_prep.md",
     "lines": "25",
     "quote": "**Symptom**: 21 sample_response_error + 41 out_of_period + 39 factual_error + named-content-trap families (`content_lakota_pre1607` 14, `content_muscovy_east_india` 7, `content_navigation_acts` 3, `content_requerimiento_overclaim` 2) = chain hallucinating concrete, name-able anachronisms in Unit 1 content."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md",
     "lines": "45",
     "quote": "- `apush-u1-1505-leq-medium`: LEQ rubric included Northeastern evidence outside a Southwest / Great Basin prompt."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md",
     "lines": "51",
     "quote": "- SAQ answer-key verifier must ensure every requested component appears in the sample responses, not just in the student-facing parts."
    }
   ],
   "against": "A simple year check caught only a fraction: \"- `year_bound.check_leq` catches 1 of 7 LEQ chronology failures (true positive ~14%) and 0 valid candidates (0% FP) — this one is net-positive alone.\" (crystal variant-calibration-lab-snapshot/KNOWN_ISSUES.md lines 135-137).",
   "adds_to_existing": [
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write each wrong option from a misconception students actually hold, in the same category and grain as the key; absurd or anachronistic options are easy to rule out, and a judge may still pass them.",
   "kind": "adopted rule",
   "found_by": "The grader's rubric and the project's criteria pack call for misconception-based options; a red-team showed options that were plainly wrong on the merits still passed every option check.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_evaluation.txt",
     "lines": "288",
     "quote": "- Distractors align with known common misconceptions (especially those from Curriculum API)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/ib_pass_criteria_pack/README.md",
     "lines": "44",
     "quote": "3. **`distractor_quality` MODERATE (decisive=0.070)** — distractors target known misconceptions or common errors, NOT random wrong values."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/EXPLOIT-002-stimulus-strip.md",
     "lines": "70-73",
     "quote": "This pattern automatically satisfies `distractor_quality` and `reveals_misconceptions` default-pass conditions and never triggers the \"borderline-correct\" or \"length-imbalance\" failure modes."
    }
   ],
   "against": "The planned test of misconception-seeded options has no recorded result in the files read: \"4. If +3pp on distractor_quality → fire full 150-mcq replication; recommend production injection\" (helpers/data/output/path_e/path_e_build_notes.md line 42).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Show the writer three to five verified examples of the item type taken from other topics, so it copies the form but not the content; this lifted a 3.3% pass rate to 26.7%.",
   "kind": "measured",
   "found_by": "An A/B on question sets prepended verified examples whose topic differed from the target; pass rate rose 3.3% -> 26.7% and answer-letter balance went from 0 to 30/30.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/serve/fewshot_mcqset.py",
     "lines": "5-7",
     "quote": "for MCQ_SET, sample 3-5 verified exemplars (IB-graded 1.0) from the 669-pool, picking exemplars whose KC DIFFERS from the target KC so the output stays fresh, and prepend them as a TEMPLATE SEED."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/serve/fewshot_mcqset.py",
     "lines": "7-8",
     "quote": "This lifted IB MCQ_SET 3.3% -> 26.7% and fixed answer_balance 0 -> 30/30."
    }
   ],
   "against": "Example banks can make output static: \"DBQ and MCQ_SET had extreme duplicate groups in A0F. Static output can inflate short-slice scores and then collapse on variety/focus.\" (crystal parallel-ideas-lab/reports/WEEKLY_APUSH_PIL_REPORT_20260520.md line 492); and \"- For dense courses like APUSH, too many prompt examples can hurt; prefer exact facts/source packs over long example lists.\" (den-of-ideation/reports/ap_social_studies_generator_distilled.md line 186).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Measure how many distinct items a generator delivers for each item type; one run passed 88% of its document-based items, but only 6 of 216 were distinct.",
   "kind": "measured",
   "found_by": "A fingerprint check of a 1,080-item delivered run found document-based items 2.8% unique and question sets 5.1% unique, because the generator ignored its sampling settings and fell back to fixed templates; several candidates per row were identical.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/run_0506c1fd_v2_final_variety_static.md",
     "lines": "15",
     "quote": "| DBQ | 216 | 88.4% | 6 | 2.8% |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/run_0506c1fd_v2_final_variety_static.md",
     "lines": "27",
     "quote": "- The showcase architecture generated multiple candidates, but the underlying all-units generator was still effectively deterministic because `apush_all_units_generator.call_fireworks()` hard-coded `temperature=0.0` and ignored the showcase profile temperature hints."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md",
     "lines": "62",
     "quote": "Takeaway: K was not producing useful diversity for MCQ_SET in this archive. It produced duplicate payloads. Anti-static guard must treat identical candidates as one candidate, not six chances."
    }
   ],
   "against": "Variety and pass rate trade off: \"- Pass rate may move either direction; this is a quality/variety repair, not a guaranteed score-only patch.\" (run_0506c1fd_v2_final_variety_static.md line 41).",
   "adds_to_existing": [
    65
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Replay any new automatic filter over saved, already-judged items and adopt it only if it costs no passes for any item type; a bundle of plausible filters cut one type from 10/10 to 3/10.",
   "kind": "measured",
   "found_by": "Replaying a filter bundle over 150 saved, graded rows lowered the pass rate from 91.3% to 87.3%; one filter caught no real failures while rejecting valid items, another rejected about 15% of good sets.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/gemini_selector_calibration_final.md",
     "lines": "96",
     "quote": "| mcq_set/hard | 10 | 10/10 | 3/10 | 10/10 |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/gemini_selector_calibration_final.md",
     "lines": "104",
     "quote": "- filter→gemini pass rate (proposed v2 selector): **87.3%**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/KNOWN_ISSUES.md",
     "lines": "129-130",
     "quote": "**Root cause**: the filters in `scripts/filters/*.py` are individually plausible but their bundle over-rejects valid candidates."
    }
   ],
   "against": "Single filters can still help: \"These were measured net-negative when bundled with other filters in my prior replay, but applied alone they recover ~6/40 MCQ_SET candidates that Gemini otherwise picks.\" (variant-calibration-lab-snapshot/next_live_run_prep.md line 65).",
   "adds_to_existing": [
    37,
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Read failure reasons from the judge's structured scores, not by keyword-matching its prose; a pattern match tagged 71 of 72 failures with a fault that wasn't there.",
   "kind": "measured",
   "found_by": "A regex over the judge's narrative matched the name of a check ('Integrity check passed') and tagged 71 of 72 failures; another regex flagged 154 rows for an echo of request metadata, and a 5-row spot check found none.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/KNOWN_ISSUES.md",
     "lines": "107-108",
     "quote": "**Symptom**: 71 of 72 failed rows tagged `integrity_violation`; reading the underlying narrative shows almost none are actual violations."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/KNOWN_ISSUES.md",
     "lines": "110-111",
     "quote": "**Root cause**: my regex matched the *metric name* (e.g. \"Integrity check passed\") in evaluator reasoning text, not actual violations."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/next_live_run_prep.md",
     "lines": "87",
     "quote": "Spot-check of 5 randomly-sampled failed rows showed 0 actually mention \"grade 1\" as a failure cause."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "State with every score which judge and version, how many items, which build and route, and whether it came from a full delivery-mode run; a 149/150 stitched from the best slices of two builds proved nothing.",
   "kind": "measured",
   "found_by": "A '99.33%' result was assembled from the best 50-row windows of two different builds; small calibration slices were being read as proof of 99%; local, partial and live results were being confused.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md",
     "lines": "104",
     "quote": "This is a valid 149/150-style stitched evidence result. It is not proof that current live production is solved because the selected window combines builds `6f0ffdf` and `e429b16`."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/MASTER_SYNTHESIS.md",
     "lines": "135",
     "quote": "- whether the score is official IB, local IB, diagnostic eval, older IB, self-eval, targeted repair, spread sample, or schema-only."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/SELECTOR_CALIBRATION_TAKEAWAYS_20260520.md",
     "lines": "33",
     "quote": "- Evidence: small calibration sets can validate machinery but cannot prove 99%."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24,
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't predict the gain of combined methods or repeated attempts by multiplying their odds as if they were independent; failures cluster by topic, so measure the combination.",
   "kind": "measured",
   "found_by": "Two methods that each helped failed to add up when stacked; a pipeline design assumed five independent attempts would reach 99.66%, while one topic failed all ten attempts.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_main_session_close/02_CONSOLIDATED_STATE.md",
     "lines": "96",
     "quote": "| **Combo routing + RAG** | Failed to compose lifts | `project_combo_routing_plus_rag_failed.md` | Methods correlate; multiplicative stacking is wishful |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/serve/serve99stack.py",
     "lines": "8",
     "quote": "- At K=5 with 68% raw base: P(all 5 fail) = 0.32⁵ = 0.34% → 99.66% per cell from Layer 3 alone"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/pending_review/2026-05-23T082229Z_exploits_EXPLOIT-005-leq-no-stimulus/source_report.md",
     "lines": "54-55",
     "quote": "Tried 2 rounds of K=5 (10 attempts) and never crossed 0.80."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    65,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Run a small fixed smoke set — one item per type plus items from each known failure family — end to end before any full measurement and after every change.",
   "kind": "adopted rule",
   "found_by": "Two builds burned full 150-item grading runs before a format collapse was visible; five deployed changes carried unverified gain claims; recurring failure families kept returning after fixes.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/coordination/scripts/SHIP_PRECONDITIONS.md",
     "lines": "79-80",
     "quote": "A 5-item probe surfaces format collapse, deployment-side breakage, and obvious regressions for ~3% of the cost."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/evidence/FUTURE_RUN_IMPROVEMENT_BACKLOG_20260521.md",
     "lines": "209",
     "quote": "- Convert each family into 3-5 fixed regression prompts."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/system_improvement_brainstorm.md",
     "lines": "25",
     "quote": "**Value**: HIGH. Right now we have 5 deploys with no measured impact. Each deploy carries an unverified +N pp claim."
    }
   ],
   "against": "A tiny smoke set cannot judge everything: \"- The 7-response smoke had DBQ uniqueness `2/2`, but MCQ_SET uniqueness `1/2`; this is only a warning at that sample size, but it confirms the next pre-live gate should use at least `--diversity-per-qtype 5`.\" (crystal evidence/RUN_MODE_TAXONOMY_AND_GATES_20260521.md line 95).",
   "adds_to_existing": [
    38,
    47
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write new questions instead of copying or paraphrasing released exam items, and use only sources whose licence has been checked.",
   "kind": "adopted rule",
   "found_by": "Set as a hard constraint on question writing and as an inclusion criterion for any pipeline component; source corpora were licence-audited row by row.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/t5_dbq_stem_template.md",
     "lines": "4-5",
     "quote": "NO verbatim College Board prompts; NO paraphrase of released exams; net-new stems anchored to verified primary documents."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/INCLUSION_CRITERIA.md",
     "lines": "64",
     "quote": "7. **License / source-clean**: no scraped copyrighted material, no Anthropic / OpenAI-output-as-training, no PII"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/2026-05-22T2308Z_v93_phase3_reaudit_VERDICT_ADJUST.md",
     "lines": "54",
     "quote": "- Wikipedia: every row has `\"license\":\"CC BY-SA 4.0\"`."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make hard items hard through reasoning — a subtle distinction, synthesis or weighing a counter-argument — not through obscure names or facts outside the scope, and keep easy items free of giveaway wording.",
   "kind": "adopted rule",
   "found_by": "Written into the generator checklist and the run-improvement backlog after hard items failed on obscure or out-of-period content.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/evidence/FUTURE_RUN_IMPROVEMENT_BACKLOG_20260521.md",
     "lines": "233-234",
     "quote": "- hard questions should require reasoning, not obscure names or out-of-period facts."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/common_pre_checklist.md",
     "lines": "71",
     "quote": "- [ ] Hard: subtle distinction, synthesis, or counterargument evaluation"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/apllm-history/runtime_assets/ib_satisfaction_kit_v1/failure_mode_index.json",
     "lines": "41",
     "quote": "\"fix\": \"All required facts must be curriculum-standard\""
    }
   ],
   "against": "The judge cannot check difficulty without written definitions: \"**If no definitions provided**: `difficulty_alignment = 1.0`. Do NOT invent criteria.\" (raw_rubrics/_base_evaluation.txt line 137).",
   "adds_to_existing": [
    33
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Use a model judge only to choose among items that already pass the code checks, and keep it only if it beats simply taking the first valid item.",
   "kind": "measured",
   "found_by": "Invalid but fluent candidates beat passing ones when they reached the selector; on a saved archive the model selector tied first-valid; extra candidates sometimes scored worse than the first.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/SELECTOR_CALIBRATION_TAKEAWAYS_20260520.md",
     "lines": "17",
     "quote": "- Evidence: if bad candidates reach the selector, a fluent but invalid MCQ_SET can beat the actually passing raw candidate."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md",
     "lines": "39",
     "quote": "Takeaway: Gemini did not beat first-valid on this archive."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/SELECTOR_CALIBRATION_TAKEAWAYS_20260520.md",
     "lines": "9",
     "quote": "- Evidence: MCQ_SET k=1 candidates in the current calibration passed, while several alternate k=2..k=6 candidates scored 0.0 or hit scoring failure."
    }
   ],
   "against": "On another archive the selector did well: \"**Selector recall** (on rows where at least one candidate passed): 137/145 = 0.945\" (variant-calibration-lab-snapshot/gemini_selector_calibration_final.md line 15).",
   "adds_to_existing": [
    65,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Strip drafting, self-checking and debug text from an item before a student or judge sees it; leftover working notes are penalised and leaked metadata broke the delivery contract.",
   "kind": "adopted rule",
   "found_by": "A draft-verify-revise generation spec found verification text is penalised by the judge; a saved winning item failed delivery validation because it carried pipeline metadata.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/02_R42_CoVe_DBQ_spec.md",
     "lines": "150",
     "quote": "The verification meta-text WILL be penalized — IB rubric scores presence of meta-pedagogical voice negatively (we saw this in R10 paraphrase-composition)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/common_pre_checklist.md",
     "lines": "51",
     "quote": "- [ ] No \"this question tests…\" preamble visible to students"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/WEEKLY_APUSH_PIL_REPORT_20260520.md",
     "lines": "500",
     "quote": "Debug metadata belongs in archives/logs, not official payloads."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Fix an item's structure and answer key first, then write explanations against that fixed key, and check that every explanation, hint and feedback line refers to the item's actual options and key.",
   "kind": "adopted rule",
   "found_by": "Another project's two-stage build (structure and key first, explanations second) stopped explanations contradicting keys; the grader's rubric fails any item whose explanations name options or values that aren't there.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/k_12_social_studies_distilled.md",
     "lines": "44",
     "quote": "- This prevents the model from generating an explanation that contradicts the answer key."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_evaluation.txt",
     "lines": "85",
     "quote": "- **FIELD MISMATCH**: Explanations, hints, feedback templates, or `additional_details` describe distractors, answers, or values that do NOT match the actual options or correct answer"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt",
     "lines": "66",
     "quote": "- Do explanations/rationales match the correct answer and options?"
    }
   ],
   "against": "The two-stage pattern was proven only for some item types: \"- Match/fill-in/article were less proven and flagged for more validation.\" (k_12_social_studies_distilled.md line 49).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Build a source set so every document bears on the question, each carries a clear point of view, and together they support more than one defensible argument.",
   "kind": "adopted rule",
   "found_by": "The grader's rubric for document-based tasks fails sets with irrelevant documents, perspective-free documents, or documents that all point one way.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/dbq_evaluation.txt",
     "lines": "54",
     "quote": "- Score 1.0: Every document can be used to support, complicate, or inform an analysis related to the prompt"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/dbq_evaluation.txt",
     "lines": "60",
     "quote": "- Score 0.0: All documents point to one obvious conclusion; no real analysis or argumentation is possible"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/dbq_evaluation.txt",
     "lines": "44",
     "quote": "- Score 1.0: Multiple documents have clear perspective, purpose, or context that students can analyze; sourcing/analysis opportunities exist"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Choose sources and frame the task for the exact objective requested, not the broad theme of its period; drifting to a nearby topic was the single most common failure.",
   "kind": "measured",
   "found_by": "A row-level failure map of a 1,080-item run put 156 of the failures under standard alignment, far ahead of any other class; document-based items defaulted to generic period themes and missed specific objectives.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/DBQ_GAP_ANALYSIS.md",
     "lines": "4",
     "quote": "Failures are driven almost entirely by **topic/rubric misalignment**, not hallucination or structural errors."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/a0f_completed_failure_map_20260520.md",
     "lines": "23",
     "quote": "| quality_fail_standard_alignment | 156 |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/IB_A0F_99_RECOVERY_PLAN_20260519.md",
     "lines": "214",
     "quote": "1. The item drifts from the requested substandard into a nearby Unit 1 topic."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    58
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Carry the request's course, unit, period and standard ID unchanged through every step, and fetch the standard's facts by its exact ID rather than by fuzzy topic search.",
   "kind": "measured",
   "found_by": "A cross-project synthesis listed scope passthrough among the real fixes; exact-ID lookup hit 100% on a 40-standard check; a mismatched ID format silently routed every request to a fallback path.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/MASTER_SYNTHESIS.md",
     "lines": "145",
     "quote": "The request's course, unit, period, type, standard/substandard, and node identifiers must flow through every layer without rederivation."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md",
     "lines": "68",
     "quote": "- Exact `node_id` lookup beat fuzzy topic search. A 40-standard check reportedly found 100% hit rate."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/quarantine/2026-05-22T1731Z_den_solver_delivery/QUARANTINE_REASON.md",
     "lines": "25",
     "quote": "Different format → den's substandard_lookup falls through → deterministic template path skipped → v80bchain fallback only."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Drop an item or source that fails audit instead of patching it into a pass.",
   "kind": "adopted rule",
   "found_by": "Adopted as a standing rule for sources and training rows after fabricated and truncated material was found in corpora.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_main_session_close/01_HANDOVER.md",
     "lines": "89",
     "quote": "Drop-don't-patch when sources fail."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md",
     "lines": "359",
     "quote": "- **Drop-don't-patch** on any audit failure."
    }
   ],
   "against": "The later pipeline patched instead: \"If the model returns malformed JSON after a successful model call, the route performs deterministic schema repair from the retrieved context and marks the route internally as `model_json_repaired`; this preserves the one-attempt model contract while avoiding official schema 500s.\" (apllm-history/README.md line 30) and \"- Apply a targeted repair function that mutates the failing candidate to address the specific criterion\" (helpers/data/output/99stack_layer4_repair_spec.md line 14).",
   "adds_to_existing": [
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Audit a whole generated set's distributions — key positions, label validity — not just each item's format and the row count; a set that passed row-count checks had 64.5% of its keys on one letter.",
   "kind": "measured",
   "found_by": "A full-dataset audit of a 1,036-row build found the key on A in 64.5% of items and D in 0.7%, plus 77.5% invalid standard IDs, after the build had passed its row-count validation.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_data_session/HANDOVER.md",
     "lines": "287",
     "quote": "Build ran, validated row-count, missed the structural defect."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01_session_end/SHADOW_HANDOVER.md",
     "lines": "60",
     "quote": "| MCQ answer-A bias | A=64.5%, B=27%, C=7.8%, **D=0.7%**, E=0% (vs uniform 25% expected) |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md",
     "lines": "357",
     "quote": "- **T0 D13 full-census, no sampling**."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    8,
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Never let the writer grade or certify its own items; a self-graded 95.2% was design evidence only, and a small writer tends to answer 'yes' to checks on its own flawed drafts.",
   "kind": "adopted rule",
   "found_by": "Two earlier generators' headline benchmarks were graded by the same model family that wrote the items; a verification spec warned that small models confirm their own flawed drafts.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/k_12_social_studies_distilled.md",
     "lines": "10",
     "quote": "- Critical caveat: that 95.2% benchmark used Gemini 2.0 Flash self-evaluation of Gemini-generated questions."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/k_12_social_studies_distilled.md",
     "lines": "60",
     "quote": "The repo says this directly: if Gemini gives 90% and Claude gives 60%, the 90% is meaningless."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/02_R42_CoVe_DBQ_spec.md",
     "lines": "174",
     "quote": "Madaan et al. (A5, NeurIPS 2023) report self-refine adds <1pp at <13B and can hurt below 7B; the mechanism is that small models confabulate \"yes, this is correct\" answers to verification questions about flawed drafts, then fail to identify what to revise."
    }
   ],
   "against": "Self-verification helped a large model in the cited study: \"CoVe joint-style +15.5 FACTSCORE pp on biographies (Llama-2-65B-chat).\" (02_R42_CoVe_DBQ_spec.md line 22).",
   "adds_to_existing": [
    43,
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a valid item can't be produced, fail visibly — refuse item types that were never measured and return an error rather than a weak or fallback item.",
   "kind": "adopted rule",
   "found_by": "The production generator refused unmeasured types, document-based generation without real sources returned an error, and the pre-emit checklist preferred an error to a weak item.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/apllm-history/README.md",
     "lines": "137",
     "quote": "- We have no signal on `msq` / `fill-in` / `match` / `sequence` / `article` from internal eval — gated to 501 to avoid shipping unvalidated outputs."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/system_prompt_dbq.md",
     "lines": "135",
     "quote": "Without D13: do not generate this DBQ. Return an error indicating \"real-source documents required\"."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/common_pre_checklist.md",
     "lines": "83",
     "quote": "This is better than emitting a low-quality item that wastes an IB call."
    }
   ],
   "against": "Fallback items were later recommended for acceptance: \"main-a recommends YES — the cached archetype is itself derived from live-IB-validated v80bchain content, so it's not \"deterministic-from-bank\" in the prior sense.\" (artifacts/validated/2026-05-22T2116Z_den_solver_v8_FIRST_VALIDATED/VALIDATION_REASON.md line 62).",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Set the ship, hold and abort thresholds before running the measurement, then apply them as written.",
   "kind": "adopted rule",
   "found_by": "Decision trees and confirmation thresholds were written before each evaluation; a hypothesis was rejected because the result fell below its pre-set threshold.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/coordination/RESULTS.md",
     "lines": "85",
     "quote": "Cont mean 0.704 is far below the 0.92 confirmation threshold; the cell main-A predicted would lift most (MCQ) actually regressed slightly under RAG."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/memory/project_v93_falsifier_kill_2026_05_23.md",
     "lines": "28",
     "quote": "Per orch decision matrix (PASS ≥+3pp overall AND ≥+10pp factual / ABORT <+5pp AND <+0pp):"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/v38_decision_rules.md",
     "lines": "33",
     "quote": "### If v38 aggregate continuous within ±0.01 (0.928–0.948) of v29"
    }
   ],
   "against": "Overlapping bands left a result undecided: \"- v93 lands at ABORT/ADJUST boundary on overall but FAILS PASS gate clearly\" (memory/project_v93_falsifier_kill_2026_05_23.md line 30).",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Spread the evaluation items across every unit and standard the claim covers; results differ by unit, and a set drawn from three of nine units can't speak for the course.",
   "kind": "measured",
   "found_by": "The goal-tracking evaluation set was found to sample only three units; one unit scored about 9 points below the full course; some standards failed systematically while others always passed.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/analytics.md",
     "lines": "156",
     "quote": "⚠ Unit-coverage skew: eval set only samples APUSH Units 3/6/8 — main agent should blend before deploy."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/2026-05-27T2130Z_v80b_u1_baseline_course_check.md",
     "lines": "29",
     "quote": "v80b on U1 is ~9pp below its full-course aggregate. U1 is a harder period for the chain."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/system_improvement_brainstorm.md",
     "lines": "39",
     "quote": "Some substandards (KC-1.1.I.* on MCQ_SET) systematically fail; others systematically pass."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Record how each finding was established — own measurement, single trial, published study, inference or hearsay — and re-test outside results on your own items before relying on them.",
   "kind": "adopted rule",
   "found_by": "Every memory entry carried an evidence tier; another team's takeaways were filed as low-confidence priors to test; predicted lifts stayed at the lowest tier until measured.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/EXPORT_README.md",
     "lines": "115",
     "quote": "(T0 = measured on our data, T1 = single trial, T2 = top-tier paper, T3 = inference, T4 = hearsay)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-parent/.agent/memory/auto/research_parallel_team_takeaways.md",
     "lines": "12",
     "quote": "audit_note: T3 not T2 because their stack/account/data may differ; treat as priors not conclusions; low confidence"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/02_R42_CoVe_DBQ_spec.md",
     "lines": "8",
     "quote": "**Evidence tier:** T2 (cited, scope-flagged). Predicted lift is T4 until Quill measures."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "How much context to give a writer is unsettled: layering curriculum notes on top of source documents did worse in a six-item trial, while injected scope boundaries were credited with keeping items in scope.",
   "kind": "open question",
   "found_by": "A small arm-by-arm trial on document-based items and a cross-project note that too many examples hurt dense courses conflict with a generator kit that injects curriculum context on every call.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md",
     "lines": "136",
     "quote": "- DBQ route should prefer D13-only source grounding. Do not layer generic curriculum notes into the DBQ prompt until an A/B proves no regression; PATH G hybrid was worse than D13-only."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md",
     "lines": "186",
     "quote": "- For dense courses like APUSH, too many prompt examples can hurt; prefer exact facts/source packs over long example lists."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/README.md",
     "lines": "139",
     "quote": "| Out-of-scope questions slip through | `assessment_boundaries` injected at gen time |"
    }
   ],
   "against": "The 'worse' result rests on six items: \"6 dbq prompts (from WAVE B subset). Build inputs for:\" (helpers/data/build_PATH_G_dbq_hybrid.py line 4).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Whether source-free recall items serve practice as well as source-based items is untested: the judge passed both, and the source-free form differs from the exam form.",
   "kind": "open question",
   "found_by": "Source-stripped items passed the judge at 90-100% and read as ordinary review questions, but nobody measured what students learn from them versus source-based items.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/EXPLOIT-002-stimulus-strip.md",
     "lines": "197-198",
     "quote": "A real APUSH teacher reading any of the 30 items would call them \"fine, mid-tier AP-prep MCQs\" — not adversarial."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/EXPLOIT-002-stimulus-strip.md",
     "lines": "206-209",
     "quote": "The only \"tell\" is that they lack a primary-source stimulus — which makes them weaker AP-prep than the live exam form (where stimulus analysis is the whole point), but is **not** something a teacher would flag as evaluator-gaming."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/SECOND_TIER_REASON.md",
     "lines": "19",
     "quote": "- **Stem-only review-drill products**: explicit non-exam-format MCQs (no stimulus) for AP-prep practice apps, where the IB grader rubric matches the product shape."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Generate each item type with its own pipeline and checks rather than one shared generator; pushing every type through one generator destroyed the structured types.",
   "kind": "adopted rule",
   "found_by": "Four corpora independently confirmed per-type generation; one shared generator trained across all types dropped document-based items and question sets to 0%.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/MASTER_SYNTHESIS.md",
     "lines": "74",
     "quote": "| Per-type generation | confirmed | confirmed | confirmed | confirmed | compatible | T1 |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md",
     "lines": "54",
     "quote": "- This is the right ownership boundary: change MCQ_SET without risking DBQ or SAQ."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/memory/project_v94_brain_idea_falsified_at_scale_2026_05_25.md",
     "lines": "30",
     "quote": "- **DBQ + MCQ_SET catastrophically destroyed** — structured-format competence overwritten by narrative weight updates"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt",
   "lines": "40",
   "quote": "**Display Timing**: Content is ONLY an \"answer giveaway\" if shown BEFORE the student attempts to answer."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/next_live_run_prep.md",
   "lines": "75",
   "quote": "**Symptom**: 24 rows tagged `answer_telegraph` — stem repeats the distinctive noun phrase of the correct option."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/pending_review/2026-05-22T211855Z_exploits_EXPLOIT-003-mcqset-phrase-anchor/source_report.md",
   "lines": "92-94",
   "quote": "The judge cannot reliably distinguish \"question explicitly quotes a stimulus phrase\" from \"question genuinely requires that phrase to answer\"."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/common_pre_checklist.md",
   "lines": "43",
   "quote": "- [ ] Question fails the counterfactual: \"if I deleted the stimulus, can the student still get this right?\" — must be NO"
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_evaluation.txt",
   "lines": "387",
   "quote": "- **Borderline-correct distractors**: an option labeled incorrect is actually a defensible answer under the stem's *named* criteria."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01_session_end/SHADOW_HANDOVER.md",
   "lines": "60",
   "quote": "| MCQ answer-A bias | A=64.5%, B=27%, C=7.8%, **D=0.7%**, E=0% (vs uniform 25% expected) |"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/next_live_run_prep.md",
   "lines": "58",
   "quote": "**Symptom**: 62 of 71 MCQ_SET failures fire `educational_accuracy` aggregate; 61 fire `answer_balance` (children share correct letter); 47 fire `redundant_questions` (children test same skill)."
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_set_evaluation.txt",
   "lines": "345",
   "quote": "- Each question tests a distinct aspect"
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/KNOWN_ISSUES.md",
   "lines": "45-46",
   "quote": "The correct denominator for IB pass rate is `pass + fail` (excluding skips), not `pass + fail + skip`."
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt",
   "lines": "23",
   "quote": "- Self-advocacy metadata arguing every metric should pass"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/v18_rebuild_scope.md",
   "lines": "54-55",
   "quote": "4. **Atlas verify** (free) — every source URL must 200; every passage must substring-match the verified URL's body."
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md",
   "lines": "122",
   "quote": "If a visual source is ever allowed, the actual visual or a faithful OCR/caption payload must be supplied by retrieval, not invented by the model."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/KNOWN_ISSUES.md",
   "lines": "10",
   "quote": "**Symptom**: local mirror's DBQ pass rate is 5-25%; live export shows 90%+."
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/k_12_social_studies_distilled.md",
   "lines": "63",
   "quote": "- Article evaluation falsely failed long articles because only the first 3,000 chars were evaluated; raising the limit to 12,000 fixed the evaluator-side bug."
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md",
   "lines": "155",
   "quote": "- Transform-layer data loss was catastrophic: MCQ_SET stimulus attribution, SAQ stimulus attribution, LEQ scoring notes, DBQ author/title/date/HIPP fields were dropped before evaluation."
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt",
   "lines": "5",
   "quote": "You should only fail a metric when you find a clear, concrete, unambiguous violation that you can quote and explain."
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/RUBRIC_BLINDSPOTS.md",
   "lines": "75-77",
   "quote": "Without a quotable spec, this metric default-passes regardless of how non-standard the item is (stem-only, no stimulus, terse explanation)."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/quarantine/2026-05-22T163819Z_reports_mcqset_50_50_live_verified_20260522/source_report.md",
   "lines": "25",
   "quote": "- Two inherited-passing candidates failed live IB and were not included in final artifact."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/02_R42_CoVe_DBQ_spec.md",
   "lines": "151",
   "quote": "With IB's 17pp per-cell variance on identical inputs (R41 finding), a single 30-prompt DBQ eval is uninterpretable."
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_oracle_session/HANDOVER.md",
   "lines": "396",
   "quote": "- **B1.** When IB curriculum API returns 503, does `evaluators/base.py` fail-the-row, fall-back-to-bundled-facts, skip-factual-verification, or default-pass?"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/CHANGELOG.md",
   "lines": "30",
   "quote": "- **Quill `s-quill-ib-calibration-spot-check-1500`** — 10 known-correct curriculum API facts → MCQ stems → IB grader → expect 10/10 factual_accuracy=1."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/FINAL_REPORT.md",
   "lines": "8-10",
   "quote": "lifts a deliberately mid-quality hand-crafted batch from \"no chance\" to **100% (30/30)**."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/SELECTOR_CALIBRATION_TAKEAWAYS_20260520.md",
   "lines": "12",
   "quote": "2. Winner-only scoring is not selector calibration."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/coordination/.archive/CLONE_PARTIAL_WORK_2026-04-30T1510Z.md",
   "lines": "28",
   "quote": "2. Save rejected attempts to `*_rejects.jsonl` for debugging (script currently only writes kept rows)"
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/analytics.md",
   "lines": "46",
   "quote": "On the same 297 prompts, the IB grader (gpt-5.2 default-PASS bias) gives **92.3%**, but the held-out Gemini-3.1-pro judge gives **49.2%**."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/analytics.md",
   "lines": "64",
   "quote": "- DBQ + mcq_set cells: held-out judge says **0/30** even when IB says 70-100%."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/coordination/.archive/CLONE_VERIFY_GRADER.md",
   "lines": "12",
   "quote": "- **+25.92pp swing from grader version alone**"
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/achieved.md",
   "lines": "69",
   "quote": "Root cause: paqpgdst's MCQ_SET pass rate on HOLDOUT prompts is **0%** (0/176 K=3 attempts), vs ~20% on eval baseline."
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/CHANGELOG.md",
   "lines": "20",
   "quote": "- **Quill Q1 (13:30Z):** APUSH/SAQ vs APWH/SAQ +23pp factual_accuracy gap, clustered in APUSH unit-6 (Gilded Age) + unit-8 (Cold War) named-entity hallucinations"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/d13_dbq_corpus_pipeline_spec.md",
   "lines": "33",
   "quote": "**Every row carries source_snapshot_hash** — provenance integrity intact"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/CHANGELOG.md",
   "lines": "81",
   "quote": "- Verified extraction completeness: 8/8 md5 hash spot-checks MATCHED between source and oracle"
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/postmortem_v89_v90_v91.md",
   "lines": "32",
   "quote": "Per v91 ABORT_DEAD: pipeline-side handling of DBQ scores 87.9% — the model CAN do DBQ when given runtime context, but cannot be TRAINED to."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md",
   "lines": "157",
   "quote": "- Flash research stage could hallucinate facts that poisoned compile; verified facts were better than LLM-generated research."
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/DBQ_GAP_ANALYSIS.md",
   "lines": "4",
   "quote": "Failures are driven almost entirely by **topic/rubric misalignment**, not hallucination or structural errors."
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/ib_pass_criteria_pack/README.md",
   "lines": "72",
   "quote": "When `factual_accuracy` or `stimulus_quality` zeros, the row passes 0% of the time (kills=1.0)."
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt",
   "lines": "250",
   "quote": "| 1 | 0–2 | 0.70–0.84 | INFERIOR |"
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/MASTER_SYNTHESIS.md",
   "lines": "264",
   "quote": "Every failed result should map to a failed hard dimension and item type before any fix is chosen."
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/quarantine/2026-05-22T155705Z_data_v87_step_function_gate.py/source_report.md",
   "lines": "51",
   "quote": "crit_collapse = any(d <= -5.0 for d in crit.values())"
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/fact_lookup_for_generation/README.md",
   "lines": "88",
   "quote": "| `req.grade` | unit number as string (e.g., `\"1\"`) |"
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/run_0506c1fd_v2_final_live_export_analysis.md",
   "lines": "11",
   "quote": "- Grade echo issue detected in export content/request metadata."
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md",
   "lines": "55",
   "quote": "Why it fails: the model describes an absent map."
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/WEEKLY_APUSH_PIL_REPORT_20260520.md",
   "lines": "480",
   "quote": "Gemini should only rank validator-clean candidates. If every candidate has the same flaw, Gemini cannot create a passing item."
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/analytics.md",
   "lines": "41",
   "quote": "| v29 + RAG + BoN K=8 (v2.4.0) | 92.3% | 49.2% | n/a | ⚠ 43.1pp Goodhart gap |"
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/CHANGELOG.md",
   "lines": "93",
   "quote": "**Goodhart risk surfaced:** training rows aligned to grader rubric → higher pass rate, but at risk of optimizing the rubric not actual AP skill."
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_set_evaluation.txt",
   "lines": "132",
   "quote": "- Object counts and answer balance analysis are AUTHORITATIVE - do NOT attempt to re-count or recalculate."
  },
  {
   "truth": 67,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/KNOWN_ISSUES.md",
   "lines": "129-130",
   "quote": "**Root cause**: the filters in `scripts/filters/*.py` are individually plausible but their bundle over-rejects valid candidates."
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/pending_review/2026-05-22T211855Z_exploits_EXPLOIT-003-mcqset-phrase-anchor/source_report.md",
   "lines": "66-68",
   "quote": "The single failing critical metric is `educational_accuracy`, driven by ≥1 of 3 child questions failing its own MCQ-level checks"
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/pending_review/2026-05-23T000424Z_exploits_EXPLOIT-004-saq-no-stimulus/source_report.md",
   "lines": "122-124",
   "quote": "Add a check: the criterion must specify a SPECIFIC, NAMED historical fact that the example must satisfy, not a generic category."
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/02_R42_CoVe_DBQ_spec.md",
   "lines": "149",
   "quote": "One knob per eval, or you can't attribute deltas."
  }
 ]
}
```
