# verify:gap:ap-lab-runs-and-analyses

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "ap-lab-runs-and-analyses",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "statement": "A failure to deliver or to grade an item is not a quality verdict: count it on its own and keep it out of the pass rate's denominator.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/analyzer/reports/run_324d5e51_what_is_really_going_on.md",
     "lines": "4",
     "quote": "**TL;DR:** The headline 14.6 % \"pass rate\" is **meaningless**. The actual model is performing at **70.2 %** on the items that survived two stacked infrastructure failures.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/run_73348c1a_orchestrator_contract.md",
     "lines": "98",
     "quote": "- Schema failures must be counted separately and excluded from quality pass-rate denominators.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/analyzer/reports/production_surface_40d.md",
     "lines": "21",
     "quote": "- **Proof it's not code/model:** the same commit (`bb577e2`) produced a 0.0% run and an 84.3% run **26 minutes apart**.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md",
     "lines": "211",
     "quote": "- My initial analyzer conflated skips with failures.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/reports/run_4c9da828_live_export_analysis.md",
     "lines": "7",
     "quote": "Pass rate on evaluated rows only: 861/1020 = 84.4%",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/reports/run_4c9da828_overview.md",
     "lines": "36",
     "quote": "**Overall: 861/1080 (79.7%)**",
     "verbatim": true
    }
   ],
   "against": "The lab sometimes counted the other way ('- MCQ_SET still needs at least `+10` counting score errors as failures.', NOTES.md line 874); leaving failures out is only safe with the completion rate reported beside the pass rate ('Report four metrics separately:', run_73348c1a_orchestrator_contract.md line 139).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "All three original quotes are verbatim at the cited lines. 14.6%, 70.2%, n=225 and 0.0% vs 84.3% match, and the 26 minutes checks against runs_to_commits_40d.md lines 31-32. The statement is unchanged; I added evidence. One run (4c9da828) reads 79.7% over all 1,080 rows and 84.4% over the 1,020 graded ones. The synapse check-in (line 34) then quoted the 79.7% against a fully graded 85.7% run as the effect of switching the kit on, which is exactly the harm this truth prevents. It is related to truth 9 but distinct: it covers items never delivered or never graded, not an unsure judge."
  },
  {
   "index": 1,
   "verdict": "keep-with-fix",
   "statement": "When every item gets the same score (all zeros or one floor value), check the measuring before the content: a misread field, a wrong input shape or a failed lookup.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/per_unit_bench_corrected_20260527T1009Z.md",
     "lines": "6",
     "quote": "Fix: score now read from ev['overall']['score'] (was ev['score']=None)",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/per_unit_bench_20260527T0916Z.md",
     "lines": "12",
     "quote": "| 1 | 10 | 0 | **0.0%** | 0 | 0 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_conscience/2026-05-28T0030Z_proactive_log_self_catch_research_first.md",
     "lines": "11",
     "quote": "**Within ~6 minutes**, I recognized this signature as wrong-schema-not-content-fail (the 0.55 floor + 0/30 = grader rejecting \"not a DBQ\" not grading badness of source).",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/.agent/reports/e2e_v97_live_20260607T100840Z.md",
     "lines": "6",
     "quote": "Note: corrected: verdict = overall.score (prior summary read nonexistent overall_pass).",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/analyzer/reports/production_surface_40d.md",
     "lines": "20",
     "quote": "A **subject-taxonomy rename (`apush` → `American History`) broke the evaluator out from under the runs**, zeroing every score.",
     "verbatim": true
    }
   ],
   "against": "A uniform zero can also be a real break on the generating side: 'A two-cell code path broke; ~45% aggregate = 3 cells working + 2 cells bugged to zero.' (production_surface_40d.md line 24). That is still a pipeline fault, not content quality.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; 0.55, 0/30 and the corrected 60.0% for unit 1 match. The statement is unchanged. I added the uncorrected per-unit report (0916Z, the same 90-request workload), which shows 0.0% for every unit. I also added the subject-rename run that zeroed every score. The found_by relies on both, but no quote carried them. This is new; no existing truth covers uniform-score diagnostics."
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "statement": "Check what the judge takes each label to mean: a unit number it read as a school grade quietly cut item scores by 10-40 points and looked like a content regression.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/analyzer/reports/run_f54d5849_what_is_going_wrong.md",
     "lines": "144",
     "quote": "The second one is quieter and therefore more dangerous: it lowers numbers by 10–40 pp on individual items in a way that looks like a model regression.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/analyzer/reports/run_f54d5849_what_is_going_wrong.md",
     "lines": "142",
     "quote": "`grade: \"1\"` interpreted as *1st grade* instead of *Unit 1*",
     "verbatim": true
    }
   ],
   "against": "Line 135's original analysis blamed the 43-point MCQ fall on a grader-side change. The file's own full-run update calls the bug pre-existing and steady ('81 fingerprints across 1 079 evals at consistent rate', line 19), and it touched only 27 of 193 MCQ items (line 30). So most of the fall from 69% to 19% had another cause.",
   "general": true,
   "duplicate_of": "63",
   "name_bearing_source": false,
   "reason": "All three original quotes are verbatim at 135, 144 and 27. The lead claim, though (treat a sudden drop as a measurement fault), is not borne out by its own source: even if all 27 affected MCQ items had passed, MCQ would sit near 33%, not 69%. The diagnosis-file quote (from_analyzer line 27) is a warning, not a measurement. What survives is the label-meaning lesson, which is truth 63; that truth already carries this case through existing evidence (line 19 and the orchestrator contract's grade-echo rule). Line 144 adds how large and how quiet the effect was, so I kept it only as added evidence for 63. The original against overstated one point: the retired detector (deploy packet line 32) was a regex matching the request echo, not this grader behaviour."
  },
  {
   "index": 3,
   "verdict": "keep-with-fix",
   "statement": "Judge a run only once it has finished; an early snapshot can land on a clean window and overstate the pass rate.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/analyzer/reports/run_f54d5849_what_is_going_wrong.md",
     "lines": "13",
     "quote": "**Real pass rate 37.0 % (n = 897, full run).** F1 was a lucky early-window slice; later items pass-rated lower.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/analyzer/reports/run_f54d5849_what_is_going_wrong.md",
     "lines": "61",
     "quote": "A measurement-integrity report got partially fooled by its own measurement window.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/analyzer/reports/run_324d5e51_what_is_really_going_on.md",
     "lines": "54",
     "quote": "The 70.2 % on n=225 is real for *the items that survived*, but the survival itself is not random — it's truncated at the queue's natural drain point.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/handoff_from_calibration/README.md",
     "lines": "66",
     "quote": "- The lab marks a packet `confidence: low` if the analysis was on a partial export (eval_ratio < 60%) — main-a should wait for a fuller draw.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. 48.9% (n=266) vs 37.0% (n=897) is the correction table on line 13, and the clean 09:35-10:35 buckets are lines 40-41. The statement is unchanged. I added the handoff README's adopted rule that an analysis of a partial export gets low confidence. This is new."
  },
  {
   "index": 4,
   "verdict": "keep",
   "statement": "Don't adopt a change, or a rule for one item type, on a single small run; repeat it on independent draws first, because single-draw winners flipped and small-sample gains halved or vanished.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md",
     "lines": "75",
     "quote": "- Single-draw conclusions FLIP between draws (e.g., SAQ best-profile changed from `exam_precision` (single-draw) to `tight_alignment` (3-draw mean)).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_analyzer/2026-05-29T0644Z_dream_sequence_sync_06Z.md",
     "lines": "21",
     "quote": "single-seed n=50 Path β ablation showed +10pp lifts (cell-conditional); multi-seed n=90 revealed those were noise.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_4way_verdict_20260526.md",
     "lines": "79",
     "quote": "Per-cell, the 2.5 \"DBQ 3/3 vs 0/3\" was small-N noise — both DBQ cells normalized to 2/3 on 3.5.",
     "verbatim": true
    }
   ],
   "against": "The cross-draw packet that enforced this shipped its decisions on two draws, short of the three-draw rule ('# CROSS-DRAW measurement — Unit 1 n=150 BoN (2 draws)', 20260520T234841Z_XDRAW_MEASUREMENT_unit1_n150.md line 1).",
   "general": true,
   "duplicate_of": "15",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim and the numbers match. Note that the 3/3 vs 0/3 rerun used a different generator version (2.5 vs 3.5 Flash). This is truth 15 (never adapt on fewer than three observations) applied to design changes. The lab's own three-seed rule (guide line 76) is already attached to 15 as existing evidence. I kept this as added evidence: single-draw winners flipped and single-seed lifts vanished on a multi-seed rerun."
  },
  {
   "index": 5,
   "verdict": "keep",
   "statement": "Size the sample to the claim: a high pass gate needs enough items per type to tell it from a lower rate, and differences inside the noise floor aren't worth acting on.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/analyzer/reports/run_324d5e51_what_is_really_going_on.md",
     "lines": "55",
     "quote": "n=45 per cell is small; 95 % requires <2/45 cell misses, and MCQ_SET alone has 25 misses here.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_14way_verdict_20260526.md",
     "lines": "66",
     "quote": "5. **n=15 noise floor is roughly ±1 row per cell.** Per-cell numbers like \"2/3 vs 0/3\" should be interpreted as directional only.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/handoff_from_calibration/README.md",
     "lines": "67",
     "quote": "- Any packet whose `expected_lift_pp` < 1.0 is below noise floor for n=150 measurements — don't bother.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim and support the statement. The found_by overstates line 55: it says 'n=45 per cell is small', not 'cannot show 95%'. The source's own arithmetic is also loose (95% of 45 allows two misses, not '<2'), but MCQ_SET's 25 misses settle the point either way. This is distinct from truth 34 and from candidate 4: it concerns sample size and noise floor, not replication."
  },
  {
   "index": 6,
   "verdict": "keep",
   "statement": "Keep an item judged good only after it passes on at least two independent judgings; items banked on one high score failed when re-scored unchanged.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md",
     "lines": "320",
     "quote": "- Single-score banking overfits IB noise. Several candidates that previously scored `1.0` failed when rescored unchanged.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md",
     "lines": "578",
     "quote": "- Need a stability gate: a MCQ_SET candidate should pass at least two independent IB scores or pass after serial retry before it is eligible for assembly.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md",
     "lines": "553",
     "quote": "- Prior-score assembly without fresh validation is unreliable. `mixed_step_union_v2` expected `145/150` but fresh-aborted at `47/61`.",
     "verbatim": true
    }
   ],
   "against": "An over-strict version removed good items: '- Clean-pass purity hurt selection. It removed useful candidates with some historical fail evidence but strong fresh behavior.' (NOTES.md line 767).",
   "general": true,
   "duplicate_of": "66",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim, and these figures check: 138/150 predicted vs 126/150 (lines 310, 314), 145/150 vs 47/61, a row falling from 1.0 to 0.0 (line 322), 77.03% (line 563), 84.76% (line 613) and 85.61% (line 707). This is the same lesson as truth 66 (confirm judge-picked items with a check that took no part in picking), and WINS line 49 is already attached to 66. I kept it for the added evidence: a second prior-score assembly that collapsed, and the stability-gate trajectory."
  },
  {
   "index": 7,
   "verdict": "keep-with-fix",
   "statement": "Check a model picker against the final judge and against simply taking the first valid draft before using it, and drop it if it isn't better; one model judge choosing among six drafts did no better than a single draft.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/BEAD_EVIDENCE_INDEX.md",
     "lines": "57",
     "quote": "- Finding: **K=6 + Gemini-judge gives 22/25 = 88%, WORSE than K=1 (23/25)**. MCQ_SET dropped 4/5 → 2/5. Gemini-judge is not a good MCQ_SET discriminator. **Production: K=1 only.**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pil_monitor/inbox/2026-05-19T1456Z_den_best_of_n_protocol.md",
     "lines": "96",
     "quote": "Do not trust Gemini/LLM judge until calibrated against repeated IB outcomes.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pil_monitor/inbox/2026-05-19T1456Z_den_best_of_n_protocol.md",
     "lines": "192",
     "quote": "If judge-selected winners are not reliably better than deterministic filters, do not use Gemini judge. Use the deterministic filter plus stable candidate bank instead.",
     "verbatim": true
    }
   ],
   "against": "The same kind of judge lifted another type from 22/30 to 28/30 (NOTES.md lines 945-947), but that compared it with a stored bank, not with a single draft. At n=25, 22 vs 23 is a one-item gap.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim, and 22/25 vs 23/25 and MCQ_SET 4/5 vs 2/5 match. The original's first clause (a picker helps only where it agrees with the judge) is a truism, so the statement now leads with the action. I replaced the SELECTOR_CALIBRATION evidence: every mode there, including the oracle, tied at 13/15, and 12 of its 15 rows had a single candidate (K_sweep line 36). That shows no headroom, not a failing picker. The 'den' in the path is a lab workspace name (den-of-ideation), not a person."
  },
  {
   "index": 8,
   "verdict": "keep",
   "statement": "Remove drafts that fail code checks before a model ranks the rest; a model ranker let through answer leaks, cut-off options, reversed facts and invented sources.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
     "lines": "75",
     "quote": "- Gemini ranking must happen after deterministic local validators remove obvious bad candidates.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
     "lines": "76",
     "quote": "- Do not trust Gemini to catch MCQ_SET answer leaks, truncated options, wrong crop direction, or DBQ source hallucination. Evidence from the rejected branch shows it missed these.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/unit1_workflow_v2_branch_result_20260525T093757Z.md",
     "lines": "81",
     "quote": "- Gemini did not reliably reject these candidates.",
     "verbatim": true
    }
   ],
   "against": "Code checks catch only the obvious: 'The visible deterministic rules catch the obvious defects but cannot reliably identify the evaluator's latent concerns without damaging passed controls.' (a0f_validator_probe_20260519.md line 42). The rejected branch also already ran local validators before its model ranker (branch report lines 38, 82).",
   "general": true,
   "duplicate_of": "67",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; K=4 is at branch-report line 34 and the final 3/5 at line 65. This is truth 67 (settle in code what code can settle) applied to selection; line 76 is already attached to truth 32. I kept it for the added evidence that a model ranker let leaks, truncations and a factual inversion through. Running code checks first was necessary but not sufficient."
  },
  {
   "index": 9,
   "verdict": "keep",
   "statement": "When a model chooses among drafts, have it return only which one and serve that draft unchanged from code; a model asked to fit or reshape drafts rewrote them, even when told not to.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md",
     "lines": "52",
     "quote": "| K=3 + Gemini Flash 3.5 \"reshape\" | -23pp vs PEAK | Gemini regenerated content from scratch (weaker domain knowledge) |",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md",
     "lines": "54",
     "quote": "| K=3 + Gemini \"structure-only\" | Still regenerating | Schema constraint + token cap overrode \"verbatim\" hard rules |",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md",
     "lines": "56",
     "quote": "| Current (picker-only, v0.4.0) | TBD — needs IB run | Gemini emits only `{best_index: N}`, Python serves verbatim |",
     "verbatim": true
    }
   ],
   "against": "The picker-only fix went live before its quality was measured (its row reads 'TBD — needs IB run', synapse check-in line 56).",
   "general": true,
   "duplicate_of": "29",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim, and the live design is spelled out at lines 101-106. This is truth 29 (every choice is a bounded judgment) applied to picking among drafts. I kept it for the added evidence that a model asked to fit or copy drafts rewrote them, even under explicit verbatim rules. The fix itself was never measured."
  },
  {
   "index": 10,
   "verdict": "keep",
   "statement": "Before crediting or blaming a change to the writer's instructions, confirm from the output that it reached the writer for every item type; hidden repair routes and template bypasses ignored it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_live_verdict_20260526.md",
     "lines": "25",
     "quote": "The v80bchain balanced15 result (E 14/15 > A 12/15) was a false signal: v80bchain selects deterministic repair routes (`dbq_source_repaired`, `mcq_set_repaired`) before the duck directives reach the model.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/BEAD_EVIDENCE_INDEX.md",
     "lines": "61",
     "quote": "**Duck directives don't reach the model for those cells. Code-port required (pil-6bp.10).**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "2092",
     "quote": "Initial `model_required` env was insufficient because Unit 1 had a hardcoded scored-template bypass before `call_fireworks`.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. E 14/15 > A 12/15 on the repair-route writer reversed to A 10/15 > E 8/15 on the clean path (live verdict lines 16-17). This is new: truth 24 is about measuring from the delivered file, not tracing whether a change reached the writer."
  },
  {
   "index": 11,
   "verdict": "keep",
   "statement": "Record which path produced each item and report fresh output apart from fallbacks and previously approved stock; a pass rate that includes served stock or retries is a different measure from first-attempt quality.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_analyzer/2026-05-30T0640Z_dream_sequence_2_sync.md",
     "lines": "20",
     "quote": "Layer distribution (final): 71.2% L3 fresh ML + 28.8% L5 cached fallback + **0% exc** (was 9% pre-fix).",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/validated_library_20260525.md",
     "lines": "55",
     "quote": "- 46/50 strict fresh LLM passes = 92.0%.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/conscience/audit_log/2026-05-29T0908Z_CHECKIN_to_main_a.md",
     "lines": "83",
     "quote": "The argument is mathematically correct (K=5 retry on a 95% per-cell base = 99.97%), but it shifts the gate from \"model passes 95% standalone\" to \"stack passes 99% with model as one component.\"",
     "verbatim": true
    }
   ],
   "against": "The serving side treated fallback as legitimate for delivery: 'L5 fallback IS the production-correct path for catastrophic cells (degraded mode returning known-good cached items).' (to_analyzer/2026-05-29T1840Z_dream_sequence_sync.md line 32). That is acceptable for delivery, not as a measure of new content.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; 71.2%/28.8%, 46/50 = 92.0% and 4/50 timeout fallbacks (line 56) match. The found_by overstates the audit, which calls the shift 'not a gate-criterion change' and records 'Currently no drift' (lines 83, 87). Its 99.97% is also the source's own arithmetic (five tries at 95% give about 99.99997%). The quote still shows that a stacked pass rate is a different measure. This is related to truth 50 and to candidate 13; the new part is reporting fresh output separately."
  },
  {
   "index": 12,
   "verdict": "keep-with-fix",
   "statement": "When no draft passes, fail visibly or serve a vetted item, never a filler: padding gaps with placeholder text produced fake, repeated sources that the judge failed.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "247",
     "quote": "- The generic DBQ fallback padded missing source documents with curriculum facts using `Retrieved APUSH Unit {unit} source N`, which produced fake repetitive documents.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "1851",
     "quote": "- The same placeholder pattern existed in the generic MCQ_SET fallback: 179 generation rows contained `Retrieved APUSH`.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "1845",
     "quote": "- MCQ_SET: 12/193 = 6.22%.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "255",
     "quote": "Generic DBQ fallback no longer pads with `Retrieved APUSH` curriculum facts; it raises a DBQ source-quality error rather than emitting fake documents.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
     "lines": "62",
     "quote": "- If no LLM candidate passes gates, fail closed rather than return a canned final.",
     "verbatim": true
    }
   ],
   "against": "Blocking with no fallback turned quality failures into no output: 'Lesson: do not hard-reject all deterministic MCQ_SET quality failures unless K is expanded or a fallback candidate policy exists.' (24H_CARETAKER_STATE_20260521.md line 29).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; 179 placeholder rows and 12/193 (line 1845) check. I reworded 'return nothing': the repair that worked raised an error instead of emitting fake documents, and it added a vetted-source route (lines 255-257). The against shows that blocking everything left 0/3 rows served. I could not find the found_by's 'least-bad fallback leaked a wrong-period item' in the sources."
  },
  {
   "index": 13,
   "verdict": "keep",
   "statement": "Label every result with how it was produced (full official run, sampled smoke check, local re-score, mixed draws) and never present a sample or a re-score as the official number.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md",
     "lines": "161",
     "quote": "The lab refuses to conflate evidence classes. Every artifact is labeled:",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md",
     "lines": "167",
     "quote": "- `LIVE_FULL_IB_EXPORT_ANALYSIS` is NOT `LIVE_FULL_IB`; cross-draw `LOCAL_MIX` is NOT board-quality",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/request_trace/2026-05-21T075822Z_2926c4107df0.md",
     "lines": "9",
     "quote": "The trajectory is to operationalize that taxonomy and implement the agreed gates/backlog so future runs do not confuse exploratory local evidence with official live benchmark evidence.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; this is an adopted rule. The found_by's 'report scripts were patched to stamp the class' isn't shown in these lines, which say only that every artifact is labelled. It overlaps candidate 11 (path per item), but this one is about the evidence class per result."
  },
  {
   "index": 14,
   "verdict": "keep",
   "statement": "Measure one fixed version per run; a run that spans several deployments, or starts within minutes of a change, is not evidence for any of them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "241",
     "quote": "- The export is invalid as evidence for the fixed endpoint because it continued through multiple deployments and includes old placeholder generations plus the intermediate DBQ source-gate 502s.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/runs_to_commits_40d.md",
     "lines": "63",
     "quote": "- Render auto-deploys on push; typical deploy-live latency 1-3 min. Runs that fire within ~2 min of a commit push may be reading the prior version.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "2115",
     "quote": "- Important methodology note: deterministic same-build slice `300-349` remains valid only for deterministic/template mode. It cannot be counted as LLM-required proof.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. Line 2115 is about mode (template vs model-required) rather than version, but it applies the same one-fixed-configuration rule. The found_by's 'restarted' is not shown in the source. This is new."
  },
  {
   "index": 15,
   "verdict": "keep",
   "statement": "Draw test items from across the whole item set; a gate built from the first item of each type tested one objective per type and proved nothing about the rest.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "1005",
     "quote": "The completion audit caught an important scope error: the prior 135/135 gate used the replay harness's default `first_per_type` selector. That proves each unit's first benchmark standard per type, not the full benchmark files and not standard diversity across each file.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/goal_runs/RUNNING_SUMMARY.md",
     "lines": "17",
     "quote": "- `official_n30_balanced_20260514T225509Z`: 20/30 = 66.67%; expansion exposed the second APUSH Unit 3 independence-movement cluster.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/goal_runs/official_n30_balanced_after_7e027d7_20260515T011350Z/RESULTS.md",
     "lines": "33",
     "quote": "- Patched the smoke harness selector so `--per-type 6` actually produces 30 rows, balanced 2 easy / 2 medium / 2 hard per type.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; 135/135, 15/15 (goal runs line 16) and 20/30 check. Related to truth 48, but this one is about coverage of the test set."
  },
  {
   "index": 16,
   "verdict": "keep",
   "statement": "Check a fix on the items it targeted, then on their neighbours and on a fresh balanced set from the same build; targeted wins repeatedly came with broad regressions.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
     "lines": "40",
     "quote": "| `0.1.300` | exact MCQ_SET blockers `2/2`, balanced15 effective `8/15 = 53.33%` | Targeted green, broad regression |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "2039",
     "quote": "- Process note: targeted failed-row retests were not sufficient here. The widened family regression gate caught a live breakage in an already-green neighboring row, so future patches should include an affected-family or affected-slice regression gate before claiming a fix is safe.",
     "verbatim": true
    },
    {
     "path": "~/.openclaw/workspace-incept/memory/ap-benchmark-context.md",
     "lines": "12",
     "quote": "| benchmark.retest | `python -m benchmark.retest --unit N --concurrency 30` | Retest failures + control, regression check |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. 2/2 and 8/8 targeted vs 8/15, 12/15 and 35/50 broad (ultimate lines 32, 37, 40) and the neighbour falling to 0.65 (line 2033) all check. The ap-benchmark-context line is a tool description: weak but consistent. This is new; truths 60 and 70 do not cover regression scope."
  },
  {
   "index": 17,
   "verdict": "keep",
   "statement": "Compare versions on the same items and count which items each one passes; equal totals hid versions that solved different items.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_14way_verdict_20260526.md",
     "lines": "38",
     "quote": "G and C both hit 12/15. Neither strictly dominates: **G_only=2 (MCQ rows), C_only=2 (MCQ_SET + DBQ rows).** They solve different rows.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_14way_verdict_20260526.md",
     "lines": "64",
     "quote": "4. **Strict dominance is rare.** Only C strictly dominates I (1-0). Every other pair has crossings — recipes trade row classes for row classes.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/combo_tournament_protocol_20260525.md",
     "lines": "15",
     "quote": "5. Promote only after same-row and fresh-row evidence.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "60",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim, and the 12/15 tie with G_only=2 and C_only=2 checks. This is the same lesson as the second half of truth 60 (an unchanged average can hide a new failure), applied to comparing versions. I kept it for the added evidence from the 14-recipe same-row matrix."
  },
  {
   "index": 18,
   "verdict": "keep",
   "statement": "Changes that each helped don't simply add up: test the combination itself and remove one change at a time, keeping only those whose removal hurts.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_search_20260526.md",
     "lines": "19",
     "quote": "It produced `candidate_top_n20_repair_recorded`, which lost the random100 gate **73/100 vs incumbent 76/100** at avg overall `0.8904` vs `0.9094`, while still depending on `dbq_source_repaired` (18/20) and `mcq_set_repaired` (19/20) routes — i.e., not strict-fresh at all.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/handovers/20260526T064354Z_TYPED_DUCK_COMBO_HANDOVER.md",
     "lines": "124",
     "quote": "These do not add cleanly. The first is the primary DBQ policy. The second is fallback style only when real packs are unavailable. Treating them as simultaneous positive ingredients is wrong.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/combo_tournament_protocol_20260525.md",
     "lines": "129",
     "quote": "3. If performance does not drop, remove that duck permanently.",
     "verbatim": true
    }
   ],
   "against": "The losing bundle also ran through repair routes that bypassed its instructions (typed_recipe_search_20260526.md line 19), so not all of its loss is due to non-additivity.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; 73/100 vs 76/100 at 0.8904 vs 0.9094 checks. This is new: non-additivity and drop-one ablation go beyond truth 70."
  },
  {
   "index": 19,
   "verdict": "keep-with-fix",
   "statement": "An added instruction can help or hurt and small runs mispredict which, so add instructions one at a time and keep each only if it measurably helps.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_14way_verdict_20260526.md",
     "lines": "62",
     "quote": "3. **Grounding ducks (the new inventory adds) hurt overall.** Despite static_pass and despite intuitive appeal, M/N/O/P all underperform their non-grounded parents. Hypothesis: prompt-attention dilution. Verified by P (lean+grounding) ≤ I (lean), M ≤ C, N ≤ G.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/sweep_n25_final_verdict_20260526.md",
     "lines": "49",
     "quote": "1. **`ib_rubric_criterion_alignment` is the breakthrough duck.** Adding it to G yields the unique top recipe at 23/25 with the highest avg score (0.978) AND MCQ_SET 4/5. Predicted at -5 from n=15, actual at +3.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/sweep_n25_final_verdict_20260526.md",
     "lines": "53",
     "quote": "3. **Surprise: dropping `serve_time_single_ib_grade_contract` from G lifts MCQ_SET 1/5 → 3/5.** That directive may be confusing Gemini's MCQ_SET focus. Worth investigating word-level rephrase.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/sweep_n25_final_verdict_20260526.md",
     "lines": "38",
     "quote": "| 2 | G drop_serve_time_single_ib_grade_contract | 22 | 22/25 | 0.942 | 5/5 | 5/5 | 4/5 | **3/5** | 5/5 |",
     "verbatim": true
    }
   ],
   "against": "Per-type counts are 3-5 items from one seed ('n=15 noise floor is roughly ±1 row per cell', 14-way line 66). The directive set as a whole was worth +8 passes ('5. **The duck system is worth +8 passes = +32pp** (F baseline 15/25 → G+ib_rubric 23/25).', sweep line 57), so additions do not generally hurt.",
   "general": true,
   "duplicate_of": "70",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. The original's general claim that extra directives cost passes overstates the evidence. Two of the three grounding comparisons at n=15 differ by one item, inside the source's own noise floor. A directive predicted at -5 gave +3 at n=25. The directive drop that lifted MCQ_SET from 1/5 to 3/5 also cost MCQ (5/5 to 4/5, sweep line 38). What holds is 'measure each addition', which is truth 70; kept as added evidence. The found_by's 'four fewer directives' repeats the source, but its own table shows 19 vs 24 (five fewer)."
  },
  {
   "index": 20,
   "verdict": "keep",
   "statement": "The right option must not be findable by matching words or close synonyms from the stem, the source or its labels; when it is, change what the question asks rather than swapping in synonyms.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "109",
     "quote": "- `mcqset_repair_offline_v2`: changed Q2 wording away from \"supremacy\"; score 0.78 because \"taking precedence\" was still treated as a synonym leak for \"supreme.\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "110",
     "quote": "- `mcqset_repair_offline_v3`: changed Q2 to ask why the principle mattered historically under the Articles rather than asking students to name/paraphrase the principle. Local IB scored 1.0.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md",
     "lines": "56",
     "quote": "Penalize keyed answers sharing words with labels; otherwise IB sees decorative/source-cued items.",
     "verbatim": true
    }
   ],
   "against": "The rubric-derived writer prompt pushed the other way: '- The stem must reference the stimulus explicitly (\"According to the source...\", \"The passage above suggests...\").' (system_prompt_mcq.md line 91). A warning to the writer alone did not help either: '- Answer-hiding phrasing alone did not improve MCQ_SET.' (NOTES.md line 807).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; 0.78 and 1.0 check. The found_by's 31 flagged items are in official_exports/local_eval/local_eval_report.md line 39 ('31: mcq answer copies stem terms'), a heuristic count, not a judge result. The ultimate report's validator list states the same rule ('no correct answer copied or synonym-mapped from stimulus', line 130). Related to truth 3 but more specific: it names the lexical leak and the remedy (change what is asked)."
  },
  {
   "index": 21,
   "verdict": "keep-with-fix",
   "statement": "When an item tests course knowledge, make it need taught knowledge the given text doesn't state, never knowledge beyond what was taught, and let difficulty come from that knowledge rather than from reading load.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
     "lines": "134",
     "quote": "- difficulty must be earned by outside APUSH context, not reading comprehension.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md",
     "lines": "117",
     "quote": "- MCQ misses are mostly educational-accuracy failures: answer can be found by reading, answer leaks, or weak APUSH knowledge demand.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_leq.md",
     "lines": "43",
     "quote": "- Students can earn full marks using ONLY the curriculum (no obscure outside knowledge required).",
     "verbatim": true
    }
   ],
   "against": "The same prompts let the easiest level match the taught statement almost word for word ('- Easy: direct recall of one curriculum fact; correct answer matches statement nearly verbatim.', system_prompt_mcq.md line 96). In a reading lesson, the text itself is what is tested (truth 5).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. As written, the statement would contradict reading assessment, where a question should be answerable from the text, so I scoped it to items that test course knowledge. There, it is supported (also kit MCQ line 110 on stimulus-paraphrase answers). The 'never beyond what was taught' half is an adopted kit rule, untested on its own."
  },
  {
   "index": 22,
   "verdict": "keep-with-fix",
   "statement": "Build wrong options from the same theme, period and category as the right one and of similar length, so the key isn't the only option that touches the topic, while keeping each one clearly wrong.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/B0045_STAGED_MCQSET_INTERIM_20260519.md",
     "lines": "55",
     "quote": "Gender-role MCQ_SET Q2 fails because only the keyed option visibly signals gender.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "460",
     "quote": "- MCQ_SET `hard-4`: religious-liberty Q3 used treaties/taxes as distractors, making the Virginia Statute too obvious.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "461",
     "quote": "- Fix: replace distractors with same-domain religious-disestablishment alternatives.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md",
     "lines": "82",
     "quote": "- Be in the **same category** as the correct answer (e.g., if correct is a person, distractors are people; if a date, distractors are dates from the same era).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md",
     "lines": "112",
     "quote": "4. **Option grain-size mismatch**: 3 options are short, 1 is long with reasoning embedded. Length-balanced options only.",
     "verbatim": true
    }
   ],
   "against": "A first same-theme attempt regressed to 1/3 and was reverted, reason not given ('| v7 gender same-theme distractor attempt | 1/3 | Regressed badly; reverted. |', B0045 line 41). The report warns that such options must not become 'historically defensible alternate keys' (line 57).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; the 1.0 after the same-domain fix is at line 462. I added kit line 112 because no quote carried the similar-length clause. The original against said same-theme options 'can turn into defensible second keys', but the source gives that as a warning, not as the cause of the v7 regression. Truth 6 covers 'clearly wrong'; the same-domain construction is new."
  },
  {
   "index": 23,
   "verdict": "keep-with-fix",
   "statement": "Check the facts in an item's supporting text as well as its question (model answers, marking notes, explanations, source dates and attributions); good-looking items failed on errors there.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pil_monitor/inbox/2026-05-19T1456Z_den_unit1_trap_verifier.md",
     "lines": "17",
     "quote": "Observed LLM-required failures are mostly not structurally bad items. They are good-looking items poisoned by historically wrong teacher-facing metadata:",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md",
     "lines": "87",
     "quote": "SAQ can have fine prompts but fail because the sample response contains factual errors.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/24H_CARETAKER_STATE_20260521.md",
     "lines": "27",
     "quote": "`ap-apush-1-mcq_set-medium-12` improved from `0.33` to `0.97`",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; 0.33 to 0.97 checks, though under a release that also tightened leak checks (line 28), so 'explanation alone' is not shown. The 'document dated after its author's death' is at trap-verifier line 22. I reworded 'parts students don't see': source dates and attributions are visible in a document-based item. Related to truth 59; this adds where such errors hide. The 'den' in the path is a lab workspace name, not a person."
  },
  {
   "index": 24,
   "verdict": "keep-with-fix",
   "statement": "Use real, verified source texts; when none is available, describe a source by role and period rather than inventing a named author or date.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "88",
     "quote": "- Dynamic DBQ cannot be allowed to invent source documents. It needs retrieved vetted documents or document-bank retrieval by standard. Source retrieval fixed the focused institution DBQ slice: `dynamic_source_gate_dbq_mcqset_v1` DBQ scored 0.98.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pil_monitor/inbox/2026-05-19T1456Z_den_unit1_trap_verifier.md",
     "lines": "58",
     "quote": "Prefer generic-safe attributions over fancy named sources unless the person/date pair is verified.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_conscience/2026-05-29T1840Z_dream_sequence_sync.md",
     "lines": "16",
     "quote": "- **Gemini-vs-IB calibration** 14:55Z: 81.1% overall; DBQ 16.7% (Gemini correctly catches synthetic-source pattern; LEQ/MCQ_SET/SAQ 100%)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_conscience/2026-05-30T0640Z_dream_sequence_2_sync.md",
     "lines": "8",
     "quote": "Gemini-vs-IB calibration 97.8% on n=90 post-DBQ-realsource-swap (was 81.1% pre-swap)",
     "verbatim": true
    }
   ],
   "against": "Role-only attributions are a fallback, not a substitute: 'Role-based source descriptions can avoid hallucinated names; use carefully because real source packs are preferable.' (killer_pipeline_atomic_ducks_20260525.md line 98); 'Generic fabricated documents can reduce obvious fact-check failures, but may conflict with source authenticity expectations.' (deep_repo_extraction_20260525.md line 138). The 81.1% to 97.8% figure is agreement between two judges, which is consistency, not correctness (truth 35).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; 0.98 and 81.1%/16.7% check. I added the source of the found_by's 97.8% (to_conscience 2026-05-30 line 8), which no quote carried. Related to truth 57 (verified facts as the writer's only source), but this is about the source documents inside the item."
  },
  {
   "index": 25,
   "verdict": "keep-with-fix",
   "statement": "A source helps only if it fits the item's exact objective: locking items to retrieved but mismatched documents scored worse on average than using no retrieved documents.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/ib_d13_wrapper_eval/RESULTS.md",
     "lines": "24",
     "quote": "- The local v4 retrieval/doc-lock route is not usable as-is: it frequently retrieves irrelevant/misaligned packs, and doc-locking those packs hurts.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/ib_d13_wrapper_eval/RESULTS.md",
     "lines": "15",
     "quote": "| Local v4 D13 doc-lock | `y4axbi4f_d13_doclocked_generations.jsonl` | 0/30 | 0.0% | 0.1283 | 1 | 0 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/full150_y4axbi4f/RESULTS.md",
     "lines": "26",
     "quote": "| apush/dbq | 0/30 | 0.00% | 0.673667 |",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
     "lines": "106",
     "quote": "- source pack mismatch, e.g. prompt names Africans but documents only cover Native Americans.",
     "verbatim": true
    }
   ],
   "against": "Retrieval keyed to the exact objective worked: 'Source retrieval fixed the focused institution DBQ slice: `dynamic_source_gate_dbq_mcqset_v1` DBQ scored 0.98.' (failed_export_replay/RUNNING_SUMMARY.md line 88). Pass counts were 0/30 both with and without retrieval; the gap is in mean score (0.128 vs 0.674), and retrieval without the lock scored 3/30 (D13 RESULTS line 14).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. 'Did worse than none' had no baseline in the evidence, so I added the same model's 30-row DBQ baseline from the same day and judge version (full150 RESULTS line 26); the D13 file says its hotpatch input shares those baseline row IDs (line 23). It overlaps candidate 29 and truth 58; I kept it for the retrieval-specific point."
  },
  {
   "index": 26,
   "verdict": "keep",
   "statement": "Keep editorial text out of the body of a source: summaries, conclusions and notes on its usefulness read as fabricated or as aimed at the marker, so put them in the label or the marking guide.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/unit1_workflow_v2_branch_result_20260525T093757Z.md",
     "lines": "74",
     "quote": "- Local IB treated that as evaluation-gaming and zeroed DBQ.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "284",
     "quote": "- Important negative lesson: adding modern summaries inside DBQ `content` made relevance better but failed factual/stimulus quality because IB treats that as fabricated primary-source text.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "1997",
     "quote": "- Only failure was row 60 DBQ easy (`c_9eQY` Native environment), scoring 0.82 because the environment DBQ's Document 7 gave away the synthesis.",
     "verbatim": true
    }
   ],
   "against": "The same family later failed because its documents were 'too neutral and list-like for sourcing analysis' (production RUNNING_SUMMARY line 2008), so the evidence-inventory rewrite used for row 60 can overcorrect.",
   "general": true,
   "duplicate_of": "25",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; 0.82 rising to 1.0 after the rewrite is at lines 2001-2002. This extends truth 25 (keep reading directions apart from the words) from directions to any added framing, and failed_export_replay line 284 is already attached to 25. I kept it for the added evidence that meta text was zeroed as gaming and that summaries read as fabricated."
  },
  {
   "index": 27,
   "verdict": "keep",
   "statement": "Give a set of sources for an argument task distinct provenance and opposing views; an accurate but redundant, one-sided or neutral list-like set failed.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "448",
     "quote": "- DBQ `medium-7`: individual-liberties document pack was accurate but redundant and one-sided.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "2008",
     "quote": "rows 61-62 DBQ hard/medium failed because the documents were too neutral and list-like for sourcing analysis,",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
     "lines": "97",
     "quote": "- source-role diversity for demographic/disease prompts;",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. The tension-rich replacement scored 1.0 (line 450), and the rewrite into sourceable accounts with distinct provenance is at line 2010. This is new, and general for document sets used in argument tasks."
  },
  {
   "index": 28,
   "verdict": "keep-with-fix",
   "statement": "Count how many distinct items a run produced; a generator that served a few identical items over and over passed many checks but was exposed by variety checks and by objective-specific misses.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/A0F_COMPLETED_RUN_READINESS_20260520.md",
     "lines": "44",
     "quote": "| DBQ | 216 | 6 | 72 identical payloads |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/A0F_COMPLETED_RUN_READINESS_20260520.md",
     "lines": "50",
     "quote": "DBQ and MCQ_SET are behaving like static template banks. That can pass many rows, but it is exposed by variety scoring and by substandard-specific alignment failures.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/reports/run_324d5e51_live_update_decision.md",
     "lines": "21",
     "quote": "- MCQ_SET fingerprint uniqueness is below 30%; static stimulus templates are still active.",
     "verbatim": true
    }
   ],
   "against": "Variety needs enough samples to measure: 'The small sample showed MCQ_SET duplicate fingerprint `1/2`, so future pre-live diversity smoke should use at least 5 extra DBQ/MCQ_SET samples.' (request_trace/2026-05-21T075822Z_2926c4107df0.md line 27).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. 216 items with 6 distinct and 72 identical, plus 211 items with 13 distinct (line 45), check. Four distinct per 45 for MCQ_SET and SAQ is in the 324d5e51 decision table (lines 15-16). The original's 'failed each request's specific objective' overstated line 50, which says static banks 'can pass many rows'; I reworded it to match."
  },
  {
   "index": 29,
   "verdict": "keep",
   "statement": "Match content to the item's exact objective, not its broad topic or title; an item that passed for one objective failed when reused for a narrower neighbouring one.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/B0045_STAGED_MCQSET_INTERIM_20260519.md",
     "lines": "25",
     "quote": "3. Regression risk: broad winner reuse can fail a narrower substandard, as seen for gender/family when a labor-oriented passed sibling was reused.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/UNIT1_TO_ALL_UNITS_TRANSFER_PLAN.md",
     "lines": "80",
     "quote": "- Description-specific routes must beat generic lesson-title matches.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/analyzer/reports/run_f54d5849_what_is_going_wrong.md",
     "lines": "20",
     "quote": "Of 125 DBQ failures: **`curriculum_alignment = 0` in 98 % (122 / 125); `factual_accuracy = 0` in only 2 % (3 / 125).**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. 122/125 = 98% checks, and so does '71 of 98 quality failures' (a0f_failure_map lines 21-25: 6+11+8+71+2). It overlaps truth 58 (check topic relevance as its own check) but adds the grain: the exact objective, not the broad topic."
  },
  {
   "index": 30,
   "verdict": "keep-with-fix",
   "statement": "Treat example items given to a writer as a risk: it copies their content and flaws, so vet them and strip examples from other topics down to structure.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "71",
     "quote": "The first dynamic smoke copied a bad few-shot-like Gilded Age/Riis MCQ into an APUSH Unit 3 request.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "74",
     "quote": "- Strip historical substance from few-shot examples so they cannot donate wrong content.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "144",
     "quote": "- Same-unit few-shots can supply real content patterns; cross-unit examples are scrubbed to structure only so Unit 6/8 content cannot contaminate Unit 3.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/UNIT1_TO_ALL_UNITS_TRANSFER_PLAN.md",
     "lines": "60",
     "quote": "- Do not trust high-scoring few-shot/pattern rows blindly.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md",
     "lines": "548",
     "quote": "- Primary-source few-shot with long examples: `0/13`; likely overfits to source shape and drifts from the target objective.",
     "verbatim": true
    }
   ],
   "against": "Some example-based styles were the best for one type: '- Exam-writer few-shot MCQ_SET prompts are the best stable MCQ_SET style so far:' (NOTES.md line 538), though only at 4/13.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. The found_by's 83/150 vs 113/150 is fewshot_goldshape_v3 vs historians_only_v3, from the prompt_perfection runs' analysis.md files. I added lines 74 and 144, which state the remedy the statement gives; no original quote carried it. Related to truth 57, but this is about examples, not facts."
  },
  {
   "index": 31,
   "verdict": "keep",
   "statement": "When a pick-from-several pipeline fails, check whether any draft passed: if one did, fix the picking; if none did, fix how drafts are written, because more checks only reject.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md",
     "lines": "109",
     "quote": "If a passing candidate exists but was not selected, fix retrieval/selector; if none exists, fix generation/data.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md",
     "lines": "107",
     "quote": "- bank_gap rescue rate **0/4 = 0%** (confirmed: parent's fallback can't help; lab mining needed)",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/LLM_FINAL_ROUTE_STATUS_20260522T185623Z.md",
     "lines": "179",
     "quote": "The new guards caught the previous leaks, but the LLM filled the gap with new failure modes. More generic guard stacking is likely to chase symptoms.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. The 114/45 split and 9/11 vs 0/4 check against guide lines 97-107. This is a new diagnostic fork."
  },
  {
   "index": 32,
   "verdict": "keep",
   "statement": "Before adopting an automatic check, run it on known failures and known passes and report both how many failures it catches and how many good items it would wrongly reject.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/a0f_validator_probe_20260519.md",
     "lines": "3",
     "quote": "This is a local probe against the A0F export. It measures candidate validators against both failed rows and passed controls.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/a0f_validator_probe_20260519.md",
     "lines": "11",
     "quote": "- False rejects: 22 (0.063)",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md",
     "lines": "222",
     "quote": "- Both retired; were matching metric NAMES in evaluator narrative, not actual failures.",
     "verbatim": true
    }
   ],
   "against": "A check's audit needs enough cases: one regex family was retired as a false positive after a 0/5 check of sampled failure reasonings ('Confirmed 0/5 random failed-row reasonings cite this.', 20260520T201911Z_run_0506c1fd_v2_deploy_packet.md line 32).",
   "general": true,
   "duplicate_of": "37",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; 19 of 102 caught (0.186, line 9) and 22 of 351 known passes rejected check. This is truth 37 (score a judged check on labelled cases), with the judge's outcomes standing in for labels. I kept it for the added evidence, especially the false-reject side and detectors that matched metric names."
  },
  {
   "index": 33,
   "verdict": "keep",
   "statement": "A passed format check says nothing about quality; runs that were fully valid in shape still hid failing items.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/24H_CARETAKER_STATE_20260521.md",
     "lines": "54",
     "quote": "A scored `0.1.37` preflight found hidden quality failures despite shape passing",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
     "lines": "1030",
     "quote": "This proves the local candidate can emit schema-compatible content for all 26,355 benchmark rows, but it is not a substitute for IB scoring.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
     "lines": "31",
     "quote": "| `0.1.186` | fresh balanced50 shape `50/50`, score `41/50` | Availability fixed, quality not |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. 50/50 shape vs 41/50 score, the 26,355 rows, and the hidden 0.0 and 0.75 (caretaker line 54) check. This is general and not on the list."
  },
  {
   "index": 34,
   "verdict": "keep",
   "statement": "Write a report's narrative from the run's own numbers; templated summary text claimed 95% passing for a run in which every item scored zero.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/reports/run_5eb118bd_success_patterns.md",
     "lines": "93",
     "quote": "Almost everything passes (95%). Pass rows have ~7 documents (matches the live overlay hard rule) and roughly even doc word counts.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/runs_to_commits_40d.md",
     "lines": "41",
     "quote": "| 2026-05-26 19:59 | `5eb118bd` | 673 | 0.0% | `da0bc27` | `0.1.303-llm-final-mcqset-shape-repair` | dbq=0/132 leq=0/135 mcq=0/138 mcq_set=0/132 saq=0/136 |",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/reports/run_324d5e51_failure_modes.md",
     "lines": "1",
     "quote": "# Run-0133 v2 — failure deep-dive",
     "verbatim": true
    }
   ],
   "against": "The per-run tables in the same report family were computed from each run: '| dbq | 0/0 | n/a | 0 | n/a |' (run_5eb118bd_live_update_decision.md line 12).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. I checked beyond the sample: all 30 non-empty failure- and success-pattern reports carry the title 'Run-0133 v2', and all 15 success-pattern reports carry the identical 'Almost everything passes (95%)' sentence. Meanwhile the 5eb118bd tables count 0 passing rows (lines 85-88). This is new; truth 24 is about measuring from the delivered file, not about narrative text."
  },
  {
   "index": 35,
   "verdict": "keep",
   "statement": "Apply an extra pipeline stage only to the item types it measurably helps; source injection lifted source-based types while the same stages lowered free-response types.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/.openclaw/workspace-incept/memory/2026-05-21.md",
     "lines": "16",
     "quote": "- LEQ: Pipeline 90.4% vs Model standalone 100% (-9.6pp)",
     "verbatim": true
    },
    {
     "path": "~/.openclaw/workspace-incept/memory/2026-05-21.md",
     "lines": "23",
     "quote": "MCQ_SET and DBQ must remain in the pipeline because they rely on stimulus/RAG injection (+58.6pp and +20.9pp respectively).",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/BEAD_EVIDENCE_INDEX.md",
     "lines": "66",
     "quote": "- Finding: 19/25 = 76%. DBQ 4/5 (fallback works), but MCQ/MCQ_SET regress. **Use per-KC only, never globally.**",
     "verbatim": true
    }
   ],
   "against": "The lab guide took the opposite general stance: '**Architectural rule:** raw model is one component; pipeline is the multiplier.' (LAB_PIPELINE_GUIDE.md line 68). The memory note gives no sample sizes.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; -9.6 (line 16), -2.3 (line 17), +58.6, +20.9 and 19/25 check. The evidence is thin, since the memory note gives no n and the fallback result is n=25, but the statement is suitably hedged ('measurably helps'). This is new."
  },
  {
   "index": 36,
   "verdict": "keep-with-fix",
   "statement": "Name why items fail before choosing a fix; forty days of layered tactics added no overall lift and some type-specific regressions, while the decline they chased was mostly measurement faults.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/analyzer/reports/production_surface_40d.md",
     "lines": "8",
     "quote": "Every tactic layered on top (anti-static, selector, source-fallback, shape-repair, pubdate-strict) produced **zero aggregate lift** and several **cell-specific regressions**.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/analyzer/reports/production_surface_40d.md",
     "lines": "33",
     "quote": "The 40-day \"regression\" is largely **two infra contract-breaks masquerading as model collapse**",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md",
     "lines": "129",
     "quote": "Before prompt churn, check whether the failing KC is period-mismapped or criterion-misaligned.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/PIPELINE_WRAPPER_ACTION_PLAN.md",
     "lines": "105",
     "quote": "- Failure-forensics gate before pipeline changes.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "60",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; flat ~84% and the DBQ crash to 12.5% (line 25) check. The original said the fixes were made 'without a diagnosis', which the source doesn't show; I reworded it to what the source does show. This is close to truth 60 (read the failing items themselves); I kept it for the 40-day evidence and the adopted forensics-first gate."
  },
  {
   "index": 37,
   "verdict": "keep-with-fix",
   "statement": "Make each part of a multi-part question answerable on its own, give each prompt a single task, and order parts from lower to higher demand.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_saq.md",
     "lines": "71",
     "quote": "2. **Chained dependencies.** Part b is impossible to answer without first answering part a correctly. Parts should be independent within a shared context.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_leq.md",
     "lines": "76",
     "quote": "4. **Multi-task prompt.** \"Discuss the causes AND consequences AND legacies of X\" — that's three essays. One task per LEQ.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_saq.md",
     "lines": "83",
     "quote": "- [ ] Verb difficulty escalates a → b → c (typical pattern)",
     "verbatim": true
    }
   ],
   "against": "The kit's whole-set effect is unclear, not negative. The 79.7% cited for 'kit on' counts 60 ungraded rows as fails (861/1080, run_4c9da828_overview.md line 36; 861/1020 = 84.4% on graded rows, run_4c9da828_live_export_analysis.md line 7). The baseline was fully graded at 85.7% (926/1080, 20260520T201911Z deploy packet lines 8-9), so the gap is about 1.3 points between different releases. These rules are untested one by one, and the escalation line says 'typical pattern', not a requirement.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim, and the statement and evidence are unchanged. I corrected the against: the reader's caveat that switching the kit on lowered the pass rate (79.7% vs 85.7%) mixes denominators, which is the very mistake in candidate 0. This is an adopted rule and new; truth 68 is about a shared source, not part independence."
  },
  {
   "index": 38,
   "verdict": "keep-with-fix",
   "statement": "Match a question's thinking demand to what its objective asks; recall questions on analysis objectives, and prompts whose verb doesn't match the named skill, fail.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md",
     "lines": "115",
     "quote": "7. **Recall-only on a higher-order standard**: standard demands analysis but stem asks \"what year did X happen\". Match cognitive demand to the standard.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_leq.md",
     "lines": "73",
     "quote": "1. **Reasoning skill mismatch.** Prompt is labeled \"comparison\" but actually asks for causation. Match the verb to the skill.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
     "lines": "387",
     "quote": "- Repaired MCQ hard institution item to require synthesis rather than recall.",
     "verbatim": true
    }
   ],
   "against": "The same kit caveat, corrected: on graded rows the kit-on run scored 84.4% against 85.7% for the minimal run (run_4c9da828_live_export_analysis.md line 7; 20260520T201911Z deploy packet line 9). Those were different releases, so the kit's effect is unmeasured rather than negative.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim, and the statement and evidence are unchanged; I corrected the against's denominator error. The synthesis rewrite at line 387 is one targeted repair. This is an adopted rule, general and new."
  },
  {
   "index": 39,
   "verdict": "keep-with-fix",
   "statement": "Check a question set as a whole: no two questions may test the same fact or share a correct answer, and no answer may contradict another's.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq_set.md",
     "lines": "89",
     "quote": "6. **Inter-question contradictions**: Q1's correct answer says \"X caused Y\", Q3's correct answer says \"Y caused X\". Audit consistency across the set.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq_set.md",
     "lines": "63",
     "quote": "- No two questions have the same correct answer or test the same fact.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/reports/run_324d5e51_failure_modes.md",
     "lines": "18",
     "quote": "| `redundant_questions` | 17 |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; the 17 redundant_questions tags are a regex-and-sub-score tally (failure-modes lines 5-6). 'Share a key' could be read as sharing an answer letter, which is truth 8, so I reworded it. The no-repeat half overlaps truth 41; the contradiction check is new."
  },
  {
   "index": 40,
   "verdict": "drop",
   "statement": "Require a judge to quote the evidence behind each verdict, and discard verdicts that come without one.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pil_monitor/inbox/2026-05-19T1456Z_den_best_of_n_protocol.md",
     "lines": "92",
     "quote": "If `evidence_quote` is empty, invalidate the judge result.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pil_monitor/inbox/2026-05-19T1456Z_den_best_of_n_protocol.md",
     "lines": "74",
     "quote": "Only judge surviving candidates. The judge must output evidence:",
     "verbatim": true
    }
   ],
   "against": "No measured result for this rule appears in the sources.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim at lines 74 and 92, but they come from a single proposal message. A search of the lab's reports, rubber_ducks folder, lab guide and NOTES found no sign that the evidence-quote rule was adopted or measured. Labelling it an adopted rule overstates the evidence. The nearest settled truths are 17 (quote exactly, checked in code) and 32."
  },
  {
   "index": 41,
   "verdict": "keep",
   "statement": "Pin and record the judge's version with every score, and re-grade older results before comparing them; scores from an earlier judge version are design evidence, not current results.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/HANDOVER_PARALLEL_IDEAS.md",
     "lines": "23",
     "quote": "The parent project has old 90%+ results, but those were on older grader behavior. Do not treat them as current performance unless regraded on the current InceptBench version.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/PIPELINE_WRAPPER_ACTION_PLAN.md",
     "lines": "104",
     "quote": "- Grader-version pinning in every eval artifact.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pipeline_status_2026-05-18.md",
     "lines": "164",
     "quote": "5. Claims from older InceptBench versions should be treated as design evidence, not certified current scores.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "45",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; the sibling generator's 97% on an older judge is at pipeline_status line 148. This is the same lesson as truth 45 (fix the rubric before measuring), which already carries the judge-version items from the analyzer memory and the action packet. I kept it for the added evidence."
  },
  {
   "index": 42,
   "verdict": "keep",
   "statement": "Treat a gain that comes from exploiting a gap in the judge's rubric as fragile, not as better content.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md",
     "lines": "132",
     "quote": "MCQ/SAQ/LEQ no-stimulus may pass current rubrics, but it is a known rubric hole and should be treated as fragile/second-tier unless the product spec allows review-drill shape.",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/sweep_n25_final_verdict_20260526.md",
     "lines": "73",
     "quote": "| `mcq_no_stimulus_can_help` | **rubric_exploit** | If IB patches no-stim blindspot, fall back to C (loses MCQ 5/5, recovers MCQ_SET 3/5) |",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md",
     "lines": "141",
     "quote": "Different optimization targets (pass judge vs serve educators)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. This is an adopted rule: every recipe carrying the no-stimulus directive scored 3/3 on MCQ at n=15 (14-way line 60), and the lab tagged it as an exploit with a named fallback. Related to truth 44 but more specific: the gain comes from a gap in the rubric."
  },
  {
   "index": 43,
   "verdict": "keep",
   "statement": "Refuse to produce kinds of item that have never been checked against the judge rather than ship unvalidated output.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/README.md",
     "lines": "67",
     "quote": "Unsupported (returns 501): `msq`, `fill-in`, `match`, `sequence`, `article`.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/README.md",
     "lines": "137",
     "quote": "- We have no signal on `msq` / `fill-in` / `match` / `sequence` / `article` from internal eval — gated to 501 to avoid shipping unvalidated outputs.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. This is an adopted policy with no measured outcome. It is general and close in spirit to truth 47, but it concerns refusing unvalidated item kinds."
  },
  {
   "index": 44,
   "verdict": "keep",
   "statement": "Give the writer the full description of the objective and the criteria its work will be judged by, not just the topic name.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/sweep_n25_final_verdict_20260526.md",
     "lines": "49",
     "quote": "1. **`ib_rubric_criterion_alignment` is the breakthrough duck.** Adding it to G yields the unique top recipe at 23/25 with the highest avg score (0.978) AND MCQ_SET 4/5. Predicted at -5 from n=15, actual at +3.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_analyzer/2026-06-01T1838Z_dream_sequence_sync.md",
     "lines": "28",
     "quote": "injects expanded LO + KC-description text into the DBQ generator prompt directly, so curriculum-alignment signal lands in the input, not just the rubric.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md",
     "lines": "45",
     "quote": "- `assessment_boundaries`: `{{assessment_boundaries}}` (what to assess; what NOT to assess)",
     "verbatim": true
    }
   ],
   "against": "The same directive had been predicted to cost five passes ('| add_ib_rubric_criterion_alignment | **-5** |', sweep_pre_score_analysis_20260526.md line 93). The sweep was one seed of 25 items, and the re-measurement of the description injection is not in the sources.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; 23/25, 0.978 and the 67-recipe sweep (line 5) check. The evidence is thin: one single-seed 25-item sweep, and the description injection was never re-measured (the re-run ask at to_analyzer 06-01 line 34 has no reply in from_analyzer). This is the writer-side counterpart of truth 33, not a duplicate."
  },
  {
   "index": 45,
   "verdict": "keep-with-fix",
   "statement": "When generated items get facts wrong, check whether those facts are in the generator's material (training data or supplied context) before choosing a fix: if missing, add them; if present, change how the generator is conditioned or sized.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_analyzer/2026-05-27T1741Z_DIAGNOSIS_data_adequacy_binding_lever.md",
     "lines": "16",
     "quote": "**The discriminating test (please make the data-adequacy assessment answer THIS, not just row count):** take the off-period hallucination cases (e.g. the 1920s-DBQ-for-Unit-1 sample) and check whether those specific Unit-1 facts are PRESENT in the training corpus.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_analyzer/2026-05-27T1741Z_DIAGNOSIS_data_adequacy_binding_lever.md",
     "lines": "19",
     "quote": "Row-count alone (\"14k = not enough\") cannot tell these apart, and it's the exact spot where \"bigger base\" gets pulled without the binding lever named.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_analyzer/2026-06-01T1838Z_dream_sequence_sync.md",
     "lines": "30",
     "quote": "This addresses §2 coverage-lever side of your 5/27 binding-lever fork: facts ARE in the corpus, but the generator wasn't conditioned on the curriculum context that defines the alignment criterion.",
     "verbatim": true
    }
   ],
   "against": "The test was asked for again, but no verdict file exists: 'Drop verdict at `from_analyzer/<UTC>_COVERAGE_VS_CAPACITY_v4.md`.' (to_analyzer/2026-05-28T0614Z_dream_sequence_sync_2.md line 39). The later message asserts 'facts ARE in the corpus' without the test.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. The source's fork is coverage (fix the data) vs capacity (a bigger model, lines 13-14); a later message picked conditioning. The original's 'material the writer was given' and 'how the writer uses it' blurred that, so I reworded it. I confirmed that from_analyzer holds only two files: an acknowledgement and this diagnosis."
  },
  {
   "index": 46,
   "verdict": "keep-with-fix",
   "statement": "Check an item's stated difficulty against how real students do on it (the share who answer correctly) rather than trusting the writer's or the judge's label.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Documents/aptraining/analyzer/.lanes/teaching-benchmark/STRATEGY_REPORT.md",
     "lines": "33",
     "quote": "- **P-Value & Point-Biserial Mapping:** Store real-world question difficulty (p-value) against generated questions. If a generated \"Medium\" question has a real-world p-value of 0.20 (Hard), we register a `difficulty_misalignment` failure.",
     "verbatim": true
    }
   ],
   "against": "Proposals only; no student data or measured result appears in the sources.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "The quote is verbatim. I dropped the workspace strategy report's line 82 from the evidence: it is verbatim, but it flags facts where students' success rate is low, which concerns teaching gaps, not difficulty labels. This remains an open question, since it was proposed and never run."
  },
  {
   "index": 47,
   "verdict": "keep",
   "statement": "Keep each rule for an item in one place; instructions that contradicted each other, or a prompt rule that disagreed with a code check, made the writer refuse or were silently overridden.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md",
     "lines": "51",
     "quote": "| Satisfaction kit DBQ refusal | 0% on DBQ | `system_prompt_dbq.md` line 135: \"Without D13: refuse\" — we don't wire D13 |",
     "verbatim": true
    },
    {
     "path": "~/Documents/aptraining/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md",
     "lines": "91",
     "quote": "\"EXACTLY 4 questions\" conflicted with hardcoded validator at",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/WINS_20260514.md",
     "lines": "152",
     "quote": "- The kit is prepended to the system prompt, then the original service prompt is appended as the hard schema authority. This prevents the kit's illustrative field names from breaking InceptBench JSON shape.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. The four-vs-three validator clash being silently overridden (lines 91-93) and the refusal over contradictory period framing (lines 113-114) check. This is new."
  }
 ],
 "existing_checked": [
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Documents/aptraining/analyzer/reports/run_f54d5849_what_is_going_wrong.md",
   "lines": "19",
   "quote": "Wrapper sends `grade: \"1\"` for Unit 1; grader reads as 1st grade; zeros `educational_accuracy` and `clarity_precision`.",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/run_73348c1a_orchestrator_contract.md",
   "lines": "57",
   "quote": "- Echo grade as `AP United States History`, not numeric unit values like `\"1\"` or `\"3\"`.",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pipeline_status_2026-05-18.md",
   "lines": "152",
   "quote": "1. Authoritative course/unit propagation is critical.",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/a0f_failure_map_20260519.md",
   "lines": "24",
   "quote": "| quality_fail_standard_alignment | 71 |",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/WINS_20260514.md",
   "lines": "49",
   "quote": "- Naive best-of-scored-candidates composite predicted `138/150`, but fresh IB scored `126/150`. Conclusion: single-score banking overfits IB noise.",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/PIPELINE_WRAPPER_ACTION_PLAN.md",
   "lines": "255",
   "quote": "Recovery cascade: 1. keep first patch K=1 only; 2. add BoN only in separate bead; 3. require held-out judge before selection.",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports (rejected: line 43 concerns the contract and ethics of picking with the target judge, not confirming picks with an independent check; the supporting line is 41, '- It has not passed main-a independent n=50 hidden hold-out.')",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/candidate_library_20260525.md",
   "lines": "43",
   "quote": "- It relies on build-time IB oracle selection, which is acceptable for offline banks only if contract and ethics are explicit.",
   "ok": false
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
   "lines": "1948",
   "quote": "the grader showed nondeterminism on repeated MCQ batches.",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports (rejected: one score shows no variation; the same folder's analysis.md line 3 re-scored the same outputs at 109/150 with per-type swings, but it is dated 21 May against 13 May, so a judge-version change cannot be ruled out)",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/prompt_perfection/runs/ib_safe_v2_t0.0_p1.0/analysis.8001.md",
   "lines": "3",
   "quote": "Passed: 106/150 (70.67%)",
   "ok": false
  },
  {
   "truth": 65,
   "effect": "supports (rejected: in that run only MCQ was generated K=6; DBQ/LEQ/SAQ/MCQ_SET were served from a stored bank (NOTES.md lines 930-931, 951), so the flat MCQ_SET curve does not test best-of-K)",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/K_sweep_99pct_20260519T180652Z.md",
   "lines": "48",
   "quote": "| apush/mcq_set | 16/30 (53.3%) | 16/30 (53.3%) | 16/30 (53.3%) | 16/30 (53.3%) | 16/30 (53.3%) | 16/30 (53.3%) |",
   "ok": false
  },
  {
   "truth": 65,
   "effect": "supports (rejected: the K=1-5 values are proxies from archived model-judge scores, not judge results (K_sweep line 41), and with the MCQ_SET contrast void the line does not separate random slips from systematic failures)",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/K_sweep_99pct_20260519T180652Z.md",
   "lines": "47",
   "quote": "| apush/mcq | 6/30 proxy | 9/30 proxy | 17/30 proxy | 21/30 proxy | 26/30 proxy | 28/30 (93.3%) |",
   "ok": false
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/handover_observations_training_questions_2026_05_27.md",
   "lines": "25",
   "quote": "synapse learning `cc714738` (K=N transfers format not facts):",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pil_monitor/inbox/2026-05-19T1456Z_den_best_of_n_protocol.md",
   "lines": "137",
   "quote": "Those need repair layers, not more N.",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
   "lines": "81",
   "quote": "- Store enough candidate payload to replay selector mistakes. Prior K-sweep was weakened because full unselected candidate payloads were missing.",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/reports/run_324d5e51_live_update_decision.md",
   "lines": "38",
   "quote": "- Do not add broad deterministic filters unless a selector replay proves net lift.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_search_20260526.md",
   "lines": "109",
   "quote": "if a future change broke any of the audit rules, this control would fail to fail — that's the canary.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/PIPELINE_WRAPPER_ACTION_PLAN.md",
   "lines": "60",
   "quote": "| Local validation | known visual-map DBQ is rejected | regex false-positive on legitimate text source; narrow regex | visual-map DBQ passes |",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md",
   "lines": "59",
   "quote": "All children sharing one correct letter is a set-level smell.",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
   "lines": "89",
   "quote": "Q2 content was fixed, but answer keys clustered on A/B and scored 0.84.",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq_set.md",
   "lines": "84",
   "quote": "Verify every question requires the stimulus by testing the counterfactual",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md",
   "lines": "116",
   "quote": "8. **Multi-correct**: two options are defensibly correct. Verify with the rationale that only ONE option survives strict reasoning.",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/UNIT1_TO_ALL_UNITS_TRANSFER_PLAN.md",
   "lines": "66",
   "quote": "use overly broad \"best explains\" stems with multiple defensible answers.",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
   "lines": "2024",
   "quote": "row 336 MCQ_SET easy scored 0.75 because Q2 asked for European disagreement not actually present in the stimulus,",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
   "lines": "105",
   "quote": "- `dynamic_source_gate_mcqset_v2`: MCQ_SET regressed to 0.0 because generated questions referenced phrases not present in the enforced stimulus (`system of checks and balances`, `supreme law of the land`).",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
   "lines": "98",
   "quote": "- MCQ_SET validator now rejects quoted phrases in child questions/explanations when those phrases are absent from the enforced stimulus.",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/HANDOVER_PARALLEL_IDEAS.md",
   "lines": "52",
   "quote": "the model emits fabricated visual/document promises that InceptBench hard-zeroes.",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/PIPELINE_WRAPPER_ACTION_PLAN.md",
   "lines": "151",
   "quote": "- prose description of a missing visual is invalid,",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq_set.md",
   "lines": "51",
   "quote": "- If image: provide rich descriptive caption (the grader sees text, not image).",
   "ok": true
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md",
   "lines": "243",
   "quote": "- Deterministic compression solved grader length but destroyed educational signal / source richness.",
   "ok": true
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
   "lines": "284",
   "quote": "Context belongs in source labels/rubrics, not document content.",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/24H_CARETAKER_STATE_20260521.md",
   "lines": "29",
   "quote": "Lesson: do not hard-reject all deterministic MCQ_SET quality failures unless K is expanded or a fallback candidate policy exists.",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/WINS_20260514.md",
   "lines": "207",
   "quote": "- Service commit `985f867` changed `/v1/per-question-generator` to one generation only, with MCQ_SET quality checks recorded as advisory metadata instead of blocking responses.",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "supports (rejected: a project-scope rule about which model may write questions, not evidence that every choice and check should be a bounded judgment)",
   "path": "~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md",
   "lines": "9",
   "quote": "- External models may be used only for judging/selection; they must not generate AP question content.",
   "ok": false
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
   "lines": "76",
   "quote": "- Do not trust Gemini to catch MCQ_SET answer leaks, truncated options, wrong crop direction, or DBQ source hallucination. Evidence from the rejected branch shows it missed these.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Documents/aptraining/analyzer/.agent/BRIEFING.md",
   "lines": "28",
   "quote": "Grader (IB v2.5.x) co-evolved with chain — \"sometimes a sycophant of the chain\"",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md",
   "lines": "141",
   "quote": "Different optimization targets (pass judge vs serve educators)",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Documents/aptraining/analyzer/.agent/MEMORY.md",
   "lines": "44",
   "quote": "3. **Grader co-evolved with chain.** IB v2.5.3 → v2.5.6 → v2.5.7 → v2.5.11 shifts what \"passes\" mean retroactively. No ensemble, no cross-judge calibration. Treat the grader as a variable.",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/MAIN_AGENT_ACTION_PACKET.md",
   "lines": "58",
   "quote": "Use current IB v2.5.7 only. Do not compare against v2.5.6/v2.5.3 without regrade.",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
   "lines": "249",
   "quote": "The next proof must be a fresh dynamic generation run using the patched pipeline, followed by the prior n=30 regression gate and eventually the full failed-export replay.",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/promotion_gate_20260525.md",
   "lines": "47",
   "quote": "- Failed re-validation/cherry-pick artifacts including old Den 50/50 proof and EXPLOIT-003.",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md",
   "lines": "127",
   "quote": "- **SAQ silent regression -4.5pp** — nobody was focused on this; warrants bisect of deploys 0506c1fd→e7e1d980",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/UNIT1_TO_ALL_UNITS_TRANSFER_PLAN.md",
   "lines": "118",
   "quote": "- Use the same stop rule: if any type drops below 90% in the sample, stop and repair that type before broadening.",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md",
   "lines": "2054",
   "quote": "This meets the raw 95% slice threshold but fails the methodology/type-floor gate because MCQ_SET is 8/9 = 88.89%.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
   "lines": "80",
   "quote": "- Log every candidate, validation reason, selector score, selected index, model, qtype, row id, and final content hash.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
   "lines": "146",
   "quote": "- Every dynamic run writes `retrieval_manifest.jsonl`, proving per row how many curriculum facts, local constraints, source docs, question-bank examples, and few-shots were used.",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_saq.md",
   "lines": "39",
   "quote": "- Scoring criteria are concrete enough to grade consistently — describe what makes an answer correct, don't dictate the exact answer.",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_saq.md",
   "lines": "73",
   "quote": "4. **Ambiguous scoring.** \"Acceptable answers should be reasonable.\" → Useless. Replace with \"Acceptable answers identify [type of factor] and explain [type of mechanism].\"",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pipeline_status_2026-05-18.md",
   "lines": "154",
   "quote": "3. SAQ scoring notes should avoid hallucination-prone evidence lists.",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
   "lines": "209",
   "quote": "SAQ sample responses were too generic to be scorer-facing.",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
   "lines": "225",
   "quote": "- SAQ repair now emits concrete scorer-facing examples by topic, such as Jay's Treaty, Neutrality, XYZ, and Quasi-War for foreign-policy differences.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/PIPELINE_WRAPPER_ACTION_PLAN.md",
   "lines": "108",
   "quote": "- Few-shot for format only, not factual hallucination.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md",
   "lines": "55",
   "quote": "**Do NOT fabricate quotes or sources.** If you don't know a verifiable source, drop the stimulus and write a non-stimulus item.",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq_set.md",
   "lines": "74",
   "quote": "- The set fails if ANY single question fails any metric.",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Documents/aptraining/analyzer/reports/production_surface_40d.md",
   "lines": "25",
   "quote": "Pattern: a fix aimed at one cell kills that cell and never repairs the chronically-broken one.",
   "ok": true
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Documents/aptraining/analyzer/.agent/MEMORY.md",
   "lines": "42",
   "quote": "fewshot_bank = v43soup + v52b + their own outputs.",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md",
   "lines": "809",
   "quote": "- Next MCQ_SET attempt needs stronger content construction, not another wording-only leak warning.",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "supports (rejected: the line prefers post-generation validation to another broad instruction; it says nothing about naming what to use instead of what to avoid)",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/WINS_20260514.md",
   "lines": "104",
   "quote": "- The wrong move is another broad instruction.",
   "ok": false
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pil_monitor/inbox/2026-05-19T1456Z_den_unit1_trap_verifier.md",
   "lines": "25",
   "quote": "These are deterministic trap failures. Retrieval and prompting can reduce them, but a verifier can catch them cheaply.",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pipeline_status_2026-05-18.md",
   "lines": "178",
   "quote": "2. Split schema normalization from content generation so unsupported fields cannot leak.",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/a0f_validator_probe_20260519.md",
   "lines": "42",
   "quote": "The visible deterministic rules catch the obvious defects but cannot reliably identify the evaluator's latent concerns without damaging passed controls.",
   "ok": true
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq_set.md",
   "lines": "86",
   "quote": "3. **Stimulus too thin**: 30-word stimulus + 4 questions = no question can actually require it. Match stimulus depth to set size.",
   "ok": true
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
   "lines": "171",
   "quote": "- rubric must match prompt scope;",
   "ok": true
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md",
   "lines": "224",
   "quote": "- LEQ repair is topic-specific instead of using a generic regional-economic rubric.",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md",
   "lines": "23",
   "quote": "The version numbers are not monotonic improvements. Treat every version as a measured hypothesis.",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/.openclaw/workspace-incept/memory/ap-benchmark-context.md",
   "lines": "48",
   "quote": "diagnose → fix one thing → commit → retest → check regression → repeat until 98%",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/full150_y4axbi4f/RESULTS.md",
   "lines": "12",
   "quote": "After retrying all 25 initial score-error rows with a longer single-row timeout:",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/WINS_20260514.md",
   "lines": "245",
   "quote": "- Per user direction, the long IB run was stopped and treated as grader instability rather than a pipeline result.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md",
   "lines": "101",
   "quote": "- No metadata in the student-visible fields hinting at the correct answer.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md",
   "lines": "50",
   "quote": "Map labels should be names/regions only; descriptors cause reading-comprehension leaks.",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md",
   "lines": "62",
   "quote": "Pairwise stem cosine catches redundant child questions.",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/B0045_STAGED_MCQSET_INTERIM_20260519.md",
   "lines": "24",
   "quote": "passed rows have balanced distractors, historically accurate content, concise stimulus use, and distinct child-question jobs.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md",
   "lines": "203",
   "quote": "- Real source of (1)/(2) export 81.6% baseline is `/v1/apush-all-units-generator` (every item id starts `apush-all-units-`).",
   "ok": true
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md",
   "lines": "76",
   "quote": "- **Rule:** every recommendation requires ≥3-seed evidence before shipping a packet.",
   "ok": true
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Documents/aptraining/parallel-ideas-lab/reports/unit1_workflow_v2_branch_result_20260525T093757Z.md",
   "lines": "74",
   "quote": "- Local IB treated that as evaluation-gaming and zeroed DBQ.",
   "ok": true
  }
 ]
}
```
