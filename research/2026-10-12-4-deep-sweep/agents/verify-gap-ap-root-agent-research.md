# verify:gap:ap-root-agent-research

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "ap-root-agent-research",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "Indices are 0-based positions in the reader's candidate list. The quotes check out at the cited lines and the numbers match. The original said to report the single-attempt rate 'as its quality'. But when the delivered pipeline itself selects, the aided rate is what learners get (truth 24), so the fix reports the two rates separately. I dropped the reader's eval_baseline.md line 243 quote ('~70 pp of inference-crutch lift', 83.3% vs 13.3%) because it compares a different model on a different grader and server. In its place: the same-model estimate (failure_taxonomy.md line 382) and the standing rule (memory/MEMORY.md line 194). Not a duplicate: 65 is about what selection can fix, 66 about confirming selected items. Safety note for the merge: eval_baseline.md also has a plaintext key at line 38 (section 1.1), outside the sections the reader listed. Quote nothing from lines 36-40.",
   "statement": "Report a generator's single-attempt pass rate, with no retries, selection or after-the-fact filters, apart from any rate reached with those aids; the aids can add tens of points and hide failures such as cut-off outputs.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "352",
     "quote": "Aggregate APUSH+APWH for these two N=30 runs: **52% (clean) → 86% (+crutch) = +34pp**.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "382",
     "quote": "**Crutch-inflation summary:** the 83.3% headline on sft-v4-14b BoN+2bi is roughly **34-50pp inflated** over clean one-shot when you average across the matrix.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/eval_baseline.md",
     "lines": "16",
     "quote": "The prior pipeline hid this with retry; one-shot exposes it.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "194",
     "quote": "BoN K=N is data-harvest + diagnostic + param-discovery only, never quoted as goal progress.",
     "verbatim": true
    }
   ],
   "against": "The per-cell samples behind the 52%→86% pair are tiny and partly mismatched (failure_taxonomy.md line 349: '(different prompts; clean N=3 is too small)'). A retry on a failed delivery that does not look at the output was kept as legitimate (inference_clean.md line 42: 'Transport-level retry on transient 5xx — does not condition on output content.'). eval_baseline.md line 243's '~70 pp' compares a different model, grader and server, so it overstates the effect.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep",
   "reason": "The quotes are verbatim and 95%, ~100%, 100%/0%, 2 sources and -13.3pp match. Added memory/MEMORY.md line 75: the fabrication rate held across three model versions. The 'can' keeps the claim within the evidence, and it applies to any item that carries a source text. Not a duplicate: 17 checks quotes against a known text and 58 is a topic check. This is the failure a general judge lets through.",
   "statement": "Check source texts for fabrication with a check of their own, because a general quality judge can pass nearly every item whose sources were invented.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "80",
     "quote": "v29 fabricates MCQ_SET stimuli at 95% under BAML rubric; IB passes at ~100%.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "75",
     "quote": "MCQ_SET fab rate 100% across v25b/v29/v40h; recipe variations don't fix it.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "177",
     "quote": "SAQ/LEQ 0% fab; MCQ/MCQ_SET/DBQ 100% fab",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "81",
     "quote": "Oracle's BAML-rubric rescore: -13.3pp aggregate Goodhart gap; SAQ 4/6 not 6/6; **2 fabricated primary sources in MCQ_SET**",
     "verbatim": true
    }
   ],
   "against": "The fabrication verdicts came from another model-based rubric, not from a person checking each source. That rubric (BAML) was later retired as the promotion grader (memory/MEMORY.md line 76). The calibration-gap entry is P1/T1, and its investigation was 'deferred until D13 ships + v41-d13 eval.' (memory/MEMORY.md line 80). The general judge did catch some invented sources (failure_taxonomy.md line 244: 'likely fabricated source content'). It was later changed to hard-fail fabricated documents (feedback_curriculum_api_mandatory_2026_05_11.md line 9). '100% fab' in BEADS.md line 177 is unexplained shorthand.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "The kept quotes are verbatim. This is truth 57 (verified sources as the writer's only source) applied to source documents, plus truth 17's word-for-word use, so it is marked a duplicate of 57. It stays because it adds measured evidence: 0% to 4 of 6 once matched real documents were supplied and used word for word. It also adds a drop-don't-patch rule. The reader's lead quote (FINAL_PLAN_2026_05_11_v3.md line 118: 10/11 DBQ failures at stimulus_quality 0.0, read as fabricated documents) is verbatim. Its fabrication reading was later contested, so I swapped it for a judge rationale that names fabrication directly. I also added the line saying the writer used the documents word for word, plus the pipeline's drop rule.",
   "statement": "Never let a writer invent a source text and attach a real author or date to it: take source texts from a verified bank, use them word for word, and drop any item whose source can't be matched rather than patching it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "244",
     "quote": "Several documents present historically unreliable information (notably the Declaratory Act excerpt and other implausible or likely fabricated source content), which could directly misteach students about key events and policies.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/STATE_CURRENT_2026_05_12T0805Z.md",
     "lines": "88",
     "quote": "### D13 inference injection: 4/6 = 66.7% DBQ (was 0%)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/STATE_CURRENT_2026_05_12T0805Z.md",
     "lines": "90",
     "quote": "Model uses docs verbatim → stim_q=1.0 → pass",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/PILLARS_2026_05_12.md",
     "lines": "64",
     "quote": "- Stimulus matches /search hit? (else drop)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "187",
     "quote": "every text field in any new corpus must trace to a primary source; LLMs are tools (search/OCR/reformat) not content authors; drop-don't-patch when sources fail.",
     "verbatim": true
    }
   ],
   "against": "A later forensic put 26 of 30 DBQ stimulus failures down to prose descriptions of visuals that were not there (state_training_chain_2026_05_12T1300Z.md line 54: 'IB rule: prose description of absent visual = stimulus_quality 0 hard'). So the lift from real text documents may owe as much to removing described visuals as to removing invented text. The injection result rests on 6 items. Training the writer on real documents did not stop fabrication (memory/MEMORY.md line 67: 'D13 source-grounded hypothesis falsified.'). Documents plus extra guidance backfired (BEADS.md line 388: 'PATH G DBQ hybrid D13+curriculum = counterproductive (context overload)'). memory/MEMORY.md line 187 is a rule for training corpora, applied here by analogy.",
   "general": true,
   "duplicate_of": "57",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep",
   "reason": "The quotes are verbatim and 198/436 matches. Added the same line's wrong-work finding: it backs the found_by's 'a different work from the one their label named', which had no quote. Applies to any item built on sources. Not a duplicate: 50 records provenance and 63 checks course and unit labels. This one checks attribution labels against the text.",
   "statement": "Check that every source's label (which work, who wrote it, when, what kind of document) matches its text, both in generated items and in a source bank before anything is built from it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "296",
     "quote": "Document 1 contradicts itself: it is labeled as a manuscript illustration of a dhow but described as a historical map with shaded regions and arrows.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "248",
     "quote": "Several documents are labeled with specific primary-source titles and dates that do not match what the text says",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "72",
     "quote": "F-D13-12 caught 198/436 era misclassifications.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "72",
     "quote": "F-D13-18 caught 4 wrong-work Gutenberg IDs in Branch C",
     "verbatim": true
    }
   ],
   "against": "The bank audit (memory/MEMORY.md line 72) was an agent audit of a training corpus with spot-checks, not a full manual review. The two judge rationales are single items.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep",
   "reason": "The quotes are verbatim. The ~14 count matches failure_taxonomy.md lines 266 and 448 and .agent/MEMORY.md line 113. Added the line-266 description of the failure: an answer key and scoring guidance inside the question content. Close in spirit to 12 (words aimed at the marker), but about generated items, so kept separate. .agent/MEMORY.md also holds names, emails and key-like lines elsewhere; quote only lines 76 and 113.",
   "statement": "Scan generated items for text aimed at the judge, such as embedded scores, rationales or grading instructions, and void any item that contains it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "266",
     "quote": "Evaluation voided: integrity_check failed. The content contains embedded evaluation/score data and score-steering instructions.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "266",
     "quote": "**This is a prompt-injection style failure where the model has emitted an answer key + scoring guidance INSIDE the question content.**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "448",
     "quote": "Recommended: scrub the training set for any stimulus containing strings like `\"score:\"`, `\"rationale:\"`, `\"part_1_*\"` regex match.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/MEMORY.md",
     "lines": "113",
     "quote": "**Scrub training data of prompt-injection-style stimuli** — F1 found ~14 MCQ_SET records with embedded scoring directives in `stimulus`.",
     "verbatim": true
    }
   ],
   "against": "Some integrity voids were the judge's own bug (inference_clean.md line 50: 'Known IB v2.4 bug.'; line 64: 'Empty stems trigger InceptBench integrity_check false positive'). The ~14 records were stored items in a training bundle. The action taken was a training-data scrub, not a live check on new items.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep",
   "reason": "The quotes are verbatim. An adopted rule from a line-by-line audit of the pipeline code, and it applies to any judged content. The reader's counter quote spans lines 414-415 across a line break and is otherwise verbatim. Not a duplicate of 10 or 23.",
   "statement": "Don't reword, trim or pad generated content after the fact to satisfy a judge; fix the content itself, because edits made for the judge change the score without improving the item.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "72",
     "quote": "Rewrites generator output specifically to game the grader. Textbook crutch.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "403",
     "quote": "The post-process scans, deletes overlapping items, and pads with a generic placeholder if cleanup leaves <3. This is the rubric grader literally seeing different content because of the post-process.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "405",
     "quote": "Rewrites the actual text the grader scores. Direct rubric manipulation.",
     "verbatim": true
    }
   ],
   "against": "The rule covers edits the judge sees. Edits outside its view were kept (inference_clean.md lines 414-415: 'Any post-process that lives outside the grader's view (image gen, logging, transport retry, chat-template normalization) is fine.'). Dropping a failed candidate was still allowed (PILLARS_2026_05_12.md line 64: '- Stimulus matches /search hit? (else drop)'). The audit's test was the project's one-shot rule, not a measured loss of item quality.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep",
   "reason": "The quotes are verbatim. An adopted rule from the same audit, and it applies to any generator that takes requests. Not a duplicate: 63 checks scope labels when judging; this forbids changing them when generating.",
   "statement": "Generate what was asked: never silently change a requested level, topic or scope to suit the judge, and correct a wrong request where it was made.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "74",
     "quote": "Silent input mutation to game the grader. The clean contract honors what the caller asked for.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "75",
     "quote": "Either the benchmark is right (then the model must handle it) or wrong (then fix the benchmark). Not the generator's job.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "410",
     "quote": "The rubric checks `curriculum_alignment` against the time_period the request claims; mutating the period changes what the grader sees vs what was requested.",
     "verbatim": true
    }
   ],
   "against": "The mutations existed because some requests were arguably unsuitable (inference_clean.md line 74 quotes the code comment: 'DBQ, LEQ, and SAQ are inherently complex formats — easy is misleading and causes evaluator difficulty_alignment failures').",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim and 0.071-0.133 matches eval_baseline.md line 267. I softened 'manufactures failures' to 'can manufacture failures': the source only estimates the effect and says 'probably'. Safety note: eval_baseline.md line 38 holds a plaintext key; quote nothing from lines 36-40.",
   "statement": "Use a judge only on item types it was built for and apply only the criteria that fit each type; a misapplied criterion can manufacture failures, and an unsupported type gets scored zero or waved through.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/eval_baseline.md",
     "lines": "267",
     "quote": "SAQ has no distractors, so this is an IB grader oddity — it's penalizing SAQ for lacking distractors.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/eval_baseline.md",
     "lines": "97",
     "quote": "Pass an SAQ/LEQ/DBQ in and it falls through the MCQ structural rules and hard-fails on `mcq_wrong_option_count` + `explanation_too_short` — every one scored 0.0 with no useful dimensions.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/eval_baseline.md",
     "lines": "42",
     "quote": "Anything that ran against it for AP types either passed through or was no-oped.",
     "verbatim": true
    }
   ],
   "against": "The size of the effect is an estimate, and the misapplication was never confirmed (eval_baseline.md line 267: 'Investigate whether the IB rubric should skip distractor_quality for non-MCQ types (probably). If it should skip and isn't, it's contributing ~5 pp of artificial failure.').",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep",
   "reason": "The quotes are verbatim. 63.64/89.56/+25.92, 90.67/~54.7, and 70.0 against 62.89 (-7.1) all match. Added the same line's standing rule and the eval template's requirement to record the judge version. Overlaps candidate 9 (stale baselines), but this is the narrower, better-evidenced case.",
   "statement": "Never compare scores from different judge versions or judge instances; re-score both sides with the same judge and record the judge version with every score.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "186",
     "quote": "Same v29 generations score 63.64% (v2.4.0 endpoint 192.168.1.26:8001) vs 89.56% (v2.5.3 endpoint 192.168.1.10:8001). +25.92pp swing from grader alone, no model change.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "186",
     "quote": "**Rule:** every pass-rate citation must specify grader version explicitly. Don't compute deltas across versions; require both endpoints same OR re-score one side.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_iterative_improvement_not_fresh_models_2026_05_12.md",
     "lines": "81",
     "quote": "The \"v43-soup was 90.67%\" memory entries refer to IB v2.5.3. After grader update, v43-soup is ~54.7%.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/plan.md",
     "lines": "489",
     "quote": "Audit baseline (2026-05-14 s7 single-shot): 70.0% — drift -7.1pp. Likely grader-version delta between IB instances (audit used iCloud local IB; this is 192.168.1.15:8001).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent-v2/templates/eval-cycle.md",
     "lines": "45",
     "quote": "IB grader version captured (v2.5.11 currently)",
     "verbatim": true
    }
   ],
   "against": "plan.md line 489 calls the instance gap only 'Likely' a grader-version delta, and it compares one seed with a three-seed mean. Part of the 90.67%→~54.7% drop comes from hard-zero checks the later judge added: a real change in strictness, not noise.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. 0.9475/0.9307/87.56%, 68.22% and -4.4/-5.4/-8.2 match. I removed 'in the same session', which no source requires. Added plan.md line 76 to show the comparison was against the stored 68.22%. A model whose weights never moved (line 107) scored about 5.4 points below that number, while its own three seeds were within about 2 points of each other (lines 71-74).",
   "statement": "Re-run the baseline fresh, under the same conditions as the new version, rather than comparing against a stored number.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "114",
     "quote": "v29 inference at temp=0 gives DIFFERENT continuous (0.9475 frozen vs 0.9307 fresh) on same prompts/model. Binary same (87.56%). All test configs use fresh gens; baseline must too. Several \"regressions\" reverse to \"real lifts\" with proper baseline.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "184",
     "quote": "Reverses v42/v40h regression framings — both now stat-tied with v29",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/plan.md",
     "lines": "76",
     "quote": "vs v80b 68.22% → **-5.43pp regression** (between v81b's -4.44 and v81e's -8.22).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/plan.md",
     "lines": "111",
     "quote": "The -4.4 / -5.4 / -8.2pp eval deltas are most likely measurement noise around an essentially-unchanged v80b",
     "verbatim": true
    }
   ],
   "against": "Later practice froze a baseline instead (feedback_test_2_at_a_time_2026_05_12.md line 44: '- Baseline number 56.48% is FROZEN reference; no re-eval needed unless serving drifts'). The snapshot calls the inert-model deltas 'most likely' noise without re-running the baseline, and serving or grader differences were never ruled out.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim; σ 1.54 and 7-9, and 24/30 against 19/30, match. I removed the claim that long multi-part items vary more than short ones, because the sources contradict it. I also widened the statement to cover spread across generation seeds, which is what PLAN.md line 279 limits. It builds on 34 (verdicts vary) by adding the decision rule, so it is not a duplicate.",
   "statement": "Measure the run-to-run spread of scores for each item type, both rescoring unchanged outputs and repeating generation seeds, and count a difference only when it clears that spread; the spread differs widely between item types.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "112",
     "quote": "3-run probe: APUSH agg σ=1.54pp, DBQ σ=7-9pp. Win-declaration thresholds per-cell. MCQ/LEQ deterministic.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "197",
     "quote": "Same v29 gens scored to 24/30 vs 19/30 on apush/dbq across runs. ~1-3pp aggregate noise.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "197",
     "quote": "**Don't trust deltas under 5pp single-call.**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/PLAN.md",
     "lines": "279",
     "quote": "**Inter-seed std-dev ≤ 4pp**. If std-dev > 4pp, fire F13 (re-eval 2 additional seeds before branching). High variance means the mean is uninterpretable.",
     "verbatim": true
    }
   ],
   "against": "The types that did not vary were MCQ and LEQ (memory/MEMORY.md line 112). LEQ is a long-essay type, so length does not explain the spread. The large DBQ spread was later traced mostly to the pass/fail cut (memory/MEMORY.md line 113: 'DBQ \"noise\" was ~all threshold artifact').",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep",
   "reason": "The quotes are verbatim; +1.77 and -0.88 match. The v38 decision rules were written before the results came in, so reporting both scores was planned in advance. Not a duplicate.",
   "statement": "Compare versions on the averaged continuous score as well as the pass rate, because a pass/fail cut turns small score shifts into apparent noise or false gains.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "113",
     "quote": "Switch primary metric from binary pass-rate to averaged-continuous overall. Compass R41: threshold at 0.85 causes most apparent variance. FREE; ~5× sharper. Reveals v36b binary +1.77pp = continuous -0.88; DBQ \"noise\" was ~all threshold artifact.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/v38_decision_rules.md",
     "lines": "11",
     "quote": "Report: aggregate binary pass-rate + aggregate continuous score + per-cell breakdown",
     "verbatim": true
    }
   ],
   "against": "Accepting an item still has to be binary on critical criteria (achieved.md line 133: 'CRITICAL_VETO_CAP=0.84'), and later gates went back to pass rates (PLAN.md line 276: '**Measured:** 3-seed mean K=1 on n=150 IB v2.5.7 standard, T=0.').",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep",
   "reason": "The quotes are verbatim; p=0.7744, 0/297 and 30/30 match. Added the eval template's paired-test requirement. Related to 38 (a check that never fired), but about interventions, so not a duplicate. The training-run case is used only for its measurement lesson.",
   "statement": "Before crediting or blaming a change, confirm it actually took effect in the outputs, and test the difference on the same items with a paired test.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "130",
     "quote": "McNemar p=0.7744 on APUSH (within noise); 0/297 v35 outputs emit any reflection token at decode (Self-RAG mechanism didn't fire).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "180",
     "quote": "CoVe scaffold didn't fire at 14B (30/30 DBQ items `cove_stage=no_block`)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/plan.md",
     "lines": "107",
     "quote": "Across 190 steps and ~5.85M tokens, **DPO extracted zero signal**. The policy never updated.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent-v2/templates/eval-cycle.md",
     "lines": "50",
     "quote": "Statistical significance check (paired-t or BH-FDR if applicable)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim; 92%, 30/30, ~80% and σ=0.424 match. I softened 'often luck' to 'can be luck', since there are only two cases. I trimmed the BEADS.md line 182 quote to the part that still stands. Its '-3.78pp vs v29' framing was reversed once the baseline was re-run.",
   "statement": "Audit unexpected wins as closely as losses; a record result from one run on a small set can be luck and fall back when re-run.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/PILLARS_2026_05_12.md",
     "lines": "37",
     "quote": "For any cell or arm that PASSED unexpectedly, audit the prompt + generation",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "104",
     "quote": "Original cell-routed 92% used single-pass mcq_set (got lucky 30/30); 3-way eval revealed v43-soup mcq_set true ceiling ~80% under stochastic 3-seed (σ=0.424).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "104",
     "quote": "Always 3-seed before claiming K=1 numbers.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "182",
     "quote": "Prior 0.9-class single-run was statistical noise — R8 caught it",
     "verbatim": true
    }
   ],
   "against": "BEADS.md line 184 reverses the found_by's '-3.78 points below the baseline' ('both now stat-tied with v29'). PILLARS_2026_05_12.md line 38 gives auditing wins a second purpose: harvesting templates for the next training set.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep",
   "reason": "The quotes are verbatim. 5/50 against 95.56%, 45/50 against 100%, and 5,927 rows match. Added the eval template's input audit. Kin to 48 and 66 but about claims made for a generator, so kept.",
   "statement": "Re-test any claimed result on fresh items that took no part in producing or tuning it, and check that the test items don't overlap anything the generator learned from.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "705",
     "quote": "FAIL: 5/50 = 10.00% on n=50 fresh Unit-1 prompts (independent of den's 30-prompt training set). Delta -85.56pp from den's self-reported 95.56%. Recipe does NOT generalize.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "708",
     "quote": "FAIL: 45/50 = 90.00% on n=50 fresh Unit-1 MCQ from e7e1d980 (no KC overlap with Cheater's 16-KC apush_baseline). -10pp delta from claimed 100%.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/PLAN.md",
     "lines": "280",
     "quote": "**Contamination spot-check passes**. Sample 10 random eval prompts; verify none appear in the 5,927-row audited training corpus. If any match → F14 (poison candidate; do not promote).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent-v2/templates/eval-cycle.md",
     "lines": "34",
     "quote": "Verifier confirms inputs not from training distribution",
     "verbatim": true
    }
   ],
   "against": "The first data audit had no near-duplicate check between hold-out and training items (data_audit.md line 190: '**No near-dup leakage protection.** This audit does NOT yet de-near-dup against the training pool.').",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep",
   "reason": "The quotes are verbatim; 13.3% (TRUE ~45%) and 10-25pp match. Added the memory index's T0 entry and the status note's judge-timeout rate. Adds evidence to 9 on timeouts but is broader.",
   "statement": "Count failures by kind (delivery failure, unreadable output, wrong structure, judge timeout, judged content failure) and never lump them together or drop them silently.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/LESSONS_LEARNED.md",
     "lines": "65",
     "quote": "**Lesson:** Always bucket: parse fail (model output broken) vs transport fail (5xx) vs schema fail (valid JSON, wrong structure). Don't aggregate them.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "162",
     "quote": "`parse_ok=false` lumps 5xx with JSON fails; misread cost a wrong \"v20a more brittle\" claim. Always bucket by error type.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/STATE_CURRENT_2026_05_12T0805Z.md",
     "lines": "49",
     "quote": "| apush/mcq_set | 20% | 13.3% (TRUE ~45%) | 16.7% | Grader timeout on long outputs; TRUE rate higher |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/STATE_CURRENT_2026_05_12T0805Z.md",
     "lines": "97",
     "quote": "mcq_set grader times out on long outputs (~67% grade_fail rate)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "452",
     "quote": "If errors are added back, the apparent pass rates fall by another 10-25pp depending on cell.",
     "verbatim": true
    }
   ],
   "against": "The 'TRUE ~45%' figure is the status note's estimate, not a re-graded rate.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "keep",
   "reason": "The quotes are verbatim; 0/150, −6.67pp and 0.0 match. Added the standing rule from memory/MEMORY.md line 89. Not a duplicate of 36.",
   "statement": "When a run collapses or scores all zeros, check the measuring pipeline (judge connection, output cleaning, score lookup) before blaming the content.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "221",
     "quote": "Retraction: bon_decode 0/150 root cause is IB endpoint IP mismatch (.10 vs .17), NOT best_of_n.py",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "109",
     "quote": "The −6.67pp v29 \"drift\" was a stale `strip_think` in `oneshot_generate.py` (matched `<thinking>` long-form only; Qwen3 emits `<think>` short-form).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "101",
     "quote": "Misnested lookup silently returns 0.0; bug hit in oracle rescore script.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "89",
     "quote": "(3) For all-zero/all-fail anomalies, check grader endpoint health BEFORE diagnosing model bug.",
     "verbatim": true
    }
   ],
   "against": "An audit can come back clean (SESSION_DECISIONS_2026_05_11.md line 29: 'All three CLEAN;') even though its grader check replayed only one row (BEADS.md line 284: 'May-6 LEQ row 58482 replay = identical 1.0/SUPERIOR; no grader drift'). So a clean audit is weak evidence that the content itself changed.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 17,
   "verdict": "keep",
   "reason": "The quotes are verbatim; 73.33%, and 88.67% against 90.67%, match. Added the standing rule to re-derive baselines from the summary files. Analogous to 17 but about numbers in reports, so kept separate.",
   "statement": "Every number in a report must trace to the run's own results file, checked in code, and any figure found nowhere in the results is rejected.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "23",
     "quote": "proved \"73.33% catastrophic\" doesn't exist in any eval file.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_use_claim_validator_before_save.md",
     "lines": "34",
     "quote": "| **R3** | Pass-rate-shaped number (≥2 decimals, 0.40-1.0 or 40-100) NOT in any `summary_*.json` | REJECT | Phantom-number prevention; uses `scripts/grep_claim.sh` |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "213",
     "quote": "(1) v43-soup baseline was 88.67% verified, not 90.67% claimed (state_current marked unverified)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "89",
     "quote": "(2) Re-derive baseline numbers from on-disk summary JSON, not state_current.",
     "verbatim": true
    }
   ],
   "against": "The code check has false positives on numbers stored in other formats (feedback_use_claim_validator_before_save.md line 88: '## Known false-positive: R3 on 0.9 pass rates').",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep",
   "reason": "The quotes are verbatim; 50%, 13/30 and 17/30 match. Related to 49 (report by skill) and 60, but this is an acceptance rule for a generator.",
   "statement": "Test a generator on every item type it must produce and accept it on its worst type, with a floor for each, not on its average.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/NORTH_STAR.md",
     "lines": "24",
     "quote": "We need to win every cell, not the average. Average can hide a regression on the hardest cell.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/OVERNIGHT_RECAP.md",
     "lines": "105",
     "quote": "**v8/v15 numbers were MCQ-only.** v8 was trained on MCQ records only — and on the 10-cell test, **v8's DBQ outputs fail to parse 50% of the time** (13/30 APUSH, 17/30 APWH).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/NORTH_STAR.md",
     "lines": "45",
     "quote": "The mission is the min over 10 cells, not the mean.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim; +6.7/-8.9 and +0.67/+1.33 match. I narrowed 'add none' to background facts, because adding matched real documents to the document-based type helped. Added the rule from line 198.",
   "statement": "Set and test the background given to a writer separately for each item type, and don't add background facts to types that already carry their own source text; the effects can run in opposite directions by type and cancel out in the average.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "198",
     "quote": "RAG-at-decode + curriculum API top-3 helped MCQ/SAQ/LEQ but HURT DBQ + MCQ_SET (which already have stimulus).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "198",
     "quote": "**Rule: RAG only when prompt doesn't carry its own source content.**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "122",
     "quote": "Full 150-item: MCQ +6.7pp REAL LIFT, SAQ -8.9pp REAL REGRESS. Aggregate washes out.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "388",
     "quote": "PATH G DBQ hybrid D13+curriculum = counterproductive (context overload); D13-only at 17%, D13-targeted retrieval at 66.7%",
     "verbatim": true
    }
   ],
   "against": "The overall effect was within noise (memory/MEMORY.md line 198: 'Aggregate +0.67pp / cell-routed +1.33pp APUSH (within noise) but per-cell direction is reusable.'). The two entries disagree on whether the short-answer type gained (top-3 facts) or lost (richer context). Supplying the real source documents themselves helped the document type (STATE_CURRENT_2026_05_12T0805Z.md line 88: '### D13 inference injection: 4/6 = 66.7% DBQ (was 0%)').",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep",
   "reason": "The quotes are verbatim; 5 of 9 and 100%→43% match. Added the failure taxonomy's root-cause line. Not a duplicate of 63, which checks labels when judging. This one states the limits to the writer and checks every part of the item.",
   "statement": "State the scope's hard limits in every request (time span, unit, what is out of bounds), especially where neighbouring units overlap, and check every part of the item, marking guide included, against them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "121",
     "quote": "Targeted 9-item probe: assessment_boundaries injection resolves 5 stable APUSH fails outright + 2 improved.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/plans/PLAN-mission-2026-04-26.md",
     "lines": "71",
     "quote": "Without it, APWH u3 dropped 100% → 43% in prior runs.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "233",
     "quote": "as evidence for a prompt limited to 1800-1848, which is chronologically incorrect for this question's time period.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "322",
     "quote": "The model lacks a constraint to treat the unit's time window as a hard filter.",
     "verbatim": true
    }
   ],
   "against": "The probe was 9 items, and the boundary notes themselves were model-written (memory/MEMORY.md line 210: 'same record mixes CB-canonical statement with Haiku-generated misconceptions/assessment_boundaries'). The 100%→43% figure is carried over from a prior plan ('prior plan I-6' in the same table row), not re-measured.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "keep",
   "reason": "The quotes are verbatim and 70-99% matches. The set's questions share one stimulus, so this is truth 68: a distinct element for each question on a shared source. Kept as a duplicate because it adds the measured failure share and the fix of planning coverage before writing.",
   "statement": "Decide what each item in a set will cover before writing any of them, so each tests a different element; left alone, a writer piles every item onto the most salient case.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "328",
     "quote": "**Manifestation:** ~70-99% of MCQ_SET failures fail `cognitive_demand` (specifically `difficulty_distribution` + `concept_coverage`).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "329",
     "quote": "the Plan step in MCQ_SET generation does not enforce multi-entity coverage. The model picks the most prominent/salient entity in the topic and concentrates there.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "330",
     "quote": "Plan step must enumerate `nations_to_cover: [\"Portugal\", \"Spain\", \"France\", \"England\"]` and Question step must be locked to \"each question MUST address a different nation from this list\" (postmortem prescription).",
     "verbatim": true
    }
   ],
   "against": "These files never record what the planning fix achieved, and the set type stayed the weakest (achieved.md line 14: '- MCQ_SET: 4% (v80b same as v75 — DPO didn't fix; v54 routes for 27%)').",
   "general": true,
   "duplicate_of": "68",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. Added failure_taxonomy.md line 330, which backs the per-item check that previously had no source. Applies to any item set with a stated level.",
   "statement": "A difficulty label doesn't make an item that hard; build the difficulty into what the item asks, and check each item in a set against the set's stated level.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/sota_strategy.md",
     "lines": "114",
     "quote": "The hga fix already showed that injecting difficulty *labels* without content variation does nothing.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "204",
     "quote": "The set is marked as 'hard,' but two questions are explicitly labeled 'Easy' and 'Medium,' so the quiz does not match the requested single-difficulty level.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "330",
     "quote": "Additionally: enforce per-question difficulty assignment matching the set's stated difficulty.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/plans/PLAN-mission-2026-04-26.md",
     "lines": "80",
     "quote": "Minor effect; model learns difficulty implicitly from data.",
     "verbatim": true
    }
   ],
   "against": "The result that labels do nothing is second-hand (sota_strategy.md line 113 cites the 'handoff hga-fix lesson'). PLAN-mission-2026-04-26.md line 80 supports only the first clause.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "drop",
   "reason": "The quotes are verbatim, but nothing tested the claim. The bead that would have tested it was bulk-closed without running (BEADS.md line 386). The curriculum search it depended on was not wired into production (STATE_CURRENT_2026_05_12T0805Z.md line 56). The misconception lists were model-generated (memory/MEMORY.md line 210), so calling them 'documented misconceptions' overstates them. This is a design intention, not a learning truth. Bring it back as an open item if it is ever measured.",
   "statement": "Draw wrong options from documented misconceptions about the topic.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_curriculum_api_mandatory_2026_05_11.md",
     "lines": "25",
     "quote": "- `common_misconceptions` — 12 per topic, perfect MCQ distractor candidates",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/PILLARS_2026_05_12.md",
     "lines": "57",
     "quote": "MCQ: misconceptions as distractor seeds + rich context",
     "verbatim": true
    }
   ],
   "against": "Never measured here: the bead meant to test it was bulk-closed (BEADS.md line 386: 'PATH E — Misconceptions-as-MCQ-distractors' ... 'BULK-CLOSE 2026-05-22T15:10Z: Superseded'). The misconception lists were model-generated (memory/MEMORY.md line 210: 'Haiku-generated misconceptions/assessment_boundaries').",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep",
   "reason": "The quote is verbatim. There is only one source, but it records a mix actually found in a real source and the ruling that followed. It refines 50 (record each asset's source) down to the field level; not a duplicate.",
   "statement": "Record provenance for each field, not each record, because one record can mix verified statements with model-written additions.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "210",
     "quote": "Curriculum API merge_source is record-level; same record mixes CB-canonical statement with Haiku-generated misconceptions/assessment_boundaries. Treat curriculum API as retrieval/few-shot reference, NOT direct training data.",
     "verbatim": true
    }
   ],
   "against": "A single agent audit of one curriculum source; it does not say how many records were mixed.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 25,
   "verdict": "keep",
   "reason": "The quotes are verbatim and 14/43 = 33% matches. Applies to any item built on a passage. Related to 64 (never describe a picture that isn't there) but broader.",
   "statement": "Check that everything an item says its source contains is actually in the source.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/gate1_decision.md",
     "lines": "35",
     "quote": "`passage_reference` failing in 33% of fails is the second pattern: the model writes stimulus passages that reference content the stimulus doesn't actually contain.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "99",
     "quote": "factual_accuracy 32/43 = 74%, passage_reference 14/43 = 33%, clarity_precision 6/43, curriculum_alignment 3/43, others <5%.",
     "verbatim": true
    }
   ],
   "against": "The reading 'content the stimulus doesn't actually contain' is the analyst's gloss on the passage_reference dimension (gate1_decision.md line 35). The failing items themselves are not quoted, and the run was 60 multiple-choice items from one model.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "keep",
   "reason": "The quotes are verbatim; 74.0%, -8.67pp and 25-63pp match. The drop is about five times the aggregate spread of 1.54pp. Applies to any writer model, though it is about output settings rather than content rules.",
   "statement": "Forcing a rigid output format while a model writes reasoning-heavy content can lower its quality, so measure the trade-off before switching it on.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/SESSION_DECISIONS_2026_05_11.md",
     "lines": "28",
     "quote": "UPLIFT-3 constrained decode = 74.0% (-8.67pp, Synapse Item 25 predicted), UPLIFT-3b per-cell schema = 84.0% (+1.33pp, within noise).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "150",
     "quote": "JSON mode loses 25-63pp on reasoning tasks; per-cell decision; default OFF for free-form cells.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/FINAL_PLAN_2026_05_11_v3.md",
     "lines": "27",
     "quote": "**Zero parse_fail.** Format-fragility hypothesis is dead.",
     "verbatim": true
    }
   ],
   "against": "A benchmark cited in the strategy review reported a small gain (sota_strategy.md line 142: 'Reports ~3% improvement using guidance/constrained decoding.'). The −8.67-point result is a single run. The 25-63pp figures are cited by venue only (memory/MEMORY.md line 150: 'T2 (Tam EMNLP 2024 + Park NeurIPS 2024)').",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. I widened 'shown to a writer' to cover tuning data, because failure_taxonomy.md line 314 is about fine-tuning. The reader's counter-evidence said examples 'did lift' some types by 3-8 points. The note behind that number lists it as an expected lift, not a measured one, so I corrected that counter-evidence. The 'facts must come from a verified source' clause overlaps 57.",
   "statement": "Worked examples given to a writer, in the prompt or in tuning data, teach the form of the output, not correct facts; facts must come from a verified source, and an example's content can carry over into unrelated items.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "154",
     "quote": "ICL works via format/distribution; refutes \"few-shot fixes DBQ veracity\"; lifts mcq_set/saq +3-8pp at K=3 with chat-template-aligned demos.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "314",
     "quote": "Fine-tuning teaches structural patterns, not facts.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/spec_v97_dbq_focused_criterion_grounded_dpo_2026_05_25.md",
     "lines": "153",
     "quote": "v80b's factual reliability on synthetic Unit-1 content is the bottleneck (Civil War few-shot transferred to pre-contact KCs in Cheater v6).",
     "verbatim": true
    }
   ],
   "against": "The +3-8 points is a forecast, not a measurement: work/auto-memory-backup/research_fewshot_format_not_facts.md line 36 lists it under 'Expected lift', and its audit note rates the size T3. The review cites papers by venue with no DOI or URL. The carry-over case is a single observation.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim; 99.11% and 82.67% match. The source prescribes sampling at random from the pool (feedback_k8_bon_winner_trap_2026_05_11.md lines 9-32), not keeping production order, so I replaced that clause. The FINAL_PLAN quote is trimmed to leave out a person's name.",
   "statement": "When estimating single-attempt or best-of-several rates from a stored pool of scored candidates, sample candidates at random or regenerate; never read the top of a score-sorted list, which always returns the pool's best.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_k8_bon_winner_trap_2026_05_11.md",
     "lines": "7",
     "quote": "The `all_scores` array is sorted DESCENDING by IB score (winner first). Slicing the first N entries gives you the TOP N from the K=8 pool, and the max of that is always `all_scores[0]` = the K=8 winner.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_k8_bon_winner_trap_2026_05_11.md",
     "lines": "36",
     "quote": "On 2026-05-11, orch reported \"B0161 K=2 BoN = 99.11% mean\" computed from existing K=8 data via `max(all_scores[:2])`. This number is identical to K=8 winner pass rate.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/FINAL_PLAN_2026_05_11_v3.md",
     "lines": "23",
     "quote": "K=1 was 99.11% per K=8 candidate-0 → wrong (sorted-by-score artifact).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/FINAL_PLAN_2026_05_11_v3.md",
     "lines": "24",
     "quote": "**1h ago**: UPLIFT-1 single-seed K=1 T=0 = 82.67% on v43-soup `ty16vgj9`.",
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
   "reason": "The quotes are verbatim; 70% < 90% and 60% < 80% match. Restated as the action the evidence supports: re-grade a stratified sample, require agreement, watch the in-between class. Related to 37 and 61 but about labels made for training, so kept separate.",
   "statement": "Before building on model-made labels (such as 'supported by the source'), re-grade a stratified sample independently and require high agreement, especially on the in-between classes.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "133",
     "quote": "Aggregate 70% < 90% \"clean\" bar; partially-class 60% < 80% \"rebuild\" bar.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "133",
     "quote": "Bidirectional noise on the pivotal partially class — model can't learn calibration offset.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/plan_v92_pipeline_distillation_single_model_2026_05_22.md",
     "lines": "77",
     "quote": "Done when: ≥27/30 pairs confirmed \"chosen clearly better than rejected on rubric dim\"",
     "verbatim": true
    }
   ],
   "against": "The re-grade was itself done by another model, not a person (memory/MEMORY.md line 133: 're-graded 30 stratified IsSup spans from `sftv31_self_rag_train.jsonl` with gemini-3.1-pro-preview vs Quill's gemini-2.5-pro labels'). plan_v92 line 77 is a planned completion criterion, not a result.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 30,
   "verdict": "keep",
   "reason": "The quotes are verbatim; 37/50, 13 misses and 99.7% (4 of 5 cells) match. Added the same audit's verdict on template banks.",
   "statement": "When items are served from a bank of pre-checked items, report the bank's coverage of fresh requests separately from item quality.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "714",
     "quote": "37 passes = cache hits; 13 cap_reached = substandards not in cache.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/COMPREHENSIVE_PLAN_v2_2026_06_02.md",
     "lines": "36",
     "quote": "| Layer 1 cache delivers 99.7% IB aggregate (4 of 5 cells) | Cheater 09:50Z delivery |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
     "lines": "707",
     "quote": "deterministic templates are cherry-picking by another name",
     "verbatim": true
    }
   ],
   "against": "Both figures come from agent-built banks on narrow scopes (one unit; four of five types).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep",
   "reason": "The quotes are verbatim; 74.4% + 2pp and σ_floor 1.54pp match, and the bar was set before results came in. Not a duplicate of 45 (fix the rubric) or 24.",
   "statement": "Fix the bar for a new version before measuring: it must beat what learners currently receive, not one of its parts, by more than the noise margin.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/PLAN.md",
     "lines": "447",
     "quote": "Forgetting this lets a 75% noise-band result be promoted as a +0.6pp \"win\" over the actual user-facing baseline.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/PLAN.md",
     "lines": "120",
     "quote": "A \"step-function win\" must beat the deployable, not the component.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/v38_decision_rules.md",
     "lines": "12",
     "quote": "Statistical threshold: σ_floor = 1.54pp (APUSH aggregate from R41 probe)",
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
   "verdict": "keep",
   "reason": "The quotes are verbatim; 0/176 and ~20% match.",
   "statement": "Compare versions only on the same frozen set of items, because two sets of the same item type can differ sharply in difficulty.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/achieved.md",
     "lines": "69",
     "quote": "Root cause: paqpgdst's MCQ_SET pass rate on HOLDOUT prompts is **0%** (0/176 K=3 attempts), vs ~20% on eval baseline. Holdout prompts are systematically harder.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent-v2/templates/eval-cycle.md",
     "lines": "29",
     "quote": "Hold-out set freeze with checksum",
     "verbatim": true
    }
   ],
   "against": "The hold-out comparison mixed sampling methods (0/176 over K=3 attempts against a ~20% baseline rate), so part of the gap may come from sampling. The source still concludes the hold-out prompts are harder.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 33,
   "verdict": "keep",
   "reason": "The quotes are verbatim; n=3, n ≥ 30 and n<10 match. The failure taxonomy also reports per-type rates at n=2 (0%) and n=4 (25%), all of which the source itself flags as too small.",
   "statement": "Report the number of items behind every rate and attach no verdict to tiny samples.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "113",
     "quote": "**Tier 1:** n=3, pass=3, fail=0 (100%) — **<5 samples, statistically vacuous.**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "13",
     "quote": "4. T0 evidence requires actual measurement on our data (n ≥ 30 OR multiple confirming runs).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "69",
     "quote": "scripts/validate_claim.sh blocks: R1 (n<10 + verdict word), R3 (phantom number not in summary), R6 (IB-only promotion w/o BAML).",
     "verbatim": true
    }
   ],
   "against": "The project still read one-item differences on 30-item sets as wins (OVERNIGHT_RECAP.md line 95: 'v15 with 174 pairs pushed APUSH from 86.7% → 90%. First evidence DPO works in our regime').",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 34,
   "verdict": "keep",
   "reason": "The quotes are verbatim; 11 metrics, 0.84 and 2× match. Safety note: .agent/MEMORY.md holds names, emails and key-like lines outside lines 76 and 113; quote only those two lines.",
   "statement": "Read the judge's actual criteria, weights and caps from its own source before writing content for it or interpreting its scores.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/MEMORY.md",
     "lines": "76",
     "quote": "**InceptBench rubric — actual 11 metrics for `question` content type** (correction to the earlier 5-dim claim)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/achieved.md",
     "lines": "133",
     "quote": "Identified BAML/Gemini grader, CRITICAL_VETO_CAP=0.84, critical metrics (factual_accuracy + educational_accuracy 2× weight).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
     "lines": "206",
     "quote": "**Reference for every agent: schema before training rows; rubric before scoring expectations; curriculum before factual claims.**",
     "verbatim": true
    }
   ],
   "against": "The 2× weight and the 0.84 cap are reported from a read of the judge's code, not quoted from it.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 35,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. Reworded so the rule does not forbid recall where the objective calls for it. The evidence is a generator rule, a regeneration trigger that existed because recall stems failed the judge, and an analyst's summary of typical judge rationales.",
   "statement": "Make each item demand the thinking its objective and stated level call for (for example explaining, or weighing several causes), not just recall of a fact.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "128",
     "quote": "Use analytical question stems, not recall",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "65",
     "quote": "Cognitive_demand failures on recall stems.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "225",
     "quote": "rubric \"complexity\" guidance fails to require students to weigh multiple causes, undermining the stated difficulty level.",
     "verbatim": true
    }
   ],
   "against": "No before-and-after measurement. failure_taxonomy.md line 225 paraphrases 'typical' judge rationales rather than quoting one.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 36,
   "verdict": "keep",
   "reason": "The quotes are verbatim. A code comment records that the judge hard-fails this, and the audit moved the fix into the content itself.",
   "statement": "In a source-based task, the marking guide's examples of outside knowledge must not repeat what the provided sources already say.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "69",
     "quote": "LLM sometimes lists Doc 5's content as outside evidence — causes factual_accuracy hard-fails because the evaluator checks for this contradiction",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "403",
     "quote": "Fix in training data — train the model to never list document content as outside evidence.",
     "verbatim": true
    }
   ],
   "against": "No count of how often it happened.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 37,
   "verdict": "drop",
   "reason": "The quote is verbatim, but it is one line of a generator's system prompt with no failure or outcome behind it. The statement's rationale ('so only the reasoning the question asks for separates them') is not in the source. 'Every option accurate in itself' also does not hold for item types whose wrong options are wrong facts. Wrong-option quality rarely failed in this project (failure_taxonomy.md line 51).",
   "statement": "Make every option accurate in itself and of the same kind and scope as the key, so only the reasoning the question asks for separates them.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
     "lines": "129",
     "quote": "For MCQ: all 4 options historically accurate, same period, same category",
     "verbatim": true
    }
   ],
   "against": "No measurement in these files, and wrong-option quality was rarely the failing criterion (failure_taxonomy.md line 51: '| 4 | distractor_quality | 1 | 10% | 11% |').",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 38,
   "verdict": "drop",
   "reason": "The quote is verbatim, but the claim overstates it. The item scored 0.82, and its only failing dimension was stimulus_quality (failure_taxonomy.md line 209: 'score=0.82, failing_dims=`['stimulus_quality']`'). 'Accurate but tangential' is the analyst's own comment on the explanation, not the judge's verdict, so the found_by's 'a judge marked down an item' for it is not supported. Single example.",
   "statement": "An answer explanation must justify the key by the reasoning the question asks for, not by a true but tangential fact.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
     "lines": "209",
     "quote": "accurate but tangential to the asked purpose, weakening pedagogical clarity.",
     "verbatim": true
    }
   ],
   "against": "Single example; the recorded failing dimension was a side dimension (failure_taxonomy.md line 209).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/eval_baseline.md",
   "lines": "266",
   "quote": "the IB grader thinks the documents in the DBQ are not \"core/integral\" — i.e. the model emits documents but the prompt could be answered without them.",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
   "lines": "46",
   "quote": "Each block traces to a Gate finding (\"Gate 3: 80% of MCQ_SET failures were answer_balance\").",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
   "lines": "72",
   "quote": "Regex-rewrites generator output: `the excerpt → the passage`, `the source → the text`, `Source: → Origin:`.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_pipeline_eval_not_model_eval_2026_05_12.md",
   "lines": "44",
   "quote": "Pipeline output: NEVER MEASURED — eval has been bypassing the wrapper",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/plans/PLAN-mission-2026-04-26.md",
   "lines": "150",
   "quote": "Dep-03  Final canary: 10-cell re-eval through the integrated path",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
   "lines": "607",
   "quote": "need T1 system-prompt move + T2 post-validation reject + T3 D13 RAG",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
   "lines": "402",
   "quote": "The rubric scores text content; image is a separate channel.",
   "ok": false
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_model_lineage_discipline_2026_05_11.md",
   "lines": "24",
   "quote": "3-seed eval gate before promotion (Synapse Item 12 — single-seed misranks 30%+ of the time).",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/v39_master_record.md",
   "lines": "62",
   "quote": "Single-run 90.67% was misleading — passes 2-3 never ran (deployment destroyed by auto-delete trap).",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
   "lines": "112",
   "quote": "MCQ/LEQ deterministic.",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/FINAL_PLAN_2026_05_11_v3.md",
   "lines": "161",
   "quote": "**Risk**: doesn't actually lift past 90.67% — just stabilizes it. Won't hit 97% alone.",
   "ok": false
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
   "lines": "169",
   "quote": "Quill 7/10 IB calibration PASS (3 fa=0 verdicts are LEGIT grader catches; grader is calibrated even with /curriculums 503).",
   "ok": false
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/eval_baseline.md",
   "lines": "144",
   "quote": "but the actual generation prompt is gone — we'd have to reconstruct it.",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
   "lines": "192",
   "quote": "Every run saves: full per-item raw, run-level metadata (grader version + endpoint + timestamp + model_id + decode params + git_sha), append-only manifest at workspace/eval/runs/MANIFEST.jsonl.",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/eval_baseline.md",
   "lines": "318",
   "quote": "so a cross-version comparison would conflate rubric-drift with model-drift.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
   "lines": "209",
   "quote": "484/492 rows have dead URLs",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
   "lines": "130",
   "quote": "For SAQ: scoring guidance describes criteria, not evidence lists",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
   "lines": "82",
   "quote": "the model fills `sample_response` and `acceptable_evidence` fields with plausible-sounding but wrong historical examples.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_curriculum_api_mandatory_2026_05_11.md",
   "lines": "9",
   "quote": "IB v2.5.6 grader added DBQ stimulus_quality hard-zero (fabricated docs auto-fail) — and our model was generating BLIND to the source materials the grader checks against. Result: DBQ = 0/89 catastrophic across all v50 seeds.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/plans/PLAN-mission-2026-04-26.md",
   "lines": "59",
   "quote": "Without them, the model hallucinates dates and fails `factual_accuracy`.",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/achieved.md",
   "lines": "133",
   "quote": "Identified BAML/Gemini grader, CRITICAL_VETO_CAP=0.84, critical metrics (factual_accuracy + educational_accuracy 2× weight).",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/best_approach_analysis.md",
   "lines": "152",
   "quote": "The fix is **stricter dimension-level filters** (filter on `factual_accuracy = 1.0` per failure_taxonomy.md §5 recommendations), not the overall ≥0.95 score.",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
   "lines": "112",
   "quote": "Failure-overlap diagnostic: ZERO row_ids fail in both v8 AND v9 — v9 fixed all 9 v8 fails but introduced 11 new ones.",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/FINAL_PLAN_2026_05_11_v3.md",
   "lines": "29",
   "quote": "**Therefore**: UPLIFT-3 (constrained decode), UPLIFT-3b (per-cell schema), UPLIFT-2 (few-shot) all addressed the wrong failure mode.",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
   "lines": "16",
   "quote": "The postmortem (Apr 24) is explicit that telling the 14B \"no specific facts in scoring notes\" results in *wrong* specific facts.",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/BEADS.md",
   "lines": "607",
   "quote": "visual-artifact filter in user-prompt ineffective",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/state_training_chain_2026_05_12T1300Z.md",
   "lines": "52",
   "quote": "26 of 30 failures (87%) flag visual artifact promise/deliver mismatch",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/state_training_chain_2026_05_12T1300Z.md",
   "lines": "53",
   "quote": "Model promises \"Document 1: [a map of X]\" but only writes prose description",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
   "lines": "35",
   "quote": "IB flags these as poor stimulus quality since they describe images rather than containing text",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
   "lines": "63",
   "quote": "38 failing items classified: 76% stochastic variance (decode instability), 13% chronic DBQ veracity fails (Unit 8, D13_docs lever), 5% SFT-forget, 5% systematic fabrication.",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
   "lines": "129",
   "quote": "DBQ remains data-veracity bound — D13 real-source corpus is the unique remaining lever.",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
   "lines": "185",
   "quote": "Goodhart contamination (IB-aggregator → judge says 49% vs IB 92%, 43pp gap).",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/FINAL_PLAN_2026_05_11_v3.md",
   "lines": "135",
   "quote": "But the \"100% K=8 majority\" headline used IB-judge for both selection and grading — that's the Goodhart trap.",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
   "lines": "75",
   "quote": "IB rated v29 +20pp over v25b — Goodhart-shaped on IB.",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent-v2/ARCHITECTURE.md",
   "lines": "151",
   "quote": "5. **R5 — Verifier independence.** Verifier profile has no write to training pipeline. Period.",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/inference_clean.md",
   "lines": "78",
   "quote": "Validates correct_answer matches answer_options keys, explanation matches answer letter.",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/research/failure_taxonomy.md",
   "lines": "240",
   "quote": "**Structural failure:** the DBQ has only 4 documents instead of the required 7 (`generated_content.documents` has length 4).",
   "ok": true
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/MEMORY.md",
   "lines": "82",
   "quote": "main-A's generic 4-dim prompt missed cell-specific failure modes Oracle's BAML rubric caught — 33pp divergence on SAQ.",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/NORTH_STAR.md",
   "lines": "42",
   "quote": "One change per experiment. Single-variable diffs against v7 baseline.",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/.agent/memory/feedback_anti_regression_opposite_direction_2026_05_11.md",
   "lines": "9",
   "quote": "At most 2 knobs per iteration:",
   "ok": false
  }
 ]
}
```
