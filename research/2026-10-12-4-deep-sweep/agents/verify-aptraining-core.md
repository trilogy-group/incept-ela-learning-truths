# verify:aptraining-core

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "aptraining-core",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "All quotes verbatim at the cited lines and numbers match. The swing was the same 297 generations re-scored (63.64% vs 89.56%), so 'the same items' holds; added the analytics line that says so directly. The v2.5.6 file compares 30 rows at 100% on the old grader with 76.7/80.0/70.0% across three runs on the new one, driven mainly by one dimension (educational_accuracy -0.244, plus -0.089 on a second). General to any automated judge. Related to truth 45 and to candidate 28, not the same claim.",
   "statement": "Record the grader's version with every score and compare only scores from the same version; the same items moved 25.92 points when the grader version changed.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/coordination/.archive/CLONE_VERIFY_GRADER.md",
     "lines": "12",
     "quote": "- **+25.92pp swing from grader version alone**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/analytics.md",
     "lines": "18",
     "quote": "Same v29 generations score 63.64% on v2.4.0 but 89.56% on v2.5.3 (+25.92pp from grader change alone).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/forensics/mcq_v2.5.6_rubric_tightening.md",
     "lines": "6",
     "quote": "v50 r1/r2/r3 v2.5.6: ~30 mcq rows each (76.7%, 80.0%, 70.0% pass on NEW grader)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_main_session_close/02_CONSOLIDATED_STATE.md",
     "lines": "135",
     "quote": "| ONLY IB v2.5.3 | All historical comparisons require explicit grader-version tagging; some \"regressions\" may be artifacts | `feedback_ib_grader_version_v240_to_v253.md` |",
     "verbatim": true
    }
   ],
   "against": "Pinning the version is necessary but not sufficient: \"Same generations re-scored produce 17pp per-cell variance, ~1-2pp aggregate variance.\" (helpers/shadow/output/analytics.md line 12). The version change also moved scoring to a different grader endpoint, so 'version alone' bundles both.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim and numbers match (17pp per-cell; sigma 5.09pp at T=0 with 6 of 30 prompts disagreeing; 0.87 vs 0.73). Extended the analytics quote to the thresholds the project set from that measurement (per-cell deltas under 5pp and aggregate under 3pp treated as noise), which supports the second half directly, and added the line showing a second draw flipped a 'best profile' decision. The seed file blames the T=0 disagreement most likely, not certainly, on judge non-determinism. Turns truth 34 (verdicts vary) into an operating rule; not a duplicate.",
   "statement": "Re-score identical items several times to find the judge's noise floor, and treat any difference smaller than that floor as no difference.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/analytics.md",
     "lines": "12",
     "quote": "Same generations re-scored produce 17pp per-cell variance, ~1-2pp aggregate variance. **Per-cell deltas <5pp are noise. Aggregate deltas <3pp are noise.**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/forensics/mcq_seed_variance_diff.md",
     "lines": "5",
     "quote": "v50 mcq seed σ = 5.09pp at T=0 (should be 0 if deterministic).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/KNOWN_ISSUES.md",
     "lines": "260",
     "quote": "**Symptom**: LEQ exam_precision pass rate was 0.87 on one draw, 0.73 on another. Single-draw \"LEQ exam_precision is best\" claim was wrong.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/system_improvement_brainstorm.md",
     "lines": "15",
     "quote": "**Value**: HIGH. The single-draw → 2-draw step already flipped SAQ's best profile (exam_precision → tight_alignment).",
     "verbatim": true
    }
   ],
   "against": "Aggregates can look steady while item types swing: \"Variance σ < 1pp across seeds — stable, reproducible measurement.\" (crystal full-copy/aptraining-root/achieved.md line 83), while document-based items in the same table ran 6, 7 and 9 of 30 across the three seeds.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim and numbers match, but the second clause's example does not hold. The '-0.88 continuous' reading for v36b came from comparison against stored baseline generations and turned into a gain once the baseline was regenerated (CONSOLIDATED_STATE line 138: 'Several regressions reverse to real lifts'; the underlying memo gives -0.88 to +0.80). Rewrote the example to the paired-test finding that does hold: a +1.33-point lift resting on 12 discordant items out of 150, split 5/7, p = 0.7744. Replaced the line-137 evidence with the protocol line that makes paired continuous deltas the decision rule. Kept the published-paper citation as external support.",
   "statement": "Decide between two versions item by item on the same items, using the continuous score and a paired test; a pass-rate gain can be noise, as when a +1.33-point lift rested on 12 changed items out of 150, split 5 against 7 (p = 0.7744).",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/03_R41D_implementation.md",
     "lines": "20",
     "quote": "Binary pass/fail at threshold 0.85 stays as a *secondary* report. Decisions get made on continuous-mean deltas with paired tests.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/audits/v35_pressure_test/feedback_v35_within_noise.draft.md",
     "lines": "21",
     "quote": "- Paired McNemar on the same 150 APUSH prompts under the same canonical grader (IB v2.5.3): b=5 (v29-only passes), c=7 (v35-only passes), exact two-sided p = **0.7744**.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/audits/v35_pressure_test/feedback_v35_within_noise.draft.md",
     "lines": "21",
     "quote": "No version of \"more samples might tighten this\" survives — the per-row contingency only has 12 disagreements out of 150, and their direction is split 5/7.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/03_R41D_implementation.md",
     "lines": "28",
     "quote": "| M1 | Card, Henderson, Khandelwal, Jia, Mahowald, Jurafsky. *With Little Power Comes Great Responsibility.* EMNLP 2020. | NLP benchmarks routinely under-powered; advocates continuous metrics + paired tests over binary accuracy at small n. Direct fit for our n=30 per cell. |",
     "verbatim": true
    }
   ],
   "against": "Small effects still need many items: \"5. **Power note:** at n=30 per cell and observed SD ≈ 0.15, paired-t detects Δ ≥ ~0.05 with 80% power. Smaller effects need n≥120 per cell — relevant if you want to distinguish CoVe from no-op at 1pp lift.\" (03_R41D_implementation.md line 440). The continuous score is also more sensitive to generation variance, so it needs a regenerated baseline: \"| Fresh baseline rule | Several \"regressions\" reverse to \"real lifts\" with proper baseline |\" (02_CONSOLIDATED_STATE.md line 138).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep-with-fix",
   "reason": "Quote verbatim at line 449. It is a prescribed step in an implementation spec; no record of the smoke test being run was read, so 'adopted rule' fits. Softened 'means the measuring setup is broken' to 'signals', since at alpha 0.10 one false positive can occur by chance; the source's own diagnosis is a wrong pairing key. Added line 450, which puts the self-comparison before any real comparison. Related to truth 38 (prove a check on a planted fault), not a duplicate.",
   "statement": "Before comparing two versions, compare one version with itself; a 'significant' difference in that self-comparison signals a broken measuring setup, such as items paired wrongly.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/03_R41D_implementation.md",
     "lines": "449",
     "quote": "4. Smoke test: compare v29 baseline against itself with a different seed run. Expect `per_cell.*.significant_at_alpha == false` everywhere; `mean_diff_overall ≈ 0`. If false-positives appear under self-comparison, the pairing key is wrong — check (row_id, cell) keying.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/03_R41D_implementation.md",
     "lines": "450",
     "quote": "5. Only then run a real comparison (e.g., v29 vs v29+CoVe).",
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
   "reason": "Both quotes verbatim (CONSOLIDATED_STATE line 138; coordination HANDOVER line 102). The underlying memo (not cited, its path carries a user name) confirms the mechanism: on the same 150 prompts and model, fresh generations scored 0.9307 continuous against 0.9475 for stored ones, so new configurations compared with stored output looked worse; v36b moved from -0.88 to +0.80. The rule is scoped to continuous comparisons. General.",
   "statement": "Regenerate and re-score the baseline under the same conditions as the new version; comparing new output with stored old output made gains look like regressions.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_main_session_close/02_CONSOLIDATED_STATE.md",
     "lines": "138",
     "quote": "| Fresh baseline rule | Several \"regressions\" reverse to \"real lifts\" with proper baseline | `feedback_baseline_must_be_fresh_gen.md` |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/coordination/HANDOVER.md",
     "lines": "102",
     "quote": "7. Fresh-gen baseline for continuous comparisons",
     "verbatim": true
    }
   ],
   "against": "Scoped by the source to continuous-score comparisons (\"7. Fresh-gen baseline for continuous comparisons\", coordination/HANDOVER.md line 102); binary pass rates did not show the bias.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (01_HANDOVER lines 66 and 68; THELOOP line 753). The second clause garbled the example: the cited 'collapse' figure (73.33%) had no result file at all, and the only v39 file came from a run that never ran (0/150 in 8 ms, empty prompts); a later review judged the regression real on other grounds (against). Rewrote to state both phantom cases accurately. General provenance rule; not truth 24.",
   "statement": "Act on a quality number only if it traces to a stored result file from a run that really generated and scored the items; a baseline cited across five-plus memos had no file behind it, and the only file behind one cited collapse was a run that took 8 ms on empty prompts.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/THELOOP.md",
     "lines": "753",
     "quote": "1. **Shadow T8 phantom** (2026-05-06T0005Z) — v29 baseline 0.8667 was being cited across 5+ memos including v42/v40h FINAL verdicts; citation trail terminated at \"historical\" with no on-disk file at canonical schema.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_main_session_close/01_HANDOVER.md",
     "lines": "66",
     "quote": "- The only v39 summary file shows 0/150 with **8ms elapsed** — eval never actually ran",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_main_session_close/01_HANDOVER.md",
     "lines": "68",
     "quote": "- Eval harness was sending **empty user prompts**, model responded with chatbot fallback",
     "verbatim": true
    }
   ],
   "against": "A missing file does not prove the claim false: \"**Reality:** the only v39 summary in `workspace/eval/runs/` does show 0/150 with 8ms elapsed — true. But the regression IS real per 0758Z REFRESHER (\"v39 catastrophic, v40 empty outputs, both auto-deleted by Fireworks\").\" (handover/2026-05-01_session_end/SHADOW_HANDOVER.md line 127).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; numbers match (4,800 instant 401s; 29/150 score errors; -26.7pp). The four-way split comes from the run backlog (infra, contract, content, variety), now cited. Dropped 'unparsed outputs' from the missing-evidence list: output the generator returns in the wrong shape is a contract failure of the delivered item, not missing evidence (see against). Corrected the selector-takeaways citation to lines 28-29 (rule heading plus evidence). Adds to truth 9 without duplicating it.",
   "statement": "Sort every failed item into infrastructure, format, content or variety failure before computing a pass rate; timeouts and authentication errors are missing evidence, not bad items.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/evidence/FUTURE_RUN_IMPROVEMENT_BACKLOG_20260521.md",
     "lines": "147",
     "quote": "Infra failures should not be analyzed as content quality.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/evidence/FUTURE_RUN_IMPROVEMENT_BACKLOG_20260521.md",
     "lines": "149-154",
     "quote": "Future run classification should first split: … `infra_failure`: model 404/502, timeout, auth, Render cold start, Gemini timeout. … `contract_failure`: response shape invalid for OpenAPI/IB. … `content_failure`: IB evaluated content and failed. … `variety_failure`: passable but static/reused.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/SELECTOR_CALIBRATION_TAKEAWAYS_20260520.md",
     "lines": "28-29",
     "quote": "6. Timeouts are evidence gaps, not content failures. - Evidence: first calibration smoke marked DBQ as 0.0 because local IB timed out, while existing winner scores showed the same rows passed.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/.agent/memory/feedback_check_score_phase_duration.md",
     "lines": "29",
     "quote": "The script masked this as per-row scoring errors (`ib_overall=None`, `ib_hard_fails=[\"ib_http_401\"]`) instead of aborting on systemic failure.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/coordination/RESULTS.md",
     "lines": "71",
     "quote": "**mcq_set diverges by -26.7pp** in clone's run — driven by `n_score_err=29/150` in clone's scoring pass, almost certainly concentrated on mcq_set (avg_overall=0.179 implausibly low otherwise; auto-zeroed errors deflate that cell).",
     "verbatim": true
    }
   ],
   "against": "Format failures still count against what is delivered: \"8. OpenAPI shape must be enforced at the boundary.\" (crystal full-copy/parallel-ideas-lab/reports/WEEKLY_APUSH_PIL_REPORT_20260520.md line 498).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (v35 audit line 22; CONSOLIDATED line 86; R42 line 140). The audit shows the +1.33-point lift was within noise (p = 0.7744) and the trained mechanism appeared in 0 of 297 outputs, so the gain did not 'come from' the change; reworded to say it was credited to a mechanism that never showed up. General; different object from truth 38.",
   "statement": "Before crediting a change with a gain, check that it actually took effect in the outputs; one claimed gain was credited to a mechanism that showed up in none of 297 outputs.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/audits/v35_pressure_test/feedback_v35_within_noise.draft.md",
     "lines": "22",
     "quote": "- All 297 v35 generations under vanilla `oneshot_generate.py`: zero `[Retrieval=...]`, zero `[IsRel=...]`, zero `[IsSup=...]`, zero `[IsUse=...]`, zero `<paragraph>...</paragraph>`.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_main_session_close/02_CONSOLIDATED_STATE.md",
     "lines": "86",
     "quote": "| **v35 Self-RAG SFT** | 92.26% / 89.33% APUSH on canonical (looked like +1.33pp lift) | **RETRACTED** — McNemar p=0.7744, 0/297 reflection-token emission, mechanism never fired | Self-RAG vocab-extension is non-optional; \"lift\" was grader noise + threshold artifact |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/02_R42_CoVe_DBQ_spec.md",
     "lines": "140",
     "quote": "Log the `stage` (`revise` / `draft_fallback` / `no_block`) per item in the score record so we can quantify how often the verification phase actually fired.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; the re-test line of the den quarantine note is line 5, and line 4 holds the 172/180 = 95.56% claim, now quoted. The '10 to 87 points' range was loose. The comparison table shows drops of 12 (86 to 74), 36 (100 to 64), 10 (100 to 90) and 87.5 (87.5 to 0, on a partial 10-item re-test), plus 85.56 (95.56 to 10); one self-test held (100 to 100, 92 strict). Rewrote with exact figures. Adds to truths 66 and 48 without duplicating them.",
   "statement": "Re-test every claimed improvement yourself on fresh items its author never saw; one self-reported 95.56% on chosen items fell to 10% on 50 fresh items, and four other self-tests fell by 10 to 87.5 points.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/quarantine/2026-05-22T1755Z_den_mcqset_50_50_proof/QUARANTINE_REASON.md",
     "lines": "4",
     "quote": "**Source claim:** 172/180 = 95.56% candidate pass on Unit-1 cherry-picked source prompts",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/quarantine/2026-05-22T1755Z_den_mcqset_50_50_proof/QUARANTINE_REASON.md",
     "lines": "5",
     "quote": "**Independent re-test:** 5/50 = **10.00%** on Unit-1 prompts from e7e1d980 (no overlap with den's 30-prompt training set)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/quarantine/2026-05-22T2120Z_cheater_exploit_003/QUARANTINE_REASON.md",
     "lines": "34",
     "quote": "| Den v6 (fresh K=2) | 10/10 = 100% | 32/50 = 64% (second_tier) |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/quarantine/2026-05-22T2120Z_cheater_exploit_003/QUARANTINE_REASON.md",
     "lines": "36",
     "quote": "| Cheater EXPLOIT-002 (stim-strip MCQ) | 32/32 = 100% | 45/50 = 90% (second_tier) |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/quarantine/2026-05-22T2120Z_cheater_exploit_003/QUARANTINE_REASON.md",
     "lines": "37",
     "quote": "| Cheater EXPLOIT-003 (phrase-anchor MCQ_SET) | 14/16 = 87.5% | 0/10 partial = 0% (**QUARANTINE**) |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/INCLUSION_CRITERIA.md",
     "lines": "24",
     "quote": "Cherry-picked subsets, single-prompt wins, and self-reported metrics from sub-agents do NOT qualify.",
     "verbatim": true
    }
   ],
   "against": "One self-test held on the hidden set: \"| Den v8 (fresh + timeout-fallback) | 50/50 = 100% | 50/50 = 100% / 46/50 = 92% strict → **VALIDATED** |\" (artifacts/quarantine/2026-05-22T2120Z_cheater_exploit_003/QUARANTINE_REASON.md line 35). The 87.5-to-0 drop rests on a partial 10-item re-test, and the independent re-tests reused one hold-out file and later counted predicted passes (see candidates 9 and 10).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Only the first three of 50 acceptance records were read. Record 1 carries ib_rating PREDICTED_PASS_CACHE_NEIGHBOR and an audit-trail decision 'predicted_pass_skip_live_ib', records 2-3 carry the same rating, and the validation note itself describes 'archetype-predictor scoring'. So the '100% STRICT FRESH' verdict counted predicted passes for at least those records. Whether all 50 were predicted is unverified. 'A cached verdict' was imprecise: the cache returned the real judge's earlier verdict on identical content, and the fault was serving cached content, so reworded.",
   "statement": "Count a pass only when the real judge scored the very item delivered; a score predicted from similar past items, or a pass earned by serving cached or pre-made fallback content, says nothing about what the generator produced.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/VALIDATION_REASON.md",
     "lines": "5",
     "quote": "**Verdict:** 50/50 = **100.0% STRICT FRESH** — zero timeout-fallback, all v80bchain fresh generation",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/VALIDATION_REASON.md",
     "lines": "28",
     "quote": "**No fallback path.** Parallel K=4 with archetype-predictor scoring. Best fresh K of 4 returned.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/den_solver_acceptance_20260523T082319Z.jsonl",
     "lines": "1",
     "quote": "\"ib_score\": 0.95, \"ib_rating\": \"PREDICTED_PASS_CACHE_NEIGHBOR\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/den_solver_acceptance_20260523T082319Z.jsonl",
     "lines": "1",
     "quote": "\"decision\": \"predicted_pass_skip_live_ib\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1830Z_den_solver_v2_online_K_N_with_cache/SECOND_TIER_REASON.md",
     "lines": "39",
     "quote": "Effective behavior: high pass rate ONLY for substandards the cache has seen before; cap_reached for novel substandards. Pass rate ≈ cache hit rate.",
     "verbatim": true
    }
   ],
   "against": "The project argued fallback passes were acceptable: \"main-a recommends YES — the cached archetype is itself derived from live-IB-validated v80bchain content, so it's not \"deterministic-from-bank\" in the prior sense.\" (artifacts/validated/2026-05-22T2116Z_den_solver_v8_FIRST_VALIDATED/VALIDATION_REASON.md line 62). Only the first 3 of 50 records of the acceptance file were read.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Added the v8 acceptance summary, which names the same input file (/tmp/holdout_for_den_v2.jsonl, line 13) and so confirms the hold-out was reused across validations, and the inclusion rule requiring re-validation on a different 50-item sample, which that reuse broke. The routing memo (line 51; also line 60, 'progressions ... closed remaining failure rows') shows repairs tuned against the hidden set. The cache clause rests on the second-tier note: 37 passes were cache hits from the same pipeline run the hold-out prompts came from.",
   "statement": "Keep held-out items truly unseen: never tune repairs against them, never reuse the same set round after round, and keep them out of any cache or pool the generator can consult.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/memory/project_den_routing_98pct_unit1_2026_05_24.md",
     "lines": "51",
     "quote": "- Per-cell heuristics tuned via iterative repair against hidden hold-out",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/den_solver_acceptance_20260523T082319Z_summary.json",
     "lines": "13",
     "quote": "\"input_jsonl\": \"/tmp/holdout_for_den_v2.jsonl\",",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/validated/2026-05-22T2116Z_den_solver_v8_FIRST_VALIDATED/den_solver_acceptance_20260522T210237Z_summary.json",
     "lines": "13",
     "quote": "\"input_jsonl\": \"/tmp/holdout_for_den_v2.jsonl\",",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/INCLUSION_CRITERIA.md",
     "lines": "62",
     "quote": "5. **Reproducible**: re-running the validation on a different n=50 sample must clear the threshold ±2pp (no luck-of-the-draw cherry-picks)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1830Z_den_solver_v2_online_K_N_with_cache/SECOND_TIER_REASON.md",
     "lines": "50",
     "quote": "37 passes = substandards in cache from prior runs (e7e1d980 pipeline outputs).",
     "verbatim": true
    }
   ],
   "against": "Fresh sets differ in difficulty, so a fresh set must match the target mix: \"Holdout prompts are systematically harder.\" (crystal full-copy/aptraining-root/achieved.md line 69).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The summary shows n=90, agreement 0.9778, kappa 0.0, tn=0, fp=0 and an IB pass rate of 1.0, so the 0.95 bar was met on an all-pass sample. Added the docstring where that number was reused as '~97.8% IB correlation' for the cheaper judge (eval_v90c_gemini_raw.py line 4), and paired agreement with kappa in one quote. The labeller line (99.6% at the top score) is a related ceiling case. Adds to truths 37 and 38; not a duplicate.",
   "statement": "Calibrate a judge on a sample with known failures as well as passes, and report chance-corrected agreement; 97.8% agreement on an all-pass sample had a kappa of 0 and showed nothing.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/serve/runs_calibrate_gemini_vs_ib_after_swap/calibration_summary.json",
     "lines": "6-7",
     "quote": "\"agreement\": 0.9777777777777777, \"kappa\": 0.0,",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/serve/calibrate_gemini_vs_ib.py",
     "lines": "4-5",
     "quote": "Uses the 90 Cheater Layer 1 cached items as the calibration sample (each has authoritative IB v2.5.11 score from build-time).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/serve/eval_v90c_gemini_raw.py",
     "lines": "4",
     "quote": "Uses Gemini-3.1-flash-lite judge via layer3_gemini_judge.py (~97.8% IB correlation).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/analytics.md",
     "lines": "140",
     "quote": "| IsUse 5/4 | 962/4 ⚠ 99.6% degenerate-at-5 (gpt-4o-mini ceiling) |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Added RUBRIC_BLINDSPOTS lines 32-35: the zero-knowledge probe, the rubric's costliest check, runs only when a stimulus is present. Replaced the '68% to 100%' line, because its 68% is the model's all-type aggregate set against an MCQ-only batch; the deliberately mid-quality hand-made batch at 30/30 shows the effect without that mismatch. On 50 fresh items the source-free MCQs passed 45/50, against 86% for the raw model's MCQs, so the lift shrank to on-par. The statement (checks gated on presence let items pass by omission) still holds.",
   "statement": "Make the judge fail an item that leaves out a part its type requires; checks that run only when the part is present let items pass by leaving it out.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/RUBRIC_BLINDSPOTS.md",
     "lines": "16-18",
     "quote": "For APUSH MCQs, the curriculum data does **not** carry that flag, so Mode C applies and \"no stimulus = PASS\" — even though every real AP US History MCQ includes a primary-source stimulus.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/RUBRIC_BLINDSPOTS.md",
     "lines": "32-35",
     "quote": "The probe is the single most expensive check in the MCQ rubric — it catches almost all of the v50 failures. But it is *only* run when a stimulus is present. Strip the stimulus and the probe never fires.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/EXPLOIT-002-stimulus-strip.md",
     "lines": "7",
     "quote": "- Hand-crafted control batch: **30/30 = 100%** (avg 0.9987; 28 SUPERIOR, 2 ACCEPTABLE)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/pending_review/2026-05-23T000424Z_exploits_EXPLOIT-004-saq-no-stimulus/source_report.md",
     "lines": "5",
     "quote": "**Pass rate**: **34/34 = 100%** on n=34 items (17 distinct APUSH SAQ KCs × 2 variants) via v80bchain (avg overall score **0.994**)",
     "verbatim": true
    }
   ],
   "against": "On fresh items the source-free version passed 90%, not 100% (\"- **n_pass / total**: 45 / 50 = **90.00%**\", artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/cheater_validation_verdict.md line 3), only on par with the raw model's MCQs (\"| v80b standalone MCQ | 86% | 90% | **+4pp lift over raw model** |\", SECOND_TIER_REASON.md line 10). Source-free items are legitimate for drills: \"- **Stem-only review-drill products**: explicit non-exam-format MCQs (no stimulus) for AP-prep practice apps, where the IB grader rubric matches the product shape.\" (SECOND_TIER_REASON.md line 19); and the project's own generator checklist said \"- [ ] If unsure of a source — drop the stimulus, write a non-stimulus item\" (common_pre_checklist.md line 24).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (RUBRIC_BLINDSPOTS 51-55; EXPLOIT-005 95-97). Replaced the failure-mode-index line, a generator tip against self-advocacy that bears only loosely on the claim, with EXPLOIT-005 lines 102-103, where the judge passed items because sophistication moves were merely listed in the notes. Overlaps truths 12 and 30 in spirit, but the self-heal rule that flips a failed check to match the judge's own narrative is a distinct judge-design fault.",
   "statement": "Judge what the task itself demands, not what the item's notes or explanation claim about it, and never let a judge's written reasoning flip a failed check to a pass; templated rationales and listed 'features' bought passes.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/RUBRIC_BLINDSPOTS.md",
     "lines": "51-55",
     "quote": "But because the judge writes reasoning BEFORE the score is applied, a template-driven explanation that prefills the judge's reasoning toward \"content is correct\" will force the score to 1.0 even when the judge's gut would have failed it.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/pending_review/2026-05-23T082229Z_exploits_EXPLOIT-005-leq-no-stimulus/source_report.md",
     "lines": "95-97",
     "quote": "\"Multiple defensible positions\" currently passes if rubric_notes literally lists two opposing thesis sentences.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/pending_review/2026-05-23T082229Z_exploits_EXPLOIT-005-leq-no-stimulus/source_report.md",
     "lines": "102-103",
     "quote": "Current rubric passes if sophistication moves are LISTED in rubric_notes.",
     "verbatim": true
    }
   ],
   "against": "Explanations themselves are allowed: \"Genuine educational explanations in answer/rationale fields are NOT violations.\" (helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt line 29); the project itself wrote the judge's criteria into training items' notes: \"- DBQ: rubric_notes = IB DBQ criteria text; additional_details = top-3 misconceptions; image_url = \"[]\"\" (helpers/data/build_u1_maximal_corpus_v6_curriculum_enriched.py line 15).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep",
   "reason": "All three quotes verbatim at the cited lines (EXPLOIT-004 27-29; base rubric 88; distilled report 159). The rubric itself says analytical verbs do not rescue an item, yet the judge rewarded 'Explain ONE way' with no added demand; another project saw 'Describe'/'Identify' treated as recall whatever the context. The fault runs both ways. General; distinct from truth 10 (marking answers by meaning).",
   "statement": "Judge how much thinking a task demands from what it actually requires, not from its command verb; swapping in an analytical verb passed with no added demand.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/pending_review/2026-05-23T000424Z_exploits_EXPLOIT-004-saq-no-stimulus/source_report.md",
     "lines": "27-29",
     "quote": "Using \"Explain ONE way\" hits the analytical sweet spot on the rubric's wording without any actual increase in cognitive demand.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt",
     "lines": "88",
     "quote": "Verbs like *evaluate / claim / analyze / explain / justify* in the question stem do **not** rescue the item — they describe the cover, not the actual cognitive demand.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md",
     "lines": "159",
     "quote": "- “Describe” and “Identify” verbs were treated as recall even when surrounded by analytical language.",
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
   "reason": "Quotes verbatim; EXPLOIT-001 shows the probe failing educational_accuracy on 5 of 10 items through paraphrase leaks. Added the rubric's 'mechanism-naming leak' line, the source of the second route ('naming what the source describes'). Scoped the statement to items meant to test subject knowledge, since the rubric skips the probe for reading items (against). Distinct from truth 5, which says a question must need the text; this one says the text's wording alone must not be enough.",
   "statement": "On items meant to test subject knowledge, check that a student without that knowledge cannot reach the answer from wording alone — by matching the source to an option, naming what the source describes, or ruling out implausible options.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt",
     "lines": "76",
     "quote": "Working only from the stimulus (including any image-analysis content) and the question stem, attempt to pick the correct answer step by step.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt",
     "lines": "86",
     "quote": "1. **Mechanism-naming leak.** The stimulus describes a process / mechanism / scenario in lay vocabulary; the question asks the student to supply the conventional label or technical term *for that exact described thing*.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/_logs/watcher_replay_dupes_20260522T2018Z/2026-05-22T201819Z_exploits_EXPLOIT-001-historian-frame-self-leak/source_report.md",
     "lines": "32-34",
     "quote": "1. **Vocabulary / paraphrase leak.** The judge's zero-knowledge counterfactual probe (per `_base_evaluation.txt` Checklist B1) found that the abstract historian claim word-matched one option:",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/RUBRIC_BLINDSPOTS.md",
     "lines": "37-40",
     "quote": "**Patch:** for closed-form history MCQs without a stimulus, add a stem-only variant of the probe that asks \"could a student with no APUSH knowledge eliminate three of these four options purely from common-knowledge / lay-vocabulary reasoning?\".",
     "verbatim": true
    }
   ],
   "against": "The probe does not apply to reading items, where the text is the point: \"- **Skip the probe entirely** when: `request.subject` is ELA / reading / language-arts; the content type is `nonfiction_reading` / `fiction_reading` / `article` (those *are* reading-comprehension by design); or no stimulus is present.\" (_base_evaluation.txt line 80).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Added the autopsy verdict: generated 'documents' were visual-artifact or fabricated-source descriptions, so document-based items scored zero. Also added the generator rule to copy retrieved documents and attributions verbatim, and the standing rule that every text field traces to a primary source. Numbers check: 0% without real sources, 87.9% vs 67% with the source corpus, 33.3% for a naive retrieval patch (against). Overlaps truths 57, 17 and 64, but stimulus authenticity is its own claim, backed by measured evidence; not a duplicate.",
   "statement": "Build source-based items from real documents copied verbatim with true attribution and supplied at generation time; never let the writer invent, paraphrase or describe a source.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md",
     "lines": "9",
     "quote": "DBQ is structurally zero on the current InceptBench path because the generator emits DBQ \"documents\" that are visual artifact descriptions or fabricated source descriptions, not usable source text.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md",
     "lines": "111",
     "quote": "The contrast is the whole story: normal generation without real source injection sits at DBQ 0%; D13 source injection immediately produces non-zero DBQ, but the current naive retrieval/prompting still fails often.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/d13_corpus_v5_inventory.md",
     "lines": "68",
     "quote": "Pipeline-on-v80b uses this and scores **87.9% DBQ** (vs 67% v80b standalone).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/system_prompt_dbq.md",
     "lines": "129-130",
     "quote": "1. Copy each document's source/content/metadata verbatim from the retrieval. 2. Do NOT rewrite or summarize the source attribution — keep it exactly as retrieved.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_main_session_close/01_HANDOVER.md",
     "lines": "89",
     "quote": "**No mock data.** Every text field traces to a primary source. LLMs are tools (search/OCR/reformat), not content authors. Drop-don't-patch when sources fail.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/v18_rebuild_scope.md",
     "lines": "15-17",
     "quote": "D8b confirmed plausible-but-fictional content (real attributions, unverified text) — fine for ≤95% but the floor at 99%.",
     "verbatim": true
    }
   ],
   "against": "Real sources were necessary but not sufficient: \"The full D13 hot-patch reached only 33.3% and still had 64% `stimulus_quality` zero-rate, so token-overlap + unit bonus is not enough for 97%.\" (dbq_structural_zero.md line 137); the live service generated images from described documents: \"This turns the model's prose description into an actual visual artifact the IB grader can score.\" (apllm-history/main.py lines 532-533); a criteria pack advised \"Use authentic primary-source language patterns, period-correct vocabulary, plausible attribution lines (author/date/source citation).\" (helpers/data/output/ib_pass_criteria_pack/README.md line 23).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 17,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Extended the first quote to the rest of line 43 (5 of 6 rows rejected for library preambles, bookplates, OCR garbage and header pollution), which is the evidence for the 'library boilerplate' part. Numbers match (exactly 50,000 chars; 85-96%; 322/761; 109/109; 92 + 556 of 648). General.",
   "statement": "Before using a fetched source text, check it is the complete text — not a landing page, a metadata stub, a length-capped excerpt or a page wrapped in library boilerplate.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md",
     "lines": "43",
     "quote": "**F-D13-13**: all 6 rows truncated at exactly 50,000 chars, losing 85-96% of fulltext. 5 of 6 rows reject (Spanish library preamble, BYU bookplate, Newberry Library + Latin OCR garbage, PG header pollution).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/SHADOW_HANDOFF.md",
     "lines": "36",
     "quote": "D13 pipeline broken (322/761 LoC URLs Cloudflare-blocked, 109/109 Gutenberg URLs are landing pages).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/d13_corpus_v5_inventory.md",
     "lines": "28",
     "quote": "- v3 has 648 docs: **92 fulltext + 556 metadata_only** (LoC frequently has metadata but not transcribed fulltext for newer/obscure items)",
     "verbatim": true
    }
   ],
   "against": "Hashing proved the files unchanged but not complete: \"- **D13 U1 SHA256 staging held up.** 8 docs, content-hashed, no re-fetch needed.\" (handover/2026-05-01T1039Z_data_session/HANDOVER.md line 275).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; numbers match (76/96 = 79% mistagged; 211 gross violations quarantined; 23 left). Scoped to primary sources: the re-audit kept later commemorative documents filed by subject, which suits secondary material but not a source standing in for its period. Holds for any course built on dated primary sources.",
   "statement": "File each primary source under the period it was created in, not the period it mentions, and check every period label against the source's date in code.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md",
     "lines": "39",
     "quote": "U4 LoC 96-row topic cluster. **79% era-mistag** (76/96 dates outside 1800-1860, mostly 1904 Louisiana Purchase Expo commemoratives). **F-D13-12** = era-tagger doing semantic-association not date-of-creation.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/2026-05-22T2308Z_v93_phase3_reaudit_VERDICT_ADJUST.md",
     "lines": "28",
     "quote": "- **0 gross anachronisms** (>50-year mismatch) — the 211 gross violations were successfully quarantined.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/2026-05-22T2308Z_v93_phase3_reaudit_VERDICT_ADJUST.md",
     "lines": "29",
     "quote": "- **23 subject-level anachronisms** remain (±20-year or subject-obvious mismatches).",
     "verbatim": true
    }
   ],
   "against": "Later documents about an earlier period were kept by subject: \"- **Commemorative/meta docs** (Brown v. Board 2015–2024, Pearl Harbor 1973–1995 in Unit 7/8) are date-mismatched but **subject-correct**; excluded from the 23 count because the content is about the tagged unit's era.\" (same file, line 42).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; numbers match (76 KCs = 1.61%; 803/1036 = 77.5%). 'Invalid' overstated the IDs: the source calls them non-canonical opaque hashes, with only 14% matching the official pattern, so reworded. The 76 are flags from a ±25-year audit that the file says still need manual review. The period table belongs to the prompt builder, a reference table the generator consults.",
   "statement": "Audit the knowledge base's own labels in code before generating from it; an audit flagged 76 facts dated outside their unit's period, a period table off by one unit made requests contradict themselves, and 77.5% of one build's standard IDs were non-canonical.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/curriculum_kc_period_audit.md",
     "lines": "8",
     "quote": "- **76 KCs** flagged as period-mismatched.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/.agent/memory/data_quirk_apwh_period_table.md",
     "lines": "28",
     "quote": "Concrete observed failure: an apwh/leq Unit 6 prompt had `LEARNING OBJECTIVE: Explain how the development of new technologies changed the world from 1900 to present` paired with `TIME PERIOD: c. 1750 to c. 1900 (STRICT -- nothing outside this range)`.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01_session_end/SHADOW_HANDOVER.md",
     "lines": "59",
     "quote": "| Non-canonical KC IDs | 77.5% (803/1036) use opaque hashes (`c_4EvW`, `s_saxW`); only 14% match `KC-X.Y.Z+N` |",
     "verbatim": true
    }
   ],
   "against": "Automated flags still need human review: \"- `suggested_unit` is best-effort: the unit whose window contains the parsed date range. Manual review still required before any data-side fix.\" (curriculum_kc_period_audit.md line 69).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (oracle handover 343 and 345; bundle README 51). The statement merged two courses: the period-shifted IDs were in one course (APEURO), the near-zero overlap in another (APUSH, where 39% of one source and 99.8% of the other had no match). Rewrote to keep them apart. General to any generator drawing on more than one standards source.",
   "statement": "Reconcile each knowledge source against the official framework, course by course, before choosing one, and key every standard by course plus ID; in one course a source's IDs were off by one period, in another 99.8% of one source's entries had no match in the other, and the same ID recurs across courses.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_oracle_session/HANDOVER.md",
     "lines": "343",
     "quote": "InceptBench APEURO IDs off by one period vs CB CED. Curriculum repo IDs match official CB CED.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_oracle_session/HANDOVER.md",
     "lines": "345",
     "quote": "39% of curriculum has no IB match; 99.8% of IB has no curriculum match.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/apllm-history/runtime_assets/curriculum_facts_bundle_v1/README.md",
     "lines": "51",
     "quote": "# Same node_id can exist in multiple courses (e.g. KC-1.1.I.A in APUSH + APEURO).",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Added the line-39 finding of topics with zero documents, which supports 'one or zero'. Numbers match (1 row each; 46 rows = 37% of a 126-row cluster; 648 new docs; 1,385 docs / 5.8M chars). The audits ran on topic clusters of about 100 rows drawn from a 653-row set, so 'large pool' is relative. General.",
   "statement": "Audit a source pool's coverage against the curriculum's topics before generating from it; a large pool held one or zero sources for several required topics and leaned heavily on one kind of voice.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md",
     "lines": "38",
     "quote": "Slavery/labor = 1 row, Jamestown = 1 row (critical under-rep).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md",
     "lines": "39",
     "quote": "Sectionalism/slave-revolts/2nd Awakening/transcendentalism = 0 each.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md",
     "lines": "41",
     "quote": "ADST oral histories = 46 rows / 37% (elite foreign-policy skew confirmed).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/d13_corpus_v5_inventory.md",
     "lines": "8",
     "quote": "v3 ingest added **648 new docs** across Units 1/2/4/6/9 (the units missing or sparse in v2), bringing the combined v2+v3 corpus to **1,385 docs / 5.8M chars**.",
     "verbatim": true
    }
   ],
   "against": "Coverage counts themselves can mislead: \"False-positive rate documented per-tick (e.g., \"gilded age / labor\" cluster on U6 had 21/34 false-positives = foreign antitrust).\" (atlas HANDOVER.md line 128) and \"## Per-unit aggregate (across all sources, deduplication NOT applied — caveat)\" (helpers/data/output/v93_data_inventory.md line 24).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; numbers match (1,080-row export; 21 sample-answer errors, 41 out of period, 39 factual errors). Those family counts come from pattern tags on the judge's text, the same tagger that put a false-positive 'grade echo' tag on all 154 failures, so treat them as indicative. The calibration rows give row-level confirmation. Split 'inside the parts the request names' into its own clause about covering every requested part, and added the prep note that marking notes and sample answers cite out-of-period years, plus the short-answer item whose sample responses skipped required parts.",
   "statement": "Keep every fact in an item — stem, options, sample answers and marking notes — inside the period and region the request names, make sample answers cover every part the request asks for, and check dates in code.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/next_live_run_prep.md",
     "lines": "25",
     "quote": "**Symptom**: 21 sample_response_error + 41 out_of_period + 39 factual_error + named-content-trap families (`content_lakota_pre1607` 14, `content_muscovy_east_india` 7, `content_navigation_acts` 3, `content_requerimiento_overclaim` 2) = chain hallucinating concrete, name-able anachronisms in Unit 1 content.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/next_live_run_prep.md",
     "lines": "46",
     "quote": "**Symptom**: LEQ rubric_notes routinely cite years outside Unit 1 (1491-1607); SAQ sample_responses do the same.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md",
     "lines": "45",
     "quote": "- `apush-u1-1505-leq-medium`: LEQ rubric included Northeastern evidence outside a Southwest / Great Basin prompt.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md",
     "lines": "46",
     "quote": "- `apush-u1-0760-saq-hard`: SAQ sample responses failed to answer religious justifications and gender roles required by the prompt.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md",
     "lines": "51",
     "quote": "- SAQ answer-key verifier must ensure every requested component appears in the sample responses, not just in the student-facing parts.",
     "verbatim": true
    }
   ],
   "against": "A simple year check caught only a fraction: \"- `year_bound.check_leq` catches 1 of 7 LEQ chronology failures (true positive ~14%) and 0 valid candidates (0% FP) — this one is net-positive alone.\" (crystal variant-calibration-lab-snapshot/KNOWN_ISSUES.md lines 135-137).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Added the generator checklist lines behind the 'same grain and category' and 'seeded from misconceptions' rules, and the rubric's pass lines for distractors. The red-team quote shows same-category options that were plainly wrong on the merits still passing every option check, so 'easy to rule out' became what the source shows. No measured test of misconception-seeded options was found (against). An adopted item-writing rule; no existing truth covers distractor design.",
   "statement": "Write each wrong option from a misconception students actually hold, in the same category and grain as the key; options a knowledgeable reader sees as plainly wrong can still pass a judge's option checks.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_evaluation.txt",
     "lines": "287-288",
     "quote": "- Distractors are plausible and likely chosen by students with partial mastery - Distractors align with known common misconceptions (especially those from Curriculum API)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/common_pre_checklist.md",
     "lines": "36",
     "quote": "- [ ] All options same grain size and same category",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/common_pre_checklist.md",
     "lines": "38",
     "quote": "- [ ] Distractors seeded from `common_misconceptions` where possible",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/EXPLOIT-002-stimulus-strip.md",
     "lines": "68-72",
     "quote": "obviously-wrong-on-the-merits to a knowledgeable reader (each distractor names a real historical claim that is anachronistic or factually inverted, not nonsense). This pattern automatically satisfies `distractor_quality` and `reveals_misconceptions` default-pass conditions",
     "verbatim": true
    }
   ],
   "against": "The planned test of misconception-seeded options has no recorded result in the files read: \"4. If +3pp on distractor_quality → fire full 150-mcq replication; recommend production injection\" (helpers/data/output/path_e/path_e_build_notes.md line 42).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep",
   "reason": "Both quotes verbatim (docstring lines 5-7 and 7-8). The A/B appears to be about 30 items (answer balance 0 to 30/30), so 3.3% to 26.7% is about 1 to 8 passes: a small sample, though the answer-balance fix is clear-cut. Against quotes verified. General.",
   "statement": "Show the writer three to five verified examples of the item type taken from other topics, so it copies the form but not the content; this lifted a 3.3% pass rate to 26.7%.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/serve/fewshot_mcqset.py",
     "lines": "5-7",
     "quote": "for MCQ_SET, sample 3-5 verified exemplars (IB-graded 1.0) from the 669-pool, picking exemplars whose KC DIFFERS from the target KC so the output stays fresh, and prepend them as a TEMPLATE SEED.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/serve/fewshot_mcqset.py",
     "lines": "7-8",
     "quote": "This lifted IB MCQ_SET 3.3% -> 26.7% and fixed answer_balance 0 -> 30/30.",
     "verbatim": true
    }
   ],
   "against": "Example banks can make output static: \"DBQ and MCQ_SET had extreme duplicate groups in A0F. Static output can inflate short-slice scores and then collapse on variety/focus.\" (crystal parallel-ideas-lab/reports/WEEKLY_APUSH_PIL_REPORT_20260520.md line 492); and \"- For dense courses like APUSH, too many prompt examples can hurt; prefer exact facts/source packs over long example lists.\" (den-of-ideation/reports/ap_social_studies_generator_distilled.md line 186).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 25,
   "verdict": "keep",
   "reason": "Quotes verbatim; numbers match (216 document-based items, 88.4% pass, 6 unique = 2.8%; question sets 11 unique = 5.1%). The same file says the repair/fallback behaviour 'preserves passable shapes but collapses variety', and the official run reported a 9.32% variety score. General.",
   "statement": "Measure how many distinct items a generator delivers for each item type; one run passed 88% of its document-based items, but only 6 of 216 were distinct.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/run_0506c1fd_v2_final_variety_static.md",
     "lines": "15",
     "quote": "| DBQ | 216 | 88.4% | 6 | 2.8% |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/run_0506c1fd_v2_final_variety_static.md",
     "lines": "27",
     "quote": "- The showcase architecture generated multiple candidates, but the underlying all-units generator was still effectively deterministic because `apush_all_units_generator.call_fireworks()` hard-coded `temperature=0.0` and ignored the showcase profile temperature hints.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md",
     "lines": "62",
     "quote": "Takeaway: K was not producing useful diversity for MCQ_SET in this archive. It produced duplicate payloads. Anti-static guard must treat identical candidates as one candidate, not six chances.",
     "verbatim": true
    }
   ],
   "against": "Variety and pass rate trade off: \"- Pass rate may move either direction; this is a quality/variety repair, not a guaranteed score-only patch.\" (run_0506c1fd_v2_final_variety_static.md line 41).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; numbers match (91.3% to 87.3%; mcq_set/hard 10/10 to 3/10). The source's adoption rule is per-filter replay with a net gain of at least 3 rows (KNOWN_ISSUES 147-149). 'Costs no passes for any item type' was the reader's inference, so rewrote to the source's rule and cited it.",
   "statement": "Replay each new automatic filter on its own over saved, already-judged items and adopt it only if the replay shows a net gain; a bundle of individually plausible filters cut one item type from 10/10 to 3/10 and the overall pass rate from 91.3% to 87.3%.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/KNOWN_ISSUES.md",
     "lines": "147-149",
     "quote": "**Fix**: never ship the filter bundle. Recommend filters individually with per-filter replay numbers. Add a filter only if its replay shows net gain ≥ 3 rows.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/gemini_selector_calibration_final.md",
     "lines": "96",
     "quote": "| mcq_set/hard | 10 | 10/10 | 3/10 | 10/10 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/gemini_selector_calibration_final.md",
     "lines": "103-104",
     "quote": "- baseline pass rate (current Gemini selector): **91.3%** - filter→gemini pass rate (proposed v2 selector): **87.3%**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/KNOWN_ISSUES.md",
     "lines": "129-130",
     "quote": "**Root cause**: the filters in `scripts/filters/*.py` are individually plausible but their bundle over-rejects valid candidates.",
     "verbatim": true
    }
   ],
   "against": "Single filters can still help: \"These were measured net-negative when bundled with other filters in my prior replay, but applied alone they recover ~6/40 MCQ_SET candidates that Gemini otherwise picks.\" (variant-calibration-lab-snapshot/next_live_run_prep.md line 65).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep",
   "reason": "Quotes verbatim (KNOWN_ISSUES 107-108 and 110-111; prep note 87); numbers match (71 of 72; 0 of 5 spot-checked rows). The source's fix replaced the regex tag with the judge's sub-score. General; complements truth 60.",
   "statement": "Read failure reasons from the judge's structured scores, not by keyword-matching its prose; a pattern match tagged 71 of 72 failures with a fault that wasn't there.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/KNOWN_ISSUES.md",
     "lines": "107-108",
     "quote": "**Symptom**: 71 of 72 failed rows tagged `integrity_violation`; reading the underlying narrative shows almost none are actual violations.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/KNOWN_ISSUES.md",
     "lines": "110-111",
     "quote": "**Root cause**: my regex matched the *metric name* (e.g. \"Integrity check passed\") in evaluator reasoning text, not actual violations.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/next_live_run_prep.md",
     "lines": "87",
     "quote": "Spot-check of 5 randomly-sampled failed rows showed 0 actually mention \"grade 1\" as a failure cause.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 'Proved nothing' overstated the source, which calls the stitched 149/150 'valid' evidence that is not proof of the live system; reworded. Added the synthesis's list of what every result must state (evaluator/version, sample size, endpoint/mode, model route vs fallback, K, proof class). Overlaps candidate 0 on version and truth 46 on delivery mode; kept as the broader rule.",
   "statement": "State with every score which judge and version, how many items, which build and route, and whether it came from a full delivery-mode run; a 149/150 stitched from the best slices of two builds was not proof that the live system worked.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md",
     "lines": "104",
     "quote": "This is a valid 149/150-style stitched evidence result. It is not proof that current live production is solved because the selected window combines builds `6f0ffdf` and `e429b16`.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/MASTER_SYNTHESIS.md",
     "lines": "128",
     "quote": "Every result must state:",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/MASTER_SYNTHESIS.md",
     "lines": "130-135",
     "quote": "- evaluator/version; - sample size; - endpoint/mode; - model route versus fallback route; - K value; - whether the score is official IB, local IB, diagnostic eval, older IB, self-eval, targeted repair, spread sample, or schema-only.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/SELECTOR_CALIBRATION_TAKEAWAYS_20260520.md",
     "lines": "33",
     "quote": "- Evidence: small calibration sets can validate machinery but cannot prove 99%.",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The design doc's '0.32⁵ = 0.34% → 99.66%' assumes independent attempts, yet one topic failed all 10 attempts and whole substandards fail systematically (added the brainstorm line). The repeated-attempts half restates truth 65 (best of several fixes random slips, not systematic failures). Kept as a duplicate because it adds the stacked-methods result and the independence-math error as new evidence.",
   "statement": "Don't predict the gain of stacked methods or repeated attempts by multiplying their odds as if independent; failures cluster by topic, so measure the combination.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_main_session_close/02_CONSOLIDATED_STATE.md",
     "lines": "96",
     "quote": "| **Combo routing + RAG** | Failed to compose lifts | `project_combo_routing_plus_rag_failed.md` | Methods correlate; multiplicative stacking is wishful |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/serve/serve99stack.py",
     "lines": "8",
     "quote": "- At K=5 with 68% raw base: P(all 5 fail) = 0.32⁵ = 0.34% → 99.66% per cell from Layer 3 alone",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/pending_review/2026-05-23T082229Z_exploits_EXPLOIT-005-leq-no-stimulus/source_report.md",
     "lines": "54-55",
     "quote": "Tried 2 rounds of K=5 (10 attempts) and never crossed 0.80.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/system_improvement_brainstorm.md",
     "lines": "39",
     "quote": "Some substandards (KC-1.1.I.* on MCQ_SET) systematically fail; others systematically pass.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "65",
   "name_bearing_source": false
  },
  {
   "index": 30,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Added the smoke composition (five fixed items, one per type, drawn from the held-out pool), the reason it was adopted (two builds burned full 150-row runs before their collapse showed), and the backlog's 'run them locally and live after every deploy'. Numbers match (~3% of the cost; 5 deploys with no measured impact). Related to truth 47 but about generator smoke sets, not lesson play-throughs.",
   "statement": "Run a small fixed smoke set — one item per type plus items from each known failure family — end to end before any full measurement and after every change.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/coordination/scripts/SHIP_PRECONDITIONS.md",
     "lines": "76-78",
     "quote": "v38 (262 rows, eval=0/150 parse_ok) and v39 (1036 rows, −16.2pp binary) both burned the full 150-row IB-grader run before their collapse was visible.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/coordination/scripts/SHIP_PRECONDITIONS.md",
     "lines": "79-80",
     "quote": "A 5-item probe surfaces format collapse, deployment-side breakage, and obvious regressions for ~3% of the cost.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/coordination/scripts/SHIP_PRECONDITIONS.md",
     "lines": "82-85",
     "quote": "**Smoke composition.** 5 APUSH items, one per cell type (`MCQ`, `MCQ_SET`, `SAQ`, `DBQ`, `LEQ`), drawn from the held-out eval pool (NOT the training set). Items are fixed across runs so smoke results are comparable;",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/evidence/FUTURE_RUN_IMPROVEMENT_BACKLOG_20260521.md",
     "lines": "209",
     "quote": "- Convert each family into 3-5 fixed regression prompts.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/evidence/FUTURE_RUN_IMPROVEMENT_BACKLOG_20260521.md",
     "lines": "210",
     "quote": "- Run them locally and live after every deploy.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/system_improvement_brainstorm.md",
     "lines": "25",
     "quote": "**Value**: HIGH. Right now we have 5 deploys with no measured impact. Each deploy carries an unverified +N pp claim.",
     "verbatim": true
    }
   ],
   "against": "A tiny smoke set cannot judge everything: \"- The 7-response smoke had DBQ uniqueness `2/2`, but MCQ_SET uniqueness `1/2`; this is only a warning at that sample size, but it confirms the next pre-live gate should use at least `--diversity-per-qtype 5`.\" (crystal evidence/RUN_MODE_TAXONOMY_AND_GATES_20260521.md line 95).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep",
   "reason": "Quotes verbatim (stem template 4-5; inclusion criteria 64; re-audit 54). Adopted rules, applied in a licence audit of the source corpus. General.",
   "statement": "Write new questions instead of copying or paraphrasing released exam items, and use only sources whose licence has been checked.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/t5_dbq_stem_template.md",
     "lines": "4-5",
     "quote": "NO verbatim College Board prompts; NO paraphrase of released exams; net-new stems anchored to verified primary documents.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/INCLUSION_CRITERIA.md",
     "lines": "64",
     "quote": "7. **License / source-clean**: no scraped copyrighted material, no Anthropic / OpenAI-output-as-training, no PII",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/2026-05-22T2308Z_v93_phase3_reaudit_VERDICT_ADJUST.md",
     "lines": "54",
     "quote": "- Wikipedia: every row has `\"license\":\"CC BY-SA 4.0\"`.",
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
   "reason": "Quotes verbatim. The backlog quote sits on line 233, not 233-234, and line 234 holds the 'easy questions should still avoid giveaway wording' half, now quoted. The reader's claim that this came after hard items failed on obscure or out-of-period content is only partly shown in the files read; the rule itself is well sourced.",
   "statement": "Make hard items hard through reasoning — a subtle distinction, synthesis or weighing a counter-argument — not through obscure names or facts outside the scope, and keep easy items free of giveaway wording.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/evidence/FUTURE_RUN_IMPROVEMENT_BACKLOG_20260521.md",
     "lines": "233",
     "quote": "- hard questions should require reasoning, not obscure names or out-of-period facts.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/evidence/FUTURE_RUN_IMPROVEMENT_BACKLOG_20260521.md",
     "lines": "234",
     "quote": "- easy questions should still avoid giveaway wording.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/common_pre_checklist.md",
     "lines": "71",
     "quote": "- [ ] Hard: subtle distinction, synthesis, or counterargument evaluation",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/apllm-history/runtime_assets/ib_satisfaction_kit_v1/failure_mode_index.json",
     "lines": "41",
     "quote": "\"fix\": \"All required facts must be curriculum-standard\"",
     "verbatim": true
    }
   ],
   "against": "The judge cannot check difficulty without written definitions: \"**If no definitions provided**: `difficulty_alignment = 1.0`. Do NOT invent criteria.\" (raw_rubrics/_base_evaluation.txt line 137).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 33,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Added the takeaways rule (deterministic filters before Gemini; 'a selector, not a rescue path') and the policy line requiring the selector to beat first-valid in calibration, and extended the calibration takeaway to its 'audit-only until ... proves a lift' sentence. Replaced the K-of-N line (line 9), which is about extra candidates rather than the selector. Caveat: the 15-row archive tied every mode, the oracle included, so it could not show a lift either way.",
   "statement": "Let a model judge choose only among items that already pass the code checks, and keep it as a selector only if, on saved candidates, it beats simply taking the first valid item.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/SELECTOR_CALIBRATION_TAKEAWAYS_20260520.md",
     "lines": "17",
     "quote": "- Evidence: if bad candidates reach the selector, a fluent but invalid MCQ_SET can beat the actually passing raw candidate.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/SELECTOR_CALIBRATION_TAKEAWAYS_20260520.md",
     "lines": "18",
     "quote": "- Rule: deterministic filters come before Gemini. Gemini is a selector, not a rescue path.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md",
     "lines": "39",
     "quote": "Takeaway: Gemini did not beat first-valid on this archive. Do not enable Gemini as a selector for this policy from this evidence. It is audit-only until a larger saved-candidate calibration proves a lift.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/SELECTOR_CALIBRATION_TAKEAWAYS_20260520.md",
     "lines": "44",
     "quote": "- MCQ_SET: staged route; extra K only after filters, and selector must beat first-valid in calibration.",
     "verbatim": true
    }
   ],
   "against": "On another archive the selector did well: \"**Selector recall** (on rows where at least one candidate passed): 137/145 = 0.945\" (variant-calibration-lab-snapshot/gemini_selector_calibration_final.md line 15).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 34,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (R42 150; checklist 51; weekly report 500). Added line 287: a saved winner failed schema validation on a leaked prompt_pipeline_meta field. The penalty claim in R42 is a prediction resting on an earlier observation (R10). General.",
   "statement": "Strip drafting, self-checking and debug text from an item before a student or judge sees it; leftover working notes are penalised and leaked metadata broke the delivery contract.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/02_R42_CoVe_DBQ_spec.md",
     "lines": "150",
     "quote": "The verification meta-text WILL be penalized — IB rubric scores presence of meta-pedagogical voice negatively (we saw this in R10 paraphrase-composition).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/common_pre_checklist.md",
     "lines": "51",
     "quote": "- [ ] No \"this question tests…\" preamble visible to students",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/WEEKLY_APUSH_PIL_REPORT_20260520.md",
     "lines": "287",
     "quote": "- old saved winner failed on `prompt_pipeline_meta`",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/WEEKLY_APUSH_PIL_REPORT_20260520.md",
     "lines": "500",
     "quote": "Debug metadata belongs in archives/logs, not official payloads.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 35,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Added the distilled report's transferable rule (lock structure and key first, explanations second) and its finding that single-stage generation gave bad answer counts until two-stage generation plus validation fixed it. That project's numbers were self-evaluated (candidate 41), so this is design evidence. General.",
   "statement": "Fix an item's structure and answer key first, then write explanations against that fixed key, and check that every explanation, hint and feedback line refers to the item's actual options and key.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/k_12_social_studies_distilled.md",
     "lines": "44",
     "quote": "- This prevents the model from generating an explanation that contradicts the answer key.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/k_12_social_studies_distilled.md",
     "lines": "73",
     "quote": "- Use two-stage generation for answer-bearing item types: lock structure/key first, generate explanations second.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/k_12_social_studies_distilled.md",
     "lines": "64",
     "quote": "- Single-stage MSQ produced bad answer-count behavior; the fix was two-stage MSQ plus validation.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_evaluation.txt",
     "lines": "85",
     "quote": "- **FIELD MISMATCH**: Explanations, hints, feedback templates, or `additional_details` describe distractors, answers, or values that do NOT match the actual options or correct answer",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt",
     "lines": "66",
     "quote": "- Do explanations/rationales match the correct answer and options?",
     "verbatim": true
    }
   ],
   "against": "The two-stage pattern was proven only for some item types: \"- Match/fill-in/article were less proven and flagged for more validation.\" (k_12_social_studies_distilled.md line 49).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 36,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (document-question rubric lines 54, 60 and 44). The rubric asks that multiple documents carry a clear perspective, not each one, so softened 'each'. This is the judge's rubric rather than a measured finding: an adopted rule for document-based tasks in any subject.",
   "statement": "Build a source set so every document bears on the question, several carry a clear point of view or purpose to analyse, and together they support more than one defensible argument.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/dbq_evaluation.txt",
     "lines": "54",
     "quote": "- Score 1.0: Every document can be used to support, complicate, or inform an analysis related to the prompt",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/dbq_evaluation.txt",
     "lines": "60",
     "quote": "- Score 0.0: All documents point to one obvious conclusion; no real analysis or argumentation is possible",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/dbq_evaluation.txt",
     "lines": "44",
     "quote": "- Score 1.0: Multiple documents have clear perspective, purpose, or context that students can analyze; sourcing/analysis opportunities exist",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 37,
   "verdict": "keep",
   "reason": "Quotes verbatim. The 1,080-row failure map counts 156 standard-alignment failures against 24 for the next class (chronology), 86 of them in question sets. The gap analysis and recovery plan describe drift to generic or nearby topics. The generation-side counterpart to truth 58, adding evidence; not a duplicate.",
   "statement": "Choose sources and frame the task for the exact objective requested, not the broad theme of its period; drifting to a nearby topic was the single most common failure.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/DBQ_GAP_ANALYSIS.md",
     "lines": "4",
     "quote": "Failures are driven almost entirely by **topic/rubric misalignment**, not hallucination or structural errors.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/a0f_completed_failure_map_20260520.md",
     "lines": "23",
     "quote": "| quality_fail_standard_alignment | 156 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/IB_A0F_99_RECOVERY_PLAN_20260519.md",
     "lines": "214",
     "quote": "1. The item drifts from the requested substandard into a nearby Unit 1 topic.",
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
   "reason": "Quotes verbatim (synthesis 145; distilled report 68; quarantine 25). The 100% exact-ID hit rate is second-hand ('reportedly'); the format mismatch that dropped every hold-out request to the fallback path is first-hand. General.",
   "statement": "Carry the request's course, unit, period and standard ID unchanged through every step, and fetch the standard's facts by its exact ID rather than by fuzzy topic search.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/MASTER_SYNTHESIS.md",
     "lines": "145",
     "quote": "The request's course, unit, period, type, standard/substandard, and node identifiers must flow through every layer without rederivation.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md",
     "lines": "68",
     "quote": "- Exact `node_id` lookup beat fuzzy topic search. A 40-standard check reportedly found 100% hit rate.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/quarantine/2026-05-22T1731Z_den_solver_delivery/QUARANTINE_REASON.md",
     "lines": "25",
     "quote": "Different format → den's substandard_lookup falls through → deterministic template path skipped → v80bchain fallback only.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 39,
   "verdict": "keep-with-fix",
   "reason": "Both quotes verbatim (01_HANDOVER 89; atlas handover 359). In both places the rule covers sources and corpus rows (line 89 sits under 'No mock data. Every text field traces to a primary source'), so narrowed 'item or source ... into a pass' to what the rule says. The later pipeline did repair failing outputs (against): an adopted rule the project did not keep.",
   "statement": "Drop a source or row that fails an audit instead of patching it until it passes.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_main_session_close/01_HANDOVER.md",
     "lines": "89",
     "quote": "Drop-don't-patch when sources fail.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md",
     "lines": "359",
     "quote": "- **Drop-don't-patch** on any audit failure.",
     "verbatim": true
    }
   ],
   "against": "The later pipeline patched instead: \"If the model returns malformed JSON after a successful model call, the route performs deterministic schema repair from the retrieved context and marks the route internally as `model_json_repaired`; this preserves the one-attempt model contract while avoiding official schema 500s.\" (apllm-history/README.md line 30) and \"- Apply a targeted repair function that mutates the failing candidate to address the specific criterion\" (helpers/data/output/99stack_layer4_repair_spec.md line 14).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 40,
   "verdict": "keep",
   "reason": "Quotes verbatim (data session line 287, a line that also appears at 80; shadow handover 60; atlas 357). Numbers match (A 64.5%, D 0.7%; the same 1,036-row build had 77.5% non-canonical IDs). The set was a training set of generated items. Adds evidence to truth 8, but the rule here is the set-level audit.",
   "statement": "Audit a whole generated set's distributions — key positions, label validity — not just each item's format and the row count; a set that passed row-count checks had 64.5% of its keys on one letter.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_data_session/HANDOVER.md",
     "lines": "287",
     "quote": "Build ran, validated row-count, missed the structural defect.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01_session_end/SHADOW_HANDOVER.md",
     "lines": "60",
     "quote": "| MCQ answer-A bias | A=64.5%, B=27%, C=7.8%, **D=0.7%**, E=0% (vs uniform 25% expected) |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md",
     "lines": "357",
     "quote": "- **T0 D13 full-census, no sampling**.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 41,
   "verdict": "keep",
   "reason": "Quotes verbatim (k-12 distilled 10 and 60; R42 174). The 95.2% was graded by the same model family that wrote the items. The small-model claim is the spec's summary of a published self-refine study, hedged here as 'tends to'. The against (verification helped a 65B model) checks out at R42 line 22. General; no existing truth covers it.",
   "statement": "Never let the writer grade or certify its own items; a self-graded 95.2% was design evidence only, and a small writer tends to answer 'yes' to checks on its own flawed drafts.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/k_12_social_studies_distilled.md",
     "lines": "10",
     "quote": "- Critical caveat: that 95.2% benchmark used Gemini 2.0 Flash self-evaluation of Gemini-generated questions.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/k_12_social_studies_distilled.md",
     "lines": "60",
     "quote": "The repo says this directly: if Gemini gives 90% and Claude gives 60%, the 90% is meaningless.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/02_R42_CoVe_DBQ_spec.md",
     "lines": "174",
     "quote": "Madaan et al. (A5, NeurIPS 2023) report self-refine adds <1pp at <13B and can hurt below 7B; the mechanism is that small models confabulate \"yes, this is correct\" answers to verification questions about flawed drafts, then fail to identify what to revise.",
     "verbatim": true
    }
   ],
   "against": "Self-verification helped a large model in the cited study: \"CoVe joint-style +15.5 FACTSCORE pp on biographies (Llama-2-65B-chat).\" (02_R42_CoVe_DBQ_spec.md line 22).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 42,
   "verdict": "keep",
   "reason": "Quotes verbatim (service README 137; document-question prompt 135; checklist 83, which follows an instruction to return an error after 2 internal retries). The counter-practice checks out at the v8 note, line 62. General.",
   "statement": "When a valid item can't be produced, fail visibly — refuse item types that were never measured and return an error rather than a weak or fallback item.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/apllm-history/README.md",
     "lines": "137",
     "quote": "- We have no signal on `msq` / `fill-in` / `match` / `sequence` / `article` from internal eval — gated to 501 to avoid shipping unvalidated outputs.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/system_prompt_dbq.md",
     "lines": "135",
     "quote": "Without D13: do not generate this DBQ. Return an error indicating \"real-source documents required\".",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/common_pre_checklist.md",
     "lines": "83",
     "quote": "This is better than emitting a low-quality item that wastes an IB call.",
     "verbatim": true
    }
   ],
   "against": "Fallback items were later recommended for acceptance: \"main-a recommends YES — the cached archetype is itself derived from live-IB-validated v80bchain content, so it's not \"deterministic-from-bank\" in the prior sense.\" (artifacts/validated/2026-05-22T2116Z_den_solver_v8_FIRST_VALIDATED/VALIDATION_REASON.md line 62).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 43,
   "verdict": "keep",
   "reason": "Quotes verbatim (RESULTS 85; v93 memo 28; v38 rules 33, from a decision tree written before the run). The against quote sits on line 29 of the v93 memo, not 30; corrected. Related to truth 45 (fix the rubric first), but this is about decision thresholds.",
   "statement": "Set the ship, hold and abort thresholds before running the measurement, then apply them as written.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/coordination/RESULTS.md",
     "lines": "85",
     "quote": "Cont mean 0.704 is far below the 0.92 confirmation threshold; the cell main-A predicted would lift most (MCQ) actually regressed slightly under RAG.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/memory/project_v93_falsifier_kill_2026_05_23.md",
     "lines": "28",
     "quote": "Per orch decision matrix (PASS ≥+3pp overall AND ≥+10pp factual / ABORT <+5pp AND <+0pp):",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/v38_decision_rules.md",
     "lines": "33",
     "quote": "### If v38 aggregate continuous within ±0.01 (0.928–0.948) of v29",
     "verbatim": true
    }
   ],
   "against": "Overlapping bands left a result undecided: \"- v93 lands at ABORT/ADJUST boundary on overall but FAILS PASS gate clearly\" (memory/project_v93_falsifier_kill_2026_05_23.md line 29).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 44,
   "verdict": "keep",
   "reason": "Quotes verbatim (analytics 156; course check 29; brainstorm 39). Numbers match (~9pp; units 3/6/8). The coverage note sits under a training-seed table but names the eval set itself. Distinct from truth 49 (report by skill): this one is about sampling.",
   "statement": "Spread the evaluation items across every unit and standard the claim covers; results differ by unit, and a set drawn from three of nine units can't speak for the course.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/analytics.md",
     "lines": "156",
     "quote": "⚠ Unit-coverage skew: eval set only samples APUSH Units 3/6/8 — main agent should blend before deploy.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/2026-05-27T2130Z_v80b_u1_baseline_course_check.md",
     "lines": "29",
     "quote": "v80b on U1 is ~9pp below its full-course aggregate. U1 is a harder period for the chain.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/system_improvement_brainstorm.md",
     "lines": "39",
     "quote": "Some substandards (KC-1.1.I.* on MCQ_SET) systematically fail; others systematically pass.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 45,
   "verdict": "keep",
   "reason": "Quotes verbatim (export README 115; takeaways memo 12; R42 line 8). An adopted evidence-tier practice, applied to outside results and predicted lifts. General.",
   "statement": "Record how each finding was established — own measurement, single trial, published study, inference or hearsay — and re-test outside results on your own items before relying on them.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/EXPORT_README.md",
     "lines": "115",
     "quote": "(T0 = measured on our data, T1 = single trial, T2 = top-tier paper, T3 = inference, T4 = hearsay)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-parent/.agent/memory/auto/research_parallel_team_takeaways.md",
     "lines": "12",
     "quote": "audit_note: T3 not T2 because their stack/account/data may differ; treat as priors not conclusions; low confidence",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/02_R42_CoVe_DBQ_spec.md",
     "lines": "8",
     "quote": "**Evidence tier:** T2 (cited, scope-flagged). Predicted lift is T4 until Quill measures.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 46,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (autopsy 136; distilled report 186; kit README 139). The kit README lists injected scope boundaries as the fix for out-of-scope items in a design table, and nothing measured that, so 'credited with' became 'listed as the fix'. The 'worse' arm rests on six items (against). A fair open question.",
   "statement": "How much context to give a writer is unsettled: layering curriculum notes on top of source documents did worse in a six-item trial and many examples can hurt dense courses, while injected scope boundaries are listed as the fix for out-of-scope items.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md",
     "lines": "136",
     "quote": "- DBQ route should prefer D13-only source grounding. Do not layer generic curriculum notes into the DBQ prompt until an A/B proves no regression; PATH G hybrid was worse than D13-only.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md",
     "lines": "186",
     "quote": "- For dense courses like APUSH, too many prompt examples can hurt; prefer exact facts/source packs over long example lists.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/README.md",
     "lines": "139",
     "quote": "| Out-of-scope questions slip through | `assessment_boundaries` injected at gen time |",
     "verbatim": true
    }
   ],
   "against": "The 'worse' result rests on six items: \"6 dbq prompts (from WAVE B subset). Build inputs for:\" (helpers/data/build_PATH_G_dbq_hybrid.py line 4).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 47,
   "verdict": "keep-with-fix",
   "reason": "Swapped the two quotes that name a job role for verbatim fragments of the same passage (lines 206-208 and 209-211). Source-free items passed the judge at 90% on fresh items and 100% on chosen ones, and the files read hold no measure of what students learn from either form, so the question is open.",
   "statement": "Whether source-free recall items serve practice as well as source-based items is untested: the judge passed both, and the source-free form differs from the exam form.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/EXPLOIT-002-stimulus-strip.md",
     "lines": "206-208",
     "quote": "The only \"tell\" is that they lack a primary-source stimulus — which makes them weaker AP-prep than the live exam form (where stimulus analysis is the whole point)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/EXPLOIT-002-stimulus-strip.md",
     "lines": "209-211",
     "quote": "Many textbook drills and formative-assessment items omit stimuli for the same reason (faster recall practice).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/SECOND_TIER_REASON.md",
     "lines": "19",
     "quote": "- **Stem-only review-drill products**: explicit non-exam-format MCQs (no stimulus) for AP-prep practice apps, where the IB grader rubric matches the product shape.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 48,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, but the third piece of evidence is a training result: fine-tuning one model on narrative data (v94) wiped out the document-based and question-set formats. That is model-training mechanics, not one generator per type against a shared one, so dropped that clause and that evidence. Cited instead the distilled report's rule (per-type modules, no single shared prompt surface) and its type-specific validators. Changed kind to adopted rule: the synthesis tallies the pattern as 'confirmed' in four projects without a measured comparison.",
   "statement": "Generate each item type through its own steps with type-specific checks, so a change to one type cannot break another.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/MASTER_SYNTHESIS.md",
     "lines": "74",
     "quote": "| Per-type generation | confirmed | confirmed | confirmed | confirmed | compatible | T1 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md",
     "lines": "172",
     "quote": "- Use per-type generator modules. APUSH production should not have one shared prompt surface for all cells.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md",
     "lines": "54",
     "quote": "- This is the right ownership boundary: change MCQ_SET without risking DBQ or SAQ.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/k_12_social_studies_distilled.md",
     "lines": "74",
     "quote": "- Add type-specific deterministic validators before scoring: option count, answer count, explanation consistency, answer uniqueness, schema validity.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt",
   "lines": "40",
   "quote": "**Display Timing**: Content is ONLY an \"answer giveaway\" if shown BEFORE the student attempts to answer.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/next_live_run_prep.md",
   "lines": "75",
   "quote": "**Symptom**: 24 rows tagged `answer_telegraph` — stem repeats the distinctive noun phrase of the correct option.",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/pending_review/2026-05-22T211855Z_exploits_EXPLOIT-003-mcqset-phrase-anchor/source_report.md",
   "lines": "92-94",
   "quote": "The judge cannot reliably distinguish \"question explicitly quotes a stimulus phrase\" from \"question genuinely requires that phrase to answer\".",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/common_pre_checklist.md",
   "lines": "43",
   "quote": "- [ ] Question fails the counterfactual: \"if I deleted the stimulus, can the student still get this right?\" — must be NO",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_evaluation.txt",
   "lines": "387",
   "quote": "- **Borderline-correct distractors**: an option labeled incorrect is actually a defensible answer under the stem's *named* criteria.",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01_session_end/SHADOW_HANDOVER.md",
   "lines": "60",
   "quote": "| MCQ answer-A bias | A=64.5%, B=27%, C=7.8%, **D=0.7%**, E=0% (vs uniform 25% expected) |",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/next_live_run_prep.md",
   "lines": "58",
   "quote": "**Symptom**: 62 of 71 MCQ_SET failures fire `educational_accuracy` aggregate; 61 fire `answer_balance` (children share correct letter); 47 fire `redundant_questions` (children test same skill).",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_set_evaluation.txt",
   "lines": "345",
   "quote": "- Each question tests a distinct aspect",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/KNOWN_ISSUES.md",
   "lines": "45-46",
   "quote": "The correct denominator for IB pass rate is `pass + fail` (excluding skips), not `pass + fail + skip`.",
   "ok": false
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt",
   "lines": "23",
   "quote": "- Self-advocacy metadata arguing every metric should pass",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/v18_rebuild_scope.md",
   "lines": "54-55",
   "quote": "4. **Atlas verify** (free) — every source URL must 200; every passage must substring-match the verified URL's body.",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md",
   "lines": "122",
   "quote": "If a visual source is ever allowed, the actual visual or a faithful OCR/caption payload must be supplied by retrieval, not invented by the model.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/KNOWN_ISSUES.md",
   "lines": "10",
   "quote": "**Symptom**: local mirror's DBQ pass rate is 5-25%; live export shows 90%+.",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/k_12_social_studies_distilled.md",
   "lines": "63",
   "quote": "- Article evaluation falsely failed long articles because only the first 3,000 chars were evaluated; raising the limit to 12,000 fixed the evaluator-side bug.",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md",
   "lines": "155",
   "quote": "- Transform-layer data loss was catastrophic: MCQ_SET stimulus attribution, SAQ stimulus attribution, LEQ scoring notes, DBQ author/title/date/HIPP fields were dropped before evaluation.",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt",
   "lines": "5",
   "quote": "You should only fail a metric when you find a clear, concrete, unambiguous violation that you can quote and explain.",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/RUBRIC_BLINDSPOTS.md",
   "lines": "75-77",
   "quote": "Without a quotable spec, this metric default-passes regardless of how non-standard the item is (stem-only, no stimulus, terse explanation).",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/quarantine/2026-05-22T163819Z_reports_mcqset_50_50_live_verified_20260522/source_report.md",
   "lines": "25",
   "quote": "- Two inherited-passing candidates failed live IB and were not included in final artifact.",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/02_R42_CoVe_DBQ_spec.md",
   "lines": "151",
   "quote": "With IB's 17pp per-cell variance on identical inputs (R41 finding), a single 30-prompt DBQ eval is uninterpretable.",
   "ok": true
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_oracle_session/HANDOVER.md",
   "lines": "396",
   "quote": "- **B1.** When IB curriculum API returns 503, does `evaluators/base.py` fail-the-row, fall-back-to-bundled-facts, skip-factual-verification, or default-pass?",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/CHANGELOG.md",
   "lines": "30",
   "quote": "- **Quill `s-quill-ib-calibration-spot-check-1500`** — 10 known-correct curriculum API facts → MCQ stems → IB grader → expect 10/10 factual_accuracy=1.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/FINAL_REPORT.md",
   "lines": "8-10",
   "quote": "lifts a deliberately mid-quality hand-crafted batch from \"no chance\" to **100% (30/30)**.",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/SELECTOR_CALIBRATION_TAKEAWAYS_20260520.md",
   "lines": "12",
   "quote": "2. Winner-only scoring is not selector calibration.",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/coordination/.archive/CLONE_PARTIAL_WORK_2026-04-30T1510Z.md",
   "lines": "28",
   "quote": "2. Save rejected attempts to `*_rejects.jsonl` for debugging (script currently only writes kept rows)",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/analytics.md",
   "lines": "46",
   "quote": "On the same 297 prompts, the IB grader (gpt-5.2 default-PASS bias) gives **92.3%**, but the held-out Gemini-3.1-pro judge gives **49.2%**.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/analytics.md",
   "lines": "64",
   "quote": "- DBQ + mcq_set cells: held-out judge says **0/30** even when IB says 70-100%.",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/coordination/.archive/CLONE_VERIFY_GRADER.md",
   "lines": "12",
   "quote": "- **+25.92pp swing from grader version alone**",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/achieved.md",
   "lines": "69",
   "quote": "Root cause: paqpgdst's MCQ_SET pass rate on HOLDOUT prompts is **0%** (0/176 K=3 attempts), vs ~20% on eval baseline.",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/CHANGELOG.md",
   "lines": "20",
   "quote": "- **Quill Q1 (13:30Z):** APUSH/SAQ vs APWH/SAQ +23pp factual_accuracy gap, clustered in APUSH unit-6 (Gilded Age) + unit-8 (Cold War) named-entity hallucinations",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/d13_dbq_corpus_pipeline_spec.md",
   "lines": "33",
   "quote": "**Every row carries source_snapshot_hash** — provenance integrity intact",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/CHANGELOG.md",
   "lines": "81",
   "quote": "- Verified extraction completeness: 8/8 md5 hash spot-checks MATCHED between source and oracle",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/postmortem_v89_v90_v91.md",
   "lines": "32",
   "quote": "Per v91 ABORT_DEAD: pipeline-side handling of DBQ scores 87.9% — the model CAN do DBQ when given runtime context, but cannot be TRAINED to.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md",
   "lines": "157",
   "quote": "- Flash research stage could hallucinate facts that poisoned compile; verified facts were better than LLM-generated research.",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/DBQ_GAP_ANALYSIS.md",
   "lines": "4",
   "quote": "Failures are driven almost entirely by **topic/rubric misalignment**, not hallucination or structural errors.",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/ib_pass_criteria_pack/README.md",
   "lines": "72",
   "quote": "When `factual_accuracy` or `stimulus_quality` zeros, the row passes 0% of the time (kills=1.0).",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt",
   "lines": "250",
   "quote": "| 1 | 0–2 | 0.70–0.84 | INFERIOR |",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/MASTER_SYNTHESIS.md",
   "lines": "264",
   "quote": "Every failed result should map to a failed hard dimension and item type before any fix is chosen.",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/quarantine/2026-05-22T155705Z_data_v87_step_function_gate.py/source_report.md",
   "lines": "51",
   "quote": "crit_collapse = any(d <= -5.0 for d in crit.values())",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/data/output/fact_lookup_for_generation/README.md",
   "lines": "88",
   "quote": "| `req.grade` | unit number as string (e.g., `\"1\"`) |",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/run_0506c1fd_v2_final_live_export_analysis.md",
   "lines": "11",
   "quote": "- Grade echo issue detected in export content/request metadata.",
   "ok": false
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md",
   "lines": "55",
   "quote": "Why it fails: the model describes an absent map.",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/WEEKLY_APUSH_PIL_REPORT_20260520.md",
   "lines": "480",
   "quote": "Gemini should only rank validator-clean candidates. If every candidate has the same flaw, Gemini cannot create a passing item.",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/analytics.md",
   "lines": "41",
   "quote": "| v29 + RAG + BoN K=8 (v2.4.0) | 92.3% | 49.2% | n/a | ⚠ 43.1pp Goodhart gap |",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/CHANGELOG.md",
   "lines": "93",
   "quote": "**Goodhart risk surfaced:** training rows aligned to grader rubric → higher pass rate, but at risk of optimizing the rubric not actual AP skill.",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_set_evaluation.txt",
   "lines": "132",
   "quote": "- Object counts and answer balance analysis are AUTHORITATIVE - do NOT attempt to re-count or recalculate.",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/KNOWN_ISSUES.md",
   "lines": "129-130",
   "quote": "**Root cause**: the filters in `scripts/filters/*.py` are individually plausible but their bundle over-rejects valid candidates.",
   "ok": false
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/pending_review/2026-05-22T211855Z_exploits_EXPLOIT-003-mcqset-phrase-anchor/source_report.md",
   "lines": "66-68",
   "quote": "The single failing critical metric is `educational_accuracy`, driven by ≥1 of 3 child questions failing its own MCQ-level checks",
   "ok": true
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/artifacts/pending_review/2026-05-23T000424Z_exploits_EXPLOIT-004-saq-no-stimulus/source_report.md",
   "lines": "122-124",
   "quote": "Add a check: the criterion must specify a SPECIFIC, NAMED historical fact that the example must satisfy, not a generic category.",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/handover/2026-05-01T1039Z_compass_session_close/02_R42_CoVe_DBQ_spec.md",
   "lines": "149",
   "quote": "One knob per eval, or you can't attribute deltas.",
   "ok": true
  }
 ]
}
```
