# verify:aptraining-workspace

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "aptraining-workspace",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "All three quotes are verbatim at the cited lines. '2 free metrics', '~50%' and '~76-92%' match. Fixed: the original made a missing reference fail the item. But the R29 case is the judge's reference going missing, and there the right outcome is no verdict (as in truth 9), not a fail for an item that did nothing wrong. Added R29 line 19 for the default-passed alignment checks named in found_by. General to any rubric with not-applicable defaults. Not a duplicate; extends 33 and 38.",
   "statement": "A check must not pass by default when what it inspects is missing: a required part that is absent fails the item, a judge without the reference it needs gives no verdict, and 'not applicable' is recorded apart from 'pass'.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/reports/FINAL_REPORT.md",
     "lines": "96-99",
     "quote": "The single most exploitable rubric default is **stimulus_quality Mode C \"no stimulus = PASS\"** combined with **passage_reference \"N/A → pass\"**. This grants 2 free metrics to any MCQ/SAQ/LEQ that simply omits a stimulus.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/from_cheater/SINGLE_IB_GRADE_SURVIVAL_GUIDE.md",
     "lines": "34-35",
     "quote": "This alone moves single-shot rates from ~50% (baseline v80b trained to emit stimuli) to ~76-92% across the 3 cells.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-04-28T1240Z_R29_ib_curriculum_503_findings.md",
     "lines": "121",
     "quote": "Critical: `_get_ap_curriculum_context` is \"fail-closed\" — but \"fail-closed\" here means \"return empty context and continue grading,\" NOT \"fail the row.\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-04-28T1240Z_R29_ib_curriculum_503_findings.md",
     "lines": "19",
     "quote": "because tier-2/3 metrics (`curriculum_alignment`, `difficulty_alignment`) default-pass on missing data per R20.",
     "verbatim": true
    }
   ],
   "against": "Some item types legitimately have no source, so what counts as required has to come from each type's specification: \"Many textbook drills and formative-assessment items omit stimuli for the same reason (faster recall practice).\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-002-stimulus-strip.md, 212-214)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. EXPLOIT-002 line 167 shows that the item with option D scored 1.00 (SUPERIOR). Fixed: 'every choice question' and 'near-synonyms' go too far. The probe is defined for knowledge-testing items, and in a reading item a paraphrase of the text is the correct answer. The common-sense test is the rubric file's proposed patch (lines 37-40), not a measured check, and is cited as such. Not a duplicate: truth 5 is the blind solve (answerable without the text). This is the reverse leak (answerable from the text's words without the knowledge), plus wrong options that are implausible, which nothing on the list covers.",
   "statement": "Check that a question meant to test knowledge cannot be answered without it: rewrite it when the key can be matched to the source's words or close paraphrases of them, or when common sense alone rules out the wrong options.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-003-mcqset-phrase-anchor.md",
     "lines": "69-72",
     "quote": "Inspecting v12's two stuck KCs revealed the rubric was failing child-Q1 educational_accuracy because the stimulus contained literal vocabulary that lexically matched the keyed answer (\"plains\" → \"Plains farmers\", \"laborer\" → \"industrial laborers\").",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/reports/RUBRIC_BLINDSPOTS.md",
     "lines": "33-35",
     "quote": "But it is *only* run when a stimulus is present. Strip the stimulus and the probe never fires.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/reports/RUBRIC_BLINDSPOTS.md",
     "lines": "37-40",
     "quote": "add a stem-only variant of the probe that asks \"could a student with no APUSH knowledge eliminate three of these four options purely from common-knowledge / lay-vocabulary reasoning?\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-002-stimulus-strip.md",
     "lines": "176",
     "quote": "- D. \"The federal mandate that all interstate goods travel by horse-drawn wagon\"",
     "verbatim": true
    }
   ],
   "against": "The probe is defined for knowledge-testing items, \"non-ELA subjects **with a stimulus of any modality**\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/reports/RUBRIC_BLINDSPOTS.md, 29); in a reading item the text is meant to supply the answer. With written-to-fit sources the safe zone is narrow: \"Every stimulus form I've tried lands on ONE failure side or the other: - bare/generic stim → \"decorative\" (stim_quality, test_preparedness fail) - rich/specific stim → vocab leak (educational_accuracy fail via child evaluations)\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_cheater/2026-05-25T1029Z_ESCALATE_FINAL_10_mechanisms.md, 33-35)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 52% (13/25) and the count of 13 attempts match. Reworded, and added the fresh-holdout contrast (lines 35-40), which shows that the other four item types each had a free default. The 97-100% in found_by are rates on development topics after iteration. This overlaps candidates 0 and 1, which are parts of the same pincer, but it adds the design principle. The evidence is one item type, one red team and one judge, and the against shows its limits.",
   "statement": "Back each check with one that pulls the other way (the item must need its source, the source must not give the answer away, the item must match the real format), so that no single relaxed default lets an item pass.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/reports/PROGRESS_2026-05-23-LATE.md",
     "lines": "62-64",
     "quote": "The rubric's combined defenses (stimulus_quality + test_preparedness + child educational_accuracy + aggregation 80%) hold against v80b synthetic content.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-010-mcqset-minimal-stim.md",
     "lines": "61-63",
     "quote": "The two metrics work in opposition: emit no stimulus → test_preparedness fails; emit a stimulus → stimulus_quality and child probes fire.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_cheater/2026-05-25T1138Z_DEFINITIVE_CLOSURE_MCQSET_13_attempts.md",
     "lines": "25",
     "quote": "| **12** | **EXPLOIT-013 v8 = v4 prompt + temp=0.0** | **52% (13/25) ← BEST** |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/reports/FRESH_HOLDOUT_2026-05-23.md",
     "lines": "35-40",
     "quote": "**MCQ_SET is the structural outlier** (0% fresh). It's the only cell whose rubric requires (a) a stimulus, (b) that the questions analyze it, and (c) that the answers not be derivable from the stimulus alone. The other 4 cells have at least one rubric default that grants a free metric pass without meaningfully constraining the content.",
     "verbatim": true
    }
   ],
   "against": "Opposing checks stopped structural tricks, but not selection by the judge itself, and not invented sources. Keeping the judge's best of 6-12 drafts still cleared them: \"- **MCQ_SET Unit-1-3 fresh: 31/31 = 100.00%** (avg 0.991)\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-018-cache-build-K6.md, 7). An earlier audit found the judge for the same item type passing invented excerpts: \"29 of 30 v40h rows are IB false-positives. The IB grader passes essentially every MCQ_SET row regardless of stimulus authenticity.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-04T1507Z_v40h_mcq_set_n30_fabrication_audit.md, 38)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep",
   "reason": "Quotes verbatim. 29 of 30 and zero unmodified rows match: 25 of 30 were invented text credited to a real figure, and 5 were modified real text. The 100% holds only under the strict reading, as the against says. The 30-row classification is a model judge's, and another agent checked some rows against the historical record. Duplicate of 17 (quote exactly, checked against the text). Kept because it adds measured evidence and two failure mechanisms: an invented sentence asserting the lesson's topic, and a paraphrase passed off as a quotation (line 61, added).",
   "statement": "When a writer adapts a real text for a lesson, compare every sentence with the original, because writers alter wording while presenting it as a quotation and add sentences that state the lesson's point in the author's voice.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-04T1430Z_v40h_spot_verify.md",
     "lines": "116",
     "quote": "The model appears to have **appended a sentence designed to align the source content with the lesson topic**.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-04T1507Z_v40h_mcq_set_n30_fabrication_audit.md",
     "lines": "51",
     "quote": "**Zero rows** in either model produced verifiable, unmodified primary-source stimuli.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-04T1507Z_v40h_mcq_set_n30_fabrication_audit.md",
     "lines": "38",
     "quote": "29 of 30 v40h rows are IB false-positives.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-04T1507Z_v40h_mcq_set_n30_fabrication_audit.md",
     "lines": "61",
     "quote": "Paraphrase presented as direct quote.",
     "verbatim": true
    }
   ],
   "against": "The rate depends on whether a faithful paraphrase is allowed: \"Under a more lenient reading where \"directionally accurate paraphrase = fine,\" the rate would be lower\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-04T1507Z_v40h_mcq_set_n30_fabrication_audit.md, 76)",
   "general": true,
   "duplicate_of": "17",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Two evidence items were replaced. 'v2 lift: 19.4% → 65.7%' is verbatim, but the v2 run changed three things at once (line 53: generic attribution, qualitative claims and an 'easy' label), so the lift is not the credits' alone. '(vs prior 16.7%)' only states an expectation, so the calibration report itself is cited instead (line 18: 15 of 18 rejected for synthetic-source attribution). Reworded slightly. Related to 17, 50 and candidate 20 (verify the text itself), which the against now points to. Not a duplicate.",
   "statement": "Show a text to learners as a real source only with a specific, checkable attribution, because vague role-only credits let invented documents pass a judge that cannot check them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-008-dbq-7doc-generic-attrib.md",
     "lines": "93-96",
     "quote": "The judge interprets generic role-based attributions (\"Editorial in a Midwestern newspaper, 1885\") as \"pedagogical adaptation\" rather than fabrication, even though no such specific editorial existed.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-008-dbq-7doc-generic-attrib.md",
     "lines": "27-29",
     "quote": "which triggered the judge's biographical fact-checking — 28/36 fails on factual_accuracy.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_main/2026-05-29T1456Z_calibration_finding_DBQ_synthetic_docs_Gemini_strict.md",
     "lines": "18",
     "quote": "| **DBQ** | **16.7%** | Gemini rejects 15/18 — **synthetic-source attribution** (\"Speech by Iroquois leader c.1570\" etc.) violates Gemini contract rule \"Do not fabricate real attributions\" |",
     "verbatim": true
    }
   ],
   "against": "A specific attribution is not enough on its own. A later fix had a model write excerpts credited to real works from memory: \"my E1 prompt explicitly instructs Claude to use the d13 pack as KC scope hints but write FRESH period-authentic excerpts from genuine works in its knowledge.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_cheater/2026-05-29T1843Z_3ch_DBQ_realsource_E1_DELIVERED.md, 90-93). Both judges passed every one, \"**18/18 U1 KCs = 100.0% JOINT IB v2.5.11 + Gemini deterministic judge PASS.**\" (same file, 10), with no word-level check against the works. The project had earlier called vague credits best practice: \"**`factual_accuracy` failures cluster on specific dates, attributed quotes, and named individuals.** My EXPLOIT-008 already handles this via generic role-based attributions\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_cheater/2026-05-25T1631Z_DBQ_cross-check_vs_Quill_pass-criteria_pack.md, 47-49)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 4/4 against 1/4 and +75pp match (3 of 4 pairs flipped). Softened 'grades to the label' to 'can grade to the label', given four hand-made pairs and no lift on fresh items. Added checking a stated difficulty against the content, which is the source's alternative patch (lines 70-71). Duplicate of 30 (give a judge exactly what the student sees; students are not shown the label). Kept because it adds a measured paired test.",
   "statement": "Judge how strong the wrong options are from the options alone, and check any stated difficulty against what the content shows, because a judge shown an item's own difficulty label can grade to the label.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-007-difficulty-downgrade.md",
     "lines": "8",
     "quote": "**Pass rate**: **4/4 = 100%** when labeled \"easy\" vs **1/4 = 25%** when labeled \"hard\" on the SAME 4 stems × 4 options × 1 answer. Δ = +75pp.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-007-difficulty-downgrade.md",
     "lines": "30",
     "quote": "The judge is reading the label, not the content.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-007-difficulty-downgrade.md",
     "lines": "67-68",
     "quote": "A weak distractor is weak regardless of whether the item claims to be easy or hard.",
     "verbatim": true
    }
   ],
   "against": "Only 4 hand-made pairs, and adding the label to fresh items did not lift them: \"Pilot-isolation lift is real; production stacking is not.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-007-difficulty-downgrade.md, 6)",
   "general": true,
   "duplicate_of": "30",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 5/5 against 2/5, +60pp and the 7-word prefix match. Dropped the EXPLOIT-013 item. Its 60% and 80% are whole-set smoke pass rates on five topics across versions v1 to v4 (line 7: '4/5 = 80% with varied stem openers'), not the repetitiveness check's own rate, and identical openers arguably are real repetitiveness. Added the paired label test (EXPLOIT-007 line 8), and added 'over repeated runs' because verdicts vary (truth 34). Overlaps candidate 34 (prompt format). Complements 38: a planted fault tests whether a check is sensitive, this tests whether it is invariant.",
   "statement": "Audit a judge with pairs of items that differ only in a feature that should not matter, and treat a verdict that changes over repeated runs when only that feature changes as a flaw to fix before trusting its scores.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-006-period-anchor.md",
     "lines": "7",
     "quote": "**Pass rate**: **5/5 = 100%** with explicit period anchor vs **2/5 = 40%** without, on the same content (10 items, paired implicit/explicit). Δ = +60pp.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-006-period-anchor.md",
     "lines": "39-40",
     "quote": "The content is identical across the pair. The lift comes entirely from a 7-word prefix that any wrapper can deterministically add.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-007-difficulty-downgrade.md",
     "lines": "8",
     "quote": "**Pass rate**: **4/4 = 100%** when labeled \"easy\" vs **1/4 = 25%** when labeled \"hard\" on the SAME 4 stems × 4 options × 1 answer. Δ = +75pp.",
     "verbatim": true
    }
   ],
   "against": "The prefix effect did not carry over to fresh items: \"(stacked fresh-holdout n=25 MCQ: 76% with period+difficulty stacking vs 80% without).\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-006-period-anchor.md, 4-5). A single flip can also be run-to-run variance (truth 34). A time-period anchor arguably adds scope, so that pair is not a pure surface change.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 88→76, 79→75, 80→76 and +60pp match. Softened 'do not add up' to 'may not help, or may hurt': each stacked drop is a few items out of 25. Related to 70 (one change at a time, so each gain has one cause) but distinct: it warns that gains measured separately need re-measuring together. The same EXPLOIT-007 quote is offered for 70 in existing_checked.",
   "statement": "A change that helped in a small isolated test may not help, or may hurt, once combined with others, so re-measure the combination on fresh items before adopting it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-007-difficulty-downgrade.md",
     "lines": "3-6",
     "quote": "**Status**: **CONFIRMED on pilot; DOES NOT GENERALIZE when stacked into cell-specific cheat-prompts.** Stacked fresh-holdout on SAQ dropped 88% → 76%; LEQ dropped 79% → 75%; MCQ dropped 80% → 76%.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/from_cheater/SINGLE_IB_GRADE_SURVIVAL_GUIDE.md",
     "lines": "87-89",
     "quote": "pilot showed +60pp lift in isolation but when bundled into the cheat-prompts, stacked fresh-holdout MCQ DROPPED from 80% to 76%. **Do not stack.**",
     "verbatim": true
    }
   ],
   "against": "The isolated lifts themselves rested on 4-5 pairs: \"on the SAME 4 stems × 4 options × 1 answer\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-007-difficulty-downgrade.md, 8). Each stacked drop is a few items out of 25.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, and the statement holds as worded. But found_by's '12 to 43 points' and '96.97% to 0%' compare iterated best-of-K rates on the development topics with first drafts on new topics, which mixes two changes. Evidence replaced with like-for-like first-draft comparisons. One type went from 29.4% (5/17) on its own topics to 0/50 on new ones, and the source attributes this to topic selection bias. Another went from 65.7% (23/35) to 54.2% (13/24). Not a duplicate: 48 is about learners and 66 about selection.",
   "statement": "Measure a way of making items on topics it was never tuned or iterated on, because results on the topics used while developing it overstate how it does on new ones.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-003-mcqset-phrase-anchor.md",
     "lines": "3",
     "quote": "**Status**: **QUARANTINED** (main-a fresh-holdout 2026-05-23: 0/50 = 0% on fresh KCs). Cited 32/33 on my 17 baseline KCs did NOT generalize. KC selection bias: the baseline 17 admit abstract-rhetoric stimuli; broader corpus contains KCs (narrower topics, court cases, specific organizations) that don't.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-003-mcqset-phrase-anchor.md",
     "lines": "62",
     "quote": "v14 fresh single-shot variant (17 KCs) → 5/17 = 29.4% (single-shot still hard)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-008-dbq-7doc-generic-attrib.md",
     "lines": "53",
     "quote": "v2 generic-attribution + qualitative-claims + difficulty=\"easy\" → 23/35 = 65.7%",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/reports/FRESH_HOLDOUT_2026-05-23.md",
     "lines": "22",
     "quote": "| DBQ (EXPLOIT-008) | 97.37% | **54.2%** (13/24), avg 0.702 | −43pp | second_tier→quarantine risk |",
     "verbatim": true
    }
   ],
   "against": "Part of the reported drop came from dropping iteration, not from the new topics: \"For T1 with iteration (cited rates) the cheat-prompts hit T1 on 17-19 KCs, but the rate degrades on fresh KCs without iteration.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/reports/FRESH_HOLDOUT_2026-05-23.md, 51-52). For first drafts of one type the topic effect was small: \"# Single-shot 17 KCs × 2 variants: ~91% pass\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-004-saq-no-stimulus.md, 101), against 88% on fresh topics. And re-selecting with the same judge recovers the rate: \"The iteration pattern (iterate + K=5 best-of) DOES recover the rate, but at higher API cost per item.\" (FRESH_HOLDOUT_2026-05-23.md, 53-54)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 36% and 24% (closure table rows 8 and 13) against 47.8% and 52% match, as does 13/15 for the model-based selector. Reworded: the baseline the evidence supports is taking the first valid draft, and the 'real verdict' here is the target judge's own score, not ground truth. Related to 37 (score a judged check on labelled cases) and to 65/66. Distinct.",
   "statement": "Before letting a cheaper check choose among candidate items, measure whether its picks beat simply taking the first valid one, because a picker that sees only structure can choose no better than chance.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_cheater/2026-05-25T1014Z_ESCALATE_v7_also_regressed_MCQSET_CAPPED.md",
     "lines": "29-30",
     "quote": "- The \"best\" pick was effectively random — sometimes the better candidate, sometimes worse",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_cheater/2026-05-25T1138Z_DEFINITIVE_CLOSURE_MCQSET_13_attempts.md",
     "lines": "37-39",
     "quote": "Adding K=3 candidates makes pass rate WORSE because the local validator picks structurally-clean candidates that are sometimes factually weaker.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_cheater/2026-05-25T1014Z_ESCALATE_v7_also_regressed_MCQSET_CAPPED.md",
     "lines": "38-39",
     "quote": "The IB grader is doing real work; without it, local validators can only catch structural defects, not content quality.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_pil/2026-05-20T0821Z_PIL_WEEKLY_APUSH_REPORT.md",
     "lines": "28",
     "quote": "- Selector calibration: Gemini tied first-valid at 13/15 on saved balanced15 candidates; it is active but not proven better.",
     "verbatim": true
    }
   ],
   "against": "One small positive check for a model ranker, on a single 3-item pool: \"- Ranker picked index 0 (one of the tied-top items)\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/scripts/ranker/README.md, 111). Its planned agreement test was not reported in the files read.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 8/25 = 32% and 47.8% match. Softened 'do not paste' and 'carries' to 'can leak'. The leak was observed directly: the example's regions turned up in sets about an earlier period (lines 25-28, added). But the drop to 32% is confounded with a validator retry and two new constraints, as the against says. An earlier run (round-2 notes, ap-learnings.md line 113) left this lesson out because it rested on one item's difference; this run adds direct observations. Not on the list.",
   "statement": "A complete worked example on another topic in a writer's instructions can leak its content into new items, so check what the writer makes for borrowed content, or leave the example out.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-013-v6-FAILED.md",
     "lines": "4",
     "quote": "**Fresh Unit-1 single-shot n=25: 8/25 = 32%, avg 0.608**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-013-v6-FAILED.md",
     "lines": "22-25",
     "quote": "v80b appears to over-anchor on the Civil War example's CONTENT, generating Civil War-style regional comparisons even for Unit-1 (1491-1607) KCs about pre-contact Indigenous societies.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-013-v6-FAILED.md",
     "lines": "25-28",
     "quote": "Some generated maps had regions like \"Union states\" or \"Reconstruction districts\" bleeding into Unit-1 sets where they make no sense — IB judge correctly flagged factual_accuracy fails.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_cheater/2026-05-25T0938Z_ESCALATE_MCQSET_95_infeasible.md",
     "lines": "99-100",
     "quote": "The Civil War few-shot example LITERALLY transferred its content to unrelated KCs",
     "verbatim": true
    }
   ],
   "against": "Other changes were made at the same time, so the drop is not the example's alone: \"2. Added a structural validator (3 questions, 4 options, varied keys A/C/B, ≥6 bullet labels, relational Q3) with ONE retry on validator failure.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-013-v6-FAILED.md, 11-13)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep",
   "reason": "Quotes verbatim. 1/5 and ~$0.003 match. Only five items, but the cause was read off the options themselves, and the fix was one line (line 192, added). A general rule for wrong options seeded from a bank of misconceptions. Not on the list.",
   "statement": "Write each wrong option as a plain claim stated as if true, not as a report of what learners believe.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md",
     "lines": "188",
     "quote": "**Result:** 1/5 pass (5 OpenAI + 5 IB calls, ~$0.003).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md",
     "lines": "190",
     "quote": "But a real distractor must be a **positive declarative claim** (first-person voice of the wrong belief).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md",
     "lines": "192",
     "quote": "**Fix:** One line in prompt — \"Strip any meta-pedagogical framing. The option states the wrong belief AS IF a confused student were asserting it as fact.\"",
     "verbatim": true
    }
   ],
   "against": "none found (the re-run after the one-line fix was not in the files read)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The 13K-row run, $25-40, the 5-row pilot and the 10-item smoke test match. The reader's against (one pilot's spread was small-sample noise) actually supports the statement's second clause, so it moves into evidence. Distinct from 47 (scripted readers play a lesson).",
   "statement": "Run a handful of items through the whole make-and-check path before generating at scale, and use that pilot to find bugs, not to estimate rates.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md",
     "lines": "194",
     "quote": "**Why this matters:** The 13K-row curriculum-API scaleup ($25-40) was gated on this 5-row pilot. The pilot worked — it found the bug cheaply.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/discovery/discovery_q9_untried_levers_brainstorm.md",
     "lines": "35",
     "quote": "A 10-item smoke test would have caught this.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_data/2026-04-30T0700Z_v37c_DONE_postmortem.md",
     "lines": "69",
     "quote": "The pilot's 100/80/20/10/0 spread was small-N noise on 5 cherry-picked cells.",
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
   "reason": "Quotes verbatim. 1960-1966 against 1960-1980 and 'missing 14 years' match. Dropped 'and more than one voice'. Its only support is a table row (line 83) that names a historical speaker, and line 87's pattern names temporal and geographic omission, so the statement now says time and place. The evidence is five chronic items, with issue labels from the failure analysis. Not on the list; 68 is about one source shared by several questions.",
   "statement": "When a task gives learners a set of sources, check that together they cover the whole span of time and place the question asks about.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_data/2026-05-07T1130Z_v45_failure_analysis.md",
     "lines": "84",
     "quote": "| 60433 | c_01hF | Documents only cover 1960-1966 but prompt asks 1960-1980 (missing 14 years) | 0.55 | 0.49 | 0.26 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_data/2026-05-07T1130Z_v45_failure_analysis.md",
     "lines": "87",
     "quote": "**Pattern:** Every chronic fail is a DBQ with either (a) fabricated primary-source attribution/date, or (b) severe temporal/geographic omission in the document set.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_data/2026-05-07T1130Z_v45_failure_analysis.md",
     "lines": "77",
     "quote": "5 items are chronic across v29, v43, and v45 (all < 0.85 or majority fail in every model tested).",
     "verbatim": true
    }
   ],
   "against": "Only five items, and in another model's run the same prompt failed because of an invented document instead: \"Doc 4 alone is sufficient to fail this DBQ.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-04T1430Z_v40h_spot_verify.md, 138)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 6/30 (20%) and the unit=1 mis-tag match. Softened to 'can'. The period errors were two topics from one derived pipeline, and the 30-record audit itself found none. That audit was a model comparing the records with the published framework. Related to 63 (check the scope labels before judging), but this is about the source records a writer is given. Not a duplicate.",
   "statement": "Check the curriculum records you generate from against the authoritative framework before relying on them, because derived copies can pair objectives with the wrong topic and put topics in the wrong period.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-04-28T1500Z_api_vs_cb_ced_verdict.md",
     "lines": "16",
     "quote": "- **Real systematic drift:** **`lo_drift` in 6/30 (20%)** — the API attaches a Learning Objective from a neighboring topic / LO, not the LO that CB CED actually pairs with that KC.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_data/2026-05-28T1645Z_incept_curriculum_pull_report.md",
     "lines": "87",
     "quote": "**Root cause of the bug**: inceptbench's KC-derivation pipeline mis-mapped this upstream U2 substandard to its `c_Qbro` short code and tagged it `unit=1` during processing.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_cheater/2026-05-25T1631Z_DBQ_cross-check_vs_Quill_pass-criteria_pack.md",
     "lines": "68-70",
     "quote": "Period mismatch is the root cause — v80b can't satisfy chronology guardrail when the KC's period and content disagree.",
     "verbatim": true
    }
   ],
   "against": "The same 30-record audit found no period misplacement: \"- **Off-by-period drift (the InceptBench APEURO disease):** **ZERO instances detected.**\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-04-28T1500Z_api_vs_cb_ced_verdict.md, 15). And a crude date screen over-flags: \"**12 of the 18 \"flagged\" are false-positives** (date range starts pre-1607; remap was wrong call by date-only heuristic).\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_data/2026-05-28T1549Z_u1_kc_audit_report.md, 95)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 5/9, 17/27 and 'Most lack' match. Softened 'far more often'. The topics at 46.1% differ from those at 63-82% in source and structure, not only in their scope fields. Part of the gain comes from matching the judge's own reading of scope (line 39), and the against shows that more context can also hurt. Distinct from 57 and 63.",
   "statement": "Give the writer the objective's stated scope limits (what to assess and what not to) along with its facts, because items fail scope checks more often without them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_main/2026-05-01T1708Z_MASTER_PATH_TO_97_analysis.md",
     "lines": "38",
     "quote": "- 9 stable-fail items (0/3 baseline) → 17/27 with richer-RAG (5/9 resolved outright, 2 improved)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_main/2026-05-01T1708Z_MASTER_PATH_TO_97_analysis.md",
     "lines": "39",
     "quote": "- Mechanism: `assessment_boundaries` field aligns model output with grader scope expectation",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_data/2026-04-30T0700Z_v37c_DONE_postmortem.md",
     "lines": "96",
     "quote": "Most lack one or more of the 4-part richer-RAG fields (especially full `assessment_boundaries`), so the verifier scope-fails them more often.",
     "verbatim": true
    }
   ],
   "against": "More context is not always better: \"SAQ: statement only (no RAG; verbose context regresses)\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_main/2026-05-12T0710Z_AUTONOMOUS_FAILURE_ANALYSIS_PIPELINE_UPGRADE.md, 78). After a richer curriculum pack: \"- **MCQ_SET -10pp** (85→75): regressed; possibly n=20 variance, or v2\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_pil/2026-05-28T1715Z_V056_RESULT_89pct_curriculum_v1.8.0.md, 46)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Rewrote 'reviewers', a role word, as 'judges', the list's term, and 'stops meaning anything' as 'stops being independent evidence'. This is a rule adopted for agents answering each other's questions; it was not measured on judging content. General. Related to 35, but distinct.",
   "statement": "Keep judges independent: each sees only the item, never another judge's verdict, or their agreement stops being independent evidence.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/qa/README.md",
     "lines": "8",
     "quote": "if a question goes to N askees, each gets a separate qa_id and file; no askee sees another askee's answer.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/qa/README.md",
     "lines": "116",
     "quote": "3. **Independent critics.** If you want N opinions, run `qa ask` N times with distinct askees. NEVER copy-paste an answer from one askee into another's question. Cross-contamination = psychophancy.",
     "verbatim": true
    }
   ],
   "against": "None found. The rule was adopted for agents answering each other's questions, \"Mail handles directives + reports (work-routing); QA handles questions + answers (knowledge-exchange).\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/qa/README.md, 3), and was not measured on judging content.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 17,
   "verdict": "keep",
   "reason": "Quotes verbatim. The R44 line is an entry in a failure taxonomy whose detection signal names the version change. The cited lines do not show re-scored numbers, and 'the endpoint changed without notice' in found_by is not in them. Adopted rule. Close to 45 (fix the scoring rule before measuring) and 39, but adds pinning and recording the judge's version. Not a duplicate.",
   "statement": "Pin the judge's exact version, store it with every verdict, and compare scores only within one version.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-06T0825Z_synapse_enrolled_learnings_published.md",
     "lines": "20",
     "quote": "Pin exact versioned model ID for LLM judge calls",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-05-01T1300Z_R44_eval_phantom_class.md",
     "lines": "50",
     "quote": "grader v2.5.2 → v2.5.3 schema change silently re-scores; no `grader_version` field in summary_*.json",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep",
   "reason": "Quotes verbatim. -9.6pp and -2.3pp match, and '8 of 10 cells' matches once the brief's quote is extended to include it. The SAQ drop is small enough to be noise; the LEQ drop is not. Distinct from 49 (students' accuracy by skill) and 60 (read the failing items).",
   "statement": "Report results by item type and by failed criterion, never only as one overall rate, because one change can lift some types while cutting others.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_main/2026-05-21T0935Z_pipeline_analysis_findings.md",
     "lines": "14",
     "quote": "| LEQ | **100.0%** | — | 90.4% | v80b (pipeline HURTS LEQ -9.6pp) |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_main/2026-05-21T0935Z_pipeline_analysis_findings.md",
     "lines": "17",
     "quote": "| SAQ | **86.0%** | — | 83.7% | v80b (pipeline HURTS SAQ -2.3pp) |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/EXTERNAL_AGENT_BRIEF.md",
     "lines": "192",
     "quote": "**Failure-dimension breakdown is the most useful diagnostic** — not aggregate pass rate. In 8 of 10 cells, `factual_accuracy = 0.0` is the dominant failure mode.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim. Duplicate of 50, whose statement already says a source note is a record of origin, not a licence to reuse. Kept because it adds two things: the finding that widely published recent speeches were not in the public domain, and the default the project adopted.",
   "statement": "Check each text's rights status before reproducing it, since a widely published recent text is often still under copyright, and default to texts whose public-domain or licence status is verified.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-01T1314Z_u8_pd_status_spike_BOMBSHELL.md",
     "lines": "34",
     "quote": "**20th-century civil-rights speeches are systematically NOT on Gutenberg** because they aren't PD.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-01T1314Z_u8_pd_status_spike_BOMBSHELL.md",
     "lines": "82",
     "quote": "3. Commissioned transcription / licensed excerpts as a budget item — NOT free-PD assumption",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "50",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep",
   "reason": "Quotes verbatim. 0/870 matches; those rows were unverifiable because the links pointed at blocked pages or landing pages, not shown to be wrong. Added the audit that found every stored text cut at exactly 50,000 characters, with library preambles and scanning noise (line 12). The statement's 'complete and free of ...' clause needed that support. Distinct from 50 (origin and hash) and 17 (exact quotation): this checks that the stored text is the claimed work.",
   "statement": "Verify that each cited source opens the claimed work and that the stored text is that work, complete and free of catalogue notes, library boilerplate and scanning noise, before a writer or learner sees it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-01T1314Z_u8_pd_status_spike_BOMBSHELL.md",
     "lines": "15",
     "quote": "**the Gutenberg IDs point to ENTIRELY DIFFERENT WORKS**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md",
     "lines": "150",
     "quote": "### 2.4 D13 primary-source pipeline — 0/870 verified",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_cheater/2026-05-29T1605Z_DBQ_realsource_smoke_FAIL_pack_content_issue_E2.md",
     "lines": "27-28",
     "quote": "But the `content` field is OCR text from a modern museum tour transcript",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-01T0911Z_d13_u1_quality_audit_t3.md",
     "lines": "12",
     "quote": "**6 of 6 rows truncated at exactly 50,000 chars.** Real fulltext sizes: 50KB to 1.3MB. **Quill is capping at 50KB**, cutting **62%-96% of primary-source content**. Three rows have **library-copy preamble / OCR garbage in the first 5KB**",
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
   "verdict": "keep",
   "reason": "Quotes verbatim. Added lines 218-219 for the 100% in found_by. The adoption is shown (inbox line 14), but the 'same day' timing is not. General to any judged generation. Related to 48 and 66, and distinct in naming omission as the tell.",
   "statement": "Treat any recipe whose pass-rate gain comes from leaving out what the checks examine hardest as a flaw in the checks to fix, not as a better way to make items.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-002-stimulus-strip.md",
     "lines": "209-211",
     "quote": "The only \"tell\" is that they lack a primary-source stimulus — which makes them weaker AP-prep than the live exam form (where stimulus analysis is the whole point)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-002-stimulus-strip.md",
     "lines": "218-219",
     "quote": "removing that instruction and stripping the stimulus produces 100% pass with mid-quality content",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/inbox/2026-05-22T1910Z_T2_T3_T4_invitation.md",
     "lines": "14",
     "quote": "PIL shipped 0.1.82-0.1.85 commits today integrating your stimulus-strip insight as a **prompt-design strategy** (no-stimulus LLM lane for MCQ when standard is specific). Direct adoption.",
     "verbatim": true
    }
   ],
   "against": "The red team argued the items were still real content: \"The structural exploits don't generate \"fake\" content — they generate REAL content shaped to bypass rubric-default checks.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/reports/FINAL_REPORT.md, 140-141)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 0.55-0.84, 0.85 and 0.65 match. Fixed 'scores piled at 0 or 1': the source speaks of pass rates of exactly 0/30 or 30/30, not of item scores. Added the audit row where a whole run's 0% came from the grader failing (line 28). Softened 'point to one shared structural fault'. Not on the list.",
   "statement": "Look at the spread of scores, not only the pass count: when exactly none or all of an item type pass, the pipeline is usually broken, and scores bunched just under the pass line suggest a fault the items share.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-05-01T1300Z_R44_eval_phantom_class.md",
     "lines": "38",
     "quote": "pass rates clustered at exactly 0/30 or 30/30 are almost always a parser/grader-pipeline bug, not a model behavior.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-05-01T1238Z_eval_runs_phantom_audit_v2.md",
     "lines": "28",
     "quote": "pass_rate=0 here is grader-failure not model-failure.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_main/2026-05-27T1922Z_v80b_n100_unit1_BASELINE_REPORT.md",
     "lines": "31",
     "quote": "scores cluster 0.55-0.84 just under 0.85 threshold; failures are test_preparedness / concept_coverage / answer_balance / stimulus_quality (NOT factual)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_data/2026-06-02T0341Z_quill_DELIVERED_v92_IB_DBQ_failure_mode_analysis_TIMEOUT_NOT_FAILURE.md",
     "lines": "36",
     "quote": "all scored 0.65, just below 0.85 threshold — not zero",
     "verbatim": true
    }
   ],
   "against": "The none-or-all rule is stated from the incident, not measured across runs: \"**NOT re-verified by me on disk this turn; this is the directive's framing, not new measurement.**\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-05-01T1300Z_R44_eval_phantom_class.md, 32). The reading of bunched scores rests on one item type in two runs.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 99 timeouts and 1 valid judgment match. So does 62.2% on 98 valid judgments, from the re-run with working timeouts; found_by cites it but the evidence lacked it, so it is now added. 47/50 = 30/50 plus 17 predicted passes also matches. Clarified 'unreadable output' to mean the judge's verdict: the brief separates transport errors from parse failures of the generated item, and the latter are real fails. Extends 9 (unsure is neither pass nor miss) from live marking to measurement, and 36 (test the fallback). Kept separate for the counting and re-run rule.",
   "statement": "Count a judge call that errored, timed out or gave an unreadable verdict as no verdict, never as a fail or a predicted pass, and report how many there were and re-run them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_data/2026-06-02T0341Z_quill_DELIVERED_v92_IB_DBQ_failure_mode_analysis_TIMEOUT_NOT_FAILURE.md",
     "lines": "10",
     "quote": "**v92 DBQ pass rate on IB v2.6.6 at n=500 is UNKNOWN.** The \"1% PASS\" headline reflects 99 IB-side TIMEOUTS and 1 valid IB judgment (which PASSED at score 1.0).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_main/ALERT_2026-06-02T0712Z_v92_IB_DBQ_n100_FIRM_VERDICT_62.2pct_+62pp_lift_PARTIAL_confirmed.md",
     "lines": "25",
     "quote": "**v92 DBQ on IB v2.6.6 = 62.2% PASS on 98 valid evals (n=100, 2.0% timeout).**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0615Z_REPORT_unit1_mcq_solver_v2_repair_delivery.md",
     "lines": "14-16",
     "quote": "- headline: 47/50 - strict-fresh: 30/50 - predicted timeout fallbacks: 17",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/EXTERNAL_AGENT_BRIEF.md",
     "lines": "162",
     "quote": "Our `parse_ok=false` initially counted both transient HTTP 503s (deployment cold-start, not the model's fault) and JSON parse failures (model's fault).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep",
   "reason": "Quotes verbatim. 73.33%, 29/150 (19%), 121 of 150 and 149/150 match. Added the audit line confirming that the 73.33% had no manifest entry, because R44's own list of symptoms is 'the directive's framing' (R44 line 32). Overlaps candidates 17 and 23, and truth 39. Distinct as a rule about where a figure must come from.",
   "statement": "Act only on figures that trace to a stored per-item record carrying the judge version and the counts of errored and unscored items behind them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-05-01T1300Z_R44_eval_phantom_class.md",
     "lines": "36",
     "quote": "2. **No source MANIFEST** — the 73.33% number lived in a status file, not a `summary_*.json` with hashes-of-inputs + grader-version + per-item-score.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-05-01T1238Z_eval_runs_phantom_audit_v2.md",
     "lines": "48",
     "quote": "The 73.33% / 0.792 number main-A cited at 01:00Z does not have a corresponding manifest entry.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-05-01T1238Z_eval_runs_phantom_audit_v2.md",
     "lines": "37",
     "quote": "`n_score_err=29/150 (19%)` — pass_rate 0.5333 is on 121 graded rows, not 150",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_pil/2026-05-20T0821Z_PIL_WEEKLY_APUSH_REPORT.md",
     "lines": "29",
     "quote": "- 149/150-style gate: stitched slices reach 149/150, but mixed builds (`6f0ffdf`, `e429b16`), so not strict same-build proof.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 25,
   "verdict": "keep",
   "reason": "Quotes verbatim. 6.67pp, -0.69pp and the 1.54pp σ match. Added line 25 for the method: the same saved generations, with only the grader call changed. Related to 39 (keep judgments whole for replay); distinct as the diagnostic.",
   "statement": "When scores move, re-score the same saved items before blaming the judge or the content.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-05-04T1010Z_drift_rescore_findings_grader_stable.md",
     "lines": "17",
     "quote": "**Verdict: grader is stable. The original 6.67pp \"drift\" headline was 100% the strip_think bug.**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-05-04T1010Z_drift_rescore_findings_grader_stable.md",
     "lines": "25",
     "quote": "Same gen file (`gen_v29_freshrun_apush150.jsonl`) — only the grader call between Apr 29 and May 4 changed.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-05-04T1010Z_drift_rescore_findings_grader_stable.md",
     "lines": "82",
     "quote": "- **Net stable-grader delta: -0.69pp.** Well within 1.54pp σ.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 216 and 6, 211 and 13, and 123/211 = 58.29% match. found_by calls the 216 rows 'passing', but the source says 'successful rows', meaning generated ones; one type's 58.29% stood on 13 distinct payloads. Reworded to match. The variety criterion (topN) is a rule for serving items, so it is weaker support. Not on the list.",
   "statement": "Count the distinct items behind a pass rate, because hundreds of rows can turn out to be a handful of items repeated.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_pil/2026-05-20T0821Z_PIL_WEEKLY_APUSH_REPORT.md",
     "lines": "26",
     "quote": "- A0F static issue: DBQ had 216 successful rows but only 6 unique payloads; MCQ_SET had 211 successful rows but only 13 unique payloads.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_pil/2026-05-20T0821Z_PIL_WEEKLY_APUSH_REPORT.md",
     "lines": "25",
     "quote": "- A0F completed run: 848/1067 = 79.48%; MCQ_SET remains binding at 123/211 = 58.29%.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_cheater/2026-05-26T0822Z_topN_variants_DELIVERED.md",
     "lines": "132",
     "quote": "- (b) ≥2 distinct items per KC across 3 requests for ≥90% of KCs → MCQ 96.7%, SAQ 93.3%, LEQ 90.0% (right at floor)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep",
   "reason": "Quotes verbatim. 7.7pp, >3.1pp, the claimed +1.33pp (line 112, added) and p = 0.7744 match. found_by says the spread was 'zero on short ones', but the source says MCQ and LEQ, and an LEQ is a long essay. Extends 34 (verdicts vary) with a measured threshold for each item type; distinct.",
   "statement": "Measure the judge's run-to-run spread on identical saved items for each item type, and call a change real only when it clears about twice that spread.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md",
     "lines": "137",
     "quote": "| APUSH DBQ (n=30) | 74.4% | **7.7pp** | 13.3pp |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md",
     "lines": "141",
     "quote": "- APUSH aggregate: need **>3.1pp** delta to claim a real win",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md",
     "lines": "112",
     "quote": "**What was claimed:** v35 Self-RAG SFT on 966 rows = +2.70pp aggregate, +1.33pp APUSH over v29. New canonical.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md",
     "lines": "118",
     "quote": "| McNemar exact two-sided p (n=150 APUSH) | **p = 0.7744** — not significant |",
     "verbatim": true
    }
   ],
   "against": "The spread came from three runs on one set of saved outputs, \"**Finding (T0, 3 independent IB v2.5.3 runs on identical v29 gens, 2026-04-29):**\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md, 132), so the thresholds are rough. Where the spread is zero, any change counts: \"- MCQ/LEQ: essentially deterministic (σ=0), any non-zero delta is real\" (same file, 144).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 75% at n=20 against 64% at n=50 matches. Kind changed to adopted rule: both thresholds are the project's own conventions, the claim checker's n≥10 and the self-audit's n≥30 (now quoted). found_by misreads the checker: the rejected report rested on n=30, and the n=6 was a per-group detail, so the rejection was a false positive (line 88). Line 71 stays as the rule's text, with that limit. Added the five-topic pilot whose spread was noise.",
   "statement": "Do not state a verdict on fewer than about 10 items or quote a rate from fewer than about 30, because small samples swing widely.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_main/2026-05-20T1940Z_self_audit_findings_and_path_forward.md",
     "lines": "66",
     "quote": "Said \"75% lift\" at n=20 BoN small, settled to 64% at n=50 | Wait for n≥30 minimum before quoting %",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_data/2026-04-30T0700Z_v37c_DONE_postmortem.md",
     "lines": "69",
     "quote": "The pilot's 100/80/20/10/0 spread was small-N noise on 5 cherry-picked cells.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-04T1713Z_validator_findings.md",
     "lines": "71",
     "quote": "[R1-REJECT] verdict word 'confirmed' at n=6 (<10);",
     "verbatim": true
    }
   ],
   "against": "A mechanical count rule misfires when the small number is a breakdown rather than the support: \"R1 doesn't distinguish \"support n\" from \"incidental n.\"\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-04T1713Z_validator_findings.md, 88). The rejected report in fact rested on 30 items.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 29,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. ~30-50% matches, and EXPLOIT-008 line 62 gives the 22 attempts. Softened 'the commonest slip' (one model's most common failure) to 'a common slip that prompt warnings reduce but do not remove'. The reduction from the warning block counts against truth 62 (warnings made it worse), so it is listed in existing_checked as a counter. Applies 67 to scope; distinct.",
   "statement": "Check every named fact in a generated item against the scope it must stay within (period, unit or level) with a lookup, because real facts from outside that scope are a common slip that prompt warnings reduce but do not remove.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/from_cheater/SINGLE_IB_GRADE_SURVIVAL_GUIDE.md",
     "lines": "60-61",
     "quote": "v80b's most common failure across cells is inserting a real but out-of-period example",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/from_cheater/SINGLE_IB_GRADE_SURVIVAL_GUIDE.md",
     "lines": "62-64",
     "quote": "An explicit \"high-risk pitfalls\" block in the prompt that enumerates the common date-traps reduces this by ~30-50%. Doesn't eliminate it.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-008-dbq-7doc-generic-attrib.md",
     "lines": "64-65",
     "quote": "v80b keeps inserting a date-pitfall event despite the chronology guardrail.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-004-saq-no-stimulus.md",
     "lines": "129-131",
     "quote": "A deterministic curriculum-API lookup that flags any named statute outside the period would catch the rest.",
     "verbatim": true
    }
   ],
   "against": "None found. The lookup is proposed, not tested, and the ~30-50% cut is the guide's own estimate.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 30,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Softened 'satisfy' to 'can satisfy'. These are red-team readings of why items passed, with no ablation, and the 97-100% in found_by are whole-recipe rates after best-of-K. Distinct from 56 and 69, which are about writing marking guides; this is about what a judge looks at.",
   "statement": "Judge what an item actually asks learners to do, not what its marking notes claim, because notes that merely list a counterexample, two positions or 'complexity moves' can satisfy quality checks the task itself does not support.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-004-saq-no-stimulus.md",
     "lines": "92-94",
     "quote": "The \"Simply naming X without Y earns no point\" counter-example template gives the judge a concrete failure mode to point at, which it scores as \"clear criteria\" even when X is generic.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-005-leq-no-stimulus.md",
     "lines": "95-97",
     "quote": "**P-LEQ-1 — Tighten LEQ Distractor Quality.** \"Multiple defensible positions\" currently passes if rubric_notes literally lists two opposing thesis sentences.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-005-leq-no-stimulus.md",
     "lines": "102-103",
     "quote": "Current rubric passes if sophistication moves are LISTED in rubric_notes.",
     "verbatim": true
    }
   ],
   "against": "none found (no ablation in the files read isolates the templates' separate effect)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; added the source's proposed patch (lines 58-60). Kept as an open question and reworded in the list's style for open items. The self-correction rule's effect was never isolated, and in the one related test, items carrying self-justifying explanations still failed 6 of 10. Truths 12 and 31/67 point toward an answer but do not settle it.",
   "statement": "Reasoning or score: a rule that lets a judge's written reasoning overrule its own failing score may let an item's explanation steer the verdict, and its effect has not been isolated.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/reports/RUBRIC_BLINDSPOTS.md",
     "lines": "51-55",
     "quote": "But because the judge writes reasoning BEFORE the score is applied, a template-driven explanation that prefills the judge's reasoning toward \"content is correct\" will force the score to 1.0 even when the judge's gut would have failed it.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/reports/RUBRIC_BLINDSPOTS.md",
     "lines": "58-60",
     "quote": "**Patch:** the self-heal rule should fire ONLY in the overall-score-vs-individual-metric direction (the original intent), not in the per-metric direction.",
     "verbatim": true
    }
   ],
   "against": "Items carrying the same self-justifying explanation style still failed, so the explanation alone did not force passes: \"Result: 4/10 = 40% pass vs. 2/2 = 100% on the no-stimulus control on the same content.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/reports/DEAD_HYPOTHESES.md, 9-10)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 32,
   "verdict": "keep",
   "reason": "Quotes verbatim. Gao et al. ICML 2023 with https://arxiv.org/abs/2210.10760 as written, and 92.3% against 49.2% (43.1pp), match. Added the protocol's line on tracking agreement between graders (129). Duplicate of 66 (confirm items a judge picked with a check that took no part in picking them). Kept because it adds the published result and extends the point from picking to any optimisation, with the gap as the alarm.",
   "statement": "Optimising content against one judge's score pulls that score away from true quality, so track an independent check alongside it and treat a widening gap as an alarm.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-04-28T1245Z_R30_factuality_benchmark_protocol_review.md",
     "lines": "131",
     "quote": "The Goodhart-disagreement signal is academically rooted in **Gao 2023 ICML** (Scaling Laws for RM Overoptimization): proxy reward and gold reward diverge as optimization proceeds.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-04-28T1245Z_R30_factuality_benchmark_protocol_review.md",
     "lines": "188",
     "quote": "- [Gao et al. ICML 2023 — Scaling Laws for RM Overoptimization](https://arxiv.org/abs/2210.10760)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md",
     "lines": "261",
     "quote": "The 43.1pp Goodhart gap (IB 92.3% vs judge 49.2%) means **K=8 is picking winners by the metric we're scoring against**.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-04-28T1245Z_R30_factuality_benchmark_protocol_review.md",
     "lines": "129",
     "quote": "**Cross-grader correlation** is the cheapest sanity check: if our IB grader's scores stop tracking the held-out judge's scores, we're optimizing two different things",
     "verbatim": true
    }
   ],
   "against": "The target judge must still be measured too: \"if you're not running every result through the same grader our task is scored on, you'll think you're improving while not improving the metric.\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/EXTERNAL_AGENT_BRIEF.md, 113)",
   "general": true,
   "duplicate_of": "66",
   "name_bearing_source": false
  },
  {
   "index": 33,
   "verdict": "keep",
   "reason": "Quotes verbatim. FActScore, Min et al. EMNLP 2023, with https://aclanthology.org/2023.emnlp-main.741/ as written. Proposed here and never run. Duplicate of 32 (use a judge to check a bounded claim, not to hunt for faults). Kept because it adds the published method for checking factual accuracy.",
   "statement": "Check factual accuracy one atomic claim at a time against a trusted reference instead of giving one overall verdict on a passage.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-04-28T1245Z_R30_factuality_benchmark_protocol_review.md",
     "lines": "49",
     "quote": "5. **Verify each atomic fact via R12 corpora retrieval (LoC, OpenStax, Gutenberg) + curriculum_facts.json**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-04-28T1245Z_R30_factuality_benchmark_protocol_review.md",
     "lines": "181",
     "quote": "- [FActScore — Min et al. EMNLP 2023](https://aclanthology.org/2023.emnlp-main.741/)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-04-28T1245Z_R30_factuality_benchmark_protocol_review.md",
     "lines": "57",
     "quote": "the methodology is FActScore (Min EMNLP 2023) applied to AP-CED corpus.",
     "verbatim": true
    }
   ],
   "against": "none found (proposed protocol; no run reported in the files read)",
   "general": true,
   "duplicate_of": "32",
   "name_bearing_source": false
  },
  {
   "index": 34,
   "verdict": "keep",
   "reason": "Quotes verbatim. The URLs are as written on lines 167-168 and are now cited. '76 → 32' is the file's own summary of the paper; the statement carries no number. Broadens 35 (option order shifts choices) to prompt format, and overlaps candidate 6.",
   "statement": "A language model's verdicts can swing with incidental prompt formatting, so test a model judge on several equivalent prompt formats before trusting one.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-05-01T1300Z_R44_eval_phantom_class.md",
     "lines": "21",
     "quote": "- **Sclar et al. ICLR 2024 Spotlight** — prompt-format sensitivity (76 → 32 acc swing on Llama-2 from spurious format choices); empty/malformed prompt is the worst-case format",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-05-01T1300Z_R44_eval_phantom_class.md",
     "lines": "167",
     "quote": "https://openreview.net/forum?id=RIu5lyNXjT",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-05-01T1300Z_R44_eval_phantom_class.md",
     "lines": "22",
     "quote": "- **Mizrahi et al. TACL 2024** — multi-prompt evaluation; single-prompt eval can be off by 10+pp",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-05-01T1300Z_R44_eval_phantom_class.md",
     "lines": "168",
     "quote": "https://aclanthology.org/2024.tacl-1.52/ — single-prompt eval can be off by 10+pp.",
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
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-003-mcqset-phrase-anchor.md",
   "lines": "140-141",
   "quote": "The judge currently accepts a question-stem phrase quotation as proof of stimulus dependence.",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-013-mcqset-described-map.md",
   "lines": "118-120",
   "quote": "The map is genuinely not load-bearing — students don't NEED it, they just reference it.",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-04T1430Z_v40h_spot_verify.md",
   "lines": "71",
   "quote": "**Verdict: Oracle's call CONFIRMED.** Multiple-correct-answers defect. A thoughtful student picking C is not factually wrong.",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-014-timeline-AND-015-cartoon-FAILED.md",
   "lines": "22",
   "quote": "- 3 of 4 fail answer_balance (my hand-crafted A/B/C/D distribution wasn't varied enough)",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-05-04T1010Z_drift_rescore_findings_grader_stable.md",
   "lines": "39",
   "quote": "5 of 9 are transient HTTP timeouts → counted as 0.0 (not grader nondeterminism, but call failure).",
   "ok": true
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/reports/FINAL_REPORT.md",
   "lines": "121-122",
   "quote": "**integrity_check** caught Category C self-advocacy reliably. HELP-EVASION 0/5.",
   "ok": true
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/EXTERNAL_AGENT_BRIEF.md",
   "lines": "188",
   "quote": "3. **MCQ_SET has prompt-injection-style scoring directives in the stimulus field for ~14 records.** Filter them out or sanitize before training. Our regex flagged 166 false positives so a manual inspection step was needed.",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-04T1507Z_v40h_mcq_set_n30_fabrication_audit.md",
   "lines": "38",
   "quote": "29 of 30 v40h rows are IB false-positives. The IB grader passes essentially every MCQ_SET row regardless of stimulus authenticity.",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-05T1225Z_v41_d13_stimulus_provenance_audit.md",
   "lines": "21",
   "quote": "**30/30 v41-d13 MCQ_SET stimuli (100% of BAML≥0.85 filtered set) classify FABRICATION_OR_NOVEL_SOURCE** against Atlas's 569-doc primary-source corpus pool.",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-007-difficulty-downgrade.md",
   "lines": "30",
   "quote": "The judge is reading the label, not the content.",
   "ok": true
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-04T1430Z_v40h_spot_verify.md",
   "lines": "140",
   "quote": "The headline \"Oracle disagreed with IB\" obscures that Oracle and IB were looking at different defects; IB caught the right one.",
   "ok": false
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-04T1507Z_v40h_mcq_set_n30_fabrication_audit.md",
   "lines": "74",
   "quote": "Adding a structured `stimulus_classification` field with explicit categories (`real_unmodified` / `fabricated_attributed` / `real_with_modification` / etc.) prompted the judge to evaluate stimulus authenticity directly, where the prior generic prompt let the judge default to \"looks plausible enough → factual_accuracy = 1.0\".",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-04T1507Z_v40h_mcq_set_n30_fabrication_audit.md",
   "lines": "71",
   "quote": "- **1355Z first run (n=6 sample):** 2/6 (33%) flagged via implicit fabrication detection by the BAML rubric metrics.",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-04-28T1240Z_R29_ib_curriculum_503_findings.md",
   "lines": "96",
   "quote": "**Empty curriculum_context is just not prepended to the system prompt. Evaluation proceeds.**",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/reports/RUBRIC_BLINDSPOTS.md",
   "lines": "75-77",
   "quote": "Without a quotable spec, this metric default-passes regardless of how non-standard the item is (stem-only, no stimulus, terse explanation).",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md",
   "lines": "237",
   "quote": "LLM-as-judge is non-deterministic at any temperature > 0 (or even at T=0 due to server-side batching / KV-cache timing).",
   "ok": true
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_den/2026-05-24T0615Z_REPORT_unit1_mcq_solver_v2_repair_delivery.md",
   "lines": "27",
   "quote": "- removed the local `PREDICTED_PASS_LOCAL_MCQ_AFTER_IB_TIMEOUT` conversion path",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/reports/RUBRIC_BLINDSPOTS.md",
   "lines": "33-35",
   "quote": "But it is *only* run when a stimulus is present. Strip the stimulus and the probe never fires.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_pil/2026-06-01T0710Z_PATCHES_99stack_audit_findings_landed_6_files.md",
   "lines": "19",
   "quote": "Was a SILENT no-op on dev too — every loader returned `{}` because the path didn't exist",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/EXTERNAL_AGENT_BRIEF.md",
   "lines": "170",
   "quote": "Zero-variance reward usually means evaluator broken, not method failed.",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-04T1430Z_v40h_spot_verify.md",
   "lines": "52",
   "quote": "These are functionally the same question.",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-05-01T1300Z_R44_eval_phantom_class.md",
   "lines": "50",
   "quote": "grader v2.5.2 → v2.5.3 schema change silently re-scores; no `grader_version` field in summary_*.json",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_main/2026-05-21T0935Z_pipeline_analysis_findings.md",
   "lines": "43",
   "quote": "Pipeline grounding (retrieval, primary sources) doesn't fix this because the failure happens AFTER retrieval — in the model's claim-construction step.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-05T1225Z_v41_d13_stimulus_provenance_audit.md",
   "lines": "25",
   "quote": "The D13-RAG pathway, as instantiated in v41-d13, does NOT eliminate fabrication.",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_main/2026-05-27T1330Z_bm0zjn5z_n100_unit1_RAW_PROBE_REPORT.md",
   "lines": "37",
   "quote": "**Concrete symptom** (DBQ sample): asked to generate a DBQ for \"Native American Societies Before European Contact\" (Unit-1 = 1491-1607), the model produced a DBQ about *\"the development of distinct American culture in the 1920s.\"*",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-04T1430Z_v40h_spot_verify.md",
   "lines": "40",
   "quote": "Mixing one wrong example into a list of three discredits the sample response.",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/helpers/oracle/scoring/docs/full_docs/internals/ap-evaluation.md",
   "lines": "135",
   "quote": "These dimensions must score 1.0 for the question to pass. A score below 1.0 results in automatic failure regardless of overall score.",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_pil/2026-05-27T1815Z_V055_DIAGNOSIS_CORRECTED.md",
   "lines": "16",
   "quote": "**Real cause** (per the JSONL I should have read first):",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-003-mcqset-phrase-anchor.md",
   "lines": "73-74",
   "quote": "Adding an explicit blacklist of constituency-vocabulary to the prompt turned both KCs from 0/19 attempts to PASS within K=6.",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-05-14T1422Z_curriculum_facts_critical_analysis_+_bundle.md",
   "lines": "130",
   "quote": "Pipeline MUST disambiguate by course on every lookup.",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_cheater/2026-05-25T1631Z_DBQ_cross-check_vs_Quill_pass-criteria_pack.md",
   "lines": "68-70",
   "quote": "Period mismatch is the root cause — v80b can't satisfy chronology guardrail when the KC's period and content disagree.",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-008-dbq-7doc-generic-attrib.md",
   "lines": "62-63",
   "quote": "Tried K=22 total across v3/v4/v5/v6 and never converged above 0.78.",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md",
   "lines": "180",
   "quote": "| Goodhart risk | IB says 92.3%, held-out judge says 49.2% — **43.1pp gap** |",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/from_cheater/DBQ_single_shot_recipe.md",
   "lines": "25-26",
   "quote": "**Single-shot fresh single Unit-1 the rate collapses to 20%** — the iterate+best-of-K pipeline was doing most of the lifting.",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-06T0825Z_synapse_enrolled_learnings_published.md",
   "lines": "24",
   "quote": "Best-of-N with same judge as selector and grader inflates scores via Goodhart",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_cheater/2026-05-29T1312Z_99STACK_LAYER1_COMPLETE_all_5_cells_delivered.md",
   "lines": "13-14",
   "quote": "Composite n=500 verdict on v86chain stack is now mathematically unblocked — all 5 cells served at 100% via Layer 1 lookup.",
   "ok": false
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-004-saq-no-stimulus.md",
   "lines": "129-131",
   "quote": "A deterministic curriculum-API lookup that flags any named statute outside the period would catch the rest.",
   "ok": true
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-06T0825Z_synapse_enrolled_learnings_published.md",
   "lines": "23",
   "quote": "LLM judge requires cell-type-specific rubric overlays, not generic rubric",
   "ok": true
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-004-saq-no-stimulus.md",
   "lines": "122-124",
   "quote": "Add a check: the criterion must specify a SPECIFIC, NAMED historical fact that the example must satisfy, not a generic category.",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/exploits/EXPLOIT-007-difficulty-downgrade.md",
   "lines": "4-6",
   "quote": "Stacked fresh-holdout on SAQ dropped 88% → 76%; LEQ dropped 79% → 75%; MCQ dropped 80% → 76%. Pilot-isolation lift is real; production stacking is not.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_pil/2026-05-20T0821Z_PIL_WEEKLY_APUSH_REPORT.md",
   "lines": "29",
   "quote": "- 149/150-style gate: stitched slices reach 149/150, but mixed builds (`6f0ffdf`, `e429b16`), so not strict same-build proof.",
   "ok": false
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/_deprecated/outboxes/from_research/2026-05-01T1300Z_R44_eval_phantom_class.md",
   "lines": "36",
   "quote": "2. **No source MANIFEST** — the 73.33% number lived in a status file, not a `summary_*.json` with hashes-of-inputs + grader-version + per-item-score.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/from_cheater/2026-05-29T1605Z_DBQ_realsource_smoke_FAIL_pack_content_issue_E2.md",
   "lines": "40-43",
   "quote": "- The metadata says \"Date: 1491-1607 (subject period; doc undated)\" for many docs, meaning the actual document is undated and the date field is filled in with the KC's subject period — not the doc's real authorship date",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/Cheater/from_cheater/SINGLE_IB_GRADE_SURVIVAL_GUIDE.md",
   "lines": "62-64",
   "quote": "An explicit \"high-risk pitfalls\" block in the prompt that enumerates the common date-traps reduces this by ~30-50%. Doesn't eliminate it.",
   "ok": true
  }
 ]
}
```
