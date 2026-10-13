# verify:memories-and-small

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "memories-and-small",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim at the cited lines. I removed the clause 'more rounds of the same method don't fix it'. The two runs used different methods, and a third method (preference tuning on synthetic pairs) later moved the same item type by +16.7 points. The claim that the same items fail under both methods also fails a chance check. Among the same 58 items the runs had 42 and about 48 failures, so at least 32 must overlap, and independence predicts about 35. The source found 36. Three things do hold. The stand-in documents had perfect structure and real, period-correct names. Their text was written by a model and never checked. Factual accuracy was the top failure in both runs. This is truth 17 (quote exactly) seen from the failure side, so I keep it only as added evidence. I reworded it to avoid the word 'author'.",
   "statement": "When an item presents a quoted source attributed to a real person, use the real, cited text: model-written stand-ins can have perfect structure and real, period-correct names and still be wrong on fact.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "44",
     "quote": "- 50/50 have exactly 7 documents (100% structural compliance)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "47",
     "quote": "- **Document TEXT is unverified.** The teacher generation pipeline (`raft_combined.jsonl`) is itself LLM-produced; the quoted content from real authors is **plausible-but-likely-fabricated**.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "20",
     "quote": "| **factual_accuracy** | **28** | **56%** |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "27",
     "quote": "| **factual_accuracy** | **26** | **62%** |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_no_hallucination_in_training_data.md",
     "lines": "25",
     "quote": "1. **Document text** must be verbatim or near-verbatim quotation from a citable primary source.",
     "verbatim": true
    }
   ],
   "against": "The fabrication is only 'likely': the audit could not verify the sampled text (project_dbq_floor_is_data_veracity.md line 47). That the factual failures come from the documents, not other parts of the item, is the bank's own inference. A later run without real sources moved the same item type: \"This doesn't kill the data-veracity hypothesis — it narrows it. Real-source corpus (D11/D13) is still the path to >50% DBQ. But preference signal alone can deliver +20pp on the floor.\" (project_v27_irpo_v15pairs_result.md line 49). No result of the real-source rebuild is recorded in scope.",
   "general": true,
   "duplicate_of": "17",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, but the candidate's rule rests on an overlap no better than chance. Among the 58 shared items, v20b failed 42 (16/58 passed) and v25b failed at least 48 (10/60 passed overall). At least 32 shared failures are therefore forced, and independent runs would share 34.8 to 36.2. The source found 36. It never made this comparison and read the overlap as proof that the method made no difference (line 37). I rewrote the statement to the lesson the numbers support. I removed the half saying only scattered failures merit resampling, because it repeats truth 65. Kind changed to calculation.",
   "statement": "Compare a failure overlap between runs with chance before reading it as a pattern: when both runs fail most items, many shared failures are forced. 36 of 58 items failing in both runs was read as proof that the same items fail whatever the method, yet with 42 and about 48 failures among those 58 items at least 32 must overlap and chance alone gives about 35.",
   "kind": "calculation",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "17",
     "quote": "### v25b DBQ (10/60 = 16.7% pass)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "24",
     "quote": "### v20b DBQ (16/58 = 27.6% pass) — different training method, same shape",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "33",
     "quote": "- 58 common DBQ items in both v20b and v25b runs.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "34",
     "quote": "- **36 of those (62%) fail in BOTH** — same items broken across radically different training regimes (SFT-only vs DPO-from-v23).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "37",
     "quote": "If the bottleneck were optimizer state (LR, epochs, DPO LR), v25b's 1.5 orders of magnitude of additional training steps over v20b would have moved at least the easy items. It didn't. **The bottleneck is invariant to training method.**",
     "verbatim": true
    }
   ],
   "against": "The bank also reports that 27 of the 36 shared failures failed on the same criteria (project_dbq_floor_is_data_veracity.md line 35). That figure was not compared with chance either. For factual accuracy it may exceed chance: 18 of the 36 share it, against roughly 35% expected from the per-run shares of 56% and 62%. The planned test that sorts failures into consistent or scattered (feedback_diagnostic_before_treatment.md line 22) has no recorded result.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, and the shares match the per-run tables. On factual accuracy, 28 of 50 and 26 of 42 failed items failed; on passage reference, 3 and 3. 'Can't move a total' overstated a projection; the arithmetic gives only an upper bound, so I reworded it. The n=58 in found_by is the count of shared items; the breakdowns were on 50 and 42 failed items. I replaced the governance quote that says 'method-invariant', which candidate 1 undercuts, with the per-run rows. Related to 49 and 60, not a repeat.",
   "statement": "Break your own items' failures down by criterion before choosing a fix, and size the fix by its criterion's share: fixing a criterion behind 6–7% of failures can recover at most that share while another sits behind 56–62%. A breakdown measured on your own items outranks a literature-based guess about the cause.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "20",
     "quote": "| **factual_accuracy** | **28** | **56%** |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "22",
     "quote": "| passage_reference | 3 | 6% |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "27",
     "quote": "| **factual_accuracy** | **26** | **62%** |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "29",
     "quote": "| passage_reference | 3 | 7% |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_dbq_floor_is_data_veracity.md",
     "lines": "72",
     "quote": "Self-RAG addresses attribution (6-7% of failures), not memorization (56-62%). Mostly addresses the wrong slice.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/MEMORY_GOVERNANCE.md",
     "lines": "98",
     "quote": "T0 measurement on our data dominates T2 literature inference for OUR scope.",
     "verbatim": true
    }
   ],
   "against": "The ruling kept part of the literature view: \"Both readings are partially right — Compass's capacity argument is correct (14B has bits) but our training data prevents using them.\" (MEMORY_GOVERNANCE.md line 98). That the literature fix touches only attribution is itself an assumption. The cut from +10–18 to +0–5 points is a projection, and the mini-probe that would test it is not recorded.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, but the candidate misstates the rule. The rule allows prompts, model answers and connecting text written by hand (feedback_no_hallucination_in_training_data.md lines 27-29), and it covers only new training sets (line 8). Its stricter half, no model-written text anywhere, would contradict truths 29 and 57 for lesson content. I narrowed the statement to the drop-don't-patch rule, which is general and adds a curation step to 57 and 59. Adopted rule; no measured effect.",
   "statement": "When a fact can't be traced to a cited source, drop the item rather than patch the gap with a generated claim.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_no_hallucination_in_training_data.md",
     "lines": "33",
     "quote": "**Drop-don't-patch rule:** if a fact in a candidate record can't be cited to a primary source, the record gets dropped from the corpus, not patched with a synthesized claim.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_no_hallucination_in_training_data.md",
     "lines": "19",
     "quote": "If we curate a \"real-source corpus\" but allow LLM-generated content anywhere in it (gold responses, glue text, paraphrased document text), we recreate the same failure mode. **The point of curation is verified facts; hallucination defeats the purpose.**",
     "verbatim": true
    }
   ],
   "against": "The same project then had a model write items from verified facts and kept those that passed the grader: \"- v29 SFT data: pull all KCs per course, generate one MCQ + one SAQ per KC using the bundled scaffolding as the prompt context, IB-grade, keep ≥0.85\" (reference_curriculum_api_lan.md line 85). No result of applying the rule is recorded in scope.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep",
   "reason": "The quotes are verbatim. The figures 2,703 records, 43% and 88 records (3%) match line 29; the other course was 77% (line 30). The statement is general and supported as an adopted rule backed by a field audit. It extends truth 50 to field level rather than repeating it.",
   "statement": "Record provenance for each field, not each record: one record can mix official statements with generated fields, and anything that uses the record whole will treat the generated parts as authoritative.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_field_level_provenance.md",
     "lines": "17",
     "quote": "When a corpus marks provenance at the record level (e.g., `merge_source: inceptbench_remapped`), do **NOT** treat all fields in that record as equally authoritative. Different fields in the same record can have different provenance. A consumer that trains on the record as a unit will train on the LLM-generated fields as if they were authoritative.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_field_level_provenance.md",
     "lines": "12",
     "quote": "The CB CED does not publish assessment_boundaries or common_misconceptions for APEURO; null fields were filled by Haiku-4.5. Record-level merge_source masks this from consumers.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_field_level_provenance.md",
     "lines": "29",
     "quote": "- APUSH (2,703 records): 43% have any LLM-tagged field. **Misconceptions/boundaries/LOs LLM-filled in only 88 records (3%).** date+theme are the dominant LLM-backfill targets.",
     "verbatim": true
    }
   ],
   "against": "Generated fields were few, and they were kept as a lower tier rather than dropped: \"- For the LLM-tagged remainder (3%/1%): use as inspiration only, IB-graded as truth-checker\" (feedback_field_level_provenance.md line 33). In the other course 77% of records had a generated field, mostly dates and themes (line 30).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, and 239, 224 and 218 match line 36. The claim that a wrong ID 'makes' a grader fail correct content comes from the source's reasoning (line 28) and was never measured, so I softened it to 'can make'. Related to truth 63 (check scope labels), but it adds the rule of matching by content when merging lists.",
   "statement": "When you anchor items to a standards list or merge two lists, match entries by content and check their IDs against the official framework: in one source 218 of 224 content matches sat under a different ID, all shifted by one period of the framework, and a wrong ID can make a grader mark correct content as wrong.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_oracle_source_reconciliation.md",
     "lines": "36",
     "quote": "I checked content Jaccard similarity for all 239 InceptBench APEURO entries.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_oracle_source_reconciliation.md",
     "lines": "36",
     "quote": "224 of them have a >= 0.80 content match in the curriculum repo, but 218 of those 224 are at a different ID.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_oracle_source_reconciliation.md",
     "lines": "36",
     "quote": "**InceptBench's APEURO IDs are off by one period from CB CED.**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_oracle_source_reconciliation.md",
     "lines": "28",
     "quote": "- **APEURO with InceptBench IDs**: training rows get tagged with KC IDs that are off-by-one-period vs official CB CED. Atlas passes on schema, Quill uses them as anchors, InceptBench grader marks factual_accuracy = 0 even when content is correct, because the KC claim is wrong. Pass rate suffers.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md",
     "lines": "22",
     "quote": "- **Result:** 30/30 records compared via Gemini 2.5 Pro against current published CED PDFs (APUSH / APWH-Modern / APEURO from collegeboard.org)",
     "verbatim": true
    }
   ],
   "against": "The shift stayed in one source: \"- **Critical finding:** **0/10 APEURO records showed off-by-period drift** — the InceptBench APEURO bug (off-by-one-period vs CB CED) did NOT propagate to the canonical API at `192.168.1.26:8002`\" (project_grader_audit_results_2_of_3_pass.md line 23). The clean source still had a wrong label: \"- 1 wrong_unit: APWH `c_lAtP` Columbian Exchange tagged Unit 0 instead of Unit 4 — single-record fix needed in API\" (line 26).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, and 39%, 99.8%, 1,049 and 838 match lines 30 and 44. The gap was measured in one course. In another course the two sources mostly matched, so how far apart the levels sit depends on how each source was built. 'Use the objectives as the tagging skeleton' is the source's plan; I kept it as advice, not as a result.",
   "statement": "Learning objectives and a bank of cited atomic facts sit at different levels of the same knowledge; keep both, tagging items to the objectives and attaching the cited facts beneath as evidence, since either source alone can miss most of what the other holds.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_oracle_source_reconciliation.md",
     "lines": "44",
     "quote": "The two sets are at different tiers of the CB hierarchy.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_oracle_source_reconciliation.md",
     "lines": "44",
     "quote": "39% of curriculum repo APUSH has no InceptBench match; 99.8% of InceptBench's atomic facts have no curriculum match. **Best path: merge them — use curriculum repo as the canonical tagging skeleton, layer InceptBench's atomic facts as the evidence tier underneath.**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_oracle_source_reconciliation.md",
     "lines": "30",
     "quote": "- **APUSH with either alone**: curriculum-only loses 1,049 atomic facts; InceptBench-only loses 838 sub-KC pedagogical decompositions with common-misconceptions. Single-source halves the pedagogy.",
     "verbatim": true
    }
   ],
   "against": "In another course one source was kept as primary and backfilled (feedback_oracle_source_reconciliation.md line 21), and there the sources overlapped heavily: \"78% of curriculum repo APWH content is already in InceptBench (with matching CB-format KC IDs).\" (line 40). The merge is a plan with no result in scope, and the analysis covered \"Histories (APUSH, APWH, APEURO) only — non-history AP subjects not analyzed.\" (line 8).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, and 7/10 and 3/10 match project_grader_audit_results_2_of_3_pass.md line 33. 'By hand' is not in the source: a helper agent reported the three fails as real errors, and how they were checked is not recorded in scope. The check assumed that items built from correct facts are themselves correct ('expect 10/10 ... Anything less = grader broken'). The result shows the writing step breaks that assumption, and only the fails were examined. This is truth 37 (score a judged check on person-labelled cases) applied to the finished items; I keep it as added evidence.",
   "statement": "To calibrate a grader, label every finished item, not the facts it was built from, and check its passes as well as its fails: a 10-item check built from known-correct facts and expected to pass 10/10 returned 3 factual fails, which turned out to be real errors added while writing the items.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_curriculum_api_canonical.md",
     "lines": "38",
     "quote": "- **Quill 10-row IB false-negative spot-check** runs immediately to test grader calibration: 10 known-correct facts from the API → MCQ stems → submit to IB → expect 10/10 factual_accuracy=1. Anything less = grader broken.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md",
     "lines": "33",
     "quote": "- **Result:** 7/10 factual_accuracy=1, 3/10 factual_accuracy=0",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md",
     "lines": "34",
     "quote": "- **Critical finding:** the 3 factual_accuracy=0 verdicts are **LEGITIMATE grader catches of generator errors** — i.e., the test rows had real factual issues that the grader correctly identified",
     "verbatim": true
    }
   ],
   "against": "The check had ten items. No check of the seven passes is recorded, so a grader that wrongly passes items would not have shown up. The bank's pending source read was about exactly that: \"- If R29 contradicts Quill (e.g., grader actually fails open with default-PASS): re-eval; this would invalidate Atlas's findings on factual_accuracy=0 verdicts being \"real catches\" since \"real catches\" requires the grader to not default-pass.\" (project_grader_audit_results_2_of_3_pass.md line 42).",
   "general": true,
   "duplicate_of": "37",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "drop",
   "reason": "The quotes are verbatim, but this restates truth 66 (confirm items picked by a judge's score with a check that took no part in picking them). Its only addition is a 3-point alarm gap that never fired and was never tested. The bank's recipe for 66 is already in the evidence for existing truths (research_best_of_n_decode.md line 24).",
   "statement": "When content is tuned or picked against one grader, run an independent check on held-out items beside it, and treat any gain the grader shows beyond that check (here 3 points or more) as gaming, not improvement.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_main_self_discipline_phase_1_2_3.md",
     "lines": "78",
     "quote": "**Goodhart alarm threshold:** IB pass rate ≥3pp ahead of FActScore = we're gaming, not improving.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_best_of_n_decode.md",
     "lines": "19",
     "quote": "**Goodhart risk in our setup:** grader (IB) = training reward. Worst-case configuration. argmax_IB(argmax_IB(...)).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_oracle_helper.md",
     "lines": "51",
     "quote": "Optimize the rubric criteria too aggressively and you'll start passing the grader for the wrong reasons.",
     "verbatim": true
    }
   ],
   "against": "No alarm result is recorded in scope. A gap in the other direction was to be read as a possibly over-strict grader: \"Unusual. Indicates IB grader is calibrated stricter than FActScore — could be IB rubric drift or our training distribution moving away from IB's stylistic expectations.\" (feedback_main_self_discipline_phase_1_2_3.md line 128).",
   "general": true,
   "duplicate_of": "66",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, and −5.0, −4.4 and +2.7 match lines 23-25. The order 64.3 > 60.9 > 57.6 became 63.64 > 59.26 > 53.20. 'On the same outputs' read as if candidates should be compared on identical outputs. I reworded it to say the saved outputs were re-scored and that candidates are compared on one deployment. Related to 45 (fix the rubric before measuring) and 34 (verdicts vary). It adds that the same grader version on another host, with other reference data, is a different instrument.",
   "statement": "Compare candidates only on scores from one grader deployment, and re-score all of them when it changes: the same saved outputs re-scored on a second deployment of the same grader version (another host, other reference data) moved by −5.0, −4.4 and +2.7 points, and the top two swapped places.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v29_new_canonical_external_ib.md",
     "lines": "12",
     "quote": "All three models scored same gen files via the same grader.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v29_new_canonical_external_ib.md",
     "lines": "23",
     "quote": "| v25b (DPO from v23) | 64.3% | **59.26%** | -5.0pp |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v29_new_canonical_external_ib.md",
     "lines": "24",
     "quote": "| v28 (DPO from v25b w/ D5 pairs) | 57.6% | **53.20%** | -4.4pp |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v29_new_canonical_external_ib.md",
     "lines": "25",
     "quote": "| **v29 (SFT from v25b w/ 988 D9 fact-recall pairs)** | 60.9% | **63.64%** ✓ | **+2.7pp** |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v29_new_canonical_external_ib.md",
     "lines": "50",
     "quote": "- v25b's \"64.3%\" memory is no longer load-bearing — it was on a now-superseded grader.",
     "verbatim": true
    }
   ],
   "against": "The cause was not isolated: \"Same v2.4.0 codebase but different host, different curriculum dataset, possibly different grading prompts.\" (project_v29_new_canonical_external_ib.md line 17). Only three candidates were re-scored. Part of the shift may be run-to-run variation. In project_v20a_lr1e4_result.md, the first-pass and clean scores of the same outputs differ on item types with no lost items: apush/leq is about 77% in the line-43 note and 90.0% in the line-24 table. A later note still compared a new score with the stale 64.3% (feedback_data_ceiling_not_capacity_ceiling.md line 24).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, and 24, 6, 22, 2/297 and 6/297 match lines 25-27. 'Never produced or graded' was wrong. The first scoring graded the lost items as zeros (project_v20a_lr1e4_result.md line 17), and that is what made the comparison wrong. Related to truth 9 (a missing verdict is not a miss), but this is about generation, so I kept it separate.",
   "statement": "Before reading failures as a quality result, split them by cause: an item lost to a service error was never produced, so counting it as a failure measures the service, not the content. Counting them reversed a comparison: 24 failures against 6 became 2 against 6 once the lost items were retried.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_eval_503_hiccup.md",
     "lines": "16",
     "quote": "The model never produced output.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_eval_503_hiccup.md",
     "lines": "25",
     "quote": "**All 24 of v20a's failures were `http_503`s — deployment infrastructure errors, not model output errors.** v18's 6 failures were genuine `Unterminated string` JSON failures. Apples to oranges.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_eval_503_hiccup.md",
     "lines": "27",
     "quote": "After retry of the 22 503'd prompts (2 of the 24 were JSON failures), v20a's true parse robustness is **2/297 JSON failures**, vs v18's **6/297**. v20a is actually **more** robust at producing valid JSON, not less.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v20a_lr1e4_result.md",
     "lines": "17",
     "quote": "(Initial pass had 22 records lost to deployment 503s, which scored 0; clean re-score after retry is the real number.)",
     "verbatim": true
    }
   ],
   "against": "The record contradicts itself on the count. Line 25 says all 24 were service errors, while line 27 says \"(2 of the 24 were JSON failures)\". project_v20a_lr1e4_result.md line 41 agrees with 22 and 2.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep",
   "reason": "The quotes are verbatim. The figures 2,821 records, 13/30, 17/30 and 85% match project_v8_mcq_only.md lines 14-20. The point is close to obvious, since the generator was never trained on the failing type. Still, the general rule holds and is not on the list. Related to 49 and 47.",
   "statement": "Judge a content generator on every item type it must produce: a good score on one type said nothing about another type, about half of whose outputs were unusable.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v8_mcq_only.md",
     "lines": "14",
     "quote": "v8's training data was filtered to MCQ records only (2,821 records, all `question_type=mcq`). When tested on the full 10-cell holdout, v8 produces non-parseable output ~50% of the time on DBQ:",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v8_mcq_only.md",
     "lines": "22",
     "quote": "Single-cell results without the 10-cell context can hide DBQ-style failures.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_ops.md",
     "lines": "20",
     "quote": "- Cell-balance matters: don't optimize one cell while breaking others. Test on the full eval set, not just the one you're working on.",
     "verbatim": true
    }
   ],
   "against": "The breakage was concentrated in the most complex type: \"Other untrained types (mcq_set, saq, leq) parse OK 86-100% — they're structurally simpler.\" (project_v8_mcq_only.md line 18).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, but the '7 of 10' claim (line 42) comes from first-pass scoring, in which 22 unproduced items were scored zero. The clean table in the same file (lines 21-32, totalling 175/297) shows the mean falling on only 3 of 10 types. It diverges from the pass rate on 2 of them, one by a single item. I rewrote the statement on the clean figures. 'Fix in advance which one decides' is backed by the fixed 0.85 threshold.",
   "statement": "A pass rate at a threshold and a mean score can move in opposite directions, so report both and fix in advance which one decides: on one item type the pass rate rose from 20.0% to 43.3% while the mean fell from 0.779 to 0.732.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v20a_lr1e4_result.md",
     "lines": "21",
     "quote": "| Cell | v18 | v20a (clean) | Δ |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v20a_lr1e4_result.md",
     "lines": "31",
     "quote": "| apwh/mcq_set | 20.0% (0.779) | 43.3% (0.732) | +23.3pp |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_inceptbench.md",
     "lines": "82",
     "quote": "The grader's per-dim binary check + non-critical aggregation lands `overall` in clusters: 0.0/0.30/0.60-0.69/0.75-0.84/0.85-0.99/1.00.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_inceptbench.md",
     "lines": "82",
     "quote": "Threshold of 0.85 is fixed by mission.",
     "verbatim": true
    }
   ],
   "against": "This is one item type at n=30. The same file's first-pass and clean numbers disagree on types with no lost items: apush/leq is about 77% in the line-43 note and 90.0% in the table. Per-type shifts of a few items may therefore be re-scoring noise.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "drop",
   "reason": "The quotes are verbatim, but the candidate fails on four counts. (1) 'A cut nearly every item passes does no filtering' is true by definition. (2) The per-criterion filter was recommended, never measured, and restates truth 59. (3) The 99.4% figure comes from another team's notes, which the bank files at tier T3 with low confidence (research_parallel_team_takeaways.md lines 6-8). (4) The 184-of-185 figure is not clearly a model's overall judgment. The search engine that supplied 173 of the 185 resources (results/resource_summary.txt line 25) computes its quality score from content length, title and description length and web domain (common-core-resource-aggregator/crawlers/engines/firecrawl_search.py lines 333-367).",
   "statement": "A quality cut that nearly every item passes does no filtering; filter on the specific criterion that fails most (such as full marks on factual accuracy), not on an overall or holistic score.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_parallel_team_takeaways.md",
     "lines": "21",
     "quote": "| 2 | \"Quality ≥0.95 threshold is near-no-op\" (99.4% of catchup is ≥0.95 anyway) | Our D1 audit found 11,295 ≥0.95 records — corresponds to nearly all of catchup_raw. Filter isn't doing meaningful work. |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_parallel_team_takeaways.md",
     "lines": "71",
     "quote": "2. **Stricter dimension-level filters** instead of overall ≥0.95 — per failure_taxonomy.md, filter `factual_accuracy=1.0` on training records (not just overall ≥0.95). Bigger lift on the dominant failure mode.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/common-core-resource-aggregator/results/resource_summary.txt",
     "lines": "29-30",
     "quote": "HIGH QUALITY RESOURCES (Quality Score > 0.7):\n184",
     "verbatim": true
    }
   ],
   "against": "The first measurement is another team's claim: \"the team work this came from did NOT fully succeed, so claims are filtered through our own evidence\" (research_parallel_team_takeaways.md line 3). The per-criterion filter has no measured result.",
   "general": true,
   "duplicate_of": "59",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, and the 23 points and the two units match. The candidate turned one measurement on one item type into 'errors cluster on names and dates'. I restated it as a check to run, with that case as evidence. 'Instead of regenerating everything' recast a retraining choice as item regeneration, so I reworded it. Related to 49 and 60.",
   "statement": "Break factual failures down by unit and by kind of fact before fixing them: errors can concentrate. A 23-point factual-accuracy gap between two courses' short-answer items sat in two units, on names and dates (laws, treaties, organisations, dates of events), which makes those units the target for a direct fix.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_data_ceiling_not_capacity_ceiling.md",
     "lines": "23",
     "quote": "| Quill Q1 (13:30Z): APUSH/SAQ vs APWH/SAQ +23pp factual_accuracy gap, clustered in APUSH unit-6 + unit-8 named entities | Failures aren't broad-distribution; they're surgical: specific units where v18 hallucinated |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v30b_v18_broader_regressed.md",
     "lines": "51",
     "quote": "2. **Quill Q1 (13:30Z):** APUSH/SAQ vs APWH/SAQ +23pp factual_accuracy gap clusters in APUSH unit-6 + unit-8 — model hallucinates named entities (Immigration Act 1882, SALT I, HRC Fund, détente dates)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_data_ceiling_not_capacity_ceiling.md",
     "lines": "59",
     "quote": "- **Surgical interventions in identified hallucination-cluster units** (Quill Q1: APUSH unit-6 Gilded Age, unit-8 Cold War). Curriculum-API rows in these units specifically. Not broad-distribution retrain.",
     "verbatim": true
    }
   ],
   "against": "\"Quill T4 alone could be DBQ-specific; Quill Q1 alone could be SAQ-specific; v30b alone could be soup heuristic violation.\" (feedback_data_ceiling_not_capacity_ceiling.md line 12). This is one measurement, its raw report is outside scope, and the targeted fix has no recorded result.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "drop",
   "reason": "The quotes are verbatim, but the headline drop is measured against a superseded grader's number. v30b (58.25%) was scored after evaluation moved to the new grader; a run earlier the same day was already scored 'n=297 on external IB' (project_v30a_sft_iter2_overfit.md line 12). On that grader the comparison model scored 59.26%, not 64.3% (project_v29_new_canonical_external_ib.md lines 23 and 50), a gap of about 1 point, or 3 items of 297. The run's base model is not stated, so it is unclear whether the right baseline is 63.64%. The measure was the overall pass rate, not factual accuracy. 'Not noise' (project_v30b_v18_broader_regressed.md line 23) was asserted with no noise estimate (mission_locked_95_aggregate.md line 85), and the per-type breakdown was still awaited (line 58). One confounded run can't carry 'volume adds wrong content'. Related to truth 57.",
   "statement": "More material from an unverified source makes generated content less accurate, not more: volume doesn't dilute wrong content, it adds to it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_data_ceiling_not_capacity_ceiling.md",
     "lines": "24",
     "quote": "| v30b (15:45Z): 58.25% on broader-v18 retrain (vs v25b 64.3%, -6.05pp) | More v18 = worse, not better. Broader training compounds the wrong content |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v30b_v18_broader_regressed.md",
     "lines": "34",
     "quote": "Instead it regressed below v25b — meaning more v18 = MORE wrong-content learning.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_grape_data_selection_v28.md",
     "lines": "75",
     "quote": "- Don't SFT on all 47K (the \"more of the same flavor\" trap; LIMA-killer)",
     "verbatim": true
    }
   ],
   "against": "\"- v25b's \"64.3%\" memory is no longer load-bearing — it was on a now-superseded grader.\" (project_v29_new_canonical_external_ib.md line 50); on the newer grader that model scored 59.26% (line 23).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. 'Transfer form and format, not facts' and 'can't fix factual errors' stretch the cited finding. The finding is that wrong labels in demonstrations barely hurt (line 21); it says nothing about facts in generated text. I restated the claim at that strength. It complements truth 57 rather than repeating it.",
   "statement": "Don't count on example items to fix a writer's factual errors: the study cited found that demonstrations work mainly by showing the input and output format (random labels in them barely hurt), so facts have to come from a verified source.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_fewshot_format_not_facts.md",
     "lines": "21",
     "quote": "- Random labels in demos barely hurt performance — the demos function as a format prompt, not a knowledge prompt",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_fewshot_format_not_facts.md",
     "lines": "20",
     "quote": "- ICL works because demos show **input distribution + output format**, NOT because they convey correct facts",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_fewshot_format_not_facts.md",
     "lines": "76",
     "quote": "- Min et al., *Rethinking the Role of Demonstrations* — EMNLP 2022 (https://aclanthology.org/2022.emnlp-main.759/)",
     "verbatim": true
    }
   ],
   "against": "Not measured on this kind of content: \"medium on magnitude of mcq_set/saq lift (T3 magnitude — no published measurement on AP-history-shaped tasks).\" (research_fewshot_format_not_facts.md line 12). The planned A/B test has no recorded result.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 17,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. The 25–63 points matches the table (−25.8, −27.3, −63.1), and 41.6% → 60.3% matches line 30. 'Reasoning-heavy free text' went beyond the study, which measured a maths reasoning set (GSM8K) and a classification set (DDXPlus), so I reworded it. Not a repeat of 29.",
   "statement": "Forcing a strict output format (JSON mode) can cut accuracy sharply on reasoning tasks yet help on classification-like ones; choose per item type and test on a small sample first.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_constrained_decoding_per_cell.md",
     "lines": "28",
     "quote": "Three of four mainstream models lose 25–63pp on a reasoning task in JSON mode. **This is a capability tax, not a measurement-fairness adjustment.**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_constrained_decoding_per_cell.md",
     "lines": "30",
     "quote": "Same paper shows JSON mode *helps* on classification (Gemini-1.5-Flash 41.6% → 60.3% on DDXPlus). **Direction depends on task.**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_constrained_decoding_per_cell.md",
     "lines": "62",
     "quote": "- [Tam et al., *Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models*, EMNLP 2024 Industry Track](https://aclanthology.org/2024.emnlp-industry.91/)",
     "verbatim": true
    }
   ],
   "against": "Not every model lost: \"| Gemini-1.5-Flash | 89.3% | 89.2% | −0.1pp |\" (research_constrained_decoding_per_cell.md line 26). The per-type A/B the bank recommended has no recorded result.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. The evidence covers training only. 'Everything a writer is shown' goes beyond it, and the project's own plan to show held-out items as examples ran the other way, so I narrowed the statement to training data. Distinct from 48, which is about learners.",
   "statement": "Keep evaluation items, including a grader's own reference set and your held-out set, out of a writer's training data, and check for overlap before each training run.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_oracle_helper.md",
     "lines": "24",
     "quote": "- `evaluator_code/inceptbench_src/golden/golden_dataset.json` — InceptBench's regression eval set (REFERENCE ONLY; training on these = direct test contamination)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_grape_data_selection_v28.md",
     "lines": "31",
     "quote": "2. Verify zero overlap with the 297-record holdout (dedupe by row_id)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v8_best.md",
     "lines": "18",
     "quote": "- Dataset: 2,821 records — APUSH+APWH MCQ only, `quality_tier=high` (≥0.95), holdout-excluded, no images",
     "verbatim": true
    }
   ],
   "against": "The project's example-selection plan drew demonstrations from the held-out set: \"- Demos selected from holdout where IB `overall ≥ 0.95`. Same 3 demos per cell type, locked across evals.\" (research_fewshot_format_not_facts.md line 62). Whether it ran is not recorded. No contamination incident or effect is measured in scope.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. The pilot's 0.96 is the grader's mean on items that grader itself chose, so it can't show the recipe works (truth 66); I moved it to against. I added the provenance check because the same bank found misconception fields filled in by a model for one course. This is an adopted plan with no measured result.",
   "statement": "Build each item on one official knowledge statement, draw its wrong options from misconceptions recorded for that statement after checking they were not model-written, and give the writer that statement's scope limits.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_curriculum_api_lan.md",
     "lines": "72",
     "quote": "- **`common_misconceptions` array = MCQ distractor seeds.** This is the missing piece for our 90%-passing MCQ cells to hit 99%.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_curriculum_api_lan.md",
     "lines": "73",
     "quote": "- **`assessment_boundaries` = scope guard.** Eliminates \"out-of-scope\" generation failures Quill's D8a found.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_curriculum_api_lan.md",
     "lines": "85",
     "quote": "- v29 SFT data: pull all KCs per course, generate one MCQ + one SAQ per KC using the bundled scaffolding as the prompt context, IB-grade, keep ≥0.85",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_field_level_provenance.md",
     "lines": "32",
     "quote": "97% of APUSH, 99% of APWH misconceptions are CB-canonical, safe as authoritative distractor seeds",
     "verbatim": true
    }
   ],
   "against": "\"Quill v30g pilot 454 rows mean chosen IB 0.96 → on the right track.\" (feedback_data_ceiling_not_capacity_ceiling.md line 58) is a mean over items the grader picked. \"The CB CED does not publish assessment_boundaries or common_misconceptions for APEURO; null fields were filled by Haiku-4.5. Record-level merge_source masks this from consumers.\" (feedback_field_level_provenance.md line 12). The claims that scope limits 'eliminate' out-of-scope failures and that misconceptions are 'the missing piece' to reach 99% are assertions, not measurements.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, and 3, 191, 1.6% and 29% match line 26. The candidate said the spot-check 'missed' the 29% and that it 'polluted the signal'. The source lists the small sample and the unflagged share as two separate lapses and calls the share a pollution risk, so I reworded it. The rule covers only high-stakes uses (line 37).",
   "statement": "Before a generated set feeds anything that matters, check every item, not a sample: a 3-item spot-check of 191 items (1.6%) was accepted, and a 29% share built on a fallback prompt was not treated as a risk.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_subagent_skepticism.md",
     "lines": "26",
     "quote": "I also accepted Quill's D1 with a 3-sample spot-check on 191 rows (1.6% coverage) and didn't flag the 29% sp_fallback (system-prompt fallback) as a real DPO-signal pollution risk.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_subagent_skepticism.md",
     "lines": "30",
     "quote": "- Before using a subagent artifact in a training run (DPO pairs, F-DPO collection): require full-coverage validation, not spot-checks.",
     "verbatim": true
    }
   ],
   "against": "\"- It's not \"block on every claim\". For low-stakes or low-cost claims, fast acceptance is fine. For claims that drive memory entries or training submissions, slow down.\" (feedback_subagent_skepticism.md line 37). The same file calls the set \"mostly correct\" (line 35).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. 'So a result can't be reinterpreted afterwards' is contradicted by the bank's own record: a 7/10 result met the preset halt rule and was overridden (project_grader_audit_results_2_of_3_pass.md line 51). The rule counted items passing, a stand-in for whether the grader was right, which is why it bent. I rewrote the statement to that lesson. Related to 45 (fix the rubric before measuring).",
   "statement": "Write down before each measurement what each result will mean and what you will do, and define the count on the thing you care about: a preset 'halt at 7/10 or fewer passes' for a grader check came back 7/10 and was overridden once its three fails turned out to be real errors the grader had caught.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_main_self_discipline_phase_1_2_3.md",
     "lines": "58",
     "quote": "| Quill 10-row IB grader calibration spot-check (`s-quill-ib-calibration-spot-check-1500`) | 10/10 = trust factual_accuracy verdicts; 8-9/10 = noisy, treat individual verdicts as low-confidence (≥2-row signal required); ≤7/10 = **HALT all training pending IB recovery** |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_main_self_discipline_phase_1_2_3.md",
     "lines": "110",
     "quote": "| ≥+5pp aggregate over baseline | Ship BoN K=4 as v25b/v29 production decode strategy. Proceed to Phase 2 FLAME. Update HANDOFF. |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_data_ceiling_not_capacity_ceiling.md",
     "lines": "54",
     "quote": "The probe's purpose is to RESOLVE the unknown, not to hedge the bet. Either result is informative.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md",
     "lines": "51",
     "quote": "- ✅ Quill calibration spot-check: ≤7/10 = HALT (not triggered; 7/10 passed plus 3 are legit catches)",
     "verbatim": true
    }
   ],
   "against": "The override may have been right. The three fails were real errors the grader caught (project_grader_audit_results_2_of_3_pass.md line 34), so 7/10 was not the grader failure the rule was meant to detect. No other decision table's outcome is recorded in scope.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. The found_by figure of 20% → 53% is a first-pass number, and the clean table in the source file contradicts it (43.3%). I replaced it with clean figures on the item type the band was measured on: MCQ went from 80.0% to 90.0% and from 76.7% to 93.3%, against a band of 76.7–85.0%. Related to 35 (agreement is consistency, not correctness), but this one is about runs that share a confound.",
   "statement": "When many runs agree on a limit, find what they all share before calling it a limit: eleven runs sat in one band, all with the same mis-set training setting, and the first run with it corrected passed the band.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/MEMORY_GOVERNANCE.md",
     "lines": "113",
     "quote": "- **\"All 11 experiments saw X, so X is a law.\"** → no. Check the shared confounds (e.g., wrong LR across all 11).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_lr_was_too_low.md",
     "lines": "24",
     "quote": "**v8/v18/v9/v11/v12/v13d/v14a/v15/v16b/v17 all used LR 2e-5.** All experiments tonight are confounded by this mistake.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_14b_saturation.md",
     "lines": "15",
     "quote": "The pattern band is tight: every \"useful\" variant lands in [76.7%, 85.0%] aggregate.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v20a_lr1e4_result.md",
     "lines": "25",
     "quote": "| apush/mcq | 80.0% (0.902) | **90.0%** (0.941) | +10.0pp |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v20a_lr1e4_result.md",
     "lines": "30",
     "quote": "| apwh/mcq | 76.7% (0.894) | **93.3%** (0.925) | +16.6pp |",
     "verbatim": true
    }
   ],
   "against": "The fix did not lift everything: \"| apush/mcq_set | 50.0% (0.862) | 36.7% (0.699) | **−13.3pp** |\" (project_v20a_lr1e4_result.md line 26). The band came from runs scored on the 60 MCQ prompts, mostly trained on MCQ only, while the corrected run was trained on all types. The list of runs at the wrong setting names ten, not eleven, and one of them used 1.5e-5 (project_lr_was_too_low.md lines 24 and 31).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, and 6/30 and 8/30 match lines 25 and 27. The candidate stated the review's reading as fact, but the bank rates that reading T2/T3 (line 67), so I reworded it to 'read on review'. This is truth 10 (mark meaning, not wording) in a new setting; I keep it as added evidence.",
   "statement": "When a judge compares content with an official standard, separate 'more specific than the standard' from 'contradicts it': in a 30-record audit, 6 objective drifts and 8 statement divergences were read on review as the content being more specific, not wrong.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md",
     "lines": "25",
     "quote": "- 20% LO-drift across all three courses (6/30 lo_drift drops) — Gemini was strict on edge cases where API was more specific than CED framework framing; not a factual divergence",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md",
     "lines": "27",
     "quote": "- 8/30 statement_divergence: API more specific than CED; Gemini-strict calls",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md",
     "lines": "67",
     "quote": "20% LO-drift was Gemini-strict — API was more specific than the CED framework on edge cases. NOT a factual divergence; semantic-strictness disagreement.",
     "verbatim": true
    }
   ],
   "against": "\"Honest tier: T2 for \"API and CED are semantically aligned\"; T3 for \"20% drift is acceptable noise floor for our use case.\"\" (project_grader_audit_results_2_of_3_pass.md line 67). The reading is a helper agent's, and the raw verdicts are outside scope.",
   "general": true,
   "duplicate_of": "10",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim and the arithmetic checks: 191 + 58 = 249 (83.8%) and 191 + 85 = 276 (92.9%), against 282 needed (line 19). I changed the kind from measured to calculation: the inputs are measured pass rates, but the ceilings are guesses. The conclusion holds even at the top of the guesses.",
   "statement": "Before committing to an overall target, add up each item type's realistic headroom: with every other type near its ceiling, the weakest type at its best-ever rate gave 83.8% overall and at 80% gave 92.9%, both short of a 95% target.",
   "kind": "calculation",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/mission_locked_95_aggregate.md",
     "lines": "44",
     "quote": "**Without solving DBQ:** non-DBQ ceilings at +47, DBQ at all-time-best +11 = **+58 max**. 191 + 58 = **249/297 = 83.8%.** Below bar.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/mission_locked_95_aggregate.md",
     "lines": "46",
     "quote": "**With DBQ at 80% pass rate (24+24=48 vs current 10):** +38 from DBQ + +47 from non-DBQ = +85. **191 + 85 = 276/297 = 92.9%.** Still below bar.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/mission_locked_95_aggregate.md",
     "lines": "52",
     "quote": "DBQ is the structural constraint.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/mission_locked_95_aggregate.md",
     "lines": "19",
     "quote": "Operationally: **282 of 297 prompts must pass.**",
     "verbatim": true
    }
   ],
   "against": "The per-type ceilings are estimates (\"maybe 8-10\", mission_locked_95_aggregate.md line 37). The +47 for the other types sits inside the 41–52 range the table implies. Even at 52, with the weakest type at 80%, the total is 281, one short of 282.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 25,
   "verdict": "drop",
   "reason": "The quotes are verbatim, but the same 53% is described four incompatible ways. It is people who 'report box-ticking behaviors' (script.md line 30), who 'doubt these metrics capture real business value' (line 7), who 'disagree that current metrics capture business impact' (line 16), and who are 'unsure if their AI use creates real value' (crazy-script.md line 7). Only the box-ticking reading supports the claimed behaviour; the other three describe an opinion about the metric. The sample was the 10% who answered, and the report itself says they 'aren't a representative sample' (crazy-script.md line 145). The subject is workplace AI-tool use, not learning content.",
   "statement": "Time spent in a learning tool shows exposure, not learning; when time is the target, people keep the tool open to meet it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/meaningful_ai_learning/script.md",
     "lines": "30",
     "quote": "• **Measurement disconnect**: 53% of respondents report \"box-ticking\" behaviors—keeping AI windows open to meet metrics rather than driving value—highlighting the gap between time tracking and impact",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/meaningful_ai_learning/crazy-script.md",
     "lines": "7",
     "quote": "But high adoption without clear competency standards creates a paradox: employees optimize for time-in-tool rather than transformative outcomes.",
     "verbatim": true
    }
   ],
   "against": "\"The 10% survey response rate likely reflects competing priorities and survey fatigue across our organization.\" (crazy-script.md line 143); \"53% of employees doubt these metrics capture real business value\" (script.md line 7).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "drop",
   "reason": "The quotes are verbatim, but the evidence doesn't bear on the question. The deferred recipe put facts into training prompts, and the measured case trained on fact-to-answer pairs. Neither compares structured with flat facts, and neither concerns a writer's prompt. The literature note records only that no paper endorses flat facts and that one method built on a knowledge graph credits the graph for its gains, which is not a comparison. The one positive run was +4.4 points over one model on one grader, with noise unmeasured. Repeating training on the same pairs then cost 9.1 points (project_v30a_sft_iter2_overfit.md line 17).",
   "statement": "Do verified facts help a writer more as structured knowledge (linked entities and relations) than as a flat list? The literature reviewed favours structure, yet flat fact-to-answer pairs still raised scores here.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_curriculum_facts_deferred.md",
     "lines": "23",
     "quote": "1. **No top-tier paper directly endorses the recipe.** Closest is KG-SFT (Knowledge Graph-Driven SFT) which requires structured (entity, relation, fact) triples. Our `curriculum_facts.json` is closer to a flat fact list per the teacher pipeline.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_curriculum_facts_deferred.md",
     "lines": "25",
     "quote": "2. **Mechanism doesn't transfer.** KG-SFT's gain comes from the structure (the explanations are generated from the graph). Without the graph, prepending facts is just prompt-stuffing.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v29_new_canonical_external_ib.md",
     "lines": "27",
     "quote": "External IB grades harsher on most cells but v29's fact-recall training pattern actually scores BETTER on it. Hypothesis: external IB rewards factuality more than format.",
     "verbatim": true
    }
   ],
   "against": "\"2. **D9's signal is SAQ-skewed.** When using D9 as training data, mix it with structurally diverse rows or expect SAQ-amplification.\" (project_v30a_sft_iter2_overfit.md line 45).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "drop",
   "reason": "The quotes are verbatim, but the measured pattern doesn't fit the claim. The same short-answer shape rose 30.0 points in one course and fell 33.3 in the other (project_v30a_sft_iter2_overfit.md lines 25 and 33), so 'improves that shape' fails half the time. The run repeated training on pairs the model had already been trained on (line 44), so over-training is the simpler explanation. It was one run at n=30 per type. Elsewhere in the bank, re-scoring identical outputs moved a type by several items.",
   "statement": "Examples of a single item shape improve that shape and erode the others; keep the examples a writer learns from varied across every item structure it must produce.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v30a_sft_iter2_overfit.md",
     "lines": "21",
     "quote": "The aggregate hides a clear over-specialization pattern:",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v30a_sft_iter2_overfit.md",
     "lines": "38",
     "quote": "D9 has 988 KC-anchored fact-recall pairs that are **single-question SAQ-shaped** (one fact → one short answer). Iter 2 SFT amplified the SAQ-skill while degrading multi-question/multi-stimulus structures (mcq_set = 3 questions per stimulus, leq = long-form essay, dbq = 7-doc analysis).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v30a_sft_iter2_overfit.md",
     "lines": "34",
     "quote": "| **apush/mcq_set** | 53.3% | 16.7% | **-36.6pp** |",
     "verbatim": true
    }
   ],
   "against": "\"1. **SFT chain at full LR doesn't extend from v29 on the same data.** v29 already extracted what D9 had to give.\" (project_v30a_sft_iter2_overfit.md line 44); \"| apwh/saq | 83.3% | 50.0% | -33.3pp |\" (line 33).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 60,
   "effect": "supports, weakly: the per-type drops behind this reading are 1–3 items, within the re-scoring variation seen elsewhere in the bank",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v20b_lr2e4_result.md",
   "lines": "34",
   "quote": "**Pattern: Higher LR lifts the floor, cracks the ceiling.** v20b is more aggressive — it commits harder to regions of input space that the model could already handle marginally (DBQ, hard mcq_sets) but slightly destabilises regions it had nailed (apwh/mcq, the cells where v20a was at 90%+).",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_warm_start_hurts.md",
   "lines": "18",
   "quote": "- v9 had ZERO failure-overlap with v8 (shuffled the failure surface, didn't shrink it)",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_best_of_n_decode.md",
   "lines": "24",
   "quote": "- If held-out-judge lift << IB-only lift → we're reward-hacking; back off K",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_oracle_helper.md",
   "lines": "51",
   "quote": "Per Compass's `research_best_of_n_decode.md`, the mitigation is: hold out ~30 items for an independent judge (Gemini-3-Pro on a non-InceptBench rubric) and confirm gains transfer.",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_shadow_helper.md",
   "lines": "64",
   "quote": "| Type | Judgment-bearing (does this paragraph cite this source faithfully?) | Mechanical (URL resolves, schema valid, hash matches) |",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_shadow_helper.md",
   "lines": "69",
   "quote": "When in doubt about which helper owns a verification task: if the verdict needs interpretation (\"is this corpus good enough?\"), Shadow. If the verdict is mechanical (\"do all 1000 URLs resolve?\"), Atlas.",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_teacher_data.md",
   "lines": "72",
   "quote": "| **CHOSEN** (≥0.85 + no hard fail) | **408** |",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_teacher_data.md",
   "lines": "52",
   "quote": "\"hard_fail_dimensions\": [],         // dim names that scored 0.0 (drives DPO REJECTED)",
   "ok": true
  },
  {
   "truth": 31,
   "effect": "unclear: describes a grader built this way, not whether that works; another record in the bank shows non-binary dimension scores (reference_teacher_data.md lines 54-56)",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_inceptbench.md",
   "lines": "82",
   "quote": "The grader's per-dim binary check + non-critical aggregation lands `overall` in clusters: 0.0/0.30/0.60-0.69/0.75-0.84/0.85-0.99/1.00.",
   "ok": false
  },
  {
   "truth": 68,
   "effect": "does not bear: 29/30 single questions against 13/30 shared-source sets is a far bigger gap than compounding single-question errors predicts (0.967^3 ≈ 0.90), and the bank attributes set failures to shape and distractors, not to shared-source errors",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/mission_locked_95_aggregate.md",
   "lines": "33",
   "quote": "| apush/mcq | 29/30 | 1 | at ceiling |",
   "ok": false
  },
  {
   "truth": 68,
   "effect": "does not bear: see the line-33 entry; a low set pass rate alone doesn't show a shared-source mechanism",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/mission_locked_95_aggregate.md",
   "lines": "39",
   "quote": "| apush/mcq_set | 13/30 | 17 | maybe 12-15 |",
   "ok": false
  },
  {
   "truth": 68,
   "effect": "does not bear: says set failures are not a data-quantity problem; nothing about distinct elements in a shared source",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_parallel_team_takeaways.md",
   "lines": "25",
   "quote": "| 6 | MCQ_SET is NOT a data-quantity problem | Pending v18 IB scoring confirms; their v3 had similar all-types coverage and still failed at 18% MCQ_SET |",
   "ok": false
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md",
   "lines": "26",
   "quote": "- 1 wrong_unit: APWH `c_lAtP` Columbian Exchange tagged Unit 0 instead of Unit 4 — single-record fix needed in API",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "does not bear: shows missing subject labels; the score that passed these resources was a length-and-domain heuristic (crawlers/engines/firecrawl_search.py lines 333-367), not a judge checking labels",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/common-core-resource-aggregator/results/resource_summary.txt",
   "lines": "8-9",
   "quote": "TOP SUBJECTS:\n  Unknown: 143",
   "ok": false
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_oracle_helper.md",
   "lines": "12",
   "quote": "8/8 md5 spot-checks matched between source and oracle/.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports (source recorded, no hash; a plan)",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_curriculum_api_lan.md",
   "lines": "88",
   "quote": "- All generated stems carry `synthesis_provenance: curriculum_api/v0.1.0/<KC>` for Atlas audit",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_main_self_discipline_phase_1_2_3.md",
   "lines": "62",
   "quote": "**Don't act on a factual_accuracy verdict — positive or negative — until at least Quill's calibration result lands.** That includes interpreting Phase 1 BoN K=4 results.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "not counter-evidence: shows an agent assigned the 'human spot-check' steps, with no result on whether its checks matched human judgment",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/reference_shadow_helper.md",
   "lines": "43",
   "quote": "- Verification authority — perform \"human spot-check\" steps; URL verification, sample audits, eval-rubric edge sampling",
   "ok": false
  },
  {
   "truth": 29,
   "effect": "limits: in a curated set of verified facts, even free text such as model answers is kept free of model writing",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_no_hallucination_in_training_data.md",
   "lines": "28",
   "quote": "4. **Gold responses** must come from published Sample Responses, scoring guidelines, or human-written rubric-aligned responses. No LLM-generated gold answers.",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/research_fewshot_format_not_facts.md",
   "lines": "68",
   "quote": "3. **Demo selection drift**: lock the demo set per cell.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports (the bank's diagnosis; one of its three supporting measurements was compared against a superseded grader's number)",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_data_ceiling_not_capacity_ceiling.md",
   "lines": "26",
   "quote": "The model has capacity. It's faithfully learning what's in the corpus. The corpus has wrong content.",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/feedback_shadow_course_checker.md",
   "lines": "41",
   "quote": "6. **Cell-coverage drift.** Is one cell sucking attention away from cells closer to target? Worst-cell focus is the mission; aggregate is a side effect.",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports, by inference (added by the verifier). This first-pass note puts apush/leq near 77% on a type with no lost items, while the clean table, which re-scored the same outputs, gives 90.0% (line 24). apwh/mcq_set likewise falls from +33pp over 20.0% (line 38) to 43.3% (line 31), a drop that retrying lost items cannot cause. The file gives no reason.",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/auto-memory-backup/project_v20a_lr1e4_result.md",
   "lines": "43",
   "quote": "This regression is real even after fixing 503s — it's measured on the cells with 0 503s.",
   "ok": true
  }
 ]
}
```
