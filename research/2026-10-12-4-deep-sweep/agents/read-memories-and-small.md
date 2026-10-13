# read:memories-and-small

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "memories-and-small",
 "coverage": {
  "read": [
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/ (AP question-generation project memory bank). Read in full: MEMORY.md, MEMORY_GOVERNANCE.md, mission.md, mission_revised.md, mission_locked_95_aggregate.md, project_dbq_floor_is_data_veracity.md, project_grader_audit_results_2_of_3_pass.md, project_v8_mcq_only.md, project_v8_best.md, project_14b_saturation.md, project_lr_was_too_low.md, project_v20a_lr1e4_result.md, project_v20b_lr2e4_result.md, project_v22_lr1p5e4_result.md, project_v23_modelsoup_result.md, project_v25_dpo_lr_sweep.md, project_v26_soup_regressed.md, project_v27_irpo_v15pairs_result.md, project_v29_new_canonical_external_ib.md, project_v30a_sft_iter2_overfit.md, project_v30b_v18_broader_regressed.md, feedback_no_hallucination_in_training_data.md, feedback_field_level_provenance.md, feedback_oracle_source_reconciliation.md, feedback_curriculum_api_canonical.md, feedback_data_ceiling_not_capacity_ceiling.md, feedback_subagent_skepticism.md, feedback_eval_503_hiccup.md, feedback_verify_eval_infra_first.md, feedback_diagnostic_before_treatment.md, feedback_main_self_discipline_phase_1_2_3.md, feedback_resolve_technical_rulings_locally.md, feedback_shadow_course_checker.md, feedback_doc_snapshot_breadcrumb.md, feedback_ops.md, feedback_proactive_notetaking.md, research_fewshot_format_not_facts.md, research_constrained_decoding_per_cell.md, research_best_of_n_decode.md, research_curriculum_facts_deferred.md, research_grape_data_selection_v28.md, research_parallel_team_takeaways.md, research_best_approach.md, reference_inceptbench.md, reference_curriculum_api_lan.md, reference_oracle_helper.md, reference_teacher_data.md, reference_atlas_helper.md",
   "auto-memory-backup, skimmed or keyword-scanned (training mechanics or operations, nothing about content found): project_dpo_rules.md, project_warm_start_hurts.md, project_lora_chain_works.md, project_v19_qwen3p5.md, research_3stage_chain_max.md, research_dpo_lr_sweep_v24.md, research_grpo_dead_raft_alive.md, research_irpo_from_refined_base.md, research_model_soups_v23.md, research_perplexity_template_probe.md, research_qwen3_chat_template_realign.md, research_qwen3_dense_tops_at_32b.md, reference_shadow_helper.md, reference_multiagent_inbox_outbox.md, reference_session_bootstrap.md, reference_project_state.md, feedback_comms.md, feedback_helper_directives_via_inbox.md, feedback_scale_down_old_deployments.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/meaningful_ai_learning/: sow.txt, script.md (full), crazy-script.md (keyword scan plus the opening and survey-figure lines)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/common-core-resource-aggregator/: README.md, analysis/bottleneck_summary.md, results/resource_summary.txt, inputs/user_instructions.txt, inputs/discovery_config.txt, inputs/README.md and README_quick_start.md (keyword scan), and the quality-scoring code paths in crawlers/pdf_judge_gemini.py, processors/discovery_agent.py, crawlers/batch_quality_scorer.py (targeted reads)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ai_coach/: README.md, outputs/documentation/MASSIVE_LEARNING_RESULTS.md (first 80 lines), AI_COACH_EVOLUTION_REPORT.md, PROFESSIONAL_COACHING_ENHANCEMENT_SUMMARY.md, VISUAL_COACHING_ENHANCEMENT_SUMMARY.md, outputs/backups/README.md, outputs/legacy_files/AI_COACH_ULTIMATE.md (keyword scans for limitations or lessons)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/expertise-inflation-index/: README.md (first 80 lines), methodology.md, docs/testing_guide.md, config/score_prompt_enhanced.txt, plus a grep of src/web_dashboard.py and src/enhanced_analysis.py for how scores are combined"
  ],
  "skipped": [
   "auto-memory-backup/user_[name].md: a personal profile (the task says skip personal material)",
   "auto-memory-backup/reference_sftq_keys.md: a key file (rule: no key or credential files)",
   "auto-memory-backup/feedback_unset_anthropic_key_in_cron.md and feedback_launchd_fda_required.md: credential and cron infrastructure, not content",
   "auto-memory-backup/reference_fireworks_deploy.md, reference_fireworks_models.md, reference_deepseek_models.md, reference_fireworks_dpo_schema.md, reference_sftq_payload.md, reference_qwen3_think_strip.md: vendor and infrastructure reference",
   "All .env, .env.backup and .secrets.baseline files in every folder (rule)",
   "ai_coach data dumps: *.jsonl, *.csv (up to 460 MB), large *.json state files, evolved_coaches/ (1,225 entries), __pycache__/, venv/; also openevolve-btc-algo/ (a trading algorithm, not learning)",
   "common-core-resource-aggregator: venv/, data/, analysis/*.json, *.log files, logs/, tests/, archive/, pdf_downloads/ (empty), crawler and API code beyond the quality-scoring paths",
   "expertise-inflation-index: data/*.json article dumps, n8n/aws/supabase configs, setup and integration docs (api, dynamodb, n8n, linkedin, web dashboard, team competition), TODOs/, screenshots/, the .zip",
   "All .git directories"
  ],
  "notes": "Triage. Only auto-memory-backup holds rich learning-content material: it is the memory bank of an AP question-generation project (five item types across two courses, graded by an automated rubric grader). common-core-resource-aggregator is partly relevant: it collects learning resources, and only its results summary and quality-scoring code bear on judging learning materials. meaningful_ai_learning is a report on workplace AI upskilling with one point about measuring learning. ai_coach (productivity nudges tested on synthetic users) and expertise-inflation-index (satirical scoring of AI articles) hold nothing about learning content.\n\nThings I observed that no source records as a lesson, so they are not candidates:\n(1) In expertise-inflation-index, the synthetic-ethos rubric runs in the opposite direction to the combining code. config/score_prompt_enhanced.txt defines 7-10 as evidence-based, but src/web_dashboard.py line 1132 adds the score to the inflation total at 0.20, and missing scores default to 5 (lines 1129-1130). Its methodology.md also treats agreement between two model judges as reliability and averages them, which is the opposite of truth 35 and is unmeasured.\n(2) In common-core-resource-aggregator, crawlers/pdf_judge_gemini.py line 231 assigns 0.7 ('Reasonable quality assumption') from a URL heuristic, and processors/discovery_agent.py line 375 assigns 0.5 when the judge's reply can't be parsed. Silent defaults like these run against truth 9.\n(3) ai_coach reports 98.75% acceptance and 100% effectiveness on 1,000 users it simulated itself and states no limitations. That is a caution for truth 47 (scripted readers), not a recorded lesson.\n\nCaveats on the memory bank's numbers:\n(a) Each item type has n=30, so one item is 3.3 points. Run-to-run grader noise was never measured: mission_locked_95_aggregate.md line 85 says the grader 'may have lower-bound noise we haven't characterized'.\n(b) The v30b note compares a new score against a score from a grader that the bank had already declared superseded (see candidate on grader switching).\n(c) Many memories cite sub-reports and data under the aptraining repo and a teacher/ folder, which are outside this scope. I could not check those raw numbers.\n\nOther notes:\n- The mission's ban on best-of-N, retries and verifier loops was a product constraint, later relaxed (best-of-4 became Phase 1), so I did not treat it as a lesson.\n- The skepticism memory briefs reviewers of research claims adversarially (feedback_subagent_skepticism.md line 32). That is a different scope from truth 32 (content judges); it may limit 32 but I did not list it as counter-evidence.\n- Quotes contain helper-agent persona names (Quill, Atlas, Compass, Shadow); these are agents, not people. I avoided quotes that name the owner wherever possible. No file I relied on has a person's name in its path."
 },
 "candidates": [
  {
   "statement": "When an item quotes a source attributed to a real author, use the real, cited text: a generated stand-in with a real name and the right structure still fails on fact, and more rounds of the same method don't fix it.",
   "kind": "measured",
   "found_by": "Two very different production methods failed the same source-based items on the same criteria (factual accuracy and source quality). An audit of 50 of the 961 underlying records found perfect structure and real, period-correct attributions, but the quoted text had been produced by a model and was likely fabricated.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "34",
     "quote": "- **36 of those (62%) fail in BOTH** — same items broken across radically different training regimes (SFT-only vs DPO-from-v23)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "47",
     "quote": "- **Document TEXT is unverified.** The teacher generation pipeline (`raft_combined.jsonl`) is itself LLM-produced; the quoted content from real authors is **plausible-but-likely-fabricated**."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "67",
     "quote": "4. Therefore: more iterations (DPO LR sweeps, IRPO) won't move DBQ. Bigger base won't move DBQ. **Replacing fabricated docs with real-sourced docs is the only lever.**"
    }
   ],
   "against": "A later run narrowed the claim: \"This doesn't kill the data-veracity hypothesis — it narrows it. Real-source corpus (D11/D13) is still the path to >50% DBQ. But preference signal alone can deliver +20pp on the floor.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v27_irpo_v15pairs_result.md line 49). No result of the real-source rebuild is recorded in scope, and the plan itself foresaw it might not help: \"- The data-veracity hypothesis is incomplete; revisit.\" (mission_locked_95_aggregate.md line 79, conditional on the pilot failing).",
   "adds_to_existing": [
    17,
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before choosing a fix, check whether the same items fail every time on the same criterion: failures that survive a change of method point to the source material, and only scattered failures are worth attacking by resampling or retuning.",
   "kind": "measured",
   "found_by": "Of 58 items scored under two very different methods, 36 failed under both, and 27 of those 36 failed on the same criteria, even though one method had far more training. A cheap test that sorts failures into consistent or scattered was then required before any expensive fix.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "35",
     "quote": "- **27 of those 36 (75%) fail on the SAME dimensions** — primarily factual_accuracy (18 items) and stimulus_quality (10 items)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "37",
     "quote": "If the bottleneck were optimizer state (LR, epochs, DPO LR), v25b's 1.5 orders of magnitude of additional training steps over v20b would have moved at least the easy items. It didn't. **The bottleneck is invariant to training method.**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_diagnostic_before_treatment.md",
     "lines": "22",
     "quote": "- **Cheap diagnostic queued:** D11 ($2, classifies failure mode as consistent-wrong vs scattered-wrong)."
    }
   ],
   "against": "A third method did move some of these items: \"This is a real contradiction of `project_dbq_floor_is_data_veracity.md`'s \"DBQ is data-veracity bound, only lever is real-source corpus.\" v15 pairs (synthetic, NOT real-source) moved apush/dbq +16.7pp.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v27_irpo_v15pairs_result.md line 45). The result of the consistent-vs-scattered test is not recorded in scope.",
   "adds_to_existing": [
    65,
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Break failures down by criterion on your own items before choosing a fix: a fix aimed at a criterion behind 6–7% of failures can't move a total driven by one behind 56–62%, and that measured breakdown outranks a literature-based guess about the cause.",
   "kind": "measured",
   "found_by": "A literature-backed plan targeted how items cite their source documents. The measured breakdown of failed items (n=58, two methods) put citation problems behind 6–7% of failures and factual accuracy behind 56–62%. The plan's expected lift was cut from +10–18 points to +0–5.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/MEMORY_GOVERNANCE.md",
     "lines": "98",
     "quote": "DBQ failures are 56-62% factual_accuracy + 50-54% stimulus_quality, only 6-7% passage_reference; method-invariant; LLM-fabricated training docs"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/MEMORY_GOVERNANCE.md",
     "lines": "98",
     "quote": "T0 measurement on our data dominates T2 literature inference for OUR scope."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "72",
     "quote": "Self-RAG addresses attribution (6-7% of failures), not memorization (56-62%). Mostly addresses the wrong slice."
    }
   ],
   "against": "The ruling kept part of the literature view: \"Both readings are partially right — Compass's capacity argument is correct (14B has bits) but our training data prevents using them.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/MEMORY_GOVERNANCE.md line 98). The +0–5 point figure is a projection; the probe that would test it is not recorded in scope.",
   "adds_to_existing": [
    49,
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every text in an item set (source text, prompt, model answer, even connecting text) must trace to a cited source; when a fact can't be cited, drop the item rather than patch it with a generated claim.",
   "kind": "adopted rule",
   "found_by": "Adopted after fabricated source text was found behind most factual failures. The project judged that allowing generated text anywhere in a curated set would recreate the same failure.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_no_hallucination_in_training_data.md",
     "lines": "33",
     "quote": "**Drop-don't-patch rule:** if a fact in a candidate record can't be cited to a primary source, the record gets dropped from the corpus, not patched with a synthesized claim."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_no_hallucination_in_training_data.md",
     "lines": "19",
     "quote": "If we curate a \"real-source corpus\" but allow LLM-generated content anywhere in it (gold responses, glue text, paraphrased document text), we recreate the same failure mode. **The point of curation is verified facts; hallucination defeats the purpose.**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_no_hallucination_in_training_data.md",
     "lines": "31",
     "quote": "**LLMs are tools, not authors.** Use them for: search, OCR, structural reformatting. Never for content generation or \"filling gaps\"."
    }
   ],
   "against": "The same project still had a model write items from verified facts and kept the ones that passed the grader: \"- v29 SFT data: pull all KCs per course, generate one MCQ + one SAQ per KC using the bundled scaffolding as the prompt context, IB-grade, keep ≥0.85\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_curriculum_api_lan.md line 85). The rule's stated scope is new training corpora.",
   "adds_to_existing": [
    57,
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Record provenance for each field, not each record: one record can mix official statements with generated fields, and anything that uses the record whole will treat the generated parts as authoritative.",
   "kind": "adopted rule",
   "found_by": "An audit found records under a single source tag whose statements were official but whose misconceptions and scope notes had been filled in by a model, because the official framework doesn't publish them. In one course, 43% of records had at least one generated field.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_field_level_provenance.md",
     "lines": "17",
     "quote": "When a corpus marks provenance at the record level (e.g., `merge_source: inceptbench_remapped`), do **NOT** treat all fields in that record as equally authoritative. Different fields in the same record can have different provenance. A consumer that trains on the record as a unit will train on the LLM-generated fields as if they were authoritative."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_field_level_provenance.md",
     "lines": "12",
     "quote": "The CB CED does not publish assessment_boundaries or common_misconceptions for APEURO; null fields were filled by Haiku-4.5. Record-level merge_source masks this from consumers."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_field_level_provenance.md",
     "lines": "29",
     "quote": "- APUSH (2,703 records): 43% have any LLM-tagged field. **Misconceptions/boundaries/LOs LLM-filled in only 88 records (3%).** date+theme are the dominant LLM-backfill targets."
    }
   ],
   "against": "Generated fields were few, and they were kept as a lower tier rather than dropped: \"- For the LLM-tagged remainder (3%/1%): use as inspiration only, IB-graded as truth-checker\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_field_level_provenance.md line 33).",
   "adds_to_existing": [
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When you anchor items to a standards list or merge two lists, match entries by content and check their IDs against the official framework: IDs can be shifted wholesale, and a wrong ID makes a grader mark correct content as wrong.",
   "kind": "measured",
   "found_by": "A content-similarity comparison of 239 entries from two sources found 224 content matches. 218 of them sat under a different ID, systematically one period off the official framework.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_oracle_source_reconciliation.md",
     "lines": "36",
     "quote": "224 of them have a >= 0.80 content match in the curriculum repo, but 218 of those 224 are at a different ID."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_oracle_source_reconciliation.md",
     "lines": "28",
     "quote": "- **APEURO with InceptBench IDs**: training rows get tagged with KC IDs that are off-by-one-period vs official CB CED. Atlas passes on schema, Quill uses them as anchors, InceptBench grader marks factual_accuracy = 0 even when content is correct, because the KC claim is wrong. Pass rate suffers."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md",
     "lines": "22",
     "quote": "- **Result:** 30/30 records compared via Gemini 2.5 Pro against current published CED PDFs (APUSH / APWH-Modern / APEURO from collegeboard.org)"
    }
   ],
   "against": "The shift was confined to one source: \"- **Critical finding:** **0/10 APEURO records showed off-by-period drift** — the InceptBench APEURO bug (off-by-one-period vs CB CED) did NOT propagate to the canonical API at `192.168.1.26:8002`\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md line 23). The clean source still had a wrong label: \"- 1 wrong_unit: APWH `c_lAtP` Columbian Exchange tagged Unit 0 instead of Unit 4 — single-record fix needed in API\" (line 26).",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Official learning objectives and a bank of cited atomic facts are different levels of the same knowledge; use the objectives as the tagging skeleton and hang the cited facts beneath them, because either alone misses most of what the other holds.",
   "kind": "measured",
   "found_by": "Comparing two sources for one course: 39% of objective-level entries had no match among the facts, and 99.8% of the facts had no match among the objectives. One source alone lost 1,049 cited facts; the other alone lost 838 sub-objective breakdowns with misconceptions.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_oracle_source_reconciliation.md",
     "lines": "44",
     "quote": "The two sets are at different tiers of the CB hierarchy."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_oracle_source_reconciliation.md",
     "lines": "44",
     "quote": "39% of curriculum repo APUSH has no InceptBench match; 99.8% of InceptBench's atomic facts have no curriculum match. **Best path: merge them — use curriculum repo as the canonical tagging skeleton, layer InceptBench's atomic facts as the evidence tier underneath.**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_oracle_source_reconciliation.md",
     "lines": "30",
     "quote": "- **APUSH with either alone**: curriculum-only loses 1,049 atomic facts; InceptBench-only loses 838 sub-KC pedagogical decompositions with common-misconceptions. Single-source halves the pedagogy."
    }
   ],
   "against": "For another course, one source was kept as primary and only backfilled: \"| **APWH** | `helpers/oracle/scoring/evaluator_code/inceptbench_src/curricula/ap/curriculum_facts.json` (APWH-filtered) | Keep InceptBench as primary; backfill ~110 missing + pedagogical attrs (assessment_boundaries, common_misconceptions) from curriculum repo |\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_oracle_source_reconciliation.md line 21). The merge is a plan; no result of it is recorded in scope.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Before trusting a grader's fail verdicts, send it items built from facts known to be correct and check every fail by hand: writing the item can add real errors, and here all 3 fails out of 10 were such errors, correctly caught.",
   "kind": "measured",
   "found_by": "A 10-item calibration run built from known-correct facts returned 7 passes and 3 factual-accuracy fails. Hand-checking showed the 3 items really did contain factual errors introduced while writing them, so the grader was trusted. Until then, no verdict, pass or fail, was acted on.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_curriculum_api_canonical.md",
     "lines": "38",
     "quote": "- **Quill 10-row IB false-negative spot-check** runs immediately to test grader calibration: 10 known-correct facts from the API → MCQ stems → submit to IB → expect 10/10 factual_accuracy=1. Anything less = grader broken."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md",
     "lines": "34",
     "quote": "- **Critical finding:** the 3 factual_accuracy=0 verdicts are **LEGITIMATE grader catches of generator errors** — i.e., the test rows had real factual issues that the grader correctly identified"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_main_self_discipline_phase_1_2_3.md",
     "lines": "62",
     "quote": "**Don't act on a factual_accuracy verdict — positive or negative — until at least Quill's calibration result lands.** That includes interpreting Phase 1 BoN K=4 results."
    }
   ],
   "against": "Only 10 items, and a pending read of the grader's source could still overturn the result: \"- If R29 contradicts Quill (e.g., grader actually fails open with default-PASS): re-eval; this would invalidate Atlas's findings on factual_accuracy=0 verdicts being \"real catches\" since \"real catches\" requires the grader to not default-pass.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md line 42).",
   "adds_to_existing": [
    37,
    39
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When content is tuned or picked against one grader, run an independent check on held-out items beside it, and treat any gain the grader shows beyond that check (here 3 points or more) as gaming, not improvement.",
   "kind": "adopted rule",
   "found_by": "The grader used to pick and train outputs was also the scorer, which the project called the worst case for gaming. A held-out factuality check using a different rubric was set beside it with a fixed alarm gap.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_main_self_discipline_phase_1_2_3.md",
     "lines": "78",
     "quote": "**Goodhart alarm threshold:** IB pass rate ≥3pp ahead of FActScore = we're gaming, not improving."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_best_of_n_decode.md",
     "lines": "19",
     "quote": "**Goodhart risk in our setup:** grader (IB) = training reward. Worst-case configuration. argmax_IB(argmax_IB(...))."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_oracle_helper.md",
     "lines": "51",
     "quote": "Optimize the rubric criteria too aggressively and you'll start passing the grader for the wrong reasons."
    }
   ],
   "against": "No alarm result is recorded in scope. A gap in the other direction was to be read as a possibly over-strict grader, not as a win: \"Unusual. Indicates IB grader is calibrated stricter than FActScore — could be IB rubric drift or our training distribution moving away from IB's stylistic expectations.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_main_self_discipline_phase_1_2_3.md line 128).",
   "adds_to_existing": [
    66,
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Compare only scores from the same grader on the same outputs: moving the same grader code to a different host and reference data shifted scores by −5.0 to +2.7 points and reordered the candidates.",
   "kind": "measured",
   "found_by": "Saved outputs from three candidates were re-scored on a second deployment of the same grader version. Two fell by 5.0 and 4.4 points and one rose by 2.7, which flipped the ranking, and the earlier scores were declared stale. A later note in the same bank still compared a new score with the stale 64.3%.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v29_new_canonical_external_ib.md",
     "lines": "23",
     "quote": "| v25b (DPO from v23) | 64.3% | **59.26%** | -5.0pp |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v29_new_canonical_external_ib.md",
     "lines": "25",
     "quote": "| **v29 (SFT from v25b w/ 988 D9 fact-recall pairs)** | 60.9% | **63.64%** ✓ | **+2.7pp** |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v29_new_canonical_external_ib.md",
     "lines": "50",
     "quote": "- v25b's \"64.3%\" memory is no longer load-bearing — it was on a now-superseded grader."
    }
   ],
   "against": "The cause wasn't isolated: \"Same v2.4.0 codebase but different host, different curriculum dataset, possibly different grading prompts.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v29_new_canonical_external_ib.md line 17). Only three candidates were re-scored.",
   "adds_to_existing": [
    45,
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before reading a failure count as a quality result, split failures by cause: an item lost to a service error was never produced or graded, and counting such items as broken reversed a comparison.",
   "kind": "measured",
   "found_by": "A run showed 24 parse failures against a baseline's 6 and was first recorded as more brittle. 22 of the 24 were service errors; after retrying them, its true count was 2 of 297 against the baseline's 6 of 297.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_eval_503_hiccup.md",
     "lines": "25",
     "quote": "**All 24 of v20a's failures were `http_503`s — deployment infrastructure errors, not model output errors.** v18's 6 failures were genuine `Unterminated string` JSON failures. Apples to oranges."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_eval_503_hiccup.md",
     "lines": "27",
     "quote": "After retry of the 22 503'd prompts (2 of the 24 were JSON failures), v20a's true parse robustness is **2/297 JSON failures**, vs v18's **6/297**. v20a is actually **more** robust at producing valid JSON, not less."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_eval_503_hiccup.md",
     "lines": "32",
     "quote": "- Until then, treat the aggregate pass-rate from a 5xx-contaminated eval as a **lower bound** on the model's true performance."
    }
   ],
   "against": "The record contradicts itself on the count: line 25 says all 24 were service errors, while line 27 says \"(2 of the 24 were JSON failures)\". The first scoring pass silently scored the lost items as zero: \"(Initial pass had 22 records lost to deployment 503s, which scored 0; clean re-score after retry is the real number.)\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v20a_lr1e4_result.md line 17).",
   "adds_to_existing": [
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge a content generator on every item type it must produce: a good score on one type said nothing about another type, about half of whose outputs were unusable.",
   "kind": "measured",
   "found_by": "A generator tuned only on single multiple-choice questions scored 85% on them. On the full set, its outputs for the most complex type (a multi-document task) were unusable about half the time: 13/30 and 17/30 usable.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v8_mcq_only.md",
     "lines": "14",
     "quote": "v8's training data was filtered to MCQ records only (2,821 records, all `question_type=mcq`). When tested on the full 10-cell holdout, v8 produces non-parseable output ~50% of the time on DBQ:"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v8_mcq_only.md",
     "lines": "22",
     "quote": "Single-cell results without the 10-cell context can hide DBQ-style failures."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_ops.md",
     "lines": "20",
     "quote": "- Cell-balance matters: don't optimize one cell while breaking others. Test on the full eval set, not just the one you're working on."
    }
   ],
   "against": "The breakage was concentrated in the most complex type: \"Other untrained types (mcq_set, saq, leq) parse OK 86-100% — they're structurally simpler.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v8_mcq_only.md line 18).",
   "adds_to_existing": [
    49,
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A pass rate at a threshold and a mean score can move in opposite directions; report both, and decide beforehand which one decides.",
   "kind": "measured",
   "found_by": "After one change, the pass rate rose while the mean score fell on 7 of 10 item types: more items cleared the threshold while the near-misses scored lower. The grader's overall scores fall in a few clusters, so mean and pass rate can diverge.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v20a_lr1e4_result.md",
     "lines": "42",
     "quote": "- avg_overall **dropped on 7 of 10 cells** — pass rates went up because more items cleared 0.85, but the \"soft fails\" (0.6-0.84) have lower avg."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_inceptbench.md",
     "lines": "82",
     "quote": "The grader's per-dim binary check + non-critical aggregation lands `overall` in clusters: 0.0/0.30/0.60-0.69/0.75-0.84/0.85-0.99/1.00."
    }
   ],
   "against": "The means were partly dragged down by unproduced items: \"(Numbers above are based on first-pass scoring with 22 503s zeroed out — true v20a aggregate after re-score will be higher.)\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v20a_lr1e4_result.md line 42).",
   "adds_to_existing": [
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A quality cut that nearly every item passes does no filtering; filter on the specific criterion that fails most (such as full marks on factual accuracy), not on an overall or holistic score.",
   "kind": "measured",
   "found_by": "An overall-score cut kept almost the whole pool, since 99.4% was already above it. Separately, a model's holistic quality score put 184 of 185 collected learning resources above 0.7, including 143 of unknown subject and an unrelated thesis page, while 0 of 185 cleared the confidence cut.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_parallel_team_takeaways.md",
     "lines": "21",
     "quote": "| 2 | \"Quality ≥0.95 threshold is near-no-op\" (99.4% of catchup is ≥0.95 anyway) | Our D1 audit found 11,295 ≥0.95 records — corresponds to nearly all of catchup_raw. Filter isn't doing meaningful work. |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_parallel_team_takeaways.md",
     "lines": "71",
     "quote": "2. **Stricter dimension-level filters** instead of overall ≥0.95 — per failure_taxonomy.md, filter `factual_accuracy=1.0` on training records (not just overall ≥0.95). Bigger lift on the dominant failure mode."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/common-core-resource-aggregator/results/resource_summary.txt",
     "lines": "29-30",
     "quote": "HIGH QUALITY RESOURCES (Quality Score > 0.7):\n184"
    }
   ],
   "against": "The first measurement comes from another team's notes, flagged as \"the team work this came from did NOT fully succeed, so claims are filtered through our own evidence\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_parallel_team_takeaways.md line 3). The per-criterion filter was recommended, not measured.",
   "adds_to_existing": [
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Factual errors in generated items cluster on named entities and dates in particular units; find those clusters and fix those units directly instead of regenerating everything.",
   "kind": "measured",
   "found_by": "Comparing short-answer items across two courses found a 23-point factual-accuracy gap concentrated in two units. The errors there were names of laws, treaties and organisations, and dates of events.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_data_ceiling_not_capacity_ceiling.md",
     "lines": "23",
     "quote": "| Quill Q1 (13:30Z): APUSH/SAQ vs APWH/SAQ +23pp factual_accuracy gap, clustered in APUSH unit-6 + unit-8 named entities | Failures aren't broad-distribution; they're surgical: specific units where v18 hallucinated |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v30b_v18_broader_regressed.md",
     "lines": "51",
     "quote": "2. **Quill Q1 (13:30Z):** APUSH/SAQ vs APWH/SAQ +23pp factual_accuracy gap clusters in APUSH unit-6 + unit-8 — model hallucinates named entities (Immigration Act 1882, SALT I, HRC Fund, détente dates)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_data_ceiling_not_capacity_ceiling.md",
     "lines": "59",
     "quote": "- **Surgical interventions in identified hallucination-cluster units** (Quill Q1: APUSH unit-6 Gilded Age, unit-8 Cold War). Curriculum-API rows in these units specifically. Not broad-distribution retrain."
    }
   ],
   "against": "This is one measurement on one item type, read together with others: \"Quill T4 alone could be DBQ-specific; Quill Q1 alone could be SAQ-specific; v30b alone could be soup heuristic violation.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_data_ceiling_not_capacity_ceiling.md line 12).",
   "adds_to_existing": [
    49,
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "More material from an unverified source makes generated content less accurate, not more: volume doesn't dilute wrong content, it adds to it.",
   "kind": "measured",
   "found_by": "A broader retrain on the same unverified corpus scored 58.25%, below the best earlier model. The project concluded that more of that corpus meant more wrong content learned, consistent with its literature-based warning against wholesale ingestion.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_data_ceiling_not_capacity_ceiling.md",
     "lines": "24",
     "quote": "| v30b (15:45Z): 58.25% on broader-v18 retrain (vs v25b 64.3%, -6.05pp) | More v18 = worse, not better. Broader training compounds the wrong content |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v30b_v18_broader_regressed.md",
     "lines": "34",
     "quote": "Instead it regressed below v25b — meaning more v18 = MORE wrong-content learning."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_grape_data_selection_v28.md",
     "lines": "75",
     "quote": "- Don't SFT on all 47K (the \"more of the same flavor\" trap; LIMA-killer)"
    }
   ],
   "against": "The 64.3% baseline came from a grader the bank had already called superseded: \"- v25b's \"64.3%\" memory is no longer load-bearing — it was on a now-superseded grader.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v29_new_canonical_external_ib.md line 50). On the newer grader that model scored 59.26% (same file, line 23), so the stated 6-point drop mixes graders. The per-type breakdown was still awaited (project_v30b_v18_broader_regressed.md line 58).",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Example items shown to a writer transfer form and format, not facts; they can't fix factual errors, which need a verified source.",
   "kind": "external research",
   "found_by": "A literature check, Min et al., Rethinking the Role of Demonstrations, EMNLP 2022 (https://aclanthology.org/2022.emnlp-main.759/), was used to reject the hope that a few verified example items at generation time would fix fabricated content.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_fewshot_format_not_facts.md",
     "lines": "20",
     "quote": "- ICL works because demos show **input distribution + output format**, NOT because they convey correct facts"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_fewshot_format_not_facts.md",
     "lines": "61",
     "quote": "- **Complete examples**, NOT bullet-pointed facts (Min et al.: facts don't transfer; format does)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_fewshot_format_not_facts.md",
     "lines": "76",
     "quote": "- Min et al., *Rethinking the Role of Demonstrations* — EMNLP 2022 (https://aclanthology.org/2022.emnlp-main.759/)"
    }
   ],
   "against": "Magnitudes were not measured on this kind of content: \"medium on magnitude of mcq_set/saq lift (T3 magnitude — no published measurement on AP-history-shaped tasks).\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_fewshot_format_not_facts.md line 12). The planned A/B test is not recorded in scope.",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Forcing strictly structured output can cost a lot on reasoning-heavy free text while helping short classification-like answers; decide per item type, after a small test.",
   "kind": "external research",
   "found_by": "A literature check, Tam et al., Let Me Speak Freely?, EMNLP 2024 Industry Track (https://aclanthology.org/2024.emnlp-industry.91/), overturned a blanket plan to force structured output on every item type.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_constrained_decoding_per_cell.md",
     "lines": "28",
     "quote": "Three of four mainstream models lose 25–63pp on a reasoning task in JSON mode. **This is a capability tax, not a measurement-fairness adjustment.**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_constrained_decoding_per_cell.md",
     "lines": "30",
     "quote": "Same paper shows JSON mode *helps* on classification (Gemini-1.5-Flash 41.6% → 60.3% on DDXPlus). **Direction depends on task.**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_constrained_decoding_per_cell.md",
     "lines": "62",
     "quote": "- [Tam et al., *Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models*, EMNLP 2024 Industry Track](https://aclanthology.org/2024.emnlp-industry.91/)"
    }
   ],
   "against": "Not every model lost: \"| Gemini-1.5-Flash | 89.3% | 89.2% | −0.1pp |\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_constrained_decoding_per_cell.md line 26). Not tested on this content in scope.",
   "adds_to_existing": [
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep evaluation items, including a grader's own reference set and your held-out set, out of everything a writer is shown or trained on, and check for overlap before each use.",
   "kind": "adopted rule",
   "found_by": "The grader's bundled reference set was marked reference-only, because training on it would be direct test contamination. Each new training pool was deduplicated against the held-out set.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_oracle_helper.md",
     "lines": "24",
     "quote": "- `evaluator_code/inceptbench_src/golden/golden_dataset.json` — InceptBench's regression eval set (REFERENCE ONLY; training on these = direct test contamination)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_grape_data_selection_v28.md",
     "lines": "31",
     "quote": "2. Verify zero overlap with the 297-record holdout (dedupe by row_id)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v8_best.md",
     "lines": "18",
     "quote": "- Dataset: 2,821 records — APUSH+APWH MCQ only, `quality_tier=high` (≥0.95), holdout-excluded, no images"
    }
   ],
   "against": "The project's own example-selection plan broke the rule: \"- Demos selected from holdout where IB `overall ≥ 0.95`. Same 3 demos per cell type, locked across evals.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_fewshot_format_not_facts.md line 62).",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Build each item from one official knowledge statement, seed its wrong options from misconceptions recorded for that statement, and give the writer that statement's assessment boundaries so items stay in scope.",
   "kind": "adopted rule",
   "found_by": "A knowledge service holding, for each statement, a list of misconceptions and notes on what should and shouldn't be tested was adopted as the source for writing items. A 454-item pilot built on it averaged 0.96 on the grader among the items kept.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_curriculum_api_lan.md",
     "lines": "72",
     "quote": "- **`common_misconceptions` array = MCQ distractor seeds.** This is the missing piece for our 90%-passing MCQ cells to hit 99%."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_curriculum_api_lan.md",
     "lines": "73",
     "quote": "- **`assessment_boundaries` = scope guard.** Eliminates \"out-of-scope\" generation failures Quill's D8a found."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_data_ceiling_not_capacity_ceiling.md",
     "lines": "58",
     "quote": "Quill v30g pilot 454 rows mean chosen IB 0.96 → on the right track."
    }
   ],
   "against": "The misconception and boundary fields were not always official: \"The CB CED does not publish assessment_boundaries or common_misconceptions for APEURO; null fields were filled by Haiku-4.5. Record-level merge_source masks this from consumers.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_field_level_provenance.md line 12). That boundaries 'eliminate' out-of-scope failures is a claim, not a measurement, and the pilot's 0.96 is the mean of kept items only.",
   "adds_to_existing": [
    58
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check every item of a generated set before using it, not a sample: a 3-item check of 191 items (1.6%) missed that 29% of them had been built on a fallback prompt.",
   "kind": "measured",
   "found_by": "A generated set of 191 items was accepted on a 3-item spot-check. 29% of the items turned out to have been built on a fallback prompt, a fault that polluted the signal. Full-coverage checks became the rule before any such set is used.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_subagent_skepticism.md",
     "lines": "26",
     "quote": "I also accepted Quill's D1 with a 3-sample spot-check on 191 rows (1.6% coverage) and didn't flag the 29% sp_fallback (system-prompt fallback) as a real DPO-signal pollution risk."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_subagent_skepticism.md",
     "lines": "30",
     "quote": "- Before using a subagent artifact in a training run (DPO pairs, F-DPO collection): require full-coverage validation, not spot-checks."
    }
   ],
   "against": "The rule is limited to high-stakes uses: \"- It's not \"block on every claim\". For low-stakes or low-cost claims, fast acceptance is fine. For claims that drive memory entries or training submissions, slow down.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_subagent_skepticism.md line 37). The same file calls the set \"mostly correct\" (line 35).",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write down before each measurement what each possible result will mean and what you'll do (for example, at least +5 points: adopt; +2 points or less: don't), so a result can't be reinterpreted afterwards.",
   "kind": "adopted rule",
   "found_by": "Decision tables with fixed thresholds were written for each pending measurement, so that each result would settle a question rather than hedge it.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_main_self_discipline_phase_1_2_3.md",
     "lines": "110",
     "quote": "| ≥+5pp aggregate over baseline | Ship BoN K=4 as v25b/v29 production decode strategy. Proceed to Phase 2 FLAME. Update HANDOFF. |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_data_ceiling_not_capacity_ceiling.md",
     "lines": "54",
     "quote": "The probe's purpose is to RESOLVE the unknown, not to hedge the bet. Either result is informative."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_main_self_discipline_phase_1_2_3.md",
     "lines": "58",
     "quote": "| Quill 10-row IB grader calibration spot-check (`s-quill-ib-calibration-spot-check-1500`) | 10/10 = trust factual_accuracy verdicts; 8-9/10 = noisy, treat individual verdicts as low-confidence (≥2-row signal required); ≤7/10 = **HALT all training pending IB recovery** |"
    }
   ],
   "against": "A preset threshold was bent once the result arrived: \"- ✅ Quill calibration spot-check: ≤7/10 = HALT (not triggered; 7/10 passed plus 3 are legit catches)\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md line 51). A 7/10 result met the halt rule but was read as a pass after hand-checking.",
   "adds_to_existing": [
    45,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When many trials agree, find what they all share before treating the result as a limit: eleven runs showed the same ceiling because all used one wrong setting, and fixing it broke the ceiling.",
   "kind": "measured",
   "found_by": "Eleven runs plateaued in the same band and were recorded as a ceiling. All eleven shared one mis-set parameter, and the first run with it fixed lifted hard item types sharply, one from 20% to 53%.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/MEMORY_GOVERNANCE.md",
     "lines": "113",
     "quote": "- **\"All 11 experiments saw X, so X is a law.\"** → no. Check the shared confounds (e.g., wrong LR across all 11)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_lr_was_too_low.md",
     "lines": "24",
     "quote": "**v8/v18/v9/v11/v12/v13d/v14a/v15/v16b/v17 all used LR 2e-5.** All experiments tonight are confounded by this mistake."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_14b_saturation.md",
     "lines": "12",
     "quote": "same dataset at LR 1e-4 broke the alleged ceiling on multiple cells (apwh/mcq_set 20→53%, apwh/leq 70→85%). The 11-experiment \"ceiling\" was the LR confound predicted in project_lr_was_too_low.md."
    }
   ],
   "against": "The fix didn't lift everything: \"| apush/mcq_set | 50.0% (0.862) | 36.7% (0.699) | **−13.3pp** |\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v20a_lr1e4_result.md line 26).",
   "adds_to_existing": [
    35,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a judge compares content with an official standard, keep 'more specific than the standard' apart from 'contradicts the standard': in a 30-record audit, 6 objective drifts and 8 statement divergences were the content being more specific, not wrong.",
   "kind": "measured",
   "found_by": "A model judge compared 30 knowledge records with the official framework documents. Its flagged drifts and divergences were reviewed as strictness about more-specific wording; the one real error found was a wrong unit label.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md",
     "lines": "25",
     "quote": "- 20% LO-drift across all three courses (6/30 lo_drift drops) — Gemini was strict on edge cases where API was more specific than CED framework framing; not a factual divergence"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md",
     "lines": "27",
     "quote": "- 8/30 statement_divergence: API more specific than CED; Gemini-strict calls"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md",
     "lines": "67",
     "quote": "20% LO-drift was Gemini-strict — API was more specific than the CED framework on edge cases. NOT a factual divergence; semantic-strictness disagreement."
    }
   ],
   "against": "The 'more specific, not wrong' reading was itself a judgment and was given a low evidence tier: \"Honest tier: T2 for \"API and CED are semantically aligned\"; T3 for \"20% drift is acceptable noise floor for our use case.\"\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md line 67).",
   "adds_to_existing": [
    10
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before committing to an overall quality target, add up each item type's realistic headroom: if the weakest type can't rise far enough, the overall target is out of reach however well the others do.",
   "kind": "measured",
   "found_by": "Per-type arithmetic on measured pass rates showed that even with every other type near its ceiling, the weakest type gave 83.8% at its best-ever rate and 92.9% at 80%. Both fall short of a 95% overall target.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/mission_locked_95_aggregate.md",
     "lines": "44",
     "quote": "**Without solving DBQ:** non-DBQ ceilings at +47, DBQ at all-time-best +11 = **+58 max**. 191 + 58 = **249/297 = 83.8%.** Below bar."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/mission_locked_95_aggregate.md",
     "lines": "46",
     "quote": "**With DBQ at 80% pass rate (24+24=48 vs current 10):** +38 from DBQ + +47 from non-DBQ = +85. **191 + 85 = 276/297 = 92.9%.** Still below bar."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/mission_locked_95_aggregate.md",
     "lines": "52",
     "quote": "DBQ is the structural constraint."
    }
   ],
   "against": "The per-type ceilings were estimates (for example \"maybe 8-10\" more passes, mission_locked_95_aggregate.md line 37), not measurements.",
   "adds_to_existing": [
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Time spent in a learning tool shows exposure, not learning; when time is the target, people keep the tool open to meet it.",
   "kind": "measured",
   "found_by": "An internal survey on workplace AI learning found most respondents doubting that time-in-tool metrics reflect real value. The report described this as people keeping tool windows open to meet the metric.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/meaningful_ai_learning/script.md",
     "lines": "30",
     "quote": "• **Measurement disconnect**: 53% of respondents report \"box-ticking\" behaviors—keeping AI windows open to meet metrics rather than driving value—highlighting the gap between time tracking and impact"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/meaningful_ai_learning/crazy-script.md",
     "lines": "7",
     "quote": "But high adoption without clear competency standards creates a paradox: employees optimize for time-in-tool rather than transformative outcomes."
    }
   ],
   "against": "The sample was weak: \"The 10% survey response rate likely reflects competing priorities and survey fatigue across our organization.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/meaningful_ai_learning/crazy-script.md line 143). The same 53% is elsewhere described as \"53% of employees doubt these metrics capture real business value\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/meaningful_ai_learning/script.md line 7), which is doubt about the metric, not observed box-ticking. This is workplace learning, not lesson content.",
   "adds_to_existing": [
    48,
    51
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Do verified facts help a writer more as structured knowledge (linked entities and relations) than as a flat list? The literature reviewed favours structure, yet flat fact-to-answer pairs still raised scores here.",
   "kind": "open question",
   "found_by": "A literature check deferred feeding flat fact lists to the writer, because the only supporting work relied on structured triples. Separately, a model trained on 988 flat fact-recall pairs became the best on the newer grader.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_curriculum_facts_deferred.md",
     "lines": "23",
     "quote": "1. **No top-tier paper directly endorses the recipe.** Closest is KG-SFT (Knowledge Graph-Driven SFT) which requires structured (entity, relation, fact) triples. Our `curriculum_facts.json` is closer to a flat fact list per the teacher pipeline."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_curriculum_facts_deferred.md",
     "lines": "25",
     "quote": "2. **Mechanism doesn't transfer.** KG-SFT's gain comes from the structure (the explanations are generated from the graph). Without the graph, prepending facts is just prompt-stuffing."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v29_new_canonical_external_ib.md",
     "lines": "27",
     "quote": "External IB grades harsher on most cells but v29's fact-recall training pattern actually scores BETTER on it. Hypothesis: external IB rewards factuality more than format."
    }
   ],
   "against": "The flat pairs leaned toward one item shape, and a second pass on them regressed: \"2. **D9's signal is SAQ-skewed.** When using D9 as training data, mix it with structurally diverse rows or expect SAQ-amplification.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v30a_sft_iter2_overfit.md line 45).",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Examples of a single item shape improve that shape and erode the others; keep the examples a writer learns from varied across every item structure it must produce.",
   "kind": "measured",
   "found_by": "A second training pass on 988 one-question, one-answer examples raised short-answer items by 30 points and dropped a three-questions-per-source type by 36.6 points, a net loss of 9.1 points overall.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v30a_sft_iter2_overfit.md",
     "lines": "21",
     "quote": "The aggregate hides a clear over-specialization pattern:"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v30a_sft_iter2_overfit.md",
     "lines": "38",
     "quote": "D9 has 988 KC-anchored fact-recall pairs that are **single-question SAQ-shaped** (one fact → one short answer). Iter 2 SFT amplified the SAQ-skill while degrading multi-question/multi-stimulus structures (mcq_set = 3 questions per stimulus, leq = long-form essay, dbq = 7-doc analysis)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v30a_sft_iter2_overfit.md",
     "lines": "34",
     "quote": "| **apush/mcq_set** | 53.3% | 16.7% | **-36.6pp** |"
    }
   ],
   "against": "Confounded with repeating the same data: \"1. **SFT chain at full LR doesn't extend from v29 on the same data.** v29 already extracted what D9 had to give.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v30a_sft_iter2_overfit.md line 44). This was a single run.",
   "adds_to_existing": [],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v20b_lr2e4_result.md",
   "lines": "34",
   "quote": "**Pattern: Higher LR lifts the floor, cracks the ceiling.** v20b is more aggressive — it commits harder to regions of input space that the model could already handle marginally (DBQ, hard mcq_sets) but slightly destabilises regions it had nailed (apwh/mcq, the cells where v20a was at 90%+)."
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_warm_start_hurts.md",
   "lines": "18",
   "quote": "- v9 had ZERO failure-overlap with v8 (shuffled the failure surface, didn't shrink it)"
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_best_of_n_decode.md",
   "lines": "24",
   "quote": "- If held-out-judge lift << IB-only lift → we're reward-hacking; back off K"
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_oracle_helper.md",
   "lines": "51",
   "quote": "Per Compass's `research_best_of_n_decode.md`, the mitigation is: hold out ~30 items for an independent judge (Gemini-3-Pro on a non-InceptBench rubric) and confirm gains transfer."
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_shadow_helper.md",
   "lines": "64",
   "quote": "| Type | Judgment-bearing (does this paragraph cite this source faithfully?) | Mechanical (URL resolves, schema valid, hash matches) |"
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_shadow_helper.md",
   "lines": "69",
   "quote": "When in doubt about which helper owns a verification task: if the verdict needs interpretation (\"is this corpus good enough?\"), Shadow. If the verdict is mechanical (\"do all 1000 URLs resolve?\"), Atlas."
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_teacher_data.md",
   "lines": "72",
   "quote": "| **CHOSEN** (≥0.85 + no hard fail) | **408** |"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_teacher_data.md",
   "lines": "52",
   "quote": "\"hard_fail_dimensions\": [],         // dim names that scored 0.0 (drives DPO REJECTED)"
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_inceptbench.md",
   "lines": "82",
   "quote": "The grader's per-dim binary check + non-critical aggregation lands `overall` in clusters: 0.0/0.30/0.60-0.69/0.75-0.84/0.85-0.99/1.00."
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/mission_locked_95_aggregate.md",
   "lines": "33",
   "quote": "| apush/mcq | 29/30 | 1 | at ceiling |"
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/mission_locked_95_aggregate.md",
   "lines": "39",
   "quote": "| apush/mcq_set | 13/30 | 17 | maybe 12-15 |"
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_parallel_team_takeaways.md",
   "lines": "25",
   "quote": "| 6 | MCQ_SET is NOT a data-quantity problem | Pending v18 IB scoring confirms; their v3 had similar all-types coverage and still failed at 18% MCQ_SET |"
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md",
   "lines": "26",
   "quote": "- 1 wrong_unit: APWH `c_lAtP` Columbian Exchange tagged Unit 0 instead of Unit 4 — single-record fix needed in API"
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/common-core-resource-aggregator/results/resource_summary.txt",
   "lines": "8-9",
   "quote": "TOP SUBJECTS:\n  Unknown: 143"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_oracle_helper.md",
   "lines": "12",
   "quote": "8/8 md5 spot-checks matched between source and oracle/."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_curriculum_api_lan.md",
   "lines": "88",
   "quote": "- All generated stems carry `synthesis_provenance: curriculum_api/v0.1.0/<KC>` for Atlas audit"
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_main_self_discipline_phase_1_2_3.md",
   "lines": "62",
   "quote": "**Don't act on a factual_accuracy verdict — positive or negative — until at least Quill's calibration result lands.** That includes interpreting Phase 1 BoN K=4 results."
  },
  {
   "truth": 44,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_shadow_helper.md",
   "lines": "43",
   "quote": "- Verification authority — perform \"human spot-check\" steps; URL verification, sample audits, eval-rubric edge sampling"
  },
  {
   "truth": 29,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_no_hallucination_in_training_data.md",
   "lines": "28",
   "quote": "4. **Gold responses** must come from published Sample Responses, scoring guidelines, or human-written rubric-aligned responses. No LLM-generated gold answers."
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_fewshot_format_not_facts.md",
   "lines": "68",
   "quote": "3. **Demo selection drift**: lock the demo set per cell."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_data_ceiling_not_capacity_ceiling.md",
   "lines": "26",
   "quote": "The model has capacity. It's faithfully learning what's in the corpus. The corpus has wrong content."
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_shadow_course_checker.md",
   "lines": "41",
   "quote": "6. **Cell-coverage drift.** Is one cell sucking attention away from cells closer to target? Worst-cell focus is the mission; aggregate is a side effect."
  }
 ]
}
```
