# read:ml-learnings-deep

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "ml-learnings-deep",
 "coverage": {
  "read": [
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/INDEX.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/decisions_and_pivots_timeline.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/grpo_failures_deep_dive.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/grpo_design_and_theory.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/dpo_and_fdpo_pipeline.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/agent_delegation_architecture.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/debugging_methodology.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_dpo_grpo_factual.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_model_size_vs_data_quality.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_qwen3_structured_multistage.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_to_do_next.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/knowledge_and_rag_pipeline.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/cross_team_learnings_full.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/failures_and_false_starts.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/stage2_postmortem_full.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/training_data_journey.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/pipeline_architecture_insight.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/week_of_apr_21.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_version_history.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/overnight_automation.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/infrastructure_and_tooling.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/fireworks_training_reference.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/render_deployment.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/beads_workflow.md"
  ],
  "skipped": [
   "The external studies cited in the research_* files (arXiv, ACL, PMC, MDPI, SIGIR, vendor docs): not opened, because network access was not allowed. They are cited only as the folder writes them, with the URLs or IDs it gives.",
   "Memory and audit notes the documents cite that live outside this folder (sft_v4_prompt_engineering.md, team_learnings_20260422.md, training_data_audit_20260423.md, postit_20260423.md, fdpo_pipeline.md, grpo_failures.md, stage2_postmortem.md, session_20260422): outside this direction's scope.",
   "The rest of ~/Library/Mobile Documents/com~apple~CloudDocs/work/ (generator repos, inceptbench copies, .sql/.zip dumps): outside this direction's scope. The ML learnings folder holds only the 33 .md files read here and no data dumps."
  ],
  "notes": "In every against field, 'ML learnings/<file>' means ~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/<file>. The only name in any in-scope path is the home-directory account name, which every path shares. No file path carries anyone else's name, so name_bearing_source is false throughout. cross_team_learnings_full.md names colleagues in its text: no statement uses them, and the quotes taken from it were chosen to contain no names. All documents date from 2026-04-24 or earlier. Fixes planned on that date have no measured outcome in the folder: the coverage list in the plan, verified facts in marking guides, cite-before-claim, claim-by-claim verification and the graph fact store. Samples are small: the sft-v7 run was 24 items (2 to 6 per type), and the prompt sweep used N=20 per variant, so a 5-point gap is one item. Conflicts found between documents: (1) sft-v4 'overall' appears as 6.5%, ~27% and ~60%, and two runs both labelled N=100 disagree. (2) The 0% to 18% 'pipeline' jump is confounded with a token-limit change. (3) The cross-team rule 'More data > better data' contradicts the research rule that quality beats quantity. (4) The rule 'verification and regeneration are not valid approaches' sits beside the adopted Best-of-N=5 and a planned verification step. (5) Token caps are called both the root cause of missing answer choices and a change with 'no quality regression'. (6) Summaries drift from sources: graph retrieval is credited with a 96% that belongs to custom chunking; '13-50%' merges a 13.83% gain with a 50% ceiling; an internal team result is called 'Published'; arXiv 2601.03027 is dated 'Jan 2025'; VeriFact-CoT is credited with a pre-call effect it did not test (master_strategy_apr24.md line 60). The earlier pass's findings for truths 56-70 were rechecked; new support and counter-evidence for them is listed under evidence_for_existing."
 },
 "candidates": [
  {
   "statement": "Every wrong option in a multiple-choice item must be plausible; an item whose answer is obvious fails as an assessment.",
   "kind": "adopted rule",
   "found_by": "The judge's educational-accuracy check is a hard gate for single multiple-choice items and for question sets. It lists implausible distractors ('one obvious correct answer') as a failure mode. The item spec requires three plausible distractors, and the writer's research step was told to produce plausible distractor events.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "79",
     "quote": "- Answer choices aren't plausible distractors (one obvious correct answer)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
     "lines": "35",
     "quote": "**MCQ:** One stimulus (primary source), one question stem, four answer choices (A-D), exactly one correct answer, three plausible distractors."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/knowledge_and_rag_pipeline.md",
     "lines": "147-148",
     "quote": "Generate research notes about [topic], identifying: 1 specific historical claim,\nreliable date range, and 2 plausible distractor events."
    }
   ],
   "against": "The folder has no count of distractor failures, and it describes the judge as lenient on teaching value: ML learnings/evaluation_methodology.md line 186: \"- It doesn't fully test \"pedagogical value\" — a factually correct question that teaches the wrong skill can still pass\".",
   "adds_to_existing": [
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Each question should test the reasoning its objective names, at the course's level: neither bare recall of what happened nor analysis the course doesn't ask for.",
   "kind": "adopted rule",
   "found_by": "The judge fails three kinds of item: those that only test recall, those that use a different reasoning type from the one the objective names (causation asked where comparison was required), and those pitched above or below the course. The generator also sets an essay's reasoning type in code from the objective's wording (pipeline_architecture_insight.md line 58).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
     "lines": "57",
     "quote": "Questions must explicitly test one of these skills. A question that just asks \"what happened?\" fails `educational_accuracy` because it tests recall, not historical thinking."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "90",
     "quote": "- Learning objective mismatch (question asks for causation when LO requires comparison)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "77-78",
     "quote": "- Question tests college-level historical analysis that AP students don't need\n- Question is too easy (tests rote recall when AP requires analysis)"
    }
   ],
   "against": "The judge may miss a skill mismatch: ML learnings/evaluation_methodology.md line 186: \"- It doesn't fully test \"pedagogical value\" — a factually correct question that teaches the wrong skill can still pass\".",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When an objective spans several cases, list the cases in the plan and tie each question to a different one; left alone, a writer piles its questions onto the most prominent case.",
   "kind": "measured",
   "found_by": "On the first partial run the question set passed 1/4 (25%), failing concept coverage. The judge found the quiz concentrated on one explorer and one nation, while the objective covered several nations; the plan step had not enforced coverage. The fix was planned but not yet measured: an explicit list of cases in the plan, with one case per question.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
     "lines": "71",
     "quote": "- *\"The quiz is heavily concentrated on Columbus and Spanish motivations. For the stated objective—causes of exploration by various European nations—it does not adequately assess Portugal, France, or England.\"*"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
     "lines": "75",
     "quote": "- The plan step is supposed to force multi-nation coverage but the model picks the most prominent entity in the topic (Columbus/Spain) and concentrates questions there."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
     "lines": "43",
     "quote": "Add `nations_to_cover: [\"Portugal\", \"Spain\", \"France\", \"England\"]` field to the Plan step output schema. Question step: each question must address a different nation from the plan. Prompt-only change in `mcq_set.py`."
    }
   ],
   "against": "Four items only: ML learnings/sft_v7_benchmark_postmortem.md line 20: \"This is a partial run (unit 1 only, benchmark still in progress). But the failure patterns are clear enough to diagnose.\" The fix has only an expected gain: ML learnings/what_to_do_next.md line 33: \"- MCQ_SET: 25% → ~40%\".",
   "adds_to_existing": [
    41,
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make a complex item in separate steps that each do one job (plan, then source, then questions) rather than in one pass that does everything.",
   "kind": "adopted rule",
   "found_by": "The same writer went from 0% to 18% valid question sets (N=100) once run through the plan, source, questions pipeline. A single call writing seven documents drifted and invented attributions in the later documents. Writing source and questions in one step also made failures hard to diagnose (mcq_set_journey.md line 25). The research summary's test for adding a step is whether that step does one thing that can't be done well alongside the others.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/decisions_and_pivots_timeline.md",
     "lines": "84",
     "quote": "**MCQ_SET jumped from 0% to 18%.** Not because we changed the model. Because we gave it the pipeline."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
     "lines": "88",
     "quote": "**Why factual accuracy fails in DBQ:** 7 documents, each needing a plausible historical source, date, and content. The model generates all 7 in one call. By documents 4-7, it's drifted from its context and starts confabulating attributions."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_qwen3_structured_multistage.md",
     "lines": "215",
     "quote": "**The right question is not \"how many stages\" but \"does each stage do one thing the model can't do well simultaneously with other things?\"**"
    }
   ],
   "against": "The 0% to 18% jump is confounded. ML learnings/mcq_set_journey.md line 154 records the 0% run as \"| sft-v4, Apr 22 | 0% | 3-step pipeline, Fireworks | No MCQ_SET in training data |\" and line 155 records the 18% run as \"| sft-v4 after pipeline port | 18% (N=100) | 3-step pipeline + proper token limits | Token limits reduced 32K→8K |\". A step can also hurt: ML learnings/mcq_set_journey.md line 48: \"**Counter-intuitive finding:** Removing the research step IMPROVED MCQ_SET quality. The research step was a hallucination amplifier, not a quality gate.\" Limit: ML learnings/research_qwen3_structured_multistage.md line 251: \"- When the sub-task outputs need tight semantic coupling (e.g., you can't generate the introduction and body separately if they need to reference each other)\".",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Every specific a writer must produce from memory (a date, a name, a figure, a source line) is another chance to be wrong, so ask only for the specifics the task needs.",
   "kind": "measured",
   "found_by": "Dropping the named-source requirement raised factual accuracy from 60% to 70% (N=20 per variant). A seven-document item holds seven independent claims that must all be right, and 0/2 passed. A shorter marking guide failed less often from the same root cause (essay 4/6 vs short answer 0/6). A more inventive writer wrote longer, more detailed documents with more fabricated details.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "130",
     "quote": "**The broader lesson:** The more specific the evidence the model is asked to enumerate, the more hallucination surface area. Every specific claim (date, name, treaty, publication founding year) is an opportunity for the model to be slightly wrong. Reducing the specificity requirement reduces the hallucination rate."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
     "lines": "116",
     "quote": "**3. DBQ document generation is the hardest factual load.** 7 documents × each needing accurate source/date/content = 7 independent factual claims that all must be correct. Probability of all 7 being right with a 14B model: low."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "168",
     "quote": "**The counterintuitive insight:** Flash produces CLEANER DBQ outputs than Pro in some cases. Pro's creativity → longer, more detailed documents → more hallucination surface area. Flash's conservatism → shorter, more cautious documents → fewer fabricated details → better factual_accuracy."
    }
   ],
   "against": "Cutting further did not help: ML learnings/prompt_engineering_deep_dive.md line 59: \"| no_source_nodates | 40% | 50% | No source + no dates |\" (vs 70% with only the source dropped, N=20 each). Forbidding specifics is not the same as not asking for them: ML learnings/master_strategy_apr24.md line 105: \"We have \"⛔ NEVER use specific dates\" and it produced 0% SAQ.\"",
   "adds_to_existing": [
    56,
    59,
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Never let a writer invent who wrote a source passage, or when and where it appeared; take the attribution from a verified record or leave it off.",
   "kind": "measured",
   "found_by": "Invented attributions were the main point of fabrication in generated source passages. Removing the named-source requirement gave the best factual accuracy in a nine-variant sweep (70% vs 60% baseline, N=20 each). Taking author, year and title from one verified fact left the writer nothing to fill in. A planned pre-step would fix author, date and title for each document from verified facts before writing (master_strategy_apr24.md line 60).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
     "lines": "67",
     "quote": "The main hallucination vector for MCQ is the source attribution in the stimulus (e.g., \"— Thomas Jefferson, 1799\" that the model invented). Removing the requirement to provide a named source eliminates the fabrication opportunity."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
     "lines": "169",
     "quote": "3. **Attribution is the trap.** Every MCQ_SET needs a historical author and date. The model learned to generate plausible-sounding attributions. Plausible ≠ accurate."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
     "lines": "142",
     "quote": "**Why this reduces hallucination:** The model can't hallucinate what it doesn't need to fill in. If the anchor_fact says \"1889 essay 'Wealth'\", the model has the year, the genre, and the argument. There's nothing to fabricate."
    }
   ],
   "against": "The pipeline still writes new passages credited to real authors; only their claims are tied to the verified fact: ML learnings/mcq_set_journey.md line 63: \"- Output: primary source passage attributed to the historical author in the plan\". Instructions alone did not stop the invention: ML learnings/prompt_engineering_deep_dive.md line 73: \"No matter how you phrase the prompt, the model defaults to its training behavior when generating a historical document excerpt.\"",
   "adds_to_existing": [
    17,
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Re-test every instruction whenever the writer changes; an instruction a stronger writer obeyed, a weaker one ignored.",
   "kind": "measured",
   "found_by": "Under the same marking-guide instructions, the large writer scored 95-100% on short-answer items and a smaller fine-tuned writer scored 0/6, with every failure in its marking guide. A fact-hint setup that was good enough for the large writer at 97% was not good enough for the smaller one.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
     "lines": "130",
     "quote": "1. **The anchor-fact pattern was invented for stimuli, not rubrics.** When MCQ_SET was broken at 0%, we fixed the stimulus with anchor-facts. SAQ was already at 95-100% on Gemini, so its scoring notes weren't a problem. Nobody connected the dots to apply it to rubrics."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
     "lines": "132",
     "quote": "2. **The current approach (negative prompting) seemed to work on Gemini.** Because Gemini is large enough to mostly respect the \"no specific evidence\" instruction and has accurate enough parametric memory that when it does include evidence, it's usually right. The instruction that's good enough for a large model is insufficient for a 14B model."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/knowledge_and_rag_pipeline.md",
     "lines": "234",
     "quote": "None of these are implemented yet. The current system (4,177 facts, cluster matching, \"facts as hints\") is good enough for Gemini at 97%. It's not good enough for sft-v4/sft-v7 at the target rates."
    }
   ],
   "against": "The step structure did carry over to the new writer: ML learnings/week_of_apr_21.md line 17: \"The same scaffolding transfers to Fireworks with only token limit adjustments.\"",
   "adds_to_existing": [
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before reading a result, confirm that every measured item came from the system under test, with the change switched on and by the path it will run in.",
   "kind": "measured",
   "found_by": "Four silent failures: (1) A hard-coded import sent one item type to a different generator, so that type's earlier results were 'meaningless'. (2) A research step silently fell back to an older one-shot path and never ran. (3) A sampling feature was 'deployed' but not active, so results did not change. (4) A format test went through a pipeline that cleaned output the raw path did not clean: 4/5 valid there, then 1416/1416 parse failures on the raw path (grpo_failures_deep_dive.md lines 33, 37).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
     "lines": "39",
     "quote": "**Why this wasn't caught earlier:** The bug only manifests with `LLM_BACKEND=fireworks`. Every previous sft-v4/sft-v5/sft-v6 benchmark was probably silently skipping all MCQs. The MCQ numbers from those runs are meaningless."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
     "lines": "31",
     "quote": "**Result:** The MCQ Research step NEVER WORKED. Every MCQ and MCQ_SET generation silently fell back to a legacy one-shot path. The research was supposed to gather verified primary sources — it never ran."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/failures_and_false_starts.md",
     "lines": "163",
     "quote": "**Result:** Best-of-N was \"deployed\" but not activated. The benchmark showed the same results as before because the feature wasn't actually running."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24,
    36,
    38,
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Record every pass rate with its sample size, scope and setup; without them, results for the same writer can't be compared.",
   "kind": "measured",
   "found_by": "Different documents record the same writer at 6.5%, ~27% and ~60% overall. Two runs both labelled N=100 give different per-type rates: 67% vs 90% on single questions and 0% vs 18% on question sets. One gap was traced to 'clean units only' versus 'all units'.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_version_history.md",
     "lines": "40",
     "quote": "- The 27% vs 36% discrepancy from earlier session: the 36% was clean units only; 27% is all units"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_version_history.md",
     "lines": "22",
     "quote": "- Pass rates (N=100, April 21): MCQ 67%, SAQ 67%, LEQ ~98%, MCQ_SET 0%, DBQ 0%, Overall ~6.5%"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/fireworks_training_reference.md",
     "lines": "27",
     "quote": "- **Pass rates (teacher's N=100):** MCQ 90%, LEQ 71%, SAQ 67%, MCQ_SET 18%, DBQ 10%"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Score every run you compare with the same judge; two judges gave different verdicts on identical items.",
   "kind": "adopted rule",
   "found_by": "Two evaluators with different semantics gave different pass/fail decisions on identical content. After repeated confusion, one was barred from benchmarking and the tools were declared not interchangeable.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "20",
     "quote": "**Hard rule:** Never use localhost:8080 for official benchmarking. The `/get_standard` API has different semantics that can produce different pass/fail decisions on identical content."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/failures_and_false_starts.md",
     "lines": "155",
     "quote": "**This caused confusion multiple times.** The tools are not interchangeable. Rule: for Fireworks backend testing, always use `benchmark/runner.py`."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Measure how often the judge changes its verdict on identical items, per item type, and set the number of runs and items from that; for noisy types one run decides nothing.",
   "kind": "measured",
   "found_by": "Scoring identical items four times flipped verdicts at rates from 0% to 50%, depending on type. At a 50% flip rate, N=20 carries about ±10% uncertainty, and the noise caps a single run near 90% even for a perfect writer. The record's rule for the noisiest type: 3 runs give direction, 5+ runs give a reliable signal.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "123-128",
     "quote": "**Flip rates by type (discovered April, N=4 repeated trials):**\n- DBQ: 30% flip rate\n- MCQ_SET: 50% flip rate (!)\n- SAQ: 10% flip rate\n- LEQ: 0% flip rate\n- MCQ: 0% flip rate"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "139",
     "quote": "4. **Benchmark pass rates have error bars.** N=20 at 50% flip rate for MCQ_SET means our pass rate estimate has ±10% uncertainty. Always run N≥20 for MCQ_SET benchmarks."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "168-173",
     "quote": "Never make decisions on a single run. For MCQ_SET with 50% flip rate:\n- Single run pass rate = noise\n- 3 runs, average = directional signal\n- 5+ runs, average = reliable signal\n\nFor MCQ/LEQ with 0% flip rate, single run N≥20 is reliable."
    }
   ],
   "against": "Clear passes are stable and the noise sits in borderline items: ML learnings/evaluation_methodology.md line 135: \"The noise doesn't affect items that score 0.95+ consistently.\"",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check every fact in the examples a writer learns from or imitates; invented details in them get copied into new items.",
   "kind": "measured",
   "found_by": "The writer was built from examples that carried invented attributions, and it reproduced the pattern. Some of the 18,768 example sets still held wrong dates or sources even though they had passed a judge that flips 50% of the time on that type. The research summary notes that learning from another writer's output inherits that writer's inventions.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
     "lines": "15",
     "quote": "This is *not* a model size problem. A 14B model has ~28B bits of theoretical capacity — more than all of English Wikipedia. The gap to 70B is 6-8 MMLU points, not an order of magnitude. **The problem is that our training data contained fabricated attributions, and we taught the model exactly the wrong pattern.**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
     "lines": "112",
     "quote": "**Why 40% might be the new ceiling:** The training data (raft_combined) itself has fabricated attributions. Some of the 18,768 MCQ_SET records have slightly wrong dates or sources — they just passed InceptBench at the time, which has a 50% flip rate. Training on data that sometimes has wrong attributions = training on signal + noise."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_model_size_vs_data_quality.md",
     "lines": "108",
     "quote": "| Knowledge distillation (from Gemini) | Teaches format/style | Inherits hallucinations from teacher | Medium — we're already doing this and it's the source of the problem |"
    }
   ],
   "against": "Another note assumed the selected examples were already verified: ML learnings/week_of_apr_21.md line 117: \"generation adds new hallucination risk; selection only passes through verified Gemini-quality outputs.\" The cross-team summary ranks volume first: ML learnings/cross_team_learnings_full.md line 162: \"1. **More data > better data > architecture tricks.** Get the training data right before doing DPO, GRPO, or scaling.\"",
   "adds_to_existing": [
    61,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before producing more material, audit what already exists and ask whether the failure is an absence, which more material fixes, or a fault in what exists, which more of the same doesn't.",
   "kind": "measured",
   "found_by": "A plan to generate 500 new example sets was dropped when an audit found 18,768 already on hand. Adding examples of a missing item type lifted it from 0% to 12%; that fixed the format, but content still failed, and the hoped-for 80%+ stalled at ~12%. A 70k-record plan was cancelled once analysis showed that more data in the same format wouldn't fix the factual failures.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/decisions_and_pivots_timeline.md",
     "lines": "107",
     "quote": "**The audit finding:** We had been planning to generate 500 new MCQ_SET examples when we already had 18,768+ after combining raft_combined and sft_v6_combined."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/training_data_journey.md",
     "lines": "111",
     "quote": "**Lesson:** Before building a bigger dataset, ask: does the failure mode respond to more data? MCQ_SET at 0% responded to adding examples (0%→12%). MCQ at 60% ceiling did NOT respond to more prompt engineering. Different failures need different fixes."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/decisions_and_pivots_timeline.md",
     "lines": "98",
     "quote": "**What we got wrong:** Thought 504 examples would get MCQ_SET to 80%+. Actual ceiling was ~12%. The format problem was solved; the content quality problem wasn't."
    }
   ],
   "against": "The audit's premise that existing material is better was itself wrong here. ML learnings/decisions_and_pivots_timeline.md line 111: \"The existing data is usually better quality (Gemini-generated, verified) than what you'd generate quickly under time pressure.\" But ML learnings/mcq_set_journey.md line 112 reports existing records where \"Some of the 18,768 MCQ_SET records have slightly wrong dates or sources\". The cross-team view: ML learnings/cross_team_learnings_full.md line 73: \"**The pattern:** More representative examples of the hardest cases = better coverage of the output space.\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Find duplicate items by comparing whole items, not their openings; items that share a stock opening are not duplicates.",
   "kind": "measured",
   "found_by": "Hashing only the first 200 characters flagged 34% of distinct records as duplicates, because item types share stock openings. About 59k records looked like 37k, which prompted plans to generate more. Hashing the whole response restored 56,554 unique records from one source alone.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/training_data_journey.md",
     "lines": "7",
     "quote": "**Bug:** Used MD5 hash of first 200 chars of assistant content for deduplication."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/training_data_journey.md",
     "lines": "9-12",
     "quote": "This caused massive FALSE POSITIVES. Many different records share the same opening 200 characters:\n- MCQs starting with \"Which of the following best describes...\"\n- LEQs starting with \"Evaluate the extent to which...\"\n- DBQs starting with \"Using the documents...\""
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/training_data_journey.md",
     "lines": "14",
     "quote": "Result: Appeared to have only 37k unique records from what should have been 59k+. A 34% false dedup rate made the dataset look much smaller than it was, and caused us to think we needed to generate more data."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Sample items shown to a writer leak their own facts, sources and period into what it writes, so show the required structure rather than sample content.",
   "kind": "measured",
   "found_by": "Adding two or three example items to the prompt lowered the pass rate to 40% (baseline 45%) and factual accuracy to 55% (baseline 60%), at N=20. The writer reused elements of the examples and drifted toward their periods.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/failures_and_false_starts.md",
     "lines": "120",
     "quote": "**Result:** 40% pass rate — worse than the 45% baseline."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/failures_and_false_starts.md",
     "lines": "122",
     "quote": "**Why:** The few-shot examples gave the model specific historical content (dates, sources, attributions from the examples) that contaminated its generation. The model sometimes referenced elements from the example questions in its generated questions, or the examples biased its style toward those specific historical periods."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
     "lines": "58",
     "quote": "| fewshot | 40% | 55% | Few-shot examples added |"
    }
   ],
   "against": "The gap is one item in twenty: ML learnings/prompt_engineering_deep_dive.md line 50: \"**Method:** test_variants.py — 9 variants, N=20 each, APUSH Unit 7\". A cited grounding method depends on examples of a format: ML learnings/research_rag_factual_grounding.md line 202: \"Implementation via ICL with few-shot examples: provide 3-5 examples of the desired citation format, then instruct the model to follow the pattern.\"",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give the writer the item's exact structure and make every field that matters required; left to free form or to optional fields, it drops parts.",
   "kind": "measured",
   "found_by": "Generating with no schema fell to a 5% pass rate against a 45% baseline (N=20). A smaller writer often left out optional fields such as the source attribution, so the key field was made required. Any structural deviation fails the item.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
     "lines": "62",
     "quote": "| bare | 5% | 50% | No schema, raw generation |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/week_of_apr_21.md",
     "lines": "135",
     "quote": "Gemini reliably fills all JSON schema fields including optional ones. Fireworks model frequently omits optional fields (e.g., `source_attribution`). Keep required fields minimal; never rely on optional field presence for correctness. The `anchor_fact` field is required in the schema specifically because of this."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
     "lines": "45",
     "quote": "Any structural deviation = automatic fail on `specification_compliance`."
    }
   ],
   "against": "Structure doesn't carry correctness: ML learnings/research_model_size_vs_data_quality.md line 150: \"- The knowledge and content quality within the structure is what differentiates model sizes — not the structural compliance itself\". In the same sweep, factual accuracy moved much less than the pass rate (50% with no schema vs 60% baseline).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A well-formed item is not a correct one; check structure and content separately, because fixing one leaves the other as it was.",
   "kind": "measured",
   "found_by": "Once examples taught the question-set format (0% to 12%), items still failed the content gates 88% of the time. A grammar can force a well-formed date field but not the right date.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
     "lines": "92",
     "quote": "**What 12% means:** The model now generates MCQ_SET format (3 questions, stimulus, all required fields). But the quality threshold (factual_accuracy, stimulus_quality) was still failing 88% of the time."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
     "lines": "94",
     "quote": "**What 12% doesn't mean:** We solved MCQ_SET quality. We solved MCQ_SET FORMAT. These are different problems."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
     "lines": "251",
     "quote": "The limitation is critical: you can force the model to emit a syntactically valid JSON field for `\"year\": <int>`, but you cannot force the value to be `1919` rather than `1914` via grammar constraints alone. Semantic fact-checking requires a different mechanism."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A graded quality score can be won by length, fluency and confidence even when facts are wrong, so factual correctness needs its own pass/fail gate.",
   "kind": "external research",
   "found_by": "Two cited studies. Binary RAR (arXiv:2510.17733, https://arxiv.org/html/2510.17733v1) found that continuous rewards 'get gamed by output style (longer, more confident responses get higher scores even with wrong facts)'. FLAME (arXiv:2405.01525) found that reward signals 'prioritize helpfulness, verbosity, and fluency over correctness'. In the project, an item scoring 0.92 overall still fails if any one hard dimension misses.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_dpo_grpo_factual.md",
     "lines": "146",
     "quote": "The binary reward is specifically better than continuous scores in this paper because continuous rewards get gamed by output style (longer, more confident responses get higher scores even with wrong facts). Binary RAR forces the model to be either fully correct or abstain."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_dpo_grpo_factual.md",
     "lines": "85",
     "quote": "FLAME diagnoses a specific problem: conventional SFT+DPO alignment pipelines inadvertently *increase* hallucination because reward signals prioritize helpfulness, verbosity, and fluency over correctness."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
     "lines": "40",
     "quote": "This is NOT just overall_score ≥ 0.85. An item can score 0.92 overall and still hard-fail if a single hard-fail dimension drops below 1.0. The hard-fail dimensions are binary gates — they must all be perfect."
    }
   ],
   "against": "A pass/fail gate on its own gives no signal for improving weak output: ML learnings/grpo_failures_deep_dive.md line 19: \"**The key insight:** GRPO needs a GRADED reward signal (0.0 to 1.0) with variance between candidates. Binary 0/1 from hard-fails gives you nothing to compare. The evaluator was designed as a quality gate, not a reward shaper.\"",
   "adds_to_existing": [
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When no verified fact supports a specific claim, give the writer an explicit way out (describe the kind of evidence instead of naming one) rather than a bare prohibition.",
   "kind": "adopted rule",
   "found_by": "A bare ban on dates left the short-answer type at 0%. The next prompt plan replaced it with 'If no verified fact supports the claim, describe the analytical CATEGORY only'. Cited work warns that rewarding only correctness encourages confident guessing, and recommends rewarding abstention under uncertainty (arXiv:2505.24630; arXiv:2512.19920). A cited self-critique principle says to omit an uncertain year rather than guess (Constitutional AI, arXiv:2212.08073).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
     "lines": "36",
     "quote": "If no verified fact supports the claim, describe the analytical CATEGORY only."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_dpo_grpo_factual.md",
     "lines": "187",
     "quote": "**Key caution:** \"Reasoning Models Hallucinate More\" (arXiv:2505.24630) shows that standard RL fine-tuning with binary correctness rewards can *increase* hallucination by incentivizing confident guessing. The fix is to incorporate factuality verification at each step (FSPO, their method) or use calibration rewards that reward abstention under uncertainty (Behavioral Calibration RL, arXiv:2512.19920)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_dpo_grpo_factual.md",
     "lines": "323",
     "quote": "Applied to factual accuracy: write a constitution with factual principles like \"All historical dates must be accurate\", \"Never attribute a quote to a person without certainty\", \"When in doubt about a specific year, omit the year rather than guess.\""
    }
   ],
   "against": "Not tested in this folder; only an expected gain is recorded: ML learnings/master_strategy_apr24.md line 45: \"**Expected T1 impact:** SAQ 0% → ~40-50%, MCQ_SET 20% → ~35-40%, overall ~33% → ~45-55%.\"",
   "adds_to_existing": [
    62,
    56
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give a writer only the few verified facts that match the item's exact topic, not everything for its unit; neighbouring-topic facts get blended in and long lists get used less.",
   "kind": "adopted rule",
   "found_by": "With facts drawn for the whole unit, an item on one topic mixed in another topic's facts. Facts were then matched to the item's topic cluster first; this was reported as improving relevance, with no pass-rate figure. The research summary advises giving the 10-15 most relevant facts rather than all 3,347, because facts in the middle of a long block are ignored most.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/knowledge_and_rag_pipeline.md",
     "lines": "171",
     "quote": "If the question topic was about Progressivism but the injected facts were about immigration, the model might generate a question that mixed both — or the curriculum facts wouldn't help at all."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
     "lines": "404",
     "quote": "**More context injection / longer fact lists:** The Lost-in-the-Middle problem means that making the fact list longer reduces the model's ability to use it. Better to use a retriever (Technique 7) to inject only the 10-15 most relevant facts rather than all 3,347."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
     "lines": "34",
     "quote": "- **Context position**: Facts buried in the middle of a long context block are more likely to be ignored than facts at the very beginning or end (Lost-in-the-Middle problem)."
    }
   ],
   "against": "Another note favours more facts, though it refers to the store, not the prompt: ML learnings/knowledge_and_rag_pipeline.md line 228: \"2. **Fact expansion:** Grow the corpus from 4,177 to 20,000+ facts. More facts = better coverage = fewer hallucination opportunities.\" The cluster change has no measured effect: ML learnings/infrastructure_and_tooling.md line 158: \"Cluster-matched facts > unit-level-only improved relevance.\"",
   "adds_to_existing": [
    57,
    58
   ],
   "name_bearing_source": false
  },
  {
   "statement": "After an item is written, pull out each specific claim and check it on its own against the source, replacing or dropping any that fails.",
   "kind": "external research",
   "found_by": "A cited four-stage method (generate, extract claims, verify each claim, refine) reported 83% factual accuracy vs 72%, and a 12% hallucination rate vs 25%, without retraining (VeriFact-CoT, arXiv 2509.05741, https://arxiv.org/html/2509.05741v1). A cited fact-checker scores responses claim by claim (LEAF, arXiv:2410.23526). The project planned claim extraction and substitution against its fact store as its top fix without retraining; it was not yet measured.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "141-142",
     "quote": "- Factual Accuracy: **83%** (vs 72% standard CoT, 78% CoT+RAG)\n- Hallucination Rate: **12%** (vs 25% standard CoT, 18% CoT+RAG)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
     "lines": "52-55",
     "quote": "Add a verification step after SAQ/LEQ/DBQ generation that:\n1. Extracts all specific historical claims from rubric fields (dates, names, events)\n2. Checks each against `curriculum_facts.json`\n3. Substitutes unverified claims with category descriptions or verified alternatives"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_dpo_grpo_factual.md",
     "lines": "301",
     "quote": "LEAF is a three-component framework: (1) **RAFE** — a fact-checking module using retrieval to evaluate response accuracy claim-by-claim; (2) **Fact-Check-then-RAG** — inference-time correction without parameter updates; (3) **Learning from Fact Check** — either SFT on fact-checked responses or SimPO/DPO using fact-check scores to rank chosen vs. rejected. The training approach uses fact-checking scores as pseudo-labels to construct preference pairs, requiring no human annotation."
    }
   ],
   "against": "The cited check verified claims against the writer's own knowledge, not an independent source: ML learnings/research_educational_content_generation.md line 137: \"3. Verify each claim against internal knowledge\". An earlier project rule bars verification steps: ML learnings/research_rag_factual_grounding.md line 406: \"**Inference-time verification / regeneration:** Per project principles, \"verification and regeneration are not valid approaches.\"\"",
   "adds_to_existing": [
    31,
    59,
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count an item as grounded only when every judge finds no unsupported claim; a single objection fails it.",
   "kind": "external research",
   "found_by": "The FACTS grounding benchmark counts a response as grounded only when all judge models agree it contains no unsupported claims (arXiv 2501.03200, https://arxiv.org/pdf/2501.03200). The project's per-item hard gate is described as mirroring this and as stricter than anything published.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "184",
     "quote": "The closest published threshold is from the FACTS Benchmark Suite, which deems a response as \"successfully grounded\" only when all judge models agree it contains no unsupported claims. This binary per-item pass/fail mirrors our InceptBench approach."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "182",
     "quote": "- **Our InceptBench setup** (hard-fail at 1.0): Stricter than anything published. We require perfect factual accuracy per item, not an aggregate pass rate."
    }
   ],
   "against": "With noisy judges, requiring unanimity will also fail sound items: ML learnings/evaluation_methodology.md line 125: \"- MCQ_SET: 50% flip rate (!)\".",
   "adds_to_existing": [
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Refine a marking guide against real student answers before relying on it, rather than writing it in one pass.",
   "kind": "external research",
   "found_by": "A cited grading pipeline (marking-guide generation, grading, post-grading review) treats writing the guide as iterative optimisation. It found guides tuned on actual student answers more accurate and reliable (Grade Like a Human, arXiv 2405.19694, https://arxiv.org/pdf/2405.19694). The project never tried this.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "55",
     "quote": "- Relevant insight: rubrics optimized against actual student answers are more accurate and reliable"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "56",
     "quote": "- **The key technique:** rubric generation as an optimization problem, not a single-shot generation"
    }
   ],
   "against": "The cited work doesn't address factual content inside a guide: ML learnings/research_educational_content_generation.md line 75: \"Most work treats rubrics as frozen artifacts used for scoring, not as generated content that must be historically accurate.\"",
   "adds_to_existing": [
    69,
    37
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write each marking criterion as a specific, observable definition, and have a person approve any generated marking guide before it is used.",
   "kind": "external research",
   "found_by": "A cited assessment framework builds marking guides from course materials, syllabus and assignment. Its criteria are operational definitions that are 'specific and observable', and the guides are approved before deployment (RubiSCoT, arXiv 2510.17309, https://arxiv.org/html/2510.17309).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "65",
     "quote": "- Rubric criteria have \"operational definitions\" that are \"specific and observable\""
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "66",
     "quote": "- Instructors review and approve AI-generated rubrics before deployment"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    69,
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Mark in two steps: first find the parts of the answer that each criterion refers to, then score each part against its criterion.",
   "kind": "external research",
   "found_by": "A cited multi-agent marking framework has one agent identify the components relevant to the marking guide and another score them. It reports that the explicit checkpoints improve accuracy and make marks easier to interpret (AutoSCORE, arXiv 2509.21910, https://arxiv.org/html/2509.21910v1).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "69",
     "quote": "- Multi-agent framework: one agent identifies rubric-relevant components, another scores"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "70",
     "quote": "- Explicit checkpoints constrain reasoning path — improves accuracy and interpretability"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    31,
    33
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check a question's fit to the curriculum by asking whether it can be answered from the official curriculum's own scope for that unit.",
   "kind": "external research",
   "found_by": "A cited study judged validity partly by whether a question 'should be answerable using the curriculum's own scope definition'. Grounding generation in official curriculum documents took validity from 12-15% to 92-96% with the same generator (arXiv 2508.04442, https://arxiv.org/html/2508.04442).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "94",
     "quote": "**How validity is measured:** Semantic Textual Similarity against official curriculum + RAG-QA test (a curriculum-aligned question should be answerable using the curriculum's own scope definition). This is analogous to our curriculum_alignment dimension."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "92",
     "quote": "RAG methods go from 12-15% validity to 92-96% validity by grounding generation in official curriculum documents. The study uses GPT-4o as the generator for all conditions — the variable is retrieval, not the model."
    }
   ],
   "against": "The study covers one other subject: ML learnings/research_educational_content_generation.md line 276: \"- [Automated Generation of Curriculum-Aligned MCQs for Malaysian Secondary Mathematics](https://arxiv.org/html/2508.04442)\".",
   "adds_to_existing": [
    58,
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Build and check generated items and marking guides against the official released exams, their marking guidelines and sample answers.",
   "kind": "external research",
   "found_by": "The research survey found no academic benchmark for this kind of question generation. It named the exam body's released past exams, scoring guidelines and sample responses as the only verified items and guides (https://apcentral.collegeboard.org/courses/ap-united-states-history/exam/past-exam-questions; https://apcentral.collegeboard.org/courses/ap-world-history/exam/past-exam-questions). The project's checks did not yet use them.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "164",
     "quote": "**These are the highest-quality labeled AP rubric examples available.** The College Board releases approximately 3 years of past exams publicly. These are the ground-truth rubrics that a fine-tuning dataset should be derived from or validated against."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "168",
     "quote": "No academic dataset or benchmark for AP history question generation appears in the literature. The College Board materials are the only source of verified AP-style questions and rubrics. Any training dataset must be built from these or synthetically generated and verified against InceptBench."
    }
   ],
   "against": "The released set is small: ML learnings/research_educational_content_generation.md line 164: \"The College Board releases approximately 3 years of past exams publicly.\"",
   "adds_to_existing": [
    37,
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Verify the reference facts themselves against the official curriculum, and version them, before using them to write or check items.",
   "kind": "open question",
   "found_by": "The fact store served as the writer's only source and as a check, but it was never verified against the official curriculum ('Some facts may be outdated or approximate'). Its size appears as both 3,347 and 4,177 in different documents.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/knowledge_and_rag_pipeline.md",
     "lines": "230",
     "quote": "3. **Fact verification:** Each fact in curriculum_facts.json should be verified against AP curriculum documents. Some facts may be outdated or approximate."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/knowledge_and_rag_pipeline.md",
     "lines": "14",
     "quote": "**Size:** 4,177 facts (as of April 2026; earlier sessions showed 3,347 facts)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "108",
     "quote": "Our existing `curriculum_facts.json` (3,347+ facts) is a form of RAG grounding. The literature suggests more structured retrieval (graph-based or with explicit entity matching) would improve factual accuracy beyond what flat keyword retrieval achieves."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    57,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Measure on every unit and course the materials must serve, and check hardest where the subject is least documented and verified facts are thinnest.",
   "kind": "adopted rule",
   "found_by": "The target was set across all 28 units, because strength on the best-covered course hides weakness elsewhere. The less-documented courses had weaker writer memory, fewer verified facts per unit (100-200 vs 150-300) and more factual failures. Cited work finds that supplied sources beat training by the widest margin for rare facts (SIGIR-AP 2024, https://arxiv.org/html/2403.01432v3).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
     "lines": "97",
     "quote": "Why 28 units matters: a system that performs well on APUSH but poorly on APWH/APEURO is not production-ready. The 97% target is across ALL 28 units, not just the most-trained ones."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/knowledge_and_rag_pipeline.md",
     "lines": "217",
     "quote": "**Coverage gaps:** Some units have more facts than others. APUSH tends to have 150-300 facts per unit; APWH and APEURO units may have 100-200. This means APWH/APEURO questions have slightly less curriculum grounding. This partially explains why APWH factual_accuracy failures are more common than APUSH failures."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_model_size_vs_data_quality.md",
     "lines": "113",
     "quote": "The most relevant finding: **\"Fine Tuning vs. RAG for Less Popular Knowledge\"** (SIGIR-AP 2024) showed that RAG surpasses fine-tuning by a large margin specifically for rare or less popular factual knowledge. AP history content includes many obscure primary source documents, minor historical figures, and precise dates — exactly the type of content where parametric knowledge is unreliable in any model under 100B+ parameters."
    }
   ],
   "against": "No per-course failure rates are given; the record claims only partial cause: ML learnings/knowledge_and_rag_pipeline.md line 217: \"This partially explains why APWH factual_accuracy failures are more common than APUSH failures.\"",
   "adds_to_existing": [
    49,
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Where two units overlap in time or theme, give the writer the rule that tells them apart; otherwise it drifts into the neighbouring unit.",
   "kind": "measured",
   "found_by": "The writer conflated two units that share one date range. An explicit rule separating them cut alignment failures for the pair (about a 1% overall gain). A cited survey lists adjacent-topic drift as a common failure of generated questions.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "110",
     "quote": "**Why this works:** The model already knows the content of both units. The disambiguation doesn't teach new facts — it removes ambiguity about which unit to draw from given a shared time period."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "112",
     "quote": "**Impact:** Reduced curriculum_alignment failures on APWH Unit 3/4 overlap. ~1% improvement."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "25",
     "quote": "2. **Adjacent-topic drift**: Content from a nearby era/domain bleeds in despite topic constraints"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    58,
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat a failure that repeats across items as a specific bug to find (wrong labels, a missing item type, an instruction that invites invention) and keep sampling for the last scattered slips.",
   "kind": "measured",
   "found_by": "At 81.9% the remaining failures were systematic, not random. Nine targeted fixes added 15.1 points in about 48 hours, while most of the ~40-50 automated iterations changed nothing. The record's bands: 60-80% means systematic bugs, 80-95% prompt design, 95-99% random slips, 99%+ judge noise.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "13",
     "quote": "At 81.9%, the system was generating correct AP questions most of the time. The remaining ~18% failures were not random — they were systematic, patterned failures. The key insight that drove the relentless push: every failure is evidence of a specific, fixable bug."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "184",
     "quote": "**Total:** 15.1 percentage point improvement from 9 targeted fixes over ~48 hours."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
     "lines": "225",
     "quote": "**60-80%:** Usually systematic bugs (wrong metadata, wrong course, missing training examples for a type)"
    }
   ],
   "against": "A repeating failure is not always fixable in the instructions: ML learnings/prompt_engineering_deep_dive.md line 73: \"The failure is at the weight level, not the prompt level.\"",
   "adds_to_existing": [
    65,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Read the shape of the failures before fixing: a whole unit failing while others pass points to wrong scope labels, a whole item type failing to missing examples, right content on the wrong topic to an ignored constraint, and right content with wrong specifics to invented details.",
   "kind": "adopted rule",
   "found_by": "The project's diagnostic framework runs: aggregate, dimension, item, two or three hypotheses, a test that tells them apart, then a targeted fix. It comes with a catalogue of failure signatures. Each time the team skipped from an aggregate straight to a fix, it 'wasted a training run'.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/debugging_methodology.md",
     "lines": "128-129",
     "quote": "**Signature:** Entire unit/course at 0% despite other units passing\n**Cause:** Wrong metadata (time period, course, unit) being passed to model"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/debugging_methodology.md",
     "lines": "137-138",
     "quote": "**Signature:** Model generates correct content for the WRONG thing it was told to do\n**Cause:** Training data lacked hard negatives for constraint adherence"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/debugging_methodology.md",
     "lines": "19",
     "quote": "Never skip to step 7. Every time we skipped steps (went from aggregate failure to guessing at a fix), we wasted a training run."
    }
   ],
   "against": "Even with the framework, the first hypotheses were wrong: ML learnings/stage2_postmortem_full.md line 180: \"5. **Three wrong turns is normal.** The first hypothesis is usually \"something broke.\" The second is \"maybe we can fix it at inference time.\" The third is \"maybe the conditions weren't right.\" Root cause often requires ruling all of these out.\"",
   "adds_to_existing": [
    60,
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Re-measure any gain an automated improver reports with a check it doesn't control; its self-reports ran high and some of its edits made things worse.",
   "kind": "measured",
   "found_by": "An unattended improvement agent claimed 90% on question sets where the real rate was 70-75%. The automated analyst sometimes proposed changes that made results worse (a 0.5% regression). It rarely caught code bugs; those needed a person's review.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/failures_and_false_starts.md",
     "lines": "103",
     "quote": "- Claimed 90% MCQ_SET pass rate (actual: 70-75%)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/overnight_automation.md",
     "lines": "225",
     "quote": "- Sometimes proposed a prompt change that made things slightly worse (0.5% regression)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/overnight_automation.md",
     "lines": "226",
     "quote": "- Rarely caught code bugs (like the f-string bug) — those needed human review"
    }
   ],
   "against": "The automated loop did produce real gains when the next run measured every change: ML learnings/gemini_benchmark_relentless.md line 197: \"The system applied ~40-50 iterations over 48 hours. Most iterations were 0.0% improvement. 9 were significant.\"",
   "adds_to_existing": [
    43,
    66,
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Whether output length caps silently cut the ends off items (such as missing answer options) is unsettled; size any cap from the longest real outputs plus headroom and check that delivered items are complete.",
   "kind": "open question",
   "found_by": "The synthesis blamed missing answer choices and incomplete output on a borderline output cap. It cited vendor guidance that a cap below worst-case length truncates output silently (https://www.alibabacloud.com/help/en/model-studio/qwen-structured-output). Another record reports no quality loss after cutting the caps, and gives a rule to set caps at 50% of where timeouts begin.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
     "lines": "18",
     "quote": "Missing answer choices, incomplete JSON. Root cause: **token limit truncation** — Alibaba Cloud docs explicitly warn that capping `max_tokens` below worst-case output causes silently truncated JSON. Our `mcq_set_questions` limit of 8192 is borderline. Secondary cause: SFT loss doesn't shape partial schema correctness."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_qwen3_structured_multistage.md",
     "lines": "54",
     "quote": "- **Never set `max_tokens` below the worst-case full output length.** For complex AP exam questions with 5+ nested fields, estimate the maximum possible output and add a 20-30% buffer."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/pipeline_architecture_insight.md",
     "lines": "73",
     "quote": "Rule: For any new model, find the token ceiling empirically. Run 5 DBQ requests, find where timeouts start, set limit at 50% of that."
    }
   ],
   "against": "ML learnings/pipeline_architecture_insight.md line 70: \"- No quality regression observed after the reduction\"",
   "adds_to_existing": [
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check every cited result against its source before acting on it; summaries merged, moved and relabelled numbers.",
   "kind": "measured",
   "found_by": "Found by comparing the summaries with the source sections. A 13.83% grounding gain and a ~50% coverage ceiling became '13-50% grounding improvement'. A 96% validity result belongs to custom-chunked retrieval in one study (research_educational_content_generation.md line 90), but the index and the synthesis credit it to graph retrieval. An internal team result was called 'Published results' (research_educational_content_generation.md line 231). A verification method was credited with the effect of a pre-writing step it never tested (master_strategy_apr24.md line 60).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
     "lines": "204",
     "quote": "Results: Citation grounding improved by **13.83%** on production benchmarks versus standard RAG prompting. However, only ~50% of sentences achieved perfect citation coverage without fine-tuning, suggesting a ceiling that requires SFT to overcome fully."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
     "lines": "30",
     "quote": "Force the model to emit `[FACT: <exact quote from curriculum_facts>]` before each specific historical claim in scoring notes. Zero cost to try. Published results: 13-50% grounding improvement. Ceiling ~50% without training, but combined with the existing anchor-fact constraint this should push SAQ above 0%."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/INDEX.md",
     "lines": "85",
     "quote": "| [research_educational_content_generation.md](research_educational_content_generation.md) | GraphRAG (96% curriculum validity), VeriFact-CoT (83% vs 72%), frontier baseline 69% |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Whether generated items below roughly a 60% pass rate save any review time is unmeasured; the record asserts that reviewing them costs more than it saves.",
   "kind": "open question",
   "found_by": "A quality-level framing in the project's context document, with no time measurement behind it.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
     "lines": "114-115",
     "quote": "### Below 60%\nUnreliable. Some questions are excellent, many have significant errors. Teacher would spend more time reviewing than they'd save from automation."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Store a course's facts as linked entities with verified attributes and relations, so items can follow the course's own facts even where a writer's general knowledge disagrees.",
   "kind": "external research",
   "found_by": "A cited comparison tested deliberately altered textbook facts and found that graph-structured retrieval kept to the curriculum even where it contradicted the writer's own knowledge (arXiv 2509.07846, https://arxiv.org/html/2509.07846; KnowShiftQA, https://arxiv.org/html/2412.08985v1). The synthesis planned an entity-relationship fact store; it was not built or measured here.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
     "lines": "101",
     "quote": "- When tested on altered textbook facts (KnowShiftQA dataset), GraphRAG Local maintained adherence to curriculum content even when it contradicted the LLM's internal knowledge"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
     "lines": "64",
     "quote": "Better: entity-relationship graph — events and people as nodes, verified dates as attributes, causal relationships as edges. Force rubric evidence to come from retrieved *graph nodes* not flat strings."
    }
   ],
   "against": "The synthesis credits graph retrieval with another method's result. ML learnings/master_strategy_apr24.md line 65: \"Published result: 96% curriculum validity vs 12% ungrounded using the same model.\" But the source table gives that 96% to custom chunking: ML learnings/research_educational_content_generation.md line 90: \"| Manual RAG with custom chunking | 0.89 | 96% |\".",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Have the writer copy the exact supporting fact before each specific claim, so every claim is tied to a source that code can check.",
   "kind": "external research",
   "found_by": "A cited prompting method makes the writer locate evidence before committing to a claim. It improved citation grounding by 13.83%, with only ~50% of sentences fully covered without further training (Cite Before You Speak, arXiv:2503.04830, https://arxiv.org/abs/2503.04830). The project's next prompt plan required a '[FACT: <exact phrase>]' marker before each specific claim in marking guides; it was not tested here.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
     "lines": "200",
     "quote": "Rather than generating claims freely and optionally citing afterward, the \"cite first\" constraint forces the model to locate supporting evidence before committing to a claim. This exploits the autoregressive structure: once the model has emitted a citation token pointing to a specific fact, the conditional probability of hallucinating a different fact drops sharply."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/master_strategy_apr24.md",
     "lines": "34-35",
     "quote": "Before writing any specific date, name, treaty, or event in scoring notes, first write:\n[FACT: <copy the exact phrase from VERIFIED FACTS above that supports this claim>]"
    }
   ],
   "against": "ML learnings/research_rag_factual_grounding.md line 204: \"However, only ~50% of sentences achieved perfect citation coverage without fine-tuning, suggesting a ceiling that requires SFT to overcome fully.\"",
   "adds_to_existing": [
    17,
    57
   ],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
   "lines": "12",
   "quote": "2. All 3 questions must be independently answerable from the stimulus alone"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/cross_team_learnings_full.md",
   "lines": "147",
   "quote": "1. **Yes/No class balance** (one team): Model was biased toward one answer class because training data had 70/30 split. Balancing to 50/50 improved calibration."
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/dpo_and_fdpo_pipeline.md",
   "lines": "30-31",
   "quote": "- Higher bar preferred: score ≥ 0.90 (not just barely passing)\n- Rationale: the \"chosen\" side needs to be clearly good, not borderline"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
   "lines": "108",
   "quote": "2. The verbatim copy creates a ground truth to compare against"
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
   "lines": "86",
   "quote": "2. `specification_compliance`: InceptBench occasionally treats DBQ as if it should be a closed-ended MCQ question, not a document-based essay prompt. This may be an evaluator misconfiguration, not a real quality issue."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
   "lines": "121",
   "quote": "InceptBench has a stochastic evaluation component (likely using a language model as part of the rubric). Running the SAME generation through the evaluator 4 times produces different results."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/debugging_methodology.md",
   "lines": "148",
   "quote": "**Diagnostic:** Errors are in specific facts, not structural; model is consistent in its errors"
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
   "lines": "31",
   "quote": "**Result:** The MCQ Research step NEVER WORKED. Every MCQ and MCQ_SET generation silently fell back to a legacy one-shot path. The research was supposed to gather verified primary sources — it never ran."
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
   "lines": "179",
   "quote": "**Known:** InceptBench was calibrated against AP teacher review panels. It's not perfect, but it's the closest proxy available."
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
   "lines": "48-49",
   "quote": "- Multi-dimensional calibration via trained neural network; 2x improvement over uncalibrated baselines\n- Achieves RMS error < 0.5 on 1-4 scale predicting human judge satisfaction"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_dpo_grpo_factual.md",
   "lines": "442-444",
   "quote": "Take this AP history exam question and introduce one subtle factual error (wrong year,\nwrong person, wrong founding date). Keep everything else identical. The error should be\nplausible — not obviously wrong, but verifiably incorrect per standard AP curriculum."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_dpo_grpo_factual.md",
   "lines": "447",
   "quote": "Run the synthetic rejected responses through InceptBench to confirm they fail factual_accuracy before including them in training. Keep only (chosen=PASS, rejected=FAIL) pairs."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/dpo_and_fdpo_pipeline.md",
   "lines": "98",
   "quote": "**The `prompt_messages` fix:** `eval_finetuned.py` was modified to save `prompt_messages` (the system + user turns that preceded the generation) in each result when `SAVE_ALL_CONTENT=1`. Without this, `build_fdpo_dataset.py` only had the generated content, not the full conversation context needed for DPO pairs."
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
   "lines": "37",
   "quote": "**MCQ_SET:** One shared stimulus, THREE questions that all reference that same stimulus, each testing a different historical thinking skill."
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/debugging_methodology.md",
   "lines": "203",
   "quote": "The CC provides an independent diagnostic perspective. When you've been staring at a failure for 2 hours and have formed strong hypotheses, an external audit can quickly confirm or reject them without the same anchoring bias."
  },
  {
   "truth": 43,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
   "lines": "137-141",
   "quote": "3. Verify each claim against internal knowledge\n4. Refine and correct the output\n\n**Quantitative results:**\n- Factual Accuracy: **83%** (vs 72% standard CoT, 78% CoT+RAG)"
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
   "lines": "189",
   "quote": "**Practical implication:** InceptBench 97% pass rate does NOT mean 97% of questions are publishable. Some will require teacher review. But it's a reliable quality gate for training and benchmarking purposes."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
   "lines": "14",
   "quote": "The most cited statistic in recent literature (2024-2025) is that when AI-generated exam questions are reviewed by subject experts, approximately **69% are fit for inclusion with little or no modification**, while **31% are rejected for factual inaccuracies or misalignment with learning objectives**. This is the baseline for unconstrained frontier model generation (GPT-4 class)."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
   "lines": "18",
   "quote": "- \"Assessing the Quality of AI-Generated Exams: A Large-Scale Field Study\" (arXiv 2508.08314) — field study at scale; AI-authored questions that pass quality assurance \"do not perform differently from human-authored questions\""
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/overnight_automation.md",
   "lines": "226",
   "quote": "- Rarely caught code bugs (like the f-string bug) — those needed human review"
  },
  {
   "truth": 44,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
   "lines": "106",
   "quote": "Every question would be usable on an actual AP exam without teacher modification. Correct historical content, period-accurate, right cognitive level, right structural format. A teacher reviewing these questions would accept them for direct use."
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/stage2_postmortem_full.md",
   "lines": "62",
   "quote": "**CC's finding:** The training format was actually CLOSER to the evaluation format than the production generator format. Stage 2 learned to respond to simplified prompts correctly. Running it through the production generator (the MOST out-of-distribution option) would make things worse, not better."
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/grpo_failures_deep_dive.md",
   "lines": "39",
   "quote": "**The critical lesson:** ALWAYS test the raw rollout format, not the production pipeline format. They are NOT the same. Production: `model → strip_thinking → json.loads`. GRPO rollout: `model → json.loads`. That stripping step is not there."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
   "lines": "187",
   "quote": "- It doesn't test \"student experience\" — a confusing but technically correct question can pass"
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
   "lines": "158",
   "quote": "**Look at which dimensions failed, not just whether it passed.**"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/fireworks_training_reference.md",
   "lines": "62",
   "quote": "- **Assessment:** Never benchmarked. Did this become sft-v6? Unknown. sft-v6 was deployed at some point with a pass rate of ~27%."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/failures_and_false_starts.md",
   "lines": "137",
   "quote": "**Pattern:** Metadata bugs are easy to overlook because they don't affect training quality directly. But they accumulate over time and make later analysis harder. Worth fixing before the next DPO dataset build."
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
   "lines": "47",
   "quote": "The failures are NOT in the question itself. They're in the **scoring notes the model generates**."
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
   "lines": "35",
   "quote": "- **Task format**: When the generation task involves producing many fields simultaneously (like a structured rubric with question stem, answer choices, scoring guide, and historical evidence), the model's attention dilutes across fields and it falls back on parametric defaults for lower-salience fields like rubric details."
  },
  {
   "truth": 56,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
   "lines": "132",
   "quote": "2. **The current approach (negative prompting) seemed to work on Gemini.** Because Gemini is large enough to mostly respect the \"no specific evidence\" instruction and has accurate enough parametric memory that when it does include evidence, it's usually right. The instruction that's good enough for a large model is insufficient for a 14B model."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
   "lines": "92",
   "quote": "RAG methods go from 12-15% validity to 92-96% validity by grounding generation in official curriculum documents. The study uses GPT-4o as the generator for all conditions — the variable is retrieval, not the model."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
   "lines": "229",
   "quote": "This is a \"closed-world\" approach: rather than asking the model to generate historical facts from open memory, you preemptively supply the plausible candidates and the model's job is selection rather than recall."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
   "lines": "33",
   "quote": "- **Fact dynamicity**: Models are least persuadable by retrieved context for *static* historical facts (dates, names, places) — exactly the kind of facts in our rubrics. Dynamic/recent facts are easier to override with context. (ECIR 2025 keynote, arXiv:2603.09654)"
  },
  {
   "truth": 57,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/knowledge_and_rag_pipeline.md",
   "lines": "230",
   "quote": "3. **Fact verification:** Each fact in curriculum_facts.json should be verified against AP curriculum documents. Some facts may be outdated or approximate."
  },
  {
   "truth": 57,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
   "lines": "113",
   "quote": "2. At inference time, the model will sometimes follow the constraint, sometimes not"
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
   "lines": "25",
   "quote": "2. **Adjacent-topic drift**: Content from a nearby era/domain bleeds in despite topic constraints"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/what_is_ap_and_why_it_matters.md",
   "lines": "125",
   "quote": "4. Wrong information in practice questions could hurt student performance on the actual exam"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
   "lines": "89",
   "quote": "- One wrong date in one document = hard fail for the whole DBQ"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_educational_content_generation.md",
   "lines": "180",
   "quote": "- **Medical domain** (strictest): 100% factual accuracy required for clinical exam questions; 69% pass rate reported for unconstrained GPT-4 generation"
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
   "lines": "70",
   "quote": "The curriculum facts help non-critical dimensions (educational_accuracy, etc.) enough to push borderline items above the 0.85 threshold, even though they don't help factual_accuracy specifically."
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
   "lines": "24",
   "quote": "- Research step chained stimulus to potentially bad sources (if the research hallucinated a source, the stimulus inherited the hallucination)"
  },
  {
   "truth": 61,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
   "lines": "36",
   "quote": "- MCQ: 96% → 100% (research step immediately improved factual accuracy)"
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/sft_v7_benchmark_postmortem.md",
   "lines": "62",
   "quote": "**Why it doesn't work:** The model ignores negative constraints. It has strong parametric associations (France → exploration → Protestant → Huguenots → plausible but wrong) that override the instruction. Telling the model \"don't use specific facts\" just means it uses wrong specific facts instead of right ones."
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/failures_and_false_starts.md",
   "lines": "124",
   "quote": "**The \"caution\" variant also failed:** Adding \"be careful\" warnings about factual accuracy produced 30% pass rate — worse than anything. Warnings that tell the model to be careful without giving it actual constraints just introduce hedging behavior. The model starts prefacing with qualifications instead of generating confident content."
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/stage2_postmortem_full.md",
   "lines": "82",
   "quote": "**Result:** Failures persisted. Stage 2 still generated about William Penn when asked for FDR."
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
   "lines": "81",
   "quote": "**Why this was missed:** The code was doing \"clever\" re-derivation of course/unit from substandard_id. The problem with re-derivation: KC-prefixed standards are APWH-specific notation that the parser didn't handle. Passing explicit values eliminates the re-derivation entirely."
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
   "lines": "29",
   "quote": "Every APEURO Unit 4 question automatically failed `curriculum_alignment` because the generated content referenced 1648-1815 material but the evaluator expected 1914-present content."
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/cross_team_learnings_full.md",
   "lines": "137",
   "quote": "**One team tried:** 0.01 weight on items where model references missing images. Helped eliminate that specific failure mode."
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_model_size_vs_data_quality.md",
   "lines": "140",
   "quote": "**Practical implication:** If the 14B model's failure rate is 67% (as currently), even N=100 won't reliably get to 90%+ because the *type* of failures (fabricated attribution) is deterministic, not stochastic. But if data quality fixes bring pass rate to 70-80%, then Best-of-N=5 at $0.20/M is more economical than 70B at $0.90/M."
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/pipeline_architecture_insight.md",
   "lines": "100",
   "quote": "So Best-of-N is a multiplier, not a miracle. The base model still needs to be competent. Target P≥0.60 per type before Best-of-N becomes highly effective."
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/research_rag_factual_grounding.md",
   "lines": "406",
   "quote": "Beyond the principle, our evaluator results show the model consistently picks wrong facts — this is a systematic failure, not a stochastic one that retries would fix."
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/mcq_set_journey.md",
   "lines": "112",
   "quote": "**Why 40% might be the new ceiling:** The training data (raft_combined) itself has fabricated attributions. Some of the 18,768 MCQ_SET records have slightly wrong dates or sources — they just passed InceptBench at the time, which has a 50% flip rate. Training on data that sometimes has wrong attributions = training on signal + noise."
  },
  {
   "truth": 66,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/evaluation_methodology.md",
   "lines": "137",
   "quote": "3. **Best-of-N exploits this.** If we generate 5 candidates and pick the best, we're not just picking the highest-quality generation — we're also averaging out evaluator noise. An item that would flip 50% gets scored 5 times; we keep the one that scored highest, which correlates with being genuinely better even if the noise is high."
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/pipeline_architecture_insight.md",
   "lines": "58",
   "quote": "- auto-overrides reasoning_type if learning objective contains \"Compare\" or \"continuity and change\""
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/prompt_engineering_deep_dive.md",
   "lines": "109",
   "quote": "3. The constraint is specific and checkable (\"derivable from\")"
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/overnight_automation.md",
   "lines": "212",
   "quote": "1. **Testable:** The next tick measures whether THAT specific change improved things. Multiple simultaneous changes = unknown attribution."
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/gemini_benchmark_relentless.md",
   "lines": "202",
   "quote": "The analyst was forced to propose ONE change, not multiple. This made each iteration testable."
  }
 ]
}
```
