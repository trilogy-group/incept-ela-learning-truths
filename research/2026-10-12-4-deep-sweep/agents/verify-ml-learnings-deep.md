# verify:ml-learnings-deep

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "ml-learnings-deep. I reread all cited files. The 38 candidates quote 101 passages and evidence_for_existing quotes 57; every one appears verbatim at its cited lines. Two multi-line quotes match only if the source's trailing spaces are kept: master_strategy_apr24.md line 54, and research_dpo_grpo_factual.md lines 442-443. Every number in the statements and quotes checks out. I also checked the quotes in each against field.\n\nVerdicts: 10 keep, 24 keep-with-fix, 4 drop. Candidate 18 is dropped as a restatement of truth 62. Candidates 21, 23 and 36 are dropped because each rests on one benchmark's convention, one framework's design or one study summarised without figures, with no result behind it. Two kinds of fix recur. 'measured' is relabelled where the evidence is a diagnosis or a tiny run. Claims are softened to 'can' where the source says 'might' or 'sometimes'.\n\nDeeper AP and knowledge findings for the merge:\n(1) The 0% to 18% 'pipeline' jump has no pipeline change behind it. decisions_and_pivots_timeline.md line 82 says the only change was the token limit, and mcq_set_journey.md line 154 shows the 0% run already on the 3-step pipeline.\n(2) The anchor-fact '100% pass rate' is not a measurement (sft_v7_benchmark_postmortem.md line 126; what_to_do_next.md line 11). The constraint was added on Apr 24 (mcq_set_journey.md line 64; knowledge_and_rag_pipeline.md line 100) and was 'Not yet tested in benchmark' (training_data_journey.md line 128). The Gemini 97-100% came from the earlier April runs. So truth 57's support inside this folder is planned, not measured.\n(3) Prompts call the fact store 'VERIFIED correct facts' (sft_v7_benchmark_postmortem.md line 150), but the store was never checked against the curriculum (knowledge_and_rag_pipeline.md lines 230 and 234).\n(4) sft-v7 was trained from the raw base on question-set and document items only (sft_version_history.md line 52; fireworks_training_reference.md line 109). Its 0/6 short-answer and 4/6 essay results therefore come from a writer never trained on those types.\n(5) fireworks_training_reference.md lines 18 and 27 give identical 'teacher's N=100' figures to two model versions. sft-v4's 'Overall ~6.5%' is far from the mean of its own per-type rates, so what 'overall' means is never stated.\n\nname_bearing_source is false for every candidate. The only name in any path is the account's home directory, which every file shares; no file is named after a person. Statements contain no names or job roles; 'writer', 'judge' and 'marker' are the list's existing words for system components.\n\nExisting-evidence check: 54 of the 57 items hold. Three don't bear on their truth: the class-balance item for truth 8, and the 69% expert-review figure and the field study for truth 44.",
 "verified": [
  {
   "index": 0,
   "verdict": "keep",
   "reason": "All quotes verbatim at the cited lines. The judge lists implausible distractors as an educational-accuracy failure (line 79), and line 82 says such a failure makes the item unusable whatever its facts, which supports 'fails as an assessment'. Plausible distractors are a standard item-writing rule across subjects and grades. Not a duplicate: truth 6 has the text settle one answer and each option checked on its own; this adds that the wrong options must be tempting. Adopted rule; no measured effect.",
   "statement": "Every wrong option in a multiple-choice item must be plausible; an item whose answer is obvious fails as an assessment.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "79",
     "quote": "- Answer choices aren't plausible distractors (one obvious correct answer)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "82",
     "quote": "An educational accuracy failure means the question isn't usable on an AP exam regardless of factual accuracy.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
     "lines": "35",
     "quote": "**MCQ:** One stimulus (primary source), one question stem, four answer choices (A-D), exactly one correct answer, three plausible distractors.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/knowledge_and_rag_pipeline.md",
     "lines": "147-148",
     "quote": "Generate research notes about [topic], identifying: 1 specific historical claim,\nreliable date range, and 2 plausible distractor events.",
     "verbatim": true
    }
   ],
   "against": "No count of distractor failures anywhere in the folder; the rule is the judge's stated criterion. The judge is described as lenient on teaching value: evaluation_methodology.md line 186: \"- It doesn't fully test \"pedagogical value\" — a factually correct question that teaches the wrong skill can still pass\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Fixed because 'neither bare recall' carries over an AP-only premise (line 49: 'AP Social Studies is not a memorization test'). Where an objective calls for recall, a recall question is right. The general truth is matching the named reasoning and the course's level. Line 90 is one of the judge's curriculum-alignment failure modes and lines 77-78 are educational-accuracy ones: stated criteria, not measured effects. Not on the list.",
   "statement": "Each question should test the reasoning its objective names, at the course's level: a recall question fails an objective that asks for analysis, and so does a different kind of reasoning or analysis beyond the course.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
     "lines": "57",
     "quote": "Questions must explicitly test one of these skills. A question that just asks \"what happened?\" fails `educational_accuracy` because it tests recall, not historical thinking.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "90",
     "quote": "- Learning objective mismatch (question asks for causation when LO requires comparison)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "77-78",
     "quote": "- Question tests college-level historical analysis that AP students don't need\n- Question is too easy (tests rote recall when AP requires analysis)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
     "lines": "49",
     "quote": "AP Social Studies is not a memorization test.",
     "verbatim": true
    }
   ],
   "against": "The judge may miss a skill mismatch: evaluation_methodology.md line 186: \"- It doesn't fully test \"pedagogical value\" — a factually correct question that teaches the wrong skill can still pass\". No failure counts per kind of mismatch are given.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 1/4 = 25% matches line 14. 'Left alone, a writer piles its questions onto the most prominent case' generalises from the judge's comment on at most three failing sets out of four, so it becomes 'can'. The coverage requirement is the judge's concept-coverage check, an adopted rule. Listing the cases in the plan was planned (master_strategy_apr24.md line 43) and never measured. Related to truths 41 and 68, but adds covering the objective's breadth, which neither states.",
   "statement": "When an objective spans several cases, a question set must cover them: list the cases in the plan and give each question a different one, because a writer left alone can pile its questions onto the most prominent case.",
   "kind": "adopted rule (the judge's coverage check) with one observation; planned fix not measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
     "lines": "71",
     "quote": "- *\"The quiz is heavily concentrated on Columbus and Spanish motivations. For the stated objective—causes of exploration by various European nations—it does not adequately assess Portugal, France, or England.\"*",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
     "lines": "75",
     "quote": "- The plan step is supposed to force multi-nation coverage but the model picks the most prominent entity in the topic (Columbus/Spain) and concentrates questions there.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
     "lines": "78",
     "quote": "But the plan step doesn't enforce concept coverage across questions.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
     "lines": "43",
     "quote": "Add `nations_to_cover: [\"Portugal\", \"Spain\", \"France\", \"England\"]` field to the Plan step output schema. Question step: each question must address a different nation from the plan. Prompt-only change in `mcq_set.py`.",
     "verbatim": true
    }
   ],
   "against": "One partial run of 4 question sets: sft_v7_benchmark_postmortem.md line 20: \"This is a partial run (unit 1 only, benchmark still in progress). But the failure patterns are clear enough to diagnose.\" The fix has only an expected gain: what_to_do_next.md line 33: \"- MCQ_SET: 25% → ~40%\". Another failing set in the run failed on structure, not coverage: sft_v7_benchmark_postmortem.md line 72: \"- *\"No answer choices shown\"* — questions generated without multiple-choice options in one failure.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, but the headline evidence is contradicted by its own source. decisions_and_pivots_timeline.md line 84 says 'MCQ_SET jumped from 0% to 18%... Because we gave it the pipeline', yet line 82 of the same file and mcq_set_journey.md lines 154-155 show the pipeline was already in place at 0% and the only change was the token limit. That evidence is replaced with three things: the adopted rule (failures_and_false_starts.md line 110; pipeline_architecture_insight.md line 5), the one-job test (research_qwen3_structured_multistage.md line 215), and the diagnostic benefit (mcq_set_journey.md line 25). The statement now carries the one-job condition, because the record also shows a chained step lowering results; truth 61 covers that side. The folder has no clean measurement of splitting.",
   "statement": "Make a complex item in steps that each do one job the writer can't do well alongside the others (plan, then source, then questions), rather than in one pass that does everything.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/failures_and_false_starts.md",
     "lines": "110",
     "quote": "Breaking generation into multiple complementary steps is the only reason to add steps — verification and regeneration are not valid approaches.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/pipeline_architecture_insight.md",
     "lines": "5",
     "quote": "Gemini doesn't score 97% because it's a smarter model. It scores 97% because complex question types (MCQ_SET, DBQ) are broken into multiple complementary steps, each optimized for a specific subtask.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_qwen3_structured_multistage.md",
     "lines": "215",
     "quote": "**The right question is not \"how many stages\" but \"does each stage do one thing the model can't do well simultaneously with other things?\"**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
     "lines": "25",
     "quote": "- Stimulus generation and question generation in one step produced tightly coupled outputs that were hard to diagnose",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
     "lines": "88",
     "quote": "**Why factual accuracy fails in DBQ:** 7 documents, each needing a plausible historical source, date, and content. The model generates all 7 in one call. By documents 4-7, it's drifted from its context and starts confabulating attributions.",
     "verbatim": true
    }
   ],
   "against": "The 0% to 18% figure can't count for the pipeline: decisions_and_pivots_timeline.md line 82: \"**The surprise:** `.env` already had `LLM_BACKEND=fireworks` set. The routing was already there. The ONLY change needed was reducing token limits from Gemini scale to sft-v4 scale. That was a 5-minute code change.\" mcq_set_journey.md line 154 records the 0% run as already \"3-step pipeline, Fireworks\". A step can hurt: mcq_set_journey.md lines 44-46: \"1. Research→Compile (single step): 60% — worse than before\n2. Research→Stimulus→Questions (3 steps): 60% — same problem\n3. Stimulus (from scratch, no research)→Questions: 80% — best\". Limit: research_qwen3_structured_multistage.md line 251: \"- When the sub-task outputs need tight semantic coupling (e.g., you can't generate the introduction and body separately if they need to reference each other)\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep",
   "reason": "Quotes verbatim; numbers match. Line 130 is the record's general lesson from a measured change: line 126 reports that 15 of 17 short-answer factual failures disappeared once the marking guide stopped asking for named evidence. The no-source variant also raised factual accuracy from 60% to 70% at N=20, a difference of two items. General: the more unverified specifics an item needs, the more chances to void it. It generalises truth 56 beyond marking guides to sources and documents, so it stays its own record; it shares only the consequence with truth 59.",
   "statement": "Every specific a writer must produce from memory (a date, a name, a figure, a source line) is another chance to be wrong, so ask only for the specifics the task needs.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "130",
     "quote": "**The broader lesson:** The more specific the evidence the model is asked to enumerate, the more hallucination surface area. Every specific claim (date, name, treaty, publication founding year) is an opportunity for the model to be slightly wrong. Reducing the specificity requirement reduces the hallucination rate.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "126",
     "quote": "**Result:** 15 of 17 factual_accuracy failures in SAQ disappeared immediately.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
     "lines": "116",
     "quote": "**3. DBQ document generation is the hardest factual load.** 7 documents × each needing accurate source/date/content = 7 independent factual claims that all must be correct. Probability of all 7 being right with a 14B model: low.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "168",
     "quote": "**The counterintuitive insight:** Flash produces CLEANER DBQ outputs than Pro in some cases. Pro's creativity → longer, more detailed documents → more hallucination surface area. Flash's conservatism → shorter, more cautious documents → fewer fabricated details → better factual_accuracy.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
     "lines": "56",
     "quote": "| no_source | 50% | 70% | Best factual_accuracy |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
     "lines": "57",
     "quote": "| baseline | 45% | 60% | Standard prompt |",
     "verbatim": true
    }
   ],
   "against": "Cutting more specifics did not keep helping: prompt_engineering_deep_dive.md line 59: \"| no_source_nodates | 40% | 50% | No source + no dates |\" (vs 70% factual with only the source dropped, N=20 each). Forbidding specifics is not the same as not asking for them: master_strategy_apr24.md line 105: \"We have \"⛔ NEVER use specific dates\" and it produced 0% SAQ.\" Line 168's finding holds only 'in some cases'.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 70% vs 60% at N=20 matches. The evidence is fixed. mcq_set_journey.md line 142 ('There's nothing to fabricate') overstates: the passage text is still written by the model (line 63), and the anchor-fact constraint was 'Not yet tested in benchmark' (training_data_journey.md line 128). It is replaced by line 129, which shows the failure the rule targets. The sweep is labelled '9 variants' but its table lists 8. Caveat for the merge: an attribution taken from a record does not make a written passage a real quote, so pair this with truth 17 (quote exactly, checked in code). It applies truth 57 to attributions and adds the leave-it-off option, the one variant the sweep measured.",
   "statement": "Never let a writer invent who wrote a source passage, or when and where it appeared; take the attribution from a verified record or leave it off.",
   "kind": "measured (small sample)",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
     "lines": "67",
     "quote": "The main hallucination vector for MCQ is the source attribution in the stimulus (e.g., \"— Thomas Jefferson, 1799\" that the model invented). Removing the requirement to provide a named source eliminates the fabrication opportunity.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
     "lines": "56",
     "quote": "| no_source | 50% | 70% | Best factual_accuracy |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
     "lines": "57",
     "quote": "| baseline | 45% | 60% | Standard prompt |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
     "lines": "169",
     "quote": "3. **Attribution is the trap.** Every MCQ_SET needs a historical author and date. The model learned to generate plausible-sounding attributions. Plausible ≠ accurate.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
     "lines": "129",
     "quote": "Model then writes a stimulus \"inspired by\" this theme. Carnegie may or may not have written this. 1889 may or may not be when he wrote relevant things. The model fills in gaps.",
     "verbatim": true
    }
   ],
   "against": "The gain is two items in twenty: prompt_engineering_deep_dive.md line 50: \"**Method:** test_variants.py — 9 variants, N=20 each, APUSH Unit 7\". Dropping the source did not give the best pass rate: line 55: \"| no_source_facts | 60% | 60% | Best overall pass rate |\". Instructions alone did not stop invention: prompt_engineering_deep_dive.md line 73: \"No matter how you phrase the prompt, the model defaults to its training behavior when generating a historical document excerpt.\" The pipeline still credits a newly written passage to a real author: mcq_set_journey.md line 63: \"- Output: primary source passage attributed to the historical author in the plan\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 95-100%, 97% and 0/6 match. 'An instruction a stronger writer obeyed, a weaker one ignored' is the record's explanation (line 132), not a measurement. The 0/6 also comes from six items on a writer trained from the raw base on two other item types only. So the clause is softened to what was observed. week_of_apr_21.md line 135 adds a second case of the same instructions behaving differently: one writer filled the optional fields and the other dropped them. General and not on the list; it is truth 70 applied to a change of writer.",
   "statement": "Re-test every instruction whenever the writer changes; the same instructions held for one writer and failed for another.",
   "kind": "observed (small sample, confounded)",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
     "lines": "130",
     "quote": "1. **The anchor-fact pattern was invented for stimuli, not rubrics.** When MCQ_SET was broken at 0%, we fixed the stimulus with anchor-facts. SAQ was already at 95-100% on Gemini, so its scoring notes weren't a problem. Nobody connected the dots to apply it to rubrics.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
     "lines": "132",
     "quote": "2. **The current approach (negative prompting) seemed to work on Gemini.** Because Gemini is large enough to mostly respect the \"no specific evidence\" instruction and has accurate enough parametric memory that when it does include evidence, it's usually right. The instruction that's good enough for a large model is insufficient for a 14B model.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/knowledge_and_rag_pipeline.md",
     "lines": "234",
     "quote": "None of these are implemented yet. The current system (4,177 facts, cluster matching, \"facts as hints\") is good enough for Gemini at 97%. It's not good enough for sft-v4/sft-v7 at the target rates.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/week_of_apr_21.md",
     "lines": "135",
     "quote": "Gemini reliably fills all JSON schema fields including optional ones. Fireworks model frequently omits optional fields (e.g., `source_attribution`). Keep required fields minimal; never rely on optional field presence for correctness. The `anchor_fact` field is required in the schema specifically because of this.",
     "verbatim": true
    }
   ],
   "against": "The weaker writer had no short-answer training examples, which confounds the 0/6: sft_version_history.md line 52: \"- Focus: MCQ_SET and DBQ are the failure modes. Other types excluded (already have training data from sft-v6)\" and fireworks_training_reference.md line 109: \"- **Base:** `accounts/fireworks/models/qwen3-14b` (raw, same as Stage 1)\". The step structure did carry over: week_of_apr_21.md line 17: \"The same scaffolding transfers to Fireworks with only token limit adjustments.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep",
   "reason": "Quotes verbatim; 4/5 and 1416/1416 match grpo_failures_deep_dive.md lines 37 and 33. Four separate incidents produced results that did not come from the system under test: a wrong backend import, a silent fallback, a flag that was never switched on, and a test path that cleaned output the real path didn't. General. Truths 24, 36 and 46 each cover one of these paths, but none states the provenance check, so it stays its own record. Line 39 hedges with 'probably', but line 26 confirms the run's MCQ items came back empty.",
   "statement": "Before reading a result, confirm that every measured item came from the system under test, with the change switched on and by the path it will run in.",
   "kind": "observed incidents",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
     "lines": "39",
     "quote": "**Why this wasn't caught earlier:** The bug only manifests with `LLM_BACKEND=fireworks`. Every previous sft-v4/sft-v5/sft-v6 benchmark was probably silently skipping all MCQs. The MCQ numbers from those runs are meaningless.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
     "lines": "26",
     "quote": "**Symptom:** All MCQ items returned empty content (`generated_content: {}`), score 0.0.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
     "lines": "31",
     "quote": "**Result:** The MCQ Research step NEVER WORKED. Every MCQ and MCQ_SET generation silently fell back to a legacy one-shot path. The research was supposed to gather verified primary sources — it never ran.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/failures_and_false_starts.md",
     "lines": "163",
     "quote": "**Result:** Best-of-N was \"deployed\" but not activated. The benchmark showed the same results as before because the feature wasn't actually running.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/grpo_failures_deep_dive.md",
     "lines": "37",
     "quote": "**Why this wasn't caught earlier:** The sft-v3 baseline test (5 prompts) showed 4/5 valid JSON. But that test went through the production pipeline, which strips thinking blocks before returning the response. Raw GRPO rollout bypasses the pipeline entirely. Two different code paths.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim; 6.5%, ~27%, ~60%, 67 vs 90 and 0 vs 18 all match. The problem goes deeper than the reader noted. fireworks_training_reference.md line 18 gives the identical 'teacher's N=100' figures to a different model version, so the 67-vs-90 pair may be one run filed under two versions. The 'Overall ~6.5%' in sft_version_history.md line 22 is also far from the mean of its own per-type rates (about 46%), so 'overall' meant something unstated. Both strengthen the rule: without sample size, scope, setup and how 'overall' is computed, the record could not say which numbers belong together. General; not on the list.",
   "statement": "Record every pass rate with its sample size, scope and setup; without them, results for the same writer can't be compared.",
   "kind": "observed (record inconsistencies)",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_version_history.md",
     "lines": "40",
     "quote": "- The 27% vs 36% discrepancy from earlier session: the 36% was clean units only; 27% is all units",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_version_history.md",
     "lines": "22",
     "quote": "- Pass rates (N=100, April 21): MCQ 67%, SAQ 67%, LEQ ~98%, MCQ_SET 0%, DBQ 0%, Overall ~6.5%",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/fireworks_training_reference.md",
     "lines": "27",
     "quote": "- **Pass rates (teacher's N=100):** MCQ 90%, LEQ 71%, SAQ 67%, MCQ_SET 18%, DBQ 10%",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/fireworks_training_reference.md",
     "lines": "18",
     "quote": "- sft-v3 baseline: MCQ 90%, LEQ 71%, SAQ 67%, MCQ_SET 18%, DBQ 10% (teacher's N=100 results)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/INDEX.md",
     "lines": "95",
     "quote": "| sft-v4 overall | ~60% | N=100, teacher's measurement |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
     "lines": "153",
     "quote": "sft-v4 with pipeline went from 6.5% to ~27%. Without pipeline, it was 6.5%.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The evidence is fixed: failures_and_false_starts.md line 155 is about a diagnostic tool failing with connection errors when the other evaluator was down (lines 143-149), not about divergent verdicts. It is dropped and evaluation_methodology.md line 5 is added. 'Two judges gave different verdicts' becomes 'can give', matching line 20's 'can produce'. Close to truth 45 (fix the rubric before measuring), but this is about the instrument, not the criteria, so it stays separate.",
   "statement": "Score every run you compare with the same judge; judges with different semantics can give different verdicts on identical items.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "20",
     "quote": "**Hard rule:** Never use localhost:8080 for official benchmarking. The `/get_standard` API has different semantics that can produce different pass/fail decisions on identical content.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "5",
     "quote": "This project uses TWO different evaluators and mixing them up causes subtle, hard-to-diagnose failures.",
     "verbatim": true
    }
   ],
   "against": "No instance of two judges disagreeing on the same item is recorded; the rule rests on the stated difference in semantics. failures_and_false_starts.md line 149 shows the cited 'confusion' was a dependency failure: \"4. Tool fails with connection error because localhost:8080 is down\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep",
   "reason": "Quotes verbatim; numbers match. It extends truth 34 (verdicts vary between runs) with per-type rates and a rule for how many runs and items each type needs, so it is kept as a duplicate that adds evidence. The '±10%' at N=20 is about one binomial standard error (about ±11%); a 95% interval is roughly twice that, which makes 'one run decides nothing' stronger, not weaker.",
   "statement": "Measure how often the judge changes its verdict on identical items, per item type, and set the number of runs and items from that; for noisy types one run decides nothing.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "123-128",
     "quote": "**Flip rates by type (discovered April, N=4 repeated trials):**\n- DBQ: 30% flip rate\n- MCQ_SET: 50% flip rate (!)\n- SAQ: 10% flip rate\n- LEQ: 0% flip rate\n- MCQ: 0% flip rate",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "130",
     "quote": "**What \"flip\" means:** Item scored as pass on trial 1, fail on trial 3 (or vice versa), with identical input.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "139",
     "quote": "4. **Benchmark pass rates have error bars.** N=20 at 50% flip rate for MCQ_SET means our pass rate estimate has ±10% uncertainty. Always run N≥20 for MCQ_SET benchmarks.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "168-173",
     "quote": "Never make decisions on a single run. For MCQ_SET with 50% flip rate:\n- Single run pass rate = noise\n- 3 runs, average = directional signal\n- 5+ runs, average = reliable signal\n\nFor MCQ/LEQ with 0% flip rate, single run N≥20 is reliable.",
     "verbatim": true
    }
   ],
   "against": "Clear passes are stable: evaluation_methodology.md line 135: \"The noise doesn't affect items that score 0.95+ consistently.\" The rates come from 4 trials on an unstated number of items. Line 133 also reads '50% of items flipped across trials' as a per-run chance of flipping, which is a different quantity.",
   "general": true,
   "duplicate_of": "34",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 18,768 matches. The kind is corrected from 'measured' to diagnosis. The record asserts that the examples held invented attributions and that the writer learned them, but nobody counted bad examples, and other files describe the same data as high quality with real sources. 'Get copied' is changed to 'learns ... as part of the pattern', which is what the record actually claims. The rule is still sound and general: examples teach what they contain. Related to truths 61 and 66 (mcq_set_journey.md line 112 is already logged for 66), but distinct because it is about the examples, not pipeline notes or selection by a judge.",
   "statement": "Check every fact in the examples a writer learns from or imitates; it learns their invented details as part of the pattern.",
   "kind": "diagnosis (not measured)",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
     "lines": "15",
     "quote": "This is *not* a model size problem. A 14B model has ~28B bits of theoretical capacity — more than all of English Wikipedia. The gap to 70B is 6-8 MMLU points, not an order of magnitude. **The problem is that our training data contained fabricated attributions, and we taught the model exactly the wrong pattern.**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
     "lines": "112",
     "quote": "**Why 40% might be the new ceiling:** The training data (raft_combined) itself has fabricated attributions. Some of the 18,768 MCQ_SET records have slightly wrong dates or sources — they just passed InceptBench at the time, which has a 50% flip rate. Training on data that sometimes has wrong attributions = training on signal + noise.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
     "lines": "73",
     "quote": "The model learned to produce source attributions from training data that had fabricated attributions.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_model_size_vs_data_quality.md",
     "lines": "108",
     "quote": "| Knowledge distillation (from Gemini) | Teaches format/style | Inherits hallucinations from teacher | Medium — we're already doing this and it's the source of the problem |",
     "verbatim": true
    }
   ],
   "against": "No audit of the examples was done: what_to_do_next.md line 65: \"- **Training data quality audit:** If sft-v8 planned, audit training examples for scoring note factual accuracy before including them\". The same records are elsewhere called sound: training_data_journey.md line 26: \"Quality: High. All passing InceptBench or close to it.\" and line 31: \"Content: Gemini-quality. Real primary sources, well-reasoned explanations.\" Volume ranked first by the cross-team summary: cross_team_learnings_full.md line 162: \"1. **More data > better data > architecture tricks.** Get the training data right before doing DPO, GRPO, or scaling.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 500, 18,768, 504, 0% to 12% and 80%+ match. The kind is corrected to adopted rule. The audit lesson is adopted (decisions_and_pivots_timeline.md line 111) and the absence case is measured (0% to 12%), but the fault case is a hypothesis: the 70k cancellation rested on reasoning, and sft-v7's test of it was still pending. The audit counted records but never checked their quality, while mcq_set_journey.md line 112 says some are wrong, so 'how good it is' is added. General; not on the list.",
   "statement": "Before producing more material, audit what already exists, both how much there is and how good it is, and ask whether the failure is an absence, which more material can fix, or a fault in what exists, which more of the same won't.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/decisions_and_pivots_timeline.md",
     "lines": "107",
     "quote": "**The audit finding:** We had been planning to generate 500 new MCQ_SET examples when we already had 18,768+ after combining raft_combined and sft_v6_combined.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/decisions_and_pivots_timeline.md",
     "lines": "111",
     "quote": "Always audit existing data before generating new.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/training_data_journey.md",
     "lines": "111",
     "quote": "**Lesson:** Before building a bigger dataset, ask: does the failure mode respond to more data? MCQ_SET at 0% responded to adding examples (0%→12%). MCQ at 60% ceiling did NOT respond to more prompt engineering. Different failures need different fixes.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/decisions_and_pivots_timeline.md",
     "lines": "98",
     "quote": "**What we got wrong:** Thought 504 examples would get MCQ_SET to 80%+. Actual ceiling was ~12%. The format problem was solved; the content quality problem wasn't.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
     "lines": "112",
     "quote": "Some of the 18,768 MCQ_SET records have slightly wrong dates or sources",
     "verbatim": true
    }
   ],
   "against": "The 'more of the same won't fix a fault' half was never tested: decisions_and_pivots_timeline.md line 127: \"**What's unknown:** Will more MCQ_SET training data fix the quality problem, or is the bottleneck the training data having fabricated attributions (which sft-v7 data also has)?\" failures_and_false_starts.md line 23 answers its own proposed mini-test without running it. The cross-team summary favours volume: cross_team_learnings_full.md line 73: \"**The pattern:** More representative examples of the hardest cases = better coverage of the output space.\" The second example in training_data_journey.md line 111 is about prompt changes, not more data.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 34%, 37k, 59k and 56,554 match. The 34% is the loss against 56k; against 59k it would be 37%. Wording fixed: 'items that share a stock opening are not duplicates' reads as if such items can never be duplicates, but the evidence only shows that a shared opening alone doesn't make them so. General to any generated item bank. A whole-item hash catches only exact copies; near-duplicates need another test, which the folder doesn't cover.",
   "statement": "Find duplicate items by comparing whole items, not their openings; sharing a stock opening doesn't make two items duplicates.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/training_data_journey.md",
     "lines": "7",
     "quote": "**Bug:** Used MD5 hash of first 200 chars of assistant content for deduplication.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/training_data_journey.md",
     "lines": "9-12",
     "quote": "This caused massive FALSE POSITIVES. Many different records share the same opening 200 characters:\n- MCQs starting with \"Which of the following best describes...\"\n- LEQs starting with \"Evaluate the extent to which...\"\n- DBQs starting with \"Using the documents...\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/training_data_journey.md",
     "lines": "14",
     "quote": "Result: Appeared to have only 37k unique records from what should have been 59k+. A 34% false dedup rate made the dataset look much smaller than it was, and caused us to think we needed to generate more data.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/training_data_journey.md",
     "lines": "16",
     "quote": "**Fix:** Full content MD5 hash of the entire assistant response.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/training_data_journey.md",
     "lines": "17",
     "quote": "**After fix:** 56,554 from raft_combined alone were correctly unique. We didn't need to generate anything.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 40 vs 45% and 55 vs 60% match. The leak itself is a qualitative observation ('sometimes referenced elements', line 122), and the score gap is one item in twenty, within sampling noise. So 'leak' becomes 'can leak' and the kind is corrected. Showing structure rather than content fits the format-only examples that the counter-evidence uses. General. It relates to truth 57, since unverified sample content acts as a source, but is not on the list.",
   "statement": "Sample items shown to a writer can leak their facts, sources and period into what it writes, so show the required structure rather than sample content.",
   "kind": "observed (effect within noise)",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/failures_and_false_starts.md",
     "lines": "120",
     "quote": "**Result:** 40% pass rate — worse than the 45% baseline.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/failures_and_false_starts.md",
     "lines": "122",
     "quote": "**Why:** The few-shot examples gave the model specific historical content (dates, sources, attributions from the examples) that contaminated its generation. The model sometimes referenced elements from the example questions in its generated questions, or the examples biased its style toward those specific historical periods.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
     "lines": "58",
     "quote": "| fewshot | 40% | 55% | Few-shot examples added |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
     "lines": "57",
     "quote": "| baseline | 45% | 60% | Standard prompt |",
     "verbatim": true
    }
   ],
   "against": "The gap is one item in twenty on both pass rate and factual accuracy: prompt_engineering_deep_dive.md line 50: \"**Method:** test_variants.py — 9 variants, N=20 each, APUSH Unit 7\". A cited grounding method relies on examples of a format: research_rag_factual_grounding.md line 202: \"Implementation via ICL with few-shot examples: provide 3-5 examples of the desired citation format, then instruct the model to follow the pattern.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 5% vs 45% at N=20 matches. 'It drops parts' was not shown for the no-schema variant: the record gives only its pass rate. The clause now states what was measured (far more failures) and what was observed (optional fields left out, week_of_apr_21.md line 135). General; not on the list; complements truth 29.",
   "statement": "Give the writer the item's exact structure and make every field that matters required; without a structure items failed far more often, and fields left optional got left out.",
   "kind": "measured (small sample) and observed",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
     "lines": "62",
     "quote": "| bare | 5% | 50% | No schema, raw generation |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
     "lines": "57",
     "quote": "| baseline | 45% | 60% | Standard prompt |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/week_of_apr_21.md",
     "lines": "135",
     "quote": "Gemini reliably fills all JSON schema fields including optional ones. Fireworks model frequently omits optional fields (e.g., `source_attribution`). Keep required fields minimal; never rely on optional field presence for correctness. The `anchor_fact` field is required in the schema specifically because of this.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
     "lines": "45",
     "quote": "Any structural deviation = automatic fail on `specification_compliance`.",
     "verbatim": true
    }
   ],
   "against": "Structure doesn't carry correctness: research_model_size_vs_data_quality.md line 150: \"- The knowledge and content quality within the structure is what differentiates model sizes — not the structural compliance itself\". In the same sweep, factual accuracy moved much less than the pass rate (50% with no schema vs 60% baseline). Structure is a hard fail only for some item types (evaluation_methodology.md lines 44-50).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 0% to 12% and 88% match. 'Fixing one leaves the other as it was' overstates. Content couldn't be judged before the format existed, and the reverse case (fixing content leaves the form unchanged) is not in the evidence. Fixed to what was shown, with research_model_size_vs_data_quality.md line 150 added. General; shares only the spirit of truth 28 (gate every check).",
   "statement": "A well-formed item is not a correct one; check structure and content separately, because fixing the form didn't fix the content.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
     "lines": "92",
     "quote": "**What 12% means:** The model now generates MCQ_SET format (3 questions, stimulus, all required fields). But the quality threshold (factual_accuracy, stimulus_quality) was still failing 88% of the time.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
     "lines": "94",
     "quote": "**What 12% doesn't mean:** We solved MCQ_SET quality. We solved MCQ_SET FORMAT. These are different problems.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
     "lines": "251",
     "quote": "The limitation is critical: you can force the model to emit a syntactically valid JSON field for `\"year\": <int>`, but you cannot force the value to be `1919` rather than `1914` via grammar constraints alone. Semantic fact-checking requires a different mechanism.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_model_size_vs_data_quality.md",
     "lines": "150",
     "quote": "- The knowledge and content quality within the structure is what differentiates model sizes — not the structural compliance itself",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 17,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 0.92 matches. Narrowed: the cited studies (Binary RAR, FLAME) show style gaming where a model is trained against a score, not for every graded score. Selection by score (best-of-N) is the case inside the project. prompt_engineering_deep_dive.md line 70 adds support from the folder itself: supplied facts lifted other dimensions enough to push borderline items over the line without improving factual accuracy. The prescription is truth 59; kept as a duplicate because it adds the mechanism and outside evidence. Neither paper was opened.",
   "statement": "A graded score that output is trained or selected against can be won by length, fluency and confidence even when facts are wrong, so factual correctness needs its own pass/fail gate.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_dpo_grpo_factual.md",
     "lines": "146",
     "quote": "The binary reward is specifically better than continuous scores in this paper because continuous rewards get gamed by output style (longer, more confident responses get higher scores even with wrong facts). Binary RAR forces the model to be either fully correct or abstain.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_dpo_grpo_factual.md",
     "lines": "85",
     "quote": "FLAME diagnoses a specific problem: conventional SFT+DPO alignment pipelines inadvertently *increase* hallucination because reward signals prioritize helpfulness, verbosity, and fluency over correctness.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "40",
     "quote": "This is NOT just overall_score ≥ 0.85. An item can score 0.92 overall and still hard-fail if a single hard-fail dimension drops below 1.0. The hard-fail dimensions are binary gates — they must all be perfect.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
     "lines": "70",
     "quote": "The curriculum facts help non-critical dimensions (educational_accuracy, etc.) enough to push borderline items above the 0.85 threshold, even though they don't help factual_accuracy specifically.",
     "verbatim": true
    }
   ],
   "against": "A pass/fail gate on its own gives no signal for improving weak output: grpo_failures_deep_dive.md line 19: \"**The key insight:** GRPO needs a GRADED reward signal (0.0 to 1.0) with variance between candidates. Binary 0/1 from hard-fails gives you nothing to compare. The evaluator was designed as a quality gate, not a reward shaper.\"",
   "general": true,
   "duplicate_of": "59",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "drop",
   "reason": "Quotes verbatim, but three problems. (1) 'An explicit way out rather than a bare prohibition' is truth 62 (tell a writer what to use, not what to avoid), and 'describe the kind of evidence instead of naming one' is truth 56. (2) The new part, a fallback for when no verified fact exists, was planned and never measured. (3) The research quotes concern RL training rewards (line 187) and a constitution the summary proposes to write (line 323), not a finding of the cited paper. Nothing usable beyond truths 62 and 56. If the fallback is ever measured, it belongs as a clause of truth 57.",
   "statement": "When no verified fact supports a specific claim, give the writer an explicit way out (describe the kind of evidence instead of naming one) rather than a bare prohibition.",
   "kind": "planned rule (unmeasured)",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
     "lines": "36",
     "quote": "If no verified fact supports the claim, describe the analytical CATEGORY only.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_dpo_grpo_factual.md",
     "lines": "187",
     "quote": "**Key caution:** \"Reasoning Models Hallucinate More\" (arXiv:2505.24630) shows that standard RL fine-tuning with binary correctness rewards can *increase* hallucination by incentivizing confident guessing. The fix is to incorporate factuality verification at each step (FSPO, their method) or use calibration rewards that reward abstention under uncertainty (Behavioral Calibration RL, arXiv:2512.19920).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_dpo_grpo_factual.md",
     "lines": "323",
     "quote": "Applied to factual accuracy: write a constitution with factual principles like \"All historical dates must be accurate\", \"Never attribute a quote to a person without certainty\", \"When in doubt about a specific year, omit the year rather than guess.\"",
     "verbatim": true
    }
   ],
   "against": "Only an expected gain: master_strategy_apr24.md line 45: \"**Expected T1 impact:** SAQ 0% → ~40-50%, MCQ_SET 20% → ~35-40%, overall ~33% → ~45-55%.\"",
   "general": true,
   "duplicate_of": "62",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 10-15 and 3,347 match. Line 171 is hypothetical ('might generate'), not an observed blend, so 'get blended in' becomes 'can get blended in'. The long-list point is the external Lost-in-the-Middle result as summarised. The project only ever gave the writer five facts, so the comparison with all 3,347 answers a setup nobody ran. The adopted rule (match facts to the item's topic cluster first) is solid; its effect was never measured. General. It refines truth 57 (which facts to give) and duplicates neither 57 nor 58.",
   "statement": "Give a writer only the few verified facts that match the item's exact topic, not everything for its unit; neighbouring-topic facts can get blended in, and long lists get used less.",
   "kind": "adopted rule; its reasons are a hypothesis and external research",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/knowledge_and_rag_pipeline.md",
     "lines": "171",
     "quote": "If the question topic was about Progressivism but the injected facts were about immigration, the model might generate a question that mixed both — or the curriculum facts wouldn't help at all.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/knowledge_and_rag_pipeline.md",
     "lines": "175",
     "quote": "**Impact:** Cluster-matched facts are more relevant to the specific question being generated. The model has better grounding for the specific topic rather than unit-level context.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
     "lines": "404",
     "quote": "**More context injection / longer fact lists:** The Lost-in-the-Middle problem means that making the fact list longer reduces the model's ability to use it. Better to use a retriever (Technique 7) to inject only the 10-15 most relevant facts rather than all 3,347.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
     "lines": "34",
     "quote": "- **Context position**: Facts buried in the middle of a long context block are more likely to be ignored than facts at the very beginning or end (Lost-in-the-Middle problem).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/week_of_apr_21.md",
     "lines": "23",
     "quote": "Cluster-matched facts (not just unit-level) improved relevance.",
     "verbatim": true
    }
   ],
   "against": "The cluster change's effect was never measured: infrastructure_and_tooling.md line 158: \"Cluster-matched facts > unit-level-only improved relevance.\" Only five facts were ever given: knowledge_and_rag_pipeline.md line 208: \"2. Calls `_build_facts_context(course, unit, cluster, limit=5)`\". Another note favours more facts in the store, not the prompt: knowledge_and_rag_pipeline.md line 228: \"2. **Fact expansion:** Grow the corpus from 4,177 to 20,000+ facts. More facts = better coverage = fewer hallucination opportunities.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; master_strategy_apr24.md line 54 ends in a trailing space in the source, reproduced here. The 83% vs 72% and 12% vs 25% figures match, but they come from self-verification against the writer's own knowledge. So they support claim-by-claim checking with repair in general, not checking against a source. The source-based form is LEAF's retrieval checker (research_dpo_grpo_factual.md line 301), whose reported gain (line 307) comes from a proprietary deployment. Pulling out claims and checking each is truth 32 (a judge checks bounded claims); kept as a duplicate because it adds the repair step and outside evidence. Planned here, never measured.",
   "statement": "After an item is written, pull out each specific claim and check it on its own against the source, replacing or dropping any that fails.",
   "kind": "external research; planned here, not measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "141-142",
     "quote": "- Factual Accuracy: **83%** (vs 72% standard CoT, 78% CoT+RAG)\n- Hallucination Rate: **12%** (vs 25% standard CoT, 18% CoT+RAG)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "137",
     "quote": "3. Verify each claim against internal knowledge",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_dpo_grpo_factual.md",
     "lines": "301",
     "quote": "LEAF is a three-component framework: (1) **RAFE** — a fact-checking module using retrieval to evaluate response accuracy claim-by-claim; (2) **Fact-Check-then-RAG** — inference-time correction without parameter updates; (3) **Learning from Fact Check** — either SFT on fact-checked responses or SimPO/DPO using fact-check scores to rank chosen vs. rejected. The training approach uses fact-checking scores as pseudo-labels to construct preference pairs, requiring no human annotation.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_dpo_grpo_factual.md",
     "lines": "307",
     "quote": "- **83% improvement in factuality scores** in healthcare deployment (proprietary medical documents)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
     "lines": "52-55",
     "quote": "Add a verification step after SAQ/LEQ/DBQ generation that:\n1. Extracts all specific historical claims from rubric fields (dates, names, events)\n2. Checks each against `curriculum_facts.json` \n3. Substitutes unverified claims with category descriptions or verified alternatives",
     "verbatim": true
    }
   ],
   "against": "The headline numbers come from checking claims against the writer's own knowledge, not a source: research_educational_content_generation.md line 137: \"3. Verify each claim against internal knowledge\". A project rule barred verification steps: research_rag_factual_grounding.md line 406: \"**Inference-time verification / regeneration:** Per project principles, \"verification and regeneration are not valid approaches.\"\"",
   "general": true,
   "duplicate_of": "32",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "drop",
   "reason": "Quotes verbatim, but the evidence is one benchmark's scoring convention as a summary describes it, with no result showing the convention works better. Line 182 is the summary's comparison, not a finding. As a rule it conflicts with truth 9 (an unsure judge is neither pass nor miss), and because verdicts flip between runs (truth 34), it would fail sound items. The strict per-item part is already truth 59.",
   "statement": "Count an item as grounded only when every judge finds no unsupported claim; a single objection fails it.",
   "kind": "external research (one benchmark's scoring convention)",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "184",
     "quote": "The closest published threshold is from the FACTS Benchmark Suite, which deems a response as \"successfully grounded\" only when all judge models agree it contains no unsupported claims. This binary per-item pass/fail mirrors our InceptBench approach.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "182",
     "quote": "- **Our InceptBench setup** (hard-fail at 1.0): Stricter than anything published. We require perfect factual accuracy per item, not an aggregate pass rate.",
     "verbatim": true
    }
   ],
   "against": "With noisy judges, unanimity fails sound items: evaluation_methodology.md line 125: \"- MCQ_SET: 50% flip rate (!)\".",
   "general": true,
   "duplicate_of": "59",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep",
   "reason": "Quotes verbatim. One cited study (Grade Like a Human), as the folder summarises it. Its reported claim is comparative ('more accurate and reliable'), so it supports the rule. General: building a marking guide against real answers holds across subjects. Not on the list; it complements truth 37 (score a judged check on person-labelled cases) and truth 69. The project never tried it, and the paper was not opened.",
   "statement": "Refine a marking guide against real student answers before relying on it, rather than writing it in one pass.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "55",
     "quote": "- Relevant insight: rubrics optimized against actual student answers are more accurate and reliable",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "56",
     "quote": "- **The key technique:** rubric generation as an optimization problem, not a single-shot generation",
     "verbatim": true
    }
   ],
   "against": "The cited work treats rubrics as scoring tools and doesn't test facts inside them: research_educational_content_generation.md line 75: \"Most work treats rubrics as frozen artifacts used for scoring, not as generated content that must be historically accurate.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "drop",
   "reason": "Quotes verbatim, but both lines describe one framework's design (RubiSCoT) with no reported effect, and a design choice is not evidence that the rule works. The approval half restates truth 44 (machine checks are not human judgment), and 'specific' criteria overlap truth 69. The observable-definition idea is untested here.",
   "statement": "Write each marking criterion as a specific, observable definition, and have a person approve any generated marking guide before it is used.",
   "kind": "external research (design description, no result)",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "65",
     "quote": "- Rubric criteria have \"operational definitions\" that are \"specific and observable\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "66",
     "quote": "- Instructors review and approve AI-generated rubrics before deployment",
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
   "reason": "Quotes verbatim. One cited study (AutoSCORE), as summarised, reports better accuracy and interpretability but gives no figures. General. Related to truth 31 (one yes/no question per candidate) and truth 33 (give the marker what the rule refers to), but it adds a separate step that finds the relevant parts before scoring. Untested in the project; paper not opened.",
   "statement": "Mark in two steps: first find the parts of the answer that each criterion refers to, then score each part against its criterion.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "69",
     "quote": "- Multi-agent framework: one agent identifies rubric-relevant components, another scores",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "70",
     "quote": "- Explicit checkpoints constrain reasoning path — improves accuracy and interpretability",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 12-15% and 92-96% match. Line 92 is a result about grounding generation, measured with this test, so it doesn't show the test is valid. The support is that one study used the test as half of its validity measure (line 94). Kept as a concrete method for truth 58 (check topic relevance as its own blocking check), the way truth 5 tests whether a question needs its text, and reworded as that method.",
   "statement": "Test a question's fit to the curriculum by checking that the unit's official scope can answer it.",
   "kind": "external method (one study's validity test)",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "94",
     "quote": "**How validity is measured:** Semantic Textual Similarity against official curriculum + RAG-QA test (a curriculum-aligned question should be answerable using the curriculum's own scope definition). This is analogous to our curriculum_alignment dimension.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "92",
     "quote": "RAG methods go from 12-15% validity to 92-96% validity by grounding generation in official curriculum documents. The study uses GPT-4o as the generator for all conditions — the variable is retrieval, not the model.",
     "verbatim": true
    }
   ],
   "against": "The test's own accuracy is not reported; it was the yardstick, not the thing tested. The study covers one other subject: research_educational_content_generation.md line 276: \"- [Automated Generation of Curriculum-Aligned MCQs for Malaysian Secondary Mathematics](https://arxiv.org/html/2508.04442)\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Kind corrected: these lines are the research summary's recommendation plus its finding that no other verified set exists, not a tested result. The rule is general wherever official released items exist, which covers most assessed courses. The marking side overlaps truth 37 (person-labelled cases) and truth 43 (an independent reference); building items from released ones is new. Wording tightened to name scored sample answers (line 162).",
   "statement": "Build and check generated items and marking guides against official released exam items, their scoring guidelines and scored sample answers.",
   "kind": "recommendation (untested)",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "162",
     "quote": "- Complete scoring guidelines with rubrics, evidence examples, and sample student responses",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "164",
     "quote": "**These are the highest-quality labeled AP rubric examples available.** The College Board releases approximately 3 years of past exams publicly. These are the ground-truth rubrics that a fine-tuning dataset should be derived from or validated against.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "168",
     "quote": "No academic dataset or benchmark for AP history question generation appears in the literature. The College Board materials are the only source of verified AP-style questions and rubrics. Any training dataset must be built from these or synthetically generated and verified against InceptBench.",
     "verbatim": true
    }
   ],
   "against": "The released set is small: research_educational_content_generation.md line 164: \"The College Board releases approximately 3 years of past exams publicly.\" Nothing in the folder tried it.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 3,347 and 4,177 match. Kind corrected from open question: the statement is a rule, and the record names it as a needed step that was never implemented (line 234). The new evidence is that prompts called the store 'VERIFIED correct facts' (sft_v7_benchmark_postmortem.md line 150) while it had never been checked, and that its size changed between documents with no version recorded. This is a precondition of truth 57, with truth 50 covering versioning. Kept as a duplicate because it adds that evidence; knowledge_and_rag_pipeline.md line 230 is already logged against 57.",
   "statement": "Check the reference facts themselves against the official curriculum, and record their version, before calling them verified or using them to write or check items.",
   "kind": "recognised gap (planned, not done)",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/knowledge_and_rag_pipeline.md",
     "lines": "230",
     "quote": "3. **Fact verification:** Each fact in curriculum_facts.json should be verified against AP curriculum documents. Some facts may be outdated or approximate.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/knowledge_and_rag_pipeline.md",
     "lines": "234",
     "quote": "None of these are implemented yet.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
     "lines": "150",
     "quote": "The following are VERIFIED correct facts for this topic.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/knowledge_and_rag_pipeline.md",
     "lines": "14",
     "quote": "**Size:** 4,177 facts (as of April 2026; earlier sessions showed 3,347 facts)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "108",
     "quote": "Our existing `curriculum_facts.json` (3,347+ facts) is a form of RAG grounding. The literature suggests more structured retrieval (graph-based or with explicit entity matching) would improve factual accuracy beyond what flat keyword retrieval achieves.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "57",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep",
   "reason": "Quotes verbatim; 28 units, 150-300 and 100-200 match. The first half is the project's adopted target. The second half is an inference from three things: thinner fact coverage, a stated weaker writer memory (what_is_ap_and_why_it_matters.md line 99, added) and an external result on rare facts. General. Related to truth 49 (report accuracy by skill), but this one is about coverage of units and courses.",
   "statement": "Measure on every unit and course the materials must serve, and check hardest where the subject is least documented and verified facts are thinnest.",
   "kind": "adopted rule plus inference",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
     "lines": "97",
     "quote": "Why 28 units matters: a system that performs well on APUSH but poorly on APWH/APEURO is not production-ready. The 97% target is across ALL 28 units, not just the most-trained ones.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
     "lines": "99",
     "quote": "**The APWH/APEURO challenge:** These courses have less internet training data than US history. The model's parametric memory is weaker for World and European history → more hallucination risk → factual_accuracy harder to achieve.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/knowledge_and_rag_pipeline.md",
     "lines": "217",
     "quote": "**Coverage gaps:** Some units have more facts than others. APUSH tends to have 150-300 facts per unit; APWH and APEURO units may have 100-200. This means APWH/APEURO questions have slightly less curriculum grounding. This partially explains why APWH factual_accuracy failures are more common than APUSH failures.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_model_size_vs_data_quality.md",
     "lines": "113",
     "quote": "The most relevant finding: **\"Fine Tuning vs. RAG for Less Popular Knowledge\"** (SIGIR-AP 2024) showed that RAG surpasses fine-tuning by a large margin specifically for rare or less popular factual knowledge. AP history content includes many obscure primary source documents, minor historical figures, and precise dates — exactly the type of content where parametric knowledge is unreliable in any model under 100B+ parameters.",
     "verbatim": true
    }
   ],
   "against": "No per-course failure rates are given, and the record claims only partial cause: knowledge_and_rag_pipeline.md line 217: \"This partially explains why APWH factual_accuracy failures are more common than APUSH failures.\" The weaker-memory claim in line 99 is asserted, not measured.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 29,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; ~1% matches. The drift was seen 'sometimes' and for one pair of units only (gemini_benchmark_relentless.md line 105, added), so 'it drifts' becomes 'it can drift'. General. A writer-side fix that complements truths 58 and 63.",
   "statement": "Where two units overlap in time or theme, give the writer the rule that tells them apart; otherwise it can drift into the neighbouring unit.",
   "kind": "measured (approximate)",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "105",
     "quote": "**The confusion:** When a prompt says \"Unit 4, 1450-1750,\" the model sometimes generated content about land-based empires (Unit 3 material) because both units share the same time period string.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "110",
     "quote": "**Why this works:** The model already knows the content of both units. The disambiguation doesn't teach new facts — it removes ambiguity about which unit to draw from given a shared time period.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "112",
     "quote": "**Impact:** Reduced curriculum_alignment failures on APWH Unit 3/4 overlap. ~1% improvement.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "25",
     "quote": "2. **Adjacent-topic drift**: Content from a nearby era/domain bleeds in despite topic constraints",
     "verbatim": true
    }
   ],
   "against": "The gain is approximate and overall (~1%), with no counts for the pair.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 30,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 81.9%, 15.1 points, 9 fixes, ~48 hours and ~40-50 iterations match. The second clause ('keep sampling for the last scattered slips') restates truth 65, so it is removed and the record carries only the new half: a failure that repeats points to one specific fault, and each of the nine fixes that worked removed one (line 197). Per-fix gains are approximate.",
   "statement": "Treat a failure that repeats across items as a specific fault to find (wrong scope labels, a missing item type, an instruction that invites invention), not as noise.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "13",
     "quote": "At 81.9%, the system was generating correct AP questions most of the time. The remaining ~18% failures were not random — they were systematic, patterned failures. The key insight that drove the relentless push: every failure is evidence of a specific, fixable bug.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "184",
     "quote": "**Total:** 15.1 percentage point improvement from 9 targeted fixes over ~48 hours.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "197",
     "quote": "The system applied ~40-50 iterations over 48 hours. Most iterations were 0.0% improvement. 9 were significant. The 9 that worked all had the same structure: **a specific, identifiable code/prompt bug causing a specific, measurable dimension to fail.**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "225",
     "quote": "**60-80%:** Usually systematic bugs (wrong metadata, wrong course, missing training examples for a type)",
     "verbatim": true
    }
   ],
   "against": "A repeating failure is not always fixable in the instructions: prompt_engineering_deep_dive.md line 73: \"The failure is at the weight level, not the prompt level.\" The source's 'every failure is evidence of a specific, fixable bug' overreaches: its own last 3% were random (gemini_benchmark_relentless.md line 208: \"The remaining 3% failures are stochastic hallucinations:\").",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The catalogue is the project's heuristic. As written ('points to'), it reads as a diagnosis, but the folder's own MCQ import bug made a whole item type fail for a different reason. So each pattern is framed as a hypothesis to test (debugging_methodology.md steps 4-6, lines 13-15), and 'or a routing fault' is added. The cost of skipping the test is observed (line 19). Overlaps truths 60 and 63; adds the step from pattern to hypothesis.",
   "statement": "Read the shape of the failures, then test the cause it points to before fixing: a whole unit failing suggests wrong scope labels; a whole item type failing, missing examples or a routing fault; right content on the wrong topic, an ignored constraint; right content with wrong specifics, invented details.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/debugging_methodology.md",
     "lines": "128-129",
     "quote": "**Signature:** Entire unit/course at 0% despite other units passing\n**Cause:** Wrong metadata (time period, course, unit) being passed to model",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/debugging_methodology.md",
     "lines": "119-120",
     "quote": "**Signature:** Entire type/class at 0% or near-0%\n**Cause:** That class has little or no representation in training data",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/debugging_methodology.md",
     "lines": "137-138",
     "quote": "**Signature:** Model generates correct content for the WRONG thing it was told to do\n**Cause:** Training data lacked hard negatives for constraint adherence",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/debugging_methodology.md",
     "lines": "146-147",
     "quote": "**Signature:** Facts are mostly right, but specific details (dates, attributions, names) are wrong\n**Cause:** Model's parametric memory generates plausible details that aren't factually correct",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/debugging_methodology.md",
     "lines": "13-15",
     "quote": "4. HYPOTHESIS → generate 2-3 possible root causes\n5. DISTINGUISH → find the test that differentiates hypotheses\n6. CONFIRM → run the test, accept one hypothesis",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/debugging_methodology.md",
     "lines": "19",
     "quote": "Never skip to step 7. Every time we skipped steps (went from aggregate failure to guessing at a fix), we wasted a training run.",
     "verbatim": true
    }
   ],
   "against": "A whole item type failed because of a routing fault, not missing examples: sft_v7_benchmark_postmortem.md line 26: \"**Symptom:** All MCQ items returned empty content (`generated_content: {}`), score 0.0.\" Even with the framework, the first hypotheses were wrong: stage2_postmortem_full.md line 180: \"5. **Three wrong turns is normal.** The first hypothesis is usually \"something broke.\" The second is \"maybe we can fix it at inference time.\" The third is \"maybe the conditions weren't right.\" Root cause often requires ruling all of these out.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 32,
   "verdict": "keep",
   "reason": "Quotes verbatim; 90% vs 70-75% and 0.5% match. The inflated claim and the regressions come from two different automated improvers (failures_and_false_starts.md lines 102-103; overnight_automation.md lines 224-226), and the statement covers both. General. It applies truth 43 (check against something that doesn't assume the answer) and is close to truth 66, but its target is an improver's reports of its own gains; it adds evidence.",
   "statement": "Re-measure any gain an automated improver reports with a check it doesn't control; its self-reports ran high and some of its edits made things worse.",
   "kind": "observed",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/failures_and_false_starts.md",
     "lines": "103",
     "quote": "- Claimed 90% MCQ_SET pass rate (actual: 70-75%)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/overnight_automation.md",
     "lines": "225",
     "quote": "- Sometimes proposed a prompt change that made things slightly worse (0.5% regression)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/overnight_automation.md",
     "lines": "226",
     "quote": "- Rarely caught code bugs (like the f-string bug) — those needed human review",
     "verbatim": true
    }
   ],
   "against": "The automated loop did produce real gains when the next run measured every change: gemini_benchmark_relentless.md line 197: \"The system applied ~40-50 iterations over 48 hours. Most iterations were 0.0% improvement. 9 were significant.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 33,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 8192, 20-30% and 50% match. Recast from an open question to the rule the evidence supports. Vendor guidance and the research summary say to size caps from real maximum lengths plus headroom. The project also saw timeouts return empty or truncated items and added a completeness check (gemini_benchmark_relentless.md lines 161-164). The open part, whether caps caused the missing options, stays in against. The completeness check overlaps truth 24 (measure from the delivered file).",
   "statement": "Size any output length cap from the longest real outputs plus headroom, and check that every delivered item is complete; a cap or timeout can cut an item short without an error.",
   "kind": "vendor guidance and observed",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_qwen3_structured_multistage.md",
     "lines": "54",
     "quote": "- **Never set `max_tokens` below the worst-case full output length.** For complex AP exam questions with 5+ nested fields, estimate the maximum possible output and add a 20-30% buffer.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_qwen3_structured_multistage.md",
     "lines": "59",
     "quote": "**Practical recommendation:** Profile your longest outputs per question type before setting token limits. Add 30% headroom. For mcq_set (3 questions + stimulus), 8192 is probably borderline — consider 12000-16000.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "161",
     "quote": "**Result of timeout:** The generator returned an empty or truncated response. Score: 0.0.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "163-164",
     "quote": "**Fix:** Added JSON truncation detection after the Pro call:\n1. Check if the response JSON is complete (count opening vs closing braces)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
     "lines": "18",
     "quote": "Missing answer choices, incomplete JSON. Root cause: **token limit truncation** — Alibaba Cloud docs explicitly warn that capping `max_tokens` below worst-case output causes silently truncated JSON. Our `mcq_set_questions` limit of 8192 is borderline. Secondary cause: SFT loss doesn't shape partial schema correctness.",
     "verbatim": true
    }
   ],
   "against": "Whether caps caused the missing answer options here is unsettled: pipeline_architecture_insight.md line 70: \"- No quality regression observed after the reduction\". The project's own rule can set a cap below the worst case: pipeline_architecture_insight.md line 73: \"Rule: For any new model, find the token ceiling empirically. Run 5 DBQ requests, find where timeouts start, set limit at 50% of that.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 34,
   "verdict": "keep",
   "reason": "Quotes verbatim; 13.83%, ~50% and 96% match. Traced further back. The '13-50%' merge starts in the research summary itself (research_rag_factual_grounding.md line 359) before the synthesis calls it 'Published results'. The misplaced pre-writing effect starts in research_qwen3_structured_multistage.md line 281. An arXiv 2601 ID is also dated 'Jan 2025' (research_dpo_grpo_factual.md line 26). General; not on the list. Close to truth 61 (don't build on unchecked notes), but about acting on research summaries.",
   "statement": "Check every cited result against its source before acting on it; summaries merged, moved and relabelled numbers.",
   "kind": "observed (cross-document audit)",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
     "lines": "204",
     "quote": "Results: Citation grounding improved by **13.83%** on production benchmarks versus standard RAG prompting. However, only ~50% of sentences achieved perfect citation coverage without fine-tuning, suggesting a ceiling that requires SFT to overcome fully.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
     "lines": "359",
     "quote": "Expected result: 13-50% grounding improvement based on the SIGIR 2025 paper.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
     "lines": "30",
     "quote": "Force the model to emit `[FACT: <exact quote from curriculum_facts>]` before each specific historical claim in scoring notes. Zero cost to try. Published results: 13-50% grounding improvement. Ceiling ~50% without training, but combined with the existing anchor-fact constraint this should push SAQ above 0%.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "90",
     "quote": "| Manual RAG with custom chunking | 0.89 | 96% |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/INDEX.md",
     "lines": "85",
     "quote": "| [research_educational_content_generation.md](research_educational_content_generation.md) | GraphRAG (96% curriculum validity), VeriFact-CoT (83% vs 72%), frontier baseline 69% |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "231",
     "quote": "Published results show 93→97% pass rates after DPO in our own session logs (team_learnings_20260422.md).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
     "lines": "60",
     "quote": "VeriFact-CoT paper shows this halves hallucination rate from ~25% to ~12%.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_qwen3_structured_multistage.md",
     "lines": "281",
     "quote": "The VeriFact-CoT and FADER research both show that explicitly surfacing relevant facts before the generative call reduces hallucination from ~25% to ~12%.",
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
   "reason": "Quote verbatim; 60% matches. Rephrased as an open question, the way the list words its open items, and without the record's job-role wording. No review time was measured anywhere in the folder; the quality bands in what_is_ap_and_why_it_matters.md lines 105-115 are all framing.",
   "statement": "How low a pass rate can go before reviewing generated items costs more time than it saves is unmeasured (open); the record guesses about 60%.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
     "lines": "114-115",
     "quote": "### Below 60%\nUnreliable. Some questions are excellent, many have significant errors. Teacher would spend more time reviewing than they'd save from automation.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 36,
   "verdict": "drop",
   "reason": "Quotes verbatim, but the support is one study summarised without figures, for an architecture the project planned and never built. The synthesis credits it with a 96% that belongs to another method (research_educational_content_generation.md line 90). The goal, following the course's facts over the writer's own, is truth 57, and nothing shows the storage choice is what achieves it. Re-raise if it is ever measured.",
   "statement": "Store a course's facts as linked entities with verified attributes and relations, so items can follow the course's own facts even where a writer's general knowledge disagrees.",
   "kind": "external research (one study, no figures)",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "101",
     "quote": "- When tested on altered textbook facts (KnowShiftQA dataset), GraphRAG Local maintained adherence to curriculum content even when it contradicted the LLM's internal knowledge",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
     "lines": "64",
     "quote": "Better: entity-relationship graph — events and people as nodes, verified dates as attributes, causal relationships as edges. Force rubric evidence to come from retrieved *graph nodes* not flat strings.",
     "verbatim": true
    }
   ],
   "against": "The synthesis credits graph retrieval with another method's result: master_strategy_apr24.md line 65: \"Published result: 96% curriculum validity vs 12% ungrounded using the same model.\" The source table gives that 96% to custom chunking: research_educational_content_generation.md line 90: \"| Manual RAG with custom chunking | 0.89 | 96% |\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 37,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 13.83% and ~50% match (research_rag_factual_grounding.md line 204). The measured part is a 13.83% gain in citation grounding, with only about half the sentences fully covered, in e-commerce dialogue. That limit is added to the statement. The verbatim anchor the project did deploy supplies the part code can check (prompt_engineering_deep_dive.md lines 107-108). Exact copying checked in code is truth 17; kept as a duplicate because it adds the cite-before-claim order and outside evidence. Planned here, not tested.",
   "statement": "Have the writer copy the exact supporting fact before each specific claim, so code can check each claim's source; prompting alone left about half the sentences without full support.",
   "kind": "external research; planned here, not measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
     "lines": "200",
     "quote": "Rather than generating claims freely and optionally citing afterward, the \"cite first\" constraint forces the model to locate supporting evidence before committing to a claim. This exploits the autoregressive structure: once the model has emitted a citation token pointing to a specific fact, the conditional probability of hallucinating a different fact drops sharply.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
     "lines": "204",
     "quote": "Results: Citation grounding improved by **13.83%** on production benchmarks versus standard RAG prompting. However, only ~50% of sentences achieved perfect citation coverage without fine-tuning, suggesting a ceiling that requires SFT to overcome fully.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
     "lines": "107",
     "quote": "1. Forces explicit selection commitment (anchor_fact in plan JSON = traceable)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
     "lines": "108",
     "quote": "2. The verbatim copy creates a ground truth to compare against",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
     "lines": "34-35",
     "quote": "Before writing any specific date, name, treaty, or event in scoring notes, first write:\n[FACT: <copy the exact phrase from VERIFIED FACTS above that supports this claim>]",
     "verbatim": true
    }
   ],
   "against": "The mechanism in line 200 is the summary's explanation, not a measurement. The synthesis misquotes the result: master_strategy_apr24.md line 30: \"Published results: 13-50% grounding improvement.\"",
   "general": true,
   "duplicate_of": "17",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 6,
   "effect": "supports: each question must be answerable from the source alone",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
   "lines": "12",
   "quote": "2. All 3 questions must be independently answerable from the stimulus alone",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "indirect at best: training-label balance for a yes/no model (one team, no figures), not where the key sits among options",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/cross_team_learnings_full.md",
   "lines": "147",
   "quote": "1. **Yes/No class balance** (one team): Model was biased toward one answer class because training data had 70/30 split. Balancing to 50/50 improved calibration.",
   "ok": false
  },
  {
   "truth": 9,
   "effect": "supports by analogy: borderline passes kept out of the training signal",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/dpo_and_fdpo_pipeline.md",
   "lines": "30-31",
   "quote": "- Higher bar preferred: score ≥ 0.90 (not just barely passing)\n- Rationale: the \"chosen\" side needs to be clearly good, not borderline",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports (a predicted benefit of the verbatim anchor, not measured)",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
   "lines": "108",
   "quote": "2. The verbatim copy creates a ground truth to compare against",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports weakly: the judge applied the wrong item type's rules; the record calls the cause only a possible misconfiguration",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
   "lines": "86",
   "quote": "2. `specification_compliance`: InceptBench occasionally treats DBQ as if it should be a closed-ended MCQ question, not a document-based essay prompt. This may be an evaluator misconfiguration, not a real quality issue.",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
   "lines": "121",
   "quote": "InceptBench has a stochastic evaluation component (likely using a language model as part of the rubric). Running the SAME generation through the evaluator 4 times produces different results.",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports the first half: the writer's errors are consistent",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/debugging_methodology.md",
   "lines": "148",
   "quote": "**Diagnostic:** Errors are in specific facts, not structural; model is consistent in its errors",
   "ok": true
  },
  {
   "truth": 36,
   "effect": "supports by analogy: a generation fallback, not a marking fallback, ran silently for every item",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
   "lines": "31",
   "quote": "**Result:** The MCQ Research step NEVER WORKED. Every MCQ and MCQ_SET generation silently fell back to a legacy one-shot path. The research was supposed to gather verified primary sources — it never ran.",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports (calibration asserted; no figures)",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
   "lines": "179",
   "quote": "**Known:** InceptBench was calibrated against AP teacher review panels. It's not perfect, but it's the closest proxy available.",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
   "lines": "48-49",
   "quote": "- Multi-dimensional calibration via trained neural network; 2x improvement over uncalibrated baselines\n- Achieves RMS error < 0.5 on 1-4 scale predicting human judge satisfaction",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports: plant one subtle fault, then confirm the check catches it (used here to build training pairs); source lines 442-443 end in trailing spaces, reproduced",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_dpo_grpo_factual.md",
   "lines": "442-444",
   "quote": "Take this AP history exam question and introduce one subtle factual error (wrong year, \nwrong person, wrong founding date). Keep everything else identical. The error should be \nplausible — not obviously wrong, but verifiably incorrect per standard AP curriculum.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_dpo_grpo_factual.md",
   "lines": "447",
   "quote": "Run the synthetic rejected responses through InceptBench to confirm they fail factual_accuracy before including them in training. Keep only (chosen=PASS, rejected=FAIL) pairs.",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports the first half: keep the full prompt with each result",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/dpo_and_fdpo_pipeline.md",
   "lines": "98",
   "quote": "**The `prompt_messages` fix:** `eval_finetuned.py` was modified to save `prompt_messages` (the system + user turns that preceded the generation) in each result when `SAVE_ALL_CONTENT=1`. Without this, `build_fdpo_dataset.py` only had the generated content, not the full conversation context needed for DPO pairs.",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
   "lines": "37",
   "quote": "**MCQ_SET:** One shared stimulus, THREE questions that all reference that same stimulus, each testing a different historical thinking skill.",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/debugging_methodology.md",
   "lines": "203",
   "quote": "The CC provides an independent diagnostic perspective. When you've been staring at a failure for 2 hours and have formed strong hypotheses, an external audit can quickly confirm or reject them without the same anchoring bias.",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "counter, partial: a self-check against the writer's own knowledge still raised accuracy (83% vs 72%, and above CoT+RAG at 78%); not shown to equal an independent check",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
   "lines": "137-141",
   "quote": "3. Verify each claim against internal knowledge\n4. Refine and correct the output\n\n**Quantitative results:**\n- Factual Accuracy: **83%** (vs 72% standard CoT, 78% CoT+RAG)",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
   "lines": "189",
   "quote": "**Practical implication:** InceptBench 97% pass rate does NOT mean 97% of questions are publishable. Some will require teacher review. But it's a reliable quality gate for training and benchmarking purposes.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "not about machine checks: expert review of unchecked generations, with no machine check in the comparison",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
   "lines": "14",
   "quote": "The most cited statistic in recent literature (2024-2025) is that when AI-generated exam questions are reviewed by subject experts, approximately **69% are fit for inclusion with little or no modification**, while **31% are rejected for factual inaccuracies or misalignment with learning objectives**. This is the baseline for unconstrained frontier model generation (GPT-4 class).",
   "ok": false
  },
  {
   "truth": 44,
   "effect": "does not bear on 44 as quoted: the kind of quality assurance is unstated, and the finding is that checked items perform like human-written ones",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
   "lines": "18",
   "quote": "- \"Assessing the Quality of AI-Generated Exams: A Large-Scale Field Study\" (arXiv 2508.08314) — field study at scale; AI-authored questions that pass quality assurance \"do not perform differently from human-authored questions\"",
   "ok": false
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/overnight_automation.md",
   "lines": "226",
   "quote": "- Rarely caught code bugs (like the f-string bug) — those needed human review",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "counter, weak: an unmeasured assertion, contradicted by evaluation_methodology.md line 189",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
   "lines": "106",
   "quote": "Every question would be usable on an actual AP exam without teacher modification. Correct historical content, period-accurate, right cognitive level, right structural format. A teacher reviewing these questions would accept them for direct use.",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/stage2_postmortem_full.md",
   "lines": "62",
   "quote": "**CC's finding:** The training format was actually CLOSER to the evaluation format than the production generator format. Stage 2 learned to respond to simplified prompts correctly. Running it through the production generator (the MOST out-of-distribution option) would make things worse, not better.",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/grpo_failures_deep_dive.md",
   "lines": "39",
   "quote": "**The critical lesson:** ALWAYS test the raw rollout format, not the production pipeline format. They are NOT the same. Production: `model → strip_thinking → json.loads`. GRPO rollout: `model → json.loads`. That stripping step is not there.",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports the first half: a passed gate doesn't cover student experience",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
   "lines": "187",
   "quote": "- It doesn't test \"student experience\" — a confusing but technically correct question can pass",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports by analogy: break results down by dimension, not just pass/fail",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
   "lines": "158",
   "quote": "**Look at which dimensions failed, not just whether it passed.**",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports: a training job's lineage was lost",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/fireworks_training_reference.md",
   "lines": "62",
   "quote": "- **Assessment:** Never benchmarked. Did this become sft-v6? Unknown. sft-v6 was deployed at some point with a pass rate of ~27%.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/failures_and_false_starts.md",
   "lines": "137",
   "quote": "**Pattern:** Metadata bugs are easy to overlook because they don't affect training quality directly. But they accumulate over time and make later analysis harder. Worth fixing before the next DPO dataset build.",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
   "lines": "47",
   "quote": "The failures are NOT in the question itself. They're in the **scoring notes the model generates**.",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports (mechanism, as summarised)",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
   "lines": "35",
   "quote": "- **Task format**: When the generation task involves producing many fields simultaneously (like a structured rubric with question stem, answer choices, scoring guide, and historical evidence), the model's attention dilutes across fields and it falls back on parametric defaults for lower-salience fields like rubric details.",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "counter, limit: the 'no specific evidence' instruction failed on a smaller writer, and the next plan allowed verified facts in marking guides",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
   "lines": "132",
   "quote": "2. **The current approach (negative prompting) seemed to work on Gemini.** Because Gemini is large enough to mostly respect the \"no specific evidence\" instruction and has accurate enough parametric memory that when it does include evidence, it's usually right. The instruction that's good enough for a large model is insufficient for a 14B model.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
   "lines": "92",
   "quote": "RAG methods go from 12-15% validity to 92-96% validity by grounding generation in official curriculum documents. The study uses GPT-4o as the generator for all conditions — the variable is retrieval, not the model.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
   "lines": "229",
   "quote": "This is a \"closed-world\" approach: rather than asking the model to generate historical facts from open memory, you preemptively supply the plausible candidates and the model's job is selection rather than recall.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports the mechanism; also warns that supplied fixed facts (dates, names, places) are the hardest to make a writer follow",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
   "lines": "33",
   "quote": "- **Fact dynamicity**: Models are least persuadable by retrieved context for *static* historical facts (dates, names, places) — exactly the kind of facts in our rubrics. Dynamic/recent facts are easier to override with context. (ECIR 2025 keynote, arXiv:2603.09654)",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "counter: the store called verified was never checked",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/knowledge_and_rag_pipeline.md",
   "lines": "230",
   "quote": "3. **Fact verification:** Each fact in curriculum_facts.json should be verified against AP curriculum documents. Some facts may be outdated or approximate.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "counter (predicted, not measured)",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
   "lines": "113",
   "quote": "2. At inference time, the model will sometimes follow the constraint, sometimes not",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
   "lines": "25",
   "quote": "2. **Adjacent-topic drift**: Content from a nearby era/domain bleeds in despite topic constraints",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports (rationale, not a measurement)",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
   "lines": "125",
   "quote": "4. Wrong information in practice questions could hurt student performance on the actual exam",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
   "lines": "89",
   "quote": "- One wrong date in one document = hard fail for the whole DBQ",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
   "lines": "180",
   "quote": "- **Medical domain** (strictest): 100% factual accuracy required for clinical exam questions; 69% pass rate reported for unconstrained GPT-4 generation",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports: an aggregate rose for reasons unrelated to the dimension being fixed",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
   "lines": "70",
   "quote": "The curriculum facts help non-critical dimensions (educational_accuracy, etc.) enough to push borderline items above the 0.85 threshold, even though they don't help factual_accuracy specifically.",
   "ok": true
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
   "lines": "24",
   "quote": "- Research step chained stimulus to potentially bad sources (if the research hallucinated a source, the stimulus inherited the hallucination)",
   "ok": true
  },
  {
   "truth": 61,
   "effect": "counter: for single questions on the large writer, the research step raised 96% to 100% (sample size not given)",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
   "lines": "36",
   "quote": "- MCQ: 96% → 100% (research step immediately improved factual accuracy)",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
   "lines": "62",
   "quote": "**Why it doesn't work:** The model ignores negative constraints. It has strong parametric associations (France → exploration → Protestant → Huguenots → plausible but wrong) that override the instruction. Telling the model \"don't use specific facts\" just means it uses wrong specific facts instead of right ones.",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "supports (30% vs 45% pass at N=20; factual accuracy unchanged at 60%)",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/failures_and_false_starts.md",
   "lines": "124",
   "quote": "**The \"caution\" variant also failed:** Adding \"be careful\" warnings about factual accuracy produced 30% pass rate — worse than anything. Warnings that tell the model to be careful without giving it actual constraints just introduce hedging behavior. The model starts prefacing with qualifications instead of generating confident content.",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/stage2_postmortem_full.md",
   "lines": "82",
   "quote": "**Result:** Failures persisted. Stage 2 still generated about William Penn when asked for FDR.",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
   "lines": "81",
   "quote": "**Why this was missed:** The code was doing \"clever\" re-derivation of course/unit from substandard_id. The problem with re-derivation: KC-prefixed standards are APWH-specific notation that the parser didn't handle. Passing explicit values eliminates the re-derivation entirely.",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
   "lines": "29",
   "quote": "Every APEURO Unit 4 question automatically failed `curriculum_alignment` because the generated content referenced 1648-1815 material but the evaluator expected 1914-present content.",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports weakly: one team, judged 'Not well-validated' at line 138",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/cross_team_learnings_full.md",
   "lines": "137",
   "quote": "**One team tried:** 0.01 weight on items where model references missing images. Helped eliminate that specific failure mode.",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_model_size_vs_data_quality.md",
   "lines": "140",
   "quote": "**Practical implication:** If the 14B model's failure rate is 67% (as currently), even N=100 won't reliably get to 90%+ because the *type* of failures (fabricated attribution) is deterministic, not stochastic. But if data quality fixes bring pass rate to 70-80%, then Best-of-N=5 at $0.20/M is more economical than 70B at $0.90/M.",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports; the same file's best-of-N arithmetic assumes independent tries, which systematic failures break",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/pipeline_architecture_insight.md",
   "lines": "100",
   "quote": "So Best-of-N is a multiplier, not a miracle. The base model still needs to be competent. Target P≥0.60 per type before Best-of-N becomes highly effective.",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
   "lines": "406",
   "quote": "Beyond the principle, our evaluator results show the model consistently picks wrong facts — this is a systematic failure, not a stochastic one that retries would fix.",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports (asserted; no count of wrong records is given)",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
   "lines": "112",
   "quote": "**Why 40% might be the new ceiling:** The training data (raft_combined) itself has fabricated attributions. Some of the 18,768 MCQ_SET records have slightly wrong dates or sources — they just passed InceptBench at the time, which has a 50% flip rate. Training on data that sometimes has wrong attributions = training on signal + noise.",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "counter, unsupported: keeping the top of five noisy scores selects for judge noise rather than averaging it out, which is the bias truth 66 guards against",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
   "lines": "137",
   "quote": "3. **Best-of-N exploits this.** If we generate 5 candidates and pick the best, we're not just picking the highest-quality generation — we're also averaging out evaluator noise. An item that would flip 50% gets scored 5 times; we keep the one that scored highest, which correlates with being genuinely better even if the noise is high.",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/pipeline_architecture_insight.md",
   "lines": "58",
   "quote": "- auto-overrides reasoning_type if learning objective contains \"Compare\" or \"continuity and change\"",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports weakly (a predicted benefit): the judge is bound to a fact that code fixed verbatim",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
   "lines": "109",
   "quote": "3. The constraint is specific and checkable (\"derivable from\")",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/overnight_automation.md",
   "lines": "212",
   "quote": "1. **Testable:** The next tick measures whether THAT specific change improved things. Multiple simultaneous changes = unknown attribution.",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
   "lines": "202",
   "quote": "The analyst was forced to propose ONE change, not multiple. This made each iteration testable.",
   "ok": true
  }
 ]
}
```
