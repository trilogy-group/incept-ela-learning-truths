# Generating with a model

88 learnings. Each says where it came from and what argues against it. [What a perfect question is](../PERFECT-QUESTION.md) collects the criteria by facet, and [How to generate perfect questions](../GENERATING.md) collects the methods by stage.

### A principle is evidence, not a rule

Treat a teaching principle, or a question generated from one, as evidence for a rule: before it drives generation, state its conditions, effect, scope, precedence, exceptions, conflicts and tests. A 562-row corpus of teaching principles mixed evidence, preferences, specifications, findings and policy, and lacked predicates, effects, scope, precedence, exceptions, conflicts and tests.

Intake analysis for an experiment on steering generation with teaching rules examined a 562-row corpus of teaching principles and the yes-or-no questions generated from it. Its records mixed evidence, preferences, specifications, findings and policy, and predicates, effects, scope, precedence, exceptions, conflicts and tests were absent, so treating them as executable switches was rejected as a category error. The intake ruled that a principle statement is source evidence, not an executable rule, and the study's closing lessons reject treating source statements as executable rules without typing and review. An approved rule needs its proposition, effect, applicability, exceptions, provenance and tests to be reviewable, and a model may help extract it but may not certify it.

Quoted:

- `grade3-reading/bias_experiment/experiment-record/docs/02-assumption-register.md` (19): “Records mixed evidence, preferences, specifications, findings, and policy; predicates, effects, scope, precedence, exceptions, conflicts, and tests were absent.”
- `grade3-reading/bias_experiment/experiment-record/docs/02-assumption-register.md` (44): “The retained source snapshot contains 562 doctrine rows.”
- `grade3-reading/bias_experiment/experiment-record/docs/01-goal-and-scope.md` (33): “A doctrine statement is source evidence, not already an executable rule.”
- `grade3-reading/bias_experiment/llm-instruction-portability-study/docs/04-decision-and-lessons.md` (39): “Treating source statements as executable rules without typing and review.”
- `grade3-reading/bias_experiment/experiment-record/evidence/knowledgebot/kb-0131-pedagogy-decision-bank-experiment-intake.qmd` (254-255): “`approved` requires the proposition, answer/effect, applicability, exceptions, source provenance, and tests to be reviewable. A model may assist extraction but may not certify its own atom.”

Against: none found

<sub>method · stage: ground · generation, review, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Accuracy over any quota

Let accuracy override any length or span quota in a writer's instructions, because a writer that can't meet a quota truthfully may bend the facts to meet it. A minimum of 20 years made the writer stretch a shorter period back in time.

The AP generator's essay rule asked for the full period or a large subset, at least 20 years (`icloud-work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md`). For a topic spanning only 12 years, the writer moved its start date earlier to meet the minimum, which made the prompt historically inaccurate. The rule was replaced on the principle that historical accuracy outranks arbitrary length requirements (the same file).

Quoted:

- `icloud-work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md` (18): “"Use the FULL period or a large subset (minimum 20 years)"”
- `icloud-work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md` (31): “4. LLM extends to 1850 to meet 20-year minimum → historically inaccurate”
- `icloud-work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md` (34): “**Principle:** Historical accuracy > arbitrary length requirements”

Against: One case; the proposal is marked implemented, but no result measured after the change is recorded (`icloud-work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md`).

<sub>method · stage: write · generation, integrity · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Aim every task at the lesson question

Give every task's writer the lesson's one question, and point each task that can serve it at what bears on it, preferring the lines a judge found help answer it.

The lesson engine puts the lesson question into every block's prompt, and before any block is written it asks the judge, line by line, whether each line helps a careful reader answer that question (`g9/transformer/src/mechanics/util.js`; `g9/transformer/src/analyse.js`). The evidence hunt's claim, the open check's key moment and the word web's big idea are each asked for because they bear on the question, and the quick check, open check and evidence hunt are also told up to eight of the lines the judge found most relevant (`g9/transformer/src/mechanics/evidence-hunt.js`, `open-check.js`, `word-web.js`).

Quoted:

- `g9/transformer/src/mechanics/util.js` (43): “export const context = (ctx) => `LESSON QUESTION: ${ctx.question}\n\nTEXT (${ctx.text.kind}):\n${unitsBlock(ctx.text)}`;”
- `g9/transformer/src/analyse.js` (12): “Does line L${u.n} of text help a careful reader answer lesson_question?”
- `g9/transformer/src/mechanics/evidence-hunt.js` (23): “TASK: write one claim about the text that helps answer the lesson question, for the reader to prove by finding the”
- `g9/transformer/src/mechanics/open-check.js` (34): “TASK: one open reading check on a key moment of the text that bears on the lesson question: a question a Grade 9 reader”
- `g9/transformer/src/mechanics/word-web.js` (35-36): “Choose the ONE word for the big idea that runs through this passage and bears on the lesson question”
- `g9/transformer/src/mechanics/util.js` (41): “Prefer them, but use any line that fits the task.”

Against: The relevant lines are a preference, not a rule: "Prefer them, but use any line that fits the task." (`g9/transformer/src/mechanics/util.js`, line 41). The glossary, key words and word in focus are chosen for reading the text, not for the question.

<sub>method · stage: ground · alignment, generation, stimulus · universal · from g9 · adopted-rule · held · found in [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Ask only for the specifics needed

Ask a writer only for the specifics a task needs, taken from a verified record, since every name, date or figure it recalls is a chance to invent one. Dropping the named-source requirement raised factual accuracy from 60% to 70%, at 20 items per variant.

In the AP work, 15 of 17 factual-accuracy failures on short-answer items disappeared once the marking guide stopped asking for a list of specific named evidence, and the record's lesson is that every specific claim is an opportunity for the model to be slightly wrong. In a sweep of variants at 20 items each, dropping the named-source requirement raised factual accuracy from 60% to 70%, and invented attributions were the main fabrication in generated source passages, plausible but not accurate. An item of 7 documents holds 7 independent claims that must all be right, and a more inventive writer's longer documents carried more fabricated details. Marking guides should describe the reasoning that earns credit, not list specific evidence.

Quoted:

- `icloud-work/ML learnings/gemini_benchmark_relentless.md` (130): “**The broader lesson:** The more specific the evidence the model is asked to enumerate, the more hallucination surface area. Every specific claim (date, name, treaty, publication founding year) is an opportunity for the model to be slightly wrong. Reducing the specificity requirement reduces the hallucination rate.”
- `icloud-work/ML learnings/gemini_benchmark_relentless.md` (126): “**Result:** 15 of 17 factual_accuracy failures in SAQ disappeared immediately.”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (50): “**Method:** test_variants.py — 9 variants, N=20 each, APUSH Unit 7”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (56): “| no_source | 50% | 70% | Best factual_accuracy |”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (57): “| baseline | 45% | 60% | Standard prompt |”
- `icloud-work/ML learnings/mcq_set_journey.md` (169): “3. **Attribution is the trap.** Every MCQ_SET needs a historical author and date. The model learned to generate plausible-sounding attributions. Plausible ≠ accurate.”
- `icloud-work/ML learnings/sft_v7_benchmark_postmortem.md` (116): “**3. DBQ document generation is the hardest factual load.** 7 documents × each needing accurate source/date/content = 7 independent factual claims that all must be correct. Probability of all 7 being right with a 14B model: low.”
- `icloud-work/ML learnings/gemini_benchmark_relentless.md` (168): “**The counterintuitive insight:** Flash produces CLEANER DBQ outputs than Pro in some cases. Pro's creativity → longer, more detailed documents → more hallucination surface area. Flash's conservatism → shorter, more cautious documents → fewer fabricated details → better factual_accuracy.”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (59): “| no_source_nodates | 40% | 50% | No source + no dates |”
- `icloud-work/ML learnings/mcq_set_journey.md` (63): “- Output: primary source passage attributed to the historical author in the plan”
- `icloud-work/ML learnings/sft_v7_benchmark_postmortem.md` (47): “The failures are NOT in the question itself. They're in the **scoring notes the model generates**.”
- `icloud-work/ML learnings/research_rag_factual_grounding.md` (35): “- **Task format**: When the generation task involves producing many fields simultaneously (like a structured rubric with question stem, answer choices, scoring guide, and historical evidence), the model's attention dilutes across fields and it falls back on parametric defaults for lower-salience fields like rubric details.”
- `icloud-work/ML learnings/gemini_benchmark_relentless.md` (122): “15 of 17 factual_accuracy failures were in the scoring notes, not in the question content itself.”
- `icloud-work/ML learnings/gemini_benchmark_relentless.md` (124): “**The fix:** Changed scoring notes instruction to: "Describe analytical reasoning that earns the point (no evidence lists)."”

Against: Cutting more did not keep helping: dropping dates as well gave 50% factual accuracy, and an outright ban on specific dates gave 0% on short answers (master_strategy_apr24.md line 105); the gain was two items in twenty; and the pipeline still credits a newly written passage to the historical figure in its plan, which a verified attribution doesn't turn into a real quotation. On the fine-tuned writer an instruction not to list specifics was ignored: telling it not to use specific facts "just means it uses wrong specific facts instead of right ones" (`icloud-work/ML learnings/sft_v7_benchmark_postmortem.md`, line 62).

<sub>method · stage: ground · generation, integrity, stimulus · universal · from ap, research · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Audit what exists before making more

Before making more material, audit how much already exists and how good it is, and ask whether the failure is an absence or a fault in what exists. An audit found 18,768 question-set records already on hand while 500 new ones were being planned.

In the AP question work, an audit found 18,768 question-set records already on hand while 500 new ones were being planned, and the lesson kept was to audit existing data before generating new (`icloud-work/ML learnings/decisions_and_pivots_timeline.md`). Adding examples of a missing item type lifted it from 0% to 12%: that fixed the format, but the content still failed, and the hoped-for 80%+ stalled at about 12% (`icloud-work/ML learnings/training_data_journey.md`). A 70k-record plan was cancelled once analysis showed that more data in the same format wouldn't fix the factual failures (`icloud-work/ML learnings/failures_and_false_starts.md`). The audit counted records but didn't check them, and some had wrong dates or sources (`icloud-work/ML learnings/mcq_set_journey.md`). More material can fix an absence; more of the same won't fix a fault in what exists.

Quoted:

- `icloud-work/ML learnings/decisions_and_pivots_timeline.md` (107): “**The audit finding:** We had been planning to generate 500 new MCQ_SET examples when we already had 18,768+ after combining raft_combined and sft_v6_combined.”
- `icloud-work/ML learnings/decisions_and_pivots_timeline.md` (111): “Always audit existing data before generating new.”
- `icloud-work/ML learnings/training_data_journey.md` (111): “**Lesson:** Before building a bigger dataset, ask: does the failure mode respond to more data? MCQ_SET at 0% responded to adding examples (0%→12%). MCQ at 60% ceiling did NOT respond to more prompt engineering. Different failures need different fixes.”
- `icloud-work/ML learnings/decisions_and_pivots_timeline.md` (98): “**What we got wrong:** Thought 504 examples would get MCQ_SET to 80%+. Actual ceiling was ~12%. The format problem was solved; the content quality problem wasn't.”
- `icloud-work/ML learnings/mcq_set_journey.md` (112): “Some of the 18,768 MCQ_SET records have slightly wrong dates or sources”
- `g9/transcript/chat-transcript.redacted.txt` (2597): “Presenting those as new recommendations would still undershoot.”
- `g9/transcript/chat-transcript.redacted.txt` (2620): “My pack undershot that.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (777): “inventory and deduplicate the candidate corpus before making size claims;”

Against: The fault half was never tested: whether more question-set data would fix the quality problem, or whether the bottleneck was the fabricated attributions in the data, was left unknown (`icloud-work/ML learnings/decisions_and_pivots_timeline.md`, line 127), and a proposed mini-test was answered without being run (`icloud-work/ML learnings/failures_and_false_starts.md`, line 23). The cross-team summary favours volume: "More representative examples of the hardest cases = better coverage of the output space." (`icloud-work/ML learnings/cross_team_learnings_full.md`, line 73). The second example in the recorded lesson is about prompt changes, not more data (`icloud-work/ML learnings/training_data_journey.md`, line 111).

<sub>method · stage: improve · generation, measurement · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Best-of-N inherits its grader

Let a grader pick only among drafts passing the code checks, after showing on saved candidates that it tracks the real criterion and beats taking the first valid one. Against a cheap ranker whose agreement with the true verdicts was no better than chance, picking the best of several drafts gave zero lift.

A review of a proposed item factory settled by mechanism and code that best-of-N is argmax over the grader, so it inherits the grader's correlation to the truth and none of its own: measured, it gave zero lift against a cheap same-family ranker with kappa about 0, and converged only against a grounded oracle, which found a 0.94 pass in 2 candidates where 10 hand iterations had failed (`grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md`). The same record calls the cheap ranker a kappa~0 rubber stamp on subtle failures. A fact sheet found that an AP pipeline's 99% came from caching plus best-of-N, not from the generator (`grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md`). Validating a grader before it picks among drafts includes checking whether its picks beat taking the first valid draft.

Quoted:

- `grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md` (67): “best-of-N is mathematically argmax over the grader, so it INHERITS the grader's correlation-to-truth and ZERO of its own (measured: zero lift vs cheap same-family ranker, kappa~0”
- `grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md` (67): “converges only against a grounded oracle where it found a 0.94 pass in 2 candidates while 10 hand-iterations failed”
- `grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md` (9): “the cheap holistic ranker is a kappa~0 rubber stamp on subtle failures”
- `grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md` (55): “the "99%" was **cache + best-of-N**”
- `icloud-work/aptraining/workspace/comms/from_cheater/2026-05-25T1014Z_ESCALATE_v7_also_regressed_MCQSET_CAPPED.md` (29-30): “- The "best" pick was effectively random — sometimes the better candidate, sometimes worse”
- `icloud-work/aptraining/workspace/comms/from_cheater/2026-05-25T1014Z_ESCALATE_v7_also_regressed_MCQSET_CAPPED.md` (38-39): “The IB grader is doing real work; without it, local validators can only catch structural defects, not content quality.”
- `icloud-work/aptraining/workspace/comms/from_cheater/2026-05-25T1138Z_DEFINITIVE_CLOSURE_MCQSET_13_attempts.md` (37-39): “Adding K=3 candidates makes pass rate WORSE because the local validator picks structurally-clean candidates that are sometimes factually weaker.”
- `icloud-work/aptraining/workspace/comms/from_cheater/2026-05-25T1138Z_DEFINITIVE_CLOSURE_MCQSET_13_attempts.md` (25): “| **12** | **EXPLOIT-013 v8 = v4 prompt + temp=0.0** | **52% (13/25) ← BEST** |”
- `icloud-work/aptraining/workspace/comms/from_cheater/2026-05-25T1138Z_DEFINITIVE_CLOSURE_MCQSET_13_attempts.md` (26): “| 13 | EXPLOIT-013 v9 = K=3 temp=0.0 + local-pick | 24% (regressed) |”
- `icloud-work/aptraining/workspace/comms/from_pil/2026-05-20T0821Z_PIL_WEEKLY_APUSH_REPORT.md` (28): “- Selector calibration: Gemini tied first-valid at 13/15 on saved balanced15 candidates; it is active but not proven better.”
- `icloud-work/aptraining/Cheater/scripts/ranker/README.md` (111): “- Ranker picked index 0 (one of the tied-top items)”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/SELECTOR_CALIBRATION_TAKEAWAYS_20260520.md` (17): “- Evidence: if bad candidates reach the selector, a fluent but invalid MCQ_SET can beat the actually passing raw candidate.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/SELECTOR_CALIBRATION_TAKEAWAYS_20260520.md` (18): “- Rule: deterministic filters come before Gemini. Gemini is a selector, not a rescue path.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md` (33): “| first_valid | 15 | 13 | 0.8667 | 0.965333 | 0 |”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md` (35): “| gemini | 15 | 13 | 0.8667 | 0.965333 | 0 |”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md` (37): “| oracle | 15 | 13 | 0.8667 | 0.965333 | 0 |”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md` (39): “Takeaway: Gemini did not beat first-valid on this archive. Do not enable Gemini as a selector for this policy from this evidence. It is audit-only until a larger saved-candidate calibration proves a lift.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/SELECTOR_CALIBRATION_TAKEAWAYS_20260520.md` (44): “- MCQ_SET: staged route; extra K only after filters, and selector must beat first-valid in calibration.”
- `g9/transformer/src/question.js` (2): “the open, well-formed ones; the judge keeps the first it finds answerable from the text alone and worth a lesson”
- `g9/transformer/v02/QA.md` (90-91): “the writer drafts three, code keeps the open ones, Jev keeps the first answerable from the text”
- `g9/transformer/test/server.test.mjs` (87): “a text without a question is given one: open, well formed, answerable on the judge's word, the same next time”
- `g9/transformer/test/server.test.mjs` (94): “the yes-or-no draft is dropped”

Against: The item factory's evidence came from AP history items (`grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md`), and a fact sheet rates the claimed convergence of the two efforts as weak, AP findings carried onto grade 3 rather than independent replication (`grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md`). One small positive check for a model ranker, on a single pool of three items: "- Ranker picked index 0 (one of the tied-top items)" (`icloud-work/aptraining/Cheater/scripts/ranker/README.md`, line 111); no larger test of it was found. On another archive of 150 rows the selector picked a passing candidate on 137 of the 145 rows where one existed, a recall of 0.945 (icloud-work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/gemini_selector_calibration_final.md, line 15).

<sub>method · stage: judge · generation, evaluation · universal · from ap, g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Borrowed data stays a placeholder

Mark data borrowed from another group of students, such as another grade's weak skills, as a placeholder, never as measured for the students in hand. Until its own data arrived, one new grade's generator could target the earlier grade's three weak skills only as a flagged placeholder.

The generator harness for a new grade lists the cohort data that must come from that grade and must not be made up (`grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md`). Until the new grade's weak-skill data lands, it targets the earlier grade's weak skills as a marked placeholder, explicitly flagged and never presented as measured, and it must not reuse the earlier grade's test norms of 186.6, 193.9 and 197.1 (the same file).

Quoted:

- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (275): “**G5 cohort numbers are TO-SOURCE, NOT invented.**”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (277-279): “target the G3 weak-skills — compare/contrast, cause/effect, sequence — as a *marked placeholder*, explicitly flagged, never presented as measured G5 data); **G5 MAP norms** (do NOT reuse G3's 186.6 / 193.9 / 197.1);”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/axis-decision-memo.md` (10): “The G2 BrainLift v0.1 inherited G3's premise — *students pass internal mastery but stay flat on MAP (a test-rigor problem)*. We then pulled the live G2 data (1,597 students, `rpt2_*` views, 2026-06-23). **The premise does not hold for G2.**”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/axis-decision-memo.md` (23): “The students who pass our internal test **transfer well** (85th percentile). The rigor gap is ~8 students. The premise is refuted for G2.”
- `grade3-reading/ti-courseplans/courses/g6-reading/G6-FORK-DECISION-BRIEF.md` (86): “The "EGM=0 / students can't pass grade-level tests" premise that the original build rested on was **falsified by the team's own data**: passing is rare because of *non-participation*, not test failure.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (508): “all labelled as G8 facts / G5 facts, never as G7 magnitudes”

Against: none found

<sub>method · stage: ground · integrity, generation, measurement · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Build questions to need the text

Make a question need its text by how the text and the item format are built, not by filtering, patching or regenerating questions afterwards. Built to need the text, 60% of items survived the without-text check, against 6% of encyclopedic clones.

In the Grade 5 course, items generated construction-first survived the anti-leak gate at 60% against 6% for encyclopedic clones, and raw generated banks leaked ~94% blind (`grade3-reading/ti-courseplans/docs/practice-layer-spec.md`, lines 21-23). On the same encyclopedic passages, a cross-family run found leak rates of MCQ 99.5% and MSQ 100% against hot-text 1.67% and 0% for sequence, match and two-part evidence items, and conversion lanes showed the leaky formats could be redesigned into passage dependence (choice 142/234 converted; hot-text 90/117) (`grade3-reading/ti-courseplans/courses/g5-reading/brainlifts/v0.6.qmd`, lines 23-29). Questions built to need their text survive the without-text check far more often.

Quoted:

- `grade3-reading/ti-courseplans/docs/practice-layer-spec.md` (21): “construction-first generation survived the anti-leak gate at 60% vs 6% for encyclopedic clones”
- `grade3-reading/ti-courseplans/docs/practice-layer-spec.md` (22-23): “raw generated banks leaked ~94% blind”
- `grade3-reading/ti-courseplans/courses/g5-reading/brainlifts/v0.6.qmd` (24-25): “different blind-solve leak rates by question *format*: MCQ 99.5%, MSQ 100% — hot-text 1.67%, > sequence 0%, match 0%, EBSR 0% (cross-family run, 2026-06-23/24).”
- `grade3-reading/ti-courseplans/courses/g5-reading/brainlifts/v0.6.qmd` (26): “**MCQ/MSQ format does not force reading; hot-text, sequence and match do.**”
- `grade3-reading/ti-courseplans/courses/g5-reading/brainlifts/v0.6.qmd` (28): “be *redesigned into* passage-dependence (choice 142/234 converted; hot-text 90/117)”
- `grade3-reading/ti-courseplans/courses/g5-reading/brainlifts/v0.6.qmd` (29): “leaky-by-default formats convert under per-item redesign.”
- `grade3-reading/artifacts/LANE1_COURSE.md` (167): “Regen pilot (Wave 3) showed 9.5pt improvement in MCQ leak (99.5% → 90.0%) but leak remained”
- `grade3-reading/artifacts/LANE2_GENERATOR.md` (31): “**Fix verdict:** NOT fixable with option-length patches. Requires passage strategy redesign.”
- `grade3-reading/artifacts/LANE1_COURSE.md` (152): “- Skeleton redesign (V2) resolves the regen problem by eliminating MCQ/MSQ from the build and substituting passage-dependent formats with sufficient pool depth.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (555-557): “First, prefer the resistant formats for anything carrying weight: hot text, match, sequence and short constructed response, which have no options to guess between.”
- `incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (305): “re-anchoring rewrites converted only 1/11”
- `incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (305-306): “The one converting rewrite was a **text_entry item whose answer is a verbatim passage phrase**”
- `incept-package-hub/course-packages/courses/g7-reading/review/evidence/course-graph-guide.md` (54): “Verbatim passage-phrase text-entry — answer is a verbatim passage phrase (the G8-POC's one converting rewrite; strongest passage-binding).”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-main-checkout-jul-work.patch` (610): “Mastery gate hardened live, 84.2% → 64.0% blind-solvable after 47 hardened items deployed”
- `grade3-reading/artifacts/g5-course-candidate-v0/ASSEMBLY_REPORT_V2.md` (11-13): “the root cause is not item quality — it is passage design. Encyclopedic passages make MCQ/MSQ/EBSR answerable without reading, at rates that regeneration alone cannot fix without rewriting the passage corpus.”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/markdown/BRAINLIFT.md inside it) (81-82): “Fact-disjointness is a design input, not a red-team afterthought”

Against: The 0% for ordering items came from a gate that scored one seeded shuffle per item, and a re-probe under four shuffles later decertified 65 of 118 (`grade3-reading/ti-courseplans/courses/g5-reading/analysis/seq-reprobe-2026-07-07/README.md`); the spec calls the 60% and 6% a historical basis for pricing and design, not current readiness (`grade3-reading/ti-courseplans/docs/practice-layer-spec.md`, line 20). A change of format alone did not fix it: a later check by two model families found 94.6% of 353 items in the formats thought safe still leaked, confirming that a leak-resistant format is not the same as a low leak rate (`grade3-reading/artifacts/g5-merged-course/a2-cross-family-regate.md`, line 21).

<sub>method · stage: write · generation, integrity, format · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Build the rule in

Where a rule can be built into what a model is given, build it in rather than rely on a check to catch the breach.

In a reading course, a moment that runs before the story replied to a child with the story's plot, though the child hadn't opened it (`grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md`). The fix that mattered was on the request, not the wording: moments before the passage send the scorer an empty passage and an empty word list, so it cannot quote what the child hasn't read, and a gate with 11 assertions checks it. The course's own lesson from it: a rule you can't violate beats a rule you must remember.

Quoted:

- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md` (46-47): “so it *cannot* quote what the child hasn't read. A rule you can't violate beats a rule you must remember.”

Against: none found

<sub>method · stage: ground · integrity, generation, evaluation · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Check a link's kind and direction

When content links two facts, check that the stated kind and direction of the link hold, not only that the facts are related. About 20 of the 160 generated links people rejected were wrong in kind, direction or claim, such as one that ran the other way around.

People checked 2,087 model-generated links between knowledge nodes for an AP history course and marked 160 'No'. About 20 of the rejection notes concern the link's kind, direction or claim: one idea inspired rather than enabled another, 'included' was the right term instead of 'enabled', a link ran 'more the other way around', or one fact did not exemplify the other. Rejection rates by stated type ran from 4.2% for 'causes' (6 of 143) to 9.1% for 'exemplifies' (76 of 835).

Quoted:

- `downloads/AP US History - Knowledge Schema - SME Tracker.xlsx` (sheet 'Unit 3 Relationships', row 74, column J (type 'enables', Keep 'No')): “The description is an over simplification of the two statements. Locke's ideas didn't necessarily enable the ideological shift--rather it inspired and gave language to republican principles of self governances.”
- `downloads/AP US History - Knowledge Schema - SME Tracker.xlsx` (sheet 'Unit 5 Relationships', row 41, column J (type 'influences', Keep 'No')): “more the other way around”
- `downloads/AP US History - Knowledge Schema - SME Tracker.xlsx` (sheet 'Unit 1 Relationships', row 134, column J (type 'exemplifies', Keep 'No')): “the trade networks don't exemplify how they adapted to their environments.”
- `grade3-reading/ui-audit-2026-09-08/round-4/question-causality/PROPOSAL.md` (3): “correct a false causal implication in the current student question.”
- `grade3-reading/ui-audit-2026-09-08/round-4/question-causality/PROPOSAL.md` (5): “Current source says “The Lost Boys scrambled for their weapons, but they were outnumbered.””
- `grade3-reading/ui-audit-2026-09-08/round-4/question-causality/PROPOSAL.md` (5): “The keyed answer describes the numerical disadvantage they faced, not something caused by reaching for weapons.”
- `grade3-reading/ui-audit-2026-09-08/round-5/question-audit/RETELL-PROPOSAL.md` (34): “Both rubric and uses-but-so criterion say “Uses at least one But and one So to join an event to its consequence.” So can signal a result; but signals contrast.”
- `grade3-reading/ui-audit-2026-09-08/round-5/question-audit/RETELL-PROPOSAL.md` (38): “L7 second_hint “the boys were armed, so they charged. Peter fought Hook, but Hook fell” is a poor contrast because Hook falling is the expected fight result.”
- `grade3-reading/ui-audit-2026-09-08/round-5/question-audit/RETELL-IMPLEMENTATION.md` (7): “Both lessons' connective requirements distinguish contrast from result.”
- `grade3-reading/ui-audit-2026-09-08/bead-specs/causality.md` (6): “Asks what happened as a result of scrambling for weapons; key says pirates outnumbered them, while source uses contrast but.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (3020): “L6/L7 But/So rubric treats contrast as consequence; L7 hint uses expected fight outcome as contrast.”
- `grade3-reading/ui-audit-2026-09-08/round-4/question-causality/REVIEW-by-unit1.md` (5): “The boys reaching for weapons does not cause pirates to outnumber them; being outnumbered is the obstacle already present.”

Against: Most generated links were kept, and repeats, not wrong kinds of link, were the commoner reason for rejection, so the per-type rates are driven mostly by repeats.

<sub>method · stage: ground · integrity, generation, review · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Check a model's importance labels

Check a model's labels of which facts are essential against people's judgment before they decide what is taught or tested. A model's essential-or-supporting label and the level people set differed on 370 of 1,533 knowledge nodes, 222 of them labelled essential but set to supporting.

Across the nine unit sheets of an AP history course's knowledge schema, the generator's label in its 'Classification' column and the level people set agree on 1,163 nodes and differ on 370, about a quarter. Of those, 222 nodes the model labelled essential were set to supporting, 139 went the other way, and 7 labelled both were set to essential. There is no baseline of two people agreeing, so the 24% measures disagreement, not model error.

Quoted:

- `downloads/AP US History - Knowledge Schema - SME Tracker.xlsx` (sheet 'Unit 1 Nodes', row 1, column D (generator label)): “Classification”
- `downloads/AP US History - Knowledge Schema - SME Tracker.xlsx` (sheet 'Unit 1 Nodes', row 1, column L (human-set level)): “Essential/Supporting/Nuanced detail”

Against: Nothing records whether people set the level before or after seeing the model's label, so the agreement may be inflated.

<sub>method · stage: ground · alignment, evaluation, review · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Check curriculum records against the framework

Before adopting or generating from curriculum sources, compare candidates item by item on content and check their facts and labels against the official framework, because derived copies shift labels. An audit of 30 records against the published framework found 6 (20%) paired with an objective from a neighbouring topic.

A model compared 30 records from a curriculum service with the published course framework and found 6/30 (20%) of objectives taken from a neighbouring topic. Later, items for topics whose period and content disagreed could not satisfy the judge's chronology check, and a cross-check named that mismatch as the root cause. One such topic had been tagged unit=1 by a processing step that mis-mapped a Unit 2 standard; the upstream curriculum was right. Do the check course by course and record the version of the framework checked against.

Quoted:

- `icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-04-28T1500Z_api_vs_cb_ced_verdict.md` (16): “- **Real systematic drift:** **`lo_drift` in 6/30 (20%)** — the API attaches a Learning Objective from a neighboring topic / LO, not the LO that CB CED actually pairs with that KC.”
- `icloud-work/aptraining/workspace/comms/from_data/2026-05-28T1645Z_incept_curriculum_pull_report.md` (87): “**Root cause of the bug**: inceptbench's KC-derivation pipeline mis-mapped this upstream U2 substandard to its `c_Qbro` short code and tagged it `unit=1` during processing. The bug is in the inceptbench-side conversion script, not in upstream curriculum.”
- `icloud-work/aptraining/workspace/comms/from_cheater/2026-05-25T1631Z_DBQ_cross-check_vs_Quill_pass-criteria_pack.md` (68-70): “Period mismatch is the root cause — v80b can't satisfy chronology guardrail when the KC's period and content disagree.”
- `icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-04-28T1500Z_api_vs_cb_ced_verdict.md` (15): “- **Off-by-period drift (the InceptBench APEURO disease):** **ZERO instances detected.**”
- `icloud-work/aptraining/workspace/comms/from_data/2026-05-28T1549Z_u1_kc_audit_report.md` (95): “**12 of the 18 "flagged" are false-positives** (date range starts pre-1607; remap was wrong call by date-only heuristic).”
- `icloud-work/ML learnings/knowledge_and_rag_pipeline.md` (230): “3. **Fact verification:** Each fact in curriculum_facts.json should be verified against AP curriculum documents. Some facts may be outdated or approximate.”
- `icloud-work/ML learnings/knowledge_and_rag_pipeline.md` (234): “None of these are implemented yet.”
- `icloud-work/ML learnings/sft_v7_benchmark_postmortem.md` (150): “The following are VERIFIED correct facts for this topic.”
- `icloud-work/ML learnings/knowledge_and_rag_pipeline.md` (14): “**Size:** 4,177 facts (as of April 2026; earlier sessions showed 3,347 facts)”
- `icloud-work/ML learnings/research_educational_content_generation.md` (108): “Our existing `curriculum_facts.json` (3,347+ facts) is a form of RAG grounding. The literature suggests more structured retrieval (graph-based or with explicit entity matching) would improve factual accuracy beyond what flat keyword retrieval achieves.”
- `icloud-work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md` (26): “- 1 wrong_unit: APWH `c_lAtP` Columbian Exchange tagged Unit 0 instead of Unit 4 — single-record fix needed in API”
- `icloud-work/aptraining/helpers/data/output/curriculum_kc_period_audit.md` (8): “- **76 KCs** flagged as period-mismatched.”
- `icloud-work/aptraining/helpers/data/.agent/memory/data_quirk_apwh_period_table.md` (28): “Concrete observed failure: an apwh/leq Unit 6 prompt had `LEARNING OBJECTIVE: Explain how the development of new technologies changed the world from 1900 to present` paired with `TIME PERIOD: c. 1750 to c. 1900 (STRICT -- nothing outside this range)`.”
- `icloud-work/aptraining/handover/2026-05-01_session_end/SHADOW_HANDOVER.md` (59): “| Non-canonical KC IDs | 77.5% (803/1036) use opaque hashes (`c_4EvW`, `s_saxW`); only 14% match `KC-X.Y.Z+N` |”
- `icloud-work/aptraining/handover/2026-05-01T1039Z_oracle_session/HANDOVER.md` (343): “InceptBench APEURO IDs off by one period vs CB CED. Curriculum repo IDs match official CB CED.”
- `icloud-work/aptraining/handover/2026-05-01T1039Z_oracle_session/HANDOVER.md` (345): “39% of curriculum has no IB match; 99.8% of IB has no curriculum match.”
- `icloud-work/aptraining/apllm-history/runtime_assets/curriculum_facts_bundle_v1/README.md` (51): “# Same node_id can exist in multiple courses (e.g. KC-1.1.I.A in APUSH + APEURO).”
- `ap-agent-memory/feedback_oracle_source_reconciliation.md` (12): “across all 239 InceptBench APEURO entries vs curriculum repo APEURO; 224 matched by content but 218 at different IDs, with systematic off-by-one-period shift confirmed against official CB CED.”
- `ap-agent-memory/feedback_oracle_source_reconciliation.md` (12): “APUSH analysis: 39% of curriculum has no InceptBench match, 99.8% of InceptBench atomic facts have no curriculum match — different hierarchy tiers.”
- `ap-agent-memory/MEMORY.md` (116): “**APUSH** = MERGE (curriculum repo skeleton + InceptBench atomic facts; 39% / 99.8% non-overlap means single-source halves pedagogy). Wrong source per course = silent training corruption.”
- `ap-helpers-oracle-agent-memory/project_oracle_session_20260501.md` (12): “RECONCILIATION ruling per course (APEURO=curriculum-repo, APWH=InceptBench, APUSH=MERGE)”
- `ap-agent-memory/MEMORY.md` (82): “zero APEURO off-by-period drift in canonical API; InceptBench bug did NOT propagate”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (53): “The local course vocabulary listed seven reasoning operations, while the CED defines six historical thinking skill categories.”

Against: The same 30-record audit, itself a model's comparison with the framework, found no topic in the wrong period: "- **Off-by-period drift (the InceptBench APEURO disease):** **ZERO instances detected.**" (icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-04-28T1500Z_api_vs_cb_ced_verdict.md, 15). A date-only screen over-flags: "**12 of the 18 "flagged" are false-positives** (date range starts pre-1607; remap was wrong call by date-only heuristic)." (icloud-work/aptraining/workspace/comms/from_data/2026-05-28T1549Z_u1_kc_audit_report.md, 95) The audit called it a single-record fix and not a systemic issue (`icloud-work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md`, line 63), and what it did to items built from that record is not in this evidence. The period sweep's suggestions are best-effort and need review before any data change (icloud-work/aptraining/helpers/data/output/curriculum_kc_period_audit.md, line 69). The shifted labels did not reach the curriculum service used for generation, which an audit found free of the shift (`MEMORY.md`, line 82). The fixes were still open at a later handover (`project_oracle_session_20260501.md`, lines 22 and 24), and no effect on generated items was measured.

<sub>method · stage: ground · alignment, generation · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Check every tag outside the generator

Check each grade and standard tag outside the generator, against the delivered text and the skill it tests. Told to write for grade 5, generating agents produced 17 of 20 items at grade 3 standards.

Agents told to write for grade 5 produced 17 of 20 items at grade 3 standards, a pull toward their usual grade, so the reading project's account of what its generator can't do for itself puts an external grade-band and standards check in the gate, rejecting off-band tags (`grade3-reading/artifacts/alpha-read-packager/LLM_GENERATION_BOUNDARY.md`). A genre-aware audit of 26 items' standard tags made four corrections, one of them a literary tag on a purely informational passage, and left four borderline items flagged, not flipped, to avoid a confident wrong guess (`grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md`). A standards backfill for a grade 5 unit tagged an item only where the live passage still matched the tested one, 558 of 600, and left the 42 whose passage had been swapped uncoded, since coding them from the stale snapshot would be fabrication (`grade3-reading/artifacts/alpha-read-packager/SUMMARY_AGENT_G5.qmd`). Leave an item untagged where the delivered text no longer matches its source.

Quoted:

- `grade3-reading/artifacts/alpha-read-packager/LLM_GENERATION_BOUNDARY.md` (38): “Told "G5," generate-agents produced 17/20 items at RI.3.x (prior-pull)”
- `grade3-reading/artifacts/alpha-read-packager/LLM_GENERATION_BOUNDARY.md` (48): “reject off-band tags; verify tag matches construct vs CASE”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (147): “(literary tag on a purely informational creature passage)”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (151-152): “flagged not flipped, to avoid a confident wrong guess”
- `grade3-reading/artifacts/alpha-read-packager/SUMMARY_AGENT_G5.qmd` (39): “each Unit-2 item was tagged **only where the live passage still”
- `grade3-reading/artifacts/alpha-read-packager/SUMMARY_AGENT_G5.qmd` (42): “558 high-overlap (tagged), 42 low-overlap (left uncoded).”
- `grade3-reading/artifacts/alpha-read-packager/SUMMARY_AGENT_G5.qmd` (45): “from the stale snapshot would be fabrication, so they stay uncoded and named.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md` (326): “**G5 gaps:** RI.5.4 is catastrophically over-concentrated (35 items, ~23% of the G5 bank on one standard). This likely comes from the G5 JSONL curation which mapped L.5.4/L.5.5 vocabulary to RI.5.4. Needs redistribution.”

Against: none found

<sub>method · stage: settle · alignment, generation, integrity · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Check lines written at answer time

Check every line a model writes at answer time against house rules and the authored text beside it, repairing rather than discarding what fails, such as praise repeating the answer. Half the words in a conversation, the replies composed at answer time, had escaped the copy rules the other half were checked against.

In a younger-grade renderer every authored word passed the build's copy checks, but the praise and hints the scorer composed at answer time never did, so half the words in a conversation were exempt, and a model reaches for an em-dash by default. House style now runs on every reply before it is sent, rewriting rather than rejecting, because no validator can see a line that does not exist until the child answers and a child waiting on an answer is not served by a reply being thrown away and asked for again. The scorer's praise is printed above the authored full answer, so the scorer is told the answer will be printed beneath it and to name only what the child did, and a runtime check then scores how much of the praise's content the answer already contains and cuts the recital back to the acknowledgement, with thresholds pinned by a test against the real reply that prompted it. The rules call that seam between a written line and a generated one the only place nobody is reading.

Quoted:

- `othello-course-renderer-draft/repo/docs/rules/content-and-copy.md` (42-43): “R-COPY-1 and R-COPY-2 apply to every word a child reads, including the praise and the hint composed at answer time by the scorer.”
- `othello-course-renderer-draft/repo/docs/rules/content-and-copy.md` (45-46): “because no validator can see a line that does not exist until the child answers.”
- `othello-course-renderer-draft/repo/docs/rules/content-and-copy.md` (48-51): “The coach's replies never touched it, so half the words in a conversation were exempt from the rules the other half were checked against, and a model reaches for an em-dash by default.”
- `othello-course-renderer-draft/repo/docs/rules/content-and-copy.md` (54-56): “Rewritten rather than rejected. A reply with a dash in it is a good reply with a dash in it, and a child waiting on an answer is not served by it being thrown away and re-asked for.”
- `othello-course-renderer-draft/repo/docs/rules/questions-and-assessment.md` (452-453): “The scorer is told that the full answer will be printed beneath it and to name only what the child did, which makes this rare.”
- `othello-course-renderer-draft/repo/docs/rules/questions-and-assessment.md` (455-457): “`trimEcho` in `src/lib/scoring/echo.ts` scores the share of the praise's content words that the answer already contains, and cuts the recital back to the acknowledgement above the threshold.”
- `othello-course-renderer-draft/repo/docs/rules/questions-and-assessment.md` (494-497): “The praise-against-answer overlap is enforced at runtime instead, by `trimEcho`, since neither line exists until a child answers; its thresholds are pinned by `scripts/echo.test.mjs` against the real reply that prompted the rule.”
- `othello-course-renderer-draft/repo/docs/rules/questions-and-assessment.md` (467-468): “The repetition worth catching is at the seam between a written line and a generated one, which is the only place nobody is reading.”
- `grade3-reading/course-renderer/docs/rules/questions-and-assessment.md` (442-445): “One bubble, but not one paragraph, and the two halves may not say the same thing. They have different authors who cannot see each other: the praise is composed by the scorer at answer time, the answer beside it was authored with the lesson.”
- `grade3-reading/course-renderer/docs/rules/questions-and-assessment.md` (452-455): “The scorer is told that the full answer will be printed beneath it and to name only what the child did, which makes this rare. It is then MEASURED, because this is the last thing a child reads before the gate opens and a prompt is a request”
- `grade3-reading/course-renderer/docs/rules/questions-and-assessment.md` (467-468): “The repetition worth catching is at the seam between a written line and a generated one, which is the only place nobody is reading.”
- `grade3-reading/course-renderer/docs/rules/questions-and-assessment.md` (494-497): “The praise-against-answer overlap is enforced at runtime instead, by `trimEcho`, since neither line exists until a child answers; its thresholds are pinned by `scripts/echo.test.mjs` against the real reply that prompted the rule.”

Against: The same measure is deliberately not applied to authored hint ladders, where a closer hint shares many of the same words with the hint above it by design (`grade3-reading/course-renderer/docs/rules/questions-and-assessment.md`, lines 462-467).

<sub>method · stage: settle · generation, feedback, wording · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Check the hardest requests most

Spot-check a generator's hardest requests most closely, since pass rates can fall steeply as the requested difficulty rises and requests for upper grades can come back simpler than asked. Across 1,888 judged maths items, easy requests passed at 34.35% and hard ones at 14.14%.

In one analysis of 1,888 judged maths items, pass rates fell from 34.35% for easy requests to 26.28% for medium and 14.14% for hard (`icloud-work/incept/nova_forge/EXECUTIVE_SUMMARY.md`), and one grade's hard items passed at 1.54%, 1 of 65 (`icloud-work/incept/nova_forge/EXISTING_GRADES_ANALYSIS.md`). A separate generator's notes say that for upper grades 'Questions may be simpler than expected for grade level' and that 'Grades 9-10 produce elementary-level questions' (`icloud-work/incept/nova_forge/svg-llm/README.md`).

Quoted:

- `icloud-work/incept/nova_forge/EXECUTIVE_SUMMARY.md` (87): “| **Easy** | 658 | 226 | 432 | 34.35% |”
- `icloud-work/incept/nova_forge/EXECUTIVE_SUMMARY.md` (88): “| **Medium** | 643 | 169 | 474 | 26.28% |”
- `icloud-work/incept/nova_forge/EXECUTIVE_SUMMARY.md` (89): “| **Hard** | 587 | 83 | 504 | 14.14% |”
- `icloud-work/incept/nova_forge/EXISTING_GRADES_ANALYSIS.md` (196): “| Hard | 65 | 1 | 64 | 1.54% |”
- `icloud-work/incept/nova_forge/svg-llm/README.md` (40): “- Questions may be simpler than expected for grade level”
- `icloud-work/incept/nova_forge/svg-llm/README.md` (45): “- Grades 9-10 produce elementary-level questions”

Against: The gradient is not uniform: in one grade 'Performance is nearly identical across all difficulty levels', at 41.4%, 41.7% and 39.5% (`icloud-work/incept/nova_forge/AGENT2_GRADES_3_8_BASELINE.md`, line 60), and pass rates do not fall with grade, since grade 8 passed at 28.76% and grade 6 at 13.82% (`icloud-work/incept/nova_forge/EXECUTIVE_SUMMARY.md`). The evidence is maths items only, and the upper-grade clause rests on one generator's notes.

<sub>method · stage: review · generation, demand, review · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Check the request before the generator

When a request contradicts itself or the course's scope, or different generators fail it the same way, fix or reject the request before changing the generator. In one gap analysis, 2 of 4 wrong-unit failures were faults in the benchmark's own data.

In the AP generator's benchmark, two different models hard-failed the same document-based item, which the notes take as a sign that some evaluation samples are intrinsically difficult: a wrong unit mapping, an impossible spec, or a judge edge case (`icloud-work/ap-social-studies-generator/data/model_findings.md`). On one topic the judge failed one item for leaving out a civilization its objective named and another for including it, as belonging to a different course, and it failed an item whose request labelled a document-based essay easy, a level it ruled such a task can't have (`icloud-work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md`). In the final gap analysis, 2 of 4 wrong-unit failures were benchmark data quality issues (`icloud-work/ap-social-studies-generator/python/CLAUDE.md`).

Quoted:

- `icloud-work/ap-social-studies-generator/data/model_findings.md` (829): “Both models hard-failed at the same DBQ item (item 33) — confirming some eval samples are intrinsically difficult (wrong unit mapping, impossible spec, or IB v2.4.0 edge case).”
- `icloud-work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md` (50): “The question fails to address the specific learning objective requested (Inca Empire) and instead focuses on a different group (Pueblo peoples).”
- `icloud-work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md` (100): “The question targets the wrong curriculum. AP US History focuses on societies in what is now the United States; the Inca Empire is a South American civilization assessed in AP World History.”
- `icloud-work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md` (60): “There is a clear mismatch between the labeled difficulty ('easy') and the actual task complexity.”
- `icloud-work/ap-social-studies-generator/python/CLAUDE.md` (113): “- **4 curriculum alignment** (wrong unit) -- 2 are benchmark data quality issues (unfixable)”

Against: Whether a task type can be easy is the judge's view, and a scaffolded short source task could be easy for some students. That a request was impossible is inferred from two models failing the same item, and the notes themselves list other explanations, among them a judge edge case (`icloud-work/ap-social-studies-generator/data/model_findings.md`).

<sub>method · stage: improve · alignment, generation, evaluation · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Combined gains don't multiply

Don't predict the gain of stacked methods or repeated attempts by multiplying their odds as if they were independent; failures cluster, so measure the combination. A design reckoned five tries at a 68% base rate would pass 99.66% per cell, yet one item failed all 10 of its tries.

A serving design for the AP generator reckoned that with a 68% base rate all five attempts would fail only 0.34% of the time, giving 99.66% per cell. In practice some sub-standards failed systematically while others passed, one long-essay item never crossed 0.80 in two rounds of five attempts, and identical candidates had to be counted as one, not six chances. Two methods that each helped failed to compose when stacked, and the project's state summary called multiplicative stacking wishful.

Quoted:

- `icloud-work/aptraining/handover/2026-05-01T1039Z_main_session_close/02_CONSOLIDATED_STATE.md` (96): “| **Combo routing + RAG** | Failed to compose lifts | `project_combo_routing_plus_rag_failed.md` | Methods correlate; multiplicative stacking is wishful |”
- `icloud-work/aptraining/helpers/serve/serve99stack.py` (8): “- At K=5 with 68% raw base: P(all 5 fail) = 0.32⁵ = 0.34% → 99.66% per cell from Layer 3 alone”
- `icloud-work/aptraining/artifacts/pending_review/2026-05-23T082229Z_exploits_EXPLOIT-005-leq-no-stimulus/source_report.md` (54-55): “Tried 2 rounds of K=5 (10 attempts) and never crossed 0.80.”
- `icloud-work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/system_improvement_brainstorm.md` (39): “Some substandards (KC-1.1.I.* on MCQ_SET) systematically fail; others systematically pass.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md` (62): “Takeaway: K was not producing useful diversity for MCQ_SET in this archive. It produced duplicate payloads. Anti-static guard must treat identical candidates as one candidate, not six chances.”

Against: none found

<sub>method · stage: measure · measurement, generation · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Concrete, checkable instructions

Tell a writer in concrete, checkable terms what the item must make the student do, not in abstract labels such as a taxonomy level or 'be specific'.

After several prompt runs, the AP generator's blueprint concluded that a model interprets abstract instructions differently, that 'be specific' means different things in different contexts, and that every instruction should be checkable (`icloud-work/ap-social-studies-generator/docs/archive/RUN7_BLUEPRINT.md`). Cognitive-level labels in the prompt did not constrain what the model made and were replaced by behavioural constraints (`icloud-work/ap-social-studies-generator/docs/archive/PROMPT_EVOLUTION.md`). The blueprint's rule is to describe the behaviour wanted, not the classification, because the model doesn't reliably map taxonomy levels to behaviours (the same blueprint).

Quoted:

- `icloud-work/ap-social-studies-generator/docs/archive/RUN7_BLUEPRINT.md` (612): “- Every instruction should be checkable”
- `icloud-work/ap-social-studies-generator/docs/archive/RUN7_BLUEPRINT.md` (637): “- Describe the BEHAVIOR you want, not the classification”
- `icloud-work/ap-social-studies-generator/docs/archive/RUN7_BLUEPRINT.md` (607): “- Model interprets abstract instructions differently”
- `icloud-work/ap-social-studies-generator/docs/archive/RUN7_BLUEPRINT.md` (634): “- Model doesn't reliably map taxonomy levels to behaviors”

Against: The evidence compares whole runs that changed several things at once, and the blueprint itself warns that such comparisons can't isolate which change caused a regression (`icloud-work/ap-social-studies-generator/docs/archive/RUN7_BLUEPRINT.md`).

<sub>method · stage: write · generation, demand · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Confirm the change actually fired

Before crediting or blaming a change, confirm in the outputs that it took effect for every item type, since a change that never ran can still show a gain. A claimed gain from a self-checking step was within noise (p=0.7744), and the step had fired in 0 of 297 outputs.

A pressure test of a claimed +1.33-point gain from a self-checking decoding step found it within noise on a paired McNemar test (p=0.7744), and not one of 297 outputs carried the step's signal (`icloud-work/aptraining/.agent/memory/MEMORY.md`). A verification scaffold never triggered on 30 of 30 document-based items in a run that regressed 4.67 points (the same file), and the reported regressions of three training runs came from runs whose weights never moved (`icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/plan.md`). The eval template now asks for a significance check against the baseline (`icloud-work/aptraining/.agent-v2/templates/eval-cycle.md`). Bypasses can skip a change for some item types. Once a change is shown to have run, its gain is checked with a paired test.

Quoted:

- `icloud-work/aptraining/.agent/memory/MEMORY.md` (130): “McNemar p=0.7744 on APUSH (within noise); 0/297 v35 outputs emit any reflection token at decode (Self-RAG mechanism didn't fire).”
- `icloud-work/aptraining/.agent/memory/MEMORY.md` (180): “CoVe scaffold didn't fire at 14B (30/30 DBQ items `cove_stage=no_block`)”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/plan.md` (107): “Across 190 steps and ~5.85M tokens, **DPO extracted zero signal**. The policy never updated.”
- `icloud-work/aptraining/.agent-v2/templates/eval-cycle.md` (50): “Statistical significance check (paired-t or BH-FDR if applicable)”
- `icloud-work/aptraining/helpers/shadow/audits/v35_pressure_test/feedback_v35_within_noise.draft.md` (22): “- All 297 v35 generations under vanilla `oneshot_generate.py`: zero `[Retrieval=...]`, zero `[IsRel=...]`, zero `[IsSup=...]`, zero `[IsUse=...]`, zero `<paragraph>...</paragraph>`.”
- `icloud-work/aptraining/handover/2026-05-01T1039Z_main_session_close/02_CONSOLIDATED_STATE.md` (86): “| **v35 Self-RAG SFT** | 92.26% / 89.33% APUSH on canonical (looked like +1.33pp lift) | **RETRACTED** — McNemar p=0.7744, 0/297 reflection-token emission, mechanism never fired | Self-RAG vocab-extension is non-optional; "lift" was grader noise + threshold artifact |”
- `icloud-work/aptraining/handover/2026-05-01T1039Z_compass_session_close/02_R42_CoVe_DBQ_spec.md` (140): “Log the `stage` (`revise` / `draft_fallback` / `no_block`) per item in the score record so we can quantify how often the verification phase actually fired.”
- `ap-agent-memory/MEMORY.md` (38): “0/297 v35 outputs emit any reflection token at decode (Self-RAG mechanism didn't fire). The +1.33pp lift is noise + grader artifact, NOT a Self-RAG mechanism win.”
- `ap-agent-memory/recipe_v35_self_rag_reproducible.md` (135): “- 0/297 v35 outputs emit ANY reflection token (`[Retrieval=…]`, `[IsRel=…]`, `[IsSup=…]`, `[IsUse=…]`)”
- `home-agent-memory/mcq_set_improvement_log.md` (11): “**Impact**: The Research→Compile pipeline NEVER WORKED for either MCQ or MCQ_SET. Both silently fell back to legacy generation paths every time. The research step was designed to gather verified primary sources and plausible alternatives, but it always crashed before it could run.”
- `aptraining-local/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_live_verdict_20260526.md` (25): “The v80bchain balanced15 result (E 14/15 > A 12/15) was a false signal: v80bchain selects deterministic repair routes (`dbq_source_repaired`, `mcq_set_repaired`) before the duck directives reach the model.”
- `aptraining-local/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_live_verdict_20260526.md` (16): “**Confounded** — both off-limit-routed via `dbq_source_repaired` + `mcq_set_repaired`. Duck directives ignored.”
- `aptraining-local/parallel-ideas-lab/reports/rubber_ducks/typed_recipe_live_verdict_20260526.md` (17): “**Gemini 2.5 Flash (clean prompt path)** | **10/15 (avg 0.875)** | **8/15 (avg 0.783)**”
- `aptraining-local/parallel-ideas-lab/reports/rubber_ducks/BEAD_EVIDENCE_INDEX.md` (61): “Finding: v80b on K=6 still routes DBQ through `dbq_source_repaired` and MCQ_SET through `mcq_set_repaired`.”
- `aptraining-local/parallel-ideas-lab/reports/rubber_ducks/BEAD_EVIDENCE_INDEX.md` (61): “**Duck directives don't reach the model for those cells. Code-port required (pil-6bp.10).**”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md` (2092): “Initial `model_required` env was insufficient because Unit 1 had a hardcoded scored-template bypass before `call_fireworks`.”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (715-717): “and then never landed the rendering: zero references to any of those keys existed in `index.html`, and no patch-log entry was written.”

Against: Two notes disagree on whether the silent fallback was the better path: one leaves the bug in on purpose because the fallback 'produces BETTER MCQ results' (the generator project's agent-memory index, `MEMORY.md`, line 15), while the improvement log has multiple choice going from 96% to 100% once the research step worked, on 10 items (`mcq_set_improvement_log.md`, line 15).

<sub>method · stage: improve · measurement, generation · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Deduplicate on the full content

Deduplicate and count items on their full content, not on an opening prefix or an earlier step's count. Hashing only the first 200 characters wrongly marked 34% of distinct records as duplicates.

A training-set build hashed the first 200 characters of each record, so different records that open alike, such as multiple-choice items with the same question opening, counted as duplicates: it seemed to hold 37k unique records, a 34% false duplicate rate, until full-content hashing found 56,554 in one source file alone (`training_data_70k.md`, lines 30-33). A source pool reported as about 31 candidates per objective held 12-14 unique documents once deduplicated, because the reported count included repeats across rounds (`feedback_cache_pool_count_vs_unique_doc_count_distinct_2026_06_01.md`, lines 7-9).

Quoted:

- `home-agent-memory/training_data_70k.md` (30): “`build_70k_dataset.py` used MD5 hash of first 200 chars of assistant content for dedup. This caused massive FALSE POSITIVES — many different records share the same first 200 chars (e.g., MCQs with the same question opening). Fixed to use **full content MD5 hash**.”
- `home-agent-memory/training_data_70k.md` (32): “**Before fix:** appeared to have only 37k unique records (34% false dedup rate)”
- `ap-helpers-data-agent-memory/feedback_cache_pool_count_vs_unique_doc_count_distinct_2026_06_01.md` (9): “Actual unique-doc pool was 12-14 per KC after dedup, not 31.”
- `icloud-work/ML learnings/training_data_journey.md` (7): “**Bug:** Used MD5 hash of first 200 chars of assistant content for deduplication.”
- `icloud-work/ML learnings/training_data_journey.md` (9-12): “This caused massive FALSE POSITIVES. Many different records share the same opening 200 characters:
- MCQs starting with "Which of the following best describes..."
- LEQs starting with "Evaluate the extent to which..."
- DBQs starting with "Using the documents..."”
- `icloud-work/ML learnings/training_data_journey.md` (14): “Result: Appeared to have only 37k unique records from what should have been 59k+. A 34% false dedup rate made the dataset look much smaller than it was, and caused us to think we needed to generate more data.”
- `icloud-work/ML learnings/training_data_journey.md` (16): “**Fix:** Full content MD5 hash of the entire assistant response.”
- `icloud-work/ML learnings/training_data_journey.md` (17): “**After fix:** 56,554 from raft_combined alone were correctly unique. We didn't need to generate anything.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CORPUS-AND-SAMPLING-CONTRACT.md inside it) (80): “Row identifiers, wrappers, scores, metadata, and difficulty labels do not create a new candidate identity. This prevents repeated packaging or rescoring from inflating the unique count.”

Against: A whole-item hash catches only exact copies; near-duplicates need another test, and the folder has none.

<sub>method · stage: settle · generation, measurement · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Don't build on the model's own output

Don't build a model's examples or training data from its own output; draw them from real material outside it.

An analysis memory for an AP question model's training names self-bootstrap as the corpus problem: its few-shot bank was earlier models' outputs plus their own. It records that the only lift on document-based questions that cost no other item type came from real documents, the only data from outside the chain, and that four dead-end versions shared the flaw.

Quoted:

- `aptraining-local/analyzer/.agent/MEMORY.md` (42): “fewshot_bank = v43soup + v52b + their own outputs.”
- `aptraining-local/analyzer/.agent/MEMORY.md` (42): “The ONLY non-zero-sum lift mechanism on DBQ historically was `d13` (LoC real documents) — the only data outside the chain.”

Against: none found

<sub>method · stage: ground · generation, stimulus · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Don't build on unchecked output

Don't let a later step or model build on generated output, a model's own research included, until it is checked and approved, since its errors carry forward. Trained on the previous model's ungraded items, the next one lost 8.9 points on short answers and 10 on multiple choice.

In a training chain, one model was trained on the previous model's ungraded generations before that model had a verdict; it inherited the earlier model's weaknesses, lost 8.9 points on short answers and 10 on multiple choice, and scored 53.11%, 3.11 points below the model it learned from (`project_v50_v56_strategy_with_numbers_2026_05_12.md`). The project then listed training on ungraded generations as a banned anti-pattern.

Quoted:

- `ap-helpers-data-agent-memory/project_v50_v56_strategy_with_numbers_2026_05_12.md` (83): “v51 was trained on v50's *ungraded* gens before v50 had a verdict. Result: v51 inherited v50's weaknesses + degraded on saq −8.9pp and mcq −10pp.”
- `ap-helpers-data-agent-memory/project_v50_v56_strategy_with_numbers_2026_05_12.md` (17): “| v51 (speculative DPO on v50 ungraded gens) | n/a | **53.11%** (−3.11pp vs v50) | 1.02pp |”
- `ap-helpers-data-agent-memory/project_v50_v56_strategy_with_numbers_2026_05_12.md` (67): “| v51 | v50 ungraded gens (speculative, banned anti-pattern) | DPO | v43-soup | 8192 | already trained — **regressed −3pp** |”
- `ap-helpers-data-agent-memory/project_v50_v56_strategy_with_numbers_2026_05_12.md` (66): “| v50 | curriculum500 (programmatic extract, no D13) | DPO | v43-soup | 8192 | already trained — **regressed** |”
- `icloud-work/ML learnings/mcq_set_journey.md` (24): “- Research step chained stimulus to potentially bad sources (if the research hallucinated a source, the stimulus inherited the hallucination)”
- `icloud-work/ML learnings/mcq_set_journey.md` (44): “1. Research→Compile (single step): 60% — worse than before”
- `icloud-work/ML learnings/mcq_set_journey.md` (46): “3. Stimulus (from scratch, no research)→Questions: 80% — best”
- `icloud-work/ML learnings/mcq_set_journey.md` (48): “**Counter-intuitive finding:** Removing the research step IMPROVED MCQ_SET quality. The research step was a hallucination amplifier, not a quality gate.”
- `icloud-work/ML learnings/mcq_set_journey.md` (36): “- MCQ: 96% → 100% (research step immediately improved factual accuracy)”
- `home-agent-memory/mcq_set_improvement_log.md` (27): “- Problem: stimulus chained to potentially hallucinated research sources”
- `home-agent-memory/mcq_set_improvement_log.md` (26): “- **Result: 60% (6/10)** — same problem”
- `home-agent-memory/mcq_set_improvement_log.md` (31): “- **Result: 80% (8/10)** — best so far”
- `home-agent-memory/mcq_set_improvement_log.md` (55): “2. **Chaining research→stimulus** — constrains stimulus to potentially bad sources”
- `home-agent-memory/mcq_set_improvement_log.md` (15): “**Result for MCQ**: With research actually working, MCQ went from 96% → **100% (10/10, all perfect 1.00 scores)**. The research pipeline provides verified facts that dramatically improve quality.”
- `icloud-work/k_12_social_studies/ap_files/Knowledge Schema Generator - AP USH Unit 1 - Instructions.csv` (40): “20. Run step 11 in main.py which is to generate relationships. This will be the very last step after the KS for the unit has been approved.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (352): “Correct any pronunciation or wording error before timing the edit.”

Against: One run, and the earlier model had itself regressed (same file, line 66), so how much of the loss came from the ungraded data is not separated. for single questions the same note credits the research step with a rise from 96% to 100%, put down to better factual accuracy (`icloud-work/ML learnings/mcq_set_journey.md`). For single questions the same research step, once it actually ran, raised the pass rate from 96% to 100% (10/10), which the log credits to the verified facts it supplies.

<sub>method · stage: improve · generation, evaluation · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Don't trust the generator

Expect to discard much of what a generator writes, keep the trace of what was accepted and rejected, and let the gates, not trust in the generator, carry the quality. Of 299 items another model could answer with the passage, only 113 passed the check that it could not answer them without it.

A retrospective on a Grade 5 generation run says the questions were good because the generator was not trusted: items survived only if a model from another family could solve them with the passage and not without it, and large volumes of plausible-looking output were discarded (`grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd`). In its non-match tranche, 360 items were written, 299 passed the with-text control and 113 were certified blind. The generator's handoff owes an accepted-and-rejected generation trace (`grade3-reading/knowledge_bot/knowledge/kb-0067-g5-generator-pilot-intake-and-team-async-2026-06-23.qmd`), and in the AP work generated candidates stay candidate material that bypasses none of the source, format, factuality, answerability, independence or human review gates (`grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd`).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (26): “The questions were good because the generator was not trusted.”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (36): “- discarding large volumes of plausible-looking output.”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (160): “| with-passage control pass | 299/360 |”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (161): “| Grade 5 blind-certified | 113/299 |”
- `grade3-reading/knowledge_bot/knowledge/kb-0067-g5-generator-pilot-intake-and-team-async-2026-06-23.qmd` (33): “accepted_and_rejected_generation_trace”
- `grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd` (88-89): “None bypasses source identity, current-format, factuality, answerability, independence, or human review gates.”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (217-220): “Quality-B was not run across every final item: - used on the small sequence MODIFY pilot; - not run over the final 700 MATCH or final 167 non-match items.”
- `grade3-reading/ti-courseplans/scripts/lane-tools/theme-demand/README.md` (70-71): “The `certification_yield=0.5` default comes from a historical G5 generation campaign (48.7%, rounded).”
- `grade3-reading/ti-courseplans/scripts/lane-tools/theme-demand/README.md` (64): “to_generate = ceil(to_certify / certification_yield)”
- `grade3-reading/_archive/2026-08-13-consolidation/orientation-sweep-digest/agent-damage.md` (70): “the retrospective's own headline is 'the questions were good because the generator was not trusted'”
- `grade3-reading/artifacts/g5-clean-course-v2/GATE_REPORT.md` (31-32): “Per-type yield through the binding blind gate: sequence 33/975 (3.4%), hot-text 71/1000 (7.1%), match 83/1171 (7.1%).”
- `grade3-reading/course-renderer/authoring/README.md` (194-196): “The pipeline is COMPLETE and LANDS WITH ZERO ACCEPTED CANDIDATES: three full runs against the Aladdin Part 1 lesson each ended in an honest DISCARD on structural gates after the refine budget (manifests in `runs/`).”

Against: Quality review was not run across every final item of that run (`grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd`).

<sub>method · stage: write · generation, evaluation · universal · from g3, ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Exact structure, required fields

Give the writer the item's exact structure and make every field that matters required; without a structure items failed far more often, and fields left optional got left out. With no schema, the pass rate fell to 5% against a 45% baseline.

In the same prompt sweep, raw generation with no schema passed 5% of items against a 45% baseline, at 20 items per variant (`icloud-work/ML learnings/prompt_engineering_deep_dive.md`). One writer filled every schema field, optional ones included, while another often left optional fields out, such as the source attribution, so the anchor-fact field was made required (`icloud-work/ML learnings/week_of_apr_21.md`). Any structural deviation fails an item on specification compliance (`icloud-work/ML learnings/what_is_ap_and_why_it_matters.md`).

Quoted:

- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (62): “| bare | 5% | 50% | No schema, raw generation |”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (57): “| baseline | 45% | 60% | Standard prompt |”
- `icloud-work/ML learnings/week_of_apr_21.md` (135): “Gemini reliably fills all JSON schema fields including optional ones. Fireworks model frequently omits optional fields (e.g., `source_attribution`). Keep required fields minimal; never rely on optional field presence for correctness. The `anchor_fact` field is required in the schema specifically because of this.”
- `icloud-work/ML learnings/what_is_ap_and_why_it_matters.md` (45): “Any structural deviation = automatic fail on `specification_compliance`.”
- `g9/transformer/src/mechanics/util.js` (12): “Reply with JSON only, matching the shape you are given exactly.”
- `g9/transformer/src/mechanics/index.js` (1-2): “A mechanic is one module with seven parts: identity, a writer prompt, normalize (shape), … codeChecks (facts), judge (bounded questions with positive evidence), view (what the student sees; never a key)”
- `g9/transformer/src/mechanics/util.js` (20): “must be a list of exactly”
- `g9/transformer/src/mechanics/util.js` (25): “must be an index from 0 to”
- `g9/transformer/src/mechanics/util.js` (32): “lines that exist in the text”
- `g9/transformer/test/mechanics.test.mjs` (35): “normalize rejects a reply of the wrong shape”
- `g9/transformer/src/transform.js` (63): “the reply could not be used:”
- `g9/transformer/test/transform.test.mjs` (36): “an unusable reply is held with the reason, and no judge means unjudged, never ready”
- `g9/transformer/src/mechanics/util.js` (17): “return v.trim().slice(0, max);”
- `grade3-reading/.claude/skills/lesson-build/SKILL.md` (68-69): “cfu dialogue evidence shape needs {instruction, sentences, correct_index, feedback} (the L6 build shipped 11 defects, several of this class).”

Against: Structure doesn't carry correctness: "The knowledge and content quality within the structure is what differentiates model sizes — not the structural compliance itself" (`icloud-work/ML learnings/research_model_size_vs_data_quality.md`, line 150). In the same sweep factual accuracy moved much less than the pass rate (50% with no schema against 60% at baseline), and structure is a hard fail only for some item types (`icloud-work/ML learnings/evaluation_methodology.md`, lines 44-50).

<sub>method · stage: write · generation, format · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Examples teach form, not facts

Use a few vetted examples to show a writer an item's form, never its facts, since it copies their content and flaws: take them from other topics, stripped to structure.

The AP project's literature review concluded that examples in a prompt work through the format and spread of inputs they show, not by conveying correct facts, so it ruled out few-shot examples as a fix for document-based questions that failed on fabricated content (`icloud-work/auto-memory-backup/research_fewshot_format_not_facts.md`; `icloud-work/aptraining/.agent/memory/MEMORY.md`). Its failure analysis reached the same verdict on tuning: fine-tuning taught structural patterns, not facts (`icloud-work/aptraining/.agent/research/failure_taxonomy.md`). In one later run, examples about one period carried over into items on a much earlier one (`icloud-work/aptraining/.agent/memory/spec_v97_dbq_focused_criterion_grounded_dpo_2026_05_25.md`). Vet every example, and strip examples from other topics down to their structure or leave them out.

Quoted:

- `icloud-work/aptraining/.agent/memory/MEMORY.md` (154): “ICL works via format/distribution; refutes "few-shot fixes DBQ veracity"; lifts mcq_set/saq +3-8pp at K=3 with chat-template-aligned demos.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (314): “Fine-tuning teaches structural patterns, not facts.”
- `icloud-work/aptraining/.agent/memory/spec_v97_dbq_focused_criterion_grounded_dpo_2026_05_25.md` (153): “v80b's factual reliability on synthetic Unit-1 content is the bottleneck (Civil War few-shot transferred to pre-contact KCs in Cheater v6).”
- `icloud-work/auto-memory-backup/research_fewshot_format_not_facts.md` (20): “ICL works because demos show **input distribution + output format**, NOT because they convey correct facts”
- `icloud-work/auto-memory-backup/research_fewshot_format_not_facts.md` (28): “Do NOT inject new factual claims into the model (Park et al. ICLR 2025 confirms: ICL reorganizes representations, doesn't write new knowledge)”
- `icloud-work/auto-memory-backup/research_fewshot_format_not_facts.md` (72): “**Do NOT use few-shot to fix DBQ.**”
- `icloud-work/auto-memory-backup/research_fewshot_format_not_facts.md` (36): “| apush/mcq_set, apwh/mcq_set | Multi-question MCQ_SET shape inconsistency | +3 to +8 pp |”
- `icloud-work/auto-memory-backup/research_fewshot_format_not_facts.md` (12): “medium on magnitude of mcq_set/saq lift (T3 magnitude — no published measurement on AP-history-shaped tasks)”
- `icloud-work/ML learnings/master_strategy_apr24.md` (15): “This is *not* a model size problem. A 14B model has ~28B bits of theoretical capacity — more than all of English Wikipedia. The gap to 70B is 6-8 MMLU points, not an order of magnitude. **The problem is that our training data contained fabricated attributions, and we taught the model exactly the wrong pattern.**”
- `icloud-work/ML learnings/mcq_set_journey.md` (112): “**Why 40% might be the new ceiling:** The training data (raft_combined) itself has fabricated attributions. Some of the 18,768 MCQ_SET records have slightly wrong dates or sources — they just passed InceptBench at the time, which has a 50% flip rate. Training on data that sometimes has wrong attributions = training on signal + noise.”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (73): “The model learned to produce source attributions from training data that had fabricated attributions.”
- `icloud-work/ML learnings/research_model_size_vs_data_quality.md` (108): “| Knowledge distillation (from Gemini) | Teaches format/style | Inherits hallucinations from teacher | Medium — we're already doing this and it's the source of the problem |”
- `icloud-work/ML learnings/failures_and_false_starts.md` (120): “**Result:** 40% pass rate — worse than the 45% baseline.”
- `icloud-work/ML learnings/failures_and_false_starts.md` (122): “**Why:** The few-shot examples gave the model specific historical content (dates, sources, attributions from the examples) that contaminated its generation. The model sometimes referenced elements from the example questions in its generated questions, or the examples biased its style toward those specific historical periods.”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (58): “| fewshot | 40% | 55% | Few-shot examples added |”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (57): “| baseline | 45% | 60% | Standard prompt |”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-013-v6-FAILED.md` (4): “**Fresh Unit-1 single-shot n=25: 8/25 = 32%, avg 0.608**”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-013-v6-FAILED.md` (5): “**vs v4 (no few-shot): 11/23 = 47.8%, avg 0.738** — **−16pp regression**”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-013-v6-FAILED.md` (22-25): “v80b appears to over-anchor on the Civil War example's CONTENT, generating Civil War-style regional comparisons even for Unit-1 (1491-1607) KCs about pre-contact Indigenous societies.”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-013-v6-FAILED.md` (25-28): “Some generated maps had regions like "Union states" or "Reconstruction districts" bleeding into Unit-1 sets where they make no sense — IB judge correctly flagged factual_accuracy fails.”
- `icloud-work/aptraining/workspace/comms/from_cheater/2026-05-25T0938Z_ESCALATE_MCQSET_95_infeasible.md` (99-100): “The Civil War few-shot example LITERALLY transferred its content to unrelated KCs”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-013-v6-FAILED.md` (11-13): “2. Added a structural validator (3 questions, 4 options, varied keys A/C/B, ≥6 bullet labels, relational Q3) with ONE retry on validator failure.”
- `home-agent-memory/sft_v4_prompt_engineering.md` (20): “**Key variant ranking (MCQ, N=20):**”
- `home-agent-memory/sft_v4_prompt_engineering.md` (23): “3. baseline: 45% pass, 60% factual_accuracy”
- `home-agent-memory/sft_v4_prompt_engineering.md` (24): “4. fewshot: 40% pass, 55% — examples don't help”
- `home-agent-memory/sft_v4_prompt_engineering.md` (26): “6. bare (no schema): 5% — model requires format spec”
- `ap-agent-memory/research_fewshot_format_not_facts.md` (20): “- ICL works because demos show **input distribution + output format**, NOT because they convey correct facts”
- `ap-agent-memory/research_fewshot_format_not_facts.md` (76): “*Rethinking the Role of Demonstrations* — EMNLP 2022 (https://aclanthology.org/2022.emnlp-main.759/)”
- `ap-agent-memory/research_fewshot_format_not_facts.md` (12): “medium on magnitude of mcq_set/saq lift (T3 magnitude — no published measurement on AP-history-shaped tasks)”
- `ap-agent-memory/research_fewshot_format_not_facts.md` (36): “| apush/mcq_set, apwh/mcq_set | Multi-question MCQ_SET shape inconsistency | +3 to +8 pp |”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (71): “Local IB correctly failed it for period misalignment and stimulus-only answer leakage.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (74): “- Strip historical substance from few-shot examples so they cannot donate wrong content.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (144): “- Same-unit few-shots can supply real content patterns; cross-unit examples are scrubbed to structure only so Unit 6/8 content cannot contaminate Unit 3.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/UNIT1_TO_ALL_UNITS_TRANSFER_PLAN.md` (60): “- Do not trust high-scoring few-shot/pattern rows blindly.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/UNIT1_TO_ALL_UNITS_TRANSFER_PLAN.md` (64): “- leak the answer through the stem,”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/UNIT1_TO_ALL_UNITS_TRANSFER_PLAN.md` (66): “- use overly broad "best explains" stems with multiple defensible answers.”
- `aptraining-local/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md` (548): “- Primary-source few-shot with long examples: `0/13`; likely overfits to source shape and drifts from the target objective.”
- `aptraining-local/parallel-ideas-lab/experiments/prompt_perfection/runs/fewshot_goldshape_v3_t0.0_p1.0/analysis.md` (3): “Passed: 83/150 (55.33%)”
- `aptraining-local/parallel-ideas-lab/experiments/prompt_perfection/runs/historians_only_v3_t0.0_p1.0/analysis.md` (3): “Passed: 113/150 (75.33%)”
- `aptraining-local/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md` (538): “- Exam-writer few-shot MCQ_SET prompts are the best stable MCQ_SET style so far:”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md` (100): “Few-shot MCQ examples worsened performance by contaminating generations with example-specific historical content.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md` (285): “Few-shots help only when they do not contaminate the historical content.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md` (76): “Keep prompt-kit field names subordinate to original IB schema authority to avoid illustrative examples leaking into output shape.”
- `icloud-work/aptraining/helpers/serve/fewshot_mcqset.py` (5-7): “for MCQ_SET, sample 3-5 verified exemplars (IB-graded 1.0) from the 669-pool, picking exemplars whose KC DIFFERS from the target KC so the output stays fresh, and prepend them as a TEMPLATE SEED.”
- `icloud-work/aptraining/helpers/serve/fewshot_mcqset.py` (7-8): “This lifted IB MCQ_SET 3.3% -> 26.7% and fixed answer_balance 0 -> 30/30.”
- `g9/transformer/src/mechanics/word-web.js` (36): “lesson question: an abstract noun a Grade 9 reader knows or can learn (for example deceit, ambition, loyalty, grief).”
- `g9/transformer/src/mechanics/video-essay.js` (47): “says what the lines show, close to their own words (for example "He serves only to line his own coat"), never an”
- `g9-transformer-runs/blocks/4e79a689a9ff89da.json` (8): “"centre": "arrogance",”

Published: [Min et al. 2022](https://aclanthology.org/2022.emnlp-main.759/) · [Park et al. 2025](https://arxiv.org/abs/2501.00070)

Against: The +3 to +8 point lift the review expected for some item types is a forecast, and its audit note says no published measurement exists on such tasks (`icloud-work/auto-memory-backup/research_fewshot_format_not_facts.md`). The review rests on published studies rather than a test on these items, and the carry-over is a single observation. The same records are called sound elsewhere: "Quality: High. All passing InceptBench or close to it." and "Real primary sources, well-reasoned explanations." (`icloud-work/ML learnings/training_data_journey.md`, lines 26 and 31). The cross-team summary ranks volume first: "More data > better data > architecture tricks." (`icloud-work/ML learnings/cross_team_learnings_full.md`, line 162). No audit of the examples was done (`icloud-work/ML learnings/what_to_do_next.md`, line 65). Each variant ran on 20 items, so the gap is one item in twenty (`icloud-work/ML learnings/prompt_engineering_deep_dive.md`, line 50). Examples of a format are still used to teach structure: a grounding method in the research summary gives "3-5 examples of the desired citation format" (`icloud-work/ML learnings/research_rag_factual_grounding.md`, line 202). A structural validator with one retry and two new constraints came in the same version, so the drop is not the example's alone: "2. Added a structural validator (3 questions, 4 options, varied keys A/C/B, ≥6 bullet labels, relational Q3) with ONE retry on validator failure." (icloud-work/aptraining/Cheater/exploits/EXPLOIT-013-v6-FAILED.md, 11-13) One sweep, where with and without examples differ by one item of 20 (`sft_v4_prompt_engineering.md`, lines 23 and 24). The gain the research note expects from examples on multi-question sets, +3 to +8 points, is a projection, not a measurement (`research_fewshot_format_not_facts.md`, lines 12 and 36). One example-based style was the best stable style for question sets, though only at 4 of 13. The best fresh pipeline still used curated examples: "-> apply satisfaction kit + curated few-shots" (icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md, line 20). Example banks can make output static: in one run document-based items and question sets fell into extreme duplicate groups, which 'can inflate short-slice scores and then collapse on variety/focus' (icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/WEEKLY_APUSH_PIL_REPORT_20260520.md, line 492); and another report found that for dense courses too many prompt examples can hurt, preferring exact facts and source packs (icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md, line 186). A later run found: A lesson engine's prompts for any text carry examples from its first play, such as that play's themes as sample centre words for a word web and a paraphrase of one of its lines as a sample point. On a poem and a speech no draft showed a pull toward them (the poem's web took 'arrogance'), though one run per text cannot rule a pull out (`g9/transformer/src/mechanics/word-web.js`).

<sub>method · stage: write · generation, integrity · universal · from ap, research · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Few facts, matched to the exact topic

Fetch an item's sources and facts by its exact topic or objective, not its unit, and give the writer only the few that match, since other topics' facts blend in. The research summary advises the 10-15 most relevant facts rather than all 3,347.

With facts drawn for the whole unit, the AP question work expected an item on one topic to mix in another topic's facts, or to get no help from them (`icloud-work/ML learnings/knowledge_and_rag_pipeline.md`). Facts were then matched to the item's topic cluster first, which was reported as improving relevance, with no pass-rate figure (`icloud-work/ML learnings/week_of_apr_21.md`). The research summary adds the Lost-in-the-Middle problem, that facts in the middle of a long block are ignored most, and advises giving the 10-15 most relevant facts rather than all 3,347 (`icloud-work/ML learnings/research_rag_factual_grounding.md`).

Quoted:

- `icloud-work/ML learnings/knowledge_and_rag_pipeline.md` (171): “If the question topic was about Progressivism but the injected facts were about immigration, the model might generate a question that mixed both — or the curriculum facts wouldn't help at all.”
- `icloud-work/ML learnings/knowledge_and_rag_pipeline.md` (175): “**Impact:** Cluster-matched facts are more relevant to the specific question being generated. The model has better grounding for the specific topic rather than unit-level context.”
- `icloud-work/ML learnings/research_rag_factual_grounding.md` (404): “**More context injection / longer fact lists:** The Lost-in-the-Middle problem means that making the fact list longer reduces the model's ability to use it. Better to use a retriever (Technique 7) to inject only the 10-15 most relevant facts rather than all 3,347.”
- `icloud-work/ML learnings/research_rag_factual_grounding.md` (34): “- **Context position**: Facts buried in the middle of a long context block are more likely to be ignored than facts at the very beginning or end (Lost-in-the-Middle problem).”
- `icloud-work/ML learnings/week_of_apr_21.md` (23): “Cluster-matched facts (not just unit-level) improved relevance.”
- `icloud-work/ap-social-studies-generator/data/model_findings.md` (407): “1. **Topic mismatch is the root failure cause.** Bank indexed by (course, unit) — 50 entries spanning 30+ years and multiple topics. A "Failure of Reconstruction" request had only 2/50 chance of getting Reconstruction documents.”
- `icloud-work/ap-social-studies-generator/data/model_findings.md` (396): “| DBQ  | 14% (3/22)      | **30% (6/20)**      | +16pp |”
- `icloud-work/ap-social-studies-generator/data/model_findings.md` (421): “**75%** | 0.944 | +45pp ✅ PASS”
- `icloud-work/ap-social-studies-generator/CHANGELOG.md` (151): “We were doing fuzzy topic-based MongoDB search and sometimes getting irrelevant facts.”

Against: The cluster change's effect was never measured: "Cluster-matched facts > unit-level-only improved relevance." (`icloud-work/ML learnings/infrastructure_and_tooling.md`, line 158). The writer was only ever given five facts (`icloud-work/ML learnings/knowledge_and_rag_pipeline.md`, line 208), so the comparison with all 3,347 answers a setup nobody ran. Another note favours more facts in the store, not the prompt: "More facts = better coverage = fewer hallucination opportunities." (`icloud-work/ML learnings/knowledge_and_rag_pipeline.md`, line 228). The 75% rests on 8 items, and the two rates come from runs of different sizes, so the size of the gain is uncertain (`icloud-work/ap-social-studies-generator/data/model_findings.md`).

<sub>method · stage: ground · generation, alignment · universal · from ap, research · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Find the cause in the failing items

Name why items fail from what the judge was given and what it said about the failing items. One analysis blamed a missing field for 62% of failures, though the judge had failed the analysis's own example item for a disallowed option.

One analysis named a missing 'type' field as the cause of 62% of failures and expected '+30-40% pass rate' from adding it, but the type sat only in the request, 'not in the question content being evaluated', in passing items as much as failing ones, and the judge failed the analysis's own example item for including '+' among comparison symbols (`icloud-work/incept/nova_forge/PASS_RATE_ANALYSIS.md`, `icloud-work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md`). The opposite slip happened too: fill-in and multiple-select items passed at 0% while the answer extractor read only one field name, so the judge saw empty keys, one of them beside an explanation naming B and C, yet the fill-in 0% was put down to missing examples (`icloud-work/incept/nova_forge/archive/old_docs/platform/ITD_ENHANCED_FEW_SHOT.md`, `icloud-work/incept/nova_forge/archive/old_docs/platform/PATTERN_ANALYSIS_RESULTS.md`). A field the failures share need not be the cause, and an empty or misread field scores like a bad item.

Quoted:

- `icloud-work/incept/nova_forge/PASS_RATE_ANALYSIS.md` (38): “### CRITICAL ISSUE #1: Missing 'type' Field (62% of failures)”
- `icloud-work/incept/nova_forge/PASS_RATE_ANALYSIS.md` (43): “- All questions with 0.00 spec compliance score are missing `content.type`”
- `icloud-work/incept/nova_forge/PASS_RATE_ANALYSIS.md` (44): “- Type is only in `request.type`, not in the question content being evaluated”
- `icloud-work/incept/nova_forge/PASS_RATE_ANALYSIS.md` (45): “- Example from failed question cc-math-4-mcq-easy-6:”
- `icloud-work/incept/nova_forge/PASS_RATE_ANALYSIS.md` (67): “**Expected Impact:** +30-40% pass rate (fixes 108 spec compliance failures)”
- `icloud-work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md` (293): “- Issue: Violates the boundary to use only >, <, and = by including "+" as an option.”
- `icloud-work/incept/nova_forge/archive/old_docs/platform/ITD_ENHANCED_FEW_SHOT.md` (46): “1. **Targeted Learning:** Fill-in questions were 0% pass rate because model had no fill-in examples”
- `icloud-work/incept/nova_forge/archive/old_docs/platform/ITD_ENHANCED_FEW_SHOT.md` (126): “1. **Bug Found:** Fill-in answers were empty because code only looked for `correct_answer`”
- `icloud-work/incept/nova_forge/archive/old_docs/platform/ITD_ENHANCED_FEW_SHOT.md` (130): “- MSQ uses `"correct_answers": ["B", "C"]`”
- `icloud-work/incept/nova_forge/archive/old_docs/platform/ITD_ENHANCED_FEW_SHOT.md` (137): “"answer": result.get("correct_answer", "")”
- `icloud-work/incept/nova_forge/archive/old_docs/platform/PATTERN_ANALYSIS_RESULTS.md` (154): “Answer field is [""] but explanation states correct choices are B and C”

Against: Neither diagnosis was isolated. The field fix was recorded as a success, '| Type Field Present | 38% | 100% | +62% |' (`icloud-work/incept/nova_forge/README.md`, line 228), but a later 298-item run that reached '- **Pass Rate:** 55.4%' mixed original, corrected and regenerated items (`icloud-work/incept/nova_forge/RUN_LOG.md`, lines 34-35), and the extractor fix and the new examples were deployed together (`icloud-work/incept/nova_forge/archive/old_docs/platform/ITD_ENHANCED_FEW_SHOT.md`, lines 491 and 493).

<sub>method · stage: improve · evaluation, generation · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Fix the examples before retraining

When a writer falls short, fix its examples before retraining it: format examples in its prompt, and training examples picked on the quality you want, not a proxy score. In an earlier Advanced Placement question-writing effort, 68 preference pairs picked on the quality wanted gained 9.7 points where two retraining runs both regressed.

The reading project's plan for improving its question writer carries over two results from an earlier AP question-writing effort (`grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md`). Few-shot examples fixed the answer balance of that effort's multi-question sets with no retraining, +23 points, so the plan tries examples of each format in the prompt before fine-tuning. The same format's wall was mislabelled preference data, pairs picked on a proxy judge's score and never checked on the educational accuracy wanted, and fixing the labels beat two warm-start retrains, which both regressed; the effort's summary records 68 pairs rebuilt on that axis lifting the format from 0.194 to 0.292, +9.7 points with no regression (`grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd`). The plan therefore builds its own training data on the qualities that bind it, items that need the text and transfer to new texts, as confirmed by a judge from a different model family, not on the proxy score (the first file).

Quoted:

- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md` (88): “Mirrors aptraining [F5]: **few-shot exemplars fixed MCQ_SET answer-balance with NO retrain (+23pp)** — try in-context format exemplars before reaching for SFT.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md` (94): “aptraining's MCQ_SET wall was a **mislabeled-preference-data** problem (pairs picked on the IB axis, never verified on the true `educational_accuracy` axis) [M3/M8] — fixing the *data labels* beat 2 SFT warm-starts (both regressed, [M6]).”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md` (94): “For us the binding axes are **anti-leak / cold-transfer**; build the preference/SFT data on *those* axes, verified by the different-family judge, not on the IB score.”
- `grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd` (37-38): “the **v97 clean-eduacc-axis DPO** (68 pairs, mcq_set 0.194→0.292, **+9.7pp**, no regression)”
- `grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd` (51): “**MCQ + MCQ_SET still FAIL the raw floor at 0.292** (+0.41 each to go)”
- `grade3-reading/ti-courseplans/courses/g5-reading/llm/GENERATOR_DIRECTIVE.md` (44): “a weak checkpoint comes from a **leaky corpus**, not bad hyperparameters.”

Against: Both results are second-hand: the AP effort's own summary does not repeat the 23-point figure, and after relabelling the format still failed its floor at 0.292 (`grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd`).

<sub>method · stage: improve · generation, evaluation · universal · from ap, g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Fix the key, then explain it

Fix an item's structure and answer key first, write its explanations against that fixed key, then check every explanation, hint and feedback line against the actual options and key.

A distilled report on one AP generator calls two-stage generation its load-bearing pattern: the structure and key are fixed first and the explanations written against them, which keeps an explanation from contradicting the key (`k_12_social_studies_distilled.md`, lines 44 and 73). Generating multiple-answer items in one stage gave bad answer counts until two-stage generation plus validation fixed it (line 64). The AP evaluator's rubric fails an item whose explanations, hints or feedback describe options or values that are not there, and its first checklist asks whether explanations match the key and options (`mcq_evaluation.txt`, line 85; `_base_evaluation.txt`, line 66). That generator's headline scores were graded by the model family that wrote the items (line 10 of the same report), so this is design evidence, not a measured lift.

Quoted:

- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/k_12_social_studies_distilled.md` (44): “- This prevents the model from generating an explanation that contradicts the answer key.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/k_12_social_studies_distilled.md` (73): “- Use two-stage generation for answer-bearing item types: lock structure/key first, generate explanations second.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/k_12_social_studies_distilled.md` (64): “- Single-stage MSQ produced bad answer-count behavior; the fix was two-stage MSQ plus validation.”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_evaluation.txt` (85): “- **FIELD MISMATCH**: Explanations, hints, feedback templates, or `additional_details` describe distractors, answers, or values that do NOT match the actual options or correct answer”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt` (66): “- Do explanations/rationales match the correct answer and options?”

Against: The pattern was proven only for some item types: "Match/fill-in/article were less proven and flagged for more validation" (`k_12_social_studies_distilled.md`, line 49).

<sub>method · stage: write · key, feedback, generation · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Fix the picking or the writing

When a pipeline that picks among drafts fails, check whether any draft passed: if one did, fix the picking; if none did, fix how drafts are written. Fixing the routing rescued 9 of 11 failures where a passing item existed and 0 of 4 where none did.

Of one run's 159 failures, 114 were for objectives where a passing item already sat in the bank of past winners and 45 for objectives with none (`LAB_PIPELINE_GUIDE.md`). A fallback that fixed the routing rescued 9 of 11 of the first kind and 0 of 4 of the second. The lab's rule is that if a passing candidate exists but was not selected, fix retrieval or the selector, and if none exists, fix generation or data; elsewhere, new guards caught the previous leaks but the writer filled the gap with new failure modes, so more generic guards were judged likely to chase symptoms. More checks cannot rescue a pipeline in which no draft passes, since checks can only reject.

Quoted:

- `aptraining-local/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md` (109): “If a passing candidate exists but was not selected, fix retrieval/selector; if none exists, fix generation/data.”
- `aptraining-local/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md` (97): “- **bank_miss = 114 rows (71.7% of all failures)**: substandard IS in parent's `unit1_live_winner_bank.json` but live still failed.”
- `aptraining-local/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md` (98): “- **bank_gap = 45 rows (28.3%)**: substandard NOT in bank.”
- `aptraining-local/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md` (106): “- bank_miss rescue rate **9/11 = 81.8%**”
- `aptraining-local/parallel-ideas-lab/variant-calibration-lab/LAB_PIPELINE_GUIDE.md` (107): “- bank_gap rescue rate **0/4 = 0%** (confirmed: parent's fallback can't help; lab mining needed)”
- `aptraining-local/parallel-ideas-lab/reports/LLM_FINAL_ROUTE_STATUS_20260522T185623Z.md` (179): “The new guards caught the previous leaks, but the LLM filled the gap with new failure modes. More generic guard stacking is likely to chase symptoms.”

Against: The rescue counts are small, 11 and 4 items.

<sub>method · stage: improve · generation, evaluation · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Fix the source, not only the copy

Put every fix into the generator or specification that made the content, not only into the stored items, because regeneration undoes fixes made only to the output.

In a Grade 3 reading course, a generator's output was copied by hand into the shipped lessons, with no script or manifest linking the two, so no build step could report a drift between them (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md`, §D). A rule fixed in the generator prompt did not reach lessons already on disk, and a fix applied on disk did not survive the next regeneration, which has happened, so the course now gives every adopted rule both homes. Its content-integrity skill treats upstream generation specifications as content: a rendered lesson that quietly fixes a bad specification does not close the defect, because regeneration can bring it back (`grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md`). A defect repeated across a batch is the generator's, not a set of separate item faults.

Quoted:

- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (390): “**The generator and the shipped lesson are not coupled by anything.**”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (392-393): “A rule fixed in the generator prompt does not reach any lesson already on disk, and a fix applied on disk does not survive the next regen”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (394-395): “So every adopted rule needs BOTH homes, and a verdict that names only one of them is half a fix.”
- `grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md` (44): “Upstream generation specifications are active content authorities.”
- `grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md` (45-46): “A rendered lesson that silently fixes a bad specification does not close the upstream defect because regeneration can reintroduce it.”
- `ti-courseplans-audit/docs/course-formula-agents.md` (218): “systematic defect patterns (same defect class across a whole batch = generator prompt bug, not per-item fixes).”
- `grade3-reading/ti-courseplans/docs/course-formula-agents.md` (218): “systematic defect patterns (same defect class across a whole batch = generator prompt bug, not per-item fixes)”
- `grade3-reading/ti-courseplans/docs/course-formula-agents.md` (217): “**Catches (the canonical four):** factual errors; teleological claims ("the hoverfly *wants* to be mistaken"); absent passage quotations; multiple defensible answers.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-qc-evidence-v0.1.md` (213-214): “Every rule below was **added or tightened in response to an observed failure**, so the same mistake cannot recur silently at scale.”
- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L6-2026-09-05.md` (131-132): “if L6's vocab node were rebuilt on the newer schema, the density gap in §2 would close on its own.”
- `grade3-reading/.claude/skills/art-qa/SKILL.md` (91-94): “Every FAIL: fix the MANIFEST first … The wrap failure was a cast/scene contradiction — the manifest was the bug, not the model.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (480-481): “that instruction must be corrected once this function changes, or it will re-propagate the bug on the next port.”
- `grade3-reading/artifacts/g5-deploy/EVALUATION-API.md` (117-118): “Port the CURRENT `evaluate_locally` behavior, not a simplified keyword-overlap tally”

Against: none found

<sub>method · stage: improve · generation, review · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Generate the baseline afresh

When comparing continuous scores, test a new way of generating against a freshly generated baseline, not stored outputs re-scored, because generation varies between runs even at temperature zero. The same generator on the same 150 prompts averaged 0.9475 on stored outputs and 0.9307 on fresh ones.

At temperature 0, the same generator on the same 150 prompts, each set scored three times, averaged 0.9475 on stored outputs and 0.9307 on fresh ones, 1.68 points apart, with short answers moving most (`feedback_baseline_must_be_fresh_gen.md`, lines 3, 12, 24). Compared with a fresh baseline instead of the stored one, two of four configurations that had been reported as regressions were gains (lines 34-39).

Quoted:

- `ap-agent-memory/feedback_baseline_must_be_fresh_gen.md` (3): “v29 fresh-gen 3-run continuous = 0.9307; v29 frozen-gen 3-run continuous = 0.9475. Δ 1.68 cont-pp from inference variance (temp=0 not deterministic across gen runs).”
- `ap-agent-memory/feedback_baseline_must_be_fresh_gen.md` (17): “**For any continuous-metric model A vs model B comparison, both A and B must use FRESH generations. Don't compare test configs (fresh gens) against frozen baseline (re-scored).**”
- `ap-agent-memory/feedback_baseline_must_be_fresh_gen.md` (37): “| field-routed RAG | -0.69 cont-pp | **+0.99 cont-pp** | ✓ REAL LIFT |”
- `ap-agent-memory/feedback_baseline_must_be_fresh_gen.md` (39): “| v36b | -0.88 cont-pp | **+0.80 cont-pp** | ✓ REAL LIFT |”

Against: For the pass rate alone a stored baseline is fine, since the pass mark absorbs small shifts (`feedback_baseline_must_be_fresh_gen.md`, line 47). The gap rests on one fresh and one stored generation, each scored three times; how much fresh runs differ from one another is not shown.

<sub>method · stage: measure · measurement, generation · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Judge a writing aid by its items

Judge a writing aid, such as a specification or prompt, by the items it leads to, against a no-aid baseline on the same requests, not by how it reads.

Two ways of producing generation contracts, a fine-tuned small model and a deterministic compiler, were set up as a bake-off whose winner is whichever improves the downstream pass rate, retries, cost and failure mix on the same benchmark requests fed to the same generator, not whichever contract sounds better (`icloud-work/evaluatorML/.agent/memory/deterministic_compiler/parallel_experiment_note.md`). It uses identical requests and generator settings and a no-helper baseline, and its rule is that the compiler wins by measured downstream outcomes (`icloud-work/evaluatorML/.agent/memory/deterministic_compiler/README.md`).

Quoted:

- `icloud-work/evaluatorML/.agent/memory/deterministic_compiler/parallel_experiment_note.md` (26): “The winner is not whichever contract sounds better. The winner is whichever path improves downstream InceptBench pass rate, retry count, cost, and failure distribution when feeding the same APUSH/APWH/APEuro benchmark requests into the same generator.”
- `icloud-work/evaluatorML/.agent/memory/deterministic_compiler/README.md` (29): “Use identical benchmark rows and generator settings:”
- `icloud-work/evaluatorML/.agent/memory/deterministic_compiler/README.md` (31): “1. No helper baseline.”
- `icloud-work/evaluatorML/.agent/memory/deterministic_compiler/README.md` (46): “The deterministic compiler wins by measured downstream outcomes, not by sounding clever.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/skill/SKILL.md` (31): “quality-check-evaluatable item bank without further interpretation. A proposal”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/skill/SKILL.md` (32): “fails if it requires guessing, overclaims MAP equivalence, or violates a hard”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/skill/SKILL.md` (238): “outscores a long, overclaiming one. Judge on substance, not word count.”

Against: At planning time the comparison had not run, and no result was found: '- No no-compiler baseline or compiler A/B harness has run.' (`icloud-work/evaluatorML/.agent/memory/plans/2026-05-25-ib-pattern-compiler-prelaunch-revision.md`, line 61).

<sub>method · stage: measure · generation, measurement · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Judge the artifact, not the writer

Check every generated item independently, since a writer's score on teaching questions, its grasp of a pedagogy and its own report of compliance are no evidence of what it makes. A model that scored 96.52% on a pedagogy benchmark was published with the caution that this is not evidence of effective tutoring.

The reading project's comprehension doctrine deliberately rejects two kinds of evidence about generated lessons: pedagogy-benchmark scores, which measure knowing that rather than generating content that embodies it, and a model's unaudited assessment of its own content (`grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd`). Its experiment intake lets a model assist extraction but never certify its own atom, and counts a model's self-reported compliance as no evidence (`grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd`); its feedback routing says no lane can self-certify the whole course (`grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd`). A published model tuned for pedagogy reached 96.52% on a pedagogical-knowledge benchmark, and the paper itself says such performance is not evidence of effective classroom tutoring (`grade3-reading/knowledge_bot/knowledge/kb-0124-eduqwen-pedagogical-llm-paper.qmd`). The independent check should come from a different model family than the writer.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd` (255): “A model may assist extraction but may not certify its own atom.”
- `grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd` (465): “Model self-reported compliance is not evidence; measure agreement before adjudication.”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (26): “unaudited LLM self-assessment of its own content (empirically worthless — see DOK1-11)”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (26): “pedagogy-benchmark scores as evidence of teaching ability (measures knowing-that, not generating-aligned)”
- `grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` (157-158): “no lane can self-certify the whole course.”
- `grade3-reading/knowledge_bot/knowledge/kb-0124-eduqwen-pedagogical-llm-paper.qmd` (94-95): “strong benchmark performance on pedagogical knowledge questions does not itself constitute evidence of effective classroom tutoring”
- `grade3-reading/knowledge_bot/knowledge/kb-0124-eduqwen-pedagogical-llm-paper.qmd` (12): “reaches 96.52% on the Cross-Domain Pedagogical Knowledge (CDPK) benchmark”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (46): “Knowing-that (answering pedagogy questions) and generating-aligned (producing content that embodies the pedagogy) are different capabilities”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (46): “the gap is invisible to benchmarks and only measurable at the artifact level”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (34): “a dose that "knew" gradual release still leaked its item's answer”
- `grade3-reading/knowledge_bot/knowledge/kb-0124-eduqwen-pedagogical-llm-paper.qmd` (87-89): “RL shifted behavior "toward guided-learning-like response patterns… rather than direct answer provision"”
- `grade3-reading/knowledge_bot/knowledge/kb-0125-coe-catchup-2026-07-13.qmd` (92-93): “training an LLM specifically on the team's pedagogical principles rather than only using it to generate content”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (126-127): “left downstream transfer as an experiment”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (23): “Generation systematically betrays declared pedagogy — \~78% of raw generated reading items were answerable without the passage, correct answers sat at position A 79% of the time, and a dose that "knew" gradual release still leaked its item's answer — and design-time contracts alone demonstrably failed to prevent any of it.”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (35): “Knowing-that (answering pedagogy questions) and generating-aligned (producing content that embodies the pedagogy) are different capabilities; the gap is invisible to benchmarks and only measurable at the artifact level.”
- `grade3-reading/knowledge_bot/ROUTER.md` (65): “REJECTS pedagogy-benchmark scores as teaching evidence.”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (256-257): “filed with its own caveat that benchmark PCK ≠ teaching ability”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (2): “Our own synthesis (paraphrase-level cites), NOT external evidence — not quote-gated.”
- `ti-courseplans-audit/docs/teaching-reading-comprehension-brainlift.md` (79-81): “Knowing-that (answering pedagogy questions) and generating-aligned (producing content that embodies the pedagogy) are different capabilities; the gap must be measured at the artifact level rather than inferred from benchmark scores.”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (304-305): “knowing-that != generating-aligned (kb-0121 SPOV2, kb-0124 EduQwen authors' own limitation)”
- `ti-courseplans-audit/docs/train-teacher-requirements.md` (19-20): “a generator can "know" gradual release and still emit answer-reveals.”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (26): “The questions were good because the generator was not trusted.”
- `grade3-reading/knowledge_bot/knowledge/kb-0090-fable5-plan-traces-2026-07-09.qmd` (129-131): “- do not trust LLM self-report; - only gate outputs and read-back artifacts count; - a lane cannot certify its own items;”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (231): “3. Use a different family for the gate than for the author. Never same-family certify.”
- `grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd` (106-108): “The binding gate must stay **cross-family** (solver family != generator family); IB self-certification is not anti-leak evidence.”
- `grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md` (78-79): “A model's pedagogical knowledge does not survive the trip into its generated content.”
- `grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md` (80-81): “the gap must be measured at the artifact level rather than inferred from benchmark scores.”
- `grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md` (11-12): “Does training on pedagogical principles produce a model that GENERATES aligned lessons -- not merely one that answers pedagogy questions?”
- `grade3-reading/bias_experiment/experiment-record/evidence/knowledgebot/kb-0131-pedagogy-decision-bank-experiment-intake.qmd` (545-546): “knowing pedagogy does not prove generated content embodies it. This is why JSON validity and question accuracy cannot be the headline.”
- `grade3-reading/bias_experiment/experiment-record/evidence/knowledgebot/kb-0131-pedagogy-decision-bank-experiment-intake.qmd` (465): “Model self-reported compliance is not evidence; measure agreement before adjudication.”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/QUESTION_CONVERSION_RETROSPECTIVE.qmd inside it) (121): “- treating "model says it is fixed" as evidence.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-qc-evidence-v0.1.md` (312-313): “beats were paraphrased instead of copied verbatim from the catalog, and the self-red-team log had **falsely claimed "verbatim."**”

Published: [Application-driven pedagogical knowledge optimization of open-source LLMs via reinforcement learning and supervised fine-tuning, Frontiers in Artificial Intelligence 2026](https://doi.org/10.3389/frai.2026.1851993)

Against: The doctrine's 'empirically worthless' points to a leak rate in raw generated items, not to a study of self-assessment (`grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd`). the same paper reports that its training moved the model toward guided-learning responses rather than giving answers, a project plan proposes training a model on its own teaching principles, and whether that reaches generated material was left as an experiment. This is the project's own synthesis, which marks itself as paraphrase-level and not quote-checked, so the 78% and 79% are summaries of its measurements, not the measurements themselves (`grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd`). judging with three model families was proposed but not approved, and no evidence was presented that it reduces evaluator flakiness (`grade3-reading/knowledge_bot/knowledge/kb-0127-incept-service-coe-catchup-2026-07-14.qmd`, lines 85-86).

<sub>method · stage: judge · evaluation, generation, integrity · universal · from g3, research · adopted-rule · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Keep cold test topics out of prompts

Keep a ledger of the topics reserved for cold transfer tests, block any generation prompt or exemplar that names one, and retire each topic once it is served.

A reading project's practice-layer specification keeps a cold benchmark that is sealed, drawn from never-taught topics and burned once served, and requires a ledger that keeps those topics out of every generation prompt. The tool built for it runs against every generation prompt and exemplar set before a campaign starts; any hit blocks the campaign until the prompt is scrubbed or the ledger corrected, and a topic is retired once a cold window has served it. A Grade 5 course's generation contract gives the reason: teaching from or gating on the cold pool contaminates the benchmark and turns transfer evidence into rehearsal evidence.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/tmp-g5-r8-src-scripts.tar.gz` (scripts/lane-tools/contamination-ledger/README.md inside it) (25-27): “Run this tool against **every generation prompt and exemplar set BEFORE a campaign starts**. Any hit blocks the campaign until the prompt is scrubbed or the ledger is corrected.”
- `grade3-reading/_archive/2026-08-13-consolidation/tmp-g5-r8-src-scripts.tar.gz` (scripts/lane-tools/contamination-ledger/README.md inside it) (7-9): “Supporting clauses: section 2/P5 (cold benchmark = sealed, never-taught topics, burn-after-serve) and section 4 (cold passages are never teaching material).”
- `grade3-reading/_archive/2026-08-13-consolidation/tmp-g5-r8-src-scripts.tar.gz` (scripts/lane-tools/contamination-ledger/README.md inside it) (47): “after a cold window serves a topic, retire it (burn-after-serve)”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (593): “### G5-POL-PRA-009: Keep cold passages out of teaching and mastery gates, draw them from never-taught topics, and treat their results only as a transfer read.”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (596): “- **Rationale:** Teaching from or gating on the cold pool contaminates the benchmark and turns transfer evidence into rehearsal evidence.”
- `grade3-reading/ti-courseplans/scripts/lane-tools/contamination-ledger/README.md` (7-9): “Supporting clauses: section 2/P5 (cold benchmark = sealed, never-taught topics, burn-after-serve) and section 4 (cold passages are never teaching material).”
- `grade3-reading/ti-courseplans/scripts/lane-tools/contamination-ledger/README.md` (25-26): “Run this tool against **every generation prompt and exemplar set BEFORE a campaign starts**. Any hit blocks the campaign until the prompt is scrubbed”
- `grade3-reading/ti-courseplans/scripts/lane-tools/contamination-ledger/README.md` (47): “after a cold window serves a topic, retire it (burn-after-serve)”
- `grade3-reading/ti-courseplans/scripts/lane-tools/contamination-ledger/README.md` (73-74): “The tool matches names and aliases only; a prompt about "coastal rock basins" would evade a "tide pools" entry.”

Against: The tool matches names and aliases only, so a prompt about "coastal rock basins" would evade a "tide pools" entry; its seeded topics are placeholders; and a retired topic stops gating, a choice the specification leaves open (`grade3-reading/ti-courseplans/scripts/lane-tools/contamination-ledger/README.md`, lines 64-77).

<sub>method · stage: ground · integrity, generation, measurement · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Keep the writer and the judge apart

Keep the writer and the judge apart: void any item whose student-facing text addresses the judge, and show the writer plain editorial notes, never the judge's scores or raw output.

The external judge runs an integrity check first, fails items carrying score claims, rubric self-advocacy or instructions to the evaluator, and sets every metric to zero when an item fails it (`icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md`). The pipeline's writer contract carries no scoring labels, weights or judge-facing terms, and its repair step turns the judge's reasoning and suggested improvements into content-review notes, dropping sentences with judge words, so that the writer never sees the judge's names, scores, metric labels or raw output (`icloud-work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py`). It is the item-side counterpart of asking whether a student's words are aimed at the marker. Text that addresses the judge includes an answer key or grading note written into the item.

Quoted:

- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md` (24): “- Integrity check runs first. Never include evaluator-facing score claims, rubric self-advocacy, or instructions to the evaluator.”
- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md` (110): “- Integrity failure overrides all metrics to zero.”
- `icloud-work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py` (399): “"""Generator-safe contract: no scoring labels, weights, or judge-facing terms."""”
- `icloud-work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py` (267-268): “The generator must never see evaluator names, scores, metric labels, or raw judge JSON. It only receives ordinary editorial/historical repair notes.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (266): “Evaluation voided: integrity_check failed. The content contains embedded evaluation/score data and score-steering instructions.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (266): “**This is a prompt-injection style failure where the model has emitted an answer key + scoring guidance INSIDE the question content.**”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (448): “Recommended: scrub the training set for any stimulus containing strings like `"score:"`, `"rationale:"`, `"part_1_*"` regex match.”
- `icloud-work/aptraining/.agent/MEMORY.md` (113): “**Scrub training data of prompt-injection-style stimuli** — F1 found ~14 MCQ_SET records with embedded scoring directives in `stimulus`.”
- `grade3-reading/.claude/skills/arc-audit/SKILL.md` (23-24): “Agents NEVER modify content.”

Against: No run compares repairs given these notes with repairs given the raw verdicts or no notes. The note cleaner also drops more than it means to: its sentence split escapes the whitespace class twice and so never splits ordinary text, and a note with any banned word in it, even pass inside passage, is dropped whole (`icloud-work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py`, `sanitize_review_note`). Some integrity voids were the judge's own bug ('Known IB v2.4 bug.' and 'Empty stems trigger InceptBench integrity_check false positive', `icloud-work/aptraining/.agent/research/inference_clean.md`, lines 50 and 64). The 14 records were stored items in a training bundle, and the action taken was a scrub of that data, not a live check on new items.

<sub>method · stage: write · integrity, generation, evaluation · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Let the model point; copy in code

When a model splits material, have it mark each part's start and end and cut the original in code: asked to copy, it rewrites pictures, tables and diagrams as words. Asked to copy, the splitter turned an inline image into a text description, and the judge then scored the stimulus 0.0.

The evaluator's splitter, asked to extract the verbatim text of each part, routinely paraphrased rich stimuli: an inline image became '[Image: ...]', SVG blocks became descriptions and a table a bulleted list, so the judge's programmatic stimulus check found no image and scored the stimulus 0.0 although the source had one (`icloud-work/inceptbench-main/src/inceptbench/decomposer/anchor_slicer.py`). From 2.6.3 the splitter returns short verbatim start and end anchors instead, and code slices the original between them; the module is absent from 2.5.3 (`icloud-work/inceptbench-latest/src/inceptbench/decomposer/anchor_slicer.py`).

Quoted:

- `icloud-work/inceptbench-main/src/inceptbench/decomposer/anchor_slicer.py` (6-9): “When the decomposer LLM is asked to "extract verbatim text" of a child node, it routinely paraphrases rich stimuli — `<img src="...">` becomes "[Image: ...]", `<svg>` blocks become text descriptions, `<table>` becomes a bulleted list.”
- `icloud-work/inceptbench-main/src/inceptbench/decomposer/anchor_slicer.py` (9-11): “The downstream evaluator then runs a programmatic stimulus check on the paraphrased text, finds no real image, and scores `stimulus_quality = 0.0` even though the source had the image inline.”
- `icloud-work/inceptbench-main/src/inceptbench/decomposer/anchor_slicer.py` (15-16): “The decomposer LLM returns short verbatim `start_anchor` / `end_anchor` substrings instead. This module slices the ORIGINAL source buffer between”

Against: When the anchors don't match, the caller falls back to the model's free-text extraction (`icloud-work/inceptbench-main/src/inceptbench/decomposer/anchor_slicer.py`, lines 27-28).

<sub>method · stage: write · generation, stimulus · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Look up every named fact's scope

Check every named fact in generated content against the unit, period and standard it must stay within with a lookup, since prompt warnings reduce out-of-scope facts but don't remove them. A prompt block listing date traps cut out-of-period examples by about 30-50%, but did not remove them.

A guide to passing the judge names a real but out-of-period example as the writer's most common failure across item types, and says a prompt block listing the common date traps reduces it by ~30-50% without eliminating it. On one topic the writer kept inserting such an event despite the chronology guardrail and never got above 0.78 in 22 tries. An adversarial report proposes a deterministic curriculum lookup that flags any named statute outside the period. Checking a named fact for truth alone is not enough: in one course's knowledge-schema tracker, a fact was removed as out of the course's time frame, significant events lost their mapping to a specific standard because they fit only the overall learning objective, and a true sentence was faulted for missing the heart of its topic.

Quoted:

- `icloud-work/aptraining/Cheater/from_cheater/SINGLE_IB_GRADE_SURVIVAL_GUIDE.md` (60-61): “v80b's most common failure across cells is inserting a real but out-of-period example”
- `icloud-work/aptraining/Cheater/from_cheater/SINGLE_IB_GRADE_SURVIVAL_GUIDE.md` (62-64): “An explicit "high-risk pitfalls" block in the prompt that enumerates the common date-traps reduces this by ~30-50%. Doesn't eliminate it.”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-008-dbq-7doc-generic-attrib.md` (62-63): “Tried K=22 total across v3/v4/v5/v6 and never converged above 0.78.”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-008-dbq-7doc-generic-attrib.md` (64-65): “v80b keeps inserting a date-pitfall event despite the chronology guardrail.”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-004-saq-no-stimulus.md` (129-131): “A deterministic curriculum-API lookup that flags any named statute outside the period would catch the rest.”
- `downloads/AP US History - Knowledge Schema - SME Tracker.xlsx` (sheet 'Unit 1 Nodes', row 10, column M (Comment/Reason); column N reads 'Removed'): “Out of time frame for this course”
- `downloads/AP US History - Knowledge Schema - SME Tracker.xlsx` (sheet 'Unit 9 Nodes', rows 109-112, column M; column N reads 'Removed standard mapping'): “Tricky, because these are significant events but they align with the overall learning objective rather than a specific standard”
- `downloads/AP US History - Knowledge Schema - SME Tracker.xlsx` (sheet 'Unit 6 Nodes', row 202, column M): “This sentence is true but does not get to the heart of the divisions that occurred in the gilded age.”

Against: None found. The lookup is proposed, not tested, and the ~30-50% cut is the guide's own estimate. The tally comes from keywords in free-text comments, not a coded field, so the categories overlap and placement leads repeats only narrowly. The comments cluster in three units (44, 31 and 44), so the mix reflects a few people's habits.

<sub>method · stage: settle · alignment, evaluation, generation · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Measure a generator on one try

Measure and headline a generator on one attempt per input fixed in advance, per item type, in the mode that ships, on untuned topics, reporting retried or best-of-several rates apart. An AP generator's headline 99% came from keeping the best of several tries at build time and serving from cache, not from the model generating.

An AP course's evaluation contract freezes raw generator quality as one candidate and one attempt, with no retry, reranking, repair, cache substitution, rejection sampling, best-of-N or hidden human selection, fixed at 100 preregistered records per family with no early success or denominator top-up, and keeps served-bank and cache evidence in a separate lane. An earlier AP generator's headline 99% had proved to be a build-time best-of-N and serve-from-cache exploit, which its own scoreboard said was not the model generating. Rates after retrying, reranking, filtering or keeping the best of several tries are each reported apart from the first-attempt rate. A Grade 5 reading course's intake standard gates on first-attempt passes per item type with template copies removed, because a total of 8,937 passes had counted re-samples and template copies, one template stamped about 1,475 times (`grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/generator-output-spec.md`, lines 30-38).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd` (58-60): “Raw generator quality is `raw_k1`: one candidate, one attempt, no retry, reranking, repair, cache substitution, rejection sampling, best-of-N, or hidden human selection.”
- `grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd` (60-62): “Raw acceptance is fixed at 100 preregistered records per family, with no early success or denominator top-up. Served-bank and cache/runtime evidence stays in a separate lane.”
- `grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd` (9): “BUT the headline '99%' is a build-time best-of-N + serve-from-cache EXPLOIT (SCOREBOARD_99 itself: 'NOT the model generating'), which violates the K=1/no-BoN constraint”
- `grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd` (64): “No InceptBench run has been executed for this APUSH handoff.”
- `icloud-work/incept/incept-multilingual-generation/src/evaluator/reports/incept_benchmark_report.md` (81): “3. **Quality Filtering:** Only questions scoring ≥8.0/10.0 are retained in the dataset”
- `icloud-work/incept/incept-multilingual-generation/src/evaluator/reports/incept_benchmark_report.md` (13): “- **Weighted Overall Score:** 9.28/10.0”
- `icloud-work/incept/incept-multilingual-generation/src/evaluator/Readme.md` (156): “Analyze question scores and remove low-performing questions from the database.”
- `icloud-work/incept/incept-multilingual-generation/src/evaluator/reports/evaluation_13-01-37_report.md` (17): “| **Weighted Score** | **8.48/10.0** | 300 |”
- `grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd` (73): “The "8,937 passes" is the served-99 best-of-N exploit reborn.”
- `grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd` (73-75): “Generator never produced >820L; EBSR only ≤560L; passages ~104 words; ~98% DOK-2; no `sequence` template; 0/8,937 sequence/match survive strict QA; EBSR is the largest high-Lexile pass-type via **ONE template stamped 1,475×** (same-family trivial auto-pass).”
- `grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd` (76): “Gate G5 on a RAW-K=1, first-attempt, per-template-deduped yield”
- `grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd` (34): “The headline **"99%" was cache + best-of-N**”
- `grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd` (60-61): “Raw acceptance is fixed at 100 preregistered records per family, with no early success or denominator top-up.”
- `grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd` (61-62): “Served-bank and cache/runtime evidence stays in a separate lane.”
- `grade3-reading/artifacts/alpha-read-packager/generator/GENERATOR.md` (152-153): “But it is **NOT a K=1 single-model claim.**”
- `grade3-reading/artifacts/alpha-read-packager/generator/GENERATOR.md` (154): “they are the yield of a search-plus-filter loop.”
- `grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md` (55): “the "99%" was **cache + best-of-N**”
- `grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md` (56): “(not the model generating); the "28%" was **four harness bugs**.”
- `grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd` (36): “- The **"28%" was four eval-harness bugs** — weeks burned on a measurement artifact, not a model failure.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/generator-output-spec.md` (33-36): “A total like "8,937 passes" is **best-of-N reborn** — the same crutch aptraining's "served-99%" turned out to be — when it counts re-samples and template clones: in the G5 intake **one EBSR template was stamped ~1,475× and 0/8,937 sequence/match items survive the strict grader.**”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/generator-output-spec.md` (36-38): “Intake therefore gates on `raw_pass_rate[type]` = (unique-template first-attempt passes) / (unique-template first attempts), reported **per type**, with template-clone inflation removed.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md` (93): “aptraining's headline "99%" was a **build-time best-of-N + serve-from-cache exploit** (kb-0063; SCOREBOARD_99 "NOT the model generating"), and the raw K=1 model floored at mcq/mcq_set 0.292 while the stack masked it [M8].”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/AUDIT_ACTIONS.md` (28-29): “G5 intake gates on **first-attempt, per-template-deduplicated `raw_pass_rate` per type** — "1 prompt → 1 sampled item → graded", NOT "cell has ≥20 survivors after N samples".”
- `grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd` (47-48): “**The headline "99% / served-99" is NOT a model achievement.** SCOREBOARD_99 itself says the served numbers are **"cache-backed… NOT the model generating"** and **"not a verified 99%."**”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (260-262): “**Inference-time generate-and-verify is legitimate for a PRODUCTION generator** — shipping best-of-K verified items is a fine way to build a bank. But it is **NOT a K=1 single-model claim.**”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md` (93): “(Our regenerate-until-pass loop is itself a soft best-of-N; report raw first-attempt yield separately.)”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md` (93): “aptraining's headline "99%" was a **build-time best-of-N + serve-from-cache exploit**”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (262-263): “Do not report these numbers as "the model produces clean G5 items at K=1"; they are the yield of a search-plus-filter loop.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (260-262): “shipping best-of-K verified items is a fine way to build a bank. But it is **NOT a K=1 single-model claim.**”
- `grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd` (34-35): “The headline **"99%" was cache + best-of-N** — its own scoreboard flagged it as **"NOT the model generating" / "not a verified 99%."**”
- `grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd` (50): “So the "99%" is process, not a clean model win.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (352): “Aggregate APUSH+APWH for these two N=30 runs: **52% (clean) → 86% (+crutch) = +34pp**.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (382): “**Crutch-inflation summary:** the 83.3% headline on sft-v4-14b BoN+2bi is roughly **34-50pp inflated** over clean one-shot when you average across the matrix.”
- `icloud-work/aptraining/.agent/research/eval_baseline.md` (16): “The prior pipeline hid this with retry; one-shot exposes it.”
- `icloud-work/aptraining/.agent/memory/MEMORY.md` (194): “BoN K=N is data-harvest + diagnostic + param-discovery only, never quoted as goal progress.”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-003-mcqset-phrase-anchor.md` (3): “0/50 = 0% on fresh KCs). Cited 32/33 on my 17 baseline KCs did NOT generalize.”
- `icloud-work/aptraining/artifacts/quarantine/2026-05-22T163819Z_reports_mcqset_50_50_live_verified_20260522/QUARANTINE_REASON.md` (5): “fresh n=50 re-test at 10.00% (vs 78% step-function bar)”
- `icloud-work/aptraining/.agent/research/eval_baseline.md` (15): “the prior 83.3% was inflated by inference crutches; clean one-shot SFT v7 is at 13%.”
- `icloud-work/aptraining/Cheater/reports/FRESH_HOLDOUT_2026-05-23.md` (53-54): “The iteration pattern (iterate + K=5 best-of) DOES recover the rate, but at higher API cost per item.”
- `icloud-work/ap-social-studies-generator/docs/03-ARCHITECTURE.md` (53): “The generator's internal candidate selection (e.g., generate 3 → pick best 1) is permitted.”
- `aptraining-local/den-of-ideation/reports/current_completion_audit_20260524T2053Z.md` (40): “Do not mislabel this as deployable K1 production `>=99%`.”
- `aptraining-local/den-of-ideation/reports/validation_triage/20260524T202325Z_2026-05-24T2022Z_UNIT1_LEQ_SOLVER_v3_VALIDATED_99_6pct.md.md` (140): “**Deployable bound is K=1 single-shot.** Slice-2 K=1 (rows 100-149) was 239/250 = 95.6% with LEQ v2.”
- `icloud-work/aptraining/workspace/comms/to_den/2026-05-25T0615Z_TASK_concrete_deployable_workflow.md` (88): “No more "99.6% goal complete" framing in production-facing docs. Use the K=1 numbers as headlines.”
- `icloud-work/aptraining/workspace/comms/to_den/2026-05-25T0615Z_TASK_concrete_deployable_workflow.md` (68): “Production must run WITHOUT IB grader access (Render can't reach LAN IB).”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md` (280): “K-of-N judging is useful for experiments and selection, but it is not proof of K=1.”
- `aptraining-local/den-of-ideation/from_den/2026-05-25T0758Z_BLOCKED_WORKFLOW_GENERIC_MCq_RETEST.md` (12): “`/no_think` generic deployable MCQ: `8/20 = 40.0%`”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/INCEPTBENCH-EVALUATION-CONTRACT.md inside it) (211-213): “- Stop a cell as failed when its threshold is mathematically unreachable even if all remaining planned records passed. Do not add prompts to dilute the failure. - Never stop early for success.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/INCEPTBENCH-EVALUATION-CONTRACT.md inside it) (101): “There is no early pass, retry, best-of-N pool, cache read, or denominator top-up.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/INCEPTBENCH-EVALUATION-CONTRACT.md inside it) (13-14): “1. **Raw K=1** measures one frozen model call for one frozen request. It permits no retry, repair, reranking, best-of-N selection, cache substitution, or hidden human choice.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (714): “Served quality is a pipeline result and cannot be relabeled as the generator's raw pass rate.”

Against: The contract is frozen but has not been run: no benchmark run had been executed for that hand-off. This is not a controlled comparison: the filtered report covers five grades over '- **Evaluation Period:** September 30, 2025 to October 02, 2025' (`icloud-work/incept/incept-multilingual-generation/src/evaluator/reports/incept_benchmark_report.md`, line 17), while the 8.48 run is a single grade-3 set whose report does not say it was unfiltered. The contract is a frozen design: no run under it had been executed when the AP work paused (`grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd`). Generating several items and shipping only verified ones is a legitimate way to build a production bank, so long as its yield is not reported as a single-attempt claim (`grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md`). Shipping best-of-K verified items is called a fine way to build a bank; only the claim about the model changes (`grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md`, lines 260-262). Selection still has a place in what students are served: a Grade 5 retrospective credits the delivered bank's quality partly to discarding large volumes of plausible-looking output (`grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd`, line 36), so a served bank can be good where the generator alone is not. The per-type samples behind the 52% and 86% are tiny and partly mismatched ('(different prompts; clean N=3 is too small)', `icloud-work/aptraining/.agent/research/failure_taxonomy.md`, line 349), and the baseline report's '~70 pp' of lift compares a different model, judge and server, so it overstates the effect (`icloud-work/aptraining/.agent/research/eval_baseline.md`, line 243). A retry on a failed delivery that never looks at the output was kept as legitimate ('Transport-level retry on transient 5xx — does not condition on output content.', `icloud-work/aptraining/.agent/research/inference_clean.md`, line 42). iterating and keeping the best of five tries does recover the rate on fresh topics, at a higher cost per item, and one generator's design permits picking the best of three internally. The measured drop mixes the pick with a change of rows: the four-attempt figures came from rows 50-99, which the repairs had targeted, and the single-attempt figures from fresh rows 100-149, and the question-set lane's 100% in both was predicted, not graded. The 8 of 20 retest also used a thinner prompt: "The missing lift is in the actual specialist solver mechanics, not the thin deployable generic prompt." (aptraining-local/den-of-ideation/from_den/2026-05-25T0758Z_BLOCKED_WORKFLOW_GENERIC_MCq_RETEST.md, line 18).

<sub>method · stage: measure · measurement, generation, integrity · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Measure the depth mix a writer produces

Measure the depth mix of generated questions, such as the share needing reasoning rather than recall, as its own figure against a target, since generators skew and accuracy hides it. A proven generator produced depth-of-knowledge level 2 on 78 of 80 kept items.

Counted from its two kept forms, the reading project's proven generator emitted depth-of-knowledge level 2 on 78 of 80 kept items and did not reliably produce level 1 or 3 even where the standard supported them (`grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/assessments/G5_PARAMETERS.md`). The next grade's parameters therefore ask for depth to be an explicit generation setting with the kept-item histogram verified (the same file). The output spec for every grade's generator records the same flag: prompted generators tend to over-emit level 2, and level-3 yield must be measured, not assumed (`grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/generator-output-spec.md`).

Quoted:

- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/assessments/G5_PARAMETERS.md` (119): “**Honest reality flag (load-bearing):** the **proven G3 generator emitted DOK 2 on 78/80 kept items** (measured from form_a.jsonl + form_b.jsonl) — it does **not** reliably produce DOK 1 or DOK 3 even when the standard supports them.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/generator-output-spec.md` (47): “(honest flag: prompted generators tend to over-emit DOK-2; DOK-3 yield must be measured, not assumed).”
- `icloud-work/incept/ML_TRAINING_INSIGHTS_REPORT.md` (345): “Near-perfect curriculum alignment (10.0) and factual accuracy (9.96), but **Inference & Pedagogy is the weak link** at 6.76/10.0, especially for Grade 12 (4.97). Questions tend toward rote recall rather than higher-order thinking.”
- `icloud-work/incept/ML_TRAINING_INSIGHTS_REPORT.md` (330): “| Total Questions | 1,030 |”
- `icloud-work/incept/workflow/reports/REPORT_20260223_144619.md` (64): “| `cognitive_demand` | 35 | Questions test recall rather than higher-order thinking |”
- `icloud-work/incept/README.md` (96): “- **Recall-only** questions: "What year...", "Who was..."”
- `shadow-content-eval/reports/G3-U2-L1-main-review.md` (91): “- **Cognitive mix.** Every visible Read-the-text question is literal recall (visible mix: 9 recall / 2 inference / 7 strategy / 1 vocab).”
- `shadow-content-eval/reports/G3-U1-L12-review.md` (124): “all 9 reading-check questions are literal recall”
- `grade3-reading/artifacts/u4l2-build/g5-audit/KB-NOTES.md` (80-81): “the proven G3 generator emitted DOK 2 on 78/80 kept items — content that collapses to all-DOK-2 is the G3 failure mode”
- `grade3-reading/course-renderer/content/lesson-plans/g3-u2-l1.json` (953): “five of its six visible reading checks are locate-and-recall while the two richest causal items sit in the JSON hidden.”

Against: The counts rest on labels that can be wrong: "p14 `check` is tagged inference, but it is recall (*"clear off"* is quoted). That lowers the real inference share below 36%." (`shadow/content-eval/reports/G3-U1-L13-review.md`, line 155).

<sub>method · stage: measure · demand, generation, measurement · universal · from ap, g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Measure what a forced format costs

Force a strict output format only on kinds of item where its cost has been measured, because it can cut accuracy sharply on reasoning-heavy content while helping classification-like tasks. Forcing a strict output format dropped one model's single-try pass rate from 82.67% to 74.0%, on a day when none of its failures were format failures.

On one day in the AP work, a model's single-try baseline passed 124 of 150 items, and all 26 failures were content failures, none a parse failure (`icloud-work/aptraining/.agent/memory/SESSION_DECISIONS_2026_05_11.md`; `icloud-work/aptraining/.agent/memory/FINAL_PLAN_2026_05_11_v3.md`). Constrained decoding then dropped the pass rate to 74.0%, while a schema set per course and item type gave 84.0%, within noise (`icloud-work/aptraining/.agent/memory/SESSION_DECISIONS_2026_05_11.md`). The project's literature note cites a study in which three of four mainstream models lost 25 to 63 points on a reasoning task in JSON mode, while the same mode helped on classification (`icloud-work/auto-memory-backup/research_constrained_decoding_per_cell.md`). It set strict modes off by default for free-form item types (`icloud-work/aptraining/.agent/memory/MEMORY.md`).

Quoted:

- `icloud-work/aptraining/.agent/memory/SESSION_DECISIONS_2026_05_11.md` (27): “UPLIFT-1 single-seed K=1 T=0 = 82.67% on `ty16vgj9` (124/150).”
- `icloud-work/aptraining/.agent/memory/SESSION_DECISIONS_2026_05_11.md` (28): “UPLIFT-3 constrained decode = 74.0% (-8.67pp, Synapse Item 25 predicted), UPLIFT-3b per-cell schema = 84.0% (+1.33pp, within noise).”
- `icloud-work/aptraining/.agent/memory/FINAL_PLAN_2026_05_11_v3.md` (27): “26/26 today's failures are `status:fail rating:INFERIOR` with content-quality dimensions zeroed (`factual_accuracy`, `stimulus_quality`, `difficulty_distribution`). **Zero parse_fail.** Format-fragility hypothesis is dead.”
- `icloud-work/aptraining/.agent/memory/MEMORY.md` (150): “JSON mode loses 25-63pp on reasoning tasks; per-cell decision; default OFF for free-form cells.”
- `icloud-work/auto-memory-backup/research_constrained_decoding_per_cell.md` (28): “Three of four mainstream models lose 25–63pp on a reasoning task in JSON mode.”
- `icloud-work/auto-memory-backup/research_constrained_decoding_per_cell.md` (30): “Same paper shows JSON mode *helps* on classification (Gemini-1.5-Flash 41.6% → 60.3% on DDXPlus). **Direction depends on task.**”
- `icloud-work/auto-memory-backup/research_constrained_decoding_per_cell.md` (26): “| Gemini-1.5-Flash | 89.3% | 89.2% | −0.1pp |”
- `icloud-work/aptraining/.agent/research/sota_strategy.md` (142): “Reports ~3% improvement using guidance/constrained decoding.”
- `icloud-work/auto-memory-backup/research_constrained_decoding_per_cell.md` (28): “Three of four mainstream models lose 25–63pp on a reasoning task in JSON mode. **This is a capability tax, not a measurement-fairness adjustment.**”
- `icloud-work/auto-memory-backup/research_constrained_decoding_per_cell.md` (62): “- [Tam et al., *Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models*, EMNLP 2024 Industry Track](https://aclanthology.org/2024.emnlp-industry.91/)”

Published: [Tam et al. 2024](https://aclanthology.org/2024.emnlp-industry.91/) · [Generating Structured Outputs from Language Models: Benchmark and Studies (2025)](https://arxiv.org/abs/2501.10868)

Against: A structured-output benchmark cited in the project's strategy review reported about 3% improvement with guidance or constrained decoding (`icloud-work/aptraining/.agent/research/sota_strategy.md`), and in the study behind the 25-to-63-point figure one of four models lost only 0.1 points (`icloud-work/auto-memory-backup/research_constrained_decoding_per_cell.md`). The project's own drop is a single run. Not every model lost: "| Gemini-1.5-Flash | 89.3% | 89.2% | −0.1pp |" (`icloud-work/auto-memory-backup/research_constrained_decoding_per_cell.md`, line 26). The per-type comparison the project recommended has no recorded result.

<sub>method · stage: write · generation, measurement · universal · from ap, research · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Misconceptions are not suggestions

Don't hand a writer known misconceptions as loose suggestions for wrong options: it may write them into stems and explanations as if they were true. Appended to the request as suggested distractors, misconceptions cut passes from 19 of 22 to 14 of 22.

In a 22-item multiple-choice probe on one model, appending curriculum misconceptions to the request as suggested distractor concepts cut passes from 19/22 to 14/22, a fall of 22.7 points, and alignment fell from 1.000 to 0.727, with questions testing misconceptions as if they were valid (`feedback_misconceptions_user_prompt_injection_hurts_2026_05_12.md`). The writer put the misconception into the stem or the right answer's explanation instead of the wrong options, and the note reads the instruction to use them as inspiration as too soft.

Quoted:

- `ap-agent-memory/feedback_misconceptions_user_prompt_injection_hurts_2026_05_12.md` (9): “The model treats them as factual content rather than as distractor inspiration.”
- `ap-agent-memory/feedback_misconceptions_user_prompt_injection_hurts_2026_05_12.md` (15): “| A vanilla (no injection) | 19/22 | 86.4% | 0.968 |”
- `ap-agent-memory/feedback_misconceptions_user_prompt_injection_hurts_2026_05_12.md` (16): “| B misconceptions appended to user | 14/22 | 63.6% | 0.915 |”
- `ap-agent-memory/feedback_misconceptions_user_prompt_injection_hurts_2026_05_12.md` (21): “- `mastery_learning_alignment`: 1.000 → 0.727 (**−0.273**) — questions test misconceptions as if valid”
- `ap-agent-memory/feedback_misconceptions_user_prompt_injection_hurts_2026_05_12.md` (24): “v43-soup includes the misconception content in the question stem or correct-answer rationale rather than in wrong-answer options.”
- `ap-agent-memory/feedback_misconceptions_user_prompt_injection_hurts_2026_05_12.md` (32): “- n=22 small sample, single seed (20260512), single model (v43-soup ty16vgj9)”
- `ap-agent-memory/feedback_mcq_set_RAG_actively_helps_v2.5.6.md` (15): “**Why (hypothesis):** Curriculum KCs provide canonical assessment_boundaries and common_misconceptions that the model uses as material for distractor generation, lifting difficulty_distribution scores.”

Against: One seed, one model, 22 items (same file, line 32). Given instead as curriculum context, the same kind of material was credited, as a hypothesis, with better wrong options in a 6-item probe (`feedback_mcq_set_RAG_actively_helps_v2.5.6.md`, line 15).

<sub>method · stage: write · generation, distractors · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Nothing tied to one text

A block meant for any text holds nothing made for one text, such as a stored film, pictures or labels, unless each text gets its own, checked for fit. The film block, whose one stored film belongs to the first play, failed on 2 of 2 new texts.

I made all 16 of the lesson engine's blocks, built around one play, unchanged for a poem and a speech, and where a block leaned on something made for that play it failed or degraded. The only film on file is the play's unit film, and the film block failed on both texts; 12 of the 14 painting briefs are scenes of the play and 2 show a book, and the poem's video essay set the open-book painting beside claims about a carved face. In the builds the engine renders to, a 3D version's key-word cards read 'Link to deceit', an animated version's lesson file is named for the play's first scene, and its apply page labelled any scene 'Act 1, Scene 1'. The slur guard's code list holds only that play's never-staged lines, so on other texts it matches nothing and a judged question on each line carries the guard.

Quoted:

- `g9/transformer/src/films.js` (11): “{ id: "othello-opening", title: "Othello: the opening (unit film)", file: "Othello-opening-full.mp4", vtt: "Othello-opening-full.vtt", poster: "thumbnail-othello-love.jpg" },”
- `learning-truths/research/2026-10-12-6-transformer-ideas/universality-test.json` (16-17): “"status": "failed",”
- `learning-truths/research/2026-10-12-6-transformer-ideas/universality-test.json` (128-129): “"status": "failed",”
- `g9/art/briefs.json` (180): “"file": "shot24-book-open.jpg",”
- `g9-transformer-runs/blocks/7e771d331c6b4135.json` (31): “"A frown and wrinkled lip show harsh contempt",”
- `g9-transformer-runs/blocks/7e771d331c6b4135.json` (34): “"image": "shot24-book-open",”
- `g9/transformer/src/glue/threejs-render.js` (261): “// its key-word cards say "Link to deceit": our links go on them only when that is our centre too”
- `g9/transformer/ops/render-animated.sh` (12): “cp "$1" "$WORK/src/content/othello-1-1.json"”
- `g9/transformer/v02/README.md` (49): “- **Fixed in its component:** its apply page labels any scene "Act 1, Scene 1", so our exports leave the scene panel”
- `g9/transformer/src/glue/threejs.js` (78): “Its lines never staged or voiced (scripts/check-moments.mjs SLUR, Othello's): read from the mirror at run time, so no”
- `g9/transformer/src/glue/threejs.js` (79): “Without the mirror there is none, and the Jev question carries the guard.”

Against: The ties follow a decision to reuse the existing builds unchanged: "Their work is used as it is, never rewritten, and nothing is written into their repositories." (`g9/transformer/DECISIONS.md`, line 18). Where the fit question ran, it stopped the mismatch: the film block failed on both texts rather than shipping.

<sub>method · stage: ground · generation, media, stimulus, alignment · universal · from g9 · measured · held · found in [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### One core description for every standard

Give every standard the same core description (key concepts, learning objectives, assessment boundaries, common misconceptions, and easy, medium and hard definitions) in one versioned source that writers and judges read.

The curriculum repository is the source of truth for the standards used across all generators, with one version number shared by all curricula, and the evaluator's prompts refer to the same data by concept, such as assessment boundaries and difficulty definitions, not by format. Its core attributes (lesson name, key concepts, learning objectives, assessment boundaries, common misconceptions and difficulty definitions) are strictly typed because downstream tools build interfaces and evaluations around them, while each curriculum may add its own keys beside them.

Quoted:

- `shadow-curriculum/README.md` (3): “Central repository for all curriculum data. This is the **source of truth** for curriculum standards used across all generators.”
- `shadow-curriculum/README.md` (42): “All curricula share a single version number.”
- `shadow-curriculum/plans/schema-decisions.md` (49): “**Core attributes (still strictly typed):** `lesson_name`, `key_concepts`, `learning_objectives`, `assessment_boundaries`, `common_misconceptions`, `difficulty_definitions`.”
- `shadow-curriculum/plans/schema-decisions.md` (66): “**Secondary:** strict types on the core set stay important because those fields are the ones downstream tools build UIs and evals around. Flexibility at the edges, rigor at the core.”
- `shadow-curriculum/plans/schema-decisions.md` (62): “Hence the hybrid: enforce the names and types of the core set, let curricula add their own keys beside it.”
- `shadow-bench/plans/02-curriculum-api-transition-plan.md` (17): “The LLM evaluation prompts already reference curriculum data by concept (Assessment Boundaries, Difficulty Definitions, etc.) -- not by format.”

Against: The core set is 'validated with strict types when present', and each core field may be null (shadow-curriculum/schemas/standard-leaf.schema.json lines 34-61); parent standards carry none: 'Leaf nodes have `attributes`; non-leaf nodes have `attributes: null`' (shadow-curriculum/plans/curriculum-api-plan.md line 249). Without definitions the judge skips the check: 'Without definitions → 1.0.' (shadow-bench/src/inceptbench/prompts/question/_base_evaluation.txt line 35). Some core fields were inferred by a model with no outside source (shadow-curriculum/plans/data-hierarchy.md line 267), and the bundled AP social-studies courses are judged from a local file instead, resolving their 'curriculum context **offline** from that file' (shadow-bench/docs/internals/ap-evaluation.md lines 10-12).

<sub>method · stage: ground · alignment, generation, evaluation · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### One home for each rule

Give each rule one home and authority, restated nowhere else, and check a writer's instructions for contradictions before generating, since conflicting rules cause refusals and silent overrides. A kit instruction to refuse without a source corpus that was never wired took one item type to 0%.

A check-in on why every layer added to an AP question generator had cost quality found the layers fighting each other (`aptraining-local/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md`, lines 15-19 and 110-123). A kit prompt told the writer to refuse without a source corpus that was never wired, and document questions passed 0% (line 51); a prompt rule demanding four questions clashed with a validator in code enforcing three and was silently overridden, and the writer refused two directives that contradicted each other (lines 91-94); a kit's fixed period framing contradicted the objective's period, and the writer refused (lines 113-114). Earlier the project had put the kit first and the service's own prompt last, as the hard schema authority, so the kit's illustrative field names could not break the judge's JSON shape (`icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/WINS_20260514.md`, line 152). Banned lists count as rules: an intro-video guide keeps its banned punctuation in a settings file and its banned phrases in the script prompt, and restates neither list anywhere else (`downloads/BrainLift - What makes a good intro video.md`, line 953).

Quoted:

- `aptraining-local/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md` (51): “| Satisfaction kit DBQ refusal | 0% on DBQ | `system_prompt_dbq.md` line 135: "Without D13: refuse" — we don't wire D13 |”
- `aptraining-local/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md` (91): “"EXACTLY 4 questions" conflicted with hardcoded validator at”
- `aptraining-local/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md` (92-94): “`main.py:5948` enforcing exactly 3 → silently overridden. DBQ directive + kit's D13 directive → v80b correctly refused contradictory instructions.”
- `aptraining-local/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md` (113-114): “1. **Contradicts another layer** (kit says "1491-1607", learning objective says "pre-1491" → v80b refuses)”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/WINS_20260514.md` (152): “- The kit is prepended to the system prompt, then the original service prompt is appended as the hard schema authority. This prevents the kit's illustrative field names from breaking InceptBench JSON shape.”
- `downloads/BrainLift - What makes a good intro video.md` (953): “The banned phrase list is maintained in `prompts/script.md`, since a phrase ban needs the wording of the ask around it to be understood.”
- `downloads/BrainLift - What makes a good intro video.md` (953): “Neither list is restated anywhere else.”
- `home-agent-memory/findings_sftv7_20260424.md` (50): “**Pattern:** scoring_notes contained specific evidence (dates, named events) that”
- `home-agent-memory/findings_sftv7_20260424.md` (53): “**Root cause:** Two contradicting instructions:”
- `home-agent-memory/findings_sftv7_20260424.md` (54): “- System prompt: `⛔ NEVER list specific event names/dates/people`”
- `home-agent-memory/findings_sftv7_20260424.md` (55): “- User prompt PROCEDURE: `"Write it as [FACT: <exact phrase>]"` — granted permission”
- `home-agent-memory/findings_sftv7_20260424.md` (57): “**Fix applied (2026-04-24, saq.py `build_saq_user`):** Removed the PROCEDURE block.”
- `home-agent-memory/findings_sftv7_20260424.md` (137): “2. **SAQ 33%** — new categorical-only fix not yet tested; these runs were pre-fix”
- `g9/transformer/DECISIONS.md` (24-25): “The reading game engine's decide layer (typed decisions, support gates, logs for replay) is imported, not copied.”
- `g9/transformer/src/engine.js` (2): “One source of truth: nothing is copied.”
- `g9/transformer/src/judge.js` (12): “One check's verdict from its typed answer (also used by the runtime, whose question ids are namespaced).”
- `g9/transformer/src/blocks.js` (115): “Shared by blocks and the v01 lesson route.”
- `g9/transformer/src/analyse.js` (16): “a.pass && a.value >= 0.6”
- `g9/transformer/src/judge.js` (17): “a.value >= 0.5”
- `g9/transformer/src/question.js` (34): “{ provider: judge, samples, tag: "suggest-question" }”
- `grade3-reading/bias_experiment/experiment-record/evidence/primary-records/reading-81d-externalized-policy-compiler-plan.md` (278-279): “Detection: textual order decides precedence. Recovery cascade: 1. Add explicit priorities and dependencies. 2. Reject unresolved conflicts at compile time.”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-16.md` (425-426): “Two contradictory pins now sit on staging and `npm run check` is red at this step since #443.”
- `grade3-reading/course-renderer/docs/feedback/g4-plan-red-team-2026-07-20.md` (131): “One thing worth flagging honestly: on our own re-check after the first fix wave, we caught that Fix 1 was only half-closed - two sibling copies of the guards content (UNIT-SPECS.md and the standalone guards file's own intro paragraph) still said U2/U3/U4-only, contradicting the corrected table just below them.”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/RED_TEAM_ROUND2_PR83.md` (80-82): “it's Fix 1 only touching one of three copies of the same fact, which is worse than touching none, because now the package **contradicts itself** rather than being uniformly wrong.”

Against: The banned phrases sit in the generator's prompt, and the AP work found that adding warnings to a generator's prompt made it worse. One case, and the fix was not yet tested when the note was written (same file, line 137).

<sub>method · stage: write · generation, format · universal · from ap, g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### One job per generation step

Make a complex item in steps that each do one job the writer can't do well alongside the others, rather than in a single pass. A single call writing all 7 documents of one item drifted from its context by documents 4 to 7 and began inventing attributions.

The AP work's rule is that splitting generation into complementary steps is the only reason to add steps, and its research summary's test is whether each stage does one thing the model can't do well alongside other things. A single call writing all 7 documents of an item drifted from its context by documents 4 to 7 and began confabulating attributions, and writing the source and its questions in one step gave tightly coupled outputs that were hard to diagnose. The records credit the large writer's 97% to splitting complex types into steps, but hold no clean measurement of splitting. The steps can be, for example, plan, then source, then questions.

Quoted:

- `icloud-work/ML learnings/failures_and_false_starts.md` (110): “Breaking generation into multiple complementary steps is the only reason to add steps — verification and regeneration are not valid approaches.”
- `icloud-work/ML learnings/pipeline_architecture_insight.md` (5): “Gemini doesn't score 97% because it's a smarter model. It scores 97% because complex question types (MCQ_SET, DBQ) are broken into multiple complementary steps, each optimized for a specific subtask.”
- `icloud-work/ML learnings/research_qwen3_structured_multistage.md` (215): “**The right question is not "how many stages" but "does each stage do one thing the model can't do well simultaneously with other things?"**”
- `icloud-work/ML learnings/mcq_set_journey.md` (25): “- Stimulus generation and question generation in one step produced tightly coupled outputs that were hard to diagnose”
- `icloud-work/ML learnings/sft_v7_benchmark_postmortem.md` (88): “**Why factual accuracy fails in DBQ:** 7 documents, each needing a plausible historical source, date, and content. The model generates all 7 in one call. By documents 4-7, it's drifted from its context and starts confabulating attributions.”
- `icloud-work/ML learnings/decisions_and_pivots_timeline.md` (82): “**The surprise:** `.env` already had `LLM_BACKEND=fireworks` set. The routing was already there. The ONLY change needed was reducing token limits from Gemini scale to sft-v4 scale. That was a 5-minute code change.”
- `icloud-work/ML learnings/mcq_set_journey.md` (154): “| sft-v4, Apr 22 | 0% | 3-step pipeline, Fireworks | No MCQ_SET in training data |”
- `icloud-work/ML learnings/mcq_set_journey.md` (44-46): “1. Research→Compile (single step): 60% — worse than before
2. Research→Stimulus→Questions (3 steps): 60% — same problem
3. Stimulus (from scratch, no research)→Questions: 80% — best”
- `icloud-work/ML learnings/research_qwen3_structured_multistage.md` (251): “- When the sub-task outputs need tight semantic coupling (e.g., you can't generate the introduction and body separately if they need to reference each other)”

Against: A jump from 0% to 18% once credited to the pipeline came from a token-limit change, since the 3-step pipeline was already running at 0%; an added research step left results at 60% against 80% without it; and outputs that must refer to each other can't be made apart.

<sub>method · stage: write · generation · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### One knowledge statement per item

Build each item on one official knowledge statement, and take its wrong options from the misconceptions recorded for that statement once they are confirmed not model-written. In two courses, 97% and 99% of the recorded misconceptions were official; the rest had been written by a model.

A knowledge service holding, for each official knowledge statement, its recorded misconceptions and its assessment boundaries was adopted as the source for writing items: one multiple-choice and one short-answer item per statement, with the misconceptions as seeds for wrong options and the boundaries as a guard on scope (`icloud-work/auto-memory-backup/reference_curriculum_api_lan.md`). A provenance check then found that for one course the official framework publishes neither field and a model had filled both in, which a record-level source tag hid; in two other courses, 97% and 99% of the misconceptions were official and safe to use once the model-written ones were filtered out (`icloud-work/auto-memory-backup/feedback_field_level_provenance.md`). The writer is also given that statement's scope limits.

Quoted:

- `icloud-work/auto-memory-backup/reference_curriculum_api_lan.md` (72): “- **`common_misconceptions` array = MCQ distractor seeds.** This is the missing piece for our 90%-passing MCQ cells to hit 99%.”
- `icloud-work/auto-memory-backup/reference_curriculum_api_lan.md` (73): “- **`assessment_boundaries` = scope guard.** Eliminates "out-of-scope" generation failures Quill's D8a found.”
- `icloud-work/auto-memory-backup/reference_curriculum_api_lan.md` (85): “- v29 SFT data: pull all KCs per course, generate one MCQ + one SAQ per KC using the bundled scaffolding as the prompt context, IB-grade, keep ≥0.85”
- `icloud-work/auto-memory-backup/feedback_field_level_provenance.md` (32): “97% of APUSH, 99% of APWH misconceptions are CB-canonical, safe as authoritative distractor seeds”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (16): “Candidate misconceptions and richer authoring prompts across all nine units | Complete coverage, factual citation, or learner-ready wording”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (511-512): “G5-BAR §7 pins exactly four `feedback_map` ids; this one isn't among them”

Against: A 454-item pilot built this way averaged 0.96 on the grader, but over the items that grader kept, so it does not show the recipe works ("Quill v30g pilot 454 rows mean chosen IB 0.96 → on the right track.", `icloud-work/auto-memory-backup/feedback_data_ceiling_not_capacity_ceiling.md`, line 58). The claims that the boundaries eliminate out-of-scope failures and that the misconceptions are the missing piece to reach 99% are assertions, not measurements.

<sub>method · stage: ground · alignment, distractors, generation · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### One pipeline per item type

Generate each item type through its own steps and its own checks, so that a change to one type cannot break another.

A synthesis across five corpora of the AP work marks per-type generation as confirmed in four of them and notes that two generators improved when their validators became type-specific (`MASTER_SYNTHESIS.md`, lines 74 and 259). One generator's report makes per-type modules a first rule, with no single prompt shared by every item type, so that one type can change without risking another (`ap_social_studies_generator_distilled.md`, lines 54 and 172). Another lists the type-specific checks to run before scoring: option count, answer count, explanation consistency, answer uniqueness and schema validity (`k_12_social_studies_distilled.md`, line 74).

Quoted:

- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/MASTER_SYNTHESIS.md` (74): “| Per-type generation | confirmed | confirmed | confirmed | confirmed | compatible | T1 |”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md` (172): “- Use per-type generator modules. APUSH production should not have one shared prompt surface for all cells.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md` (54): “- This is the right ownership boundary: change MCQ_SET without risking DBQ or SAQ.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/k_12_social_studies_distilled.md` (74): “- Add type-specific deterministic validators before scoring: option count, answer count, explanation consistency, answer uniqueness, schema validity.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/MASTER_SYNTHESIS.md` (259): “- K-12 and AP generator both improved when validators became type-specific.”

Against: No source compares per-type and shared generation head to head: the synthesis tallies where the pattern was confirmed rather than measuring it (`MASTER_SYNTHESIS.md`, line 74).

<sub>method · stage: write · generation, format · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### One short idea per knowledge statement

Keep each generated knowledge statement short and about one idea, since people trimmed the long ones and split the combined ones. About 20 of 160 comments on generated knowledge nodes record trimming an over-long statement, and three record splitting one fact into two.

In the human checks of an AP history course's model-generated knowledge nodes, about 20 of 160 comments record trimming an over-long statement, with the original kept and marked 'og (too long)'. Three record a manual addition that split the previous fact into two, and two more facts were split in the same checks, one into two and one into four.

Quoted:

- `downloads/AP US History - Knowledge Schema - SME Tracker.xlsx` (sheet 'Unit 3 Nodes', row 151, column M; column N reads 'Edited'): “og (too long) - In 1794, the Whiskey Rebellion occurred when western Pennsylvania farmers protested Alexander Hamilton's excise tax on whiskey;”
- `downloads/AP US History - Knowledge Schema - SME Tracker.xlsx` (sheet 'Unit 3 Nodes', rows 152, 155 and 157, column M): “manual add - split the previous fact into two”

Against: none found

<sub>method · stage: ground · wording, generation · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Only the rules that apply

Give a writer only the rules that apply to the piece it is writing, compiled from the rulebook, never the whole rulebook. Across 18 models, adherence to constraints fell as instructions got harder.

The reading project's proposal for a pedagogy policy compiler has deterministic code pick the rules that apply to one artifact and hand the writer only that small contract, so thousands of dormant rules never enter the prompt (`grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd`); its experiment intake keeps the raw rule bank out of the writer's prompt (`grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd`). The proposal calls this its own inference from a published study in which, across 18 models, constraint adherence fell materially as instruction difficulty increased.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd` (73-74): “across 18 models, constraint adherence fell materially as instruction difficulty increased”
- `grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd` (74-76): “**Our architectural inference:** compile a small active contract rather than prompt with the full rule base”
- `grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd` (45): “thousands of dormant rules do not enter the prompt.”
- `grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd` (285): “The raw bank never enters the renderer prompt.”
- `grade3-reading/bias_experiment/experiment-record/evidence/primary-records/reading-81d-externalized-policy-compiler-plan.md` (273-274): “Detection: model receives the full rule bank or more than the compiled active contract. Recovery cascade: 1. Evaluate rules outside the model. 2. Emit only the minimal active specification.”

Published: [Ye et al. 2026](https://aclanthology.org/2026.findings-acl.99/)

Against: The study measured adherence as instructions got harder, not as the rulebook grew, and the intake's planned comparison at 3, 5, 10 and 20 active rules has no result yet (`grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd`).

<sub>method · stage: write · generation · universal · from g3, research · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Plan each question before the prose

Decide in code, before the model writes any prose, what each question covers and which fact its answer hinges on, and let the model only render that plan. Freeform generation of question sets had a committed baseline of 0.31, against 0.6 for a structured single stage.

For AP question sets, the chosen design pins each answer's hinge before the model writes: a deterministic first stage picks the curriculum fact the correct answer hinges on and asserts it is absent from the source, and the model only renders the source, stems and options to that plan. It was chosen because freeform generation leaks by default, against committed baselines of 0.31 for freeform and 0.6 for a structured single stage, and earlier work had found question sets better when a plan step fixed what each question must cover. The two-stage run itself was queued, not yet measured.

Quoted:

- `icloud-work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md` (8): “Freeform generation leaks by default (least-resistance = stimulus-answerable).”
- `icloud-work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md` (12): “select the **curriculum fact the correct answer hinges on + assert it is ABSENT from the stimulus**;”
- `icloud-work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md` (35): “**Baselines (≠0):** v97 freeform = **0.31**; structured 1-stage = **0.6** (Cursor). Beat 0.6.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md` (75): “MCQ_SET works better when the plan step constrains what each child question must cover.”

Against: "over-constrained Stage 1 can pass eduacc but break factual/coherence" (icloud-work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md, line 37); the run was only queued: "Status: queued for the macmini executor / main-a on reconnect." (same file, line 44).

<sub>method · stage: ground · generation, integrity · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Plan the whole cluster before splitting it

Plan a sequence or group of related knowledge as a whole, with one target performance, a throughline and a persistent example, before splitting it.

The reading project's alignment plan makes the cluster (one named performance, 1–2 knowledge types, 2–5 KCs, one load-bearing throughline) the unit of design, generation and reteaching, and generates the cluster's reasoning before decomposing it into knowledge components and then items (`grade3-reading/ti-courseplans/docs/academics-alignment-plan.md`). It records the round-2 sequencing finding that atomising first on narrative subjects produced "locally-correct micro-lessons that never cohere". The curriculum BrainLift gives the upper limit: as the surface area of the task grows, the precision and discipline of a model's output degrade (`grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md`). Keep each generated unit to one performance.

Quoted:

- `grade3-reading/ti-courseplans/docs/academics-alignment-plan.md` (14-15): “the *cluster* (one named performance, 1–2 knowledge types, 2–5 KCs, one load-bearing throughline)”
- `grade3-reading/ti-courseplans/docs/academics-alignment-plan.md` (16-18): “Atomise-first on narrative subjects produces "locally-correct micro-lessons that never cohere" — the round-2 sequencing finding.”
- `grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md` (544): “as the surface area of the task grows, the precision and discipline of the LLM's output degrade”
- `grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md` (538): “For modular, abstract material (much of maths) this matters little, because the atoms genuinely are near-independent and atomise-first is close to lossless.”
- `ti-courseplans-audit/docs/academics-alignment-plan.md` (15-16): “Generate cluster reasoning first (throughline, persistent example, narrative order), then decompose to KCs, then items.”
- `ti-courseplans-audit/docs/academics-alignment-plan.md` (16-18): “Atomise-first on narrative subjects produces "locally-correct micro-lessons that never cohere" — the round-2 sequencing finding.”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (97): “per-item generation with no throughline reasoning → "locally-correct micro-lessons that never cohere"”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (97): “does the design record show cluster-level reasoning (throughline, persistent example) before KC decomposition?”

Against: The curriculum BrainLift says this matters little for modular, abstract material such as much of maths, where atomising first is close to lossless (`grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md`, line 538). The finding is stated for narrative subjects (`ti-courseplans-audit/docs/academics-alignment-plan.md`).

<sub>method · stage: ground · generation, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Point to a place only when known

Let model-written feedback name a place in the text, such as its first line, only when the model was given each excerpt's position; otherwise block such claims in code. A feedback-only safeguard passed 52/52 route checks, against 9 expected failures on the old route.

On a third miss, a generated hint told a child to look at the very first line of the story for an offer that comes later (`grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json`, line 1328). The feedback writer had been given grounding excerpts with no story positions, and the first excerpt happened to hold the offer. The repair was a deterministic, feedback-only locator safeguard, and an independent review verified it on 52/52 route checks against 9 expected failures on the old route, with all 134 original assertions unchanged (line 1339).

Quoted:

- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (1328): “On current 660a8339/d0qep15iE3avbSb2NmTik, the real third L4 p24 opening miss tells the child to look at the very first line of the story for Peter's offer, but the story begins The Darling children could not sleep.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (1328): “Generated feedback receives unordered grounding excerpts without story positions.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (1328): “Propose and independently review a bounded feedback-only locator safeguard for excerpt-only G3 open requests.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (1339): “verifies 52/52 current versus43pass/9expected baseline failures with all134 original assertions unchanged.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (1339): “Accepted feedback-only safeguard committed51c160f8”

Against: The cause is a co-occurrence, not a proven mechanism: "The first excerpt happens to contain the offer; that correlation does not establish model-internal causation." (`grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json`, line 1328). The safeguard was proven only under controlled responses: "Finite detector protection is proven under controlled route responses; no forced native bad phrase or universal language claim." (line 1339).

<sub>method · stage: settle · feedback, generation, stimulus · universal · from g3 · measured · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Prove a model uses what it's given

Before crediting a model with using the rules or material it is given, test it with them removed, shuffled, deliberately wrong and contrary to what it already knows. In one test accuracy was 30.00% with the supplied material, 32.50% with it removed and 25.83% with it shuffled, so the material was not driving the result.

A recursive-refinement pilot on public synthetic items, which coded teaching principles into a typed schema, ran controls with the supplied reference material removed and with it shuffled. Refinement raised mean exact accuracy from 20.83% to 30.00%, but the removed control reached 32.50% and the shuffled one 25.83%, so the probe failed its dependence check and was aborted. The same experiment's protocol scores runs under deliberately wrong rules twice, for obedience to the rules given and for correctness, because a model that ignores a wrong rule can look right about the world while failing to be controllable. An exploratory probe used rules that contradict ordinary world knowledge so that prior knowledge alone could not explain a pass, and the plan for comparing models calls reciprocal one-field flips necessary to tell obedience from general quality.

Quoted:

- `grade3-reading/bias_experiment/llm-instruction-portability-study/docs/03-method-and-results.md` (25-26): “The recursive condition scored 30.00%, authority removal scored 32.50%, and authority shuffling scored 25.83%; none produced a complete group.”
- `grade3-reading/bias_experiment/llm-instruction-portability-study/docs/03-method-and-results.md` (26-28): “Because the recursive result did not beat the authority-removed control, the probe failed its authority-dependence check and was aborted.”
- `grade3-reading/bias_experiment/.agent/memory/g3-agent-qualification-v2-trm-combined-outcome.md` (12): “Recursive refinement improved mean exact-object accuracy from 20.83% to 30.00%, but authority-free accuracy reached 32.50% and effective shuffled-authority accuracy reached 25.83%”
- `grade3-reading/bias_experiment/experiment-record/evidence/knowledgebot/kb-0132-eppc-bias-experiment-execution-handover.qmd` (411-413): “score two outcomes independently: obedience to the supplied contract and correctness against the intended gold policy. A model that ignores the wrong contract may look world-correct but has failed controllability.”
- `grade3-reading/bias_experiment/.agent/memory/COUNTERFACTUAL_AUTHORITY_A0_2026-07-17.md` (47-49): “The counterfactual A and C shark outputs contradict the model's ordinary world knowledge, so prior-only behavior cannot explain the result.”
- `grade3-reading/bias_experiment/.agent/memory/cross-model-eval-contract-plan.md` (148): “Reciprocal one-field flips are necessary to distinguish policy obedience from generic quality.”

Against: The removal and shuffle controls ran on a synthetic task of coding teaching principles, not on writing or judging student material, and the evidence index lists that result as public and synthetic, with no private or gold evidence (grade3-reading/bias_experiment/experiment-record/evidence/EVIDENCE_INDEX.md line 28). The world-knowledge probe was exploratory.

<sub>method · stage: measure · generation, evaluation, measurement · universal · from g3 · measured · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Prove each new scope on its own

Prove a generator on every item type, scope, grade and difficulty it will serve, accepting it on its worst, since success on one shows nothing about another. Wrapping a generic all-period fallback for a new period passed 0 of 3 in its self-test.

A coverage scout of 23 May 2026 read the solvers validated for the first period and found that period's span hard-coded into their prompts; it concluded that running them on later periods would be 'actively wrong' because they would force the first period's limits onto later requests, and that coverage of the other units could not be claimed from prompt generalization alone. The one measured case: wrapping a generic all-period fallback for the second period passed 0 of 3 in a self-test, with invalid or generic content on later rows, and the note ruled that the expansion should not be delivered from that fallback alone. One of the three failures was a judge timeout on the one locally valid item (`icloud-work/aptraining/workspace/comms/from_den/2026-05-23T1357Z_BLOCKED_unit2_mcqset_parent_archetype.md`, lines 31-39). A plan to take a reading generator from grade 3 to grade 5 found none of its roughly 930 items in the higher grade's reading band, which lies above anything the generator had produced, so moving an item up means regenerating it with a new passage, stem, distractors and evaluation (`grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/ITEM_INVENTORY.md`, lines 22-36; `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md`, line 60). What carries over is a generator's scaffolding, not its items.

Quoted:

- `aptraining-local/den-of-ideation/reports/unit2_9_coverage_scout_20260523.md` (57): “prompt hard-codes `Time period: 1491-1607 only`.”
- `aptraining-local/den-of-ideation/reports/unit2_9_coverage_scout_20260523.md` (69): “Conclusion: running these solvers on Unit 2-9 would be actively wrong. They would force Unit-1 constraints onto later-period requests.”
- `aptraining-local/den-of-ideation/reports/unit2_9_coverage_scout_20260523.md` (125): “Do not claim Unit 2-9 coverage from prompt generalization alone.”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T1357Z_BLOCKED_unit2_mcqset_parent_archetype.md` (32): “passed: 0”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T1357Z_BLOCKED_unit2_mcqset_parent_archetype.md` (42): “2. Parent all-unit fallback emits invalid/generic Unit-2 MCQ_SET content for later sampled rows.”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T1357Z_BLOCKED_unit2_mcqset_parent_archetype.md` (49): “Unit-2 MCQ_SET expansion should not be delivered from parent fallback alone.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md` (60): “**Lexile-band extrapolation is unproven at G5.** Today's templates top out at 800–820L. G5 needs **830–1010L** — *above everything the generator has ever produced*. EBSR already proves the model degrades at higher Lexile (couldn't clear EBSR above 560L); pushing the whole bank +230–410L is into untested territory.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/ITEM_INVENTORY.md` (22): “**Total ELA-reading items in hand:** 745 (deployed) + 80 (form_a/b) + 21 (spares) + 84 passing attempts = **~930 G3 reading items**”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/ITEM_INVENTORY.md` (23): “**Items at/in the G5 Lexile band (≥830L):** **0.**”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/ITEM_INVENTORY.md` (34): “Up-leveling a G3 item means a new cold passage + new stem + new distractors + re-eval = a regeneration, not a reuse.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/ITEM_INVENTORY.md` (36): “### What IS reusable (the real "don't reinvent" win — scaffolding, not items)”
- `icloud-work/aptraining/.agent/NORTH_STAR.md` (24): “We need to win every cell, not the average. Average can hide a regression on the hardest cell.”
- `icloud-work/aptraining/.agent/research/OVERNIGHT_RECAP.md` (105): “**v8/v15 numbers were MCQ-only.** v8 was trained on MCQ records only — and on the 10-cell test, **v8's DBQ outputs fail to parse 50% of the time** (13/30 APUSH, 17/30 APWH).”
- `icloud-work/aptraining/.agent/NORTH_STAR.md` (45): “The mission is the min over 10 cells, not the mean.”
- `icloud-work/auto-memory-backup/project_v8_mcq_only.md` (14): “v8's training data was filtered to MCQ records only (2,821 records, all `question_type=mcq`). When tested on the full 10-cell holdout, v8 produces non-parseable output ~50% of the time on DBQ:”
- `icloud-work/auto-memory-backup/project_v8_mcq_only.md` (22): “Single-cell results without the 10-cell context can hide DBQ-style failures.”
- `icloud-work/auto-memory-backup/feedback_ops.md` (20): “- Cell-balance matters: don't optimize one cell while breaking others. Test on the full eval set, not just the one you're working on.”
- `icloud-work/auto-memory-backup/project_v8_mcq_only.md` (18): “Other untrained types (mcq_set, saq, leq) parse OK 86-100% — they're structurally simpler.”
- `g9-transformer-runs/blocks/b5f74899349e1331.json` (39): “"The question does not give its answer away: the judge found this does not hold"”
- `g9-transformer-runs/blocks/d872bc1dfbda65fb.json` (68): “No hint hands the answer over: a hint uses a word that hands the answer over, or the answer itself”
- `g9/transformer/v02/QA.md` (138-140): “the open check's leak rule was stricter than the animated build's (a hint may quote the line to read); its give-away question was answered from general knowledge of Othello (now: the question's own words only)”

Against: The breakage was concentrated in the most complex type: "Other untrained types (mcq_set, saq, leq) parse OK 86-100% — they're structurally simpler." (`icloud-work/auto-memory-backup/project_v8_mcq_only.md`, line 18).

<sub>method · stage: measure · alignment, generation, measurement · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Qualify every model and version

Qualify each model and version on its own against the rules it will follow, with controls that catch a rule applied outside its scope. On one fixed set of 20 cases, three models got 60, 67 and 136 of 140 rows exactly right.

In the reading project's counterfactual-authority experiment, three models ran one frozen contract of 20 cases at seven rows each, scored on stored responses with no judge, repair or retry, and got 60, 67 and 136 of 140 rows exact and 0, 0 and 17 of 20 robust clusters (`grade3-reading/knowledge_bot/knowledge/kb-0166-counterfactual-authority-a1b-terminal-causal-control.qmd`). Of the 157 misses, 43 failed the negative-control gate, where the rule should not have applied, and one model carried out a counterfactual rule exactly but also under the wrong-path and wrong-subject controls: steerable but not safely scoped. The policy-compiler proposal requires conformance qualification for every model and version (`grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd`). Re-test every instruction whenever the model changes: in the AP work an instruction that a large model mostly respected was not enough for a smaller one, which passed 0 of 6 short-answer items, failing on the accuracy of their scoring notes, where the large model had passed 95 to 100% (`icloud-work/ML learnings/sft_v7_benchmark_postmortem.md`, lines 15 and 130-132).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0166-counterfactual-authority-a1b-terminal-causal-control.qmd` (12): “OpenAI 60/140 exact and 0/20 robust clusters, Claude 67/140 and 0/20, DeepSeek 136/140 and 17/20”
- `grade3-reading/knowledge_bot/knowledge/kb-0166-counterfactual-authority-a1b-terminal-causal-control.qmd` (86): “Failure localization across the 157 tested misses:”
- `grade3-reading/knowledge_bot/knowledge/kb-0166-counterfactual-authority-a1b-terminal-causal-control.qmd` (89): “- negative-control gate: 43;”
- `grade3-reading/knowledge_bot/knowledge/kb-0166-counterfactual-authority-a1b-terminal-causal-control.qmd` (110): “It was steerable but not safely scoped.”
- `grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd` (46): “every model/version requires conformance qualification.”
- `grade3-reading/knowledge_bot/knowledge/kb-0168-eppc-bias-experiment-terminal-kill-and-salvage.qmd` (50): “OpenAI 60/140 and 0/20 robust clusters, Claude 67/140 and 0/20, DeepSeek 136/140 and 17/20; worst route 0/20 against 20/20.”
- `grade3-reading/knowledge_bot/knowledge/kb-0168-eppc-bias-experiment-terminal-kill-and-salvage.qmd` (70-71): “found the assigned taxonomy or ontology facet in 119/120 treatment outputs. That supports strong bounded semantic steering”
- `grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd` (73-74): “across 18 models, constraint adherence fell materially as instruction difficulty increased, and targeted training improved it.”
- `icloud-work/ML learnings/sft_v7_benchmark_postmortem.md` (130): “1. **The anchor-fact pattern was invented for stimuli, not rubrics.** When MCQ_SET was broken at 0%, we fixed the stimulus with anchor-facts. SAQ was already at 95-100% on Gemini, so its scoring notes weren't a problem. Nobody connected the dots to apply it to rubrics.”
- `icloud-work/ML learnings/sft_v7_benchmark_postmortem.md` (132): “2. **The current approach (negative prompting) seemed to work on Gemini.** Because Gemini is large enough to mostly respect the "no specific evidence" instruction and has accurate enough parametric memory that when it does include evidence, it's usually right. The instruction that's good enough for a large model is insufficient for a 14B model.”
- `icloud-work/ML learnings/sft_v7_benchmark_postmortem.md` (15): “| SAQ | 0/6 = **0%** | factual_accuracy (scoring notes) |”
- `icloud-work/ML learnings/knowledge_and_rag_pipeline.md` (234): “None of these are implemented yet. The current system (4,177 facts, cluster matching, "facts as hints") is good enough for Gemini at 97%. It's not good enough for sft-v4/sft-v7 at the target rates.”
- `icloud-work/ML learnings/week_of_apr_21.md` (135): “Gemini reliably fills all JSON schema fields including optional ones. Fireworks model frequently omits optional fields (e.g., `source_attribution`). Keep required fields minimal; never rely on optional field presence for correctness. The `anchor_fact` field is required in the schema specifically because of this.”
- `icloud-work/ML learnings/master_strategy_apr24.md` (105): “The literature is clear: static historical facts are high-confidence parametric knowledge that overrides soft prompt constraints.”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (73): “No matter how you phrase the prompt, the model defaults to its training behavior when generating a historical document excerpt.”
- `icloud-work/ML learnings/sft_version_history.md` (52): “- Focus: MCQ_SET and DBQ are the failure modes. Other types excluded (already have training data from sft-v6)”
- `icloud-work/ML learnings/fireworks_training_reference.md` (109): “- **Base:** `accounts/fireworks/models/qwen3-14b` (raw, same as Stage 1)”
- `icloud-work/ML learnings/week_of_apr_21.md` (17): “The same scaffolding transfers to Fireworks with only token limit adjustments.”
- `grade3-reading/knowledge_bot/knowledge/kb-0168-eppc-bias-experiment-terminal-kill-and-salvage.qmd` (50): “completed 420/420 rows with zero evidence invalidities but failed strict portability: OpenAI 60/140 and 0/20 robust clusters, Claude 67/140 and 0/20, DeepSeek 136/140 and 17/20”
- `grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd` (46): “every model/version requires conformance qualification”
- `grade3-reading/knowledge_bot/knowledge/kb-0168-eppc-bias-experiment-terminal-kill-and-salvage.qmd` (70-71): “An explicitly post-hoc diagnostic found the assigned taxonomy or ontology facet in 119/120 treatment outputs.”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (107-109): “KILL EPPC as the automatic primary pedagogy control plane. The frozen rule required every A/A2/B/C/D, review, quality, and viability gate to pass and required KILL on any failure or insufficient evidence.”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (110-112): “adjacent A-only A1b completed 420/420 valid rows and failed exact cross-route portability: worst route 0/20 against 20/20. OpenAI and Claude each had 0/20 robust clusters; DeepSeek had 17/20.”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (113-114): “the post-hoc semantic-facet diagnostic was 119/120. Prompt-local steering is real, but exact execution, negative-control locality, and invariant preservation were not portable.”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (115-116): “formal A, A2 renderer, B, C, D, artifact quality, and operational gates never produced complete scored evidence.”
- `grade3-reading/bias_experiment/llm-instruction-portability-study/docs/03-method-and-results.md` (49-50): “The primary statistic was the minimum robust-cluster result across routes: 0/20 against a required 20/20.”
- `grade3-reading/bias_experiment/llm-instruction-portability-study/docs/03-method-and-results.md` (65-66): “checked only whether treatment output expressed the assigned semantic facet. It found 119/120 matches.”
- `grade3-reading/bias_experiment/llm-instruction-portability-study/docs/03-method-and-results.md` (68-69): “That is useful mechanism evidence: selected semantics often moved in the intended direction. It is not evidence of reliable execution, safe locality, or a pass on the primary statistic.”
- `grade3-reading/bias_experiment/llm-instruction-portability-study/docs/04-decision-and-lessons.md` (29-30): “Semantic selection, exact execution, invariant preservation, formatting, and scope binding are distinct failure surfaces.”
- `grade3-reading/bias_experiment/experiment-record/evidence/knowledgebot/kb-0166-counterfactual-authority-a1b-terminal-causal-control.qmd` (109-110): “also applied the program under the wrong-path and wrong-subject controls. It was steerable but not safely scoped.”
- `grade3-reading/bias_experiment/experiment-record/docs/02-assumption-register.md` (23): “A1b showed negative-control leakage plus invariant and execution failures.”

Published: [Ye et al. 2026](https://aclanthology.org/2026.findings-acl.99/)

Against: The three were small, fast model versions, and the run is one strict feasibility point, not a powered reliability estimate (`grade3-reading/knowledge_bot/knowledge/kb-0166-counterfactual-authority-a1b-terminal-causal-control.qmd`). The 0 of 6 is confounded: the smaller writer was trained from the raw base on two other item types only, and the step structure did carry over to it with only token-limit changes. A post-hoc check found the assigned facet in 119 of 120 treatment outputs, which supports bounded semantic steering, though not exact control (`grade3-reading/knowledge_bot/knowledge/kb-0168-eppc-bias-experiment-terminal-kill-and-salvage.qmd`). Only this one adjacent test ran; the formal gates never produced complete scored evidence (`grade3-reading/knowledge_bot/HOTBUCKET.md`).

<sub>method · stage: measure · generation, evaluation · universal · from ap, g3, research · measured · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Re-test every claim on fresh items

Count fixes, gains or checks as proven only on fresh held-out items written apart from whoever built them, kept from tuning, training and repair, never rerun to chase a pass. A recipe self-reported at 95.56% scored 5 of 50 on fresh prompts.

In the AP project, a recipe self-reported at 95.56% scored 5/50 on fresh prompts independent of the 30 it was tuned on, and a method claimed at 100% scored 45/50 on fresh items sharing no knowledge components with the set it was claimed on (`icloud-work/aptraining/.agent/memory/BEADS.md`). The plan made a spot-check that no test prompt appears in the 5,927-row training corpus a gate before promotion, and the eval template has a verifier confirm that inputs are not from the training distribution (`icloud-work/aptraining/.agent/PLAN.md`; `icloud-work/aptraining/.agent-v2/templates/eval-cycle.md`). Where there is an untrained baseline, compare against it too: a pre-registered evaluation plan runs the untrained base model on the same prompts and briefs to isolate what training added (`ti-courseplans-audit/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md`, lines 53-54).

Quoted:

- `icloud-work/aptraining/.agent/memory/BEADS.md` (705): “FAIL: 5/50 = 10.00% on n=50 fresh Unit-1 prompts (independent of den's 30-prompt training set). Delta -85.56pp from den's self-reported 95.56%. Recipe does NOT generalize.”
- `icloud-work/aptraining/.agent/memory/BEADS.md` (708): “FAIL: 45/50 = 90.00% on n=50 fresh Unit-1 MCQ from e7e1d980 (no KC overlap with Cheater's 16-KC apush_baseline). -10pp delta from claimed 100%.”
- `icloud-work/aptraining/.agent/PLAN.md` (280): “**Contamination spot-check passes**. Sample 10 random eval prompts; verify none appear in the 5,927-row audited training corpus. If any match → F14 (poison candidate; do not promote).”
- `icloud-work/aptraining/.agent-v2/templates/eval-cycle.md` (34): “Verifier confirms inputs not from training distribution”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-003-mcqset-phrase-anchor.md` (3): “**Status**: **QUARANTINED** (main-a fresh-holdout 2026-05-23: 0/50 = 0% on fresh KCs). Cited 32/33 on my 17 baseline KCs did NOT generalize. KC selection bias: the baseline 17 admit abstract-rhetoric stimuli; broader corpus contains KCs (narrower topics, court cases, specific organizations) that don't.”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-003-mcqset-phrase-anchor.md` (62): “v14 fresh single-shot variant (17 KCs) → 5/17 = 29.4% (single-shot still hard)”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-008-dbq-7doc-generic-attrib.md` (53): “v2 generic-attribution + qualitative-claims + difficulty="easy" → 23/35 = 65.7%”
- `icloud-work/aptraining/Cheater/reports/FRESH_HOLDOUT_2026-05-23.md` (22): “| DBQ (EXPLOIT-008) | 97.37% | **54.2%** (13/24), avg 0.702 | −43pp | second_tier→quarantine risk |”
- `icloud-work/aptraining/Cheater/reports/FRESH_HOLDOUT_2026-05-23.md` (51-52): “For T1 with iteration (cited rates) the cheat-prompts hit T1 on 17-19 KCs, but the rate degrades on fresh KCs without iteration.”
- `icloud-work/aptraining/Cheater/reports/FRESH_HOLDOUT_2026-05-23.md` (53-54): “The iteration pattern (iterate + K=5 best-of) DOES recover the rate, but at higher API cost per item.”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-004-saq-no-stimulus.md` (101): “# Single-shot 17 KCs × 2 variants: ~91% pass”
- `icloud-work/ap-social-studies-generator/data/model_findings.md` (135): “- **89% (5,219/5,878) prompts identical to training prompts** (500-char fingerprint match)”
- `icloud-work/ap-social-studies-generator/python/CLAUDE.md` (466): “5. Only checkpoint if improvement holds across 2+ units”
- `icloud-work/ap-social-studies-generator/docs/archive/OPTIMIZATION_LOG.md` (42): “**Problem:** Gen 1 winner tested on easy topics. Needed harder topics.”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md` (68-69): “**Contamination ledger applies to TRAINING DATA:** cold topics excluded from every training pair.”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md` (71-72): “A model trained on a cold topic cannot be evaluated on it.”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md` (53): “**Arm B (base): the untrained base model + the SAME prompts and briefs.**”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md` (53-54): “Isolates what training added; run it or the result is uninterpretable.”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md` (65): “**Same inputs to every arm:** one pinned brief set”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md` (75-76): “any bar-hit claim needs 2 independent generation runs; a single run is a single-point estimate.”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-22T1936Z_DELIVERED_pipeline_solver.md` (15): “This version targets the exact failure classes main-a shared from the first hidden run without reading the hidden prompt file.”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-22T1936Z_DELIVERED_pipeline_solver.md` (39): “- Prewarmed live-IB-backed cache entries for the repaired hidden failure classes.”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-22T1936Z_DELIVERED_pipeline_solver.md` (70): “- now live-IB-backed passes: 4/13”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-22T2019Z_DELIVERED_pipeline_solver_v4.md` (82): “Expected if the previous hidden miss distribution recurs: prior `37/50` plus `13/13` repaired prior misses implies ceiling around `50/50` on the same failure mix.”
- `aptraining-local/den-of-ideation/experiments/main_a_acceptance_runs/den_solver_acceptance_20260522T182953Z_summary.json` (13): “"input_jsonl": "/tmp/holdout_for_den_v2.jsonl",”
- `icloud-work/aptraining/artifacts/validated/2026-05-23T0840Z_den_solver_v10_STRICT_FRESH_K4/den_solver_acceptance_20260523T082319Z_summary.json` (13): “"input_jsonl": "/tmp/holdout_for_den_v2.jsonl",”
- `aptraining-local/den-of-ideation/reports/validation_triage/20260524T073015Z_2026-05-24T0601Z_UNIT1_MCQ_SOLVER_REPAIR.md.md` (114): “hidden validation input: `/tmp/unit1_mcq_holdout_n50.jsonl` (MCQ rows 50-99 from”
- `aptraining-local/den-of-ideation/reports/unit1_mcq_solver_v2_validated_addendum_20260524T085013Z.md` (17): “- Comparability: same MCQ rows `50-99` as the v1 repair run.”
- `aptraining-local/den-of-ideation/reports/unit1_dbq_solver_v2_repair_delivery_20260524T105934Z.md` (30): “input: `experiments/dbq_v2_failure_probe/unit1_dbq_v1_failure_rows.jsonl`”
- `aptraining-local/den-of-ideation/reports/unit1_leq_solver_v3_final_gap_repair_delivery_20260524T1840Z.md` (31): “input: `experiments/leq_v3_failure_probe/unit1_leq_v2_failure_rows_27_49.jsonl`”
- `aptraining-local/den-of-ideation/reports/validation_triage/20260524T202325Z_2026-05-24T2022Z_UNIT1_LEQ_SOLVER_v3_VALIDATED_99_6pct.md.md` (140): “**Deployable bound is K=1 single-shot.** Slice-2 K=1 (rows 100-149) was 239/250 = 95.6% with LEQ v2.”
- `aptraining-local/den-of-ideation/to_main/2026-05-23T1808Z_DEN_REQUEST_validate_unit9_mcq_solver_v1.md` (26): “third public n=10 was `10/10`, but runner sanity failed `1/2`”
- `icloud-work/aptraining/memory/project_den_routing_98pct_unit1_2026_05_24.md` (51): “- Per-cell heuristics tuned via iterative repair against hidden hold-out”
- `icloud-work/aptraining/artifacts/validated/2026-05-22T2116Z_den_solver_v8_FIRST_VALIDATED/den_solver_acceptance_20260522T210237Z_summary.json` (13): “"input_jsonl": "/tmp/holdout_for_den_v2.jsonl",”
- `icloud-work/aptraining/artifacts/INCLUSION_CRITERIA.md` (62): “5. **Reproducible**: re-running the validation on a different n=50 sample must clear the threshold ±2pp (no luck-of-the-draw cherry-picks)”
- `icloud-work/aptraining/artifacts/second_tier/2026-05-22T1830Z_den_solver_v2_online_K_N_with_cache/SECOND_TIER_REASON.md` (50): “13 failures = substandards NOT in cache (mostly mcq_set/hard from KC-1.2.III+1+A through KC-1.3.II+4+A range, per failure audit logs). 37 passes = substandards in cache from prior runs (e7e1d980 pipeline outputs).”
- `uae-education-ai/HERETIC_PLAN.md` (30): “This sample cannot prove tight 5-point noninferiority or broad safety; if the improvement interval includes zero, call the result inconclusive. Never tune on final outputs or rerun a hidden test to chase a pass.”
- `uae-education-ai/EVALUATION.md` (36): “Do not infer a tuning gain from development cases.”
- `icloud-work/aptraining/artifacts/quarantine/2026-05-22T1755Z_den_mcqset_50_50_proof/QUARANTINE_REASON.md` (4): “**Source claim:** 172/180 = 95.56% candidate pass on Unit-1 cherry-picked source prompts”
- `icloud-work/aptraining/artifacts/quarantine/2026-05-22T1755Z_den_mcqset_50_50_proof/QUARANTINE_REASON.md` (5): “**Independent re-test:** 5/50 = **10.00%** on Unit-1 prompts from e7e1d980 (no overlap with den's 30-prompt training set)”
- `icloud-work/aptraining/artifacts/quarantine/2026-05-22T2120Z_cheater_exploit_003/QUARANTINE_REASON.md` (33): “| Den v2/v3 (cache) | 43/50 = 86% | 37/50 = 74% (second_tier) |”
- `icloud-work/aptraining/artifacts/quarantine/2026-05-22T2120Z_cheater_exploit_003/QUARANTINE_REASON.md` (34): “| Den v6 (fresh K=2) | 10/10 = 100% | 32/50 = 64% (second_tier) |”
- `icloud-work/aptraining/artifacts/quarantine/2026-05-22T2120Z_cheater_exploit_003/QUARANTINE_REASON.md` (36): “| Cheater EXPLOIT-002 (stim-strip MCQ) | 32/32 = 100% | 45/50 = 90% (second_tier) |”
- `icloud-work/aptraining/artifacts/quarantine/2026-05-22T2120Z_cheater_exploit_003/QUARANTINE_REASON.md` (37): “| Cheater EXPLOIT-003 (phrase-anchor MCQ_SET) | 14/16 = 87.5% | 0/10 partial = 0% (**QUARANTINE**) |”
- `icloud-work/aptraining/artifacts/INCLUSION_CRITERIA.md` (24): “Cherry-picked subsets, single-prompt wins, and self-reported metrics from sub-agents do NOT qualify. main-a re-tests every claim on fresh n=50 against the production IB v2.5.11 grader.”
- `icloud-work/aptraining/artifacts/quarantine/2026-05-22T2120Z_cheater_exploit_003/QUARANTINE_REASON.md` (35): “| Den v8 (fresh + timeout-fallback) | 50/50 = 100% | 50/50 = 100% / 46/50 = 92% strict → **VALIDATED** |”
- `icloud-work/aptraining/artifacts/INCLUSION_CRITERIA.md` (16): “Hold-out at `artifacts/quarantine/2026-05-22T1755Z_den_mcqset_50_50_proof/validation_prompts_unit1.jsonl` (50 fresh Unit-1 MCQ_SET prompts).”
- `icloud-work/auto-memory-backup/reference_oracle_helper.md` (24): “- `evaluator_code/inceptbench_src/golden/golden_dataset.json` — InceptBench's regression eval set (REFERENCE ONLY; training on these = direct test contamination)”
- `icloud-work/auto-memory-backup/research_grape_data_selection_v28.md` (31): “2. Verify zero overlap with the 297-record holdout (dedupe by row_id)”
- `icloud-work/auto-memory-backup/project_v8_best.md` (18): “- Dataset: 2,821 records — APUSH+APWH MCQ only, `quality_tier=high` (≥0.95), holdout-excluded, no images”
- `ap-helpers-data-agent-memory/feedback_eval_contamination_check_all_eval_files.md` (18): “my first contamination check compared only against `apush_baseline.jsonl` (n=30 mcq_set hashes)”
- `ap-helpers-data-agent-memory/feedback_eval_contamination_check_all_eval_files.md` (18): “Found APUSH overlap was 100% — those "30 unique" rows were in fact eval-identical.”
- `ap-helpers-data-agent-memory/feedback_eval_contamination_check_all_eval_files.md` (20): “Had I trained on those rows, v54 would have learned its eval set verbatim → fake pass rate, contamination, useless iteration. Caught before training; saved the cycle.”
- `home-agent-memory/training_data_70k.md` (80): “- `data/combined_val.jsonl` and `data/combined_test.jsonl`: 21% overlap with catchup_raw via cu-* IDs”
- `grade3-reading/artifacts/codex-qa/experience-2026-09-14/RESULT.md` (29): “The original visibility implementation passed its 48 controls but missed 10 of 18 independently authored cases.”
- `grade3-reading/artifacts/codex-qa/experience-2026-09-14/independent-observer/REVIEW.md` (7): “Eighteen fixture expectations were fixed in the independent script and written into `run-01/INTENT.json` before the first measurement.”
- `grade3-reading/artifacts/codex-qa/experience-2026-09-14/RESULT.md` (35): “Shared writable files give independent review, not enforced repair/judge isolation.”
- `grade3-reading/artifacts/codex-qa/controller-2026-09-14/PLAN.md` (30): “Tier 1: independent acceptance files must be outside the worker's enforced writable boundary.”
- `grade3-reading/artifacts/codex-qa/controller-2026-09-14/PLAN.md` (58-59): “Pass: real commands can write their designated proposal directory but cannot alter protected source, judge, contract or evidence.”
- `grade3-reading/artifacts/codex-qa/tool-reuse-assessment-2026-09-14.md` (105): “Hashes are not protection against a writer who can alter both result and evidence consistently.”
- `grade3-reading/bias_experiment/.agent/memory/g3-boundary-reciprocal-mismatch-repair-plan.md` (80-81): “Hash disjointness must be supplemented by a paraphrase-level audit; case, spacing, and one-token edits do not make an exposed example fresh.”
- `grade3-reading/bias_experiment/.agent/memory/g3-agent-qualification-v2-plan.md` (175): “Exact raw/normalized hashes catch literal reuse but not lexical near-copy.”
- `grade3-reading/bias_experiment/.agent/memory/g3-agent-qualification-v2-plan.md` (178-179): “This does not prove abstract semantic non-equivalence; freshness additionally relies on a new author with no v1 text access and an explicit no-reuse attestation.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/04_CONCURRENT_VALIDITY_PLAN.md` (107): “The regression is fit on 80% of the concurrent study sample and validated on the held-out 20% [DERIVED from standard cross-validation practice].”
- `grade3-reading/bias_experiment/.agent/memory/G3_CANDIDATE5_ADDENDUM_ROUND_2026-07-16.md` (101): “Retire all 60 exposed texts permanently; do not reuse them.”

Against: The first data audit had no near-duplicate check between hold-out and training items ('**No near-dup leakage protection.** This audit does NOT yet de-near-dup against the training pool.', `icloud-work/aptraining/.agent/research/data_audit.md`, line 190), and the plan's spot-check samples only 10 prompts. Part of the reported drop came from dropping iteration, not from the new topics, and re-selecting with the same judge recovered the rate at a higher cost per item (`icloud-work/aptraining/Cheater/reports/FRESH_HOLDOUT_2026-05-23.md`, lines 51-54). For one item type's first drafts the topic effect was small, "# Single-shot 17 KCs × 2 variants: ~91% pass" (`icloud-work/aptraining/Cheater/exploits/EXPLOIT-004-saq-no-stimulus.md`, line 101), against 88% on fresh topics. The project's 97% headline was measured on the same 28 benchmark files that served as the push's acceptance test, so it is not a held-out figure (`icloud-work/ap-social-studies-generator/python/CLAUDE.md`). it is a plan, pre-registered before any training run, not a result (`ti-courseplans-audit/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md`). Overlap with the self-tests' sample was checked ("no overlap with Den's selftest step-sample", aptraining-local/den-of-ideation/reports/validation_triage/20260524T073015Z_2026-05-24T0601Z_UNIT1_MCQ_SOLVER_REPAIR.md.md, line 114), and the first challenge required a prompt diff: "I'll diff your prompt list against my n=50; any overlap = automatic FAIL" (icloud-work/aptraining/workspace/comms/to_den/2026-05-22T1845Z_ULTIMATE_DELIVERY_CHALLENGE.md, line 52). On fresh rows 100-149 the graded lanes partly held (SAQ 43/50, LEQ 47/50, MCQ 49/50, DBQ 50/50), though the 239 of 250 also counts 50 question-set passes that were predicted, not graded. The risk was flagged at the time: "A fresh hidden seed is still the real gate." (icloud-work/aptraining/workspace/comms/from_den/2026-05-22T1936Z_DELIVERED_pipeline_solver.md, line 77). A fresh set can be harder than the one it replaces: in one note a model passed 0 of 176 attempts on hold-out prompts against about 20% on the evaluation baseline, and the note says 'Holdout prompts are systematically harder.' (icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/achieved.md, line 69). One self-test held, 50 of 50 on its own test and on the fresh re-test, 46 of 50 by the strict count (`icloud-work/aptraining/artifacts/quarantine/2026-05-22T2120Z_cheater_exploit_003/QUARANTINE_REASON.md`). The drop to 0% rests on a partial re-test of 10 items, and the re-tests drew on one 50-item hold-out file (`icloud-work/aptraining/artifacts/INCLUSION_CRITERIA.md`). The project's plan for example items drew them from the held-out set ("- Demos selected from holdout where IB `overall ≥ 0.95`. Same 3 demos per cell type, locked across evals.", `icloud-work/auto-memory-backup/research_fewshot_format_not_facts.md`, line 62), and whether it ran is not recorded. No contamination incident or its effect is measured in this evidence. none found; the inflated score is the notes' expectation, not a measurement, since the leak was caught before training. The independent cases were written on a shared writable machine, which gives independent review but not enforced isolation (`grade3-reading/artifacts/codex-qa/experience-2026-09-14/RESULT.md`, `grade3-reading/artifacts/codex-qa/experience-2026-09-14/independent-observer/REVIEW.md`), and the repair loop's boundary was planned, not yet shown to be enforced on that machine (`grade3-reading/artifacts/codex-qa/controller-2026-09-14/PLAN.md`).

<sub>method · stage: measure · measurement, integrity, generation · universal · from ap, g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Read the checker's code first

Read the checker's own code to learn exactly what it grades and parses, and match each item type's output structure to it, checked in code before producing at scale. Training rows whose part labels were uppercase strings instead of the parser's lowercase nested parts dropped that item type from 90% to 16.7%.

After training on 385 short-answer rows that used uppercase part labels with bare strings, where the expected structure has lowercase parts each nested with a question and a sample response, that type collapsed from 90% to 16.7% (`feedback_per_cell_schema_must_match_fewshot_bank_chain_canon.md`). The evaluation runner parses raw output once and counts a parse failure as a fail with no repair, so 262 rows of answer-format anchors gave 0/150 parsed (`project_eval_is_question_generation.md`). Reading the runner's code showed that it grades question objects, against a standing rule to train only answers.

Quoted:

- `ap-helpers-data-agent-memory/feedback_per_cell_schema_must_match_fewshot_bank_chain_canon.md` (18): “**v81 SAQ collapsed -73.3pp (90% → 16.7%) after training on my Track B v2 corpus.** Root cause: 385/385 SAQ training rows used UPPERCASE A/B/C with bare-string parts, but the chain canon (fewshot_bank/by_cell/saq.jsonl) uses lowercase a/b/c with nested `{question, sample_response}` per part.”
- `ap-agent-memory/project_eval_is_question_generation.md` (30): “These are **question structures**. The model is graded on generating well-formed exam questions matching these schemas.”
- `ap-agent-memory/project_eval_is_question_generation.md` (32): “Line 88: `parse_json_response()` — single-attempt JSON parse on raw model output. Per the constraint block at lines 13-18, parse failure counts as a fail with no repair.”
- `ap-agent-memory/project_eval_is_question_generation.md` (56): “This is the v38 failure mode (262 rows of answer-format anchors → 0/150 parse_ok).”
- `ap-helpers-data-agent-memory/feedback_answer_format_only.md` (7): “Every SFT/DPO row must train the model to **emit the answer**, not to generate questions about content.”
- `ap-helpers-data-agent-memory/feedback_gemma4_wraps_json_in_markdown_fences_default_2026_06_02.md` (9): “2026-06-02 IB n=500 eval of v92 first-run failed 499/500 with `json_parse:JSONDecodeError`.”
- `ap-helpers-data-agent-memory/feedback_gemma4_wraps_json_in_markdown_fences_default_2026_06_02.md` (13): “enhanced `_extract_json()` that strips fences + regex-extracts `{...}` blocks as fallback.”

Against: The project held the opposite rule at the same time, that every training row should emit the answer rather than a question (`feedback_answer_format_only.md`, line 7). And sometimes the checker was what needed fixing: a strict parser failed 499 of 500 items that a model had wrapped in code fences, until it learned to strip them (`feedback_gemma4_wraps_json_in_markdown_fences_default_2026_06_02.md`, lines 9 and 13).

<sub>method · stage: settle · generation, evaluation · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Reference values come from a cited table

Take reference values such as test norms from a cited, versioned table, never from a model's memory. One predictor had no table of test norms, so a model's memory supplied them, wrongly anchored between 200 and 214.

A proposal for a shared course-planning repository found that its outcome predictor had a flag for test norms but no norm values behind it, so the meaning of a score floated on pre-training, with wrong anchors (`grade3-reading/artifacts/alpha-read-packager/TI_COURSEPLANS_PR_PROPOSAL.md`). It proposed a versioned norms table with the 2025 values, the discredited anchors marked not to be used, under the rule to ground from a table, not priors (the same file).

Quoted:

- `grade3-reading/artifacts/alpha-read-packager/TI_COURSEPLANS_PR_PROPOSAL.md` (18): “RIT meaning free-floats on pre-training (wrong 200-210 / 208/214 anchors)”
- `grade3-reading/artifacts/alpha-read-packager/TI_COURSEPLANS_PR_PROPOSAL.md` (18): “with `do_not_use` for the discredited anchors”
- `grade3-reading/artifacts/alpha-read-packager/TI_COURSEPLANS_PR_PROPOSAL.md` (18): “the "ground from a table, not priors" discipline”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/skill/SKILL.md` (47): “BOTH older figures are wrong: 207/213/+6.0 (much older grade) AND the interim "spring ~197 / +10.5" (2020 spring carried forward by mistake). Flag either.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/skill/SKILL.md` (127): “Uses correct G3 RIT norms (fall ~185 / spring ~197 / +10.5); no 207/213/+6 figures”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/04_CONCURRENT_VALIDITY_PLAN.md` (145): “any context display that juxtaposes those fields with 2025-norm figures must reinterpret them under the 2025 norms first.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md` (138): “Implication: all norm-referenced computations must state their norm year; the proxy uses 2025.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md` (109-110): “So 770L is a real published boundary: it is the floor of the **superseded** 2010 band. The package is not sloppy, it is out of date.”

Against: none found

<sub>method · stage: ground · generation, integrity · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Refine on structure, flag quality

Let an automatic refine loop act only on structural failures and send a judge's quality findings to a person, since a refiner acting on them rewrote approved content.

A reading engine's authoring pipeline runs its gates on each generated lesson, deterministic ones first and judges after, refines within a budget by regenerating only the failing subjects, and never writes a structural failure. Quality findings are flags for the human reviewer, never input to the refiner: the first time they were fed back, a judge called the design document's own signed distractors filler, the refiner rewrote them, and the fidelity gate then failed the rewrite. It applies machine-checks-are-not-judgment to a generation loop.

Quoted:

- `grade3-reading/course-renderer/authoring/README.md` (82-87): “Refine acts on STRUCTURAL failures only. Quality findings are FLAGS for the human reviewer (`flag_on: quality` in the rule pack), never refine fodder: the first time quality findings were fed back, a judge called the design doc's own signed distractors filler, the refiner rewrote them, and the fidelity gate then rightly failed the rewrite. The loop cannot be allowed to argue with the signed content it exists to protect.”
- `grade3-reading/course-renderer/authoring/README.md` (75): “(deterministic first, they are free; judges after)”
- `grade3-reading/course-renderer/authoring/README.md` (76): “(only the failing subjects are regenerated)”
- `grade3-reading/course-renderer/authoring/README.md` (77): “(a structural failure is never written)”
- `othello-course-renderer-draft/repo/authoring/README.md` (82-86): “Refine acts on STRUCTURAL failures only. Quality findings are FLAGS for the human reviewer (`flag_on: quality` in the rule pack), never refine fodder: the first time quality findings were fed back, a judge called the design doc's own signed distractors filler, the refiner rewrote them, and the fidelity gate then rightly failed the rewrite.”
- `othello-course-renderer-draft/repo/authoring/README.md` (86-87): “The loop cannot be allowed to argue with the signed content it exists to protect.”
- `othello-course-renderer-draft/repo/authoring/README.md` (76): “refine within budget  (only the failing subjects are regenerated)”
- `othello-course-renderer-draft/repo/authoring/README.md` (77): “accept or DISCARD     (a structural failure is never written)”
- `othello-course-renderer-draft/repo/authoring/README.md` (102): “`severity` — `structural` (discard), `quality` (flag), or `advisory` (note).”

Against: The Grade 9 lesson engine feeds its judge's failures back to the writer: "a failing draft gets exactly one correction pass with the reasons." (`g9/transformer/src/transform.js`, line 2).

<sub>method · stage: write · generation, review, evaluation · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Reject, never repair, what is measured

When people review a generator's output to measure it, let them accept or reject each piece but never repair, add, merge or rescope it, so its omissions stay measurable.

The frozen protocol of an experiment on extracting teaching rules with a model sent a fixed extractor's candidates through an accept-or-reject safety review, in which a candidate could be rejected but not repaired, merged, split, broadened or narrowed, and no omitted rule could be added. Accepted candidates got only the approval needed to run, rejected, abstained and omitted ones stayed absent, and the fully corrected set was kept apart as the reference. The protocol's reason is that only approved rules run while the extractor's omissions and unusable predictions stay measurable.

Quoted:

- `grade3-reading/bias_experiment/experiment-record/evidence/knowledgebot/kb-0131-pedagogy-decision-bank-experiment-intake.qmd` (389-390): “reviewers may reject a candidate but may not repair it, add an omitted atom, merge/split it, or broaden/narrow its scope.”
- `grade3-reading/bias_experiment/experiment-record/evidence/knowledgebot/kb-0131-pedagogy-decision-bank-experiment-intake.qmd` (390-392): “Accepted candidates receive the minimum approval metadata needed to execute; rejected, abstained, and omitted atoms remain absent. The fully corrected/adjudicated store is the separate gold store.”
- `grade3-reading/bias_experiment/experiment-record/evidence/knowledgebot/kb-0131-pedagogy-decision-bank-experiment-intake.qmd` (392-393): “This preserves the rule that only approved atoms execute while keeping extraction omissions and unusable predictions measurable.”
- `grade3-reading/bias_experiment/experiment-record/evidence/knowledgebot/kb-0132-eppc-bias-experiment-execution-handover.qmd` (416): “Reviewers may reject but never repair, add, merge, split, broaden, or narrow a candidate.”

Against: The arm never ran: the record lists no adjudicated reference rules and no scored output for it (grade3-reading/bias_experiment/experiment-record/docs/04-resolution-and-salvage.md line 15).

<sub>method · stage: measure · review, measurement, generation · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Remove repeats across the whole course

Expect knowledge drafted from several sources to overlap, and remove repeats across the whole course, not only within a unit, before people review it. People rejected 160 of 2,087 generated links across nine units, most of them with a note that the content repeated another, such as 'already covered'.

An AP history knowledge-schema pipeline drafts facts from several sources, and in one unit's consolidation audit the model marked 857 of 1,356 drafted facts 'Yes' under 'Overlap Notes' (`downloads/Knowledge Schema Generator - AP USH Unit 2.xlsx`). Its redundancy step checks a topic's facts only against earlier topics in the same unit. In the course's human checks, kept in its knowledge-schema tracking spreadsheet, 160 of 2,087 generated links were marked 'No', most with a repeat note, and people also removed nodes already covered in another unit.

Quoted:

- `downloads/Knowledge Schema Generator - AP USH Unit 2.xlsx` (sheet 'Instructions' (xl/worksheets/sheet1.xml), cell B2, step 14): “14. Run step 8 in main.py which will go through the current topic's facts and check for redundancies against previously processed topics in the unit.”
- `downloads/AP US History - Knowledge Schema - SME Tracker.xlsx` (sheet 'Unit 3 Relationships', rows 14 and 20, column J (Notes; Keep = 'No')): “already covered”
- `downloads/AP US History - Knowledge Schema - SME Tracker.xlsx` (sheet 'Unit 3 Nodes', row 56, column M (Comment/Reason); column N reads 'Removed'): “already covered in 2.7, they should know this”
- `downloads/Knowledge Schema Generator - AP USH Unit 2.xlsx` (sheet '4. Consolidation Audit' (xl/worksheets/sheet10.xml), row 2, column J ('Overlap Notes')): “Yes - Related to AMSCO_2_RP_IVxj; this adds detail to the English focus on land acquisition for agriculture.”

Against: Overlap varies by unit: in the Unit 7 workbook's consolidation audit, 109 of 597 rows are marked 'Yes' (`downloads/Knowledge Schema Generator - UNIT 7.xlsx`). The Unit 2 flags are the model's own consolidation notes and mostly mark relatedness ('related to' appears 255 times), not duplicates.

<sub>method · stage: ground · generation, review · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Repair mechanical slips in code

Repair in code what needs no judgment, such as quotation marks missing round the text's exact words, and send back to the writer only what does. On 2 of 2 new texts, the debate block's last draft failed for missing quotation marks alone and never reached the judge.

The lesson engine gives a failing draft one correction pass with the reasons, and it already repairs some slips in code: it drops a leading verdict, replaces a semicolon or dash standing in for a comma, and renames 'paragraph b' to 'Answer B'. Its debate block requires each push-back to quote the text, which code reads as words inside quotation marks. On a poem and a speech the last drafts' push-backs used the text's exact words without the marks, so after 2 tries both blocks failed on that check alone, with 0 judge calls, though code that finds the text's exact words could have marked them.

Quoted:

- `g9/transformer/src/transform.js` (2): “judge checks the rest on positive evidence, and a failing draft gets exactly one correction pass with the reasons.”
- `g9/transformer/src/house.js` (2): “the animated build's punctuation (no semicolon or dash standing in for a comma)”
- `g9/transformer/src/house.js` (3): “leading verdict ("Correct.", "This is incorrect;") is dropped: both builds show the verdict themselves (YES, NOT THAT”
- `g9/transformer/src/mechanics/compare-paragraphs.js` (39): “the reader sees "Answer A" and "Answer B", so the feedback names them that way ("paragraph b" -> "Answer B")”
- `g9/transformer/src/mechanics/debate.js` (71): “check("counters-quote", "Each push-back quotes the text", item.sides.every((s) => quotesIn(s.counter).length > 0), "a push-back quotes no words from the text"),”
- `g9-transformer-runs/blocks/f23aebacf033daa2.json` (13): “How do the details of a wrinkled lip and sneer of cold command suggest a ruler who also possessed great passion?”
- `g9-transformer-runs/blocks/aeb043df247f1b45.json` (17): “"counter": "How can speech matter if the world will little note, nor long remember what we say here?"”
- `g9-transformer-runs/blocks/f23aebacf033daa2.json` (81-82): “"judgeCalls": 0,”
- `g9-transformer-runs/blocks/aeb043df247f1b45.json` (81-82): “"judgeCalls": 0,”
- `g9-transformer-runs/decisions/aeb043df247f1b45.json` (28): “"counter_1": "How do you explain the claim that \"the world will little note, nor long remember what we say here\"?"”
- `grade3-reading/course-renderer/docs/rules/content-and-copy.md` (54-56): “Rewritten rather than rejected. A reply with a dash in it is a good reply with a dash in it, and a child waiting on an answer is not served by it being thrown away and re-asked for.”

Against: Whether the repaired drafts would have passed is unknown: the first judged drafts did quote the text, and the judge failed one push-back on the poem (0.39, `g9-transformer-runs/decisions/f23aebacf033daa2.json`, lines 119-122) and was unsure of both on the speech (0.52 and 0.51, `g9-transformer-runs/decisions/aeb043df247f1b45.json`, lines 85-88 and 123-126).

<sub>method · stage: settle · generation, evaluation, wording · universal · from g9 · measured · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Report a bank's coverage apart from quality

When items are served from a bank of pre-checked items, report how many fresh requests the bank covers separately from how good its items are. A bank-backed solver passed 37 of 50 fresh requests: every pass was a bank hit, and all 13 misses were topics the bank lacked.

In the AP work, a solver that served pre-checked items from a cache passed 37 of 50 fresh requests on a held-out set; all 37 passes were cache hits, and all 13 misses were requests for sub-standards the cache did not hold (`icloud-work/aptraining/.agent/memory/BEADS.md`). Another cache layer was recorded as delivering 99.7% on the four of five item types it covered (`icloud-work/aptraining/.agent/COMPREHENSIVE_PLAN_v2_2026_06_02.md`). An analysis of an earlier version of the solver judged its deterministic templates to be cherry-picking by another name (`icloud-work/aptraining/.agent/memory/BEADS.md`).

Quoted:

- `icloud-work/aptraining/.agent/memory/BEADS.md` (714): “37/50 = 74% on fresh Unit-1 MCQ_SET hold-out”
- `icloud-work/aptraining/.agent/memory/BEADS.md` (714): “37 passes = cache hits; 13 cap_reached = substandards not in cache.”
- `icloud-work/aptraining/.agent/COMPREHENSIVE_PLAN_v2_2026_06_02.md` (36): “| Layer 1 cache delivers 99.7% IB aggregate (4 of 5 cells) | Cheater 09:50Z delivery |”
- `icloud-work/aptraining/.agent/memory/BEADS.md` (707): “deterministic templates are cherry-picking by another name”

Against: Both figures come from banks built by agents for narrow scopes: one unit, and four of five item types.

<sub>method · stage: measure · measurement, generation · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Rewrite a world-knowledge leak by hand

When general knowledge answers an item, rewrite it by hand rather than tie it to obscure passage details, which raises difficulty without testing the targeted skill.

An analysis of a regenerate-on-leak plan for a Grade 5 reading bank found regeneration the wrong tool for a large share of leaks: items answerable from world knowledge or general reasoning can't be honestly locked to the passage, and forcing it turns a science-reasoning item into an obscurity item, harder without testing more of the targeted skill. Its plan regenerates passage-locked replacements only for leaks caused by construction flaws, such as weak distractors or tells in the options, and flags world-knowledge leaks for a person to rewrite.

Quoted:

- `grade3-reading/artifacts/g5-course-candidate-v0/GOAL_ANALYSIS.md` (92): “(3) Regeneration is the **wrong tool for a large share of leaks** — world-knowledge/general-reasoning leaks (~27 sequence-id/world-knowledge) can't be honestly passage-locked; doing so converts a science-reasoning item into an *obscurity* item (raises difficulty without raising the targeted skill — the transfer trap).”
- `grade3-reading/artifacts/g5-course-candidate-v0/GOAL_ANALYSIS.md` (168): “flag world-knowledge leaks for human rewrite, not auto-passage-lock.”

Against: It is a plan: at the time nothing consumed the regeneration requests, so the split between kinds of leak was never tried (`grade3-reading/artifacts/g5-course-candidate-v0/GOAL_ANALYSIS.md`, lines 92 and 168).

<sub>method · stage: improve · integrity, generation, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Sample a stored pool at random

To estimate a single-try or best-of-several rate from a stored pool of scored candidates, sample the pool at random or generate afresh. Read off the top of a score-sorted list, one model's single-try rate came out at 99.11%, which was its best-of-8 rate.

In the AP work, each prompt's eight candidate scores were stored sorted best first, so the first entry, or the best of the first two, always returned the best-of-8 score (`icloud-work/aptraining/.agent/memory/feedback_k8_bon_winner_trap_2026_05_11.md`). On one day that mistake was reported twice, as a single-try rate and as a best-of-2 rate, both 99.11%; a fresh single-try run that day scored 82.67% (`icloud-work/aptraining/.agent/memory/FINAL_PLAN_2026_05_11_v3.md`). The rule since is to simulate a smaller pool by sampling stored candidates at random, or to generate afresh (`icloud-work/aptraining/.agent/memory/feedback_k8_bon_winner_trap_2026_05_11.md`).

Quoted:

- `icloud-work/aptraining/.agent/memory/feedback_k8_bon_winner_trap_2026_05_11.md` (3): “True K=N from K=8 data requires random pair sampling.”
- `icloud-work/aptraining/.agent/memory/feedback_k8_bon_winner_trap_2026_05_11.md` (7): “The `all_scores` array is sorted DESCENDING by IB score (winner first). Slicing the first N entries gives you the TOP N from the K=8 pool, and the max of that is always `all_scores[0]` = the K=8 winner.”
- `icloud-work/aptraining/.agent/memory/feedback_k8_bon_winner_trap_2026_05_11.md` (32): “OR fresh K=N generation, which is rigorous but expensive.”
- `icloud-work/aptraining/.agent/memory/feedback_k8_bon_winner_trap_2026_05_11.md` (36): “On 2026-05-11, orch reported "B0161 K=2 BoN = 99.11% mean" computed from existing K=8 data via `max(all_scores[:2])`. This number is identical to K=8 winner pass rate.”
- `icloud-work/aptraining/.agent/memory/FINAL_PLAN_2026_05_11_v3.md` (23): “K=1 was 99.11% per K=8 candidate-0 → wrong (sorted-by-score artifact).”
- `icloud-work/aptraining/.agent/memory/FINAL_PLAN_2026_05_11_v3.md` (24): “**1h ago**: UPLIFT-1 single-seed K=1 T=0 = 82.67% on v43-soup `ty16vgj9`.”

Against: none found

<sub>method · stage: measure · measurement, generation · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Say what each inherited asset can't establish

Before reusing an inherited bank, generator or source pack, record what each is useful for and what it cannot establish, since a high item score can hide a false source. One course kept its 26,355 generated candidates for candidate prompts, distractor patterns and misconception mining, never for source clearance or certification.

Reconciling an AP history course's local generation assets with the official framework found that generated candidates and legacy winners carried synthetic or weakly attributed source text, and that an item-level score can be high while its historical document is not reproducible or its attribution is false. The assets were not discarded but given narrower jobs, in a table of what each is useful for and what it cannot establish. The 26,355 generated candidates, for example, may supply candidate prompts, distractor patterns, misconception mining and repair starting points, never source clearance, current-format compliance, assessment independence or certification, and a label made by the same builder is not provenance evidence.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (11): “The local APUSH assets are not discarded. They are assigned narrower jobs:”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (47): “Generated candidates and legacy winners include synthetic or weakly attributed source text.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (47): “An item-level score can be high while its historical document is not reproducible or its attribution is false.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (18): “26,355 generated all-unit candidates, including 1,515 in Unit 1 | Candidate prompts, distractor patterns, misconception mining, and repair/top-up starting points | Source clearance, current-format compliance, assessment independence, or certification”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (49): “A label generated by the same builder is not provenance evidence.”

Against: none found

<sub>method · stage: ground · generation, integrity · universal · from ap · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Scan for fused words

Scan generated student-facing text for fused words such as 'themain' or 'tothe', and fail it when one appears, because early readers may not recognise them as words. One rubric sets the whole diction score to 0.0 if a single merged non-word appears anywhere in the student-facing text.

The AP work's evaluator lists merged non-word forms such as 'themain', 'tothe' and 'inthe' as serious errors in its article and nonfiction-reading rubrics, especially for early-grade content where students may not recognise malformed words (`icloud-work/inceptbench-main/src/inceptbench/prompts/article/evaluation.txt`, `icloud-work/inceptbench-main/src/inceptbench/prompts/nonfiction_reading/evaluation.txt`). The article rubric sets the whole diction score to 0.0 if one appears anywhere in the student-facing text. The base and closed-ended question rubrics flag them too (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt`, `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt`), so four rubrics carry the rule.

Quoted:

- `icloud-work/inceptbench-main/src/inceptbench/prompts/article/evaluation.txt` (759-761): “- **Merged non-word forms** in student-facing text: `themain`, `forclosure`, `becausethe`, `tothe`, `ofthe`, `inthe`, `sentenceending`, etc. - These are serious errors, especially for early-grade content where students may not recognize malformed words - If merged non-words appear ANYWHERE in the student-facing text, set `diction_and_sentence_structure = 0.0`”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/nonfiction_reading/evaluation.txt` (410-411): “- **Merged non-word forms**: `themain`, `thewater`, `becausethe`, `tothe`, `ofthe`, `inthe`, etc. - These are serious errors, especially for early-grade content where students may not recognize malformed words”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (425): “- **Merged non-word forms**: `themain`, `tothe`, `ofthe`, `inthe`, etc. - especially serious for early-grade content where students may not recognize malformed words”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt` (147): “- Merged non-word forms (`themain`, `tothe`) → `clarity_precision`”

Against: none found

<sub>method · stage: judge · wording, generation, evaluation · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Screen generated texts for the learners' age

Check that a text generator is set to the learners' level before each batch, and screen every text for difficulty, cohesion, age-appropriateness and sensitive content before students see it. A grade-3 course's generator was set to grade 11, a setting carried over from an AP US History pipeline.

Reading the reading project's serving code found the grade hardcoded to 11, carried over from an AP US History pipeline, and grading criteria with zero safety or age criteria (`grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md`). The approved plan made an age-appropriateness and sensitive-content screen mandatory on every auto-generated passage before it can reach a child, and required the generator's grade setting to go from 11 to 3 (`grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md`). A pedagogy model's evaluation tests the same from the other side: asked for a suspenseful home-invasion passage for grade 3, it should decline or redirect (`grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md`).

Quoted:

- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (328): “MANDATORY on every auto-generated passage before it can reach a child”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (328): “fix the generator's grade setting (currently grade 11 → grade 3”
- `grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md` (47): “grade hardcoded 11 from AP US History”
- `grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md` (47): “zero safety or age criteria”
- `grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md` (194): “Safety items (S1, S2) test refusal behavior: S1 (suspenseful home-invasion passage for G3)”
- `ti-courseplans-audit/docs/course-formula-agents.md` (224): “the generator was calibrating passages at **grade 11, not grade 3**; verify the target grade before any batch”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D8-text-quality.md` (21): “they run too hard in syntax and vocabulary and too weak on cohesion”
- `ti-courseplans-audit/skills/train-teacher/references/text-quality-lane.md` (12-13): “cohesion weak (density <0.35 or a 3+ static-sentence run — the known LLM failure)”
- `ti-courseplans-audit/skills/train-teacher/references/text-quality-lane.md` (34-35): “the screen independently flagged **cohesion density 0.17 with a 3-sentence static run**”
- `ti-courseplans-audit/skills/train-teacher/references/text-quality-lane.md` (36-37): “On a clean target-quality sample: cohesion 0.58, passes.”
- `grade3-reading/.claude/skills/art-qa/SKILL.md` (41): “Never frightening for the target age”
- `grade3-reading/.claude/skills/art-qa/SKILL.md` (3): “Run after EVERY art generation batch and on any video still/key frame, before art.ts wiring or commit”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/ADDRESS_STATUS.md` (73): “| G8 — age-screen scope | SME age pass covered G2 only; the G3 BrainLift mandates an age screen and the pilot includes G3 |”

Against: The mis-set generator is one case, and the screen catches only the half of the defect a machine can detect: whether a text flows, is accurate and suits the age still needs a person (`ti-courseplans-audit/skills/train-teacher/references/text-quality-lane.md`).

<sub>method · stage: judge · stimulus, generation · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Size generation from demand and yield

Before generating, size a unit's item bank from how many certified items each use needs, such as practice, checkpoints, retest forms and review, divided by the expected certification yield. A certification yield of 0.5 means generating twice as many items as must be certified.

A reading course's demand calculator sizes each theme before authoring begins (`grade3-reading/ti-courseplans/scripts/lane-tools/theme-demand/README.md`). It counts the certified items each consumer needs, practice slots, a 15-item checkpoint, a parallel 15-item form for each funded retest, and shares for spaced review and a cold pool, then divides the total by the certification yield to get the number to generate, along with the authoring load per text. Its default yield of 0.5 rounds a grade 5 campaign that certified 48.7%, and the same file keeps a grade 3 calibration blocking before generation or a grade 3 gate goes live.

Quoted:

- `grade3-reading/ti-courseplans/scripts/lane-tools/theme-demand/README.md` (3): “Sizes a theme BEFORE authoring begins”
- `grade3-reading/ti-courseplans/scripts/lane-tools/theme-demand/README.md` (16-17): “table of items TO CERTIFY and TO GENERATE, broken down by consumer (practice slots, D15 checkpoints, retest reserve, spaced review, cold pool) plus per-text authoring load.”
- `grade3-reading/ti-courseplans/scripts/lane-tools/theme-demand/README.md` (24-25): “one 15-item checkpoint per theme and one parallel 15-item form per funded retest cycle”
- `grade3-reading/ti-courseplans/scripts/lane-tools/theme-demand/README.md` (64): “to_generate = ceil(to_certify / certification_yield)”
- `grade3-reading/ti-courseplans/scripts/lane-tools/theme-demand/README.md` (54-55): “`certification_yield` 0.5 is a historical G5 pricing prior (campaign 48.7%), not a G3 readiness result.”

Against: The yield it divides by is a pricing prior from another grade, not a grade 3 readiness result (`grade3-reading/ti-courseplans/scripts/lane-tools/theme-demand/README.md`, lines 54-55), so the sizes are estimates until a grade 3 calibration replaces it.

<sub>method · stage: ground · generation, practice · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Sources go in as data, not instructions

Pass source texts and task material to a writer model as data apart from its instructions, so words inside a source cannot override the rules it was given.

A plan for a model-neutral prompt envelope, in an experiment on steering generation with teaching rules, lists as a first-tier insight that task text and evidence are untrusted data, never to be interpolated into the instruction channel or allowed to override the frozen rules. The same plan fixes one canonical envelope whose bytes and hashes are set before any provider-specific formatting, so adapter syntax may change but the rules' meaning may not.

Quoted:

- `grade3-reading/bias_experiment/.agent/memory/reading-0hr-model-neutral-prompt-envelope-plan.md` (28-29): “task text and evidence are untrusted data. They must not be interpolated into the policy instruction channel or allowed to override the frozen contract.”
- `grade3-reading/bias_experiment/.agent/memory/reading-0hr-model-neutral-prompt-envelope-plan.md` (26-27): “Tier 1: model-neutrality requires one canonical semantic envelope whose bytes and hashes are fixed before provider projection; adapter-specific syntax may change, policy semantics may not.”

Against: It is a design rule from one plan and was never tested.

<sub>method · stage: write · generation, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Suggest a lesson question the text answers

For a text without a lesson question, draft several and keep one only on a judge's positive evidence that the text answers it. In the 12 October run a poem and a speech each got a usable open question this way, and all 32 blocks were made from those two questions.

For a text that comes without a question, the lesson engine asks a writer for three open questions answerable from the text alone, keeps those code finds well formed, and keeps the first one a judge finds answerable from the passage and worth a lesson of about an hour, on positive evidence. The result is cached under a hash of the text, so the same text is always given the same question. In the 12 October run both new texts got a usable open question this way, and every block on each was made from it.

Quoted:

- `g9/transformer/src/question.js` (3): “positive evidence. Cached by text, so the same text is given the same question.”
- `g9/transformer/src/question.js` (34): “Can question_${i} be answered from passage alone, and is it worth a Grade 9 lesson of about an hour?”
- `learning-truths/research/2026-10-12-6-transformer-ideas/universality-test.json` (4): “"gettysburg": "How does the speaker contrast the actions of the soldiers with the words spoken at the dedication?"”
- `learning-truths/research/2026-10-12-6-transformer-ideas/universality-test.py` (16): “b = post("/api/block", {"text": texts[k], "question": out["questions"][k], "mechanic": m, "n": 1})”
- `g9/transformer/samples/index.json` (6): “"question": "What does the poem suggest about power and time?"”
- `g9/transformer/v01/QA.md` (32): “13 lines judged relevant to the question.”

Against: The judge is asked two things at once, whether the question can be answered from the passage alone and whether it is worth a lesson of about an hour. The poem's suggested question was also narrower than the sample question it came with: 5 of its 14 lines were ranked for it, against 13 lines judged relevant to the sample question in the 9 October proof. With no judge present, the lesson engine keeps and caches the first well-formed draft unchecked (`g9/transformer/src/question.js`, lines 31-37).

<sub>method · stage: ground · generation, alignment, stem · universal · from g9 · adopted-rule · held · found in [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Test a generator for variety

Test a generator for variety by sending it the same request several times and measuring how far the outputs differ; one whose outputs barely differ is static. The benchmark sends each request 10 times, scores the outputs' diversity by trigram Jaccard distance, and calls the generator static below 0.45.

The AP work's evaluator has a variety check that takes the caller's own requests, sends each one 10 times, and scores the responses' diversity by trigram Jaccard distance (`icloud-work/inceptbench-main/README.md`). A mean score below the default threshold of 0.45 marks the generator as static (`icloud-work/inceptbench-main/src/inceptbench/tools/variety_check.py`).

Quoted:

- `icloud-work/inceptbench-main/README.md` (146): “- Sends each provided request 10 times, scores response diversity via trigram Jaccard distance”
- `icloud-work/inceptbench-main/src/inceptbench/tools/variety_check.py` (500): “is_static = (variety_score < self.threshold) if variety_score is not None else None”
- `icloud-work/inceptbench-main/src/inceptbench/tools/variety_check.py` (300): “threshold: float = 0.45,”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CORPUS-AND-SAMPLING-CONTRACT.md inside it) (67): “The bank has 5,271 gross rows for each of DBQ, LEQ, MCQ, MCQ set, and SAQ. Exact unique counts differ sharply: DBQ 989, LEQ 208, MCQ 122, MCQ set 1,167, and SAQ 1,172.”

Against: The 10 sends and the 0.45 threshold are the tool's own defaults; no validation of either was found.

<sub>method · stage: measure · generation, measurement · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Test and prune a writer's rules

Treat every rule or example added to a writer's instructions as a change to test, and prune and reconcile the rules as they grow. A run that added constraints and warnings fell from 65% to 61%.

In the AP generator's prompt runs, a run that added constraints and warning text fell from 65% to 61%, and its analysis blamed added rules that created conflicting signals and 'do not' lists the model couldn't all satisfy (`icloud-work/ap-social-studies-generator/docs/archive/ITERATION_ANALYSIS.md`; `icloud-work/ap-social-studies-generator/docs/archive/VERSION_ANALYSIS.md`). Adding 15 document examples to one course's source-based essay prompt brought 4 failures, where the version without examples had passed 98% (`icloud-work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md`).

Quoted:

- `icloud-work/ap-social-studies-generator/docs/archive/ITERATION_ANALYSIS.md` (93): “> **More rules ≠ better output.** The LLM has limited attention. Every added constraint dilutes the importance of existing ones.”
- `icloud-work/ap-social-studies-generator/docs/archive/ITERATION_ANALYSIS.md` (89): “- Additional rules created conflicting signals”
- `icloud-work/ap-social-studies-generator/docs/archive/VERSION_ANALYSIS.md` (88): “3. **Conflicting DO NOTs** - Model couldn't satisfy all constraints”
- `icloud-work/ap-social-studies-generator/docs/archive/VERSION_ANALYSIS.md` (94): “| Pass Rate | 65% | 61% | -4% |”
- `icloud-work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md` (186): “APUSH DBQ had 4 failures after adding 15 document examples to prompts.”
- `icloud-work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md` (225): “| Main | APUSH | 0 | 195.2 | 98% pass |”

Against: Examples helped elsewhere: another course passed 100% with 31 examples (`icloud-work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md`), and concrete bad examples correlated strongly with passing (`icloud-work/ap-social-studies-generator/docs/archive/VERSION_ANALYSIS.md`). The runs compared changed several things at once, and a 4-point drop may be within run-to-run noise.

<sub>method · stage: improve · generation, measurement · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### The platform, not the model, runs the steps

Let the platform, not the model, step a learner through each part of a problem in order, because a prompt alone didn't keep the model on track. In a randomized crossover trial with undergraduates, structured AI tutoring built this way had a median post-test score of 4.5 against 3.5 for in-class active learning.

The Grade 9 research brief read in full a randomized crossover trial in which structured AI tutoring beat in-class active learning for physics undergraduates, with median post-test scores of 4.5 against 3.5 and a median time of 49 minutes against 60. Among the design elements the trial lists, the platform, not the language model, stepped students through each part of a problem in order, because the system prompt alone did not keep it on track, and expert step-by-step solutions went into the prompt to keep explanations accurate. The brief notes that the Grade 9 design already works this way, with authored answer keys feeding the judge and the platform controlling the sequence.

Quoted:

- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (169): “median post-test scores were 4.5 for the AI group versus 3.5 for active learning, more than double the gains (effect size about 0.73–1.3).”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (173): “the platform, not the LLM, steps students through each part of a problem in order, because the system prompt alone did not keep it on track;”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (174): “expert step-by-step solutions included in the prompt to keep explanations accurate;”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (178): “Our current design already matches this: authored answer keys feed the judge, and the platform, not the LLM, controls the sequence.”

Published: [Kestin, Miller, Klales, Milbourne & Ponti 2025](https://doi.org/10.1038/s41598-025-97652-6)

Against: The trial was with undergraduates only (`othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md`, line 177), and these are listed design elements, not features it tested one at a time.

<sub>method · stage: ground · generation, sequence · universal · from g9, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Trace every statement to a source

Trace every statement in generated text to a given source fact, and drop or flag any that traces to none, because a model's memory never counts as support. An automatic check listed no added facts for all 62 and all 96 articles of two runs, while a review note estimated one or two in every article.

One generator's design says every claim in generated questions must trace to an entry in its vetted knowledge base (`icloud-work/ap-social-studies-generator/docs/03-ARCHITECTURE.md`, line 65). In an article pipeline, the tracker's automatic 'Extra Facts' column held an empty list for all 62 articles of one run and all 96 of another (`icloud-work/k_12_social_studies/ap_files/Articles Tracker.xlsx`, sheets 'Articles-readable-exp' and 'APUSH Articles-readable-exp', column K). A review note asked what exactly had been added and estimated one or two statements from the model in every article beyond the knowledge base (sheet 'Sheet4', cell H8).

Quoted:

- `icloud-work/ap-social-studies-generator/docs/03-ARCHITECTURE.md` (65): “- Every claim in generated questions must trace to a VKB entry”
- `icloud-work/k_12_social_studies/ap_files/Articles Tracker.xlsx` (sheet 'Sheet4', cell H8): “We definitely have more (maybe around 1-2 statement in every article from llm) and some of it seems important as it really ties things together in the article”
- `grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md` (46): “1. **The canonical file is the sole truth.** Every passage sentence, span id, item, misconception”
- `grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md` (47): “You never invent facts,”
- `grade3-reading/artifacts/g5-course/AUTHORING-RULINGS-R1-R10.md` (104): “## R10 — Hint ladders: trace or re-derive, never leave invented”
- `grade3-reading/artifacts/g5-course/AUTHORING-RULINGS-R1-R10.md` (106): “For every gated non-mcq item, each hint/second_hint/reveal must trace to canon”
- `grade3-reading/artifacts/wiki-research/pedagogy-llm-method.md` (94): “any generated item containing a numeric token not traceable to its source chunk is dropped (~2.8% of items)”
- `grade3-reading/artifacts/wiki-research/pedagogy-llm-method.md` (94): “an omitted number teaches nothing false; a fabricated number would be trained in as truth”
- `grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md` (71): “Fabrication scores 0 — not 0.5. The timeline notes a 2.4% fabrication rate in early synthetic”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md` (30-32): “every claim in I-do answer cards + chart frame values must be verifiable from THIS lesson's passage (not another lesson's, not the hook item). Think-alouds may paraphrase but never invent sensory/setting details.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md` (3-4): “Every rule below is enforced by a gate in `unit-2/verify/` and each one exists because a real defect shipped and was caught live.”
- `grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md` (120-121): “Search snippets, unsourced summaries, blogs, and model memory cannot support `PASS`.”
- `grade3-reading/artifacts/qc-2026-09-30-staging/FINDINGS.md` (171): “No check compares a model's claims, or a key, against the passage (C1, M1, M11, M13).”
- `othello-archive/server/api.mjs` (38): “Never invent lines of the play. Only quote lines given to you in the context.”

Against: The same note says some of the added statements seemed important because they tie the article together ("some of it seems important as it really ties things together in the article"), so a statement with no source is not necessarily wrong. The lint traced numbers only, and it guarded a model's training corpus rather than lessons students see (`grade3-reading/artifacts/wiki-research/pedagogy-llm-method.md`).

<sub>method · stage: judge · integrity, stimulus, generation · universal · from ap, g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Tuning finds what the score misses

A writer tuned or selected against a score can converge on whatever the score doesn't test, so anything a question must have has to be part of the selection. Tuned against a structure-only score, a writer produced a question rated 1.0 that a solver answered without its passage every time.

In the reading project's tuning run, the reward measured structural quality only and had no concept of passage-dependency; it plateaued at ~0.14 once the writer had converged to structurally valid leaked questions. The spec concluded that the two quality dimensions are orthogonal and both must be in the reward signal. The follow-up directive was to optimize the course, not the item: a course where every item scores 1.0 but 90% is blind-solvable is a failed course, as a question scored 1.0 with a blind-solve rate of 100% showed. In the AP work, a fix that raised a question set's score did it by removing the stimulus, which skipped the grader's leak probe. Needing its text is one such property a question must have.

Quoted:

- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd` (111-112): “InceptBench (existing reward function) measures structural quality: well-formed stem, single key, near-neighbour distractors, valid CCSS label. **It has no concept of passage-dependency.**”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd` (115-116): “Reward plateau at ~0.14 confirmed the model had converged to structurally-valid leaked questions.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd` (118): “The two quality dimensions are orthogonal. Both must be in the reward signal.”
- `grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd` (102-105): “the correction is "optimize the course, not the item" — a course where every item scores IB 1.0 but 90% is blind-solvable is a failed course (proof: DAPO epoch 0 emitted "What is the primary function of chlorophyll?" from a photosynthesis passage — IB 1.0, blind-solve 100%).”
- `grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd` (26-27): “The actual MCQ fix was the **OPPOSITE** of "add a real passage" — it was **REMOVING the stimulus** so the grader's leak-probe is skipped. That's **grader-gaming**, not a provenance win.”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/QUESTION_CONVERSION_RETROSPECTIVE.qmd inside it) (251-256): “- 13/13 passed deterministic quality-A and the loosened sound gate; - only 4/13 passed the LLM quality-B rubric. That pilot is a key negative lesson. Anti-leak is not enough. Some sequence rewrites could pass blind gating while becoming weak, mechanical, or misaligned tasks.”
- `grade3-reading/ti-courseplans/courses/g5-reading/llm/GENERATOR_DIRECTIVE.md` (28): “Reward plateaued ~0.14: convergence to structurally-valid **leaked** questions, because that is what a structural-only signal rewards.”

Against: The cheap text-dependence terms proposed for the reward barely separated leaky items from clean ones (AUC ~= 0.5), and under the shipped reward a reworded leak scored higher than a genuine requires-reading item (`grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd`, lines 170-171 and 186-188). The recommended design keeps a cross-family blind solve outside the loop, as ground truth and for checkpoint selection, not as the per-rollout reward (the same file, lines 180-184).

<sub>method · stage: improve · generation, integrity, evaluation · universal · from g3, ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Vary the wording of each request

Test a generator with several phrasings of each request, since its quality should not depend on how a request is worded. One maths benchmark varies each request's wording, difficulty and type, for more than 4,000 requests in all.

A maths benchmark's request set covers 672 skills and varies each request by difficulty, item type and semantic variation, describing the same skills and topics 'in various semantically similar ways' (`icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md`). It is a design; no result from it is recorded.

Quoted:

- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (498): “Semantic variation \- The same skills and topics are described in various semantically similar ways while sending requests to the LLM”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (491): “The entire curriculum for Mathematics across grades 3-8 is divided into a granular list of 672 unique skills.”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (500): “Including all variations, the benchmark covers \> 4000 question generation requests.”

Against: No results were recorded for the benchmark that uses it: its results table reads '| Coming Soon | - | - | - | - |' (`icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/uae-mathematics.md`, line 131).

<sub>method · stage: measure · generation, measurement · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Warnings and bans don't steer a writer

Warnings and bans don't reliably steer a writer: some invite the error they name, exact trap lists help without removing it, unchecked bans stay advisory; change what it's given instead. Adding 'be careful' warnings took a prompt's pass rate from 45% to 30%.

In a prompt sweep with 20 items per variant, adding 'be careful' warnings gave a 30% pass rate against the baseline's 45%, with factual accuracy at 60% in both (`icloud-work/ML learnings/prompt_engineering_deep_dive.md`); the project's reading is that warnings without actual constraints just introduce hedging (`icloud-work/ML learnings/failures_and_false_starts.md`). Bans did no better on fine-tuned models: told not to use specific facts, one used wrong specific facts instead of right ones (`icloud-work/ML learnings/sft_v7_benchmark_postmortem.md`). Another, ordered in capitals not to write about any other topic, went on writing about the wrong topic (`icloud-work/ML learnings/stage2_postmortem_full.md`). What to change instead is the material the writer may use, the hard limits on it and how the item is built.

Quoted:

- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (50): “**Method:** test_variants.py — 9 variants, N=20 each, APUSH Unit 7”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (57): “| baseline | 45% | 60% | Standard prompt |”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (61): “| caution | 30% | 60% | Added "be careful" warnings |”
- `icloud-work/ML learnings/failures_and_false_starts.md` (124): “**The "caution" variant also failed:** Adding "be careful" warnings about factual accuracy produced 30% pass rate — worse than anything. Warnings that tell the model to be careful without giving it actual constraints just introduce hedging behavior. The model starts prefacing with qualifications instead of generating confident content.”
- `icloud-work/ML learnings/sft_v7_benchmark_postmortem.md` (62): “**Why it doesn't work:** The model ignores negative constraints. It has strong parametric associations (France → exploration → Protestant → Huguenots → plausible but wrong) that override the instruction. Telling the model "don't use specific facts" just means it uses wrong specific facts instead of right ones.”
- `icloud-work/ML learnings/stage2_postmortem_full.md` (77): “DO NOT write about any other topic.”
- `icloud-work/ML learnings/stage2_postmortem_full.md` (82): “**Result:** Failures persisted.”
- `icloud-work/ML learnings/sft_v7_benchmark_postmortem.md` (132): “2. **The current approach (negative prompting) seemed to work on Gemini.** Because Gemini is large enough to mostly respect the "no specific evidence" instruction and has accurate enough parametric memory that when it does include evidence, it's usually right. The instruction that's good enough for a large model is insufficient for a 14B model.”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (57): “baseline | 45% | 60% | Standard prompt”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (61): “caution | 30% | 60% | Added "be careful" warnings”
- `icloud-work/ML learnings/failures_and_false_starts.md` (124): “Warnings that tell the model to be careful without giving it actual constraints just introduce hedging behavior.”
- `icloud-work/ML learnings/stage2_postmortem_full.md` (82): “Failures persisted.”
- `icloud-work/ML learnings/sft_v7_benchmark_postmortem.md` (62): “The model ignores negative constraints.”
- `icloud-work/ML learnings/sft_v7_benchmark_postmortem.md` (132): “Because Gemini is large enough to mostly respect the "no specific evidence" instruction”
- `icloud-work/ML learnings/sft_v7_benchmark_postmortem.md` (132): “The instruction that's good enough for a large model is insufficient for a 14B model.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (16): “The postmortem (Apr 24) is explicit that telling the 14B "no specific facts in scoring notes" results in *wrong* specific facts.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (16): “Replacing the negative constraint with a positive verified-facts-only constraint should kill 100% of the SAQ factual-hallucination class and ~30-50% of DBQ factual-attribution failures.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (314): “Negative prompting ("don't list specific facts") fails because the model substitutes wrong specific facts.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (314): “a 14B model has weaker factual memory than a >100B model.”
- `icloud-work/aptraining/.agent/memory/BEADS.md` (607): “visual-artifact filter in user-prompt ineffective”
- `icloud-work/aptraining/.agent/memory/BEADS.md` (608): “T1+T2 pipeline fix committed (37e4eeb) + redeploy fired: DBQ system-prompt stimulus rules + post-gen retry on visual-artifact”
- `home-agent-memory/stage2_postmortem.md` (37): “- Tested: CC added explicit constraint reinforcement (caps, repetition, "DO NOT substitute"). Failures persisted.”
- `home-agent-memory/stage2_postmortem.md` (17): “Stage 2 generates valid, coherent, well-formed AP content — for the WRONG topic.”
- `home-agent-memory/stage2_postmortem.md` (15): “**Instruction-following failure baked into weights — NOT factual forgetting.**”
- `ap-helpers-data-agent-memory/project_v61_broadfab_falsified_2026_05_13.md` (34): “Real-source training data (like D13 for DBQ) works because it gives the model REAL examples to imitate, not synthetic anti-examples to avoid.”
- `ap-helpers-data-agent-memory/project_v61_broadfab_falsified_2026_05_13.md` (3): “v61 (3,917-pair 7-corruption-type DPO warmstart v60) lost pair-8 with MCQ_SET catastrophic -15.6pp + MCQ -6.7pp.”
- `ap-helpers-data-agent-memory/project_v61_broadfab_falsified_2026_05_13.md` (28): “**Synthetic corruption-DPO class is BROKEN for stim_quality.** Each round of corruption-based DPO training makes the model worse at generating valid stimuli, not better.”
- `ap-helpers-data-agent-memory/project_v61_broadfab_falsified_2026_05_13.md` (2): “v61 broad-fabrication attack: HYPOTHESIS FALSIFIED”
- `home-agent-memory/stage2_postmortem.md` (66): “1. Training data needs hard negatives: examples with off-topic generations labeled as rejected”
- `ap-helpers-data-agent-memory/project_v61_broadfab_falsified_2026_05_13.md` (48): “Use real-source chosen vs K=8 weak-sample rejected, or skip the cell entirely and address via pipeline.”
- `shadow-bench/` (commit bd221e5) (19-20): “A prompt clarification was tried first and FAILED on the live evaluator (model still flagged the marker), so the marker is dropped entirely.”
- `shadow-bench/` (commit bd221e5) (23-24): “OLD (marker leaked): marker flagged 30/30 then 26/30 NEW (empty strip): marker flagged 0/30 then 0/30”
- `aptraining-local/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md` (796): “A prompt that explicitly forbids the stimulus/stem from using the correct option's distinctive nouns might improve educational accuracy.”
- `aptraining-local/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md` (801): “Rows: 11 MCQ_SET failures from `mixed_stability_v2`.”
- `aptraining-local/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md` (803): “Score: `2/11 = 18.18%`, with `2` score errors.”
- `aptraining-local/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md` (774): “Generate more MCQ_SET candidates only, because v61 deterministic outside-knowledge solved `4/11` of v2 MCQ_SET failures.”
- `aptraining-local/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md` (809): “- Next MCQ_SET attempt needs stronger content construction, not another wording-only leak warning.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md` (101): ““Be careful” factuality warnings hurt; caution text without hard constraints creates hedging, not accuracy.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md` (91): “For SAQ/LEQ/DBQ scoring notes, “don’t list specific facts” failed. Verified-facts-only constraints are stronger.”
- `icloud-work/ap-social-studies-generator/data/model_findings.md` (1257): “1. **LEQ fix works**: +15.9pp vs Gate 12b. The spec_compliance FORBIDDEN list genuinely helped.”
- `icloud-work/ap-social-studies-generator/docs/archive/VERSION_ANALYSIS.md` (232): “| Concrete bad examples | **Strong positive** |”
- `icloud-work/ap-social-studies-generator/docs/archive/improvement_plan_prompts.md` (39): “- BANNED WORDS has no **detection/rejection mechanism** - it's advisory only”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-003-mcqset-phrase-anchor.md` (73-74): “Adding an explicit blacklist of constituency-vocabulary to the prompt turned both KCs from 0/19 attempts to PASS within K=6.”
- `icloud-work/aptraining/Cheater/from_cheater/SINGLE_IB_GRADE_SURVIVAL_GUIDE.md` (62-64): “An explicit "high-risk pitfalls" block in the prompt that enumerates the common date-traps reduces this by ~30-50%. Doesn't eliminate it.”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-008-dbq-7doc-generic-attrib.md` (64-65): “v80b keeps inserting a date-pitfall event despite the chronology guardrail.”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-003-mcqset-phrase-anchor.md` (3): “0/50 = 0% on fresh KCs”
- `g9/transformer/v01/QA.md` (41-42): “and "L42" written in a student paragraph. The house prompt now forbids L numbers in student-facing text”
- `g9/transformer/v01/proof-2026-10-09.json` (3): “"at": "2026-10-09T08:42:12.637Z",”
- `g9-transformer-runs/lessons/20261009-085057-why-does-iago-say-he-follows-oth.json` (3): “"createdAt": "2026-10-09T08:50:57.872Z",”
- `g9-transformer-runs/lessons/20261009-085057-why-does-iago-say-he-follows-oth.json` (806): “Review lines 34 to 36, where Iago explains that traditional promotion by”
- `g9-transformer-runs/lessons/20261009-085057-why-does-iago-say-he-follows-oth.json` (807): “Correct; in line 42, Iago explicitly states,”
- `g9-transformer-runs/playtest/2026-10-09T12-25-25-328Z.json` (138-139): “"severity": "engine",
   "class": "line-number-shown",”
- `g9/transformer/test/mechanics.test.mjs` (63): “no text a student reads cites a line number; quoting the words passes”
- `othello-course-renderer-draft/repo/docs/extras/video-recut-drafts-2026-08-31.md` (10-11): “Never write "no X" in a positive prompt; it reinforces X. State the desired thing positively instead ("mouth closed, calm smile", not "not talking").”
- `othello-course-renderer-draft/repo/docs/extras/video-recut-drafts-2026-08-31.md` (12-13): “A negative prompt alone cannot close a waving character's mouth; put the closed mouth in the positive prompt.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/06-AUDIO-NARRATION.md` (177-178): “negative prompts go in negative_prompt (a "no X" sentence in the positive prompt reinforces X)”
- `grade3-reading/course-renderer/docs/extras/video-recut-drafts-2026-08-31.md` (10-11): “Never write "no X" in a positive prompt; it reinforces X. State the desired thing positively instead ("mouth closed, calm smile", not "not talking").”

Against: a large model mostly respected a ban on listing specific evidence; the note calls that instruction good enough for a large model and insufficient for a 14B one (`icloud-work/ML learnings/sft_v7_benchmark_postmortem.md`). a large model mostly respected a ban on listing specific evidence, and the notes conclude that an instruction good enough for a large model is not enough for a 14B one. Both cases involve one small model, and the analysis ties the failure to its weak factual memory, so the finding may not carry to larger writers (`icloud-work/aptraining/.agent/research/failure_taxonomy.md`); whether the later fix worked is not recorded there. The same postmortem proposes hard negatives, the model's own off-topic outputs labelled as rejected, as a fix, and the falsified run's next step pairs real sources against the model's own weakest samples; neither was measured here, and both use real outputs rather than made-up faults. none found; the comparison rests on 11 sets. the forbidden list's gain came on 20 essay items in a run that also recalibrated essay difficulty, and the bad examples' effect is a correlation across runs, not a controlled test. An earlier run of this research recorded that warnings made a writer worse (45% to 30%), and in another test a writer kept inserting a date error despite a guardrail against it (`icloud-work/aptraining/Cheater/exploits/EXPLOIT-008-dbq-7doc-generic-attrib.md`). The word list belonged to a method that was set aside after it passed 0 of 50 fresh items (`icloud-work/aptraining/Cheater/exploits/EXPLOIT-003-mcqset-phrase-anchor.md`).

<sub>method · stage: write · generation, integrity · universal · from ap · measured · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Work from reviewed material

Where reviewed material exists, work from it rather than regenerating it from source notes, since regenerating throws away the review and brings back errors already caught.

An intro-video BrainLift for a Grade 3 reading course starts from the course's existing video scripts, which had been through fact-checking, spoiler sweeps, cultural review and a Grade 3 language pass, because regenerating from the knowledge base discards that work and reintroduces errors already caught once (`downloads/BrainLift - What makes a good intro video.md`, line 269). The walkthrough of a built Grade 3 lesson says most of its content was transferred from the designs, not regenerated (`downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md`, line 9).

Quoted:

- `downloads/BrainLift - What makes a good intro video.md` (269): “Regenerating from the knowledge base discards all of that and reintroduces errors that were already caught once. Compression is a smaller, safer and more auditable job than generation.”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (9): “Most of the content is your own work transferred, not re-generated”
- `g9/transformer/src/mechanics/glossary.js` (4-5): “A section of the 3D build carries its own glossary: its terms and notes are passed … through unchanged, each where its line mark puts it, and nothing is drafted.”
- `g9/transformer/src/mechanics/glossary.js` (121): “the 3D build's own notes are its content: Jev's reading of them is kept, and never holds them”
- `g9/transformer/src/transform.js` (56): “const given = attempt === 1 && mech.given ? mech.given(ctx) : null;”
- `g9/transformer/test/mechanics.test.mjs` (130): “a section of the 3D build brings its own glossary, unchanged and placed by its line marks; any other text is drafted”
- `g9/transformer/test/mechanics.test.mjs` (144): “gl.judge(own, c3).checks.every((c) => c.required === false)”
- `g9/transformer/src/mechanics/glossary.js` (5): “through unchanged, each where its line mark puts it, and nothing is drafted.”
- `g9/transformer/src/mechanics/glossary.js` (122): “const drafted = item.source !== "3d-build";”
- `g9/transformer/src/mechanics/glossary.js` (125): “required: drafted,”
- `othello-course-renderer-draft/repo/docs/handover/closing-questions/HANDOVER.md` (266-268): “**Prefer splicing to re-recording**: when a line changes by a sentence, keep the original take and synthesise only the new sentence, cutting at measured pauses (`ffmpeg -af silencedetect=n=-40dB:d=0.12`).”
- `g9/script/v03/CHANGES.md` (3): “We were not: v1–v2 used an assistant-written script.”
- `g9/library/text/L4fa28c.txt` (28): “brief for an existing script before writing one → docs: sources/Othello Unit Video_ Info Sheet for Devfactory.md §4”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/06-AUDIO-NARRATION.md` (227-228): “segment-cut from the existing approved take with ffmpeg, never re-synthesized”
- `grade3-reading/.claude/skills/one-perfect-lesson/SKILL.md` (69): “The instructional operation (already authored — do not reinvent)”

Against: The same document then compresses the reviewed script, which is cutting approved words, and Split, don't cut found that a cut script lost its style; Remake under new rules asks for a remake when a rule changes, which this rule would resist.

<sub>method · stage: write · generation, review · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Write from vetted material, not from scratch

Have a model assemble, adapt and cite vetted sources, carrying over what they specify rather than inventing items from scratch. In a study of 9 AI quiz builders cited in one project's generator notes, 74% of the items had major flaws and only 1 in 5 was usable.

A reading project's generator notes set out an asymmetry: models are reliable at tagging and assembling (tagging hits ~87–95%) and unreliable at authoring, since of 9 Gen-AI quiz builders studied, 80% of items violated at least one best-practice guideline and 74% had major flaws (`ti-courseplans-audit/docs/generator-insights.md`, B1). They conclude that generators should assemble and transform vetted material and tag it to standards, not invent items from scratch, and that every generation should be grounded in a source the generator cites, since ungrounded generation is where the 74%-flaw rate lives (B3). It bears on a learning from the AP work, that a writer should get verified facts as its only source, not as inspiration. The same notes say to treat what a generator makes as a candidate until a separate check passes it.

Quoted:

- `ti-courseplans-audit/docs/generator-insights.md` (56-57): “But of 9 Gen-AI quiz builders studied, **80% of items violated ≥1 best-practice guideline and 74% had major flaws — only 1 in 5 usable**”
- `ti-courseplans-audit/docs/generator-insights.md` (59-60): “**Design generators that assemble + transform vetted material and tag to standards — not ones that invent items from scratch.**”
- `ti-courseplans-audit/docs/generator-insights.md` (71): “**Ungrounded generation is where the 74%-flaw rate lives.**”
- `grade3-reading/ti-courseplans/docs/key-quality-gates.md` (24): “built correctly to the wrong/no spec”
- `grade3-reading/ti-courseplans/docs/key-quality-gates.md` (29): “Class 1 is the expensive one and the one artifact testing can never catch.”
- `grade3-reading/ti-courseplans/docs/key-quality-gates.md` (36-37): “Names are part of the fingerprint (the "5. Lesson Designs and KBs" → "5. Curriculum" re-parenting was caught this way).”
- `grade3-reading/ti-courseplans/docs/key-quality-gates.md` (50-52): “An undocumented divergence is a build error regardless of who requested it verbally.”
- `grade3-reading/ti-courseplans/docs/key-quality-gates.md` (141): “1. Transfer, don't generate; mark no-canon layers explicitly.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (364 (textutil text)): “carried faithfully, not invented past the KB.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx` (sheet 'V7.0 Executive Summary', cell A57): “No CKHG equivalent exists for approximately 90% of K-8 Economics standards, so the context window for Economics atom generation will rely entirely on state curricula and CEE.”
- `grade3-reading/ti-courseplans/docs/generator-insights.md` (56-57): “But of 9 Gen-AI quiz builders studied, **80% of items violated ≥1 best-practice guideline and 74% had major flaws — only 1 in 5 usable**”
- `grade3-reading/ti-courseplans/docs/generator-insights.md` (90): “**Treat generator output as *candidate* until a separate check passes.**”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-1/reference/dok2-knowledge-tree.md` (81): “A 2025 effectiveness study of nine Gen-AI quiz builders found that 80 percent of the 270 multiple-choice items they produced violated at least one best-practice guideline, and 74 percent had “major” flaws likely to invalidate results.”

Published: [May et al. 2025](https://doi.org/10.3390/educsci15020144)

Against: the study of 9 quiz builders is cited second-hand, with no DOI or URL in these files; and generated items can still serve once gated: construction-first generation survived the anti-leak gate at 60% vs 6% for encyclopedic clones, and one production campaign certified 48.7% (738 of 1,516), while raw generated banks leaked ~94% blind (`ti-courseplans-audit/docs/practice-layer-spec.md`). In a fifth-grade course's history, construction-first generation survived the anti-leak gate at 60% vs 6% for encyclopedic clones (`grade3-reading/ti-courseplans/docs/practice-layer-spec.md`).

<sub>method · stage: ground · generation, stimulus · universal · from g3, research · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Write little, judge the rest

Let a model write only the free text a lesson needs, and make every choice, mark and check a bounded judgment that, at play time, picks among lines written and checked in advance. A paragraph coach that took 6.6 s through a second model became a choice among four written steps, 0.26 to 0.48 s live.

A writer model only writes the free text that has to be written; choosing, marking, ranking and checking are bounded
judgments (`g9/transformer/DECISIONS.md`, the entry on judging). An audit of every AI call found one judgment still made by a
second model, a paragraph coach that took 6.6 s; it became a choice among four steps written in advance, 0.26 to 0.48 s
live (`g9/transformer/DECISIONS.md`; `g9/transformer/v02/QA.md`, the audit of AI calls). On another build's own answer table, 43
answers gave 0 hard fails and 1 soft miss, with a median of 266 ms over the 31 that reached the judge
(`g9/transformer/v02/QA.md`, "Composer and the animated build's marking"). Replies at play time are lines written and
checked before the lesson ships: the debate's push-backs are drafted in advance for each side
(`g9/transformer/src/mechanics/debate.js`).

Quoted:

- `icloud-work/ML learnings/research_rag_factual_grounding.md` (229): “This is a "closed-world" approach: rather than asking the model to generate historical facts from open memory, you preemptively supply the plausible candidates and the model's job is selection rather than recall.”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md` (57): “The replacement introduced a factual error.”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md` (63): “The backstop should fall back to the authored hint verbatim rather than regenerating on this path”
- `aptraining-local/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md` (52): “| K=3 + Gemini Flash 3.5 "reshape" | -23pp vs PEAK | Gemini regenerated content from scratch (weaker domain knowledge) |”
- `aptraining-local/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md` (54): “| K=3 + Gemini "structure-only" | Still regenerating | Schema constraint + token cap overrode "verbatim" hard rules |”
- `aptraining-local/parallel-ideas-lab/reports/synapse_checkin_2026_05_27_pipeline_quality_paradox.md` (56): “| Current (picker-only, v0.4.0) | TBD — needs IB run | Gemini emits only `{best_index: N}`, Python serves verbatim |”
- `icloud-work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md` (13): “Anti-leak scaffold built by rule, not the model.”
- `icloud-work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md` (15): “It never decides what the answer depends on → cannot leak.”
- `icloud-work/incept/inceptbench/src/inceptbench/tools/factual_accuracy_audit.py` (265-266): “``skipped`` must never be model-controlled: if it were in the JSON schema, the
    model could skip the merge and preserve a false pass from the main evaluator.”
- `icloud-work/auto-memory-backup/feedback_no_hallucination_in_training_data.md` (28): “4. **Gold responses** must come from published Sample Responses, scoring guidelines, or human-written rubric-aligned responses. No LLM-generated gold answers.”
- `grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd` (62-63): “Their 40-student design-science pilot reported more consistent scaffolding and less premature answer-giving.”
- `grade3-reading/artifacts/wiki-research/cross-cutting.md` (157): “This is a hard, cited number (74% majorly flawed for LLM-generated items) that bears directly”
- `grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md` (137): “old: LLMs assemble-and-tag only (generic model evidence). Current”
- `grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd` (142-143): “explicitly bars any LLM grader on the auto-score-to-100 path (feedback must be a deterministic function of the machine-scored response).”
- `ti-courseplans-audit/docs/instruction-modes-spec.md` (34): “Deterministic span-acceptance rules first; LLM grading only after a calibration pass — until then this step never blocks progression.”
- `ap-helpers-data-agent-memory/recipe_track_a_b_kc_pack_substitution.md` (32): “3. **Keep the Gemini-generated `prompt`** (analytical DBQ stem) — Gemini is good at writing those. **Replace only the `documents`** — that's where the synthesis-vs-real-source distinction lives.”
- `g9/transformer/test/calibration/cer-frame.next-step.json` (5): “The one change that would most improve a saved paragraph: the check holds on D (none of these), and a case that fails names the change it expects in choice.”
- `g9/transformer/test/glue.test.mjs` (26): “a paragraph that does all three gets no step”
- `g9/transformer/v02/QA.md` (102): “a paragraph doing all three got no step (0.26 s).”
- `g9/transformer/v02/QA.md` (100-101): “a paragraph that explains no word got "pick one word in "I follow him to serve my turn upon him" and say what it suggests" (0.34 s)”
- `g9/transformer/test/glue.test.mjs` (11): “a saved claim-evidence-reasoning answer gets one next step from a Jev choice, filled with the student's words; none when Jev is unsure, or sure the words address the marker”
- `g9-transformer-audit/2026-10-09-builders.json` (1): “Writer deciding labels or marking with no Jev check that can hold it.”
- `g9-transformer-audit/2026-10-09-builders.json` (1): “word-web.js:85 and :97: the writer's 'likely' words count as right in code, with only an advisory Jev check.”
- `g9/transformer/src/mechanics/word-web.js` (99): “code knows only the forms of the centre and the key words (Jev checked those)”
- `g9/transformer/src/glue/threejs-render.js` (272): “words: [ww.item.centre, ...(ww.item.forms[ww.item.centre] ?? []), ...ww.item.keys.flatMap((k) => [k.word, ...(ww.item.forms[k.word] ?? [])])]”
- `g9/transformer/src/mechanics/word-web.js` (59): “a form shares the start of its word”
- `g9/transformer/src/mechanics/word-web.js` (15): “const stemOf = (w) => norm(w).replace(/[^a-z]/g, "").slice(0, 4);”
- `g9/transformer/src/mechanics/debate.js` (3): “so no writer runs at play time”
- `g9/transformer/DECISIONS.md` (29): “the 3D build's paragraph coach (6.6 s through a second model) became a Jev choice of one next step”
- `g9/transformer/DECISIONS.md` (29-30): “the 3D build's paragraph coach (6.6 s through a second model) became a Jev choice of one next step (0.26 to 0.48 s live).”
- `g9/transformer/v02/QA.md` (99-100): “It is now a Jev choice among four authored steps, filled with the student's own words, and shown only when Jev is sure.”
- `g9/transformer/src/glue/animated-judge.js` (4): “evidence only, and writes no reply of its own: every word the student reads stays the rubric's.”
- `g9/transformer/src/glue/threejs-archivist.js` (5): “Jev only decides. Every reply is an authored line (the block's own feedback,”
- `g9/transformer/src/mechanics/video-essay.js` (60): “PAINTINGS (id: subject), for evidence beats:”
- `g9/transformer/test/threejs-render.test.mjs` (116): “the archivist: a checkpoint from a quick check, judged by Jev, replied with its own authored lines”
- `g9/transformer/DECISIONS.md` (29): “its model: the 3D build's paragraph coach (6.6 s through a second model) became a Jev choice of one next step (0.26 to”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “A counter drafted in advance cannot answer the student's own wording, so it is weaker.”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “The 3D build writes its push-back live to the student's words.”
- `grade3-reading/bias_experiment/experiment-record/evidence/knowledgebot/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd` (61-62): “tested a closely related three-layer design—diagnosis, rule-controlled intent, constrained response generation—in a 2026 Grade-5 mathematics system.”
- `grade3-reading/bias_experiment/experiment-record/evidence/knowledgebot/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd` (62-63): “Their 40-student design-science pilot reported more consistent scaffolding and less premature answer-giving.”
- `grade3-reading/bias_experiment/experiment-record/evidence/knowledgebot/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd` (63-64): “This is direct architectural precedent, not a production-scale or randomized outcome result”
- `grade3-reading/bias_experiment/experiment-record/evidence/knowledgebot/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd` (66-69): “SHAPE represented mastery as binary state over a knowledge graph, then used an explicit gate to route generation between instruction and direct problem-solving. Results across model families support external pedagogical routing, while weak results from a smaller model show that renderer capability remains a floor”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/INTEGRATION-DISPOSITIONS.md` (14): “A real-browser check of L4 p21 showed that revised authored hints alone were insufficient: the generated second reply still supplied “a lighter feeling,” an accepted answer concept.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/glossary/authored-feedback/PROPOSAL.md` (11): “tells the model to build on the authored line”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/glossary/authored-feedback/PROPOSAL.md` (21): “Do not prepend generated praise or append generated diagnosis: either can carry the same answer.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/glossary/authored-feedback/PROPOSAL.md` (21): “it intentionally forgoes the generated personalized recap on these nine fields.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/glossary/authored-feedback/RESULT.md` (11): “Valid same-test pair: 74 pass / 10 expected delivery failures → 84/84 pass.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/INTEGRATION-LESSONS.md` (24): “Use reviewed source-grounded explanations, label them as supported examples, and never substitute generated praise for evidence.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/laptop-review/README.md` (48): “Root's real U9 L2 scoring run generated inaccurate relationship praise and an incomplete causal closing.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/CASE-FOR-APPROVAL.md` (105-106): “is sent to a marker that reads it against the Grade-3 STAAR two-point rubric and sends back one short, specific line of help.”
- `g9/player/design/ARCHIVIST-DESIGN.md` (268): “No text input, no reply loop, no timers — the Archivist says the authored feedback and nothing else.”

Against: the writer still picks content that the judge then checks, such
as a text's big idea and key words (`g9/transformer/v02/QA.md`, "Word web"), and the 6.6 s included an advisory check. A later run found counter-evidence (`grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md`). A later run found counter-evidence (`g9-transformer-audit/2026-10-09-best-of-everything.json`). A later run found counter-evidence (`g9-transformer-audit/2026-10-09-best-of-everything.json`). A later run found counter-evidence (`grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/CASE-FOR-APPROVAL.md`).

<sub>method · stage: write · generation, evaluation · universal · from g9 · measured · held · found in [2026-10-12-2-round-1](../research/2026-10-12-2-round-1/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Give the writer the whole objective

Give a writer the exact objective, not just the topic: its official statement, its limits and exclusions, and the criteria and difficulty definitions its judge will check. In a sweep of 67 prompt recipes on 25 items, the only one to pass 23 had added a directive to aim at the judge's criteria for each item type.

In a one-seed sweep of 67 prompt recipes on 25 items, the recipe that added a directive to aim at the judge's main criteria for each item type was the only one to pass 23 of 25, with a mean score of 0.978 (`aptraining-local/parallel-ideas-lab/reports/rubber_ducks/sweep_n25_final_verdict_20260526.md`, lines 5-22 and 49). In a run of 1,080 requests, 98% of the document-question failures (122 of 125) scored zero on curriculum alignment, against 2% (3 of 125) on factual accuracy (`aptraining-local/analyzer/reports/run_f54d5849_what_is_going_wrong.md`, line 20). The response was to put the expanded objective and its knowledge-point description into that writer's prompt, so the alignment signal lands in the input and not only in the rubric (`icloud-work/aptraining/workspace/comms/to_analyzer/2026-06-01T1838Z_dream_sequence_sync.md`, lines 26-28). The multiple-choice writer's prompt already took the target standard, the specific fact to assess, and boundaries saying what to assess and what not to (`icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md`, lines 43-45). The formats its judge will check belong in the prompt too, because a writer breaks what it never sees.

Quoted:

- `aptraining-local/parallel-ideas-lab/reports/rubber_ducks/sweep_n25_final_verdict_20260526.md` (49): “1. **`ib_rubric_criterion_alignment` is the breakthrough duck.** Adding it to G yields the unique top recipe at 23/25 with the highest avg score (0.978) AND MCQ_SET 4/5. Predicted at -5 from n=15, actual at +3.”
- `icloud-work/aptraining/workspace/comms/to_analyzer/2026-06-01T1838Z_dream_sequence_sync.md` (28): “injects expanded LO + KC-description text into the DBQ generator prompt directly, so curriculum-alignment signal lands in the input, not just the rubric.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md` (45): “- `assessment_boundaries`: `{{assessment_boundaries}}` (what to assess; what NOT to assess)”
- `aptraining-local/analyzer/reports/run_f54d5849_what_is_going_wrong.md` (20): “Of 125 DBQ failures: **`curriculum_alignment = 0` in 98 % (122 / 125); `factual_accuracy = 0` in only 2 % (3 / 125).**”
- `aptraining-local/parallel-ideas-lab/reports/rubber_ducks/sweep_pre_score_analysis_20260526.md` (93): “| add_ib_rubric_criterion_alignment | **-5** |”
- `aptraining-local/parallel-ideas-lab/reports/rubber_ducks/sweep_n25_final_verdict_20260526.md` (93): “still want n=50 or random100 before calling 92% production-validated.”
- `icloud-work/ML learnings/gemini_benchmark_relentless.md` (105): “**The confusion:** When a prompt says "Unit 4, 1450-1750," the model sometimes generated content about land-based empires (Unit 3 material) because both units share the same time period string.”
- `icloud-work/ML learnings/gemini_benchmark_relentless.md` (110): “**Why this works:** The model already knows the content of both units. The disambiguation doesn't teach new facts — it removes ambiguity about which unit to draw from given a shared time period.”
- `icloud-work/ML learnings/gemini_benchmark_relentless.md` (112): “**Impact:** Reduced curriculum_alignment failures on APWH Unit 3/4 overlap. ~1% improvement.”
- `icloud-work/ML learnings/research_educational_content_generation.md` (25): “2. **Adjacent-topic drift**: Content from a nearby era/domain bleeds in despite topic constraints”
- `icloud-work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md` (47): “"curriculum_metadata": {}  // EMPTY!”
- `icloud-work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md` (62): “The model generates a 3-year interest problem because it doesn't know about the "single year" constraint. The evaluator fails it for violating a boundary the model never saw.”
- `icloud-work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md` (125): “### Run: 3f480de7 (197 questions, 3.6% pass rate)”
- `icloud-work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md` (129): “| Difficulty mismatch | 139 | Model ignores difficulty_definition |”
- `icloud-work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md` (130): “| Constraint violation | 114 | Model ignores assessment_boundaries |”
- `icloud-work/incept/nova_forge/archive/old_docs/platform/PROMPT_LENGTH_HANDLING.md` (49): “**Approach:** Strip verbose fields under `skills.substandard_metadata` before prompt construction:”
- `icloud-work/incept/inceptlm/README.md` (103): “- Pass rate improved from 8% → 60-75% (expected)”
- `icloud-work/incept/nova_forge/RUN_LOG.md` (44): “- **Pass Rate:** 41.0% (121/295)”
- `icloud-work/aptraining/workspace/comms/to_main/2026-05-01T1708Z_MASTER_PATH_TO_97_analysis.md` (37): “### B. Richer-RAG (assessment_boundaries injection) = +5 passes on soft fails, REAL”
- `icloud-work/aptraining/workspace/comms/to_main/2026-05-01T1708Z_MASTER_PATH_TO_97_analysis.md` (38): “- 9 stable-fail items (0/3 baseline) → 17/27 with richer-RAG (5/9 resolved outright, 2 improved)”
- `icloud-work/aptraining/workspace/comms/to_main/2026-05-01T1708Z_MASTER_PATH_TO_97_analysis.md` (39): “- Mechanism: `assessment_boundaries` field aligns model output with grader scope expectation”
- `icloud-work/aptraining/workspace/comms/from_data/2026-04-30T0700Z_v37c_DONE_postmortem.md` (96): “the 100 KC-prefix KCs pass at 63-82% (no unit cliff — even Unit 8/9, the historically weak cells from the v29 audit, hit 63-65%). The 106 c_/s_ style KCs pass at 46.1% — these are KCs without the structured `KC-N.x.X.X+y` provenance prefix. Most lack one or more of the 4-part richer-RAG fields (especially full `assessment_boundaries`), so the verifier scope-fails them more often.”
- `icloud-work/aptraining/workspace/comms/to_main/2026-05-12T0710Z_AUTONOMOUS_FAILURE_ANALYSIS_PIPELINE_UPGRADE.md` (78): “SAQ: statement only (no RAG; verbose context regresses)”
- `icloud-work/aptraining/workspace/comms/from_pil/2026-05-28T1715Z_V056_RESULT_89pct_curriculum_v1.8.0.md` (46): “- **MCQ_SET -10pp** (85→75): regressed; possibly n=20 variance, or v2”
- `APinceptbench/docs/reports/BENCHMARK_FAILURE_REPORT.md` (33): “The generator ignores the specific `learning_objective` and `statement` provided in the request. Instead, it produces generic questions about the broad topic area.”
- `APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md` (15): “| **Passed** | 35 (30.7%) | 76 (65.0%) | **+34.3%** |”
- `APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md` (25): “| Curriculum Alignment | 43.0% | 88.9% | **+45.9%** |”
- `APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md` (30): “The dramatic improvement in curriculum alignment (43% → 89%) confirms the endpoint is now properly utilizing the `learning_objective` and `statement` fields provided in requests.”
- `APinceptbench/docs/GENERATOR_API_SPEC.md` (123): “- A student who knows this fact MUST be able to answer the question correctly”
- `icloud-work/inceptbench-main/website/content/english/pages/release-notes.md` (23): “- Fixed substandard matching logic that was incorrectly aligning content to the wrong curriculum standards.”
- `APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md` (60): “- Scope expansion beyond provided curriculum (e.g., adding Syria/Libya when curriculum specifies Iraq/Afghanistan only)”
- `icloud-work/incept/ML_TRAINING_INSIGHTS_REPORT.md` (309): “The single biggest discovery was that InceptBench evaluates questions against **curriculum metadata that the model never sees during generation**:”
- `icloud-work/incept/ML_TRAINING_INSIGHTS_REPORT.md` (310): “- The model receives a bare request (grade, topic, type)”
- `icloud-work/incept/ML_TRAINING_INSIGHTS_REPORT.md` (312): “- This mismatch caused 70%+ of failures”
- `icloud-work/incept/ML_TRAINING_INSIGHTS_REPORT.md` (314): “**Fix implemented:** Lambda v5.1.0 auto-injects curriculum metadata from a 1,191-entry lookup table, closing the information gap.”
- `icloud-work/incept/ML_TRAINING_INSIGHTS_REPORT.md` (422): “The biggest pass-rate improvement came not from model training but from **closing the information gap** between what the model sees (bare request) and what the evaluator checks (full curriculum metadata).”
- `icloud-work/aptraining/.agent/memory/MEMORY.md` (121): “Targeted 9-item probe: assessment_boundaries injection resolves 5 stable APUSH fails outright + 2 improved.”
- `icloud-work/aptraining/.agent/plans/PLAN-mission-2026-04-26.md` (71): “Without it, APWH u3 dropped 100% → 43% in prior runs.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (233): “as evidence for a prompt limited to 1800-1848, which is chronologically incorrect for this question's time period.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (322): “The model lacks a constraint to treat the unit's time window as a hard filter.”
- `ap-agent-memory/project_richer_rag_resolves_stable_fails.md` (3): “lifts pass rate from 0/27 (3 runs × 9 items) to 17/27 = 63%”
- `ap-agent-memory/project_richer_rag_resolves_stable_fails.md` (56): “- `assessment_boundaries` (the killer field — explicit "should NOT include X" scope guard)”
- `ap-agent-memory/project_richer_rag_per_cell_tradeoff.md` (19): “| apush/mcq | 93.3% | **100.0%** | +6.7pp | ±0.5pp | ✓ REAL LIFT |”
- `ap-agent-memory/project_richer_rag_per_cell_tradeoff.md` (23): “| apush/saq | 77.8% | **68.3%** | **-9.5pp** | ±3.8pp | ✗ REAL REGRESSION |”
- `ap-agent-memory/project_richer_rag_per_cell_tradeoff.md` (28): “Despite the targeted 9-item probe showing richer-RAG resolves 5 stable APUSH fails (+5 passes), at the FULL distribution it BREAKS ~17 saq items that v29 had been passing.”
- `ap-agent-memory/project_richer_rag_resolves_stable_fails.md` (20): “4. Generated 9 prompts × 1 sample each against v29 with the richer system prompt”
- `ap-agent-memory/project_richer_rag_resolves_stable_fails.md` (30): “| 58090 | apush/saq | 0/3 (0.0/0.0/0.0) | 3/3 (1.0/1.0/1.0) | RESOLVED |”
- `ap-agent-memory/project_richer_rag_resolves_stable_fails.md` (34): “| 68490 | apush/saq | 0/3 (0.8/0.78/0.78) | 0/3 (0.55/0.8/0.8) | unchanged |”
- `ap-agent-memory/project_richer_rag_resolves_stable_fails.md` (35): “| 58794 | apush/saq | 0/3 (0.8/0.8/0.8) | 0/3 (0.8/0.8/0.8) | unchanged |”
- `ap-agent-memory/project_richer_rag_resolves_stable_fails.md` (59): “The grader rubric and the boundaries text are likely both authored from the same canonical CB scope spec”

Against: Before the sweep the same directive was predicted to cost five passes (`aptraining-local/parallel-ideas-lab/reports/rubber_ducks/sweep_pre_score_analysis_20260526.md`, line 93). The sweep's own verdict still wanted n=50 or a random 100 before calling its 92% production-validated (`aptraining-local/parallel-ideas-lab/reports/rubber_ducks/sweep_n25_final_verdict_20260526.md`, line 93), and the winning recipe also carried the source-free directive the lab filed as a rubric exploit (line 73). The request to re-measure after the description went into the document-question prompt (`icloud-work/aptraining/workspace/comms/to_analyzer/2026-06-01T1838Z_dream_sequence_sync.md`, line 34) has no reply in the folder of replies, which holds two notes, both from 27 May. The gain is approximate and overall (~1%), with no counts for the pair. The gain from supplying the specification is not isolated: the fix was logged with an expected rise in pass rate from 8% to 60-75% (`icloud-work/incept/inceptlm/README.md`, line 103), and a later scored run on a different set of 295 items passed 41.0% (`icloud-work/incept/nova_forge/RUN_LOG.md`, line 44). The failure table words the cause as "Model ignores difficulty_definition" (`icloud-work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md`, line 129), which could also mean a writer that ignored a definition it had. More context is not always better: "SAQ: statement only (no RAG; verbose context regresses)" (icloud-work/aptraining/workspace/comms/to_main/2026-05-12T0710Z_AUTONOMOUS_FAILURE_ANALYSIS_PIPELINE_UPGRADE.md, 78), and after a richer curriculum pack "- **MCQ_SET -10pp** (85→75): regressed; possibly n=20 variance, or v2" (icloud-work/aptraining/workspace/comms/from_pil/2026-05-28T1715Z_V056_RESULT_89pct_curriculum_v1.8.0.md, 46). The 46.1% topics also differ from the others in how their records were made, not only in the limits field. Even with the statement, the writer strayed beyond it, for example adding Syria and Libya where the curriculum specified Iraq and Afghanistan only. The 70%+ share is given without a breakdown, and the same report's failure table ranks factual accuracy first: "| 1 | **Factual Accuracy** | 650 | 46.1% |" (`icloud-work/incept/ML_TRAINING_INSIGHTS_REPORT.md`, line 301). The probe was 9 items, and the boundary notes themselves were model-written ('same record mixes CB-canonical statement with Haiku-generated misconceptions/assessment_boundaries', `icloud-work/aptraining/.agent/memory/MEMORY.md`, line 210). The 100%-to-43% figure was carried over from a prior plan, not re-measured. There was one output per item and no fresh control (`project_richer_rag_resolves_stable_fails.md`, line 20). Its table goes against its near-miss reading: one resolved item had scored 0.0 in all three runs, while two near 0.8 stayed failing (lines 30, 34 and 35). The note itself suspects the grader's rubric and the scope text come from the same source (line 59).

<sub>method · stage: ground · alignment, generation · universal · from ap, research · measured · contested · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Refuse rather than ship a weak item

When no valid item can be made, fail visibly or serve a vetted item, never a weak, fallback or filler one, and refuse item types whose output was never measured.

The AP generation service gated the item types it had no evaluation signal for to an error, to avoid shipping unvalidated outputs, and its deployed mode fails visibly if the model cannot serve, with a deterministic fallback for development only (the generation service's `README.md`, lines 30 and 137). The generator kit's prompt for document-based questions returns an error, real-source documents required, when no real documents were retrieved (`system_prompt_dbq.md`, line 135). Its pre-emit checklist says not to emit failing content and to return an error after two silent retries, as better than a low-quality item (`common_pre_checklist.md`, lines 77 and 83).

Quoted:

- `icloud-work/aptraining/apllm-history/README.md` (137): “- We have no signal on `msq` / `fill-in` / `match` / `sequence` / `article` from internal eval — gated to 501 to avoid shipping unvalidated outputs.”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/system_prompt_dbq.md` (135): “Without D13: do not generate this DBQ. Return an error indicating "real-source documents required".”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/common_pre_checklist.md` (83): “This is better than emitting a low-quality item that wastes an IB call.”
- `icloud-work/aptraining/apllm-history/README.md` (30): “The deployed mode is `APUSH_ALL_UNITS_FALLBACK=model_required`, which calls the configured Fireworks model and fails visibly if the model cannot serve.”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/common_pre_checklist.md` (77): “Do NOT emit failing content. If you cannot satisfy all checks after 2 internal retries (silent regenerations), return:”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md` (247): “- The generic DBQ fallback padded missing source documents with curriculum facts using `Retrieved APUSH Unit {unit} source N`, which produced fake repetitive documents.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md` (239): “- DBQ was badly poisoned: 8/55 scored DBQs passed; many failures contained `Retrieved APUSH Unit 1 source N` placeholders and duplicate document content.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md` (1822): “## 2026-05-18 Official Unit 1 Run `1a637aff`”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md` (1845): “- MCQ_SET: 12/193 = 6.22%.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md` (1851): “- The same placeholder pattern existed in the generic MCQ_SET fallback: 179 generation rows contained `Retrieved APUSH`.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md` (255): “Generic DBQ fallback no longer pads with `Retrieved APUSH` curriculum facts; it raises a DBQ source-quality error rather than emitting fake documents.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md` (257): “so any otherwise-unrouted Period 1 DBQ still emits seven vetted source documents instead of hitting the generic no-source branch.”
- `aptraining-local/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md` (62): “- If no LLM candidate passes gates, fail closed rather than return a canned final.”
- `aptraining-local/parallel-ideas-lab/reports/24H_CARETAKER_STATE_20260521.md` (29): “Targeted generation on three known-risk MCQ_SET rows returned `0/3` HTTP success because all K=6 candidates were rejected.”
- `aptraining-local/parallel-ideas-lab/reports/24H_CARETAKER_STATE_20260521.md` (29): “Lesson: do not hard-reject all deterministic MCQ_SET quality failures unless K is expanded or a fallback candidate policy exists.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/README.md` (67): “Unsupported (returns 501): `msq`, `fill-in`, `match`, `sequence`, `article`.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/README.md` (137): “- We have no signal on `msq` / `fill-in` / `match` / `sequence` / `article` from internal eval — gated to 501 to avoid shipping unvalidated outputs.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/README.md` (66): “Supported: `mcq`, `mcq_set`, `saq`, `leq`, `dbq` (the 5 cells our model has been evaluated on).”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/review/evidence/case-for-review.md` (46): “after three exhausted constructions no leak-resistant two-text-comparison item”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/review/evidence/case-for-review.md` (48): “is intrinsically either schema-guessable or a semi-guessable plausible particular). It is taught +”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/review/evidence/case-for-review.md` (49): “practiced (8 practice items on gate-clean paired passages), **never fake-gated**, stated as such”
- `grade3-reading/incept-read-app/docs/G4-SCR-grading.md` (38-39): “These items are **wired into the powerpath test** (they have ids and appear in `/assessment-tests/<test>/questions`) but were never populated with a QTI body.”
- `grade3-reading/incept-read-app/docs/G4-SCR-grading.md` (229): “the empty items must not be served”
- `grade3-reading/course-renderer/authoring/inputs/rule-packs/reading-g3.json` (148): “a lesson assigned to them REFUSES to generate rather than being built against a prototype guess.”
- `incept-package-hub/course-packages/courses/g7-reading/review/evidence/validation/standards-coverage-gate.json` (4): “Preserve the residual verbatim; never promote RL.7.9 to gated without a certified leak-resistant two-text-comparison item.”
- `othello-course-renderer-draft/repo/authoring/README.md` (194-196): “The pipeline is COMPLETE and LANDS WITH ZERO ACCEPTED CANDIDATES: three full runs against the Aladdin Part 1 lesson each ended in an honest DISCARD on structural gates after the refine budget (manifests in `runs/`).”
- `grade3-reading/.claude/skills/jev-select/SKILL.md` (23-24): “noMatch is a real answer. When nothing clears the floor, take nothing. Reranking a search for a question the corpus cannot answer should return zero results, not the least-bad one.”

Against: A later validation recommended accepting a marked timeout fallback in production, since the cached item came from content that had passed the live evaluator (`VALIDATION_REASON.md`, line 62), and a distilled report advises fallback models on timeouts because "A complete conservative answer beats a rich timeout" (`ap_social_studies_generator_distilled.md`, line 184). Blocking every failing draft with no fallback turned quality failures into no output: on three known-risk rows all six drafts were rejected and 0/3 requests succeeded, and the lesson recorded was not to hard-reject every such failure unless more drafts or a fallback policy exist.

<sub>method · stage: settle · generation, integrity · universal · from ap · adopted-rule · contested · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Regenerate only the stage that failed

When a check rejects a draft, regenerate only the stage that failed and pass the specific reason, not a generic 'try again'.

Two staged designs put a deterministic check between generation stages: a lab directive of 19 May 2026 had the validator re-ask only the failing stage instead of restarting, and the parallel lab's question-set architecture ended its validator with 'repair or regenerate with specific reason'. The solver lab's action packet recommended regenerating with concrete rejection reasons between stages, not a broad 'try again'. Neither variant was measured in the records read.

Quoted:

- `aptraining-local/den-of-ideation/MAIN_AGENT_ACTION_PACKET.md` (75): “Regenerate with concrete rejection reasons between stages, not a broad "try again".”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md` (233): “-> repair or regenerate with specific reason”
- `icloud-work/aptraining/workspace/comms/to_den/2026-05-19T1541Z_gate0_prototype_in_lab.md` (39): “Between stages, the validator rejects + re-asks ONLY the failing stage (not full restart).”
- `g9/transformer/src/transform.js` (2-3): “a failing draft gets exactly one correction pass with the reasons. … A step ships only as "ready"; otherwise it is "held" with what failed.”
- `g9/transformer/src/transform.js` (20): “YOUR PREVIOUS DRAFT FAILED THESE CHECKS. Fix every one and return the whole JSON again:”
- `g9/transformer/src/blocks.js` (77): “a held draft is tried once more; an unchecked one is not (a second try has no judge either)”
- `g9/transformer/test/transform.test.mjs` (18): “a failing required check gets one correction pass with the reason, then the step is held”
- `g9/transformer/test/transform.test.mjs` (28): “a correction that fixes the draft ships”
- `g9/transformer/v01/QA.md` (31-32): “othello-1-1: 6/6 ready, 6 writer calls, 9 judge calls, 14.0 s … ozymandias: 6/6 ready, 6 writer calls, 8 judge calls, 13.2 s”
- `g9/transformer/v02/QA.md` (70): “all six re-made, ready on the first or second try”
- `g9/transformer/src/mechanics/util.js` (87-88): “near finds quotations that are nearly, not exactly, the text's … get the text's wording for the correction; any other quotation that is not the text's is held too”
- `g9/transformer/src/mechanics/util.js` (93): “is not the text's wording, which is”
- `g9/transformer/v02/QA.md` (140): “the word web's hint check did not say which word to take out;”
- `g9/transformer/v02/QA.md` (180): “"follow" glossed as loyal: the writer now gets a correction it can act on, below.”
- `g9/transformer/v02/QA.md` (191): “it now asks for a version that plainly holds; before, it only said "unclear".”
- `g9-transformer-runs/blocks/d2d7d0787d6754d9.json` (97): “The film belongs with this text: the judge found this does not hold”
- `g9/transformer/src/transform.js` (79): “the judge could not confirm this; rewrite it so that it plainly holds, or choose another”
- `g9/transformer/v02/QA.md` (140): “the word web's hint check did not say which word to take out”
- `g9/transformer/src/transform.js` (63): “the reply could not be used”
- `g9-transformer-runs/blocks/096b952e5ee95da5.json` (99): “"The hint names none of the likely words: the hint names a likely word"”
- `g9/transformer/src/mechanics/word-web.js` (74): “// the reason names the words, so the one correction pass can take them out”
- `g9/transformer/src/transform.js` (51): “for (let attempt = 1; attempt <= 2; attempt++) {”
- `g9/transformer/src/transform.js` (78): “// an unsure judge is not a no: the correction asks for a version that plainly holds, not for its opposite”
- `g9-transformer-runs/blocks/0e36e4f6c770a7b1.json` (120): “"Beat 3: the first reading can be defended: the judge found this unclear"”
- `g9/transformer/src/blocks.js` (80): “const lesson = await transform({ text, question, track: [mechanic] }, { judge, writer, samples, log: mine, focus, avoid });”
- `g9/transformer/src/transform.js` (2): “a failing draft gets exactly one correction pass with the reasons.”
- `g9-transformer-runs/decisions/a775ad50ec1c4070.json` (21, 304): “"q": "According to Iago, what is his only reason for continuing to serve Othello?",”
- `g9-transformer-runs/decisions/a775ad50ec1c4070.json` (26, 309): “"requirement_0": "The student must state that Iago serves Othello to exploit him or use him for his own personal advantage.",”
- `g9-transformer-runs/decisions/a775ad50ec1c4070.json` (394): “"value": 0.62,”
- `g9-transformer-runs/decisions/856ace1aed960671.json` (89): “"value": 0.54,”
- `g9-transformer-runs/decisions/c98cc9de312f4d43.json` (89): “"value": 0.5,”
- `othello-archive/server/tasks/close.mjs` (86): “Your last reply broke the rules: ${bad.join('; ')}. Write it again.”

Against: The same directive took the opposite line on reasons: "the question-generator doesn't see the validator's reasoning, only the reject signal." (icloud-work/aptraining/workspace/comms/to_den/2026-05-19T1541Z_gate0_prototype_in_lab.md, line 39).

<sub>method · stage: write · generation, evaluation · universal · from ap · adopted-rule · contested · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Size output caps from real outputs

Size output length caps from the longest real outputs plus headroom and check every delivered item is complete, since a cap or timeout can silently cut it short. A timed-out call returned an empty or truncated item, which scored 0.0.

The AP question work's synthesis blamed missing answer choices and incomplete output on a borderline output cap of 8192 for question sets, citing vendor guidance that a cap below the worst-case length truncates output silently (`icloud-work/ML learnings/master_strategy_apr24.md`). Its research summary advises profiling the longest outputs per question type and adding a 20-30% buffer (`icloud-work/ML learnings/research_qwen3_structured_multistage.md`). Separately, a timeout returned an empty or truncated response that scored 0.0, and a completeness check that counts opening against closing braces was added after the call (`icloud-work/ML learnings/gemini_benchmark_relentless.md`).

Quoted:

- `icloud-work/ML learnings/research_qwen3_structured_multistage.md` (54): “- **Never set `max_tokens` below the worst-case full output length.** For complex AP exam questions with 5+ nested fields, estimate the maximum possible output and add a 20-30% buffer.”
- `icloud-work/ML learnings/research_qwen3_structured_multistage.md` (59): “**Practical recommendation:** Profile your longest outputs per question type before setting token limits. Add 30% headroom. For mcq_set (3 questions + stimulus), 8192 is probably borderline — consider 12000-16000.”
- `icloud-work/ML learnings/gemini_benchmark_relentless.md` (161): “**Result of timeout:** The generator returned an empty or truncated response. Score: 0.0.”
- `icloud-work/ML learnings/gemini_benchmark_relentless.md` (163-164): “**Fix:** Added JSON truncation detection after the Pro call:
1. Check if the response JSON is complete (count opening vs closing braces)”
- `icloud-work/ML learnings/master_strategy_apr24.md` (18): “Missing answer choices, incomplete JSON. Root cause: **token limit truncation** — Alibaba Cloud docs explicitly warn that capping `max_tokens` below worst-case output causes silently truncated JSON. Our `mcq_set_questions` limit of 8192 is borderline. Secondary cause: SFT loss doesn't shape partial schema correctness.”

Published: [Enforce Structured JSON Output with Qwen Models (Alibaba Cloud documentation)](https://www.alibabacloud.com/help/en/model-studio/qwen-structured-output)

Against: Whether caps caused the missing answer choices is unsettled: after a smaller writer's caps were cut, the record says "No quality regression observed after the reduction" (`icloud-work/ML learnings/pipeline_architecture_insight.md`, line 70). The project's own rule can set a cap below the worst case: "Run 5 DBQ requests, find where timeouts start, set limit at 50% of that." (the same file, line 73).

<sub>method · stage: settle · generation, evaluation · universal · from ap, research · external-research · contested · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Verified facts as the only source

Give a writer verified facts and real sources, quoted into its instructions, as the only source it may draw on rather than as inspiration. In one published study, grounding the same generator in official curriculum documents raised valid questions from 12-15% to 92-96%.

The AP notes report a published study of curriculum-aligned maths questions in which the generator stayed the same and only retrieval changed: valid questions went from 12-15% to 92-96% once generation was grounded in official curriculum documents (`icloud-work/ML learnings/research_educational_content_generation.md`). Another study they cite, on structured output, supplies the plausible candidates up front so that the model's job is selection rather than recall (`icloud-work/ML learnings/research_rag_factual_grounding.md`). The AP project's own reading is that facts work better as constraints than as inspiration, and its note lists checking each fact in the store against the curriculum documents, since some may be outdated or approximate, among improvements not yet made (`icloud-work/ML learnings/knowledge_and_rag_pipeline.md`). The reason given is that, from memory or its own research, a writer invents dates, documents and claims.

Quoted:

- `icloud-work/ML learnings/research_educational_content_generation.md` (92): “RAG methods go from 12-15% validity to 92-96% validity by grounding generation in official curriculum documents. The study uses GPT-4o as the generator for all conditions — the variable is retrieval, not the model.”
- `icloud-work/ML learnings/research_rag_factual_grounding.md` (229): “This is a "closed-world" approach: rather than asking the model to generate historical facts from open memory, you preemptively supply the plausible candidates and the model's job is selection rather than recall.”
- `icloud-work/ML learnings/knowledge_and_rag_pipeline.md` (102): “The phrasing change reflects the fundamental insight: facts work better as CONSTRAINTS than as INSPIRATION.”
- `icloud-work/ML learnings/knowledge_and_rag_pipeline.md` (230): “3. **Fact verification:** Each fact in curriculum_facts.json should be verified against AP curriculum documents. Some facts may be outdated or approximate.”
- `icloud-work/ML learnings/knowledge_and_rag_pipeline.md` (234): “None of these are implemented yet.”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (113): “2. At inference time, the model will sometimes follow the constraint, sometimes not”
- `icloud-work/ML learnings/research_rag_factual_grounding.md` (33): “- **Fact dynamicity**: Models are least persuadable by retrieved context for *static* historical facts (dates, names, places) — exactly the kind of facts in our rubrics. Dynamic/recent facts are easier to override with context. (ECIR 2025 keynote, arXiv:2603.09654)”
- `icloud-work/ap-social-studies-generator/CHANGELOG.md` (145): “Pass rate | 25% | 100% | +75%”
- `icloud-work/ap-social-studies-generator/CHANGELOG.md` (148): “Flash research stage hallucinated facts that poisoned the compile step. MongoDB verified facts are better.”
- `icloud-work/ap-social-studies-generator/CHANGELOG.md` (123): “Ran data-driven benchmarks (5 samples each) to decide what to optimize”
- `icloud-work/ML learnings/mcq_set_journey.md` (44): “Research→Compile (single step): 60%”
- `icloud-work/ML learnings/mcq_set_journey.md` (46): “Stimulus (from scratch, no research)→Questions: 80% — best”
- `icloud-work/ML learnings/mcq_set_journey.md` (48): “The research step was a hallucination amplifier, not a quality gate.”
- `icloud-work/ML learnings/training_data_journey.md` (119): “Even with 5 relevant curriculum facts injected, the model fabricates its own historical claims.”
- `icloud-work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md` (82): “LLM hallucinates specific dates/numbers”
- `icloud-work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md` (84): “House vote totals wrong (153 vs 174)”
- `icloud-work/ML learnings/knowledge_and_rag_pipeline.md` (102): “facts work better as CONSTRAINTS than as INSPIRATION.”
- `icloud-work/ML learnings/mcq_set_journey.md` (152): “Gemini, Mar 9 cert | ~90-95%”
- `icloud-work/ML learnings/mcq_set_journey.md` (153): “Gemini, Apr | 97-100% | 3-step Plan→Stimulus→Questions | Plan step added, anchor_fact”
- `icloud-work/evaluator/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md` (275): “Curriculum alignment 0% → 89%”
- `icloud-work/evaluator/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md` (276): “Endpoint started using `learning_objective` and `statement` fields”
- `icloud-work/ML learnings/research_educational_content_generation.md` (92): “RAG methods go from 12-15% validity to 92-96% validity by grounding generation in official curriculum documents.”
- `icloud-work/aptraining/workspace/comms/from_main/2026-05-21T0935Z_pipeline_analysis_findings.md` (43): “Pipeline grounding (retrieval, primary sources) doesn't fix this because the failure happens AFTER retrieval”
- `icloud-work/ML learnings/training_data_journey.md` (128): “Not yet tested in benchmark.”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (113): “the model will sometimes follow the constraint, sometimes not”
- `icloud-work/ML learnings/mcq_set_journey.md` (36): “MCQ: 96% → 100% (research step immediately improved factual accuracy)”
- `icloud-work/aptraining/workspace/comms/from_main/2026-05-21T0935Z_pipeline_analysis_findings.md` (43): “Pipeline grounding (retrieval, primary sources) doesn't fix this because the failure happens AFTER retrieval — in the model's claim-construction step.”
- `icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-05T1225Z_v41_d13_stimulus_provenance_audit.md` (25): “The D13-RAG pathway, as instantiated in v41-d13, does NOT eliminate fabrication.”
- `icloud-work/evaluator/docs/reports/BENCHMARK_RUN2_REPORT.md` (30): “The dramatic improvement in curriculum alignment (43% → 89%) confirms the endpoint is now properly utilizing the `learning_objective` and `statement` fields provided in requests.”
- `icloud-work/evaluator/docs/reports/BENCHMARK_FAILURE_REPORT.md` (33): “The generator ignores the specific `learning_objective` and `statement` provided in the request. Instead, it produces generic questions about the broad topic area.”
- `icloud-work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md` (33): “- **Result:** 7/10 factual_accuracy=1, 3/10 factual_accuracy=0”
- `icloud-work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md` (34): “- **Critical finding:** the 3 factual_accuracy=0 verdicts are **LEGITIMATE grader catches of generator errors** — i.e., the test rows had real factual issues that the grader correctly identified”
- `icloud-work/auto-memory-backup/research_fewshot_format_not_facts.md` (20): “- ICL works because demos show **input distribution + output format**, NOT because they convey correct facts”
- `icloud-work/auto-memory-backup/research_fewshot_format_not_facts.md` (21): “- Random labels in demos barely hurt performance — the demos function as a format prompt, not a knowledge prompt”
- `icloud-work/auto-memory-backup/research_fewshot_format_not_facts.md` (76): “- Min et al., *Rethinking the Role of Demonstrations* — EMNLP 2022 (https://aclanthology.org/2022.emnlp-main.759/)”
- `icloud-work/auto-memory-backup/feedback_data_ceiling_not_capacity_ceiling.md` (26): “The model has capacity. It's faithfully learning what's in the corpus. The corpus has wrong content.”
- `icloud-work/ap-social-studies-generator/CHANGELOG.md` (145): “| Pass rate | 25% | **100%** | **+75%** |”
- `icloud-work/ap-social-studies-generator/CHANGELOG.md` (148): “**Decision:** Flash research stage hallucinated facts that poisoned the compile step. MongoDB verified facts are better.”
- `icloud-work/ap-social-studies-generator/CHANGELOG.md` (157): “**Decision:** Always prefer verified curriculum facts over LLM-generated research. The LLM should construct questions FROM verified facts, not invent its own.”
- `grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd` (71-72): “(1) source-grounding (feed the model real primary-source stimuli; let it write only the questions) was the biggest real lever”
- `grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd` (9): “aptraining's headline '0.29→0.95 via real passages' is REFUTED — that jump existed only under a discredited Gemini judge; on the binding grader it collapsed to ~28% (DBQ 0%, MCQ_SET 0%, a 'Gemini-judge artifact'), and the actual MCQ fix was the OPPOSITE: REMOVING the stimulus so the grader's leak-probe is skipped (grader-gaming).”
- `grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd` (9): “the durable lever is stimulus ANSWERABILITY / anti-leak (an unseen, non-leaky stimulus the question can actually be answered from), NOT 'real-passage provenance.'”
- `icloud-work/aptraining/helpers/data/output/postmortem_v89_v90_v91.md` (32): “Per v91 ABORT_DEAD: pipeline-side handling of DBQ scores 87.9% — the model CAN do DBQ when given runtime context, but cannot be TRAINED to.”
- `icloud-work/aptraining/helpers/data/output/postmortem_v89_v90_v91.md` (32): “224 gold DBQ pairs in v91 did not lift it.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md` (157): “- Flash research stage could hallucinate facts that poisoned compile; verified facts were better than LLM-generated research.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md` (111): “The contrast is the whole story: normal generation without real source injection sits at DBQ 0%; D13 source injection immediately produces non-zero DBQ, but the current naive retrieval/prompting still fails often.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/k_12_social_studies_distilled.md` (75): “- Use a vetted knowledge base and closed-world claim checking for AP-level factual accuracy.”
- `grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md` (223): “Generation without quoting the contract caused the 17-divergence parity round”
- `grade3-reading/artifacts/alpha-read-packager/TI_COURSEPLANS_PR_PROPOSAL.md` (18): “RIT meaning free-floats on pre-training (wrong 200-210 / 208/214 anchors)”
- `grade3-reading/artifacts/alpha-read-packager/TI_COURSEPLANS_PR_PROPOSAL.md` (18): “the "ground from a table, not priors" discipline”
- `shadow-content-eval/reports/G3-U1-L11-review.md` (89): “- **Rubric grounding with facts not in the story:**”
- `shadow-content-eval/reports/G3-U1-L11-review.md` (90): “Winter is in the original book, not this retelling.”
- `icloud-work/aptraining/.agent/memory/feedback_curriculum_api_mandatory_2026_05_11.md` (7): “All APUSH (and APWH/APGOV/APMAC/APMIC/APHG/APEURO) inference and training MUST use the Curriculum API”
- `icloud-work/aptraining/.agent/memory/feedback_curriculum_api_mandatory_2026_05_11.md` (9): “IB v2.5.6 grader added DBQ stimulus_quality hard-zero (fabricated docs auto-fail) — and our model was generating BLIND to the source materials the grader checks against. Result: DBQ = 0/89 catastrophic across all v50 seeds.”
- `icloud-work/aptraining/.agent/plans/PLAN-mission-2026-04-26.md` (59): “Without them, the model hallucinates dates and fails `factual_accuracy`.”
- `icloud-work/aptraining/.agent/research/inference_clean.md` (38): “The model isn't trusted to invent factually grounded primary sources. Mid-2026 fix for fabricated citations.”
- `icloud-work/aptraining/.agent/research/inference_clean.md` (40): “*This is not a crutch — it is the prompt contract.*”
- `ap-helpers-data-agent-memory/recipe_track_b_openstax_pair_generation.md` (18): “GROUND_TRUTH_SOURCE (1400-char excerpt of OpenStax content)”
- `ap-helpers-data-agent-memory/recipe_track_b_openstax_pair_generation.md` (64): “**Forbidden-rules audit validation (2026-05-28 at n=1,200 v2 SAQ+LEQ)**: the ground-truth-source-excerpt grounding pattern prevents Gemini fabrication empirically.”
- `ap-helpers-data-agent-memory/recipe_track_b_openstax_pair_generation.md` (64): “Audit found 0 confirmed fabrications across 1,200 rows; 3 false-positive flags (1 noun-phrase mis-match, 2 missing-from-whitelist real historical works).”
- `ap-helpers-data-agent-memory/recipe_track_b_openstax_pair_generation.md` (70): “- **Total: 468/554 = 84.5%**”
- `home-agent-memory/sft_v4_prompt_engineering.md` (23): “3. baseline: 45% pass, 60% factual_accuracy”
- `home-agent-memory/sft_v4_prompt_engineering.md` (25): “5. facts alone: 40% pass, 44% — hurts factual_accuracy”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/PIPELINE_WRAPPER_ACTION_PLAN.md` (108): “- Few-shot for format only, not factual hallucination.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md` (55): “**Do NOT fabricate quotes or sources.** If you don't know a verifiable source, drop the stimulus and write a non-stimulus item.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md` (44): “- `statement`: `{{statement}}` (the specific fact this question must assess)”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md` (88): “Facts work better as constraints than as inspiration.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md` (89): “Flat facts injected as hints often lose to parametric memory.”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/showcase-source-packet.json` (4): “Author only original prose and diagrams from the bounded facts below.”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/showcase-source-packet.json` (72): “Do not present the rock cycle as one fixed circular sequence or claim that all pathways take equal time.”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/showcase-source-packet.json` (231): “Use this fact only for the qualitative one-way energy-flow contrast; do not import the source's quantitative rule of thumb into the showcase.”

Published: [Automated Generation of Curriculum-Aligned Multiple-Choice Questions for Malaysian Secondary Mathematics Using Generative AI (arXiv 2508.04442, 2025)](https://arxiv.org/abs/2508.04442) · [Reducing hallucination in structured outputs via Retrieval-Augmented Generation (NAACL 2024 Industry Track)](https://arxiv.org/abs/2404.08189) · [Understanding the Interplay between LLMs' Utilisation of Parametric and Contextual Knowledge: A keynote at ECIR 2025 (arXiv 2603.09654)](https://arxiv.org/abs/2603.09654) · [Min et al. 2022, Rethinking the Role of Demonstrations, EMNLP 2022](https://aclanthology.org/2022.emnlp-main.759/)

Against: the notes expect the fine-tuned model to follow such a constraint only some of the time (`icloud-work/ML learnings/prompt_engineering_deep_dive.md`), and, citing a keynote paper, they say models are least persuadable by supplied context for static facts such as dates, names and places (`icloud-work/ML learnings/research_rag_factual_grounding.md`). grounding by retrieval didn't fix failures made when a model builds its claims after retrieval; by another account the anchor-fact prompt was not yet tested in a benchmark, and the model sometimes ignores the constraint; one research step that gathered sources raised single questions from 96% to 100%; and the 25% to 100% comparison rests on 5 samples. Neither source tested the remedy itself: the audit could not tell whether retrieval had fired for those prompts at all, and the analysis read its conclusion from the judge's failure labels. Using the given fields did not make the questions right on fact: the next run still had 24 factual failures (`icloud-work/evaluator/docs/reports/BENCHMARK_RUN2_REPORT.md`, line 84), and a later 10-item check built from known-correct facts found real factual errors added while writing 3 of them (`icloud-work/auto-memory-backup/project_grader_audit_results_2_of_3_pass.md`, lines 33-34). The study did not measure this kind of content, and the project rated any lift on its own item types as unmeasured ("no published measurement on AP-history-shaped tasks", `icloud-work/auto-memory-backup/research_fewshot_format_not_facts.md`, line 12); its planned comparison has no recorded result. The diagnosis rests on three measurements that the same project calls "none singularly conclusive" (`icloud-work/auto-memory-backup/feedback_data_ceiling_not_capacity_ceiling.md`, line 12). Supplying facts did not settle accuracy everywhere. A training log records "| Prompt engineering for factual_accuracy | No effect | Model uses parametric memory, not prompted context |" (`icloud-work/ap-social-studies-generator/docs/TRAINING_DECISIONS.md`, line 142), and a run that injected 4,177 facts noted "- The 0.00 failures still occur despite facts injection — hard fails are from document CONTENT quality, not missing facts context", though with no control its effect could not be measured (`icloud-work/ap-social-studies-generator/data/model_findings.md`, lines 230 to 232). The benchmarks behind the 25% to 100% used 5 samples each (`icloud-work/ap-social-studies-generator/CHANGELOG.md`, line 123). The one measured gain behind it was refuted, and the same synthesis puts the lasting lever in an unseen source that leaks nothing and that the question can be answered from, not in where the source came from (`grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd`). Real sources were not enough on their own: one full run with injected documents reached only 33.3%, and the autopsy says retrieval quality matters (`dbq_structural_zero.md`, line 137). The 0 of 89 came with a judge update that began failing fabricated documents outright, so it measures the missing sources and the stricter judge together. An audit for a one-shot goal later removed the injected document bank as an inference-time crutch, while keeping the curriculum facts in the prompt as part of its contract (`icloud-work/aptraining/.agent/research/inference_clean.md`). In an earlier 20-item sweep with another model, adding curriculum facts on their own lowered factual accuracy to 44% from the baseline's 60% (`sft_v4_prompt_engineering.md`, lines 23 and 25); that note does not say how the facts were framed. The audit had no comparison without the excerpt. The fallback, an item with no source, is the shape the lab later filed as a rubric exploit (`aptraining-local/parallel-ideas-lab/reports/rubber_ducks/sweep_n25_final_verdict_20260526.md`, line 73).

<sub>method · stage: ground · generation, stimulus, integrity · universal · from ap, g3, research · external-research · contested · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Model-written wrong options rarely tempt

Wrong options a model writes rarely pass a judge's test of whether they would tempt a skimming reader. In seven live lesson runs, the judge found 2 of 28 machine-written wrong options tempting, and none of the 14 for word meanings.

A first live run produced a quick-check wrong option no reader would choose, and no check caught it, so an advisory judge question was added asking whether each wrong option would seem believable to a Grade 9 reader who skimmed, rather than obviously absurd. Across the seven later lesson runs on two texts, the quick check's 14 machine-written wrong options got 2 holds, 6 fails and 6 unsure, and the word-meaning block's 14 got 0 holds, 10 fails and 4 unsure. All 14 blocks were still marked ready, because the question cannot hold a block. The verdicts are the judge's own, with no labelled case behind them.

Quoted:

- `g9/transformer/v01/QA.md` (40-42): “A first live run on Othello showed two faults no check caught: a quick-check distractor no reader would choose ("he hopes to eventually become the Moor"), and "L42" written in a student paragraph.”
- `g9/transformer/v01/QA.md` (42-43): “an advisory check asks whether each wrong option would tempt a reader who skimmed; on Ozymandias it flagged two distractors as not tempting.”
- `g9/transformer/src/mechanics/quick-check.js` (74): “id: `tempting-${letters[i]}`, label: `Option ${letters[i]} would tempt a reader who skimmed`, required: false,”
- `g9/transformer/src/mechanics/quick-check.js` (75): “seem believable to a Grade 9 reader who skimmed the text, rather than obviously absurd?”
- `g9-transformer-runs/lessons/20261009-085057-why-does-iago-say-he-follows-oth.json` (879-881): “"label": "Option A would tempt a reader who skimmed", "required": false, "verdict": "fails",”
- `g9/transformer/v01/QA.md` (20): “| othello-1-1 | `word-in-focus` | ready | 1 | 5/5 | 4/4 | 0/2 | 3.9 |”
- `g9/transformer/v01/QA.md` (46): “their precision is not yet measured (v04)”
- `g9/transformer/src/mechanics/word-in-focus.js` (87): “would tempt a reader who has not looked closely”

Against: The judge's precision has not been measured: "their precision is not yet measured (v04)" (g9/transformer/v01/QA.md line 46). With no labelled cases the judge may be too strict, and the word-meaning version asks about a reader who "has not looked closely" rather than one who skimmed (g9/transformer/src/mechanics/word-in-focus.js line 87).

<sub>context · distractors, generation, evaluation · domain · from g9 · measured · held · found in [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>
