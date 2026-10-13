# Writing questions

170 learnings. Each says where it came from and what argues against it. [What a perfect question is](../PERFECT-QUESTION.md) collects the criteria by facet, and [How to generate perfect questions](../GENERATING.md) collects the methods by stage.

### A cause that explains the difference

In a comparison item, the keyed explanation must name a cause that differs between the things compared; a cause that applies to both explains nothing about the difference.

One of eight copy-task audits added to an item evaluator for issue 962 fails a keyed explanation that applies equally to both subjects of a comparison, since it explains the general direction of change rather than the difference (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt`). The audit fires only on data tables comparing exactly two named subjects (the same file, line 102), and it rests on one rubric, not a measurement.

Quoted:

- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (116): “If the correct answer's causal explanation applies equally to both subjects, it explains the general direction of change for all subjects — not the specific comparative difference.”

Against: none found

<sub>criterion · key, demand · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### A choice's note argues for it

A note shown beside a choice before the learner picks must give the reason someone might believe that choice, never argue against it, or it gives the answer away. In all four lessons of one live walk, the wrong card's note argued against itself in print before the child tapped.

A live walk of four grade-3 reading lessons played every visible page as one child in one session. Where the three earlier lessons' wrong-card notes argued for the wrong card, all four of these printed a note that argued against it before the child tapped. The walk's fix gives each wrong note the reason a child might believe it, and it records that no check compared a wrong choice's note with its tone.

Quoted:

- `grade3-reading/artifacts/qc-2026-09-30-staging/LIVE-WALK.md` (4): “every visible page of L4–L7 was played as one child in one session”
- `grade3-reading/artifacts/qc-2026-09-30-staging/LIVE-WALK.md` (15): “In L1–L3 the wrong card's note argues for the wrong card.”
- `grade3-reading/artifacts/qc-2026-09-30-staging/LIVE-WALK.md` (16): “In L4–L7 the wrong card's note argues against itself, in print, before the child taps:”
- `grade3-reading/artifacts/qc-2026-09-30-staging/LIVE-WALK.md` (22): “give each wrong note the reason a child might believe it.”
- `grade3-reading/artifacts/qc-2026-09-30-staging/LIVE-WALK.md` (162): “No check compares a wrong choice's note with its tone (W1).”

Against: none found

<sub>criterion · distractors, integrity, options · universal · from g3 · measured · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A diagnostic item measures one thing

An item used to diagnose must test one piece of knowledge, because a wrong answer to a bundled item can't say what is missing. With about 10 students per course, a bundled item can't be untangled by statistics, so it has to measure one thing by design.

A diagnostic-assessment BrainLift worked through on AP courses names items that confound core knowledge with experience of the question format as a common failure, since a wrong answer then can't say why it is wrong (`grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md`, lines 310 and 336). With about 10 students per course at a time, a bundled item can't be decomposed statistically, so each item must measure one thing by design, in the simplest format that gives the information, and a multi-part item whose part (b) needs part (a) is split for diagnostics (lines 337, 397 and 402). It judges a diagnostic by whether students who follow its recommendations learn more efficiently (line 307), and the reading courses' adversarial review asks of every item whether a wrong answer identifies one component (`grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md`, line 165). Test that knowledge in the plainest format that shows it, and split dependent parts into separate items; bundled items are often exam-style ones.

Quoted:

- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (310): “Using test items (such as AP-style exam questions) that confound core knowledge with experience in answering that type of question.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (336): “If a student gets it wrong, you don't know *why* they got it wrong.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (337): “we must ensure, by design, that each item measures one thing cleanly.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (397): “Prefer the simplest format that gives you the diagnostic information you need.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (402): “If the student fails, you learn about part (a) but nothing about part (b). For diagnostics, split these into independent items.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (307): “A diagnostic is good if students who follow its recommendations learn more efficiently than students who don't.”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (165): “does a wrong answer identify ONE KC? (reading exception: OK when the stimulus IS the KC, then strip everything else)”
- `grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd` (68): “The question is evaluative (it tells you whether the student can do this task) but not diagnostic (it doesn't tell you what's missing).”
- `grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd` (69): “Estimating how each item loads on multiple latent dimensions requires thousands of students, not hundreds.”
- `grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd` (69): “~10 students per course at a time”
- `grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd` (69): “we must ensure, by design, that each item measures one thing cleanly.”
- `grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd` (86): “For diagnostic assessment, the much-maligned MCQ is not a compromise — it is the optimal format.”
- `grade3-reading/knowledge_bot/knowledge/kb-0155-diagnostic-assessment-evidence-base.qmd` (255): “The completed practice test is insufficient to establish this proficiency at topic level.”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (165): “passage-parse + content + reasoning in one item → wrong answer uninterpretable”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md` (29): “Each diagnostic item isolates one KC — no bundling (e.g. reading comprehension inside a science item)”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md` (31): “No all-or-nothing multi-part item where (b) depends on (a); split into independent items”

Against: Both sources allow a stimulus-based item when the stimulus is the skill, as in reading comprehension (the BrainLift, line 397; the checklist, line 165), and the reading comprehension BrainLift holds that no valid diagnostic comprehension test exists (`grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md`, lines 88-89). The taxonomy makes one exception for reading: bundling is acceptable when the stimulus itself is the knowledge component being tested, with everything else stripped (`ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md`).

<sub>criterion · evidence-of-learning, format · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### A driving question the text can answer

A lesson's driving question is open, never yes or no, answerable from the text alone, about what the text shows or how it shows it, and short.

Texts dropped or pasted into the lesson engine's composer arrive without a lesson question. The engine drafts three, keeps in code those that end in a question mark, run to at most 26 words, open with no yes-or-no word and cite no line number, and asks the judge whether each can be answered from the passage alone and is worth a Grade 9 lesson of about an hour (`g9/transformer/src/question.js`, lines 12-34). The first one the judge confirms becomes the lesson question the blocks are written toward.

Quoted:

- `g9/transformer/src/question.js` (22-23): “Each is open (never yes or no), answerable from the text alone, about what the text shows or how it shows it, at most 22 words, ending in "?".”
- `g9/transformer/src/question.js` (1-2): “The writer drafts three; code keeps … the open, well-formed ones; the judge keeps the first it finds answerable from the text alone and worth a lesson”

Against: The judge's question joins two claims in one yes-or-no: "Can question_${i} be answered from passage alone, and is it worth a Grade 9 lesson of about an hour?" (`g9/transformer/src/question.js`, line 34). The prompt asks for at most 22 words while code allows 26 (lines 23 and 12), and the first confirmed question is kept, not the best one: "question = qs.find((_, i) => results[i]?.verdict === "holds") ?? null;" (line 35).

<sub>criterion · stem, alignment · universal · from g9 · adopted-rule · held · found in [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### A frame shows the shape, not the answer

A response frame may show an answer's shape but must never prefill the evidence or quotation, or supply the reasoning, the learner is meant to produce.

A Grade 5 reading course's instruction review profile asks, wherever learner construction is required, whether learners must supply all intended evidence and reasoning, with frames and formatting clarifying rather than completing the answer. It rejects a step where required evidence or a quote is prefilled, quotation conventions are unclear, or a frame supplies the reasoning. Review feedback mapped to that criterion asked one independent step to make the learner type the quotation as well as the explanation instead of prefilling the evidence; the mapping implies no verdict on the current course.

Quoted:

- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/generated/instruction-review-profile.json` (319): “Where learner construction is required, must learners supply all intended evidence and reasoning, with frames and formatting clarifying rather than completing the answer?”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/generated/instruction-review-profile.json` (323): “Required evidence or a quote is prefilled, quotation conventions are unclear, or a frame supplies the reasoning.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/generated/feedback-2026-08-11-crosswalk.json` (339): “Require the learner to type the quotation as well as the explanation instead of prefilling the evidence.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/generated/feedback-2026-08-11-crosswalk.json` (18): “Two or more criteria are required to evaluate the complete observation; no current-course verdict is implied.”

Against: none found

<sub>criterion · demand, format, hints · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A giveaway depends on role and audience

Judge whether a visible support such as a picture or diagram gives the answer away by the item's role and audience.

The evaluator first decides whether an item is a worked example or instructional question, where showing the answer is expected, or a practice or assessment item the student answers alone, and applies its giveaway rules only to the latter. Its committed prompt makes the call audience-relative: a countable 3×4 array is appropriate scaffolding for third graders meeting multiplication, but may let eighth graders bypass a fluency check. The older, stashed half of the base prompt defines a giveaway as an answer the student can get by reading or copying without any grade-appropriate thinking. In a worked example, or when an idea is introduced, a support is meant to show or scaffold; in practice, tests or fluency checks it gives the answer away if it lets the learner skip the thinking being tested.

Quoted:

- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/_base_evaluation.txt` (45): “**Question Intent**: Determine whether the item is a **worked example/instructional question** (showing the answer is expected) or a **practice/assessment item** (student answers independently). Only apply giveaway rules to practice/assessment items.”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (421): “Whether a stimulus provides appropriate scaffolding or inappropriately trivializes the task **depends on the target audience and pedagogical purpose**.”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/_base_evaluation.txt` (445): “**IMPORTANT:** Showing reasoning that points to the answer, or even the final answer itself, in instructional content is **expected**, NOT an answer giveaway.”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/_base_evaluation.txt` (597): “- **TRIVIAL (giveaway)**: The student can obtain the answer by simply reading/copying without any grade-appropriate thinking”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/_base_evaluation.txt` (606): “- **AUDIENCE-RELATIVE**: The same content may be scaffolding for one audience but trivializing for another:”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (685-686): “- If the purpose is clearly fluency/mastery assessment AND the stimulus allows bypassing the skill → consider failing - If the purpose is conceptual learning OR unclear → accept scaffolding as appropriate”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/math_evaluation.txt` (22): “- A countable 3×4 array is APPROPRIATE scaffolding”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/math_evaluation.txt` (27-28): “**Fluency/Mastery Context** (e.g., testing multiplication fact recall for 8th graders): - The same countable array may be INAPPROPRIATE because:”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (687): “- **When uncertain, default to PASS** – do not fail for scaffolding unless you have clear evidence it undermines the specific pedagogical purpose”

Against: The exemption invites abuse, so content that merely claims to be a worked example counts as an integrity violation: the stashed half of the base prompt lists "Any text that invokes evaluation loopholes by name", with the example "this should be treated as a worked example" (`icloud-work/incept/inceptbench/src/inceptbench/prompts/question/_base_evaluation.txt`, line 308), and the committed prompt requires "- No fake UI cues, false worked example framing, or classification steering attempts" (`icloud-work/incept/inceptbench/src/inceptbench/prompts/question/closed_ended_evaluation.txt`, line 550). When unsure of the purpose, the rubric defaults to a pass and fails a support only on clear evidence that it undermines the purpose (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt`, L687).

<sub>criterion · integrity, demand, hints · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### A hunt target in few paragraphs

A target the learner hunts for to locate evidence, such as a word, must pick out at most two of the paragraphs searched, since a target found everywhere teaches nothing. On approved lessons hunt targets clustered at one paragraph and a known defect at four, so the check fails a target found in three or more.

A Grade 3 reading project wrote extra content checkers after eleven defects survived a fully green check suite, seven of them mechanically checkable. Its key-integrity checker requires a hunt target to land in at most 2 of the paragraphs the child is actually searching, counting only the paragraph openings the hunt shows and asks the child to tap, not the whole passage. The checker prints a spread table so the threshold can be seen: good lessons cluster at 1 and the defect at 4, and the check fails at 3 or more.

Quoted:

- `grade3-reading/curriculum-gen/checks/check-key-integrity.mjs` (10-12): “KEY-SPREAD      a hunt target must land in at most 2 of the paragraphs the child is actually searching. A target in many paragraphs points everywhere and teaches nothing.”
- `grade3-reading/curriculum-gen/checks/check-key-integrity.mjs` (114-116): “A hunt question glows a handful of paragraph openings (`hunt.first_lines`) and asks the child to tap one. That glowing set — not the whole chapter — is the search space, so it is the honest denominator.”
- `grade3-reading/curriculum-gen/checks/check-key-integrity.mjs` (437-438): “The spread table makes the threshold visible and defensible rather than arbitrary: you can see the good lessons cluster at 1 and the defect at 4.”
- `grade3-reading/curriculum-gen/checks/check-key-integrity.mjs` (440): “hunt-target spread (threshold: fail at 3+)”
- `grade3-reading/curriculum-gen/.agent/AGENT.md` (75-77): “**Green is the floor, not the bar.** On 2026-08-21 eleven defects survived a fully green `npm run check`, and seven of them were mechanically checkable — nobody had written the check.”
- `grade3-reading/artifacts/witw-feedback-2026-08-24.qmd` (17-19): “In L14's last task, the word the child is asked to hunt for is "Toad". It appears in thirteen of the paragraphs they are searching, so it points everywhere at once.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md` (68-69): “"hunt" (keyword spotting) was ruled out 2026-08-25 because many texts have no clean keyword to hunt for”

Against: The recorded baseline still holds one key-spread finding on an approved lesson (`grade3-reading/curriculum-gen/STATE.md`, line 110) that the sources read never adjudicate, and the threshold was calibrated only on this course's lessons. A later ruling in the same project dropped keyword hunting from the finding procedure, because many texts have no clean keyword to hunt for (`grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md`, lines 68-69).

<sub>criterion · integrity, key, demand · domain · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A lesson target only the text supplies

Choose a lesson's target idea so that it can't be stated correctly without reading the text, since a takeaway every learner already knows makes the whole lesson blind-solvable.

Research before authoring a lesson on a famous episode found that the usual takeaway is the best-known fact about its hero and the answer a published class magazine prints in its own key, so a child who never read the passage would produce it (`othello-course-renderer-draft/repo/docs/research/g4-u1-l2-the-cyclops.md`, lines 446-450). The brief argued that such a lesson fails the course's rule that a question must not be answerable without the text at the level of the lesson rather than the item, and that its evidence hunt degenerates, since a hunt with nothing genuinely rejected is a reveal (lines 448-456; `othello-course-renderer-draft/repo/docs/rules/questions-and-assessment.md`, line 41). The lesson plan rejected that takeaway for this reason (`othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l2.json`, line 60).

Quoted:

- `othello-course-renderer-draft/repo/docs/research/g4-u1-l2-the-cyclops.md` (448-450): “A SPINE lesson whose target concept can be stated correctly without reading fails R-Q-3 at the level of the lesson rather than the item.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l2-the-cyclops.md` (454-456): “R-PED-5 forbids modelling hard thinking as if it were easy, and a hunt with nothing genuinely rejected is a reveal, which is why `validate-contracts.mjs` requires a rejection at all.”
- `othello-course-renderer-draft/repo/docs/rules/questions-and-assessment.md` (41): “A question must not be answerable without the text”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l2.json` (60): “it is the answer a child produces without reading anything, so a SPINE lesson built on it would fail R-Q-3 at the level of the lesson rather than the item.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l2-the-cyclops.md` (442): “Yes. This section is my argument, not a finding.”

Against: The brief marks the section as argument: "Yes. This section is my argument, not a finding." (`othello-course-renderer-draft/repo/docs/research/g4-u1-l2-the-cyclops.md`, line 442).

<sub>criterion · alignment, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A performance task needs an evidenced choice

A performance task asks for a delivery choice, such as a stressed word or a pause, justified by the text's words, and accepts any choice the explanation supports. One drama task scored three things, the exact word chosen, a plausible intended meaning and the link between delivery and that meaning, and accepted any word that fit.

The rebuilt Grade 5 drama unit made it a release rule that a performance task must require an evidenced delivery choice, not only the selection of a fact. Its final task asks which word in a line to stress and what that emphasis helps the audience understand, and it accepts several words when the explanation fits. An audit of the independent tasks confirmed that the rubric accepts multiple defensible words rather than imitation of the model.

Quoted:

- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/README.md` (59): “A performance task must require an evidenced delivery choice, not only selection of a fact.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/lesson-07.md` (50): “Multiple keys are valid when the explanation fits. Criteria: exact chosen word, plausible intended meaning, connection between delivery and that meaning.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/INDEPENDENT-TASK-AUDIT.md` (22): “Rubric explicitly accepts multiple defensible words, not imitation.”

Against: A planned delivery is not yet a performance: "It assesses performance planning; actual delivery is a separate requirement if the curriculum expects a performance." (`grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/INDEPENDENT-TASK-AUDIT.md`, line 22).

<sub>criterion · format, demand, scoring-guide · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A question must need the knowledge

A question meant to test subject knowledge fails if a reader without that knowledge can reach the answer from what the item gives.

Disagreement reports on an item evaluator showed its judge passing items whose stimulus already gave the answer away; in one, the judge ran a zero-knowledge probe and still passed the item, because a technical word ("pipes") was missing from the passage (`icloud-work/inceptbench-main/tests/test_evaluator_prompt_rules_976.py`). The rubric now asks whether grade-level subject reasoning is still needed once the stimulus is absorbed, counts a task that collapses to looking and reporting as a leak, and calls it an evaluation error to clear an item only because the literal answer word is absent (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt`). The probe and the ban on that defense were added after version 2.5.3. Such a reader may match or paraphrase the source's wording, name what it describes, read a label or arrow, or rule out options by common sense. To fix such an item, change what it asks rather than swapping in synonyms.

Quoted:

- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt` (125): “Discriminator: after fully absorbing the stimulus, is grade-level `{request.subject}` reasoning **still required** to pick the answer? If the cognitive demand collapses to "look and report" or "match restated description to its conventional name", it is a leak. → `educational_accuracy`”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt` (110): “It is an evaluation error to claim an item is NOT a mechanism-naming leak simply because the literal answer word does not appear in the stimulus.”
- `icloud-work/inceptbench-main/tests/test_evaluator_prompt_rules_976.py` (4-6): “Root cause: evaluator performed the zero-knowledge counterfactual probe but rationalized past a connect-the-paragraphs leak by claiming a missing technical word ("pipes") in the stimulus meant subject knowledge was still required.”
- `icloud-work/aptraining/apllm-history/runtime_assets/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt` (97): “If the cognitive demand collapses to "look and report" or "match restated description to its conventional name", it is a leak.”
- `icloud-work/ap-social-studies-generator/docs/archive/ITERATION_ANALYSIS.md` (176-177): “→ The question TELLS the student what the Progressive Era was about. → Student can answer by reading, not by KNOWING.”
- `icloud-work/ap-social-studies-generator/docs/archive/VERSION_ANALYSIS.md` (140): “Hard difficulty broken - 58% → 38% (-20%)”
- `icloud-work/aptraining/apllm-history/runtime_assets/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt` (94): “the targeted skill IS reading / interpreting / measuring the stimulus”
- `icloud-work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md` (408): “Ensure 60-70% of answer derivable from stimulus alone”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-003-mcqset-phrase-anchor.md` (69-72): “Inspecting v12's two stuck KCs revealed the rubric was failing child-Q1 educational_accuracy because the stimulus contained literal vocabulary that lexically matched the keyed answer ("plains" → "Plains farmers", "laborer" → "industrial laborers").”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-003-mcqset-phrase-anchor.md` (73-74): “Adding an explicit blacklist of constituency-vocabulary to the prompt turned both KCs from 0/19 attempts to PASS within K=6.”
- `icloud-work/aptraining/Cheater/reports/RUBRIC_BLINDSPOTS.md` (33-35): “But it is *only* run when a stimulus is present. Strip the stimulus and the probe never fires.”
- `icloud-work/aptraining/Cheater/reports/RUBRIC_BLINDSPOTS.md` (37-40): “add a stem-only variant of the probe that asks "could a student with no APUSH knowledge eliminate three of these four options purely from common-knowledge / lay-vocabulary reasoning?"”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-002-stimulus-strip.md` (167): “**EX002-04 — Market Revolution transportation (score 1.00, SUPERIOR)**”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-002-stimulus-strip.md` (176): “- D. "The federal mandate that all interstate goods travel by horse-drawn wagon"”
- `icloud-work/aptraining/Cheater/reports/RUBRIC_BLINDSPOTS.md` (29): “non-ELA subjects **with a stimulus of any modality**”
- `icloud-work/aptraining/workspace/comms/from_cheater/2026-05-25T1029Z_ESCALATE_FINAL_10_mechanisms.md` (33-35): “Every stimulus form I've tried lands on ONE failure side or the other: - bare/generic stim → "decorative" (stim_quality, test_preparedness fail) - rich/specific stim → vocab leak (educational_accuracy fail via child evaluations)”
- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md` (28): “- Stimulus answer leaks fail `educational_accuracy` when a zero-knowledge student can reach the answer from the stimulus and stem alone.”
- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md` (41): “- Avoid stimulus leaks: mechanism-naming, connect-the-paragraphs, visual-depicts-answer, and numbered-path mechanism-labeling leaks.”
- `icloud-work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build2_eval/evaluation_report.md` (16): “- Zero metrics: {'concept_coverage': 1, 'difficulty_alignment': 1, 'difficulty_distribution': 3, 'educational_accuracy': 14, 'mastery_learning_alignment': 2, 'non_repetitiveness': 2, 'specification_compliance': 3, 'stimulus_quality': 2, 'test_preparedness': 3}”
- `icloud-work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build2_eval/evaluation_report.md` (9): “- Failed: 15”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt` (76): “Working only from the stimulus (including any image-analysis content) and the question stem, attempt to pick the correct answer step by step.”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt` (86): “1. **Mechanism-naming leak.** The stimulus describes a process / mechanism / scenario in lay vocabulary; the question asks the student to supply the conventional label or technical term *for that exact described thing*.”
- `icloud-work/aptraining/artifacts/_logs/watcher_replay_dupes_20260522T2018Z/2026-05-22T201819Z_exploits_EXPLOIT-001-historian-frame-self-leak/source_report.md` (26-28): “Across 10 items (mixed APUSH units 4–8): 40% pass, dimension fails dominated by `educational_accuracy` (5/10), `clarity_precision` (5/10), and `mastery_learning_alignment` (5/10).”
- `icloud-work/aptraining/artifacts/_logs/watcher_replay_dupes_20260522T2018Z/2026-05-22T201819Z_exploits_EXPLOIT-001-historian-frame-self-leak/source_report.md` (32-34): “1. **Vocabulary / paraphrase leak.** The judge's zero-knowledge counterfactual probe (per `_base_evaluation.txt` Checklist B1) found that the abstract historian claim word-matched one option:”
- `icloud-work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/RUBRIC_BLINDSPOTS.md` (37-40): “**Patch:** for closed-form history MCQs without a stimulus, add a stem-only variant of the probe that asks "could a student with no APUSH knowledge eliminate three of these four options purely from common-knowledge / lay-vocabulary reasoning?".”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (109): “- `mcqset_repair_offline_v2`: changed Q2 wording away from "supremacy"; score 0.78 because "taking precedence" was still treated as a synonym leak for "supreme."”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (110): “- `mcqset_repair_offline_v3`: changed Q2 to ask why the principle mattered historically under the Articles rather than asking students to name/paraphrase the principle. Local IB scored 1.0.”
- `aptraining-local/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md` (56): “Penalize keyed answers sharing words with labels; otherwise IB sees decorative/source-cued items.”
- `aptraining-local/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md` (130): “- no correct answer copied or synonym-mapped from stimulus;”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/official_exports/local_eval/local_eval_report.md` (39): “- `31`: mcq answer copies stem terms”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md` (91): “- The stem must reference the stimulus explicitly ("According to the source...", "The passage above suggests...").”
- `aptraining-local/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md` (807): “- Answer-hiding phrasing alone did not improve MCQ_SET.”
- `grade3-reading/artifacts/generator_review/leak_control_and_certification_schema.md` (13-15): “In a knowledge subject, an answer you can find *in the source* is a leak. **In reading, finding the answer in the passage *is* the skill** — so we deliberately **skip the history-style "answer is in the source" check.**”
- `grade3-reading/artifacts/Peter-Pan-L4-review-response-2026-08-25.pdf` (p.3 (pdftotext lines 146-148)): “The check tests the paraphrase 'lovely', so a child who never learned 'enchanting' can answer it correctly. Compare Aladdin, whose stem names its word outright: 'Which sentence uses the word betrayal correctly?' Ours should name the word.”
- `grade3-reading/artifacts/arc-audit/L7.md` (31): “stem "Which sentence uses the word triumphant correctly?"”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (71-72): “Do not use a later event as period evidence, invent a direct quotation, treat Indigenous societies as interchangeable, or make the stimulus itself reveal the answer.”

Against: The probe is skipped for reading items, and it must pass items whose targeted skill is reading or interpreting the stimulus (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt`, lines 102 and 120). It over-fired on a question asking for the category an instance belongs to (issue 972) and on a science phenomenon diagram (issue 977) (`icloud-work/inceptbench-main/tests/test_evaluator_prompt_rules_972.py`, `icloud-work/inceptbench-main/tests/test_evaluator_prompt_rules_977.py`). the same rubric exempts items whose skill is reading, interpreting or measuring the stimulus, and one failure report asks for 60-70% of the answer to be derivable from the stimulus alone. The check is defined for knowledge-testing items, "non-ELA subjects **with a stimulus of any modality**" (`icloud-work/aptraining/Cheater/reports/RUBRIC_BLINDSPOTS.md`, line 29); in a reading item the text is meant to supply the answer. With sources written to fit the item the safe zone is narrow, a bare source reading as decorative and a rich one leaking the key's words: "Every stimulus form I've tried lands on ONE failure side or the other" (`icloud-work/aptraining/workspace/comms/from_cheater/2026-05-25T1029Z_ESCALATE_FINAL_10_mechanisms.md`, lines 33-35). The probe runs only when a source is present, so items without one were never checked: '- B2: zero-knowledge educational probe runs only when a stimulus is present.' (`icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-criteria-pack-audit.md`, line 64). The probe does not apply to reading items, where the text is the point: the rubric skips it for reading subjects and for fiction, nonfiction and article content, since those are reading comprehension by design (icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt, line 80). A rubric-derived writer prompt pulls the other way, asking the stem to refer to the stimulus explicitly ('According to the source...'), and a warning to the writer alone did not help: answer-hiding phrasing on its own did not improve the sets it was tried on (`prompt_perfection/NOTES.md`).

<sub>criterion · integrity, demand, stimulus · universal · from ap · adopted-rule · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A question must need the text

A question about a text must need the text. With the text hidden, a stronger model still found the key for 75 of 95 questions that a weaker one had passed.

In the reading project, questions were given to a model from a different family with the passage withheld; when it
still picked the key, the question did not test the passage. On one seed bank, 4 of 11 items that had all passed a
quality benchmark leaked
(`grade3-reading/knowledge_bot/knowledge/kb-0070-passage-blind-solve-g5-seedbank-2026-06-24.qmd`). Re-run with a
stronger solver from another family, only 20 of 95 items that had passed survived, and 187 of 3,146 untested
candidates (`grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd`). The
lesson engine's own give-away check was answered from general knowledge of a famous text until it was narrowed to the
question's own words (`g9/transformer/v02/QA.md`, "Found and fixed in integration").

Quoted:

- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-003-mcqset-phrase-anchor.md` (97-99): “The judge cannot reliably distinguish "question explicitly quotes a stimulus phrase" from "question genuinely requires that phrase to answer". A lexical link is enough for stimulus_quality = 1.0.”
- `icloud-work/inceptbench/docs/AP_EVALUATION.md` (141): “Questions must require the stimulus”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (76): “~78% of raw machine-generated reading items were answerable without the passage by a cross-family solver”
- `grade3-reading/knowledge_bot/knowledge/kb-0076-coe-catchup-2026-06-30.qmd` (26): “75.3% leakable”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (172): “control-pass rate did not predict blind certifiability”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (47): “An in-lesson knowledge check answerable from explicitly-taught knowledge is legitimate (that's what checking taught knowledge means); the same overlap in a comprehension/transfer item is a leak.”
- `grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd` (44): “| Blind accuracy on the audited items | `1.0` | about `0.0` |”
- `grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd` (72): “Passage-dependent items can look "kid-gameable" under the wrong blind-solver and still be clean.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd` (29): “Documented blind-solve leakage: MCQ 99.5%, MSQ 100%.”
- `grade3-reading/knowledge_bot/knowledge/kb-0126-claude-takeover-audit-2026-07-13.qmd` (29-30): “was exactly solved blind in 3/8 shuffles and that low solver confidence had hidden those hits”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (617): “→ The stimulus must be **critical and integral** to the educational task — not merely non-harmful, engaging, or decorative.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (671): “A question is NOT penalized simply because it can be solved from text alone.”
- `grade3-reading/knowledge_bot/knowledge/kb-0070-passage-blind-solve-g5-seedbank-2026-06-24.qmd` (54): “IB passed all 11; the different-family blind solve failed 4.”
- `grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd` (47): “separate from InceptBench, which graded answer-leaking items 1.0”
- `grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd` (103-104): “a course where every item scores IB 1.0 but 90% is blind-solvable is a failed course”
- `grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd` (104-105): “emitted "What is the primary function of chlorophyll?" from a photosynthesis passage — IB 1.0, blind-solve 100%”
- `grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd` (40-41): “PASS if with-passage correct-rate >= 0.80 AND without-passage correct-rate <= chance-rate + 0.15 margin”
- `grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd` (180-181): “model answers without passage in >=3/5 trials at temp 0.3 = fail”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (233): “Always run with-passage control before blind certification.”
- `grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd` (61-62): “120 pass a cross-family blind-solve (binding gate, solver = OpenAI gpt-4o-mini, != Gemini generator) -> 79 also answerable with the passage”
- `grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd` (64-65): “Rejected items recovered far above chance (sequence 58% vs. 3% blind; hot-text 79% vs. 14%; match 86% vs. 41%)”
- `grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd` (182): “LLM ablation may false-positive/negative vs real students”
- `grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd` (70): “A solver that can bluff its way through without the passage will inflate leak rates.”
- `grade3-reading/knowledge_bot/knowledge/kb-0070-passage-blind-solve-g5-seedbank-2026-06-24.qmd` (59): “prefer fictional proper nouns over real-world entities”
- `grade3-reading/knowledge_bot/knowledge/kb-0070-passage-blind-solve-g5-seedbank-2026-06-24.qmd` (47-48): “a world-knowledge-rich passage invites guessing; a savvy test-taker could beat it without reading.”
- `grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd` (48-49): “the `L.3.4` template pre-defined the affix in the stem → rewritten to be passage-dependent”
- `grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd` (119-120): “cold-solvable ~0.8 because camel adaptations are world-famous general knowledge; distractor surgery can't close it, needs full content replacement”
- `grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd` (26-27): “in reading, finding the answer in the passage IS the skill, so the usual history-style "answer is in the source" leak check is deliberately skipped.”
- `grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd` (29-30): “the item is **passage-dependent** -- answerable only by reading the passage, not from world knowledge or test-taking heuristics.”
- `grade3-reading/knowledge_bot/knowledge/kb-0134-g5-reading-v2-local-design-package.qmd` (99-100): “I03 had leaked through forced one-of-four guessing: 5/8 plain-blind exact guesses.”
- `grade3-reading/knowledge_bot/knowledge/kb-0134-g5-reading-v2-local-design-package.qmd` (108-109): “I03 became dual-blind safe with 2/8 exact guesses in each blind condition and no leak trigger.”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md` (4): “**Based on:** Forensic analysis of 150 MCQ + 100 MSQ items (62.7% MCQ leak rate, 51.0% MSQ leak rate)”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/MSQ_REGEN_GUIDE.md` (3): “**Status:** MSQ pool is 100% leaked (0 of 1,346 structural-pass items usable).”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (313): “items become **blind-solvable from background knowledge** — all 5 carry `blind_solvable_risk=HIGH`”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (314): “This is the coherence↔leak tension”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/PASSAGE_DESIGN_RULES.md` (9): “Could a student who studied this topic in school — but never read this specific passage — answer every one of my questions correctly using only prior knowledge?”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md` (17): “| sequence | 185 | **58.4%** | 3.0% | **~19×** | adjacent-pair order 85.2% |”
- `grade3-reading/artifacts/g5-merged-course/a2-cross-family-regate.md` (14): “| **All 353** | 353 | **334** | **19** | **94.6%** |”
- `grade3-reading/artifacts/g5-merged-course/a2-cross-family-regate.md` (19): “**Verdict: the 353 are overwhelmingly leaky.** Only **19 items** genuinely require the passage under a”
- `grade3-reading/artifacts/g5-merged-course/a2-cross-family-regate.md` (21): “anti-leak FORMAT ≠ low leak”
- `grade3-reading/artifacts/g3-control-set-2026-07-10/G3-CALIBRATION-REPORT.md` (49): “Construction, not format or grade, is the lever.”
- `grade3-reading/artifacts/LANE1_COURSE.md` (136): “| hot-text | 1,479 | ~17.5% | ~1,220 |”
- `grade3-reading/artifacts/LANE1_COURSE.md` (140): “| MCQ (corpus) | 1,473 | 99.5% | 7 |”
- `grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md` (84): “- only 4/13 passed the LLM quality-B rubric”
- `grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md` (89): “Anti-leak success is not enough.”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (328): “for reading, "anti-leak" is a build-time lint (answer not in the stem, honest distractors) — NOT a comprehension guarantee, since finding the answer in the passage IS the reading skill.”
- `grade3-reading/artifacts/g5-merged-course/VERDICT_TEMPLATE.md` (70): “2. **KCT1 Domain-knowledge ≈ 0 — by design.** Domain-recall items are passage-independent → removed”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (305-306): “The key rule: accept only after with-passage control plus cross-family blind failure;”
- `grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd` (64-65): “Rejected items recovered far above chance (sequence 58% vs. 3% blind; hot-text 79% vs. 14%; match 86% vs. 41%), which is the evidence the kept 97 require the passage.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md` (24): “**No answer giveaway in the stem** — no pre-defined affix/definition, no cue words”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/passage_blind_verdicts.json` (137): “Stem giveaway + option self-evidence: the stem restates the full target inference”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md` (69-70): “a same-family-IB-passed bank that is **36% leaky** (RI.5.9 MCQ stem-giveaway + … RL.5.1 hot-text stem-giveaway; the EBSR pair self-confirmed)”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (83): “include prior-knowledge answerability, EBSR Part-B-restates-Part-A, and keyword-match answerability.”
- `grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd` (94): “**Make the target cognitive process unavoidable.** If students can succeed via pattern matching, shallow guessing strategies, or memorizing repeated items, the app is gameable and its signals are untrustworthy.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (267-269): “Anti-leak (kb-0064) means "you must read the passage to answer" — it does NOT mean the passage's own facts are sourced or true. A perfectly anti-leak item can sit on an unsourced machine-authored passage.”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (36): “An in-lesson knowledge check answerable from explicitly-taught knowledge is legitimate (that's what checking taught knowledge means); the same overlap in a comprehension/transfer item is a leak. Mis-classifying the item makes the same text both correct and defective — it took five adversarial rounds to isolate this.”
- `grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd` (73-75): “KCT1 (domain-knowledge recall) is ~0 **by design** — passage-independent items are exactly what the anti-leak filter removes; covering KCT1 needs a different item design (generation), not relaxed gating.”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (100): “Later items must not be answerable from earlier lessons without reading the new text.”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (106-108): “the solver receives all prior lesson content (on-ramp pre-teach, ledger state, prior passages) but not the new text; later items must fail.”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (135-137): “the historical Gemini 2.5 run found **1 catch of 16**. `rivers-demo-choice-hottext-20` was **0/3 exact plain-blind but 3/3 exact + high confidence spine-conditioned.**”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (137-140): “A calibrated 2026-07-13 Gemini 3.5 Flash replication was 3/3 in both conditions, so the same item is currently a direct plain-blind leak and the historical context-lift interpretation does not generalize across model versions.”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (106): “(measured on one theme, not universal)”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/README.md` (90): “The required current-model check changed the verdict.”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/README.md` (90-92): “After a `1/1` with-passage calibration, `gemini-group/gemini-3.5-flash` solved the item `3/3` plain-blind and `3/3` with prior-course context.”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/README.md` (92): “The old context-lift claim does not survive model drift; the item is directly gameable.”
- `grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd` (276): “85/90 exact blind-recovered = 94% leak under the strict sample.”
- `grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd` (271): “- construction is the lever, not format alone.”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (208): “- MCQ leaked through ordinary school knowledge, vocabulary, or a "textbook correct" option;”
- `grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd` (66-67): “~78% of raw generated items were blind-solvable before this gate”
- `grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd` (279): “- Redesigning the wrong construction does not work if the item encodes world knowledge or obvious order.”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (127-128): “Lesson: anti-leak success alone is insufficient. Some items became mechanical ordering tasks or failed standard fit even after passing the blind gate.”
- `grade3-reading/ti-courseplans/courses/g5-reading/brainlifts/v0.6.qmd` (24-25): “different blind-solve leak rates by question *format*: MCQ 99.5%, MSQ 100% — hot-text 1.67%, > sequence 0%, match 0%, EBSR 0% (cross-family run, 2026-06-23/24).”
- `grade3-reading/ti-courseplans/courses/g5-reading/brainlifts/v0.6.qmd` (25): “The passage is not the only lever.”
- `shadow-bench/src/inceptbench/prompts/question/inline_choice_evaluation.txt` (32-33): “A correct inline choice must require the student to have read and understood the passage — it is NOT acceptable if grammar alone (e.g., article agreement) or common knowledge determines the answer.”
- `shadow-bench/src/inceptbench/prompts/question/inline_choice_evaluation.txt` (66-67): “- Any option produces an ungrammatical sentence when inserted (all options must fit grammatically — the skill being tested is comprehension, not grammar correction).”
- `shadow-bench/` (commit e435432) (5-8): “Replaces rubric-only passage-dependency (an LLM opinion formed with the passage visible) with an empirical test: strip the passage/stimulus, have a cross-family OpenAI solver attempt the bare item, and hard-override passage_reference -> 0.0 when it answers correctly with high confidence (confident-correct).”
- `icloud-work/incept/inceptbench/docs/AP_EVALUATION.md` (141): “| `stimulus_alignment` | MCQ_SET | Questions must require the stimulus |”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/mcq_set/evaluation.txt` (310): “- Any question can be answered without the stimulus”
- `icloud-work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/ck_gen - prompts.json` (96): “Determine whether a student must read this specific passage to answer the question correctly, or if they could answer it using general knowledge.”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-003-mcqset-phrase-anchor.md` (140-141): “The judge currently accepts a question-stem phrase quotation as proof of stimulus dependence.”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-013-mcqset-described-map.md` (118-120): “The map is genuinely not load-bearing — students don't NEED it, they just reference it.”
- `icloud-work/evaluator/ap_benchmark/prompts/official_ap_prompts.py` (136-139): “- FAIL if questions can be answered without the stimulus”
- `icloud-work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md` (28): “It can be answered entirely from outside knowledge about Portuguese Indian Ocean strategy without any engagement with the stimulus.”
- `icloud-work/ap-social-studies-generator/python/generators/saq.py` (433): “⛔ STIMULUS INTEGRATION TEST: Cover the stimulus. Can ALL parts be answered”
- `icloud-work/k_12_social_studies/ap_files/Articles Tracker.xlsx` (sheet 'Articles-readable-exp', cell M16): “There is a reference to Sumni/Shia in the reflection but they are not mentioned in this reading.”
- `icloud-work/ap-social-studies-generator/data/model_findings.md` (635): “DBQ passage_reference: questions aren't explicitly referencing their assigned document.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/mcq_set/evaluation.txt` (310): “- Any question can be answered without the stimulus”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md` (248): “If the model selects the correct answer in ≥3/5 trials, the item fails — it is answerable from background knowledge alone, not from careful reading of the specific passage.”
- `incept-package-hub/course-packages/courses/g8-reading/review/evidence/case-for-review.md` (55-56): “The redesign defeats the G8 POC's 98.6%-leak failure.”
- `grade3-reading/artifacts/g5_build_2026_07_02/g5_analysis_digest.md` (41): “the 120 L.5 vocab seeds LEAK 99.2% and must be re-authored + re-certified, never deployed as-is”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md` (254): “- Text-dependence ablation uses a language model, which may have different knowledge than a typical G3–G5 student. Items that fail for LLMs may be valid for students (false positives) or vice versa.”
- `grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd` (66-67): “~78% of raw generated items were blind-solvable before this gate; G5 bank certified 1.67%/0%/0% across 172 items”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (45): “An item answerable without the passage is not measuring reading”
- `icloud-work/aptraining/artifacts/pending_review/2026-05-22T211855Z_exploits_EXPLOIT-003-mcqset-phrase-anchor/source_report.md` (92-94): “The judge cannot reliably distinguish "question explicitly quotes a stimulus phrase" from "question genuinely requires that phrase to answer".”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/common_pre_checklist.md` (43): “- [ ] Question fails the counterfactual: "if I deleted the stimulus, can the student still get this right?" — must be NO”
- `grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd` (66-67): “(~78% of raw generated items were blind-solvable before this gate”
- `grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd` (72): “4. Passage-dependent items can look "kid-gameable" under the wrong blind-solver and still be clean.”
- `grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md` (58): “anti-leak/answerability is a real, construct-general item-quality lever”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md` (38): “**But self-containment ≠ passage-dependence.**”
- `grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/exemplars-rubric.md` (97): “answerable from prior knowledge, so it fails Transfer and Evidence precision at the root.”
- `grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md` (75): “- Items answerable without the passage are defects, not questions (provenance: ~78% of raw”
- `grade3-reading/artifacts/wiki-research/redteam-standard.md` (232): “- **6/6** — the number of items an LLM-judge passed that a blind-solve cracked, the commitment-9”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (43): “It cites Hirsch and Willingham and then forbids knowledge from helping.”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (74-76): “Passage-dependency is currently judged by LLM rubric and regex, not by an empirical passage-withheld solve. Red-team history says rubric passage-dependency can pass while blind probes solve the items trivially.”
- `grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd` (74-75): “(passage withheld, model+version pinned, temp 0.3, **N=5, FAIL at k≥3/5**, per-format answer-space rules, `ablation_trials[]` persisted)”
- `grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd` (77-78): “prior call was that re-checking IB+Opus-passed items is redundant — logged as corroboration, not re-pushed.”
- `ti-courseplans-audit/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md` (43): “6/6 were solvable without the passage:”
- `ti-courseplans-audit/docs/course-formula-agents.md` (233): “a course-wide audit found **~half of ~700 items gameable**”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (172-173): “Measured lesson: control-pass rate did not predict blind certifiability.”
- `grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd` (30-31): “`novelty:"unseen"` guarantees the passage is new; it does NOT guarantee passage-dependence”
- `grade3-reading/knowledge_bot/knowledge/kb-0221-early-planning-history-and-sep22-snapshots.qmd` (78): “(5) treat anti-leak as a build-time lint for reading, not a deep guarantee.”
- `grade3-reading/ti-courseplans/docs/course-formula-agents.md` (233): “a course-wide audit found **~half of ~700 items gameable**. InceptBench scored one gameable item **1.0**”
- `grade3-reading/ti-courseplans/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md` (47): “answerable by any knowledgeable solver with no passage.”
- `grade3-reading/ti-courseplans/docs/practice-layer-spec.md` (27-28): “exempt from passage-dependence **by design**; gated instead on spine membership (taught content only)”
- `shadow-content-eval/SKILL.md` (370-371): “If the key can be picked from general knowledge, the option wording or common sense, the item tests nothing about the text.”
- `shadow-content-eval/reports/G3-U1-L2-review.md` (44): “That leaves one option without any reading.”
- `icloud-work/aptraining/.agent/research/eval_baseline.md` (266): “the IB grader thinks the documents in the DBQ are not "core/integral" — i.e. the model emits documents but the prompt could be answered without them.”
- `shadow-bench/src/inceptbench/prompts/lesson_bundle/evaluation.txt` (93): “Fail: more than 20% of questions can be answered without the passage — the lesson is gameable at scale.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq_set.md` (84): “Verify every question requires the stimulus by testing the counterfactual”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md` (230): “all child questions depend on stimulus”
- `grade3-reading/artifacts/demo-unit-2026-07-10/spine-gate/SPINE-GATE-REPORT.md` (81-82): “is a schema generalization the earlier lessons make derivable”
- `grade3-reading/artifacts/demo-unit-2026-07-10/spine-gate/SPINE-GATE-REPORT.md` (83): “exactly why the item cannot serve as evidence the student read text 4.”
- `grade3-reading/artifacts/demo-unit-2026-07-10/spine-gate/SPINE-GATE-REPORT.md` (86-87): “re-author with distractors that are schema-consistent alternatives only text 4 disambiguates”
- `grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/gate-capstone-summary.json` (16): “"spine_leaky": 2,”
- `grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd` (32): “(choice-hottext-20: plain-blind 0/3 but 3/3 with prior-lesson corpus)”
- `grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd` (33): “Current Gemini 3.5 replay: 3/3 in both conditions - direct blind leak; old lift is historical.”
- `grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd` (39-40): “10 candidates, 0 certified, 8 plain-blind leaks, 2 spine-conditioned leaks, 0 defective.”
- `grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd` (42-43): “Its immutable protocol still replays 6 certified and 1 spine-leaky.”
- `grade3-reading/knowledge_bot/knowledge/kb-0098-incept-service-coe-catchup-2026-07-09.qmd` (39): “later questions become answerable from earlier lessons without proving true comprehension.”
- `grade3-reading/artifacts/spine-solve-calibration-2026-07-10/REPORT.md` (15-16): “It does not isolate the effect of prior-course context, calibrate the bar, or certify a future themed course.”
- `g9/transformer/v02/QA.md` (139-140): “its give-away question was answered from general knowledge of Othello (now: the question's own words only)”
- `g9/transformer/src/mechanics/open-check.js` (87): “Judge only the wording of q, not what a reader may already know about the work.”
- `g9/transformer/src/mechanics/open-check.js` (86): “a famous text's answer is known to anyone who knows the work, which is no give-away of the question's”
- `g9/transformer/src/mechanics/quick-check.js` (77): “Does the wording of the question by itself reveal which option is correct, without reading the text?”
- `g9/transformer/src/mechanics/open-check.js` (86): “// its own words only: a famous text's answer is known to anyone who knows the work, which is no give-away of the question's”
- `g9-transformer-runs/blocks/0419fc2dc6f6bacf.json` (13): “"stem": "When was Shakespeare's play Othello written?",”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “Nothing tests whether a key can be picked without reading.”
- `othello-archive/src/content/checks.ts` (9): “expects: ['Othello chose Cassio as his lieutenant instead of Iago (Iago was passed over for promotion)'] }”
- `g9/library/text/L25efa0.txt` (36): “Part 2's check can be answered without reading part 2.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (550-551): “A source must be necessary unless the item is explicitly labeled as a retrieval check.”

Against: some leaks were near
misses where world knowledge tempts but the key needs the text, and the root cause was encyclopedic passages, not the
questions (the same two files). A later run found: the leak verdict depended on the blind solver, since the same audited items had blind accuracy 1.0 under one solver and about 0.0 under another (`grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd`). A later run found: a model's blind solve may give false positives or negatives against real students, and a solver that bluffs its way through without the passage inflates leak rates (`grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd`). A later run found: a form rebuilt on a familiar topic went live with all 5 items rated at high risk of being answered from background knowledge, accepted as formative practice rather than a check that the passage was read (`grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md`). A later run found counter-evidence (`grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md`). A later run found counter-evidence (`grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md`). A later run found counter-evidence (`grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd`). A later run found counter-evidence (`grade3-reading/knowledge_bot/knowledge/kb-0221-early-planning-history-and-sep22-snapshots.qmd`). A later run found counter-evidence (`grade3-reading/ti-courseplans/docs/practice-layer-spec.md`). The first run's headline case no longer stands: a calibrated newer solver answers it 3/3 without either the text or the earlier lessons, and the report withdraws the claim that a plain blind check could not detect it (`grade3-reading/artifacts/demo-unit-2026-07-10/spine-gate/SPINE-GATE-REPORT.md`, lines 7 and 105-113). The capstone counts come from the same dated solver. The first catch is historical, since a newer solver answered that item 3 of 3 times with no text at all (`grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd`), and the one run built to measure the effect used different solvers and bars in its two conditions, so it could not isolate what earlier lessons add (`grade3-reading/artifacts/spine-solve-calibration-2026-07-10/REPORT.md`). A later run found: The lesson engine's give-away check was narrowed to the question's own words after it answered from general knowledge of a famous text, and by design it now passes a question anyone who knows the work can answer; the engine has no other check that a question cannot be answered without the text (`g9/transformer/v02/QA.md`). A later run found counter-evidence (`g9/transformer/src/mechanics/open-check.js`). A later run found counter-evidence (`g9-transformer-audit/2026-10-09-best-of-everything.json`).

<sub>criterion · integrity, stimulus · universal · from g3, g9 · measured · held · found in [2026-10-12-2-round-1](../research/2026-10-12-2-round-1/), [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### A source that calls for knowledge

When a source is there to call up knowledge rather than to test reading, each question should need both the source and that knowledge. A leak probe failed a whole set when more than 20% of its questions could be answered from the source alone.

In AP history question sets the source is there to prompt course knowledge: the judge's leak probe failed a set when more than 20% of its questions could be answered from the source alone, and a pipeline's checks required outside knowledge as well as that every question depend on the source. The eight sets still failing after known rescues needed outside-knowledge hooks, distractors from the same period and no dependence on the source's phrasing. For such sources this narrows 'A question must need the text' and 'One answer the text settles': the text is needed, but it must not settle the answer alone. Check that each question fails with the source hidden and that the source alone doesn't settle it.

Quoted:

- `icloud-work/aptraining/workspace/comms/MCQSET_GENERATION_LEVER.md` (7): “The eduacc leak-probe fails a set when >20% of child questions are answerable **from the stimulus alone**.”
- `aptraining-local/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md` (109): “Fix generation/selector semantics for the eight remaining rows: outside-knowledge hooks, same-period distractors, no stimulus phrase dependency, and compact payloads to avoid score timeouts.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md` (229): “APUSH outside knowledge required”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md` (230): “all child questions depend on stimulus”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/TEACHING-ASSESSMENT-CONTRACT.md inside it) (166-167): “8. **Leak gate:** Removing subject knowledge must break the path to the correct response. Removing a required stimulus must also break the path. Passing one condition does not excuse failing the other.”

Against: "The first version over-blocked known passing rows because InceptBench tolerates some source-referential wording." (aptraining-local/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md, line 24).

<sub>criterion · stimulus, demand, integrity · domain · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A stand-in test matches its target's interactions

A test standing in for another must reproduce its interactions, navigation rules and per-sitting format mix, since a different interface changes how students respond and what scores mean. One stand-in reading test requires at least 12 technology-enhanced items in every 40-item session.

A stand-in for an outside reading test follows that test's documented interaction conventions, forward-only navigation, an answer before each advance and all six item interactions, so that its scores stay comparable and the official test measures reading rather than interface novelty (`grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/MAP_PROXY_VALIDITY_CASE.md`). It argues from response-process validity in the testing standards: students who interact with items differently on another platform respond differently, and their scores are not comparable. Its design review makes a floor of 12 technology-enhanced items per 40-item session a hard constraint and counts an all-multiple-choice session as a violation (`grade3-reading/ti-courseplans/courses/map-proxy-assessment/skill/SKILL.md`).

Quoted:

- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/MAP_PROXY_VALIDITY_CASE.md` (372): “If students interact with items differently on our platform than on MAP — different cognitive load from an unfamiliar UI, different navigation affordances, different format rendering — response patterns will differ and scores will not be comparable.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/MAP_PROXY_VALIDITY_CASE.md` (343): “The interface follows MAP's publicly documented interaction conventions, so that students experience familiar testing conventions and the official test measures reading rather than interface novelty:”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/MAP_PROXY_VALIDITY_CASE.md` (345): “**Forward-only navigation**: once an item is answered, it is locked; no back button”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/skill/SKILL.md` (45): “**TE floor ≥12 per 40-item session** — every format except plain MCQ counts as TE (MSQ, EBSR, hot-text, sequence, match/gap-match)”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/skill/SKILL.md` (45): “All-MCQ is a violation.”

Published: [AERA, APA & NCME 2014, Standards for Educational and Psychological Testing](https://www.testingstandards.net/open-access-files.html)

Against: Parity is partial: of the six formats, three are confirmed for the reference test's reading levels, two are documented only for its other subjects and one only in secondary materials (`grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/MAP_PROXY_VALIDITY_CASE.md`, line 92).

<sub>criterion · format, measurement · universal · from g3, research · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A stem that stands on its own

Write each stem as a full question that names everything it asks students to relate, so that a student who knows the material can answer it with the options covered. An item with no question in it passed even the judge that noticed, at 0.88.

The AP generator's item checklist asks for a stem understandable without reading the options, and its guidance answers stem ambiguity by reviewing stems before options are added (`icloud-work/ap-social-studies-generator/docs/analysis/best_practices.md`). A cross-review found an item with no question stem at all, which both model judges passed (`icloud-work/ap-social-studies-generator/docs/archive/CLAUDE_CROSS_EVAL_REPORT.md`). A review of generated questions listed comparisons with one side missing among its clarity issues, and a judge failed a part for a vague region label (`icloud-work/k_12_social_studies/python/docs/EVALUATION-RESULTS-2026-02-23.md`; `icloud-work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md`). The writer rules require naming both things compared (`icloud-work/ap-social-studies-generator/python/generators/saq.py`). Write it as a question, not a sentence to complete.

Quoted:

- `icloud-work/ap-social-studies-generator/docs/analysis/best_practices.md` (381): “- [ ] **Clear stem**: Question understandable without reading options”
- `icloud-work/ap-social-studies-generator/docs/analysis/best_practices.md` (159): “**Fix**: Review stems independently before adding options”
- `icloud-work/ap-social-studies-generator/docs/archive/CLAUDE_CROSS_EVAL_REPORT.md` (80): “- ⚠️ Missing question stem (what exactly is being asked?)”
- `icloud-work/ap-social-studies-generator/docs/archive/CLAUDE_CROSS_EVAL_REPORT.md` (82): “- **Claude Score:** 0.88 - Pass with minor issues”
- `icloud-work/k_12_social_studies/python/docs/EVALUATION-RESULTS-2026-02-23.md` (259): “| **Unclear comparisons** | "More significant than..." (than what?) | Complete the comparison |”
- `icloud-work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md` (76): “Part C of the prompt uses the vague descriptor 'southern regions,' which is imprecise.”
- `icloud-work/ap-social-studies-generator/python/generators/saq.py` (282): “RULE: A student should never need to infer WHAT is being compared — name both items.”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (65): “read the stem, cover the options, and ask whether a knowledgeable student could formulate an answer.”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (92): “confirm that a knowledgeable student could answer the question from the stem alone (cover-the-options test).”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (103): “Before submitting: re-read the stem with options covered. If you cannot answer from the stem alone, revise the stem.”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/L4-REVIEW-GAPS-2026-09-16.md` (117): “Item stems are questions, not completion fragments (D5.11)”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/L5-REVIEW-GAPS-2026-09-17.md` (7): “was a completion fragment ("…staying here could mean ___"), the only fragment stems in L5”
- `g9/transformer/test/threejs-render.test.mjs` (54): “a quick check is asked open, an evidence hunt asks for the words; their lines stay on the server”
- `g9/transformer/test/threejs-render.test.mjs` (63): “stem: "Which of these is true?"”
- `g9/transformer/test/threejs-render.test.mjs` (64): “assert.match(skip.skipped[0].reason, /beside its options/);”
- `g9/transformer/src/glue/threejs-render.js` (33): “// a question that only works beside its options ("Which of these…") is not asked open”
- `g9/transformer/src/glue/threejs-render.js` (34): “const OPTIONS_ONLY = /\b(which of (these|the following|the options)|which option|all of the above|none of the above|true or false)\b/i;”
- `g9/transformer/src/glue/threejs-render.js` (145): “skipped.push({ id: b.id, reason: "its question only works beside its options" })”
- `g9/transformer/src/glue/threejs-render.js` (147): “entry: { q: it.stem, expects: [right], source: "draft" }”
- `grade3-reading/ui-audit-2026-09-08/round-5/question-scope/REPAIR.md` (5): “The question says Who flew first? with Peter Pan among the options, while the prior story says Peter already floated and its wrong-Peter feedback explicitly confirms he was already airborne.”
- `grade3-reading/ui-audit-2026-09-08/round-5/question-scope/REPAIR.md` (7): “Cause: the question omitted the comparison group; answer-index testing alone never tests competing interpretations.”
- `grade3-reading/ui-audit-2026-09-08/round-5/question-scope/REPAIR.md` (7): “Change only the silent stem to Which of the Darling children flew first?”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (3052): “The question says Who flew first? with Peter Pan among the options, while the prior story says Peter already floated and its wrong-Peter feedback explicitly confirms he was already airborne.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (3052): “Change only the silent stem to Which of the Darling children flew first?”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-16.md` (54): “three stems are completion fragments — p2 `vocab-nursery-form2` ("…is called a...", has a clip → recut), p17 `skill-check` ("…are there to show ___", silent), p24 follow-up full/brief ("…tells us she is ___", no clip)”
- `g9/transcript/chat-transcript.redacted.txt` (5159): “The following feels a little disconnected - "You job is to trace how he goes from one to another - from A to B" - A and B have non definition.”
- `grade3-reading/course-renderer/docs/feedback/g3-internal-review-2026-08-12.md` (69-71): “When I read the story and went to answer "Right after the Sky-God named his price, what did he do?" nothing came to mind, and then when I read options I got some idea.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (12): “I censused every stem in L1 (13) and L2 (19) — 32 for 32 are direct questions, zero ellipsis or blank-completion.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (97): “D5.11 (three completion-fragment stems): DONE — rewritten as questions”

Against: none found

<sub>criterion · stem, wording · universal · from ap, g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### A summary cloze on the causal links

Put a summary gap-fill's blanks on the causal links that hold the whole text together, never on incidental details or connecting words. The specification sets exactly four blanks, and the course gives them a bank of six words.

The curriculum's lesson-component specification makes the summary a compressed, causal retell with exactly four blanks on the links in the student's mental model, so that it checks the student followed the flow of the story, not incidental detail, and uses wrong words that were true earlier but not now to test that the student tracked the change (`grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/procedures/Example_Lesson_Components.txt`, line 20). The course's criteria register adds a bank of six words, answers true to the text and no blank on a connecting word, checked by a person (`grade3-reading/artifacts/criteria-register.csv`, line 26).

Quoted:

- `grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/procedures/Example_Lesson_Components.txt` (20): “so it checks that the child has followed the flow of the story, not incidental detail”
- `grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/procedures/Example_Lesson_Components.txt` (20): ““true-earlier-but-not-now” distractors test that the child tracked how things changed”
- `grade3-reading/artifacts/criteria-register.csv` (26): “exactly four blanks on the links of the mental model, bank of 6, answers text-true, no connective blank”
- `downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx` (20 (textutil text)): “exactly four blanks that sit on the links in the child's mental model — so it checks that the child has followed the flow of the story, not incidental detail.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx` (12 (textutil text)): “It covers the whole text and teaches children what a summary is, instead of a section untouched by the other exercises.”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (151): “each blank sits on a link in the mental model (the leaver, the friend, the refusal, the promise).”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 9. The Invisible World Microorganisms - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx` (195 (textutil text)): “Rule 3: cloze on the untouched "What Are Microorganisms?" and "Why They Matter" sections, tap-in-order not drag.”
- `grade3-reading/curriculum-gen/audits/PETER-PAN-AUDIT-2026-08-24.md` (96-97): “It must immediately follow the full read, compress the causal story flow, include the taught word”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/HUMAN-g3r-2026-07-27T08-38-36-019fa24b-fb42-7e61-a954-216db3ef77a4.md` (1108): “It is a compressed, causal retell of the story with exactly four blanks that sit on the links in the child's mental model — so it checks that the child has followed the flow of the story, not incidental detail.”

Against: The whole-text rule was not applied consistently: six of the nine science designs still certify the old untouched-section gap-fill in their closing line, for example `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 9. The Invisible World Microorganisms - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx`, line 195.

<sub>criterion · format, distractors, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A theme drawn from the text itself

Derive a text's theme from patterned details in that text, never from a moral the unit planned in advance.

A Grade 5 reading course's curriculum graph lets a unit's related myths explore the consequences of ignoring limits, but says the exact theme must be derived from each text rather than imposed in advance. Its link from quoting evidence to theme requires patterned support in the text rather than a free-floating moral, and its task comparing two tellings of a myth explains a shared pattern without imposing a universal moral. These are definitions in a design graph; no outcome was measured.

Quoted:

- `incept-package-hub/course-packages/courses/g5-reading/review/evidence/course-graph-guide.md` (51): “the exact theme must be derived from each text rather than imposed in advance.”
- `incept-package-hub/course-packages/courses/g5-reading/review/evidence/course-graph-guide.md` (103): “Theme claims require patterned textual support rather than a free-floating moral.”
- `incept-package-hub/course-packages/courses/g5-reading/review/evidence/course-graph-guide.md` (77): “without imposing a universal moral.”

Against: none found

<sub>criterion · key, demand, stimulus · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A writing task leaves nothing to guess

A writing task must say what to write about, in what form, at what length and from which sources, leaving the student nothing to guess. One rubric requires four things of every extended-writing prompt: the topic, the form, the length and the sources.

The evaluator's extended-writing rubric requires every prompt to specify what to write about, the form, how long or how many paragraphs, and what sources to use (`shadow/bench/src/inceptbench/prompts/question/ecr_evaluation.txt` lines 119-120). A mandatory audit fails the prompt outright when the writing mode is unclear or a student can't tell the genre from the prompt alone (lines 54-60). The short-answer rubric likewise requires the stem to say exactly what the student needs to write about, and fails vague stems and stems that ask two questions (`question/scr_evaluation.txt` lines 124-129).

Quoted:

- `shadow-bench/src/inceptbench/prompts/question/ecr_evaluation.txt` (119-120): “- The prompt must specify: (a) what to write about, (b) what form to write in, (c) how long/how many paragraphs are expected, (d) what sources to use.”
- `shadow-bench/src/inceptbench/prompts/question/ecr_evaluation.txt` (59-60): “A student must be able to determine what kind of writing is expected without guessing.”
- `shadow-bench/src/inceptbench/prompts/question/scr_evaluation.txt` (124): “- The question stem must specify exactly what the student needs to write about.”

Against: none found

<sub>criterion · stem, format · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### A wrong key or fact fails the item

Every part of an item, shown to students or not, must be factually right and agree with the key, since a wrong key or fact anywhere fails the whole item. Over 1,124 graded rows, an item whose factual accuracy scored zero passed 0% of the time.

A criteria pack built from 1,124 graded rows of one AP model found that when factual accuracy or source quality scored zero, the row passed 0% of the time, and marked both as must-pass gates (the pass-criteria `README.md`, lines 12 and 72). The AP evaluator's scoring table counts a wrong answer or false claim as a critical failure, and with one critical failure an item scores 0.84 at most, below the 0.85 where acceptable begins (`_base_evaluation.txt`, lines 232, 244, 250 and 262). Being right and agreeing with the key applies to explanations, hints, feedback, model answers, marking notes and source details alike, and a failed source fails the item as surely as a wrong key, however good the rest is.

Quoted:

- `icloud-work/aptraining/helpers/data/output/ib_pass_criteria_pack/README.md` (72): “When `factual_accuracy` or `stimulus_quality` zeros, the row passes 0% of the time (kills=1.0).”
- `icloud-work/aptraining/helpers/data/output/ib_pass_criteria_pack/README.md` (12): “(c) empirical decisive-weight from 1,124 real graded rows of v80b (the current chain-final canonical model)”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt` (250): “| 1 | 0–2 | 0.70–0.84 | INFERIOR |”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt` (232): “- Wrong answer, false claims → `factual_accuracy`”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt` (244): “Let **C** = count of CRITICAL metric failures: `factual_accuracy`, `educational_accuracy`”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt` (262): “- **ACCEPTABLE (0.85–0.98)**: Meets quality standards”
- `icloud-work/ML learnings/evaluation_methodology.md` (40): “This is NOT just overall_score ≥ 0.85. An item can score 0.92 overall and still hard-fail if a single hard-fail dimension drops below 1.0. The hard-fail dimensions are binary gates — they must all be perfect.”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (86): “- Must produce 7 distinct documents”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (89): “- One wrong date in one document = hard fail for the whole DBQ”
- `icloud-work/ML learnings/what_is_ap_and_why_it_matters.md` (125): “4. Wrong information in practice questions could hurt student performance on the actual exam”
- `icloud-work/ML learnings/what_is_ap_and_why_it_matters.md` (128): “- InceptBench's hard-fail on factual_accuracy is not optional”
- `icloud-work/ML learnings/research_educational_content_generation.md` (180): “- **Medical domain** (strictest): 100% factual accuracy required for clinical exam questions; 69% pass rate reported for unconstrained GPT-4 generation”
- `icloud-work/ML learnings/research_educational_content_generation.md` (181): “- **General educational** (moderate): Human-in-the-loop acceptance rate used; no hard threshold”
- `icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-04T1430Z_v40h_spot_verify.md` (40): “Mixing one wrong example into a list of three discredits the sample response.”
- `icloud-work/aptraining/workspace/comms/_deprecated/helpers/oracle/scoring/docs/full_docs/internals/ap-evaluation.md` (135): “These dimensions must score 1.0 for the question to pass. A score below 1.0 results in automatic failure regardless of overall score.”
- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md` (29): “- Factual claims, answer keys, rationales, feedback, and support fields all count for `factual_accuracy`.”
- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md` (38): “- The keyed answer must be factually correct and internally consistent with all explanations, hints, feedback, and additional details.”
- `icloud-work/evaluator/ap_benchmark/calibration/gold_standard.json` (460): “"failure_reason": "Factual inconsistency: Question says 1946 (correct), but explanation says 1948 (incorrect)"”
- `icloud-work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py` (194): “Answer explanations must not contradict option text.”
- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md` (19): “The practical rule for the generator is: **do not aim for “mostly good”; produce a checklist-complete item with no score-zero openings.**”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pil_monitor/inbox/2026-05-19T1456Z_den_unit1_trap_verifier.md` (17): “Observed LLM-required failures are mostly not structurally bad items. They are good-looking items poisoned by historically wrong teacher-facing metadata:”
- `aptraining-local/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md` (87): “SAQ can have fine prompts but fail because the sample response contains factual errors.”
- `aptraining-local/parallel-ideas-lab/reports/24H_CARETAKER_STATE_20260521.md` (27): “`ap-apush-1-mcq_set-medium-12` improved from `0.33` to `0.97`”
- `grade3-reading/ui-audit-2026-09-08/round-5/final-standard-verification/l6-dialogue-ship-wording/SHIP-WORDING-TRIAGE.md` (32): “These authored lines provide a plausible source for the model's “took the ship” wording.”
- `othello-archive/sources/act1/KB - Overview.csv` (145): “Iago does follow Othello, but for himself.”

Against: outside that field, published practice uses a human-in-the-loop acceptance rate with no hard threshold (`icloud-work/ML learnings/research_educational_content_generation.md`). In an earlier AP evaluator one non-critical failure still scored 0.85 to 0.89, a pass, and only a critical failure such as a wrong fact always failed (`icloud-work/evaluator/docs/EVALUATION_PROCESS.md`, lines 97-123), so whether every other flaw sinks an item depends on the grader. The rise from 0.33 to 0.97 came under a release that also tightened leak checks, so the explanation fix alone is not shown.

<sub>criterion · key, integrity, stimulus · universal · from ap, research · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Access without changing what is measured

Let no access need block participation, use equivalent access modes only where what is measured stays unchanged, so reading-test passages are never read aloud, and disclose supports that change it.

The review hub's student-course quality standard makes it a universal requirement that access needs neither prevent participation nor change the construct without disclosure, shown by automated checks plus manual keyboard, focus, screen-reader, zoom, contrast, reduced-motion, target-size, audio-fallback and target-device tests on the exact artifact. Its requirement for source-based work lets the complete first encounter with a source use an equivalent access mode when that does not change the construct. Both are requirements of a standard, with no measured outcome behind them.

Quoted:

- `grade3-reading/edullm-review-hub/course-packages/quality/golden-student-course/versions/1.0.0/STANDARD.qmd` (568): “Access needs do not prevent participation or change the construct without disclosure.”
- `grade3-reading/edullm-review-hub/course-packages/quality/golden-student-course/versions/1.0.0/STANDARD.qmd` (640): “A complete encounter may use an equivalent access mode when that does not change the construct.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/skill/SKILL.md` (54): “TTS on stems/answer choices only — NEVER on reading passages”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/skill/SKILL.md` (54): “Passages read aloud measure listening comprehension, not reading (NWEA's own per-part TTS control enforces the same boundary).”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RED_TEAM_RESPONSE.md` (97): “TTS available on stems and answer choices, **not on reading passages** (a reading-comprehension score obtained with passages read aloud measures a different construct)”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md` (342): “- No audio — cold, silent reading”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/ADDRESS_STATUS.md` (66): “The accommodations note claimed TTS on stems/choices; **the product had none**”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/ADDRESS_STATUS.md` (66): “stems+choices only, never passages”

Against: The reference publisher leaves construct policy to states (`grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RED_TEAM_RESPONSE.md`, line 97), so where the line falls can differ from one state's test to another's.

<sub>criterion · accessibility, measurement, stimulus · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Accessible interaction types from the start

Every interaction a student uses must work by keyboard and assistive technology and be legible, checked from the start, because an item a learner can't operate yields an invalid score. In one reading course, 406 of 1,005 items (40%) could not be operated by keyboard or assistive technology.

A round-1 red team of a grade 4 reading course counted 406 of 1,005 items (40%) that could not be operated by keyboard or assistive technology (`grade3-reading/ti-courseplans/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md`). In a grade 5 course the anti-leak design deliberately concentrated items in hot-text, sequence and match formats (525 of 772), precisely the accessibility-risk types (`grade3-reading/ti-courseplans/docs/redteam-sources/g5-reading-redteam-round1-2026-07-06.md`). A review of the grade 3 course found its drag-and-drop and matching items unusable this way and added that an item type that cannot be made accessible is also not a faithful rehearsal of the test. The item generator's rubric now builds accessibility in from the start, because the team's own evaluation had never checked it (`grade3-reading/ti-courseplans/docs/course-formula-agents.md`). This covers drag-to-order, text selection and audio controls. No anti-guessing control may block an accessible path or let a screen reader give part of the answer away, as when 192 of 198 match items announced an unused decoy category to screen readers (`grade3-reading/artifacts/g5_build_2026_07_02/package/G5_EXECUTED_ACTIONS_CHECKLIST.md`, line 39; `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd`, line 535).

Quoted:

- `grade3-reading/ti-courseplans/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md` (63): “* Accessibility: 406/1,005 (40%) not keyboard/AT-operable”
- `grade3-reading/ti-courseplans/docs/redteam-sources/g5-reading-redteam-round1-2026-07-06.md` (15): “the anti-leak thesis deliberately concentrates items in the TEI formats (hot-text/sequence/match = 525/772) that are precisely the accessibility-risk types.”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (128): “An item type that cannot be made accessible is also not a faithful rehearsal of the test.”
- `grade3-reading/ti-courseplans/docs/course-formula-agents.md` (224): “*WCAG in the rubric, not as an afterthought* — G3 was flagged because the team's own eval **never checked accessibility** (a criteria gap)”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RED_TEAM_FINDINGS.md` (41): “an inaccessible item isn't just bad UX, it's an invalid score.”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (103): “An item type that cannot be made accessible is also not a faithful rehearsal of the test.”
- `grade3-reading/artifacts/g5_build_2026_07_02/package/G5_EXECUTED_ACTIONS_CHECKLIST.md` (39): “192/198 match items announce a `__decoy_unused` "Unused category" target to screen readers”
- `grade3-reading/artifacts/g5_build_2026_07_02/package/G5_EXECUTED_ACTIONS_CHECKLIST.md` (38): “a clean static scan does **not** imply a WCAG 2.1 AA pass (dynamic half in NOT-done)”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (126): “must be accessible to all students (WCAG 2.1 AA and Section 508)”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (128): “The drag-and-drop and matching items are not keyboard or assistive-technology operable”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (128): “one hot-text item offered twelve selectable options, an excessive motor and cognitive load for an eight-year-old.”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (130): “Engineer keyboard and assistive-technology support for every interaction and cap the number of selectable options.”
- `grade3-reading/knowledge_bot/knowledge/kb-0085-g5-red-team-findings-2026-07-06.qmd` (25-26): “RT-2 accessibility: anti-leak concentrates items into TEI formats (525/772), no attestation.”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (370): “**Accessibility (#10) is now a hard LEGAL blocker** (drag-to-order + hot-text keyboard/AT; check how MAP implements).”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/app-package-agent.md` (37): “Keyboard-operable and screen-reader-aware vocabulary and audio controls.”
- `ti-courseplans-audit/docs/redteam-sources/g5-reading-redteam-round1-2026-07-06.md` (15): “the anti-leak thesis deliberately concentrates items in the TEI formats (hot-text/sequence/match = 525/772) that are precisely the accessibility-risk types.”
- `ti-courseplans-audit/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md` (63): “Accessibility: 406/1,005 (40%) not keyboard/AT-operable”
- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (535): “Anti-gaming controls must not block legitimate accessibility paths.”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (128): “An item type that cannot be made accessible is also not a faithful rehearsal of the test.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (105): “The Axolotl lesson's opening selection item rendered black text on a black background, legible only on hover.”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (130): “Engineer keyboard and assistive-technology support for every interaction”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/STUDENT_READY_CRITICISM_FRAMEWORK.qmd inside it) (126-128): “The student may use keyboard navigation, assistive technology, non-hover access, or high-contrast needs. Drag/match/hot-text designs cannot be defended by saying they are good anti-leak items if the renderer blocks some students.”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/approval-package/VISUAL_RUNTIME_ACCEPTANCE.md inside it) (16-17): “- `D10-ACCESSIBILITY-EVIDENCE.md`: match and hot-text keyboard paths passed the recorded inspection; sequence keyboard movement failed to reorder neighbours and remains a renderer/platform defect.”
- `grade3-reading/_archive/2026-08-13-consolidation/top-level-docs/HANDOFF_3_KEY_ISSUES.md` (50): “- **Skeleton V2 decision (G5):** MCQ/MSQ eliminated from the build after 99.5–100% leak; match pool culled to 653; this SUPERSEDED the MCQ-regen effort — don't restart regen.”
- `grade3-reading/edullm-review-hub/course-packages/quality/golden-student-course/versions/1.0.0/STANDARD.qmd` (535): “Anti-gaming controls must not block legitimate accessibility paths.”
- `grade3-reading/course-renderer/docs/rules/accessibility.md` (40-42): “"The drag-and-drop and matching items are not keyboard or assistive-technology operable... An item type that cannot be made accessible is also not a faithful rehearsal of the test."”
- `othello-archive/src/scene/Moment.tsx` (62): “keyboard: Enter makes a click move (the canvas is not focusable)”
- `g9/prototypes/app-narrated-qa/QA.md` (28): “Tab lands skip-link → settings → content → footer; `:focus-visible` 3 px #b98c45 outline; 0 icon-only buttons”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RED_TEAM_FINDINGS.md` (72): “**Accommodations policy now, WCAG audit moved up from Stage 4** — an inaccessible assessment item is an invalid score, not a cosmetic gap.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/ADDRESS_STATUS.md` (51): “**WCAG**: automated audit DONE + fixes merged (PR #55: critical 4→0, serious 2→0, EBSR keyboard fixed)”

Against: The grade 4 count was disclosed as platform-dependent: whether an item can be operated also depends on the platform that serves it (`grade3-reading/ti-courseplans/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md`). The same checklist says a clean static scan does not imply a WCAG 2.1 AA pass, and the dynamic half of the audit was not done. the 406/1,005 figure is marked platform-dependent (`ti-courseplans-audit/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md`). The real test uses the same formats for Grade 3, so the fix is to build them accessibly, as the test does, rather than drop them: "MAP uses these for G3 — check MAP's implementation" (`grade3-reading/knowledge_bot/knowledge/kb-0076-coe-catchup-2026-06-30.qmd`, line 21).

<sub>criterion · accessibility, format, integrity · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Aligned to the target, not the topic

Fit an item and its sources to the exact target and focus its standard or objective names, not to its broad topic, period, theme or kind of evidence. A document-based essay task on the wrong sub-topic scored 1.0 for alignment while the rubric failed only a completely different subject.

A document-based essay task requested on one sub-topic came back about others and still scored 1.0 on alignment, because the rubric failed only a "completely different subject/topic" and the judge called both the same general domain (issue 1004, `icloud-work/inceptbench-main/tests/test_evaluator_prompt_rules_1004.py`). The essay rubric now fails prompts and documents on a different focus even within the same period or unit (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/dbq_evaluation.txt`), and an audit for choice items requires the options to make claims about the standard's named target, not a different subject inferred from the same evidence (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt`). Check the finished item against that objective, since a source that doesn't fit can do worse than none.

Quoted:

- `icloud-work/inceptbench-main/tests/test_evaluator_prompt_rules_1004.py` (8-10): “Root cause: the DBQ evaluation prompt used "completely different subject/topic" as the failure threshold, allowing the evaluator to rationalize that gender roles vs religion/labor were "same general subject domain" and therefore pass.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (53): “The distinction that matters: the answer options must make claims **about the standard's named target**, not about a *different* subject that can be *inferred using* the same evidence. The evidence type and the cognitive target are not the same thing.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/dbq_evaluation.txt` (29): “A DBQ whose prompt and documents address a DIFFERENT specific analytical focus or sub-topic than what the standard explicitly requires, even within the same broad historical period or unit.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/DBQ_GAP_ANALYSIS.md` (4): “Failures are driven almost entirely by **topic/rubric misalignment**, not hallucination or structural errors.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/a0f_completed_failure_map_20260520.md` (23): “| quality_fail_standard_alignment | 156 |”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/IB_A0F_99_RECOVERY_PLAN_20260519.md` (214): “1. The item drifts from the requested substandard into a nearby Unit 1 topic.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/a0f_completed_failure_map_20260520.md` (7): “- Total requests: 1080”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/a0f_completed_failure_map_20260520.md` (21): “| quality_fail_chronology | 24 |”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/DBQ_GAP_ANALYSIS.md` (9): “1. **Topic Extraction Pre-step:** Extract the exact "core required theme" from the LO before pulling documents.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/DBQ_GAP_ANALYSIS.md` (12): “4. **Validation Gate:** Add a fast pass/fail judge comparing the final DBQ rubric focus against the raw LO sub-topic before finalizing the payload.”
- `shadow-bench/src/inceptbench/evaluators/guards.py` (2157-2161): “The evaluator may admit that the DBQ prompt and documents address a different specific sub-topic or analytical focus than the standard requires (e.g., the standard asks for gender roles but the DBQ covers religion, labor, or sovereignty), yet rationalize a pass by claiming it falls within the "same general subject domain" or "same broad historical period."”
- `shadow-bench/src/inceptbench/evaluators/guards.py` (2162-2163): “When this self-contradiction is detected, override curriculum_alignment to 0.0 and recompute the overall score.”
- `shadow-bench/src/inceptbench/prompts/question/_base_evaluation.txt` (34): “- Failing `curriculum_alignment` because the question tests a closely related skill within the same subject and topic.”
- `shadow-bench/src/inceptbench/prompts/question/_base_evaluation.txt` (34): “Only fail for completely different subjects or unrelated skills.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/B0045_STAGED_MCQSET_INTERIM_20260519.md` (25): “3. Regression risk: broad winner reuse can fail a narrower substandard, as seen for gender/family when a labor-oriented passed sibling was reused.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/UNIT1_TO_ALL_UNITS_TRANSFER_PLAN.md` (80): “- Description-specific routes must beat generic lesson-title matches.”
- `aptraining-local/analyzer/reports/run_f54d5849_what_is_going_wrong.md` (20): “Of 125 DBQ failures: **`curriculum_alignment = 0` in 98 % (122 / 125); `factual_accuracy = 0` in only 2 % (3 / 125).**”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/a0f_failure_map_20260519.md` (24): “| quality_fail_standard_alignment | 71 |”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/ib_d13_wrapper_eval/RESULTS.md` (24): “- The local v4 retrieval/doc-lock route is not usable as-is: it frequently retrieves irrelevant/misaligned packs, and doc-locking those packs hurts.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/ib_d13_wrapper_eval/RESULTS.md` (15): “| Local v4 D13 doc-lock | `y4axbi4f_d13_doclocked_generations.jsonl` | 0/30 | 0.0% | 0.1283 | 1 | 0 |”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/ib_d13_wrapper_eval/RESULTS.md` (14): “| Local v4 D13 prompt-wrap only | `y4axbi4f_d13_wrapped_generations.jsonl` | 3/30 | 10.0% | 0.3030 | 1 | 1 timeout |”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/full150_y4axbi4f/RESULTS.md` (26): “| apush/dbq | 0/30 | 0.00% | 0.673667 |”
- `aptraining-local/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md` (106): “- source pack mismatch, e.g. prompt names Africans but documents only cover Native Americans.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (88): “- Dynamic DBQ cannot be allowed to invent source documents. It needs retrieved vetted documents or document-bank retrieval by standard. Source retrieval fixed the focused institution DBQ slice: `dynamic_source_gate_dbq_mcqset_v1` DBQ scored 0.98.”
- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE5.md` (9): “topic coverage does not equal source compliance.”

Against: The general question rule stays lenient: it passes a question that exercises the named skill or any prerequisite, component or application within the same domain and grade-level topic (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt`, line 163), so the stricter test applies only through that audit and the essay rubric. The general rubric is looser: it lists as a false positive to avoid '- Failing `curriculum_alignment` because the question tests a closely related skill within the same subject and topic.' and says 'Only fail for completely different subjects or unrelated skills.' (`shadow-bench/src/inceptbench/prompts/question/_base_evaluation.txt`, line 34). The guard runs on document-based essay items only. Retrieval keyed to the exact objective worked: one slice of document-based items scored 0.98 once vetted documents were retrieved by standard. Pass counts were 0 of 30 both with the lock and in the baseline, so the gap is in mean score, and the same wrapper with prompting only passed 3 of 30.

<sub>criterion · alignment, options, stimulus · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### An inference is never written out

An inference question's answer must be supported by the text but not stated in it, because a stated conclusion only tests finding.

A reading curriculum's inference lesson design ends with a soundness sweep that checks both answers are supported by the text but not stated: neither reason is written out, and both are inferred. Its quick finding checks are the contrast case, where the answer is stated in the sentence just read. A stated conclusion is a leak unless finding the answer is the skill being tested.

Quoted:

- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (354 (textutil text)): “Both answers supported by the text, not stated.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (354 (textutil text)): “Neither reason is written out; both are inferred.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (89 (textutil text)): “Pure literal FIND: the answer is stated in the sentence just read.”
- `grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd` (26-27): “in reading, finding the answer in the passage IS the skill, so the usual history-style "answer is in the source" leak check is deliberately skipped.”
- `grade3-reading/knowledge_bot/knowledge/kb-0231-pp-depth-6h-doc-diffs.qmd` (75-76): “stating the trait/conclusion itself is a disguised-FIND violation).”
- `grade3-reading/knowledge_bot/knowledge/kb-0231-pp-depth-6h-doc-diffs.qmd` (84): “| **Total** | **18** | **16** | **1** | **1** |”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (469): “Do not state the lesson's takeaway in the text”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (472): “The passage must let the child infer the point. Do not write the moral into the story.”
- `grade3-reading/course-renderer/docs/rules/content-and-copy.md` (217-218): “**Rule.** The passage must let the child infer the point. Do not write the moral into the story.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (336-339): “the review warns against choosing texts that are too explicit, because "very explicit texts provide few opportunities for inferences to be made", which is an argument against a passage that states why anybody did anything.”
- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE3.md` (52): “The original Design 1 explicitly calls betrayal/betrayed an encapsulating word absent from the text and reserved for the independent task. This change makes the interpretation appear directly in the passage.”
- `grade3-reading/workspace/comms/from_plan/2026-08-31T182831Z-work-queue.md` (57-59): “A you-do explicitness table per lesson: item id, question text, verdict (TEXT-STATES-IT-EXPLICITLY / REQUIRES-INFERENCE), with the source passage line quoted for every EXPLICIT verdict”
- `grade3-reading/artifacts/pp-depth-6h/INFERENCE-INTEGRITY-L5-L7.md` (52): “the item explicitly frames itself as an inference ("one thing the text does not say straight out") and instructs the child to use the exact two words ("clever," "brave") that the very next sentence of the pinned passage states outright.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (273): “Both answers are stated outright in the paragraph above, which is appropriate for a Check but means it is retrieval, so the lesson needs something beyond it.”
- `grade3-reading/knowledge_bot/knowledge/kb-0231-pp-depth-6h-doc-diffs.qmd` (112-113): “sequence is currently correct, flagged only because a future reorder of p21a ahead of p16b would create a violation.”

Against: The probe covered 18 items in three lessons of one course, and the project treats its reading leak check as a build-time lint, not a deep guarantee (`grade3-reading/knowledge_bot/knowledge/kb-0221-early-planning-history-and-sep22-snapshots.qmd`).

<sub>criterion · demand, key, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Answers in a set must agree

No correct answer in a set may contradict another, and what one step marks right or teaches must still hold in the next, so check the whole set.

The rubric-derived writer prompt for question sets (`system_prompt_mcq_set.md`) lists contradictions between questions among its set-level fail traps: one question's correct answer saying that X caused Y while another's says that Y caused X. It asks for consistency to be audited across the whole set, on top of the checks each question gets on its own.

Quoted:

- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq_set.md` (89): “6. **Inter-question contradictions**: Q1's correct answer says "X caused Y", Q3's correct answer says "Y caused X". Audit consistency across the set.”
- `shadow-content-eval/reports/G3-U1-L2-review.md` (22): “A student who carries their Step 3 words forward, as the method teaches, fails Step 4.”
- `shadow-content-eval/reports/G3-U1-L11-review.md` (26): “A student who follows steps 1 and 2 as taught ends up looking in the wrong paragraph for the clue they must copy.”
- `shadow-content-eval/reports/G3-U1-L12-review.md` (22): “A student who carries Step 3's answer forward gets marked unpredictably.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/CONTENT-SCHEMA.md` (426): “A we-do that disagrees with its own floor teaches the child two different answers to one question”
- `othello-archive/sources/act1/KB - Overview.csv` (148): “undercut the lesson's defiant AND dutiful thesis.”

Against: none found

<sub>criterion · key, integrity · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Ask about every inference the text sets up

Plan at least two inference points in every passage and ask a question that needs each one; an inference the text sets up that no question asks is decoration. An audit counted 3 inference points in one lesson against the minimum of 2, each with its own question.

The grade-3 rulebook's first question rule has every passage carry at least two inference points, a feeling or motive shown rather than stated, or a design choice in the writing worth interpreting, each cashed by a question that requires it. Shown-not-stated with no question is decoration, and a why question about a stated fact is recall in a costume. An audit of one lesson counted three such points, each cashed by its own question.

Quoted:

- `grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md` (184-187): “**R1**: every passage carries ≥2 inference points — feeling/motive SHOWN not stated, or authorial design worth interpreting — and EACH is cashed by a question that requires it. Shown-not-stated with no question = decoration; a why about a stated fact = recall in a costume.”
- `grade3-reading/artifacts/l4-audit/03-INSTRUCTION-DESIGN.md` (175): “≥2 inference points, each cashed by a question — L4 carries 3”

Against: none found

<sub>criterion · demand, stimulus, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Ask about goals and motives

Ask inference questions about characters' goals, motives and relationships: they draw out the causal inferences skilled readers make, building story understanding as effectively as a text stating those links.

Lesson research for a reading unit took its inference evidence from a 2008 literature review for Key Stages 2 and 3, quoted directly. The review reports that asking inference questions about relationships between characters, goals and motivations enhanced story understanding as effectively as modifying the story so that all this information was stated (Sundbye 1987, quoted through McGee and Johnson 2003), and that why-questions were particularly beneficial to pupils in years 4 to 8 (Pressley 2000). The research called the first the strongest single result for its design, since a good motive question does as much as rewriting the text to state the answer. The finding reaches the lesson secondhand, through the review.

Quoted:

- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (266-271): “Sundbye found that asking inference questions about "relationships between characters, goals and motivations enhanced story understanding as effectively as if the story had been modified so that all this information were explicitly stated" (Kispal, quoting McGee and Johnson 2003 on Sundbye 1987). That last one is the strongest single result for our design: a good motive question does as much as rewriting the text to state the answer.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (264-265): “Pressley found why-questions "particularly beneficial to pupils in years 4-8"”
- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (241-243): “My primary source is the NFER review of the inference literature for Key Stages 2 and 3 by Kispal, which reviews the primary studies and is quoted below”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (259-261): “comprehension is guided by why questions, rather than what-happens-next, how, when or where questions”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (261-262): “the answers to why-questions expose superordinate goals and causal antecedents”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (265): “why-questions "particularly beneficial to pupils in years 4-8"”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (267-269): “relationships between characters, goals and motivations enhanced story understanding as effectively as if the story had been modified so that all this information were explicitly stated”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (347-348): “Although the characteristics of good inferencers have been identified, there is limited research evidence”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (350): “the routine is well motivated and thinly evidenced as a routine”

Published: [Kispal 2008](https://eric.ed.gov/?id=ED501868) · [Sundbye 1987](https://doi.org/10.2307/747722) · [Effective Teaching of Inference Skills for Reading: Literature Review (NFER for the DCSF, 2008, DCSF-RR031)](https://www.nfer.ac.uk/publications/effective-teaching-of-inference-skills-for-reading-literature-review/)

Against: The same review cautions that, although the characteristics of good inferencers have been identified, "there is limited research evidence" on how best to improve pupils' inferencing, and the brief calls its routine well motivated and thinly evidenced as a routine (`grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md`, lines 347-350). Where such questions go also matters: in another study, frequent causal questions during reading cut grade-4 recall of what they did not ask about (few-questions-during-reading).

<sub>criterion · demand, stem · universal · from g3, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Ask about one link in a chain

A cause question over a chain of causes must name the one link it asks about, because 'what causes this?' makes several links defensible. Six practice items were dropped after a quality screen showed more than one defensible key, traced to causal-chain passages asked 'what causes X?'.

A cross-family quality screen of Grade 3 items that had passed a blind-solve gate showed six practice items with more than one defensible key, each confirmed by reading it; the report gives the root cause as a passage built as a causal chain with a 'what causes X?' prompt, made worse when the key is set on a link further back to defeat blind solvers. A QA pass over a shared item bundle confirmed a matching item with several correct answers for the same reason, and the report calls for a single-link redesign of chain-based items.

Quoted:

- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (102): “6 practice items dropped after the screen credibly showed a **multi-defensible key**”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (104-105): “Root cause: a causal-**chain** passage + a "what causes X?" prompt makes several links defensible, and anti-leak keying the *non-proximate* link worsens it.”
- `grade3-reading/artifacts/alpha-read-packager/BUNDLE_CONTENT_BUGS.md` (53): “The passage is one continuous transitive causal chain”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (128): “chain-based hot-text/EBSR need a single-link redesign (a future round)”

Against: none found

<sub>criterion · stem, key · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Ask about the writer's structural choices

Ask why a writer structured a text as they did, not how many paragraphs or headings it has, since the state reading test rewards explaining the writer's choices. A learner who says a text's structure is that it has four paragraphs has counted its parts, not explained the writer's choices.

In a build meeting on 8 October 2026, one participant said the state reading test asks learners not only to recognise a text's structure but to talk about the writer's choices, and that some questions in another reading course only asked them to spot features, such as how many headings an article has, which that test does not reward (`g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_08 10_30 CEST - Notes by Gemini.md`, lines 366-370). The same participant said learners have a poor sense of why a writer has structured something and tend to think structure simply means how many paragraphs a text has (line 374). The transcript is machine-made, and its 'STAR' is the state test.

Quoted:

- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_08 10_30 CEST - Notes by Gemini.md` (366): “they need to not only recognize the structure, but the key thing in the STAR tests is why they need to be able to talk about the writer's choices.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_08 10_30 CEST - Notes by Gemini.md` (366): “they're simply asking kids to just feature spot.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_08 10_30 CEST - Notes by Gemini.md` (370): “They're saying how many headings are in this article or you know none of that is rewarded in the STAR test.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_08 10_30 CEST - Notes by Gemini.md` (374): “kids have a very poor understanding of why a writer has structured something”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_08 10_30 CEST - Notes by Gemini.md` (374): “whereas the kid thinks that structure simply means oh it's got four paragraphs”

Against: It is one person's account in a meeting, not a measured result.

<sub>criterion · demand, stem, alignment · domain · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Ask for operations with a purpose

Ask only for operations with a purpose in the scenario, since an arbitrary instruction tests whether students follow directions, not the skill. A Grade 3 line-plot question asked for the total number of crayons in all lengths except 2 1/2 inches, with no reason given for leaving that length out.

The evaluator passed a Grade 3 line-plot question asking for the total number of crayons in all lengths except 2 1/2 inches without flagging the exclusion, and review found no reason for leaving out exactly that value. A must-fail audit was added to the math rules: a data-interpretation question must connect its operation to a real purpose in the scenario, and an arbitrary count, sum, exclusion or filter fails educational accuracy because it only tests whether a student can follow an unmotivated directive. The rule rests on that one reviewed item.

Quoted:

- `shadow-bench/src/inceptbench/prompts/question/math_evaluation.txt` (14-19): “Questions that ask students to perform arbitrary, unmotivated operations on data — for example, counting items that exclude a specific value without a stated reason, summing an arbitrary subset, or filtering by a criterion that is not meaningful in the scenario — fail `educational_accuracy` because they do not assess a genuine mathematical skill; they only test whether a student can follow an unmotivated directive.”
- `shadow-bench/` (commit 0af5df4) (3-5): “The evaluator passed a Grade 3 line-plot question asking 'What is the total number of crayons in all lengths except 2 1/2 inches?' without flagging the unmotivated exclusion criterion.”
- `shadow-bench/src/inceptbench/prompts/question/math_evaluation.txt` (23-24): “A good data-interpretation question connects the operation to a real purpose in the scenario”

Against: none found

<sub>criterion · demand, stem, alignment · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Ask what would make anyone act so

Ask what would make anyone act as a character did, not what would make the learner, and check the answer against a clue the text prints.

Lesson research on motive questions, reading a literature review of inference teaching, found that a reader's own background changes the inferences they draw, and that even on texts designed to produce one agreed inference some readers inferred emotions that were the precise opposite of the one intended. The character-motivation variation of the course's inference procedure asks what would make me do what the character did, which the research says invites exactly this projection. It recommends the general form, what would make anyone do that, with the answer then checked back against a printed clue, and the lesson plan adopts the general form. The same research has scoring accept any motive tied to a real clue, with the accept-list written from the clues.

Quoted:

- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (297-300): “Narvaez's work reported in the review found that a reader's own moral and cultural background changes the inferences they draw while reading”
- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (305-307): “even on texts designed to produce one agreed inference "there was no consensus. In fact some readers inferred emotions that were the precise opposite of that intended" (Kispal, quoting Gygax et al. 2004).”
- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (310-316): “That wording invites exactly this failure. My recommendation is to keep the variation but voice it in the general form, what would make anyone do that, and then require the answer to be checked back against a printed clue. Second, single-correct motive items are riskier than they look, so the scoring of the child's written motive must accept any reason that is tied to a real clue, and the accept-list has to be written from the clues rather than from one exemplar sentence.”
- `grade3-reading/course-renderer/content/lesson-plans/g4-u1-l3.json` (106): “Step 3 is where the variation is amended: its published wording is if that happened to me, what would make me do what the character did, and this lesson voices it in the general form instead.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (9): “Written before the lesson is authored.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (309-311): “the character-motivation variation says step 3 is "If that happened to me, what would make me do what the character did?". That wording invites exactly this failure.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (311-313): “My recommendation is to keep the variation but voice it in the general form, what would make anyone do that, and then require the answer to be checked back against a printed clue.”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l3.json` (142): “Step 3 is voiced in the general form, never the first person.”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l3.json` (142): “Do not write if that happened to me, do not write how would you feel, and do not write anything that asks the child to supply their own reaction.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (299-300): “a reader's own moral and cultural background changes the inferences they draw while reading”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (305-307): “there was no consensus. In fact some readers inferred emotions that were the precise opposite of that intended”

Published: [Kispal 2008, Effective Teaching of Inference Skills for Reading: Literature Review, NFER (DCSF-RR031)](https://www.nfer.ac.uk/publications/effective-teaching-of-inference-skills-for-reading-literature-review/)

Against: The research note was "Written before the lesson is authored." (`grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md`, line 9), and no result with learners is recorded for either wording.

<sub>criterion · wording, stem, demand · universal · from g3, research · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Ask where the answer was given

Ask a question right after the part that answers it, make sure it needs that part, and never stop mid-sentence.

A line was added to the film so that the check after its second scene could be answered from what had been heard
(`g9/film/v03/render/QA.md`). In an animated version's first lesson, one part's check could be answered without reading
that part (`g9/review/2026-10-08-lesson1-build-map/README.md`, "Measured"), and in another film the first stop cut in
mid-sentence (`g9/review/three-film-comparison/COMPARISON.md`). The film player pauses at the end of a scene, in its
silent tail (`g9/player/content/archivist-checks.json`). The lesson engine stops a film 0.3 s after the words that
answer a question, and asks the judge whether each question is answered by what has been said by then
(`g9/transformer/src/mechanics/film-check.js`).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd` (42-43): “interpolated inferential questions cut grade-4 recall .30->.07”
- `grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd` (43): “ask AFTER not DURING reading”
- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md` (27): “**14 written causal questions per story** appeared during reading, after reading, or not at all.”
- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md` (29): “The quoted **.30 control → .07 during-reading** result is Grade4 recall of **untargeted information**, not overall comprehension.”
- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md` (31): “**Design conclusion:** frequent unsupported interruptions can be costly for younger readers.”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (204): “G3 iter-3: the passage is one block read ONCE, all questions after it (0 mid-passage stops across 18 lessons)”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (205): “stop at key points INSIDE the text and ask right there (REL West), not only at the end”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D3-reading-architecture.md` (13): “Questions are posed at key points *inside* the text, not only at the end”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (89 (textutil text)): “Pure literal FIND: the answer is stated in the sentence just read.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 10. The Wind in the Willows, Part 3 (FICTION, INFER) — v3 (new INFER design).docx` (85 (textutil text)): “FIND only: the answer is stated word-for-word in the sentence just read.”
- `grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd` (43): “inferential questions cut grade-4 recall .30->.07; her rule is ask AFTER not DURING reading, a”
- `grade3-reading/artifacts/criteria-register.csv` (25): “the answer is stated in the just-read sentence”
- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md` (145): “p7–p12 (never more than 2 reads without a check)”
- `grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd` (42-44): “interpolated inferential questions cut grade-4 recall .30->.07; her rule is ask AFTER not DURING reading”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (205): “stop at key points INSIDE the text and ask right there (REL West), not only at the end”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (639): “- Failure signals: Analysis before encounter; hidden source; universal title shortcut; valid synthesis rejected.”
- `shadow-content-eval/SKILL.md` (66): “the correct option is supported only by passage text *after* this page — unanswerable when asked”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (431): “The CFU is the primary encoding event — retrieval immediately after instruction is what converts short-term exposure to durable memory (testing effect; Roediger & Butler, 2011).”
- `g9/transformer/src/glue/threejs-render.js` (45): “Cut the text so that each checkpoint comes right after the lines its answer is in (the build asks one checkpoint per”
- `g9/transformer/src/glue/threejs-render.js` (57): “a cut moves on to the end of its speech, a few lines at most, and never into the lines the next checkpoint asks about”
- `g9/transformer/src/glue/threejs-render.js` (62): “a short tail joins the last section rather than standing alone, a section with nothing to ask”
- `g9/transformer/src/glue/threejs-render.js` (162): “the build asks one checkpoint per section, and no lines are left after its evidence for one more”
- `g9/transformer/test/threejs-render.test.mjs` (40): “is read before its checkpoint”
- `g9/transformer/src/mechanics/worked-model.js` (84): “the animated build asks the rebuild under the first word's card ("did you follow what I just said?")”
- `g9/transformer/src/glue/threejs-render.js` (6): “its reading sections, cut so that each checkpoint comes right after the lines it asks about”
- `g9/transformer/v02/QA.md` (105): “question is answered by what has been said by its stop”
- `g9/transformer/src/video/produce.js` (110): “const stops = plan.checks.map((c) => ({ after: c.after, at: +(beats[c.after].start + LEAD + beats[c.after].audio_seconds + 0.3).toFixed(2) }));”
- `g9/transformer/src/mechanics/film-check.js` (36): “- cue: the number of the caption whose words answer it (the film stops right after that caption).”
- `g9/player/media/Othello-opening-full.vtt` (27): “in love with his wife, Desdemona,”
- `g9/transformer/test/threejs-render.test.mjs` (30): “the text becomes the build's reading sections, cut so each checkpoint follows the lines it asks about”
- `g9/transformer/test/video.test.mjs` (72): “each stop right after its beat's narration”
- `g9/transcript/chat-transcript.redacted.txt` (5177): “Every question for me is showing up before the content is presented. I wonder if that was because I had paused the content and went back 10 secs once in the beginning.”
- `g9/transcript/chat-transcript.redacted.txt` (5321): “I didn’t reproduce the reported timing drift. Straight playback and an early pause/rewind test both triggered the first question at 1:18, on the same Cyprus-map frame.”
- `g9/script/v02/CHANGES.md` (6): “Without it, check 1 part 2 ("who holds power there?") was inferable but never stated.”
- `g9/film/v03/render/QA.md` (16): “so the Archivist check after scene 2 is answerable from what was heard.”
- `g9/film/v03/render/QA.md` (16): “Scene 2 clip regenerated (42.0 s, word-exact), realigned (matched 1.0).”
- `g9/player/content/archivist-checks-v5.json` (2): “the other three are DRAFTS from what the narration has just said.”
- `g9/transcript/chat-transcript.redacted.txt` (5162): “You come across this question before you have been informed about where acts 2-5 are set”
- `g9/library/text/Ldb4a38.txt` (15): “The first stop cuts in mid-sentence after "Acts 2 to 5 move to Cyprus:", just before "…where the general's word is law", which is the answer to the second stop.”
- `grade3-reading/artifacts/Peter-Pan-L4-review-response-2026-08-25.pdf` (p.3 (pdftotext lines 118-119)): “Still owed: the two questions ask about moments at roughly 0-8s and 24s but both fire in the final seconds. Reachable is not the same as well timed.”

Against: A later run found: a review cited a 2001 study in which inferential questions asked during reading cut grade-4 recall from .30 to .07, and asked for reading questions after the text rather than during it; it was left for a ruling (`grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd`). A later run found: In a published study, interpolated inferential questions cut grade-4 recall from .30 to .07 (van den Broek et al. 2001, https://doi.org/10.1037/0022-0663.93.3.521), and a design review of a reading lesson asked for questions after reading, not during it; this record's evidence is from film, and the timing question is open in its own record (`grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd`). A later run found counter-evidence (`grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd`). A later run found counter-evidence (`grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md`). A later run found counter-evidence (`grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd`). A later run found counter-evidence (`grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd`).

<sub>criterion · alignment, media · universal · from g9 · measured · held · found in [2026-10-12-2-round-1](../research/2026-10-12-2-round-1/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Ask young learners for the target skill

For young learners, ask for the target skill directly, and give prerequisite results or split the item into steps rather than packing a chain of sub-problems into one stem. A Grade 3 question asked students to solve two prerequisite problems and then combine the results, and was judged too complex for the grade.

A Grade 3 question asked students to first solve two prerequisite problems and then use those results to solve a composite problem, and review found the framing too complex for the grade. The math rules now say that for the lower elementary grades (approximately K–3), a stem packed with prerequisite sub-problems, without scaffolding or worked-example framing, can overwhelm working memory and comprehension and fails educational accuracy. The rule rests on that one reviewed item.

Quoted:

- `shadow-bench/src/inceptbench/prompts/question/math_evaluation.txt` (8): “The question should be self-contained and ask for the target skill directly; prerequisite computations should be provided or the item should be broken into separate steps.”
- `shadow-bench/src/inceptbench/prompts/question/math_evaluation.txt` (8): “For the lower elementary grades (approximately K–3), a question stem that asks students to first solve multiple prerequisite sub-problems and then use those intermediate results to solve a composite problem — without scaffolding or worked-example framing — can overwhelm working memory and comprehension.”
- `shadow-bench/` (commit 6078ea3) (3-4): “A Grade 3 question asked students to first solve two prerequisite problems and then use those intermediate results to solve a composite problem.”

Against: none found

<sub>criterion · demand, stem, format · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Assess with more than a few task types

Assess with more than a few kinds of task, because what a test asks shapes what is taught and one usual format can narrow teaching to it.

A reading project's research synthesis quotes the RAND Reading Study Group: assessments that are widely used today focus heavily on only a few tasks and thus may inadvertently limit the reading curriculum to preparation for those few tasks (p. xix) (`ti-courseplans-audit/docs/reading-science/SYNTHESIS.qmd`). The same passage adds that while comprehension is defined by default as reading a passage and answering a few multiple-choice questions, there is little incentive to teach the deeper construct (p. 113). Never let one format, such as a passage with a few multiple-choice questions, become the definition of a skill.

Quoted:

- `ti-courseplans-audit/docs/reading-science/SYNTHESIS.qmd` (127-129): “"assessments that are widely used today focus heavily on only a few tasks and thus may inadvertently limit the reading curriculum to preparation for those few tasks."”
- `grade3-reading/knowledge_bot/knowledge/kb-0108-rand-appendix-b-assessment-rfa.qmd` (127-129): “as long as we define comprehension by default as reading a passage and answering a few multiple-choice questions about it,”
- `grade3-reading/knowledge_bot/knowledge/kb-0108-rand-appendix-b-assessment-rfa.qmd` (120-122): “the absence of attention to these consequences in widely used reading assessments diminishes the emphasis on them in instructional practices as well.”
- `grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd` (699): “**114. Defaulting to 'read a passage, answer a few multiple-choice questions' as the operational definition of comprehension gives teachers little incentive to teach toward a deeper, more accurate conception of the construct.**”
- `grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd` (759): “**124. No single assessment can satisfy all these requirements; the RFA instead calls for building an integrated system of multiple assessments serving different purposes (accountability, diagnosis, instruction-guidance) and different reader groups.**”
- `grade3-reading/ti-courseplans-wiki/Perfect-Course-Rulebook.md` (233-234): “Variety is not a quality goal. The same format can be excellent for one construct and invalid for another.”
- `grade3-reading/ti-courseplans-wiki/Peter-Pan-Quality-Case-Study-2026-08-24.md` (36): “Variety for its own sake is noise.”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (664): “Do not let single-select MCQ dominate; STAAR caps it at 75 percent of points and the 2026-06-29 build was at about 87 percent.”
- `grade3-reading/course-renderer/docs/rules/questions-and-assessment.md` (286-288): “"about 87 percent of items are single-select multiple choice, STAAR's inline-choice and text-entry item types are missing, and at least one item is mistagged."”
- `othello-course-renderer-draft/repo/docs/feedback/academics-review-2026-06-29.md` (88): “But about 87 percent of items are single-select multiple choice, STAAR’s inline-choice and text-entry item types are missing, and at least one item is mistagged (a vocabulary item labelled Inference and Evidence), which weakens the claim of full standards alignment.”

Published: [RAND Reading Study Group 2002, Reading for Understanding: Toward an R&D Program in Reading Comprehension (MR-1465)](https://www.rand.org/pubs/monograph_reports/MR1465.html)

Against: It is a study group's argument from 2002, not a measurement. A later run found counter-evidence (`grade3-reading/ti-courseplans-wiki/Perfect-Course-Rulebook.md`). A later run found counter-evidence (`grade3-reading/ti-courseplans-wiki/Peter-Pan-Quality-Case-Study-2026-08-24.md`).

<sub>criterion · format, measurement · universal · from research · external-research · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Assume and test only what was taught

An item, its options, hints and pointers may require only what the student has met by then on every path, common knowledge, or what the item or reference materials supply. One item's third part required specific knowledge of an 1873 act that is not a standard topic in its course.

The reading project's lint checks that what a lesson assumes is a subset of what earlier lessons in the unit added, in unit order. A weekly quality check still found a taught word that never appears in its lesson's passage, while three of that lesson's checks assessed the child on it. What the item supplies includes the student's reference materials, and a further value or principle must be given too. The same bound covers response forms: no item may require or grade a response form the lesson hasn't taught and modelled.

Quoted:

- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md` (16): “`lesson.assumes` is a subset of the union of prior lessons' `adds`, in unit order.”
- `grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd` (74): “Taught word "betrayal" never appears in the L1 passage”
- `grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd` (75-76): “yet p23/p27b/p28 assess the child on "betrayal."”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md` (67-68): “no cross-unit baseline exists in the contract, so a unit's first lesson must have empty `assumes`”
- `icloud-work/ap-social-studies-generator/python/benchmark_runs/analysis_iter2.md` (58): “However, Part (c) requires specific knowledge of the Timber Culture Act (1873), which is not a standard APUSH curriculum topic”
- `icloud-work/ap-social-studies-generator/python/generators/saq.py` (247): “• ALL parts must be answerable using CORE AP curriculum content”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (76): “That fact must be provided in the stem; students should not be required to supply it from outside knowledge.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (190): “Testing the physics of the tool rather than its application is outside the standard's scope.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/leq_evaluation.txt` (22): “- Score 0.0: Rubric is unachievable (e.g., requires evidence that doesn't exist in the curriculum)”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt` (163): “**PASS if**: the question exercises the standard's named skill, OR any prerequisite/component/application within the same subject domain and grade-level topic.”
- `APinceptbench/docs/GENERATOR_API_SPEC.md` (123): “- A student who knows this fact MUST be able to answer the question correctly”
- `APinceptbench/docs/GENERATOR_API_SPEC.md` (124): “- The question MUST NOT require knowledge outside the scope of this fact (except for scaffolding context)”
- `APinceptbench/ap_benchmark/prompts/official_ap_prompts.py` (237): “- Can each part be answered with AP course content?”
- `APinceptbench/ap_benchmark/prompts/official_ap_prompts.py` (239): “- FAIL if parts require obscure knowledge”
- `APinceptbench/docs/GENERATOR_API_SPEC.md` (242): “- All parts MUST be answerable based on `curriculum_fact` + reasonable outside knowledge”
- `APinceptbench/ap_benchmark/prompts/official_ap_prompts.py` (309): “| **Evidence (Outside)** | 0-1 | Uses specific evidence beyond the documents |”
- `grade3-reading/ti-courseplans/feedback/feedback1/Practice BrainLift.md` (38): “if the feedback needed to correct the response is longer and more complex than the original instruction, the item has crossed the boundary.”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json` (452): “Retrieval may activate prior knowledge, but it must not grade content the course has not taught or established as a prerequisite.”
- `grade3-reading/ti-courseplans/skills/train-teacher/references/gauntlet-spec.md` (82): “| You-do requires untaught knowledge | round 1 F3 |”
- `grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md` (404-406): “the lesson grades the child on producing `The text says "…"` while the modelling omits the quote marks, so we grade a form we do not demonstrate.”
- `grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md` (398): “Reproduced passage text carries quote marks; quote frame punctuated consistently | 60”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/alpha-read/modelling-moment-procedures-v2/INDEX.qmd` (147-149): “it does not introduce an untaught response routine.”
- `shadow-bench/src/inceptbench/prompts/question/ap_chemistry_evaluation.txt` (38-40): “Any value the solution needs must be derivable, on the reference materials, or supplied in the stem. An item that hinges on a recalled constant is broken.”
- `shadow-bench/src/inceptbench/prompts/question/frq_long_evaluation.txt` (122): “A part that secretly requires a recalled constant is broken →”
- `shadow-bench/src/inceptbench/prompts/mcq_set/evaluation.txt` (5): “rely only on the stimulus plus reference materials a student would have available (a periodic table and standard constants), not on a memorized constant.”
- `shadow-bench/src/inceptbench/prompts/question/scr_evaluation.txt` (112): “- Fails if: (a) the question requires outside knowledge not available from the passage,”
- `grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd` (86-87): “a question/option/hint on page N must not depend on a concrete story noun the child has not read yet”
- `grade3-reading/knowledge_bot/knowledge/kb-0225-g3-closing-questions-adoption-2026-09-24.qmd` (60): “or WITW points at content the child never met.”
- `grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd` (88-89): “explicitly excludes taught vocabulary and invented practice scenarios from false-positiving.”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (123): “- N2: relational-reference factuality. "As you saw last lesson" claims must be true against order.”
- `grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd` (87-89): “explicitly excludes taught vocabulary and invented practice scenarios from false-positiving”
- `grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd` (73-74): “not referenced by `npm run check` or any other known gate at ingestion time”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md` (141-142): “A child who learned L5 **correctly** was marked wrong.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md` (144-145): “every other gate reads one lesson at a time.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md` (152): “> **"Already seen" must be an INTERSECTION over branch points, never a union.**”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md` (163): “The intersection changed the finding from *"39 of 46 clean"* to **6 more real defects**”
- `grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md` (47): “or use a safely-true vague form ("earlier in the course") when the exact neighbour is uncertain.”
- `grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md` (47): “an unverifiable relational claim is a defect, not a flourish.”
- `grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md` (64): “small bugs jar ("remember last time" on the first story; "inspiration tap").”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/TEACHING-ASSESSMENT-CONTRACT.md inside it) (88-89): “Assessment never introduces the knowledge required to pass itself. A cold source may be new, but the historical knowledge and reasoning operation it demands must have been taught and practiced.”
- `g9/transcript/chat-transcript.redacted.txt` (5162): “You come across this question before you have been informed about where acts 2-5 are set”
- `grade3-reading/course-renderer/docs/feedback/g3-internal-review-2026-08-12.md` (18-20): “for someone who hasn't been through the lesson yet, these statements as feedback sounds a little confusing since they refer to knowledge that will be taught in next sections.”
- `g9/script/v03/CHANGES.md` (17): “the list of the dead names two characters now introduced in Lesson 1; "the fall ends in death" keeps the genre fact”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (173): “Before Unit 6 the language device slot is empty, because no device terminology has been banked yet.”
- `g9/library/text/L5d411f.txt` (6): “Without it, check 1 part 2 ("who holds power there?") was inferable but never stated.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (240-241): “was last swept via an audit of 46 strings that found 6 further real defects (e.g. the Raven name leak)”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (244-247): “a plain content-fix pass found and corrected forward-referencing MCQ options and feedback text (Aladdin/Peter Pan quick-check items) where an option or its feedback assumed something the child had not yet seen by that page”

Against: The lint has no baseline across units, so a unit's first lesson must assume nothing, and the spec says nothing about what a unit may assume on entry. What counts as standard course content was judged by a model, not checked against the course framework. The same contract loosens the rule for short-answer items, which may draw on the target fact plus reasonable outside knowledge (`APinceptbench/docs/GENERATOR_API_SPEC.md`), and the essay rubric gives a point for specific evidence beyond the documents (`APinceptbench/ap_benchmark/prompts/official_ap_prompts.py`). Read together, the bound is what the course taught, not a single fact or a single set of documents. It holds where the assessment supplies reference materials or a passage; where recall is the skill being tested, a recalled fact is the point. The check deliberately leaves out taught vocabulary and invented practice scenarios, which would otherwise be flagged falsely (`grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd`).

<sub>criterion · alignment, sequence · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Call a partial task a component

Label a task that rehearses part of an exam format as a component, and give the format's own name only to items that meet its full current specification. One course could not host a full document-based question in its first unit, because the official range begins in 1754.

An audit of an AP history course found that a three-document set for its first period could be mistaken for an exam-aligned document-based question, although the official range for that format begins in 1754. The course's design notes hold that calling such an exercise by the full format's name would make it look more advanced while weakening the measurement contract, and its assessment system records question family, instructional role, format fidelity and evidence state separately, so an item can be excellent guided practice without being an exam simulation. Its contract counts a partial or out-of-range document task as a component, never as a full item, and its verifier rejects copies in which components are mislabelled as full items.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (124-125): “Calling a three-document Period 1 exercise a DBQ would make the artifact look more advanced while weakening the measurement contract.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (123-124): “Unit 1 cannot host a full official-range DBQ, because the current DBQ range begins in 1754.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (530-531): “The assessment system separates question family, instructional role, format fidelity, and evidence state. A question can be excellent guided practice without being a full exam simulation.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/DELIVERABLE-CONTRACT.md inside it) (131-132): “This preserves the instructional progression while making the reviewer-facing count honest: full exam-family items and partial teaching exercises never share a label.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/DELIVERABLE-CONTRACT.md inside it) (113): “A partial or out-of-range document task; never counted as a full DBQ.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CASE-FOR-PLAN-REVIEW.md inside it) (28): “A Unit 1 document set could also be mistaken for an exam-aligned DBQ even though the official DBQ range begins in 1754.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/DELIVERABLE-CONTRACT.md inside it) (206): “components mislabeled as full items”

Against: A limit, not a counter: some exam properties cannot be reproduced inside one unit at all: "A real exam distributes the three required SAQs across different historical periods, which a Unit 1 checkpoint cannot reproduce." (grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz:apush/docs/UNIT1-VERTICAL-SLICE.md, line 46).

<sub>criterion · format, integrity · universal · from ap · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Check the detail the idea turns on

Aim each check at what the page is for: the detail the lesson's idea or theme turns on, never an incidental detail nothing depends on. A spot-check of four lessons found two checks about incidental details.

In one lesson, the reading check on the part holding the line the theme of betrayal turns on asked about a gold coin instead, so that detail went unchecked until the modelling moment; the check was then reworded to it (`grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd`). A spot-check of four other lessons asked whether each part-check was about the thematic hinge, not an incidental detail: most landed on the same hinge as their part's purpose line, and two checks in one lesson were incidental rather than thematic (the same file). What the page is for also covers the causes and effects the lesson builds on later and the goals it states.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd` (58-59): “are our part-checks about the thematic hinge, not an incidental detail?”
- `grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd` (52-53): “the p10 reading check instead asks about the gold coin, so the betrayal-theme detail is not checked until the modelling moment”
- `grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd` (60): “Two L4 checks are incidental rather than thematic”
- `grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd` (64-66): “on whether the 20.09 reading-checks-stay-retrieval ruling (checks stay literal) extends to requiring the literal check be about the hinge specifically. Not applied without that ruling.”
- `grade3-reading/artifacts/criteria-register.csv` (113): “Quick-checks mix cause-and-effect pickup with pointers at the key details the lesson focuses on later; no low-leverage detail questions”
- `grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt` (9): “They need to be a mix of ensuring students can pick up the cause and effect in the text”
- `grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd` (49): “"can this check about his mother never mentioning the brother as it's a key/crucial bit for the theme of betrayal"”
- `grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd` (60-62): “Two L4 checks are incidental rather than thematic: p10 "Who jumped first?" (purpose: what the children must believe before they can fly) and p12 "What happened to the lights of London?" (purpose: how Peter makes Neverland sound).”
- `grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd` (64-66): “whether the 20.09 reading-checks-stay-retrieval ruling (checks stay literal) extends to requiring the literal check be about the hinge specifically.”
- `shadow-content-eval/reports/G3-U1-L2-review.md` (88): “- **p8:** the reading goal *"Notice what the jewels buy"* is never tested.”
- `shadow-content-eval/reports/G3-U1-L2-review.md` (85): “- **p14 `check`:** the densest page (test, servants, marriage) is only tested on its first sentence, but its reading goal is *"what Aladdin uses the genie's power to reach for."*”
- `shadow-content-eval/SKILL.md` (372-374): “Does each comprehension question ask about what the text is *for* (the turn, the character's reason, the idea the lesson teaches), or about a detail nothing depends on?”
- `othello-archive/src/content/checks.ts` (1-2): “aim each at "the key / crucial bit”

Against: Whether a literal reading check must also be about the hinge was still awaiting a ruling, so the two incidental checks were not changed (`grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd`). On the audited lesson one sequence check was left in place, since no harm was shown (`grade3-reading/artifacts/criteria-register.csv`, line 113). Fixing the project's own two checks was held pending a ruling on whether checks that stay literal must also be about the hinge (`grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd`, lines 64-66).

<sub>criterion · alignment, stem · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Choose the format the target needs

Fit each item's format to its target and learners: production wherever the target is to produce, and the formats of the test the course prepares for that suit their grade. An incumbent course's top measured failure was that 100% of its items were single-select multiple choice.

The course plans' generator notes record an incumbent course's top measured failure as 100% single-select multiple choice against the test's 6 formats, and say their own generator output spans all six (`grade3-reading/ti-courseplans/docs/generator-insights.md`). An evaluator gap analysis treats recognition-versus-production match as binding: write, explain and draw targets cannot be assessed by multiple choice alone (`grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd`). The instruction-quality standard gates formats by development: two-part evidence items are about grade 4 and up and do not ship at grade 3 (`grade3-reading/ti-courseplans/docs/instruction-quality-standard.md`). Leave out formats above the learners' level, and have them produce an answer where the target is to produce one.

Quoted:

- `grade3-reading/ti-courseplans/docs/generator-insights.md` (102): “The incumbent's #1 measured failure was 100% single-select MCQ vs MAP's 6 formats.”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (122): “"Write/explain/draw" targets cannot be assessed by MCQ alone.”
- `grade3-reading/ti-courseplans/docs/instruction-quality-standard.md` (77-78): “**EBSR / two-part evidence items are ~grade-4+**; do not ship them at G3.”
- `grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt` (56): “the added two-part (Part A / Part B) evidence items are likely developmentally inappropriate for grade 3 — that type generally appears on state tests around grade 4 and above.”
- `grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md` (135): “Current: ruled off-construct (~grade-4+), 56 items declared”
- `grade3-reading/artifacts/edullm-agent-entrypoint-g3-practical-test-2026-08-06/REPORT.qmd` (36): “- 48/48 lessons include banned G3 EBSR items.”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (124): “N3: recognition-vs-production match. "Write/explain/draw" targets cannot be assessed by MCQ alone.”
- `grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` (86-87): “match the task family to the knowledge: recognition is not enough for productive, representational, justificatory, or integrative constructs;”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (51-52): “Vocabulary requires **production**, not recognition — say it back, use it in a sentence, type it; multiple-choice alone is not enough”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (38-39): “judge a lesson by *production* (say/write/type) over *selection* (click)”
- `grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd` (86): “For diagnostic assessment, the much-maligned MCQ is not a compromise — it is the optimal format.”
- `icloud-work/evaluator/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md` (134): “51% avg, no improvement over 7 runs”
- `icloud-work/evaluator/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md` (135): “38% avg, dropped to 21% in Run 4”
- `icloud-work/evaluator/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md` (390): “1:1 format eliminates analytical challenge”
- `icloud-work/evaluator/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md` (391): “No distractors = simple elimination”
- `icloud-work/ap-social-studies-generator/docs/archive/RUN6_ANALYSIS.md` (87): “90% of fill-in questions fail cognitive demand.”
- `icloud-work/k_12_social_studies/docs/archive/OPENCLAW_HUMAN_REVIEW.md` (72): “Well-designed matching with complex descriptions that require understanding, not just memorization”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (72): “~80% of students check a word as "known," ~50% can give an example, ~20% can explain it”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (124): “"Write/explain/draw" targets cannot be assessed by MCQ alone.”
- `grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd` (29): “Practice must require recall, not just recognition.”
- `grade3-reading/knowledge_bot/knowledge/kb-0074-g3-reviewer-feedback-distilled-for-g5-2026-06-30.qmd` (49): “FRQ-stays-out”
- `icloud-work/evaluator/docs/reports/BENCHMARK_FAILURE_REPORT.md` (132): “- Learning objectives require "explain how and why" but questions only test "what"”
- `icloud-work/evaluator/docs/reports/BENCHMARK_RUN6_REPORT.md` (99): “| **Cognitive Demand** | **35** (90% of fill-in!) |”
- `icloud-work/evaluator/docs/GENERATOR_API_SPEC.md` (128): “- Use the action verbs in the objective to guide question construction (e.g., "Explain" → requires explanation, "Compare" → requires comparison)”
- `APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md` (108): “| "Explain causes of the Columbian Exchange and its effects" | Fill-in-blank for term "Atlantic World" | Tests vocabulary, not causation |”
- `APinceptbench/docs/reports/BENCHMARK_RUN3_REPORT.md` (78): “- Tests recall regardless of difficulty setting”
- `APinceptbench/docs/reports/BENCHMARK_RUN6_REPORT.md` (105): “**90% of fill-in questions fail cognitive demand.** The format is fundamentally incompatible with AP-level analytical requirements.”
- `APinceptbench/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md` (107): “| fill-in | 66% | 50% | **21%** | 25% | 23% | 45% | **38%** |”
- `APinceptbench/ap_benchmark/core/curriculum.py` (335): “"fill-in": "Fill-in-the-blank testing key vocabulary/concepts",”
- `APinceptbench/ap_benchmark/core/curriculum.py` (351): “lines.append("  - Questions should test historical thinking, not just factual recall")”
- `APinceptbench/ap_benchmark/prompts/base.py` (15): “PROMPT_VERSION = "2026.02.24.1"  # Relaxed cognitive demand - recall is OK”
- `APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md` (121): “| **Fill-in** | 21 | 11 | 65.6% |”
- `APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md` (122): “| **MCQ** | 14 | 9 | 60.9% |”
- `grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` (86-87): “- match the task family to the knowledge: recognition is not enough for productive, representational, justificatory, or integrative constructs;”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (143): “MCQ recognition alone — however many options — never counts as a cash”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (135-136): “never cashed in L6/L7 — merciless/triumphant were acquired but no graded surface required using them”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (61): “Word knowledge is a continuum: \~80% of students check a word as "known," \~50% can give an example, \~20% can explain it”
- `grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd` (21): “2. **Enforce mastery gates at ≥90% accuracy.** Do not advance students based on time, completion, or self-report.”
- `ti-courseplans-audit/docs/instruction-quality-standard.md` (132): “Production targets get production formats.”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md` (49): “If the target is production, the format requires production (MCQ ≠ constructed response)”
- `ti-courseplans-audit/skills/course-red-team/references/opportunities-to-respond-brainlift.md` (30): “If a child never has to compose or explain an answer, the app cannot tell whether the child understood”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx` (125 (textutil text)): “The free-response format specifically exposes conceptual misconceptions because students must explain their reasoning, not just calculate.”
- `downloads/WF - Brainlift Opportunities to - 260724-110911.md` (30): “If a child never has to compose or explain an answer, the app cannot tell whether the child understood”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (285): “Vocabulary is only owned when it is produced about new content”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (285): “makes it word *plus evidence*, so a bare echo of the definition does not pass.”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (19): “Recognition can be guessed; production shows the word or idea is owned”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (353): “whether they own them durably is a different question the course answers with spaced returns, not with a medal”
- `downloads/WF - Brainlift Opportunities to - 260724-110911.md` (23): “Neither type is better than the other; each belongs to a different job.”
- `shadow-bench/src/inceptbench/prompts/question/ap_chemistry_evaluation.txt` (32-33): “a discrete MCQ whose task is purely to *produce* a graph or representation is mis-aligned to its section.”
- `shadow-bench/docs/internals/ap-evaluation.md` (144-145): “Science Practice 3 (Representing Data) is free-response-only, so a pure "produce a representation" MCQ is mis-aligned to its section.”
- `shadow-curriculum/schemas/_shared/supported-formats.schema.json` (7): “Optional. Declares which (format, difficulty) combinations this leaf supports for downstream assessment/benchmark generation. Keys must be one of the supported format identifiers: 'fill-in', 'mcq', 'msq'.”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (628-630): “- **mcq:** Use for recognition or discrimination when every option represents a plausible misconception or error and the stem alone states the intended decision. - **msq:** Use only when the construct requires an exact set and the scoring contract makes omission and over-selection visible. - **hot_text:** Use for passage-span selection when selecting evidence is part of the construct; do not substitute it for explaining the evidence.”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (633-635): “- **sequence:** Use when ordered relations are the construct and every element is required exactly once. - **ebsr:** Use when the second response supplies evidence for the first and both parts are scored as one declared claim-evidence contract. - **scr:** Use for production, justification, or integration with a human-calibrated rubric; uncalibrated prose scoring cannot advance a learner.”
- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (209): “No EBSR / two-part evidence items at G3 (state blueprints introduce them ~G4+).”
- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (210): “EBSR/two-part evidence items are banned at G3 but enter blueprints ~G4+ — at G5 they are in scope, so the G3-derived format must not exclude them.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (113-114): “NO EBSR at G3 (grade-4+ format).”
- `grade3-reading/artifacts/qc-2026-09-30-staging/contradictions.md` (17): “2026-06-29: "well built", a strength. 2026-07-08: "likely developmentally inappropriate for grade 3 — that type generally appears on state tests around grade 4 and above".”
- `grade3-reading/artifacts/qc-2026-09-30-staging/contradictions.md` (17): “This course is Grade 4.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/07-SCORING-FEEDBACK-XP.md` (203-204): “the second note's own reasoning allows them for grade 4+, and this course is grade 4”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/07-SCORING-FEEDBACK-XP.md` (205-206): “Left pending; ebsr is a supported bank type in the meantime.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md` (28): “Calculation/multi-step defaults to short constructed-response unless distractors are diagnostic”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (2037): “Default to short constructed-response for calculation-heavy items unless the distractors map to specific procedural errors you want to detect.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (2099): “When the same problem is presented as an MCQ, each option invites a separate mental simulation — "could 24 be right? what about 36?" — creating competing representations that load working memory simultaneously.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (2099): “The MCQ format adds cognitive demand rather than reducing it.”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/generation-contract.md inside it) (112-113): “Where the target knowledge is representational or justificatory rather than a single fact, prefer a short constructed response over an MCQ.”
- `grade3-reading/artifacts/g5-course-candidate-v0/ASSEMBLY_REPORT_V2.md` (119-120): “Standard NWEA MAP G5 Reading uses MCQ throughout. Our MAP-equiv uses hot-text / match / sequence / EBSR / vocab-MCQ.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (267): “"Answer in your own words" is production rather than selection.”
- `othello-archive/BRIEF.md` (39): “Production, not selection, wherever the student is asked to think: they say or type. Selection is fine for quick factual checks.”
- `g9/library/text/L36b8ba.txt` (267): “"Answer in your own words" is production rather than selection.** Worth naming as a standard.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_CASE_FOR_APPROVAL.md` (95): “The incumbent measurement layer is 100% single-select MCQ — all 1,077 incumbent course items and the 33-item STAAR test (Direct-pull).”

Against: An audit of an assessment's approval case found the claim that all six formats were confirmed for the test's reading levels overstated its source, which confirmed three (`grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md`), and notes from the same review, on two dates, called two-part items "well built" and then "likely developmentally inappropriate for grade 3", a ruling still pending (`grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/07-SCORING-FEEDBACK-XP.md`). A grade 5 design required every format of its target test to be practised from the start, two-part items included (`grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md`, line 290); that follows the same test-led rule at a grade where the type belongs. The project's diagnostic-assessment BrainLift argues that for diagnosis multiple choice is the optimal format, fast and isolating one piece of knowledge; that fits matching the response to the target, not a general preference for producing over choosing. a model's review of 6 matching items found them well designed, with descriptions that required understanding rather than memorization. the research is cited without a link, and a settled call in the same project keeps free-response items out of the course. The judge's rubric was later relaxed to accept recall, so the measured failure rate depends on the rubric version: '- Recall and memorization questions ARE ACCEPTABLE' (`icloud-work/evaluator/ap_benchmark/prompts/base.py`, line 88). Fill-in also passed 65.6% in one run (`icloud-work/evaluator/docs/reports/BENCHMARK_RUN2_REPORT.md`, line 121). Every verdict came from one model judge whose own context described fill-in as testing key vocabulary while requiring questions to test historical thinking, not just factual recall, so part of the failure was built into the rubric. The cognitive-demand rule was later relaxed to accept recall, and in an earlier run fill-in passed 65.6%, above multiple choice at 60.9%. This is a secondary citation with no DOI or URL in the source, and nothing here re-measured it. Production shows understanding at the moment, not that it lasts: the same lesson's walkthrough says "whether they own them durably is a different question the course answers with spaced returns, not with a medal". The early-reading synthesis also holds that "Neither type is better than the other; each belongs to a different job.", and the physics note is an uncited assertion about one exam's format. Stated for one exam's section design. The curriculum's per-standard format declaration is optional and lists only selected-response and fill-in formats: 'Keys must be one of the supported format identifiers: 'fill-in', 'mcq', 'msq'.' (`shadow-curriculum/schemas/_shared/supported-formats.schema.json`, line 7). A later run found counter-evidence (`grade3-reading/artifacts/g5-course-candidate-v0/ASSEMBLY_REPORT_V2.md`).

<sub>criterion · format, demand, alignment · universal · from ap, g3, research · measured · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Choose the number of options on purpose

Choose how many options a question offers on purpose: avoid two-option items, cap how many a young reader must weigh, and never add a filler option to reach a count. One item offered an eight-year-old twelve selectable options.

A review of the Grade 3 course asked for at least four options on multiple-choice questions, because a two-option yes-or-no item permits a 50/50 guess (`grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd`). An earlier review found a hot-text item with twelve selectable options, too heavy a motor and cognitive load for an eight-year-old, and asked for the number to be capped (`grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd`). The project's routing note says an agent must not settle the question of three or four options by adding filler (`grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd`), and later course feedback agrees that the four-option request is not a license for a weak fourth distractor (`grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd`). Two-option and yes/no items let a guess get them right half the time. Offer only as many options as can be made plausible.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (112): “MCQs need at least four options. A two-option yes/no item permits a 50/50 guess.”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (128): “one hot-text item offered twelve selectable options, an excessive motor and cognitive load for an eight-year-old.”
- `grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` (104-105): “An agent must not resolve this by adding filler”
- `grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd` (51): “not a license to create a fourth weak distractor.”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (130): “cap the number of selectable options.”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (69): “clearly favours three options: most items cannot sustain more than two plausible distractors, and non-functioning distractors waste time without improving measurement.”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (69): “if you cannot write a third plausible distractor for a given item, use three options rather than adding filler.”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (69): “A weak fourth distractor is worse than no fourth distractor because it provides testwiseness cues and wastes time.”
- `grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd` (80-81): “to prevent guessing" — a two-option item is a 50/50 guess)”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (112): “A two-option yes/no item permits a 50/50 guess.”
- `grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` (102-103): “the MCQ BrainLift reports a research consensus favoring three”
- `grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd` (132-133): “flagged 137/772 items over a 5-option cognitive-load cap (mostly hot-text)”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (140): “accessibility option-count caps;”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (1206): “Do not put a large field of selectable targets in front of an eight- or nine-year-old.”
- `grade3-reading/course-renderer/docs/rules/accessibility.md` (56-57): “"one hot-text item offered twelve selectable options, an excessive motor and cognitive load for an eight-year-old."”
- `grade3-reading/course-renderer/docs/extras/alpharead-lesson-design-aladdin-part-1.md` (254): “The whole passage is split into tappable segments: 3 correct and 11 distractors.”
- `incept-package-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “Avoids filler distractors while preserving misconception-grounded choice sets.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (371-372): “replace the filler distractors with plausible, passage-grounded wrong answers that key a real misreading”

Published: [Rodriguez 2005](https://doi.org/10.1111/j.1745-3992.2005.00006.x)

Against: the multiple-choice BrainLift the project follows reports a research consensus favouring three options and recommends four only when every distractor stays plausible and diagnostically useful, so the default count is still open (`grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd`, lines 102-104). The reading course standardised on exactly four options to prevent guessing (`grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd`), and its v2 review asked for at least four (`grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd`), which leaves filler or a broken rule wherever a fourth plausible option can't be written. The sources split on the default: one rule fixes exactly four options and a review asks for at least four, while the multiple-choice BrainLift favours three and leaves the default to an explicit decision. The cap of five is a chosen limit; the scan counted items over it rather than measuring an effect on students. A later run found counter-evidence (`grade3-reading/course-renderer/docs/extras/alpharead-lesson-design-aladdin-part-1.md`).

<sub>criterion · options, distractors, accessibility · universal · from g3, research · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Collect widely, write about the best

Have learners collect more evidence than they will use and write about only the strongest of it. In one Grade 3 design the learner finds three quotations and writes about the best two.

A Grade 9 unit carries in a decision from an earlier unit: students collect a range of evidence but write about only the best of it, with no fixed number of quotes. A review of the unit's prototype found a counter in independent practice that conflicts with the decision if all three quotes it counts must be analysed, and left that open. A Grade 3 lesson design makes choosing the best evidence its own step once three clues are collected.

Quoted:

- `g9/sources/Othello_1_Feedback_DevFactory.md` (388): “Students collect a range of evidence but write about only the best of it. No fixed number of quotes.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (334): “Three mandated break-downs is a fixed number. If the three are collection this is fine; if all three must be analyzed, it contradicts the decision.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (248): “The child has found three quotations and picks the two worth writing about.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (251): “Any FIND or INFER lesson, once three clues are collected.”
- `g9/library/text/L36b8ba.txt` (388): “Students collect a range of evidence but write about only the best of it. No fixed number of quotes.”
- `g9/library/text/L36b8ba.txt` (382): “These were settled on the Aladdin passes and apply to Othello too.”
- `g9/library/text/L36b8ba.txt` (375): “Collection, or three mandated analyses? Three mandated conflicts with the 20 September decision.”
- `g9/library/text/L8d5159.txt` (248): “The child has found three quotations and picks the two worth writing about.”

Against: The two designs differ on fixing the numbers: the Grade 3 design fixes three found and two picked, with an "n of 3 found" tracker (`g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx`, lines 71 and 248), while the Grade 9 decision sets no fixed number. Whether the Grade 9 prototype's "1 of 3" counter means collection or three required analyses is open (`g9/sources/Othello_1_Feedback_DevFactory.md`, line 126).

<sub>criterion · demand, format · universal · from g3, g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Declare each item's cueing intent

State in each item's specification the cueing it intends (none, support, diagnostic or authentic), and treat any cue it doesn't declare as a defect.

An assessment BrainLift holds that cueing is a design lever to name or eliminate: unnamed cueing leaks validity, deliberate cueing speeds diagnosis, and declaring the intent up front aligns an item's claims, scoring and feedback and prevents accidental narrowing of what it measures. It notes that difficulty and discrimination tend to shift after cue edits, and asks for a cueing-intent field in every specification and a cue sweep in review. A Grade 3 reading red-team standard adopts the rule as an item-construction criterion checked in human review: every item declares its cue intent, and residual cues are defects.

Quoted:

- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md` (45): “Every item declares cue intent (authentic/diagnostic/support/none); residual cues are defects”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1476): “Unnamed cueing leaks validity; deliberate cueing speeds diagnosis.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1477): “Declaring cue intent up front aligns item claims, scoring, and feedback—and prevents accidental construct narrowing.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1478): “Difficulty and discrimination tend to shift after cue edits.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1480): “Add Cueing Intent (authentic/diagnostic/support/none) to every spec;”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1481): “Run a Cue Sweep in review”

Against: none found

<sub>criterion · integrity, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Delivery questions need choice and context

Ask how a line should be spoken only where it allows clearly different deliveries and the lines around it show what the speaker wants, which decides the key. On the first live proof the judge, given the surrounding lines, picked the written delivery on both texts with a confidence of 0.98 or above.

The lesson engine's delivery block asks the writer for a line that could be delivered in clearly different ways, where the lines around it show which delivery fits, and for three deliveries of which exactly one fits what the speaker wants at that moment (`g9/transformer/src/mechanics/direct-the-line.js`). A judge reading the same surrounding lines must pick the same delivery, and an advisory check asks whether the line really allows different deliveries. On the first live proof both checks held on both of its texts, the second at p 0.92 and 0.94 (`g9/transformer/v01/proof-2026-10-09.json`).

Quoted:

- `g9/transformer/src/mechanics/direct-the-line.js` (24): “delivery fits best. Offer three deliveries; exactly one fits what the speaker wants at this moment.”
- `g9/transformer/src/mechanics/direct-the-line.js` (2): “The judge, reading the same lines around it, must pick the same delivery.”
- `g9/transformer/src/mechanics/direct-the-line.js` (60): “label: "The line genuinely allows different deliveries", required: false”
- `g9/transformer/v01/proof-2026-10-09.json` (197-200): “"id": "one-delivery", "required": true, "verdict": "holds", "p": 1”
- `g9/transformer/v01/proof-2026-10-09.json` (203-206): “"id": "line-has-choices", "required": false, "verdict": "holds", "p": 0.92”
- `g9/transformer/v01/proof-2026-10-09.json` (469-472): “"id": "one-delivery", "required": true, "verdict": "holds", "p": 0.98”
- `g9/transformer/v01/proof-2026-10-09.json` (475-478): “"id": "line-has-choices", "required": false, "verdict": "holds", "p": 0.94”
- `g9/transformer/src/mechanics/direct-the-line.js` (55): “Math.abs(x.n - u.n) <= 3”
- `g9/transformer/src/mechanics/direct-the-line.js` (67): “x.n < u.n && x.n >= u.n - 3”

Against: The check that the line allows different deliveries only advises and holds nothing back; the fitting delivery sat second of three in all 4 saved blocks; and the judge reads up to three lines either side of the line while the student's card shows only the three before it (`g9/transformer/src/mechanics/direct-the-line.js`, `g9-transformer-runs/blocks/`).

<sub>criterion · format, stimulus, key · domain · from g9 · adopted-rule · held · found in [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Demand is what the student does

A task's thinking demand is the operation a learner must perform to answer it, not its stem's verb, the skill it claims, its difficulty label or expected pass rate.

Items whose evaluate, explain or justify stems reduced to matching text, and items that described a skill instead of exercising it, were passing an item evaluator. Its base rubric now says such verbs describe the cover, not the demand (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt`); its reading-and-writing rubric requires items to exercise the targeted skill, not describe it (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt`); and a regression test fails vocabulary-in-context items that pair an everyday word with a direct synonym, since they test synonym recognition (`icloud-work/inceptbench-main/tests/test_evaluator_prompt_rules_969.py`). An item's level should be tagged by the work it requires, and even an easy item needs some thinking.

Quoted:

- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt` (114): “Verbs like *evaluate / claim / analyze / explain / justify* in the question stem do **not** rescue the item — they describe the cover, not the actual cognitive demand.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt` (80-81): “Items must exercise the targeted SAT R&W substandard, not describe the substandard in the abstract.”
- `icloud-work/inceptbench-main/tests/test_evaluator_prompt_rules_969.py` (5-7): “Items that use a foundational everyday word and a direct synonym answer test synonym recognition rather than determining meaning in context, and should fail `curriculum_alignment`.”
- `icloud-work/aptraining/apllm-history/runtime_assets/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt` (88): “they describe the cover, not the actual cognitive demand.”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-004-saq-no-stimulus.md` (27-29): “hits the analytical sweet spot on the rubric's wording without any actual increase in cognitive demand.”
- `icloud-work/aptraining/apllm-history/runtime_assets/ib_satisfaction_kit_v1/raw_rubrics/mcq_evaluation.txt` (333): “do not start from the labeled level and try to justify it”
- `icloud-work/aptraining/Cheater/reports/EXPLOIT_CATALOG.md` (14): “label downgrade | 4/4 vs 1/4 control (+75pp)”
- `icloud-work/ap-social-studies-generator/docs/archive/STATISTICAL_ANALYSIS.md` (180): “Add cognitive_demand pre-check for easy questions”
- `icloud-work/ap-social-studies-generator/docs/archive/STATISTICAL_ANALYSIS.md` (181): “Easy ≠ "recall only"”
- `icloud-work/aptraining/Cheater/reports/FINAL_REPORT.md` (65): “EXPLOIT-007 difficulty=easy label | pilot-only; doesn't generalize when stacked”
- `icloud-work/aptraining/apllm-history/runtime_assets/ib_satisfaction_kit_v1/raw_rubrics/mcq_evaluation.txt` (523): “explicitly describes recall, identity facts, or base fact recognition as the expected cognitive level”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (73): “When tagging items by cognitive level, describe the cognitive process required, not the expected pass rate.”
- `grade3-reading/knowledge_bot/knowledge/kb-0161-assessment-item-difficulty-core.qmd` (96): “your "difficulty alignment" check will confirm the misclassification because it's using the same flawed definitions.”

Against: the label effect was pilot-only and didn't generalize when stacked with other tricks, and the same rubric accepts recall where the curriculum's own definition of a level describes recall.

<sub>criterion · demand, alignment · universal · from ap, g3, research · adopted-rule · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Difficulty spreads in lessons, not exam sets

Across a lesson, the questions on one source should range from easier to harder without strict ordering, while an exam-style set on one source keeps them at one level. One rubric expects uniform difficulty across a set of 3-5 questions sharing a single stimulus, as standardized tests do.

The evaluator's lesson rubric, for one passage with a mixed set of questions, passes a lesson whose questions run from recall to inference and synthesis and fails one where all cluster at one level, without requiring strict easy-to-hard order (`shadow/bench/src/inceptbench/prompts/lesson_bundle/evaluation.txt` lines 95-97). Its rubric for a small set of questions sharing one stimulus expects uniform difficulty instead, unlike a quiz, to match standardized test formats (`mcq_set/evaluation.txt` line 3), and the AP chemistry overlay says the same of stimulus-based sets (`question/ap_chemistry_evaluation.txt` lines 55-57). Both are adopted rules; neither has been measured on learners.

Quoted:

- `shadow-bench/src/inceptbench/prompts/lesson_bundle/evaluation.txt` (96): “Pass: questions span a range from easier (recall/retrieval) to harder (inference/synthesis), appropriate for the grade level. Perfect E→M→H ordering is NOT required.”
- `shadow-bench/src/inceptbench/prompts/mcq_set/evaluation.txt` (3): “Unlike quizzes which require Easy/Medium/Hard distribution, MCQ sets are expected to have UNIFORM difficulty - all questions should be at the same appropriate difficulty level.”
- `shadow-bench/src/inceptbench/prompts/question/ap_chemistry_evaluation.txt` (56-57): “uniform (not escalating) difficulty across the set is expected.”

Against: none found

<sub>criterion · demand, sequence · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Distractors from the words taught

In a word-meaning check, make every wrong option a word the lesson taught, because an untaught word can be ruled out by unfamiliarity alone and so tests nothing.

The reading course's content-failure log adds this to its vocabulary gate: a meaning-check distractor must be a word the lesson teaches, since a distractor naming an untaught word can only be eliminated by unfamiliarity (`grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md`, lines 73-74). It is one rule from one log, with no count of how many checks broke it.

Quoted:

- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md` (73): “Also: a meaning-check distractor must be a word **this lesson teaches**.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md` (73-74): “A distractor naming an untaught word can only be eliminated by unfamiliarity, so it tests nothing.”
- `grade3-reading/engine/reports/PETER-PAN-IMPROVEMENTS-2026-09-28.md` (10-11): “Fix: distractors in the same form (enchanting → boring, puzzling, soothing; menacing → comforting, welcoming, charming).”

Against: A later run found counter-evidence (`grade3-reading/engine/reports/PETER-PAN-IMPROVEMENTS-2026-09-28.md`).

<sub>criterion · distractors, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Don't define the word being tested

A question on a taught word must make the learner use the idea, never define the word in the question or key an answer that just repeats its definition.

A review of one reading test's items, run separately from an AI quality benchmark, found a vocabulary template that defined the affix in the stem and rewrote it so the item depends on the passage. A checker written for the reading project fails a vocabulary item whose right option just echoes the taught definition, though it was one of four checkers not yet wired into the build. The same holds for a question on a taught definition, and defining the word's parts, such as an affix, in the question counts as defining it.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd` (49): “pre-defined the affix in the stem”
- `grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd` (93-94): “DEFINITION-ECHO (a vocab-testing item's correct option must not just echo the taught definition).”
- `icloud-work/evaluatorML/.agent/memory/plans/2026-05-25-ap-history-request-expectation-mapping.md` (35): “- Definitional standards must be transformed into assessment tasks, not copied into stems.”
- `icloud-work/evaluatorML/.agent/memory/plans/2026-05-25-ap-history-request-expectation-mapping.md` (156): “### F3: APWH definitional rows become copied stems.”
- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-ap-history-ib-expectation-matrix.md` (213): “- Definitional text rather than task verb: identify the concept as the content target; require generator to transform it into a reasoning task rather than copy the definition.”
- `icloud-work/evaluatorML/.agent/memory/request_expectations/ap_history_request_expectations_summary.md` (3): “- Rows written: 53790”
- `icloud-work/evaluatorML/.agent/memory/request_expectations/ap_history_request_expectations_summary.md` (8): “- By reasoning mode: {'definition_to_assessment': 510, 'causation': 25695, 'statement_to_assessment': 4515, 'comparison': 5880, 'evidence_source_analysis': 105, 'contextualization': 465, 'continuity_change_over_time': 13320, 'explanation_general': 2910, 'evaluation_argument': 390}”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/vocabulary-use-routine-and-volume.md` (17): “So when we write the sentence frames, the word is always in the sentence frame and it's always open-ended. That's why you see a lot of our sentence frames ending with because”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/vocabulary-use-routine-and-volume.md` (19): “So that's an example of a closed frame because there's really just one answer to it. You're just asking for a definition.”
- `grade3-reading/artifacts/arc-audit/L7.md` (32): “Delivered Form 2 (`vocab-form2`) is a definition-recall MCQ ("You win a great victory after a hard struggle. Which word says that?").”

Against: A later run found counter-evidence (`grade3-reading/artifacts/arc-audit/L7.md`).

<sub>criterion · stem, key, integrity · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Don't spend a later step's evidence early

No step may use up what a later one teaches or tests. One lesson's follow-up keys repeated the guide's line just before them at 1.00 overlap, and measured 0 after the rewrite.

A comparison of one course's branched follow-up checks measured how much each key repeated the guide's line just before it: one lesson echoed its answer at 1.00 overlap and another at 0.80, against 0.50 in a third, and both measured 0 after the rewrite; before it, the right answer had been the sentence the guide just said, word for word (`grade3-reading/artifacts/compare-2026-09-23/index.html`). An external audit of four lessons found a vocabulary check whose key reused the teaching card's own example, an early check whose key was the exact line the next page's worked model then 'finds', and a search step whose right answer named two of the three lines the next step asks for (`grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md`). A curriculum audit found an early check that spent the worked model's clue before the model used it (`grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md`), and a gap list found a goal line that supplied the inference before the model asked for it (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/PP-STANDING.md`). It is the step-to-step form of nothing-gives-the-answer-first. A key that repeats the line just heard, or the example that taught it, tests only echo, and an earlier line that names a later step's evidence or inference leaves that step nothing to do.

Quoted:

- `grade3-reading/artifacts/compare-2026-09-23/index.html` (68): “Measured across every branched cfu, ours were the outliers: L4 echoed its answer at”
- `grade3-reading/artifacts/compare-2026-09-23/index.html` (77): “The right answer is the sentence Scout just said, word for word.”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (63): “and it reuses the p2 card's own key concept (bared teeth)”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (94): “p13's key ('John grabbed a wooden sword and stood in front of his little brother.') is the exact line p14's I-do model later 'finds'”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (127): “The Search step's correct answer names two of the three Step-3 evidence lines directly”
- `grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md` (112): “pre-spends the MM clue "without a mother"”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/PP-STANDING.md` (36): “L5 goal pre-supplies the inference”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (78): “You-do step 1 never answers the lesson's question. Its MCQ asks what to hunt FOR, not the question itself; an option set that resolves the question is a leak.”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (79): “checked by validate-blind-solve + validate-question-claims (partial)”
- `grade3-reading/course-renderer/docs/qa/new-lesson-qa-invariants.md` (45-47): “**A6. You-do step 1 never answers the lesson's question.** Its MCQ asks what to hunt FOR, not the question itself; an option set that resolves the question is a leak.”
- `grade3-reading/course-renderer/docs/qa/new-lesson-qa-invariants.md` (47-49): “partially automated — validate-blind-solve + validate-question-claims; OWED: fail a step-1 option that keyword-overlaps the you-do question's answer.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (334): “A plan is not a model answer, and a model answer at this point would remove the writing.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (334): “The likely reading is that the plan carries what the paragraph has to contain — answer, quote, word, second word, restatement — without supplying the words.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (374): “A plan or a model answer. A model answer at that point would remove the writing.”
- `othello-course-renderer-draft/repo/authoring/inputs/prompt-packs/reading-g3/base.md` (160-161): “Never use the taught word anywhere in the modelling pages. It is cashed by the child in the independent task.”
- `othello-course-renderer-draft/repo/authoring/inputs/rule-packs/reading-g3.json` (186): “The rule: the taught word NEVER appears in the modelling moment (it pre-answers the model) and MUST be cashed in the independent task. Enforced by vocab:taught-word-withheld-from-model.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/final-u9-review.json` (43): “The reading says a long search could suggest doubt, then the independent task asks how Jo could show doubt. It repeats an already supplied interpretation.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/README.md` (125): “Check the entire prior learner-visible transcript, not just the model excerpt.”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md` (381): “L7 p16 independent Search key names two of the three actions Step 3 asks for;”
- `grade3-reading/artifacts/qc-2026-09-29-staging/FINDINGS.md` (48): “**MINOR: the p7 reading goal gives the model's answer away.** It names "the gentle Lost Boys", and the p14 model then concludes "gentle, lonely characters".”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/base.md` (160-161): “Never use the taught word anywhere in the modelling pages. It is cashed by the child in the independent task.”
- `grade3-reading/course-renderer/docs/video/u1-script-critique.md` (244-246): “The item still requires judging what a section spends most of its words on, which is the skill, so this is a watch item rather than a defect.”
- `g9/library/text/L36b8ba.txt` (334): “A plan is not a model answer, and a model answer at this point would remove the writing.”
- `othello-course-renderer-draft/repo/docs/video/u1-script-critique.md` (242): “**The video now hands the child the answer to Lesson 1's own main-idea item.**”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (464): “a retrieval task that activates a prerequisite without previewing the independent answer;”
- `grade3-reading/artifacts/pp4-v4-design.txt` (80): “They stay off the two actions saved for the Modelling Moment and the Independent Task (Wendy freeing herself; Peter driving Hook to the railing), so nothing is pre-answered.”
- `grade3-reading/artifacts/pp3-v3-design.txt` (80): “Both on "but something changes" content (the raid and the capture), not on the bravery or cruelty evidence, which is saved for the FIND Modelling Moment and Independent Task.”
- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L7-2026-09-05.md` (223-225): “None pre-answer the two FIND-target actions (Wendy's rope-freeing, Peter's disarm/slash are deliberately held for p14 and p16 respectively).”
- `grade3-reading/artifacts/u4l2-build/BEAT-SPEC.md` (277-278): “no cross-stop or forward leak (no stop may ask for an I-do/we-do/you-do answer).”

Against: A later run found counter-evidence (`grade3-reading/course-renderer/docs/video/u1-script-critique.md`).

<sub>criterion · integrity, sequence, key · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Don't stop at one copied quote

An evidence or written task must not be passable by copying one sentence from the source. One redesign had students judge six statements, two of which the text contradicts, after finding their evidence.

A value analysis of a redesigned reading lesson named its old ending, one tapped block, one copied quote and one word, as the strategy's known failure: evidence located, concept never built. The redesign had the student judge six statements, two of which the text contradicts, and asked for two different quotes, since one quote proves only that the student can copy (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/L6-VALUE.md`, lines 9-23).

Quoted:

- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/L6-VALUE.md` (10-11): “evidence located, concept never built”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/L6-VALUE.md` (11-12): “The new Refine step makes the child judge six statements, two of which the text contradicts; that is retrieval PLUS falsification”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/L6-VALUE.md` (20-21): “One quote proves the child can copy; two different quotes prove the claim is supported”
- `shadow-bench/src/inceptbench/prompts/question/scr_evaluation.txt` (172-173): “- Score 0.0: A student can earn full credit by copying a single sentence from the passage without demonstrating understanding.”
- `shadow-bench/src/inceptbench/prompts/question/scr_evaluation.txt` (121): “- Fails if the question only requires copying a sentence from the passage (locating, not inferring).”
- `shadow-bench/src/inceptbench/prompts/question/ecr_evaluation.txt` (168): “- Fails if the prompt reduces to a summary task or copying from the source.”
- `shadow-bench/src/inceptbench/prompts/question/hot_text_evaluation.txt` (19-21): “When the stem asks for evidence, the central idea, a theme statement, or an error within the passage, the answer being located in the text is the assessed reading skill”
- `grade3-reading/course-renderer/docs/qa/new-lesson-qa-invariants.md` (169): “**F3. Quote words never satisfy the own-words blank.**”
- `grade3-reading/course-renderer/docs/feedback/g3-parity-audit.md` (29): “deterministic client parrot rule in SpeakGate (>= 0.9 content-word overlap, or >= 6-word verbatim run at >= 0.8): a parroted pass becomes a miss with own-words feedback”
- `grade3-reading/ti-courseplans-wiki/Perfect-Course-Rulebook.md` (308-309): “The rubric accepts semantically defensible variants and rejects evidence-free or copied text”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/CONTENT-SCHEMA.md` (460): “shown when ≥60% of 8-grams overlap the tapped line”
- `othello-archive/scripts/qc-judge-cases.json` (242-244): “"answer": "it means he is not what he is",”

Against: The analysis calls its case "NOT measured learning.", and the additions cost about three to five minutes, with the second quote partly transcription (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/L6-VALUE.md`, lines 4 and 32-35). When locating evidence is itself the skill, finding the answer in the text is intended: 'When the stem asks for evidence, the central idea, a theme statement, or an error within the passage, the answer being located in the text is the assessed reading skill' (`shadow-bench/src/inceptbench/prompts/question/hot_text_evaluation.txt`, lines 19-21).

<sub>criterion · demand, format · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Each evidence option fits one reading

In a two-part item asking for evidence behind the first answer, only the keyed evidence may support the right answer, and each wrong evidence option should fit a wrong reading.

Two-part evidence items came into the evaluator with mandatory copy-task audits of how the evidence part links to the answer part (`shadow-bench/src/inceptbench/prompts/question/ebsr_evaluation.txt`). An item fails when an evidence option is not drawn from the passage or when a wrong evidence option also supports the keyed answer, and each wrong evidence option must align to a wrong reading of the first part, not to the key. When a test-wise student can pick the evidence through a surface cue without doing the first part, the item measures test-wiseness instead of evidence-based reasoning; mixing quotations with paraphrases among the evidence options is failed as an unintended cue.

Quoted:

- `shadow-bench/src/inceptbench/prompts/question/ebsr_evaluation.txt` (62): “- a Part B option has `appears_in_passage: NO` (evidence is fabricated, not drawn from the passage);”
- `shadow-bench/src/inceptbench/prompts/question/ebsr_evaluation.txt` (65-66): “- a NON-keyed Part B option has `supports_part_a_keyed_answer: YES` (a distractor is itself valid supporting evidence, so the Part B key is not the unique/complete set).”
- `shadow-bench/src/inceptbench/prompts/question/ebsr_evaluation.txt` (69): “Each Part B distractor must align to a WRONG Part A reading, not to the key.”
- `shadow-bench/src/inceptbench/prompts/question/ebsr_evaluation.txt` (82-84): “When a test-wise student can pick the evidence without performing the Part A comprehension, the item no longer measures evidence-based reasoning — it measures test-wiseness, defeating the EBSR purpose.”
- `shadow-bench/src/inceptbench/prompts/question/ebsr_evaluation.txt` (97-98): “mixing quotes and paraphrases turns citation style into an unintended cue”
- `shadow-bench/` (commit e435432) (14): “ebsr/match/sequence/saq/scr reported not-probeable (v1 scope).”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md` (212): “- **No vocabulary EBSR or hot-text:** Vocabulary items use short context sentences as stimulus, not full passages. Two-part text-evidence format does not apply.”

Against: The evaluator's text-hidden probe does not cover this item type: 'ebsr/match/sequence/saq/scr reported not-probeable (v1 scope).' (`shadow-bench`, git commit e435432, line 14).

<sub>criterion · options, distractors, integrity, stimulus · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Each part specific, scored on its own

Build each part of an open question so that a vague, generic answer cannot earn credit and the part can be scored on its own.

The short-answer rubric gives full marks when the parts require specific evidence, examples or reasoning, so that generic answers would not earn points (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/saq_evaluation.txt`). It also asks for the expected number of parts, each with a clear task verb, connected to one another but independently scorable (the same file). It governs how the question is built, not how its marking guide is written.

Quoted:

- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/saq_evaluation.txt` (41): “- Score 1.0: Parts require specific evidence, examples, or reasoning; generic answers would not earn points”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/saq_evaluation.txt` (36): “- Score 1.0: Has the expected number of parts (check metadata/curriculum context for requirements); each part has a clear task verb; parts are logically connected but independently scorable”
- `grade3-reading/ti-courseplans-wiki/Perfect-Course-Rulebook.md` (316): “Exact-match grading; rubric has no reject boundary”

Against: none found

<sub>criterion · stem, demand, scoring-guide · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Each reasoning skill has its element

Teach and credit each reasoning skill by its element: one dimension evidenced on both sides for comparison, a mechanism for cause, a baseline for change, a qualifying move for complexity.

An AP history course's design document has evidence perform a named function: in a causal answer it connects a development to an effect through a mechanism, in a comparison it addresses the same dimension for both cases, and in continuity and change the student names the baseline. It teaches complexity as moves, qualifying a claim by actor, region, timeframe or persistence, corroborating across different evidence, or modifying it for a counter case, and a response must earn the relationship rather than insert a phrase. It sets this against a predictable error: students and generators imitate rubric terms, so a sentence beginning 'Although' is not automatically complex and naming two events is not comparison. The design document has since been marked historical, and no outcome was measured.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (398-402): “The course models a reasoning chain in which evidence performs a named function. In a causal answer, each piece of evidence must connect a development to an effect through a mechanism. In comparison, evidence for both cases must address the same dimension. In continuity and change, the student must name the baseline against which change is judged.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (204): “compare the same dimension across two cases;”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (591-593): “Complexity is not taught as a decorative concession. Students learn to qualify by actor, region, timeframe, or persistence; corroborate across different evidence; or modify a claim when a counter case changes its scope. A response must earn the relationship, not insert a phrase.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (410-412): “Students and generators can imitate rubric terms without performing the historical work. A sentence beginning "Although" is not automatically complex. Mentioning purpose is not sourcing. Naming two events is not comparison.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/PROCEDURE-PROPOSAL.md` (20): “Do not label this CONNECT: pupils must construct two evidence-bearing sides on one dimension before explaining similarity or difference.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/PROCEDURE-PROPOSAL.md` (22): “Read question: determine what comparison and explanation the question requires.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/PROCEDURE-PROPOSAL.md` (23): “Name dimension: hold one meaningful dimension constant, such as response to other people's needs or what draws a character toward others.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/PROCEDURE-PROPOSAL.md` (24): “Build each side: select evidence for both sides on that dimension. Reject a true but irrelevant detail or a comparison that changes dimensions halfway through.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/PROCEDURE-PROPOSAL.md` (25): “Explain comparison: explain the shared pattern and/or meaningful difference; do not merely restate two quotations.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/integration/final-page-census/G5-U1-L7-sg-model.txt` (35): “region "COMPARE: worked example"”
- `othello-course-renderer-draft/repo/docs/pedagogy/grade5-procedure-proposal.md` (20): “pupils must construct two evidence-bearing sides on one dimension before explaining similarity or difference.”
- `othello-course-renderer-draft/repo/docs/pedagogy/grade5-procedure-proposal.md` (24): “3. Build each side: select evidence for both sides on that dimension. Reject a true but irrelevant detail or a comparison that changes dimensions halfway through.”
- `othello-course-renderer-draft/repo/docs/pedagogy/grade5-procedure-proposal.md` (25): “4. Explain comparison: explain the shared pattern and/or meaningful difference; do not merely restate two quotations.”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures-g4-g5.md` (180): “At Grade 4 the dimension is supplied by the question”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures-g4-g5.md` (180-181): “Choosing the dimension for yourself is the later release move.”

Against: The comparison procedures are still proposals: the Grade 4 and 5 document marks its additions as proposed and not yet signed off, open to being rewritten or rejected (`othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures-g4-g5.md`, lines 10-12), and the Grade 5 draft says its additions require explicit sign-off before merge (`grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/PROCEDURE-PROPOSAL.md`, line 5, and its copy `othello-course-renderer-draft/repo/docs/pedagogy/grade5-procedure-proposal.md`, line 5). The history course's design document is marked historical and superseded, and no outcome was measured (`grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz`, member `apush/docs/BRAINLIFT.md`, line 5).

<sub>criterion · demand, scoring-guide · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Each wrong option a named misconception

Build each wrong option from a different, named misconception or predictable error that students really make, so that choosing it shows what was misunderstood. One audit found only about 7% of choice items naming, in their feedback, the misconception a wrong option targets.

An assessment BrainLift used as feedback for the reading courses calls distractor and feedback quality coupled decisions: misconception-based distractors carry the highest risk of the negative suggestion effect, and Butler & Roediger (2008) showed that feedback largely neutralises it (`grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md`, line 1991). The courses' instruction-quality standard makes each distractor the answer a named misconception picks, with feedback that names it (`grade3-reading/ti-courseplans/docs/instruction-quality-standard.md`, lines 129-130), yet an assessment memo found only ~7% of choice items (15 of 48 lessons) naming, in their feedback, the specific misconception a wrong option targets (`grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md`, line 44). An adversarial review's checklist calls strong misconception distractors with no feedback teaching the error, and a fourth option no misconception would pick filler, worse than three options (`grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md`, lines 160 and 166); the BrainLift agrees that a weak fourth distractor is worse than none (line 2006). The predictable errors include a wrong time, place, cause or actor, and each wrong option should sit in the same category and grain as the key. Record which error each option targets and give it feedback that corrects that error, since an uncorrected lure can teach the error, and an option nobody would pick is only filler.

Quoted:

- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1991): “they carry the highest risk of the negative suggestion effect, where exposure to plausible wrong answers implants false knowledge.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1991): “Butler & Roediger (2008) showed that feedback largely neutralises this risk, while the absence of feedback leaves it unchecked.”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0164-g3-v2-feedback-agent-routing.qmd` (95-96): “plausible lures can seed false knowledge;”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (166): “strong misconception distractors + no feedback = teaching the error (negative suggestion effect)”
- `grade3-reading/ti-courseplans/docs/instruction-quality-standard.md` (129-130): “Distractors are misconception-coded (each = the answer a named misconception picks); feedback names the misconception.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md` (44): “only **~7% of choice items (15 of 48 lessons)** name the *specific misconception* a distractor targets in its feedback”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (2006): “A weak fourth distractor is worse than no fourth distractor because it provides testwiseness cues and wastes time.”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (160): “can you name what a student choosing each distractor is thinking? if not, it's filler (worse than 3 options)”
- `icloud-work/ap-social-studies-generator/docs/analysis/failure_analysis.md` (221): “Absolute language: "total," "complete," "all," "immediate," "never"”
- `icloud-work/ap-social-studies-generator/docs/analysis/failure_analysis.md` (224): “Historically absurd: contradicts basic knowledge”
- `icloud-work/ap-social-studies-generator/docs/analysis/failure_analysis.md` (229): “Scope confusion: True for different region/group/time period”
- `icloud-work/ap-social-studies-generator/docs/analysis/failure_analysis.md` (230): “Partial truth: Contains accurate element but wrong overall conclusion”
- `icloud-work/ap-social-studies-generator/docs/analysis/failure_analysis.md` (234): “Would a good student who studied but didn't master the material choose this?”
- `icloud-work/ap-social-studies-generator/docs/analysis/best_practices.md` (23): “Based on academic literature (Haladyna & Rodriguez, 2013; University of Waterloo CTE; BMC Medical Education)”
- `icloud-work/ap-social-studies-generator/docs/analysis/best_practices.md` (33): “Similar length to the correct answer”
- `icloud-work/ap-social-studies-generator/docs/analysis/best_practices.md` (44): “Each should be selected by at least 5% of test-takers”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-002-stimulus-strip.md` (71): “obviously-wrong-on-the-merits to a knowledgeable reader”
- `icloud-work/ap-social-studies-generator/CHANGELOG.md` (132): “Zero pass rate improvement”
- `icloud-work/ap-social-studies-generator/CHANGELOG.md` (123): “Ran data-driven benchmarks (5 samples each) to decide what to optimize”
- `icloud-work/incept/ap-benchmark-standalone/ap_benchmark/prompts/mcq.py` (17): “- Each distractor represents a different type of misconception”
- `icloud-work/incept/inceptbench/docs/MCQ_SET_PASS_SPEC.md` (621): “1. **Plausible**: Each distractor should be a real mistake a student might make”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (258): “- If Curriculum API provided Common Misconceptions → verify distractors align with those specific misconceptions”
- `icloud-work/incept/inceptbench/inceptbench_new/tools/misconception_analysis.py` (72): “issues.append(f"redundant (same error): {', '.join(sorted(redundant_keys))}")”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/_base_evaluation.txt` (724): “- When Curriculum API provides Common Misconceptions → You MUST verify distractors align with those misconceptions”
- `icloud-work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md` (358): “1. Generated 36 questions from the live inference endpoint.”
- `icloud-work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md` (368): “Main failure dimensions (most frequent 0.0):”
- `icloud-work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md` (369): “- `distractor_quality` (16/36)”
- `icloud-work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md` (370): “- `reveals_misconceptions` (12/36)”
- `icloud-work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md` (404): “- Distractors are often not tied to *specific misconceptions* (diagnostic weakness).”
- `icloud-work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md` (490): “- Issue: Because every option is correct, the item cannot differentiate between correct understanding and common errors.”
- `icloud-work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md` (406): “- Issue: One option (“+”) is non-parallel and implausible for a comparison task, reducing distractor quality.”
- `icloud-work/incept/nova_forge/README.md` (303): “| Distractors | 30 | … HARDER (content) | Low |”
- `icloud-work/evaluator/docs/reports/LATEST.md` (79): “| distractor_quality        |   69 |  152 |     31.2% |      0.35 |”
- `icloud-work/evaluator/docs/reports/LATEST.md` (176): “Option A is too easily dismissed as an extreme/absurd distractor.”
- `icloud-work/evaluator/ap_benchmark/prompts/base.py` (97): “- FAIL for obviously absurd distractors”
- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md` (39): “- Distractors must be plausible, homogeneous, grammatically parallel, similar in specificity/length, and tied to real misconceptions.”
- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md` (40): “- Avoid opposite/negation distractors, borderline-correct distractors, and partial-question giveaways.”
- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-ap-history-ib-expectation-matrix.md` (124): “- Write distractors from wrong period, wrong region, wrong cause, wrong actor, or overgeneralized interpretation.”
- `icloud-work/ap-social-studies-generator/docs/analysis/best_practices.md` (28): “- Each distractor should target a specific student misconception or common error”
- `icloud-work/ap-social-studies-generator/docs/analysis/best_practices.md` (45): “- Non-functioning distractors (never selected) indicate poor design”
- `icloud-work/ap-social-studies-generator/docs/analysis/best_practices.md` (69): “**Key Finding**: Distractors generated by predicting student choice behavior significantly outperform those generated by similarity-based methods.”
- `icloud-work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md` (24): “Q1-D (declaring war over the Treaty of Tordesillas) is easily eliminated and does not reflect a realistic student misconception.”
- `icloud-work/ap-social-studies-generator/docs/archive/COMPREHENSIVE-AUDIT-2026-02-18.md` (81): “| Distractor Quality | C | Plausible but not misconception-based |”
- `icloud-work/inceptbench/src/inceptbench/evaluators/base.py` (600): “A high-quality MCQ should have at least one distractor that targets one of these misconceptions, and the correct answer must NOT match any of them.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (505): “- No connection to common misconceptions (especially those provided by Curriculum API)”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (600): “In that narrow case, if every distractor violates the same sub-criterion the question loses diagnostic value → `distractor_quality = 0.0`.”
- `icloud-work/inceptbench-main/tests/test_evaluator_prompt_rules_371_382.py` (25-26): “does not over-fire on single-skill items (avoids golden-suite regression).”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md` (356): “`options[i].misconception` field required on all non-key options.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md` (351): “- **Scope error** — true detail presented at wrong granularity”
- `APinceptbench/docs/GENERATOR_API_SPEC.md` (173): “- Distractors MUST represent plausible student misconceptions, not absurd options”
- `APinceptbench/docs/reports/BENCHMARK_FAILURE_REPORT.md` (222, 227): “Questions that passed tended to: … 5. Use distractors representing real student misconceptions”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md` (350): “Each MCQ has exactly 3 distractors, one of each:”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md` (243): “| Dim 11: Distractor coverage | Four distractor types present (scope, conflation, prior knowledge, partial) | Hard gate |”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (175): “Students produce MC lures as answers on later tests, even when warned not to guess.”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (175): “The effect scales with the plausibility and number of competitive distractors”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (176): “Without feedback, the negative suggestion effect persists.”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (176): “both immediate and delayed feedback were effective”
- `grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` (95-96): “potent misconception-based distractors require product-appropriate corrective feedback or post-test correction because plausible lures can seed false knowledge;”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_evaluation.txt` (287-288): “- Distractors are plausible and likely chosen by students with partial mastery - Distractors align with known common misconceptions (especially those from Curriculum API)”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/common_pre_checklist.md` (36): “- [ ] All options same grain size and same category”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/common_pre_checklist.md` (38): “- [ ] Distractors seeded from `common_misconceptions` where possible”
- `icloud-work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/EXPLOIT-002-stimulus-strip.md` (68-72): “obviously-wrong-on-the-merits to a knowledgeable reader (each distractor names a real historical claim that is anachronistic or factually inverted, not nonsense). This pattern automatically satisfies `distractor_quality` and `reveals_misconceptions` default-pass conditions”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md` (27): “| 6 | **Misconception-tagged distractors** — each wrong option maps to a named cluster: `schema_mis_mapping` / `strategy_substitution` / `inference_overreach` | distractors with no diagnostic intent |”
- `grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd` (105-106): “Action: add a per-option enum validator (fail-and-retry) to our generator;”
- `grade3-reading/knowledge_bot/knowledge/kb-0008-alpha-courses-repo.qmd` (132-133): “Every selected-response item carries **misconception- cluster tags** (A = strategy-substitution / B = schema-mismapping / C = inference-overreach).”
- `grade3-reading/knowledge_bot/knowledge/kb-0008-alpha-courses-repo.qmd` (135-136): “deterministic dose assembler + LLM misconception tagging”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (160): “can you name what a student choosing each distractor is thinking? if not, it's filler (worse than 3 options)”
- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (773): “J16-ASS-001: Use only plausible, diagnostically useful response options; do not add filler to meet a count.”
- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (770): “Claim boundary: No fixed option count belongs in the universal standard.”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md` (20): “If 4 options, all 4 are plausible — drop to 3 rather than add a weak 4th”
- `grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd` (69): “Chunk-stop distractors are self-declared filler, not real near-neighbour traps.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx` (248 (textutil text)): “Assessment items should include distractors based on known misconceptions. A student who can state the correct definition but selects the misconception when presented as a plausible alternative does not truly hold the correct understanding.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx` (248 (textutil text)): “The FCI (Force Concept Inventory) model — forced choice between the correct answer and the most common misconception — is the gold standard.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx` (240 (textutil text)): “The College Board explicitly designs multiple-choice distractors around the "bond breaking releases energy" misconception and the teleological "atoms want full shells" reasoning.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 6. Life in Water - CONNECT - Lesson Design.docx` (10 (textutil text)): “Exactly one deliberate misconception distractor per item.”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (67): “Each distractor is a coded misconception (a happy place, a cheerful place, a cozy-ordinary thing) and its feedback names the mismatch”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 3. Aladdin and the Wonderful Lamp, Part 3 (FICTION, INFER) — v3 (new INFER design).docx` (97 (textutil text)): “4 short plausible options, one stated in the text, no trick distractors.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx` (75 (textutil text)): “four short options all plausible to a drifting child; built to Rule 2.”
- `shadow-bench/src/inceptbench/prompts/question/ap_chemistry_evaluation.txt` (58-61): “- Distractors should each correspond to a **specific, predictable chemistry error** (e.g. an inverted ratio, a dropped stoichiometric coefficient, confusing a quantity with its logarithm, using mass where moles are required, selecting a conjugate instead of the named species) rather than arbitrary wrong values.”
- `shadow-bench/src/inceptbench/prompts/question/science_evaluation.txt` (30-31): “Strong science items are built around **known student misconceptions**”
- `shadow-bench/src/inceptbench/prompts/question/science_evaluation.txt` (32-33): “Distractors or expected wrong answers should map to such predictable errors rather than to arbitrary or obviously-wrong alternatives.”
- `shadow-bench/src/inceptbench/prompts/question/inline_choice_evaluation.txt` (49-50): “Every distractor must represent a genuine misreading of the passage — not a grammatically wrong option, an obviously off-topic word, or one no reader would seriously consider.”
- `shadow-bench/src/inceptbench/prompts/question/sat_math_evaluation.txt` (74-75): “At least one incorrect distractor must require a genuine misapplication of the tested concept to be tempting.”
- `shadow-bench/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (527): “- Distractors are plausible and likely chosen by students with partial mastery”
- `shadow-bench/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (531): “- Has strong diagnostic value”
- `shadow-bench/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (629): “An incorrect-but-content-plausible distractor that a non-expert student could be tempted by is acceptable distractor design, not a failure.”
- `g9/transformer/src/mechanics/quick-check.js` (23): “the other two are tempting to a skimmer but the text”
- `g9/transformer/src/mechanics/quick-check.js` (75): “Would option ${letters[i]} seem believable to a Grade 9 reader who skimmed the text, rather than obviously absurd?”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md` (352): “- **Concept conflation** — right topic, wrong relationship”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md` (353): “- **Prior-knowledge override** — world-plausible but text-unsupported”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md` (354): “- **Partial comprehension** — correct at midpoint, overturned by ending”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/skill/SKILL.md` (49): “each wrong answer must be grounded in the passage, true-sounding, and exploitable only by partial comprehension”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/HUMAN-g3r-2026-07-20T11-20-06-019f7ed3-5205-72f0-a25a-caf13bf2a620.md` (277-280): “The flagship "misconception-mapped MCQ" on the energy lesson (G5-U4L3-I01) maps its distractors to source-block LOCATION ("which fragment is in Source A vs Source C") and its feedback coaches "recheck Source A," not the energy science.”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/HUMAN-g3r-2026-07-20T11-20-06-019f7ed3-5205-72f0-a25a-caf13bf2a620.md` (267-273): “- YELLOW - Your anti-generic distractor gate has a blind spot. 7 of the 52 science MCQs use per-option templated ids like "mc-...-a-unsupported-detail" - a generic label, not a diagnosed misconception. Your own quality scan reports "generic fallbacks absent," but its blocklist is only {wrong-choice, wrong-part, wrong-span} - it never scans for "unsupported-detail," so these 7 pass as if they were specific.”
- `grade3-reading/course-renderer/docs/pedagogy/misconceptions/cross-cutting-synthesis.md` (305): “A student who can state the correct definition but selects the misconception when presented as a plausible alternative does not truly hold the correct understanding.”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/item-types/mcq.md` (11-12): “Exactly one deliberate misconception distractor per item: an option a child who half-followed would genuinely pick.”
- `grade3-reading/ti-courseplans/courses/g4g5-math-checkpoints/brainlifts/v0.1.md` (32): “Distractors built from executed error-patterns diagnose *which* rule is broken”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/ASSESSMENT-QUALITY-MEMO.md inside it) (44): “only **~7% of choice items (15 of 48 lessons)** name the *specific misconception* a distractor targets in its feedback”
- `othello-course-renderer-draft/repo/authoring/inputs/rule-packs/reading-g3.json` (69): “Their Rule 2 asks for exactly one deliberate misconception distractor per item, NAMED in the design doc.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (552-553): “Distractors should represent plausible misconceptions or reasoning errors rather than generic wrongness.”

Published: [Butler & Roediger 2008](https://doi.org/10.3758/MC.36.3.604) · [Haladyna & Rodriguez 2013, Developing and Validating Test Items](https://doi.org/10.4324/9780203850381) · [Generating Plausible Distractors for Multiple-Choice Questions via Student Choice Prediction (2025)](https://doi.org/10.48550/arXiv.2501.13125) · [Roediger & Marsh 2005](https://doi.org/10.1037/0278-7393.31.5.1155) · [Hestenes, Wells & Swackhamer 1992, Force Concept Inventory, The Physics Teacher](https://doi.org/10.1119/1.2343497)

Against: in an exploit study, options parallel in form but obviously wrong to a knowledgeable reader still passed the judge's distractor checks, and a step that rebuilt weak distractors gave no gain in pass rate over 5 samples. The quiz pipeline's plausibility rule: "If the distractor has ANY connection to the passage OR question, it PASSES (score=1)" (`icloud-work/incept/aplit-quiz-generation/lit-question-qc.json`, line 8). Among near misses, the project's own fix list counted 30 distractor problems and rated fixing them harder, needing content work, and low in impact (`icloud-work/incept/nova_forge/README.md`, line 303). One run report proposed the opposite for easy items, in a prompt it recommended for the writer: '- Have obviously wrong distractors (for MCQ)' (`icloud-work/evaluator/docs/reports/BENCHMARK_RUN4_REPORT.md`, line 326). No student responses were ever collected, so the guidance's own test of a working wrong option, chosen by at least 5% of test-takers, was never applied, and plausibility was judged only by models (`icloud-work/ap-social-studies-generator/docs/analysis/best_practices.md`). For a single-skill standard, wrong options that share a failure category are normal good design (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt`, line 600). The misconception list reaches the judge only on the unmerged AP branch; the current AP context has no misconception field (`icloud-work/inceptbench-main/src/inceptbench/evaluators/base.py`, lines 796-817). The spec is inconsistent on the count: it says each item has exactly 3 distractors, one of each, then lists four types, while the item bank's gate asks for four types present. The benchmark's link between such distractors and passing is an observation, not a test. The research's minimum effective feedback is showing the correct answer, while the reading course never reveals a single-select item's answer after a set number of tries, because a short option list lets the child eliminate their way to it (`grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd`); whether eliminating to the right option corrects a lure as well as being shown it has not been measured here. A planned test of misconception-seeded options, to be replicated on 150 items if distractor quality rose 3 points, has no recorded result in the files read (icloud-work/aptraining/helpers/data/output/path_e/path_e_build_notes.md, line 42). In that strand the tags were assigned by a model ("deterministic dose assembler + LLM misconception tagging", `grade3-reading/knowledge_bot/knowledge/kb-0008-alpha-courses-repo.qmd`, lines 135-136), and an enum validator checks that each option carries a tag from the list, not that the tag is right. The grade 3 profile also requires at least 4 options on every multiple-choice item and no true/false item in the mastery pool, since a yes/no is a 50/50 guess, while the same criteria drop to 3 options rather than add a weak fourth, so where no fourth real error exists the two rules conflict (`ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md`). Quick are-you-still-reading checks are treated differently: one story design keeps them free of trick distractors, while the science designs build theirs to the same rule, misconception distractor included. The general bar is softer: an incorrect but content-plausible option that could tempt a non-expert student is acceptable, not a failure, and the SAT math rule asks for only one such option. A later run found counter-evidence (`grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/item-types/mcq.md`). A later run found counter-evidence (`othello-course-renderer-draft/repo/authoring/inputs/rule-packs/reading-g3.json`).

<sub>criterion · distractors, feedback · universal · from ap, g3, research · external-research · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Enough data for the conclusion asked for

A question asking for a conclusion from data or an experiment must give enough data to reach it, vary only the factor tested and never present correlation as cause.

The evaluator's science rules require an item built on an experiment, procedure or data set to support the inference it asks for: a controlled comparison varies the intended variable while holding the others fixed, the data provided must be sufficient to reach the asked-for conclusion, and correlation is not presented as established causation without support. A reading-the-data or interpret-the-graph task must give enough information for the intended answer to be determinate. These are adopted rules for the judge, with no measurement behind them.

Quoted:

- `shadow-bench/src/inceptbench/prompts/question/science_evaluation.txt` (21-25): “- When an item involves an experiment, procedure, or data set, the design must support the inference it asks for: a controlled comparison varies the intended variable while holding others fixed; the data provided must actually be sufficient to reach the asked-for conclusion; correlation must not be presented as established causation without support.”
- `shadow-bench/src/inceptbench/prompts/question/science_evaluation.txt` (26-27): “- A reading-the-data or interpret-the-graph task must give enough information for the intended answer to be determinate.”

Against: none found

<sub>criterion · stimulus, demand, integrity · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Every part of an item agrees

An item's parts must agree: the stem asks for what the options offer, the key names an option that exists, and the explanation and feedback support that key. An answer letter that disagreed with its explanation made 7 of 30 questions fail a cross-check by another model.

In a 295-item run, 34 items failed the judge's factual-accuracy check while the pipeline's maths check reported 'math_errors_found: 0' (`icloud-work/incept/nova_forge/PASS_RATE_ANALYSIS.md`). The project's judged failures include a key contradicted by its own explanation (`icloud-work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md`), a stem that asks for a model while only numeric answers are offered, and a key labelled 'A' on an item with no choices (`icloud-work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md`). The explanation and feedback are written once the option order is fixed and tied to the options' wording rather than their letters, and they say why the common wrong choices are wrong. The agreement is checked in code.

Quoted:

- `icloud-work/incept/nova_forge/PASS_RATE_ANALYSIS.md` (117): “- 34 questions failed factual_accuracy”
- `icloud-work/incept/nova_forge/PASS_RATE_ANALYSIS.md` (118): “- GVC shows "math_errors_found: 0" but InceptBench still finds issues”
- `icloud-work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md` (138): “- Generated: Answer "A" but explanation proves "B" is correct”
- `icloud-work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md` (78): “- **Issue:** The stem asks for a model, but only numeric answers are provided and no model is shown, creating conflicting cues about what action is required.”
- `icloud-work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md` (208): “- **Issue:** Field mismatch: the answer is labeled “A” but no choices are presented; the item appears to be fill-in.”
- `icloud-work/ap-social-studies-generator/docs/archive/TECHNICAL-DECISIONS.md` (106): “Fixed answer bias (all answers were "B") by shuffling options after generation.”
- `icloud-work/ap-social-studies-generator/docs/archive/MCQ_BUG_HISTORY.md` (49): “Still shuffling after generation, which is fundamentally fragile”
- `icloud-work/ap-social-studies-generator/docs/archive/MCQ_BUG_HISTORY.md` (6): “This bug caused 7 out of 30 questions (23%) to fail in Claude cross-evaluation”
- `icloud-work/k_12_social_studies/docs/URGENT-BUG-STILL-PRESENT.md` (28): “Result: 7 out of 10 questions (70%) have the bug.”
- `icloud-work/ap-social-studies-generator/docs/archive/CLAUDE_CROSS_EVAL_REPORT.md` (30): “Gemini Score: 0.96 | Claude Score: 0.75”
- `icloud-work/ap-social-studies-generator/docs/archive/CLAUDE_CROSS_EVAL_REPORT.md` (35): “Answer is listed as "A" but explanation says "correct answer is B"”
- `icloud-work/ap-social-studies-generator/docs/archive/CLAUDE_CROSS_EVAL_REPORT.md` (164): “Gemini passed Q36 and Q44 despite this critical flaw.”
- `icloud-work/ap-social-studies-generator/docs/archive/HOLISTIC_REVIEW_2026-02-19.md` (121): “Place correct answer at position {pos}.”
- `icloud-work/ap-social-studies-generator/docs/archive/HOLISTIC_REVIEW_2026-02-19.md` (127): “{answer} is correct. Explain why {answer} is right and others are wrong.”
- `icloud-work/ap-social-studies-generator/docs/archive/HOLISTIC_REVIEW_2026-02-19.md` (130): “100% first-attempt pass rate (up from 72%)”
- `icloud-work/ap-social-studies-generator/docs/archive/MCQ_BUG_HISTORY.md` (65): “IT DID NOT CHECK IF A WRONG ANSWER WAS MARKED AS CORRECT”
- `icloud-work/ap-social-studies-generator/docs/archive/MCQ_BUG_HISTORY.md` (66): “Default return was `True` when no indicators found (should be `False`)”
- `icloud-work/incept/inceptbench/docs/MCQ_SET_PASS_SPEC.md` (552): “| 4 | Explanation references wrong option | factual_accuracy (Critical) | Option reordering after explanation written | Generate explanations LAST |”
- `icloud-work/incept/inceptbench/docs/MCQ_SET_PASS_SPEC.md` (457): “"explanation": "The Declaration's assertion of equality fueled debates about expanding democratic participation and who deserved the rights it proclaimed."”
- `icloud-work/incept/inceptbench/docs/MCQ_SET_PASS_SPEC.md` (591): “5. REORDER OPTIONS so the correct content lands in the assigned position.”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (87): “- **FIELD MISMATCH**: Explanations, hints, feedback templates, or `additional_details` describe distractors, answers, or values that do NOT match the actual options or correct answer”
- `icloud-work/incept/aplit-quiz-generation/main.py` (1829): “do not use 'Choice A', 'Choice B', etc; quote the beginning and the end of the option.”
- `icloud-work/incept/workflow/reports/REPORT_20260223_144619.md` (104): “Every question must include an explanation of why the correct answer is correct and why common wrong choices are incorrect.”
- `icloud-work/incept/workflow/reports/REPORT_20260223_144619.md` (57): “| `missing_explanation` | 18 | Question lacks required explanation for correct answer |”
- `icloud-work/incept/ML_TRAINING_INSIGHTS_REPORT.md` (211): “3. **Answer key consistency** -- explanation must match the marked answer”
- `icloud-work/incept/README.md` (98): “- **Missing explanation**: No or minimal explanation provided”
- `icloud-work/incept/README.md` (93): “Questions are automatically rejected (score=0.0) without API call if:”
- `g9/transformer/src/mechanics/cer-frame.js` (50): “the explained word is not in the quotation”
- `g9/transformer/src/mechanics/cer-frame.js` (51): “the reasoning never mentions the word it explains”
- `g9/transformer/src/mechanics/worked-model.js` (83): “The rebuild, set right, makes its sentence”
- `g9/transformer/src/transform.js` (68): “if (codeFail.length) { reasons = codeFail.map((c) =>”
- `g9/transformer/test/mechanics.test.mjs` (118): “find((c) => c.id === "rebuild-makes-sentence").ok, false”
- `grade3-reading/artifacts/arc-audit/PRE-WEEKEND-SMOKE-2026-08-28.md` (42-44): “every blank's `answer` is a member of the top-level `bank`; every blank's `feedback` dict covers exactly `bank - {answer}` (checked per-blank, not just presence).”
- `grade3-reading/artifacts/arc-audit/L7.md` (79-81): “All `hot_text` nodes have correctly-`null` feedback on their own correct indices (no accidental "wrong" message on a correct tap).”
- `grade3-reading/artifacts/Peter-Pan-L4-review-response-2026-08-25.pdf` (p.4 (pdftotext lines 205-206)): “Our error was that the hunt asked for London while cueing lines that did not contain it.”
- `grade3-reading/.claude/skills/pre-weekend-audit/SKILL.md` (40-41): “Child-path integrity: every answer key internally consistent (index ranges, permutations, bank membership, feedback coverage).”

Against: In an earlier 257-item run the maths check and the judge agreed, with '- **Result:** ✅ All math is already correct!' and '- Math accuracy: 100% ✅' (`icloud-work/incept/nova_forge/archive/old_docs/gvc/GVC_FINAL_ARCHITECTURE.md`, lines 60 and 65); that run's failures were put down to format. the generator's first code check for the mismatch looked only at whether the key was called right or wrong, never at a wrong option called correct, and passed by default when it found neither. When code has proved the key right, the committed evaluator counts a mismatched explanation as a clarity fault, not a wrong fact: "This is a `clarity_precision` failure, NOT a `factual_accuracy` failure." (`icloud-work/incept/inceptbench/src/inceptbench/prompts/question/closed_ended_evaluation.txt`, line 99). It fits the record on feedback that sends the student back only once a student's attempts are over, since that record says feedback on a wrong answer never says what the student has to produce.

<sub>criterion · key, options, stem · universal · from ap · measured · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Every question needs a way to answer

Never ask a question or invite a response, on screen or aloud, without a way for the learner to give it, including a lesson's closing question.

Internal reviews of a grade 3 reading course found a lesson ending on a question with no way to take input, which looked incomplete, and a guide line asking the child to tell a story when nothing was listening. The rule now gives every question on screen an input, and every authored lesson closes on a receipt that states what the child did and asks nothing (`grade3-reading/course-renderer/docs/rules/ui.md`, lines 210-225). The general case, a question anywhere with no input beside it, is not yet checked.

Quoted:

- `grade3-reading/course-renderer/docs/rules/ui.md` (212-213): “Every question on screen has an input. A closing prompt with no way to respond is not a closing.”
- `grade3-reading/course-renderer/docs/extras/g3-internal-review-2026-08-05.md` (44): “it also says “Now tell a story about a time when you did something clever.” but we are not listening so should probably remove it, happened in issue 6 as well”
- `grade3-reading/course-renderer/docs/rules/ui.md` (224-225): “What is not checked is the general case, a question node anywhere with no input beside it.”
- `othello-course-renderer-draft/repo/docs/rules/ui.md` (212-213): “**Rule.** Every question on screen has an input. A closing prompt with no way to respond is not a closing.”
- `othello-course-renderer-draft/repo/docs/rules/ui.md` (215-216): “Course ending with a question which has no way to take input looks incomplete.”
- `othello-course-renderer-draft/repo/docs/rules/ui.md` (222-224): “every authored lesson closes on a `receipt`, which states what the child did, the words they learned and what they now understand, and asks nothing.”
- `othello-course-renderer-draft/repo/docs/rules/ui.md` (224-225): “What is not checked is the general case, a question node anywhere with no input beside it.”

Against: none found

<sub>criterion · format, stem · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Every source given must be needed

When the skill is combining sources or formats, every source given must be needed to reach the answer.

Integration items carried pictures their own explanations never used, and synthesis items came down to matching a single note. The ELA rubric now fails alignment for any stimulus that isn't load-bearing and requires integration to demand combining at least two formats (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/ela_evaluation.txt`); a deterministic check fails an integration item whose explanation never refers to its image (`icloud-work/inceptbench-main/src/inceptbench/evaluators/question.py`); and the reading and writing rubric fails the alignment of a synthesis item that keyword matching against one note can answer (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt`). It carries the rule that a question must need its text over to items with several sources.

Quoted:

- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/ela_evaluation.txt` (19): “- ANY row with `load_bearing=NO` → `curriculum_alignment = 0.0`.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/ela_evaluation.txt` (20): “Integration must demand combining at least two formats to reach the answer.”
- `icloud-work/inceptbench-main/src/inceptbench/evaluators/question.py` (904-907): “if the item carries an image_url but the answer_explanation never references any visual element, the image is decorative and the item fails the integration demand.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt` (100-102): “If the aim is so narrow that only one note is relevant and the student can identify the correct answer by simple keyword matching, the item reduces synthesis to a matching exercise.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (281-282): “the stem itself states the direction (urchin→otter), so a student can answer correctly from the stem's own wording without ever consulting the diagram or applying the rule.”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (357-358): “the rule now lives only in the passage/key text, never on the map.”

Against: none found

<sub>criterion · stimulus, demand · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Every wrong statement names its error

In a select-all item, every wrong statement must contain an error that can be named, because a statement that is merely less good is not false.

One generator's failure analysis quotes the judge failing a select-all option that was not clearly false, only a mischaracterization. Its fix tells the writer that wrong answers in a select-all item must be false statements, not misleading but plausible ones: for each, the writer completes a sentence naming the specific error, and one it can't complete is too ambiguous. Select-all items passed 40% in that benchmark, their key issue being that they had been written as single-answer items.

Quoted:

- `icloud-work/ap-social-studies-generator/docs/analysis/failure_analysis.md` (18): “MSQ | 40% | CRITICAL: Wrong format (4 options, 1 answer instead of 5/2-3)”
- `icloud-work/ap-social-studies-generator/docs/analysis/failure_analysis.md` (106): “Option B is NOT clearly factually incorrect - it's more of a mischaracterization/distractor”
- `icloud-work/ap-social-studies-generator/docs/analysis/failure_analysis.md` (243): “In MSQ, wrong answers must be STATEMENTS THAT ARE FALSE, not "misleading but plausible."”
- `icloud-work/ap-social-studies-generator/docs/analysis/failure_analysis.md` (255): “If you cannot complete that sentence, the statement is too ambiguous.”
- `icloud-work/ap-social-studies-generator/docs/archive/CLAUDE_MANUAL_REVIEW.md` (21): “MSQ | 62.5% (5/8) | 100% (8/8) | Gemini too strict”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/item-types/msq.md` (5-7): “The two untrue statements are FALSIFIABLE directly from the text — a child can point at the sentence that proves them wrong. Never merely unlikely, never outside the passage.”
- `grade3-reading/artifacts/pp4-v4-design.txt` (326): “Refine sets are 6 statements each, 4 true + 2 incorrect, all falsifiable from the text.”

Against: in an earlier batch, a model's review of 8 such items passed all 8 where the writer's own model, judging, passed 5, and called that judge too strict.

<sub>criterion · distractors, options, key · universal · from ap · adopted-rule · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Evidence across two sentences is one pick

When the evidence for an answer spans two sentences, make them one selectable unit, so the learner isn't asked to choose between two right answers.

A review of a tap-the-evidence item in a grade 3 reading course found the correct answer split into two sentences, which left the reader unsure which to pick when both were right. The course now highlights such evidence as one selectable unit, beside a rule that evidence may be more than one sentence, or two ideas from different places that the child synthesises (`grade3-reading/course-renderer/docs/rules/questions-and-assessment.md`, lines 81-92).

Quoted:

- `grade3-reading/course-renderer/docs/rules/ui.md` (165-166): “If the correct evidence spans two sentences, present them as one selectable thing.”
- `grade3-reading/course-renderer/docs/rules/questions-and-assessment.md` (90-92): “where the correct answer spans two sentences, highlight them as one so the child is not asked to choose between two right answers”
- `grade3-reading/course-renderer/docs/rules/questions-and-assessment.md` (81-82): “**Rule.** Allow and expect evidence that is more than one sentence, or two ideas from different places that the child synthesises.”

Against: none found

<sub>criterion · options, key · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Evidence that doesn't give itself away

In a two-part evidence item, hinge the first part on a detail only the passage gives, and keep the keyed evidence from announcing itself or containing that part's answer. Across eleven redesign families, 2 of 13 two-part items passed a text-hidden solve on both parts, both built on an arbitrary passage detail and de-signalled evidence.

A grade-5 conversion round took 13 two-part evidence items that had all leaked and rebuilt their option text and prompts across eleven design families, keeping only items whose two parts both failed blind and both succeeded with the passage under a cross-family solver. Only 2 of 13 were certified, both hinging the first part on an arbitrary passage detail with a flat one-in-four prior, rewriting the keyed quote so it no longer announced itself as the evidence, and using real, topically parallel passage sentences as the wrong quotes. The other 11 leaked on the evidence part, because when the right evidence sentence contains the first part's answer a blind solver reads it off the option list, which the report calls a property of the format under a strong solver. A grade-4 probe found the same pattern, with evidence options restating the first part's answer.

Quoted:

- `grade3-reading/ti-courseplans/courses/g5-reading/analysis/rt5-ebsr-2026-07-06/README.md` (3): “**Headline: EBSR moves from 0-certified to 2-certified. 2 / 13 certified.**”
- `grade3-reading/ti-courseplans/courses/g5-reading/analysis/rt5-ebsr-2026-07-06/README.md` (5-6): “baseline: 0/13 clean; the g5-blind-solve finding put EBSR leak at ~94% on encyclopedic passages”
- `grade3-reading/ti-courseplans/courses/g5-reading/analysis/rt5-ebsr-2026-07-06/README.md` (37-38): “Keeper = **both parts blind-fail on all votes AND both parts with-passage succeed**.”
- `grade3-reading/ti-courseplans/courses/g5-reading/analysis/rt5-ebsr-2026-07-06/README.md` (43): “11 design families explored”
- `grade3-reading/ti-courseplans/courses/g5-reading/analysis/rt5-ebsr-2026-07-06/README.md` (21-22): “the correct evidence is a real passage sentence that *self-identifies* as the best-stated evidence, so a blind lexical solver back-solves it directly.”
- `grade3-reading/ti-courseplans/courses/g5-reading/analysis/rt5-ebsr-2026-07-06/README.md` (47-48): “**Arbitrary passage-specific fact + de-signaled evidence.** Part A hinges on a concrete detail with a flat 1-of-4 prior a blind solver cannot know”
- `grade3-reading/ti-courseplans/courses/g5-reading/analysis/rt5-ebsr-2026-07-06/README.md` (50-51): “rewritten so it does **not** announce itself as "the evidence," and the three distractor quotes are each real, topically-parallel passage sentences.”
- `grade3-reading/ti-courseplans/courses/g5-reading/analysis/rt5-ebsr-2026-07-06/README.md` (55-56): “when the correct evidence sentence contains the Part A answer, a blind solver reads it off the option list.”
- `grade3-reading/ti-courseplans/courses/g5-reading/analysis/rt5-ebsr-2026-07-06/README.md` (79-80): “This is a real property of the two-part select-the-evidence format under a strong cross-family solver, not a tooling gap.”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/RED_TEAM_FINDINGS.md` (33): “**Part B restates Part A** — G3's measured root cause, verbatim present”

Against: Every rebuild kept the keys and changed only option text and prompts (`grade3-reading/ti-courseplans/courses/g5-reading/analysis/rt5-ebsr-2026-07-06/README.md`, lines 26-29), so the ceiling was measured under that constraint. A grade-4 plan carries an earlier grade-5 figure of about 0% cross-family leak for two-part items (`grade3-reading/ti-courseplans/courses/g4-reading/approval-package/topic-selection.md`, lines 252-253), so measured leak rates for the format differ between gates.

<sub>criterion · integrity, format, options · universal · from g3 · measured · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Find the evidence first, then explain

For an answer that needs evidence, have the learner first find and mark the evidence in the text, then explain it in their own words in a separate slot.

Reviews of a Grade 3 reading course flagged its evidence-writing task as backwards in two consecutive rounds, on 2026-07-20 and 2026-07-24: finding and copying the sentence and then rewording it in one box teaches plagiarism (`grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md`, item 9; `grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md`). The fix asked for was to highlight or underline the sentence in the text first and then write in the learner's own words, or to split the task into two parts. Keep the source in view while the learner does this, and let the evidence come from more than one place if need be. The quote then holds only the text's words, and the inference has to be produced, not copied.

Quoted:

- `grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md` (215): “**The writing task teaches plagiarism**: find-and-copy-the-sentence then own-words in one box.”
- `grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md` (215): “Highlight/underline in the text first, then write in own words; or split into two parts.”
- `grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md` (54-55): “Reverse to **find-and-highlight the sentence FIRST, then write it in your own words**;”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (86): “Prompts ask for textual evidence, but the passage is hidden when the student needs to cite it.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (87): “No model of a strong response is shown.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (116): “The current order is backwards. Students should first find and highlight the sentence, then write it in their own words: find it, then write about it. The I-do should model the evidence-finding step.”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (81): “"say it with evidence" had write-then-find; correct is find+highlight FIRST, then write in own words”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (80): “often it's 2 ideas synthesized from different places”
- `ti-courseplans-audit/skills/course-red-team/SKILL.md` (179-181): “copy-then-paraphrase writing prompts that teach plagiarism (fix: highlight the sentence IN the text, then write in own words — or split into two explicit parts)”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md` (48): “Evidence tasks: find-and-highlight the sentence first, then write in own words; the I-do models the finding”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (350 (textutil text)): “Inference words (safe, desperate, ambitious, determined) live only in the "I know…" / "So I think…" steps, never in "The text says…".”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (261): “the text’s words go inside quotation marks, and the mood word can never hide there — the inference has to be produced, not retrieved.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx` (189 (textutil text)): “Any inference sits in State/Refine/Extra thinking, never inside a "the text says" quote.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/FEEDBACK-RESPONSES.md` (169-170): “**First, point at the proof.** The child taps the line in the passage that shows the answer, and is told whether that line does the job.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (522-524): “stops at locating the mistake sentence; canonical I03 asks for the cross-sentence event→repair inference (locate the mistake AND state how it was fixed and why).”

Against: none found

<sub>criterion · format, demand, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Find the part, then the line

In an evidence task, have students find the part of the text where the evidence lives before they hunt for the exact line.

In the independent task of a built Grade 3 lesson, the second step asks where in the story the clues live, and only then is the matching paragraph found in the text (`downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md`, line 239). The walkthrough's reason is that locating the evidence neighbourhood first keeps the hunt a comprehension act rather than a scan-everything act (line 241); the step came from a review suggestion. It rests on one source, and no outcome was measured.

Quoted:

- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (241): “locating the evidence neighborhood before hunting in it keeps the hunt a comprehension act rather than a scan-everything act.”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/CODEX-HISTORY-EVERYTHING-OUT.md` (67-69): “**Locate Routine v2** (remember evidence as CONTENT never position; zoom to 60–120 words; PAUSE narration until the child re-reads; keyword scan only after re-read);”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (207): “Mirrors how released items scope: "Based on lines 1 through 11 of the poem..."”
- `grade3-reading/.claude/skills/one-perfect-lesson/SKILL.md` (49-50): “Locate Routine v2 (evidence as content never position, 60–120-word zoom, pause narration until re-read)”

Against: none found

<sub>criterion · demand, format · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Formats the player can deliver

Use a question format only once the student's own player has been seen to render it, and keep a fallback format for the rest. Three item types uploaded without an error and then showed students an empty quiz.

Live probes of the reading project's delivery platform found that matching, hot-text and text-entry items uploaded cleanly (201, valid QTI, GET 200) but showed an empty quiz to students and had to be turned into single-choice items (`grade3-reading/knowledge_bot/knowledge/kb-0009-timeback-alpha-read-packager.qmd`). A production reading course there held 1,077 items, 100% single-choice, with no interactive item ever rendered, while the project's Grade 5 contract required all six formats, so it could fully certify a form that could not be delivered; the action was a delivery gate asking for a live render in the student's view of every non-choice format, with a choice-only fallback form (`grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd`). A publishing plugin distilled from AP science builds exists to stop items that return 200 OK but render broken or empty in the student's view (`grade3-reading/knowledge_bot/knowledge/kb-0020-incept-timeback-plugin.qmd`).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0009-timeback-alpha-read-packager.qmd` (116-117): “**R3 — `match`, `hot-text`, `text-entry` render BLANK.** They push fine (201, valid QTI, GET 200) but the quiz body is empty — must be transformed to single-select choice.”
- `grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd` (68-71): “a live probe found the PRODUCTION TimeBack G3 Reading course is **1,077 items, 100% `cardinality=single`, zero TE ever rendered**. Our G5 contract hard-requires all six formats + 40% TEI → we can fully certify a form that **physically cannot be delivered**.”
- `grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd` (71-72): “Action: add a deliverability gate — every non-MCQ format needs a live student-UI render artifact; absent that, mark TEI `humanApproved:false-for-delivery` and define an MCQ-only fallback form.”
- `grade3-reading/knowledge_bot/knowledge/kb-0020-incept-timeback-plugin.qmd` (21): “items that return `200 OK` but render broken/empty in the student UI, silent data loss on updates, etc.”
- `grade3-reading/knowledge_bot/knowledge/kb-0022-incept-team-sync-2026-06-17.qmd` (33): “All-MCQ/MSQ is a fallback only.”
- `g9/transformer/src/glue/animated.js` (2): “Blocks map to its native nodes where one exists; the rest are listed, not forced.”
- `g9/transformer/src/glue/threejs-render.js` (18): “The rest are listed, not forced.”
- `g9/transformer/src/glue/animated.js` (15): “a key-term page used as a choice card (the line as the term, the lines before it under it), until”
- `g9/transformer/v02/QA.md` (80): “a reading page of its own (the two answers as its text, the pick as its quick check);”
- `g9/transformer/v02/QA.md` (40-41): “The evidence hunt and the comparison were listed, not forced, as they have no screen of their own yet.”
- `g9/transformer/v02/QA.md` (122): “compare, film, say it back and debate have no screen there yet and play in our view under the frame.”
- `g9/transformer/README.md` (22-23): “A block a build cannot draw plays in the lesson view under it.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (2588): “Native ce19052a G3-U1-L5/p16 asks for two clues in story, but Book HotText routes to standalone single-best buttons and rejects authored Captain Hook was watching.”
- `grade3-reading/incept-read-app/docs/G4-SCR-grading.md` (130): “So the adapter has **never received a real input** — it is effectively dead code.”
- `grade3-reading/_archive/2026-08-13-consolidation/redteam-g3-round3-report-and-evidence.tar.gz` (RED_TEAM_ROUND3.md inside it) (163-164): “- MSQ uses the MCQ handler; every click clears prior selection (line 158), so a two-key answer cannot be submitted or graded all-or-nothing.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/CONTENT-SCHEMA.md` (283): “as a workaround after a child hit `Unsupported question type: inline_choice` at question 4 of 10”

Against: The project chose not to cut its courses down to single choice for the platform's sake: all-choice is a fallback only, and a separate delivery app was planned for the richer formats (`grade3-reading/knowledge_bot/knowledge/kb-0022-incept-team-sync-2026-06-17.qmd`).

<sub>criterion · format, review · universal · from g3, ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Frames end in because or so that

A frame for using a taught word includes the word and ends in 'because' or 'so that', never a blank for the word or its definition.

A grade-3 reading rulebook's vocabulary routine says open frames end in because or so that, and a reading quality canon applied in a grade-5 audit requires a sentence frame to contain the target word and stay open-ended, banning the closed anti-patterns 'admire means ___' and fill-the-blank-with-the-word. The same canon asks vocabulary checks to reach the generative level, such as completing an idea that ends in because, rather than associational matching. An open ending means the learner's answer has to give a reason, not just the word.

Quoted:

- `grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md` (178-180): “Open frames end in BECAUSE / SO THAT; contrast near-neighbours; never assess a word the turn you taught it; a glossary pop-up is never instruction; prefer generative words; never target a word the passage explains in place.”
- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (354): “A sentence frame contains the target word and is open-ended (ends in 'because…/so that…'); ban the closed anti-patterns ('*admire* means ___' and fill-the-blank-with-the-word).”
- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (348): “Vocabulary checks reach the generative level (idea-completion '…forbidden to play with matches because ___'; 'would you want a frail person on your team? why?'), not associational matching; classify items by cognitive demand.”

Against: A different exercise keeps the closed form on purpose: the record practise-taught-words-by-typed-recall cues each taught word by its meaning in a one-blank sentence for typed recall, which practises recalling the word rather than using it.

<sub>criterion · format, demand, hints · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Guides describe reasoning, not fact lists

A marking guide describes the reasoning that earns credit in a few checks, not facts or keywords, which can be wrong or matched by an answer lacking the reasoning. In one set of short-answer items, wrong facts caused 14 of 18 failures, and a postmortem traced them to the examples the writer put in the guide.

The AP generator's system message tells it that short-answer scoring guidance describes criteria, not evidence lists (`icloud-work/aptraining/.agent/research/inference_clean.md`). In the failure analysis, factual accuracy caused 14 of 18 failures in one course's short-answer items, and a postmortem traced them to the guide itself: the writer filled its sample-response and acceptable-evidence fields with plausible but wrong historical examples (`icloud-work/aptraining/.agent/research/failure_taxonomy.md`). Every fact a guide lists, especially one its writer recalls rather than verifies, is another chance to be wrong.

Quoted:

- `icloud-work/aptraining/.agent/research/inference_clean.md` (130): “For SAQ: scoring guidance describes criteria, not evidence lists”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (70-76): “#### Cell 3: APUSH × SAQ … | 1 | factual_accuracy | 14 | 78% | 76% |”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (82): “the model fills `sample_response` and `acceptable_evidence` fields with plausible-sounding but wrong historical examples.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (82): “Negative prompting ("don't include specific facts") fails because the 14B has strong-but-wrong parametric associations.”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (36): “SAQ scoring notes said "list 2-4 specific named evidence items." This is where hallucinations concentrated (wrong dates, wrong attributions). Changed to "describe analytical reasoning" (no evidence lists). Eliminated 15/17 factual accuracy failures instantly.”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (37): “**Critical lesson:** The more specific the evidence the model is asked to enumerate, the more opportunities for hallucination. Analytical framing → less fabrication surface area.”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (120): “The most impactful single change in the entire project was removing the evidence list from SAQ scoring notes. One change eliminated 15 of 17 factual accuracy failures.”
- `icloud-work/ML learnings/sft_v7_benchmark_postmortem.md` (132): “2. **The current approach (negative prompting) seemed to work on Gemini.** Because Gemini is large enough to mostly respect the "no specific evidence" instruction and has accurate enough parametric memory that when it does include evidence, it's usually right. The instruction that's good enough for a large model is insufficient for a 14B model.”
- `icloud-work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md` (175): “15 of 17 factual_accuracy hard-fails came from SAQ scoring notes.”
- `icloud-work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md` (178): “- Scoring philosophy changed from "list 2-4 specific named evidence items" to "describe what analytical reasoning earns the point"”
- `icloud-work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md` (183): “**Data:** factual_accuracy hard-fails: 17 -> 2.”
- `icloud-work/ap-social-studies-generator/python/generators/saq.py` (226): “3. States what does NOT earn the point (e.g., "just naming X without explaining = 0")”
- `grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd` (475): “Two-to-four checks: (1) correct principle stated, (2) applied to the case, (3) addresses counter-case/constraint, (4) conclusion warranted.”
- `grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd` (117): “with a tiny micro-rubric (e.g., credit for any 2 of the accepted set)”
- `home-agent-memory/findings_sftv7_20260424.md` (50-51): “**Pattern:** scoring_notes contained specific evidence (dates, named events) that
InceptBench hard-fails when wrong.”
- `home-agent-memory/findings_sftv7_20260424.md` (57): “**Fix applied (2026-04-24, saq.py `build_saq_user`):** Removed the PROCEDURE block.”
- `home-agent-memory/findings_sftv7_20260424.md` (58): “Replaced with categorical-only mandate: no names, dates, events in scoring_notes.”
- `home-agent-memory/findings_sftv7_20260424.md` (137): “2. **SAQ 33%** — new categorical-only fix not yet tested; these runs were pre-fix”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md` (122): “For SAQ/LEQ/DBQ, replace hallucination-prone evidence lists with verified-facts-only or analytical-category scoring notes.”
- `aptraining-local/den-of-ideation/HANDOVER.md` (123): “SAQ scoring notes should avoid hallucination-prone evidence lists”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/HANDOVER.md` (123): “SAQ scoring notes should avoid hallucination-prone evidence lists”
- `grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md` (174): “16. **Grading guidance MUST demand stance, not tokens; quotes fail closed (F16).**”
- `grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md` (175): “*Check:* no `scoring`/`accept` spec passes on keyword presence alone — negated, hedged, or”
- `grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md` (176): “off-topic responses route to unscorable/needs-work”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (327): “the rubric asks for the arc’s heart (the change and the how), not a checklist — a retell, not a quiz wearing a retell’s clothes.”
- `shadow-bench/docs/internals/ap-evaluation.md` (126-128): “Justify/Explain require reasoning tied to a chemical principle, with a correct answer + wrong reasoning earning nothing”
- `shadow-bench/src/inceptbench/prompts/question/ap_chemistry_evaluation.txt` (68-70): “AP awards the point only for a correct response **and** a valid justification tied to the relevant principle — a correct answer with missing or wrong reasoning earns nothing.”
- `shadow-bench/src/inceptbench/prompts/question/ap_chemistry_evaluation.txt` (70-71): “Items and their scoring criteria should reflect these conventions.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_saq.md` (39): “- Scoring criteria are concrete enough to grade consistently — describe what makes an answer correct, don't dictate the exact answer.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_saq.md` (73): “4. **Ambiguous scoring.** "Acceptable answers should be reasonable." → Useless. Replace with "Acceptable answers identify [type of factor] and explain [type of mechanism]."”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pipeline_status_2026-05-18.md` (154): “3. SAQ scoring notes should avoid hallucination-prone evidence lists.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (209): “SAQ sample responses were too generic to be scorer-facing.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (225): “SAQ repair now emits concrete scorer-facing examples by topic”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (218): “15/15 = 100%, avg overall 0.998667.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (249): “This is a strong step-level win, but it is not the final goal proof yet because `v5` repairs an existing generated run.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1471): “- Your “acceptable answers” list exceeds ~15–20 variants.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1455): “Result: a brittle, ever-growing ruleset that still misses clever but correct answers.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1469): “Reserve full automation for numeric/diagram/property-based tasks with explicit tolerances.”
- `grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd` (160): “Default: use a micro-rubric (0/1/2) for short text and explanations.”
- `grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd` (152): “Scorers (human or LLM-assist with thresholds) apply 2–3 checks.”
- `grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd` (147): “Result: a brittle, ever-growing ruleset that still misses clever but correct answers.”
- `grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd` (163): “Your “acceptable answers” list exceeds ~15–20 variants.”
- `grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd` (164): “You’ve edited the key twice post-launch to add more exceptions.”
- `grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/sources/GENERATION-CONTRACT.md` (20): “**A3 · Micro-rubric 0/1/2 is the scoring format for short text (`[WF 1467]`).**”
- `grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/sources/GENERATION-CONTRACT.md` (21-22): “**switch fully to the rubric** the moment the acceptable- answer list exceeds ~15–20 variants, or the key is edited twice, or correct-but-missed responses”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1472): “You’ve edited the key twice post-launch to add more exceptions.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1473): “You keep finding “should-be-correct” responses that the rules miss.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (410-413): “Students and generators can imitate rubric terms without performing the historical work. A sentence beginning "Although" is not automatically complex. Mentioning purpose is not sourcing. Naming two events is not comparison. The course scores the relationship between claim, evidence, and historical object, not the presence of a phrase.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/07-SCORING-FEEDBACK-XP.md` (8-9): “Meaning scoring replaced substring detection everywhere (a word detector wearing a rubric's clothes praises listed words in wrong sentences).”
- `g9/library/text/L01e07f.txt` (1): “The displayed praise and “That holds up” response do not establish that a student’s interpretation is true or well supported.”
- `g9/library/text/Lb99a1c.txt` (57-58): “"He wanted to be Othellos ancient but Cassio got to be the ancient" has the ranks backwards, but it met "someone else got it".”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (140): “The open word response is stored for review rather than judged correct by a keyword match.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (412-413): “The course scores the relationship between claim, evidence, and historical object, not the presence of a phrase.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/strategy/grade-9-strategy.md` (149): “The largest risks are a guide that sounds like a younger product in disguise, and a judge that grades evidence by keyword when Grade 9 asks for reasoning.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/strategy/grade-9-strategy.md` (156): “| The judge rewards matching quotes, not reasoning | Rubric criteria for relevant and sufficient evidence and for reasoning that links them (RI.9-10.8) |”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (130): “**RI.9-10.8:** "Delineate and evaluate the argument… whether the reasoning is valid and the evidence is relevant and sufficient; identify false statements and fallacious reasoning."”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (133): “The LLM rubric should grade how relevant and sufficient the evidence is, and the reasoning, not just whether a matching span was found.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/canvases/01-readers-desk-odyssey.html` (44): “Where your argument stands”
- `othello-course-renderer-draft/repo/docs/design/grade-9/canvases/01-readers-desk-odyssey.html` (44): “The claim answers the question”
- `othello-course-renderer-draft/repo/docs/design/grade-9/canvases/01-readers-desk-odyssey.html` (44): “The evidence is relevant”
- `othello-course-renderer-draft/repo/docs/design/grade-9/canvases/01-readers-desk-odyssey.html` (44): “The reasoning links evidence to claim”
- `othello-course-renderer-draft/repo/docs/design/grade-9/canvases/01-readers-desk-odyssey.html` (44): “The counterclaim is answered”
- `othello-course-renderer-draft/repo/docs/design/grade-9/prototype/README.md` (41): “The judge is rules, not an LLM.”

Published: [Common Core State Standards for ELA & Literacy (NGA & CCSSO, 2010)](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf)

Against: Telling the small writer to leave specific facts out did not work: it wrote wrong specific facts instead (the same analysis). the same note calls that instruction good enough for a large model and insufficient for a 14B one (`icloud-work/ML learnings/sft_v7_benchmark_postmortem.md`). The course's own published guide lists examples: its short-answer scoring guidelines say what credited responses must do and then give "Examples that earn this point include the following:" (`icloud-work/ap-social-studies-generator/curriculum/ceds/ap-european-history-ced.pdf`, pdftotext -layout output, line 12660). The same change also removed about 300 lines of other prompt constraints (`icloud-work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md`, line 179), so the drop is not the list change alone. It is design guidance, not a measurement, and for a short recall answer the same library credits any two of an accepted set instead (`grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd`). The fix was not yet tested when the note was written; those runs came before it (same file, line 137). A ban on lists alone did not work: the same report says that for these notes “don’t list specific facts” failed and that verified-facts-only constraints are stronger. The handover's techniques come from a sibling generator whose best run used a different grader version, which it calls design evidence, not certified current scores. In a 15-item replay, short-answer sample responses were too generic for the scorer, and the repair that added concrete examples by topic was one of the changes in the version that passed 15 of 15 (`icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md`, lines 205-225); that version repaired an existing run rather than a fresh one (line 249). The same BrainLift keeps full automation for numeric, diagram and property-based answers with explicit tolerances, where the space of valid answers is small.

<sub>criterion · scoring-guide, integrity · universal · from ap, g3, g9 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Hard for the right reason

Put an item's or a level's difficulty in the knowledge or reasoning it demands, never in labels, untaught words, hard syntax, negatives, obscure facts, padded reading or reworded easier lessons.

The assessment BrainLift holds that an item whose difficulty can't be explained by the knowledge it targets is almost certainly measuring a mix of construct and noise, and that hardness from convoluted language, tricky negatives and obscure contexts is an invalid obstacle, not rigour (`grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md`, lines 2366-2367); its diagnostic section adds that an item should not punish students who know the material but are tripped up by wording (line 398). In the Grade 3 course an ordering item shipped as a menu of position numbers per event, which taxed exactly the working memory the item existed to measure comprehension with; it became drag-and-drop with its own check, and the build rules now say to match the gesture to the shape of the answer (`grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md`, lines 757-766). Difficulty from what is tested means more steps, synthesis, a subtle distinction or a plausible confusion. Wording difficulty includes rare or untaught words, hard syntax and negatives, and extra help in the stem should not set the level either. If plainer wording that tests the same thing would make the item easier, remove that difficulty.

Quoted:

- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (2366): “Any item whose difficulty cannot be explained in KC/KDT terms (steps, conversions, cue structure, etc.) is almost certainly measuring a messy mix of construct and noise.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (2367): “In a mastery model, these items are not rigorous; they are simply invalid obstacles.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (398): “The item should not reward test-taking savvy or punish students who know the material but are tripped up by wording.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md` (760-761): “**The interaction taxed exactly the working memory the item exists to measure comprehension with.**”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md` (766): “* **Match the gesture to the shape of the answer.**”
- `icloud-work/evaluator/docs/reports/BENCHMARK_RUN3_REPORT.md` (80): “- Difficulty adjustment only changes vocabulary complexity, not cognitive demand”
- `icloud-work/evaluator/docs/reports/BENCHMARK_RUN5_REPORT.md` (92): “**24 out of 39 hard questions failed (62%)**”
- `icloud-work/evaluator/docs/reports/BENCHMARK_RUN5_REPORT.md` (114): “**Pattern:** The endpoint adds too much context/scaffolding, which paradoxically makes hard questions easier to answer.”
- `icloud-work/evaluatorML/.agent/memory/packages/apush_unit1_pipeline_v0/docs/KNOWN_FAILURES.md` (44): “- Make the medium difficulty come from an APUSH inference, not wording complexity.”
- `icloud-work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py` (216): “Do not make difficulty depend on obscure wording; make it depend on historical reasoning.”
- `icloud-work/ap-social-studies-generator/HANDOFF-finetune-status.md` (69): “**Why it failed:** The difficulty labels were added but content difficulty doesn't vary.”
- `icloud-work/ap-social-studies-generator/HANDOFF-finetune-status.md` (70): “**Result:** MCQ_SET 86% → 62%. The retrain also regressed DBQ (67% → 33%) and SAQ (100% → 60%).”
- `icloud-work/ap-social-studies-generator/HANDOFF-finetune-status.md` (71): “**Lesson:** Label injection without content variation teaches nothing. The model needs examples with structurally different question types at each difficulty level.”
- `icloud-work/ap-social-studies-generator/docs/archive/RUN6_ANALYSIS.md` (41): “**ACTUAL:** Questions became cognitively shallow recall exercises”
- `icloud-work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md` (104): “"What would X group think?" pattern is single-step reasoning.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt` (151): “Flag only when the wording demonstrably adds reading load without adding cognitive demand → `clarity_precision`.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt` (152): “This commonly occurs when generation tries to "cover" as much of the standard as possible by inserting unrelated topics into the stem.”
- `icloud-work/inceptbench-main/tests/test_evaluator_prompt_rules_411_418.py` (9-11): “G6 ELA items with "First X. Then, based on X, Y." stems and adult-register passages were passing evaluation at 0.95 ACCEPTABLE despite real grade-band problems.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (96): “Being in the same broad curriculum standard does not make a clause connected — the clause must provide information *necessary* to answering this specific question.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt` (125-126): “Three or more reasoning steps, or transfer of the skill to a novel but supported context. - Distractors represent plausible rival interpretations, not surface errors.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt` (127): “- Length alone is not difficulty.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/match_evaluation.txt` (315): “Hard vocabulary or long item text does not elevate an EASY structure to MEDIUM, but genuine item ambiguity does.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/match_evaluation.txt` (322): “Ask: "What is the wrong category a partially-knowing student would pick for this item, and why would they pick it?"”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/match_evaluation.txt` (504): “If the majority of items in a Medium question are recycled from its Easy counterpart, set `difficulty_alignment = 0.0` for the Medium question — it is not genuinely harder, just relabelled.”
- `icloud-work/inceptbench/docs/EVALUATOR_VARIANCE_FIX.md` (at e5be84f^) (288): “8. **Cross-difficulty recycling** — The evaluator still can't detect cross-difficulty item recycling (same facts rephrased across easy/medium/hard) because each question is evaluated independently.”
- `APinceptbench/docs/reports/BENCHMARK_FAILURE_REPORT.md` (211): “- Difficulty should affect cognitive demand, not just vocabulary”
- `APinceptbench/docs/reports/BENCHMARK_RUN3_REPORT.md` (80): “- Difficulty adjustment only changes vocabulary complexity, not cognitive demand”
- `APinceptbench/docs/reports/BENCHMARK_RUN5_REPORT.md` (114): “**Pattern:** The endpoint adds too much context/scaffolding, which paradoxically makes hard questions easier to answer.”
- `APinceptbench/docs/reports/BENCHMARK_RUN5_REPORT.md` (32): “**Key observation:** Run 5 fixed easy difficulty (27% → 68%) but broke hard difficulty (58% → 38%) and cognitive demand (70% → 59%).”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (152): “if I simplified the wording of this item without changing what it tests, would it become easier? If yes, the current difficulty is at least partly extraneous.”
- `grade3-reading/knowledge_bot/knowledge/kb-0161-assessment-item-difficulty-core.qmd` (70): “If you cannot explain why an item is hard, you should not be using it”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (126): “N5: linguistic validity. Untaught vocabulary or syntax can create construct-irrelevant difficulty.”
- `icloud-work/aptraining-crystal-copy-20260521/evidence/FUTURE_RUN_IMPROVEMENT_BACKLOG_20260521.md` (233): “- hard questions should require reasoning, not obscure names or out-of-period facts.”
- `icloud-work/aptraining-crystal-copy-20260521/evidence/FUTURE_RUN_IMPROVEMENT_BACKLOG_20260521.md` (234): “- easy questions should still avoid giveaway wording.”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/common_pre_checklist.md` (71): “- [ ] Hard: subtle distinction, synthesis, or counterargument evaluation”
- `icloud-work/aptraining/apllm-history/runtime_assets/ib_satisfaction_kit_v1/failure_mode_index.json` (40-41): “"trap": "Required outside knowledge is obscure", "fix": "All required facts must be curriculum-standard"”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D7-knowledge-first-curriculum.md` (32): “Autonomous items are screened for untaught Tier-2 vocab, grade-inappropriate syntax, and idioms that make them test reading, not content”
- `ti-courseplans-audit/skills/train-teacher/references/curriculum-architecture.md` (99-100): “**linguistic-validity QC** (untaught Tier-2 vocab, syntax, idioms — required for teacherless delivery)”
- `icloud-work/aptraining/.agent/research/sota_strategy.md` (114): “The hga fix already showed that injecting difficulty *labels* without content variation does nothing.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (204): “The set is marked as 'hard,' but two questions are explicitly labeled 'Easy' and 'Medium,' so the quiz does not match the requested single-difficulty level.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (330): “Additionally: enforce per-question difficulty assignment matching the set's stated difficulty.”
- `icloud-work/aptraining/.agent/plans/PLAN-mission-2026-04-26.md` (80): “Minor effect; model learns difficulty implicitly from data.”
- `aptraining-local/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md` (134): “- difficulty must be earned by outside APUSH context, not reading comprehension.”
- `aptraining-local/parallel-ideas-lab/experiments/prompt_perfection/NOTES.md` (117): “- MCQ misses are mostly educational-accuracy failures: answer can be found by reading, answer leaks, or weak APUSH knowledge demand.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_leq.md` (43): “- Students can earn full marks using ONLY the curriculum (no obscure outside knowledge required).”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md` (110): “2. **Subject-knowledge bypass**: a student with zero subject knowledge could answer just by reading the stimulus. If the answer is paraphrased in the stimulus, the question fails educational_accuracy. Force the answer to require a curriculum-derived inference, not just stimulus paraphrase.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md` (96): “- Easy: direct recall of one curriculum fact; correct answer matches statement nearly verbatim.”
- `grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md` (53): “3. **Genuinely G5, never G3 dressed up.** Complexity lives in the task, not inflated prose. The”
- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md` (171): “`item-2-cards` distractors are below band.”
- `grade3-reading/artifacts/g5-book-2026-09-29/SCOUT-AND-PLAN.md` (12): “"never a Grade 3 copy; consult the canon; log the rule behind each decision"”
- `grade3-reading/artifacts/g5-book-2026-09-29/BUILD-SPEC-G5-U1-L1.md` (4): “(1) ALL G3-acquired mechanisms carry to G5 as-is”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-main-checkout-jul-work.patch` (20736): “| **AOTA / NOTA / negative stem** | "all/none of the above", "which is NOT" | hard fail |”
- `grade3-reading/_archive/2026-08-13-consolidation/redteam-g3-round3-report-and-evidence.tar.gz` (RED_TEAM_ROUND3.md inside it) (56): “| No T/F, AOTA, NOTA | PASS | 0 True/False items or option sets; 0 All/None-of-the-above; 0 classic EXCEPT/least/not-true exclusion stems. |”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/audit/full-course-review-red-team-interim-2026-07-20.md inside it) (39): “- The prohibited negative choice-stem scan is empty.”
- `grade3-reading/ti-courseplans/courses/g5-reading-v2/audit/full-course-review-red-team-interim-2026-07-20.md` (39): “- The prohibited negative choice-stem scan is empty.”
- `grade3-reading/ti-courseplans/courses/g6-science/brainlifts/v0.1.md` (21): “science items at G6 presuppose ~G4+ reading; item language must not turn science assessment into a covert reading test”
- `grade3-reading/ti-courseplans/courses/g6-science/brainlifts/v0.1.md` (21): “reading-load ceiling TO CONFIRM”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/generation-contract.md inside it) (88-90): “**"All of the above," "none of the above," and negative stems** ("which is NOT…") are also **banned outright** — they test test-taking convention, not the target skill.”
- `incept-package-hub/.artifacts/source/Grade 5 Reading - Complete Course Review.zip` (Grade 5 Reading - Complete Course Review/audit/full-course-review-red-team-interim-2026-07-20.md inside it) (39): “The prohibited negative choice-stem scan is empty.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (63): “D5.4 (no negative stem): no 'which is NOT' or negatively-framed stem found in any of the 18 selected-response items checked.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md` (15): “Stems avoid "which is NOT"; positive framing”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (2067): “Stems that ask "Which of the following is NOT..." require an additional cognitive step: the student must identify what is true and then reverse the logic.”
- `g9/transcript/chat-transcript.redacted.txt` (3085): “More difficult vocabulary alone does not raise the level of thinking.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (557-558): “Set difficulty should come from historical reasoning and evidence use, not obscure trivia.”

Against: An earlier lesson in the same project said the reverse, that hard questions must require recall, not reading, and that scaffolding makes hard questions medium (`icloud-work/ap-social-studies-generator/docs/archive/ITERATION_ANALYSIS.md`). One review allowed that heavy scaffolding might be acceptable in a practice item for struggling students (`icloud-work/ap-social-studies-generator/docs/analysis/evaluation_audit.md`). The 86%-to-62% drop came from a retrain that also regressed other item types, so it is not a clean test of labels (`icloud-work/ap-social-studies-generator/HANDOFF-finetune-status.md`). Multi-step prompts where each step drives a different decision are not flagged, and a first step that asks for a member of a closed grammatical category is exempt (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt`, lines 151 and 156). The recycling check exists only for matching items, and only when the variants are judged in the same batch (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/match_evaluation.txt`, line 492); and the rubrics disagree on item count, which the matching rubric says does not determine difficulty (the same file, line 285) while the ordering rubric sets more items for harder levels (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/sequence_evaluation.txt`, lines 157-159). The difficulty verdicts were a model judge's opinion with no learner data, and the pattern swung between runs: the run that broke hard items fixed easy ones, from 27% to 68%. The grader cannot check difficulty unless difficulty is defined for it: with no definitions given, it scores difficulty alignment 1.0 (icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/_base_evaluation.txt, line 137). The finding that labels do nothing is second-hand, from an earlier handoff lesson ('handoff hga-fix lesson', `icloud-work/aptraining/.agent/research/sota_strategy.md`, line 113), and the plan's line supports only the first clause. The same prompts let the easiest level match the taught statement almost word for word. In a reading lesson the text itself is what is tested, so there a question must need the text rather than outside knowledge. The mechanisms can carry across levels unchanged: a later ruling carried every Grade 3 mechanism to Grade 5 as it was, with the content written at Grade 5 from the course's own sources (`grade3-reading/artifacts/g5-book-2026-09-29/BUILD-SPEC-G5-U1-L1.md`).

<sub>criterion · demand, format, wording · universal · from ap, g3, research · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Higher-order needs material not seen before

Count a question as higher-order, such as application or analysis, only when it presents material new to the learner, since a longer stem over familiar content is still recall.

The assessment BrainLift used as feedback for the reading courses holds that unless an item presents material the student has not previously encountered, such as a new passage, data set, scenario or diagram, it usually tests recall of a familiar pattern however elaborate the stem looks (`grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md`, line 1995). It treats difficulty and cognitive level as independent and calls conflating them the most common tagging error in item banks (line 2010). An adversarial review's checklist lists the fake higher-order item, an inference item that is recall with a longer stem, to be retagged as recall (`grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md`, line 163). A hard question is not thereby a higher-order one.

Quoted:

- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1995): “Unless the item presents material the student has not previously encountered — a new passage, data set, scenario, or diagram — it is usually testing whether the student can recall a familiar pattern, regardless of how elaborate the stem looks.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1995): “The novel stimulus requirement is the single most reliable test of whether an item is genuinely higher-order: no new material, no higher-order thinking.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (2010): “A hard recall item is still recall. An easy application item is still application.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (2010): “These are independent dimensions, and conflating them is the most common tagging error in item banks.”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (163): “genuine higher-order needs a NOVEL stimulus (unseen passage/scenario); else retag recall”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (58): “no new material, no higher-order thinking.”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (58): “Unless the item presents material the student has not previously encountered — a new passage, data set, scenario, or diagram — it is usually testing whether the student can recall a familiar pattern, regardless of how elaborate the stem looks.”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (73): “A hard recall item is still recall.”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (163): “genuine higher-order needs a NOVEL stimulus (unseen passage/scenario); else retag recall”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md` (26): “Any "application/analysis" item presents novel stimulus; else tag it recall”

Against: none found

<sub>criterion · demand, stimulus · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Inferences rest on the text

An inference, modelled or asked for, may combine only what the text shows with what every student can be assumed to know, never an outside cultural or world fact.

A ruling in the reading project struck a worked example whose extension reached for outside-world knowledge of a foreign city that the course's students could not be expected to have: an inference may only use what the passage's own words show, and an extension deepens the mood from remaining text clues, never a civic or cultural fact the passage never gave (`grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd`). The same procedure's frame is "The text says ___, and I know ___, so I think ___", so the knowledge an inference may add is what every student can be assumed to have.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (80-82): “an inference may only use what the passage's own words show; extension deepens the mood from remaining text clues, never a civic/cultural fact the passage never gave.”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (80): “reach for outside-world knowledge”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (81): “inference may only use what the passage's own words show; extension deepens the mood from”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (82): “remaining text clues, never a civic/cultural fact the passage never gave.”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/procedures/infer.md` (13): “Three hard rules on the frame, from the authored designs:”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/procedures/infer.md` (19-21): “The "I know that" move supplies WORLD knowledge (what anyone knows about being trapped, being tired, wanting to be safe), never a second quote and never a fact the text already states.”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md` (173): “A modelled inference may only use what the passage's own words show, so the extension deepens the mood from the remaining clues instead of adding a civic "rules" layer.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (71): “London-mood, flying-mood, and Neverland-mood inferences all require either lesson-supplied knowledge bridges (Step 3 MCQ/MSQ at each release level) or common-sense prior knowledge (cold/dark, feather-in-wind)”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (272-273): “A model think-aloud reasons only from passage evidence, never from background knowledge the child cannot be expected to have.”

Against: the same procedure defines inference as combining text clues with what you know (the same file), so where assumed knowledge ends and an outside fact begins is a judgment. The project's own inference frame combines text clues with what the student knows, so where allowed background ends and an outside fact begins is a judgment (`grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd`, line 76).

<sub>criterion · demand, stimulus · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Keep facts inside the period asked

Keep every fact in an item, its sample answers and marking notes included, inside the period and region the request names, and check dates in code. In one 1,080-item run, 41 items were found out of period.

Failure analysis of a 1,080-row export of AP history items counted 41 out-of-period items and 39 factual errors, with named anachronism families recurring. Essay marking notes and short-answer sample responses routinely cited years outside the unit, and in a calibration one essay's marking notes used evidence from a region outside the one its prompt named. It holds where a request fixes a period and region, as in the AP history courses.

Quoted:

- `icloud-work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/next_live_run_prep.md` (3): “Complete 1080-row export; 926/1080 = **85.7%** overall, MCQ_SET 67.1%.”
- `icloud-work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/next_live_run_prep.md` (25): “**Symptom**: 21 sample_response_error + 41 out_of_period + 39 factual_error + named-content-trap families (`content_lakota_pre1607` 14, `content_muscovy_east_india` 7, `content_navigation_acts` 3, `content_requerimiento_overclaim` 2) = chain hallucinating concrete, name-able anachronisms in Unit 1 content.”
- `icloud-work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/next_live_run_prep.md` (46): “**Symptom**: LEQ rubric_notes routinely cite years outside Unit 1 (1491-1607); SAQ sample_responses do the same.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md` (45): “- `apush-u1-1505-leq-medium`: LEQ rubric included Northeastern evidence outside a Southwest / Great Basin prompt.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (52): “This creates period drift and can make an item look plausible while testing Unit 2 content. ... later context must be labeled and never required for the Unit 1 key.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (156-159): “Dates matter because they bound what can cause what. ... Context can reach outside a prompt period, but the response must explain the relationship instead of smuggling later knowledge into the claim.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (71-72): “Do not use a later event as period evidence, invent a direct quotation, treat Indigenous societies as interchangeable, or make the stimulus itself reveal the answer.”

Against: A simple year check caught little on its own: 1 of 7 essay chronology failures, about 14%, with no false positives (icloud-work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/KNOWN_ISSUES.md, lines 135-137).

<sub>criterion · alignment, scoring-guide · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Keep guessable formats out of scoring

Keep true/false and other two-option items out of scored decisions, and score a multi-select item only when its stem says how many to choose and its scoring rule is declared. In one course, 4 of 48 multi-select stems did not announce how to select.

An assessment BrainLift in the reading course's feedback bans true/false from summative pools, and any multi-select without a principled scoring rule, because these formats are unusually sensitive to guessing, cueing and ambiguous category boundaries; one review round's feedback added that a two-option yes/no is a 50/50 guess. The course's assessment memo then counted 0 of 432 items as true/false, declared all-or-nothing scoring for multi-select, and found 44 of 48 multi-select stems announcing how to select and 4 not; its quality standard requires an explicit count in multi-select stems.

Quoted:

- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md` (35): “Today **44 of 48** MSQ stems cue this; **4 do not**”
- `grade3-reading/ti-courseplans/docs/standards/course-quality.qmd` (40): “- explicit count in multi-select stems;”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md` (33): “Multi-select is banned unless it declares a principled scoring rule.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md` (29): “Stated plainly: 0 of 432 items are True/False.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1403): “These formats are unusually sensitive to guessing, cueing, and ambiguous category boundaries”
- `grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md` (52): “A 2-option yes/no is a 50/50 guess.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “A 0.50 chance floor cannot independently support advancement or mastery.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/ASSESSMENT-QUALITY-MEMO.md inside it) (29): “Stated plainly: 0 of 432 items are True/False.”
- `incept-package-hub/course-packages/courses/g5-reading/review/evidence/case-for-review.md` (86): “Isolated two-option items are forbidden for mastery and may appear only as declared non-mastery subdecisions with chance floor visible.”

Against: A multiple-choice BrainLift in the same file holds that single true/false items are nearly useless for inference but that in bundles of 15 or more the guessing averages out and the format becomes more defensible (`grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md`, line 2008).

<sub>criterion · format, stem, integrity · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Keep punctuation with its sentence

When words in a sentence become answer choices, blanks or glossary buttons, keep the sentence's punctuation attached to its word or final choice, and check wrapping before and after selection. One staging sweep recorded 13 places where a sentence's comma or full stop fell alone onto a line below the answer choices.

Sentence-final full stops and commas fell onto a line of their own below groups of answer chips, 13 times in one staging sweep, and once after a glossary button at the end of a passage sentence, where the button and the full stop were separate elements. A fix confirmed on the one page first reported did not cover the other sentence-completion layouts. The repair direction keeps trailing punctuation with its sentence or selected ending and checks wrapping before and after a selection.

Quoted:

- `grade3-reading/visual-findings-2026-09-07/README.md` (81): “The sentence-final period renders alone on a new line below the answer options, visibly detached from the sentence.”
- `grade3-reading/visual-findings-2026-09-07/README.md` (87): “Repair direction: keep trailing punctuation with its sentence/selected ending instead of leaving it after a block of choices. Verify wrapping before and after a selection.”
- `grade3-reading/visual-findings-2026-09-07/staging-full-sweep/README.md` (61): “Expected: punctuation should stay attached to the sentence or final chip rather than occupy a separate line.”
- `grade3-reading/visual-findings-2026-09-07/staging-full-sweep/README.md` (63): “This is the same defect family as earlier main finding V3, on additional staging pages. The previously sampled V3 fix does not cover all sentence-completion layouts.”
- `grade3-reading/visual-findings-2026-09-07/staging-full-sweep/README.md` (65-81): “Additional occurrences visually observed in the sweep (each has a saved image; the three above received dedicated re-navigation reproductions):”
- `grade3-reading/visual-findings-2026-09-07/staging-full-sweep/README.md` (89): “DOM evidence: the final glossary button uses class 'bk-gw' inside a 'bk-seek' span, followed by a separate period text node.”

Against: A later laptop sweep did not reproduce it at 1100 × 700 on the four pages where the staging sweep had seen it at that width, and limits its own claim: "No claim about other widths." (`grade3-reading/visual-findings-2026-09-07/laptop-student-sweep/README.md`, lines 60-61).

<sub>criterion · options, wording · universal · from g3 · measured · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Key to a relationship the text asserts

In a question meant to show the text was understood, key the answer to a relationship the text asserts, since a single retrievable fact is easy to leak.

The reading project's anti-leak writer rules ask for keys that hinge on a relationship the passage asserts (a cause it names, a contrast it draws, an inference it licenses) rather than a lone retrievable noun, since denser passages make relational keys both natural and harder to leak. For inference and theme items, the rationale must quote the two or more sentences whose combination licenses the inference, with no single-sentence lift.

Quoted:

- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (48-51): “At G5, prefer keys that hinge on a … **relationship the passage asserts** (a cause the text names, a contrast the text draws, … an inference the text licenses) rather than a lone retrievable noun — denser passages … make relational keys both natural and harder to leak.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (53-54): “For inference/theme items, quote the two-or-more … sentences whose combination licenses the inference (no single-sentence lift).”
- `g9-transformer-runs/blocks/d872bc1dfbda65fb.json` (8): “What facial expressions are visible on the broken statue's head?”
- `g9-transformer-runs/blocks/d872bc1dfbda65fb.json` (87): “a hint uses a word that hands the answer over, or the answer itself:”
- `g9/transformer/src/mechanics/open-check.js` (42): “"third_nudge": "the words to read again, quoted exactly, still not the answer"”
- `g9/transformer/src/mechanics/open-check.js` (63): “a hint may quote the text, even the line to”
- `g9/transformer/src/mechanics/open-check.js` (64): “read (its third rung), but it uses no leak word and copies no four-word run of the reveal outside a quotation”
- `g9-transformer-runs/blocks/b5f74899349e1331.json` (22): “"third_nudge": "Read the words \"little note, nor long remember\" alongside \"never forget\" to see the contrast.",”

Against: Some in-lesson checks are literal on purpose: a ruling keeps reading checks as retrieval, and whether a literal check must be about the theme's hinge was left open (`grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd`, lines 64-66).

<sub>criterion · key, demand, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Leaky formats stay out of mastery gates

Keep item formats that leak as a family out of every mastery gate, serving them, if at all, only in a practice lane that never gates progress. One reading plan records choice-family argument items leaking about 98.6% by construction.

A Grade 8 reading course built to a full-coverage target gate-assesses all 15 plan standards from a certified-only item pool, with its leaky formats confined to a non-gating practice lane. Its case for review counts 5 gating formats and a 43-item lane in three formats for format exposure, never routed through a mastery gate, with 0 audit errors, and says zero leaky and zero broken items serve among its gating items; its coverage matrix tells any agent to keep the partition. A Grade 7 plan drops all-choice assessment, recording that choice-family argument items leak about 98.6% by construction.

Quoted:

- `grade3-reading/edullm-review-hub/course-packages/courses/g8-reading/review/start-here.md` (28): “full item-type coverage, with the leaky formats confined to a non-gating practice lane.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g8-reading/review/evidence/case-for-review.md` (47-48): “5 gating formats (text_entry, sequence, mcq, ebsr, inline_choice) + a **43-item non-gating practice lane** (multi_select, hot_text, match) for”
- `grade3-reading/edullm-review-hub/course-packages/courses/g8-reading/review/evidence/case-for-review.md` (49): “format exposure, never routed through a mastery gate (all `gating:false`, 0 audit errors).”
- `grade3-reading/edullm-review-hub/course-packages/courses/g8-reading/review/evidence/case-for-review.md` (42-43): “Served is a strict subset of certified; **zero leaky and zero broken items serve.**”
- `grade3-reading/edullm-review-hub/course-packages/courses/g8-reading/review/evidence/validation/coverage-matrix.json` (4): “Preserve the gating/practice partition; leaky formats never route through a mastery gate.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (407-408): “choice-family argument items leak ~98.6% by construction”

Against: A record already there asks that every item a check fails leave what learners see, not only scoring, and the review behind it allowed only confinement to non-gating slots, which this lane is. In the same bank, multiple-choice and two-part evidence items rebuilt to need the passage are gating formats, so whether a format leaks as a family depends on how its items are built.

<sub>criterion · format, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Limit the load of each step

Limit what each step asks a reader to hold: few new names per section, few short options per item, no long reading without a check, each task on one screen. A scan of one course found 137 of 772 items over a five-option cap.

Reviews of a Grade 5 course flagged a ~204-word part that introduced eight new proper names before an item asked students to compare four options of ~50–70 words each, and four consecutive reading pages with no interaction (`grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md`, `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md`). A simulated outside review of four Grade 3 lessons found 3 narrated passage chunks, of 241, 273 and 279 words, that kept students passive for more than 60 seconds before a check (`grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md`). An outside review of a Grade 3 course called one item's twelve selectable options an excessive motor and cognitive load for an eight-year-old (`grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md`); a scan of a Grade 5 course found 137 of 772 items over a cap of 5 (`grade3-reading/artifacts/g5-merged-course/option_cap_report.md`), and a one-screen census found tasks running past the fold at 1440×900 and split them (`grade3-reading/artifacts/qc-run-2026-09-04/`).

Quoted:

- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md` (43): “~204-word part introduces EIGHT new proper names”
- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md` (258): “- **W-11. WORTH-FIXING — four consecutive reading pages with no interaction”
- `grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md` (493): “3 passage chunks exceed 60s passive during autoplay narration”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (103): “one hot-text item offered twelve selectable options, an excessive motor and cognitive load for an eight-year-old.”
- `grade3-reading/artifacts/g5-merged-course/option_cap_report.md` (7): “- items over cap: **137**”
- `grade3-reading/artifacts/qc-run-2026-09-04/QC Run Report — Peter Pan L4-L7 + G5 (2026-09-04).md` (31): “### 3. HIGH — one-screen census, our lane (additions row I/census)”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/LOAD-BEARING-METRIC.md inside it) (88): “**Rule of thumb (declared, not measured):** at G3, a single lesson introduces **≤ ~5 new allusive/vocabulary anchors**, and a unit spirals them rather than front-loading.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/LOAD-BEARING-METRIC.md inside it) (100): “its **G3 delivery cap** is the tightest; the same topic can spend more of its density at G6+.”

Against: none found

<sub>criterion · demand, options, accessibility, sequence · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Localize the surface, not the concept

Localize a question's surface, such as names, places and everyday objects, but never its concept, its standard units or a context the lesson needs.

One evaluation framework for generated questions requires 'culturally appropriate names, locations, objects, and contexts' in every question, and lists what is never localized: universal mathematical and scientific concepts, international context when pedagogically necessary, and standard units of measurement (`icloud-work/incept/incept-uae-api-website/inceptapi.com/INCEPT_Benchmarking_Framework.html`). The generator's cultural guidelines add that cultural points apply only where 'genuinely relevant to the learning objective' (`icloud-work/incept/incept-multilingual-generation/spiky_points_of_view.json`). Both are adopted rules, with no measurement.

Quoted:

- `icloud-work/incept/incept-uae-api-website/inceptapi.com/INCEPT_Benchmarking_Framework.html` (518): “Our localization framework ensures that all generated questions use culturally appropriate names, locations, objects, and contexts relevant to UAE students.”
- `icloud-work/incept/incept-uae-api-website/inceptapi.com/INCEPT_Benchmarking_Framework.html` (547): “Universal mathematical/scientific concepts”
- `icloud-work/incept/incept-uae-api-website/inceptapi.com/INCEPT_Benchmarking_Framework.html` (549): “International context when pedagogically necessary”
- `icloud-work/incept/incept-uae-api-website/inceptapi.com/INCEPT_Benchmarking_Framework.html` (550): “Standard units of measurement”
- `icloud-work/incept/incept-multilingual-generation/spiky_points_of_view.json` (125): “Only apply spiky points that are genuinely relevant to the learning objective”

Against: The same guidelines also direct one cultural framing everywhere: 'Prioritize Arabic and Islamic perspectives in all explanations.' (`icloud-work/incept/incept-multilingual-generation/spiky_points_of_view.json`, line 9), against their own rule that cultural points apply only where relevant.

<sub>criterion · wording, alignment · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Make a locate item demanding

When an evidence-selection item stays a locate item, make it demanding: the sentence must meet two conditions at once, or be chosen for the role it plays. In a Grade 5 reference lesson only 2 of 10 items are near-locate, and each carries two constraints or asks about a property of the representation.

The acceptance bar for a Grade 5 reading lesson maps the depth of its ten items, all passage-dependent, and most ask for inference about what a representation can't show, exact-set selection over several steps or bounded writing. Its only two near-locate items are still demanding: one asks for the sentence that both identifies a connector and states the source's limit on a claim, the other for the sentence that assigns a role to the diagram, a claim about what each representation does.

Quoted:

- `grade3-reading/artifacts/u4l2-build/g5-audit/G5-BAR.md` (137): “"Select the sentence that **both** identifies the non-food connector **and** states the source packet's limit on the fish claim"”
- `grade3-reading/artifacts/u4l2-build/g5-audit/G5-BAR.md` (141): “locate, but the target property is a meta-claim about representation roles”
- `grade3-reading/artifacts/u4l2-build/g5-audit/G5-BAR.md` (148): “So the bar: only I01/I05 are near-locate, and even those are constraint- or meta-property-locate.”

Against: It rests on one reference lesson's design, and no learner data is cited.

<sub>criterion · demand, format · domain · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Make each evidence mark a decision

Make each evidence tap or highlight a decision that can be wrong and is then discussed, steered to the parts that matter, since untrained highlighting is rated low utility. A review rated highlighting and underlining as low utility, one of five techniques so rated.

A Grade 4 lesson's research note cites a review that rates highlighting and underlining as low utility, one of five techniques so rated, with the review's own caveat that most reviewed studies gave participants no training in what to mark, so the finding argues against untrained marking, not against a taught selection routine. It concludes that a tap-the-evidence interaction is not itself the learning: what makes it work is that the tap is a decision that can be wrong and is then argued about. The Grade 9 desktop brief adds a study of 371 students in grades 5–8 in which digital highlighting was linked positively to comprehension and paper highlighting negatively, much of it falling outside the important parts of the text, and asks for highlighting steered to the parts that matter, such as a 'highlight the evidence' task.

Quoted:

- `othello-course-renderer-draft/repo/docs/research/g4-u1-l2-the-cyclops.md` (397-398): “rate highlighting and underlining as low utility, one of five techniques so rated”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l2-the-cyclops.md` (405-407): “So the finding argues against untrained marking, not against a taught selection routine.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l2-the-cyclops.md` (408-409): “What makes it work is that the tap is a decision that can be wrong and is then argued about.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md` (100): “Goodwin et al. (2020, AERJ), 371 students in grades 5–8: students highlighted and annotated less on digital text.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md` (100): “But digital highlighting was linked positively to comprehension, while paper highlighting was linked negatively (much of it fell outside the important parts of the text).”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md` (100): “*Implication:* make highlighting effortless and steer it to the parts that matter (for example a "highlight the evidence" task).”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (395-402): “**Highlighting on its own does nothing.** Dunlosky, Rawson, Marsh, Nathan and Willingham, Improving Students' Learning With Effective Learning Techniques, Psychological Science in the Public Interest 14(1), 2013, rate highlighting and underlining as low utility, one of five techniques so rated, against practice testing and distributed practice as high utility. The reported reason is that most students over-highlight and that highlighters were at a disadvantage on inference questions. [DOI 10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266);”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (407-409): “For us it argues one specific thing: a tap-the-evidence interaction is not itself the learning. What makes it work is that the tap is a decision that can be wrong and is then argued about.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (404-407): “Caveat, stated in the monograph's own limitation and repeated in secondary coverage: most reviewed studies gave participants no training in what to mark. So the finding argues against untrained marking, not against a taught selection routine.”

Published: [Dunlosky, Rawson, Marsh, Nathan & Willingham 2013](https://doi.org/10.1177/1529100612453266) · [Goodwin et al. 2020](https://files.eric.ed.gov/fulltext/EJ1260522.pdf)

Against: Digital highlighting was linked positively to comprehension in that study, a link the low-utility rating does not explain, and annotating and dictionary use showed no link (`othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md`, line 100). Most reviewed studies gave no training in what to mark: "Caveat, stated in the monograph's own limitation and repeated in secondary coverage: most reviewed studies gave participants no training in what to mark. So the finding argues against untrained marking, not against a taught selection routine." (`grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md`, lines 404-407).

<sub>criterion · format, demand, feedback · universal · from g3, g9, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Make the target thinking unavoidable

Make the thinking a task targets, such as understanding a text rather than matching its words, impossible to skip: students take any shortcut, and a gamed pass proves nothing.

The delivery platform's principles say any reward system attracts gaming and list the shortcuts students take: tanking placement tests to get easier content, clicking through explanations without reading, guessing until correct, and pattern matching on test items (`grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd`). One of its eight rules is to treat incentives as adversarial and make the target cognitive process unavoidable, since an app students can pass by pattern matching, shallow guessing or memorising repeated items is gameable and its signals are untrustworthy (`grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd`, `grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd`).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd` (178): “Any reward system attracts gaming. Students are not "bad" for doing this; they are optimizing incentives.”
- `grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd` (182-185): “Tanking placement tests to receive easier content * Clicking through explanations without reading * Guessing until correct * Pattern matching on test items rather than learning concepts”
- `grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd` (94): “**Make the target cognitive process unavoidable.** If students can succeed via pattern matching, shallow guessing strategies, or memorizing repeated items, the app is gameable and its signals are untrustworthy.”
- `grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd` (31): “7. **Prevent gaming.** Treat incentives as adversarial. Make the target cognitive process unavoidable.”
- `grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd` (35): “The independent text/task must require genuine rereading rather than a visible word-match.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (133): “- Closed-response items must require the target reasoning and must not be answerable by surface cues, keyword matching, option length, or test-wise elimination.”
- `g9/transformer/src/mechanics/evidence-hunt.js` (27): “- The claim must not copy five or more consecutive words from those lines.”
- `g9/transformer/src/mechanics/evidence-hunt.js` (46): “check("claim-no-copy", "The claim does not copy the line", run < 5, `the claim shares ${run} consecutive words with a keyed line`),”
- `g9/transformer/test/calibration/evidence-hunt.tapped-proves.json` (15): “Roderigo's line shares the words \"follow him\" but says nothing about Iago's purpose.”
- `grade3-reading/course-renderer/docs/rules/questions-and-assessment.md` (299-303): “**Rule.** The you-do passage must be long enough that the child cannot word-match their way to the answer. **Why.** "text passages must be sufficiently long to force genuine rereading rather than simple word matching."”
- `grade3-reading/course-renderer/docs/rules/questions-and-assessment.md` (308): “**Enforced.** Not applied.”
- `grade3-reading/ti-courseplans/scripts/lane-tools/drafts/m5-acceptance-rules.md` (30-31): “SPAN-GUARD: student span length `<= 3 x` the length of the best-matching keyed span (blocks highlight-everything; a whole-passage highlight can trivially satisfy SPAN-VALID).”
- `grade3-reading/ti-courseplans/scripts/lane-tools/drafts/m5-acceptance-rules.md` (29): “SPAN-VALID: `r* >= 0.50` -- the student span covers at least half of some keyed span.”
- `grade3-reading/ti-courseplans/scripts/lane-tools/drafts/m5-acceptance-rules.md` (6): “thresholds below are G3-uncalibrated proposals”
- `othello-course-renderer-draft/repo/docs/feedback/academics-review-2026-07-08.md` (31): “Whilst there were timers on text reading before the question appeared, it still seems possible to just click through, and where a "not so fast — read, read" nudge appeared it was non-blocking and skipped by clicking Next twice.”

Against: none found

<sub>criterion · integrity, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Match the gesture to the answer

Match an item's interaction to the shape of its answer, letting learners move what they must order.

A Grade 3 reading build shipped its ordering item as a dropdown of position numbers for each event, so a child on a tablet ordered a story clerically and nothing stopped two events both being numbered 3; the build's rules say the interaction taxed exactly the working memory the item exists to measure comprehension with. Reported live with a screenshot, it became drag-and-drop with a keyboard path, under a general rule: a tap is the honest gesture for picking, and an answer that is an arrangement needs things the learner can move. The conversion left the explicit check, the authored feedback, the two-attempt reveal and the scoring call untouched, because converting an interaction must not quietly convert the assessment.

Quoted:

- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (723): “because nothing stopped two events both being "3".”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (723-724): “The interaction taxed exactly the working memory the item exists to measure comprehension with.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (729): “Match the gesture to the shape of the answer.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (744): “A drag control needs a keyboard path in the same commit.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (750-751): “converting an interaction must not quietly convert the assessment.”

Against: none found

<sub>criterion · format, demand, accessibility · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Mirror or paraphrase on purpose

Decide on purpose whether a question repeats the text's wording or paraphrases it: a student who only matches words can answer the first but not the second.

A Grade 3 standards map splits finding stated information into two components, one where the question uses wording similar to the text and one where it paraphrases or uses different words. The second names the failure it catches: a child who can find answers only when the question's words exactly match the text, and fails when synonyms or rephrasing are used. A paraphrased question needs the student to match meaning, not words.

Quoted:

- `downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx` (sheet 'Standard components', cell D2): “Find explicitly stated information when the question uses similar wording to the text”
- `downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx` (sheet 'Standard components', cell D3): “Find explicitly stated information when the question paraphrases or uses different words”
- `downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx` (sheet 'Standard components', cell E3): “Child can only find answers when the question words exactly match the text. Fails when synonyms or rephrasing are used.”
- `g9/transformer/src/mechanics/evidence-hunt.js` (27): “The claim must not copy five or more consecutive words from those lines.”
- `g9/transformer/src/mechanics/evidence-hunt.js` (46): “check("claim-no-copy", "The claim does not copy the line", run < 5,”

Against: none found

<sub>criterion · wording, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Mix the kinds of demand in a set

Judge a question set as a whole: it mixes kinds of demand, such as literal, inferential and evaluative, and no one kind dominates. One reading generator's set check asks for at least two of three competency areas, with none in more than 70% of the questions.

A reading-question generator's quality control has a check that runs on the whole set rather than on single items: it fails a set that 'focuses too narrowly on a single competency' among literal comprehension, inferential thinking and evaluative analysis (`icloud-work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/ck_gen - prompts.json`). A pedagogy framework in the same project asks that questions move 'from basic recall to application to reasoning' (`icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md`). Both are adopted rules, with no measurement.

Quoted:

- `icloud-work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/ck_gen - prompts.json` (114): “Set should include questions from at least 2 of the 3 competency areas”
- `icloud-work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/ck_gen - prompts.json` (114): “No single competency should dominate (>70% of questions)”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (263): “Questions move from basic recall to application to reasoning, helping students strengthen understanding step by step.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (150): “The closing must include three distinct intellectual actions.”
- `grade3-reading/engine/reports/PETER-PAN-IMPROVEMENTS-2026-09-28.md` (33-34): “(all seven comprehension questions literal) is by design: the 2026-09-20 ruling keeps Peter Pan reading checks literal, with inference after the you-do.”

Against: A later run found counter-evidence (`grade3-reading/engine/reports/PETER-PAN-IMPROVEMENTS-2026-09-28.md`).

<sub>criterion · demand, sequence · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Name the text to connect to

Ask learners to connect an idea to another text only when the question can name a text they have read; otherwise ask for a prediction framed by the idea. One design judged a question asking for another story with the same idea four units too early, when any story counted.

It is the closing-questions design's rule of thumb for its third question (`grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt`). It was written against a closing question asking for another story where someone pretends to be someone they are not: at lesson 1 there is no knowledge web yet, so any story counts, no evidence is required and nothing returns to the text. The other form, a forward prediction framed by the idea, also serves as the next lesson's pre-reading question.

Quoted:

- `grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt` (102): “Rule of thumb: use Form B only when you can name the prior text inside the question. If you cannot name it, use Form A.”
- `grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt` (101): “At lesson 1 of the year there is no knowledge web yet, so any story counts, no evidence is required, and nothing returns to the text.”
- `othello-archive/src/content/retrieval.ts` (150): “hint assumes Macbeth (E2E minor 15); her text has no fallback, so this one is ours”
- `grade3-reading/artifacts/arc-audit/PRE-WEEKEND-SMOKE-2026-08-28.md` (68-70): “the Aladdin motivation claim ("a magician... pretended to be a long-lost uncle for one thing only, the lamp") matches L1's own Aladdin lesson content.”

Against: none found

<sub>criterion · format, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Near misses that fail for one reason

Teach and test a word or concept with surface-different examples that share its one deep feature, and near-miss non-examples that each fail for a single reason the feedback names. One vocabulary check shows three surface-different scenes with one shared feature, against three near-miss words that are each wrong for one reason.

A rebuilt lesson's vocabulary check shows three surface-different scenes that share one deep feature, with near-miss words each wrong for exactly one nameable reason, and its feedback names the mismatch; its parameter table says discrimination teaches a concept's edges. The physics misconception card applies the same idea to demonstrations: a law of motion is not to be shown only with stationary examples, but with moving ones too. The point is that the learner has to tell close meanings apart.

Quoted:

- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (77): “three surface-different scenes, one deep feature, with near-miss words — *careful, tired, polite* — each wrong for exactly one nameable reason”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (20): “Each wrong option differs by one nameable feature | Discrimination teaches a concept’s edges; each feedback names the one mismatch”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx` (93 (textutil text)): “Do NOT demonstrate Newton's third law only with stationary examples (book on table). Include MOVING examples (collisions, pushing off a wall on roller skates).”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (410): “Present examples and near-misses, prompting learners to discriminate between related meanings.”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (403): “## **What Makes a Good Vocabulary Question**”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/media-spec.md` (12): “Each film shows two positive instances and one boundary instance of its hinge.”
- `grade3-reading/.claude/skills/lesson-build/SKILL.md` (25-26): “one near-miss distractor”

Against: none found

<sub>criterion · distractors, stimulus, feedback · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Never require disclosing one's own relationships

No task may require students to disclose their own relationships.

The rule was written into a drama lesson on characters' mistaken beliefs about one another, beside a caution against treating manipulation as a healthy romantic solution. It has a single source and rests on a design decision, not on a measured problem.

Quoted:

- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/lesson-03.md` (41): “Also avoid treating manipulation as a healthy romantic solution. No response needs a student to disclose their own relationships.”

Against: none found

<sub>criterion · stem, accessibility · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### No clock unless speed counts

Put a clock on a test only when working against time is part of what it measures; on an untimed test a clock changes what is measured.

A reading assessment dropped timed sections because the test it mirrors is an untimed power test, where a clock changes the construct and rewards the rapid guessing that test penalizes (`grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md`). An audit of a reading course's positions lists 'comprehension is untimed; speed is a different construct' as borrowed from reading research, but names no study for its claim that time pressure triples the on-screen accuracy penalty (`grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md`). A clock fits, for example, when a test rehearses a timed exam.

Quoted:

- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md` (232): “| Timed sections | MAP is an untimed power test; a clock changes the construct and rewards the rapid-guessing MAP penalizes |”
- `grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md` (46): “Comprehension is untimed; speed is a different construct; time-pressure triples the on-screen accuracy penalty.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md` (97): “The gap appears only for expository text, grows under time pressure, and digital natives show no advantage.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md` (99): “Remove time pressure and ask for a self-check before showing answers.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md` (17): “| Timing | Untimed — power test, not speed test | NWEA published guidance [NWEA-VERIFIED] |”

Against: One course plan asks for a timer on a mock exam so that it mirrors the timed AP exam, which is why the rule allows a clock when a test rehearses a timed exam; that plan is not cited because its file's path carries a person's name.

<sub>criterion · format, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### No cue in the item itself

No surface feature may single out the key: keep options alike in length, grammar, register and scope. In one generated bank, 512 multiple-choice items failed a check for a key more than 20% longer than the other options.

Generated multiple-choice items were given to a model from another family with the passage withheld; it recovered the key for 62.7% of them, and the leaked items showed wrong options with absolute words, a key that was systematically the longest, wrong options that contradict each other, and keys that were the obvious balanced or textbook-sounding answer. Selection-from-the-text items leaked when the question or span wording signposted the right phrases, and in one unit they survived only with at least two competing spans of the same shape and a question the solver could not resolve without the text. Sorting items leaked when passage titles were the category labels, while neutral labels (Source A, Source B, Both) gave the construction that produced 700 certified items, and two-part answer-and-evidence items with elaborate options were left out because one part could solve the other. The key is never the longest, shortest, most specific, most hedged, odd one out or only option sharing a distinctive word with the stem or source. Use no absolute words or 'all/none of the above'. Check lengths in code, item by item and across the set, and move reasoning from the key into its feedback where it runs long.

Quoted:

- `grade3-reading/artifacts/LANE2_GENERATOR.md` (60): “1. **Absolute language tells** — wrong options use "always"/"never"/"all"/"completely" → flagged”
- `grade3-reading/artifacts/LANE2_GENERATOR.md` (61): “2. **Longest-option wins** — correct answer systematically longest (>20% margin)”
- `grade3-reading/artifacts/LANE2_GENERATOR.md` (64): “5. **Paired contradiction** — two wrong options logically contradict each other”
- `grade3-reading/artifacts/LANE2_GENERATOR.md` (68): “**512 MCQ items** fail `longest-option-tell` (>20% character length margin)”
- `grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md` (270): “- MCQ also leaked when one option was the obvious balanced or textbook-sounding answer.”
- `grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md` (272): “- Hot-text leaked when the question or span wording signposted the correct phrases.”
- `grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md` (66): “- hot-text survives only with >=2 same-shaped competitor spans AND a stem referent”
- `grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md` (69): “Arc-schema stems, paraphrase-matchable stems, and self-evident-cost spans all leaked.”
- `grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md` (16): “- Passage titles were never used as category labels.”
- `grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md` (315): “- Passage titles as categories: titles leak.”
- `grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md` (314): “- Sophisticated-option EBSR: Part A/Part B can self-solve.”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (77): “the correct option was systematically the longest”
- `grade3-reading/knowledge_bot/knowledge/kb-0068-g5-static-dataset-intake-2026-06-23.qmd` (117): “longest-option-tell: 626”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (78): “6 of 6 sampled two-part evidence items were blind-solvable, with Part B restating Part A”
- `grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd` (29): “it guessed from option-length and wording tells;”
- `grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd` (72): “Passage-dependent items can look "kid-gameable" under the wrong blind-solver and still be clean.”
- `grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd` (63-64): “The right option must not be the longest, the shortest, the odd one out, or the one that reuses the most words from the stem.”
- `grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd` (68-70): “`validate-blind-solve.mjs` fails the single shortest option, an answer that stands apart from a tightly clustered distractor set, the option that echoes the stem most, and a distractor set that is all eliminable as absolutes.”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (103): “re-read the stem with options covered. If you cannot answer from the stem alone, revise the stem.”
- `icloud-work/ML learnings/evaluation_methodology.md` (79): “- Answer choices aren't plausible distractors (one obvious correct answer)”
- `icloud-work/ML learnings/evaluation_methodology.md` (82): “An educational accuracy failure means the question isn't usable on an AP exam regardless of factual accuracy.”
- `icloud-work/ML learnings/what_is_ap_and_why_it_matters.md` (35): “**MCQ:** One stimulus (primary source), one question stem, four answer choices (A-D), exactly one correct answer, three plausible distractors.”
- `grade3-reading/knowledge_bot/knowledge/kb-0160-multiple-choice-questions-evidence-base.qmd` (78): “47% of students passed flawed items vs. 53% passing standard items”
- `grade3-reading/knowledge_bot/knowledge/kb-0160-multiple-choice-questions-evidence-base.qmd` (80): “Medical education context. Small sample of four exams from one institution.”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (175): “the very distractors that are best for diagnosis are also the most dangerous for false learning”
- `icloud-work/incept/sat-reading-generation/src/validator.py` (1391): “This helps prevent students from selecting the correct answer just based on its length.”
- `icloud-work/incept/sat-reading-generation/src/validator.py` (1451): “if correct_length > 1.1 * longest_distractor:”
- `icloud-work/incept/ap-benchmark-standalone/ap_benchmark/hard_fail/rules.py` (64): “r'all\s+of\s+the\s+above',”
- `icloud-work/incept/ap-benchmark-standalone/README.md` (95): “- **Absolute language** in distractors: "total", "complete", "immediate", "all", "never"”
- `icloud-work/incept/ap-benchmark-standalone/ap_benchmark/prompts/mcq.py` (20): “- Answer options should not give away the answer through grammar clues”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md` (53): “- Ensures consistent grammatical structure across all answer options”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md` (61): “- All options belong to the same conceptual category”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md` (66): “- Prevents correct answer from being notably more specific or vague than distractors”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md` (74): “- Prevents patterns where correct answer is consistently longest/shortest”
- `icloud-work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md` (406): “- Issue: One option (“+”) is non-parallel and implausible for a comparison task, reducing distractor quality.”
- `icloud-work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/ck_gen - prompts.json` (12): “**SPECIAL CONSTRAINT**: The correct answer MUST NEVER be the longest option.”
- `icloud-work/evaluator/ap_benchmark/prompts/mcq.py` (13): “- All options should be roughly similar in length”
- `icloud-work/evaluator/ap_benchmark/prompts/mcq.py` (20): “- Answer options should not give away the answer through grammar clues”
- `icloud-work/evaluator/ap_benchmark/hard_fail/rules.py` (64): “r'all\s+of\s+the\s+above',”
- `icloud-work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py` (191): “Avoid reusing distinctive nouns, verbs, or historical labels from the stimulus in only the correct option.”
- `icloud-work/k_12_social_studies/python/docs/EVALUATION-RESULTS-2026-02-23.md` (34): “**Frequency:** 191 questions (35% of all generated)”
- `icloud-work/k_12_social_studies/docs/archive/OPENCLAW_HUMAN_REVIEW.md` (34): “Option A ("immediate collapse") is a weak distractor — students could eliminate it by word choice alone”
- `icloud-work/ap-social-studies-generator/docs/analysis/best_practices.md` (54): “| Absolute words (always, never, all, none) | Too easily eliminated |”
- `icloud-work/ap-social-studies-generator/docs/analysis/best_practices.md` (57): “| Options significantly longer/shorter than key | Provides visual cues |”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/social_studies_evaluation.txt` (16): “When the stem names a region and the correct answer is the only option that also names that region, students can identify the correct answer by simple keyword matching rather than subject knowledge.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/match_evaluation.txt` (411): “- **Syntactic giveaway pattern**: Items in the same category share a distinctive grammatical structure that items in other categories do not — allowing a student to sort by syntax alone.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt` (73-75): “A student should not be able to identify the key from the task line alone. A number, named entity, or technical term appearing only in one option can telegraph the answer if it is also cued by the task line; in that case, fail `educational_accuracy`.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (597): “- Length imbalance reveals answer”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/match_evaluation.txt` (392): “- Also check tonal giveaway: if items in one category consistently use negative language (failure, decline, erosion, instability) while another uses neutral or positive language → FAIL.”
- `APinceptbench/docs/AP_GENERATOR_SPEC.md` (29): “**Rules**: 4 options, 1 correct, plausible distractors, parallel structure, no absolutes”
- `grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md` (34): “Closed-response items must require the target reasoning and must not be answerable by surface cues, keyword matching, option length, or test-wise elimination.”
- `APinceptbench/ap_benchmark/hard_fail/rules.py` (97): “description="Distractor contains absolute language (total, complete, never, etc.)",”
- `APinceptbench/ap_benchmark/hard_fail/rules.py` (104): “description="Correct answer contains absolute language",”
- `APinceptbench/ap_benchmark/hard_fail/checker.py` (215): “failed=len(triggered_rules) > 0,”
- `APinceptbench/ap_benchmark/prompts/official_ap_prompts.py` (34): “5. Avoid absolute language ("always", "never", "all", "none") unless historically accurate”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (77): “79% of correct answers in a generated course sat at option position A, and the correct option was systematically the longest”
- `grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd` (64-65): “it is obvious what the right answer is from the length and phrasing of the answer”
- `grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd` (67-68): “fails an answer that is the single longest option (code comment: "anti-gaming rule: length must never be the tell")”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (133): “Closed-response items must require the target reasoning and must not be answerable by surface cues, keyword matching, option length, or test-wise elimination.”
- `grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd` (76-77): “which checks the *tells* a blind solver would exploit rather than actually scoring the item blind”
- `grade3-reading/knowledge_bot/knowledge/kb-0223-g3-review-rounds-and-tooling-2026-09-18-to-21.qmd` (24): “option 2 reworded from a *the*-opener to match the wh-form distractors”
- `grade3-reading/knowledge_bot/knowledge/kb-0223-g3-review-rounds-and-tooling-2026-09-18-to-21.qmd` (30-31): “two absurd distractors replaced with near-misses a confused child could plausibly pick”
- `grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd` (49-50): “The audit says 10 MCQs were over-flagged under the old blind-solver and correctly certified after the re-baseline.”
- `grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd` (56): “correct_is_longest”
- `grade3-reading/artifacts/alpha-read-packager/LLM_GENERATION_BOUNDARY.md` (34): “At course scale the tell is endemic: 289/794 keyed MCQs have the correct option strictly longest (~36%).”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md` (16): “| Correct answer is the longest option | 28% | n/a | Length cue alone recovers the key |”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/L5-REVIEW-GAPS-2026-09-17.md` (8): “the first wording made the correct option the single longest (95 vs 91) — validator caught it”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/BUILD-SPEC-batch.md` (6): “an mcq key is never the longest/shortest”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md` (8): “"The answer is the only option not shaped like a question"”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md` (10): “"The correct sentence is the only one that does not use 'because'"”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md` (9): “key is the only option without an article”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/BUILD-SPEC-batch.md` (6): “options open in parallel form (no odd article/opener)”
- `grade3-reading/artifacts/alpha-read-packager/FIX_LIST.md` (92): “Student discriminates by sentence-TYPE, not support-relationship. Hottext variants leak because the prompt reuses the key's distinctive content words.”
- `grade3-reading/artifacts/alpha-read-packager/FIX_LIST.md` (108): “The verbatim-keyword sentence (h9) is a DISTRACTOR; the key (h8) shares no prompt keywords — keyword-matching points AWAY from the key”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (79): “Key is the only option that repeats the stem's verb ('find'→'found')”
- `grade3-reading/artifacts/alpha-read-packager/FIX_LIST.md` (102): “`mainidea-earthworm-mcq-05` leaks instead via the "pick the broadest option" main-idea heuristic (its foils are all true narrow details).”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (66): “79% of correct answers in a generated course sat at option position A, and the correct option was systematically the longest”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (65-66): “**No surface tells.** Length- and structure-match the contending options. The key must … NOT be the longest, the most specific, the most hedged, or the only grammatical fit.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (67-68): “the **longest-option-tell self-check**: if the key is the longest option, rewrite until … key length is at or below the median option length.”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (101-102): “The evaluators do not check the "correct answer is longest" tell. Build per-item and per-course length-parity census over correct vs distractor options.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (86-87): “**msq** — exactly one defensible correct SET; the keyed set must NOT be "the two/three … longest"; include at least one live-trap distractor”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md` (51): “Form-level answer-position, option-length, duplicate, enemy-item, and blueprint reports.”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (165-166): “**79% of correct answers sat at position A and the key was systematically the longest**”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (149-151): “IB does **not** check the "correct answer is the longest option" tell”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (156-157): “per-item key-vs-distractor character and word length; per-lesson max same-key run. Stdlib-only, no solver, no secret.”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (172): “key longest by word count 12 v 11 but not by characters 61 v 62”
- `ti-courseplans-audit/docs/instruction-quality-standard.md` (130-131): “**Length parity**: verdict in the option, mechanism in per-option feedback — the key is never systematically longest.”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md` (19): “Options parallel in length, grammar, register; the key is not systematically longest/most-hedged”
- `grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd` (91-92): “STEM-LEAK (no distinctive content word may sit in both the stem and only the correct option)”
- `grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd` (63): “MCQ correct answer never longest”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx` (10 (textutil text)): “Rule 2 — Multiple-choice discipline. The correct option rotates across A/B/C/D; all four options are the same length and register; each item carries one deliberate misconception distractor.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 2. Should We Save the Rainforests - WEIGH - Lesson Design.docx` (12 (textutil text)): “Correct answer rotates A/B/C/D; options length-matched; correct is never the longest; exactly one misconception distractor each.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 6. Life in Water - CONNECT - Lesson Design.docx` (10 (textutil text)): “options are matched in length, and distractors are as long as the correct answer or longer, so the correct one never stands out by length.”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (36): “≥4 plausible options; no yes/no; no stem echo; key never the longest | Guessable items measure test-wiseness, not comprehension”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (69): “a few distractors carry small length pads so the key is never the longest option”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx` (sheet 'V7.0 Executive Summary', cell A75): “Two fixes applied: em-dashes removed, MCQ lengths balanced.”
- `grade3-reading/ti-courseplans/docs/course-formula-agents.md` (225): “the correct option being consistently the longest/most-detailed, and distractors using absolute/absurd language”
- `grade3-reading/ti-courseplans/docs/course-formula-agents.md` (225): “the rubric gate passed 6/6 such items (g4 F1)”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (214): “The key is the only option of its grammatical kind”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (215): “Position shuffling does not remove this”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (217-218): “An option that is not a grammatical answer to the stem is eliminable on syntax alone”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (220-221): “no option uniquely carrying a hedge or a dash (see A1), consistent grammatical form across all four.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (2002): “read the stem, cover the options, and ask whether a knowledgeable student could formulate an answer”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1996): “"All of the above" and "None of the above" should never be used”
- `shadow-content-eval/SKILL.md` (65): “a content word from the stem appears in the correct option **and in no distractor** — word-matching finds the answer without comprehension.”
- `shadow-content-eval/SKILL.md` (343-347): “The correct option being the only one that is specific, the only one naming a character, the only one that is semantically *different in kind* from the rest.”
- `shadow-content-eval/reports/G3-U2-L1-review.md` (106): “- "Instead of flowers" in the key names and rejects that distractor, so the two options argue with each other and the student can pick without reading.”
- `shadow-content-eval/reports/G3-U1-L13-review.md` (100): “*"The mood of the tale's closing part"* is the only abstract option. The others are concrete details (the tunnel's history, the number of weasels, the cell).”
- `shadow-bench/` (commit ef4a069) (5-6): “Two test-wise answer-key tells were unchecked in the lesson bundle (the course has answer_balance; the lesson bundle had nothing):”
- `shadow-bench/` (commit ef4a069) (7-8): “- G3 correct-is-longest: the correct option being the unique longest lets a student guess by length.”
- `shadow-bench/` (commit ef4a069) (15-17): “Report-only at lesson scale — a single lesson has too few items to gate reliably; score-gating happens course-side (#1104) where item counts are large”
- `shadow-bench/` (commit ef4a069) (19-20): “- tools/item_tells.py: pure functions + is_tell/is_skewed thresholds (>=4 items & >60% for length; >=8 items & >50% for position).”
- `aptraining-local/den-of-ideation/reports/cell_family_archetype_scout_20260523.md` (84): “Answer leakage: direct MCQ can become trivial when the stem copies the correct option's nouns.”
- `aptraining-local/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md` (19): “answer phrase leakage from stimulus to correct option;”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md` (227): “no copied answer phrase”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-22T1905Z_hidden_acceptance_repair_status.md` (75): “The IB critique is consistent: factually sound, but too many question-level failures due answer leaks, weak distractors, or insufficient AP-level cognitive demand.”
- `g9/transformer/src/mechanics/compare-paragraphs.js` (51): “Math.max(...wc) <= 1.6 * Math.min(...wc)”
- `g9/transformer/src/mechanics/compare-paragraphs.js` (51): “Length does not give the stronger one away”
- `g9/transformer/src/mechanics/compare-paragraphs.js` (23): “write two short paragraphs (50 to 90 words each)”
- `g9/transformer/src/mechanics/quick-check.js` (55): “Math.max(...lens) <= 2.2 * Math.min(...lens)”
- `g9/transformer/src/mechanics/quick-check.js` (55): “No option stands out by length”
- `g9/transformer/src/mechanics/quick-check.js` (24): “Keep the options a similar length.”
- `g9/transformer/src/mechanics/quick-check.js` (55): “No option stands out by length", Math.max(...lens) <= 2.2 * Math.min(...lens)”
- `g9/transformer/src/mechanics/quick-check.js` (23-24): “- Exactly three options. Exactly one is right given the text; the other two are tempting to a skimmer but the text rules them out. Keep the options a similar length.”
- `g9/transformer/src/mechanics/quick-check.js` (55): “check("length-balanced", "No option stands out by length", Math.max(...lens) <= 2.2 * Math.min(...lens), "one option is much longer than the others"),”
- `g9/transformer/src/mechanics/quick-check.js` (24): “rules them out. Keep the options a similar length.”
- `g9-transformer-runs/blocks/5722a3741161394e.json` (49): “"A modern political appointment.",”
- `g9-transformer-runs/blocks/5722a3741161394e.json` (50): “An absolute claim of supreme power and absolute authority over all other rulers.”
- `g9-transformer-runs/blocks/5722a3741161394e.json` (51): “"A temporary rank given during wartime."”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “whether only the key echoes the stem”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “Port three content-eval tests into src/mechanics/util.js as code checks:”
- `grade3-engine-vendor/lesson-content-eval/SKILL.md` (53): “word-matching finds the answer without comprehension”
- `grade3-engine-vendor/lesson-content-eval/SKILL.md` (41): “one option breaks the others' grammatical form — visible odd-one-out”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “content-eval's margins were tuned on Grade 3 items with four options.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/final-u9-review.json` (72): “Warmth check contrasts amends with danger, fighting and crime, so the correct option follows from general positive tone rather than close reading.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/final-u9-review.json` (73): “Use related alternative grounds such as the goodbye alone, a presumed absence of mistakes, the mere fact it is the last speech, versus the promise of amends.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/README.md` (121): “L7’s model why-check uses overly remote distractors, so it is instruction with weak diagnostic value and must not count as independent mastery evidence.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/INTEGRATION-LESSONS.md` (17): “Question shape checks passed one screen but failed another character-based rule”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/INTEGRATION-LESSONS.md` (17): “Run the actual release validator on the integrated artifact, then read whether alternatives remain plausible. Do not pad distractors simply to satisfy length.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/CURRENT-HANDOFF.md` (17): “Silent CFUs in `lesson-video-scripts.json` were revised against real contract rules, including character lengths, script overlap, proper-noun cues and first-key position.”
- `grade3-reading/_archive/2026-08-13-consolidation/redteam-g3-round3-report-and-evidence.tar.gz` (RED_TEAM_ROUND3.md inside it) (195-197): “- 9/48 EBSRs have Part-A-answer → correct-Part-B overlap coefficient `>=0.50`; the key is the unique highest-overlap option in all nine. - Across all 48, the correct Part B is the unique highest lexical match in 26.”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md` (238-240): “a content evaluator run over L4–L7 (83 items, 126 mechanical signals, 9 high) with ONE confirmed defect — L6 p13 / L7 p13 `item-5-rail-hinge`: the keyed option is the only one repeating the stem's "what a character did" (stem-echo leak).”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-main-checkout-jul-work.patch` (20736): “| **AOTA / NOTA / negative stem** | "all/none of the above", "which is NOT" | hard fail |”
- `grade3-reading/_archive/2026-08-13-consolidation/redteam-g3-round3-report-and-evidence.tar.gz` (RED_TEAM_ROUND3.md inside it) (56): “| No T/F, AOTA, NOTA | PASS | 0 True/False items or option sets; 0 All/None-of-the-above; 0 classic EXCEPT/least/not-true exclusion stems. |”
- `grade3-reading/artifacts/qc-2026-09-30-staging/FINDINGS.md` (80): “**M12. The p3b vocabulary check can be answered by tone alone.** The options are friendly, **menacing**, gentle, caring: the key is the only unkind word.”
- `grade3-reading/artifacts/qc-2026-09-29-staging/ADJUDICATION-pr662.md` (13): “Added a plausible `-ing` wrong option to each. The keyed *enchanting* and *menacing* are no longer the only options with that form.”
- `grade3-reading/artifacts/qc-2026-09-29-staging/ADJUDICATION-pr662.md` (13): “Three high `PARALLEL-LEAD` signals across L4/L5 fell to zero after this and the next repair.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (121-125): “The same gate catches six anti-gaming defects at once: a key that is the single shortest option (x2), a key that echoes the stem's own wording, an evidence question built on only two candidate sentences (a coin flip), a correct answer whose own feedback never confirms it, and a key one character shorter than its nearest distractor.”
- `grade3-reading/artifacts/qc-2026-09-30-staging/FINDINGS.md` (116): “**M19. The p15b Search key echoes the question.**”
- `grade3-reading/artifacts/qc-2026-09-30-staging/FINDINGS.md` (117): “"Where Peter whispers jobs through the hatch while the pirates sleep" is the only option with "sleep" and "jobs".”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/item-types/mcq.md` (9-10): “No meta-options: never "all of the above," "none of the above," "both A and B."”
- `grade3-reading/course-renderer/authoring/pipeline/gates/deterministic.mjs` (337): “no All/None-of-the-above style option, which is answerable without reading”
- `grade3-reading/course-renderer/content/lesson-plans/g3-u2-l1.json` (975): “(4) p6's puppy and bus were nonsense rather than misconceptions, and the key was the only plant in a plants lesson; the key is now a lizard and one distractor is a tree, so topic priming misleads instead of helping.”
- `grade3-reading/course-renderer/content/lesson-plans/g3-u2-l1.json` (975): “(2) p10's three distractors were all about the plant, so the stem's own words picked the key; two are now about other living things and wrong on the science, and the three wrong-option feedbacks no longer point at breathing.”
- `grade3-reading/course-renderer/content/lesson-plans/g3-u2-l1.json` (975): “(3) p8's distractors were wrong on their quantifiers (two opened 'Only'), so elimination found the inclusive key; they are now wrong on the facts.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md` (14): “"All/none of the above" never appear”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/generation-contract.md inside it) (88-90): “**"All of the above," "none of the above," and negative stems** ("which is NOT…") are also **banned outright** — they test test-taking convention, not the target skill.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/ASSESSMENT-QUALITY-MEMO.md inside it) (41): “**No All-of-the-above / None-of-the-above:** 0 of 96.”
- `othello-course-renderer-draft/repo/authoring/inputs/prompt-packs/reading-g3/item-types/mcq.md` (9-10): “No meta-options: never "all of the above," "none of the above," "both A and B."”
- `othello-course-renderer-draft/repo/authoring/inputs/prompt-packs/reading-g3/subjects/reading.md` (44-46): “The usage checks ask which sentence uses the word correctly, with distractor sentences whose feeling or meaning is wrong, never sentences that give the answer away by valence alone.”
- `othello-course-renderer-draft/repo/authoring/inputs/prompt-packs/reading-g3/judge/distractor-quality.md` (15-16): “an option is answerable from the stem alone, without having read the text (general knowledge, valence, or grammar gives it away).”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (62): “D5.3 (no AOTA/NOTA): scanned all 13 MCQ + 5 dialogue-branch option sets — no 'all/none of the above' option anywhere.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (133-136): “the odd-one-out ban is not limited to grammatical kind — `checkOptionStyle` in `validate-contracts.mjs` now fails the build when the key is the sole option carrying a proper noun, the sole option carrying a number, the sole option carrying a quoted phrase, or every distractor shares an opener the key does not.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (136-140): “The length tell is checked against the single longest/shortest distractor, not an average: the key fails if it is more than 1.25x the length of the longest distractor, OR less than 1/1.25 the length of the shortest distractor. Any of these mechanical surface tells lets a child eliminate by form rather than comprehension.”
- `grade3-reading/engine/reports/PETER-PAN-IMPROVEMENTS-2026-09-28.md` (7): “The taught word is pickable by its shape (2 items) — highest value”
- `grade3-reading/engine/reports/PETER-PAN-IMPROVEMENTS-2026-09-28.md` (8): “the key is the only `-ing` form.”
- `grade3-reading/engine/reports/PETER-PAN-IMPROVEMENTS-2026-09-28.md` (10): “A child can pass the vocabulary check without knowing the word.”
- `grade3-reading/engine/reports/PETER-PAN-IMPROVEMENTS-2026-09-28.md` (19): “Word-matching finds the answer (2 items)”
- `grade3-reading/engine/reports/PETER-PAN-IMPROVEMENTS-2026-09-28.md` (20): “only the key repeats *character* and *did*.”
- `grade3-reading/engine/reports/PETER-PAN-IMPROVEMENTS-2026-09-28.md` (22): “Fix: reword the key, or put the echoed word in a distractor.”
- `grade3-reading/engine/reports/PETER-PAN-IMPROVEMENTS-2026-09-28.md` (4): “Every item below was re-read in `grade-3.json` before being listed.”
- `grade3-reading/engine/reports/PETER-PAN-IMPROVEMENTS-2026-09-28.md` (5): “Nothing here has been changed; this is a proposal list.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (121-123): “The same gate catches six anti-gaming defects at once: a key that is the single shortest option (x2), a key that echoes the stem's own wording”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (559-561): “is content-based and shares no content words with the key sentence (line 472); the positional cue exists only in `hint_after_2` (line 482); all four candidate sentences share vocabulary so no lexical shortcut discriminates.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (563-564): “must preserve this independence property in the locate step.”
- `grade3-reading/.claude/skills/one-perfect-lesson/SKILL.md` (49-50): “evidence as content never position”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/schema-video.md` (47): “All four choices have five words. Character lengths are 33, 33, 36 and 28; the key is neither a unique longest nor a unique shortest option.”
- `grade3-reading/_archive/2026-08-13-consolidation/redteam-g3-round3-report-and-evidence.tar.gz` (RED_TEAM_ROUND3.md inside it) (198-200): “- 14/192 single-key MCQ/EBSR surfaces fail the prior Round-2 correct-is-longest rule (key at least 15 characters or 20% longer than the largest distractor): 5 MCQ, 6 EBSR-A, 3 EBSR-B.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/UNIT.md` (404): “A child who reads nothing gets it right.”
- `grade3-reading/course-renderer/content/lesson-plans/g3-u2-l1.json` (728): “the doc's wording made the key the single shortest option”
- `grade3-reading/course-renderer/docs/video/u1-script-critique.md` (30-31): “The proposed closing checkpoint, the item the whole revision exists to fix, fails `scripts/validate-blind-solve.mjs` as written and would red the build.”
- `g9/player/design/ARCHIVIST-DESIGN.md` (341): “`tapPulse` scaling of the correct option before the pupil taps it (the answer is literally pulsing)”
- `othello-archive/src/scene/Moment.tsx` (49): “(a 'choose' names every figure on stage: the student chooses by who they are, never by a ring)”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (65): “checked all 13 MCQ option sets for register/length/grammar parity — consistently parallel”
- `grade3-reading/engine/reports/PETER-PAN-IMPROVEMENTS-2026-09-28.md` (24-25): “Mild shape tells (3 items, cheap) … the key is the only option with a definite article”
- `grade3-reading/engine/reports/PETER-PAN-IMPROVEMENTS-2026-09-28.md` (29-30): “Option-length spread (11 items) — style, not a defect … Lengths span 44–91% of the mean on those items.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/skill/SKILL.md` (275): “**length-parity keys** (the correct option never systematically longest), one-difference”

Against: A length cue matters only where length can be exploited: a review left a sorting item's uniquely short extra alone, because extras are not keyed to prompts (`grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-04-R16.md`, line 52). Removing cues does not fix leaks whose cause is the passage: for the same generator's items, the report judged the leak not fixable with option-length patches (`grade3-reading/artifacts/LANE2_GENERATOR.md`, line 31). a blind solver that guessed from option length and wording flagged items that needed the passage and were clean, so a solver's guess alone does not prove a cue. The measured effect comes from four exams at one institution and covers item-writing flaws of every kind; the AP rule is a stated criterion with no count of failures; and a research summary warns that the most plausible wrong options are also the likeliest to be learned as true when no feedback follows. The same generator's structure judge is told that "Sentence length alone (unless extreme like a phrase vs. paragraph)" is not a structural difference (`icloud-work/incept/sat-reading-generation/sat-prompts.json`, line 80), leaving length to the code check. A grades 9-10 reading generator makes the cue a fixed rule, "The correct answer MUST NEVER be the longest option." (`icloud-work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/ck_gen - prompts.json`, line 12, and again on lines 6, 18, 48 and 54); a key that is never the longest is a pattern of its own. The absolute-language list also catches ordinary words such as only, so a word filter can fail sound options (`icloud-work/evaluator/ap_benchmark/hard_fail/rules.py`, line 38). And the pipeline's fixed key order, 'Use locked answer keys A, C, and B in that order.' (`icloud-work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py`, line 201), balances each set but repeats one position pattern across every set, which is itself a surface cue. A word ban is blunt: one validation rule fails a true statement for its absolute words (`icloud-work/ap-social-studies-generator/docs/validation_rules.md`). The writer's banned-word list had no enforcement, absolute language still appeared in 35% of items, and no rate after enforcement is recorded (`icloud-work/k_12_social_studies/python/improvement_plan_prompts.md`). The length cue rests on guidance, not on a measured case. Ordinary topic-word overlap is acceptable (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt`, lines 75-76), and a single echo of a category label is borderline unless it is the dominant word in the label (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/match_evaluation.txt`, line 379). A fixed word list is blunt: the AP benchmark's check before the judge fails an item when any option, distractor or key, contains words such as "total", "complete" or "never", while the judge's own rule allows absolutes when they are historically accurate. The validators look for the tells a blind solver would exploit rather than solving the item blind, which the same file says needs a model. A recalibrated blind solver certified 10 questions an older solver had over-flagged, and the leak vectors behind those flags included the right option being the longest. In a select-all item the length cue is confounded: picking the two longest options gave one right and one wrong (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md`, line 102). An automated shape flag can be a false positive, kept on record so the raw score is not taken at face value (`grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md`, line 14). a solver audit certified as clean ten questions that an over-eager solver had flagged, partly by picking the longest option (`grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd`, lines 49-63). Most mechanical form flags were false positives once read: "The options are parallel; they only open with different words." (`shadow-content-eval/reports/G3-U1-L14-review.md`, line 112); "in none of them is the correct option the longest or shortest outlier in a way that gives it away." (`shadow-content-eval/reports/G3-U1-L11-review.md`, line 106). The thresholds were set, not measured, and neither the tell's rate in real items nor its effect on students is on record. Copying is not always a cue: a validator's first version "over-blocked known passing rows because InceptBench tolerates some source-referential wording" (aptraining-local/den-of-ideation/experiments/b0035_mcqset_stage_validator/RESULTS.md, line 24), and the records read give no measured effect of the check on its own. A later run found counter-evidence (`grade3-reading/engine/reports/PETER-PAN-IMPROVEMENTS-2026-09-28.md`).

<sub>criterion · options, integrity, distractors, stem · universal · from ap, g3, research · measured · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### No false premise in the question

Every premise a question's wording takes for granted must be true of the text, because a question can presuppose something the text contradicts.

A quality pass on a Grade 9 unit's knowledge base found a learning question that spoke of one character's refusal to follow another, although in the text he does follow him, for his own ends (`g9/sources/1. Act 1 - Knowledge Base - Overview.csv`, line 145). It reworded the question to speak of his claim to follow and marked the case fixed.

Quoted:

- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (145): “Iago's refusal to 'follow' Othello"": Iago does follow Othello, but for himself. Reworded to ""Iago's claim to 'follow' Othello"". Fixed.”

Against: none found

<sub>criterion · stem, integrity, wording · universal · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### No local knowledge the course doesn't teach

Keep an item solvable without local or cultural knowledge the course doesn't teach, in a neutral everyday setting unless the curriculum calls for a particular one.

A question benchmark's localization check passes an item only when it is solvable without local cultural knowledge, and fails one that needs such knowledge to understand or solve it (`icloud-work/incept/inceptbench/src/inceptbench/prompts/question/closed_ended_evaluation.txt`, lines 571 and 581). Its specification for item sets asks for neutral, universal contexts and no content that needs local cultural knowledge, and lists culturally specific scenarios, from defaulting to US-centric contexts, among its ten common failure modes, with universal settings as the fix (`icloud-work/incept/inceptbench/docs/MCQ_SET_PASS_SPEC.md`, lines 284-285 and 556). The evidence is a specification and a rubric, not a measured effect. Use at most one region-specific reference, write in the language of instruction, and fall back to neutral wording when these can't be met.

Quoted:

- `icloud-work/incept/inceptbench/docs/MCQ_SET_PASS_SPEC.md` (284): “- Neutral, universal contexts (classroom, shopping, measurements, nature)”
- `icloud-work/incept/inceptbench/docs/MCQ_SET_PASS_SPEC.md` (285): “- No content requiring local cultural knowledge to solve”
- `icloud-work/incept/inceptbench/docs/MCQ_SET_PASS_SPEC.md` (556): “| 8 | Culturally specific scenarios | localization_quality | Default to US-centric contexts | Use universal settings |”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (571): “- Problems solvable without local cultural knowledge”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (581): “- Requires local cultural knowledge to understand/solve”
- `icloud-work/incept/inceptbench/docs/MCQ_SET_PASS_SPEC.md` (303): “- Holidays (Christmas, Diwali, etc.) unless curriculum requires”
- `icloud-work/inceptbench/src/inceptbench/agents/localization_guidelines.json` (29): “**Universal solvability**: Problems should be solvable without requiring local cultural knowledge.”
- `icloud-work/inceptbench/src/inceptbench/agents/localization_guidelines.json` (102): “**Regional Reference Limit**: Use at most one explicit, region-specific object or concept.”
- `icloud-work/inceptbench/src/inceptbench/agents/localization_guidelines.json` (107): “**Instruction-Aligned Language**: Only switch to the student's regional/native language if instruction for that student actually uses that language.”
- `icloud-work/inceptbench/src/inceptbench/agents/localization_guidelines.json` (82): “**Neutral fallback**: If a guardrail can't be satisfied, the output should pick the neutral fallback instead of improvising.”
- `icloud-work/inceptbench/docs/legacy/EVALUATORS.md` (244): “These rules reject caricatures (e.g., stacking “camel + dates + desert”) and prevent switching languages unless instruction requires it.”
- `icloud-work/inceptbench/docs/legacy/EVALUATORS.md` (246): “Every rule in `localization_guidelines.json` is evaluated via its own micro-prompt that returns `score: 1` (pass) or `score: 0` (fail).”

Against: The curriculum can call for a particular context: the specification avoids holidays such as Christmas or Diwali only "unless curriculum requires" (`icloud-work/incept/inceptbench/docs/MCQ_SET_PASS_SPEC.md`, line 303).

<sub>criterion · accessibility, alignment · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### No wrong option alone carries the taught words

No wrong option may be the only one carrying the words the teaching just made prominent, because it pulls the learners who listened hardest toward the wrong answer.

A rewrite of a unit film's narration made two words of a definition prominent in the lines around the word being taught, while the film's closing checkpoint still keyed an older definition and one wrong option carried that vocabulary. The film's plan found the item still answerable but steering the child who listened hardest toward that wrong option, and fixed it by putting the word in the key as well, which removes the pull rather than relying on the child to discount it (`grade3-reading/course-renderer/docs/video/u1-script-and-visual-plan.md`, lines 314-325).

Quoted:

- `grade3-reading/course-renderer/docs/video/u1-script-and-visual-plan.md` (321-325): “But the narration now makes "poem" and "sung" salient in the two lines around the word epic, so the child who listened hardest is steered toward the only option carrying that vocabulary, which is the wrong direction. The fix below puts "poem" in the key as well, which removes the pull rather than relying on the child to discount it.”

Against: none found

<sub>criterion · distractors, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### No wrong option true in another version

Don't build a wrong option from a detail that is true in another version or retelling of the story, because it penalises the learner who reads widely.

A research note for a unit on a widely retold epic surveyed the versions children meet, among them a television series, a new film and short retellings, and warned against a wrong option built from a detail one of them adds, such as the guinea pigs of one television version (`grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md`, lines 521-524). The note labels the warning its author's opinion; the lesson plan lists it among its integrity rules, since a distractor true elsewhere punishes the child who reads widely, the opposite of what a knowledge-rich course should do (`grade3-reading/course-renderer/content/lesson-plans/g4-u1-l3.json`, line 309).

Quoted:

- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (521): “One more, and it is my opinion.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (522-524): “A distractor that is true in another canon punishes the child who reads widely, which is the opposite of what a knowledge-rich course should do.”
- `grade3-reading/course-renderer/content/lesson-plans/g4-u1-l3.json` (309): “No distractor built from another canon's detail, the guinea pigs of the television Circe being the specific example. A distractor that is true elsewhere punishes the child who reads widely, which is the opposite of what a knowledge-rich course should do.”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l3.json` (309): “No distractor built from another canon's detail”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l3.json` (309): “A distractor that is true elsewhere punishes the child who reads widely, which is the opposite of what a knowledge-rich course should do.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (522-524): “A distractor that is true in another canon punishes the child who reads widely, which is the opposite of what a knowledge-rich course should do.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (518): “every option must be quotable from our passage”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l2-the-cyclops.md` (790-791): “every distractor should be true or nearly true of this passage and wrong only on relevance.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (521): “One more, and it is my opinion.”

Against: The same note counts one film-derived confusion as fair game: "a child who has picked up the film secondhand may attach the forgetting flower to the woman who kept Odysseus rather than to a landfall his crew made, which is a misconception worth a distractor rather than a worry" (`grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md`, lines 495-498), a point the lesson plan repeats (`grade3-reading/course-renderer/content/lesson-plans/g4-u1-l3.json`, line 594), though the note could not verify whether the film itself moves the flower (lines 493-495). The brief offered the rule as opinion: "One more, and it is my opinion." (`othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md`, line 521).

<sub>criterion · distractors, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### No yes-or-no questions

Never ask a question a student can answer yes or no or by a two-way pick: ask what or how, and give choice questions several plausible options. A blocking checklist row requires 4 or more plausible options on every choice question and zero two-option coin flips.

A content review of a reading lesson asked that a yes-or-no question be dropped altogether, even though the app said it couldn't be answered yes or no, and recast as a what question (`grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt`). The course's QC checklist makes it a blocking row: every choice question has 4 or more plausible options and there are no two-option coin flips (`grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md`, row B8).

Quoted:

- `grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt` (25): “Even though the app says you can't just answer it yes or no, we should just avoid these questions altogether.”
- `grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md` (50): “Every MCQ has ≥4 plausible options; zero two-option coin flips”
- `g9/transformer/src/mechanics/debate.js` (46): “It is an open question (How far, To what extent, How, Why or What), never one answered yes or no.”
- `g9/transformer/src/question.js` (11): “/^(is|are|does|do|did|can|could|would|will|was|were|has|have|had|should)”
- `g9/transformer/src/question.js` (30): “map((q) => String(q).trim()).filter(wellFormed)”
- `g9/transformer/test/mechanics.test.mjs` (124): “find((c) => c.id === "question-open").ok, false”
- `g9/transformer/v02/QA.md` (90-91): “the writer drafts three, code keeps the open ones, Jev keeps the first answerable from the text”
- `g9/transformer/test/server.test.mjs` (94): “the yes-or-no draft is dropped”
- `g9/transformer/test/mechanics.test.mjs` (112): “code checks hold a gap that gives its word away, a rebuild that does not make its sentence, a phrase not in the question, a yes-or-no debate and a hint that leaks”
- `g9/transformer/src/question.js` (11): “const YES_NO = /^(is|are|does|do|did|can|could|would|will|was|were|has|have|had|should)\b/i;”
- `g9/transformer/src/mechanics/open-check.js` (35): “answers in a sentence of their own after one careful reading. Not a yes or no question, and not a choice.”
- `g9/transformer/test/mechanics.test.mjs` (124): “assert.equal(db.codeChecks(db.normalize({ ...FIX.debate, question: "Can we sympathise with Iago?" }, ctx), ctx).find((c) => c.id === "question-open").ok, false);”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (140): “TASK 3 evaluate (""X or Y?"").”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (147): “is descriptive, not ""X or Y"".”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (192): “"Is Iago more dangerous because he hides his feelings from Othello, or because he reveals them to the audience? Justify your view."”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/CODEX-HISTORY-EVERYTHING-OUT.md` (60): “off-track→down/supply+mimic; no-response→binary choice then say-together) — directly reusable”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (622): “- **Allowed two-option use:** A two-option response may appear only as a named formative subdecision inside a larger evidence-producing task or bundle, with its 0.50 chance floor recorded and no independent advancement effect.”
- `grade3-reading/course-renderer/authoring/peter-pan/fill/l4-parity/README-p24-ladder.md` (52-54): “`ladder.floor.options` has TWO options, not four. The exemplar has two, the schema (`page-contract.ts` LadderFloor: "exactly TWO — a forced choice, not an MCQ") and `checkScaffoldLadder` (`options.length !== 2` fails) require two.”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (140): “TASK 1 mimicry (the Archivist says the sentence; the student repeats it). TASK 2 apply to the extract. TASK 3 evaluate (""X or Y?"").”
- `g9/sources/3-D-Shakespeare-Othello-1.1.pdf` (123-125): “If you see a shy student who is not offering any suggestions, ask him or her some simple A/B questions such as “Do you want Character A to enter from the left side or the right side?”
- `othello-archive/scripts/check-moments.mjs` (15): “the instruction is over 16 words, or a yes/no question”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (60): “every MCQ in L4 has exactly 4 options (13/13 items); the one msq has 8; no 2-option or T/F item anywhere in the lesson.”
- `grade3-reading/.claude/skills/lesson-build/SKILL.md` (26): “no yes/no stems”

Against: A later run found: A Grade 9 unit's knowledge base ends each lesson's closing questions on an 'X or Y?' evaluation and flags a question that is not 'X or Y' as merely descriptive, and its lesson design specification's evaluation example asks learners to pick one of two readings and justify the view (`g9/sources/1. Act 1 - Knowledge Base - Overview.csv`). A later run found counter-evidence (`grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/CODEX-HISTORY-EVERYTHING-OUT.md`). A later run found counter-evidence (`grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz`). A later run found counter-evidence (`grade3-reading/course-renderer/authoring/peter-pan/fill/l4-parity/README-p24-ladder.md`). A later run found counter-evidence (`g9/sources/1. Act 1 - Knowledge Base - Overview.csv`). A later run found counter-evidence (`g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md`). A later run found counter-evidence (`g9/sources/3-D-Shakespeare-Othello-1.1.pdf`).

<sub>criterion · format, options · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Offer the strongest evidence

When students pick evidence from a set, the strongest evidence must be in the set, and the rubric must not credit evidence they can't pick. In two lessons, three tap-the-evidence items left out the strongest sentence or credited one students couldn't tap.

Reviews of tap-the-evidence items in two Grade 3 lessons found three faults (`shadow/content-eval/reports/G3-U2-L1-review.md`, `shadow/content-eval/reports/G3-U1-L14-review.md`). The sentence linking a plant's job to its survival was missing from the tappable list, a rubric accepted a sentence that isn't one of the tappable spans, and the strongest clue in a paragraph couldn't be tapped. All three were judgment calls in the reviews.

Quoted:

- `shadow-content-eval/reports/G3-U2-L1-review.md` (201): “- The sentence that links the job to survival, *"This natural way of spreading helps plants survive in new places."*, isn't in the tappable list at all.”
- `shadow-content-eval/reports/G3-U1-L14-review.md` (93): “The rubric accepts *"He stayed close, guarded Mole's back"*, but that sentence isn't one of the tappable evidence spans.”
- `shadow-content-eval/reports/G3-U1-L14-review.md` (94): “- **p20 tap-the-clue:** *"I am the reason you have all been dragged into this mess."* is the strongest "owning it" clue in the paragraph, but it isn't tappable as a clue.”

Against: none found

<sub>criterion · options, scoring-guide · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### One answer per blank, and its size

Write each blank so that only one answer fits, and say whether a term, a phrase or a concept is wanted. In one run, 15 of 28 fill-in items failed clarity.

In one AP benchmark run, 15 of 28 fill-in items failed clarity because their blanks allowed several answers at different levels of detail; the judge wrote that "The range of acceptable answers for blank 1 creates ambiguity about the expected level of specificity". The run report then set two requirements: one clear correct answer per blank, and a stated granularity (term, phrase or concept). These are the report's recommendations after the failures, not a tested fix. Before reading the key, list what students at that level might reasonably write, since correct answers missing from the accepted set leave the item without a single answer. An item evaluator's prompt runs this check and fails the item when two or more such answers fit (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt`, lines 440 to 445).

Quoted:

- `APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md` (86): “| Dimension | Failures (of 28 fill-in) |”
- `APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md` (89): “| Clarity | **15 failures** |”
- `APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md` (93): “**New clarity failures:** Fill-in blanks are ambiguous about expected answers.”
- `APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md` (97-98): “The range of acceptable answers for blank 1 creates ambiguity about the expected level of specificity”
- `APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md` (260): “1. Each blank should have ONE clear correct answer”
- `APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md` (261): “2. Specify expected granularity (term, phrase, concept)”
- `APinceptbench/docs/reports/BENCHMARK_RUN6_REPORT.md` (115-116): “Providing multiple pre-written acceptable answers reduces it to pattern matching rather than requiring critical thinking”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (440): “Apply this check ONLY to fill-in-the-blank items; skip entirely for multiple-choice, multiple-select, true/false, and matching question types.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (442): “1. Read the stem WITHOUT looking at the accepted-answer list.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (445): “4. If TWO OR MORE of your completions are factually correct, grammatically fit, AND are NOT in the accepted-answer set, this is a **concrete, unambiguous violation**: the question does not have a single correct answer.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (449): “Example of violation (topic-agnostic): Stem: "A person who writes books is called a _____." Accepted answers: only "author". A student could also correctly answer "writer" because the stem's description fits that just as well.”
- `g9/transformer/src/mechanics/key-words.js` (92): “With meaning_${i} as its cue, does gap_${i} point to word_${i} rather than to any other word in deck?”
- `g9/transformer/src/mechanics/key-words.js` (53): “"accept": ["any OTHER word of this deck that would also fit the blank; usually none"]}.”
- `g9/transformer/src/mechanics/key-words.js` (117): “"${other.word}" fits the sentence too. But this meaning is ${w.meaning}. Which word is that?”
- `g9/transformer/test/mechanics.test.mjs` (101): “assert.equal(fits.correct, null, "another deck word that fits the sentence is not a miss");”

Against: The judge also penalized one obvious fix, listing several pre-written acceptable answers: "Providing multiple pre-written acceptable answers reduces it to pattern matching rather than requiring critical thinking". One answer in meaning may still have several accepted wordings.

<sub>criterion · wording, key, format · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### One answer the text settles

A choice question needs one answer the text settles; check the right option, and each wrong one, on its own.

Every choice block asks the judge whether the keyed option is right, given what the student has read or heard, and
separately whether each other option is wrong (`g9/transformer/src/mechanics/quick-check.js`,
`g9/transformer/src/mechanics/film-check.js`, `g9/transformer/src/mechanics/video-essay.js`). All of them have to hold.

Quoted:

- `icloud-work/inceptbench/docs/AP_EVALUATION.md` (140): “Exactly one answer must be defensibly correct”
- `icloud-work/inceptbench/docs/MATH_VERIFIER.md` (70): “Check all distractors against computed answer”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (141): “| with-passage Gemini control pass | 735/1,152 |”
- `icloud-work/ML learnings/what_is_ap_and_why_it_matters.md` (35): “**MCQ:** One stimulus (primary source), one question stem, four answer choices (A-D), exactly one correct answer, three plausible distractors.”
- `icloud-work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md` (249): “- Issue: All options A–D equal 7/11, but the key lists only A and C.”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (146-147): “The 417 with-passage control failures were often ambiguity or broad `Both` keying, not necessarily blind leakage.”
- `grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md` (36): “genuinely ambiguous with the text”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md` (11): “NOT the report's own suggestion (a plant nursery is a CORRECT use of the word and cannot be a wrong option in "uses the word correctly")”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (104-105): “Root cause: a causal-**chain** passage + a "what causes X?" prompt makes several links defensible, and anti-leak keying the *non-proximate* link worsens it.”
- `grade3-reading/artifacts/alpha-read-packager/BUNDLE_CONTENT_BUGS.md` (53): “The passage is one continuous transitive causal chain”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md` (158-159): “For MSQ, all defensible answers must be keyed. For EBSR, Part B needs one uniquely strongest evidence choice and must not reveal Part A.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (86-87): “**msq** — exactly one defensible correct SET; the keyed set must NOT be "the two/three … longest"; include at least one live-trap distractor”
- `grade3-reading/knowledge_bot/knowledge/kb-0134-g5-reading-v2-local-design-package.qmd` (104): “Independent review found an initial competing S07 plus S09 interpretation.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx` (338 (textutil text)): “Each Refine step has exactly 6 statements, 4 true and 2 incorrect; the incorrect ones are falsifiable directly from the text.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx` (292 (textutil text)): “Not true (opposite of the text: the slab slammed shut on him)”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx` (301 (textutil text)): “Not true (he kept it "pressed against his chest")”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (179 (textutil text)): “Note: the don't-fit words are exactly the things Aladdin does NOT ask for, which is what the text points out.”
- `grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md` (154-156): “`PASS` requires one stable best answer/set and no material alternative. One credible competing answer is `NEEDS_HUMAN`; repeated support for two answers is `FAIL`. "The intended answer is stronger" does not repair a hard-scored item when another option also answers the question.”
- `grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md` (148): “hide the intended key;”
- `grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md` (151): “repeat with at least three option-aliased or shuffled views;”
- `shadow-bench/src/inceptbench/prompts/question/inline_choice_evaluation.txt` (68): “- Two or more options produce identical meaning in context (the blank has no unique correct answer).”
- `shadow-bench/src/inceptbench/prompts/question/ebsr_evaluation.txt` (65-66): “- a NON-keyed Part B option has `supports_part_a_keyed_answer: YES` (a distractor is itself valid supporting evidence, so the Part B key is not the unique/complete set).”
- `shadow-bench/src/inceptbench/prompts/question/science_evaluation.txt` (26-27): “- A reading-the-data or interpret-the-graph task must give enough information for the intended answer to be determinate.”
- `shadow-bench/src/inceptbench/prompts/question/sequence_evaluation.txt` (100-101): “`orderability` is high when the cohesive cues admit exactly one coherent arrangement, and low when two or more arrangements read as equally coherent.”
- `shadow-bench/src/inceptbench/prompts/question/sequence_evaluation.txt` (118-120): “The subjective-ordering failure still holds: if the stem orders by a subjective axis with no text-fixed answer (e.g., "arrange these themes from least to most important" with no basis in the passage) → `orderability = 1`.”
- `icloud-work/ML learnings/mcq_set_journey.md` (12): “2. All 3 questions must be independently answerable from the stimulus alone”
- `icloud-work/incept/inceptbench/docs/AP_EVALUATION.md` (140): “| `answer_validity` | MCQ, MCQ_SET | Exactly one answer must be defensibly correct |”
- `icloud-work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json` (21): “Equally Text-Supported**: Both correct answer and distractor are equally supported by passage evidence”
- `icloud-work/incept/nova_forge/scores/aplit-quiz-generation/results.txt` (13): “Accuracy:         66.7%”
- `icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-04T1430Z_v40h_spot_verify.md` (71): “**Verdict: Oracle's call CONFIRMED.** Multiple-correct-answers defect. A thoughtful student picking C is not factually wrong.”
- `icloud-work/evaluator/ap_benchmark/prompts/msq.py` (22): “- Each correct answer must be independently correct”
- `icloud-work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md` (22-27): “| answer_validity | 146 |”
- `icloud-work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md` (10): “There are two defensible correct answers.”
- `icloud-work/ap-social-studies-generator/python/generators/mcq_set.py` (400): “TEST: "Could an AP teacher argue this distractor is also correct?" → if yes, CHANGE IT.”
- `icloud-work/inceptbench-main/src/inceptbench/evaluators/question.py` (979-983): “Narrative-writing-evaluation items (standards naming engage/orient reader, event sequence, establish context with characters) that ask the student to pick the BEST among multiple long parallel options (drafts/passages of 40+ words each) carry a high risk of containing distractors that a reasonable student could defensibly pick.”
- `icloud-work/inceptbench/submodules/reading-question-qc/qc_pipeline/config/prompts.json` (21): “Degree-Only Difference**: Differs only in degree/intensity when the passage doesn't clearly establish the distinction”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md` (241): “| Dim 9: Answer key defensibility | Correct answer is uniquely defensible from text | Hard gate |”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_evaluation.txt` (387): “- **Borderline-correct distractors**: an option labeled incorrect is actually a defensible answer under the stem's *named* criteria.”
- `grade3-reading/knowledge_bot/knowledge/kb-0223-g3-review-rounds-and-tooling-2026-09-18-to-21.qmd` (31): “explicitly **not** the report's own suggested fix (a plant nursery is itself a correct use of the word).”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (102): “6 practice items dropped after the screen credibly showed a **multi-defensible key** (verified by reading”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md` (258): “Either way the correct answer should be statable with a single-sentence verbatim pointer.”
- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md` (186): “- **W-8. WORTH-FIXING — `item-8-match` prompt 1 is a coin-flip between two dated”
- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-25-R10.md` (104): “per the lesson's own gloss pattern) can defensibly pick the distractor and be marked wrong.”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md` (154-156): “`PASS` requires one stable best answer/set and no material alternative. One credible competing answer is `NEEDS_HUMAN`; repeated support for two answers is `FAIL`. "The intended answer is stronger" does not repair a hard-scored item when another option also answers the question.”
- `ti-courseplans-audit/skills/course-content-integrity/SKILL.md` (155-156): “"The intended answer is stronger" does not repair a hard-scored item when another option also answers the question.”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-ENTRYPOINT-CLEAN-ROOM-G3-U4-L1-2026-08-06.qmd` (59-60): “One hot-text prompt can reasonably be answered by either winter or spring camouflage, while only the winter sentence is keyed.”
- `grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md` (155-156): “"The intended answer is stronger" does not repair a hard-scored item when another option also answers the question.”
- `shadow-content-eval/reports/G3-U1-L13-review.md` (46): “`secret` makes a grammatical, true sentence.”
- `shadow-content-eval/reports/G3-U2-L1-review.md` (131): “A child who taps it is corrected for a defensible answer.”
- `shadow-content-eval/reports/G3-U2-L1-review.md` (113): “As written, "Things I already know" is a correct answer to many questions.”
- `home-agent-memory/continuous_improvement.md` (48): “- `answer_validity` — MCQ must have exactly 1 correct answer”
- `shadow-bench/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (218-222): “the answer key itself must be both **complete** (every option that is correct under the stem is keyed) and **exclusive** (no keyed option is actually incorrect). A correct option left out of the key, or an incorrect option included in the key, mismeasures every student and is a factual error in the item — not a stylistic preference. Do NOT excuse a missing-correct option by arguing the keyed options are "the best" ones; "select all that apply" means all.”
- `shadow-bench/src/inceptbench/prompts/question/hot_text_evaluation.txt` (57-59): “A hot text item must have exactly the keyed set as its defensible answer. "It is the best span" does NOT rescue the item when another selectable span also satisfies the literal instruction — ambiguous keys mismeasure students.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md` (116): “8. **Multi-correct**: two options are defensibly correct. Verify with the rationale that only ONE option survives strict reasoning.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/UNIT1_TO_ALL_UNITS_TRANSFER_PLAN.md` (66): “use overly broad "best explains" stems with multiple defensible answers.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md` (2024): “row 336 MCQ_SET easy scored 0.75 because Q2 asked for European disagreement not actually present in the stimulus,”
- `g9/transformer/src/mechanics/worked-model.js` (50): “the other two are wrong about the text or the word.”
- `g9/transformer/src/mechanics/worked-model.js` (97): “rebuilt(item, x.k, x.o)”
- `g9/transformer/src/mechanics/worked-model.js` (106): “Is sentence_${x.k}_${x.j} wrong about quote or about passage?”
- `g9-transformer-runs/blocks/be97f27fc4c4a65a.json` (120): “makes the rebuilt sentence wrong: the judge found this does not hold”
- `g9-transformer-runs/blocks/be97f27fc4c4a65a.json` (333-334): “"verdict": "fails", "p": 0.31”
- `g9/transformer/src/mechanics/quick-check.js` (68): “The keyed answer is right, judged from the cited lines”
- `g9/transformer/src/mechanics/quick-check.js` (70): “is wrong, judged from the whole text”
- `g9/transformer/src/mechanics/direct-the-line.js` (2): “The judge, reading the same lines around it, must pick the same delivery.”
- `g9/transformer/v02/QA.md` (105-106): “that the keyed option is right, the others wrong, and that every option is well formed (added after a draft offered "he is not what he am")”
- `g9/transformer/src/mechanics/film-check.js` (86): “every option is well-formed English”
- `g9/transformer/v02/QA.md` (106): “every option is well formed (added after a draft offered "he is not what he am")”
- `g9/transformer/src/mechanics/quick-check.js` (68): “{ id: "answerable", label: "The keyed answer is right, judged from the cited lines", q: noul("answerable", "Using only evidence_lines, is the option named by keyed_answer a correct answer to the question?"), expect: "yes" },”
- `g9/transformer/src/mechanics/quick-check.js` (70): “id: `wrong-${letters[i]}`, label: `Option ${letters[i]} is wrong, judged from the whole text`,”
- `g9/transformer/test/calibration/quick-check.answerable.json` (5): “A block's check, on both samples: is the keyed option right, judged only from the cited lines.”
- `g9/transformer/test/calibration/quick-check.answerable.json` (5): “Seed cases only: obvious ones”
- `g9-transformer-runs/blocks/be97f27fc4c4a65a.json` (58-62): “"long remember",”
- `g9-transformer-runs/blocks/be97f27fc4c4a65a.json` (334): “"p": 0.31,”
- `learning-truths/research/2026-10-12-6-transformer-ideas/universality-test-gettysburg.txt` (5): “The world will little note, nor long remember what we say here, but it can never forget what they did here.”
- `g9-transformer-runs/blocks/856ace1aed960671.json` (6): “"status": "ready",”
- `g9-transformer-runs/blocks/856ace1aed960671.json` (14): “"answer": 1,”
- `g9-transformer-runs/blocks/c98cc9de312f4d43.json` (6): “"status": "ready",”
- `g9-transformer-runs/blocks/c98cc9de312f4d43.json` (14): “"answer": 0,”
- `g9/transformer/v02/QA.md` (105): “question is answered by what has been said by its stop, that the keyed option is right, the others wrong, and that”
- `g9/transformer/v02/QA.md` (105): “that the keyed option is right, the others wrong”
- `g9-transformer-runs/decisions/68d85cc9b79fb956.json` (55, 288): “"sentence_0_2": "The noun wrinkled lip implies that the king held his subjects in utter contempt and felt entirely superior to them.",”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (292): “Its rollercoaster option can also seem dangerous under the actualdefinition; feedback rejects it using fun/laughter absentfromtheoption.”
- `grade3-reading/ui-audit-2026-09-08/round-5/final-standard-verification/SEMANTIC-FIVE-FLAG-DISPOSITION-by-residual.md` (14): “Separately, the fast/steep/screaming rollercoaster can reasonably seem dangerous.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_08 10_30 CEST - Notes by Gemini.md` (322): “A lot of the questions are they're uh they're not well-ritten questions in the sense that they're there's two or three plausible answers whereas to hit a mastery rate of 90% you want to you know have clarity on that.”
- `g9/library/text/L612555.txt` (128): “Hendrick explained that test items must feature single, unambiguous correct answers rather than multiple plausible options”

Against: none found

<sub>criterion · key, distractors · universal · from g9 · adopted-rule · held · found in [2026-10-12-1-seed](../research/2026-10-12-1-seed/), [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### One defensible order

An ordering item needs one defensible order: use only elements with a definite place, such as dated events or discrete steps, never a gradual process or ongoing condition.

The ordering rubric classifies every element, and one whose starting event, law or publication can't be named is an ongoing state that caps orderability at 3 (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/sequence_evaluation.txt`). Elements with explicit years or centuries turn the task into reading dates, and the stem must make the ordering criterion explicit, with no element referring forward in a way that reveals its position (the same file).

Quoted:

- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/sequence_evaluation.txt` (36): “The test: if you cannot name the specific event/law/publication that STARTED this condition → it is an ongoing_state → orderability ≤ 3.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/sequence_evaluation.txt` (176-178): “**Dates-in-items flag:** Items containing explicit years/centuries inline (e.g., "in 1492", "c. 1440 CE", "during the 15th century") reduce the task to date-reading rather than content knowledge.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/sequence_evaluation.txt` (189-190): “Does the question stem make the ordering criterion explicit? Do items avoid forward references that reveal their relative position?”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/sequence_evaluation.txt` (40): “> "Can I name the specific moment this STARTED — a named law, event, publication, battle, or decree?"”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/sequence_evaluation.txt` (64): “- An item is classified ongoing_state or process → orderability ≤ 3 (regardless of position)”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/sequence_evaluation.txt` (74): “- BIOLOGY (5): "Arrange the stages of mitosis: Prophase → Metaphase → Anaphase → Telophase" — each step has a unique, unambiguous position.”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/sequence_evaluation.txt` (78): “- ELA (1): "Arrange these themes from least to most important" — subjective, no correct order.”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/sequence_evaluation.txt` (97): “accept it as correct (score 4 or 5) even if scholarly debate exists at a higher level.”

Against: Dates are fine when the date is itself the curriculum fact being tested (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/sequence_evaluation.txt`, lines 178-179). The same rubric judges an order against what is taught at the grade, and tells the judge to "accept it as correct (score 4 or 5) even if scholarly debate exists at a higher level" (`icloud-work/incept/inceptbench/src/inceptbench/prompts/question/sequence_evaluation.txt`, line 97), so one definite place means one place at that grade.

<sub>criterion · format, key, integrity · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### One idea, three closing moves

Close a lesson with three questions on a single idea: name it, find where it works in the text, then use it beyond the text, as support fades. One design gives the first of three closing questions the most support, the second a frame and the third none.

A closing-questions design that replaces the closing three questions in every lesson is written against a closing section of three unrelated questions that happen to get harder, which it calls a quiz (`grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt`). Its three moves walk one idea from being said, to being found in this text, to being used somewhere the child has not read; the finding slots ask when, not what, so the answer shows the mechanism rather than the plot. Support fades because guidance that helps a novice harms once a schema exists, which the design rates well evidenced. Once support has faded it never comes back.

Quoted:

- `grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt` (16): “These are not three questions of increasing difficulty. They are three moves on one idea.”
- `grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt` (17): “Name it · Find it here · Use it.”
- `grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt` (80): “The slots must ask when, not what.”
- `grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt` (109): “Support fades and never returns. Maximum at Q1, a frame at Q2, nothing at Q3.”
- `g9/transformer/src/mechanics/say-it-back.js` (1): “Say it back: the first of the Grade 9 close questions (mimicry, then application, then evaluation).”
- `g9/transformer/src/glue/animated.js` (193): “the Grade 9 close: mimicry, then evaluation”
- `g9/transformer/test/mechanics.test.mjs` (18): “at("say-it-back") < at("debate")”
- `g9/transcript/chat-transcript.redacted.txt` (3132): “Mimicry → Apply → Evaluate belongs to the closing questions after independent practice.”
- `g9/transcript/chat-transcript.redacted.txt` (2874): “1. Mimicry: reproduce a demonstrated reasoning move and explain why it works.”
- `g9/transcript/chat-transcript.redacted.txt` (2875): “2. Application: select and adapt that move in a different passage or situation.”
- `g9/transcript/chat-transcript.redacted.txt` (2876): “3. Evaluation: weigh rival interpretations, test evidence, identify limitations and revise a judgment.”
- `g9/transcript/chat-transcript.redacted.txt` (2878): “This progression is a working design, not a requirement to reteach mastered steps.”
- `grade3-reading/course-renderer/docs/handover/closing-questions/design-mock-l1.html` (195): “Slots ask when, not what; production, never a word bank or tap; at least one slot in the text's own words”
- `grade3-reading/course-renderer/docs/handover/closing-questions/design-mock-l1.html` (114): “The rule mapped onto this text as mechanism, not plot.”
- `grade3-reading/course-renderer/docs/handover/closing-questions/HANDOVER.md` (109-110): “A near-miss is plot with no trust in it.”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md` (125-126): “Find it here → Use it, one idea three times, production only, no MCQ/word bank/tap in the closing three, the Q1 sentence recurs at the start of the next part.”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (186): “They are a more sophisticated version of the K–8 format, moving from mimicry, to application to the text, to evaluation at the end.”
- `othello-archive/sources/act1/KB - Overview.csv` (140): “TASK 1 mimicry (the Archivist says the sentence; the student repeats it). TASK 2 apply to the extract. TASK 3 evaluate (""X or Y?"").”

Against: It has not been measured with children: an audit found that whether children reach its target success rates, or actually infer, could not be checked from the lesson files (`grade3-reading/artifacts/curriculum-adherence-2026-09-24/CRITIC.md`).

<sub>criterion · sequence, demand, hints · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### One question at a time

Ask one thing at a time: one question per screen, and a two-part task as two turns, so the feedback can answer each part. Three pages overflowed the screen for the same reason: two choice questions stacked on one page.

A one-screen census at 1440×900 found four pages too tall, three of them for the same reason, two multiple-choice questions stacked on one page; each was split into single-question pages with every quoted option kept. A reading course's vocabulary rulebook splits saying a word and defining it into two separate turns, because one question asking both complicates the feedback when a child gets both parts wrong.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd` (107): “one-screen census failures** at 1440×900”
- `grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd` (108-109): “two MCQs stacked on one page”
- `grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd` (110-111): “each split into single-question pages/cases, all verbatim quoted options preserved”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (54-55): “Say the word first, define it second, as two **separate turns** — not one question asking both”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (55-56): “complicates simultaneous feedback if a child gets both parts wrong”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (56-57): “the split/order is not validator-checked”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (306-307): “Two asks arriving in the same instant, one of them answerable, and nothing saying which is theirs.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (308): “the defect is SIMULTANEITY, not existence.”
- `g9/player/design/ARCHIVIST-DESIGN.md` (330): “Our `check_intro_world` is two-part in `data.js`; either split it into two sequential stops at 93.4 and 93.5 s”

Against: the two-turn split is built into the card's structure, but no validator checks it.

<sub>criterion · format, feedback · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### One slip costs one point

Score the working separately from the final answer and let later parts credit work that follows from the student's own earlier answer, so a slip costs only one point. A correct setup with one arithmetic slip still earns its setup points.

The evaluator's free-response rules make method credit separable from final-answer credit, so a correct setup with a single arithmetic slip still earns its setup points (`shadow-bench/src/inceptbench/prompts/question/frq_long_evaluation.txt`). A well-formed multi-part item lets a student who erred early still earn later points by crediting work consistent with their own earlier value, and at least one part should not depend on a prior numeric result. A significant-figure slip costs only the point where precision is checked and does not cascade, and the AP Chemistry overlay states the same convention, error carried forward (`shadow-bench/src/inceptbench/prompts/question/ap_chemistry_evaluation.txt`).

Quoted:

- `shadow-bench/src/inceptbench/prompts/question/frq_long_evaluation.txt` (42-44): “Method credit is **separable** from the final-answer credit: a correct setup with a single arithmetic slip should still earn the setup point(s).”
- `shadow-bench/src/inceptbench/prompts/question/frq_long_evaluation.txt` (109-112): “- A well-formed multi-part item must allow a student who erred on an early part to still earn later points: later parts should credit work **consistent with the student's own earlier (even if wrong) value**, and at least one part should be answerable **without** depending on a prior numeric result.”
- `shadow-bench/src/inceptbench/prompts/question/frq_long_evaluation.txt` (149-150): “- Significant-figure precision is normally checked at only one or a few designated points and a sig-fig slip costs **only** that point — it does not cascade.”
- `shadow-bench/src/inceptbench/prompts/question/ap_chemistry_evaluation.txt` (66-67): “credit work that is **consistent with a student's earlier answer** (error-carried-forward).”
- `shadow-bench/src/inceptbench/prompts/question/ecr_evaluation.txt` (30): “- AUTO-ZERO CASCADE: if Trait 1 = 0, Trait 2 is automatically 0”

Against: Some rubrics cascade on purpose: '- AUTO-ZERO CASCADE: if Trait 1 = 0, Trait 2 is automatically 0' (`shadow-bench/src/inceptbench/prompts/question/ecr_evaluation.txt`, line 30), in an essay rubric whose first trait is the development of ideas and whose second is conventions.

<sub>criterion · scoring-guide, marking, format · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### One task per part

Ask for one thing in each stem or part of a question: no compound verbs such as identify and describe, no second question, no joining of separate concepts.

The evaluator's API spec bans compound task verbs such as "identify AND describe" within one part (`icloud-work/evaluator/docs/EVALUATION_API.md`), and the judge flagged a part that conflated two distinct concepts (`icloud-work/evaluator/docs/reports/LATEST.md`). The support is thin: one adopted rule and one judge note, raised once. The skill each part declares must also match what its prompt asks.

Quoted:

- `icloud-work/evaluator/docs/EVALUATION_API.md` (328): “- **NEVER** use compound verbs like "identify AND describe" in a single part”
- `icloud-work/evaluator/docs/reports/LATEST.md` (125): “| Part (c) conflates two distinct concepts — maritime technology development AND navigational skills —... | 1 |”
- `APinceptbench/docs/reports/evaluation_20260225_081919_0909a798.md` (54): “- (2x) Mismatch between stated reasoning type (causation) and actual prompt structure (...”
- `APinceptbench/docs/EVALUATION_API.md` (328): “- **NEVER** use compound verbs like "identify AND describe" in a single part”
- `shadow-bench/src/inceptbench/prompts/question/scr_evaluation.txt` (91-92): “An SCR that tests multiple unrelated concepts cannot be fairly scored on a 0/1/2 scale.”
- `shadow-bench/src/inceptbench/prompts/question/scr_evaluation.txt` (128-129): “- Fails if the question is vague ("Write about the passage"), has two different questions in one stem, or uses vocabulary significantly above the target grade level when simpler alternatives exist.”
- `shadow-bench/src/inceptbench/prompts/question/frq_long_evaluation.txt` (14-15): “- A long FRQ is a **broad, integrative** item: it is worth roughly **10 scorable points** and **spans two to three distinct topics/units**, woven into one scenario.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (273): “And the question is two questions in one, so a child can answer half and feel finished.”
- `g9/library/text/L36b8ba.txt` (273): “And the question is two questions in one, so a child can answer half and feel finished.”

Against: Multi-part items deliberately span several topics but score each part separately: '- A long FRQ is a **broad, integrative** item: it is worth roughly **10 scorable points** and **spans two to three distinct topics/units**, woven into one scenario.' (`shadow-bench/src/inceptbench/prompts/question/frq_long_evaluation.txt`, lines 14-15).

<sub>criterion · stem, format · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Only the text decides the blank

In a gap-fill choice, every option should come from the same category, read grammatically in the sentence and differ in meaning there, so only understanding the text decides.

Fill-the-blank choice items came into the evaluator with audits that write each option into the sentence (`shadow-bench/src/inceptbench/prompts/question/inline_choice_evaluation.txt`). The item fails if any option makes the sentence ungrammatical, since the skill tested is comprehension, not grammar correction, or if two options mean the same thing there, since the blank then has no unique answer. A correct choice must need the passage read and understood; grammar alone, such as article agreement, or common knowledge must not decide it. Then neither grammar nor elimination can decide the blank.

Quoted:

- `shadow-bench/src/inceptbench/prompts/question/inline_choice_evaluation.txt` (66-67): “- Any option produces an ungrammatical sentence when inserted (all options must fit grammatically — the skill being tested is comprehension, not grammar correction).”
- `shadow-bench/src/inceptbench/prompts/question/inline_choice_evaluation.txt` (68): “- Two or more options produce identical meaning in context (the blank has no unique correct answer).”
- `shadow-bench/src/inceptbench/prompts/question/inline_choice_evaluation.txt` (32-33): “A correct inline choice must require the student to have read and understood the passage — it is NOT acceptable if grammar alone (e.g., article agreement) or common knowledge determines the answer.”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (46): “Cloze retell; each gap opens exactly 3 same-category choices | Same-category trios kill syntax and elimination guessing — only the story model decides”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (149): “each trio from the same category, so the sentence stays grammatical whichever the child picks and only meaning decides.”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (151): “three same-category choices per gap means the choice cannot be made on syntax or on elimination-by-absurdity — the child must consult their model of the story.”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (337): “A cloze earns its keep when context genuinely forces the selection”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md` (379): “Gap 4 offers only past-tense answers (flickered/vanished/widened) inside a present-tense retell; the slip is in the design doc itself (`artifacts/pp1-v3-design.txt:101`).”

Against: none found

<sub>criterion · options, integrity, wording · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Options must not give a step away

When a stem asks for two steps, options that all share the first step's outcome give it away; drop that step or let the options span its outcomes.

An item evaluator's closed-ended rubric gives the case of a stem that asks students to identify the sentence with an error and then choose its correction, while every option concerns one sentence: the identification step is given away by the option set, and the fix is to drop the first step or offer options spanning all the sentences (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt`). The rule came from issue 382 and is pinned by a prompt-rule test.

Quoted:

- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (603): “If the stem asks the student to do two things (e.g., "First identify the sentence with the error, then choose the correction"), but the answer options only correspond to ONE of the source items, the identification step is given away by the option set.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (603): “Fix is either to drop the first step from the stem or to provide options spanning all source items.”

Against: It does not apply when the options' own text names the first step's output, because the student then commits to both steps in one choice (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/_base_evaluation.txt`, line 156).

<sub>criterion · options, stem, integrity · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Options that differ in meaning

Check that the options differ in meaning, not just in wording: identical or equivalent options leave more than one right answer and no real distractor.

In two runs of 298 generated items that passed at 3.7% and 3.0%, factual accuracy failed on 78% of items, among them items whose four options were identical (`icloud-work/incept/nova_forge/archive/old_docs/platform/PATTERN_ANALYSIS_RESULTS.md`, lines 10-11, 21 and 24). A production math generator's wrapper filters equivalent distractors, and its requirements rule out pairs such as 1/2 and 5/10 unless multi-answer is supported (`icloud-work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md`, lines 41 and 73). A reading question check flags a distractor that uses different wording for essentially the same meaning as the right answer (`icloud-work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json`, line 21).

Quoted:

- `icloud-work/incept/nova_forge/archive/old_docs/platform/PATTERN_ANALYSIS_RESULTS.md` (10): “**Run 1:** 3.7% pass rate (11/298 passed)”
- `icloud-work/incept/nova_forge/archive/old_docs/platform/PATTERN_ANALYSIS_RESULTS.md` (11): “**Run 2:** 3.0% pass rate (9/298 passed)”
- `icloud-work/incept/nova_forge/archive/old_docs/platform/PATTERN_ANALYSIS_RESULTS.md` (21): “### 1. Factual Accuracy (78% failure rate)”
- `icloud-work/incept/nova_forge/archive/old_docs/platform/PATTERN_ANALYSIS_RESULTS.md` (24): “- All options are identical (e.g., all 4 choices say "Four thousand five hundred sixty-seven")”
- `icloud-work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md` (41): “- filtering equivalent distractors”
- `icloud-work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md` (73): “- Avoid **equivalent distractors** (e.g., `1/2` vs `5/10`) unless multi-answer is supported.”
- `icloud-work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json` (21): “Synonymous or Near-Synonymous**: Uses different wording but conveys essentially the same meaning”
- `g9-transformer-runs/decisions/be97f27fc4c4a65a.json` (54): “"sentence_0_1": "The phrase long remember presents spoken rhetoric as something fragile that will quickly fade from human memory.",”
- `g9-transformer-runs/decisions/be97f27fc4c4a65a.json` (271): “"value": 0.24,”
- `g9-transformer-runs/decisions/68d85cc9b79fb956.json` (55): “"sentence_0_2": "The noun wrinkled lip implies that the king held his subjects in utter contempt and felt entirely superior to them.",”
- `g9-transformer-runs/decisions/68d85cc9b79fb956.json` (288): “"value": 0.53,”
- `g9-transformer-runs/decisions/b9cb3d0f3a8639c0.json` (55): “"sentence_0_2": "The phrase \"upon him\" reveals his purely opportunistic nature.",”
- `g9-transformer-runs/decisions/b9cb3d0f3a8639c0.json` (288): “"value": 0.51,”
- `g9-transformer-runs/decisions/be97f27fc4c4a65a.json` (423): “"sentence_0_2": "The phrase \"long remember\" implies that official speeches leave almost no mark on history.",”
- `g9-transformer-runs/decisions/be97f27fc4c4a65a.json` (658): “"value": 0.48,”
- `g9-transformer-runs/decisions/be97f27fc4c4a65a.json` (796): “"sentence_0_1": "The phrase long remember suggests that spoken dedications carry minimal lasting weight in human history.",”
- `g9-transformer-runs/decisions/be97f27fc4c4a65a.json` (1017): “"value": 0.31,”
- `g9-transformer-runs/blocks/be97f27fc4c4a65a.json` (120): “makes the rebuilt sentence wrong: the judge found this does not hold”
- `g9-transformer-runs/decisions/68d85cc9b79fb956.json` (271): “"value": 0.78,”
- `g9-transformer-runs/decisions/be97f27fc4c4a65a.json` (288): “"value": 0.96,”
- `g9-transformer-runs/decisions/b9cb3d0f3a8639c0.json` (271): “"value": 0.85,”
- `grade3-reading/course-renderer/content/lesson-plans/g3-u2-l1.json` (965): “p12's Amazon option was dropped rather than kept as a near-miss because 'is home to' reads as shelter, which the key already names, so it was arguably a third correct answer.”

Against: Equivalent options are allowed when every one of them is keyed: the rule holds only "unless multi-answer is supported" (`icloud-work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md`, line 73).

<sub>criterion · options, distractors, key · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Outside knowledge must come from outside

In a task built on given sources, the marking guide's examples of outside knowledge must not repeat what the sources already say.

The AP generator sometimes listed a provided document's content as outside evidence in a document-based question's marking guide, and the judge failed such items on factual accuracy because it checks for that contradiction (`icloud-work/aptraining/.agent/research/inference_clean.md`). An old pipeline patched it after generation by deleting overlapping items and padding with a generic placeholder; an audit replaced the patch with a rule to train the writer never to list document content as outside evidence (the same file).

Quoted:

- `icloud-work/aptraining/.agent/research/inference_clean.md` (69): “LLM sometimes lists Doc 5's content as outside evidence — causes factual_accuracy hard-fails because the evaluator checks for this contradiction”
- `icloud-work/aptraining/.agent/research/inference_clean.md` (403): “Fix in training data — train the model to never list document content as outside evidence.”

Against: No count of how often it happened.

<sub>criterion · scoring-guide, stimulus · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Point to the part, not its property

When a question asks about part of a picture or diagram, point to that part by name or highlight but never state the property the student must read from it.

An audit found an independent item whose stem stated the arrow direction the item was meant to make students read, so a student could answer from the stem's own wording without consulting the diagram or applying the rule. The stem was rewritten to name only the arrow's two endpoints, leaving the direction to be worked out from the rule and the diagram together, which is the construct under test. The build then highlighted the arrow meant without showing its direction: the highlight says which line, and only the arrowhead says which way.

Quoted:

- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (281-282): “the stem itself states the direction (urchin→otter), so a student can answer correctly from the stem's own wording without ever consulting the diagram or applying the rule.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (291-293): “names the two endpoints without asserting direction, forcing the student to determine direction from the rule + diagram together, which is the actual construct under test.”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (656-657): “the highlight says WHICH line, and only the map's arrowhead says which way.”

Against: none found

<sub>criterion · stem, integrity, stimulus · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Possible numbers and a sound premise

Every number in a question's setup must be possible and consistent with the others, and the reasoning to the answer must rest on a true premise, not just correct arithmetic. A yield above 100% or a probability outside its range fails even when the arithmetic is right.

The evaluator's science rules, which apply to science questions in any curriculum and question type, count a computation that is arithmetically right but rests on a wrong scientific premise as a factual-accuracy defect. Quantities must be physically plausible and dimensionally sane: consistent units, realistic magnitudes and no value past a physical bound. The chemistry free-response rules add that quantities must be chemically possible and internally consistent. No measurement comes with these rules.

Quoted:

- `shadow-bench/src/inceptbench/prompts/question/science_evaluation.txt` (11-13): “A computation can be arithmetically right yet rest on a wrong scientific premise — that is still a `factual_accuracy` defect.”
- `shadow-bench/src/inceptbench/prompts/question/science_evaluation.txt` (14-18): “- Quantities must be **physically plausible and dimensionally sane**: units are consistent and convert correctly; magnitudes are realistic for the phenomenon; a value cannot violate a physical bound (e.g. a negative amount of a conserved quantity, a probability/fraction outside its range, an efficiency or yield above 100%).”
- `shadow-bench/src/inceptbench/prompts/question/science_evaluation.txt` (3): “These rules apply to science questions across any curriculum and question type.”
- `shadow-bench/src/inceptbench/prompts/question/frq_long_evaluation.txt` (141-143): “Quantities must be chemically possible: equilibrium constants, concentrations, pH for dilute aqueous systems, yields (≤ 100%), and thermodynamic signs must be internally consistent and within plausible ranges.”

Against: none found

<sub>criterion · integrity, stem, key · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Practise taught words by typed recall

After study, practise taught words by typed recall: cue each by its meaning in a one-blank sentence pointing to it alone and containing no form of it; nudge before revealing. Code holds a deck when any sentence lacks exactly one blank or contains its word or one of its forms, quotations included.

The 9 October audit of the lesson engine found that the word web lands a lesson's key words face down but nothing makes students practise them. It proposed a set to study in which each word is cued by its meaning in a gap sentence from the text and typed from memory (`g9-transformer-audit/2026-10-09-best-of-everything.json`). The key-words block built from that proposal holds, in code, any sentence that lacks exactly one blank or contains its word or one of its forms anywhere, quotations included. It also asks the judge whether each gap, with its meaning as the cue, points to its own word rather than another word in the deck (`g9/transformer/src/mechanics/key-words.js`, lines 26-31, 75-76 and 92). Its view lists the study set in alphabetical order so no gap lines up with its word, another deck word the writer lists as fitting a gap is not marked a miss, the second miss gives the word, and marking is code only, so a session needs no model and replays exactly (the same file, lines 1-5 and 100-118).

Quoted:

- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “Each word is cued by its meaning in a gap sentence from the text, and the student types it from memory.”
- `g9/transformer/src/mechanics/key-words.js` (26): “Does the sentence give its word away: the word or one of its forms, anywhere in it, quotations included.”
- `g9/transformer/src/mechanics/key-words.js` (75): “Each sentence has exactly one blank”
- `g9/transformer/src/mechanics/key-words.js` (92): “does gap_${i} point to word_${i} rather than to any other word in deck?”
- `g9/transformer/src/mechanics/key-words.js` (100): “the study set in alphabetical order, and the gaps with their cues, so no gap lines up with its word”
- `g9/transformer/src/mechanics/key-words.js` (116): “fits the sentence (another accepted word), but the meaning cued is a different word: not a miss”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “In the animated render, keyword_cards offers a choice, not recall, so the full deck appears only in the transformer's own view.”
- `g9-transformer-audit/2026-10-09-builders.json` (1): “KW checks leaks against the deck's own forms: a block cannot see the web's forms.”
- `g9/transformer/README.md` (120): “No lesson has been reviewed by a person or used by a student.”
- `g9/transformer/src/mechanics/key-words.js` (1): “study a set, then recall each word into a gap. Each word comes back in a sentence about the text with a”
- `g9/transformer/src/mechanics/key-words.js` (2): “blank where it goes, cued by its meaning, and the student types it from memory.”
- `g9/transformer/src/mechanics/key-words.js` (4): “gets a nudge, since a taught word is spelled right; the second miss gives the word.”
- `g9/transformer/web/lesson.js` (513): “Opening.tsx KeywordCards, then the 3D build's recall”
- `g9/transformer/web/lesson.js` (514): “memory, cued by its meaning; a miss gets a nudge, the second gives the word”
- `g9/transformer/web/lesson.js` (541): “Study each word and what it means. Then put them away, and put each back into its sentence from memory.”
- `g9/transformer/src/glue/threejs-render.js` (12): “a key-words deck: study the set, then each word into its gap, cued by its meaning”
- `g9/transformer/src/mechanics/key-words.js` (121): “The word you want begins with”
- `g9/transformer/src/glue/animated.js` (152): “check: { prompt: "Which word fits?"”
- `othello-archive/src/steps/KeyWords.tsx` (5): “A word that fits the sentence but not the meaning cued is not a miss.”
- `othello-archive/src/steps/KeyWords.tsx` (151): “fits the sentence (another accepted word), but the meaning cued is a different word: not a miss”
- `othello-archive/DRAFTS.md` (405): “| 359 | alsoFits | " fits the sentence too. But this meaning is |”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/vocabulary-use-routine-and-volume.md` (21): “Or to fill in the blank with the word admire. … we're really trying to provide an opportunity for them to explore the meaning of the word, not just to say the word.”

Against: In the animated version's export the deck becomes a choice: "In the animated render, keyword_cards offers a choice, not recall, so the full deck appears only in the transformer's own view." (`g9-transformer-audit/2026-10-09-best-of-everything.json`, line 1; the export at `g9/transformer/src/glue/animated.js`, line 152). The leak check sees only the forms listed for the deck, plus a prefix match on long words, because a block cannot see the word web's forms (`g9-transformer-audit/2026-10-09-builders.json`, line 1; `g9/transformer/src/mechanics/key-words.js`, line 30). No lesson from the engine has yet been reviewed by a person or used by a student (`g9/transformer/README.md`, line 120). An animated version's export checks the deck with one gap answered by a choice, not typed from memory (`g9/transformer/src/glue/animated.js`, line 152). A later run found: an early-grades vocabulary routine calls a frame where the learner fills the blank with the word a pitfall, since it has the learner say the word rather than explore its meaning (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/vocabulary-use-routine-and-volume.md`).

<sub>criterion · practice, format, integrity, key · universal · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Pre-fill the action in a motive frame

In a why-question's answer frame, print the character's action already, leaving only the reason to write, so the answer cannot just restate the action. One lesson prints the procedure's three-part sentence with its first two parts filled, leaving only the conclusion to the child.

Lesson research on motive questions for a grade 4 reading lesson describes a child who, asked why a character tied his men up, answers that he tied them up, staying at the word and phrase level that a literature review on inference finds in poorer comprehenders. Its design consequence is an answer slot that makes restating impossible: a sentence frame whose first half is already the action, so the only place left to write is the reason. The lesson plan adopts this at its guided step, printing the procedure's three-part sentence with the first two parts filled, which it says is what stops the child restating the action instead of inferring from it.

Quoted:

- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (291-295): “A child who answers "because he tied them up" to "why did he tie them up" has stayed at that level. The design consequence is that the answer slot must make restating impossible: a sentence frame whose first half is already the action, so that the only place the child can write is the reason.”
- `grade3-reading/course-renderer/content/lesson-plans/g4-u1-l3.json` (270): “It is also the only shape that can print the procedure's own three-part sentence with the first two parts filled, which is what stops the child restating the action instead of inferring from it.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (286-288): “The review does not name this failure directly, so treat the diagnosis as my own; what it does support is the cause and the fix.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (9): “Written before the lesson is authored.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (292-295): “The design consequence is that the answer slot must make restating impossible: a sentence frame whose first half is already the action, so that the only place the child can write is the reason.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (288-289): “focussed very much at the word and phrase level of interpretation”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l3.json` (143): “The guide supplies the quote, which is what makes restating the action impossible”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l3.json` (143): “the only fix in the item's own shape is an answer slot whose first half is already the action.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (286-288): “The review does not name this failure directly, so treat the diagnosis as my own; what it does support is the cause and the fix.”

Published: [Kispal 2008, Effective Teaching of Inference Skills for Reading: Literature Review, NFER (DCSF-RR031)](https://www.nfer.ac.uk/publications/effective-teaching-of-inference-skills-for-reading-literature-review/)

Against: The research note calls the diagnosis its own: "The review does not name this failure directly, so treat the diagnosis as my own; what it does support is the cause and the fix." (`grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md`, lines 286-288). It was "Written before the lesson is authored." (line 9), and nothing records learners using the frame.

<sub>criterion · format, demand, stem · universal · from g3, research · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Questions written for their own text

Write each question for its own text and teach no rule of thumb many texts break, such as checking the title or expecting the meaning or evidence in one sentence.

In the reading course's third review round, a generic routine, find the one sentence the story is about and check it against the title, was judged bad advice: a fable's meaning is a synthesis, and titles often don't tell the main idea. The course's response made questions bespoke to the text a rule, and its red-team taxonomy now checks both for generic questions and for the misconception they taught, that text evidence is a single sentence when it is often two ideas from different places (`grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md`, lines 79-80).

Quoted:

- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (79): “round-3: "find the one sentence + check the title" is bad advice — a fable's meaning is a synthesis, titles often don't tell the main idea”
- `grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md` (37): “5. **Questions bespoke to the text, not generic templates.**”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (80): “round-3: teaching that text evidence = a single sentence; often it's 2 ideas synthesized from different places”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (72): “A fable's meaning is rarely contained in one sentence.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (73): “Titles frequently do not state the main idea, so checking against the title is not a dependable rule.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (75): “but the question must be bespoke to the text.”
- `grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd` (81-82): “questions are bespoke to the text, never a generic template like "find the one sentence the whole story is about,"”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md` (60): “Do not turn a generic taxonomy label into a universal question script.”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (93): “bespoke questions”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/TOOLING.md` (53-55): “It does not judge whether a think-aloud is authentic, whether a question is text-bespoke, or whether teaching is effective.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (80): “The lesson may also embed the misconception that text evidence always points to one sentence.”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (95): “retiring "hunt for keywords" (many texts have no clean keyword)”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (75): “the question must be bespoke to the text.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (72): “- A fable's meaning is rarely contained in one sentence.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (73): “- Titles frequently do not state the main idea, so checking against the title is not a dependable rule.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (80): “Readers often have to synthesize two ideas from different places.”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/HUMAN-g3r-2026-07-20T11-20-06-019f7ed3-5205-72f0-a25a-caf13bf2a620.md` (139-142): “The I-do models the genuinely hard step (it rejects "outside knowledge alone" and models evidence as a synthesis of two pieces, which answers the round-3 "evidence is one sentence" note).”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-main-checkout-jul-work.patch` (20661): “| **Generic-not-bespoke question** | round-3: "find the one sentence + check the title" is bad advice — a fable's meaning is a synthesis, titles often don't tell the main idea | is the comprehension question bespoke to THIS text, or a generic template? |”
- `grade3-reading/course-renderer/docs/research/g4-u1-l1-what-is-an-epic.md` (211-213): “the first-sentence error is instruction-induced, since "kids are often taught that the first sentence of a paragraph states its main idea".”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/generation-contract.md inside it) (147-149): “Do not teach or imply that textual evidence is always one sentence.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md` (211-213): “the first-sentence error is instruction-induced, since "kids are often taught that the first sentence of a paragraph states its main idea".”

Against: none found

<sub>criterion · stem, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Rank the evidence, not just find it

In an evidence hunt, label each phrase a student can pick as key clue, other clue, weaker detail or distractor, give each its own feedback, then ask which is strongest.

A Grade 3 inference design breaks its modelled passage into short tappable phrases and labels each as a clue, an interesting detail or a distractor, with one compulsory key clue. Each label gets its own feedback, and once the clues are collected a quality check asks which clue best describes what the character wants. The Grade 3 standards sheet names the usual failure in choosing evidence as picking a random, interesting or nearby detail instead of the relevant one.

Quoted:

- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (146 (textutil text)): “Each phrase is labelled CLUE / INTERESTING / DISTRACTOR.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (159 (textutil text)): “"Some evidence is better than others. Tap what you think best describes what Aladdin wants."”
- `downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx` (sheet 'Standard components', cell E7): “Child picks a random, interesting, or nearby detail instead of the one that is relevant to the question.”
- `grade3-reading/ui-audit-2026-09-08/round-5/open-hunt/CAUSE-PROPOSAL-IMPLEMENTATION.md` (10): “The old renderer rejects/disables it and prints Good thinking, but one clue describes Captain Hook even better. Try again.”
- `grade3-reading/ui-audit-2026-09-08/round-5/open-hunt/CAUSE-PROPOSAL-IMPLEMENTATION.md` (26): “every correct clue banks immediately and comparative coaching belongs in the later pick phase.”
- `grade3-reading/ui-audit-2026-09-08/round-5/open-hunt/INDEPENDENT-REVIEW-by-film-finish.md` (9): “lines1727–1729 require every useful clue to bank immediately with comparative coaching reserved for the best-pick phase.”
- `grade3-reading/ui-audit-2026-09-08/round-5/open-hunt/INDEPENDENT-REVIEW-by-film-finish.md` (15): “Both useful clues bank in either order; neither one nor both alone completes.”
- `grade3-reading/course-renderer/docs/extras/alpharead-lesson-design-witw-part-1.md` (355): “"Ooh, that's an interesting one! It tells us who lives in the wood. But an even more powerful clue is hiding in the text..."”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (248): “The child has found three quotations and picks the two worth writing about.”

Against: none found

<sub>criterion · distractors, feedback, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Reading checks at moments of change

Place quick are-you-reading checks at moments of change, and keep them literal and answerable in about 2 seconds from the sentence just read.

The Grade 3 inference designs add a layer of first-read checks to the read-aloud: pure literal retrieval, answered in about 2 seconds, placed at moments of change such as a new character, a new place or a key object, with four short options all plausible to a drifting child and only one stated in the text. A built lesson kept the layer, because drifting readers lose the thread at changes, and set each check beside the still-visible text.

Quoted:

- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 10. The Wind in the Willows, Part 3 (FICTION, INFER) — v3 (new INFER design).docx` (85 (textutil text)): “Pure literal retrieval, answered in about 2 seconds, placed at moments of CHANGE.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (89 (textutil text)): “Quick "are you still reading?" checks, placed at moments of CHANGE (a new character arrives, the place changes, a key object appears).”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (89 (textutil text)): “Four short options, all plausible to a drifting child, only one stated in the text.”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (41): “Each first-read check is literal recall at a plot turn, beside the text | Drifting readers lose the thread at changes; look-back must be actually possible”
- `g9/transformer/src/mechanics/quick-check.js` (1): “// Quick check: one first-read question (who, what, how characters relate), three options, exactly one defensible.”
- `g9/transformer/src/mechanics/quick-check.js` (20-21): “TASK: one quick multiple-choice question that checks a first reading: who is speaking, what is happening, or how two characters relate. Not interpretation. A Grade 9 reader who has read the lines once can answer it.”
- `g9/transformer/v05/README.md` (9): “reading sequences (first-read checks, close reading, analysis, writing)”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/provenance/DECISIONS.md` (28): “Most current checks are literal/sequence questions, so a research criticism of interpolated inference is not automatically this case.”
- `grade3-reading/course-renderer/docs/extras/alpharead-lesson-design-plants-l1.md` (117): “Quick first-read FIND MCQs fire at moments of change (each new plant part introduced). FIND only — the answer is stated in the sentence just read; four short options all plausible to a drifting child”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (237): “And the spot checks across the reading are good: they keep comprehension cohesive across a long text, and they should stay.”
- `grade3-reading/artifacts/pp2-v3-design.txt` (90): “Light, literal retrieval checks placed at moments of CHANGE during the first read (a new place, a new character, a key object, a mood shift). FIND only: the answer is stated in the sentence just read.”

Against: none found

<sub>criterion · sequence, options, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Response type before response count

Choose the response type a skill needs (identify, complete or generate) before counting responses, and accept the pace that type allows rather than chasing a high count. One research synthesis cites about four to six responses a minute for new material, eight to twelve for review and one or fewer for open answers.

A research synthesis on opportunities to respond in early reading comprehension takes three response formats, identify, complete and generate, from Datchuk et al. (2024) and treats them as a ladder of demand. Its rule of thumb is to pick the type the skill requires and accept the rate that type allows, since a high number of responses per minute is not evidence of quality if it came from recognition questions alone. The commonly cited targets it gives are about four to six responses per minute when a child is learning something new, about eight to twelve when practicing material already taught, and about one per minute or fewer for open responses.

Quoted:

- `downloads/WF - Brainlift Opportunities to - 260724-110911.md` (113): “The rule of thumb is to pick the type the skill actually requires, then accept the rate that type allows rather than chasing a high count.”
- `downloads/WF - Brainlift Opportunities to - 260724-110911.md` (119): “The commonly cited targets are about four to six responses per minute when a child is learning something new, about eight to twelve per minute when practicing material already taught, and about one per minute or fewer for open responses that require composing or reasoning.”
- `downloads/WF - Brainlift Opportunities to - 260724-110911.md` (23): “A high number of responses per minute is not evidence of quality if the app reached that number by asking only recognition questions.”
- `downloads/WF - Brainlift Opportunities to - 260724-110911.md` (112): “Datchuk and colleagues describe three broad response formats.”
- `downloads/WF - Brainlift Opportunities to - 260724-110911.md` (199): “https://doi.org/10.1353/etc.2015.0009”
- `downloads/WF - Brainlift Opportunities to - 260724-110911.md` (120): “Council for Exceptional Children (1987), as cited in MacSuga-Gage and Simonsen (2015).”
- `downloads/WF - Brainlift Opportunities to - 260724-110911.md` (121): “Set the often-repeated targets of four to six responses per minute for new material and higher rates for review.”
- `downloads/WF - Brainlift Opportunities to - 260724-110911.md` (6): “for a PreK to Grade 2 comprehension app”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/BRAINLIFT.md` (204-205): “A build that chased the count would degrade the lesson while improving the metric.”

Published: [MacSuga-Gage & Simonsen 2015](https://doi.org/10.1353/etc.2015.0009) · [Datchuk et al. 2024](https://doi.org/10.1177/10534512241302712)

Against: The targets are second-hand, "Council for Exceptional Children (1987), as cited in MacSuga-Gage and Simonsen (2015).", and that source line gives only four to six responses per minute for new material and higher rates for review. The synthesis is written for a PreK to Grade 2 comprehension app.

<sub>criterion · format, demand, measurement · universal · from research · external-research · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Room for more than one position

An argument task's prompt and sources must leave room for more than one defensible position.

An AP evaluator lists arguability as a hard-fail dimension for long essays and document-based questions, and an outside judge's rubric fails a document set when all documents point to one obvious conclusion. An exploit study found the check passes when the rubric notes merely list two opposing thesis sentences, and recommended that the judge verify both are genuinely defensible from the curriculum. One way is to weigh one cause against another rather than confirm a single primary cause. A check must confirm that each alternative is really defensible, not merely opposed, that each source bears on the prompt and that the scoring guide is fully earnable from what the course teaches.

Quoted:

- `icloud-work/incept/inceptbench/docs/AP_EVALUATION.md` (143): “Prompt must allow for arguable thesis”
- `icloud-work/aptraining/apllm-history/runtime_assets/ib_satisfaction_kit_v1/raw_rubrics/dbq_evaluation.txt` (60): “All documents point to one obvious conclusion; no real analysis or argumentation is possible”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-005-leq-no-stimulus.md` (96-97): “currently passes if rubric_notes literally lists two opposing thesis sentences.”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-005-leq-no-stimulus.md` (97-99): “The judge should verify both are genuinely defensible from the curriculum, not just rhetorically opposed.”
- `icloud-work/evaluator/docs/reports/LATEST.md` (34): “DBQ | 109 | 1 | 4 | 99.1%”
- `icloud-work/evaluator/docs/reports/LATEST.md` (78): “document_diversity | 30 | 80 | 27.3%”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/leq_evaluation.txt` (58): “- Score 0.0: Only one valid position exists, making the prompt non-argumentative”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/dbq_evaluation.txt` (60): “- Score 0.0: All documents point to one obvious conclusion; no real analysis or argumentation is possible”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/dbq_evaluation.txt` (55): “- Score 0.0: One or more documents are irrelevant to the prompt topic”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/leq_evaluation.txt` (22): “- Score 0.0: Rubric is unachievable (e.g., requires evidence that doesn't exist in the curriculum)”
- `icloud-work/incept/inceptbench/docs/AP_EVALUATION.md` (143): “| `prompt_arguability` | LEQ, DBQ | Prompt must allow for arguable thesis |”
- `icloud-work/ap-social-studies-generator/data/model_findings.md` (1112): “- `specification_compliance` 43% — model uses "primary cause/primarily responsible" framing → binary thesis”
- `icloud-work/ap-social-studies-generator/data/model_findings.md` (1114): “- Pattern: "primary cause" framing generates falsifiable yes/no questions instead of nuanced analytical prompts”
- `icloud-work/ap-social-studies-generator/docs/archive/GENERATOR_STATUS.md` (27): “- Prompts are genuinely arguable — students can take multiple positions”
- `icloud-work/ap-social-studies-generator/curriculum/ceds/ap-european-history-ced.pdf` (pdftotext -layout output, line 12700): “Evaluate whether the Thirty Years’ War was fought primarily for religious or primarily for political reasons.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/dbq_evaluation.txt` (63): “- Score 0.0: All documents point to one obvious conclusion; no real analysis or argumentation is possible”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/leq_evaluation.txt` (58): “- Score 0.0: Only one valid position exists, making the prompt non-argumentative”
- `g9/transformer/src/mechanics/debate.js` (45): “a debate on the text that a Grade 9 reader could take either side of, with a”
- `g9/transformer/src/mechanics/debate.js` (82): “Can a Grade 9 reader defend side_${k}, as an answer to question, with a reason from passage?”
- `g9-transformer-runs/blocks/90a1089f3e8d7ad5.json` (80-84): “"p": 0.86,”
- `g9-transformer-runs/blocks/90a1089f3e8d7ad5.json` (115-116): “"verdict": "holds", "p": 0.82”
- `g9/transformer/src/mechanics/video-essay.js` (132): “Could a careful reader defend left_${k} from passage, as an answer to lesson_question?”
- `g9-transformer-runs/blocks/34c293906aa945a2.json` (41): “"label": "Speech Is Weak",”
- `g9-transformer-runs/blocks/34c293906aa945a2.json` (48): “"label": "Action Is Powerful",”
- `g9-transformer-runs/blocks/34c293906aa945a2.json` (83): “Re-examine the two readings presented, which both place long term power on the side of physical action rather than speech.”
- `g9-transformer-runs/decisions/34c293906aa945a2.json` (1003): “"value": 0.78,”
- `g9-transformer-runs/decisions/34c293906aa945a2.json` (1020): “"value": 0.89,”
- `g9/transformer/src/mechanics/video-essay.js` (132): “Beat ${k + 1}: the first reading can be defended”
- `g9-transformer-runs/blocks/34c293906aa945a2.json` (354): “"p": 0.78,”
- `g9-transformer-runs/blocks/34c293906aa945a2.json` (370): “"p": 0.89,”
- `g9/transformer/src/mechanics/debate.js` (72): “norm(A.label) !== norm(B.label) && norm(A.counter) !== norm(B.counter)”
- `g9/transformer/src/mechanics/debate.js` (82): “as an answer to question, with a reason from passage?”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “per side: 'Is this side defensible from the text?' (both must hold)”
- `othello-archive/sources/act1/KB - Overview.csv` (147): “""how does Shakespeare present Desdemona as defiant and dutiful?"" is descriptive, not ""X or Y"".”
- `othello-archive/sources/act1/KB - Overview.csv` (140): “TASK 3 evaluate (""X or Y?"").”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (232): “Highlight "to what extent" and "entirely" as the evaluative commands; gloss "serve my turn" as use him for my own ends.”
- `othello-archive/server/tasks/oral.mjs` (50): “Either choice can be secure.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (150): “A reasoned yes, no, or qualified view is permitted.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (606-607): “The question must support more than one defensible argument path. A document set should not encode a single thesis through captions or ordering.”

Against: in one evaluator's report, document-based items passed overall at 99.1% while only 27.3% passed its document-diversity check, so a related rule did not gate the result. Official prompts also use 'primarily' when they pose two alternatives, so the judge's dislike of 'primary cause' framing may be its own preference. The gain after banning that framing, +15.9 points, came on 20 essay items, and the project counted swings of ±14 points at 17 to 24 items as not statistically meaningful; specification failures were still 88% of the remaining essay failures (`icloud-work/ap-social-studies-generator/data/model_findings.md`).

<sub>criterion · stem, stimulus, demand · universal · from ap · adopted-rule · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Sample answers cover every part

Make sure every part a question asks for appears in its sample answers, not only in the parts the student sees. One history short-answer item's sample responses failed to answer the religious justifications and gender roles its prompt required.

In a calibration of AP history items, a short-answer item's sample responses failed to answer the religious justifications and gender roles its prompt required. The fix asked the answer-key verifier to check that every requested component appears in the sample responses, not just in the student-facing parts. Failure analysis of one run's export also counted 21 sample-answer errors.

Quoted:

- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md` (46): “- `apush-u1-0760-saq-hard`: SAQ sample responses failed to answer religious justifications and gender roles required by the prompt.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/CANDIDATE_CALIBRATION_AND_149_GATE_20260520.md` (51): “- SAQ answer-key verifier must ensure every requested component appears in the sample responses, not just in the student-facing parts.”
- `icloud-work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/next_live_run_prep.md` (25): “**Symptom**: 21 sample_response_error + 41 out_of_period + 39 factual_error + named-content-trap families (`content_lakota_pre1607` 14, `content_muscovy_east_india` 7, `content_navigation_acts` 3, `content_requerimiento_overclaim` 2) = chain hallucinating concrete, name-able anachronisms in Unit 1 content.”

Against: none found

<sub>criterion · scoring-guide, key · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Say how many answers to choose

A multiple-select item says in its stem how many answers to choose, or to choose all that fit, and that number matches the key. A stem that says "select two" while three answers are keyed fails.

When the evaluator gained selectable-text and two-part evidence items, its audits began to fail a multi-answer item that leaves the student guessing how many to pick, and one whose stated count or selection limits disagree with the number of keyed answers (`shadow-bench/src/inceptbench/prompts/question/hot_text_evaluation.txt`). The two-part audit applies the same rule to an evidence part with several keys (`shadow-bench/src/inceptbench/prompts/question/ebsr_evaluation.txt`). A stated count, a 'select all that' framing, or limits that pin the number each meet it.

Quoted:

- `shadow-bench/src/inceptbench/prompts/question/hot_text_evaluation.txt` (83-84): “- the key has more than one span AND `student_can_determine_how_many_to_select: NO` (the student is left guessing how many spans to pick); OR”
- `shadow-bench/src/inceptbench/prompts/question/hot_text_evaluation.txt` (85-86): “- a stated count, `min_selections`, or `max_selections` disagrees with `number_of_keyed_answers` (e.g. stem says "select two" but three ids are keyed, or `max_selections` is below the keyed count).”
- `shadow-bench/src/inceptbench/prompts/question/ebsr_evaluation.txt` (118-119): “When Part B is multi-select, the stem must tell the student how many pieces of evidence to select (e.g. "Select two…"); a multi-key Part B with no stated count fails here.”
- `shadow-bench/src/inceptbench/prompts/question/hot_text_evaluation.txt` (75-77): “Set `student_can_determine_how_many_to_select: YES` if ANY of these hold: the stem states a count; the stem frames an unbounded "select all that [criterion]" task; OR `min_selections` / `max_selections` are present and pin the number to select”
- `shadow-bench/` (commit 246a67d) (33-35): “HT-2's no-count MUST-FAIL clause wrongly failed multi-select hot-text whose selection count is fixed by min_selections/max_selections, and would also have failed valid 'select all that [criterion]' stems.”
- `icloud-work/incept/nova_forge/EXECUTIVE_SUMMARY.md` (79): “| **MSQ** | 21.43% | 0.00% | 6.15% | 21.08% | 15.27% |”
- `icloud-work/incept/nova_forge/EXECUTIVE_SUMMARY.md` (81): “**Key Finding:** MSQ (Multiple Select Questions) have the lowest pass rate overall, with Grade 6 having 0% pass rate on MSQs.”
- `icloud-work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md` (83): “- **Fix:** Add: "Select 1 correct answer." after the stem to remove ambiguity.”
- `icloud-work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md` (84): “- **Issue:** Missing guidance on how many answers to choose creates ambiguity for students.”
- `icloud-work/incept/nova_forge/EXECUTIVE_SUMMARY.md` (257): “**Problem:** Missing "Select all that apply", unclear wording”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md` (45): “**MSQ** — stem states the explicit count (`"Which TWO…"`).”

Against: The first version over-fired: it 'wrongly failed multi-select hot-text whose selection count is fixed by min_selections/max_selections, and would also have failed valid 'select all that [criterion]' stems' (`shadow-bench`, git commit 246a67d, lines 33-35), and was narrowed to accept a stated count, select-all framing or limits that pin the number. The 0.00% rests on a small group: '- **Grade 6 MSQ (20 questions):** 0% pass rate - all failing' (`icloud-work/incept/nova_forge/EXECUTIVE_SUMMARY.md`, line 296). The low pass rate also mixes causes, among them keys that left out true options (`icloud-work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md`), so it is not the missing instruction's effect alone.

<sub>criterion · stem, key, format · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Script the conversational check

Run a conversational check as a fixed script, with set prompts, a capped number of follow-ups and declared supports, because free chat can lead the witness. One suggested turn budget is one prompt and up to two follow-ups chosen from a fixed menu.

The assessment pattern library in the reading project's knowledge base warns that ungoverned model prompts in an oral or conversational task can lead the witness, and that free conversation makes unequal demands unless a state machine is locked (`grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd`). Its design properties are fixed, neutral prompt wording, explicit branches with capped turns and an end rule for when the answer can't be reached, follow-ups chosen from a fixed menu, and no spontaneous hints unless they are tagged as support and named in the mastery claim.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd` (564): “State machine, not free chat”
- `grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd` (555): “Ungoverned LLM prompts can lead the witness (construct creep and validity loss).”
- `grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd` (557): “Free conversation creates unequal cognitive demands unless you lock a state machine.”
- `grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd` (562): “Set min/max turns and branching conditions (e.g., 1 prompt + up to 2 follow-ups).”
- `grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd` (546): “Short, branched follow-ups targeted at a known misconception or missing warrant (e.g., ≤2 follow-ups chosen from a fixed menu).”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (72): “The recovery was declared before execution in the frozen journey and next-session guide; it was not adapted to the first hint.”
- `g9/player/content/archivist-checks-v7.json` (2): “Own-words steps are followed by one scripted probe in”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (338): “Nothing tells the child, or the app, when the quote has been understood. A stem-based task ends when the paragraph is complete; a chat ends when someone gives up.”
- `othello-archive/server/tasks/close.mjs` (51): “If it is an attempt: push back ONCE.”

Against: none found

<sub>criterion · format, integrity · universal · from g3 · external-research · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Select-all options stand alone

In a select-all question every option must be decided by the text alone, and finding one right answer must not point to another. Of 1,346 select-all items that had passed structural checks, 0 were usable: the whole pool leaked.

A grade 5 select-all pool was found 100% leaked: none of 1,346 items that had passed structural checks was usable (`grade3-reading/artifacts/alpha-read-packager/generator/g5/MSQ_REGEN_GUIDE.md`, line 3). Its regeneration guide gives the reasons: each option is judged true or false on its own, so world knowledge reaches further than in a single-choice item, and a student who knows one right answer from school can guess the other; the single-choice fixes are necessary but not sufficient (the same file, lines 7-21). It requires every option to rest on a detail of the passage and the right answers not to be paired by theme (the same file, lines 25-42).

Quoted:

- `grade3-reading/artifacts/alpha-read-packager/generator/g5/MSQ_REGEN_GUIDE.md` (3): “**Status:** MSQ pool is 100% leaked (0 of 1,346 structural-pass items usable).”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/MSQ_REGEN_GUIDE.md` (12): “In MSQ each option is judged true/false independently.”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/MSQ_REGEN_GUIDE.md` (41): “**5. Knowing one correct answer must not help you find the other.**”

Against: none found

<sub>criterion · options, format, integrity · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Selectable text comes in whole pieces

Make each selectable piece of text a whole word, phrase, clause or sentence, never a fragment cut mid-word or mid-phrase.

The evaluator's rubric for items where students select parts of a text audits every selectable span, asking whether it is a whole word, phrase, clause or sentence rather than a mid-word fragment or an arbitrary cut that distorts meaning (`shadow/bench/src/inceptbench/prompts/question/hot_text_evaluation.txt` lines 115-120). A span that begins or ends mid-word, or slices a phrase into a fragment a student can't evaluate on its own, fails the item's clarity outright (lines 122-124).

Quoted:

- `shadow-bench/src/inceptbench/prompts/question/hot_text_evaluation.txt` (120): “is the span a whole word, phrase, clause, or sentence rather than a mid-word fragment or an arbitrary cut that distorts meaning?”
- `shadow-bench/src/inceptbench/prompts/question/hot_text_evaluation.txt` (122-124): “**MUST-FAIL** (`clarity_precision = 0.0`) if any selectable span has `is_coherent_unit: NO` (e.g. a span begins or ends mid-word, or slices a phrase so the selectable text reads as a fragment that a student cannot evaluate on its own).”
- `g9/transformer/src/glue/threejs-render.js` (85): “Up to n quotes from a ranked pool of units, the best first, shown in the text's order: whole clauses first (a line and”
- `g9/transformer/src/glue/threejs-render.js` (86): “the rest of its sentence, three lines of one speech at most), then single lines; never a line in `taken` or one the”
- `g9-transformer-runs/decisions/963297774d627c12.json` (22): “"L4": "L4 Half sunk a shattered visage lies, whose frown,",”
- `g9-transformer-runs/decisions/963297774d627c12.json` (23): “"L5": "L5 And wrinkled lip, and sneer of cold command,",”
- `g9-transformer-runs/decisions/963297774d627c12.json` (33): “"instructions": "Does line L4 in lines, read on its own, give clear evidence for the claim?"”
- `g9-transformer-runs/decisions/963297774d627c12.json` (60): “"value": 0.16,”
- `g9-transformer-runs/decisions/963297774d627c12.json` (217): “"value": 0.58,”
- `g9-transformer-runs/decisions/38cf6a0077428ec2.json` (22): “"L9": "L9 [IAGO] Heaven is my judge, not I for love and duty,",”
- `g9-transformer-runs/decisions/38cf6a0077428ec2.json` (90): “"value": 0.35,”
- `g9-transformer-runs/decisions/38cf6a0077428ec2.json` (460): “"value": 0.33,”
- `g9-transformer-runs/decisions/815626dc60c1b455.json` (90): “"value": 0.35,”
- `g9-transformer-runs/decisions/815626dc60c1b455.json` (458): “"value": 0.24,”
- `g9-transformer-runs/blocks/963297774d627c12.json` (13): “"reveal": "The ruined face shows a frowning mouth with a cold expression, showing the ruler's harsh authority.",”
- `g9/transformer/src/mechanics/evidence-hunt.js` (75): “Does line, read on its own, give clear evidence for claim?”
- `g9/transformer/src/mechanics/evidence-hunt.js` (82): “if (verdict === "fails") return missed(item, action);”
- `g9/transformer/src/mechanics/evidence-hunt.js` (83): “// the judge unsure or absent: the hint, no miss, and the line kept for review”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (1237): “inspect reached replay buttons: one ends with Mrs. and the next is Craven died.”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (1246): “If the correct evidence spans two sentences, present them as one selectable thing.”
- `grade3-reading/.claude/skills/lesson-build/SKILL.md` (63-64): “A quote that is a fragment of a sentence is not a sentence — tap targets are whole sentences, byte-exact (validate-passage-refs).”

Against: none found

<sub>criterion · options, format · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Some items with two right answers

Include some items with more than one right answer, such as choose-two items, so learners don't come to expect exactly one right answer to every question. One reading course's task bank adds a select-two item with exactly two correct answers.

The task bank in a Grade 3 reading course's lesson design, whose example stems are quoted from a released Grade 3 item sampler, adds a select-two item: a multiselect with exactly two correct answers, usable on any text. It gives its reason as breaking the habit that every question has one answer.

Quoted:

- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (180): “Stems in the third column are quoted verbatim from the released Grade 3 item sampler unless marked otherwise.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (242): “A multiselect with exactly two correct answers.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (245): “Any text. Breaks the habit that every question has one answer.”

Against: It is a design decision, and no effect on learners was measured.

<sub>criterion · format, key · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Spread the right answer's position

Spread the right answer's position evenly across a set, and check it in code. In one set, 29 of 40 had it first.

Across one four-lesson arc in the reading project, 29 of 40 multiple-choice questions had the right answer first and
the fourth position appeared once; a child who noticed would beat a 72% base rate by always choosing A
(`grade3-reading/artifacts/arc-audit/SIM-REVIEW-D5-D6-D11-D13.md`). Rebalanced, another set went from 56% choice A to
an even spread over 117 questions
(`grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/RESPONSE-MATRIX.md`). My own
film player lists the right option first in 5 of its 7 choice steps and never shuffles them
(`g9/player/content/archivist-checks-v7.json`, `g9/player/index.html`).

Quoted:

- `icloud-work/ap-social-studies-generator/docs/archive/TECHNICAL-DECISIONS.md` (106): “Fixed answer bias (all answers were "B") by shuffling options after generation.”
- `icloud-work/inceptbench/docs/MATH_VERIFIER.md` (74): “chi-square answer balance analysis”
- `grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd` (50): “correct answers were ~75% option "A"”
- `grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd` (56): “Key-position/length balance needs an authoring-time check (12/19 A-keys shipped before the lens).”
- `icloud-work/incept/inceptbench/docs/MCQ_SET_PASS_SPEC.md` (224): “### 3.8 Answer Balance (Non-critical) — Chi-Square Gate”
- `icloud-work/incept/inceptbench/docs/MCQ_SET_PASS_SPEC.md` (226): “This is computed **programmatically** before the LLM evaluator runs. The LLM is instructed to use the programmatic score exactly.”
- `icloud-work/incept/inceptbench/docs/MCQ_SET_PASS_SPEC.md` (228): “**Pass (1.0) if**: Chi-square goodness-of-fit p-value ≥ 0.60”
- `icloud-work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py` (201): “Use locked answer keys A, C, and B in that order.”
- `icloud-work/ap-social-studies-generator/docs/archive/EXPERIMENT_RESULTS_2026-02-18.md` (118): “- Lower temperature made answer bias worse (9/10 picked "B")”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (77): “79% of correct answers in a generated course sat at option position A, and the correct option was systematically the longest”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_set_evaluation.txt` (179): “- `answer_balance`: Are answer positions distributed well? (Collection property)”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_set_evaluation.txt` (241): “- Non-critical metrics: `concept_coverage`, `difficulty_distribution`, `non_repetitiveness`, `test_preparedness`, `answer_balance`”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_set_evaluation.txt` (253): “| 0 | 1-2 | 0.75 - 0.84 | INFERIOR |”
- `icloud-work/aptraining/helpers/serve/fewshot_mcqset.py` (7-8): “This lifted IB MCQ_SET 3.3% -> 26.7% and fixed answer_balance 0 -> 30/30.”
- `icloud-work/aptraining/handover/2026-05-01_session_end/SHADOW_HANDOVER.md` (60): “| MCQ answer-A bias | A=64.5%, B=27%, C=7.8%, **D=0.7%**, E=0% (vs uniform 25% expected) |”
- `icloud-work/aptraining/handover/2026-05-01T1039Z_data_session/HANDOVER.md` (287): “Build ran, validated row-count, missed the structural defect.”
- `grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` (93-94): “- answer position, option length, distractor function, enemy items, blueprints, and independent cold review are form-level obligations;”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (66): “79% of correct answers in a generated course sat at option position A, and the correct option was systematically the longest”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md` (51): “Form-level answer-position, option-length, duplicate, enemy-item, and blueprint reports.”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (151-152): “does not detect within-lesson position *runs* (a student-visible streak that a course-wide histogram averages away).”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (168): “**12 of 19 single-select keys at A, with a 5-run.**”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (169-170): “Post-fix (independently recomputed): spread **A8/B6/C4/D4 over 22 items, max within-lesson run 2**”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (165-166): “**79% of correct answers sat at position A and the key was systematically the longest**”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx` (10 (textutil text)): “The correct option rotates across A/B/C/D”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx` (10 (textutil text)): “Correct positions in order of appearance: B, D, A, C, B.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx` (8 (textutil text)): “The two "incorrect" statements land in different positions in every REFINE”
- `grade3-reading/ti-courseplans/docs/course-formula-agents.md` (225): “the G4 pull found **79% of MCQ correct answers at Choice A**”
- `grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md` (153-154): “79% of correct answers in a generated course sat at option position A, and the correct option was systematically the longest”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md` (119-120): “Dose teach MCQs bypassed the QTI debias pass, so rebalancing the graded bank never touched them: hook 69% A, we-do 53% A, **vocab 98% A** (53 of 54).”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md` (123): “fails above 40% for any item type”
- `ap-agent-memory/project_v39_dataset_corruption_smoking_gun.md` (24): “**Defect 2 — MCQ answer distribution (n=293 MCQ rows):**”
- `ap-agent-memory/project_v39_dataset_corruption_smoking_gun.md` (25): “- A: 64.5% (189) — vs expected 25%”
- `ap-agent-memory/project_v39_dataset_corruption_smoking_gun.md` (56): “3. Enforce uniform answer distribution at row-emit time for MCQ/MCQ_SET (rotate correct-answer position deterministically across A/B/C/D)”
- `shadow-bench/` (commit ef4a069) (9-10): “- G9 position skew: the correct answer sitting in the same slot too often (e.g. 79% Choice A in a real G4 audit) lets a student guess by position.”
- `shadow-bench/` (commit ef4a069) (15-17): “Report-only at lesson scale — a single lesson has too few items to gate reliably; score-gating happens course-side (#1104) where item counts are large”
- `shadow-bench/` (commit ef4a069) (19-20): “- tools/item_tells.py: pure functions + is_tell/is_skewed thresholds (>=4 items & >60% for length; >=8 items & >50% for position).”
- `shadow-bench/` (commit e1e761c) (7-9): “BAML hallucinated A/B/C/D answer positions, the chi-square test then reported a non-random distribution”
- `icloud-work/incept/inceptbench/docs/MCQ_SET_PASS_SPEC.md` (256): “**The golden rule: for sets of ≤4 questions, every question MUST have a different correct answer position.**”
- `icloud-work/incept/aplit-quiz-generation/convert_quiz_format.py` (43): “random.shuffle(options)”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-014-timeline-AND-015-cartoon-FAILED.md` (22): “- 3 of 4 fail answer_balance (my hand-crafted A/B/C/D distribution wasn't varied enough)”
- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md` (107): “- Answer balance for MCQ_SET uses structured extraction plus chi-square; p >= 0.60 passes, otherwise fails.”
- `icloud-work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_repair_loop_clean3/loop_summary.jsonl` (1): “"failed": 32, "pass_rate": 0.68, "zero_metrics": {"answer_balance": 15”
- `icloud-work/ap-social-studies-generator/data/model_findings.md` (528): “**CRITICAL INSIGHT:** MCQ_SET is failing almost entirely because all 3 questions have the same correct answer letter (e.g., A/A/A or B/B/B).”
- `icloud-work/ap-social-studies-generator/data/model_findings.md` (615): “- **answer_balance: NOT PRESENT** ← constraint completely fixed this”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/mcq_set/evaluation.txt` (372): “- Chi-square probability >= 60% (if provided)”
- `grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md` (47): “79% of correct answers sat at option position A”
- `grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd` (50-51): “(correct answers were ~75% option "A" → shuffled ~even A/B/C/D)”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (56): “positional bias of B ≈ 30%, C ≈ 29% vs. A ≈ 19%, D ≈ 22%”
- `icloud-work/aptraining-crystal-copy-20260521/variant-calibration-lab-snapshot/next_live_run_prep.md` (58): “**Symptom**: 62 of 71 MCQ_SET failures fire `educational_accuracy` aggregate; 61 fire `answer_balance` (children share correct letter); 47 fire `redundant_questions` (children test same skill).”
- `grade3-reading/knowledge_bot/knowledge/kb-0187-skill-catalogue-and-workflows-index.qmd` (97): “"first run caught a recurring rail defect and a 72.5% answer-position skew."”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md` (47): “L4's first round had 72.5% on one position”
- `grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md` (29): “| LENS1-03 | Key-position imbalance, 12/19 A with a 5-run (must-fix)”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-29/census-pp-L4-L7.txt` (6): “every blank's answer sits at option 0: [0, 0, 0]”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (119): “The word bank lists answers in the same order as the blanks”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/KB_FURTHER_IMPROVEMENTS.md` (117): “The correct fix is *re-keying Form A's static options*, not shuffling.”
- `grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md` (96): “79% (correct at position A, G4 census n=100 MCQ + 116 EBSR)”
- `grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md` (29): “Key-position imbalance, 12/19 A with a 5-run (must-fix)”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (119): “The word bank lists answers in the same order as the blanks (free, swords, sea), so tapping the first three words in order gets everything right without reading”
- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-28-R13.md` (40): “12 pass distinct-letters / 40%-cap / no-triple-run.”
- `grade3-reading/knowledge_bot/knowledge/kb-0227-g3-branch-hygiene-pr634-prep-2026-09-24.qmd` (60-62): “classifies answers 5 ways (full/partial/off/brief/silent), 120 clips on the pinned course-TTS route, all Puck-stamped; the off-branch answer no longer sits last in every lesson.”
- `ti-courseplans-audit/docs/course-formula-agents.md` (225): “the G4 pull found **79% of MCQ correct answers at Choice A**”
- `ti-courseplans-audit/docs/course-formula-agents.md` (255): “`shuffle="true"` in the authored XML neutralizes an answer-position skew ONLY if each renderer honors it.”
- `grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd` (50-51): “**answer-position bias fixed** (correct answers were ~75% option "A" → shuffled ~even A/B/C/D)”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx` (8 (textutil text)): “The two "incorrect" statements land in different positions in every REFINE, and the Modelling Moment set and the Part 3 set use different orders from each other.”
- `grade3-reading/ti-courseplans/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md` (53): “79% of MCQ correct answers sit at Choice A (expected ~25%)”
- `grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (151-152): “and does not detect within-lesson position *runs* (a student-visible streak that a course-wide histogram averages away).”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (2020): “Test makers systematically over-place correct answers in middle positions (B ≈ 30%, C ≈ 29% vs. A ≈ 19%, D ≈ 22% across large-scale exams).”
- `shadow-content-eval/reports/G3-U1-L12-review.md` (86): “12. **Answer position: A is the answer in 10 of 20 visible four-option items, and D in only 1.**”
- `shadow-content-eval/reports/G3-U1-L11-review.md` (79): “All 7 blanks (p15b ×4, p24b ×3) put the correct word as option 1: Mole, Rat, underground, Toad, timid, cheerful, eerie.”
- `shadow-content-eval/reports/G3-U1-L14-review.md` (70): “The script's ANSWER-BIAS check skips routine checks and dialogue items, so it missed two runs:”
- `shadow-content-eval/reports/G3-U2-L1-review.md` (238): “| 1 | Answer position (12 of 18 keyed B) | **Fixed.** Keys are spread across positions. |”
- `icloud-work/aptraining/.agent/research/inference_clean.md` (46): “Each block traces to a Gate finding ("Gate 3: 80% of MCQ_SET failures were answer_balance").”
- `ap-agent-memory/project_v39_dataset_corruption_smoking_gun.md` (37): “Defect 2 → degrades `distractor_quality` + `difficulty_alignment` (2/11 dimensions) because the model learns answer-position bias real AP exams don't have.”
- `aptraining-local/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md` (59): “All children sharing one correct letter is a set-level smell.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md` (89): “Q2 content was fixed, but answer keys clustered on A/B and scored 0.84.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md` (75): “Record answer-key distribution for MCQ_SET and repair when balance caps otherwise-good sets.”
- `g9-transformer-runs/blocks/4c5df03f78a26e6e.json` (22): “"best": 1,”
- `g9-transformer-runs/blocks/8d4652dbccf037b9.json` (23): “"best": 1,”
- `g9-transformer-runs/blocks/e47511c58b5dd64c.json` (23): “"best": 1,”
- `g9-transformer-runs/blocks/eb9231d930fa07c4.json` (23): “"best": 1,”
- `g9/transformer/src/mechanics/direct-the-line.js` (68): “context: before, deliveries: item.deliveries”
- `g9/transformer/src/mechanics/worked-model.js` (120): “rebuild: item.rebuild.parts.map((p) => (p.options ? { options: p.options } : { text: p.text }))”
- `g9/transformer/src/mechanics/direct-the-line.js` (30): “"best": 0, "why": ""”
- `g9/transformer/src/mechanics/direct-the-line.js` (27): “best: the index of the delivery that fits.”
- `g9/transformer/src/glue/animated.js` (146): “in alphabetical order, so neither the first card nor the first option is the gap's word”
- `g9/transformer/test/animated.test.mjs` (94): “in alphabetical order: the first card is not the gap's word”
- `g9/transformer/src/mechanics/key-words.js` (100): “the study set in alphabetical order, and the gaps with their cues, so no gap lines up with its word”
- `g9/transformer/src/mechanics/key-words.js` (100): “// the study set in alphabetical order, and the gaps with their cues, so no gap lines up with its word”
- `g9/transformer/src/glue/animated.js` (146): “// in alphabetical order, so neither the first card nor the first option is the gap's word”
- `g9/transformer/src/glue/animated.js` (149): “const g = it.words[0], at = g.gap.indexOf(BLANK);”
- `g9-transformer-runs/blocks/cd006e767ac5b219.json` (10): “"word": "consecrate",”
- `g9-transformer-runs/blocks/cd006e767ac5b219.json` (65): “"word": "consecrate",”
- `g9-transformer-runs/blocks/fa497dafbb0eb7c2.json` (14): “"answer": 1,”
- `g9-transformer-runs/blocks/9a28237802fccd82.json` (14): “"answer": 1,”
- `g9-transformer-runs/blocks/5722a3741161394e.json` (53): “"answer": 1,”
- `g9-transformer-runs/blocks/a75bd9643fa602d9.json` (36): “"answer": 1,”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “The 9 cached QC blocks have the key at positions 0, 1 and 2 three, five and one times.”
- `g9/transformer/src/mechanics/quick-check.js` (83): “view(item) { return { kind: "choice", stem: item.stem, options: item.options }; },”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “Order options with seededOptionOrder(options), with no avoidFirst, read from the course-renderer mirror.”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “Map indices back in respond(), and log the order with the tick.”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (19): “79% of MCQ corrects at Choice A”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (19): “skew is only exploitable if a renderer serves authored order; either way it fingerprints generator bias”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “A grep finds no shuffle in src or web, nor in the animated build.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (63): “the correct option first far more often than not — so the answer sat on the rendered A in”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (64): “13 of 18 meaning checks (72%) under tidy letters. Re-lettering is not debiasing. If you add”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/CONTENT-SCHEMA.md` (274): “Option order is AUTHORED order and is never shuffled”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/CONTENT-SCHEMA.md` (359-360): “nothing pins its options' position distribution (correctly so — the order is authored on purpose and never shuffled)”
- `grade3-reading/course-renderer/content/lesson-plans/g3-u2-l1.json` (1081): “The book renders MCQ, routine checks, dialogue and video checkpoints in AUTHORED order (verified by screenshot + src: questions.tsx Mcq/CheckpointQuestion use ABCD[i], vocabRoutine and dialogue map in order); validate-contracts scores the SEEDED order (seeded-option-order.mjs).”
- `grade3-reading/course-renderer/content/lesson-plans/g3-u2-l1.json` (1081): “B fell from 12/18 to 6/18.”
- `grade3-reading/course-renderer/content/lesson-plans/g3-u2-l1.json` (748): “The engine re-orders every option set at render time through the course-wide seeded debias shuffle, so the AUTHORED positions are not the positions a child sees, and both sets first landed on 3 and 4.”
- `grade3-reading/course-renderer/authoring/inputs/rule-packs/reading-g3.json` (62): “Tracked per item family, because a lesson whose four story checks rotate while its two vocabulary forms both sit on A is exactly what a pooled count hides.”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/markdown/PLAN-EVALUATION.md inside it) (182-183): “Position-fingerprint check (G4 red team found 79% of correct answers at Choice A)”
- `incept-package-hub/.artifacts/source/Grade 5 Reading - Complete Course Review.zip` (Grade 5 Reading - Complete Course Review/audit/full-course-review-red-team-interim-2026-07-20.md inside it) (35): “Full-course choice order is balanced: direct keys A/B/C/D = 41/41/41/40; EBSR Part A = 14/14/14/13; Part B E/F/G/H = 14/14/14/13; all six MSQ pairs occur 9 or 10 times.”
- `incept-package-hub/.artifacts/source/Grade 5 Reading - Complete Course Review.zip` (Grade 5 Reading - Complete Course Review/audit/full-course-review-red-team-interim-2026-07-20.md inside it) (37): “I07 authored keys cover all nine derangements within one count, and target rows cover all 24 source-order permutations within one count.”
- `incept-package-hub/.artifacts/source/Grade 5 Reading - Complete Course Review.zip` (Grade 5 Reading - Complete Course Review/audit/full-course-review-red-team-interim-2026-07-20.md inside it) (17): “Balanced authored order is an authoring safeguard, not proof that the production delivery application's runtime shuffles.”
- `othello-course-renderer-draft/repo/authoring/inputs/rule-packs/reading-g3.json` (62): “Tracked per item family, because a lesson whose four story checks rotate while its two vocabulary forms both sit on A is exactly what a pooled count hides.”
- `othello-course-renderer-draft/repo/docs/qa/new-lesson-qa-invariants.md` (171-172): “**F4. The rendered answer key is unbiased**: ≥3 letters, no letter above 40%, never three in a row, in the child's walk order.”
- `othello-course-renderer-draft/repo/docs/qa/new-lesson-qa-invariants.md` (172-174): “*Check: validate-contracts distribution gate (salt is the tunable, the gate never is).*”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (456): “The rendered answer key is unbiased : ≥3 letters, no letter above 40%, never three in a row, in the child's walk order.”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/audit/full-course-review-red-team-interim-2026-07-20.md inside it) (35): “- Full-course choice order is balanced: direct keys A/B/C/D = 41/41/41/40; EBSR Part A = 14/14/14/13; Part B E/F/G/H = 14/14/14/13; all six MSQ pairs occur 9 or 10 times.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “The authored direct-response groups are balanced within one across positions.”
- `grade3-reading/artifacts/signoff-packet/FIXES-CURATED-2026-08-31.md` (33): “Authored answer-key positions rebalanced (72.5% at A → ≤31% per lesson)”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-23.md` (9-11): “**The off-branch answer sat last in all four lessons.** D5.13 / D11. `answer_index` was 3 on L4, L5, L6 and L7, so a child routed to the `off` branch after a wrong answer could pick the last option every time and be right.”
- `grade3-reading/course-renderer/docs/qa/new-lesson-qa-invariants.md` (171-172): “**F4. The rendered answer key is unbiased**: ≥3 letters, no letter above 40%, never three in a row, in the child's walk order.”
- `othello-archive/src/content/practice.ts` (44): “{ options: ['to obey a leader', 'to run away', 'to give orders'], answer: 'to obey a leader' }”
- `grade3-reading/ti-courseplans/courses/g2-reading/brainlifts/v0.3.md` (84-85): “incumbent AlphaLiteracy question bank is **4% inference, sequence-schema in only ⅓ of stories, 48% of answer keys on option A, templated stems**”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/generation-contract.md` (63): “across positions, **not 79% Choice A** (the G4 red-team fingerprint); verify shuffle on both”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/markdown/PLAN-EVALUATION.md inside it) (182-183): “(G4 red team found 79% of correct answers at Choice A)”
- `othello-course-renderer-draft/repo/docs/process/CONTRACT-SIGNOFFS.md` (288-289): “validate-contracts holds it to the mcq bar (four options, the answer never first, never the single longest, a 1.3x length band)”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT1-VERTICAL-SLICE.md inside it) (36): “two original source-based MCQ sets, eight questions total, with balanced A/B/C/D answer positions and answer and distractor rationales;”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (67): “L4's 13 MCQ items split A/B/C/D = 4/3/3/3 (30.8%/23.1%/23.1%/23.1%) — close to uniform, and markedly better-balanced than L2's own precedent distribution (7/4/1/0, position D never correct).”
- `grade3-reading/.claude/skills/sim-review/SKILL.md` (3): “first run caught a recurring rail defect and a 72.5% answer-position skew”
- `grade3-reading/.claude/skills/lesson-build/SKILL.md` (28-29): “anti-gaming: answer never the longest/shortest, no CCC key runs”
- `grade3-reading/artifacts/u4l2-build/BEAT-SPEC.md` (116): “key never first”

Against: the reading project's blind-solve
checks never tested position (the same review), and the lesson engine doesn't check it yet. A later run found counter-evidence (`othello-course-renderer-draft/repo/docs/process/CONTRACT-SIGNOFFS.md`). A later run found counter-evidence (`grade3-reading/artifacts/u4l2-build/BEAT-SPEC.md`).

<sub>criterion · key, integrity · universal · from g3, g9 · measured · held · found in [2026-10-12-2-round-1](../research/2026-10-12-2-round-1/), [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Stay inside the assessment boundaries

An item that needs content the stated assessment boundaries exclude is out of scope even if it is correct, and only the stated boundaries count as exclusions.

Once the curriculum source began supplying assessment boundaries, the exclusion statements of the course description, the AP Chemistry overlay began to flag an item that requires excluded content, computation or terminology under curriculum alignment even if it is chemically correct (`shadow-bench/src/inceptbench/prompts/question/ap_chemistry_evaluation.txt`). The judge treats the provided boundaries as authoritative and must not invent exclusions beyond them. The same check was mirrored into the multiple-choice set rubric (`shadow-bench`, git commit 44a9d6e) and is documented in `shadow-bench/docs/internals/ap-evaluation.md`.

Quoted:

- `shadow-bench/src/inceptbench/prompts/question/ap_chemistry_evaluation.txt` (24-26): “an item that requires the excluded content, computation, or terminology is out of scope for AP — flag it under `curriculum_alignment` **even if it is chemically correct**.”
- `shadow-bench/src/inceptbench/prompts/question/ap_chemistry_evaluation.txt` (29-30): “Treat the provided Assessment Boundaries as authoritative; do not invent exclusions beyond them.”
- `shadow-bench/` (commit 44a9d6e) (9-11): “out-of-scope detection via the curriculum's Assessment Boundaries (CED Exclusion Statements) — fail educational_accuracy on excluded content even if chemically correct”
- `shadow-bench/docs/internals/ap-evaluation.md` (139-140): “an item requiring excluded content is a `curriculum_alignment` defect even if chemically correct”
- `shadow-curriculum/plans/data-hierarchy.md` (202): “| `assessment_boundaries`  | array of strings \| null   |”

Against: Boundaries are optional in the curriculum data, so the check can have nothing to apply: '| `assessment_boundaries`  | array of strings \| null   |' (`shadow-curriculum/plans/data-hierarchy.md`, line 202).

<sub>criterion · alignment, demand · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Stay true to the stated scenario

Content must stay consistent with every detail it states about a person or scenario.

The evaluator's base rubric for questions counts content that states a person's or scenario's details, such as an age, a name or a location, and then contradicts them as a factual error (`shadow/bench/src/inceptbench/prompts/question/_base_evaluation.txt` line 90); its rubric for other content does the same for stated context relevant to the content (`other/evaluation.txt` line 348). That rubric also fails a response that leaves out personal context given in the request when it should use it to be accurate, appropriate or complete (line 418).

Quoted:

- `shadow-bench/src/inceptbench/prompts/question/_base_evaluation.txt` (90): “- If the content explicitly references a specific user or scenario context (e.g., a student's age, name, or location) and then contradicts that explicitly stated context, this is a factual error. → `factual_accuracy`”
- `shadow-bench/src/inceptbench/prompts/other/evaluation.txt` (348): “- Contradicting explicitly stated personal or scenario context (e.g., a person's stated age, name, or location) that is relevant to the educational content”
- `shadow-bench/src/inceptbench/prompts/other/evaluation.txt` (418): “If the user explicitly provides personal context in their prompt (e.g., age, name, location, relevant background, or other identifying or situational details), and the response reasonably should incorporate that context to be accurate, appropriate, or complete, then failure to acknowledge or incorporate that explicitly provided user context is a `content_appropriateness` failure (0.0).”

Against: The second rule doesn't apply when the detail is irrelevant to the content: a name or age given with a request for a general explanation need not be echoed (`shadow/bench/src/inceptbench/prompts/other/evaluation.txt` line 418).

<sub>criterion · integrity, stem · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Tasks that need the skills together

Teach and test the combined use of skills through whole tasks that truly need them together, defined by exemplars and a rubric, because passing every part doesn't show the whole. Of 10 tasks written as integrative, the full gate certified 0, with 0 verified as integrative.

The course-quality evaluator checked atomised item quality but not whether a unit contains tasks that coordinate several taught operations, and a gate of individually good atomised checks licenses "passed the parts," never "acquired the theme" (`ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md`). A capstone trial wrote 10 declared-integrative candidates against an unseen text and the full gate certified 0/10 (8 plain-blind leaks, 2 spine-conditioned leaks, 0 integrative verified), so nothing was published (the same file). The evaluator marked a checkpoint integrative because its bank held several skills, though the bank's own metadata declared all 15 serving tasks single-operation (`ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/course-evidence-workbench.html`). The practice spec asks each theme checkpoint for at least 3 items integrative by construction, each needing two or more taught operations together, that test the combined move and never re-test the parts (`ti-courseplans-audit/docs/practice-layer-spec.md`). Passing every part doesn't show the whole, and calling a task integrative doesn't make it so.

Quoted:

- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (246-247): “A gate of individually-good atomized checks licenses "passed the parts," never "acquired the theme."”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (273-275): “the full gate certified **0/10** (8 plain-blind leaks, 2 spine-conditioned leaks; 0 integrative verified), so nothing was published.”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (294): “PR 1104 treats a multi-skill bank as integrative”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/course-evidence-workbench.html` (161): “The evaluator marks D15 integrative because the assessment bank contains multiple skills. The source metadata declares all 15 serving D15 tasks single-operation and zero integrative”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (59): “one task requiring coordination of two or more taught operations”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (69): “The integrative slots test the combined move; they never re-test the parts.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (123): “- Integrative lessons matter: students can master parts and still fail when asked to select, combine, or justify them in context.”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (129): “- N8: integrative-assessment presence. Include tasks that coordinate multiple KCs, not only atomized checks.”
- `grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd` (66): “No rendered check requires integrating both sources”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md` (182): “require synthesis to coordinate at least two prior components rather than list isolated recalls;”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md` (268): “This skill finds hard content defects.”
- `grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md` (85): “Failure mode if ignored: "passed parts, failed whole." Students look successful on micro-gates but break at any authentic task.”
- `grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md` (84): “The mastery gate for an integrative lesson must test the integration — requiring the combined move, not re-testing the parts in isolation.”
- `grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (273-276): “the full gate certified **0/10** (8 plain-blind leaks, 2 spine-conditioned leaks; 0 integrative verified)”
- `grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd` (110): “Students can "master" individual KCs yet fail whenever they must select, combine, or justify them in context.”
- `grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd` (116): “The mastery gate for an integrative lesson must test the integration — requiring the combined move, not re-testing the parts in isolation.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (123): “Integrative lessons matter: students can master parts and still fail when asked to select, combine, or justify them in context.”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (129): “Include tasks that coordinate multiple KCs, not only atomized checks.”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (129): “N8: integrative-assessment presence. Include tasks that coordinate multiple KCs, not only atomized checks.”
- `grade3-reading/knowledge_bot/knowledge/kb-0122-g3-reading-course-graph.qmd` (76): “defined by exemplars+rubric, NOT decomposed further”
- `grade3-reading/ti-courseplans/docs/academics-alignment-plan.md` (26-27): “4. **Decomposition floor.** Integrated performances (passage comprehension) stay whole as capstone KCs — exemplars + rubric-anchored outcome spaces, never sliced thinner.”
- `grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md` (551): “the capstone KC should be treated as an integrative construct — defined by rich exemplars and rubric-anchored outcome spaces rather than an exhaustive list of component KCs.”
- `incept-package-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “A selected response can show one subdecision; it cannot silently stand in for the complete reading performance.”
- `incept-package-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “if a key is repeatedly recoverable without the text or a subdecision is used as a mastery verdict, the evidence claim is invalid.”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/pedagogy-policy.json` (1656): “but it must not be mislabeled as the complete operation”
- `incept-package-hub/course-packages/courses/g5-reading/review/start-here.md` (75-77): “The 80/20 selected-to-constructed item split is the disclosed measurement partition”
- `incept-package-hub/course-packages/courses/g5-reading/review/evidence/course-graph-guide.md` (200): “The integrative task requires evidence from the source node and records the new combined judgment; component success alone does not pass.”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/docs/BRAINLIFT.md inside it) (224-226): “5. **Integration is taught before it is assessed.** Learners do not automatically coordinate separately practiced parts. **Falsifier:** if an assessment combines moves that instruction never combined, the course has outsourced teaching to the assessment.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/evidence/course-graph-guide.md` (200): “The integrative task requires evidence from the source node and records the new combined judgment; component success alone does not pass.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “if an assessment combines moves that instruction never combined, the course has outsourced teaching to the assessment.”
- `incept-package-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “Learners do not automatically coordinate separately practiced parts.”

Against: none found

<sub>criterion · demand, evidence-of-learning, alignment · universal · from g3 · measured · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Teach reading the question

Teach reading the question as its own step, marking the word that says what to do and the word naming the target, with the usual misreadings as wrong options. In one built lesson that step's wrong options were three usual misreadings: answering the previous question, grabbing a familiar name, and answering about the wrong place.

In a Grade 3 inference design the first step is reading the question: students circle the word that says what to do and the word that names the target, and label what each asks for, before they hunt for the writer's words. A built lesson's walkthrough calls reading the question a taught step, not a formality, and takes that step's distractors from the ways a Grade 3 reader misreads a question.

Quoted:

- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (241): “Reading the question is a taught step, not a formality — the distractors are the exact ways a grade-3 reader misreads a question (answers the previous question; grabs a familiar name; answers about the wrong place).”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (133 (textutil text)): “PROCESS word: circle "Why" -> draw a line -> label "Which words?" (we hunt for the writer's actual words as evidence).”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (134 (textutil text)): “TARGET word: circle "use" -> draw a line -> label "Which wants? / traits?"”
- `g9/transformer/src/mechanics/learning-question.js` (1-2): “the lesson's question on its own, with two or three of its phrases explained (what each asks, … never the answer)”
- `g9/transformer/src/mechanics/learning-question.js` (29-30): “Choose two or three short phrases of the lesson question that a Grade 9 reader should stop on, and say what each asks of them here, without answering the question.”
- `g9/transformer/src/mechanics/learning-question.js` (64): “Does note_${i} say what phrase_${i} asks or means in question, without answering question?”
- `g9/transformer/test/mechanics.test.mjs` (121): “assert.equal(lq.codeChecks(stray, ctx).find((c) => c.id === "phrases-in-question").ok, false);”
- `grade3-reading/course-renderer/docs/extras/alpharead-staar-writing-research.md` (75): “**Genre-labeling note:** 2023/2024 named the genre; **2025 said only "well-organized essay."** Train students to infer mode from the task verb ("Explain your opinion" = argue; "Explain why/how/the ways" = inform/analyze).”
- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (838): “A reader does not "find" before they have a question: the search runs inside the think-aloud, immediately after the procedure's Step 1.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (200): “MCQ on the task verb before the child starts hunting.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (173): “That protects every constructed response from a misread prompt”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (228): “Highlight "how does Shakespeare show" as the method command; gloss "true self".”
- `othello-course-renderer-draft/repo/docs/extras/alpharead-staar-writing-research.md` (75): “Train students to infer mode from the task verb ("Explain your opinion" = argue; "Explain why/how/the ways" = inform/analyze).”

Against: none found

<sub>criterion · stem, distractors, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Test a taught word somewhere new

A check on a taught word must put it in a new situation, because a key that repeats the teaching example can be picked from memory without knowing the meaning. In four lessons the key of a word check copied or nearly copied the teaching card's own example.

Hand reviews of four reading lessons found word checks whose keyed sentence copied or nearly copied the example on the word's teaching card, so a student could answer from memory of the card without knowing the word. In each case the fix the review proposed was a new situation for the key.

Quoted:

- `shadow-content-eval/reports/G3-U1-L11-review.md` (64): “A student can answer from memory of the card, without knowing what eerie means.”
- `shadow-content-eval/reports/G3-U1-L12-review.md` (95): “Memory of the example answers both, with no need to know the meaning.”
- `shadow-content-eval/reports/G3-U1-L14-review.md` (79): “This tests memory of the card, not the meaning.”
- `g9-transformer-runs/decisions/1ed330c52090f0fc.json` (20): “Half sunk a shattered visage lies, whose frown,”
- `g9-transformer-runs/decisions/1ed330c52090f0fc.json` (454): “"gap_0": "A shattered ______ lies half sunk in the desert sand near the stone legs.",”
- `g9-transformer-runs/decisions/1ed330c52090f0fc.json` (581): “"value": 0.99,”
- `g9-transformer-runs/decisions/1ed330c52090f0fc.json` (649): “"value": 0.98,”
- `g9-transformer-runs/decisions/1ed330c52090f0fc.json` (241): “"value": 0.81,”
- `g9-transformer-runs/decisions/1ed330c52090f0fc.json` (666): “"value": 0.97,”
- `g9/transformer/src/mechanics/key-words.js` (49): “to study and then recall from memory.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (292): “G3U1L5p2 teaches a stranger with cold stare and slow heavy steps. p3 correct option repeats those distinctive phrases.”
- `grade3-reading/ui-audit-2026-09-08/round-5/final-standard-verification/SEMANTIC-FIVE-FLAG-DISPOSITION-by-residual.md` (14): “The keyed stranger/shadows/cold-stare/slow-heavy-steps sentence closely copies p2's teaching example. That distinctive wording creates a recognition shortcut unrelated to applying the definition.”
- `grade3-reading/course-renderer/docs/ui-audit/2026-09-09/README.md` (24): “The keyed choice copied p2's stranger example; a rollercoaster distractor plausibly fit “dangerous,” while feedback invented fun/laughter.”
- `grade3-reading/artifacts/u4l2-build/BEAT-SPEC.md` (198-199): “bold stem (novel-context scenario)”

Against: none found

<sub>criterion · demand, key, integrity · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Test in the formats taught

A mastery test should use the formats students met during instruction.

The Direct Instruction BrainLift attached to a July 2026 feedback round on the reading course says mastery tests should match formats experienced during instruction. It is an adopted rule here; nothing in these sources measured it.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (140): “- Mastery tests should match formats experienced during instruction.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (571-573): “Students encounter secondary-source claims, primary text, and non-text sources during instruction. Unit 1's checkpoint includes one SAQ for each modality.”

Against: none found

<sub>criterion · format, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Test the skill it claims

The skill a lesson or item claims must be one its text affords and its task really demands at the stated depth, not recall or a neighbouring skill. A probe of 18 inference items found 1 whose conclusion the passage stated outright.

An integrity probe in the reading project extracted the expected conclusion of every inference-bearing item in three lessons and searched the lesson's own passage for a sentence stating it: of 18 items, 1 stated its conclusion outright and was fixed, and the reverse check found no retrieval item that secretly needed an unstated inference. The project's lesson rulings call a retrieval question dressed as an inference, or the reverse, a defect, not style. A gap analysis of its content-evaluation tools makes thinking-level alignment binding, coverage being false if an 'analyze' standard is assessed by 'identify', and a second-round review in July 2026 found a main-idea lesson serving an inference item. The depth asked can mean, for example, explaining a cause-and-effect link or weighing several causes. An identify task can't assess an analyze goal, and an inference whose conclusion the source states outright is retrieval however it is labelled.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0231-pp-depth-6h-doc-diffs.qmd` (75): “behavior is fine — that's the clue; stating the trait/conclusion itself is a disguised-FIND”
- `grade3-reading/knowledge_bot/knowledge/kb-0231-pp-depth-6h-doc-diffs.qmd` (84): “| **Total** | **18** | **16** | **1** | **1** |”
- `grade3-reading/knowledge_bot/knowledge/kb-0231-pp-depth-6h-doc-diffs.qmd` (86-87): “Zero reverse-defect violations (no FIND item anywhere in L5-L7 secretly requires an unstated inference).”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (105-106): “a FIND question dressed as INFER (or the reverse) is a defect, not style”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (122): “- N1: DOK-level alignment. Coverage is false if an "analyze" standard is assessed by "identify."”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (92): “- Example found: a main-idea lesson served an inference/evidence item.”
- `grade3-reading/knowledge_bot/knowledge/kb-0074-g3-reviewer-feedback-distilled-for-g5-2026-06-30.qmd` (51): “the cited "mistag" was defensible”
- `grade3-reading/knowledge_bot/knowledge/kb-0231-pp-depth-6h-doc-diffs.qmd` (95-97): “The item framed itself as inference while handing the child the two exact adjectives the very next sentence states outright”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (58): “The novel stimulus requirement is the single most reliable test of whether an item is genuinely higher-order: no new material, no higher-order thinking.”
- `icloud-work/ML learnings/what_is_ap_and_why_it_matters.md` (57): “Questions must explicitly test one of these skills. A question that just asks "what happened?" fails `educational_accuracy` because it tests recall, not historical thinking.”
- `icloud-work/ML learnings/evaluation_methodology.md` (90): “- Learning objective mismatch (question asks for causation when LO requires comparison)”
- `icloud-work/ML learnings/evaluation_methodology.md` (77-78): “- Question tests college-level historical analysis that AP students don't need
- Question is too easy (tests rote recall when AP requires analysis)”
- `grade3-reading/knowledge_bot/knowledge/kb-0160-multiple-choice-questions-evidence-base.qmd` (149): “Practical guidance paper, not a systematic empirical study.”
- `icloud-work/ML learnings/evaluation_methodology.md` (186): “- It doesn't fully test "pedagogical value" — a factually correct question that teaches the wrong skill can still pass”
- `icloud-work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md` (132): “- **Issue:** The task assesses basic subtraction rather than writing a one-step equation, which the stated standard/lesson emphasizes.”
- `icloud-work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md` (429): “**Failures:** 122 questions (8.7% of all failures)”
- `icloud-work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md` (371): “- `curriculum_alignment` (6/36; often due to operation mismatch vs stated skill)”
- `icloud-work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md` (406): “- Skill metadata can drift (questions sometimes include multiplication when the skill says add/sub only).”
- `icloud-work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json` (27): “The question must directly assess the standard's specific skill, not a tangentially related skill.”
- `APinceptbench/docs/reports/BENCHMARK_FAILURE_REPORT.md` (103): “### 1. Clarity (99.1% pass rate) ✅”
- `APinceptbench/docs/reports/BENCHMARK_FAILURE_REPORT.md` (134): “### 7. Curriculum Alignment (43.0% pass rate) ❌❌”
- `APinceptbench/docs/reports/BENCHMARK_FAILURE_REPORT.md` (33): “The generator ignores the specific `learning_objective` and `statement` provided in the request.”
- `APinceptbench/docs/reports/BENCHMARK_FAILURE_REPORT.md` (132): “Learning objectives require "explain how and why" but questions only test "what"”
- `APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md` (60): “- Scope expansion beyond provided curriculum (e.g., adding Syria/Libya when curriculum specifies Iraq/Afghanistan only)”
- `APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md` (30): “The dramatic improvement in curriculum alignment (43% → 89%) confirms the endpoint is now properly utilizing the `learning_objective` and `statement` fields provided in requests.”
- `grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md` (61): “A model's pedagogical knowledge does not survive the trip into its generated content”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (85): “at least one item is mistagged (a vocabulary item labelled Inference and Evidence), which weakens the claim of full standards alignment.”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (87): “spot-audit the standards tags against what each item actually assesses.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (92): “Example found: a main-idea lesson served an inference/evidence item.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (132): “do not teach one cognitive operation and assess another.”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (122): “N1: DOK-level alignment. Coverage is false if an "analyze" standard is assessed by "identify."”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (124): “N3: recognition-vs-production match. "Write/explain/draw" targets cannot be assessed by MCQ alone.”
- `grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt` (28): “This involves inference.”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (61): “but the story never states a reason”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md` (258): “Either way the correct answer should be statable with a single-sentence verbatim pointer.”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (129): “N8: integrative-assessment presence. Include tasks that coordinate multiple KCs, not only atomized checks.”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (114-115): “`concept_coverage` checks spread, not whether each lesson's claimed KC/skill matches what its items actually assess.”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (282): “standards tags do not match delivered cognitive work”
- `grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd` (66): “No rendered check requires integrating both sources”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md` (64): “Do not certify productive or integrative knowledge with recognition alone.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (91): “Lesson labels and delivered items do not line up.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (93): “Single short passages carry several question types, so lesson-level teaching claim and item-level assessment drift apart.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (132): “Preserve coherence across instruction, practice, and assessment; do not teach one cognitive operation and assess another.”
- `icloud-work/aptraining/.agent/research/inference_clean.md` (128): “Use analytical question stems, not recall”
- `icloud-work/aptraining/.agent/research/inference_clean.md` (65): “Cognitive_demand failures on recall stems.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (225): “rubric "complexity" guidance fails to require students to weigh multiple causes, undermining the stated difficulty level.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md` (115): “7. **Recall-only on a higher-order standard**: standard demands analysis but stem asks "what year did X happen". Match cognitive demand to the standard.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_leq.md` (73): “1. **Reasoning skill mismatch.** Prompt is labeled "comparison" but actually asks for causation. Match the verb to the skill.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (387): “- Repaired MCQ hard institution item to require synthesis rather than recall.”
- `aptraining-local/den-of-ideation/reports/validation_triage/20260527T132917Z_2026-05-27T1330Z_bm0zjn5z_n100_unit1_RAW_PROBE_REPORT.md.md` (130): “`mastery_learning_alignment=0` on 62% of MCQ fails — pure recall, not the "explain how" depth that AP standards demand”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T1808Z_DELIVERED_unit9_mcq_solver_v1_candidate.md` (54): “Fix: rewrote those broad summary templates into sharper cause/effect items”
- `aptraining-local/den-of-ideation/to_main/2026-05-23T1808Z_DEN_REQUEST_validate_unit9_mcq_solver_v1.md` (24): “first public n=10 was `6/10`”
- `aptraining-local/den-of-ideation/to_main/2026-05-23T1808Z_DEN_REQUEST_validate_unit9_mcq_solver_v1.md` (25): “second public n=10 was `7/10`”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T1648Z_DELIVERED_unit7_mcq_solver_v1_candidate.md` (62): “Miss: WWII military template scored `0.65 INFERIOR`”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T1648Z_DELIVERED_unit7_mcq_solver_v1_candidate.md` (63): “Fix: rewrote WWII military as a cleaner cause/effect item linking Allied victory factors to postwar U.S. power”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T1648Z_DELIVERED_unit7_mcq_solver_v1_candidate.md` (68): “Result: `3/3`”
- `downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx` (sheet 'SC Coverage', cell T5): “the Phase 3 ladder assesses the HOW of the lamp-use change, and the text has no because/so/since signal words. Reassign RL.3.1.d to a lesson whose text genuinely signals cause-effect.”
- `downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx` (sheet 'SC Coverage', cell K45): “RL.3.6.d replaces mistagged RL.3.9.d.”
- `downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx` (sheet 'SC Coverage', cell K52): “WRITER'S COMPARISON — RI.3.3 not RI.3.9 (single text).”
- `downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx` (sheet 'SC Coverage', cell K96): “RI.3.8.c (paragraph relationships) replaces mistagged RI.3.9.b.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/INTEGRATED-READINESS-REVIEW.md` (13): “A compact list of correct comparisons can meet those criteria without an organized essay.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/INTEGRATED-READINESS-REVIEW.md` (13): “The later `sg-revise / question` revises a supplied claim, rather than the student's own writing.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/INTEGRATED-READINESS-REVIEW.md` (15): “add an opening comparison, connected supporting paragraphs and a supported conclusion, with a prompt to reread and revise the student's own answer before submitting.”
- `grade3-reading/ti-courseplans/courses/g5-reading/analysis/d8-tag-audit-2026-07-06/README.md` (30-31): “**Dominant pattern:** 4 of 6 misses are the **`Rx.5.10` range/complexity band stamped as if it were a skill** — `.10` describes text complexity, not an assessable comprehension skill, so any item tagged”
- `grade3-reading/ti-courseplans/courses/g5-reading/analysis/d8-tag-audit-2026-07-06/README.md` (15): “| **Sub-skill (defensible)** | **34 / 40** | **85%** |”
- `grade3-reading/ti-courseplans/courses/g5-reading/analysis/d8-tag-audit-2026-07-06/README.md` (39-40): “Recovering the sub-skill rate to ~100% needs only a re-code of the `.10` items to the discrete skill their task exercises”
- `grade3-reading/ti-courseplans/courses/g5-reading/assessments/DESIGN.md` (44): “RL.5.10 (range-of-reading), RI.5.9 (multi-text) — not discretely assessable on single passage; remove in v3”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u02.md` (187): “item requiring the student to use a stage direction — not a spoken line — to answer (distractor:”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u02.md` (188): “treats a bracketed action as something a character said aloud”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (522-524): “stops at locating the mistake sentence; canonical I03 asks for the cross-sentence event→repair inference (locate the mistake AND state how it was fixed and why).”

Against: In the response to an earlier review, one cited mistag was judged defensible. The higher-order rule comes from a practical guidance paper, not a systematic study, and the AP judge can still pass a factually correct question that teaches the wrong skill. The external audit rated that check medium and the course judged it not serious (`grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md`, line 61); the item-statistics review rated it minor, noting it was framed as a comprehension pause rather than a strict locating item (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md`, lines 245 and 258). No before-and-after measurement, and the difficulty finding paraphrases typical judge rationales rather than quoting one. These are adopted rules from writer prompts, untested one by one, and the synthesis rewrite is a single targeted repair. The gain was measured on the ten public items being patched, and a different sample then failed: "third public n=10 was `10/10`, but runner sanity failed `1/2`" (aptraining-local/den-of-ideation/to_main/2026-05-23T1808Z_DEN_REQUEST_validate_unit9_mcq_solver_v1.md, line 26).

<sub>criterion · alignment, demand · universal · from ap, g3, research · measured · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### The complexity standard is not a skill

Tag a reading item with the operation it actually demands, never with the text-complexity standard as if that band were the skill tested. A live audit of 40 Grade 5 items found the genre tag right on all 40 but the subskill defensible on only 34.

A live audit of a Grade 5 reading course's items found genre tagging strong and subskill tagging weaker: 40 of 40 genre tags matched, but only 34 of 40 subskills were defensible, with the text-complexity band (the standard numbered .10) used as a skill and two items miscoded on another standard. The course's acceptance criteria call for recoding those items and auditing enough final items to show the tags match the cognitive work, and its retrospective records the standards and subskill clean-up as only partial.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/STUDENT_READY_CRITICISM_FRAMEWORK.qmd inside it) (180): “D8 live audit found 40/40 genre match but only 34/40 subskill defensible, with `.10` text-complexity band used as a skill and two RL.5.6 miscoded items. | Recode `.10` and wrong subskill items; audit enough final items to prove cognitive-work alignment. |”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/QUESTION_CONVERSION_RETROSPECTIVE.qmd inside it) (416-418): “Standards/subskill cleanup was partial. A D8 sample found strong genre tagging but weaker subskill precision, especially where text-complexity bands and standard codes were being used loosely.”

Against: none found

<sub>criterion · alignment, demand · domain · from g3 · measured · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### The key must trace to the source

Every claim in a keyed answer must trace to something the source says, but naming the category of what it describes is not an error.

For argument-conclusion items, an audit maps each claim in the correct option to a point the passage makes, and a correct option with an unmapped claim fails factual accuracy; appeals to synthesis don't rescue a genuine shift of domain, but naming the category of what the passage described is the skill the standard asks for (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/ela_evaluation.txt`). The audit was narrowed after it over-flagged exactly those category-label summaries and failed good concluding-statement items (`icloud-work/inceptbench-main/tests/test_evaluator_prompt_rules_411_418.py`).

Quoted:

- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/ela_evaluation.txt` (39): “- ANY correct option with a `NONE` claim → `factual_accuracy = 0.0`. "Pedagogical synthesis" / "appropriate inference for hard items" do NOT rescue genuine domain shifts. They DO rescue category-label synthesis covered by the bullet above — that is the standard's intended skill, not a violation.”
- `icloud-work/inceptbench-main/tests/test_evaluator_prompt_rules_411_418.py` (17-19): “concluding-statement items were failing on `factual_accuracy` because Audit B was over-flagging the exact category-label synthesis the standard expects.”
- `incept-package-hub/course-packages/courses/g7-reading/review/evidence/course-graph-guide.md` (33): “True-but-unsupported is wrong; the correct answer must have a citeable evidence line (inference-overreach trap).”

Against: The audit is written for argument conclusions, and applied strictly it misfired on legitimate synthesis until it was narrowed (`icloud-work/inceptbench-main/tests/test_evaluator_prompt_rules_411_418.py`, lines 17-19).

<sub>criterion · key, stimulus · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### The rejected error returns as a distractor

Have the worked example reject a likely error aloud, then offer that same error as a wrong option in the independent check, attempted cold with no hint first.

A Grade 3 course's lesson structure has the guide weigh three candidate sentences in the worked example and reject two aloud, and in the independent turn one wrong option of the first four-option check is the exact error the guide rejected. A Grade 5 audit upheld the same design when it was challenged as spoiling the independent item: the canonical design pins the rejected alternative to the worked example, the trap item is attempted first with no hints before the try, and its repair appears only in feedback after the attempt.

Quoted:

- `grade3-reading/artifacts/judgment-corpus/distilled-src/02-LESSON-STRUCTURE.md` (134-135): “Step 1 = 4-option check on what to hunt (one distractor = the exact error Scout rejected in I-do)”
- `grade3-reading/artifacts/u4l2-build/GRADE5-DECISION-LOG.md` (187-189): “canon itself pins the rejected hunter-to-prey alternative to the M2 I-do (G5-BAR §10: T-U4L2-01 is "carried by the I-do at M2, with the rejected hunter-to-prey alternative") — pre-modeling is the canonical design, and the release re-elicits it cold.”

Against: The challenge it answered held that the modelled rejection pre-teaches the trap item's repair, so the independent item draws nothing out; it was refuted by appeal to the canonical design and the cold attempt, not with learner data (`grade3-reading/artifacts/u4l2-build/GRADE5-DECISION-LOG.md`, lines 184-191).

<sub>criterion · distractors, sequence, practice · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### The task verb matches what is marked

The task verb, the skill an item claims and what its rubric rewards must match, so the instruction a student sees and the rubric ask for the same things.

The AP Chemistry overlay pairs each kind of skill with its task verbs, such as calculate or determine for a quantitative skill and justify or explain for an argument, and calls a verb that contradicts the skill an item claims a defect (`shadow-bench/src/inceptbench/prompts/question/ap_chemistry_evaluation.txt`). The free-response audit's first check is that the action the scoring criteria reward is the action the verb asks for, and the criteria must not secretly demand reasoning the verb did not ask for (`shadow-bench/src/inceptbench/prompts/question/frq_long_evaluation.txt`). A key that rewards a different action, such as a task that says 'describe' with a key that rewards 'draws', was among the defects the judge caught only on some runs (`shadow-bench`, git commit 5dae036). The instruction a student sees and the rubric ask for no more and no less than each other: reviews of reading lessons found a rubric asking for more than its prompt and an instruction asking for a word the rubric never required (`shadow-content-eval/reports/G3-U2-L1-review.md`, `shadow-content-eval/reports/G3-U1-L2-review.md`).

Quoted:

- `shadow-bench/src/inceptbench/prompts/question/ap_chemistry_evaluation.txt` (20-21): “A task verb that contradicts the skill the item claims to assess is a defect.”
- `shadow-bench/src/inceptbench/prompts/question/ap_chemistry_evaluation.txt` (17-20): “- The **task verb should match the assessed skill**: a quantitative/mathematical skill ↔ calculate/determine; an argumentation skill ↔ justify/explain/evaluate-a-claim; a model- or data-representation skill ↔ draw/represent/complete a diagram or graph; an experimental-design skill ↔ design or analyze a procedure.”
- `shadow-bench/src/inceptbench/prompts/question/frq_long_evaluation.txt` (85-86): “1. **Action match** — the action the scoring criteria / sample response *reward* must be the same action the part's task verb *asks the student to perform*.”
- `shadow-bench/src/inceptbench/prompts/question/frq_long_evaluation.txt` (54-55): “The scoring criteria must not secretly demand reasoning the verb did not ask for.”
- `shadow-bench/` (commit 5dae036) (7-11): “The flips were not noise on clean items — the evaluator was *inconsistently detecting genuine defects* that live in the scoring guide / sample-response / rubric region (e.g. a task that says "describe" but a key that rewards "draws"; an intermediate value in a worked key that cannot yield the stated answer; the same single action awarded two independent points).”
- `shadow-bench/src/inceptbench/prompts/question/frq_long_evaluation.txt` (104-106): “A key that paraphrases the task in different words, lists acceptable equivalent forms, applies ECF, or shows a correct worked solution with self-consistent numbers is **clean**”
- `shadow-content-eval/reports/G3-U2-L1-review.md` (145): “- A child who answers what was asked ("bees and animals") meets only half the rubric and is sent back to say what each helper carries, which the prompt never asked for.”
- `shadow-content-eval/reports/G3-U1-L2-review.md` (74): “12. **p24 speak:** the instruction says *"use at least one of our lesson words"*, but the rubric says a lesson word is *"never required."*”
- `shadow-content-eval/reports/G3-U2-L1-review.md` (62): “- The rubric then says the word is "welcome and never required", so the ask promises something the marking ignores.”
- `othello-archive/src/content/practice.ts` (118): “'I zoomed in on two words and named their word class.',”
- `othello-archive/src/content/practice.ts` (119): “'I used two or more key words.',”
- `othello-archive/server/tasks/practice.mjs` (43): “These are strengths, NOT requirements: a second analysed word, correct word-class labels, taught vocabulary, using the exact stem wording, length.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (3373): “The local prompt asks only what rules Neverland might have.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (3373): “Its observed rejection is consistent with the single authored criterion, which explicitly requires rule **and** feeling.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/integration/full-student-sweep/rehearsal-pardon-scoring-review.md` (7): “That is legitimate meaning to teach, yet should be explicit in the task if its omission must cause a miss.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/INTEGRATED-READINESS-REVIEW.md` (13): “A compact list of correct comparisons can meet those criteria without an organized essay.”
- `grade3-reading/ui-audit-2026-09-08/round-5/final-standard-verification/l4-extra-rule-mood-clarity/CAUSE-AND-PROPOSAL.md` (15): “The local question should state that the answer needs a plausible rule and its effect on how the place feels.”
- `grade3-reading/ui-audit-2026-09-08/round-1/g3/PROPOSAL-REVIEW-by-unit9.md` (64): “Do not add an unannounced quotation requirement to the opening solely to replace the impossible tap.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (209-211): “If a prompt says "evaluate" but the key rewards identification, or a lesson claims to teach sourcing but only asks who created a document, the verb-object-evidence chain does not align.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (569): “The prompt verbs and scoring guidance must ask the same operation.”

Against: Paraphrase is not a mismatch: 'A key that paraphrases the task in different words, lists acceptable equivalent forms, applies ECF, or shows a correct worked solution with self-consistent numbers is **clean**' (`shadow-bench/src/inceptbench/prompts/question/frq_long_evaluation.txt`, lines 104-106).

<sub>criterion · alignment, scoring-guide, demand, stem · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Transfer work needs evidence the teaching didn't use

Decide whether an item checks taught knowledge, where overlap with the teaching is the point, or independent use of a skill, which needs evidence the teaching never used. One of six repairs behind an AP unit's block was replacing independent tasks in Lessons 1, 3 and 6 that reused answer-bearing evidence from the worked example.

An independent audit of an AP unit confirmed unseen sources and no wrong or ambiguous key, yet blocked it on six repairs, one of them replacing independent tasks in Lessons 1, 3 and 6 that reused answer-bearing modelled evidence; a later commit closed the repairs with an independent, different-evidence release. A Grade 5 course writes the split in as an invariant, keeping independent item claims disjoint from teaching claims while a blocking, unscored on-ramp check retrieves a prior lesson's claim. The reading BrainLift needed five adversarial rounds to isolate the distinction: an in-lesson knowledge check answerable from explicitly taught knowledge is legitimate, the same overlap in a comprehension or transfer item is a leak, and in reading, where finding the answer in the passage is the skill, a history-style 'answer is in the source' check is skipped. Evidence for independent use must also avoid the cases the teaching and its worked example used, so that copying the model can't pass it.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd` (58-59): “The independent full read confirmed five genuinely unseen checkpoint sources, a 2/2/2/2 MCQ key distribution, no wrong or ambiguous MCQ key”
- `grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd` (60): “It still issued **BLOCKED FOR REPLICATION** on six repair buckets:”
- `grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd` (64): “Replace independent tasks that reuse answer-bearing modeled evidence in Lessons 1, 3, and 6.”
- `grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd` (87): “independent different-evidence release”
- `grade3-reading/knowledge_bot/knowledge/kb-0074-g3-reviewer-feedback-distilled-for-g5-2026-06-30.qmd` (81-82): “Independent item claim_ids must be a subset of independent_claim_ids and disjoint from teaching_claim_ids”
- `grade3-reading/knowledge_bot/knowledge/kb-0074-g3-reviewer-feedback-distilled-for-g5-2026-06-30.qmd` (77): “retrieved through a **blocking, unscored on-ramp check**”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (47): “An in-lesson knowledge check answerable from explicitly-taught knowledge is legitimate (that's what checking taught knowledge means); the same overlap in a comprehension/transfer item is a leak.”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (47): “it took five adversarial rounds to isolate this.”
- `grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd` (26-27): “in reading, finding the answer in the passage IS the skill, so the usual history-style "answer is in the source" leak check is deliberately skipped.”
- `grade3-reading/knowledge_bot/knowledge/kb-0074-g3-reviewer-feedback-distilled-for-g5-2026-06-30.qmd` (85-87): “this is a **design-level** resolution — every lesson's `evaluator_certification`/`renderer_status` still reads not-run/required-not-verified, so whether it executes correctly at runtime is unverified”
- `grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd` (53): “The APUSH deterministic validator passes with zero errors and zero warnings.”
- `grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd` (64): “2. Replace independent tasks that reuse answer-bearing modeled evidence in Lessons 1, 3, and 6.”
- `grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd` (86): “Commit `2056514` closes the six repair buckets recorded in kb-0167”
- `grade3-reading/artifacts/g5-course/AUTHORING-RULINGS-R1-R10.md` (80): “The kitchen/greenhouse/classroom modelling case never appears inside an assessed item.”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (88): “a teaching dose models the exact proposition an item tests → the item checks recall of the modeled sentence, not the skill. Reproduced across 2 units.”
- `ti-courseplans-audit/skills/train-teacher/references/teacher-contract.md` (59-60): “Authoring a fresh unit (u03 respiratory) REPRODUCED the dose-item leak the hibernation unit took 5 rounds to eliminate”
- `ti-courseplans-audit/skills/train-teacher/references/teacher-contract.md` (66-67): “The two lists must be DISJOINT — no move item may test the inference a dose step modeled.”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/labeled-defect-corpus.jsonl` (2): “teaching content leaking the answer to the check it precedes.”
- `ti-courseplans-audit/docs/teaching-reading-comprehension-brainlift.md` (85-86): “Mis-classifying the item makes the same text both correct and defective — it took five adversarial rounds to isolate this.”
- `grade3-reading/knowledge_bot/knowledge/kb-0205-g9-othello-1-1-kb-lesson-view.qmd` (32): “**"students are locked out of writing about the guided practice quote"**”
- `grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md` (82-84): “An in-lesson knowledge check answerable from explicitly-taught knowledge is legitimate”
- `grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md` (84-86): “the same overlap in a comprehension/transfer item is a leak. Mis-classifying the item makes the same text both correct and defective — it took five adversarial rounds to isolate this.”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (88): “list every FACT the dose (I-do/we-do/you-do) uses vs every FACT the MOVE items test — must be DISJOINT (knowledge-CFU items exempt)”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (88): “Reproduced across 2 units.”
- `g9/transformer/src/glue/threejs-render.js` (207): “the student's quote: lines the lesson's blocks found for the question, never the model's or a guided quote”
- `g9/transformer/src/glue/threejs-render.js` (213): “your paragraph: no other line of the text to offer as its quote (the model's own is never offered)”
- `g9/transformer/test/threejs-render.test.mjs` (186): “never the model's quote”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-main-checkout-jul-work.patch` (20670): “| **Dose-item answer leak** | teacher-gauntlet: a teaching dose models the exact proposition an item tests → the item checks recall of the modeled sentence, not the skill. Reproduced across 2 units. | list every FACT the dose (I-do/we-do/you-do) uses vs every FACT the MOVE items test — must be DISJOINT (knowledge-CFU items exempt) |”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v2/authoring/prompts/README.md` (82): “never test the exact proposition you just modeled.”
- `grade3-reading/artifacts/u4l2-build/g5-audit/G5-BAR.md` (287-288): “Independent item claim_ids must be a subset of independent_claim_ids and **disjoint from** teaching_claim_ids.”
- `g9/library/text/L36b8ba.txt` (273): “Both answers are stated outright in the paragraph above, which is appropriate for a Check but means it is retrieval, so the lesson needs something beyond it.”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/pedagogy-policy.json` (1556-1557): “The same answerability pattern is valid for a taught fact check and invalid for a comprehension item”

Against: In the Grade 5 course the split is a design-level resolution: every lesson's certification still read not run, so whether it works at runtime is unverified. none found; checks of taught knowledge are exempt by design, provided each item's class is stated (`ti-courseplans-audit/skills/train-teacher/references/teacher-contract.md`). The Grade 3 build notes apply disjointness to checks for understanding as well, saying never to test the exact proposition just modeled (`grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md`, lines 33-34).

<sub>criterion · integrity, alignment, stimulus · universal · from ap, g3, g9 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Two of a kind must differ

Two blocks of one kind in a lesson must test different things; tell the writer what the earlier one covers.

A second block of a kind on the same text is told what the earlier ones cover and must not repeat or reword them, and
code holds a block that is about what an earlier one was (`g9/transformer/src/mechanics/util.js`, `avoidNote`,
`houseChecks`). The rule came after a second quick check came out as a copy of the first (`g9/transformer/v02/QA.md`,
"Found and fixed").

Quoted:

- `icloud-work/aptraining/workspace/comms/from_main/2026-05-21T0935Z_pipeline_analysis_findings.md` (53): “22% of INFERIOR MCQ_SETs fail `non_repetitiveness`. Pipeline doesn't enforce question-set diversity.”
- `grade3-reading/knowledge_bot/knowledge/kb-0083-clone-lessons-inceptbench-results-2026-07-02-eval-summary.qmd` (64): “Non-repetitiveness is by far the weakest dimension: avg 0.14; 65 of 76 bundles scored exactly 0 on it.”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/mcq_set/evaluation.txt` (175): “- `concept_coverage`: Do questions cover different aspects/skills of the stimulus? (Collection property)”
- `icloud-work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/ck_gen - prompts.json` (12): “Existing Questions to Avoid Duplication:”
- `icloud-work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/README.md` (198): “- `{existing_questions}` - Previously generated questions for same passage”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/match_evaluation.txt` (504): “If the majority of items in a Medium question are recycled from its Easy counterpart, set `difficulty_alignment = 0.0` for the Medium question — it is not genuinely harder, just relabelled.”
- `icloud-work/inceptbench/docs/EVALUATOR_VARIANCE_FIX.md` (at e5be84f^) (288): “8. **Cross-difficulty recycling** — The evaluator still can't detect cross-difficulty item recycling (same facts rephrased across easy/medium/hard) because each question is evaluated independently.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/mcq_set/evaluation.txt` (317): “- Questions test different skills/aspects of the stimulus”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/mcq_set/evaluation.txt` (322): “- Questions all test the same skill”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (81): “Redundancy enemies: two items test the same narrow content, distorting the blueprint.”
- `grade3-reading/artifacts/compare-2026-09-24/FINDINGS.md` (24): “**The same question is asked twice in a row.**”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md` (16): “Two questions in a row asking the same thing”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md` (29): “a pairwise semantic-overlap check across every consecutive question in a lesson”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md` (33): “the we-do must **extend** the modeled skill, never replay it.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (328): “**Manifestation:** ~70-99% of MCQ_SET failures fail `cognitive_demand` (specifically `difficulty_distribution` + `concept_coverage`).”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (329): “the Plan step in MCQ_SET generation does not enforce multi-entity coverage. The model picks the most prominent/salient entity in the topic and concentrates there.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (330): “Plan step must enumerate `nations_to_cover: ["Portugal", "Spain", "France", "England"]` and Question step must be locked to "each question MUST address a different nation from this list" (postmortem prescription).”
- `shadow-bench/src/inceptbench/prompts/lesson_bundle/evaluation.txt` (100): “Pass: no two questions test the exact same skill on the exact same piece of content.”
- `shadow-bench/src/inceptbench/prompts/lesson_bundle/evaluation.txt` (101): “Fail: two or more questions are functionally redundant — a student who answers one correctly gains no additional information from the other.”
- `shadow-bench/` (commit 69d56ab) (55-57): “The deterministic detector (#30) is high-precision + zero-variance but misses SEMANTIC duplicates … token overlap 0.5, below the 0.85 bar”
- `shadow-bench/src/inceptbench/prompts/lesson_bundle/evaluation.txt` (106): “Pass: questions collectively probe multiple distinct comprehension skills”
- `shadow-bench/src/inceptbench/prompts/mcq_set/evaluation.txt` (5): “A strong set probes different skills off one stimulus — e.g. reading the data, a calculation, and an explanation/prediction.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq_set.md` (63): “- No two questions have the same correct answer or test the same fact.”
- `aptraining-local/parallel-ideas-lab/variant-calibration-lab/reports/run_324d5e51_failure_modes.md` (18): “| `redundant_questions` | 17 |”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md` (121): “For MCQ_SET, add explicit coverage fields to the plan step, such as entities/nations/themes to cover, then bind child questions to that plan.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ml_learnings_distilled.md` (75): “MCQ_SET works better when the plan step constrains what each child question must cover.”
- `icloud-work/ML learnings/what_is_ap_and_why_it_matters.md` (37): “**MCQ_SET:** One shared stimulus, THREE questions that all reference that same stimulus, each testing a different historical thinking skill.”
- `icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-04T1430Z_v40h_spot_verify.md` (52): “These are functionally the same question.”
- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md` (97-98): “- Each question should test a distinct aspect of the stimulus.”
- `icloud-work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md` (74): “There is significant overlap between parts (a) and (c).”
- `icloud-work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md` (42): “The three questions do not adequately cover distinct AP historical thinking skills.”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_set_evaluation.txt` (345): “- Each question tests a distinct aspect”
- `grade3-reading/knowledge_bot/knowledge/kb-0083-clone-lessons-inceptbench-results-2026-07-02-eval-summary.qmd` (64): “Non-repetitiveness is by far the weakest dimension: **avg 0.14; 65 of 76 bundles scored exactly 0** on it.”
- `grade3-reading/artifacts/feedback-pp-2026-08-27/REGISTER.md` (10): “Cracked both usage checks via "baby"+"sleep"”
- `grade3-reading/artifacts/eval-suite/RANKING.md` (16): “two-forms-same-job defect”
- `grade3-reading/knowledge_bot/knowledge/kb-0083-clone-lessons-inceptbench-results-2026-07-02-eval-summary.qmd` (64): “Q4, Q9, Q12, and Q13 all ask why ice floats.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md` (33): “> **Design rule:** the we-do must **extend** the modeled skill, never replay it.”
- `shadow-content-eval/reports/G3-U1-L2-review.md` (89): “- **p4:** the two items are clones of each other (a sleeping pet in both). No wrong option tests a near-miss meaning of "determined".”
- `aptraining-local/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md` (62): “Pairwise stem cosine catches redundant child questions.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/B0045_STAGED_MCQSET_INTERIM_20260519.md` (24): “passed rows have balanced distractors, historically accurate content, concise stimulus use, and distinct child-question jobs.”
- `g9/transformer/src/mechanics/util.js` (49): “The same point, near enough: equal, or (for a sentence) most of its words shared.”
- `g9/transformer/src/mechanics/util.js` (55): “return [...sa].filter((w) => sb.has(w)).length / new Set([...sa, ...sb]).size >= 0.6;”
- `g9/transformer/v02/QA.md` (64-65): “QC-2 was a copy of QC-1”
- `g9/transformer/src/mechanics/util.js` (141): “do not repeat or reword those”
- `g9/transformer/src/blocks.js` (67): “what the lesson's earlier blocks of this kind cover: those made or being made (a lone QC-3 makes no QC-1 first);”
- `g9/transformer/src/mechanics/util.js` (41): “The lines most relevant to the lesson question are ${top}. Prefer them, but use any line that fits the task.”
- `g9-transformer-runs/blocks/9a28237802fccd82.json` (16): “will little note, nor long remember what we say here”
- `g9-transformer-runs/blocks/cee942a6baad8233.json` (21): “"prompt": "Find the line that shows this."”
- `g9-transformer-runs/blocks/ed2f90f660c18774.json` (27): “Not about what an earlier Compare two answers block was: already in this lesson:”
- `g9/transformer/src/mechanics/direct-the-line.js` (16): “what this block is about, so a second block of the same kind on the same text is told to differ”
- `g9/transformer/src/blocks.js` (20-21): “QC-1 and QC-2 are two blocks: n is the number in the block's label, and block n is told what the blocks below it that … exist cover.”
- `g9/transformer/web/app.js` (544): “the number in the label tells the server which of its kind this is (QC-2 is told what QC-1 covers)”
- `g9/transformer/v02/QA.md` (64-65): “QC-2 was a copy of QC-1;”
- `g9/transformer/src/mechanics/film-check.js` (22): “// what this block is about, so a second block of the same kind on the same text is told to differ”
- `g9/transformer/test/server.test.mjs` (75): “QC-2's writer is told what QC-1 asks”
- `g9/transformer/src/mechanics/quick-check.js` (13): “// what this block is about, so a second block of the same kind on the same text is told to differ”
- `g9/transformer/src/blocks.js` (67): “what the lesson's earlier blocks of this kind cover”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (257): “Narrative. Pairs badly with the cloze; pick one.”
- `g9/library/text/L8d5159.txt` (257): “Narrative. Pairs badly with the cloze; pick one.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (258-259): “do not build two separate production prompts.”

Against: the repeat test compares words, so a reworded repeat can pass
(`g9/transformer/src/mechanics/util.js`).

<sub>criterion · alignment, integrity · universal · from g9 · measured · held · found in [2026-10-12-2-round-1](../research/2026-10-12-2-round-1/), [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Write new items, not released ones

Write new questions rather than copying or paraphrasing released exam items.

The AP work's stem template for document-based questions ruled out verbatim exam-board prompts and paraphrases of released exams, asking for new stems anchored to verified primary documents. Its inclusion criteria require every pipeline component to be licence- and source-clean: no scraped copyrighted material, no model output used as training data, and no personal data. A re-audit of the source corpus found every encyclopedia row carrying its CC BY-SA 4.0 licence.

Quoted:

- `icloud-work/aptraining/helpers/data/output/t5_dbq_stem_template.md` (4-5): “NO verbatim College Board prompts; NO paraphrase of released exams; net-new stems anchored to verified primary documents.”
- `icloud-work/aptraining/artifacts/INCLUSION_CRITERIA.md` (64): “7. **License / source-clean**: no scraped copyrighted material, no Anthropic / OpenAI-output-as-training, no PII”
- `icloud-work/aptraining/helpers/shadow/output/2026-05-22T2308Z_v93_phase3_reaudit_VERDICT_ADJUST.md` (54): “- Wikipedia: every row has `"license":"CC BY-SA 4.0"`.”

Against: none found

<sub>criterion · integrity, stimulus · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Wrong options only knowledge can reject

Each wrong option must attract a student who misunderstood, and only the tested knowledge or the text may rule it out, never common sense or surface cues. With the rule and a scoring fix, a question whose wrong options were giveaways went from passing at 0.9143 to failing about 80% of runs.

An AP evaluator's rubric fails a question when a wrong option can be ruled out by general reasoning, test-taking instinct or surface cues without the content the item assesses, which turns it into a logic puzzle; it names absolutes that carry the claim, self-contradiction with the stem, claims false on their face and options off the stem's named topic, and a guard catches the right answer being the only option that repeats a distinctive word from the stem. Before the fix, a question whose wrong options were all implausible or giveaways still passed at ~0.91, because one zeroed score was averaged away; after it, the reproducer went from PASS@0.9143 to failing ~80% of runs, with distractor_quality=0.0 in 23-25/30. No wrong option may be rejectable by common sense, a sweeping absolute, a contradiction of the stem or of another option, being true of any text on the topic, or lying outside the question's topic, period or category, and none may be generic filler. Each wrong option should also attract a student who misunderstood.

Quoted:

- `shadow-bench/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (625): “one or more distractors can be ruled out by general reasoning, test-taking instinct, or surface cues alone — *without* knowing the curriculum content the item is supposed to assess. This turns the item into a logic puzzle instead of a knowledge test”
- `shadow-bench/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (627): “**Self-contradiction with the stem or with the option's own wording**, where the option asserts a cause/effect that plainly opposes the stem's premise”
- `shadow-bench/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (628): “**Obviously-false-on-its-face claims** that any test-taker would reject from common sense rather than course mastery.”
- `shadow-bench/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (636): “- **Topically misaligned distractors**: When a question stem has a clear topical focus (e.g., asks for evidence of "economic impact" or "political structure"), distractors that address entirely different topics from the stem's named focus are poor distractors. Students can eliminate them by topical mismatch alone without subject knowledge.”
- `shadow-bench/src/inceptbench/evaluators/guards.py` (1342-1343): “Students can identify the answer through simple keyword matching rather than subject knowledge.”
- `shadow-bench/` (commit f7298c7) (5-7): “which left a single noncritical zero at ~0.91 — above the 0.85 pass threshold — so a question whose distractors are all implausible or giveaway still PASSED.”
- `shadow-bench/` (commit f7298c7) (23-24): “Live verification (concurrency=30, x2): the reproducer flipped from PASS@0.9143 to mean overall 0.78, failing ~80% of runs (distractor_quality=0.0 in 23-25/30),”
- `shadow-bench/` (commit e03b0f7) (4-5): “The LLM applied this mechanically and over-fired on legitimate golden items”
- `shadow-bench/` (commit e03b0f7) (10-13): “Narrow the rule with a removal-check: the absolute is a giveaway only when the universality is *load-bearing* (deleting the absolute word leaves no plausible claim, or the absolute contradicts the stem's own premise).”
- `shadow-bench/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (629): “do NOT over-fire: an option that is merely *incorrect* (or even somewhat weaker than the others) is NOT automatically a giveaway.”
- `icloud-work/inceptbench-main/tests/test_evaluator_prompt_rules_460.py` (3-5): “The distractor_quality and reveals_misconceptions metrics were passing items whose incorrect options were simply the logical negation/opposite of the correct answers (e.g., "good land" vs "poor land", "near people" vs "no people").”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (598): “These are too obvious to eliminate and fail `distractor_quality = 0.0` even if grammatically parallel.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (601): “Students can eliminate them by topical mismatch alone without subject knowledge.”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md` (4): “**Based on:** Forensic analysis of 150 MCQ + 100 MSQ items (62.7% MCQ leak rate, 51.0% MSQ leak rate)”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md` (15): “| Absolute language in wrong options | 27.3% | 34% | Students eliminate "always/never/all/only" without reading |”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md` (17): “| Generic topic-domain wrong option | 22% | 8% | "Any passage on this topic" option is trivially wrong |”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md` (96): “is left with a 50/50 — you have effectively built a 2-choice item.”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md` (124): “Option C uses "Both... agree" on a question asking about a *difference* — eliminatable by reading the stem alone.”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md` (125): “The problem is options B and C are too easy, so students only need to choose between A and D.”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md` (9): “"One option is not a Darling child, so it is eliminable from the stem alone"”
- `shadow-content-eval/SKILL.md` (342): “4-option item with two dead distractors is a 2-option item.”
- `shadow-content-eval/reports/G3-U2-L1-review.md` (138): “- Those describe taking in, not releasing, so a child can drop them on the verb alone. That makes it a two-option item (sugar or oxygen).”
- `icloud-work/incept/README.md` (66): “| `distractor_quality` | Non-critical | Wrong answers must be plausible |”
- `icloud-work/incept/ML_TRAINING_INSIGHTS_REPORT.md` (294): “| MCQ | 23.2% | Distractor quality issues |”
- `icloud-work/incept/ML_TRAINING_INSIGHTS_REPORT.md` (430): “The model fundamentally struggles with generating plausible, pedagogically-grounded distractor options.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/B0045_STAGED_MCQSET_INTERIM_20260519.md` (55): “Gender-role MCQ_SET Q2 fails because only the keyed option visibly signals gender.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (460): “- MCQ_SET `hard-4`: religious-liberty Q3 used treaties/taxes as distractors, making the Virginia Statute too obvious.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (461): “- Fix: replace distractors with same-domain religious-disestablishment alternatives.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (462): “- Targeted proof: `dynamic_32b_full_failed_export_v1_mcqset_hard4_repaired_v32` scored 1.0.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md` (82): “- Be in the **same category** as the correct answer (e.g., if correct is a person, distractors are people; if a date, distractors are dates from the same era).”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md` (112): “4. **Option grain-size mismatch**: 3 options are short, 1 is long with reasoning embedded. Length-balanced options only.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/B0045_STAGED_MCQSET_INTERIM_20260519.md` (41): “| v7 gender same-theme distractor attempt | 1/3 | Regressed badly; reverted. |”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/B0045_STAGED_MCQSET_INTERIM_20260519.md` (57): “The next patch must produce same-theme but clearly wrong distractors that also mention gender/family authority without becoming historically defensible alternate keys.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md` (231): “distractors same-period and plausible”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T1357Z_BLOCKED_unit2_mcqset_parent_archetype.md` (54): “reject generic option templates such as `belongs to the wider era`”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-22T1905Z_hidden_acceptance_repair_status.md` (75): “The IB critique is consistent: factually sound, but too many question-level failures due answer leaks, weak distractors, or insufficient AP-level cognitive demand.”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-22T2050Z_DELIVERED_pipeline_solver_v7_supersedes_v6.md` (49): “Result: `48/50`, mean K `1.2`, mean cost `$0.054`, mean latency `30.28258s`.”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-22T2050Z_DELIVERED_pipeline_solver_v7_supersedes_v6.md` (51): “The two n=50 failures were both perspectives/cultural-interaction prompts that generated otherwise usable fresh content but included `Pueblo Revolt of 1680` as a distractor, causing local rejection and then live IB timeout.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (55-59): “**Near-neighbour distractors.** Distractors are built from *real passage details*, with … the wrong actor / stage / effect / cause / claim swapped in. No distractor may be absurd … or eliminable by world knowledge alone. (Absurd distractors leak the key by elimination.) … At G5, a near-neighbour distractor should require *returning to a specific sentence to … reject* — that is the bar.”
- `grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd` (69): “| F13 | major | Chunk-stop distractors are self-declared filler, not real near-neighbour traps. |”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md` (26): “| 5 | **Near-neighbour distractors** — plausible, text-adjacent, not obvious-eliminable | one-obvious-right + 3 throwaways |”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (60-64): “**Bait the blind solver.** When a world-knowledge default exists, make it a *wrong* … option (a "live trap"). This actively *punishes* the non-reader rather than merely failing … to help them. At G5, the most common GK default is the textbook-true generalization; if … the passage takes a specific or counter-typical stance, key to the passage and make the … textbook generalization a distractor.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (149): “if the key matches the textbook default, treat that as a GK leak.)”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md` (184): “- Change ONE of: the subject, the cause, the effect, the relationship direction, or the scope.”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md` (70): “main-idea status (a "promoted supporting detail" distractor).”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (64): “All three distractors (friendly, gentle, caring) share the same "nice" valence, so the only unpleasant word (menacing) wins by elimination”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/L5-REVIEW-GAPS-2026-09-17.md` (8): “all three distractors were the same misconception (menacing used for something pleasant)”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/KB_FURTHER_IMPROVEMENTS.md` (40): “author named misconception catalogue (M-REVERSE, M-EFFECT-AS-CAUSE, M-LAST-FIRST…), tag each distractor”
- `g9/transformer/src/mechanics/quick-check.js` (23-24): “Exactly one is right given the text; the other two are tempting to a skimmer but the text rules them out.”
- `g9/transformer/src/mechanics/quick-check.js` (75): “seem believable to a Grade 9 reader who skimmed the text, rather than obviously absurd?”
- `g9/transformer/v01/QA.md` (40-41): “A first live run on Othello showed two faults no check caught: a quick-check distractor no reader would choose”
- `g9/transformer/v01/QA.md` (46): “their precision is not yet measured (v04)”
- `g9/transformer/v01/QA.md` (41): “a quick-check distractor no reader would choose ("he hopes to eventually become the Moor")”
- `g9/transformer/v01/QA.md` (43): “whether each wrong option would tempt a reader who skimmed; on Ozymandias it flagged two distractors as not tempting.”
- `g9-transformer-runs/blocks/06ff2f628b44b1fe.json` (45): “"stem": "What term describes the situation where the audience knows Iago is lying but Othello does not?",”
- `g9-transformer-runs/blocks/06ff2f628b44b1fe.json` (54): “The film defines an ensign as the officer who carries the flag, which is a military rank rather than a literary device.”
- `g9/transformer/src/mechanics/quick-check.js` (74): “id: `tempting-${letters[i]}`, label: `Option ${letters[i]} would tempt a reader who skimmed`, required: false,”
- `g9/transformer/v01/QA.md` (42-43): “an advisory check asks whether each wrong option would tempt a reader who skimmed; on Ozymandias it flagged two distractors as not tempting.”
- `g9/transformer/v01/proof-2026-10-09.json` (29-30): “"mechanic": "quick-check", "status": "ready",”
- `g9/transformer/v01/proof-2026-10-09.json` (53-56): “"id": "tempting-B", "required": false, "verdict": "fails", "p": 0.37”
- `g9/transformer/v01/QA.md` (46): “precision is not yet measured (v04).”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/subjects/reading.md` (44-46): “The usage checks ask which sentence uses the word correctly, with distractor sentences whose feeling or meaning is wrong, never sentences that give the answer away by valence alone.”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/judge/distractor-quality.md` (15-16): “an option is answerable from the stem alone, without having read the text (general knowledge, valence, or grammar gives it away).”
- `grade3-reading/course-renderer/docs/extras/alpharead-lesson-design-aladdin-part-1.md` (64): “Distractors: B happy, C pleasant, D ordinary-positive; none carry a valence giveaway.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (148-150): “an inanimate subject (soup, box, afternoon) that CAN'T plausibly show the trait lets a non-reader eliminate a distractor by animacy alone, without ever engaging the vocabulary meaning.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (150-151): “The sweep rewrote the determined-usage distractors course-wide.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (154-155): “The operative test is animate-UNLESS-the-trait-fits-the-thing, not animate-always.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (151-153): “Deliberate exceptions were left in place where the trait applies naturally to things: cheerful (a test CAN look cheerful), stubborn (a stubborn door is idiomatic)”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/INDEPENDENT-TASK-AUDIT.md` (20): “Option B has a pronoun error: “Her friends planned a trick” refers to Bottom.”
- `incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (310-311): “distractors logically coherent but passage-inconsistent, so a passage-blind solver cannot pick”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l2-the-cyclops.md` (559-561): “A child who knows nothing about our text but knows the trope will discard any option that sounds unheroic or unmonstrous, so every distractor must be a true or near-true statement about this passage that fails only on relevance.”
- `othello-course-renderer-draft/repo/docs/video/u1-script-critique.md` (212-213): “A child who has never seen the video can eliminate all three distractors on the giant alone, since a giant in a cave is not a choice, not a home and not a friend.”
- `grade3-reading/artifacts/u4l2-build/BEAT-SPEC.md` (276-277): “Authoring rules for our U4L2 stops: blind-solve-proof, parallel options, every distractor contradicted in-chunk, no answer-cue in lead-in or feedback”

Against: Keyed to surface words the rule over-fired: the model treated any absolute word as a giveaway and failed sound items, so it was narrowed to absolutes that carry the claim, and the rubric now warns that an option that is merely incorrect is not a giveaway. The code guard for negations fires only when every key follows the stem's direction and every wrong option opposes it (`icloud-work/inceptbench-main/src/inceptbench/evaluators/guards.py`, lines 962-974). The shares are among leaked items only; no rate for clean items is given (`grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md`, lines 13-15). A review accepted obviously wrong options in an end-of-lesson fill-in: "For blank 3, `charged`/`marched` "into the night" are grammatical but clearly wrong, which is acceptable." (`shadow-content-eval/reports/G3-U1-L14-review.md`, line 100). The training report's claim that fill-in passes at twice the multiple-choice rate does not match its own table, which gives 30.7% against 23.2% and 17.9% (`icloud-work/incept/ML_TRAINING_INSIGHTS_REPORT.md`, lines 293-295 and 430). A first attempt at same-theme wrong options for one item regressed to 1 of 3 and was reverted, reason not given, and the report warns that such options must not become defensible alternate keys. The two misses were stopped by the solver's own scope check, not by a grader verdict: "causing local rejection and then live IB timeout" (icloud-work/aptraining/workspace/comms/from_den/2026-05-22T2050Z_DELIVERED_pipeline_solver_v7_supersedes_v6.md, line 51). A word-usage check may rightly test one register violation with every wrong option, and one review downgraded the same-misuse finding to minor for that reason (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-B-D5-D6-D11-D13.md`, line 21).

<sub>criterion · distractors, integrity, demand · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Wrong options right on only one feature

When an item tests combining features or sources, include a plausible wrong option right on only one, and key the item so only all of them together answer it. One unit required its closest-case judgment to rest on at least 2 matching chart columns, with a wrong option matching only one.

Archived lesson prompts for a Grade 3 reading course, built around a chart that gains a column each lesson, repeat the rule across units (`incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts`, units 1, 5 and 6). Read-across lessons ask for checks that combine two columns, such as which trickster was clever and punished, rather than a single-cell lookup, and in the weather and water unit each wrong option mislabels one column while another is right. Cold-transfer lessons ask which taught case a new text most resembles, a judgment that must rest on at least two matching columns, with a wrong option that matches on only one, such as the same culture-region but the opposite motive.

Quoted:

- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u01.md` (169): “items that require combining two columns (e.g. "which trickster was clever AND punished?") — not a”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u01.md` (191): “the "most-like" judgment must rest on ≥2 matching columns, with a”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u01.md` (192): “distractor that matches on only one (e.g. same culture-region but opposite motive).”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u05.md` (330): “judgment must rest on ≥2 matching columns, with a distractor that matches on only one (e.g. shares”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u06.md` (237): “items that require combining two columns at once”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u06.md` (239): “column while another is right (e.g. correct process, wrong driver).”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (254-255): “a *correct-sounding* sentence that names only one source → mc-one-source-only”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (261): “replace or add a distractor that is a correct-sounding sentence naming only one source”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (788-789): “can be bridged by an answer that names one source plus the other side's content word”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (791-793): “the true one-source-only misconception is caught where canon puts it: the F9 `mc-one-source-only` distractor and the remote judge's misconception context at the release beats.”
- `grade3-reading/artifacts/u4l2-build/content/u4l2-content.json` (581): “"question": "Using only the article and the map, what can you honestly say about the fish?"”
- `grade3-reading/artifacts/u4l2-build/content/u4l2-content.json` (583): “"A": "It lives around the kelp, and neither source says what it eats."”
- `grade3-reading/artifacts/u4l2-build/content/u4l2-content.json` (586): “"D": "It lives around the kelp bed, because the map places it near the kelp."”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (262-263): “true-sounding, but uses only the map and ignores that neither source states diet”

Against: The rule comes from archived authoring prompts, which record no results for these items. The source's own example admits the option is true and wrong only for what it leaves out: "true-sounding, but uses only the map and ignores that neither source states diet" (grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md, lines 262-263); built that way it is a defensible answer, against one-answer-the-text-settles.

<sub>criterion · distractors, demand, key · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Wrong options stated as claims

Write each wrong option as a plain claim stated as if true, not as a report of what learners believe. Options carried over in the voice 'Some students may believe that...' passed 1 of 5.

A five-item pilot drew wrong options from a bank of misconceptions written in a teaching voice ("Some students may believe that..."), and its instruction to preserve meaning carried that voice into the options. It passed 1/5, at about $0.003. The fix was one line in the prompt: strip the teaching frame and state the wrong belief as if a confused student were asserting it as fact.

Quoted:

- `icloud-work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md` (188): “**Result:** 1/5 pass (5 OpenAI + 5 IB calls, ~$0.003).”
- `icloud-work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md` (190): “The source corpus (`common_misconceptions`) is written in **pedagogical-meta voice**: "Some students may believe that..." The prompt instructed "preserve semantics," which faithfully carried that voice into MCQ distractor text.”
- `icloud-work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md` (190): “But a real distractor must be a **positive declarative claim** (first-person voice of the wrong belief).”
- `icloud-work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md` (192): “**Fix:** One line in prompt — "Strip any meta-pedagogical framing. The option states the wrong belief AS IF a confused student were asserting it as fact."”

Against: none found (the re-run after the one-line fix was not in the files read)

<sub>criterion · distractors, wording · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Wrong options that catch the shortcut

Put in wrong options that a shortcut would choose, so that only applying the rule to the new material works. One sorting design added three trap animals, a whale, a jellyfish and a bat, so that the deciding rule and not appearance settles each.

Two Grade 3 designs build the shortcut into the wrong choices. In an inference design, the independent task's wrong words are the reasons from the modelled section, and the feedback on a wrong tap names the difference, so copying the model's answers fails. A classification design adds trap animals whose look points to the wrong group, which force the child to apply the deciding rule over appearance. That the first design aims to catch copying is inferred from its note and its feedback; the second states its aim.

Quoted:

- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (283 (textutil text)): “Note: the don't-fit words are the cave reasons from the Modelling Moment. Here Aladdin is reaching for something new.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (282 (textutil text)): “"Getting home was why Aladdin acted in the cave. Is that what he is reaching for now that he wants to marry the princess?"”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 3. The Animal Kingdom - SORT - Lesson Design (v2 - MCQ pauses + science sweep).docx` (205 (textutil text)): “The trap animals (whale, jellyfish, bat) force the child to apply the rule over appearance.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 3. The Animal Kingdom - SORT - Lesson Design (v2 - MCQ pauses + science sweep).docx` (161 (textutil text)): “Step 5 — Extra thinking (the trap beat): appearance can fool you.”

Against: none found

<sub>criterion · distractors, demand, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Wrong options that diagnose the process

Make each wrong option stand for a kind of comprehension failure, such as paraphrase without inference or an unwarranted link, and route feedback by the kind chosen across items.

A reading quality canon asks that distractors be designed so a child's error pattern across items diagnoses the failure type, paraphrase overuse, an unwarranted connection or a missing causal inference, with feedback routed to that process and not only to per-item misconceptions. The grade-3 rulebook names its families after the MOCCA assessment: a paraphrase option marks a local-coherence failure and a lateral connection a plausible but wrong link, with misconception-coded options as the other kind, and its feedback names the misconception and steers to the text without naming the key. The course's note on the move reads a profile only from a reliable lean across a unit, not a single miss, and quotes a talk on the assessment: a student who reliably picks the same kind of wrong response can be identified as over-relying on one process.

Quoted:

- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (212): “Distractors are designed so a child's error *pattern across items* diagnoses the failure type (paraphrase-overuse vs unwarranted connection vs missing causal inference), and feedback routes to that process — not only per-item misconceptions.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (132-135): “Distractors are PROCESS-DIAGNOSTIC (MOCCA families: paraphrase = local-coherence failure; lateral connection = plausible-wrong link) or misconception-coded — feedback names the misconception and TEACHES; a wrong answer's feedback steers to the text without naming the key.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/resources/redteam-skill/references/teaching-moves/process-diagnostic-distractors.md` (15): “So if they pick the same kind of incorrect response in a reliable manner, we're able to use that information to identify them as one of those poor comprehenders who over-relies on one specific kind of process.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/resources/redteam-skill/references/teaching-moves/process-diagnostic-distractors.md` (28): “A *reliable* lean — not a single miss — toward `paraphrase` sets `profile=paraphrase_overuse` and routes to inference-prompting feedback”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/process-diagnostic-distractors.md` (13): “when students get a response or a question incorrect, the answer choices represent strategies and cognitive processes that we know poor comprehenders tend to overuse when they're reading.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/process-diagnostic-distractors.md` (15): “So if they pick the same kind of incorrect response in a reliable manner, we're able to use that information to identify them as one of those poor comprehenders who over-relies on one specific kind of process.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/process-diagnostic-distractors.md` (17): “It turns out they tend to rely on one of two strategies; paraphrasing or making connections.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/process-diagnostic-distractors.md` (7): “prompt the paraphraser to infer, prod the connector to be selective and causal”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/process-diagnostic-distractors.md` (24): “Causal-comprehension items (cloze: the child completes a story missing a sentence) ship with exactly three choices, each tagged to a process family:”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/process-diagnostic-distractors.md` (26): “`paraphrase` — a restatement of a nearby sentence; local, true, but adds no inference (the paraphrase-overuse trap).”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/process-diagnostic-distractors.md` (27): “`lateral_connection` — a topically related, real-world-plausible sentence that makes an inference the text does not warrant (the unwarranted-connection trap).”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/process-diagnostic-distractors.md` (28): “not a single miss — toward `paraphrase` sets `profile=paraphrase_overuse` and routes to inference-prompting feedback”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/process-diagnostic-distractors.md` (32): “If a distractor is just factually wrong/nonsensical, it diagnoses nothing”

Published: [Multiple-choice Online Cloze Comprehension Assessment (MOCCA), IES video](https://www.youtube.com/watch?v=bm8ms9QVKUs)

Against: none found

<sub>criterion · distractors, feedback, measurement · universal · from g3, research · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Wrong options true elsewhere in the text

Use wrong options that are true elsewhere in the text, or were true earlier, but don't answer this question.

A reading curriculum's lesson-components spec has its summary gap-fill use true-earlier-but-not-now distractors to test that the child tracked how things changed. A science lesson design uses a true fact from the text that is not the job of any plant part as its why-wrong option, and a built retell uses distractors true of the story but wrong at that gap, which its walkthrough says separates a retrieval task from a guessing game. Such options make the item test relevance and tracking rather than spotting a falsehood.

Quoted:

- `downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx` (20 (textutil text)): “The taught word features in it, and “true-earlier-but-not-now” distractors test that the child tracked how things changed.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx` (141 (textutil text)): “a true fact, but not the job of a part.”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (151): “Distractors are true-of-the-story-but-wrong-here, which is what separates a retrieval task from a guessing game.”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/item-types/hot-text.md` (5-9): “The correct sentences are the evidence; the rest are plausible distractor sentences from the SAME section, so the child rules out neighbours rather than strangers. Include distractors of the classic wrong kinds: right scene wrong agent, true but irrelevant, and what-happens-after (wrong place in the causal chain).”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/judge/distractor-quality.md` (18-20): “Judge plausibility from the child's likely errors: wrong agent, wrong place in the causal chain, true-earlier-but-not-now, opposite valence, a detail from the wrong scene.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (558-561): “A child who knows nothing about our text but knows the trope will discard any option that sounds unheroic or unmonstrous, so every distractor must be a true or near-true statement about this passage that fails only on relevance.”
- `othello-course-renderer-draft/repo/authoring/inputs/prompt-packs/reading-g3/item-types/hot-text.md` (5-9): “The correct sentences are the evidence; the rest are plausible distractor sentences from the SAME section, so the child rules out neighbours rather than strangers. Include distractors of the classic wrong kinds: right scene wrong agent, true but irrelevant, and what-happens-after (wrong place in the causal chain).”
- `othello-course-renderer-draft/repo/authoring/inputs/prompt-packs/reading-g3/judge/distractor-quality.md` (18-20): “Judge plausibility from the child's likely errors: wrong agent, wrong place in the causal chain, true-earlier-but-not-now, opposite valence, a detail from the wrong scene.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/schema-video.md` (47): “Distractors are accurate functions described in the video but answer a different role question.”
- `grade3-reading/curriculum-gen/audits/PETER-PAN-AUDIT-2026-08-24.md` (97-98): “use true-earlier-but-not-now distractors”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/HUMAN-g3r-2026-07-27T08-38-36-019fa24b-fb42-7e61-a954-216db3ef77a4.md` (1108): “The taught word features in it, and “true-earlier-but-not-now” distractors test that the child tracked how things changed.”
- `grade3-reading/course-renderer/docs/extras/alpharead-lesson-design-witw-part-4.md` (223): “the don't-fit words (timid, hiding, fearful) describe the OLD Mole from the start of the story, so they are deliberately the traits the child must NOT pick.”
- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L5-2026-09-05.md` (193-195): “options include the literal answer ("A damp cave") vs. a plausible same-paragraph confusable ("A great circular room" — what was actually found, tests expectation-vs-reality parsing, not just word-matching).”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (442-443): “(real food-web terms from ¶2/¶8 that are not what the note said)”

Against: none found

<sub>criterion · distractors, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Wrong options wrong for the right reason

In science content, make each wrong option wrong only as its named misconception is, never garbled some other way, since a garbled option teaches its garble to every reader.

A reading course's generator rules for lessons whose text carries science make the supplied misconception cards binding and require each wrong option to encode its named misconception exactly, because an option scientifically garbled in some other way teaches that garble to every child who reads it (`grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/subjects/science.md`, lines 3-19). The course's fact-check judge fails any child-facing string that states something false, wrong options and feedback included, because a wrong option must be wrong for the right reason (`grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/judge/factual-accuracy.md`, lines 7-10).

Quoted:

- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/subjects/science.md` (17-19): “A wrong option must encode the named misconception exactly; an option that is scientifically garbled in some OTHER way teaches that garble to every child who reads it.”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/judge/factual-accuracy.md` (8-10): “states something factually false, in any field, including wrong options and feedback (a wrong option must be wrong for the RIGHT reason: a distractor that is garbled science teaches the garble);”

Against: none found

<sub>criterion · distractors, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A text fallback for spoken answers

Give a spoken-answer task a text fallback of equal status, and keep speech-recognition errors, accent and noise from counting against the content.

The assessment pattern library in the reading project's knowledge base lists speech-recognition errors, accent bias and background noise among what contaminates spoken evidence, citing published evidence of racial disparities in major recognition systems, and asks for a text-response fallback of equal status, noise and accent policies, and retakes when the environment likely interfered (`grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd`). It uses audio features only when fluency is part of the claim. The reading course scores pronunciation leniently, without penalising accent or a noisy room (`grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd`).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd` (567): “Always provide a text-response fallback of equal status”
- `grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd` (554): “Speech recognition errors, accent bias, and background noise can contaminate evidence.”
- `grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd` (539): “Evidence of racial disparities in major ASR systems”
- `grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd` (572): “Audio features (only if fluency is part of the claim): Rate-of-speech, pauses, prosody—do not use for content-only claims.”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (64): “don't penalize accent or a noisy room”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (808): “For the vocabulary say-back specifically, require speech. Do not accept typing as a substitute for saying the word.”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (1222): “Where a task needs a microphone or headphones, the child must have a route through without them”
- `grade3-reading/ui-audit-2026-09-08/round-1/g3/VOCAB-NO-SPEECH-PROPOSAL.md` (7): “This is a confirmed usability trap for a learner who cannot speak; no pronunciation or successful speech observation was obtained.”
- `grade3-reading/ui-audit-2026-09-08/round-2/g3/EXPLICIT-SPEECH-CHOICE-REVIEW-by-unit9.md` (9): “A child who chooses not to speak should be able to continue before encountering that failure.”
- `grade3-reading/ui-audit-2026-09-08/round-1/g3/VOCAB-NO-SPEECH-PROPOSAL.md` (13): “Do not mark the word mastered or pretend speech occurred.”
- `grade3-reading/edullm-review-hub/course-packages/quality/golden-student-course/versions/1.0.0/STANDARD.qmd` (703): “typed or equivalent input, silence, denial, error, and no-microphone paths complete the task”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/BRAINLIFT.md` (142-143): “a child who says nothing still finishes the lesson.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/CASE-FOR-APPROVAL.md` (106-107): “Spoken and written go to the same marker and the same rubric; the only difference is that a speaker is not marked down for punctuation they never chose.”
- `grade3-reading/course-renderer/docs/rules/vocabulary.md` (355-356): “the vocabulary say-back is spoken regardless (R-VOC-10)”
- `grade3-reading/course-renderer/docs/rules/vocabulary.md` (356-358): “So: choice everywhere, except one task where speech is compulsory, for a child who may have no microphone. Needs a decision on what that task does when speech is unavailable.”
- `othello-archive/server/tasks/oral.mjs` (12): “The answer is transcribed speech: ignore filler words, missing punctuation, capital letters and small transcription slips. Never mark down spelling.”
- `grade3-reading/ui-audit-2026-09-08/gold-standard/say-word-action-regression.log` (8): “PASS Capture failure offers honor fallback and is not a scored miss”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (873): “presence-only capability check, explicit microphone start, non-speaking route reachable before browser speech calls”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/lesson-01.md` (11): “Say and use each orally or in text. Do not require a microphone to continue.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/INTEGRATION-LESSONS.md` (26): “Tour copy must describe available typing and speech paths; omit stale narration until a matching recording exists.”
- `grade3-reading/ti-courseplans-wiki/Perfect-Course-Rulebook.md` (391-392): “Infrastructure failure is not learner failure”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/FEEDBACK-RESPONSES.md` (137): “A child with no microphone, or who says nothing, can still finish every”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (282-284): “**R-VOC-10 — say-back must be spoken, not typed**: typing is not accepted as a substitute for the vocabulary say-back specifically, because vocalizing is vital for orthographic encoding”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (287-288): “**R-VOC-11 — pronunciation is scored leniently**: anything reasonably correct passes, an accent or noisy room is never penalised, and XP is kept off the pronunciation task”
- `grade3-reading/course-renderer/docs/rules/vocabulary.md` (197-198): “**Rule.** For the vocabulary say-back specifically, require speech. Do not accept typing as a substitute for saying the word.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md` (332): “let's say the microphone is not working or they're in a noisy place, they should be able to switch and and type as well.”
- `othello-archive/src/oral/SpeakBox.tsx` (2): “Speaking is never required: typing works the same (and is all Firefox offers).”
- `othello-course-renderer-draft/repo/docs/rules/vocabulary.md` (197-198): “**Rule.** For the vocabulary say-back specifically, require speech. Do not accept typing as a substitute for saying the word.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/02-LESSON-STRUCTURE.md` (210-211): “Say "tell" rather than "say out loud" in prompts — "tell" is vaguer and captures both writing and speaking”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (87-88): “otherwise the SAME beat with a clearly labeled type-your-answer input. Talk-or-write both open on every free response.”

Published: [Koenecke et al. 2020](https://doi.org/10.1073/pnas.1915768117)

Against: The reading course requires a word's say-back to be spoken, with typing not accepted, and records as an unresolved contradiction that a child with no working microphone then has no fallback (`grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd`). A later run found: The reading course renderer's vocabulary rules record the same gap: learners may speak or type everywhere except the vocabulary say-back, which is spoken regardless, so speech is compulsory for a learner who may have no microphone, and what that task does when speech is unavailable awaits a decision (`grade3-reading/course-renderer/docs/rules/vocabulary.md`, lines 346-358) (`grade3-reading/course-renderer/docs/rules/vocabulary.md`). A later run found counter-evidence (`grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt`). A later run found counter-evidence (`grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md`). A later run found counter-evidence (`grade3-reading/course-renderer/docs/rules/vocabulary.md`). A later run found counter-evidence (`othello-course-renderer-draft/repo/docs/rules/vocabulary.md`).

<sub>criterion · accessibility, format, marking · universal · from g3, research · external-research · contested · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Close on a choice between two readings

End a literature lesson's closing questions on a choice between two defensible readings that learners must justify, since a question naming the reading it wants asks only for description.

A Grade 9 unit's knowledge base sets its closing questions as mimicry, then application to the extract, then an 'X or Y?' evaluation (`g9/sources/1. Act 1 - Knowledge Base - Overview.csv`, line 140). Its quality pass flagged one lesson's question, which asked how the text presents a character as defiant and dutiful, as descriptive, not 'X or Y', and proposed asking whether she is presented as defiant or loyal (line 147). The lesson design specification's evaluation example asks learners to choose between two readings of a character and justify the view (`g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md`, line 192).

Quoted:

- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (140): “TASK 3 evaluate (""X or Y?"").”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (147): “is descriptive, not ""X or Y"".”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (147): “present Desdemona as defiant or loyal?"" Flagged, not changed.”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (192): “"Is Iago more dangerous because he hides his feelings from Othello, or because he reveals them to the audience? Justify your view."”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (135): “Highlight "to what extent" and "entirely" as the evaluative commands”

Against: The flagged question was left unchanged (`g9/sources/1. Act 1 - Knowledge Base - Overview.csv`, line 147); the specification's top-stage learning question asks 'to what extent' rather than offering two readings (`g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md`, line 135); and another record, drawn from Grade 3 reviews, bans any question answered by a two-way pick.

<sub>criterion · stem, demand, format · domain · from g9 · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Each part stands on its own

Make each question in a set and each part of a multi-part item answerable from the source and scorable alone, with none restating, revealing or depending on another's answer.

One generator spec asks for three or four questions on a shared source, with different skills and independent answers (`icloud-work/evaluator/docs/AP_GENERATOR_SPEC.md`). The pipeline's pass contract forbids parts that depend on one another in a way that blocks independent scoring (`icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-pass-contract-matrix.md`), and the external judge's short-answer rules ask for parts that are independently scorable and connected (`icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md`). The judge flagged a pair of parts where a strong answer to the first could partly pre-answer the second (`icloud-work/evaluator/docs/reports/LATEST.md`). No part should give away or depend on another's answer, and a slip in one should cost nothing in the others.

Quoted:

- `icloud-work/evaluator/docs/AP_GENERATOR_SPEC.md` (44): “**Rules**: 3-4 questions, different skills, independent answers”
- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-pass-contract-matrix.md` (127): “- parts that depend on one another in a way that blocks independent scoring,”
- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md` (72): “- Parts should be clear, usually labeled, independently scorable, and connected.”
- `icloud-work/evaluator/docs/reports/LATEST.md` (130): “| Parts (a) and (b) have some potential overlap — a strong answer to (a) could partially pre-answer (b... | 1 |”
- `icloud-work/ap-social-studies-generator/curriculum/ceds/ap-european-history-ced.pdf` (pdftotext -layout output, line 12633): “Each point is earned independently.”
- `icloud-work/ap-social-studies-generator/python/generators/saq.py` (771): “⛔ Parts must be independently scorable — no chaining.”
- `APinceptbench/docs/AP_GENERATOR_SPEC.md` (44): “**Rules**: 3-4 questions, different skills, independent answers”
- `APinceptbench/ap_benchmark/prompts/official_ap_prompts.py` (229): “- Are parts logically connected but independently scorable?”
- `APinceptbench/docs/GENERATOR_API_SPEC.md` (239): “- Parts MUST be scaffolded (build on each other OR test related aspects)”
- `shadow-bench/src/inceptbench/prompts/mcq_set/evaluation.txt` (5): “Each question must be answerable **from the shared stimulus alone**, independently of the other questions' answers (never "using your answer to the previous question").”
- `shadow-bench/src/inceptbench/prompts/question/ap_chemistry_evaluation.txt` (55-56): “- In a stimulus-based set, every item must be answerable **from the shared stimulus alone**, independently of any other item's answer;”
- `shadow-bench/docs/internals/ap-evaluation.md` (94): “A shared data table / graph / particulate diagram / reaction scheme with a few questions, each independently answerable from the stimulus.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_saq.md` (71): “2. **Chained dependencies.** Part b is impossible to answer without first answering part a correctly. Parts should be independent within a shared context.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_leq.md` (76): “4. **Multi-task prompt.** "Discuss the causes AND consequences AND legacies of X" — that's three essays. One task per LEQ.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_saq.md` (83): “- [ ] Verb difficulty escalates a → b → c (typical pattern)”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (67): “6 of 6 sampled two-part evidence items were blind-solvable, with Part B restating Part A — the same root cause measured at 33% gameable in G3”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md` (69-70): “a same-family-IB-passed bank that is **36% leaky** (RI.5.9 MCQ stem-giveaway + … RL.5.1 hot-text stem-giveaway; the EBSR pair self-confirmed)”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (83): “include prior-knowledge answerability, EBSR Part-B-restates-Part-A, and keyword-match answerability.”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md` (158-159): “For MSQ, all defensible answers must be keyed. For EBSR, Part B needs one uniquely strongest evidence choice and must not reveal Part A.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (74-75): “**Do not lean on Part B to rescue a … GK-solvable Part A** — strengthen Part A independently.”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (78): “6 of 6 sampled two-part evidence items were blind-solvable, with Part B restating Part A — the same root cause measured at 33% gameable in G3”
- `ti-courseplans-audit/skills/course-red-team/SKILL.md` (134-135): “In the recorded G3 case, EBSR was gameable 33% of the time because Part B restated Part A”
- `ti-courseplans-audit/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md` (46): “Part B restates Part A — G3's measured root cause, verbatim present”
- `ti-courseplans-audit/skills/course-content-integrity/SKILL.md` (158-159): “For EBSR, Part B needs one uniquely strongest evidence choice and must not reveal Part A.”
- `ti-courseplans-audit/skills/course-red-team/SKILL.md` (135): “that is evidence for that profile, not a universal format rule.”
- `grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md` (156-157): “6 of 6 sampled two-part evidence items were blind-solvable, with Part B restating Part A”
- `grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md` (157-158): “the same root cause measured at 33% gameable in G3”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (16): “blind probe: compare Part B correct option text to Part A answer”
- `grade3-reading/artifacts/spine-solve-calibration-2026-07-10/REPORT.md` (94): “(ebsr, 3/3 exact, medium conf + persistent)”
- `grade3-reading/artifacts/spine-solve-calibration-2026-07-10/REPORT.md` (94): “Part-A stem keyword "curious" appears verbatim in the correct Part-B evidence quote, and that quote names the action ("pry open the lock") matching Part-A option d. Passage-independent — derivable from the option set alone.”
- `grade3-reading/artifacts/spine-solve-calibration-2026-07-10/REPORT.md` (12): “**Status: INVALID FOR LIFT OR BAR CALIBRATION.**”
- `grade3-reading/artifacts/spine-solve-calibration-2026-07-10/REPORT.md` (5): “use the named leak vectors as examples and the raw rows as harness evidence”
- `grade3-reading/artifacts/g5-expansion-kit/PLAN.md` (55): “| "sophisticated-option" EBSR | any | ebsr | leaks (Part B restates A) | refuted this run | **WON'T WORK** |”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/RED_TEAM_FINDINGS.md` (33): “**Part B restates Part A** — G3's measured root cause, verbatim present”
- `grade3-reading/ti-courseplans/courses/g5-reading/analysis/rt5-ebsr-2026-07-06/README.md` (55-56): “when the correct evidence sentence contains the Part A answer, a blind solver reads it off the option list.”
- `grade3-reading/artifacts/arc-audit/PRE-WEEKEND-SMOKE-2026-08-28.md` (108-110): “checked every cloze's distractor bank against sibling MCQ answer options on the same page (none collide); checked stems for answering-each-other patterns on shared pages — none found.”

Against: Another spec pulls the other way: '- Parts MUST be scaffolded (build on each other OR test related aspects)' (`icloud-work/evaluator/docs/GENERATOR_API_SPEC.md`, line 239). Nothing here measures what a chained part costs; the rule rests on the official guidelines and a writer rule. The same project's generator contract also requires short-answer parts to be scaffolded, building on each other or testing related aspects (`APinceptbench/docs/GENERATOR_API_SPEC.md`), so parts may connect as long as each can be scored on its own. A single item with several parts is handled differently: a well-formed multi-part item "must allow a student who erred on an early part to still earn later points", crediting work consistent with the student's own earlier value and keeping at least one part answerable without a prior result (`shadow/bench/src/inceptbench/prompts/question/frq_long_evaluation.txt` lines 109-112). These rules come from writer prompts and were not tested one by one, and the rising-difficulty item calls itself a typical pattern, not a requirement. The 33% is evidence for that course's profile, not a universal format rule, as the same skill says when choosing which format to probe first (`ti-courseplans-audit/skills/course-red-team/SKILL.md`, line 135).

<sub>criterion · format, integrity, scoring-guide · universal · from ap, g3 · adopted-rule · contested · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Give a matching task a spare target

Give a matching item more targets than prompts, without announcing which one is spare, so its last pairs can't be won by elimination. A static scan of one course found 192 matching items that announced their spare target.

The intake of a Grade 5 generator pilot asked for at least one unused decoy target in every matching item before scale (`grade3-reading/knowledge_bot/knowledge/kb-0067-g5-generator-pilot-intake-and-team-async-2026-06-23.qmd`), and a test design listed its three-by-three matching item among its honest limits as a minor elimination cue (`grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd`). A static accessibility scan of the merged Grade 5 course named 192 matching items that announce a decoy bucket (`grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd`). Let the text, rather than a common association, fix each pairing, so no pair can be won by guessing.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0067-g5-generator-pilot-intake-and-team-async-2026-06-23.qmd` (314): “- add at least one unused/decoy right bucket to match items”
- `grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd` (66): “`match` is 3×3 (minor elimination cue)”
- `grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd` (133): “192 match items announcing a decoy bucket”
- `icloud-work/evaluator/docs/reports/BENCHMARK_RUN7_REPORT.md` (58): “- difficulty_alignment: 1:1 matching without distractors reduces difficulty”
- `icloud-work/evaluator/docs/reports/BENCHMARK_RUN7_REPORT.md` (59): “- distractor_quality: No extra options to create analytical challenge”
- `icloud-work/evaluator/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md` (106): “| match | 53% | 45% | 52% | 55% | 54% | 48% | **51%** |”
- `icloud-work/evaluator/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md` (387): “| Never exceeds | 55% |”
- `icloud-work/evaluator/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md` (391): “- No distractors = simple elimination”
- `APinceptbench/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md` (106): “| match | 53% | 45% | 52% | 55% | 54% | 48% | **51%** |”
- `APinceptbench/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md` (387): “| Never exceeds | 55% |”
- `APinceptbench/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md` (390): “- 1:1 format eliminates analytical challenge”
- `APinceptbench/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md` (391): “- No distractors = simple elimination”
- `APinceptbench/docs/reports/BENCHMARK_RUN7_REPORT.md` (119-120): “The 1:1 matching format with no distractors makes this more of a medium difficulty question despite being marked as hard”
- `grade3-reading/knowledge_bot/knowledge/kb-0068-g5-static-dataset-intake-2026-06-23.qmd` (116): “unused-right-bucket-exists: 638”
- `grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd` (58): “192 match items announce a decoy bucket”
- `grade3-reading/knowledge_bot/knowledge/kb-0090-fable5-plan-traces-2026-07-09.qmd` (133): “match designs work when they force source/POV attribution, which-half attribution, or not-mentioned discrimination;”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md` (48-49): “**Match** — ≥3 text-grounded pairs (note: 3×3 equal-sides has a minor elimination cue — prefer a 4th distractor category where the generator supports it).”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (78-79): “The correct pairing must be fixed by the passage, NOT by a canonical … real-world association.”
- `grade3-reading/course-renderer/content/lesson-plans/g3-u2-l1.json` (694): “A word-bank cloze with four blanks and four bank words can be completed from grammar alone, without the text.”

Against: a structural grader run on one Grade 5 dataset listed an unused right bucket as a failure reason 638 times (`grade3-reading/knowledge_bot/knowledge/kb-0068-g5-static-dataset-intake-2026-06-23.qmd`, line 116), so one local rule treated a spare target as a defect. The judge's own matching rules allowed equal counts: '- Equal or greater number of definitions/descriptions' (`icloud-work/evaluator/ap_benchmark/prompts/match.py`, line 12). The pass rates and reasons came from one model judge, with no learner data. A scan of the merged course flagged 192 match items announcing a decoy bucket (`grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd`, line 133); an announced decoy is itself a cue, so an extra target helps only when it is not announced.

<sub>criterion · format, options, integrity · universal · from ap, g3 · adopted-rule · contested · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Inference share follows the text

Fit the share of inference questions to what the text affords: a very easy text supports few honest inferences, and a flat target manufactures forced or unsupported items. One review judged a fair early-reader quiz to be about 15–30% inferential, against the 4% it found.

A pedagogy red team on a second-grade item rebuild argued that highly decodable text at a very low readability level is low-inference by design, so the quiz's 4% inference share was partly a text-level floor, not only weak item writing (`grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md`, lines 116-120). On such text, inference items risk becoming trivial, with the answer stated, or artificially hard inferences the text doesn't support, so pushing the share up can manufacture bad items (the same file, line 122). It asked for an inference target per band or reading level, accepting that the easiest band should be inference-light, while judging 4% too low even so (the same file, line 124).

Quoted:

- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md` (120): “**Highly decodable text at FK 0.9–2.2 is, by design, low-inference text.**”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md` (122): “On FK-0.9 decodable fiction, "inference" items risk becoming either (a) trivial/forced ("why is the boy happy?" → "because he got a dog," stated), or (b) artificially hard inferences the *text doesn't support*, which is a worse item-quality failure than literal recall.”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md` (122): “Pushing inference share up against a too-easy corpus can manufacture bad items.”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md` (124): “The design should **set the inference target per band/Lexile**, not a flat blueprint share, and accept that Band A *should* be inference-light.”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md` (124): “4% is genuinely *too* low even accounting for text level — a fair early-reader quiz lands more like 15–30% inferential”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/optionB-prime-narrow-rebuild.md` (82): “Per passage: ~30–40% inference (vs 4%)”

Against: The narrowed rebuild that followed still set one target for every passage: "Per passage: ~30–40% inference (vs 4%)" (`grade3-reading/ti-courseplans/courses/g2-reading/analysis/optionB-prime-narrow-rebuild.md`, line 82).

<sub>criterion · demand, stimulus · universal · from g3 · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Absent from the text is not a fault

A wrong option absent from the text is usually a sound contrast, so never report absence from the text as a defect on its own. Across 11 lessons, nearly every wrong option flagged for being absent from the text was a well-made contrast.

The reading audit flagged wrong options that share no words with the story, and across 11 lessons nearly every hit was a well-made contrast distractor, absent from the story because it was wrong. The flag was demoted to information and must never be reported as a defect on its own, since reusing the story's words would make a distractor easier to eliminate, not harder.

Quoted:

- `shadow-content-eval/SKILL.md` (83-84): “`DISTRACTOR-UNGROUNDED` is deliberately `info` and must never be reported as a defect on its own.”
- `shadow-content-eval/SKILL.md` (84-86): “Across 11 lessons nearly every hit was a *well-made* contrast distractor — for *"Who lives in the Wild Wood besides Badger?"* the wrong animal sets are absent from the story **because they are wrong**.”
- `shadow-content-eval/SKILL.md` (87-88): “Reusing story vocabulary would make a distractor easier to eliminate, not harder, so the premise is inverted for this common, correct pattern.”

Against: none found

<sub>method · stage: settle · distractors, evaluation, stimulus · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Ask a choice question open

Ask a choice question open only if its stem stands without the options; accept the right option in any words, and reply to a wrong one with its own feedback.

The rule came from exporting the lesson engine's quick checks to a 3D version, whose reading checkpoints are answered in the student's own words: the options leave the page, and the right one is what a secure answer shows (`g9/transformer/src/glue/threejs-render.js`). A stem that only works beside its options, caught by a phrase list such as "Which of these", is listed as skipped instead. The marking adapter asks the judge whether the answer gives the right option in meaning, in any wording, and gives a wrong option the judge is sure of that option's own feedback (`g9/transformer/src/glue/threejs-archivist.js`). A test asserts that no options reach the page (`g9/transformer/test/threejs-render.test.mjs`).

Quoted:

- `g9/transformer/src/glue/threejs-render.js` (7): “a reading checkpoint, asked open: the options go, the right one is what a secure answer shows”
- `g9/transformer/src/glue/threejs-render.js` (33): “a question that only works beside its options ("Which of these…") is not asked open”
- `g9/transformer/src/glue/threejs-render.js` (145): “its question only works beside its options”
- `g9/transformer/src/glue/threejs-archivist.js` (82): “A quick check asked open: the right option in meaning is secure; a wrong option gets that option's own feedback.”
- `g9/transformer/test/threejs-render.test.mjs` (58): “no options in the page”

Against: The open-stem test is only a phrase list (`g9/transformer/src/glue/threejs-render.js`), and on the last try the answer is given in place of a wrong option's feedback (`g9/transformer/src/glue/threejs-archivist.js`).

<sub>method · stage: write · format, stem, marking, feedback · universal · from g9 · adopted-rule · held · found in [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Ask whether another passage would do

Check that a question needs its passage by asking whether it would still work for a different passage on the same topic, and redesign it if it would.

A grade-5 specification for generated vocabulary items gives this test beside its one fixing rule, after a 120-item generated pool leaked at 95-100% by substandard in a text-hidden solve: the keyed meaning must need a passage-specific clue that overrides or narrows the word's common meaning. A question that would work as well for another passage on the same topic can be answered from the topic, not the text. The specification states the test for vocabulary items, and no measurement of the test itself is recorded.

Quoted:

- `grade3-reading/ti-courseplans/courses/g5-reading/llm/LLM_SPEC.qmd` (225): “Test: "Would this question work for a different passage on the same topic?" → If yes, redesign.”
- `grade3-reading/ti-courseplans/courses/g5-reading/llm/LLM_SPEC.qmd` (209): “**Root causes measured (120-item Claude-generated pool, blind-solve 2026-06-24):**”
- `grade3-reading/ti-courseplans/courses/g5-reading/llm/LLM_SPEC.qmd` (222-223): “**The correct answer must require a passage-specific context clue that overrides or narrows the word's common meaning.**”

Against: The specification states the test for vocabulary items only, and no measurement of the test itself is recorded.

<sub>method · stage: write · integrity, stimulus, stem · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Build a set from its source

For questions that share one source, choose the source first, list the distinct reasoning moves it supports, and write each question around a different move. In one 100-item build, 12 of 19 shared-source sets failed, against 3 of the other 81 items.

The pipeline's expectation matrix and pass contract both tell the writer to choose the source first, then work out distinct reasoning moves and write each question around a different one (`icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-ap-history-ib-expectation-matrix.md`, `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-pass-contract-matrix.md`). Shared-source sets failed far more often than other types: in one 100-item build, 12 of 19 sets failed, against 3 failures among the other 81 items (`icloud-work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build2_eval/evaluation_report.md`). The later repair rules fixed one move per question: an outside cause or context, then a comparison or continuity, then a consequence (`icloud-work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py`, lines 202-204).

Quoted:

- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-ap-history-ib-expectation-matrix.md` (122): “- Choose stimulus first, then create distinct child reasoning moves.”
- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-pass-contract-matrix.md` (71): “- build set backwards from stimulus: identify distinct APUSH reasoning moves first, then write each child around a different move.”
- `icloud-work/evaluatorML/.agent/memory/e2e_pipeline/apush_unit1_deterministic_build2_eval/evaluation_report.md` (14): “- By type: {'dbq': {'total': 21, 'passed': 20, 'failed': 1}, 'leq': {'total': 21, 'passed': 21}, 'mcq': {'total': 21, 'passed': 20, 'failed': 1}, 'mcq_set': {'total': 19, 'passed': 7, 'failed': 12}, 'saq': {'total': 18, 'passed': 17, 'failed': 1}}”
- `icloud-work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py` (202): “Question 1 must ask for the outside historical cause or context that best explains the stimulus, not what the stimulus says.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (555-557): “The set must cover related but nonduplicative operations. A source can support identification, inference, context, value or limit, and causal connection, but four stems should not ask the same question with altered wording.”

Against: none found; no run isolates the effect of the build order.

<sub>method · stage: write · stimulus, demand · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Cover every case the objective spans

When an objective or standard spans several cases or elements, list them in the plan and give each question a different one, since material missing any one fails alignment. On a first partial run, question sets passed 1 of 4, with concept coverage the main failure.

On a first partial AP run, question sets passed 1 of 4, failing mainly on concept coverage: the judge found a quiz concentrated on one nation's motives while its objective covered several nations, and the record's diagnosis is that the writer picks the most prominent case in the topic and concentrates its questions there. The plan step was meant to force coverage but did not enforce it across questions. The planned fix lists the cases to cover in the plan and has each question address a different one; it has not yet been measured.

Quoted:

- `icloud-work/ML learnings/sft_v7_benchmark_postmortem.md` (14): “| MCQ_SET | 1/4 = **25%** | concept_coverage |”
- `icloud-work/ML learnings/sft_v7_benchmark_postmortem.md` (78): “But the plan step doesn't enforce concept coverage across questions.”
- `icloud-work/ML learnings/master_strategy_apr24.md` (43): “Add `nations_to_cover: ["Portugal", "Spain", "France", "England"]` field to the Plan step output schema. Question step: each question must address a different nation from the plan. Prompt-only change in `mcq_set.py`.”
- `icloud-work/ML learnings/sft_v7_benchmark_postmortem.md` (20): “This is a partial run (unit 1 only, benchmark still in progress). But the failure patterns are clear enough to diagnose.”
- `icloud-work/ML learnings/what_to_do_next.md` (33): “- MCQ_SET: 25% → ~40%”
- `icloud-work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md` (114): “The quiz omits the 'Caste' (Casta) system entirely.”
- `icloud-work/ap-social-studies-generator/python/benchmark_results/unit_3/diagnosis.md` (76): “While the quiz covers the role of women and 'Republican Motherhood' with great depth, it fails the 70% threshold for concept coverage.”
- `icloud-work/ap-social-studies-generator/docs/archive/COMPREHENSIVE-TEST-2026-02-17.md` (82): “the question completely fails to address the required sub-topic 'disease'”
- `icloud-work/inceptbench` (commit ee21a33) (8-11): “#341: curriculum_alignment partial coverage - Add COMPLETENESS CHECK: explicitly listed elements in standard must ALL appear - Add PROPORTIONALITY CHECK: 'various groups' requires 3+ representatives - curriculum_alignment = 0.0 if any explicitly required element is entirely absent”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/article/evaluation.txt` (111): “- **curriculum_alignment**: Enumerate the explicit elements listed in the standard and verify EACH one appears in the article.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md` (282): “- L.3.4 is over-concentrated on prefix meaning specifically (26 of 31 items)”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md` (176): “L.3.4 is dominated by prefix-meaning items (26 of 31 marked `deprioritize=True` in bank_forms.json).”

Against: This rests on one partial run of 4 question sets, one failing set failed on structure rather than coverage, and the fix has only an expected gain, from 25% to about 40%. The counts were small (1, 3 and 6 coverage failures in units 1 to 3, per the diagnosis headers), and covering every part across a set can pull against keeping each item narrow.

<sub>method · stage: ground · alignment, generation · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Define difficulty per skill

Define each difficulty level per skill and check every label against that skill's own definition, because one global rule for easy or hard mislabels items. Across 1,888 judged items, difficulty alignment caused 564 failures, second only to factual accuracy.

Across 1,888 judged math items, difficulty alignment was the second most common failure, with 564 failures (40.0%) after factual accuracy's 650 (`icloud-work/incept/nova_forge/EXECUTIVE_SUMMARY.md`, lines 11 and 52-56). The judge read each standard's own definitions, for example finding an item labelled easy that matched the medium definition for its standard (`icloud-work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md`, line 23). A grade 4 curriculum file defines the levels per skill, for example by which step of a pattern the question asks about (`icloud-work/incept/incept-multilingual-generation/edu_configs/curriculum_grade_4.jsonl`, line 1). A pass-rate analysis traced the failures to generic guidance such as "EASY: small numbers" (`icloud-work/incept/nova_forge/PASS_RATE_ANALYSIS.md`, line 81); that is its diagnosis, not a measurement.

Quoted:

- `icloud-work/incept/nova_forge/EXECUTIVE_SUMMARY.md` (11): “Comprehensive analysis of 1,888 existing test questions across grades 4, 6, 7, and 8 with a quality threshold of 0.85.”
- `icloud-work/incept/nova_forge/EXECUTIVE_SUMMARY.md` (52): “1. **Factual Accuracy** - 650 failures (46.1%)”
- `icloud-work/incept/nova_forge/EXECUTIVE_SUMMARY.md` (56): “2. **Difficulty Alignment** - 564 failures (40.0%)”
- `icloud-work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md` (23): “- **Issue:** Labeled as Easy but matches the provided Medium definition for this standard.”
- `icloud-work/incept/incept-multilingual-generation/edu_configs/curriculum_grade_4.jsonl` (1): “"difficulty_matrix": "EASY\n- Steps one to three are given and the question asks about step 4.”
- `icloud-work/incept/nova_forge/PASS_RATE_ANALYSIS.md` (81): “- Generic difficulty guidance ("EASY: small numbers") doesn't match specific requirements”
- `icloud-work/incept/nova_forge/FIX_SUMMARY.md` (71): “'easy': (100, 999),”
- `icloud-work/incept/nova_forge/README.md` (197): “- **Result**: <1% range errors (was 15%)”

Against: The pipeline then hard-coded one number range per level for every skill, "'easy': (100, 999)," (`icloud-work/incept/nova_forge/FIX_SUMMARY.md`, line 71), and its README reports "<1% range errors (was 15%)" (`icloud-work/incept/nova_forge/README.md`, line 197) with no scored run cited for it.

<sub>method · stage: ground · demand, alignment · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Design the evidence before the item

Before writing a scored item, state what it is evidence for: the knowledge it targets, the claim a right answer supports and the evidence that counts.

The reading project's assessment rules say that with no knowledge component, claim, evidence indicators, task conditions, outcome space and scoring rule, there is no assessment. The rule follows evidence-centred design, which the project's assessment evidence base cites (Mislevy, Almond & Lukas 2003). Besides the target, claim and evidence, state the task conditions, the range of answers including variants and near misses, the scoring rule and the shortcuts that must fail.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` (84-85): “- no KC, claim, evidence indicators, task conditions, outcome space, and scoring rule means no assessment;”
- `grade3-reading/knowledge_bot/knowledge/kb-0162-assessment-item-difficulty-evidence.qmd` (269): “Mislevy, R. J., Almond, R. G., & Lukas, J. F. (2003). A brief introduction to evidence-centered design.”
- `grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md` (541): “Two people can read the same prose KC and imagine completely different tasks, difficulty levels, and acceptance thresholds”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md` (48): “**No item ships without a knowledge claim it is evidence for.**”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md` (52): “The banks today carry **zero** `kc`, `scoring_rule`, or `cue`/`supports` fields (verified: 0/432).”
- `grade3-reading/ti-courseplans/docs/academics-alignment-plan.md` (21): “A KC without a pack is prose, not a construct.”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-ENTRYPOINT-CLEAN-ROOM-G3-U4-L1-2026-08-06.qmd` (61): “4. The constructed response has no rubric, acceptable variants, near misses, scorer, or feedback contract.”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0164-g3-v2-feedback-agent-routing.qmd` (84-85): “- no KC, claim, evidence indicators, task conditions, outcome space, and scoring rule means no assessment;”
- `grade3-reading/edullm-review-hub/course-packages/quality/golden-student-course/versions/1.0.0/STANDARD.qmd` (638): “questions declare single- or multi-location demand; scoring accepts every defensible evidence set.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/evidence/case-for-review.md` (67): “All 550 items carry measurement_contract.evidence with an explicit single-span or multi-span mode and the required relationship among spans.”
- `grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/sources/ASSESSMENT-PACKS.md` (6): “**The lever for LLM-scorer reliability is pack tightness, not prompt engineering.**”
- `grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/sources/ASSESSMENT-PACKS.md` (8-9): “Each pack has the six `[CK 541]` fields — **statement of competence · affordances · acceptance criteria · exemplars · near-misses (with the failed criterion named) · forbidden shortcuts**”
- `grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/sources/ASSESSMENT-PACKS.md` (10-12): “The **exemplars + near-misses + model answer, once human-scored, ARE the gold set** for that KC; the **acceptance criteria + forbidden shortcuts ARE the rubric** the LLM scorer is calibrated against”
- `grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/sources/GENERATION-CONTRACT.md` (10-11): “No prompt is generated until its KC's Assessment Pack exists”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/ASSESSMENT-QUALITY-MEMO.md inside it) (9): “**Every graded item is an evidence claim, not a question: it exists to license one inference about one knowledge component, under a stated scoring rule, using a task whose supports and cues are deliberate.**”

Published: [Mislevy, Almond & Lukas 2003](https://doi.org/10.1002/j.2333-8504.2003.tb01908.x)

Against: An adopted rule drawn from the reading project's assessment entries; the note records no measurement behind it.

<sub>method · stage: ground · alignment, evidence-of-learning, scoring-guide · universal · from g3, research · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Fix a cue by making the item harder

Fix a cue that points to the key by making the item harder, never by deleting what makes the key uniquely right, which can leave two options equally right. In one lesson, all three suggested rewordings that cleared a word-overlap scan fit a wrong option at least as well as the answer.

A word-overlap cue check in a Grade 3 reading build was red in all three units; one guided-practice stem carried a phrase found in exactly one option, the answer, which the build's BrainLift says lets a child match keywords instead of reading. The shipped fix reworded the stem, and the fixes ledger records the item as harder, not merely un-cued, because a wrong option also names a gift, so the item turns on whose domain is whose. In another lesson the three suggested rewordings all cleared the scan but described a wrong option at least as well as the answer, so the fix kept the answer's generality and dropped only the lexical echo, since an ambiguous item is the worse defect. The BrainLift's rule is that a fix that only removes the cue makes the item easier, while the fix worth shipping makes it harder; the build's schema adds that a cue singling out a wrong option is fine and often good.

Quoted:

- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v3/FIXES-LEDGER.md` (123): “`cue_check` red in all three units.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v3/FIXES-LEDGER.md` (124): “a phrase in exactly one option — the answer”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/BRAINLIFT.md` (189-190): “A we-do stem that hands over a phrase appearing in exactly one option lets the child match keywords instead of reading.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v3/FIXES-LEDGER.md` (128-129): “The item is harder, not merely un-cued: option 0 also names a gift, so it turns on whose domain is whose.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/content/U1-L7/AUTHORING-NOTES.md` (1243): “The three candidates offered”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/content/U1-L7/AUTHORING-NOTES.md` (1244-1245): “all clear the scan, but they also describe **option 2**”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/content/U1-L7/AUTHORING-NOTES.md` (1246): “at least as well as they describe the answer.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/content/U1-L7/AUTHORING-NOTES.md` (1248-1249): “Dropping the generality marker to satisfy a word-overlap scan would have traded a surface cue for a genuinely ambiguous item, which is the worse defect.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/content/U1-L7/AUTHORING-NOTES.md` (1251): “So the given keeps the generality and drops only the lexical echo”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/BRAINLIFT.md` (191): “fix that only removes the cue makes the item *easier*; the fix worth shipping makes it **harder**.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/CONTENT-SCHEMA.md` (609): “A cue that singles out a WRONG option is fine and often good”

Against: none found

<sub>method · stage: improve · integrity, options, distractors · universal · from g3 · measured · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Keep teaching and its check apart

Keep a worked example and the independent check of the same idea on different screens, and fail any option sharing five or more consecutive words with on-screen teaching text.

The reading course's authoring playbook, written so that the 16 mistakes of a first lesson build are prevented at authoring time, says the teaching display (example and non-example) and the independent check may not share a screen, so the check needs a reread of the passage and no option is near-verbatim to the example. Its self-audit checklist fails any check answerable by visible word-match, a run of five or more words shared by an option and the same screen's teaching text. A read of a demonstration unit as delivered found its teaching articles had pre-answered their certified release checks, a must-fix.

Quoted:

- `grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md` (86): “The teaching display (example/nonexample) and the independent check may not share a screen”
- `grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md` (301): “word overlap between an option and same-screen teaching text = fail).”
- `grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md` (27): “Gradual-release leak: l0/l1 teaching articles pre-answered their certified release checks (must-fix)”
- `othello-course-renderer-draft/repo/authoring/inputs/prompt-packs/reading-g3/procedures/find.md` (17-20): “The modelling page holds ONLY the passage and the think-aloud (plus the think-aloud's own optional `why_check`). Never put an `scr`, `msq` or other child-answered item on a modelling page: the whole point of "I do" is that the guide does it, and a gated question here reverses the release.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-23.md` (18-20): “On L4 every word of the correct option appears in the sentence just spoken (100%); on L5, L6 and L7 the overlap is 44-55%, which is ordinary. A non-responding child can clear a required gate by echoing.”
- `grade3-reading/.claude/skills/lesson-build/SKILL.md` (26): “card page → own checks page”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (327-329): “so the "independent" check is answerable purely by matching visible words from two paragraphs above it, never by rereading the passage.”

Against: Two approved reference lessons check a just-taught idea on the same page, and an adjudication ruled that teaching-then-checking on one page is the pattern, not a leak (`grade3-reading/artifacts/g5-course/G3-U1-L4-RESIDUAL-ADJUDICATION-2026-08-21.md`, line 35); the five-word threshold is one playbook's choice.

<sub>method · stage: settle · integrity, sequence, options · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Key it to what only the text holds

Key each question to what only the text settles, never to an order, category, word sense or fact the world already supplies. In one unit, 8 of 11 cause questions leaked because the key was the answer a solver without the text would most likely guess.

In one unit's text-hidden gate, 8 of 11 cause questions leaked because the key was the solver's most likely guess from the story's general shape; the survivors hid the key behind details inside the text (the order of events, who acted, which note said what) or let a decoy the world favours out-compete the key. Ordering items did best among the formats other than sorting but failed whenever the steps had a natural order, such as problem, solution, result, and in another bank ordering items built on familiar sequences passed the text-hidden check only about 45% of the time. In context-clue word questions, the 8 that survived used words in technical or domain senses and the 7 that leaked used words in their everyday meaning, and the plan for new items asks that a word's meaning be derivable only from the passage. Word each stem to ask what the text says. Where the text overturns the usual or everyday answer, make that answer a wrong option.

Quoted:

- `grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md` (62): “key is the blind solver's plurality narrative guess dies (8/11 cause leaks, incl.”
- `grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md` (64): “referents (event order, actor identity, note provenance) or anti-schema keys where”
- `grade3-reading/artifacts/LANE2_GENERATOR.md` (202): “every correct answer depends on a passage-specific invented detail that cannot be retrieved from prior knowledge”
- `grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md` (278): “Sequence worked better than the other non-match formats, but it failed whenever the fragments had a natural order:”
- `grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md` (285): “The surviving sequence items need neutral, non-orderable details whose order depends on passage location, not common logic.”
- `grade3-reading/artifacts/LANE2_GENERATOR.md` (50): “| sequence | 100% | ~45% (world-knowledge seqs) | Some steps deducible without passage |”
- `grade3-reading/artifacts/LANE1_COURSE.md` (240): “8 survivors: technical/domain-specific words (normal, base, draws, channels, reservations, niche, range, intrusive). 7 leaked: dominant-meaning words”
- `grade3-reading/artifacts/LANE3_LLM.md` (244): “a word's meaning must be derivable only from the passage, not from world knowledge”
- `grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md` (20): “| fragment-sequence | 24 | 24 | 0 | 0 | 100% |”
- `grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md` (22): “| choice-hottext | 24 | 4 | 19 | 1 | 17% |”
- `grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md` (28): “Plain choice/hot-text confirms its high-leak prior (13/16 MCQ leaked).”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md` (17): “| sequence | 185 | **58.4%** | 3.0% | **~19×** | adjacent-pair order 85.2% |”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md` (32): “real-world things have canonical categories — recoverable with zero reading.”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md` (44): “items must hinge on passage-unique facts a general model can't recover”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md` (45-46): “invented entities/quantities/relations, story-specific event order rather than canonical process order, passage-defined categories rather than natural-kind categories”
- `grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md` (65): “a world-favorite decoy out-competes the key”
- `grade3-reading/artifacts/alpha-read-packager/generator/RESULTS.md` (32): “GK default (d) "walls keep out water" is the trap; text says cold WINDS → blind solver actively misled to {a,d}; {a,b} text-locked”
- `grade3-reading/artifacts/alpha-read-packager/FIX_LIST.md` (75): “Prompt 'Match each cause to its correct effect based on how the water cycle works' explicitly invites world-knowledge, not the text.”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/MSQ_REGEN_GUIDE.md` (39): “The stem must invoke a passage-specific standard”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (90-92): “the keyed sense must be the one the PASSAGE forces, and at least one … distractor must be the word's *common* dictionary sense that the passage does NOT use — … so a blind solver who picks the everyday meaning is wrong.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (92-95): “**The tested word and its … keyed sense must both actually appear/operate in the passage** (guard against the G3 … vocab-word-mismatch bug: never test a word that isn't in the passage, never key a sense … the passage doesn't license).”
- `grade3-reading/knowledge_bot/skills/timeback-course-fix/SKILL.md` (46-47): “**Vocab word-not-in-passage … FIX by editing the PASSAGE — `PUT {QTI}/stimuli/{id}` to use the word in context. Never reword the stem to dodge it; never delete the item.”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md` (171): “Never repair a missing quote by changing the passage unless the passage authority itself is wrong.”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/analysis/methodology-2026-07-07/README.md inside it) (14-17): “- Sequence: quote NON-orderable fragments ("the earthworms in our gardens", "act like natural pipes", "thriving plant life") — no logical/world order among them, so only text position orders them. (Cloning "arrange the steps of obsidian formation" leaks: 6% survive; fragment construction: 60% survive.)”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/QUESTION_CONVERSION_RETROSPECTIVE.qmd inside it) (288-289): “Sequence was the best non-match route, but only when fragments did not form a natural story, process, or chronology.”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/QUESTION_CONVERSION_RETROSPECTIVE.qmd inside it) (344-347): “Non-orderable sequence worked when fragments were arbitrary, passage-specific, and not reconstructable from real-world chronology. Sequence failed when the order could be recovered from common chronology, narrative convention, or a single lucky shuffle.”
- `grade3-reading/artifacts/g5-course-candidate-v0/assessments/assessment_rejection_report.qmd` (11): “Exact key recovered: 148 / 152 (0.974).”
- `grade3-reading/artifacts/g5-course-candidate-v0/assessments/assessment_rejection_report.qmd` (13): “Decision: current selected assessment forms are rejected for mastery/MAP use.”
- `grade3-reading/artifacts/g5-course-candidate-v0/assessments/assessment_rejection_report.qmd` (20): “2: The feeling arc strongly cues the likely order.”
- `grade3-reading/artifacts/g5-course-candidate-v0/assessments/assessment_rejection_report.qmd` (31): “1: Each quote directly signals the category.”
- `grade3-reading/artifacts/g5-course-candidate-v0/assessments/assessment_rejection_report.qmd` (42): “Do not use sequence labels or process wording that gives chronological order without the passage.”
- `grade3-reading/artifacts/g5-course-candidate-v0/assessments/assessment_rejection_report.qmd` (43): “Do not use match categories or options that encode their own answer.”
- `grade3-reading/artifacts/spine-solve-calibration-2026-07-10/REPORT.md` (95): “*Vector:* fragments are word-for-word story quotes with intrinsic narrative chronology — orderable without the source.”
- `grade3-reading/artifacts/g5-stage3-llm-guidance/HANDOFF.md` (88-89): “the dominant residual leak is commonsense-recoverable canonical **order** (honey-making, paper recycling, chocolate, frog life-cycle)”
- `grade3-reading/artifacts/u4l2-build/g5-audit/KB-NOTES.md` (116-118): “Vocab-in-context items: keyed sense must be the one the passage forces; at least one distractor is the common dictionary sense the passage does NOT use; never test a word absent from the passage (the G3 vocab-word-mismatch bug).”
- `grade3-reading/artifacts/u4l2-build/g5-audit/KB-NOTES.md` (119): “`G5_GENERATOR.md` §(a) rule 6”
- `grade3-reading/ti-courseplans/courses/g5-reading/llm/LLM_SPEC.qmd` (205-206): “L.5 vocabulary items fail blind-solve at high rates (~99%) when the target word carries its common meaning and the student can guess from background knowledge alone.”
- `grade3-reading/ti-courseplans/courses/g5-reading/llm/LLM_SPEC.qmd` (217): “| L.5.4a (context clues) | 95% | Common vocabulary used in its most familiar sense |”
- `grade3-reading/ti-courseplans/courses/g5-reading/llm/LLM_SPEC.qmd` (222-223): “**The correct answer must require a passage-specific context clue that overrides or narrows the word's common meaning.**”
- `grade3-reading/ti-courseplans/courses/g5-reading/llm/LLM_SPEC.qmd` (231): “The 3 distractors must include the common meaning — only the passage-specific meaning is correct”
- `grade3-reading/course-renderer/docs/video/u1-script-critique.md` (212-213): “A child who has never seen the video can eliminate all three distractors on the giant alone, since a giant in a cave is not a choice, not a home and not a friend.”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/markdown/generation-contract.md inside it) (75-77): “**canon facts are banned as answers** ("Columbus sailed in 1492" is not an item).”
- `othello-course-renderer-draft/repo/docs/video/u1-script-critique.md` (216-218): “A version of checkpoint 2 that actually depends on the video would key on something the video said rather than on the category, for example which of the three the crew was warned about or what Odysseus did about the song.”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l3.json` (307): “NO ITEM'S CORRECT ANSWER MAY BE A PLOT FACT.”

Against: Items keyed to invented details passed 100% only on a check where the same model family wrote and solved them, which the report names as its one unmitigated risk (`grade3-reading/artifacts/LANE2_GENERATOR.md`, line 204). Ordering items built from snippets of a text passed the blind gate in one pilot, yet several failed on quality for testing the wrong standard, using weak fragments or becoming mechanical put-these-snippets-in-order tasks (`grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md`, line 89), and the context-clue result rests on 15 items (`grade3-reading/artifacts/LANE1_COURSE.md`, line 240). Keying against the usual answer makes the wrong options easy to rule out once the text is read: a quality screen flagged 14 of 26 such items (`grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md`, lines 94-99). The 480-item probe used one solver family with forced guessing and no with-text control (`grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md`, lines 50-57), and the unit gate's solver is now treated as historical provenance (`grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md`, lines 5-6). Pointing the stem at the text is not enough on its own: in a 480-item probe the stems said 'Based on the text…' but the answers did not depend on the text (`grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md`, line 30). How to repair a mismatch is not settled: the course-fix rule edits the passage to use the word, while a content-integrity rule says never to repair a missing quote by changing the passage unless the passage itself is wrong (`grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md`).

<sub>method · stage: write · key, integrity, distractors · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Length targets from top-scoring answers

Set a written response's target length from the measured length of top-scoring released answers, not from the size of the answer box. One test's essay box holds about 400 to 460 words, while its top-scoring grade 3 exemplars ran about 130 to 235.

A research report on a state test's grade 3 essay checked a common target of about 400 words against the released scoring guides and found it was the answer box's capacity, 2,300 characters excluding spaces, not the expected length. The top-scoring exemplars it measured across three released years ran about 130 to 235 words, so it set a realistic target of about 150 to 250 words, or 5 to 12 sentences.

Quoted:

- `grade3-reading/course-renderer/docs/extras/alpharead-staar-writing-research.md` (29): “**Word-count QA verdict:** "≈400 words" is the **box CAPACITY, not the expected length**. Box holds **2,300 characters excluding spaces** (≈400–460 words). Top-scoring (3/2) G3 exemplars run **~130–235 words** — typically **150–250 words / 5–12 sentences**. Realistic target ≈ **150–250 words**, not 400.”
- `grade3-reading/course-renderer/docs/extras/alpharead-staar-writing-research.md` (125): “**Top-score (3/2) exemplar word counts (measured):** 2025: ~230, ~235; 2024: ~130, ~230; 2023: ~190, ~180.”
- `grade3-reading/course-renderer/docs/extras/alpharead-staar-writing-research.md` (12): “Not our course, and Texas-specific.”
- `othello-course-renderer-draft/repo/docs/extras/alpharead-staar-writing-research.md` (125): “**Top-score (3/2) exemplar word counts (measured):** 2025: ~230, ~235; 2024: ~130, ~230; 2023: ~190, ~180.”
- `othello-course-renderer-draft/repo/docs/extras/alpharead-staar-writing-research.md` (129): “**Verdict: 400 words is BOX CAPACITY, not target length.**”
- `othello-course-renderer-draft/repo/docs/extras/alpharead-staar-writing-research.md` (131): “Box: **2,300 characters, not counting spaces** ≈ **~400–460 words** max capacity — the likely origin of the "400 words" number.”
- `othello-course-renderer-draft/repo/docs/extras/alpharead-staar-writing-research.md` (132): “Perfect-trait G3 exemplars run **~130–235 words** (cluster ~180–235). None near 400.”
- `othello-course-renderer-draft/repo/docs/extras/alpharead-staar-writing-research.md` (135): “**App recommendation:** set the end-of-unit target at a well-organized **~150–250-word essay**; treat 400 as a ceiling.”

Published: [Texas Education Agency, 2025 STAAR Grade 3 RLA released test scoring guide](https://tea.texas.gov/student-assessment/staar/2025-staar-rla-3-released-test-scoring-guide.pdf) · [Texas Education Agency, Grade 3 RLA Constructed-Response Scoring Guide, Spring 2024](https://tea.texas.gov/data-reports/staar/2024-staar-3-rla-scoring-guide.pdf) · [Texas Education Agency, Grade 3 RLA Constructed Response Scoring Guide, Spring 2023](https://tea.texas.gov/student-assessment/staar/2023-staar-3-rla-scoring-guide.pdf)

Against: The counts are approximate and rest on six measured exemplars, two a year over three years of one state's test, and the report marks itself as not the course's own and specific to that state ("Not our course, and Texas-specific.", `grade3-reading/course-renderer/docs/extras/alpharead-staar-writing-research.md`, line 12).

<sub>method · stage: ground · demand, alignment, format · universal · from g3 · measured · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Let the sources fix what a definition grades

Grade a concept only on features every authoritative source treats as defining, teaching usual ones as typical, and never build a wrong option on a sense any source accepts. Of three features a first pass claimed for one literary term, checking glossaries left one that every source treats as defining.

Research for a lesson on a literary term checked dictionaries and glossaries: a first pass claimed three features missing from the course's definition, and validation cut them to one that every source treats as defining (`othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md`, lines 125-129). Features only some sources list belong in the passage as what such works usually carry, never in the definition a child is graded against, and the lesson plan adopted that (lines 131-135; `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l1.json`, line 483). The same research found a broad modern sense of the term accepted by some sources, so an option built on it is nearly right rather than wrong, while one built on "it just means very long" is fair (lines 215-219). The course's shipped intro video had already keyed that broad sense as a checkpoint's correct answer (the plan, line 483).

Quoted:

- `othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md` (125-126): “The first pass on this claimed three missing features. Validation cut it to one, and the one that survives is enough on its own.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md` (128-129): “Every source checked treats that as definitional, and our definition drops it.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md` (134-135): “Both belong in the passage as what epics usually carry, never in the definition a child is graded against.”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l1.json` (483): “Long narrative POEM is universal across the sources checked.”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l1.json` (483): “divine intervention appears in only one of three glossaries and there only as something that frequently happens, so neither belongs in a definition a child is graded against.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md` (215-217): “One caution for distractor writing: a broad modern sense of epic as simply a long heroic story is accepted by some sources, so "a long story about a hero" is nearly right rather than wrong.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md` (218-219): “A distractor built on "it just means very long" is fair; one built on "a long story about a hero" is not.”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l1.json` (483): “the authored Unit 1 intro video gates on a checkpoint whose correct answer is a long story about a hero's journey and its trials, so the child is already assessed on story rather than poem”
- `grade3-reading/course-renderer/docs/research/g4-u1-l1-what-is-an-epic.md` (215-219): “One caution for distractor writing: a broad modern sense of epic as simply a long heroic story is accepted by some sources, so "a long story about a hero" is nearly right rather than wrong. The wrong part is dropping the verse form, the people's stake and the gods, not the largeness. A distractor built on "it just means very long" is fair; one built on "a long story about a hero" is not.”
- `grade3-reading/course-renderer/content/lesson-plans/g4-u1-l1.json` (490): “Distractor consequence: a broad modern sense of epic as a long heroic story is accepted by some sources, so a long story about a hero is nearly right rather than wrong. It just means very long is a fair distractor; a long story about a hero is not.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l1-what-is-an-epic.md` (131-135): “**Not universal, so not assessable:** the fate of a whole people riding on the hero appears in Abrams' glossary but not in the Poetry Foundation's. Divine intervention appears in one of three glossaries, and there only as something that "frequently" happens. Both belong in the passage as what epics usually carry, never in the definition a child is graded against.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l1-what-is-an-epic.md` (128-129): “**Universal:** an epic is a long narrative **poem**. Every source checked treats that as definitional, and our definition drops it.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l1-what-is-an-epic.md` (125-126): “The first pass on this claimed three missing features. Validation cut it to one, and the one that survives is enough on its own.”
- `grade3-reading/course-renderer/docs/video/u1-script-and-visual-plan.md` (364-368): “Research section 5 puts the people's stake in what epics usually carry and explicitly not in "the definition a child is graded against", because it is not universal across the glossaries checked. So it is spoken, and it is not assessed, and neither the closing item nor either proposed in-video item keys on it.”

Against: none found

<sub>method · stage: ground · key, distractors · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Name the leak before repairing it

To repair an item answerable without its text, name how it leaks, such as world knowledge, a keyword cue, option symmetry or chronology, then change what it asks.

A Grade 5 reading item-conversion retrospective lists what failed in its repair campaign, raw selected-response items kept as they were and wording polish without leak-vector diagnosis, and among what worked, changing the construct rather than only the wording. Its reusable recipe first classifies the leak vector (world knowledge, keyword or title cue, option symmetry, real-world chronology, Part A/Part B coupling, signposted evidence, a response-processing trap or a renderer or protocol artifact) and then chooses a construct that attacks it instead of paraphrasing. In a Grade 3 fix list, one item built on world-famous facts was rejected as unfixable by distractor surgery and in need of content replacement.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/QUESTION_CONVERSION_RETROSPECTIVE.qmd inside it) (448-451): “2. Classify the leak vector: world knowledge, keyword/title cue, option symmetry, real-world chronology, Part A/Part B coupling, signposted evidence, response processing trap, or renderer/protocol artifact. 3. Choose a construct that attacks that leak vector. Do not merely paraphrase.”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/QUESTION_CONVERSION_RETROSPECTIVE.qmd inside it) (116-119): “What failed: - raw selected-response as-is; - wording polish without leak-vector diagnosis;”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/QUESTION_CONVERSION_RETROSPECTIVE.qmd inside it) (111): “- change the construct, not just the wording;”
- `grade3-reading/_archive/2026-08-13-consolidation/top-level-docs/HANDOFF_3_KEY_ISSUES.md` (8): “(a) `cc-camels-mcq-04` rejected — needs content replacement (world-famous facts, unfixable by distractor surgery);”

Against: A Grade 3 mastery gate hardened in place went from 84.2% to 64.0% blind-solvable after 47 hardened items were deployed (`grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-main-checkout-jul-work.patch`, line 610): a partial gain, and that line does not say how the items were hardened.

<sub>method · stage: improve · integrity, format, stem · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Neutral labels for which-source items

In an item that asks which source states a detail, use neutral labels and statements balanced across the sources' topics, so only reading the sources tells which one says what. Built this way, one run kept 700 items that a solver could answer with the sources but not without them.

In a Grade 5 generation run, source-attribution items produced the volume: categories were neutral (Source A, Source B, Both), passage titles were not category labels, statements were topically symmetric, Both meant explicit shared support, and the key required reading which source stated the detail (`grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd`). The retrospective says this removes title, topic and keyword leakage and avoids chronology and world-knowledge paths, and its final cut kept 700.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (44-48): “- categories were neutral: `Source A`, `Source B`, `Both`; - passage titles were not category labels; - statements were topically symmetric; - `Both` meant explicit shared support, not broad inference; - the keyed category required reading which source stated the detail.”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (52-53): “- it removes title/topic/category keyword leakage; - it avoids chronology/process/world-knowledge paths;”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (144): “| final cut | 700 |”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (69): “the 700 MATCH tranche used a Gemini cross-family gate with `loosened` bar”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (217-220): “Quality-B was not run across every final item: - used on the small sequence MODIFY pilot; - not run over the final 700 MATCH or final 167 non-match items.”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/QUESTION_CONVERSION_RETROSPECTIVE.qmd inside it) (335-336): “- every item needed at least one Source A, one Source B, and one Both statement; - `Both` required explicit shared support, not a broad topic-level inference;”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/QUESTION_CONVERSION_RETROSPECTIVE.qmd inside it) (272-275): “The 417 source-attribution candidates that failed with-passage control were not mostly "leaky." They were often ambiguous or overbroad around `Both`, frequently missing one statement in an otherwise near-correct match. This is why with-passage control is a quality gate, not just an answerability formality.”
- `grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/RUN_REPORT_2026-07-08.md` (54): “Gemini blind leak gate run until enough additions were certified: 715 certified, 0 blind leaks observed.”

Against: Those 700 were certified under a loosened blind bar, and no quality review was run over them (the same file).

<sub>method · stage: write · options, integrity, stimulus · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Never reword a question for the interface

Never change a question's wording to feed an interface feature, such as adding a clause so an annotation has another word to mark. One question gained a clause so its annotation had a third word to mark, and was restored to its original after review.

A check sheet for one Grade 3 lesson in the reading course renderer records that a clause was prepended to its question on 16 September so the question's annotation had a third word to mark, and that a rewrite two days later turned the question into a comparison (`grade3-reading/course-renderer/scripts/verify/L2-WEDO-QC.md`, line 3). Review on 22 September rejected the rewrite, asking why there should be a comparison and what the question had been before. The restore took the question back to its original wording of 3 September, the clause and its third mark went with it, and the sheet now checks that the original question is the one shown (line 7).

Quoted:

- `grade3-reading/course-renderer/scripts/verify/L2-WEDO-QC.md` (3): “The question is the ORIGINAL 3 September one, "How does Aladdin feel when the huge genie appears?"”
- `grade3-reading/course-renderer/scripts/verify/L2-WEDO-QC.md` (3): “this question is crap. When did it become 'braver than his mother'. Why should there be a comparison? What was it before?”
- `grade3-reading/course-renderer/scripts/verify/L2-WEDO-QC.md` (3): “no "His mother is terrified." clause, the one PR #299 prepended on 16.09 so the annotation had a third word to mark”
- `grade3-reading/course-renderer/scripts/verify/L2-WEDO-QC.md` (3): “the third mark and its New word lines went with the clause”
- `grade3-reading/course-renderer/scripts/verify/L2-WEDO-QC.md` (7): “(the original, no mother clause)”

Against: none found

<sub>method · stage: write · stem, wording · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### No format is leak-proof

No item format is leak-proof and each leaks its own way, so test every item with the text hidden using a strong solver. Under the first gate, 97% of multiple-choice items were answered without the passage, against 0% of matching items.

A cross-family anti-leak gate recorded blind recovery by format: multiple-choice 97%, multiple-select 100% and two-part evidence items 80% were rejected, against hot-text 24%, sequence 42% and match 0%, which left a 541-slot skeleton only 32.7% fillable. After a passage-design fix the measured leak was 99.5% for multiple-choice, 100% for multiple-select and ~0.56% for the other formats. A strong-solver re-gate then left only 20 of 95 'clean' items and 187 of 3,146 untested candidates (5.9%), so the low rates depended on the solver. Single-choice items leak through general knowledge or a textbook-correct option, multi-select items through options that reinforce each other, highlight items through stems that signpost the span, and ordering items through events with a natural order. Design each format against its own leak, and prefer forms built to need the reading.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd` (34-36): “a 541-slot skeleton was only 32.7% fillable (177 keeper items) because the anti-leak gate scored MCQ 97% / MSQ 100% / EBSR 80% blind-recovered (reject) vs. hot-text 24% / sequence 42% / match 0% (pass).”
- `grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd` (105-106): “Measured leak by type: MCQ 99.5%, MSQ 100%, hot-text/sequence/match/EBSR ~0.56% after the 06-24 passage-design fix.”
- `grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd` (67-69): “showed the weak gpt-4o-mini gate had over-credited items — of v1's 95 re-gated "clean" items, only **20 (21%) survived**; **75 leaked** under the strong solver.”
- `grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd` (69): “Of 3,146 un-gated existing candidates, only 187 (5.9%) survived the strong blind-solve.”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (208-210): “- MCQ leaked through ordinary school knowledge, vocabulary, or a "textbook correct" option; - MSQ leaked through mutually reinforcing correct options; - hot-text leaked when stem/span wording signposted the answer.”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (214-215): “- failed when fragments had natural story/process order; - survives only when details are neutral and non-orderable without passage location.”
- `grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd` (167-170): “| MCQ | 89/90 = 98.9% | 41/89 = 46.1% | | MSQ | 83/90 = 92.2% | 21/83 = 25.3% | | hot-text | 39/90 = 43.3% | 6/39 = 15.4% | | sequence | 88/90 = 97.8% | 45/88 = 51.1% |”
- `grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd` (111-112): “20 flagged STILL_LEAKY (mechanisms: keyword echo x6 MSQ, unique-span tells x3 hottext, canonical sequences x6 order, structural tells x5 singles)”
- `grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd` (116): “order content replacement with novel arbitrary-order narratives”
- `grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd` (123): “all audits were same-family (Claude only)”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (19): “construction-gated items: fragment-sequence, source-attribution, explicit-vs-inferred”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (21-23): “construction-first generation survived the anti-leak gate at 60% vs 6% for encyclopedic clones; one production campaign yielded 48.7% (738 certified of 1,516); raw generated banks leaked ~94% blind.”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md` (59-60): “78% of raw machine-generated items failed the passage-dependence gate alone”
- `ti-courseplans-audit/docs/course-formula-agents.md` (233): “G5 proved format is necessary but not sufficient (the anti-leak-*format* pool still leaked ~78%)”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (20): “pricing and design evidence, not current readiness”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (298): “99.5% / MSQ 100% leak as authored; hot-text / sequence / match force a return to the passage”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (299): “per-item redesign converted the leaky pools and certified **549/772** under the”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (282): “certification is **per-item**, not per-format”
- `grade3-reading/artifacts/generator_review/leak_control_and_certification_schema.md` (24-25): “`novelty: "unseen"` (already in the spec) guarantees the *passage* is new to the student. It does **not** guarantee the *item* is passage-dependent — an unseen passage can still host a leaky item.”
- `grade3-reading/ti-courseplans/courses/g5-reading/analysis/rt5-ebsr-2026-07-06/README.md` (3): “**Headline: EBSR moves from 0-certified to 2-certified. 2 / 13 certified.**”
- `grade3-reading/ti-courseplans/courses/g5-reading/analysis/rt5-ebsr-2026-07-06/README.md` (79-80): “This is a real property of the two-part select-the-evidence format under a strong cross-family solver, not a tooling gap.”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/markdown/PLAN-EVALUATION.md inside it) (178-179): “leak is format-dependent. MCQ ~99.5% / MSQ 100% blind-solvable; hot-text 1.67% / sequence 0% / match 0% / EBSR-cross-family 0%.”
- `incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (281): “The G5 live build established that **format sets the default leak**”
- `incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (282): “The G5 discipline — certification is **per-item**, not per-format”
- `incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (299-300): “per-item redesign converted the leaky pools and certified **549/772** under the cross-family mean-blind-solve < 0.60 gate”
- `incept-package-hub/course-packages/courses/g8-reading/review/evidence/case-for-review.md` (47-48): “5 gating formats (text_entry, sequence, mcq, ebsr, inline_choice) + a **43-item non-gating practice lane** (multi_select, hot_text, match) for”
- `incept-package-hub/course-packages/courses/g8-reading/review/evidence/case-for-review.md` (79-80): “the leaky formats in a 43-item non-gating practice lane”
- `incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-25/artifacts/Grade 7 Reading - START HERE.md` (42-44): “no G7 selection format cleared the 60% blind-solve bar for their interpret/compare demand (mcq flatlined at 50% across two attempts; hot_text 0%)”
- `grade3-reading/red_team/findings/REGISTER.md` (41): “After the in-flight 133→68 sequence decert, **6 certified sequence items still ≥0.60 blind**”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/QUESTION_CONVERSION_RETROSPECTIVE.qmd inside it) (286-287): “This showed that control-pass rate did not predict anti-leak certification. MCQ, MSQ, and hot-text could be answerable with the passage and still leak blind.”
- `grade3-reading/_archive/2026-08-13-consolidation/top-level-docs/HANDOFF_3_KEY_ISSUES.md` (50): “- **Skeleton V2 decision (G5):** MCQ/MSQ eliminated from the build after 99.5–100% leak; match pool culled to 653; this SUPERSEDED the MCQ-regen effort — don't restart regen.”
- `grade3-reading/artifacts/g5-course-candidate-v0/assessments/assessment_rejection_report.qmd` (11): “Exact key recovered: 148 / 152 (0.974).”
- `grade3-reading/artifacts/g5-clean-course-v2/GATE_REPORT.md` (19-20): “Of the **95** v1 "clean" items re-gated, only **20 (21%)** survived — **75 leaked** under the strong solver. The weak gpt-4o-mini gate had over-credited them.”
- `grade3-reading/course-renderer/docs/video/u1-script-critique.md` (213-215): “It passes every structural tell in `validate-blind-solve.mjs`, which I confirmed by running it, but `R-Q-3` is about the item and not only about the tells.”
- `grade3-reading/ti-courseplans/courses/g5-reading/llm/GENERATOR_DIRECTIVE.md` (34): “| MCQ | 99.5% |”
- `grade3-reading/ti-courseplans/courses/g5-reading/assessments/DESIGN.md` (88): “span selection cannot be scored without the passage present; leakage cannot be measured via cross-family blind-solve.”

Against: The project's plan notes hold that selected response is not inherently leaky, but raw selected-response items often are, and that hot-text and sequence formats need extra suspicion because renderer, protocol and guessability issues can masquerade as content quality (`grade3-reading/knowledge_bot/knowledge/kb-0090-fable5-plan-traces-2026-07-09.qmd`, lines 132 and 134). The fix list's audits were all same-family, so its closed leaks have no cross-family solve behind them (`grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd`). The Grade 5 figures are historical, kept as pricing and design evidence, not current readiness (`ti-courseplans-audit/docs/practice-layer-spec.md`, line 20). A later run found counter-evidence (`grade3-reading/ti-courseplans/courses/g5-reading/assessments/DESIGN.md`).

<sub>method · stage: measure · format, integrity, measurement · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### One question, reworded for each stage

Differentiate by rewording one question over the same lines, knowledge and evidence, plainer for struggling readers and closer to the test for stronger ones, never by easier questions. One worked example gives four versions of a question on the same lines, from plain wording through the state test's phrasing to a composition.

A Grade 3 lesson design adds a second axis to its writing stages: the wording of the question changes while the core knowledge underneath stays identical, with the same lines, threshold and evidence and a different demand in the asking (`g9/library/text/L8d5159.txt`, line 43). Its worked example runs from a simplified floor with a plain verb, a plain noun and the line range spelled out, through the state test's phrasing, to a composition on the same lines and knowledge, and notes that the knowledge being tested does not move at all (lines 44-59). That gives a route down: a struggling child gets the simplified wording of the same question rather than an easier question, which keeps the class on one piece of knowledge (line 60).

Quoted:

- `g9/library/text/L8d5159.txt` (43): “Same lines, same threshold, same evidence, different demand in the asking.”
- `g9/library/text/L8d5159.txt` (60): “A child who is struggling can be given the simplified wording of the same question rather than an easier question, which keeps the class on one piece of knowledge.”
- `g9/library/text/L8d5159.txt` (58): “Same lines, same knowledge, a composition instead of an answer.”
- `g9/library/text/L8d5159.txt` (59): “The knowledge being tested does not move at all.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (43): “Stage changes what the child writes. It can also change how the question is worded, while the core knowledge underneath stays identical.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (43): “Same lines, same threshold, same evidence, different demand in the asking.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (59): “the line range goes from "5-8" to "5 through 8", which is how the released tests write it, and the verb goes from "where does" to "which words help the reader understand".”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (59): “The knowledge being tested does not move at all.”

Against: A Grade 9 planning meeting floated a different route for first-timers, a glossary and "possibly an optional No Fear Shakespeare-style side-by-side modern translation "for like a stage one learner … somebody who's really struggling"." (`g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/MEETING-2026-10-01.md`, lines 41-43). Another record keeps a level's difficulty out of hard syntax and reworded easier lessons, while part of this design's change between stages is a change of wording (`g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx`, line 59).

<sub>method · stage: write · wording, demand, accessibility · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Own words first, then the choices

To have a learner commit before seeing options, ask for an answer in their own words first, keep it on screen, then have them check it against the choices. One check asks 'In your own words: what is dramatic irony?', shows the answer back, then asks the student to check it against 3 choices.

A Grade 9 film's checks were rebuilt so that a definition check first asks for the answer in the student's own words, keeps it and shows it back as 'Your words', and then asks the student to check that idea against three choices. The own-words answer is kept but never judged or replied to, and gibberish or too-short text is refused. There are no learner data on whether committing first helps.

Quoted:

- `g9/player/content/archivist-checks.json` (30): “"type": "own_words_then_confirm",”
- `g9/player/content/archivist-checks.json` (31): “In your own words: what is dramatic irony?”
- `g9/player/content/archivist-checks.json` (32): “Now check your idea. Which of these defines dramatic irony?”
- `g9/player/README.md` (33): “Own-words answers are kept and shown back”
- `g9/player/qa/QA.md` (16): “a real sentence saved and shown back as "YOUR WORDS"”

Against: The committed answer is never checked against anything: "Own-words answers are stored, never judged by a keyword match and never replied to; gibberish and too-short text are refused with a plain prompt (feedback 1.4, 8.2)." (g9/player/content/archivist-checks.json, line 41).

<sub>method · stage: write · format, options, practice · universal · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Predictive inferences are much harder

For items on an informational text, count one needing a predictive inference as far harder than one needing a bridging or pronoun-reference inference, which readers make reliably.

The RAND Reading Study Group's 2002 report, in a reading course's digest of it, finds that among the inferences relevant to expository text, anaphoric and bridging inferences are made most reliably, whereas predictive inferences are very difficult to make (p. 108; `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd`, line 437). The digest draws the item-design point that inference items should be tiered, with predictive ones expected to be substantially harder. The finding is about the inferences readers make while reading; using it to set item difficulty is the digest's step.

Quoted:

- `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd` (437): “anaphoric and bridging inferences are made most reliably, whereas predictive inferences are very difficult to make.”
- `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd` (439): “Gives item-difficulty calibration guidance: inference-type comprehension items should be tiered, with predictive-inference items expected to be substantially harder than anaphoric/bridging items.”

Published: [RAND Reading Study Group 2002, Reading for Understanding (MR-1465)](https://www.rand.org/pubs/monograph_reports/MR1465.html)

Against: The report's finding is about the inferences readers make while reading informational text; using it to set item difficulty is the digest's own step.

<sub>method · stage: write · demand · universal · from research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Rank each topic's leak risk first

Before planning lessons or items, rank topics and stories by how much readers and models already know, key nothing to that knowledge, and test the best-known without the text. A probe found 6 of 6 sampled two-part evidence items answerable without the passage, explorer items among them answered from prior knowledge.

A grade-4 red-team review pulled 6 random two-part evidence items, hid the passage and answered all 6, some from prior knowledge of the real-world facts the course teaches, although the course's rubric gate had passed all six. The course's topic plan then ranked each unit's prior-knowledge risk, highest for its best-known exploration and colonial topics, and set a design consequence for each level: items anchored to the passage's own particulars, and a mandatory cross-family text-hidden check before any item ships. Its topic rubric puts a ceiling on how much a topic's allusion density counts for the same reason: knowledge that saturates children's media and model training makes items answerable without the passage. In a grade-5 assessment, 28 of 36 evaluable items leaked, traced to passages built on widely known domain facts.

Quoted:

- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/topic-selection.md` (239-242): “The G4 red team proved the trap empirically: **6/6 sampled EBSR items were blind-solvable, including Magellan/explorer items answerable from prior knowledge.** Knowledge-rich topics make this *worse*, the better we teach world knowledge, the more items become answerable without the passage unless disjointness is designed in.”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/topic-selection.md` (246): “Items anchor to passage-specific particulars (this voyage's dates/decisions/quotes), never to canon facts; cross-family blind-solve gate mandatory before any item ships”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/load-bearing-rubric.md` (43-45): “Extremely high allusion density means the knowledge saturates children's media and LLM pretraining — so assessment items over it become answerable *without the passage* (the measured Magellan failure).”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/RED_TEAM_FINDINGS.md` (31): “I pulled **6 random EBSR items** live, stripped the passage, and attempted them blind. **6/6 were solvable without the passage:**”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/RED_TEAM_FINDINGS.md` (34): “the knowledge-expedition design makes items about real-world facts (pitch physics, Magellan, explorer funding) answerable by any knowledgeable solver with no passage.”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/RED_TEAM_FINDINGS.md` (37): “The rubric gate (item ≥0.85 + lesson-level >20% rule) **passed all six of these items** — so the rubric is demonstrably not a substitute for the empirical run.”
- `grade3-reading/ti-courseplans/courses/g5-reading/assessments/DESIGN.md` (89): “Sequence / match / EBSR (36 evaluable items): **8 cold (22%), 28 leaked (78%)**”
- `grade3-reading/ti-courseplans/courses/g5-reading/assessments/DESIGN.md` (90): “Passages rely on widely-known domain facts; a language model can answer items from prior knowledge alone.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (446-450): “First, it is blind-solvable. "Odysseus is clever" is the single most widely known fact about Odysseus, it is the answer Storyworks prints in its own key, and a child who has never read our passage will produce it. A SPINE lesson whose target concept can be stated correctly without reading fails R-Q-3 at the level of the lesson rather than the item.”
- `grade3-reading/course-renderer/content/lesson-plans/g4-u1-l2.json` (471): “Against: it is blind-solvable, since Odysseus is clever is the single most widely known fact about him and a child who has never read our passage will produce it, which fails R-Q-3 at the level of the lesson rather than the item”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (506-507): “It cannot catch a question whose answer a child already holds.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (514-515): “The film is rated R, so most nine year olds will not have seen it, but trailers, posters and playground talk are not rated.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (500-504): “What this makes unusable. Any item whose answer is a plot fact about either episode: - What did Circe do to the men. Answer available verbatim from a television episode broadcast this year.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (516-518): “So the design rule follows from the risk: no item's correct answer may be a plot fact. Every answer must be a motive, a clue selection, or a category judgement, and every option must be quotable from our passage”

Against: Prior knowledge was not the only cause in that probe: evidence options restating the first part's answer, and distractor tells, also let items leak (`grade3-reading/ti-courseplans/courses/g4-reading/approval-package/RED_TEAM_FINDINGS.md`, lines 33-35). No measurement shows leaks rising steadily with how well known a topic is. The research note calls its case against the best-known takeaway an argument, not a finding (`grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md`, line 442); the lesson plan accepts it on its merits.

<sub>method · stage: ground · integrity, stimulus · universal · from g3 · measured · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Try a frame on each kind of text

A question frame designed on one kind of text must be tried on each other kind before it is used there.

A closing-question frame whose slots ask "when", written and worked through on a story, was used in an informational lesson, and its model answers came out as a part doing its job when it does its job, because that text has no event to point at. A review of a story lesson found the same slot worked there because the text was a story.

Quoted:

- `shadow-content-eval/reports/G3-U2-L1-review.md` (72): “That says "a part does its job when it does its job".”
- `shadow-content-eval/reports/G3-U2-L1-review.md` (74): “- The spec's "when, not what" rule is written for narrative, where "when" gets the mechanism. Here there is no event to point at.”
- `shadow-content-eval/reports/G3-U1-L2-main-review.md` (49): “"When" works here because the text is a story.”
- `g9/transformer/v04/README.md` (17): “**Exit criteria:** every component is ready on both samples, or held with a reason; the gallery renders them all.”
- `g9/transformer/v04/README.md` (15): “A gallery shows every component baked on the same text.”
- `g9/transformer/README.md` (130): “| `samples/` | public-domain texts: Othello 1.1 (lines 1–75) and Ozymandias |”
- `learning-truths/research/2026-10-12-6-transformer-ideas/README.md` (9): “a universality test: all 16 blocks made for a poem and for prose on 12 October 2026”
- `learning-truths/research/2026-10-12-6-transformer-ideas/universality-test.py` (16): “b = post("/api/block", {"text": texts[k], "question": out["questions"][k], "mechanic": m, "n": 1})”
- `learning-truths/research/2026-10-12-6-transformer-ideas/universality-test.py` (21): “out["blocks"] = list(ex.map(make, [(k, m) for k in texts for m in mechs]))”
- `g9/transformer/src/mechanics/evidence-hunt.js` (28): “- hint: one sentence that points to who speaks or what moment to look at, without quoting the line.”
- `g9-transformer-runs/blocks/963297774d627c12.json` (12): “Look at the description of the face's mouth and expression in the first sentence.”
- `g9/transformer/samples/ozymandias.md` (4): “Stand in the desert. Near them, on the sand,”
- `g9/transformer/README.md` (120): “No lesson has been reviewed by a person or used by a student.”
- `g9/transformer/README.md` (99): “`test/fixtures/othello-items.json` and a play in `src/quality/personas.js`.”
- `g9/transformer/src/films.js` (11): “{ id: "othello-opening", title: "Othello: the opening (unit film)", file: "Othello-opening-full.mp4", vtt: "Othello-opening-full.vtt", poster: "thumbnail-othello-love.jpg" },”
- `learning-truths/research/2026-10-12-6-transformer-ideas/universality-test.json` (17, 24, 59, 115, 122, 129, 171, 199, 227): “"status": "failed",”
- `g9-transformer-runs/decisions/0419fc2dc6f6bacf.json` (187, 794, 1401): “"value": 0.02,”
- `g9-transformer-runs/blocks/d2d7d0787d6754d9.json` (97): “"The film belongs with this text: the judge found this does not hold"”
- `g9/transformer/v01/QA.md` (32): “6/6 ready, 6 writer calls, 8 judge calls”
- `grade3-reading/artifacts/qc-2026-09-30-staging/LIVE-WALK.md` (47): “No word in "What is Captain Hook like?" says where to look.”

Against: The spec and the checker treat the pattern as text-neutral: "Nothing in the pattern is fiction-specific." (`shadow-content-eval/references/closing_questions_pattern.md`, lines 8-9). The finding rests on one informational lesson, and the review left the fix open: "Nonfiction probably needs its own frame variant" (`shadow-content-eval/reports/G3-U2-L1-review.md`, line 83).

<sub>method · stage: review · format, stimulus, demand · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Write against the canonical piece

Make one component canonical and write the rest against it: list what later components may not re-ask, and let none of them contradict it. One lesson design lists the two questions its film asks and the two words the film defines as off-limits for re-asking.

The lesson-components spec makes the background film canonical: no later component may contradict it or re-ask its questions. Each lesson design then lists what is off-limits for re-asking, such as the film's sync checks, its stamped definitions and naming the story pattern in the abstract, and a rebuilt lesson keeps the same discipline: glossed words and sync-checked answers are never re-asked. It is the across-components form of telling a writer what an earlier block covers.

Quoted:

- `downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx` (7 (textutil text)): “The video is canonical: no later component may contradict it or re-ask its questions.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx` (28 (textutil text)): “Off-limits for re-asking: the two sync checks above; the sultan and magician stamped definitions; naming or ordering the story pattern in the abstract.”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (32): “Glossed words and sync-checked answers are never re-asked”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/HUMAN-g3r-2026-07-27T08-38-36-019fa24b-fb42-7e61-a954-216db3ef77a4.md` (1095): “The video is canonical: no later component may contradict it or re-ask its questions.”
- `grade3-reading/course-renderer/docs/pedagogy/example-lesson-components-2026-08-06.md` (21): “The video is canonical: no later component may contradict it or re-ask its questions.”
- `othello-course-renderer-draft/repo/docs/pedagogy/example-lesson-components-2026-08-06.md` (21): “The video is canonical: no later component may contradict it or re-ask its questions.”

Against: none found

<sub>method · stage: ground · alignment, integrity, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Write each item's answerability model

Give every question a written answerability model showing how its key or each rubric point is earned from the delivered sources and declared knowledge, so another person can recompute it.

An AP history course's question record carries an answerability model beside its prompt, sources, key or rubric and scoring model, and each full long-essay and document-based item in its contract has a scoring and answerability model. Its rule is that answerability is checked before aggregate scoring: an independent reader should be able to recompute a multiple-choice key, or say how each constructed-response point can be earned from the delivered sources and declared course knowledge. A high average cannot make up for a wrong key, an impossible rubric point, a fabricated source or leaked feedback.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (618-619): “Every intrinsic question record includes the prompt, source set, key or rubric, scoring model, answerability model, provenance, and evaluation state.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (623-626): “Answerability is checked before aggregate scoring. An independent reviewer should be able to recompute the MCQ key or determine how each constructed-response point can be earned from the delivered sources and declared course knowledge. A high average score cannot compensate for a wrong key, an impossible rubric point, a fabricated source, or leaked feedback.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/DELIVERABLE-CONTRACT.md inside it) (112): “One broad prompt, current six-point rubric, scoring and answerability model, and official conditions.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/DELIVERABLE-CONTRACT.md inside it) (114): “One prompt, seven verified documents, current seven-point rubric, scoring and answerability model, and the official 1754-1980 range.”

Against: none found

<sub>method · stage: write · key, scoring-guide, integrity · universal · from ap · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Fix a cue in a wrong option

If an authored item breaks a form rule, such as a longest-option key, minimally rephrase a wrong option, log the edit, and leave the stem and key alone. When a rewrite left a 41-character key the shortest option, the fix shortened a wrong option below it instead of lengthening the key.

A reading engine's generator has one licensed form edit: where an authored wrong option breaks a form rule, for example by leaving the key the single longest or shortest option, it may minimally rephrase that option and record the edit, and its fidelity gate makes sure the stem and the key are never touched. A critique of a film script's checkpoint item made the same call by hand: a rewrite had cut the key from 49 to 41 characters while three long wrong options stayed, turning a passing item into a failing one, and the fix shortened one wrong option instead, since the key's wording, taken from the script's definition line, was the point of the rewrite. It keeps options alike in length (no-cue-in-the-item-itself) without editing signed content.

Quoted:

- `grade3-reading/course-renderer/authoring/README.md` (89-93): “One licensed form edit exists: where an AUTHORED distractor breaks a form rule (e.g. it leaves the correct answer the single longest or shortest option), the generator may minimally rephrase THAT distractor, recording it in `_gates.form_edits`. The stem and the correct option are never touched — the fidelity gate enforces exactly that split.”
- `grade3-reading/course-renderer/docs/video/u1-script-critique.md` (65-67): “The rewrite shortened the key from the shipped 49-character "A long story about a hero's journey and its trials" to 41 characters while leaving three long distractors in place, and turned a passing item into a failing one.”
- `grade3-reading/course-renderer/docs/video/u1-script-critique.md` (72-73): “**Fix.** Do not lengthen the key: its wording is line 8 and that is the point of the rewrite. Shorten one distractor below 41 characters instead.”

Against: A hand-built lesson in the same engine fixed the same gates on the key's side, logging ten divergences from its signed design that it says touch no correct option's meaning, the first because "the doc's wording made the key the single shortest option" (`grade3-reading/course-renderer/content/lesson-plans/g3-u2-l1.json`, line 728), so a word was added to the key.

<sub>method · stage: improve · distractors, options, integrity · universal · from g3 · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Needing the text can weaken distractors

A passage that rules out the obvious answers makes an item need reading but leaves wrong options easy to drop once read, so weigh that cost against the item's purpose. A quality screen flagged weak distractors on 14 of 26 items built so that a solver without the passage could not answer them.

A Grade 3 course's quality report made items resist a passage-blind solver by having the passage rule out the obvious world-knowledge causes; a cross-family quality screen then flagged weak distractors on 14 of 26 items, though every flagged key was correct, and the report judged the trade acceptable for checking that a student read an unseen passage but a limitation for telling abilities apart. When a mis-assembled form was rebuilt to match its passage on a familiar topic, all five items were rated at high risk of being answered from background knowledge and only one part of one item truly needed the passage. The report calls this the coherence-leak tension and accepted it because the form is formative practice, not a check that the passage was read. The other side of the trade is that on a familiar topic an item that matches its passage can often be answered without reading it, so choose for each item which cost its purpose can bear.

Quoted:

- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (96): “The quality screen flagged this on **14 of 26** items”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (98-99): “For a "did the student read this unseen passage?" transfer check that trade is acceptable; for MAP-style *ability discrimination* it is a noted limitation.”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (313): “items become **blind-solvable from background knowledge** — all 5 carry `blind_solvable_risk=HIGH`”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (314): “This is the coherence↔leak tension”

Against: none found

<sub>context · integrity, distractors, stimulus · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### The AP U.S. History exam's shape

From May 2027 the Advanced Placement United States History exam has source-based multiple-choice sets, sourced short answers, a document-based essay question and a broad long essay. Multiple choice gives 55 questions in 55 minutes for 40 percent of the score.

An AP history course's design documents summarise the official Course and Exam Description effective Fall 2026, and the figures match pages 497 to 500 of that description and its clarification notice, both read in this run. Multiple choice has 55 questions in 55 minutes for 40 percent, typically in sets of three to four on shared stimuli, each with four options and one defensible key; three required short answers take 40 minutes for 20 percent, the first on secondary text sources, the second on a primary text source and the third on a primary or secondary non-text source, each on a different period and in three one-point parts. The document-based question takes 60 minutes, including a 15-minute reading period, for 25 percent, uses seven documents on developments between 1754 and 1980, and must give students a genuine opportunity to use at least four documents, add outside evidence and explain the situation, audience, purpose or point of view of at least two. The long essay takes 40 minutes for 15 percent and gives one broad prompt over roughly half the course, within which the student chooses the developments; the course scores the document-based question on the current seven-point rubric and the long essay on the current six-point one, and it rejects the source-free short answers its legacy generator allowed.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (272-274): “Multiple choice contains 55 questions in 55 minutes and contributes 40 percent. Questions generally sit in source-based sets of three or four.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (539): “Four options, one defensible key; standalone use is not a section simulation”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (29): “55 stimulus-based multiple-choice questions in sets, 40 percent of the exam;”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (274): “Three required short-answer questions take 40 minutes and contribute 20 percent.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (274-277): “Under the new contract, every SAQ is sourced: question 1 uses one or more secondary text sources, question 2 uses a primary text source, and question 3 uses a primary or secondary non-text source. The three questions focus on different historical periods.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (567): “A complete SAQ has three independently achievable one-point parts.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/SEQUENCING-BRIEF.md inside it) (17): “records the all-sourced SAQ sequence and required broad LEQ design for May 2027.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (279-280): “The document-based question contributes 25 percent and allows 60 minutes, including the recommended reading period. It uses seven documents and covers 1754-1980.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (33): “one seven-document DBQ covering developments from 1754 to 1980;”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (597): “The full DBQ uses seven verified documents and the current seven-point rubric:”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (607-609): “Students need a genuine opportunity to use at least four documents in an argument, add relevant outside evidence, and explain how the situation, audience, purpose, or point of view of at least two documents matters to their argument.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (280-282): “The long essay contributes 15 percent and allows 40 minutes. It uses one broad prompt, with the student choosing the relevant development or developments within the prompt's scope.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (578): “The full LEQ uses a broad prompt and the current six-point rubric:”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT1-VERTICAL-SLICE.md inside it) (46): “an official LEQ prompt spans a broad period covering roughly half the course.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (284-285): “The legacy local generator allowed source-free SAQs, so the course rejects that behavior.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (285-286): “Unit 1's three sourced SAQs demonstrate the three source modalities, but the unit cannot demonstrate the official cross-period distribution by itself.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (611-612): “Unit 1 teaches document functions with three sources but labels the task as a Period 1 mini-DBQ rehearsal.”

Published: [College Board, AP U.S. History Course and Exam Description, effective Fall 2026, pp. 497-500](https://apcentral.collegeboard.org/media/pdf/ap-us-history-course-and-exam-description-effective-fall-2026.pdf) · [College Board, AP United States History Course and Exam Description Clarifications and Corrections, implemented for Fall 2026](https://apcentral.collegeboard.org/media/pdf/ap-us-history-course-and-exam-description-clarifications.pdf)

Against: A single unit can only rehearse these forms: one unit's three sourced short answers cannot show the official spread across periods (BRAINLIFT.md lines 285-286), and its three-source task is labelled a mini-DBQ rehearsal (lines 611-612).

<sub>context · format, stimulus, scoring-guide · domain · from ap · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Word knowledge can't need the text

A skill that is word knowledge, such as word parts, synonyms or connotation, can't be tested by a question that needs the text, so decide separately how to assess it. With the passage hidden, a model answered 36 of 45 generated vocabulary items, every word-part, synonym and connotation item among them.

A text-hidden check answered 36 of 45 generated vocabulary items, and every word-part, synonym and connotation item, because the skill is word knowledge rather than inference from the passage. The course plan concluded that those slots needed a fundamentally different design, or a decision that they cannot be tested as text-dependent items and should leave the comprehension blueprint. A later bank of 120 vocabulary seed items leaked 99.2% and was marked to be rewritten and re-certified, never used as it stood.

Quoted:

- `grade3-reading/artifacts/LANE1_COURSE.md` (242): “Skill IS word-part knowledge, not passage inference — cannot be made passage-dependent.”
- `grade3-reading/artifacts/LANE1_COURSE.md` (246): “cannot be tested as passage-dependent items and should be excluded from the comprehension-course blueprint”
- `grade3-reading/artifacts/g5_build_2026_07_02/g5_analysis_digest.md` (41): “the 120 L.5 vocab seeds LEAK 99.2% and must be re-authored + re-certified, never deployed as-is”
- `grade3-reading/ti-courseplans/courses/g5-reading/llm/LLM_SPEC.qmd` (205-206): “L.5 vocabulary items fail blind-solve at high rates (~99%) when the target word carries its common meaning and the student can guess from background knowledge alone.”
- `grade3-reading/ti-courseplans/courses/g5-reading/llm/LLM_SPEC.qmd` (222-223): “**The correct answer must require a passage-specific context clue that overrides or narrows the word's common meaning.**”
- `grade3-reading/_archive/2026-08-13-consolidation/top-level-docs/HANDOFF_3_KEY_ISSUES.md` (25): “L.5 vocab 80% blind-solve leak (36/44 slots need redesign; some substandards may be inherently world-knowledge)”

Against: Context-clue items partly worked: 8 of 15 survived, those using words in technical or domain senses (`grade3-reading/artifacts/LANE1_COURSE.md`, line 240).

<sub>context · format, integrity, alignment · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Comparison items resist needing their texts

Items comparing two texts are hard to make need the texts, since a comparison answer can often be guessed from the genres or a plausible particular. In one course, multiple-choice comparison items keyed to how the two texts diverge leaked at blind-solve rates of 0.67 to 1.00.

A Grade 7 reading course tried three constructions for its standard on comparing two texts, across a pair of accounts dense with particulars and a pair of poems making opposite claims. Multiple-choice items on how the texts diverge leaked at blind-solve rates of 0.67–1.00 because the genre schema is known in advance, claim-to-quote matching broke even with the passages, and a particular-anchored item that had certified another standard at 0.00 still leaked at 0.67. With no item under its dual-solver bar of blind-solve below 0.60, the course concluded that a comparison answer is either a schema-guessable interpretation or a semi-guessable plausible particular, and kept the standard taught and practised but ungated; that explanation is the course's own, drawn from the constructions it tried.

Quoted:

- `incept-package-hub/course-packages/courses/g7-reading/review/evidence/validation/standards-coverage-gate.json` (18): “after three exhausted constructions no leak-resistant true two-text comparison item certified under the dual-solver blind<0.60 bar.”
- `incept-package-hub/course-packages/courses/g7-reading/review/evidence/validation/standards-coverage-gate.json` (69): “No gated item certified after THREE exhausted constructions across a particular-dense account pair AND the opposite-claim poem pair”
- `incept-package-hub/course-packages/courses/g7-reading/review/evidence/validation/standards-coverage-gate.json` (69): “divergence-shape mcq leaked 0.67-1.00 (genre schema is known a priori)”
- `incept-package-hub/course-packages/courses/g7-reading/review/evidence/validation/standards-coverage-gate.json` (69): “claim<->quote match broke with-passage; the particular-anchored mcq that certified RI.7.4 at 0.00 improved the dense pair to 0.67 but still leaked.”
- `incept-package-hub/course-packages/courses/g7-reading/review/evidence/validation/standards-coverage-gate.json` (69): “a two-text COMPARISON answer is intrinsically either a schema-guessable interpretation or a semi-guessable plausible particular”
- `incept-package-hub/course-packages/courses/g7-reading/review/evidence/validation/standards-coverage-gate.json` (18): “Taught + practiced (8 practice items), never fake-gated.”
- `incept-package-hub/course-packages/courses/g8-reading/review/evidence/validation/coverage-matrix.json` (46-52): “"RI.8.9": { "text_entry": 13, "sequence": 11, "mcq": 2, "inline_choice": 3, "ebsr": 2 }”
- `incept-package-hub/course-packages/courses/g8-reading/review/evidence/course-graph-guide.md` (28): “[A9] Compare two arguments - evaluate competing arguments on one issue.”

Against: A Grade 8 course gated its two-text standard, which its course graph ties to comparing two arguments on one issue, with certified items in five formats: text entry 13, sequence 11, multiple choice 2, inline choice 3 and two-part 2 (`incept-package-hub/course-packages/courses/g8-reading/review/evidence/validation/coverage-matrix.json`, lines 46-52; `incept-package-hub/course-packages/courses/g8-reading/review/evidence/course-graph-guide.md`, line 28). It is a different demand from the Grade 7 standard, but it shows the limit may lie in the constructions tried rather than in comparison itself.

<sub>context · integrity, format, demand · universal · from g3 · measured · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>
