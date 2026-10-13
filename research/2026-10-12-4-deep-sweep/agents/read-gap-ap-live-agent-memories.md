# read:gap:ap-live-agent-memories

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "ap-live-agent-memories",
 "coverage": {
  "read": [
   "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/ — 62 of the 63 files absent from ~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/ (absence checked per file), read in full; plus the 9 files that differ from their backup copies (cmp): MEMORY.md, reference_atlas_helper.md, reference_inceptbench.md, reference_project_state.md, reference_shadow_helper.md, reference_teacher_data.md, research_best_approach.md, research_best_of_n_decode.md, research_qwen3_dense_tops_at_32b.md, read in full and diffed against the backup (the diffs are path changes, supersession notes and model-size rulings)",
   "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/ — 61 files: MEMORY.md (differs from the main folder's) and 50 unique files read; 7 files byte-identical (cmp) to the main folder (feedback_curriculum_enrichment_mandatory_2026_05_11.md, feedback_d13_inference_injection_partial_fix_2026_05_12.md, feedback_dbq_rag_inference_cannot_fix_v2.5.6.md, feedback_dbq_stimulus_v2.5.6_root_cause.md, feedback_mcq_set_RAG_actively_helps_v2.5.6.md, feedback_mcq_v2.5.6_rubric_tightening.md, feedback_misconceptions_user_prompt_injection_hurts_2026_05_12.md) read once and cited from the main folder",
   "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-oracle/memory/ — all 14 files",
   "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-ap-social-studies-generator/memory/ — MEMORY.md, feedback_agentic_practices.md, feedback_style.md, project_catchup.md, project_training.md",
   "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-ap-social-studies-generator-python/memory/MEMORY.md",
   "~/.claude/projects/{home}/memory/ — only the 13 named AP notes: sft_v4_prompt_engineering.md, team_learnings_20260422.md, training_data_audit_20260423.md, postit_20260423.md, fdpo_pipeline.md, stage2_postmortem.md, session_20260422_grpo_to_pipeline.md, findings_sftv7_20260424.md, mcq_set_improvement_log.md, training_data_70k.md, continuous_improvement.md, feedback_no_inceptbench_debug.md, project_teacher_agent.md"
  ],
  "skipped": [
   "reference_sftq_creds_location.md (aptraining memory, one of the 63 absent files) — on the never-open list",
   "reference_keys_and_endpoints.md, reference_sftq_key_location.md, reference_synapse_os_endpoints.md (helpers-data memory) — on the never-open list",
   "user_profile.md (ap-social-studies-generator memory) — a user_*.md profile on the never-open list; it was printed by mistake (see notes) and nothing from it is used",
   "Main-folder files byte-identical to auto-memory-backup (e.g. MEMORY_GOVERNANCE.md, feedback_eval_503_hiccup.md, feedback_field_level_provenance.md, feedback_no_hallucination_in_training_data.md, feedback_oracle_source_reconciliation.md, project_grader_audit_results_2_of_3_pass.md) — outside this direction; cited only through their MEMORY.md index lines, which are in scope because MEMORY.md differs",
   "All session transcripts (.jsonl) beside the memory folders — out of scope",
   "All other notes in ~/.claude/projects/{home}/memory/ — out of scope; none of the never-open files there were opened",
   "Read but no candidates, because they are infrastructure, vendor, organisational or model-training mechanics: deployment and GPU-quota rules (feedback_deployment_min0_max1_rule.md, feedback_max_two_deployments.md, feedback_21sec_scale_down_actor_2026_05_13.md, feedback_gemma4_b200_deploys_when_h100_blocked.md), training-service payload notes (feedback_fireworks_*.md, feedback_sftq_display_name_64_char_limit_2026_05_27.md, feedback_sft_messages_schema_required.md), file sync, scheduling and session notes, messaging-store plumbing (feedback_synapse_checkin*.md, the oracle synapse notes), learning-rate, epoch, adapter and model-size notes (feedback_epoch_rule_refined.md, feedback_raw_qwen3_32b_sft_LR5e5_proven_dead_3x.md, research_qwen3_dense_tops_at_32b.md, project_v34_merged_regression.md, project_v37b_3ep_aggressive_regressed.md, project_v43_soup_canonical.md, recipe_v29_bon_k8_winning.md), and model preservation and archive notes"
  ],
  "notes": "(1) Read-only: no file was created, edited or moved; quotes were checked by a stdin-only script. Mistake: printing the ap-social-studies-generator folder with a glob also printed user_profile.md, a never-open user_*.md profile; nothing from it is used. (2) One oracle file, feedback_synapse_per_role_token_var.md, holds a token-like string in plain text. I have not reproduced it; it is worth scrubbing or rotating. (3) name_bearing_source is judged on file basenames, because every path carries the account's home directory. No candidate relies on the person-named files in helpers-data (feedback_[name]_owned_docs_propose_diff_first.md, feedback_[name]_never_blocker_proxy_chain_inherits_class_authorization_2026_06_02.md, feedback_orch_host_paths_use_home_not_stanhus_2026_06_02.md); they were read and are organisational. Agent names (Quill, Atlas, Shadow, Compass, Cheater, Oracle) appear in some file names and quotes; they are agents, not people. (4) Contradictions within these memories, used as 'against' evidence: an 'answer-format only' rule versus the code-read finding that the checker grades question objects; a 97-point judge divergence that was largely reference-judge timeouts; a 'new best' record later retracted as noise because the mechanism never fired; a note to keep a pipeline bug because its fallback scored better versus a note that fixing it took the same item type to 10/10; one configuration reported as both -0.69 and +0.99 depending on the baseline; 'curriculum enrichment mandatory' blamed for a document-based zero that curriculum context could not fix; context injection for stimulus sets reversed under a later judge version on n=6. (5) Many numbers rest on n=6 to n=30 and single seeds; this is flagged in 'against'. (6) The judge changed version several times in the period (2.4.0, 2.5.3, 2.5.6, 2.5.7, 2.6.6), so numbers from different files are not comparable. (7) As a read-only subagent I did not register the work with mgr; the parent workflow owns that. (8) Where several agents described one experiment, I cited the primary measurement file."
 },
 "candidates": [
  {
   "statement": "Count a judge's timeouts, parse failures and service errors apart from its real verdicts and report how many real verdicts each score rests on, because errors counted as failures can fake a collapse.",
   "kind": "measured",
   "found_by": "A '1% pass' headline on long document-based items was 1 real verdict plus 99 timeouts; re-run at a sustainable rate it was about 60-67%. In another run 28 of 30 multi-question items timed out and corrupted the denominator, and a 13.3% rate on one type came with 20-22 of 30 rows timing out (about 40-50% when the judge answered). Earlier, lumping server errors with parse failures produced a false 'more brittle' claim, and a measuring-script mismatch made working generators look catastrophic.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_ib_grader_v266_dbq_mcqset_timeout_99pct_at_concurrency_default_2026_06_02.md",
     "lines": "10",
     "quote": "- DBQ: 1 real eval + 99 timeouts → headline 1% PASS (artifact)"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_ib_grader_timeout_300_mcq_set.md",
     "lines": "11",
     "quote": "**28 of 30 mcq_set rows timed out** producing `grade_fail status` and corrupting the cell pass-rate denominator."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "75",
     "quote": "`parse_ok=false` lumps 5xx with JSON fails; misread cost a wrong \"v20a more brittle\" claim. Always bucket by error type."
    }
   ],
   "against": "Limit: the timeouts concentrated on long outputs: \"Other cells (LEQ + MCQ + SAQ) time out at 1-6% — they're fine at default.\" (feedback_ib_grader_v266_dbq_mcqset_timeout_99pct_at_concurrency_default_2026_06_02.md, line 7).",
   "adds_to_existing": [
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Record the judge's version with every score and never compare or subtract scores made by different judge versions; re-score both sides on the same version first.",
   "kind": "measured",
   "found_by": "The same 297 generated items scored 63.64% under one judge version and 89.56% under the next (+25.92 points, no change to the items); a later version cut the same generators from 90%+ to 56-58%, and one quality dimension went from almost no failures to failing 24-30% of multiple-choice items.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_ib_grader_version_v240_to_v253.md",
     "lines": "26",
     "quote": "The same 297 generations from v29 were scored under both; +25.92pp aggregate / +25pp APUSH from the grader swap alone."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/project_v50_v56_strategy_with_numbers_2026_05_12.md",
     "lines": "9",
     "quote": "InceptBench grader jumped to v2.5.6 mid-cycle. Same models that scored 90%+ on v2.5.3 now score 56-58%. Two cell-specific tightenings drove most of the regression."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_ib_grader_version_v240_to_v253.md",
     "lines": "42",
     "quote": "- Refuse to compute deltas across grader versions; require both endpoints to agree on grader version OR re-score one side"
    }
   ],
   "against": "Old scores remain valid within their own version: \"- **Past v2.5.3 numbers stay valid as historical baselines for v2.5.3**, just like v2.4.0 numbers stayed valid as v2.4.0 baselines after the v2.4.0→v2.5.3 jump.\" (project_ib_grader_v256_canonical_2026_05_11.md, line 38). The shift had no fixed direction: one version was far more lenient, a later one far stricter.",
   "adds_to_existing": [
    45,
    39
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before calling a change better, re-score unchanged items several times to measure the judge's spread for each item type, count only differences larger than about twice that spread, and repeat a headline win before acting on it.",
   "kind": "measured",
   "found_by": "Three scorings of identical outputs gave a 1.54-point spread overall, 7.7-8.8 points on document-based essays and zero on multiple choice and long essays. None of the claimed wins since the baseline cleared that noise, and a later 'breakthrough' that once cleared a 3-point band tied the baseline under repeat seeds.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_grader_variance_discovered.md",
     "lines": "36",
     "quote": "**Insight:** DBQ drives ~all the noise. MCQ/LEQ are essentially deterministic. SAQ and MCQ_SET have small (~2pp) variance."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_grader_variance_discovered.md",
     "lines": "53",
     "quote": "**None of our \"wins\" since v29 are above the noise floor.** They're all clustered at ~133-134/150."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_three_rule_updates_20260506.md",
     "lines": "12",
     "quote": "(2) v40h \"0.9 breakthrough\" stat-tied with v29 under multi-seed (R8 caught it)."
    }
   ],
   "against": "Where the judge is deterministic, any difference counts: \"- MCQ / LEQ cells: ANY non-zero delta is real (deterministic baseline)\" (project_grader_variance_discovered.md, line 42).",
   "adds_to_existing": [
    34,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Compare versions on the mean of the continuous score, with the pass rate as a secondary figure, because items near the pass mark flip on small noise and a pass-rate gain can hide a lower average.",
   "kind": "measured",
   "found_by": "About 20% of document-based essay items sat between 0.80 and 0.90, around the 0.85 pass mark, producing 13-17 point pass-rate swings per run. A +1.77 pass-point 'gain' was -0.88 on the average, a -6.1 'regression' was +0.06, and a -2.3 'noise' result was a real -3.08 drop. The project cited statistics papers for this, without DOIs.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_r41d_continuous_metric.md",
     "lines": "27",
     "quote": "The IB grader thresholds at 0.85 internally. Items with continuous score in [0.80, 0.90] flip pass↔fail under any tiny continuous-side noise. For DBQ where ~20% of items sit in this band, this alone produces 13-17pp binary swing per run."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_r41d_continuous_metric.md",
     "lines": "69",
     "quote": "| v36b vs v29 | **+1.77 binary-pp** (within noise) | **-0.88 cont-pp** (slight regression) | binary lift was threshold-pushing borderline items, average quality actually slightly lower |"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_iteration_2026_04_29_inference_time_exhausted.md",
     "lines": "32",
     "quote": "| richer-RAG MCQ_SET \"noise\" | -2.3 binary-pp | -3.08 cont-pp ✗ REAL | continuous unmasks real regression |"
    }
   ],
   "against": "The delivered target stayed a pass mark (\"Threshold of 0.85 is fixed by mission.\", reference_inceptbench.md line 83), and the continuous score is lumpy: \"The grader's per-dim binary check + non-critical aggregation lands `overall` in clusters: 0.0/0.30/0.60-0.69/0.75-0.84/0.85-0.99/1.00.\" (same line, written about a superseded judge version). An average must not let partial credit offset a hard fail.",
   "adds_to_existing": [
    34,
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Compare a new way of generating content against a freshly generated baseline rather than stored outputs re-scored, because generation varies between runs even at temperature zero.",
   "kind": "measured",
   "found_by": "The same generator on the same 150 prompts at temperature 0 averaged 0.9475 on stored outputs and 0.9307 on fresh ones (1.68 points apart). Several configurations reported as regressions became real gains when compared fresh against fresh.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_baseline_must_be_fresh_gen.md",
     "lines": "3",
     "quote": "v29 fresh-gen 3-run continuous = 0.9307; v29 frozen-gen 3-run continuous = 0.9475. Δ 1.68 cont-pp from inference variance (temp=0 not deterministic across gen runs)."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_baseline_must_be_fresh_gen.md",
     "lines": "41",
     "quote": "Several \"regressions\" reverse to \"real lifts\" when using the correct baseline."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_baseline_must_be_fresh_gen.md",
     "lines": "17",
     "quote": "**For any continuous-metric model A vs model B comparison, both A and B must use FRESH generations. Don't compare test configs (fresh gens) against frozen baseline (re-scored).**"
    }
   ],
   "against": "\"3. **For binary pass rate**, frozen baseline is fine (insensitive to inference variance).\" (feedback_baseline_must_be_fresh_gen.md, line 47).",
   "adds_to_existing": [
    34,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat a result on about 20 items per item type as provisional and confirm it on a larger sample before building on it, especially for types that have failed before.",
   "kind": "measured",
   "found_by": "One item type scored 100% on 20 items and 0% on 100. A 99% 'promote' was retracted about six hours later, after downstream decisions had been made on it. A generator measured 83.3% on 30 items and 60% on 100; a five-item probe passed 5/5 while 31% of the full batch failed; an inserted-source fix scored 4/6, then 10/30.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_n_scale_tightens_CI_exposes_n100_anomalies_2026_06_01.md",
     "lines": "7",
     "quote": "The n=100 CI is ±15pp per cell (at n=20/cell), wide enough to mask structural floors."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_n_scale_tightens_CI_exposes_n100_anomalies_2026_06_01.md",
     "lines": "12",
     "quote": "- MCQ_SET 100% → 0% was the dramatic collapse: cell has structural issue (gemma family can't follow Option B 6-region schema at inference, matches Cheater's v90c K=18 0/16 finding 6/1 18:50Z); single-seed n=20 just got lucky"
    },
    {
     "path": "~/.claude/projects/{home}/memory/fdpo_pipeline.md",
     "lines": "12",
     "quote": "- Pass rates: **83.3% at N=30 / 60% at N=100** (N=100 is more reliable)"
    }
   ],
   "against": "\"Counter-case: When the cell has NO structural issue history (e.g., MCQ + SAQ have been consistently at 95-100% for multiple versions), n=100 100% is more credible. The skepticism scales with prior failure rate.\" (feedback_n_scale_tightens_CI_exposes_n100_anomalies_2026_06_01.md, line 26).",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check a second judge's agreement with the reference judge separately for each item type before using it to filter or promote, and when it fails every item of one type, suspect its rubric or parsing before the content.",
   "kind": "measured",
   "found_by": "A held-out judge with a single generic score gave 0/30 on every multi-part item type while agreeing on simple formats, so its 49% versus 92% 'contamination gap' mostly measured its own rubric. Another pair of judges agreed on short items but under-credited long essays by 19 points and over-credited document-based essays.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_stacked_decode_RAG_judge_result.md",
     "lines": "46",
     "quote": "Gemini scored 0/30 on EVERY mcq_set and dbq cell. The earlier Claude Opus spot-check on 24 BoN-lifted rows had 88% agreement with IB."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_stacked_decode_RAG_judge_result.md",
     "lines": "51",
     "quote": "- My single-prompt JSON rubric (\"factual_accuracy 0-1, overall 0-1\") can't decompose those"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_gemini_ib_dbq_judge_divergence_97pp_2026_06_02.md",
     "lines": "33",
     "quote": "- LEQ judge bias goes the OTHER way (Gemini under-credits LEQ). So \"Gemini judge is always wrong\" is too strong. The pattern is direction-specific per cell."
    }
   ],
   "against": "Part of a reported 97-point disagreement came from the reference judge timing out (\"- DBQ: 1 real eval + 99 timeouts → headline 1% PASS (artifact)\", feedback_ib_grader_v266_dbq_mcqset_timeout_99pct_at_concurrency_default_2026_06_02.md line 10), and judges did agree on a structural failure: \"- Both judges agreed on MCQ_SET 0% — so Gemini can be reliable when the failure mode is structural enough that both judges detect it.\" (feedback_gemini_ib_dbq_judge_divergence_97pp_2026_06_02.md, line 34).",
   "adds_to_existing": [
    37,
    69,
    31
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Score each item several times, separate the items that fail every time from those that flip, and work on the stable failures first, starting with the near misses.",
   "kind": "measured",
   "found_by": "Across three scorings of 150 items, 84% passed every time, 9.3% failed every time and 6.7% flipped. The stable near misses (0.7-0.8 every time) were the items that became triple passes once the writer got the objective's scope limits; flips were treated as judge noise.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v29_failure_analysis_3run.md",
     "lines": "20",
     "quote": "| Stable fail (0/3) | 14 | 9.3% | REAL MISSES — must train on |"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v29_failure_analysis_3run.md",
     "lines": "21",
     "quote": "| Flipped (1-2/3) | 10 | 6.7% | Grader noise — Compass R41 multi-call majority denoises |"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v29_failure_analysis_3run.md",
     "lines": "51",
     "quote": "**Soft fails (overall = 0.7-0.8 across all 3 runs)** — model is in ballpark, missing scope precision. **Highest-EV targets**:"
    }
   ],
   "against": "Across many generators no item was stable: \"- `always_passed_all`: 0 items (0.0%)\" (project_quill_discovery_cross_model_volatility_2026_05_11.md, line 19). Also, fixing the stable failures broke other items (see the whole-set re-run candidate).",
   "adds_to_existing": [
    60,
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Read the shape of failing scores: once judge errors are ruled out, failures that cluster at one value and repeat across runs and generators mark a structural defect that resampling will not fix.",
   "kind": "measured",
   "found_by": "55 of 58 valid verdicts on one item type fell below 0.70, clustered at 0.65, matching the other independent passes (five in all). Fabricated-source failures had zero variance across seeds. Across 56 generator variants, 7% of items never passed and no sampling depth helped them.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_v92_mcq_set_structural_fail_at_scale_confirmed_2026_06_02.md",
     "lines": "12",
     "quote": "- Fail <0.70 (deep): 55 (clustered at 0.65)"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_v92_mcq_set_structural_fail_at_scale_confirmed_2026_06_02.md",
     "lines": "36",
     "quote": "The score-cluster pattern at 0.65 (vs scattered fails) is the structural-fail tell."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_dbq_stimulus_v2.5.6_root_cause.md",
     "lines": "19",
     "quote": "σ=0 across seeds for v43-soup and v51; the failure is deterministic at T=0."
    }
   ],
   "against": "Identical repeat failures can also be judge errors: \"- MCQ_SET: 9 real evals + 91 timeouts → headline 0% PASS (also artifact)\" (feedback_ib_grader_v266_dbq_mcqset_timeout_99pct_at_concurrency_default_2026_06_02.md, line 11), and \"- σ=0 across seeds for the model-rate (13.3% pass rate, fully deterministic)\" sits next to \"- 20-22 of 30 rows status=grade_fail (Gemini Flash timeout on heavy outputs)\" (project_v50_v56_strategy_with_numbers_2026_05_12.md, lines 41-42).",
   "adds_to_existing": [
    65
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Re-run a fix on the whole item set, not only on the failures it targeted, because a change that repairs the targeted items can break items that used to pass.",
   "kind": "measured",
   "found_by": "Richer context turned 5 of 9 stable failures into passes (0% to 63% on that slice). On the full 150 items it broke about 17 short-answer items that had passed: -9.5 points on that type, and the overall result washed out.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_richer_rag_per_cell_tradeoff.md",
     "lines": "28",
     "quote": "Despite the targeted 9-item probe showing richer-RAG resolves 5 stable APUSH fails (+5 passes), at the FULL distribution it BREAKS ~17 saq items that v29 had been passing. Net on saq cell: -14 items = -9.5pp."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_richer_rag_resolves_stable_fails.md",
     "lines": "37",
     "quote": "**Aggregate on this 9-item slice: 0% → 63% pass rate. +63pp.** Way above the ~3pp noise floor."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_richer_rag_resolves_stable_fails.md",
     "lines": "69",
     "quote": "- Don't claim full +63pp transfers to 150-item — small sample. Pending full APUSH eval result."
    }
   ],
   "against": "The same change was a real gain on another item type: \"| apush/mcq | 93.3% | **100.0%** | +6.7pp | ±0.5pp | ✓ REAL LIFT |\" (project_richer_rag_per_cell_tradeoff.md, line 19).",
   "adds_to_existing": [
    60,
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before crediting a change with a score gain, confirm the change actually shows up in the outputs, because gains were claimed for mechanisms that never ran.",
   "kind": "measured",
   "found_by": "A model trained to emit grounding markers was declared the new best on +1.33 points; none of its 297 outputs contained a marker, and the difference was noise (McNemar p=0.7744). Separately, a research step built to supply verified sources had crashed on every call, so generation silently fell back to the old path.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "38",
     "quote": "0/297 v35 outputs emit any reflection token at decode (Self-RAG mechanism didn't fire). The +1.33pp lift is noise + grader artifact, NOT a Self-RAG mechanism win."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/recipe_v35_self_rag_reproducible.md",
     "lines": "135",
     "quote": "- 0/297 v35 outputs emit ANY reflection token (`[Retrieval=…]`, `[IsRel=…]`, `[IsSup=…]`, `[IsUse=…]`)"
    },
    {
     "path": "~/.claude/projects/{home}/memory/mcq_set_improvement_log.md",
     "lines": "11",
     "quote": "**Impact**: The Research→Compile pipeline NEVER WORKED for either MCQ or MCQ_SET. Both silently fell back to legacy generation paths every time. The research step was designed to gather verified primary sources and plausible alternatives, but it always crashed before it could run."
    }
   ],
   "against": "Two notes disagree on whether the silent fallback was better: \"- This forces legacy fallback pipeline which produces BETTER MCQ results\" (ap-social-studies-generator-python memory MEMORY.md, line 15) versus \"**Result for MCQ**: With research actually working, MCQ went from 96% → **100% (10/10, all perfect 1.00 scores)**.\" (mcq_set_improvement_log.md, line 15). Both rest on about 10 items.",
   "adds_to_existing": [
    38,
    36
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Back every reported score with the saved per-item file that reviewers can open, and check that the file covers every item submitted.",
   "kind": "measured",
   "found_by": "A 90% headline was flagged as a phantom because reviewers could not see the file behind it (it was real but unsynced). A summary was computed on 110 of 150 items. A baseline's citation chain broke and the baseline had to be re-run.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_eval_runs_sync_to_icloud.md",
     "lines": "16",
     "quote": "Without sync, helpers running phantom-audit on numeric claims correctly find no backing file, even when the claim is real on main-A's laptop."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_eval_runs_sync_to_icloud.md",
     "lines": "30",
     "quote": "Phantom-audit should grep `_meta.n_input` vs `total.n` to detect; example seen on `summary_v29_drift_recheck_v2_2026_05_04.json` where n_input=150 but total.n=110."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_three_rule_updates_20260506.md",
     "lines": "12",
     "quote": "(1) Shadow T8 v29 baseline phantom (citation chain broken — required re-running v29 at canonical schema to close)"
    }
   ],
   "against": "A missing file can be a sync delay rather than a false claim: \"- iCloud sync delay (Apple-side) can add 5–30 min on top of the 5-min sync rule. If a flag is dropped within that window, treat as advisory; outside it, treat as a real sync miss.\" (feedback_eval_runs_sync_to_icloud.md, line 31).",
   "adds_to_existing": [
    39,
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check every item used as an example or training material against every held-out test file, because checking against only one file let test items leak in and would have inflated scores.",
   "kind": "measured",
   "found_by": "A check against one test file declared 30 items unique; checking every test file showed all 30 were test items. Elsewhere, validation and test splits overlapped 21% with the training records.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_eval_contamination_check_all_eval_files.md",
     "lines": "18",
     "quote": "Found APUSH overlap was 100% — those \"30 unique\" rows were in fact eval-identical."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_eval_contamination_check_all_eval_files.md",
     "lines": "20",
     "quote": "Had I trained on those rows, v54 would have learned its eval set verbatim → fake pass rate, contamination, useless iteration. Caught before training; saved the cycle."
    },
    {
     "path": "~/.claude/projects/{home}/memory/training_data_70k.md",
     "lines": "80",
     "quote": "- `data/combined_val.jsonl` and `data/combined_test.jsonl`: 21% overlap with catchup_raw via cu-* IDs"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Deduplicate and count items on their full content, not on an opening prefix or a producer's candidate count, because items that share an opening are not duplicates and candidate counts include repeats.",
   "kind": "measured",
   "found_by": "Hashing the first 200 characters falsely marked 34% of distinct records as duplicates (items with the same question opening). A pool reported as about 31 candidates per objective held 12-14 unique documents.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}/memory/training_data_70k.md",
     "lines": "30",
     "quote": "`build_70k_dataset.py` used MD5 hash of first 200 chars of assistant content for dedup. This caused massive FALSE POSITIVES — many different records share the same first 200 chars (e.g., MCQs with the same question opening). Fixed to use **full content MD5 hash**."
    },
    {
     "path": "~/.claude/projects/{home}/memory/training_data_70k.md",
     "lines": "32",
     "quote": "**Before fix:** appeared to have only 37k unique records (34% false dedup rate)"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_cache_pool_count_vs_unique_doc_count_distinct_2026_06_01.md",
     "lines": "9",
     "quote": "Actual unique-doc pool was 12-14 per KC after dedup, not 31."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When an item needs source documents, take real excerpts from a verified collection and insert them in code, because a writer asked to supply them invents plausible but unverifiable sources even when handed a real excerpt.",
   "kind": "measured",
   "found_by": "A source-quality check failed generated documents in 98-100% of 270 attempts across three generators, with zero variance. Adding curriculum facts and objectives left it at 0/6 in three independent runs. Inserting real documents raised the pass rate from 0% to 33.3% on 30 items. With a real excerpt in the prompt, generated documents were still 'stylistic-real not literal-real'.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_dbq_stimulus_v2.5.6_root_cause.md",
     "lines": "3",
     "quote": "PILLAR 1 confirmed dbq stimulus_quality zeroed 98-100% across v43-soup + v50 + v51 on IB v2.5.6 (n=270 dbq attempts × 3 models, σ=0). Only real-source documents bypass the rubric."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/recipe_track_a_b_kc_pack_substitution.md",
     "lines": "11",
     "quote": "Even when grounded in a real OpenStax `_GROUND_TRUTH_SOURCE_` excerpt in the prompt, output documents are stylistic-real not literal-real."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/project_v50_v56_strategy_with_numbers_2026_05_12.md",
     "lines": "32",
     "quote": "- Hot-patch full validation n=30: **10/30 = 33.3% locked rate**"
    }
   ],
   "against": "Inserted sources still need checking against the question: \"In spot-checks, Track A substituted documents kept thematic coherence ~85% of the time.\" (recipe_track_a_b_kc_pack_substitution.md, line 52). A writer told to use the given documents verbatim did so only about a fifth of the time: \"- Success rate at \"use docs literally\" is ~20% on v43-soup (1 of 5 graded)\" (feedback_d13_inference_injection_partial_fix_2026_05_12.md, line 26).",
   "adds_to_existing": [
    57,
    17,
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check each source's attribution (who made it, where, when, and what kind of source it is) as a claim of its own, because generated source sets fail more on attribution than on their sentences.",
   "kind": "measured",
   "found_by": "In 15 failing document-based items, 9 factual-accuracy hits were real people attached to regions they never documented, plus a text author placed in a slot meant for an image. A 9-variant prompt sweep found that fabricated attributions and dates were the main source of invented content.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "70",
     "quote": "**NOT failing on document text sentences — failing on attribution and structure.**"
    },
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "73",
     "quote": "Model names real explorers but assigns wrong geographic scope."
    },
    {
     "path": "~/.claude/projects/{home}/memory/sft_v4_prompt_engineering.md",
     "lines": "18",
     "quote": "**Failure pattern:** Model fabricates specific source attributions and dates. SFT training examples should favor general historical description stimuli, not attributed documents."
    }
   ],
   "against": "Dropping attributions trades one check for another: \"**Why: `no_source` wins on factual_accuracy (70%) but `no_source_facts` wins on pass rate (60%).**\" (sft_v4_prompt_engineering.md, line 16). The counts are small: \"15 DBQ failures across 6 units. Dim hits:\" (findings_sftv7_20260424.md, line 64).",
   "adds_to_existing": [
    17,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A described picture, map or chart in an item must state exactly what a student will analyse (labels, routes, axes and values, figures and captions), because a generic description gives nothing to analyse.",
   "kind": "measured",
   "found_by": "Placeholder visual descriptions such as 'a historical map showing the geographic context of [topic]' failed clarity three times, with the judge noting that students could not use the document set as intended. The fix required named regions, routes, axes, data values and figures.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "92",
     "quote": "`doc[0].content = \"A historical map showing the geographic context of [topic] during the stated period, with key regions shaded in distinct colors\"` — template text, not analyzable."
    },
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "93",
     "quote": "Evaluator: *\"students cannot clearly use the document set as intended.\"*"
    },
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "97",
     "quote": "- For MAP: name regions labeled, trade routes shown, territories marked"
    }
   ],
   "against": "The fix was never re-measured, and it rests on three hits: \"3. **DBQ 12%** — all 4 fixes just applied; need fresh benchmark to measure impact\" (findings_sftv7_20260424.md, line 138).",
   "adds_to_existing": [
    64,
    21,
    22
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make every source in a set contribute a different actor, argument or angle, and check the set for near-duplicates before use.",
   "kind": "measured",
   "found_by": "Document sets failed source-quality checks when two or more documents had near-identical content; the judge flagged them as duplicates numbered as if different. Among 1,850 graded failures of question sets sharing one source, non-repetitiveness (146) and concept coverage (130) were recurring failure modes.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "103",
     "quote": "Two or more documents in the same DBQ have near-identical content/argument."
    },
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "104",
     "quote": "Evaluator: *\"Several documents are exact duplicates but numbered as if different.\"*"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/project_perfect_dpo_dataset_inventory_2026_05_18.md",
     "lines": "38",
     "quote": "| apush/mcq_set | 1850 | educational_accuracy(411), difficulty_distribution(381), factual_accuracy(221), test_preparedness(152), non_repetitiveness(146), concept_coverage(130), stimulus_quality(128) |"
    }
   ],
   "against": "The duplicate check was not re-measured: \"3. **DBQ 12%** — all 4 fixes just applied; need fresh benchmark to measure impact\" (findings_sftv7_20260424.md, line 138).",
   "adds_to_existing": [
    41,
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Never hand a writer known misconceptions or other false statements as loose suggestions, because it uses whatever text it is given as if it were true.",
   "kind": "measured",
   "found_by": "Misconceptions appended to the request as 'suggested distractor concepts' ended up in question stems and answer explanations instead of in the wrong options. Passes fell from 19/22 to 14/22 (-22.7 points) and alignment from 1.000 to 0.727, with questions testing misconceptions as if they were valid.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_misconceptions_user_prompt_injection_hurts_2026_05_12.md",
     "lines": "17",
     "quote": "| Δ | −5 | **−22.7pp** | −0.053 |"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_misconceptions_user_prompt_injection_hurts_2026_05_12.md",
     "lines": "21",
     "quote": "- `mastery_learning_alignment`: 1.000 → 0.727 (**−0.273**) — questions test misconceptions as if valid"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_misconceptions_user_prompt_injection_hurts_2026_05_12.md",
     "lines": "24",
     "quote": "The instruction \"use as inspiration\" is too soft; the model defaults to using strings literally."
    }
   ],
   "against": "\"- n=22 small sample, single seed (20260512), single model (v43-soup ty16vgj9)\" (same file, line 32). The same misconceptions inside a background block were credited with better distractors on a 6-item probe: \"**Why (hypothesis):** Curriculum KCs provide canonical assessment_boundaries and common_misconceptions that the model uses as material for distractor generation, lifting difficulty_distribution scores.\" (feedback_mcq_set_RAG_actively_helps_v2.5.6.md, line 15).",
   "adds_to_existing": [
    57,
    62
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check a writer's instructions for contradictions before generating, because when one part forbids something and another invites it, the output follows the invitation.",
   "kind": "adopted rule",
   "found_by": "Marking notes for short-answer items kept citing specific dates and named events, which then failed fact checks. The cause was a rule forbidding names and dates sitting beside a procedure that asked the writer to quote exact facts. The procedure was removed and replaced with a category-only rule.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "50",
     "quote": "**Pattern:** scoring_notes contained specific evidence (dates, named events) that"
    },
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "53",
     "quote": "**Root cause:** Two contradicting instructions:"
    },
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "55",
     "quote": "- User prompt PROCEDURE: `\"Write it as [FACT: <exact phrase>]\"` — granted permission"
    }
   ],
   "against": "\"2. **SAQ 33%** — new categorical-only fix not yet tested; these runs were pre-fix\" (findings_sftv7_20260424.md, line 137).",
   "adds_to_existing": [
    56,
    62
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Add retrieved background to a writer's request only for item types that do not already carry their own source material, and check the effect type by type.",
   "kind": "measured",
   "found_by": "Curriculum background helped item types with no source of their own (multiple choice 93.3% to 100%, long essays up). It made types that already include a stimulus or documents worse: -3.1 continuous points with any augmentation on stimulus-based sets, and -10 on document-based essays in a single run.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_cell_routed_rag_finding.md",
     "lines": "47",
     "quote": "**RAG augmentation only when prompt doesn't carry its own source content.**"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_cell_routed_rag_finding.md",
     "lines": "32",
     "quote": "| MCQ_SET | Has stimulus | HURTS | Already has source; extra context distracts |"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_iteration_2026_04_29_inference_time_exhausted.md",
     "lines": "39",
     "quote": "3. **MCQ_SET regresses with ANY augmentation**: -3.1 cont-pp regardless of field set. Already has stimulus, additional context distracts."
    }
   ],
   "against": "Under a later judge version a small probe pointed the other way for stimulus-based sets: \"On IB v2.5.6, injecting curriculum-API RAG context into mcq_set generation **lifts pass rate by +16.7pp** (2/6 → 3/6 on n=6 probe).\" (feedback_mcq_set_RAG_actively_helps_v2.5.6.md, line 9). The first test's aggregate was noise: \"**All three results sit within v29's grader-noise floor.** Aggregate-level deltas are not statistically meaningful.\" (project_cell_routed_rag_finding.md, line 23).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep the context given to a writer short and from one kind of source, because long scope notes and stacked reference blocks made outputs worse.",
   "kind": "measured",
   "found_by": "Long scope notes made a terse three-part answer format add disclaimers the judge does not reward (-9.5 points on that type). Stacking curriculum notes on top of seven real documents dropped the average from 0.502 to 0.125, with educational accuracy at zero (0/6).",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_richer_rag_per_cell_tradeoff.md",
     "lines": "38",
     "quote": "For SAQ (3 sub-questions, structured response): the verbose context confuses the response format. SAQ requires terse 2-3 sentence answers per sub-part; the boundaries text makes the model add disclaimers/scope notes that the grader doesn't reward."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_d13_inference_injection_partial_fix_2026_05_12.md",
     "lines": "18",
     "quote": "| 4 hybrid (D13 + curriculum) | 0/6 | 0.0% | **0.125** | 0.000 | **0.000** |"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_d13_inference_injection_partial_fix_2026_05_12.md",
     "lines": "32",
     "quote": "- Pick one strategy; do NOT layer"
    }
   ],
   "against": "The sample is small (\"**Rule (P0/T1; n=6 single-seed, single-model — promote to T0 after n≥30 replication):**\", feedback_d13_inference_injection_partial_fix_2026_05_12.md line 7), and long essays tolerated it: \"For LEQ: marginal benefit (1.6pp) — long-form essay tolerates verbose system prompts better.\" (project_richer_rag_per_cell_tradeoff.md, line 40).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Give a writer the official statement of what an objective includes and excludes, because near-miss items usually lack scope precision rather than facts.",
   "kind": "measured",
   "found_by": "Adding the objective, its sub-skills and its 'should not include' scope limits turned 5 of 9 stable near-miss failures into triple passes (0/27 to 17/27 scorings). A stricter judge version began failing 24-30% of multiple-choice items whose content was plausible but not aligned to the official objectives.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_richer_rag_resolves_stable_fails.md",
     "lines": "59",
     "quote": "The 4 missing fields, especially `assessment_boundaries`, are what convert soft 0.8 fails to passes. The grader rubric and the boundaries text are likely both authored from the same canonical CB scope spec — so injecting boundaries into the system prompt aligns the model output with the exact slice the grader rewards."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_richer_rag_resolves_stable_fails.md",
     "lines": "56",
     "quote": "- `assessment_boundaries` (the killer field — explicit \"should NOT include X\" scope guard)"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_mcq_v2.5.6_rubric_tightening.md",
     "lines": "21",
     "quote": "Models that generate plausible-but-not-canonical content trip the new check."
    }
   ],
   "against": "The same context hurt a terse format (\"For SAQ (3 sub-questions, structured response): the verbose context confuses the response format.\", project_richer_rag_per_cell_tradeoff.md line 38). The gain may partly reflect aligning output to the judge's own source (line 59 above). For one course the scope fields were themselves model-written: \"| Curriculum dataset | Had LLM-fabricated fields (APEURO assessment_boundaries, common_misconceptions, expanded_LOs all Haiku-generated) |\" (reference_external_ib_v253_at_10.md, line 26).",
   "adds_to_existing": [
    57,
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check that each generated question asks for the reasoning skill its objective requires, because a task framing borrowed from another item type can silently replace that skill.",
   "kind": "measured",
   "found_by": "When document-based essays dominated the examples, essay prompts for objectives that require change-over-time reasoning defaulted to comparison framing ('Evaluate the extent to which X and Y differed'), with 21 alignment failures in two such objectives. A separate generator restricted the skill each question tests to a closed list.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_cross_cell_skill_assignment_pattern_transfer_during_chain_sft_2026_06_02.md",
     "lines": "13",
     "quote": "- POST-v92 chain-step: n=500 LEQ verdict showed 76% pass with curriculum_alignment failures concentrated in 2 KCs (KC-1.2.III.C: 12 fails, KC-1.2.II.D: 9 fails — both rubric-require CCOT)"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_cross_cell_skill_assignment_pattern_transfer_during_chain_sft_2026_06_02.md",
     "lines": "14",
     "quote": "- Failure pattern: v92 generates LEQ prompts that DEFAULT TO Comparison framing (\"Evaluate the extent to which X and Y differed\") for KCs requiring CCOT, because the model learned that \"evaluate the extent\" framing from the DBQ block's gradient pressure"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-ap-social-studies-generator-python/memory/MEMORY.md",
     "lines": "22",
     "quote": "2. Added `skill_tested` enum constraint [\"sourcing\",\"causation\",\"comparison\"] in both schemas"
    }
   ],
   "against": "The essay 'regression' behind this rule came from a judge that under-credited essays: \"- LEQ: Gemini under-credits (95% IB vs 76% Gemini = +19pp gap; opposite direction). Treat Gemini-LEQ verdicts as a lower bound.\" (feedback_gemini_ib_dbq_judge_divergence_97pp_2026_06_02.md, line 25). The repair was later listed among actions taken on a false verdict: \"my Block A LEQ recovery directed at LEQ \"regression\"\" (feedback_n100_gemini_promote_must_have_ib_canonical_confirmation_2026_06_02.md, line 12).",
   "adds_to_existing": [
    58
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Read the checker's own code to learn exactly what it grades and parses, and match each item type's output structure (keys, casing, nesting) to it, verified in code before producing at scale.",
   "kind": "measured",
   "found_by": "Changing the part labels of a three-part answer format from lowercase nested objects to uppercase strings dropped that type from 90% to 16.7%. Output the checker could not parse scored 0/150. A rule to produce answers instead of questions was reversed only after someone read the checker's code, which grades question objects and does not repair parse failures.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_per_cell_schema_must_match_fewshot_bank_chain_canon.md",
     "lines": "18",
     "quote": "**v81 SAQ collapsed -73.3pp (90% → 16.7%) after training on my Track B v2 corpus.** Root cause: 385/385 SAQ training rows used UPPERCASE A/B/C with bare-string parts, but the chain canon (fewshot_bank/by_cell/saq.jsonl) uses lowercase a/b/c with nested `{question, sample_response}` per part."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_eval_is_question_generation.md",
     "lines": "32",
     "quote": "Line 88: `parse_json_response()` — single-attempt JSON parse on raw model output. Per the constraint block at lines 13-18, parse failure counts as a fail with no repair."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_eval_is_question_generation.md",
     "lines": "56",
     "quote": "This is the v38 failure mode (262 rows of answer-format anchors → 0/150 parse_ok)."
    }
   ],
   "against": "The project held the opposite rule at the same time: \"Every SFT/DPO row must train the model to **emit the answer**, not to generate questions about content.\" (feedback_answer_format_only.md, line 7). Sometimes the checker's parser was what needed fixing: \"orch shipped a fix: enhanced `_extract_json()` that strips fences + regex-extracts `{...}` blocks as fallback.\" (feedback_gemma4_wraps_json_in_markdown_fences_default_2026_06_02.md, line 13).",
   "adds_to_existing": [
    67,
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A check that a passage supports a claim must ask whether the passage itself states it, not whether it is plausible, and 'partly supported' verdicts need their own audit.",
   "kind": "measured",
   "found_by": "Re-grading 30 stratified support labels gave 70% agreement overall and 60% on 'partly supported', with errors in both directions. The clearest error marked as fully supported a claim that needed outside knowledge, against a passage that only mentioned a related debate.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_self_rag_label_audit_rebuild_trigger.md",
     "lines": "26",
     "quote": "| **partially** | **60%** | 10 | **<80% → REBUILD** |"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_self_rag_label_audit_rebuild_trigger.md",
     "lines": "41",
     "quote": "The partially class is **bidirectionally noisy** — 2 cases pulled UP to \"fully\" (Quill under-rated), 2 cases pulled DOWN to \"no\" (Quill over-rated)."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_self_rag_label_audit_rebuild_trigger.md",
     "lines": "50",
     "quote": "- Atlas verdict: \"no\" — paragraph mentions debate over treatment, NOT conversion to Christianity. Span injects fact requiring outside knowledge."
    }
   ],
   "against": "The re-grader was itself lenient on one class: \"The \"no\" class is asymmetrically lenient on Atlas's side (3 pulled \"no\" → \"partially\", 0 the other way), consistent with 3.1-pro slightly more accepting of thematic-but-not-literal entailment.\" (same file, line 43). Only 10 spans were checked per class.",
   "adds_to_existing": [
    5,
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Generate an item whose questions share one source in separate steps (the source first, then the questions written on it), and keep extra steps only if they measurably help.",
   "kind": "measured",
   "found_by": "For question sets sharing one source, a clean two-step pipeline (source, then questions) passed 8/10. Chaining the source to the writer's own research notes passed 6/10, and an extra distractor step added nothing (8/10). The project credited much of a stronger generator's 93-99% to splitting complex items into 3-7 steps.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}/memory/session_20260422_grpo_to_pipeline.md",
     "lines": "133",
     "quote": "5. **The multi-step pipeline is the architecture insight.** Gemini achieves 93-99% not because it's a better model, but because it breaks complex tasks (MCQ_SET, DBQ) into 3-7 complementary steps. sft-v4 needs the same scaffolding."
    },
    {
     "path": "~/.claude/projects/{home}/memory/mcq_set_improvement_log.md",
     "lines": "31",
     "quote": "- **Result: 80% (8/10)** — best so far"
    },
    {
     "path": "~/.claude/projects/{home}/memory/mcq_set_improvement_log.md",
     "lines": "27",
     "quote": "- Problem: stimulus chained to potentially hallucinated research sources"
    }
   ],
   "against": "\"- **Result: 80% (8/10)** — no improvement from distractor step\" and \"- Added complexity without benefit; removed\" (mcq_set_improvement_log.md, lines 38-39). Each approach was tried on 10 items.",
   "adds_to_existing": [
    61
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Use example items to show a writer the format, not to fix its facts, because examples shape structure but did not improve factual accuracy.",
   "kind": "measured",
   "found_by": "In a 9-variant prompt sweep with 20 items each, adding examples gave 40% passes and 55% factual accuracy against 45% and 60% for the baseline. Removing the format specification dropped passes to 5%. The literature review cited in the project reached the same conclusion, without DOIs.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}/memory/sft_v4_prompt_engineering.md",
     "lines": "24",
     "quote": "4. fewshot: 40% pass, 55% — examples don't help"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "67",
     "quote": "ICL works via format/distribution; refutes \"few-shot fixes DBQ veracity\"; lifts mcq_set/saq +3-8pp at K=3 with chat-template-aligned demos."
    },
    {
     "path": "~/.claude/projects/{home}/memory/sft_v4_prompt_engineering.md",
     "lines": "26",
     "quote": "6. bare (no schema): 5% — model requires format spec"
    }
   ],
   "against": "Examples did lift pass rates on some types through format (\"lifts mcq_set/saq +3-8pp at K=3 with chat-template-aligned demos\", MEMORY.md line 67), and the sweep was small: \"Exhaustive 9-variant prompt engineering sweep on sft-v4 (Fireworks: accounts/trilogy/deployments/kh9mkdob), APUSH Unit 7, N=20 per variant.\" (sft_v4_prompt_engineering.md, line 7).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Report the quality of the single draft that will actually be delivered, and treat best-of-several scores as a ceiling or a diagnostic, not as the product's quality.",
   "kind": "adopted rule",
   "found_by": "Picking the best of 8 drafts by the judge's own score reached 99.3% against 89.3% for one draft. But it multiplied judging cost, ran at about 1.8 items a minute, and picked winners by the same metric being reported. The project ruled that only single-draft numbers count toward the goal.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v35_bon_k8_99pct_canonical.md",
     "lines": "25",
     "quote": "1. **This does NOT count toward APUSH 95% goal.** Per `feedback_k1_only_for_goal.md`, K=1 only counts. K=8 is decode-time + grader-as-reward = worst-case Goodhart configuration."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_k1_only_for_goal.md",
     "lines": "52",
     "quote": "- BoN numbers are footnotes only (e.g., \"K=8 ceiling: X% — for context, doesn't count toward 95% goal\")"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_full_cost_accounting_no_zero_marginal_lie.md",
     "lines": "44",
     "quote": "| Throughput | ~1.8 prompts/min — infeasible at classroom scale |"
    }
   ],
   "against": "The project later chose a ranked best-of-several pipeline as its product path: \"product-bar via grounded-ranker + best-of-N + deterministic-compiler is the live path to 99% without raw model winning.\" (project_stand_down_single_owner_2026_06_10.md, line 15).",
   "adds_to_existing": [
    24,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Record the source of every field, not just every record, because one record can mix official curriculum text with model-written fields such as misconceptions and scope notes.",
   "kind": "adopted rule",
   "found_by": "A curriculum service tagged provenance per record, while for one course its official objective statements sat beside model-generated misconceptions, scope boundaries and expanded objectives. Later builds had to filter out records whose misconceptions were model-generated, and an earlier mixed training file could not be split by source.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "119",
     "quote": "Curriculum API merge_source is record-level; same record mixes CB-canonical statement with Haiku-generated misconceptions/assessment_boundaries."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/reference_external_ib_v253_at_10.md",
     "lines": "26",
     "quote": "| Curriculum dataset | Had LLM-fabricated fields (APEURO assessment_boundaries, common_misconceptions, expanded_LOs all Haiku-generated) |"
    },
    {
     "path": "~/.claude/projects/{home}/memory/training_data_audit_20260423.md",
     "lines": "27",
     "quote": "- Cannot separate Gemini vs Fireworks at record level without source metadata"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before adopting one source for a course's curriculum facts, compare the candidate sources by content overlap and by whether their unit labels match the official framework, and merge them when they overlap little.",
   "kind": "measured",
   "found_by": "A content-overlap analysis across three courses found one where two candidate sources barely overlapped (39% / 99.8% non-overlap), so either alone dropped much of the material. In another, the grader's bundled source had unit IDs shifted by one period, about 130 missing entries and 50 duplicates.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "116",
     "quote": "**APUSH** = MERGE (curriculum repo skeleton + InceptBench atomic facts; 39% / 99.8% non-overlap means single-source halves pedagogy). Wrong source per course = silent training corruption."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "116",
     "quote": "**APEURO** = curriculum repo (InceptBench IDs off-by-one-period from CB CED; need ID switch + backfill ~130 missing + dedupe 50 dupes)."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-oracle/memory/project_oracle_session_20260501.md",
     "lines": "12",
     "quote": "RECONCILIATION ruling per course (APEURO=curriculum-repo, APWH=InceptBench, APUSH=MERGE)"
    }
   ],
   "against": "The shifted labels did not reach the service used for generation (\"Atlas 30/30 PASS (zero APEURO off-by-period drift in canonical API; InceptBench bug did NOT propagate).\", MEMORY.md line 82), and the merge was never checked end to end: \"— md5 diff never run; potential silent divergence.\" (project_oracle_session_20260501.md, line 26).",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before declaring a unit or topic short of material, or building from 'the part of a collection about X', count what the collection actually holds for X after normalising its labels.",
   "kind": "measured",
   "found_by": "Two units looked short until descriptive era labels were mapped to unit numbers, which moved them to margins of +361k and +482k tokens with no new material. A collection assumed to contain a unit-1 slice had none, which would have silently produced a smaller set reported as complete.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_audit_normalization_before_declaring_gap_2026_05_22.md",
     "lines": "9",
     "quote": "Adding an `ERA_LABEL_TO_UNIT` dict moved Unit 7 from gap-status to +361k margin and Unit 8 from gap to +482k margin — without ingesting a single new token."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_verify_subset_exists_before_filter.md",
     "lines": "12",
     "quote": "The implied assumption: fewshot_bank's 3,806 rows contain a U1 slice. **It does not.** Unit distribution audit:"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_verify_subset_exists_before_filter.md",
     "lines": "23",
     "quote": "Had I scripted on the assumption, the consolidator would have silently produced ~468 rows (Track B only) but reported the manifest as if it included fewshot_bank — misleading downstream consumers (main-a, training spec authors)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Record a finding as shared knowledge only when it transfers to other work, is not obvious, rests on repeat evidence, fits in a paragraph and is not already recorded, and state it as a rule that says what makes it non-obvious rather than as the story of the incident.",
   "kind": "adopted rule",
   "found_by": "A shared learnings store filled with more than 119 low-value entries and was reported as '67 learnings, 0 insights'. The project then adopted a five-test usefulness bar (transferable, non-obvious, n≥30 or a confirmed mechanism, one paragraph, not redundant), rule-not-story phrasing, and an explicit non-obviousness marker for strategic claims.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_synapse_scarce_useful_only.md",
     "lines": "32",
     "quote": "3. **Reproducible OR statistically backed** — n≥30 evidence, or a documented mechanism with at least one confirming trial."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_three_rule_updates_20260506.md",
     "lines": "21",
     "quote": "**How to apply:** When publishing to Synapse, write \"rule: ...\" not \"we found ...\". If the principle came from a specific incident, the principle stands on its own without the incident."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_synapse_dok3_non_obvious_marker_2026_05_12.md",
     "lines": "48",
     "quote": "Do NOT use generic markers like \"novel finding\" or \"research-grade\". Be specific about the inversion / surprise / hidden constraint."
    }
   ],
   "against": "A companion rule strips the numbers that make a finding checkable: \"**Rule:** Cross-project Synapse records share methodology, patterns, anti-patterns, thresholds, and rules-of-thumb. They do NOT share specific pass-rates, regressions, costs, or any number that would embarrass the team.\" (feedback_synapse_no_unfavorable_numbers_2026_05_12.md, line 17).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Rank recorded findings by strength of evidence rather than recency, count one as measured only with at least 30 items or repeated confirming runs, and link every superseded finding to its replacement.",
   "kind": "adopted rule",
   "found_by": "The project's memory index must be sorted by priority and evidence tier, never by date. Top-tier evidence requires n≥30 or repeated confirming runs, superseded and retracted entries stay listed and point to their successors, and a full audit re-weighed every entry.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "4",
     "quote": "> Index sorted by **priority then evidence tier**, NOT by date. Recency is a tiebreaker only."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "13",
     "quote": "4. T0 evidence requires actual measurement on our data (n ≥ 30 OR multiple confirming runs)."
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "12",
     "quote": "3. Every `superseded` entry has at least one other entry whose `supersedes:` list contains it."
    }
   ],
   "against": "A top-tier finding on 297 items was later retracted as noise: \"audit_note: T0 — apples-to-apples on n=297, both models scored on same IB v2.5.3 with same prompts. v35 wins single-shot.\" (project_v35_self_rag_wins_canonical.md, line 12), retracted at MEMORY.md line 38. Item count alone did not make the finding true; repeated runs did the work.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Open question: does forcing a strict output schema on a writer buy structural compliance at the cost of quality in its free-text parts?",
   "kind": "open question",
   "found_by": "Schema-constrained output gave 5/5 structurally valid document-based items against 0/5 in plain structured-object mode. The research cited in the project reports large losses on reasoning tasks under strict structured-output modes, and the project kept strict modes off for free-form item types.",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "29",
     "quote": "- `json_schema`: **5/5 = 100% structural compliance**"
    },
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "30",
     "quote": "- `json_object`: **0/5 = 0% structural compliance**"
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "63",
     "quote": "JSON mode loses 25-63pp on reasoning tasks; per-cell decision; default OFF for free-form cells."
    }
   ],
   "against": "Five items only (\"Diagnostic: 5 DBQ items:\", findings_sftv7_20260424.md line 28); the research is cited in these notes without a DOI or URL.",
   "adds_to_existing": [
    67
   ],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v39_dataset_corruption_smoking_gun.md",
   "lines": "25",
   "quote": "- A: 64.5% (189) — vs expected 25%"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v39_dataset_corruption_smoking_gun.md",
   "lines": "37",
   "quote": "Defect 2 → degrades `distractor_quality` + `difficulty_alignment` (2/11 dimensions) because the model learns answer-position bias real AP exams don't have."
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v39_dataset_corruption_smoking_gun.md",
   "lines": "56",
   "quote": "3. Enforce uniform answer distribution at row-emit time for MCQ/MCQ_SET (rotate correct-answer position deterministically across A/B/C/D)"
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v39_dataset_corruption_smoking_gun.md",
   "lines": "35",
   "quote": "Defect 1 → degrades `curriculum_alignment` + `factual_accuracy` + `educational_accuracy` (3/11 IB dimensions) because the model is being trained to generate questions for AP KCs that don't exist."
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v39_dataset_corruption_smoking_gun.md",
   "lines": "21",
   "quote": "- non-canonical (opaque hashes like `c_4EvW`, `s_saxW`): 803 rows (77.5%)"
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_stacked_decode_RAG_judge_result.md",
   "lines": "53",
   "quote": "Gemini probably defaulted to <0.85 on anything it couldn't decisively grade. Format mismatch, not Goodhart."
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_stacked_decode_RAG_judge_result.md",
   "lines": "73",
   "quote": "- **Future judge runs:** build per-format rubrics for mcq_set + dbq (decompose into sub-questions / sub-rubric-items) before re-running held-out."
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_stacked_decode_RAG_judge_result.md",
   "lines": "51",
   "quote": "- My single-prompt JSON rubric (\"factual_accuracy 0-1, overall 0-1\") can't decompose those"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/session_20260422_grpo_to_pipeline.md",
   "lines": "44",
   "quote": "**LESSON:** Always test the raw rollout format, not the production pipeline format. They are different paths."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_grader_variance_discovered.md",
   "lines": "57",
   "quote": "LLM-as-judge is non-deterministic at any temperature > 0 OR even at temp=0 (small variance from server-side batching, KV-cache timing, random sampling fallback paths). Single-call evaluation is unreliable."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_self_rag_full_build_clean.md",
   "lines": "47",
   "quote": "**IsUse is degenerate** (essentially all maxed). gpt-4o-mini IsUse classifier collapsed to ceiling."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/project_v60_partial_stimfab_insufficient_2026_05_13.md",
   "lines": "53",
   "quote": "Spot-check 1-2 rejected samples per type to verify IB grader actually fails them (open API call), otherwise discard the corruption type."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_save_everything_always.md",
   "lines": "38",
   "quote": "- v29's 63.64% baseline could be re-scored on 2.5.3 because we kept the gen file — but only because we happened to save it; rule wasn't explicit"
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/mission_aim_98_floor_95.md",
   "lines": "72",
   "quote": "Mitigation: R30 factuality battery (FActScore-on-AP-bios) as the parallel held-out scorer. Alarm fires at IB-vs-FActScore drift ≥3pp."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_mcq_v2.5.6_rubric_tightening.md",
   "lines": "9",
   "quote": "What scored 100% on v2.5.3 now hits 24-30% zero-rate on v2.5.6 — this is the rubric driver of the ~25pp aggregate mcq drop."
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_apush_only_eval.md",
   "lines": "26",
   "quote": "3. Save APUSH and APWH summaries separately. Don't compute \"aggregate\" pass rate — it's misleading."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_result_tagging_discipline.md",
   "lines": "9",
   "quote": "Without per-record provenance, you can't filter, can't bisect quality regressions to a source, can't selectively re-ingest."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_curriculum_enrichment_mandatory_2026_05_11.md",
   "lines": "21",
   "quote": "- Manifest entries: record `curriculum_api_version`, `n_hits_per_row`, `query_used` per row for auditability."
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
   "lines": "58",
   "quote": "Replaced with categorical-only mandate: no names, dates, events in scoring_notes."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/recipe_track_b_openstax_pair_generation.md",
   "lines": "64",
   "quote": "Audit found 0 confirmed fabrications across 1,200 rows; 3 false-positive flags (1 noun-phrase mis-match, 2 missing-from-whitelist real historical works)."
  },
  {
   "truth": 57,
   "effect": "counter",
   "path": "~/.claude/projects/{home}/memory/sft_v4_prompt_engineering.md",
   "lines": "25",
   "quote": "5. facts alone: 40% pass, 44% — hurts factual_accuracy"
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/stage2_postmortem.md",
   "lines": "17",
   "quote": "Stage 2 generates valid, coherent, well-formed AP content — for the WRONG topic. It ignores `topic`, `time_period`, `unit`, and `qtype` constraints and picks its own topic. Examples:"
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/stage2_postmortem.md",
   "lines": "22",
   "quote": "The content is factually correct about the wrong thing."
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/continuous_improvement.md",
   "lines": "41",
   "quote": "- No HARD FAIL dimension < 1.0"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
   "lines": "95",
   "quote": "every text field in any new corpus must trace to a primary source; LLMs are tools (search/OCR/reformat) not content authors; drop-don't-patch when sources fail."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/continuous_improvement.md",
   "lines": "48",
   "quote": "- `answer_validity` — MCQ must have exactly 1 correct answer"
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/stage2_postmortem.md",
   "lines": "29",
   "quote": "- Why wrong: average scores were identical (0.833 vs 0.836). If facts were degraded, avg scores would diverge."
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/stage2_postmortem.md",
   "lines": "30",
   "quote": "- Caught by: per-item comparison showing 9 regressions were all correct-content-wrong-topic, not wrong-facts-right-topic."
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/project_v50_v56_strategy_with_numbers_2026_05_12.md",
   "lines": "83",
   "quote": "v51 was trained on v50's *ungraded* gens before v50 had a verdict. Result: v51 inherited v50's weaknesses + degraded on saq −8.9pp and mcq −10pp."
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/mcq_set_improvement_log.md",
   "lines": "27",
   "quote": "- Problem: stimulus chained to potentially hallucinated research sources"
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/stage2_postmortem.md",
   "lines": "37",
   "quote": "- Tested: CC added explicit constraint reinforcement (caps, repetition, \"DO NOT substitute\"). Failures persisted."
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/project_v61_broadfab_falsified_2026_05_13.md",
   "lines": "34",
   "quote": "Real-source training data (like D13 for DBQ) works because it gives the model REAL examples to imitate, not synthetic anti-examples to avoid."
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/team_learnings_20260422.md",
   "lines": "69",
   "quote": "- 0.01 weight on bad items helped eliminate questions that reference missing images"
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/team_learnings_20260422.md",
   "lines": "60",
   "quote": "- Don't train inline SVGs — generate image configs with known interfaces instead"
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_bon_k8_huge_lift.md",
   "lines": "44",
   "quote": "DBQ is structurally different: 7 primary documents per stimulus + 6-paragraph essay + multi-document analysis. Single-shot v29 was at 27% DBQ; even K=8 BoN only gets to 67%."
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_quill_discovery_cross_model_volatility_2026_05_11.md",
   "lines": "30",
   "quote": "for the 93% volatile items, decode-time sampling depth matters; for the 7% hard items, no depth helps."
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/mcq_set_improvement_log.md",
   "lines": "57",
   "quote": "4. **Multiple retry attempts** — masks quality issues instead of fixing them"
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_bon_k4_huge_lift.md",
   "lines": "46",
   "quote": "**21/24 (88%) agreed.** Mean IB BoN-pick = 0.949, mean Claude judge = 0.889."
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_full_cost_accounting_no_zero_marginal_lie.md",
   "lines": "45",
   "quote": "held-out judge says 49.2% pass rate vs IB's 92.3% on same RAG run. **43.1pp gap quantifies the contamination.**"
  },
  {
   "truth": 66,
   "effect": "counter",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_stacked_decode_RAG_judge_result.md",
   "lines": "48",
   "quote": "This is NOT actual quality failure across all 240 mcq_set + dbq outputs — that's implausibly bad. It's the **judge rubric being too generic** for complex multi-part outputs:"
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/research_best_of_n_decode.md",
   "lines": "24",
   "quote": "- If held-out-judge lift << IB-only lift → we're reward-hacking; back off K"
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/project_v50_v56_strategy_with_numbers_2026_05_12.md",
   "lines": "80",
   "quote": "Test whether curriculum_context (v52b primary) is necessary, or whether D13 alone (v52 control) suffices. If v52 ≥ v52b → curriculum is redundant. If v52b > v52 → curriculum is doing real work."
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/recipe_track_a_b_kc_pack_substitution.md",
   "lines": "32",
   "quote": "3. **Keep the Gemini-generated `prompt`** (analytical DBQ stem) — Gemini is good at writing those. **Replace only the `documents`** — that's where the synthesis-vs-real-source distinction lives."
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_misconceptions_user_prompt_injection_hurts_2026_05_12.md",
   "lines": "29",
   "quote": "- **For grader-side:** misconceptions field belongs in IB rubric (used to verify distractor variety) — already where the v2.5.6 grader uses them."
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/mcq_set_improvement_log.md",
   "lines": "11",
   "quote": "**Impact**: The Research→Compile pipeline NEVER WORKED for either MCQ or MCQ_SET. Both silently fell back to legacy generation paths every time. The research step was designed to gather verified primary sources and plausible alternatives, but it always crashed before it could run."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_eval_contamination_check_all_eval_files.md",
   "lines": "20",
   "quote": "Had I trained on those rows, v54 would have learned its eval set verbatim → fake pass rate, contamination, useless iteration. Caught before training; saved the cycle."
  }
 ]
}
```
