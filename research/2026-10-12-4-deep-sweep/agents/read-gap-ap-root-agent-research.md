# read:gap:ap-root-agent-research

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "ap-root-agent-research",
 "coverage": {
  "read": [
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/ (all nine: failure_taxonomy.md, eval_baseline.md, data_audit.md, best_approach_analysis.md, sota_strategy.md, inference_clean.md, gate1_decision.md, MORNING_SUMMARY.md, OVERNIGHT_RECAP.md), read in full",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/LESSONS_LEARNED.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/MEMORY.md, NORTH_STAR.md, PLAN.md, PLAN-user-prompts.md, plans/PLAN-mission-2026-04-26.md (full)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/COMPREHENSIVE_PLAN_v2_2026_06_02.md (first 170 lines in full, rest keyword-scanned: mesh/ops content)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md (all 260 lines)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_*.md (all 27 files, full)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/plan_v91_pipeline_mined_dpo_2026_05_21.md and plan_v92_pipeline_distillation_single_model_2026_05_22.md (full); plan_v93_perfect_brain_data_training_2026_05_22.md (first 140 lines full, remainder keyword-scanned)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MASTER_DECISION_TREE_v2_2026_05_11.md, SESSION_DECISIONS_2026_05_11.md, PILLARS_2026_05_12.md, FINAL_PLAN_2026_05_11_v3.md, FINAL_PLAN_2026_05_11_v4.md, OVERNIGHT_PLAN_2026_05_11_v1.md, AUTONOMOUS_CHAIN_LOOP_2026_05_20.md, HANDOFF.md (full)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md (close reasons; bulk-close boilerplate skipped)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/spec_v97_dbq_focused_criterion_grounded_dpo_2026_05_25.md (full); spec_v92, spec_v53, spec_template_iteration, STATE_CURRENT_2026_05_12T0805Z.md, state_training_chain_2026_05_12T1300Z.md, state_current_2026_05_07*.md, state_current_progress.md, THELOOP_SKILL_GATEWAY_UTILIZATION_AUDIT_2026_05_12.md, reference_fireworks_jobprogress_misleading_2026_05_12.md (keyword-scanned, relevant sections read)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/READY_FOR_[name]_* (4), [name]_OPERATING_MODEL_2026_05_12.md, [name]_OUT_OF_LOOP_AUTONOMY_2026_05_12.md (keyword-scanned as leads only; nothing cited)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent-v2/README.md, ARCHITECTURE.md, templates/postmortem.md, templates/eval-cycle.md, profiles/verifier.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/goal.md, plan.md (all 586 lines), v38_master_record.md, v39_master_record.md, v38_decision_rules.md, achieved.md (all)"
  ],
  "skipped": [
   ".agent/memory/auto/ — duplicates the auto-memory backup covered by another direction (per instructions)",
   "Scaffold: AGENT.md, SOUL.md, TOOLS.md, IDENTITY.md, USER.md, PATTERNS_CATALOG.md, KNOWLEDGE_PACK.md, GETTING_STARTED.md, HUMAN_GUIDE.md, TWEAKING.md, GOGCLI_STARTER.md, .agent/skills/ (tooling)",
   "Operations notes: AGENT_MESH_EXPANSION_2026_06_02.md, MACMINI_MIGRATION_PLAN_2026_06_02.md, MAIL_PROTOCOL.md, CLOUD_WORKFLOW.md, OVERNIGHT_PROTOCOL.md, SCHEDULED_2H_TICK_PROMPT.md, THELOOP.md (operational map, not listed), memory/synapse_daily_cycles/, synapse_agent_registry.md",
   "memory/BEADS.md.bak_20260522T151017Z (backup copy); spec_v88-v91 (training-recipe specs only)",
   ".agent-v2 builder/archivist profiles and training-cycle/hyper-sweep templates (not listed; operations)",
   "Snapshot READY_FOR_[name]_*, HANDOVER_SESSION_END, MODEL_TRAINER_RESPONSE, SCALE_UP_PLAN files (not listed; name-bearing status notes)",
   "Model-training mechanics throughout (learning rates, LoRA rank, DPO/ORPO, soups, warm-start chains, epochs, GPU quota, vendors) — excluded per instructions",
   "Never opened: .env, .local-secrets, secrets.env.template or any key/token file"
  ],
  "notes": "(1) Credentials: eval_baseline.md (setup and command blocks in its sections 1.3, 4.5, 5 and 8) and .agent/MEMORY.md (Facts section) contain plaintext API keys; none of those lines are quoted here and the merge step should not quote them either. (2) name_bearing_source: every path carries the machine owner's home-folder name, so I applied the flag to note file names (READY_FOR_*, *_OPERATING_MODEL_*, *_OUT_OF_LOOP_AUTONOMY_*). No candidate relies on those notes, so all flags are false; they were read only as leads (e.g. the operating-model note's 'Trusting numbers at face value' corroborates candidate 18 but is not cited). (3) Judge-rationale quotes were trimmed to fragments without personal or historical-figure names; agent labels (Quill, Atlas, Oracle, Compass, Shadow, Cheater, den, main-A, orch) remain inside a few quotes. (4) Project numbers conflict across files (canonical 90.67% vs verified 88.67%; a v39 '73.33%' found in no eval file; one audit recorded as drift CONFIRMED in a status note and CLEAN in SESSION_DECISIONS) — each is quoted as written. (5) Two research-backed rules (examples transfer form not facts; strict output format costs quality) cite papers with no DOI or URL in these files, so they are labelled adopted rule / measured, not external research. (6) Leads outside this direction: work/ML learnings/sft_v7_benchmark_postmortem.md (origin of the set-coverage and negative-instruction findings, cited by line in failure_taxonomy.md); Cheater and den-of-ideation artifacts/quarantine verdicts (stimulus-strip result, cache coverage) referenced at BEADS.md lines 705-714; auto-memory files project_v43soup_root_cause_visual_artifact_2026_05_12.md, research_fewshot_format_not_facts.md, research_constrained_decoding_per_cell.md, feedback_r41d_continuous_metric.md, feedback_question_critically_3_lessons_2026_05_08.md. (7) Most of this corpus is training mechanics; the candidates are the parts that bear on making, judging or measuring generated items. Read-only throughout; no mgr registration was run from this subagent because it writes to the ledger."
 },
 "candidates": [
  {
   "statement": "Measure a content generator on single attempts with no retries, selection or after-the-fact filters, and report that rate as its quality; selection and retries inflate the rate and hide failures.",
   "kind": "measured",
   "found_by": "The project's headline 83.3% pass rate came from runs with best-of-3 selection, a document filter and a retry; the same model scored 52% clean against 86% with those aids, a clean single-attempt run of the next model scored 13.3%, and retries had hidden a length cut-off that broke about half the outputs of one item type.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "352",
     "quote": "Aggregate APUSH+APWH for these two N=30 runs: **52% (clean) → 86% (+crutch) = +34pp**."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/eval_baseline.md",
     "lines": "243",
     "quote": "**The 83.3% prior baseline was carrying ~70 pp of inference-crutch lift.** Clean one-shot SFT v7 is at 13.3%."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/eval_baseline.md",
     "lines": "16",
     "quote": "The prior pipeline hid this with retry; one-shot exposes it."
    }
   ],
   "against": "Samples are small and partly mismatched (failure_taxonomy.md line 349: '(different prompts; clean N=3 is too small)'); the 83.3% and 13.3% figures come from different model versions; retrying a failed delivery was kept as legitimate (inference_clean.md line 42: 'Transport-level retry on transient 5xx — does not condition on output content.').",
   "adds_to_existing": [
    65,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check source texts for fabrication with a check of their own, because a general quality judge can pass nearly every item whose sources were invented.",
   "kind": "measured",
   "found_by": "A stricter source-checking rubric found 95% of one item type's stimulus texts fabricated while the general judge passed about 100% of them; a cross-check run recorded 100% fabrication in the source-bearing item types and 0% in types without sources; a rescore found fabricated primary sources in a version the general judge had rated highly.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "80",
     "quote": "v29 fabricates MCQ_SET stimuli at 95% under BAML rubric; IB passes at ~100%."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "177",
     "quote": "SAQ/LEQ 0% fab; MCQ/MCQ_SET/DBQ 100% fab"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "81",
     "quote": "Oracle's BAML-rubric rescore: -13.3pp aggregate Goodhart gap; SAQ 4/6 not 6/6; **2 fabricated primary sources in MCQ_SET**"
    }
   ],
   "against": "The general judge was later changed to hard-fail fabricated documents (feedback_curriculum_api_mandatory_2026_05_11.md line 9: 'IB v2.5.6 grader added DBQ stimulus_quality hard-zero (fabricated docs auto-fail)'); the calibration-gap entry is a lower-tier record whose investigation was 'deferred until D13 ships + v41-d13 eval.' (memory/MEMORY.md line 80).",
   "adds_to_existing": [
    38,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Never let a writer invent a source text and attach a real author or date to it: take source texts from a verified bank, use them word for word, and drop any item whose source can't be matched rather than patching it.",
   "kind": "measured",
   "found_by": "Generated document-based items failed the source-quality check in 10 of 11 cases because the writer produced plausible but fabricated documents; injecting matched real documents at generation time lifted that type from 0% to 4 of 6 in a smoke test, with the writer using them verbatim; the project made 'trace every text field to a primary source, drop don't patch' a standing rule.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/FINAL_PLAN_2026_05_11_v3.md",
     "lines": "118",
     "quote": "DBQ failures show `stimulus_quality: 0.0` in 10/11 cases. v43-soup generates plausible-looking but fabricated source documents."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/STATE_CURRENT_2026_05_12T0805Z.md",
     "lines": "88",
     "quote": "### D13 inference injection: 4/6 = 66.7% DBQ (was 0%)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "187",
     "quote": "every text field in any new corpus must trace to a primary source; LLMs are tools (search/OCR/reformat) not content authors; drop-don't-patch when sources fail."
    }
   ],
   "against": "The injection result rests on 6 items; training the writer on real documents did not stop fabrication (memory/MEMORY.md line 67: 'D13 source-grounded hypothesis falsified.'); stacking documents with extra guidance backfired (memory/BEADS.md line 388: 'PATH G DBQ hybrid D13+curriculum = counterproductive (context overload)').",
   "adds_to_existing": [
    57,
    17,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check that every source's label (which work, who wrote it, when, what kind of document) matches its text, both in generated items and in a source bank before anything is built from it.",
   "kind": "measured",
   "found_by": "Judges failed generated items whose document labels contradicted their content or dates; an audit of the real-source bank found 198 of 436 period tags wrong and several texts that were a different work from the one their label named.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "296",
     "quote": "Document 1 contradicts itself: it is labeled as a manuscript illustration of a dhow but described as a historical map with shaded regions and arrows."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "248",
     "quote": "Several documents are labeled with specific primary-source titles and dates that do not match what the text says"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "72",
     "quote": "F-D13-12 caught 198/436 era misclassifications."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Scan generated items for text aimed at the judge, such as embedded scores, rationales or grading instructions, and void any item that contains it.",
   "kind": "measured",
   "found_by": "The judge voided items whose question content carried an answer key, precomputed scores and score-steering instructions; about 14 such records were found in one item type and the project set a string scrub before any reuse.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "266",
     "quote": "Evaluation voided: integrity_check failed. The content contains embedded evaluation/score data and score-steering instructions."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "448",
     "quote": "Recommended: scrub the training set for any stimulus containing strings like `\"score:\"`, `\"rationale:\"`, `\"part_1_*\"` regex match."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/MEMORY.md",
     "lines": "113",
     "quote": "**Scrub training data of prompt-injection-style stimuli** — F1 found ~14 MCQ_SET records with embedded scoring directives in `stimulus`."
    }
   ],
   "against": "Some integrity voids were the judge's own bug rather than the content (inference_clean.md line 50: 'Known IB v2.4 bug.'; line 64 quotes a code comment that 'Empty stems trigger InceptBench integrity_check false positive').",
   "adds_to_existing": [
    12
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't reword, trim or pad generated content after the fact to satisfy a judge; fix the content itself, because edits made for the judge change the score without improving the item.",
   "kind": "adopted rule",
   "found_by": "An audit of the production pipeline found code that swapped words the judge penalised, deleted evidence that overlapped the sources and padded the gap with generic filler; all were ruled as gaming the measure and slated for removal.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "72",
     "quote": "Rewrites generator output specifically to game the grader. Textbook crutch."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "403",
     "quote": "The post-process scans, deletes overlapping items, and pads with a generic placeholder if cleanup leaves <3. This is the rubric grader literally seeing different content because of the post-process."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "405",
     "quote": "Rewrites the actual text the grader scores. Direct rubric manipulation."
    }
   ],
   "against": "The rule targets edits the judge sees; edits outside its view were kept (inference_clean.md lines 414-415: 'Any post-process that lives outside the grader's view (image gen, logging, transport retry, chat-template normalization) is fine.'), and the later pipeline still dropped candidates that failed validation (PILLARS_2026_05_12.md line 64: '- Stimulus matches /search hit? (else drop)').",
   "adds_to_existing": [
    10
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Generate what was asked: never silently change a requested level, topic or scope to suit the judge, and correct a wrong request where it was made.",
   "kind": "adopted rule",
   "found_by": "The same audit found the service silently raised the requested difficulty for some item types, rewrote one topic and re-picked the time span so items would score better; each was ruled an input mutation that changes what the judge compares the item against.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "74",
     "quote": "Silent input mutation to game the grader. The clean contract honors what the caller asked for."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "75",
     "quote": "Either the benchmark is right (then the model must handle it) or wrong (then fix the benchmark). Not the generator's job."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "410",
     "quote": "The rubric checks `curriculum_alignment` against the time_period the request claims; mutating the period changes what the grader sees vs what was requested."
    }
   ],
   "against": "The mutations existed because some requests were arguably unsuitable (inference_clean.md line 74 quotes the code comment: 'DBQ, LEQ, and SAQ are inherently complex formats — easy is misleading and causes evaluator difficulty_alignment failures').",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Use a judge only on item types it was built for and apply only the criteria that fit each type, because a misapplied criterion manufactures failures and an unsupported type gets scored zero or waved through.",
   "kind": "measured",
   "found_by": "The main judge scored open-response items on wrong-option quality they cannot have (0.071-0.133); a second judge built for one item type scored every other type 0.0; an older judge server passed through or skipped item types it did not support.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/eval_baseline.md",
     "lines": "267",
     "quote": "SAQ has no distractors, so this is an IB grader oddity — it's penalizing SAQ for lacking distractors."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/eval_baseline.md",
     "lines": "97",
     "quote": "Pass an SAQ/LEQ/DBQ in and it falls through the MCQ structural rules and hard-fails on `mcq_wrong_option_count` + `explanation_too_short` — every one scored 0.0 with no useful dimensions."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/eval_baseline.md",
     "lines": "42",
     "quote": "Anything that ran against it for AP types either passed through or was no-oped."
    }
   ],
   "against": "The size of the effect is an estimate (eval_baseline.md line 267: 'Investigate whether the IB rubric should skip distractor_quality for non-MCQ types (probably). If it should skip and isn't, it's contributing ~5 pp of artificial failure.').",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Never compare scores from different judge versions or judge instances; re-score both sides with the same judge and record the judge version with every score.",
   "kind": "measured",
   "found_by": "The same generated items scored 63.64% under one judge version and 89.56% under the next; a model recorded at 90.67% re-scored about 54.7% after a later judge update; the same routed setup scored 70.0% on one judge instance and 62.89% on another.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "186",
     "quote": "Same v29 generations score 63.64% (v2.4.0 endpoint 192.168.1.26:8001) vs 89.56% (v2.5.3 endpoint 192.168.1.10:8001). +25.92pp swing from grader alone, no model change."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_iterative_improvement_not_fresh_models_2026_05_12.md",
     "lines": "81",
     "quote": "The \"v43-soup was 90.67%\" memory entries refer to IB v2.5.3. After grader update, v43-soup is ~54.7%."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/plan.md",
     "lines": "489",
     "quote": "Audit baseline (2026-05-14 s7 single-shot): 70.0% — drift -7.1pp. Likely grader-version delta between IB instances (audit used iCloud local IB; this is 192.168.1.15:8001)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Re-run the baseline in the same session and under the same conditions as the new version rather than comparing against a stored number.",
   "kind": "measured",
   "found_by": "A stored baseline differed from a fresh run of the same model on the same items (0.9475 vs 0.9307) and several 'regressions' reversed once the baseline was regenerated; re-running the baseline with three samples turned two regression claims into ties; versions whose weights never changed were reported 4.4-8.2 points below a stored baseline.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "114",
     "quote": "v29 inference at temp=0 gives DIFFERENT continuous (0.9475 frozen vs 0.9307 fresh) on same prompts/model. Binary same (87.56%). All test configs use fresh gens; baseline must too. Several \"regressions\" reverse to \"real lifts\" with proper baseline."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "184",
     "quote": "Reverses v42/v40h regression framings — both now stat-tied with v29"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/plan.md",
     "lines": "111",
     "quote": "The -4.4 / -5.4 / -8.2pp eval deltas are most likely measurement noise around an essentially-unchanged v80b"
    }
   ],
   "against": "Later practice froze a baseline instead (feedback_test_2_at_a_time_2026_05_12.md line 44: '- Baseline number 56.48% is FROZEN reference; no re-eval needed unless serving drifts'); the snapshot calls the inert-model deltas 'most likely' noise without a fresh re-run of the baseline.",
   "adds_to_existing": [
    34,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Measure the judge's run-to-run spread for each item type and count a difference only when it clears that spread, since long multi-part items vary far more than short ones.",
   "kind": "measured",
   "found_by": "A three-run probe of the judge on unchanged outputs found a 1.54-point spread overall but 7-9 points on the long document-based type, with two short types not varying at all; the same outputs scored 24/30 and 19/30 on two runs; the plan then required the spread across seeds to stay under 4 points before a mean could be read.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "112",
     "quote": "3-run probe: APUSH agg σ=1.54pp, DBQ σ=7-9pp. Win-declaration thresholds per-cell. MCQ/LEQ deterministic."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "197",
     "quote": "Same v29 gens scored to 24/30 vs 19/30 on apush/dbq across runs. ~1-3pp aggregate noise."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/PLAN.md",
     "lines": "279",
     "quote": "**Inter-seed std-dev ≤ 4pp**. If std-dev > 4pp, fire F13 (re-eval 2 additional seeds before branching). High variance means the mean is uninterpretable."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Compare versions on the averaged continuous score as well as the pass rate, because a pass/fail cut turns small score shifts into apparent noise or false gains.",
   "kind": "measured",
   "found_by": "An analysis found the 0.85 pass threshold caused most of the apparent run-to-run variance; a version that gained 1.77 points on pass rate had lost 0.88 on the averaged continuous score, so reports were changed to carry both.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "113",
     "quote": "Switch primary metric from binary pass-rate to averaged-continuous overall. Compass R41: threshold at 0.85 causes most apparent variance. FREE; ~5× sharper. Reveals v36b binary +1.77pp = continuous -0.88; DBQ \"noise\" was ~all threshold artifact."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/v38_decision_rules.md",
     "lines": "11",
     "quote": "Report: aggregate binary pass-rate + aggregate continuous score + per-cell breakdown"
    }
   ],
   "against": "Accepting an item still has to be binary on critical criteria (the judge caps the score when a critical check fails: achieved.md line 133, 'CRITICAL_VETO_CAP=0.84'), and later gates went back to pass rates (PLAN.md line 276: '**Measured:** 3-seed mean K=1 on n=150 IB v2.5.7 standard, T=0.').",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before crediting or blaming a change, confirm it actually took effect in the outputs, and test the difference on the same items with a paired test.",
   "kind": "measured",
   "found_by": "A claimed +1.33-point gain from a self-checking mechanism was within noise on a paired test (p=0.7744) and the mechanism fired in 0 of 297 outputs; a verification scaffold never triggered on 30 of 30 items; reported regressions came from training runs whose weights never moved.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "130",
     "quote": "McNemar p=0.7744 on APUSH (within noise); 0/297 v35 outputs emit any reflection token at decode (Self-RAG mechanism didn't fire)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "180",
     "quote": "CoVe scaffold didn't fire at 14B (30/30 DBQ items `cove_stage=no_block`)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/plan.md",
     "lines": "107",
     "quote": "Across 190 steps and ~5.85M tokens, **DPO extracted zero signal**. The policy never updated."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Audit unexpected wins as closely as losses, because a perfect or record result on a small set is often luck.",
   "kind": "measured",
   "found_by": "A routed setup's 92% rested on one lucky 30/30 run of one item type whose true rate was about 80%; an earlier single-run 'breakthrough' fell 3.78 points below the baseline when re-run with three samples; the project then required audits of unexpected passes.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/PILLARS_2026_05_12.md",
     "lines": "37",
     "quote": "For any cell or arm that PASSED unexpectedly, audit the prompt + generation"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "104",
     "quote": "Original cell-routed 92% used single-pass mcq_set (got lucky 30/30); 3-way eval revealed v43-soup mcq_set true ceiling ~80% under stochastic 3-seed (σ=0.424)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "182",
     "quote": "3-seed mean 0.8289 ± 0.0444, -3.78pp vs v29 outside σ. NOT a promotion candidate. Prior 0.9-class single-run was statistical noise — R8 caught it"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    34,
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Re-test any claimed result on fresh items that took no part in producing or tuning it, and check that the test items don't overlap anything the generator learned from.",
   "kind": "measured",
   "found_by": "A recipe self-reported at 95.56% scored 5/50 on fresh prompts independent of its 30 tuning prompts; a method claimed at 100% scored 45/50 on fresh items with no topic overlap; the plan made an overlap spot-check between test prompts and training data a gate before promotion.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "705",
     "quote": "FAIL: 5/50 = 10.00% on n=50 fresh Unit-1 prompts (independent of den's 30-prompt training set). Delta -85.56pp from den's self-reported 95.56%. Recipe does NOT generalize."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "708",
     "quote": "FAIL: 45/50 = 90.00% on n=50 fresh Unit-1 MCQ from e7e1d980 (no KC overlap with Cheater's 16-KC apush_baseline). -10pp delta from claimed 100%."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/PLAN.md",
     "lines": "280",
     "quote": "**Contamination spot-check passes**. Sample 10 random eval prompts; verify none appear in the 5,927-row audited training corpus. If any match → F14 (poison candidate; do not promote)."
    }
   ],
   "against": "The first data audit had no near-duplicate check between hold-out and training items (data_audit.md line 190: '**No near-dup leakage protection.** This audit does NOT yet de-near-dup against the training pool.').",
   "adds_to_existing": [
    48,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count failures by kind (delivery failure, unreadable output, wrong structure, judge timeout, judged content failure) and never lump them together or drop them silently.",
   "kind": "measured",
   "found_by": "Lumping server errors with parse failures produced a false claim that one version was more brittle; judge timeouts on long outputs made one item type read 13.3% when its true rate was about 45%; excluding generation errors overstated historical pass rates by 10-25 points.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/LESSONS_LEARNED.md",
     "lines": "65",
     "quote": "**Lesson:** Always bucket: parse fail (model output broken) vs transport fail (5xx) vs schema fail (valid JSON, wrong structure). Don't aggregate them."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/STATE_CURRENT_2026_05_12T0805Z.md",
     "lines": "49",
     "quote": "| apush/mcq_set | 20% | 13.3% (TRUE ~45%) | 16.7% | Grader timeout on long outputs; TRUE rate higher |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "452",
     "quote": "If errors are added back, the apparent pass rates fall by another 10-25pp depending on cell."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a run collapses or scores all zeros, check the measuring pipeline (judge connection, output cleaning, score lookup) before blaming the content.",
   "kind": "measured",
   "found_by": "A 0/150 run came from the judge address pointing at a dead machine; a −6.67-point 'drift' came from an output-cleaning pattern that missed the model's tag; a score lookup on the wrong field silently returned 0.0.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "221",
     "quote": "Retraction: bon_decode 0/150 root cause is IB endpoint IP mismatch (.10 vs .17), NOT best_of_n.py"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "109",
     "quote": "The −6.67pp v29 \"drift\" was a stale `strip_think` in `oneshot_generate.py` (matched `<thinking>` long-form only; Qwen3 emits `<think>` short-form)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "101",
     "quote": "Misnested lookup silently returns 0.0; bug hit in oracle rescore script."
    }
   ],
   "against": "A pipeline audit can also come back clean while the drop is real (SESSION_DECISIONS_2026_05_11.md line 29: 'AUDIT-A deployment drift / AUDIT-B grader / AUDIT-C prompt template. All three CLEAN;').",
   "adds_to_existing": [
    36
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every number in a report must trace to the run's own results file, checked in code, and any figure found nowhere in the results is rejected.",
   "kind": "measured",
   "found_by": "An audit found a recorded '73.33% catastrophic' result existed in no evaluation file, and a baseline cited as 90.67% verified at 88.67%; the project added a code check that rejects pass-rate numbers absent from every summary file.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "23",
     "quote": "proved \"73.33% catastrophic\" doesn't exist in any eval file."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_use_claim_validator_before_save.md",
     "lines": "34",
     "quote": "| **R3** | Pass-rate-shaped number (≥2 decimals, 0.40-1.0 or 40-100) NOT in any `summary_*.json` | REJECT | Phantom-number prevention; uses `scripts/grep_claim.sh` |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "213",
     "quote": "(1) v43-soup baseline was 88.67% verified, not 90.67% claimed (state_current marked unverified)"
    }
   ],
   "against": "The code check has false positives on numbers stored in other formats (feedback_use_claim_validator_before_save.md line 88: '## Known false-positive: R3 on 0.9 pass rates').",
   "adds_to_existing": [
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Test a generator on every item type it must produce and accept it on its worst type, with a floor for each, not on its average.",
   "kind": "measured",
   "found_by": "A model reported at 85% had been tested on one item type only; on the full set, about half its outputs of another type failed to parse; the project set the goal as the minimum across item types because an average hides the hardest one.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/NORTH_STAR.md",
     "lines": "24",
     "quote": "We need to win every cell, not the average. Average can hide a regression on the hardest cell."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/OVERNIGHT_RECAP.md",
     "lines": "105",
     "quote": "**v8/v15 numbers were MCQ-only.** v8 was trained on MCQ records only — and on the 10-cell test, **v8's DBQ outputs fail to parse 50% of the time** (13/30 APUSH, 17/30 APWH)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/NORTH_STAR.md",
     "lines": "45",
     "quote": "The mission is the min over 10 cells, not the mean."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    49,
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Decide how much background to give the writer separately for each item type, and add none to items that already carry their own source text.",
   "kind": "measured",
   "found_by": "Retrieved background helped item types without a source text and hurt the types that already had one; a richer context lifted one type 6.7 points and cut another 8.9, washing out in the average; stacking matched documents with extra guidance overloaded the writer.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "198",
     "quote": "RAG-at-decode + curriculum API top-3 helped MCQ/SAQ/LEQ but HURT DBQ + MCQ_SET (which already have stimulus)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "122",
     "quote": "Full 150-item: MCQ +6.7pp REAL LIFT, SAQ -8.9pp REAL REGRESS. Aggregate washes out."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "388",
     "quote": "PATH G DBQ hybrid D13+curriculum = counterproductive (context overload); D13-only at 17%, D13-targeted retrieval at 66.7%"
    }
   ],
   "against": "The overall effect was within noise (memory/MEMORY.md line 198: 'Aggregate +0.67pp / cell-routed +1.33pp APUSH (within noise) but per-cell direction is reusable.'), and the two entries disagree on whether the short-answer type gained (top-3 facts) or lost (richer context).",
   "adds_to_existing": [
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "State the scope's hard limits in every request (time span, unit, what is out of bounds), especially where neighbouring units overlap, and check every part of the item, marking guide included, against them.",
   "kind": "measured",
   "found_by": "Items drifted outside their unit's time span where neighbouring units overlapped, and one unit's pass rate fell from 100% to 43% without a disambiguating line; marking guides listed evidence from after the question's own span; giving the writer the topic's assessment boundaries fixed 5 of 9 persistent failures outright.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "121",
     "quote": "Targeted 9-item probe: assessment_boundaries injection resolves 5 stable APUSH fails outright + 2 improved."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/plans/PLAN-mission-2026-04-26.md",
     "lines": "71",
     "quote": "Without it, APWH u3 dropped 100% → 43% in prior runs."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "233",
     "quote": "as evidence for a prompt limited to 1800-1848, which is chronologically incorrect for this question's time period."
    }
   ],
   "against": "The probe was 9 items, and the boundary notes themselves were model-written (memory/MEMORY.md line 210: 'same record mixes CB-canonical statement with Haiku-generated misconceptions/assessment_boundaries').",
   "adds_to_existing": [
    63,
    58
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Decide what each item in a set will cover before writing any of them, so each tests a different element; left alone, a writer piles every item onto the most salient case.",
   "kind": "measured",
   "found_by": "70-99% of failed question sets failed on coverage and difficulty spread because the writer concentrated every question on one prominent example; the prescribed fix was a planning step listing what each question must cover, with each question locked to a different entry.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "328",
     "quote": "**Manifestation:** ~70-99% of MCQ_SET failures fail `cognitive_demand` (specifically `difficulty_distribution` + `concept_coverage`)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "329",
     "quote": "the Plan step in MCQ_SET generation does not enforce multi-entity coverage. The model picks the most prominent/salient entity in the topic and concentrates there."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "330",
     "quote": "Plan step must enumerate `nations_to_cover: [\"Portugal\", \"Spain\", \"France\", \"England\"]` and Question step must be locked to \"each question MUST address a different nation from this list\" (postmortem prescription)."
    }
   ],
   "against": "The planning fix's effect is not recorded in these files, and the set type stayed the weakest (achieved.md line 14: '- MCQ_SET: 4% (v80b same as v75 — DPO didn't fix; v54 routes for 27%)').",
   "adds_to_existing": [
    41,
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A difficulty label doesn't make an item that hard; build the difficulty into what the item asks and check every item in a set against the set's stated level.",
   "kind": "adopted rule",
   "found_by": "Judges failed sets marked hard that contained items labelled easy and medium; an earlier fix that only injected difficulty labels changed nothing, and the plan recorded difficulty prompts as a minor lever.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/sota_strategy.md",
     "lines": "114",
     "quote": "The hga fix already showed that injecting difficulty *labels* without content variation does nothing."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "204",
     "quote": "The set is marked as 'hard,' but two questions are explicitly labeled 'Easy' and 'Medium,' so the quiz does not match the requested single-difficulty level."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/plans/PLAN-mission-2026-04-26.md",
     "lines": "80",
     "quote": "Minor effect; model learns difficulty implicitly from data."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Draw wrong options from documented misconceptions about the topic.",
   "kind": "adopted rule",
   "found_by": "The project's curriculum source stores about a dozen common misconceptions per topic, and the pipeline design routes them into multiple-choice generation as seeds for wrong options.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_curriculum_api_mandatory_2026_05_11.md",
     "lines": "25",
     "quote": "- `common_misconceptions` — 12 per topic, perfect MCQ distractor candidates"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/PILLARS_2026_05_12.md",
     "lines": "57",
     "quote": "MCQ: misconceptions as distractor seeds + rich context"
    }
   ],
   "against": "Never measured here: the bead meant to test it was bulk-closed (memory/BEADS.md line 386: 'PATH E — Misconceptions-as-MCQ-distractors ... BULK-CLOSE 2026-05-22T15:10Z: Superseded'), and the misconception lists were themselves model-generated (memory/MEMORY.md line 210: 'Haiku-generated misconceptions/assessment_boundaries').",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Record provenance for each field, not each record, because one record can mix verified statements with model-written additions.",
   "kind": "adopted rule",
   "found_by": "An audit of the curriculum source found records whose official statement sat beside model-generated misconceptions and scope notes under one record-level source tag, so the whole source was demoted to reference use.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "210",
     "quote": "Curriculum API merge_source is record-level; same record mixes CB-canonical statement with Haiku-generated misconceptions/assessment_boundaries. Treat curriculum API as retrieval/few-shot reference, NOT direct training data."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    50,
    61
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check that everything an item says its source contains is actually in the source.",
   "kind": "measured",
   "found_by": "A third of one model's failed items (14 of 43) failed because the question or stimulus referred to content the passage did not contain, a failure separate from wrong facts.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/gate1_decision.md",
     "lines": "35",
     "quote": "`passage_reference` failing in 33% of fails is the second pattern: the model writes stimulus passages that reference content the stimulus doesn't actually contain."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "99",
     "quote": "factual_accuracy 32/43 = 74%, passage_reference 14/43 = 33%, clarity_precision 6/43, curriculum_alignment 3/43, others <5%."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    17,
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Forcing a rigid output format while a model writes reasoning-heavy content can lower its quality, so measure the trade-off before switching it on.",
   "kind": "measured",
   "found_by": "Constrained structured decoding dropped a 150-item run from 82.67% to 74.0% (−8.67 points) on a day when none of the failures were format failures; the project's literature review recorded 25-63-point losses on reasoning tasks under strict output modes and set it off by default for free-form items.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/SESSION_DECISIONS_2026_05_11.md",
     "lines": "28",
     "quote": "UPLIFT-3 constrained decode = 74.0% (-8.67pp, Synapse Item 25 predicted), UPLIFT-3b per-cell schema = 84.0% (+1.33pp, within noise)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "150",
     "quote": "JSON mode loses 25-63pp on reasoning tasks; per-cell decision; default OFF for free-form cells."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/FINAL_PLAN_2026_05_11_v3.md",
     "lines": "27",
     "quote": "**Zero parse_fail.** Format-fragility hypothesis is dead."
    }
   ],
   "against": "A benchmark cited in the strategy review reported a small gain (sota_strategy.md line 142: 'Reports ~3% improvement using guidance/constrained decoding.'); the −8.67-point result is a single run, and this bears on output settings rather than on content rules.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Examples shown to a writer teach the form of its output, not correct facts, so facts must come from a verified source, and an example's content can leak into unrelated items.",
   "kind": "adopted rule",
   "found_by": "The project's review concluded that worked examples transfer format and distribution, not facts, so they could not fix fabricated sources and few-shot fixes were ruled out for factual failures; tuning on examples likewise taught structure, not facts; an example from one era carried over into items about a different era.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "154",
     "quote": "ICL works via format/distribution; refutes \"few-shot fixes DBQ veracity\"; lifts mcq_set/saq +3-8pp at K=3 with chat-template-aligned demos."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "314",
     "quote": "Fine-tuning teaches structural patterns, not facts."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/spec_v97_dbq_focused_criterion_grounded_dpo_2026_05_25.md",
     "lines": "153",
     "quote": "v80b's factual reliability on synthetic Unit-1 content is the bottleneck (Civil War few-shot transferred to pre-contact KCs in Cheater v6)."
    }
   ],
   "against": "Examples did lift some item types by 3-8 points on form (memory/MEMORY.md line 154), and the review is cited as three conference papers with no DOI or URL in this file.",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep every generated candidate in the order it was produced, with its score, and compute single-attempt and best-of-several rates by sampling from them, never from a list sorted by score.",
   "kind": "measured",
   "found_by": "Candidate scores were stored sorted best-first, so reading the top of the list reported the best-of-8 rate (99.11%) as a single-attempt rate and as a best-of-2 rate, twice in one day; the actual single-attempt rate that day was 82.67%.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_k8_bon_winner_trap_2026_05_11.md",
     "lines": "7",
     "quote": "The `all_scores` array is sorted DESCENDING by IB score (winner first). Slicing the first N entries gives you the TOP N from the K=8 pool, and the max of that is always `all_scores[0]` = the K=8 winner."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_k8_bon_winner_trap_2026_05_11.md",
     "lines": "36",
     "quote": "On 2026-05-11, orch reported \"B0161 K=2 BoN = 99.11% mean\" computed from existing K=8 data via `max(all_scores[:2])`. This number is identical to K=8 winner pass rate."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/FINAL_PLAN_2026_05_11_v3.md",
     "lines": "24",
     "quote": "**1h ago**: UPLIFT-1 single-seed K=1 T=0 = 82.67% on v43-soup `ty16vgj9`."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    65
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Audit model-made labels, such as 'supported by the source', against an independent check before building on them.",
   "kind": "measured",
   "found_by": "A re-grade of 30 stratified 'supported by the source' labels agreed only 70% overall and 60% on the middle 'partly supported' class, below the project's 90% and 80% bars, which blocked the run built on them; later preference-pair sets required at least 27 of 30 spot-checked pairs to pass.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "133",
     "quote": "Aggregate 70% < 90% \"clean\" bar; partially-class 60% < 80% \"rebuild\" bar."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/plan_v92_pipeline_distillation_single_model_2026_05_22.md",
     "lines": "77",
     "quote": "Done when: ≥27/30 pairs confirmed \"chosen clearly better than rejected on rubric dim\""
    }
   ],
   "against": "The re-grade was itself done by another model, not a person (memory/MEMORY.md line 133: 're-graded 30 stratified IsSup spans from `sftv31_self_rag_train.jsonl` with gemini-3.1-pro-preview vs Quill's gemini-2.5-pro labels').",
   "adds_to_existing": [
    37,
    61
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When items are served from a bank of pre-checked items, report the bank's coverage of fresh requests separately from item quality.",
   "kind": "measured",
   "found_by": "A bank-backed solver passed 37 of 50 fresh requests: every pass was a bank hit and all 13 misses were topics the bank lacked; a bank layer elsewhere delivered 99.7% on the item types it covered.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "714",
     "quote": "37 passes = cache hits; 13 cap_reached = substandards not in cache."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/COMPREHENSIVE_PLAN_v2_2026_06_02.md",
     "lines": "36",
     "quote": "| Layer 1 cache delivers 99.7% IB aggregate (4 of 5 cells) | Cheater 09:50Z delivery |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Fix the bar for a new version before measuring: it must beat what learners currently receive, not one of its parts, by more than the noise margin.",
   "kind": "adopted rule",
   "found_by": "An adversarial review of the plan found its gate compared a candidate with a weaker component rather than the deployed setup, which would have let a noise-band result count as a win; the floor was reset to the deployed baseline plus 2 points, with the noise floor written into the decision rules before results arrived.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/PLAN.md",
     "lines": "447",
     "quote": "Forgetting this lets a 75% noise-band result be promoted as a +0.6pp \"win\" over the actual user-facing baseline."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/PLAN.md",
     "lines": "120",
     "quote": "A \"step-function win\" must beat the deployable, not the component."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/v38_decision_rules.md",
     "lines": "12",
     "quote": "Statistical threshold: σ_floor = 1.54pp (APUSH aggregate from R41 probe)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24,
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Compare versions only on the same frozen set of items, because two sets of the same item type can differ sharply in difficulty.",
   "kind": "measured",
   "found_by": "The same model passed about 20% of one item type on the evaluation set but 0 of 176 attempts on a held-out set of the same type; the evaluation template freezes the hold-out set with a checksum.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/achieved.md",
     "lines": "69",
     "quote": "Root cause: paqpgdst's MCQ_SET pass rate on HOLDOUT prompts is **0%** (0/176 K=3 attempts), vs ~20% on eval baseline. Holdout prompts are systematically harder."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent-v2/templates/eval-cycle.md",
     "lines": "29",
     "quote": "Hold-out set freeze with checksum"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Report the number of items behind every rate and attach no verdict to tiny samples.",
   "kind": "adopted rule",
   "found_by": "Per-type rates from three or four items appeared as 100% or 0% in failure analyses; the memory rules required at least 30 items or repeated runs for top-tier evidence, and a code check rejected verdict words on samples under ten.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "113",
     "quote": "**Tier 1:** n=3, pass=3, fail=0 (100%) — **<5 samples, statistically vacuous.**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "13",
     "quote": "4. T0 evidence requires actual measurement on our data (n ≥ 30 OR multiple confirming runs)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "69",
     "quote": "scripts/validate_claim.sh blocks: R1 (n<10 + verdict word), R3 (phantom number not in summary), R6 (IB-only promotion w/o BAML)."
    }
   ],
   "against": "The project still read one-item differences on 30-item sets as wins (OVERNIGHT_RECAP.md line 95: 'v15 with 174 pairs pushed APUSH from 86.7% → 90%. First evidence DPO works in our regime').",
   "adds_to_existing": [
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Read the judge's actual criteria, weights and caps from its own source before writing content for it or interpreting its scores.",
   "kind": "adopted rule",
   "found_by": "The plan had described the judge as a 5-dimension rubric; reading the judge's source showed 11 metrics, two critical checks at double weight and a cap that holds any item failing a critical check below the pass line; the project then made 'rubric before scoring expectations' a rule for every agent.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/MEMORY.md",
     "lines": "76",
     "quote": "**InceptBench rubric — actual 11 metrics for `question` content type** (correction to the earlier 5-dim claim)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/achieved.md",
     "lines": "133",
     "quote": "Identified BAML/Gemini grader, CRITICAL_VETO_CAP=0.84, critical metrics (factual_accuracy + educational_accuracy 2× weight)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "206",
     "quote": "**Reference for every agent: schema before training rows; rubric before scoring expectations; curriculum before factual claims.**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make each item demand the thinking its objective and level call for, such as explaining or weighing several causes, rather than recall.",
   "kind": "adopted rule",
   "found_by": "Recall-style stems failed the judge's cognitive-demand check and the old pipeline regenerated them; marking guidance that did not require weighing multiple causes failed the difficulty check; the generation rules require analytical stems.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "128",
     "quote": "Use analytical question stems, not recall"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "65",
     "quote": "Cognitive_demand failures on recall stems."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "225",
     "quote": "rubric \"complexity\" guidance fails to require students to weigh multiple causes, undermining the stated difficulty level."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "In a source-based task, the marking guide's examples of outside knowledge must not repeat what the provided sources already say.",
   "kind": "adopted rule",
   "found_by": "The writer listed a provided document's content as 'outside evidence', which the judge treated as a factual failure; the old pipeline patched it by deleting overlaps and padding, which the audit replaced with a rule to produce real outside evidence in the first place.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "69",
     "quote": "LLM sometimes lists Doc 5's content as outside evidence — causes factual_accuracy hard-fails because the evaluator checks for this contradiction"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "403",
     "quote": "Fix in training data — train the model to never list document content as outside evidence."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    56
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make every option accurate in itself and of the same kind and scope as the key, so only the reasoning the question asks for separates them.",
   "kind": "adopted rule",
   "found_by": "The generation rules for multiple-choice items require all four options to be accurate, from the same period and of the same category.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "129",
     "quote": "For MCQ: all 4 options historically accurate, same period, same category"
    }
   ],
   "against": "No measurement in these files, and wrong-option quality was rarely the failing criterion (failure_taxonomy.md line 51: '| 4 | distractor_quality | 1 | 10% | 11% |').",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "An answer explanation must justify the key by the reasoning the question asks for, not by a true but tangential fact.",
   "kind": "measured",
   "found_by": "A judge marked down an item whose explanation justified the key with a fact that was accurate but beside the question's purpose.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "209",
     "quote": "accurate but tangential to the asked purpose, weakening pedagogical clarity."
    }
   ],
   "against": "Single example; the item scored 0.82 and its recorded failing dimension was a side dimension (failure_taxonomy.md line 209: 'score=0.82, failing_dims=`['stimulus_quality']`').",
   "adds_to_existing": [],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/eval_baseline.md",
   "lines": "266",
   "quote": "the IB grader thinks the documents in the DBQ are not \"core/integral\" — i.e. the model emits documents but the prompt could be answered without them."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
   "lines": "46",
   "quote": "Each block traces to a Gate finding (\"Gate 3: 80% of MCQ_SET failures were answer_balance\")."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
   "lines": "72",
   "quote": "Regex-rewrites generator output: `the excerpt → the passage`, `the source → the text`, `Source: → Origin:`."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_pipeline_eval_not_model_eval_2026_05_12.md",
   "lines": "44",
   "quote": "Pipeline output: NEVER MEASURED — eval has been bypassing the wrapper"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/plans/PLAN-mission-2026-04-26.md",
   "lines": "150",
   "quote": "Dep-03  Final canary: 10-cell re-eval through the integrated path"
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
   "lines": "607",
   "quote": "need T1 system-prompt move + T2 post-validation reject + T3 D13 RAG"
  },
  {
   "truth": 30,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
   "lines": "402",
   "quote": "The rubric scores text content; image is a separate channel."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_model_lineage_discipline_2026_05_11.md",
   "lines": "24",
   "quote": "3-seed eval gate before promotion (Synapse Item 12 — single-seed misranks 30%+ of the time)."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/v39_master_record.md",
   "lines": "62",
   "quote": "Single-run 90.67% was misleading — passes 2-3 never ran (deployment destroyed by auto-delete trap)."
  },
  {
   "truth": 34,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
   "lines": "112",
   "quote": "MCQ/LEQ deterministic."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/FINAL_PLAN_2026_05_11_v3.md",
   "lines": "161",
   "quote": "**Risk**: doesn't actually lift past 90.67% — just stabilizes it. Won't hit 97% alone."
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
   "lines": "169",
   "quote": "Quill 7/10 IB calibration PASS (3 fa=0 verdicts are LEGIT grader catches; grader is calibrated even with /curriculums 503)."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/eval_baseline.md",
   "lines": "144",
   "quote": "but the actual generation prompt is gone — we'd have to reconstruct it."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
   "lines": "192",
   "quote": "Every run saves: full per-item raw, run-level metadata (grader version + endpoint + timestamp + model_id + decode params + git_sha), append-only manifest at workspace/eval/runs/MANIFEST.jsonl."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/eval_baseline.md",
   "lines": "318",
   "quote": "so a cross-version comparison would conflate rubric-drift with model-drift."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
   "lines": "209",
   "quote": "484/492 rows have dead URLs"
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
   "lines": "130",
   "quote": "For SAQ: scoring guidance describes criteria, not evidence lists"
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
   "lines": "82",
   "quote": "the model fills `sample_response` and `acceptable_evidence` fields with plausible-sounding but wrong historical examples."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_curriculum_api_mandatory_2026_05_11.md",
   "lines": "9",
   "quote": "IB v2.5.6 grader added DBQ stimulus_quality hard-zero (fabricated docs auto-fail) — and our model was generating BLIND to the source materials the grader checks against. Result: DBQ = 0/89 catastrophic across all v50 seeds."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/plans/PLAN-mission-2026-04-26.md",
   "lines": "59",
   "quote": "Without them, the model hallucinates dates and fails `factual_accuracy`."
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/achieved.md",
   "lines": "133",
   "quote": "Identified BAML/Gemini grader, CRITICAL_VETO_CAP=0.84, critical metrics (factual_accuracy + educational_accuracy 2× weight)."
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/best_approach_analysis.md",
   "lines": "152",
   "quote": "The fix is **stricter dimension-level filters** (filter on `factual_accuracy = 1.0` per failure_taxonomy.md §5 recommendations), not the overall ≥0.95 score."
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
   "lines": "112",
   "quote": "Failure-overlap diagnostic: ZERO row_ids fail in both v8 AND v9 — v9 fixed all 9 v8 fails but introduced 11 new ones."
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/FINAL_PLAN_2026_05_11_v3.md",
   "lines": "29",
   "quote": "**Therefore**: UPLIFT-3 (constrained decode), UPLIFT-3b (per-cell schema), UPLIFT-2 (few-shot) all addressed the wrong failure mode."
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
   "lines": "16",
   "quote": "The postmortem (Apr 24) is explicit that telling the 14B \"no specific facts in scoring notes\" results in *wrong* specific facts."
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
   "lines": "607",
   "quote": "visual-artifact filter in user-prompt ineffective"
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/state_training_chain_2026_05_12T1300Z.md",
   "lines": "52",
   "quote": "26 of 30 failures (87%) flag visual artifact promise/deliver mismatch"
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/state_training_chain_2026_05_12T1300Z.md",
   "lines": "53",
   "quote": "Model promises \"Document 1: [a map of X]\" but only writes prose description"
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
   "lines": "35",
   "quote": "IB flags these as poor stimulus quality since they describe images rather than containing text"
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
   "lines": "63",
   "quote": "38 failing items classified: 76% stochastic variance (decode instability), 13% chronic DBQ veracity fails (Unit 8, D13_docs lever), 5% SFT-forget, 5% systematic fabrication."
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
   "lines": "129",
   "quote": "DBQ remains data-veracity bound — D13 real-source corpus is the unique remaining lever."
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
   "lines": "185",
   "quote": "Goodhart contamination (IB-aggregator → judge says 49% vs IB 92%, 43pp gap)."
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/FINAL_PLAN_2026_05_11_v3.md",
   "lines": "135",
   "quote": "But the \"100% K=8 majority\" headline used IB-judge for both selection and grading — that's the Goodhart trap."
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
   "lines": "75",
   "quote": "IB rated v29 +20pp over v25b — Goodhart-shaped on IB."
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent-v2/ARCHITECTURE.md",
   "lines": "151",
   "quote": "5. **R5 — Verifier independence.** Verifier profile has no write to training pipeline. Period."
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
   "lines": "78",
   "quote": "Validates correct_answer matches answer_options keys, explanation matches answer letter."
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
   "lines": "240",
   "quote": "**Structural failure:** the DBQ has only 4 documents instead of the required 7 (`generated_content.documents` has length 4)."
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
   "lines": "82",
   "quote": "main-A's generic 4-dim prompt missed cell-specific failure modes Oracle's BAML rubric caught — 33pp divergence on SAQ."
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/NORTH_STAR.md",
   "lines": "42",
   "quote": "One change per experiment. Single-variable diffs against v7 baseline."
  },
  {
   "truth": 70,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_anti_regression_opposite_direction_2026_05_11.md",
   "lines": "9",
   "quote": "At most 2 knobs per iteration:"
  }
 ]
}
```
