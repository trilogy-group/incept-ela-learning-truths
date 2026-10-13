# verify:gap:ap-live-agent-memories

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "ap-live-agent-memories",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "statement": "Sort a judge run's outcomes by type (real verdicts, timeouts, service errors, outputs that could not be parsed) and report how many real verdicts each score rests on, because errors counted as failures can fake a collapse.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_ib_grader_v266_dbq_mcqset_timeout_99pct_at_concurrency_default_2026_06_02.md",
     "lines": "10",
     "quote": "- DBQ: 1 real eval + 99 timeouts → headline 1% PASS (artifact)",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_ib_grader_v266_dbq_mcqset_timeout_99pct_at_concurrency_default_2026_06_02.md",
     "lines": "38",
     "quote": "Effective_eval_count = N − timeouts, which is the true sample size.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_ib_grader_timeout_300_mcq_set.md",
     "lines": "11",
     "quote": "**28 of 30 mcq_set rows timed out** producing `grade_fail status` and corrupting the cell pass-rate denominator.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "75",
     "quote": "`parse_ok=false` lumps 5xx with JSON fails; misread cost a wrong \"v20a more brittle\" claim. Always bucket by error type.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_gemma4_wraps_json_in_markdown_fences_default_2026_06_02.md",
     "lines": "9",
     "quote": "2026-06-02 IB n=500 eval of v92 first-run failed 499/500 with `json_parse:JSONDecodeError`.",
     "verbatim": true
    }
   ],
   "against": "Timeouts clustered on long outputs: \"Other cells (LEQ + MCQ + SAQ) time out at 1-6% — they're fine at default.\" (feedback_ib_grader_v266_dbq_mcqset_timeout_99pct_at_concurrency_default_2026_06_02.md, line 7). An output that cannot be parsed is the item's own failure when the format is part of the task: \"This is the v38 failure mode (262 rows of answer-format anchors → 0/150 parse_ok).\" (project_eval_is_question_generation.md, line 56). Such failures are counted apart, not dropped.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "All quotes verbatim at the cited lines; numbers match (1 real verdict plus 99 timeouts; 28 of 30; about 60-67% once re-run at a sustainable rate, same file lines 17-18). Sharpened the statement: a parse failure can belong to the item rather than the judge, so outcomes are sorted by type instead of all being set aside. Added the 500-item run that failed 499 times on a strict parser. Near 9 (an unsure judge is neither pass nor miss) but about missing verdicts and the denominator, so kept separate."
  },
  {
   "index": 1,
   "verdict": "keep-with-fix",
   "statement": "Record the judge's version with every score and never compare or subtract scores from different judge versions; re-score so both sides sit on the same version first.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_ib_grader_version_v240_to_v253.md",
     "lines": "26",
     "quote": "The same 297 generations from v29 were scored under both; +25.92pp aggregate / +25pp APUSH from the grader swap alone.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_ib_grader_version_v240_to_v253.md",
     "lines": "42",
     "quote": "- Refuse to compute deltas across grader versions; require both endpoints to agree on grader version OR re-score one side",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/project_v50_v56_strategy_with_numbers_2026_05_12.md",
     "lines": "16",
     "quote": "| v50 (DPO from curriculum500) | 79.87% (r1) | **56.22%** | 1.54pp |",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_mcq_v2.5.6_rubric_tightening.md",
     "lines": "3",
     "quote": "educational_accuracy zero-rate jumping from ~0% to 24-30% across v43-soup + v50 + v51",
     "verbatim": true
    }
   ],
   "against": "Old scores remain valid within their own version: \"- **Past v2.5.3 numbers stay valid as historical baselines for v2.5.3**, just like v2.4.0 numbers stayed valid as v2.4.0 baselines after the v2.4.0→v2.5.3 jump.\" (project_ib_grader_v256_canonical_2026_05_11.md, line 38). The shift had no fixed direction: one version was far more lenient, a later one far stricter.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 63.64% vs 89.56% and +25.92 points match (feedback_ib_grader_version_v240_to_v253.md lines 23, 26). Two fixes. The source asks for one side to be re-scored, not both (line 42). The line 'models that scored 90%+ on v2.5.3 now score 56-58%' (project_v50_v56 line 9) is not backed by its own table: the canonical model has no v2.5.6 score and v50 went 79.87% to 56.22% (line 16). The table row replaces it. Near 45 but about comparing across judge versions."
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "statement": "Before calling a change better, re-score unchanged items several times to measure the judge's spread for each item type, count only differences larger than about twice that spread, and repeat a headline win before acting on it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_grader_variance_discovered.md",
     "lines": "20",
     "quote": "**APUSH (n=150):** r1=86.67%, r2=89.33%, r3=86.67% → mean 87.56%, σ=1.54pp, range=2.67pp",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_grader_variance_discovered.md",
     "lines": "36",
     "quote": "**Insight:** DBQ drives ~all the noise. MCQ/LEQ are essentially deterministic. SAQ and MCQ_SET have small (~2pp) variance.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_grader_variance_discovered.md",
     "lines": "53",
     "quote": "**None of our \"wins\" since v29 are above the noise floor.** They're all clustered at ~133-134/150.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-oracle/memory/project_v40h_breakthrough_doctrine_drift.md",
     "lines": "9",
     "quote": "90.00% APUSH (135/150) on IB v2.5.3, +3.33pp over v29's 86.67% baseline today. Above the 3pp σ-band → real lift.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_three_rule_updates_20260506.md",
     "lines": "12",
     "quote": "(2) v40h \"0.9 breakthrough\" stat-tied with v29 under multi-seed (R8 caught it).",
     "verbatim": true
    }
   ],
   "against": "Where the judge is deterministic, any difference counts: \"- MCQ / LEQ cells: ANY non-zero delta is real (deterministic baseline)\" (project_grader_variance_discovered.md, line 42). Re-scoring stored outputs measures only the judge; regenerating adds noise of its own: \"σ_inference + σ_grader combined still gives ~0.5 cont-pp aggregate noise.\" (feedback_baseline_must_be_fresh_gen.md, line 49).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim. One number fix in the supporting text: the 1.54-point spread is for the 150-item course set, and across all 297 items it was 1.18 (lines 19-20). The detail that the later 'breakthrough' had once cleared the 3-point band comes from the oracle note (line 9), now cited. This turns 34 (verdicts vary between runs) into a decision rule, so it is not a duplicate."
  },
  {
   "index": 3,
   "verdict": "keep-with-fix",
   "statement": "Compare versions on the mean of the continuous score as well as the pass rate, because items near the pass mark flip on small noise and move the pass rate when quality has not changed.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_r41d_continuous_metric.md",
     "lines": "27",
     "quote": "The IB grader thresholds at 0.85 internally. Items with continuous score in [0.80, 0.90] flip pass↔fail under any tiny continuous-side noise. For DBQ where ~20% of items sit in this band, this alone produces 13-17pp binary swing per run.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_r41d_continuous_metric.md",
     "lines": "71",
     "quote": "| richer-RAG dbq | -6.1 binary-pp | +0.06 cont-pp | binary \"regression\" was 100% threshold artifact — DBQ continuous quality unchanged |",
     "verbatim": true
    }
   ],
   "against": "The two other examples in these notes are artifacts of comparing fresh outputs with stored ones. \"| v36b | -0.88 cont-pp | **+0.80 cont-pp** | ✓ REAL LIFT |\" (feedback_baseline_must_be_fresh_gen.md, line 39) reverses the 'pass rate up, mean down' case. The MCQ_SET '-3.08 real' drop (project_iteration_2026_04_29_inference_time_exhausted.md, line 32) equals the stored-versus-fresh gap on that type: \"- apush/mcq_set: -3.14 cont-pp\" (feedback_baseline_must_be_fresh_gen.md, line 25). The delivered target stays a pass mark (\"Threshold of 0.85 is fixed by mission.\", reference_inceptbench.md line 83), the score is lumpy, and an average must not let partial credit offset a hard fail (truths 59, 60).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim and numbers match, but the claim that 'a pass-rate gain can hide a lower average' rests on v36b (+1.77 on pass rate, -0.88 on the mean). The fresh-baseline note reversed that to +0.80. The 'real' MCQ_SET drop of -3.08 also equals the -3.14 stored-versus-fresh artifact. Kept the threshold-flip half, which two things support: about 20% of document-based items sat between 0.80 and 0.90, and a 6.1-point pass-rate drop came with an unchanged mean. The two statistics papers behind the rule are cited without links."
  },
  {
   "index": 4,
   "verdict": "keep-with-fix",
   "statement": "Compare a new way of generating content against a freshly generated baseline rather than stored outputs re-scored, because generation varies between runs even at temperature zero.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_baseline_must_be_fresh_gen.md",
     "lines": "3",
     "quote": "v29 fresh-gen 3-run continuous = 0.9307; v29 frozen-gen 3-run continuous = 0.9475. Δ 1.68 cont-pp from inference variance (temp=0 not deterministic across gen runs).",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_baseline_must_be_fresh_gen.md",
     "lines": "17",
     "quote": "**For any continuous-metric model A vs model B comparison, both A and B must use FRESH generations. Don't compare test configs (fresh gens) against frozen baseline (re-scored).**",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_baseline_must_be_fresh_gen.md",
     "lines": "37",
     "quote": "| field-routed RAG | -0.69 cont-pp | **+0.99 cont-pp** | ✓ REAL LIFT |",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_baseline_must_be_fresh_gen.md",
     "lines": "39",
     "quote": "| v36b | -0.88 cont-pp | **+0.80 cont-pp** | ✓ REAL LIFT |",
     "verbatim": true
    }
   ],
   "against": "\"3. **For binary pass rate**, frozen baseline is fine (insensitive to inference variance).\" (feedback_baseline_must_be_fresh_gen.md, line 47). The gap rests on one fresh and one stored generation, each scored three times; how much fresh runs differ from each other is not shown.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 0.9475, 0.9307, 1.68 points and the 150 prompts match (lines 3, 12). The source says 'several' regressions reversed, but its table shows two of four (lines 36-39), so those rows replace the summary line. This note also undercuts evidence for candidates 3, 9, 20 and 21, which compared fresh outputs with the stored baseline (project_iteration_2026_04_29_inference_time_exhausted.md line 19 uses 0.9475)."
  },
  {
   "index": 5,
   "verdict": "keep",
   "statement": "Treat a result on about 20 items per item type as provisional and confirm it on a larger sample before building on it, especially for types that have failed before.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_n_scale_tightens_CI_exposes_n100_anomalies_2026_06_01.md",
     "lines": "7",
     "quote": "The n=100 CI is ±15pp per cell (at n=20/cell), wide enough to mask structural floors.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_n_scale_tightens_CI_exposes_n100_anomalies_2026_06_01.md",
     "lines": "12",
     "quote": "- MCQ_SET 100% → 0% was the dramatic collapse: cell has structural issue (gemma family can't follow Option B 6-region schema at inference, matches Cheater's v90c K=18 0/16 finding 6/1 18:50Z); single-seed n=20 just got lucky",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/fdpo_pipeline.md",
     "lines": "12",
     "quote": "- Pass rates: **83.3% at N=30 / 60% at N=100** (N=100 is more reliable)",
     "verbatim": true
    }
   ],
   "against": "\"Counter-case: When the cell has NO structural issue history (e.g., MCQ + SAQ have been consistently at 95-100% for multiple versions), n=100 100% is more credible. The skepticism scales with prior failure rate.\" (feedback_n_scale_tightens_CI_exposes_n100_anomalies_2026_06_01.md, line 26).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; ±15 points at 20 per type, 100% to 0%, and 83.3% at 30 against 60% at 100 all match. In the supporting text, the five-item probe case was 82 of 282 attempts failing, which is 29.1% (recipe_track_b_openstax_pair_generation.md line 47); another note rounds it to 31%. Under the same judge, 20 of 20 and then 0 of 100 are too far apart for sampling error alone, so those runs probably differed in more than size. The rule holds either way. name_bearing_source is judged on file basenames, since every path carries the account's home folder."
  },
  {
   "index": 6,
   "verdict": "keep",
   "statement": "Check a second judge's agreement with the reference judge separately for each item type before using it to filter or promote, and when it fails every item of one type, suspect its rubric or parsing before the content.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_stacked_decode_RAG_judge_result.md",
     "lines": "46",
     "quote": "Gemini scored 0/30 on EVERY mcq_set and dbq cell. The earlier Claude Opus spot-check on 24 BoN-lifted rows had 88% agreement with IB.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_stacked_decode_RAG_judge_result.md",
     "lines": "51",
     "quote": "- My single-prompt JSON rubric (\"factual_accuracy 0-1, overall 0-1\") can't decompose those",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_gemini_ib_dbq_judge_divergence_97pp_2026_06_02.md",
     "lines": "33",
     "quote": "- LEQ judge bias goes the OTHER way (Gemini under-credits LEQ). So \"Gemini judge is always wrong\" is too strong. The pattern is direction-specific per cell.",
     "verbatim": true
    }
   ],
   "against": "Part of a reported 97-point disagreement came from the reference judge timing out (\"- DBQ: 1 real eval + 99 timeouts → headline 1% PASS (artifact)\", feedback_ib_grader_v266_dbq_mcqset_timeout_99pct_at_concurrency_default_2026_06_02.md line 10), and the judges did agree on a structural failure: \"- Both judges agreed on MCQ_SET 0% — so Gemini can be reliable when the failure mode is structural enough that both judges detect it.\" (feedback_gemini_ib_dbq_judge_divergence_97pp_2026_06_02.md, line 34).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 0/30 on every multi-part type, the 88% earlier agreement and the 19-point gap on long essays all match. The over-credit on document-based essays leaned on a reference run that was mostly timeouts. Re-run at a sustainable rate, the reference gave about 60-67% against the second judge's 98%, so the over-credit holds but is smaller. Agreement with another judge is consistency, not correctness (truths 35, 37, 44). The same notes show that the '43.1pp gap quantifies the contamination' line (feedback_full_cost_accounting_no_zero_marginal_lie.md line 45) measured this judge's rubric failing, not contamination."
  },
  {
   "index": 7,
   "verdict": "keep-with-fix",
   "statement": "Score each item's output several times and separate items that fail every time from items that flip: the flips measure the judge's noise, and the stable failures are the ones worth fixing.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v29_failure_analysis_3run.md",
     "lines": "20",
     "quote": "| Stable fail (0/3) | 14 | 9.3% | REAL MISSES — must train on |",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v29_failure_analysis_3run.md",
     "lines": "21",
     "quote": "| Flipped (1-2/3) | 10 | 6.7% | Grader noise — Compass R41 multi-call majority denoises |",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v29_failure_analysis_3run.md",
     "lines": "65",
     "quote": "**Don't waste effort on flipped items** — they're grader noise.",
     "verbatim": true
    }
   ],
   "against": "The near-miss priority did not hold in the follow-up on 9 of these items: \"| 58090 | apush/saq | 0/3 (0.0/0.0/0.0) | 3/3 (1.0/1.0/1.0) | RESOLVED |\" while \"| 58794 | apush/saq | 0/3 (0.8/0.8/0.8) | 0/3 (0.8/0.8/0.8) | unchanged |\" (project_richer_rag_resolves_stable_fails.md, lines 30 and 35). Across many generators no item passed every time: \"- `always_passed_all`: 0 items (0.0%)\" (project_quill_discovery_cross_model_volatility_2026_05_11.md, line 19).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 84%, 9.3% and 6.7% match. Dropped 'starting with the near misses'. Six items scored 0.7-0.8 in every run, and three of them became triple passes. Both items that had scored zero also became triple passes (project_richer_rag_resolves_stable_fails.md lines 27-35). So the evidence does not single out near misses. The flips here are judge noise by construction, because the same outputs were re-scored."
  },
  {
   "index": 8,
   "verdict": "keep-with-fix",
   "statement": "Read the shape of failing scores: once judge errors are ruled out, failures that cluster at one value and repeat across runs and generators mark a structural defect that resampling will not fix.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_v92_mcq_set_structural_fail_at_scale_confirmed_2026_06_02.md",
     "lines": "12",
     "quote": "- Fail <0.70 (deep): 55 (clustered at 0.65)",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_v92_mcq_set_structural_fail_at_scale_confirmed_2026_06_02.md",
     "lines": "13",
     "quote": "- Zero (timeouts): 2",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_v92_mcq_set_structural_fail_at_scale_confirmed_2026_06_02.md",
     "lines": "36",
     "quote": "The score-cluster pattern at 0.65 (vs scattered fails) is the structural-fail tell.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_dbq_stimulus_v2.5.6_root_cause.md",
     "lines": "19",
     "quote": "σ=0 across seeds for v43-soup and v51; the failure is deterministic at T=0.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_quill_discovery_cross_model_volatility_2026_05_11.md",
     "lines": "30",
     "quote": "for the 93% volatile items, decode-time sampling depth matters; for the 7% hard items, no depth helps.",
     "verbatim": true
    }
   ],
   "against": "Identical repeat failures can be judge errors: \"- MCQ_SET: 9 real evals + 91 timeouts → headline 0% PASS (also artifact)\" (feedback_ib_grader_v266_dbq_mcqset_timeout_99pct_at_concurrency_default_2026_06_02.md, line 11), and \"- σ=0 across seeds for the model-rate (13.3% pass rate, fully deterministic)\" sits next to \"- 20-22 of 30 rows status=grade_fail (Gemini Flash timeout on heavy outputs)\" (project_v50_v56_strategy_with_numbers_2026_05_12.md, lines 41-42). 'Structural' was also relative to one judge version and generator: a different, grounded generator's document sets passed a later judge 139 of 154 times (\"- DBQ: 139/154 = **90.3%**\", recipe_track_b_openstax_pair_generation.md line 67).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim. One number fix: of 58 items done, 2 timed out, so 55 of the 56 verdicts that came back fell below 0.70 (lines 9-13), not 55 of 58. The note claims five independent passes but lists only three others, and one of those clustered at 0.80, not 0.65 (line 18). This complements 65 (best of several fixes random slips, not systematic failures) with a way to tell the two apart, so it is kept separate."
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "statement": "Re-run a fix on the whole item set, not only on the failures it targeted, because a change that repairs the targeted items can break items that used to pass.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_richer_rag_resolves_stable_fails.md",
     "lines": "37",
     "quote": "**Aggregate on this 9-item slice: 0% → 63% pass rate. +63pp.** Way above the ~3pp noise floor.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_richer_rag_per_cell_tradeoff.md",
     "lines": "23",
     "quote": "| apush/saq | 77.8% | **68.3%** | **-9.5pp** | ±3.8pp | ✗ REAL REGRESSION |",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_richer_rag_per_cell_tradeoff.md",
     "lines": "24",
     "quote": "| **APUSH agg** | **87.56%** | **85.67%** | -1.89pp | ±3.1pp | noise (washed out) |",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_richer_rag_resolves_stable_fails.md",
     "lines": "69",
     "quote": "- Don't claim full +63pp transfers to 150-item — small sample. Pending full APUSH eval result.",
     "verbatim": true
    }
   ],
   "against": "The same change was a real gain on another item type: \"| apush/mcq | 93.3% | **100.0%** | +6.7pp | ±0.5pp | ✓ REAL LIFT |\" (project_richer_rag_per_cell_tradeoff.md, line 19). The full-set run compared fresh outputs with the stored baseline, and that alone moved short answers: \"- apush/saq: -3.60 cont-pp (fresh vs frozen)\" (feedback_baseline_must_be_fresh_gen.md, line 24), so part of the drop may be that artifact.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 0% to 63% on 9 items and -9.5 points on short answers match. The note says about 17 short-answer items broke, net 14 (line 28). That cannot be right: the type has 30 items, so -9.5 points is about 3 items. The table row replaces that sentence."
  },
  {
   "index": 10,
   "verdict": "keep",
   "statement": "Before crediting a change with a score gain, confirm the change actually shows up in the outputs, because gains were claimed for mechanisms that never ran.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "38",
     "quote": "0/297 v35 outputs emit any reflection token at decode (Self-RAG mechanism didn't fire). The +1.33pp lift is noise + grader artifact, NOT a Self-RAG mechanism win.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/recipe_v35_self_rag_reproducible.md",
     "lines": "135",
     "quote": "- 0/297 v35 outputs emit ANY reflection token (`[Retrieval=…]`, `[IsRel=…]`, `[IsSup=…]`, `[IsUse=…]`)",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/mcq_set_improvement_log.md",
     "lines": "11",
     "quote": "**Impact**: The Research→Compile pipeline NEVER WORKED for either MCQ or MCQ_SET. Both silently fell back to legacy generation paths every time. The research step was designed to gather verified primary sources and plausible alternatives, but it always crashed before it could run.",
     "verbatim": true
    }
   ],
   "against": "Two notes disagree on whether the silent fallback was better: \"- This forces legacy fallback pipeline which produces BETTER MCQ results\" (ap-social-studies-generator-python memory MEMORY.md, line 15) versus \"**Result for MCQ**: With research actually working, MCQ went from 96% → **100% (10/10, all perfect 1.00 scores)**.\" (mcq_set_improvement_log.md, line 15). Both rest on about 10 items.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 0/297, +1.33 points and p=0.7744 match (MEMORY.md line 38; recipe_v35_self_rag_reproducible.md lines 135-136). Near 38 (a check that never fired), but this is about crediting a gain to a mechanism that never ran."
  },
  {
   "index": 11,
   "verdict": "keep-with-fix",
   "statement": "Back every reported score with the saved per-item file that anyone checking it can open, and check that the file covers every item submitted.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_eval_runs_sync_to_icloud.md",
     "lines": "16",
     "quote": "Without sync, helpers running phantom-audit on numeric claims correctly find no backing file, even when the claim is real on main-A's laptop.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_eval_runs_sync_to_icloud.md",
     "lines": "30",
     "quote": "Phantom-audit should grep `_meta.n_input` vs `total.n` to detect; example seen on `summary_v29_drift_recheck_v2_2026_05_04.json` where n_input=150 but total.n=110.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_three_rule_updates_20260506.md",
     "lines": "12",
     "quote": "(1) Shadow T8 v29 baseline phantom (citation chain broken — required re-running v29 at canonical schema to close)",
     "verbatim": true
    }
   ],
   "against": "A missing file can be a sync delay rather than a false claim: \"- iCloud sync delay (Apple-side) can add 5–30 min on top of the 5-min sync rule. If a flag is dropped within that window, treat as advisory; outside it, treat as a real sync miss.\" (feedback_eval_runs_sync_to_icloud.md, line 31).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 150 items submitted against 110 summarised matches. Rewrote 'reviewers', which is a role word. Overlaps 39 (keep every judgment whole) and candidate 0 (report the denominator), but adds the check that the file covers every item."
  },
  {
   "index": 12,
   "verdict": "keep-with-fix",
   "statement": "Check every item used as training material or as an example against every held-out test file, because a check against one test file passed 30 'unique' items that were all test items.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_eval_contamination_check_all_eval_files.md",
     "lines": "18",
     "quote": "my first contamination check compared only against `apush_baseline.jsonl` (n=30 mcq_set hashes)",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_eval_contamination_check_all_eval_files.md",
     "lines": "18",
     "quote": "Found APUSH overlap was 100% — those \"30 unique\" rows were in fact eval-identical.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_eval_contamination_check_all_eval_files.md",
     "lines": "20",
     "quote": "Had I trained on those rows, v54 would have learned its eval set verbatim → fake pass rate, contamination, useless iteration. Caught before training; saved the cycle.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/training_data_70k.md",
     "lines": "80",
     "quote": "- `data/combined_val.jsonl` and `data/combined_test.jsonl`: 21% overlap with catchup_raw via cu-* IDs",
     "verbatim": true
    }
   ],
   "against": "none found. The inflated score is the note's expectation, not a measurement, since the leak was caught before training (line 20).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 100% overlap on 30 items and 21% overlap match. Reworded the cause: the leak was caught before training, so it would have inflated scores rather than did. The evidence is about training rows; examples are a direct extension of the same leak. Close to 48 (a later test on new items) but about keeping test items out."
  },
  {
   "index": 13,
   "verdict": "keep-with-fix",
   "statement": "Deduplicate and count items on their full content, not on an opening prefix or on the count an upstream step reports, because items that share an opening need not be duplicates and reported counts can include repeats.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}/memory/training_data_70k.md",
     "lines": "30",
     "quote": "`build_70k_dataset.py` used MD5 hash of first 200 chars of assistant content for dedup. This caused massive FALSE POSITIVES — many different records share the same first 200 chars (e.g., MCQs with the same question opening). Fixed to use **full content MD5 hash**.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/training_data_70k.md",
     "lines": "32",
     "quote": "**Before fix:** appeared to have only 37k unique records (34% false dedup rate)",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_cache_pool_count_vs_unique_doc_count_distinct_2026_06_01.md",
     "lines": "9",
     "quote": "Actual unique-doc pool was 12-14 per KC after dedup, not 31.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 34%, 37k, and 12-14 against 31 all match. Replaced 'producer', which can read as a job role, and softened 'are not duplicates' to 'need not be'."
  },
  {
   "index": 14,
   "verdict": "keep-with-fix",
   "statement": "When an item needs source documents, take real excerpts from a verified collection and place them in the item in code, because a writer asked to supply documents invents plausible authors, dates and text even when handed a real excerpt, and copies provided documents word for word only some of the time.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/recipe_track_a_b_kc_pack_substitution.md",
     "lines": "11",
     "quote": "the `documents` array is **synthesized** — Gemini invents author names + dates + content.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/recipe_track_a_b_kc_pack_substitution.md",
     "lines": "11",
     "quote": "Even when grounded in a real OpenStax `_GROUND_TRUTH_SOURCE_` excerpt in the prompt, output documents are stylistic-real not literal-real.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_dbq_stimulus_v2.5.6_root_cause.md",
     "lines": "3",
     "quote": "PILLAR 1 confirmed dbq stimulus_quality zeroed 98-100% across v43-soup + v50 + v51 on IB v2.5.6 (n=270 dbq attempts × 3 models, σ=0). Only real-source documents bypass the rubric.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/project_v50_v56_strategy_with_numbers_2026_05_12.md",
     "lines": "32",
     "quote": "- Hot-patch full validation n=30: **10/30 = 33.3% locked rate**",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_d13_inference_injection_partial_fix_2026_05_12.md",
     "lines": "26",
     "quote": "- Success rate at \"use docs literally\" is ~20% on v43-soup (1 of 5 graded)",
     "verbatim": true
    }
   ],
   "against": "Placing documents in code was designed but never run: \"- Integration tested 0 in production (will fire once Track B survivor access is resolved + PIL approves Track A)\" (recipe_track_a_b_kc_pack_substitution.md, line 74). The measured rise from 0% to 33.3% came from putting real documents in the writer's request. A different, grounded writer's own document sets passed a later judge version 139 of 154 times (\"- DBQ: 139/154 = **90.3%**\", recipe_track_b_openstax_pair_generation.md line 67), so the 98-100% failure is specific to one judge version and to writers given no excerpt; the case for real excerpts rests on authenticity. Substituted documents also need checking against the question: \"In spot-checks, Track A substituted documents kept thematic coherence ~85% of the time.\" (recipe_track_a_b_kc_pack_substitution.md, line 52).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 98-100%, 270 attempts and 10/30 match. Two fixes. The supporting text says curriculum context left these items at 0/6 'in three independent runs', but only one of those three arms added curriculum context to these items (feedback_dbq_rag_inference_cannot_fix_v2.5.6.md lines 12-14). A second arm in another probe put it in the system prompt (feedback_d13_inference_injection_partial_fix_2026_05_12.md line 17); both were 0/6. And the 33.3% came from documents in the request, not from placing them in code. Related to 17, 29 and 57, but specific to source documents."
  },
  {
   "index": 15,
   "verdict": "keep-with-fix",
   "statement": "Check each source's attribution (who made it, where, when, and what kind of source it is) as a claim of its own, because generated source sets fail more on attribution than on their sentences.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "65",
     "quote": "- `factual_accuracy`: 9",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "70",
     "quote": "**NOT failing on document text sentences — failing on attribution and structure.**",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "73",
     "quote": "Model names real explorers but assigns wrong geographic scope.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/sft_v4_prompt_engineering.md",
     "lines": "12",
     "quote": "- Removes source attribution from stimulus (main hallucination source)",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/sft_v4_prompt_engineering.md",
     "lines": "18",
     "quote": "**Failure pattern:** Model fabricates specific source attributions and dates. SFT training examples should favor general historical description stimuli, not attributed documents.",
     "verbatim": true
    }
   ],
   "against": "Dropping attributions trades one check for another: \"**Why: `no_source` wins on factual_accuracy (70%) but `no_source_facts` wins on pass rate (60%).**\" (sft_v4_prompt_engineering.md, line 16). Removing attributions moved factual accuracy from 60% to 70% on 20 items (same file, lines 22-23), and the attribution fixes were never re-measured: \"3. **DBQ 12%** — all 4 fixes just applied; need fresh benchmark to measure impact\" (findings_sftv7_20260424.md, line 138).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim. One number fix in the supporting text: the 9 factual-accuracy hits are the total across all 15 failures (line 65). Both the wrong-region pattern and the text author in an image slot fall within them (lines 72, 82), so it is 9 in all, not 9 plus one. Samples are small throughout."
  },
  {
   "index": 16,
   "verdict": "keep-with-fix",
   "statement": "A picture, map or chart in an item, or the description it is made from, must name the specific labels, routes, axes, values or captions its questions use; a generic placeholder gives nothing to analyse.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "91",
     "quote": "### Pattern 3: Generic visual description (clarity_precision, 3 hits)",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "92",
     "quote": "`doc[0].content = \"A historical map showing the geographic context of [topic] during the stated period, with key regions shaded in distinct colors\"` — template text, not analyzable.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "93",
     "quote": "Evaluator: *\"students cannot clearly use the document set as intended.\"*",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "97",
     "quote": "- For MAP: name regions labeled, trade routes shown, territories marked",
     "verbatim": true
    }
   ],
   "against": "The fix was never re-measured, and it rests on three hits: \"3. **DBQ 12%** — all 4 fixes just applied; need fresh benchmark to measure impact\" (findings_sftv7_20260424.md, line 138).",
   "general": true,
   "duplicate_of": "64",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 3 hits matches line 91. The case is a template description standing in for a visual, which 64 already rules out ('never describe one that isn't there'). So this mainly adds evidence to 64, plus the point that a visual must carry the specifics its questions use. It is also near 22 (maps from data). The evidence is thin: 3 hits, and the fix was never re-measured."
  },
  {
   "index": 17,
   "verdict": "drop",
   "statement": "Make every source in a set contribute a different actor, argument or angle, and check the set for near-duplicates before use.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "103",
     "quote": "Two or more documents in the same DBQ have near-identical content/argument.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "104",
     "quote": "Evaluator: *\"Several documents are exact duplicates but numbered as if different.\"*",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/project_perfect_dpo_dataset_inventory_2026_05_18.md",
     "lines": "38",
     "quote": "| apush/mcq_set | 1850 | educational_accuracy(411), difficulty_distribution(381), factual_accuracy(221), test_preparedness(152), non_repetitiveness(146), concept_coverage(130), stimulus_quality(128) |",
     "verbatim": true
    }
   ],
   "against": "The duplicate check was not re-measured: \"3. **DBQ 12%** — all 4 fixes just applied; need fresh benchmark to measure impact\" (findings_sftv7_20260424.md, line 138).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim, but the support is thin and partly misapplied. The duplicate-document pattern (lines 103-104) gives no count, and its fix was never re-measured (line 138). The 1,850-failure row is for question sets that share one stimulus, where non-repetitiveness and concept coverage concern the questions, not several sources. That row fits 68 and could be added there as evidence. What remains, no repetition within a set, is close to 41 and 68."
  },
  {
   "index": 18,
   "verdict": "keep-with-fix",
   "statement": "Don't hand a writer known misconceptions as loose suggestions for wrong options: it may write them into question stems and explanations as if they were true.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_misconceptions_user_prompt_injection_hurts_2026_05_12.md",
     "lines": "15",
     "quote": "| A vanilla (no injection) | 19/22 | 86.4% | 0.968 |",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_misconceptions_user_prompt_injection_hurts_2026_05_12.md",
     "lines": "16",
     "quote": "| B misconceptions appended to user | 14/22 | 63.6% | 0.915 |",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_misconceptions_user_prompt_injection_hurts_2026_05_12.md",
     "lines": "21",
     "quote": "- `mastery_learning_alignment`: 1.000 → 0.727 (**−0.273**) — questions test misconceptions as if valid",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_misconceptions_user_prompt_injection_hurts_2026_05_12.md",
     "lines": "24",
     "quote": "v43-soup includes the misconception content in the question stem or correct-answer rationale rather than in wrong-answer options.",
     "verbatim": true
    }
   ],
   "against": "\"- n=22 small sample, single seed (20260512), single model (v43-soup ty16vgj9)\" (same file, line 32). The same misconceptions inside a background block were credited with better distractors on a 6-item probe: \"**Why (hypothesis):** Curriculum KCs provide canonical assessment_boundaries and common_misconceptions that the model uses as material for distractor generation, lifting difficulty_distribution scores.\" (feedback_mcq_set_RAG_actively_helps_v2.5.6.md, line 15).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 19/22 to 14/22, -22.7 points and 1.000 to 0.727 match. Narrowed: the test covered misconceptions only, not 'other false statements', and it does not show the writer uses 'whatever text it is given'. A 5-item difference on 22 items, from one seed and one model, is suggestive rather than settled. Related to 57 and 62."
  },
  {
   "index": 19,
   "verdict": "keep-with-fix",
   "statement": "Check a writer's instructions for conflicts before generating: in one case a step asking for exact facts overrode a rule forbidding names and dates, and the marking notes it produced failed fact checks.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "50",
     "quote": "**Pattern:** scoring_notes contained specific evidence (dates, named events) that",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "53",
     "quote": "**Root cause:** Two contradicting instructions:",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "54",
     "quote": "- System prompt: `⛔ NEVER list specific event names/dates/people`",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "55",
     "quote": "- User prompt PROCEDURE: `\"Write it as [FACT: <exact phrase>]\"` — granted permission",
     "verbatim": true
    }
   ],
   "against": "\"2. **SAQ 33%** — new categorical-only fix not yet tested; these runs were pre-fix\" (findings_sftv7_20260424.md, line 137).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim. This is one case, and the fix was never re-measured (line 137), so the general claim that 'the output follows the invitation' is narrowed to what was seen. It is consistent with 62: a prohibition lost to an instruction about what to use."
  },
  {
   "index": 20,
   "verdict": "drop",
   "statement": "Add retrieved background to a writer's request only for item types that do not already carry their own source material, and check the effect type by type.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_cell_routed_rag_finding.md",
     "lines": "47",
     "quote": "**RAG augmentation only when prompt doesn't carry its own source content.**",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_cell_routed_rag_finding.md",
     "lines": "32",
     "quote": "| MCQ_SET | Has stimulus | HURTS | Already has source; extra context distracts |",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_iteration_2026_04_29_inference_time_exhausted.md",
     "lines": "39",
     "quote": "3. **MCQ_SET regresses with ANY augmentation**: -3.1 cont-pp regardless of field set. Already has stimulus, additional context distracts.",
     "verbatim": true
    }
   ],
   "against": "\"- apush/mcq_set: -3.14 cont-pp\" (feedback_baseline_must_be_fresh_gen.md, line 25) is the gap between fresh and stored outputs on that type. \"Per-cell measured effect (single run, within noise):\" (project_cell_routed_rag_finding.md, line 35). Under a later judge version a 6-item probe pointed the other way (feedback_mcq_set_RAG_actively_helps_v2.5.6.md, line 9).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim, but the claim that background hurts item types with their own source does not survive the project's own baseline correction. The '-3.1 with any augmentation' for stimulus sets equals the -3.14 gap between fresh and stored outputs on that type, and it was measured against the stored baseline (iteration file line 19). The -10 on document-based essays was one run inside that type's noise (cell-routed file lines 35 and 42; a real change there needs more than 15 points). A later 6-item probe also pointed the other way. What remains, checking the effect type by type, is already 49 and 60, and the context question survives as candidate 21's open question."
  },
  {
   "index": 21,
   "verdict": "keep-with-fix",
   "statement": "Open question: when does added context in one request (scope notes, source documents, curriculum blocks) start to lower quality? Short-answer items lost points under long scope notes, and adding curriculum notes on top of seven documents dropped the average score from 0.502 to 0.125 on 6 items, while multiple-choice items gained from the same scope notes.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_richer_rag_per_cell_tradeoff.md",
     "lines": "38",
     "quote": "For SAQ (3 sub-questions, structured response): the verbose context confuses the response format. SAQ requires terse 2-3 sentence answers per sub-part; the boundaries text makes the model add disclaimers/scope notes that the grader doesn't reward.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_d13_inference_injection_partial_fix_2026_05_12.md",
     "lines": "16",
     "quote": "| **2 D13-only** (7 docs in user) | **1/6** | **16.7%** | 0.502 | **0.200** | 0.400 |",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_d13_inference_injection_partial_fix_2026_05_12.md",
     "lines": "18",
     "quote": "| 4 hybrid (D13 + curriculum) | 0/6 | 0.0% | **0.125** | 0.000 | **0.000** |",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_richer_rag_per_cell_tradeoff.md",
     "lines": "19",
     "quote": "| apush/mcq | 93.3% | **100.0%** | +6.7pp | ±0.5pp | ✓ REAL LIFT |",
     "verbatim": true
    }
   ],
   "against": "\"**Rule (P0/T1; n=6 single-seed, single-model — promote to T0 after n≥30 replication):**\" (feedback_d13_inference_injection_partial_fix_2026_05_12.md, line 7). The short-answer drop was measured against stored outputs, and that alone moved short answers: \"- apush/saq: -3.60 cont-pp (fresh vs frozen)\" (feedback_baseline_must_be_fresh_gen.md, line 24). Training with both blocks was reported safe: \"**Training-time (v52b+):** D13 + curriculum_context in system are PROVEN safe (v52b build pattern).\" (feedback_d13_inference_injection_partial_fix_2026_05_12.md, line 36).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 0.502, 0.125 and 0/6 match. As a rule it overstates. The stacking result is 6 items from one seed and one model. The short-answer comparison partly reflects the stored-baseline artifact. And the same scope notes helped multiple choice. Recast as an open question. Note too that seven documents alone lowered the average from 0.789 to 0.502 while raising passes from 0 to 1 (lines 15-16)."
  },
  {
   "index": 22,
   "verdict": "keep-with-fix",
   "statement": "Give a writer the objective's official statement, including what it excludes, and check the effect on each item type: it turned 5 of 9 items that had failed every scoring into items that passed every scoring, but on the full set it helped multiple choice and hurt short answers.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_richer_rag_resolves_stable_fails.md",
     "lines": "3",
     "quote": "lifts pass rate from 0/27 (3 runs × 9 items) to 17/27 = 63%",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_richer_rag_resolves_stable_fails.md",
     "lines": "56",
     "quote": "- `assessment_boundaries` (the killer field — explicit \"should NOT include X\" scope guard)",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_richer_rag_per_cell_tradeoff.md",
     "lines": "19",
     "quote": "| apush/mcq | 93.3% | **100.0%** | +6.7pp | ±0.5pp | ✓ REAL LIFT |",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_richer_rag_per_cell_tradeoff.md",
     "lines": "23",
     "quote": "| apush/saq | 77.8% | **68.3%** | **-9.5pp** | ±3.8pp | ✗ REAL REGRESSION |",
     "verbatim": true
    }
   ],
   "against": "The note's own table contradicts its near-miss explanation: \"| 58090 | apush/saq | 0/3 (0.0/0.0/0.0) | 3/3 (1.0/1.0/1.0) | RESOLVED |\" (line 30) while \"| 58794 | apush/saq | 0/3 (0.8/0.8/0.8) | 0/3 (0.8/0.8/0.8) | unchanged |\" (line 35). There was one output per item, \"4. Generated 9 prompts × 1 sample each against v29 with the richer system prompt\" (line 20), and no fresh control without the added context. The gain may partly be matching the judge's own scope text (line 59). The cross-model scan lists \"1068495, 1058194, 1059567, 1059670, 1059661, 1060158\" among items that never passed (project_quill_discovery_cross_model_volatility_2026_05_11.md, line 24); if these are the probe's items 68495 and 60158, its passes did not recur there. For another course the scope fields were model-written: \"| Curriculum dataset | Had LLM-fabricated fields (APEURO assessment_boundaries, common_misconceptions, expanded_LOs all Haiku-generated) |\" (reference_external_ib_v253_at_10.md, line 26).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 0/27 to 17/27 matches. Cut 'because near-miss items usually lack scope precision rather than facts'. Among the resolved items, one scored 0.0 in all three runs and one scored 0.0/0.78/0.0, while two near misses at 0.8 stayed failing (lines 27-35). That goes against the note's own line 43. The judge-version explanation (feedback_mcq_v2.5.6_rubric_tightening.md line 21) is a hypothesis ('likely checking'). For the main course, only 3% of records had model-written scope or misconception fields (feedback_field_level_provenance.md line 29)."
  },
  {
   "index": 23,
   "verdict": "drop",
   "statement": "Check that each generated question asks for the reasoning skill its objective requires, because a task framing borrowed from another item type can silently replace that skill.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_cross_cell_skill_assignment_pattern_transfer_during_chain_sft_2026_06_02.md",
     "lines": "13",
     "quote": "- POST-v92 chain-step: n=500 LEQ verdict showed 76% pass with curriculum_alignment failures concentrated in 2 KCs (KC-1.2.III.C: 12 fails, KC-1.2.II.D: 9 fails — both rubric-require CCOT)",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_cross_cell_skill_assignment_pattern_transfer_during_chain_sft_2026_06_02.md",
     "lines": "14",
     "quote": "- Failure pattern: v92 generates LEQ prompts that DEFAULT TO Comparison framing (\"Evaluate the extent to which X and Y differed\") for KCs requiring CCOT, because the model learned that \"evaluate the extent\" framing from the DBQ block's gradient pressure",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-ap-social-studies-generator-python/memory/MEMORY.md",
     "lines": "22",
     "quote": "2. Added `skill_tested` enum constraint [\"sourcing\",\"causation\",\"comparison\"] in both schemas",
     "verbatim": true
    }
   ],
   "against": "\"- LEQ: Gemini under-credits (95% IB vs 76% Gemini = +19pp gap; opposite direction). Treat Gemini-LEQ verdicts as a lower bound.\" (feedback_gemini_ib_dbq_judge_divergence_97pp_2026_06_02.md, line 25). The repair was later listed among actions taken on a false verdict: \"my Block A LEQ recovery directed at LEQ \"regression\"\" (feedback_n100_gemini_promote_must_have_ib_canonical_confirmation_2026_06_02.md, line 12).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim, but the evidence does not carry the claim. The 21 alignment failures came from a judge that the same notes say under-credits this item type (76% against 95% from the reference judge). The repair was later listed among actions taken on a false verdict. The borrowed-framing mechanism is a hypothesis; its cure was deployed but never measured. The closed skill list in the other generator showed no gain either: 50-60% before and after (ap-social-studies-generator-python MEMORY.md lines 31-32)."
  },
  {
   "index": 24,
   "verdict": "keep",
   "statement": "Read the checker's own code to learn exactly what it grades and parses, and match each item type's output structure (keys, casing, nesting) to it, verified in code before producing at scale.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_per_cell_schema_must_match_fewshot_bank_chain_canon.md",
     "lines": "18",
     "quote": "**v81 SAQ collapsed -73.3pp (90% → 16.7%) after training on my Track B v2 corpus.** Root cause: 385/385 SAQ training rows used UPPERCASE A/B/C with bare-string parts, but the chain canon (fewshot_bank/by_cell/saq.jsonl) uses lowercase a/b/c with nested `{question, sample_response}` per part.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_eval_is_question_generation.md",
     "lines": "32",
     "quote": "Line 88: `parse_json_response()` — single-attempt JSON parse on raw model output. Per the constraint block at lines 13-18, parse failure counts as a fail with no repair.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_eval_is_question_generation.md",
     "lines": "56",
     "quote": "This is the v38 failure mode (262 rows of answer-format anchors → 0/150 parse_ok).",
     "verbatim": true
    }
   ],
   "against": "The project held the opposite rule at the same time: \"Every SFT/DPO row must train the model to **emit the answer**, not to generate questions about content.\" (feedback_answer_format_only.md, line 7). Sometimes the checker's parser was what needed fixing: \"orch shipped a fix: enhanced `_extract_json()` that strips fences + regex-extracts `{...}` blocks as fallback.\" (feedback_gemma4_wraps_json_in_markdown_fences_default_2026_06_02.md, line 13).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 90% to 16.7%, 385 of 385 rows and 0/150 match. The contradiction with the answer-format rule and the case where the parser needed fixing are both already in 'against'. Near 67 (settle in code what code can settle), but this is about matching the checker's input format."
  },
  {
   "index": 25,
   "verdict": "keep",
   "statement": "A check that a passage supports a claim must ask whether the passage itself states it, not whether it is plausible, and 'partly supported' verdicts need their own audit.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_self_rag_label_audit_rebuild_trigger.md",
     "lines": "26",
     "quote": "| **partially** | **60%** | 10 | **<80% → REBUILD** |",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_self_rag_label_audit_rebuild_trigger.md",
     "lines": "41",
     "quote": "The partially class is **bidirectionally noisy** — 2 cases pulled UP to \"fully\" (Quill under-rated), 2 cases pulled DOWN to \"no\" (Quill over-rated).",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_self_rag_label_audit_rebuild_trigger.md",
     "lines": "50",
     "quote": "- Atlas verdict: \"no\" — paragraph mentions debate over treatment, NOT conversion to Christianity. Span injects fact requiring outside knowledge.",
     "verbatim": true
    }
   ],
   "against": "The re-grader was itself lenient on one class: \"The \"no\" class is asymmetrically lenient on Atlas's side (3 pulled \"no\" → \"partially\", 0 the other way), consistent with 3.1-pro slightly more accepting of thematic-but-not-literal entailment.\" (same file, line 43). Only 10 spans were checked per class.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 60% on the middle class, 70% overall and the 2-and-2 split match. The audit is one model re-grading another model's labels on 10 spans per class (lines 18-21). So the 'errors in both directions' are disagreements, not errors against a key. The clearest case (line 50) is plainly unsupported on reading. Near 5 and 9, but about checks that a passage supports a claim."
  },
  {
   "index": 26,
   "verdict": "drop",
   "statement": "Generate an item whose questions share one source in separate steps (the source first, then the questions written on it), and keep extra steps only if they measurably help.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}/memory/session_20260422_grpo_to_pipeline.md",
     "lines": "133",
     "quote": "5. **The multi-step pipeline is the architecture insight.** Gemini achieves 93-99% not because it's a better model, but because it breaks complex tasks (MCQ_SET, DBQ) into 3-7 complementary steps. sft-v4 needs the same scaffolding.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/mcq_set_improvement_log.md",
     "lines": "31",
     "quote": "- **Result: 80% (8/10)** — best so far",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/mcq_set_improvement_log.md",
     "lines": "27",
     "quote": "- Problem: stimulus chained to potentially hallucinated research sources",
     "verbatim": true
    }
   ],
   "against": "\"- This is essentially the legacy pipeline that was always running (due to the bug)\" (mcq_set_improvement_log.md, line 32). The same pipeline on a weaker model: \"| **Overall** | **46.7%** | vs 93-99% with Gemini |\" (session_20260422_grpo_to_pipeline.md, line 92).",
   "general": true,
   "duplicate_of": "61",
   "name_bearing_source": false,
   "reason": "Quotes verbatim, but the claim overstates. The 8/10 two-step pipeline 'is essentially the legacy pipeline that was always running' (line 32), and that type was already at ~75-80% (line 4), so splitting showed no gain. There was no single-step arm, and each approach had only 10 items. Crediting the 93-99% to splitting is an assertion, and the same note undercuts it: the same pipeline on a weaker model scored 46.7% overall and 0/3 on these sets (lines 90, 92). The supported part, not chaining to the writer's unchecked research, is truth 61, whose evidence already cites line 27."
  },
  {
   "index": 27,
   "verdict": "keep-with-fix",
   "statement": "Don't expect example items to fix a writer's facts: adding examples did not raise factual accuracy, while the format specification was essential.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}/memory/sft_v4_prompt_engineering.md",
     "lines": "24",
     "quote": "4. fewshot: 40% pass, 55% — examples don't help",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/sft_v4_prompt_engineering.md",
     "lines": "26",
     "quote": "6. bare (no schema): 5% — model requires format spec",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/sft_v4_prompt_engineering.md",
     "lines": "7",
     "quote": "Exhaustive 9-variant prompt engineering sweep on sft-v4 (Fireworks: accounts/trilogy/deployments/kh9mkdob), APUSH Unit 7, N=20 per variant.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/research_fewshot_format_not_facts.md",
     "lines": "76",
     "quote": "*Rethinking the Role of Demonstrations* — EMNLP 2022 (https://aclanthology.org/2022.emnlp-main.759/)",
     "verbatim": true
    }
   ],
   "against": "One multiple-choice sweep with 20 items per variant (\"**Key variant ranking (MCQ, N=20):**\", sft_v4_prompt_engineering.md line 20); with and without examples differ by one item. The '+3-8pp' lift for multi-question sets in MEMORY.md line 67 is a projection, not a measurement: \"medium on magnitude of mcq_set/saq lift (T3 magnitude — no published measurement on AP-history-shaped tasks)\" (research_fewshot_format_not_facts.md, line 12).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 40% and 55% with examples against 45% and 60% without, and 5% without the format specification, all match (lines 23-26). Two fixes. The original 'against' treated the +3-8 points as a measured lift, but it is an expected one. And the research note does cite the literature with public links (line 76), so 'without DOIs' was wrong. That examples shape structure rests on the literature; the project's own sweep only shows that they did not fix facts."
  },
  {
   "index": 28,
   "verdict": "drop",
   "statement": "Report the quality of the single draft that will actually be delivered, and treat best-of-several scores as a ceiling or a diagnostic, not as the product's quality.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v35_bon_k8_99pct_canonical.md",
     "lines": "25",
     "quote": "1. **This does NOT count toward APUSH 95% goal.** Per `feedback_k1_only_for_goal.md`, K=1 only counts. K=8 is decode-time + grader-as-reward = worst-case Goodhart configuration.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_k1_only_for_goal.md",
     "lines": "52",
     "quote": "- BoN numbers are footnotes only (e.g., \"K=8 ceiling: X% — for context, doesn't count toward 95% goal\")",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_full_cost_accounting_no_zero_marginal_lie.md",
     "lines": "44",
     "quote": "| Throughput | ~1.8 prompts/min — infeasible at classroom scale |",
     "verbatim": true
    }
   ],
   "against": "The project later chose a ranked best-of-several pipeline as its product path: \"product-bar via grounded-ranker + best-of-N + deterministic-compiler is the live path to 99% without raw model winning.\" (project_stand_down_single_owner_2026_06_10.md, line 15).",
   "general": true,
   "duplicate_of": "66",
   "name_bearing_source": false,
   "reason": "Quotes verbatim, but this duplicates 24 (measure from what is delivered) and 66 (confirm judge-picked items with an independent check). The single-draft rule was one goal ruling, and the project later chose best-of-several plus ranking as its product path. Truth 66's evidence already includes the 21/24 independent check on picked drafts. No independent check was run on the 99.33% picks themselves (project_v35_bon_k8_99pct_canonical.md line 26)."
  },
  {
   "index": 29,
   "verdict": "keep-with-fix",
   "statement": "Record where each field came from, not only each record, because one record can mix official curriculum text with model-written fields such as misconceptions and scope notes.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "119",
     "quote": "Curriculum API merge_source is record-level; same record mixes CB-canonical statement with Haiku-generated misconceptions/assessment_boundaries.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_field_level_provenance.md",
     "lines": "21",
     "quote": "The `statement` field carries CB-canonical KC text. The `common_misconceptions` and `assessment_boundaries` fields carry Haiku-4.5-generated text",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_field_level_provenance.md",
     "lines": "29",
     "quote": "APUSH (2,703 records): 43% have any LLM-tagged field.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/reference_external_ib_v253_at_10.md",
     "lines": "26",
     "quote": "| Curriculum dataset | Had LLM-fabricated fields (APEURO assessment_boundaries, common_misconceptions, expanded_LOs all Haiku-generated) |",
     "verbatim": true
    }
   ],
   "against": "For the main course the model-written misconception and scope fields were few: \"**Misconceptions/boundaries/LOs LLM-filled in only 88 records (3%).**\" (feedback_field_level_provenance.md, line 29). No harm from mixed records was measured.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim. The third original quote (training_data_audit_20260423.md line 27) is about telling two generators apart at record level, so it supports 50 rather than field-level provenance. The field-level note replaces it, giving the 43% share and the per-field filter (line 32). This refines 50 (record each asset's source)."
  },
  {
   "index": 30,
   "verdict": "keep-with-fix",
   "statement": "Before adopting a source for a course's curriculum facts, compare candidate sources item by item on content and check their labels against the official framework, because sources can carry shifted labels or sit at different levels of the framework.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_oracle_source_reconciliation.md",
     "lines": "12",
     "quote": "across all 239 InceptBench APEURO entries vs curriculum repo APEURO; 224 matched by content but 218 at different IDs, with systematic off-by-one-period shift confirmed against official CB CED.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_oracle_source_reconciliation.md",
     "lines": "12",
     "quote": "APUSH analysis: 39% of curriculum has no InceptBench match, 99.8% of InceptBench atomic facts have no curriculum match — different hierarchy tiers.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "116",
     "quote": "**APUSH** = MERGE (curriculum repo skeleton + InceptBench atomic facts; 39% / 99.8% non-overlap means single-source halves pedagogy). Wrong source per course = silent training corruption.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-oracle/memory/project_oracle_session_20260501.md",
     "lines": "12",
     "quote": "RECONCILIATION ruling per course (APEURO=curriculum-repo, APWH=InceptBench, APUSH=MERGE)",
     "verbatim": true
    }
   ],
   "against": "The shifted labels did not reach the service used for generation: \"Atlas 30/30 PASS (zero APEURO off-by-period drift in canonical API; InceptBench bug did NOT propagate).\" (MEMORY.md, line 82). The fixes were never shown done: \"1. APEURO ID dedup + switch (Quill + Atlas) — RECONCILIATION remediation #1, no helper has filed evidence of completion.\" and \"3. APUSH merge schema (Quill + Compass) — remediation #3.\" (project_oracle_session_20260501.md, lines 22 and 24). No effect on generated items was measured.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 39% and 99.8%, about 130 missing and 50 duplicates all match. 'Barely overlapped' was loose: 39% of one source had no match, while 99.8% of the other's atomic facts had none, because the two sit at different levels (feedback_oracle_source_reconciliation.md line 12). The original 'against' quote ('md5 diff never run', oracle note line 26) concerns a different file comparison, not the merge, so lines 22 and 24 replace it. Separately, both existing-truth items for 63 taken from project_v39_dataset_corruption_smoking_gun.md (lines 21, 35) are marked not ok. That note calls c_4EvW an opaque hash for a knowledge component that does not exist, but it is the named substandard 'Immigration Gilded Age' on the evaluation's own items (project_v29_failure_analysis_3run.md line 41)."
  },
  {
   "index": 31,
   "verdict": "keep-with-fix",
   "statement": "Before declaring a unit or topic short of material, or building from 'the part of a collection about X', count what the collection actually holds for X after normalising its labels.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_audit_normalization_before_declaring_gap_2026_05_22.md",
     "lines": "9",
     "quote": "Adding an `ERA_LABEL_TO_UNIT` dict moved Unit 7 from gap-status to +361k margin and Unit 8 from gap to +482k margin — without ingesting a single new token.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_verify_subset_exists_before_filter.md",
     "lines": "12",
     "quote": "The implied assumption: fewshot_bank's 3,806 rows contain a U1 slice. **It does not.** Unit distribution audit:",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_verify_subset_exists_before_filter.md",
     "lines": "23",
     "quote": "Had I scripted on the assumption, the consolidator would have silently produced ~468 rows (Track B only) but reported the manifest as if it included fewshot_bank",
     "verbatim": true
    }
   ],
   "against": "none found. Line 9 of the normalization note names the short units as 8 and 9 and then reports the fix for 7 and 8.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; +361k, +482k and the empty unit-1 slice match. Trimmed one quote to drop role words. Line 9 of the normalization note is inconsistent about which units were short, but the statement does not depend on that. Near 63 (check scope labels), but this is about counting coverage."
  },
  {
   "index": 32,
   "verdict": "drop",
   "statement": "Record a finding as shared knowledge only when it transfers to other work, is not obvious, rests on repeat evidence, fits in a paragraph and is not already recorded, and state it as a rule that says what makes it non-obvious rather than as the story of the incident.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_synapse_scarce_useful_only.md",
     "lines": "32",
     "quote": "3. **Reproducible OR statistically backed** — n≥30 evidence, or a documented mechanism with at least one confirming trial.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_three_rule_updates_20260506.md",
     "lines": "21",
     "quote": "**How to apply:** When publishing to Synapse, write \"rule: ...\" not \"we found ...\". If the principle came from a specific incident, the principle stands on its own without the incident.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_synapse_dok3_non_obvious_marker_2026_05_12.md",
     "lines": "48",
     "quote": "Do NOT use generic markers like \"novel finding\" or \"research-grade\". Be specific about the inversion / surprise / hidden constraint.",
     "verbatim": true
    }
   ],
   "against": "\"**Rule:** Cross-project Synapse records share methodology, patterns, anti-patterns, thresholds, and rules-of-thumb. They do NOT share specific pass-rates, regressions, costs, or any number that would embarrass the team.\" (feedback_synapse_no_unfavorable_numbers_2026_05_12.md, line 17).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim, but these are directives with no measured effect. The supporting figure is also misreported: the 119+ entries were queued and never published (\"Do not retro-publish the 119+ orphan queued learnings from the prior URL outage.\", feedback_synapse_scarce_useful_only.md line 83), while the store itself held '67 learnings, 0 insights' (line 26). The companion rule withholds unfavourable numbers to protect reputation, which works against checkable evidence. This is a record-keeping policy, not a finding about teaching, judging or generating."
  },
  {
   "index": 33,
   "verdict": "drop",
   "statement": "Rank recorded findings by strength of evidence rather than recency, count one as measured only with at least 30 items or repeated confirming runs, and link every superseded finding to its replacement.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "4",
     "quote": "> Index sorted by **priority then evidence tier**, NOT by date. Recency is a tiebreaker only.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "13",
     "quote": "4. T0 evidence requires actual measurement on our data (n ≥ 30 OR multiple confirming runs).",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "12",
     "quote": "3. Every `superseded` entry has at least one other entry whose `supersedes:` list contains it.",
     "verbatim": true
    }
   ],
   "against": "A top-tier finding on 297 items was later retracted as noise: \"audit_note: T0 — apples-to-apples on n=297, both models scored on same IB v2.5.3 with same prompts. v35 wins single-shot.\" (project_v35_self_rag_wins_canonical.md, line 12), retracted at MEMORY.md line 38.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim, but this is a governance rule with no measured effect, and its one test in the same index went the wrong way: a finding ranked top-tier on 297 items was later retracted as noise. Keeping retracted findings visible with the reason is bookkeeping for the registry itself. Candidate 10 already carries the lesson from that retraction."
  },
  {
   "index": 34,
   "verdict": "keep-with-fix",
   "statement": "Open question: does forcing a strict output schema on a writer buy structural compliance at the cost of quality in its free-text parts?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "29",
     "quote": "- `json_schema`: **5/5 = 100% structural compliance**",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
     "lines": "30",
     "quote": "- `json_object`: **0/5 = 0% structural compliance**",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
     "lines": "63",
     "quote": "JSON mode loses 25-63pp on reasoning tasks; per-cell decision; default OFF for free-form cells.",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/research_constrained_decoding_per_cell.md",
     "lines": "62",
     "quote": "*Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models*, EMNLP 2024 Industry Track](https://aclanthology.org/2024.emnlp-industry.91/)",
     "verbatim": true
    },
    {
     "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/research_constrained_decoding_per_cell.md",
     "lines": "19",
     "quote": "GSM8K reasoning, same model, same prompts, free-form vs JSON-mode constrained:",
     "verbatim": true
    }
   ],
   "against": "Five items only (\"Diagnostic: 5 DBQ items:\", findings_sftv7_20260424.md line 28). The cited losses are on a math-reasoning benchmark, and the same paper found the opposite on classification: \"Same paper shows JSON mode *helps* on classification (Gemini-1.5-Flash 41.6% → 60.3% on DDXPlus). **Direction depends on task.**\" (research_constrained_decoding_per_cell.md, line 30).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes verbatim; 5/5 against 0/5 and 25-63 points match (research_constrained_decoding_per_cell.md lines 23-25: -27.3, -63.1, -25.8). The research does have a public link (line 62), so 'without a DOI or URL' was wrong. It measured math reasoning, and its direction depended on the task. Fair as an open question."
  }
 ],
 "existing_checked": [
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v39_dataset_corruption_smoking_gun.md",
   "lines": "25",
   "quote": "- A: 64.5% (189) — vs expected 25%",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v39_dataset_corruption_smoking_gun.md",
   "lines": "37",
   "quote": "Defect 2 → degrades `distractor_quality` + `difficulty_alignment` (2/11 dimensions) because the model learns answer-position bias real AP exams don't have.",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v39_dataset_corruption_smoking_gun.md",
   "lines": "56",
   "quote": "3. Enforce uniform answer distribution at row-emit time for MCQ/MCQ_SET (rotate correct-answer position deterministically across A/B/C/D)",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v39_dataset_corruption_smoking_gun.md",
   "lines": "35",
   "quote": "Defect 1 → degrades `curriculum_alignment` + `factual_accuracy` + `educational_accuracy` (3/11 IB dimensions) because the model is being trained to generate questions for AP KCs that don't exist.",
   "ok": false
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_v39_dataset_corruption_smoking_gun.md",
   "lines": "21",
   "quote": "- non-canonical (opaque hashes like `c_4EvW`, `s_saxW`): 803 rows (77.5%)",
   "ok": false
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_stacked_decode_RAG_judge_result.md",
   "lines": "53",
   "quote": "Gemini probably defaulted to <0.85 on anything it couldn't decisively grade. Format mismatch, not Goodhart.",
   "ok": true
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_stacked_decode_RAG_judge_result.md",
   "lines": "73",
   "quote": "- **Future judge runs:** build per-format rubrics for mcq_set + dbq (decompose into sub-questions / sub-rubric-items) before re-running held-out.",
   "ok": true
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_stacked_decode_RAG_judge_result.md",
   "lines": "51",
   "quote": "- My single-prompt JSON rubric (\"factual_accuracy 0-1, overall 0-1\") can't decompose those",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/session_20260422_grpo_to_pipeline.md",
   "lines": "44",
   "quote": "**LESSON:** Always test the raw rollout format, not the production pipeline format. They are different paths.",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_grader_variance_discovered.md",
   "lines": "57",
   "quote": "LLM-as-judge is non-deterministic at any temperature > 0 OR even at temp=0 (small variance from server-side batching, KV-cache timing, random sampling fallback paths). Single-call evaluation is unreliable.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_self_rag_full_build_clean.md",
   "lines": "47",
   "quote": "**IsUse is degenerate** (essentially all maxed). gpt-4o-mini IsUse classifier collapsed to ceiling.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/project_v60_partial_stimfab_insufficient_2026_05_13.md",
   "lines": "53",
   "quote": "Spot-check 1-2 rejected samples per type to verify IB grader actually fails them (open API call), otherwise discard the corruption type.",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_save_everything_always.md",
   "lines": "38",
   "quote": "- v29's 63.64% baseline could be re-scored on 2.5.3 because we kept the gen file — but only because we happened to save it; rule wasn't explicit",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/mission_aim_98_floor_95.md",
   "lines": "72",
   "quote": "Mitigation: R30 factuality battery (FActScore-on-AP-bios) as the parallel held-out scorer. Alarm fires at IB-vs-FActScore drift ≥3pp.",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_mcq_v2.5.6_rubric_tightening.md",
   "lines": "9",
   "quote": "What scored 100% on v2.5.3 now hits 24-30% zero-rate on v2.5.6 — this is the rubric driver of the ~25pp aggregate mcq drop.",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_apush_only_eval.md",
   "lines": "26",
   "quote": "3. Save APUSH and APWH summaries separately. Don't compute \"aggregate\" pass rate — it's misleading.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_result_tagging_discipline.md",
   "lines": "9",
   "quote": "Without per-record provenance, you can't filter, can't bisect quality regressions to a source, can't selectively re-ingest.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_curriculum_enrichment_mandatory_2026_05_11.md",
   "lines": "21",
   "quote": "- Manifest entries: record `curriculum_api_version`, `n_hits_per_row`, `query_used` per row for auditability.",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/findings_sftv7_20260424.md",
   "lines": "58",
   "quote": "Replaced with categorical-only mandate: no names, dates, events in scoring_notes.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/recipe_track_b_openstax_pair_generation.md",
   "lines": "64",
   "quote": "Audit found 0 confirmed fabrications across 1,200 rows; 3 false-positive flags (1 noun-phrase mis-match, 2 missing-from-whitelist real historical works).",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "counter",
   "path": "~/.claude/projects/{home}/memory/sft_v4_prompt_engineering.md",
   "lines": "25",
   "quote": "5. facts alone: 40% pass, 44% — hurts factual_accuracy",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/stage2_postmortem.md",
   "lines": "17",
   "quote": "Stage 2 generates valid, coherent, well-formed AP content — for the WRONG topic. It ignores `topic`, `time_period`, `unit`, and `qtype` constraints and picks its own topic. Examples:",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/stage2_postmortem.md",
   "lines": "22",
   "quote": "The content is factually correct about the wrong thing.",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/continuous_improvement.md",
   "lines": "41",
   "quote": "- No HARD FAIL dimension < 1.0",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/MEMORY.md",
   "lines": "95",
   "quote": "every text field in any new corpus must trace to a primary source; LLMs are tools (search/OCR/reformat) not content authors; drop-don't-patch when sources fail.",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/continuous_improvement.md",
   "lines": "48",
   "quote": "- `answer_validity` — MCQ must have exactly 1 correct answer",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/stage2_postmortem.md",
   "lines": "29",
   "quote": "- Why wrong: average scores were identical (0.833 vs 0.836). If facts were degraded, avg scores would diverge.",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/stage2_postmortem.md",
   "lines": "30",
   "quote": "- Caught by: per-item comparison showing 9 regressions were all correct-content-wrong-topic, not wrong-facts-right-topic.",
   "ok": true
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/project_v50_v56_strategy_with_numbers_2026_05_12.md",
   "lines": "83",
   "quote": "v51 was trained on v50's *ungraded* gens before v50 had a verdict. Result: v51 inherited v50's weaknesses + degraded on saq −8.9pp and mcq −10pp.",
   "ok": true
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/mcq_set_improvement_log.md",
   "lines": "27",
   "quote": "- Problem: stimulus chained to potentially hallucinated research sources",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/stage2_postmortem.md",
   "lines": "37",
   "quote": "- Tested: CC added explicit constraint reinforcement (caps, repetition, \"DO NOT substitute\"). Failures persisted.",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/project_v61_broadfab_falsified_2026_05_13.md",
   "lines": "34",
   "quote": "Real-source training data (like D13 for DBQ) works because it gives the model REAL examples to imitate, not synthetic anti-examples to avoid.",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/team_learnings_20260422.md",
   "lines": "69",
   "quote": "- 0.01 weight on bad items helped eliminate questions that reference missing images",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/team_learnings_20260422.md",
   "lines": "60",
   "quote": "- Don't train inline SVGs — generate image configs with known interfaces instead",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_bon_k8_huge_lift.md",
   "lines": "44",
   "quote": "DBQ is structurally different: 7 primary documents per stimulus + 6-paragraph essay + multi-document analysis. Single-shot v29 was at 27% DBQ; even K=8 BoN only gets to 67%.",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_quill_discovery_cross_model_volatility_2026_05_11.md",
   "lines": "30",
   "quote": "for the 93% volatile items, decode-time sampling depth matters; for the 7% hard items, no depth helps.",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/mcq_set_improvement_log.md",
   "lines": "57",
   "quote": "4. **Multiple retry attempts** — masks quality issues instead of fixing them",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_bon_k4_huge_lift.md",
   "lines": "46",
   "quote": "**21/24 (88%) agreed.** Mean IB BoN-pick = 0.949, mean Claude judge = 0.889.",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_full_cost_accounting_no_zero_marginal_lie.md",
   "lines": "45",
   "quote": "held-out judge says 49.2% pass rate vs IB's 92.3% on same RAG run. **43.1pp gap quantifies the contamination.**",
   "ok": false
  },
  {
   "truth": 66,
   "effect": "counter",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/project_stacked_decode_RAG_judge_result.md",
   "lines": "48",
   "quote": "This is NOT actual quality failure across all 240 mcq_set + dbq outputs — that's implausibly bad. It's the **judge rubric being too generic** for complex multi-part outputs:",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/research_best_of_n_decode.md",
   "lines": "24",
   "quote": "- If held-out-judge lift << IB-only lift → we're reward-hacking; back off K",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/project_v50_v56_strategy_with_numbers_2026_05_12.md",
   "lines": "80",
   "quote": "Test whether curriculum_context (v52b primary) is necessary, or whether D13 alone (v52 control) suffices. If v52 ≥ v52b → curriculum is redundant. If v52b > v52 → curriculum is doing real work.",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/recipe_track_a_b_kc_pack_substitution.md",
   "lines": "32",
   "quote": "3. **Keep the Gemini-generated `prompt`** (analytical DBQ stem) — Gemini is good at writing those. **Replace only the `documents`** — that's where the synthesis-vs-real-source distinction lives.",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining/memory/feedback_misconceptions_user_prompt_injection_hurts_2026_05_12.md",
   "lines": "29",
   "quote": "- **For grader-side:** misconceptions field belongs in IB rubric (used to verify distractor variety) — already where the v2.5.6 grader uses them.",
   "ok": true
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/.claude/projects/{home}/memory/mcq_set_improvement_log.md",
   "lines": "11",
   "quote": "**Impact**: The Research→Compile pipeline NEVER WORKED for either MCQ or MCQ_SET. Both silently fell back to legacy generation paths every time. The research step was designed to gather verified primary sources and plausible alternatives, but it always crashed before it could run.",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/.claude/projects/{home}-Library-Mobile-Documents-com-apple-CloudDocs-work-aptraining-helpers-data/memory/feedback_eval_contamination_check_all_eval_files.md",
   "lines": "20",
   "quote": "Had I trained on those rows, v54 would have learned its eval set verbatim → fake pass rate, contamination, useless iteration. Caught before training; saved the cycle.",
   "ok": true
  }
 ]
}
```
