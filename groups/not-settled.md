# Not settled yet

97 learnings. Each says where it came from and what argues against it. [What a perfect question is](../PERFECT-QUESTION.md) collects the criteria by facet, and [How to generate perfect questions](../GENERATING.md) collects the methods by stage.

### What a film's own checks should test

Should a check inside a film made from a text test the text itself, or may it test what the film argued?

The video essay builds an argument from the text, ending in two readings a careful reader could defend, and is told that each of its checks is answered by the narration so far. In the 12 October run the speech's essay asked, after its argument frame, how the two readings interpret the speaker's contrast, and its keyed option restates the film's own framing of two readings, which is the film's argument rather than the speech's words. The rule that a question about a text must need the text does not settle whether a film's argument counts as material a check may test.

Quoted:

- `g9-transformer-runs/blocks/34c293906aa945a2.json` (75): “"stem": "How do the two readings interpret the speaker's contrast?",”
- `g9-transformer-runs/blocks/34c293906aa945a2.json` (78): “One reading stresses the weakness of speech while the other stresses the power of action”
- `g9/transformer/src/mechanics/video-essay.js` (46): “two readings of the lesson question that these lines alone support.”
- `g9/transformer/src/mechanics/video-essay.js` (55): “Each question is answered by the narration so far.”

Against: none found

<sub>criterion · alignment, media, stimulus · universal · from g9 · open-question · open · found in [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Asking about a contrast the text states

How can an open question ask about a contrast the text states outright without giving the answer away, when naming both sides nearly states it? All three judged drafts of one such question named both sides of the contrast and were judged give-aways, at 0.69, 0.71 and 0.65.

In the 12 October run the open check on a speech built around a contrast it states outright was drafted three times. Every draft named both sides of the contrast and a word for lasting, endurance or durability, and the give-away check said yes each time (0.69, 0.71, 0.65), so the block failed and no wording that passes was produced.

Quoted:

- `g9-transformer-runs/decisions/b5f74899349e1331.json` (21): “"q": "What difference does the speaker draw between the endurance of the ceremony and the impact of the fighting?",”
- `g9-transformer-runs/decisions/b5f74899349e1331.json` (111): “"value": 0.69,”
- `g9-transformer-runs/decisions/b5f74899349e1331.json` (161): “"q": "How does the speaker contrast the durability of what the soldiers did with the durability of the speech?",”
- `g9-transformer-runs/decisions/b5f74899349e1331.json` (280): “"value": 0.71,”
- `g9-transformer-runs/decisions/b5f74899349e1331.json` (347): “"q": "What difference does the speaker draw between the endurance of spoken words and the actions of the soldiers?",”
- `g9-transformer-runs/decisions/b5f74899349e1331.json` (437): “"value": 0.65,”
- `g9-transformer-runs/blocks/b5f74899349e1331.json` (39): “"The question does not give its answer away: the judge found this does not hold"”

Against: The give-away check has no person-labelled cases, so it is not settled that these questions do give the answer away.

<sub>method · stage: write · stem, integrity, demand · universal · from g9 · open-question · open · found in [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### A cartoon guide and teen credibility

Whether a cartoon or illustrated guide costs a lesson credibility with young teenagers is untested, though a guide's identity changed how much middle schoolers learned in one study. In one study, middle-school girls learned more from a female guide, with a transfer effect of d = 1.03.

A research brief for a Grade 9 design looked for a study of whether a cartoon guide hurts credibility with 14- to 15-year-olds and found none. Its nearest evidence was indirect: teens abandon designs that feel childish, and in a virtual-reality lesson gender-matched guides changed middle schoolers' learning, girls doing better with a female guide (transfer d = 1.03) and boys with a drone. The brief and the design strategy both keep it as a question to pilot, comparing an illustrated guide with a minimal icon and with no guide at all. The design meanwhile settled on a human guide drawn in a 2D cel style, with female and male options and a range of looks.

Quoted:

- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (74): “I found **no study that directly tests whether a cartoon agent hurts credibility for 14–15-year-olds.**”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (74): “NN/g found teens abandon designs that feel childish (see 4.1).”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (74): “Gender-matched agents changed middle schoolers' learning in VR: girls did better with a female agent (transfer d = 1.03), boys with a drone”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (76): “Run an A/B test: illustrated fox vs. a minimal icon vs. no avatar.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/strategy/grade-9-strategy.md` (76): “No study tests whether a cartoon guide costs credibility with 14 year olds. That stays a pilot question, not a finding.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/README.md` (40): “The guide is a human character, not a monogram or a mascot, in a 2D cel style, with female and male options and a range of looks.”

Published: [A gender matching effect in learning with pedagogical agents (JCAL, 2018)](https://doi.org/10.1111/jcal.12335)

Against: none found

<sub>context · media · universal · from g9, research · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A checkpoint or a harder written answer

Whether an independent turn may drop a step's tap-to-choose checkpoint for a harder written answer, losing the step's label and practice rejecting options that don't fit, is unsettled. The design's bank offered 9 words to lock in or bounce back, where the free-typed version accepted any of 4 typed words.

A simulated review of a reading lesson found an independent-practice step with no gate and no printed label, its knowledge move carried instead by two assessed blanks in the next step's written frame (`grade3-reading/artifacts/arc-audit/REGISTER-2026-09-15.md`, lines 37-43). The prepared answer defends free writing because the independent turn should ask more of the child than the guided turn, which already offers the tapping version of the same move (line 43). An earlier audit judged a free-typed version of the step higher in demand, recall rather than recognition, but found it drops the design's practice in rejecting words that don't fit (`grade3-reading/artifacts/arc-audit/PEDAGOGY-L5-2026-09-05.md`, lines 247-256). The register held three paths for a ruling, and a later register still listed the step among gaps awaiting rulings, with nothing executed (`grade3-reading/artifacts/arc-audit/REGISTER-2026-09-24.md`, lines 25-26).

Quoted:

- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-15.md` (43): “We chose free writing over tapping at this point because the independent turn should ask more of the child than the guided turn did, and the guided turn on the previous screen already offers the tapping version of the same move.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-15.md` (40): “do we add a gated Step-3 msq and accept that p17 flips into a staged Routine while p16 stays a plain stack, add it unlabelled to keep both pages in the same mode, or rule that folding add-what-you-know into Step 4's assessed know-a/know-b blanks is the intended fade?”
- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L5-2026-09-05.md` (250-253): “The JSON's free-type version is arguably higher cognitive demand (recall vs. recognition) but is a different interaction shape than the doc specifies, and it drops the "don't fit" distractor-rejection teaching moment the doc's bank interaction provides”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-24.md` (26): “FIND rail/Refine/State on L6–L7 and INFER Step-3 bank on L4/L5 (adherence gaps 1, 2, 4, 5, 6, 7, 18)”
- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L5-2026-09-05.md` (247-248): “a free-type trait-word hunt against an accept-list of 4 words”
- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L5-2026-09-05.md` (249-250): “dangerous · kind · angry · gentle · hateful · friendly · evil · calm · threatening”

Against: The register leaned toward restoring the step: "path A recommended: gated Step 3 question, p17 becomes a stepped rail like L2/L4" (`grade3-reading/artifacts/arc-audit/REGISTER-2026-09-15.md`, line 187). The earlier audit's free-typed hunt sits in notes that only a retired player draws (the same register, line 40), though its point about the lost rejection holds for the written fold as well.

<sub>context · practice, demand, format · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A critic voice under pressure

Whether a critic voice in a panel of AI agents softens its disagreement when a student pushes back is untested.

Research for the Grade 9 lesson ideas listed sycophancy among the risks of AI voices in a lesson: a 2026 position preprint frames it as an educational safety risk for language models that teach, and a 2025 simulated-tutoring study measured models conforming to a student's stated wrong view (`grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd`). Nothing it found tests whether a critic voice in a multi-agent panel softens its disagreement under social pressure from the student, and it flags that as an open risk (the same file).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd` (328-329): “Untested anywhere found: whether a "critic" voice in a multi-agent panel softens its disagreement under social pressure from the student — flag as an open risk.”
- `grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd` (327): “a 2025 simulated-tutoring study measured models conforming to a student's stated (wrong) view”

Published: [Check My Work? Measuring Sycophancy in a Simulated Educational Context (2025)](https://arxiv.org/abs/2506.10297) · [Sycophancy is an Educational Safety Risk (2026)](https://arxiv.org/abs/2605.14604)

Against: none found

<sub>context · integrity, feedback · universal · from g9, research · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### A distinct voice for a film's checks

Whether a film's in-video checks should be asked in a voice distinct from the one that narrates it, or in that same voice, is disputed.

A direction logged on 6 October asked that students be tested throughout the film by a pop-up guide with a voice different from the narration's (`g9/library/text/L346c3d.txt`, line 22). A later version, following the brief, had the guide read the film and ask the checks in one voice (`g9/library/text/L30b6dc.txt`, line 11). The project's write-up on film, checks and production marked the distinct checking voice as disputed (`g9/library/TIMELINE.md`, line 84).

Quoted:

- `g9/library/TIMELINE.md` (84): “Commit d3b8bed: **BrainLifts** FILM / CHECKS / PRODUCTION (stills over AI video and distinct checking voice marked disputed)”
- `g9/library/text/L30b6dc.txt` (11): “the Archivist reads the film and asks the checks in one voice; takes the book at the opening, wears a badge on the A-to-B line, opens the book at the end”
- `g9/library/text/L346c3d.txt` (22): “but make sure the students are tested throughout by the archivist popup, who has a different voice from a narrator”

Against: none found

<sub>context · media · universal · from g9 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A gap-fill on the independent step

Whether the independent step should give everyone a gap-fill frame, or offer it only after a first miss so it stays no easier than guided practice, is untested.

Curriculum feedback on a Grade 3 reading lesson asked for a gap-fill frame at the last step of the independent turn. The course team pushed back that this would make the independent turn less demanding than the guided turn, whose last step is already a gap-fill, inverting the release gradient, and proposed the gap-fill as a fallback after a first miss so the scaffold is available rather than imposed. A later course record shows the gap-fill built as modelled after an instruction to make every requested change, so the outcome was a ruling, not evidence of what helps learners.

Quoted:

- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-4/feedback-on-iteration-4/feedback-0806-pedagogy.md` (289): “A gap-fill at step 4 makes the you-do less demanding than the we-do's step 4, which is already a gap-fill — that inverts the release gradient (D1.15) and breaks same-skill-faded (D1.4). Our recommendation is the fallback-after-a-miss version in draft (h)4.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-4/feedback-on-iteration-4/feedback-0806-pedagogy.md` (49): “make the gap-fill the *fallback after a first miss*, so the scaffold is available rather than imposed.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/resources/extracts/distill_player.md` (66): “Step 4 gap fill as has been modelled (#31).”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/resources/extracts/distill_player.md` (66): “Make all the changes they have requested - no exceptions”

Against: none found

<sub>context · practice, hints, sequence · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A misconception code the list lacks

Whether a wrong option grounded in the text may carry a misconception code the governing list does not name, or must be remapped to the nearest listed one, is unsettled. One audit found a lesson's governing standard pinning exactly four misconception codes while a wrong option grounded in the passage carried a fifth.

An audit of a Grade 5 reading lesson found a wrong option coded to a misconception id outside the four ids its governing bar pins, although the option, a confusion about population size, was correctly grounded in the passage. The audit left the choice to be confirmed against the governing curriculum: allow a fifth id, or remap the option to the nearest pinned one. The shipped content file still carries the invented code.

Quoted:

- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (511-514): “G5-BAR §7 pins exactly four `feedback_map` ids; this one isn't among them even though the content it's attached to (line 420, population-size confusion) is correctly grounded in the passage. Suggested fix: confirm with canon whether a fifth id is permitted, or remap to the nearest pinned id.”
- `grade3-reading/artifacts/u4l2-build/content/u4l2-content.json` (541): “"D": "mc-population-overreach"”

Against: Another learning takes each item's wrong options from the misconceptions recorded for its knowledge statement, which leans toward remapping.

<sub>context · distractors, feedback, alignment · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A shared definition or the passage's sense

When a word's one course-wide definition does not fit the sense a later passage uses, should the lesson keep the shared definition or gloss that passage's own sense? Restoring eight glossary definitions failed the one-definition check on two, and the course definition reused for one was narrower than the original gloss.

A Grade 3 reading course's rules ask both for one definition of a taught word used exactly in every later mention, the passage glossary included, and for every hard passage word to get a definition in the sense used there. Restoring a design's eight glossary definitions failed the grade-wide consistency check on two words, and the course kept six verbatim and replaced two with its existing definitions, noting that equality alone does not prove a contextual sense is appropriate. For one word the shared definition is narrower than the original gloss and describes a plan the passage does not establish; the course recorded the swap as an editorial reuse, not a correction of the original gloss and not an academic ruling.

Quoted:

- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (880): “Choose one definition for a taught word and use exactly it in every later mention, including the reading goal, the passage glossary and any feedback.”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (888): “any hard word sitting in the passage gets a tap that gives a student-friendly definition in the sense used here, and can be heard.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/glossary/VOCABULARY-CONSISTENCY-PROPOSAL.md` (7): “ends with exactly two R-VOC-5 failures”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/glossary/VOCABULARY-CONSISTENCY-PROPOSAL.md` (9): “Equality alone does not prove a contextual sense is appropriate.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/glossary/VOCABULARY-CONSISTENCY-PROPOSAL.md` (14): “This is narrower than the original PP3 gloss.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/glossary/VOCABULARY-CONSISTENCY-PROPOSAL.md` (16): “That depicts anticipation in their fight; it does not establish a particular plan or prove that nobody notices it.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/glossary/VOCABULARY-CONSISTENCY-PROPOSAL.md` (16): “it does not silently promote a validator into academic authority”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/INTEGRATION-DISPOSITIONS.md` (6): “The admitted final approach restores six definitions verbatim and standardizes anchored/cunning to the existing Grade3 definitions.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/INTEGRATION-DISPOSITIONS.md` (6): “the narrower course gloss is an explicit editorial reuse”

Against: none found

<sub>context · wording, alignment · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A voice for each character in a play

Whether giving each character in a play read aloud its own voice helps learners track who is speaking is untested.

A review of a Grade 9 prototype warns that the argument that distinct voices reduce the load of tracking who is speaking in a play is reasoning, not a cited finding, that there is no evidence specifically on multi-voice drama read aloud, and that it should not be presented as evidence-based. The same review notes that actor-read audio brings different voices with the casting, so nothing would need building for it.

Quoted:

- `g9/sources/Othello_1_Feedback_DevFactory.md` (405): “The argument that distinct voices reduce the load of tracking who is speaking in a play is reasoning, not a cited finding. There is no evidence specifically on multi-voice drama read-aloud.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (405): “It should not be presented as evidence-based.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (239): “If the audio is actor-read, that is not a feature to build — it comes with the casting.”
- `g9/library/text/L36b8ba.txt` (405): “The argument that distinct voices reduce the load of tracking who is speaking in a play is reasoning, not a cited finding. There is no evidence specifically on multi-voice drama read-aloud.”
- `g9/library/text/L36b8ba.txt` (403): “That literature is about prose, where speaker attribution is not a problem, so the general null does not straightforwardly transfer to multi-voice drama.”
- `g9/library/text/L36b8ba.txt` (403): “The reading-while-listening literature gives a small overall benefit (g ≈ 0.18) which is largely a pacing artifact”

Against: none found

<sub>context · media, stimulus · universal · from g9, research · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Absolute words in wrong options

Open: whether to flag absolute words such as always, never and all in any wrong option, or only when every wrong option carries one and the key does not.

The reading audit flags absolute words only when every distractor carries one and the key does not, because only then is the key findable by shape. An AP question benchmark instead rejects a question outright, before any model is asked, if its distractors use absolute language. Neither file records a measurement behind its choice.

Quoted:

- `shadow-content-eval/SKILL.md` (78): “every distractor carries an absolute (always/never/all/none/only…) and the key does not, so the key is findable by shape”
- `icloud-work/incept/README.md` (95): “- **Absolute language** in distractors: "total", "complete", "immediate", "all", "never"”
- `grade3-reading/course-renderer/content/lesson-plans/g3-u2-l1.json` (975): “(3) p8's distractors were wrong on their quantifiers (two opened 'Only'), so elimination found the inclusive key; they are now wrong on the facts.”

Against: none found

<sub>context · distractors, integrity, evaluation · universal · from g3, ap · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Adaptations or full originals

Should a course teach a classic work through short adaptations, through the full original with companion sessions, or through a reviewed mix of the two?

A source audit of a Grade 3 reading course found its lesson designs explicitly teaching short supplied adaptations, while a newly supplied sourcing portal asks for complete originals and prohibits replacing the original with a retelling (`grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE3.md`, lines 13 and 89). Replacing the readings alone would invalidate many exact-evidence questions, vocabulary bindings, models and narration, so the audit asks for a named academic decision between adaptations, full originals with companion sessions, or a reviewed combination, and makes none of the changes itself (same file, line 89). A card from the same sourcing portal makes a named retelling the intended core reading for another grade, so a blanket conclusion that a retelling can only be scaffolding was withdrawn (`grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE4.md`, line 74).

Quoted:

- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE3.md` (13): “This conflicts with the existing lesson designs, which explicitly teach short supplied adaptations.”
- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE3.md` (89): “Replacing readings alone would invalidate many current exact-evidence questions, vocabulary bindings, models and narration.”
- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE3.md` (89): “A named academic decision must establish whether the course uses adaptations, full originals with companion sessions, or a reviewed combination.”
- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE4.md` (74): “This card establishes a named retelling as an intended **core**, so any blanket conclusion that a retelling can only be scaffolding is withdrawn.”

Against: none found

<sub>context · stimulus, sequence · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Blatant calibration cases, subtle live faults

Does a calibration set built from blatant faults show that a judge will catch the subtle faults that actually occur? Seven of one AP judge's 15 failing calibration cases expect a cognitive-demand failure, six of them for asking only for recall.

An AP judge's calibration set holds 25 cases, 23 of them multiple choice, and its 15 failing cases are mostly blatant: seven expect a cognitive-demand failure, two absolute language, one a structural fault, two gross period misplacements and three factual errors, one of them subtle (1832 for 1830) (`APinceptbench/ap_benchmark/calibration/gold_standard.json`). In a live run, factual accuracy became the commonest failing dimension, with 24 failures whose patterns were events placed in the wrong period, geographic slips and oversimplifications (`APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md`). Whether catching the first kind predicts catching the second has not been measured.

Quoted:

- `APinceptbench/ap_benchmark/calibration/gold_standard.json` (194): “Recall-only question - just asks for a date without any analysis”
- `APinceptbench/ap_benchmark/calibration/gold_standard.json` (403): “Factual error: Midway was in the Pacific against Japan, not the Atlantic against Germany”
- `APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md` (87): “1. **Temporal confusion** - Misattributing events to wrong time periods”
- `grade3-reading/bias_experiment/.agent/memory/G3_CANDIDATE5_ADDENDUM_ROUND_2026-07-16.md` (36): “| Positive | 9/10 | 9/10 |”
- `grade3-reading/bias_experiment/.agent/memory/G3_CANDIDATE5_ADDENDUM_ROUND_2026-07-16.md` (37): “| Boundary | 3/10 | 2/10 |”

Against: none found

<sub>context · evaluation, measurement · universal · from ap · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Breadth or depth for transfer

Does transfer to unpredictable test content come from covering many knowledge areas broadly or fewer ideas in depth?

The reading-comprehension BrainLift bets on breadth because state-test topics are unpredictable: many knowledge networks, Tier-2 vocabulary and taught comprehension monitoring (`grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md`). The curriculum-architecture BrainLift, summarising a 2011 review of international comparisons, says high-performing jurisdictions teach fewer topics per grade in greater depth (`grade3-reading/ti-courseplans/feedback/feedback2/WF - Curriculum Architecture Br - 260713-123107.md`).

Quoted:

- `grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md` (90-92): “so the only rational hedge is breadth: many knowledge networks + Tier-2 vocabulary + taught comprehension monitoring.”
- `grade3-reading/ti-courseplans/feedback/feedback2/WF - Curriculum Architecture Br - 260713-123107.md` (427): “High-performing jurisdictions teach fewer topics per grade with greater depth. "Fewer things in greater depth" is the core design principle.”
- `grade3-reading/ti-courseplans/feedback/feedback2/WF - Curriculum Architecture Br - 260713-123107.md` (432): “Policy-facing and advocacy-oriented rather than neutral analysis.”
- `grade3-reading/ti-courseplans/feedback/feedback2/WF - Curriculum Architecture Br - 260713-123107.md` (434): “Limited empirical evidence directly linking design to achievement gains.”

Published: [Oates 2011](https://doi.org/10.1080/09585176.2011.578908)

Against: The depth side rests on a review that the same BrainLift calls policy-facing and advocacy-oriented rather than neutral, with limited empirical evidence linking design to achievement gains (`grade3-reading/ti-courseplans/feedback/feedback2/WF - Curriculum Architecture Br - 260713-123107.md`).

<sub>context · sequence, alignment · universal · from g3, research · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Captions and redundancy

Captions word for word with the narration: they make a film usable without sound, but in one study text identical to the narration impaired learning.

Captions are on by default in the film player (`g9/player/index.html`), and they match the script exactly
(`othello-unit-video/research/METHODS.md`).
In a published study, on-screen text identical to the narration impaired learning (Yue, Bjork & Bjork 2013,
https://doi.org/10.1037/a0031971), yet captions are what make a film usable without sound. To settle it: the same film
with captions on and off, compared on later recall, with access needs kept separate.

Quoted:

- `grade3-reading/knowledge_bot/HOTBUCKET.md` (18): “WPM self-read hold, captions, UI standardization”
- `grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd` (47): “Combine verbal and visual when both add value. Avoid redundancy.”
- `grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd` (129): “nothing may be spoken that is not printed, sentence for sentence”
- `grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd` (182): “captions are NEVER hand-written”
- `grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd` (183-184): “derives a WebVTT track from the authored `transcript[]`”
- `grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd` (184): “plus the clip's real measured duration via `ffprobe`”
- `grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd` (186): “`validate-contracts.mjs` fails a unit video with no caption track”
- `grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd` (187-188): “captions are the only way through for a child who cannot hear”
- `grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md` (59): “- Nothing is spoken that is not printed on the same page, sentence for sentence — a spoken line”
- `grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md` (61): “exists because two pages drifted 16 lines into paraphrase).”
- `grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md` (60): “readable on screen. Read-aloud is OFF by default at G5: the lesson must be 100% followable”
- `grade3-reading/artifacts/g5-course/G3-U1-L4-RESIDUAL-ADJUDICATION-2026-08-21.md` (90): “read-along rule runs one way; printed-but-unspoken is”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (39): “Read-to-me audio matches the printed words exactly, word-highlighted | Any mismatch breaks decoding support and the child’s trust in the voice”
- `grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md` (150): “Every video carries a VTT; captions toggle works”
- `grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd` (151-153): “a page may print words nobody reads aloud (question stems are deliberately silent per R-AUD-6), but it may **never speak words it does not print**”
- `grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd` (47): “| **Multimedia**   | Combine verbal and visual when both add value. Avoid redundancy.                  |”
- `ti-courseplans-audit/skills/video-red-team/references/rubric.md` (99-100): “suppressed when a text card shows the same words (r18).”
- `grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd` (65): “captions for Scout (headphones cannot be assumed)”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md` (286): “Strong evidence is L2/vocab; benefit for fluent learners in dense instructional video is not established.”
- `grade3-reading/ti-courseplans/skills/video-red-team/references/finding-taxonomy.md` (76): “| Caption duplicates text card | same words twice on screen | 09_captions suppression (r18) |”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (72-76): “### Anti-patterns (instructional failures per Mayer's multimedia learning principles) These patterns add extraneous cognitive load without aiding learning: - Decorative talking head (a face that adds no instructional content) - Stock footage that does not teach the KC - Karaoke subtitles (duplicating full narration text on screen)”
- `g9/transformer/src/video/produce.js` (108): “const captions = beats.flatMap((b) => captionsFor(b.narration, b.start + LEAD, b.audio_seconds));”
- `g9/sources/Othello Unit Video_ Info Sheet for Devfactory.md` (81): “on by default. Key words in bold as they are spoken.”
- `othello-archive/sources/act1/Othello Unit Video - Info Sheet for Devfactory.txt` (142): “Captions: on by default. Key words in bold as they are spoken.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-visuals-human-v0.1.md` (148-149): “A meta-analysis of 57 studies found that verbatim redundant text impairs learning while extracted key terms can help [17].”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (318): “Caption text must match actual spoken wording.”

Published: [Yue, Bjork & Bjork 2013](https://doi.org/10.1037/a0031971)

Against: A later run found counter-evidence (`grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd`). A later run found counter-evidence (`grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd`).

<sub>context · media, accessibility · universal · from g9, research · open-question · open · found in [2026-10-12-2-round-1](../research/2026-10-12-2-round-1/), [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Commit before the model is revealed

How can a lesson make students commit to their own answer before a modelled one is revealed, without timers, a locked Next button or yes-or-no gates?

A content review asked that a lesson's modelled thinking be protected by a commit-before-reveal step so it can't be clicked past, and named what that step must not use: timers, a disabled Next button or yes-or-no gates. The register routed it as a candidate mechanism for the shared engine without choosing one, and follow-up proposals ask for one chosen engagement mechanism in which the student's prediction or evidence comes before any intended reveal, adding that clicking a required button is not enough.

Quoted:

- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/REGISTER.md` (29): “Explicit anti-patterns named: no timers, no disabled Next, no yes/no gates.”
- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/VERIFICATION-PROPOSALS.md` (10): “prediction/evidence commitment precedes any intended reveal”
- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/VERIFICATION-PROPOSALS.md` (10): “clicking a required button is insufficient”
- `g9/transformer/src/mechanics/cer-frame.js` (101): “Saved. Here is one strong answer to compare with yours.”
- `g9/transformer/src/mechanics/cer-frame.js` (15): “The quote is checked against the text; then a model answer is shown.”
- `g9/transformer/src/mechanics/debate.js` (27): “Here is one position you could defend:”
- `g9/transformer/src/mechanics/debate.js` (130): “bare(text))) && tries(action) >= 2)”
- `g9/player/design/ARCHIVIST-DESIGN.md` (343): “the student-controlled "Hide the model, I'll try" reveal”
- `g9/player/content/archivist-checks.json` (31): “In your own words: what is dramatic irony?”
- `g9/player/content/archivist-checks.json` (32): “Now check your idea. Which of these defines dramatic irony?”
- `othello-course-renderer-draft/repo/docs/design/grade-9/prototype/README.md` (28): “4. **Pick a side**, after reading, with the marked lines in view.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/prototype/README.md` (29): “a worked example in three parts (my answer, my proof, why it proves it), arguing the side the student did not pick.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (418): “Attempting to retrieve before seeing the answer produces better retention than studying the answer alone. It is worth keeping as a prompt in the word web, but it is unverifiable, so it should not be counted as assessment.”

Against: none found

<sub>context · practice, integrity · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Comparison as a procedure of its own

Whether comparison should be taught as a procedure of its own, holding one named dimension and building each side in full before comparing, is still only a proposal.

Two documents in the reading course renderer propose a comparison procedure for grades 4 and 5, where comparing two texts starts to be asked for and no procedure existed: read the question, name one dimension and hold it, build each side's evidence on that dimension, finishing one side before starting the other, then state the likeness, the difference and what it means (`grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures-g4-g5.md`; `grade3-reading/course-renderer/docs/pedagogy/grade5-procedure-proposal.md`). The grade 5 version rejects a true but irrelevant detail or a comparison that changes dimension halfway, and the correction table says a learner who cannot find a difference has usually never built one of the two columns. Both are proposals awaiting sign-off, and a grade 5 lesson plan lists the procedure as documented but unsigned (`grade3-reading/course-renderer/content/lesson-plans/g5-u1-l7.json`, line 45). Nothing has measured it with learners.

Quoted:

- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures-g4-g5.md` (6-8): “summarizing a longer text and comparing two texts start to be asked for at Grade 4 and neither had a procedure to run.”
- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures-g4-g5.md` (175-176): “| 2 | Name the dimension | "On WHAT am I comparing them? One dimension at a time." | | 3 | Build each side | "What does the text say about each one, on that dimension? I build one column at a time, and I finish one side completely before I start the other." |”
- `grade3-reading/course-renderer/docs/pedagogy/grade5-procedure-proposal.md` (24): “Build each side: select evidence for both sides on that dimension. Reject a true but irrelevant detail or a comparison that changes dimensions halfway through.”
- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures-g4-g5.md` (240): “| Cannot find a difference | Return to Step 3: "Tell me about A. Now tell me about B." (Usually one column was never built.) |”
- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures-g4-g5.md` (11-12): “Treat the seven Grade 3 procedures as settled and these two as open to being rewritten or rejected.”
- `grade3-reading/course-renderer/docs/pedagogy/grade5-procedure-proposal.md` (5): “The two additions below require explicit sign-off before merge.”
- `grade3-reading/course-renderer/content/lesson-plans/g5-u1-l7.json` (45): “CANDIDATE: COMPARE, documented but unsigned and not in renderer union”

Against: none found

<sub>context · demand, practice · domain · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Credit for knowledge taught earlier

How a knowledge-building course should give credit for what earlier lessons taught is not settled, when a text-dependence gate removes every question that prior knowledge can answer. A gate-report template lists domain-knowledge items at about zero, by design.

A review faulted a course that by design kept assessment passages from ever overlapping taught topics, so taught knowledge could never help (`grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md`). A certification template accepts domain-knowledge items at about zero, since recall items are passage-independent and the anti-leak filter removes them (`grade3-reading/artifacts/g5-merged-course/VERDICT_TEMPLATE.md`). The review asked for taught knowledge to recur in the learning texts with cold passages kept for the test, and the approved plan fades topic coherence gradually as the last scaffold (`grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md`), which settles only part of it.

Quoted:

- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (43): “by design ensures assessment passages never overlap taught topics”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (45): “Sequence the learning texts so taught knowledge recurs and compounds, and reserve cold, non-overlapping passages for the test only, where that property belongs.”
- `grade3-reading/artifacts/g5-merged-course/VERDICT_TEMPLATE.md` (70): “2. **KCT1 Domain-knowledge ≈ 0 — by design.** Domain-recall items are passage-independent → removed”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (296): “is the last scaffold, and like every other scaffold it fades gradually”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/topic-selection.md` (239-242): “The G4 red team proved the trap empirically: **6/6 sampled EBSR items were blind-solvable, including Magellan/explorer items answerable from prior knowledge.** Knowledge-rich topics make this *worse*, the better we teach world knowledge, the more items become answerable without the passage unless disjointness is designed in.”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/markdown/BRAINLIFT.md inside it) (81): “the better we teach world knowledge, the more items become blind-solvable unless designed against.”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/markdown/PLAN-EVALUATION.md inside it) (167-168): “Knowledge-rich topics make this worse.”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/markdown/PLAN-EVALUATION.md inside it) (172): “**HIGHEST** (measured on explorer items)”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/markdown/UNIT-SPECS.md inside it) (421): “HIGH blind-solve risk (castles/knights saturate children's media).”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/markdown/UNIT-SPECS.md inside it) (422-423): “Items anchor to this text's particulars; canon facts banned as answer keys; cross-family blind-solve gate mandatory.”
- `grade3-reading/artifacts/g5-clean-course-v1/GATE_REPORT.md` (61-62): “**KCT1 Domain-knowledge = 0 — by design, not omission.** Domain-knowledge *recall* items are inherently passage-independent, so the anti-leak filter removes them.”

Against: none found

<sub>context · evidence-of-learning, integrity, sequence · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Difficulty across a shared text

Should questions that share one text sit at one difficulty level, or span easy to hard like a quiz?

The evaluator first routed sets of questions on one shared text through its quiz rules, which need all three difficulty levels present and no level above 60%, and the generator specification still requires that spread. A later dedicated evaluator expects uniform difficulty and fails a set only for wildly inconsistent levels. Both positions coexist in this snapshot: the committed half of the classifier sends such sets to the dedicated evaluator, while its stashed half still routes them to the quiz rules.

Quoted:

- `icloud-work/incept/inceptbench/docs/MCQ_SET_PASS_SPEC.md` (157): “- All three difficulty levels present (Easy, Medium, Hard)”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/mcq_set/evaluation.txt` (3): “Unlike quizzes which require Easy/Medium/Hard distribution, MCQ sets are expected to have UNIFORM difficulty - all questions should be at the same appropriate difficulty level.”
- `icloud-work/incept/inceptbench/src/inceptbench/classifier/content_classifier.py` (38): “# MCQ set → dedicated evaluator (uniform difficulty expected, unlike quizzes)”
- `icloud-work/incept/inceptbench/src/inceptbench/classifier/content_classifier.py` (45): “# MCQ set → classified as quiz (decomposed into individual MCQs)”

Against: The generator specification's pipeline still routes such sets through the quiz rules: "Classifier fast-path → ContentType.QUIZ" (`icloud-work/incept/inceptbench/docs/MCQ_SET_PASS_SPEC.md`, line 13).

<sub>context · demand, stimulus, sequence · universal · from ap · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Does a newer model obey as well?

Whether a newer model follows the same frozen teaching rules at least as well as the model it replaces, with no change to the rules, is untested.

An experiment on steering generation with teaching rules planned a paired comparison of older and newer models with zero rule edits, but no eligible upgrade comparison ran. Its failure register names the assumption that a stronger model is a more obedient one, detected when quality benchmark gains stand in for conformance replay, and answers it by testing paired older and newer checkpoints and scoring the worst model. Behaviour across models in an adjacent probe varied sharply, but that was not an old-versus-new study.

Quoted:

- `grade3-reading/bias_experiment/experiment-record/docs/02-assumption-register.md` (28): “Planned paired old/new A comparison with zero policy edits.”
- `grade3-reading/bias_experiment/experiment-record/docs/02-assumption-register.md` (28): “No eligible model-upgrade comparison ran.”
- `grade3-reading/bias_experiment/experiment-record/docs/02-assumption-register.md` (28): “Cross-route A1b behavior varied sharply but was not an old/new study.”
- `grade3-reading/bias_experiment/experiment-record/evidence/primary-records/reading-81d-externalized-policy-compiler-plan.md` (286): “### F6 - stronger model is assumed to mean more obedient model”
- `grade3-reading/bias_experiment/experiment-record/evidence/primary-records/reading-81d-externalized-policy-compiler-plan.md` (288): “Detection: quality benchmark gains substitute for conformance replay.”
- `grade3-reading/bias_experiment/experiment-record/evidence/primary-records/reading-81d-externalized-policy-compiler-plan.md` (289): “Recovery cascade: 1. Test paired older/newer checkpoints. 2. Use worst-model scoring.”

Against: none found

<sub>context · generation, evaluation · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Does a strict schema cost quality

Open question: does forcing a strict output schema on a writer buy structural compliance at the cost of quality in its free-text parts? A strict schema made 5 of 5 document-based items structurally valid against 0 of 5 in plain structured-object mode.

On 5 document-based items, schema-constrained output gave 5/5 structural compliance against 0/5 in plain structured-object mode, and the strict mode was deployed (`findings_sftv7_20260424.md`). A research note in the same project cites a study in which three of four models lost 25 to 63 points on a math-reasoning benchmark in JSON mode, and the project's index keeps strict modes off by default for free-form item types (`research_constrained_decoding_per_cell.md`, `MEMORY.md`).

Quoted:

- `home-agent-memory/findings_sftv7_20260424.md` (28): “Diagnostic: 5 DBQ items:”
- `home-agent-memory/findings_sftv7_20260424.md` (29): “- `json_schema`: **5/5 = 100% structural compliance**”
- `home-agent-memory/findings_sftv7_20260424.md` (30): “- `json_object`: **0/5 = 0% structural compliance**”
- `home-agent-memory/findings_sftv7_20260424.md` (33): “**Fix deployed:** `python/agents/fireworks.py` → `_build_response_format()` uses `json_schema` mode.”
- `ap-agent-memory/MEMORY.md` (63): “JSON mode loses 25-63pp on reasoning tasks; per-cell decision; default OFF for free-form cells.”
- `ap-agent-memory/research_constrained_decoding_per_cell.md` (19): “GSM8K reasoning, same model, same prompts, free-form vs JSON-mode constrained:”
- `ap-agent-memory/research_constrained_decoding_per_cell.md` (28): “Three of four mainstream models lose 25–63pp on a reasoning task in JSON mode.”
- `ap-agent-memory/research_constrained_decoding_per_cell.md` (30): “Same paper shows JSON mode *helps* on classification (Gemini-1.5-Flash 41.6% → 60.3% on DDXPlus). **Direction depends on task.**”
- `ap-agent-memory/research_constrained_decoding_per_cell.md` (62): “*Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models*, EMNLP 2024 Industry Track](https://aclanthology.org/2024.emnlp-industry.91/)”

Published: [Tam et al., Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models, EMNLP 2024 Industry Track](https://aclanthology.org/2024.emnlp-industry.91/)

Against: Five items only (`findings_sftv7_20260424.md`, line 28). The cited losses are on math reasoning, and the same study found JSON mode helped on a classification task, 41.6% to 60.3% for one model (`research_constrained_decoding_per_cell.md`, line 30).

<sub>context · generation · universal · from ap, research · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Does answer history bias a marker?

Does putting a learner's earlier off-topic or wrong answers into a model marker's input bias its verdict on a later correct answer?

A model marker rejected a correct answer, byte-identical to the lesson's own model answer, that a learner submitted after an off-topic one, and the marking route concatenated earlier answers into its input. The incident record called the wrong verdict potentially influenced by the hint or the accumulated off-topic history, and named history contamination plausible, not proven. The fix that followed enforced exact criterion identifiers and complete boolean validation so that malformed model output could no longer count against the learner, which left the history question untested.

Quoted:

- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (72): “A semantically wrong but well-formed `value:false` verdict, potentially influenced by the hint or accumulated off-topic history.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (72): “The route concatenates earlier answers; history contamination is plausible, not proven.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (72): “That text is byte-identical to `assessment.reveal`”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (84): “exact authored criterion IDs and complete/unique boolean validation prevent malformed model output from becoming learner-wrong”

Against: After the fix, the same answer was accepted on a second attempt in a fresh browser session, one observation rather than a test of the history question (`grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json`, line 84).

<sub>context · marking, evaluation · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Does grounding a writer in real sources help?

Does giving a question writer real source texts, so that it writes only the questions, raise item quality? Under one judge a grounded trial passed 5 of 6 items, but on the binding grader the result collapsed to about 28%.

An earlier AP question-generation effort reported grounding its writer in real source texts as a win on a six-item smoke test, 5/6 passing at 0.85 and a mean of 0.953 against 0.29, and recorded its confirmation on the real grader as blocked (`grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd`). A later insight entry found the 0.29→0.95 jump existed only under a discredited judge and collapsed to ~28% on the binding grader (`grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd`), and the reading project's item standard calls real-source provenance a separate, unproven lever (`grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md`). The reading project's generator assessment calls it the one mechanism that effort found that broke a wall, and its generator plans are built around it: feed real stimuli and let the model write only the questions (`grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md`; `grade3-reading/knowledge_bot/handoffs/g5-reading-generator-output-spec.md`).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd` (53-54): “**The recent "source-grounding breaks the wall" win is smoke only** (n=6, Unit-1: 5/6 pass@0.85, mean 0.953 vs 0.29)”
- `grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd` (55): “real-grader confirmation of an uncached served KC is BLOCKED.”
- `grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd` (24-25): “That **0.29→0.95** jump existed only under a **discredited Gemini judge**. On the **binding grader** it **collapsed to ~28%** (DBQ 0%, MCQ_SET 0%) and was logged as a **"Gemini-judge artifact."**”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md` (39-41): “(Real-source provenance is a *separate, UNPROVEN* lever: the aptraining "0.29→0.95 via real passages" result was **refuted** on the binding grader. Do not relabel machine-authored cold passages as "real.")”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md` (41-42): “Where a genuine source exists, the model writes the questions, not the passage.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md` (92): “Feed the model real/cold G5-band stimuli and let it write **only the questions**; don't have it invent the passage from nothing.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md` (92): “it's the one mechanism aptraining found that broke a wall (n=6 smoke, 5/6 pass@0.85).”
- `grade3-reading/knowledge_bot/handoffs/g5-reading-generator-output-spec.md` (74): “**Source-grounding was the biggest real lever** (feed real stimuli, model writes the questions) — exactly the cold-passage/anti-leak standard in §3. Build the generator around it.”

Against: The same standard still has the model write only the questions where a genuine source exists (`grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md`, lines 41-42), and the generator handoff calls source grounding the biggest real lever (`grade3-reading/knowledge_bot/handoffs/g5-reading-generator-output-spec.md`, line 74): the practice is kept while its measured gain is not.

<sub>context · generation, stimulus · universal · from ap, g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Extended writing under auto-scored gates

Whether a course whose gates stay auto-scored should handle the outcome test's extended written response as rubric-feedback practice, audited model scoring or an ungated strand is unsettled.

A grade-7 reading course's BrainLift leaves this open: an extended constructed response crosses the auto-scoring boundary its gates are locked on. If the state test that includes one becomes the reported anchor, it lists three options: practice only, with rubric feedback and the gates unchanged; model-scored responses with human-audited calibration; or a separate ungated strand reported alongside. It records that the fork is real and no option is selected, pending that test's blueprint and scoring rules.

Quoted:

- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (443): “Q5 — ECR handling if STAAR becomes the reported anchor. → STAYS Open.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (443-444): “Extended constructed response crosses the auto-scoring boundary the gates are locked on.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (445): “rubric feedback (gates unchanged); LLM-scored ECR with human-audited calibration; or a separate un-gated ECR strand”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (446): “*Confidence: fork is real; no option selected.*”

Against: none found

<sub>context · marking, scoring-guide, format · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Fade a routine or keep retrieving it

Whether a named thinking routine should fade once a stated condition is met, or keep returning as scheduled retrieval. A ruled fade, to a two-step option after five successful uses, was never built.

The reading project's comprehension doctrine holds this as an open dispute: named inference routines as fading scaffolds retired on a stated condition, its own stance, against scheduled recurring retrieval of the routine (`grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd`). A course ruling had a procedure collapse into a two-step option after five successful uses, but the course never got past one lesson per scaffold level, so the fade was never built (`grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd`).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (41): “named inference routines as *fading scaffolds* retired on a stated condition”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (41): “vs. scheduled recurring retrieval of the routine”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (41-42): “scaffolds fade across a unit (a procedure "collapses into a two-step option after five successful uses,"”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (42-43): “never got past one lesson per scaffold level, so this stayed unimplemented”
- `grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md` (68): “named inference routines as *fading scaffolds* retired on a stated condition”
- `grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md` (69-70): “vs. scheduled recurring retrieval of the routine (a plain reading of practice-architecture doctrine).”
- `grade3-reading/course-renderer/docs/rules/pedagogy-and-lesson-structure.md` (202): “the FIND procedure "collapses into a two-step option after five successful uses"”
- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (838): “Fixed language for modelling how to find the right part of the text, in (almost) every Modelling-Moment block (fiction and informational), all year; the modelling never fades.”

Against: none found

<sub>context · practice, hints, sequence · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Fade on a schedule or on results

Whether a scaffold should fade on a fixed schedule or on the learner's results is unsettled: a miss may mean missing knowledge, not a need for the steps. One static option collapses a procedure into a model the child can open or ignore after about five exposures.

On a course call, the question of when a child is ready for less support came with a warning: getting questions wrong doesn't mean a child still needs all the steps, since it could be a knowledge issue, not a steps issue. Two options were offered: static, where a procedure collapses into a model the child can open or ignore after about five exposures, and dynamic, where fading follows a signal from what the child does. The course repo fades nothing yet and calls static the honest first move, since it needs no inference about why a child missed an item, while its procedure specification proposes, still to be confirmed, releasing support in line with success in the app, such as moving from model to prompt at 80% success.

Quoted:

- `grade3-reading/course-renderer/docs/feedback/ela-weekly-call-2026-08-13.md` (530): “just because they're getting the questions wrong, it doesn't mean that they still need all those steps. It could be a knowledge issue, not a steps issue.”
- `grade3-reading/course-renderer/docs/pedagogy/grade-4-vs-grade-3.md` (62-63): “**Static.** After the child has seen the FIND procedure about five times, it collapses into an I-do they can open or ignore.”
- `grade3-reading/course-renderer/docs/pedagogy/grade-4-vs-grade-3.md` (64-65): “**Dynamic.** Track something the child does and fade on that signal, or collapse four steps into two.”
- `grade3-reading/course-renderer/docs/pedagogy/grade-4-vs-grade-3.md` (67-69): “Nothing in this repo fades anything yet. Static is the honest first move, because it needs no inference about why a child missed an item, and it is the one we can ship without a performance model.”
- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (826): “Across the year, the level of support the child receives gradually releases in line with their success within the app, e.g. 80% success and they move from model to prompt. TBC.”
- `grade3-reading/course-renderer/docs/extras/alpharead-fading-guidance.md` (26): “if the child got the previous same-procedure task wrong, the model is shown automatically next time”
- `othello-course-renderer-draft/repo/docs/pedagogy/grade-4-vs-grade-3.md` (58-60): “just because they're getting the questions wrong, it doesn't mean that they still need all those steps. It could be a knowledge issue, not a steps issue.”
- `othello-course-renderer-draft/repo/docs/pedagogy/grade-4-vs-grade-3.md` (62-63): “**Static.** After the child has seen the FIND procedure about five times, it collapses into an I-do they can open or ignore.”
- `othello-course-renderer-draft/repo/docs/pedagogy/grade-4-vs-grade-3.md` (64-65): “**Dynamic.** Track something the child does and fade on that signal, or collapse four steps into two.”
- `othello-course-renderer-draft/repo/docs/pedagogy/grade-4-vs-grade-3.md` (67-69): “Static is the honest first move, because it needs no inference about why a child missed an item, and it is the one we can ship without a performance model.”
- `othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md` (201-202): “fade "based on real-time student performance data", with a static fallback: the FIND procedure "collapses into a two-step option after five successful uses"”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md` (826): “Across the year, the level of support the child receives gradually releases in line with their success within the app, e.g. 80% success and they move from model to prompt. TBC.”

Against: A model curriculum's fading rules already mix the two, a fixed first-appearance rule with an automatic return of the model after a wrong answer: "if the child got the previous same-procedure task wrong, the model is shown automatically next time" (`grade3-reading/course-renderer/docs/extras/alpharead-fading-guidance.md`, line 26).

<sub>context · sequence, hints, practice · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Fine units or rich units

Whether spaced review should keep fine-grained knowledge units and group them, or merge them into fewer, richer units. One math curriculum's ~1,500 skills were collapsed into 427 knowledge units with 658 prerequisite links, and the complexity moved into each unit.

A knowledge-graph BrainLift in the reading project's knowledge store finds that a fine-grained graph works for first teaching and remediation but makes retrieval scheduling unwieldy, and that there is one proven response and one speculative alternative, with no clear winner (`grade3-reading/knowledge_bot/knowledge/kb-0116-graph-architecture-brainlift-core.qmd`). The proven response cuts the number of atoms, which moves the complexity into each one; the alternative keeps fine atoms and groups them into clusters for retrieval (the same file).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0116-graph-architecture-brainlift-core.qmd` (83): “There is one proven response and one speculative alternative, and it is not yet clear which is better.”
- `grade3-reading/knowledge_bot/knowledge/kb-0116-graph-architecture-brainlift-core.qmd` (85): “collapsing Math Academy's ~1,500 skills into 427 atoms with far cleaner prerequisite chains (658 edges vs thousands).”
- `grade3-reading/knowledge_bot/knowledge/kb-0116-graph-architecture-brainlift-core.qmd` (85): “This works, but the complexity does not disappear — it moves.”
- `grade3-reading/knowledge_bot/knowledge/kb-0116-graph-architecture-brainlift-core.qmd` (86): “An alternative is to keep the fine-grained atoms but aggregate them into clusters for retrieval purposes”

Against: none found

<sub>context · sequence, practice · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### First naming or recap

Open: whether a lesson's key idea should first appear at the step that names it, or may be stated earlier so that the naming step lands as a recap.

Two Grade 3 lesson reviews found the closing sentence already given earlier in the lesson, so the step that names it lands as a recap (`shadow/content-eval/reports/G3-U2-L1-review.md`, `shadow/content-eval/reports/G3-U1-L2-main-review.md`). One review judged that fine for learning and noted that the specification is silent on it. Nothing measured which order teaches better.

Quoted:

- `shadow-content-eval/reports/G3-U2-L1-review.md` (176): “That's fine for learning.”
- `shadow-content-eval/reports/G3-U2-L1-review.md` (177): “The spec is silent on this.”
- `shadow-content-eval/reports/G3-U1-L2-main-review.md` (134): “- **p23b is not first exposure.** p19b already tells the child the sentence (*"Keep that idea close"*), so Name it lands as a recap.”

Against: none found

<sub>context · sequence · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### From younger to older grades

Whether a teaching approach built for younger readers holds for older ones is untested, and one trial in an older grade is a probe, not proof.

A service meeting record describes the reading project's material as early-reading pedagogy, plausible for primary and early middle school but not known to cover advanced comprehension; a sixth-grade course was assigned partly to learn how far the approach reaches, a suggestion that higher grades need less scaffolding was declined because it had never been tried, and high-school reading was called a complete unknown (`grade3-reading/knowledge_bot/knowledge/kb-0130-incept-service-coe-catchup-2026-07-15.qmd`). The record's rule is never to describe the pedagogy or the trained model as grade-agnostic. To settle it: the same lesson design taught at an older grade and measured on a later test of new items.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0130-incept-service-coe-catchup-2026-07-15.qmd` (177): “Do not describe this pedagogy or the trained model as grade-agnostic. Grade 6 is a probe, not proof.”

Against: none found

<sub>context · demand, alignment · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Gating the branch for silent learners

Whether the follow-up for a learner who said nothing should gate progress at all is unsettled.

A Grade 3 reading lesson has a branch whose job is to catch a child who said nothing. Its handover lists whether that branch should gate progress at all among the rulings still to be given: a recognition check there may be right, but gating on it is the open question.

Quoted:

- `grade3-reading/_archive/handovers/HANDOVER-2026-09-23.md` (59-60): “- **Whether the silent branch should gate progress at all.** Its job is to catch a child who said nothing; a recognition check there may be right, but gating on it is the open question.”

Against: A rule on record gates every check, since one a student can skip is decoration (gate-every-check).

<sub>context · practice, integrity · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Harder instructions, weaker adherence

Writer models keep to constraints less reliably as instructions get harder, and whether giving a writer only the rules its task needs, not the whole rulebook, fixes that is untested. Across 18 models, average accuracy fell from 80.82% on the easiest constraint level to 36.76% on the hardest.

A published evaluation of 18 models from six families found average accuracy falling from 80.82% at the easiest constraint level to 36.76% at the hardest (Ye et al. 2026, https://aclanthology.org/2026.findings-acl.99/). A Grade 3 proposal for steering a writer with explicit rules cited it as the strongest counter-evidence it faced, and drew its own inference, labelled as one: compile a small active contract rather than prompt with the full rule base (`grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd`). The comparison the proposal planned never ran, because its experiment was stopped with those stages unrun (`grade3-reading/knowledge_bot/knowledge/kb-0168-eppc-bias-experiment-terminal-kill-and-salvage.qmd`). To settle it: the same tasks written from the whole rule base and from only the rules that apply, across model families, scored on the same held-out artifacts.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd` (73-74): “across 18 models, constraint adherence fell materially as instruction difficulty increased, and targeted training improved it.”
- `grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd` (74-76): “**Our architectural inference:** compile a small active contract rather than prompt with the full rule base”
- `grade3-reading/knowledge_bot/knowledge/kb-0168-eppc-bias-experiment-terminal-kill-and-salvage.qmd` (50): “Formal artifact-renderer A was not run.”
- `grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd` (103): “**Personal confidence, not a research result:**”
- `grade3-reading/bias_experiment/experiment-record/evidence/knowledgebot/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd` (73-74): “across 18 models, constraint adherence fell materially as instruction difficulty increased, and targeted training improved it.”
- `grade3-reading/bias_experiment/experiment-record/evidence/primary-records/reading-81d-externalized-policy-compiler-plan.md` (313): “Constraint interactions, ordering, and active-rule count create a measurable compliance ceiling.”

Published: [Ye et al. 2026, MulDimIF: A Multi-Dimensional Constraint Framework for Evaluating and Improving Instruction Following in Large Language Models, Findings of ACL 2026](https://aclanthology.org/2026.findings-acl.99/)

Against: The same study found that targeted training improved adherence, a remedy other than trimming the rules, and the proposal marks its own success estimate as personal confidence, not a research result (`grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd`).

<sub>context · generation · universal · from research, g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Hearing a play before reading it

Whether students should hear a play performed before reading it is unsettled, and an oral discussion of the play does not supply that hearing.

Machine-made notes of a design meeting said a play reads dry because it was written to be heard, not read silently, that the usual fix is hearing it aloud before reading it, and that the unit's oral discussion lesson already provides this. Review separated hearing a performance, using read-aloud and explaining an interpretation orally as different activities, and found the oral lesson does not by itself set up listening before reading. No listen-before-reading step was built, so nothing has tested it.

Quoted:

- `g9/transcript/chat-transcript.redacted.txt` (4985): “Shakespeare reads dry because it was written to be heard, not read silently. The usual fix is hearing it aloud before reading it”
- `g9/transcript/chat-transcript.redacted.txt` (5036): “Hearing a performance, using read-aloud, and explaining an interpretation orally are different activities.”
- `g9/transcript/chat-transcript.redacted.txt` (5036): “Lesson 3’s conversation with the Archivist doesn’t by itself establish a listen-before-reading sequence.”

Against: none found

<sub>context · sequence, media · universal · from g9 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Hints no student can reach

Whether to write and check hints a student can never reach before the answer is shown, when failures in those hints alone can hold the question. One block drafts three hints for each point but shows only the first before the answer, and two of its four held drafts failed only on the second and third.

Reading the held open-check records against the code: on a first sure miss the block gives the first hint of the first missing point, and on the next miss it shows the answer, while the 3D export passes only the first hint. Each point's second and third hints are still written, exported and checked. Of the four held open checks, the two held on the hint check named only second or third hints; the other two were held on the give-away question.

Quoted:

- `g9/transformer/test/runtime.test.mjs` (96): “a sure miss gets its hint, the second miss the answer”
- `g9/transformer/src/mechanics/open-check.js` (117): “return missed(`${vs.includes("holds") ? "Part of it is there. " : ""}${item.criteria[k].nudge}`);”
- `g9/transformer/test/animated.test.mjs` (124): “assert.equal(oc.rubric.max_tries, 2);”
- `g9/transformer/test/animated.test.mjs` (128): “assert.ok(c.nudge && c.second_nudge && c.third_nudge && c.accept.length === 3);”
- `g9/transformer/src/glue/threejs-render.js` (158): “criteria: it.criteria.map((c) => ({ requirement: c.requirement, accept: c.accept, nudge: c.nudge }))”
- `g9-transformer-runs/blocks/d872bc1dfbda65fb.json` (51): “"second_nudge": "Examine the end of line five to see what kind of sneer is sculpted.",”
- `g9-transformer-runs/blocks/d872bc1dfbda65fb.json` (68): “No hint hands the answer over: a hint uses a word that hands the answer over, or the answer itself”
- `g9-transformer-runs/blocks/7bb3a47934432969.json` (38): “No hint hands the answer over: a hint uses a word that hands the answer over, or the answer itself”
- `g9/transformer/src/glue/animated.js` (160): “second_nudge: say(c.second_nudge), third_nudge: say(c.third_nudge)”
- `g9/transformer/src/glue/animated.js` (23): “per try, the answer on the second miss”

Against: Another build is sent all three hints (g9/transformer/src/glue/animated.js line 160), and its open-check page is described as a nudge "per try, the answer on the second miss" (line 23); its hint-ladder code is not in this repo, so whether its students reach the later hints is not known.

<sub>context · hints, evaluation · universal · from g9 · open-question · open · found in [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### How a block builds on other kinds

How a lesson's separately made blocks can build on what blocks of other kinds taught, when each is made from the text, the question and its own kind alone.

The 9 October audit of the lesson engine asked for the key-word deck to be seeded from the word web's key words when a lesson has both (`g9-transformer-audit/2026-10-09-best-of-everything.json`). The build that followed found that a block is made from the text, the question and its own kind only, and cannot see the rest of the lesson. So with a word web present, the key-word block is listed as skipped in the animated export and drawn only on the engine's plain screen (`g9-transformer-audit/2026-10-09-builders.json`). Only a later block of the same kind is told what earlier ones cover, and a block's key hashes just the maker and kind versions, the text, the question, the kind and its number (`g9/transformer/src/blocks.js`, lines 23-25 and 67-74). The engine's known gaps still say that key words are not seeded from the word web's words (`g9/transformer/README.md`, line 114).

Quoted:

- `g9-transformer-audit/2026-10-09-builders.json` (1): “KW is not seeded from the strip's word web, as the audit asked. A block is made from text, question and mechanic only and cannot see the strip.”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “If the strip has a word-web block, seed the deck from its keys.”
- `g9/transformer/src/blocks.js` (67): “what the lesson's earlier blocks of this kind cover”
- `g9/transformer/src/blocks.js` (25): “return hash(MAKER, String(text).trim(), String(question).trim(), mechanic, n, ...(ver > 1 ? [ver] : []));”
- `g9/transformer/README.md` (114): “Key words are not seeded from the word web's words.”
- `g9/transformer/src/glue/threejs-render.js` (219): “key words: the word web's (cued by their meanings), and each key-words deck (each word into its gap)”
- `g9/transformer/src/glue/threejs-render.js` (224): “decks.push({ label: `Words for ${ww.item.centre}`, words: ww.item.keys.map((k) => k.word), gaps: [] });”

Against: A 3D version joins them after the fact: it puts the word web's key words into its own key-words step, as a deck labelled with the web's centre word (`g9/transformer/src/glue/threejs-render.js`, lines 219 and 224).

<sub>context · sequence, generation, alignment · universal · from g9 · open-question · open · found in [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### How far a learner may seek ahead

Whether a narrated lesson should let learners seek forward only through narration already heard, or anywhere short of the next unanswered check, is untested.

The narration handoff for one build of a narrated opening let the learner pause, seek within heard audio and replay, and real-browser QA measured it: a seek to 40 s with 29.68 s heard landed at 30.25 s, and the slider's maximum equalled the time heard. The handover's acceptance list asked that seek restrictions match the heard-audio design without making replay impossible. The film player tested the same day stops a seek only at an unanswered check instead: after the first check, a seek to 120 s was allowed and a seek to 190 s was clamped to 172 s, the second check. Nothing has compared the two designs with learners.

Quoted:

- `g9/prototypes/app-narrated/AUDIO-HANDOFF.md` (3): “The learner can pause, seek within heard audio, and replay.”
- `g9/prototypes/app-narrated-qa/QA.md` (14): “Seek limited to heard audio | PASS | tried 40 s with 29.68 s heard → landed 30.25 s; slider max = heard (30.18)”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (399): “Seek restrictions match the intended heard-audio behavior and do not make replay impossible.”
- `g9/player/README.md` (37): “Scrubbing cannot pass an unanswered check.”
- `g9/player/qa/QA.md` (14): “After check 1 done: seek to 120 s allowed; seek to 190 s clamped to 172 s (check 2)”
- `g9/player/qa/QA.md` (1): “Video lesson · browser QA · 2026-10-06”

Against: A testing limit, not a counter: "under `python3 -m http.server`, which does not honour Range requests, Chrome cannot seek inside the AAC clips: rewind and seek reset `currentTime` to 0." (g9/prototypes/app-narrated-qa/QA.md, line 7), so a seek test needs a server that supports range requests.

<sub>context · media, sequence · universal · from g9 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### How long a film before reading runs

How long a film before a reading should run is not settled: a rule, a worked example and a built lesson each give it a different length. One rule caps an intro film at 30 to 40 seconds, while a built lesson's film runs 1:54.

One version of the intro-video rules holds that an intro video is 30 to 40 seconds and a longer one is weaker, a number derived from the film's shape of five or six shots of one spoken line each (`downloads/BrainLift - What makes a good intro video.md`, line 87). The other compresses a script of about three minutes to about 60 seconds in its worked example (lines 361-363), and a built Grade 3 lesson opens with a 1:54 film (`downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md`, line 25). The short rule itself notes that educational video practice, measured on lectures, has engagement holding for several minutes (line 87, citing Guo, Kim and Rubin 2014).

Quoted:

- `downloads/BrainLift - What makes a good intro video.md` (87): “An intro video is 30 to 40 seconds, and a longer one is weaker, not richer.”
- `downloads/BrainLift - What makes a good intro video.md` (87): “This is not a SPOV because it does not stand beside the payload, it falls out of it, and because it is the least evidenced claim we hold.”
- `downloads/BrainLift - What makes a good intro video.md` (87): “Nearly all of educational video practice disagrees, where engagement holds for several minutes and length is treated as generosity, Guo, Kim and Rubin.”
- `downloads/BrainLift - What makes a good intro video.md` (363): “125 spoken words, \~60 seconds, narrator only, no stamp, no embedded checks.”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (25): “A 1:54 film of the riverbank world with captions available”
- `g9/transformer/src/mechanics/video-essay.js` (37): “TASK: a short video essay (60 to 100 seconds) that opens the lesson: three or four beats, each one frame with narration”
- `g9-transformer-runs/films/a2189e24065794e4/manifest.json` (5): “"duration": 26.2,”
- `g9-transformer-runs/films/f13d567b87dac256/manifest.json` (5): “"duration": 38.04,”
- `g9/library/curation/2026-10-07-marking-test-and-context-map.json` (64): “26 points covering all 434 words: 6 needed before reading (35.0 s), 11 that could move into reading-time notes (66.9 s), 9 framing (58.9 s); without the movable points the film would run about 1:48 (arithmetic, not a render).”
- `g9/library/text/Lbde498.txt` (28): “About 2:30–2:45, and no more than 3:00.”
- `g9/library/text/Lbde498.txt` (77): “the unit video plays at the very start of Lesson 1, before retrieval.”
- `grade3-reading/workspace/comms/from_plan/HUMAN-DECISIONS.md` (47): “### H3 — Peter Pan video ruling: BrainLift (30-40s) vs. producer brief (60-90s)”
- `grade3-reading/artifacts/signoff-packet/SIGNOFF-L4-2026-09-01.md` (266-267): “BrainLift's 30-40s world-only vs. the Peter Pan producer brief's 60-90s”
- `g9/script/v03/CHANGES.md` (3): “words, 2:30–2:45) cut to fit a 2:00 cap”
- `g9/sources/Othello Unit Video_ Info Sheet for Devfactory.md` (28): “About 2:30–2:45, and no more than 3:00.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md` (25): “Flagged the need to balance pre-reading context because 10-minute summary videos proved too dense.”
- `othello-archive/sources/act1/Othello Unit Video - Info Sheet for Devfactory.txt` (40-41): “About 2:30–2:45, and no more than 3:00. Brisk delivery, direct address ("you").”
- `g9/library/text/L64fb8b.txt` (25): “Flagged the need to balance pre-reading context because 10-minute summary videos proved too dense.”

Published: [Guo, Kim and Rubin 2014, How video production affects student engagement: an empirical study of MOOC videos, L@S 2014](https://doi.org/10.1145/2556325.2566239)

Against: The short rule's own source calls it the least evidenced claim it holds, derived from the film's shape and not measured on children (`downloads/BrainLift - What makes a good intro video.md`, line 87).

<sub>context · media · universal · from g3, research · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### How long a grade 3 passage runs

How long a grade 3 informational passage should run is unsettled: an authoring ladder sets early units well below the length a research band calls for. An early review measured the course's passages at 58 to 217 words, averaging about 166.

Documents in one reading course set different targets for the same kind of text. Its authoring ladder, written for the grade 3 build, puts a unit 1 informational passage at 380 to 420 words, and a grade 4 lesson plan says the ladder puts units 1 and 2 there. A grade 3 unit 2 lesson design, meanwhile, expanded its passage from 482 to 557 words to reach a research band of 520 to 560 words, citing five assessment and research sources. An early review had measured the course's passages at 58 to 217 words, averaging about 166.

Quoted:

- `grade3-reading/course-renderer/docs/pedagogy/grade-4-vs-grade-3.md` (17-19): “Our authoring ladder was written for the Grade 3 build and puts a Unit 1 informational passage at 380 to 420 words, which is the Grade 3 figure.”
- `grade3-reading/course-renderer/content/lesson-plans/g4-u1-l1.json` (141): “350 to 450 words, targeting 380 to 420. The authoring contract's length ladder puts U1 and U2 there and the informational sibling at the shorter end.”
- `grade3-reading/course-renderer/docs/extras/alpharead-lesson-design-plants-l1.md` (22): “The Wonderful World of Plants was expanded from 482 to 557 words to reach the research band (520 to 560 words, 45 to 55 sentences, 10 to 12 words per sentence; NWEA, Smarter Balanced, Shanahan, STAAR, CKLA).”
- `grade3-reading/course-renderer/docs/feedback/academics-review-2026-06-29.md` (72): “Course passages run 58 to 217 words, averaging about 166.”

Against: none found

<sub>context · stimulus, demand · domain · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### How many checks a reading carries

How many comprehension checks a reading should carry is unsettled: too many on a short text may stop learners forming a mental model of it. One course's design documents say exactly 2 comprehension checks per reading, while its shipped lessons ran 4.

A review of a Grade 3 reading unit asked whether it asked so many questions that children missed the point, warning that questions had been overdone on texts too short for the mental model to form. The shipped convention was four comprehension checks per reading against design documents that say exactly two, and the challenge collided with the course's response-rate ceilings and with its rule that every inference point is cashed by a question. It was routed for a ruling that had not come, and a later ruling to lean toward literal checks at first covers only those and does not resolve the overall count.

Quoted:

- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/03-INSTRUCTION-DESIGN.md` (197-198): “We've overdone questions to a detriment that we're not even allowing the mental model to occur. … too much with texts that are too short.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/03-INSTRUCTION-DESIGN.md` (199-200): “4 comprehension checks per reading is the shipped convention; the design docs say "exactly 2"”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/03-INSTRUCTION-DESIGN.md` (200-201): “It collides with the rate ceilings above and with R1's cash-every-inference rule”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/03-INSTRUCTION-DESIGN.md` (185): “and EACH is cashed by a question that requires it.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/03-INSTRUCTION-DESIGN.md` (216): “does not resolve, the still-pending overall question-density ruling above”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/03-INSTRUCTION-DESIGN.md` (214-215): “lean MORE toward sync checks initially, then dial back on reviewer request.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md` (198-200): “This is a challenge to the question DENSITY the current unit runs (4 comprehension checks per reading is the shipped convention; the design docs say "exactly 2").”
- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (125): “A question-heavy ratio must be reversed.”

Against: The interim ruling for literal checks leans toward more checks at first: "lean MORE toward sync checks initially, then dial back on reviewer request." (grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/03-INSTRUCTION-DESIGN.md, lines 214-215). The records few-questions-during-reading and hold-a-lessons-load-steady argue for few, budgeted questions.

<sub>context · sequence, practice · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### How many words a lesson teaches

How many words a lesson should teach in depth, one or a few, is not settled. A simulated review found three lessons teaching one new word each, below a two-to-three rule.

A decisions log records that the rule pack sets exactly one taught word per lesson (`grade3-reading/artifacts/DECISIONS-2026-08-24.md`). A simulated review found three lessons with one new word each, below the wiki's own rule of two to three academic (Tier-2) words per lesson, and called it an open, unresolved conflict, downgraded to a note on adversarial check (`grade3-reading/artifacts/arc-audit/SIM-REVIEW-D1-D4.md`).

Quoted:

- `grade3-reading/artifacts/DECISIONS-2026-08-24.md` (26): “- **Exactly one taught word per lesson.** The rule pack sets this.”
- `grade3-reading/artifacts/arc-audit/SIM-REVIEW-D1-D4.md` (221): “only 1 new word/lesson in L5/L6/L7 is below the wiki's own "2-3 Tier-2 words per lesson" rule, and is an open, unresolved conflict per the case study itself”
- `grade3-reading/artifacts/arc-audit/SIM-REVIEW-D1-D4.md` (221): “downgraded to NOTE on adversarial check”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (215): “Six words may also be too many for one pre-reading beat, and they are not of equal difficulty — façade and pretense are a long way harder than disloyal.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/vocabulary-selection-and-generative-items.md` (7): “over a shortlist of ~10–12 candidate words, then cut to 2–3 to teach deeply (the rest you just quickly tell)”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (548-549): “only decomposer keeps the full example/non-example/ morphology/say-back cycle (G5-BAR §4 pins exactly one blocking word)”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (520-521): “The three word-card slots carry **evidence** and **correspond** as full cards alongside **decomposer**”
- `grade3-reading/ti-courseplans-wiki/Peter-Pan-Quality-Case-Study-2026-08-24.md` (362): “the Grade 3 iteration-6 distilled instruction-design rule says **2–3 Tier-2 words per lesson**;”
- `grade3-reading/curriculum-gen/audits/PETER-PAN-AUDIT-2026-08-24.md` (54): “Exactly one high-leverage word is taught — chosen to unlock this text and to”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/HUMAN-g3r-2026-07-27T08-38-36-019fa24b-fb42-7e61-a954-216db3ef77a4.md` (1097): “Exactly one high-leverage word is taught — chosen to unlock this text and to feed the Phase 3 inference.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/generated/feedback-2026-08-11-crosswalk.json` (59): “Keep the taught vocabulary load to no more than three necessary words and drop a likely-known redundant word such as clever.”
- `grade3-reading/artifacts/qc-2026-09-29-staging/new-lesson-qa-invariants.md` (56-58): “**B1. The taught-word count is what the knowledge base prescribes** for the lesson — not a fixed number. (The original finding was one word where the knowledge base expected more; three is typical, not a rule.)”
- `grade3-reading/course-renderer/authoring/inputs/rule-packs/reading-g3.json` (179): “User ruling 2026-09-14: THREE taught words per lesson, drawn from the curriculum map's Vocab Coverage row for the text. This overrides the academics team's master spine, which says exactly one”
- `g9/library/text/L36b8ba.txt` (215): “Six words may also be too many for one pre-reading beat, and they are not of equal difficulty — façade and pretense are a long way harder than disloyal.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D4-vocabulary.md` (20): “The word set is bounded to about 6–10 across a week, with only 3–5 introduced at once”
- `grade3-reading/artifacts/Peter-Pan-L4-review-response-2026-08-25.pdf` (p.3 (pdftotext line 124)): “The Knowledge Base assigns exactly one taught word per lesson, and it does so in all eleven lessons of this unit.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (94-95): “G5-BAR §4 pins one blocking word only.”
- `grade3-reading/.claude/skills/one-perfect-lesson/SKILL.md` (53): “≤3 non-synonym vocab words with why-the-non-example-fails”

Against: A later run found counter-evidence (`grade3-reading/curriculum-gen/audits/PETER-PAN-AUDIT-2026-08-24.md`).

<sub>context · wording, sequence · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### How much context a writer needs

How much context to give a writer, and when scope notes, source documents or curriculum blocks start to lower what it makes, is unsettled.

An autopsy of document-based items found the arm that added generic curriculum notes to the real source documents did worse than the documents alone, and advised against layering such notes in until an A/B test showed no regression (`dbq_structural_zero.md`, line 136). A distilled report adds that, for dense courses, too many prompt examples can hurt (`ap_social_studies_generator_distilled.md`, line 186), while a generator kit lists scope boundaries injected at generation time as its fix for out-of-scope questions, in a design table rather than a measurement (the kit's `README.md`, line 139). To settle it: the A/B the autopsy asked for, on many more than six items, with and without each kind of context.

Quoted:

- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md` (136): “- DBQ route should prefer D13-only source grounding. Do not layer generic curriculum notes into the DBQ prompt until an A/B proves no regression; PATH G hybrid was worse than D13-only.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/ap_social_studies_generator_distilled.md` (186): “- For dense courses like APUSH, too many prompt examples can hurt; prefer exact facts/source packs over long example lists.”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/README.md` (139): “| Out-of-scope questions slip through | `assessment_boundaries` injected at gen time |”
- `ap-agent-memory/feedback_d13_inference_injection_partial_fix_2026_05_12.md` (15): “| 1 vanilla (no docs) | 0/6 | 0.0% | 0.789 | 0.000 | 1.000 |”
- `ap-agent-memory/feedback_d13_inference_injection_partial_fix_2026_05_12.md` (16): “| **2 D13-only** (7 docs in user) | **1/6** | **16.7%** | 0.502 | **0.200** | 0.400 |”
- `ap-agent-memory/feedback_d13_inference_injection_partial_fix_2026_05_12.md` (18): “| 4 hybrid (D13 + curriculum) | 0/6 | 0.0% | **0.125** | 0.000 | **0.000** |”
- `ap-agent-memory/project_richer_rag_per_cell_tradeoff.md` (38): “For SAQ (3 sub-questions, structured response): the verbose context confuses the response format. SAQ requires terse 2-3 sentence answers per sub-part; the boundaries text makes the model add disclaimers/scope notes that the grader doesn't reward.”
- `ap-agent-memory/project_richer_rag_per_cell_tradeoff.md` (19): “| apush/mcq | 93.3% | **100.0%** | +6.7pp | ±0.5pp | ✓ REAL LIFT |”
- `ap-agent-memory/project_richer_rag_per_cell_tradeoff.md` (23): “| apush/saq | 77.8% | **68.3%** | **-9.5pp** | ±3.8pp | ✗ REAL REGRESSION |”
- `ap-agent-memory/feedback_d13_inference_injection_partial_fix_2026_05_12.md` (7): “**Rule (P0/T1; n=6 single-seed, single-model — promote to T0 after n≥30 replication):**”
- `ap-agent-memory/feedback_baseline_must_be_fresh_gen.md` (36): “| richer-RAG | -1.43 cont-pp | +0.25 cont-pp | noise |”
- `ap-agent-memory/feedback_d13_inference_injection_partial_fix_2026_05_12.md` (36): “**Training-time (v52b+):** D13 + curriculum_context in system are PROVEN safe (v52b build pattern).”

Against: The worse result rests on six prompts (`build_PATH_G_dbq_hybrid.py`, line 4). Six items, one seed, one model (`feedback_d13_inference_injection_partial_fix_2026_05_12.md`, line 7). Measured against fresh outputs rather than stored ones, the richer context's overall effect on the continuous score was noise, +0.25 points (`feedback_baseline_must_be_fresh_gen.md`, line 36). Training with both blocks in the system message was reported safe (`feedback_d13_inference_injection_partial_fix_2026_05_12.md`, line 36).

<sub>context · generation, alignment · universal · from ap · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### How much knowledge comes through media

How much of a reading course's knowledge building should come through other media rather than through reading is undecided. One suggestion in a build meeting put the share of content knowledge building that relies on multiple media at maybe 30% or 40%.

In a build meeting on 8 October 2026, after watching recorded performances of key scenes was discussed, one participant said that in a course this centred on knowledge, bringing in other elements of knowledge makes sense, asked where to draw the line, and suggested putting a stake in the ground: maybe 30% or 40% of the content knowledge building relying on multiple media, with other parts purely reading (`g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_08 10_30 CEST - Notes by Gemini.md`, lines 434-464). Nothing on record fixes the share.

Quoted:

- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_08 10_30 CEST - Notes by Gemini.md` (456): “Bringing other elements of knowledge makes total sense. But where do we draw the line?”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_08 10_30 CEST - Notes by Gemini.md` (460): “So just the more things that we can kind of you know articulate and put stakes in the ground about”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_08 10_30 CEST - Notes by Gemini.md` (464): “saying yes this is a reading app but it because there's knowledge we need to bring in these elements maybe 30% or 40% of the content knowledge building will be will rely on multiple media but these aspects of it are purely reading like you read a”

Against: none found

<sub>context · media, stimulus · universal · from g9 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### How much of a lesson is review

How much of a lesson should be review, and whether that share should change with the lesson's place in a unit, is unsettled. One course's documents give about 70:30 review to new for middle lessons, about 70:30 new to review, and about 90:10 review to new.

A Grade 4 reading course's generation contract replaced a literal 90:10 review budget with a banded one: middle lessons about 70:30 review to new, openers about 50:50 because little has been taught, and synthesis or transfer lessons about 90:10. The same course's pedagogy notes and foundations document say about 70:30 new to review, and its sequencing brief sets within-unit spacing at about 90% review and 10% new across interleaved tracks, as does a Grade 1 plan. The documents agree that review runs in tracks beside the new material and differ on the share, and nothing measured which share helps learners.

Quoted:

- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/generation-contract.md` (85): “Review budget (banded, not literal 90:10)”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/generation-contract.md` (86-87): “Middle lessons ~70:30 (review:new); openers/BUILD ~50:50 (little prior; say so); synthesis/transfer ~90:10.”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/generation-contract.md` (87-88): “Show a "today's budget" line and name the review tracks.”
- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/PEDAGOGY.md` (171): “Reviewed material keeps returning inside new lessons (~70:30 new:review, DI track”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/foundations.md` (30): “Review is budgeted into every lesson (~70:30 new-to-review), mastery is re-tested after a delay,”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/SEQUENCING-BRIEF.md` (117): “**Within-unit spacing** per the DI track model (~90% review / 10% new across interleaved tracks).”
- `grade3-reading/ti-courseplans/courses/g1-reading/brainlifts/v0.1.md` (180-181): “**Track-design lesson composition** — ~90% review / 10% new across 4–6 interleaved tracks (ability-adjusted)”

Against: none found

<sub>context · sequence, practice · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### How much text a screen should hold

How much text one screen should hold at each grade is unsettled: a sparse screen suited to early grades was judged right for older readers decoding archaic language. In one build meeting a Grade 9 prototype screen was put at maybe a grade three or four kind of sparseness.

In a build meeting on 7 October 2026, one participant asked whether there was a view on how much text should be on a screen, put a Grade 9 prototype's screen at maybe a grade three or four kind of sparseness and asked for a Grade 9 metric, while calling that a guess with no background in learning science (`g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md`, lines 518-532). Another participant answered that learners were already decoding the text's archaic language, so the amount shown was accessible, and more could come where they are confident (lines 542-550). No density measure by grade is on record.

Quoted:

- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md` (518): “Also, is there an opinion about how much density of text should be on a screen?”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md` (522): “at maybe a grade three or four kind of sparseness. Do we have any metric for what we expect out of a grade nine?”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md` (532): “guesstimate with no background in learning science.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md` (542): “I think what's unique about this text is it's Elizabeth and language.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md` (546): “So I think their adjustments would just have to naturally be made because they're already trying to decode language.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md` (550): “So where they're confident, you probably could naturally have more, but they were already trying to decode this text.”
- `g9/library/text/L64fb8b.txt` (128): “**Screen Text Density Standards for Grade 9**”
- `g9/library/text/L64fb8b.txt` (128): “noting that the current sparse UI appeared more suited to Grade 3 or 4”
- `g9/library/text/L64fb8b.txt` (128): “observed that the limited text density works well for decoding complex Elizabethan language, but agreed to establish clear guidelines to eliminate guesswork and limit necessary design iterations”

Against: none found

<sub>context · demand, accessibility · universal · from g9 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### How small an honest test can be

Size a test to the claim it must settle; how small an honest validation gate can be is still open. At 50 items per type, one item moves a rate by 2 points, so a 98.8% average could not be told from a 99% target.

Pass rates per item type on 50-item sets were averaged into a 98.8% projection against a 99% target; the report called the target essentially reached while noting that resolution at n=50 per cell is ±2pp and that 98.8% sits within the noise band of 99% (24 May 2026). The parallel lab's distillation left open what the smallest statistically honest validation gate is that predicts full quality without a multi-day scoring run.

Quoted:

- `aptraining-local/den-of-ideation/reports/validation_triage/20260524T175907Z_2026-05-24T1759Z_UNIT1_DBQ_SOLVER_v3_VALIDATED_TARGET_REACHED.md.md` (135): “avg(100, 100, 100, 98, 96) = 98.8%”
- `aptraining-local/den-of-ideation/reports/validation_triage/20260524T175907Z_2026-05-24T1759Z_UNIT1_DBQ_SOLVER_v3_VALIDATED_TARGET_REACHED.md.md` (137): “Statistical resolution at n=50 per cell is ±2pp; 98.8% sits within the noise band of 99%.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md` (85): “What is the smallest statistically honest validation gate that predicts full 26,355-row quality without a multi-day scorer run?”
- `grade3-reading/bias_experiment/experiment-record/evidence/knowledgebot/kb-0132-eppc-bias-experiment-execution-handover.qmd` (528-530): “The C critical-recall gate alone needs roughly 299 independent critical-positive cases with zero misses for a nominal one-sided 95% bound before clustering/multiplicity.”
- `grade3-reading/bias_experiment/.agent/memory/COUNTERFACTUAL_AUTHORITY_A0_2026-07-17.md` (99-100): “This probe has only two rule dimensions, one prompt shell, one call per cell, no authority-removal/placebo arm, and no robust confidence bound.”

Against: none found

<sub>context · measurement · universal · from ap · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### How spelling counts in answers

How should spelling count in a comprehension answer, for each kind of task and for typed and spoken answers?

A content review of a Grade 3 lesson found a misspelled answer that the judge had marked fully correct and asked for a stated spelling policy for comprehension answers; the register put the policy question first, since whatever is ruled becomes a judge prompt and a validator. Follow-up proposals found that meaning and spelling had different contracts across gate families and asked for one explicit credit and feedback policy per task type and input mode, decided once: what earns comprehension credit, when spelling is corrected separately, and how typed and transcribed answers differ. They add that correctness must not collapse to keyword presence.

Quoted:

- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/REGISTER.md` (17): “Misspelled answer marked correct ("magician")”
- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/VERIFICATION-PROPOSALS.md` (8): “Meaning and spelling currently have different contracts across gate families.”
- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/VERIFICATION-PROPOSALS.md` (8): “Explicit credit/feedback policy per task type and input mode.”
- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/VERIFICATION-PROPOSALS.md` (16): “The spelling policy: what earns comprehension credit, when spelling is separately corrected, and how typed versus transcribed answers differ.”
- `g9/transformer/src/mechanics/say-it-back.js` (3): “a near spelling of a long word is named but not counted as a miss”
- `g9/transformer/src/mechanics/say-it-back.js` (22): “"spelling" (a slip in a word of five letters or more, named but not a miss)”
- `g9/transformer/src/mechanics/say-it-back.js` (28): “w.length >= 5 && words.some((x) => x[0] === w[0] && Math.abs(x.length - w.length) <= 2 && lev(x, w) <= (w.length > 7 ? 3 : 2))”
- `g9/transformer/test/mechanics.test.mjs` (91): “Check the spelling of "pretence"”
- `g9/transformer/src/mechanics/key-words.js` (4): “gets a nudge, since a taught word is spelled right; the second miss gives the word.”
- `g9/transformer/src/glue/threejs-archivist.js` (176): “count at once, a one-letter slip of them too (spelled right back); any other word goes to Jev, generously.”
- `g9/transformer/test/calibration/word-web.linked.json` (13): “Deceive, misspelt: the link is plain, and the web does not mark spelling.”
- `g9/transformer/src/mechanics/key-words.js` (4): “gets a nudge, since a taught word is spelled right”
- `g9/transformer/src/mechanics/key-words.js` (119): “Nearly. That is the word, but the spelling is not right yet.”
- `g9/transformer/src/mechanics/key-words.js` (3-4): “a near spelling … gets a nudge, since a taught word is spelled right”
- `g9/transformer/src/mechanics/word-web.js` (110): “Could a Grade 9 reader reasonably link word to centre: a kind of it, a sign of it, a word for someone who shows it, or what it does to people? A random word, a name, or a word with no link does not count.”
- `g9/transformer/src/glue/animated.js` (113): “One real English word or short phrase (spelling slips are fine) connected to ${it.centre}”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “Code checks that every term is there; a spelling slip is named but not counted as a miss.”
- `g9/transformer/src/mechanics/say-it-back.js` (22): “a slip in a word of five letters or more, named but not a miss”
- `g9/transformer/src/mechanics/say-it-back.js` (28): “if (w.length >= 5 && words.some((x) => x[0] === w[0] && Math.abs(x.length - w.length) <= 2 && lev(x, w) <= (w.length > 7 ? 3 : 2))) return "spelling";”
- `g9/transformer/src/glue/animated.js` (113): “(spelling slips are fine)”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/CASE-FOR-APPROVAL.md` (107): “rubric; the only difference is that a speaker is not marked down for punctuation they never chose.”
- `othello-archive/server/tasks/retrieval.mjs` (44): “Spelling slips are fine.”
- `othello-archive/server/tasks/threads.mjs` (34): “Spelling slips are fine.”
- `othello-archive/server/tasks/close.mjs` (28): “Spelling slips are fine unless a taught word is misspelled.”
- `othello-archive/src/steps/KeyWords.tsx` (4): “Spelling must be right (taught words).”
- `othello-archive/server/tasks/oral.mjs` (12): “The answer is transcribed speech: ignore filler words, missing punctuation, capital letters and small transcription slips. Never mark down spelling.”
- `g9/library/text/L36b8ba.txt` (128): “Mark misspellings rather than silently correcting them.”
- `g9/library/text/Lb6a406.txt` (6): “{"id": "w02", "check": 0, "cat": "misspelled", "answer": "manipulashun", "expected_met": ["connected"]},”
- `grade3-reading/incept-read-app/apps/broker/WRITING-SCORE.md` (132): “Spelling is never penalized.”
- `grade3-reading/course-renderer/docs/extras/alpharead-staar-writing-research.md` (157): “Spelling/punctuation errors in the revision are generally **not penalized** — the item measures revising skill.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (128): “Mark misspellings rather than silently correcting them.”
- `othello-archive/scripts/qc-judge-cases.json` (24-26): “"answer": "Rodrigo and Lago are fighting about Othello eloping with Brabantios daughter",”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1937): “If language mechanics are not part of the claim, either score them separately or don’t score them.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/01-NON-NEGOTIABLES.md` (52-53): “**Quote fidelity is 95% similarity, not exact** (2026-08-17: "The student is penalized for very tiny differences"). Levenshtein ratio ≥0.95 over normalized strings”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/07-SCORING-FEEDBACK-XP.md` (41-43): “Quote fidelity: 95% similarity (edit-distance ratio over normalized strings; case, quote marks, whitespace fold away; "sticks"/"stick" passes; truncation/paraphrase fails with the fixed "copy them just as they are" steer).”
- `grade3-reading/artifacts/u4l2-build/METHODS-CHECKLIST.md` (179-181): “**D2. Exact-quote checks fail closed.** Where the child must type the exact quote from the text, any deviation (a "botched quote") is marked not-yet-correct; only a verbatim match (modulo a declared, minimal normalization such as leading/trailing whitespace) passes.”

Against: none found

<sub>context · marking, key · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Human review or statistics for test items

Whether a measurement test's machine-written items need a person's review before students see them, or a gate on every item plus response statistics is enough, is disputed. One package's machine gate screened all 786 items, and its recheck still advised a 60-item human sample.

An adversarial review of a pre-pilot reading assessment objected that no person had read its machine-written items for young students. The package answered that for a measurement instrument the load-bearing check is statistical, not editorial: a 14-dimension machine gate screens every item, misfitting items are dropped or re-estimated at calibration, and its scores carry no consequence before validation (`grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/PROTEST_BRIEF.md`). The recheck scored the point answered, not closed, a refusal with reasons rather than a fix, and still advised a 60-item human sample (`grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RECHECK_FINDINGS.md`).

Quoted:

- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/PROTEST_BRIEF.md` (65): “For a measurement instrument, the load-bearing QC is statistical, not editorial.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/PROTEST_BRIEF.md` (66): “Its scores carry no mastery, grade, or accountability consequence before validation — by code, not by promise.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/PROTEST_BRIEF.md` (64): “the gate screened all 786.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RECHECK_FINDINGS.md` (19): “But it is a *refusal with reasons*, not a fix”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RECHECK_FINDINGS.md` (67): “sampling remains advisable even under the §9 stance — a 60-item human sample is cheap insurance”

Against: Both sides agree that items which passed no gate may not be served: 32 items written while the gate was down were replaced (`grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/PROTEST_BRIEF.md`, line 67; `grade3-reading/ti-courseplans/courses/map-proxy-assessment/skill/SKILL.md`, line 83).

<sub>context · review, measurement, generation · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Informational passages as long as stories

Whether informational passages should run as long as narrative ones, or may stay shorter for their knowledge density, is unsettled. One Grade 3 course's informational passages ran about 310–330 words against about 460–500 for its narratives.

A Grade 3 reading standard lists the informational text-length floor among the bounded questions still awaiting a ruling: its informational passages run about 310–330 words and its narratives about 460–500, and it asks whether to raise the informational floor or accept it for knowledge density. Its text-quality criteria record the same open decision and keep the mechanical length check advisory for informational texts until it is ruled. Nothing measured which length serves readers.

Quoted:

- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/g3-reading-standard.md` (257): “G3 informational currently runs ~310–330w; narrative ~460–500w. Raise the informational floor, or accept it for knowledge density?”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D8-text-quality.md` (34): “The informational-text length floor (currently ~310–330 words) is unsettled; the D8.12 mechanical length check treats the informational floor as advisory until this is ruled.”

Against: none found

<sub>context · stimulus, demand · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Likely misreadings in a rubric

Whether a rubric should list a question's likely misreadings, each checked on its own and answered when nothing else is met.

The lesson engine's marking adapter for an animated version asks the judge about each misreading a rubric lists, as a question of its own, and reports one only when no criterion is met and none is unsure (`g9/transformer/src/glue/animated-judge.js`). Every rubric the engine exports sets that list to empty (`g9/transformer/src/glue/animated.js`), and its adapter for a 3D version has no misreading check at all.

Quoted:

- `g9/transformer/src/glue/animated-judge.js` (87): “Does answer show this misreading:”
- `g9/transformer/src/glue/animated-judge.js` (104): “const misreading = met.size || unsure.length ? null :”
- `g9/transformer/src/glue/animated.js` (68): “misreadings: [],”
- `grade3-reading/incept-read-app/docs/G4-SCR-example-native-qti.md` (98): “Common wrong turns → these should score 0. This is what makes the grader *discriminate*.”
- `grade3-reading/incept-read-app/docs/G4-SCR-example-native-qti.md` (122): “Proof — the real graded response (good answer → 2/2)”
- `grade3-reading/incept-read-app/docs/G4-SCR-example-native-qti.md` (145): “**Off-target** ("Seeds need sunlight and good soil") → **0**”

Against: none found

<sub>context · scoring-guide, feedback · universal · from g9 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Machine marks on AP free responses

Can a machine marker score AP-style short answers and essays reliably enough to award mastery, once calibrated against independently scored responses?

An AP history course's production plan names the case where a response cannot be graded confidently: record it without verified mastery or XP, route low-confidence constructed responses to human review, and calibrate against independently scored AP responses before enabling mastery effects. Its status file lists target-runtime mastery, XP, event and accessibility behaviour as contracted, not run, so no calibration result exists. Until one does, the plan gives a machine score of a free response no power over mastery.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/PRODUCTION-HARDENING-PLAN.md inside it) (123-125): “1. Record the response without verified mastery or XP. 2. Route low-confidence constructed responses to human review. 3. Calibrate against independently scored AP responses before enabling mastery effects.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/FULL-COURSE-AUTHORING-STATUS.md inside it) (51): “Target-runtime mastery, XP, event, and accessibility behavior | Contracted, not run”

Published: [EduBench (2025), arXiv:2505.16160](https://arxiv.org/pdf/2505.16160) · [Henkel et al. 2024](https://arxiv.org/abs/2405.02985)

Against: Published evidence points both ways: one benchmark found model judges scoring educational responses higher than people and agreeing with them only in part, while a large study found model and human markers of short answers agreeing almost as well as people agree with each other.

<sub>context · marking, evaluation, evidence-of-learning · domain · from ap, research · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Marking open interpretations reliably

How to mark open interpretations reliably, crediting every defensible reading without forcing one approved answer, and whether a model should do that marking, is unsettled.

The Grade 9 unit's design brief lists judging defensible interpretations without forcing one approved answer among the decisions to make before building (`g9/transcript/chat-transcript.redacted.txt`, line 2893). A later list of gaps says the unit's preparation gives a framework for reviewing an unsupported claim, a misread quotation and a defensible alternative interpretation, but that the browser walk-through of the built lesson did not establish assessment reliability (line 4501). A summary of later meeting notes records that model checks of interpretations were not a settled decision (line 6017).

Quoted:

- `g9/transcript/chat-transcript.redacted.txt` (2893): “How will we judge defensible interpretations without forcing one approved answer?”
- `g9/transcript/chat-transcript.redacted.txt` (4501): “Our prep gives us a framework for reviewing those cases; the browser walkthrough did not establish assessment reliability.”
- `g9/transcript/chat-transcript.redacted.txt` (6017): “Removing the Archivist and using LLM interpretation checks were not settled team decisions.”

Against: The brief proposes what marking should reward: "Assessment must reward textual fit, justified inference and responsiveness to counterevidence rather than agreement with a model answer." (`g9/transcript/chat-transcript.redacted.txt`, line 3086). That names the target, not a reliable way to mark it.

<sub>context · marking, scoring-guide, evaluation · universal · from g9 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Mean or worst shuffle for leaks

Whether a leak gate for items served in shuffled order should judge the mean over many shuffles or the worst one is unsettled. Judged by the mean, 31 ordering and 69 matching items that the worst case had excluded were restored, and none of the 31 solved exactly.

A Grade 5 course's anti-leak gate moved from the worst case to the mean over resampled shuffles, because the platform randomises the presentation order on every attempt, so a student meets the distribution, while the worst case measures an attacker's luckiest presentation. Earlier, certifying on one seeded shuffle had shipped a leaky item and six more ordering items that a blind solver answered at 0.60 or above, one at exactly 1.000. The course's retrospective lists single-shuffle certification, and assuming worst-case and mean-case were interchangeable, among what failed, and the mean-metric evidence was among the claims its red-team records still disputed.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/analysis/mean-metric-2026-07-07/README.md inside it) (5-7): “the platform **randomizes the presentation order on every attempt**. A student cannot select the order; they face the distribution.”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/analysis/mean-metric-2026-07-07/README.md inside it) (7-9): “Their expected blind-solve performance is therefore the **mean over resampled shuffles**, not the worst case. Worst-case measures an attacker's luckiest presentation, which no student controls under `shuffle="true"`.”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/analysis/mean-metric-2026-07-07/README.md inside it) (19-21): “- Restored (borderline under worst-case, safe under mean): 31 sequence + 69 match. **0 of the 31 restored sequences exact-solve; mean 0.31–0.58; worst 0.33–0.75.** The high worst-case values are lucky single-shuffle hits the student never reliably sees.”
- `grade3-reading/_archive/2026-08-13-consolidation/orientation-sweep-digest/agent-damage.md` (60): “anti-leak gate certified on ONE seeded shuffle, shipping a leaky certified_clean item (grade5 u1-l19-q09-sequence blind pair_acc≈0.75, resampled ~88% ≥0.6) and 6 more certified sequence items ≥0.60 blind including one at exactly 1.000”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/QUESTION_CONVERSION_RETROSPECTIVE.qmd inside it) (195-198): “What failed: - single-shuffle certification for sequence items; - assuming worst-case and mean-case were interchangeable;”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/STUDENT_READY_CRITICISM_FRAMEWORK.qmd inside it) (176): “Active beads `B0154`, `B0155`, `B0156`, `B0157`, `B0160` challenge mean-metric evidence, gate arithmetic, expansion validity, construct validity, and 1241/0/0 certification.”

Against: A rule on record judges a without-text check by the worst of several option orders (run-the-without-text-check-the-hard-way).

<sub>context · integrity, evaluation · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Measuring a course, not its items

Whether measures built for questions and lessons can judge how a course sequences and builds knowledge, or a course needs measures of its own.

Notes from a July 2026 meeting on the reading project record that the benchmark in use stays useful at question and lesson level, but new metrics are needed to assess lesson sequencing and knowledge building (`grade3-reading/knowledge_bot/knowledge/kb-0125-coe-catchup-2026-07-13.qmd`). The same notes say the evaluation framework must be updated to validate the newly proposed course structure (the same file).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0125-coe-catchup-2026-07-13.qmd` (101-103): “Incept Bench remains useful at question/lesson level, but new metrics are needed to assess lesson sequencing and knowledge building”
- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/COMPOUNDING-GATE.md` (8-10): “It has **no knowledge of the course's cross-lesson reinforcement plan**, so it cannot tell whether a lesson actually *compounds* on the ones before it.”

Against: none found

<sub>context · measurement, sequence · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Mental models as skill-map nodes

Should a skill map name, as nodes of their own, the mental models its operations presuppose, such as a text being made for a purpose or claims needing support?

A proposed change to a Grade 5 reading skill graph of 47 skills notes that it names operations, schemas, facts and exam mechanics but none of the mental models the operations presuppose, and adds an audit step asking, for each operation, what model must already be in place for it to be teachable and whether the graph names it. Its candidates are a text as a made thing whose content, order and emphasis were chosen for a purpose, and claims as things that need support and can lack it. The proposal says such models are built through coordinated examples rather than stated, and that without them the graph declares students ready when their mental model is not.

Quoted:

- `grade3-reading/artifacts/semantic-judge-calibration-2026-07-10/kc-graph-change-proposal.md` (123-125): “**text as authored artifact** - a text is a made thing whose author chose content, order, and emphasis for a purpose; presupposed by infer_point_of_view, disc_reasons_and_evidence, and every source-attribution construction, captured by none of them.”
- `grade3-reading/artifacts/semantic-judge-calibration-2026-07-10/kc-graph-change-proposal.md` (129-130): “The audit asks, per operation in the closed vocabulary: what mental model must already be in place for this operation to be teachable, and does the graph name it as a node?”
- `grade3-reading/artifacts/semantic-judge-calibration-2026-07-10/kc-graph-change-proposal.md` (133-134): “Without them the graph declares students ready when their mental model is not.”
- `grade3-reading/artifacts/semantic-judge-calibration-2026-07-10/kc-graph-change-proposal.md` (9): “**Status: PROPOSAL ONLY.**”

Against: It is a proposal only: the graph was not modified, and no result of the audit is recorded (`grade3-reading/artifacts/semantic-judge-calibration-2026-07-10/kc-graph-change-proposal.md`, lines 9-12).

<sub>context · sequence, alignment · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Missing facts or unused facts

Whether wrong facts in generated items were missing from the writer's material or there and unused decides the fix, and the test that tells them apart has no recorded result.

A diagnosis in the AP work split 'not enough data' into two causes with opposite fixes: facts the training corpus does not contain, where a bigger model will not help, and facts it contains but the model fails to retain, where a bigger model is justified (`icloud-work/aptraining/workspace/comms/from_analyzer/2026-05-27T1741Z_DIAGNOSIS_data_adequacy_binding_lever.md`, lines 10-14). It asked for the failing facts to be checked against the corpus, because row count alone cannot tell the two apart (lines 16 and 19), and the check was asked for again the next day (`icloud-work/aptraining/workspace/comms/to_analyzer/2026-05-28T0614Z_dream_sequence_sync_2.md`, lines 32-39). No verdict is in the folder where it was asked for, which holds only an acknowledgement and the diagnosis, and a later fix asserted that the facts were in the corpus but the writer had not been given the curriculum context, so it changed the prompt instead (`icloud-work/aptraining/workspace/comms/to_analyzer/2026-06-01T1838Z_dream_sequence_sync.md`, line 30). To settle it: check a sample of the wrong facts against the writer's training data and the material it was given, and choose the fix by what that shows.

Quoted:

- `icloud-work/aptraining/workspace/comms/from_analyzer/2026-05-27T1741Z_DIAGNOSIS_data_adequacy_binding_lever.md` (16): “**The discriminating test (please make the data-adequacy assessment answer THIS, not just row count):** take the off-period hallucination cases (e.g. the 1920s-DBQ-for-Unit-1 sample) and check whether those specific Unit-1 facts are PRESENT in the training corpus.”
- `icloud-work/aptraining/workspace/comms/from_analyzer/2026-05-27T1741Z_DIAGNOSIS_data_adequacy_binding_lever.md` (19): “Row-count alone ("14k = not enough") cannot tell these apart, and it's the exact spot where "bigger base" gets pulled without the binding lever named.”
- `icloud-work/aptraining/workspace/comms/to_analyzer/2026-06-01T1838Z_dream_sequence_sync.md` (30): “This addresses §2 coverage-lever side of your 5/27 binding-lever fork: facts ARE in the corpus, but the generator wasn't conditioned on the curriculum context that defines the alignment criterion.”
- `icloud-work/aptraining/workspace/comms/to_analyzer/2026-05-28T0614Z_dream_sequence_sync_2.md` (39): “Drop verdict at `from_analyzer/<UTC>_COVERAGE_VS_CAPACITY_v4.md`.”
- `icloud-work/aptraining/workspace/comms/from_analyzer/2026-05-27T1741Z_DIAGNOSIS_data_adequacy_binding_lever.md` (13): “(you can't retain facts that aren't in the training set)”

Against: The later message says the facts are in the corpus without showing the test, and its request to re-measure after the change (`icloud-work/aptraining/workspace/comms/to_analyzer/2026-06-01T1838Z_dream_sequence_sync.md`, line 34) has no reply in that folder.

<sub>context · generation, integrity · universal · from ap · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Modern version first or original with glosses

Whether learners should meet a hard archaic text first in a modern version, beside one, or only in the original with glosses of key words is unsettled.

The sources differ. In a build meeting on 7 October 2026, one participant said they read a scene with students in standard English before looking at the original language, yet praised the build's glosses of key words only as support that does not make the text too easy; another recalled that the earlier plan made the original the primary text, with a translation only as an aid; and the build shown used snippets that translated lines into contemporary English (`g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md`, lines 434-488). A planning meeting on 1 October floated an optional side-by-side modern translation for learners who struggle (`g9/sources/meeting-notes/ELA - CNU + Academics - 2026_10_01 20_30 IST - Notes by Gemini.md`, line 228).

Quoted:

- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md` (484): “I'm not a purist. I will read a scene with the students in standard English. They understand it and then and then we'll look at Elizabeth language.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md` (488): “But that strategy here you had of just like keywords is great because then that still allows support but also doesn't make it too easy and accessible.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md` (442): “primary version that drives this was supposed to be the the Shakespearean you know original which is non-copyrighted”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md` (472): “One thing we one thing we did to help the student kind of assimilate or understand the Elizabeth language is to have these info snippets that basically translated”
- `g9/sources/meeting-notes/ELA - CNU + Academics - 2026_10_01 20_30 IST - Notes by Gemini.md` (228): “Now there are options. I'm sure you've seen them like a no fear Shakespeare sort of thing where they have the archaic text next to uh the modern.”
- `g9/sources/meeting-notes/ELA - CNU + Academics - 2026_10_01 20_30 IST - Notes by Gemini.md` (228): “maybe they have the option to open up that kind of translation section as they're reading.”

Against: A published classroom guide to cutting the opening scene uses no translation and ends: "Celebrate the fact that students made meaning from this scene without any internet explanation or teacher translation" (`g9/sources/Cutting-a-Scene-Othello-1.1.pdf`, pdftotext lines 140-141).

<sub>context · stimulus, accessibility, sequence · domain · from g9 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Narration that turns to the student

Whether narration before a story should ever speak to the student: one rule calls such lines filler that breaks the fiction, another keeps them as the labels that teach.

The intro-video BrainLift holds two versions of its rules, and they disagree here (`downloads/BrainLift - What makes a good intro video.md`). The world-only version says fillers like "let's meet our characters" feel engaging and do the opposite, because a narrator who turns to the audience ends the fiction that the child is already inside the world (line 106), and it bans student framing such as "in this lesson" (line 950). The other says such connective lines are not padding but the labels that name what the child is looking at (line 315), lets the narrator of a short video speak to the viewer (line 341), and ends its own worked script on "As you read, notice how each place makes you feel" (line 405).

Quoted:

- `downloads/BrainLift - What makes a good intro video.md` (106): “Fillers like let's meet our characters feel engaging and do the opposite.”
- `downloads/BrainLift - What makes a good intro video.md` (106): “The film's engagement is the fiction that the child is already inside the world, and a narrator who turns to the audience ends it.”
- `downloads/BrainLift - What makes a good intro video.md` (950): “No student framing language such as "in this lesson" or "you will learn"”
- `downloads/BrainLift - What makes a good intro video.md` (315): “They are not padding; they are the labels.”
- `downloads/BrainLift - What makes a good intro video.md` (341): “the narrator in shorter videos can just state the fact or speak to the viewer”
- `downloads/BrainLift - What makes a good intro video.md` (405): “As you read, notice how each place makes you feel.”
- `downloads/BrainLift - What makes a good intro video.md` (249): “no child has yet been observed watching one of our films.”

Against: The world-only version calls itself internal doctrine, with no child yet observed watching one of its films (`downloads/BrainLift - What makes a good intro video.md`, line 249).

<sub>context · wording, media · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Nudging a stalled reader

How to nudge a reader who stalls or keeps guessing; nothing in my engine does yet.

The lesson engine's playtest refuses idle actions because nothing in the runtime nudges a reader who is stuck, and a
guesser in a choice block has no attempt ceiling (`g9/transformer/src/quality/playtest.js`); a director that adapts is
planned for a later stage (`g9/transformer/v05/README.md`). To settle it: the scripted stuck reader and guesser finish
with a nudge, and a person-labelled set shows the nudge comes at the right moment.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (79): “the "not so fast" nudge is non-blocking and can be skipped by clicking Next twice.”
- `grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd` (63): “The system needs three outcomes, not two: promote, keep practising, or switch to corrective instruction.”
- `grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd` (65): “A mastery system that lacks an explicit “switch mode” state will inevitably turn persistence into the hidden criterion for passing.”
- `grade3-reading/knowledge_bot/knowledge/kb-0157-mastery-signal-evidence-base.qmd` (430): “when a learner is failing, we currently just let them keep attempting items.”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (187): “iter-3 `silent`/"I don't know" branch authored + gated in 18/18 but **can never fire** (any tap resolves elsewhere; no timeout / "I'm not sure" affordance)”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D2-opportunities-to-respond.md` (18): “scaffold-down (feedback / reframe / supply / model / engage) is actually reachable for the child who freezes or says "I don't know"”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (47): “Open answers route to full / brief / partial / off-track / silent paths | Every path teaches; the silent child is taught first, then re-asked easier”
- `downloads/WF - Brainlift Opportunities to - 260724-110911.md` (90): “When a child struggles, scaffold down by giving feedback, reframing, supplying an answer, offering a model to mimic, or simply keeping the child engaged (Zucker et al., 2020).”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md` (873-874): “Now a quiet "I'm not sure yet" door routes there.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md` (876-877): “**An escape hatch offered up front stops being an escape hatch.** The door is revealed after ~20s (`CFU_UNSURE_MS`), below the tappables, deliberately.”
- `grade3-reading/knowledge_bot/knowledge/kb-0192-g3-book-component-catalogue.qmd` (74-75): “after 4 wrong taps, Scout offers to find the remaining clues”
- `grade3-reading/artifacts/wiki-research/cross-cutting.md` (200): “the child who freezes needs scaffold-down”
- `grade3-reading/knowledge_bot/knowledge/kb-0227-g3-branch-hygiene-pr634-prep-2026-09-24.qmd` (63-64): “Silent branch on L4/L6 models a line from the story and asks its meaning”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D2-opportunities-to-respond.md` (18): “is actually reachable for the child who freezes or says "I don't know"”
- `grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd` (651-652): “after 4 wrong taps, Scout (the guide) offers to find the remaining clues”
- `downloads/WF - Brainlift Opportunities to - 260724-110911.md` (102): “No response or “I don’t know.” | Down (engage, mimic) | “Is Kitten happy or sad?””
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md` (876-879): “It is the one button on screen that cannot be wrong, so mounted with the options it becomes the *cheap path* and children who would have answered take it.”
- `g9/transformer/v02/QA.md` (135): “the one finding left is a gap (no idle nudge, v05).”
- `g9/transformer/src/quality/playtest.js` (156): “the runtime has no idle or timer action, so nothing nudges a reader who is stuck”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-23.md` (37-39): “They ask which line in the story supports the reason, instead of asking back the sentence Scout just modelled (red team, D5.14).”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md` (112-113): “silent branch on L4/L6 models a story line and asks its meaning (content-word overlap 1.00/0.80 → 0”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (839): “An escape hatch offered up front stops being an escape hatch.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (840): “~20s (`CFU_UNSURE_MS`), below the tappables, deliberately.”

Against: none found

<sub>context · practice · universal · from g9 · open-question · open · found in [2026-10-12-2-round-1](../research/2026-10-12-2-round-1/), [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### One storyline or sets of texts

Is knowledge better built by one continuous storyline across lessons or by sets of texts on one topic?

A course audit against a meeting's directives agreed only in part with the request for narrative continuity across lessons: building knowledge first is not the same as one forced storyline, and the audit judged sets of passages on one topic the better unit, a push-back to be documented rather than a settled answer. Elsewhere in the same project one unit runs a single story across several lessons, and a simulated review passed it on a criterion for a coherent single-topic text set.

Quoted:

- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (201): “Knowledge-first ≠ a single forced storyline; topic-coherent passage sets are the better unit”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-C-D7-D8-D10-D12.md` (28): “L5 is the second part of a single continuous Peter Pan narrative; the Fantasy Classics unit theme holds.”

Against: none found

<sub>context · sequence, stimulus · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Partial credit for two-part items

Whether a two-part claim-and-evidence item should give credit for a right first part alone, or only when both parts are right. On a published test, the first part alone earns 1, both parts 2 and a wrong first part 0.

A review of an outside measurement project found that the published test scores two-part items with partial credit, the first part alone earning 1, both 2 and a wrong first part 0, and that the project's own binary scorer biased ability estimates; it recommended partial-credit scoring with per-part keys for the reading project's own standard (`grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd`). That project later moved to partial credit (`grade3-reading/knowledge_bot/HOTBUCKET.md`), while a reading app's server scorer and the staged item standard still score a two-part item only when both parts are right (`grade3-reading/knowledge_bot/knowledge/kb-0024-beyond-alpharead-pr45-all-qti-types.qmd`, `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md`). No measured comparison of the two rules was found; to settle it, score the same answers both ways and see which better tracks the published test.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd` (85-88): “**EBSR/Composite = PARTIAL CREDIT (0/1/2)** … Their own MLEF scorer is binary → biases ability. Our standard is SILENT on the scoring model. Action: require polytomous Partial-Credit scoring for EBSR/Composite + per-part answer keys; FAIL binary EBSR scoring.”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (354): “kb-0072's divergences RESOLVED (bank 38→650; EBSR now PCM 0/1/2)”
- `grade3-reading/knowledge_bot/knowledge/kb-0024-beyond-alpharead-pr45-all-qti-types.qmd` (36-37): “**EBSR requires both parts**”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md` (46): “**EBSR** — Part B uses **verbatim** passage sentences as evidence; **both parts** required to score.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/04_CONCURRENT_VALIDITY_PLAN.md` (136): “Our EBSR partial-credit scoring (PCM 0/1/2) is a disclosed deviation from MAP's dichotomous composite rule.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/04_CONCURRENT_VALIDITY_PLAN.md` (138): “the pilot scores every EBSR both ways in parallel — PCM 0/1/2 and dichotomous”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/04_CONCURRENT_VALIDITY_PLAN.md` (139): “the mean absolute linking-residual difference between the two scoring rules, computed on EBSR-heavy sessions (≥3 EBSR items), with a bootstrap 95% confidence interval.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/04_CONCURRENT_VALIDITY_PLAN.md` (140): “- **Criterion:** dichotomous scoring wins if its linking residuals are lower *and* the CI excludes zero; otherwise PCM is retained. The decision is made before RIT output is unlocked, so the shipped RIT transformation is fitted under the winning rule.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/04_CONCURRENT_VALIDITY_PLAN.md` (141): “- **Selection caveat, flagged for item-fit analysis:** the PCM step Δ=0.5 also affects Fisher information and therefore item *selection*, not just scoring — the item-fit analysis will examine whether EBSR selection behavior differs materially between rules.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/01_PSYCHOMETRIC_DESIGN.md` (146): “NWEA's Technical Report states composite items are scored dichotomously (students must answer each part correctly for credit).”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/06_SOURCES.md` (43): “Composite Item (EBSR) partial credit scoring confirmation: Part A only = 1 point, both parts = 2 points.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/06_SOURCES.md` (42): “*NSCAS Growth paper answer keys*”
- `grade3-reading/course-renderer/docs/extras/alpharead-staar-writing-research.md` (147): “**2:** accurate answer AND relevant text evidence. **1:** one part only. **0:** incorrect/blank.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/MAP_PROXY_VALIDITY_CASE.md` (103): “Note that this is a deliberate deviation from MAP: NWEA's Technical Report states that composite items are scored dichotomously (students "must answer each part correctly" for credit).”

Against: A later run found: one package records that the reference test's own technical report scores two-part items all-or-nothing, each part right for credit, and treats its own partial credit as a deviation, its partial-credit confirmation coming from a state test's paper answer keys (`grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/01_PSYCHOMETRIC_DESIGN.md`).

<sub>context · key, format, measurement · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Partial credit from yes-or-no criteria

How should partial credit work when each criterion is judged yes or no, since an answer short of one named detail comes back not met rather than partial? On another build's answer table, 43 answers gave 0 hard fails and 1 soft miss, a partly right answer judged not met for lacking one named detail.

Another build's own answer table was run through its own page code with this engine's judge answering: 43 answers gave 0 hard fails and 1 soft miss. The soft miss was an answer the table rates partial, which came back not met because its criterion named one more detail than the answer gave. Each criterion is put to the judge as one yes-or-no question, so no criterion can be partly met, and the engine's "Part of it is there." line appears only when another criterion surely holds.

Quoted:

- `g9/transformer/v02/QA.md` (54): “43 answers, 0 hard fails, 1 soft miss.”
- `g9/transformer/v02/QA.md` (55-56): “The soft miss: "They argue about how Othello married Desdemona" came back not met where the table wants partial; the criterion asks for "in secret".”
- `g9/transformer/src/mechanics/open-check.js` (100): “Does student_text say requirement_${k}, in meaning?”
- `g9/transformer/src/mechanics/open-check.js` (117): “return missed(`${vs.includes("holds") ? "Part of it is there. " : ""}${item.criteria[k].nudge}`);”

Against: none found

<sub>context · marking, scoring-guide · universal · from g9 · open-question · open · found in [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Practice in the test's format

Whether practice and mastery checks should share formats, or practice should mostly differ from the final test on purpose, with test-format practice saved for the end.

A direct-instruction BrainLift given to the reading course plans says items in mastery tests should match the formats met during instruction (`grade3-reading/ti-courseplans/feedback/feedback1/Direct Instruction BrainLift.md`). The plans' own review gauntlet asks whether early practice looks like the test and answers that it mostly shouldn't: vocabulary in context, monitoring prompts and knowledge work, with test-format practice late and timed conditions last (`grade3-reading/ti-courseplans/skills/train-teacher/references/gauntlet-spec.md`). The alignment plan lists the two as an open tension and proposes a reading under which both hold, familiar formats on unfamiliar passages, still to be confirmed (`grade3-reading/ti-courseplans/docs/academics-alignment-plan.md`).

Quoted:

- `grade3-reading/ti-courseplans/feedback/feedback1/Direct Instruction BrainLift.md` (11): “- You should ensure test items in mastery tests match the formats experienced during instruction.”
- `grade3-reading/ti-courseplans/skills/train-teacher/references/gauntlet-spec.md` (32-34): “does early practice look like the test? (It mostly shouldn't — vocabulary-in-context, monitoring prompts, knowledge work; test-format practice concentrated late, timed conditions last.)”
- `grade3-reading/ti-courseplans/docs/academics-alignment-plan.md` (98-99): “compatible read: format familiarity + passage coldness. Confirm.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (140): “Mastery tests should match formats experienced during instruction.”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (61): “Assessment format is not instruction format (the marathon rule)”
- `grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd` (123-124): “Format familiarity is measurement hygiene, not test prep (construct-irrelevant variance, AERA/APA/NCME Standard 1.13).”

Against: none found

<sub>context · practice, format · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Practice items without a source

Whether questions with no source to read serve practice as well as source-based ones is untested: a judge passed both, but only the source-based form matches the exam. Items stripped of their source passed the AP evaluator on 45 of 50 fresh requests.

A red-team test stripped the source from AP choice questions, and generated items without one passed on 45 of 50 fresh requests, because the evaluator's most punishing checks only run when a source is present; the report credits the lift to the rubric's structure, not the generator's quality (`SECOND_TIER_REASON.md`, line 25; `EXPLOIT-002-stimulus-strip.md`, lines 31-34 and 216-217). The same report notes such items lack the source analysis that is the point of the exam form, while many textbook drills leave sources out for faster recall practice, and the project kept them only as an option for review-drill products (`EXPLOIT-002-stimulus-strip.md`, lines 206-211; `SECOND_TIER_REASON.md`, line 19). Nothing measured what students learn from either form. To settle it: the same objectives practised with and without a source, compared on a later test that has one.

Quoted:

- `icloud-work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/EXPLOIT-002-stimulus-strip.md` (206-208): “The only "tell" is that they lack a primary-source stimulus — which makes them weaker AP-prep than the live exam form (where stimulus analysis is the whole point)”
- `icloud-work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/EXPLOIT-002-stimulus-strip.md` (209-211): “Many textbook drills and formative-assessment items omit stimuli for the same reason (faster recall practice).”
- `icloud-work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/SECOND_TIER_REASON.md` (19): “- **Stem-only review-drill products**: explicit non-exam-format MCQs (no stimulus) for AP-prep practice apps, where the IB grader rubric matches the product shape.”
- `icloud-work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/SECOND_TIER_REASON.md` (25): “- Pass rate 90% (45/50) — partial generalization works on diverse Unit-1 KCs”
- `icloud-work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/EXPLOIT-002-stimulus-strip.md` (31-34): “The IB rubric's most punishing checks — the **educational_accuracy zero-knowledge counterfactual probe** and the **stimulus_quality harm check** — only fire when a stimulus is present.”
- `icloud-work/aptraining/artifacts/second_tier/2026-05-22T1715Z_cheater_exploit_002_stimulus_strip/EXPLOIT-002-stimulus-strip.md` (216-217): “the lift is therefore attributable to a rubric structure — not generator quality.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (274-277): “Under the new contract, every SAQ is sourced: question 1 uses one or more secondary text sources, question 2 uses a primary text source, and question 3 uses a primary or secondary non-text source. The three questions focus on different historical periods.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (284-285): “The legacy local generator allowed source-free SAQs, so the course rejects that behavior.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (46): “That is incompatible with the May 2027 all-sourced SAQ contract.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (46): “No legacy SAQ is accepted by shape alone. Every authored SAQ must carry a verified source and source type.”

Against: none found

<sub>context · stimulus, practice, evidence-of-learning · domain · from ap · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Print all the guide says, or some

Whether everything a lesson's guide says aloud must also be printed is unsettled: printing it all clutters the screen, while a read-along rule allows nothing spoken that isn't printed.

A reading course's index of contradictions records this as undecided: feedback dated 2026-08-06 says not everything the guide says needs to be on screen or it will be cluttered, while the repository's read-along rule, enforced by a validator, allows nothing spoken that is not printed. The course's distilled audio rules take the first side: they print the lines that carry the lesson, leave the rest as audio, and cover the unprinted lines with captions.

Quoted:

- `grade3-reading/artifacts/qc-2026-09-30-staging/contradictions.md` (15): “not everything Scout says needs to be on screen or it will be cluttered. This repo's read-along rule: nothing is spoken that is not printed, enforced by a validator.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/06-AUDIO-NARRATION.md` (59-60): “Not everything Scout says is printed (stamp the load-bearing lines; the rest is audio) — and captions cover the unprinted (below).”

Against: none found

<sub>context · media, wording, accessibility · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Questions during reading or after

Whether checks belong during reading or after is unsettled: tests between parts of a recorded lecture improved recall, but in one study inferential questions during reading cut young readers' recall. In one study, inferential questions during reading cut grade-4 recall from .30 to .07.

A design review of a reading lesson flagged as its biggest cross-lesson implication a published study in which interpolated inferential questions cut grade-4 recall from .30 to .07; the review asked for questions after reading, not during it, and the project logged it as needing a ruling rather than acting alone (`grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd`; van den Broek et al. 2001, https://doi.org/10.1037/0022-0663.93.3.521). In recorded lectures, interpolated memory tests cut mind-wandering by roughly a third and improved recall (`grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd`; Szpunar, Khan & Schacter 2013, https://doi.org/10.1073/pnas.1221764110). The reading figure is for grade 4, and that study varied both grade and timing. To settle it: the same text with checks during and after reading, compared on later recall at more than one grade.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd` (42-43): “interpolated inferential questions cut grade-4 recall .30->.07”
- `grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd` (211-212): “Interpolated memory tests inserted into recorded lectures cut mind-wandering by roughly a third and improved recall versus uninterrupted video.”
- `grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd` (43): “ask AFTER not DURING reading”
- `grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd` (44): “potential class risk for every arc's mid-passage checks including ours”
- `othello-archive/sources/act1/Othello Unit Video - Info Sheet for Devfactory.txt` (28-29): “One idea per segment. Pause-to-check questions after the key segments. A spoken summary at the end.”
- `g9/library/text/L36b8ba.txt` (235): “Love the spot checks across the course of the reading to make sure it’s cohesive, but really cool if kids could listen to it as it’s going through.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/07-SCORING-FEEDBACK-XP.md` (179-180): “Every video carries exactly one quick check, and it fires at the very end, never mid-clip: a video is watched through before it is checked, not interrupted to be checked.”

Published: [van den Broek et al. 2001](https://doi.org/10.1037/0022-0663.93.3.521) · [Szpunar, Khan & Schacter 2013](https://doi.org/10.1073/pnas.1221764110)

Against: none found

<sub>context · sequence, practice · universal · from g3, g9, research · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Quoting a misconception to refute it

Whether lesson text may quote a misconception's wording to refute it, or a misconception screen should fail that wording even inside a correction, is unsettled.

A Grade 5 science misconception gate fails any match of its pinned phrases even when the phrase appears inside a negation, a rejected alternative or a correction, and calls this deliberately stricter than a contextual judgment, so the phrase has to be rewritten before review publication. The red-team taxonomy the reading courses share says to teach random variation first and selection second and to name the misconception ('a sieve, not a sculptor'). Records already here favour refuting a wrong idea, and a word-list check in another project filters negated uses out rather than failing them. Neither rule records an effect on learners.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/docs/SCIENCE_MISCONCEPTION_CHECK.md inside it) (90-92): “Any match fails the bounded content-review gate even when it appears inside a negation, rejected alternative, or correction. This is deliberately stricter than a contextual judgment: the current hard-string policy requires the phrase to be rewritten before review publication.”
- `grade3-reading/ti-courseplans/courses/g5-reading-v2/docs/SCIENCE_MISCONCEPTION_CHECK.md` (90-92): “Any match fails the bounded content-review gate even when it appears inside a negation, rejected alternative, or correction. This is deliberately stricter than a contextual judgment: the current hard-string policy requires the phrase to be rewritten before review publication.”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-main-checkout-jul-work.patch` (20719): “| **Adaptation = genetic choice** | "animals genetically adapt" / "evolved to" | teach random variation FIRST, selection SECOND, name the misconception ("a sieve, not a sculptor"); functional description OK, causal teleology not |”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/MISCONCEPTION-COMPLIANCE-LOG.md inside it) (8): “Intentional misconception-distractors (wrong MCQ options + their refuting feedback) are **excluded by design**”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/MISCONCEPTION-COMPLIANCE-LOG.md inside it) (36): “a negation guard (`not gone` / `never gone` / `not lost`) was added to the allow-list so a correct "energy is **not** gone, it becomes heat" is not falsely flagged”
- `incept-package-hub/course-packages/courses/g5-reading/review/evidence/science-process.md` (90-91): “Any match fails the bounded content-review gate even when it appears inside a negation, rejected alternative, or correction.”
- `incept-package-hub/course-packages/courses/g5-reading/review/evidence/science-process.md` (91-92): “This is deliberately stricter than a contextual judgment: the current hard-string policy requires the phrase to be rewritten before review publication.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/KNOWLEDGE-COHERENCE.md inside it) (180): “Name-and-refute "animals choose/try to adapt."”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/MISCONCEPTION-COMPLIANCE-LOG.md inside it) (21): “a further 5 reintroduced during the teaching-move rework (U4-L6, U5-L4, U5-L7, U6-L1, U6-L2, where the "model-hard-thinking" rewrite voiced a misconception to reject it)”

Against: The strict rule bans a literal phrase, not the idea, so a refutation that names the misconception in other words can pass it. No source compares the two approaches or measures whether a misconception that is voiced and then refuted misleads students.

<sub>context · wording, stimulus · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Reading along with each line lit

Whether a text read aloud with each line lit as it is heard, under one fixed play-pause control, helps readers is untested.

A planned stage of the lesson engine reads the text aloud under one play and pause control fixed at the top, with the text moving under it and each line lit as it is heard (`g9/transformer/v07/README.md`). Nothing of it is built, and no lesson has been reviewed by a person or used by a student (`g9/transformer/README.md`).

Quoted:

- `g9/transformer/v07/README.md` (5): “- Audio-synced reading: one play and pause control fixed at the top, text moving under it, each line lit as it is”
- `g9/transformer/README.md` (120): “No lesson has been reviewed by a person or used by a student.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (410): “Karaoke-style per-word highlighting tested null against no highlighting in children with reading difficulties. This is why audio and synchronized highlighting should be separate decisions rather than one feature.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (97): “Do not pair audio with word-by-word highlighting by default. That is a separate decision.”
- `g9/library/text/L36b8ba.txt` (410): “Karaoke-style per-word highlighting tested null against no highlighting in children with reading difficulties. This is why audio and synchronized highlighting should be separate decisions rather than one feature.”

Against: none found

<sub>context · media, accessibility · universal · from g9 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Reasoning or score

Whether a judge's own reasoning should overrule its failing score is unsettled, since an item's explanation might steer that reasoning toward a pass.

The judge's instructions include an anti-contradiction step: when its reasoning concludes the content is correct but a score is 0.0, it must change the score to 1.0. An adversarial reading argues that because the judge writes its reasoning before the score is applied, an item explanation templated to read as correct can force a score of 1.0, and proposes letting the rule fire only between the overall score and the individual metrics. No run in the files read isolates the rule's effect. To settle it: score the same items with and without the per-metric rule, against verdicts a person has checked.

Quoted:

- `icloud-work/aptraining/Cheater/reports/RUBRIC_BLINDSPOTS.md` (51-55): “But because the judge writes reasoning BEFORE the score is applied, a template-driven explanation that prefills the judge's reasoning toward "content is correct" will force the score to 1.0 even when the judge's gut would have failed it.”
- `icloud-work/aptraining/Cheater/reports/RUBRIC_BLINDSPOTS.md` (58-60): “**Patch:** the self-heal rule should fire ONLY in the overall-score-vs-individual-metric direction (the original intent), not in the per-metric direction.”
- `icloud-work/aptraining/Cheater/reports/DEAD_HYPOTHESES.md` (9-10): “Result: 4/10 = 40% pass vs. 2/2 = 100% on the no-stimulus control on the same content.”

Against: Items that carried the mirror-style explanation the reading blames, under an authority-framed source, still passed only 4 of 10, so the explanation alone did not force passes: "Result: 4/10 = 40% pass vs. 2/2 = 100% on the no-stimulus control on the same content." (icloud-work/aptraining/Cheater/reports/DEAD_HYPOTHESES.md, 9-10)

<sub>context · evaluation, integrity · universal · from ap · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Recap or recognition in later parts

A film before a later part can recap earlier parts or only show how the place now stands: one rule bans recaps, another says recaps consolidate and reveal nothing.

One version of the intro-video rules says that when a later video must make the child remember, it shows the place as it now stands and never says what happened there (`downloads/BrainLift - What makes a good intro video.md`, line 63). The other has a later part's video recap the earlier one, since nothing in a part the child has read can spoil the next: "Recapping consolidates; it does not reveal" (line 297). The same passage adds that after the first unit, multi-part texts can begin with retrieval instead of a recap (line 297), and a produced outline for a story's second part opens with a recap (`downloads/5. Curriculum/Texts/G3/Grade 3 markdown/01 - Fantasy Classics/01 - Aladdin and the Wonderful Lamp/Video Outline - Aladdin and the Wonderful Lamp Part 2.docx`, line 3).

Quoted:

- `downloads/BrainLift - What makes a good intro video.md` (63): “When a later video must make the child remember, show the place as it now stands and never say what happened there.”
- `downloads/BrainLift - What makes a good intro video.md` (297): “Recapping consolidates; it does not reveal.”
- `downloads/BrainLift - What makes a good intro video.md` (297): “However, after unit 1, multi-part texts can shift to begin with retrieval instead of recapping.”
- `downloads/5. Curriculum/Texts/G3/Grade 3 markdown/01 - Fantasy Classics/01 - Aladdin and the Wonderful Lamp/Video Outline - Aladdin and the Wonderful Lamp Part 2.docx` (3 (textutil text)): “Last time, Aladdin was tricked by a magician pretending to be his uncle.”
- `downloads/BrainLift - What makes a good intro video.md` (62): “Nobody has tested recognition against recap, on a story told in parts, for a child who has forgotten the earlier one”
- `grade3-reading/artifacts/video-briefs/PETER-PAN-BRIEF-RECONCILIATION-2026-08-31.md` (34): “A summary of the past leaks the future. Choosing which three moments to repeat tells the child which threads are about to matter.”

Against: The first version admits that nobody has tested recognition against recap, on a story told in parts, for a child who has forgotten the earlier one (`downloads/BrainLift - What makes a good intro video.md`, line 62).

<sub>context · media, sequence · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Recap the example or the task

Whether a recap offered during independent practice should restate the worked example, signposted as the example, or describe the learner's current task is unsettled. In one scan, 5 of 7 recaps in two lessons gave no sign that they described the worked example rather than the learner's own question.

A cross-field scan of two Grade 3 lessons found every recap accurate to the worked example it summarised, but the hint's label gave a struggling child no sign that it was about a different character and place from the question on screen, so the child could take it for a hint about their own answer. The scan called this a labelling question, suggested signposting the recap as the example, and routed it for a ruling without changing anything. A later repair took the other route and replaced the carryover recaps in two lessons with summaries of the current task's own material.

Quoted:

- `grade3-reading/artifacts/signoff-packet/CROSS-FIELD-SCAN-2026-08-31.md` (99-102): “A child who taps the hint mid-task, without holding the "watch me think" page in memory, will read "gloomy, miserable, strict" or "Lost Boys... gentle, lonely" while looking at a Neverland/Hook question and can easily mistake it for a hint about their OWN answer”
- `grade3-reading/artifacts/signoff-packet/CROSS-FIELD-SCAN-2026-08-31.md` (103-104): “This is a UX/labeling question (should the recap open with "On my London example, I..." or similar signposting)”
- `grade3-reading/artifacts/signoff-packet/CROSS-FIELD-SCAN-2026-08-31.md` (106-108): “(5 of 7 teacher_recap instances in the scanned lessons; L4/p22 and p22d already open with unambiguous topic framing or are place-agnostic)”
- `grade3-reading/artifacts/qc-2026-09-29-staging/ADJUDICATION-pr662.md` (16): “Replaced carryover London/Lost Boys summaries with the current Neverland/Hook fit-word summaries.”

Against: The risk the scan named is predicted, not observed with a child (`grade3-reading/artifacts/signoff-packet/CROSS-FIELD-SCAN-2026-08-31.md`, lines 96-105), and another record keeps such recaps on the worked example's own material.

<sub>context · hints, practice · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Restraint with violence when no adult is present

Whether a self-paced lesson with no adult present should handle violence more cautiously than adult-led editions, with one warning line, brief reporting and no picture, awaits a ruling. One classroom magazine prints four lines of detail for eight and nine year olds where the proposal prints one sentence.

Lesson research for a grade 4 reading lesson compared what published children's versions of a violent episode print, and found that mainstream material for younger children prints far more than expected, but in settings that have an adult in the room, or a briefed adult and a letter home. For a self-paced app with neither, it recommends one guide line before the passage and restraint in the printed text, each violent act given in one clause or one action and its result with no description, and no image, since a picture is not read aloud, cannot be paced and cannot be argued about with no adult present. The lesson plan records this as a proposal that needs sign-off.

Quoted:

- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (795-798): “Recommendation: **one guide line before the passage, and restraint in the printed text**, sitting deliberately below what Storyworks prints for a younger child, because Storyworks has a teacher in the room and CKLA has a briefed adult and a letter home, and we have neither.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (815-817): “No image of the blinding, notwithstanding the Getty using a Greek vase of it with elementary classes. A picture is not read aloud, cannot be paced, and cannot be argued about in an app with no adult present.”
- `grade3-reading/course-renderer/content/lesson-plans/g4-u1-l2.json` (518): “The proposal, recorded so the sign-off has something concrete to accept or reject rather than a principle.”
- `grade3-reading/course-renderer/content/lesson-plans/g4-u1-l2.json` (517): “"status": "needs sign-off"”
- `grade3-reading/course-renderer/content/lesson-plans/g4-u1-l2.json` (516): “So printing less than they do is a departure from precedent and has to be argued, and the argument is about the setting rather than about the content.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l2-the-cyclops.md` (795-797): “Recommendation: **one guide line before the passage, and restraint in the printed text**, sitting deliberately below what Storyworks prints for a younger child”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l2-the-cyclops.md` (807-808): “The eating: reported in one clause, with no description of the men and no simile.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l2-the-cyclops.md` (816-817): “A picture is not read aloud, cannot be paced, and cannot be argued about in an app with no adult present.”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l2.json` (516): “mainstream material for younger children prints far more than expected”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l2.json` (516): “Storyworks prints four lines of detail about the blinding for eight and nine year olds”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l2.json` (516): “So printing less than they do is a departure from precedent and has to be argued, and the argument is about the setting rather than about the content.”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l2.json` (517): “needs sign-off”

Against: Printing less than mainstream editions departs from precedent: "So printing less than they do is a departure from precedent and has to be argued, and the argument is about the setting rather than about the content." (`grade3-reading/course-renderer/content/lesson-plans/g4-u1-l2.json`, line 516). The lesson plan calls printing less than published precedent "a departure from precedent" that "has to be argued", the argument being about the setting rather than the content, and its status is "needs sign-off" (`othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l2.json`, lines 516-517).

<sub>context · stimulus, media · domain · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Slurs nearby and the clean-line check

Does a slur elsewhere in the passage a judge is shown lower its confidence that a clean line is free of slurs? A clean quotation from a play whose passage carries slurs scored 0.75 and 0.80, against 0.98 to 0.99 for quotations from texts without one.

The worked model's clean-line check asks a judge whether the quotation is free of any racist or sexual slur or epithet, while the state the judge is shown also carries the whole passage. On a clean quotation from a play whose passage contains slurs, the judge answered 0.75 and 0.80 across two drafts; on quotations from a poem and a speech without one, it answered 0.98 to 0.99. The question names only the quotation.

Quoted:

- `g9/transformer/src/mechanics/util.js` (109): “Is ${field} free of any racist or sexual slur or epithet?”
- `g9/transformer/src/mechanics/worked-model.js` (108): “cleanLine("quote"),”
- `g9-transformer-runs/decisions/b9cb3d0f3a8639c0.json` (20): “"passage": "Tush! never tell me; I take it much unkindly”
- `g9-transformer-runs/decisions/b9cb3d0f3a8639c0.json` (22): “"quote": "I follow him to serve my turn upon him",”
- `g9-transformer-runs/decisions/b9cb3d0f3a8639c0.json` (360): “"value": 0.75,”
- `g9-transformer-runs/decisions/b9cb3d0f3a8639c0.json` (728): “"value": 0.8,”
- `g9-transformer-runs/decisions/68d85cc9b79fb956.json` (360): “"value": 0.98,”
- `g9-transformer-runs/decisions/68d85cc9b79fb956.json` (728): “"value": 0.99,”
- `g9-transformer-runs/decisions/be97f27fc4c4a65a.json` (356, 730): “"value": 0.98,”
- `g9-transformer-runs/decisions/be97f27fc4c4a65a.json` (1102): “"value": 0.99,”

Against: There are only two judgings of one quotation, confounded by text, and the quotation's own wording may read as hostile.

<sub>context · evaluation, integrity · universal · from g9 · open-question · open · found in [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Stage names a learner sees

Whether showing learners an ability-stage name such as beginner leads them to act like beginners is unsettled and unchecked against the research on ability labelling. One Grade 3 design asks this of a child told they are a beginner for sixteen units.

A Grade 3 reading lesson design lists naming its stages as one thing to settle before it is built: beginner, intermediate and expert is the obvious set, but a child told they are a beginner for sixteen units may behave like one (`g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx`, lines 112-113). It asks for a look at the research on ability labelling before any name is put on screen.

Quoted:

- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (112): “One thing to settle before this is built.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (113): “Beginner, intermediate and expert is the obvious set and it is the one to be careful with”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (113): “a child who is told they are a beginner for sixteen units may behave like one. This needs a look at the research on ability labeling before anything is put on screen”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (19): “Three stages: Stage 1 (beginner), Stage 2 (intermediate), Stage 3 (expert).”
- `g9/library/text/L8d5159.txt` (113): “Beginner, intermediate and expert is the obvious set and it is the one to be careful with: a child who is told they are a beginner for sixteen units may behave like one.”
- `g9/library/text/L8d5159.txt` (113): “This needs a look at the research on ability labeling before anything is put on screen”
- `g9/library/text/L9b6d99.txt` (19): “Three stages: Stage 1 (beginner), Stage 2 (intermediate), Stage 3 (expert). Each lesson has a learning question for each stage.”

Against: A Grade 9 lesson design specification names its stages beginner, intermediate and expert without saying whether learners see the names (`g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md`, line 19).

<sub>context · wording, sequence · universal · from g3, g9 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Stated difficulty against real students

Whether an item's stated difficulty matches how real students do on it is untested: a plan to compare the label with the share answering correctly has no results yet.

A strategy report for a teach-then-test loop proposed storing real-world difficulty, the share of students who answer correctly, against generated questions, and registering a difficulty mismatch when, for example, an item labelled medium has a p-value of 0.20 (`aptraining-local/analyzer/.lanes/teaching-benchmark/STRATEGY_REPORT.md`, line 33). It names released statistics or the app's own telemetry as the data (line 32). In this work difficulty is an input the writer is asked to meet (`icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md`, line 42), and no student results appear in the sources. To settle it: give generated items to students and compare each label with the share who answer correctly.

Quoted:

- `aptraining-local/analyzer/.lanes/teaching-benchmark/STRATEGY_REPORT.md` (33): “- **P-Value & Point-Biserial Mapping:** Store real-world question difficulty (p-value) against generated questions. If a generated "Medium" question has a real-world p-value of 0.20 (Hard), we register a `difficulty_misalignment` failure.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq.md` (42): “- `difficulty`: `{{difficulty}}` (easy/medium/hard — interpreted per curriculum)”

Against: Proposals only; no student data or measured result appears in the sources.

<sub>context · demand, measurement · universal · from ap · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Stills or motion

Stills or motion: in some studies still pictures with printed text teach as well as narrated animation, but across many, animation wins on average.

Finding 1 of the film study (`othello-unit-video/research/FINDINGS.md`): static diagrams with printed text did as well
as narrated animation or better on 4 of 8 comparisons (Mayer et al. 2005, https://doi.org/10.1037/1076-898X.11.4.256),
but across 26 studies animation beat still pictures on average (Höffler & Leutner 2007,
https://doi.org/10.1016/j.learninstruc.2007.09.013), and on my own per-shot test an animated version matched its
narration for more of its screen time, 51% to 41%. To settle it: the same script and voice over stills and over
realistic video, compared on first-try answers to the same checks.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0202-g9-othello-video-research-fake-ai-attention.qmd` (36): “Moving, speaking synthetic humans still read as fake.”
- `grade3-reading/knowledge_bot/knowledge/kb-0202-g9-othello-video-research-fake-ai-attention.qmd` (37): “Still AI faces are now indistinguishable from real ones”
- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md` (21): “**Design conclusion:** avoid slow letter tracing that obstructs reading; chunked reveal is a reasonable prototype.”
- `grade3-reading/artifacts/wiki-research/cross-cutting.md` (141): “This is a genuine, load-bearing tension”
- `grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd` (508-509): “switching static images as defensible, not proven-superior**, to video on learning grounds alone.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md` (38): “12. Animate ONLY genuine motion/process (procedural animation can win up to d≈1.06; loses to statics when transient).”
- `grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md` (108): “Test: replace the motion with a still of the end state — does the student lose something essential?”
- `grade3-reading/ti-courseplans/docs/academics-alignment-plan.md` (102-103): “3. **DI video-first vs Generic Instruction "default to text" (§20)** — their docs disagree; ask which governs reading.”
- `g9/transcript/chat-transcript.redacted.txt` (5560): “to have more details in the photoes, not the videos”
- `g9/transcript/chat-transcript.redacted.txt` (5585): “Use a few richly composed panels, giving students time to inspect expressions, relationships and setting. Advance between panels rather than continuously animating them.”
- `g9/transcript/chat-transcript.redacted.txt` (5963): “The target is a cinematic, narrated comic sequence with still artwork, not panels the student has to read through manually.”
- `g9/transcript/chat-transcript.redacted.txt` (6498): “an illustrated book brought to life through voiceover”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-visuals-human-v0.1.md` (134-136): “**Evidence.** Animation beats static imagery by *d*=0.37 overall, with representational animation at *d*=0.40, realistic/video at *d*=0.76, and procedural-motor content at *d*=1.06; decorational animation is *d*=-0.05 [8].”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-visuals-human-v0.1.md` (264): “Route structure, parts, and comparison to progressive static diagrams; route process, transformation, and causal chains to representational animation; route real appearance to realistic footage.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-visuals-human-v0.1.md` (336): “Animation superiority is conditional: it helps when motion carries content and can hurt when transience or decoration dominates”
- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/idea-03-comic-static-images-with-voice.md` (93-94): “a 2025 study found animated slides + voiceover did **not** beat static slides + same voiceover when visuals had clear reading conventions.”

Published: [Mayer et al. 2005](https://doi.org/10.1037/1076-898X.11.4.256) · [Höffler & Leutner 2007](https://doi.org/10.1016/j.learninstruc.2007.09.013)

Against: A later run found counter-evidence (`grade3-reading/ti-courseplans/docs/academics-alignment-plan.md`).

<sub>context · media · universal · from g9, research · open-question · open · found in [2026-10-12-2-round-1](../research/2026-10-12-2-round-1/), [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Swap a cultural word or gloss it

Whether to replace an unfamiliar, culturally specific word in a traditional tale with a familiar one, or keep it and gloss it, is unsettled.

Curriculum feedback on a Grade 3 lesson built on a West African folktale asked in one place for folktales to carry the customs of a people, and in another for the tale's culturally specific word to be replaced with a familiar one. The course team recommended keeping the word and glossing it, since the word belongs to the source and an unfamiliar concrete noun with a synonym in the sentence suits the word-solving routine the course must teach. It put the point to a ruling as a judgement call; a later course record implies every requested change was made, and nothing tested which choice serves readers.

Quoted:

- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-4/feedback-on-iteration-4/feedback-0806-pedagogy.md` (291): “The document asks in one place for folktales to carry the customs of a people and in another to remove the culturally specific word. Our recommendation is keep-and-gloss (see the verdict table).”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-4/feedback-on-iteration-4/feedback-0806-pedagogy.md` (48): “"gourd" is specific to the West African source”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-4/feedback-on-iteration-4/feedback-0806-pedagogy.md` (48): “An unfamiliar concrete noun with an in-sentence synonym is the *ideal* case for the word-solving routine we are required to teach (D4.19), not a hazard to remove.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-4/feedback-on-iteration-4/feedback-0806-pedagogy.md` (48): “it is a judgement call, not a rule.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/resources/extracts/distill_player.md` (66): “Make all the changes they have requested - no exceptions”

Against: none found

<sub>context · stimulus, wording · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Take a side before or after reading

Whether learners should commit to a position before reading and then test it, or only after reading with their marked lines in view, is unsettled. Two design canvases have learners take a side before reading, while the built prototype asks for it only after reading.

Successive Grade 9 design directions disagree. One canvas has the student make a call before reading and then read to test it, tracking a change of mind as strength, and the canvas the design index marks current opens with taking a side before reading. The built prototype shows the question only as something to keep in mind while reading, lets nobody pick a side yet, and asks for a side after reading, with the marked lines in view. No source compares the two orders with learners.

Quoted:

- `othello-course-renderer-draft/repo/docs/design/grade-9/canvases/02-case-files.html` (47): “The student commits, then reads to test it. Changing your mind is tracked as strength.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/canvases/03-desktop-othello.html` (38): “Position: take a side before reading”
- `othello-course-renderer-draft/repo/docs/design/grade-9/README.md` (32): “Desktop first (1366×640 HD Chromebook, 1180×760 landscape iPad); Othello 3.3 | **Current**”
- `othello-course-renderer-draft/repo/docs/design/grade-9/prototype/README.md` (27): “The question shows as "Keep in mind"; nobody picks a side yet.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/prototype/README.md` (28): “4. **Pick a side**, after reading, with the marked lines in view.”

Against: none found

<sub>context · sequence, demand · universal · from g9 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Teaching procedures run as rulesets

Whether a lesson that adapts at each student action within written rulesets, for reading sequences and for procedures such as comparative judgement and faded non-examples, helps readers is untested. Of three procedures planned as rulesets, two already have a block and the faded non-example has none.

A planned stage of the lesson engine would run procedures as rulesets, among them full modelling, comparative judgement and faded non-examples, and reading sequences from first-read checks through close reading and analysis to writing, with the judge deciding sequencing, hints and escalation at each action within those rules (`g9/transformer/v05/README.md`). Its exit criterion is sequencing measured with scripted readers before any student sees it. Today a worked-model block and a compare-two-answers block exist, no faded non-example does (`g9/transformer/v04/README.md`), and none of it runs as a ruleset.

Quoted:

- `g9/transformer/v05/README.md` (7): “- Adaptive sequencing, hints and escalation, decided by Jev at each action within rules.”
- `g9/transformer/v05/README.md` (8): “Procedures as rulesets: full teacher modelling, comparative judgement and faded non-examples”
- `g9/transformer/v05/README.md` (9): “reading sequences (first-read checks, close reading, analysis, writing)”
- `g9/transformer/v04/README.md` (11): “- **Judge:** compare two answers ✓, faded non-example, rank the evidence.”
- `g9/transformer/README.md` (47): “follows a quotation unpicked, rebuilds one sentence, then reads the model paragraph”
- `g9/transformer/v05/README.md` (12): “**Exit criteria:** sequencing measured with personas before any student sees it.”

Against: none found

<sub>context · sequence, practice · universal · from g9 · open-question · open · found in [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### The same lesson in different players

Whether one lesson gives comparable results in different players is open, since a block can become a different task in each and be marked by different rules. An animated version's export sets three tries by default, two on its open check and debate, and one for each word added to its word web.

Reading how two players and the lesson engine's own view draw the same blocks found that a quick check, a choice in an animated version, is asked open in a 3D version, and that an evidence hunt, a tap on a line in the engine's view, becomes a written quotation in both players (`g9/transformer/src/glue`; `g9/transformer/web/lesson.js`). Their marking adapters differ too: the number of tries, whether earlier tries count, and what an unsure judge does, which is an offline case in one player, a could-not-check line in the other and pending in the engine's view (`g9/transformer/v02/QA.md`). No single rule set across players is in place.

Quoted:

- `g9/transformer/src/glue/threejs-render.js` (7): “a reading checkpoint, asked open: the options go, the right one is what a secure answer shows”
- `g9/transformer/src/glue/animated.js` (3): “a reading page's quick multiple-choice checks (ReadingMcq)”
- `g9/transformer/web/lesson.js` (260): “Tap the line in the text, on the left.”
- `g9/transformer/src/glue/threejs-render.js` (8): “a reading checkpoint: which words show the claim, quoted (settled on the quotation in code)”
- `g9/transformer/src/glue/animated.js` (5): “a reading page of its own (ReadingNode) whose written check asks for the words”
- `g9/transformer/src/glue/animated.js` (68): “source, max_tries: 3, criteria, misreadings: [], lines:”
- `g9/transformer/src/glue/animated.js` (113): “{ max_tries: 1 }”
- `g9/transformer/src/glue/animated-judge.js` (83): “Taking answer together with earlier_answers, does the student say this, in meaning (any wording counts)”
- `g9/transformer/src/glue/threejs-archivist.js` (130): “Taking answer on its own, does the student say this, in meaning? Any wording counts, and a short answer that says it is enough:”
- `g9/transformer/v02/QA.md` (127-129): “in the 3D build it is its own offline case (not an attempt, the answer kept), in the animated build's pages the student is told it could not be checked (its generous word web takes the word), in our view it stays pending.”
- `g9/transformer/src/glue/animated.js` (42): “two tries, then the answer (the 3D build's release rule), for the written checks this file adds”

Against: The written checks the animated export adds do follow the 3D version's release rule of two tries, then the answer (`g9/transformer/src/glue/animated.js`, line 42).

<sub>context · measurement, format, marking · universal · from g9 · open-question · open · found in [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### The second check on a taught word

Whether a taught word's second check should be another usage item or give the meaning and ask which word fits, testing knowing in the other direction, is unsettled. Three built lessons swapped the design's second usage item for one that gives the meaning and asks for the word.

A reading unit's designs gave each taught word two usage items, the second as a second chance and a clean measure (`grade3-reading/artifacts/pp2-v3-design.txt`, line 54). The built lessons replaced the second with an item that states the meaning and asks which word says it, under a build-spec ruling that the two forms must do different jobs: the first tests recognising the word used correctly in a real situation, the second going from the definition back to the word (`grade3-reading/artifacts/screen-narratives/L6-NARRATIVE.md`, lines 125-130). Conformance audits recorded the swap in three lessons, and one called it an authored, self-documented adaptation of the same construct (`grade3-reading/artifacts/arc-audit/L5.md`, line 21; `grade3-reading/artifacts/arc-audit/L6.md`, line 139; `grade3-reading/artifacts/arc-audit/L7.md`, line 32).

Quoted:

- `grade3-reading/artifacts/arc-audit/L7.md` (32): “Doc's Form 2 is a second usage-discrimination sentence (knight/dragon). Delivered Form 2 (`vocab-form2`) is a definition-recall MCQ ("You win a great victory after a hard struggle. Which word says that?").”
- `grade3-reading/artifacts/arc-audit/L6.md` (139): “Form 2 changed from usage to definition-recall per spec's "two different jobs" ruling”
- `grade3-reading/artifacts/screen-narratives/L6-NARRATIVE.md` (129-130): “Form 2 tests whether the child can go from the definition back to the word — two different directions of knowing.”
- `grade3-reading/artifacts/arc-audit/L5.md` (21): “This is an authored, self-documented adaptation, not a silent drift — **defensible**, same assessed construct (word meaning) via a different item shape.”
- `grade3-reading/artifacts/pp2-v3-design.txt` (54): “FORM 2 (second chance / clean measure) — Stem: Which sentence uses the word menacing correctly?”

Against: Two rules on record would bar the meaning-to-word form: a question on a taught word must never define the word in the question (Don't define the word being tested), and a check must put the word in a new situation (Test a taught word somewhere new). Within the course a ruling settled it for the built lessons: "two vocab forms must do DIFFERENT jobs." (`grade3-reading/artifacts/screen-narratives/L6-NARRATIVE.md`, lines 127-128).

<sub>context · demand, format, evidence-of-learning · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### The taught word in closing questions

Should a lesson's closing questions make students use the word it taught, or only the language of the concept it built?

An AI review of one lesson's closing questions raised it as a question rather than a defect: the sequence worked only in the concept's language, and the taught word came back only in a later cloze and the end-of-lesson receipt. Four other lessons had the same shape, asking for the taught word only through a prompt to use today's word in the retell and the closing cloze, and the design pattern's own wording reads either way. The pattern also asks for one push for the taught word before weaker language is accepted, but the rubrics had no push mechanism; the register left the question for a ruling.

Quoted:

- `grade3-reading/artifacts/feedback-closing-questions-2026-09-24/REGISTER.md` (60): “does the closing sequence have to make the child USE THE TAUGHT WORD, or is the reading-goal concept language the only target?”
- `grade3-reading/artifacts/feedback-closing-questions-2026-09-24/REGISTER.md` (51): “Vocabulary floor: one push before accepting weaker language”
- `grade3-reading/course-renderer/docs/handover/closing-questions/HANDOVER.md` (114-119): “**The taught word is prompted, never required (every lesson).** One slot's ask ends "Can you use the word X?" with one of the lesson's taught words (L1: "Now, when was it broken? Can you use the word betrayal?"), and that slot's rubric says the word is "welcome and never required": an answer without it that meets the rest passes, and the word alone with no story moment does not.”
- `grade3-reading/course-renderer/docs/handover/closing-questions/HANDOVER.md` (119-120): “`validate-contracts.mjs` (`checkClosingFrameTaughtWord`) fails a closing Find it here frame that lacks either.”
- `grade3-reading/course-renderer/docs/extras/alpharead-lesson-design-witw-part-1.md` (428): “**Special / "magic" word requirement:** the answer must contain the taught word **"eerie"** (tested with `/eerie/i`).”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md` (137-138): “row E1 (does the closing sequence have to use the TAUGHT word?).”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/generated/feedback-2026-08-11-crosswalk.json` (363): “Design the final question to create a genuine opportunity to use the focal vocabulary.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/01-NON-NEGOTIABLES.md` (216-218): “**Wrap retell requires a lesson word** (2026-08-17): the prompt names them (trickster, cunning, outwit) and the grade deterministically requires ≥1 (any inflection), capped below full credit otherwise”
- `othello-archive/src/content/close.ts` (149): “Do not require the word "dramatic irony" or the promotion.”
- `othello-archive/server/tasks/threads.mjs` (30): “they must use one, or a form of one, e.g. "deceives" for "deceitful"”
- `othello-course-renderer-draft/repo/docs/handover/closing-questions/HANDOVER.md` (114-119): “**The taught word is prompted, never required (every lesson).** One slot's ask ends "Can you use the word X?" with one of the lesson's taught words (L1: "Now, when was it broken? Can you use the word betrayal?"), and that slot's rubric says the word is "welcome and never required": an answer without it that meets the rest passes, and the word alone with no story moment does not.”
- `grade3-reading/artifacts/arc-audit/PRE-WEEKEND-SMOKE-2026-08-28.md` (102-103): “**Retell criteria** `uses-merciless` (L6) and `uses-triumphant` (L7) — both confirmed to reference the actual vocab word taught earlier in the same lesson”

Against: none found

<sub>context · alignment, demand · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### The text's word or the taught word

Open: when pushing a student toward a stronger word, whether to push for the source text's own word or for the lesson's taught word when the text never uses it. On one course's staging content, all seven word pushes the check flagged were taught words the story never uses.

A content audit's closing-question checks ask whether a pushed word is genuinely stronger and the text's word rather than the lesson's (`shadow/content-eval/SKILL.md`). On staging all seven pushes the check flagged were taught words the story never uses, which departs from the specification's call for the stronger word the text supplies, so the check reports them as information until the choice is made. Nothing measured which push teaches better.

Quoted:

- `shadow-content-eval/SKILL.md` (203): “It is `info` for Word Power words, because on staging all seven hits are taught words the story itself never uses.”
- `shadow-content-eval/SKILL.md` (359): “**Is the pushed word genuinely stronger** than the likely child answer, and is it the text's word rather than the lesson's?”
- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L7-2026-09-05.md` (113-114): “p16 step3 type blank uses `magic_word` gate with fuzzy synonym detection ("victorious", "winning" etc. trigger coaching toward the target word)”

Against: none found

<sub>context · hints, wording · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Three options or four

Should a choice question default to three options, as research favours, or include the extra option a course review asked for?

The assessment packet records the tension: a review asks for at least four options, while the multiple-choice evidence summary says research generally favours three and keeps four as the default only when a third plausible, diagnostically useful wrong option exists (`grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md`). The packet bars filling a fourth slot with an implausible option and leaves the default to a human decision (the same file; `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/README.md`). A meta-analysis of 80 years of research found three options optimal (Rodriguez 2005, https://doi.org/10.1111/j.1745-3992.2005.00006.x). To settle it: decide the default, then count how often students choose each fourth option. Either way, no slot is filled with an implausible option, since a weak option only adds cues (`grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md`, line 2006).

Quoted:

- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md` (40-42): “The MCQ BrainLift says the research consensus generally favors three options and recommends four as Alpha's default only when a third plausible, diagnostically useful distractor exists. Do not fill a fourth slot with an implausible option.”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/README.md` (94): “decide the three-versus-four-option MCQ policy when a fourth plausible distractor cannot be written;”
- `grade3-reading/knowledge_bot/knowledge/kb-0241-alpha-read-contract-investigation-and-packager-build-2026-06.qmd` (109): “arpack's "exactly 4 choices" gate over-restricts vs the API's real 2-6+ floor”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (2006): “The discipline: if you cannot write a third plausible distractor for a given item, use three options rather than adding filler. A weak fourth distractor is worse than no fourth distractor because it provides testwiseness cues and wastes time.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (2082): “Most items cannot sustain more than two plausible distractors; the third and fourth distractors in 4- and 5-option items are typically non-functioning (selected by fewer than 5% of examinees).”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (2083): “First, four options reduce the guess rate from 33% to 25%”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0164-g3-v2-feedback-agent-routing.qmd` (102-105): “while the MCQ BrainLift reports a research consensus favoring three and recommends four as Alpha's default only when all distractors remain plausible and diagnostically useful. An agent must not resolve this by adding filler”
- `grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md` (52): “**MCQs need ≥4 options.** A 2-option yes/no is a 50/50 guess.”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (770): “Claim boundary: No fixed option count belongs in the universal standard.”
- `grade3-reading/course-renderer/scripts/validate-contracts.mjs` (366): “mcq must have exactly 4 options”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “validate-contracts.mjs line 365 requires exactly 4 MCQ options.”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “Its validators reject three-option MCQs and Grade 9 copy, so build without them.”
- `g9/transformer/src/mechanics/quick-check.js` (1): “three options, exactly one defensible.”
- `g9/transformer/src/mechanics/quick-check.js` (23): “Exactly three options. Exactly one is right given the text”
- `g9/transformer/src/mechanics/direct-the-line.js` (39): “deliveries must be a list of three”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (600): “Four options. Not two, not three.”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (619-620): “- **Default option count:** 4 - **Three-option exception:** Use three options only when an independent cold review finds that a fourth misconception- or error-grounded distractor cannot be written without filler, cueing, or ambiguity; record reviewer, reason, and candidate fourth option rejected.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/evidence/case-for-review.md` (85): “Four options are the default and three require a recorded no-filler exception after independent cold review.”
- `grade3-reading/edullm-review-hub/course-packages/quality/golden-student-course/versions/1.0.0/STANDARD.qmd` (770): “No fixed option count belongs in the universal standard.”
- `grade3-reading/artifacts/sim-review-2026-09-24/CLOSURE-PLAN.md` (128): “Neither is a summative MCQ; the four-option rule applies to the mastery pool.”
- `grade3-reading/ti-courseplans/courses/g5-reading-v2/docs/BRAINLIFT.md` (248): “| Option count | Four by default; three only with documented independent exception |”
- `incept-package-hub/course-packages/courses/g5-reading/review/evidence/case-for-review.md` (85): “Four options are the default and three require a recorded no-filler exception after independent cold review.”

Published: [Rodriguez 2005](https://doi.org/10.1111/j.1745-3992.2005.00006.x)

Against: A packager gate that demanded exactly four options was found to over-restrict a delivery format whose real floor is 2-6+ (`grade3-reading/knowledge_bot/knowledge/kb-0241-alpha-read-contract-investigation-and-packager-build-2026-06.qmd`). The course-quality standard declines to fix a number: "No fixed option count belongs in the universal standard" (`grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd`, line 770).

<sub>context · options, distractors · universal · from g3, research · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Three or four blanks in a retell

How many blanks a fill-in-the-blank retell should have is unsettled, since a component specification and a later procedure document set different counts. One component specification sets exactly four blanks, while a later procedure document sets three core words and never blanks the taught word.

The curriculum's lesson-component specification makes the summary after the read-aloud a compressed, causal retell with exactly four blanks on the links in the child's mental model, with the taught word featuring in it. An updated procedure document sets three core words, verbatim and tapped in order, with the taught word never blanked, and a dated ruling chose it over the named designs, after which a three-word cloze was built into four lessons. Another lesson's instruction blanks the taught word in a closing sentence, an exception to the document the three-word ruling rests on, and the three-or-four question was left to ride with the next branch. Whether the taught word may be one of the blanks is a second open question.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/HUMAN-g3r-2026-07-27T08-38-36-019fa24b-fb42-7e61-a954-216db3ef77a4.md` (1108): “It is a compressed, causal retell of the story with exactly four blanks that sit on the links in the child's mental model — so it checks that the child has followed the flow of the story, not incidental detail. The taught word features in it”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md` (262): “cloze 'Three core words, verbatim, tap in order. Taught word never blanked'”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md` (264): “to supersede named L6/L7 FIND and cloze designs”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md` (264): “three-word cloze (new `cloze` bank_type; L4 p13, L5/L6/L7 p11b)”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md` (326): “blanks the taught word in a closing sentence — a dated exception to the doc rule your three-word cloze ruling rests on.”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md` (374): “the L7 rows 16/18 and the cloze 3-vs-4 question ride with it.”

Against: A dated ruling chose the three-word form for four lessons (`grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md`, line 264), so for those lessons the count is settled; the taught-word question and the rest of the course are not.

<sub>context · format, key · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Trusting learners' own reports

How far can learners' own reports of what they know be trusted for routing their study? About 80% of students check a word as known, about 50% can give an example and about 20% can explain it.

The diagnostic BrainLift calls self-report the cheapest, fastest and most underused signal in diagnostic assessment, and in a low-stakes mastery setting would use it to set starting estimates that item responses then update (`grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md`). The reading-science synthesis quotes a 2002 research report finding that most child and adult readers calibrate the success of their comprehension poorly (`grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd`). The reading BrainLift records far more students checking a word as known than able to explain it (`grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md`).

Quoted:

- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (352): “Self-report is the cheapest, fastest, and most underused signal in diagnostic assessment.”
- `grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd` (180-181): “"most child and adult readers have a poor ability to calibrate the success of their comprehension"”
- `grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md` (142-143): “~80% of students check a word as "known," ~50% can give an example, ~20% can explain it”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (303): “How do students reach their stage: assigned by the teacher, set by a diagnostic, or chosen by the student?”
- `g9/library/text/L9b6d99.txt` (303): “How do students reach their stage: assigned by the teacher, set by a diagnostic, or chosen by the student?”

Published: [RAND Reading Study Group 2002](https://www.rand.org/pubs/monograph_reports/MR1465.html)

Against: none found

<sub>context · evidence-of-learning, measurement · universal · from ap, g3, research · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Two-part evidence items at Grade 3

Whether two-part claim-and-evidence items suit grade 3 is unsettled: state tests reportedly start them a grade later, and reviews of work at that grade disagree. A red team found a two-part evidence item in all 48 generated Grade 3 lessons.

The course plans' red-team taxonomy lists two-part evidence items shipped at Grade 3 as a developmentally inappropriate format, on the ground that state test blueprints put two-part evidence around grade 4 and up, and a red team found one in all 48 generated Grade 3 lessons despite the canonical instruction-quality standard. A later look at the Grade 3 checks found such items still being scored although they are banned at that grade. Against that, a Grade 5 course's acceptance framework records that feedback on the Grade 3 course praised its evidence and two-part work. The blueprint claim is secondhand and is not checked here.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-main-checkout-jul-work.patch` (20669): “| **Developmentally inappropriate formats** | EBSR shipped at G3 (state blueprints put two-part evidence ~G4+) | format census × grade-level state blueprint |”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/HUMAN-g3r-2026-07-27T08-38-36-019fa24b-fb42-7e61-a954-216db3ef77a4.md` (1068): “Also found a few checks pointing the wrong way: option counts capped at a max when the standard sets a minimum, passage length pushed toward STAAR test-prep, EBSR scored when it's banned at G3, and most checks report-only so findings never move a score.”
- `grade3-reading/_archive/2026-08-13-consolidation/redteam-g3-round3-report-and-evidence.tar.gz` (RED_TEAM_ROUND3.md inside it) (181-182): “Every generated G3 lesson includes an EBSR: **48/48**, despite the canonical instruction-quality standard”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/STUDENT_READY_CRITICISM_FRAMEWORK.qmd inside it) (189): “G3 feedback praised evidence/two-part work.”
- `grade3-reading/course-renderer/docs/rules/questions-and-assessment.md` (596): “2026-06-29 calls the two-part evidence items "well built", a genuine strength”
- `grade3-reading/course-renderer/docs/rules/questions-and-assessment.md` (598-599): “2026-07-08 calls the same type "likely developmentally inappropriate for grade 3 — that type generally appears on state tests around grade 4 and above"”
- `grade3-reading/course-renderer/docs/rules/questions-and-assessment.md` (601-602): “This repo is Grade 4, where the second note's own reasoning says the type is fine”
- `grade3-reading/course-renderer/docs/rules/questions-and-assessment.md` (602-603): “is a supported bank type. Needs a decision.”

Against: The sources quoted disagree with one another. A format record on record keeps two-part items out of Grade 3 and notes that a ruling on them is still pending (choose-the-format-the-target-needs).

<sub>context · format, demand · domain · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### What ends a step with no verdict

What should end a step whose answers never get a verdict, when a student cannot quote exactly or the judge cannot place a stance?

Tracing the lesson engine's response paths found answers that never close their step. The claim-evidence-reasoning block sends back a quotation it cannot find in the text as often as it is given one, since it never reads the try count. The debate's judged branches, for a stance the judge cannot place, one with no reason from the text, or no judge at all, return no verdict and no release, so with no judge every real stance is asked to be said once more. On the lesson page, which counts only wrong answers, a debate answer too thin or bare to judge never reaches its two-tries release either. The scripted readers never write a real stance, so no playtest reaches these branches.

Quoted:

- `g9/transformer/src/mechanics/cer-frame.js` (100): “Copy the words exactly from the text, so your quotation can be found.”
- `g9/transformer/src/mechanics/debate.js` (118): “Say it once more, plainly: where do you stand, and why?”
- `g9/transformer/src/core/runtime.js` (31): “if (!judge) return { results: Object.fromEntries(proposals.map((p) => [p.pid, unjudged(p.checks)])), decision: null };”
- `g9/transformer/src/judge.js` (25): “verdict: "unclear", reason, band: "escalate"”
- `g9/transformer/web/lesson.js` (662): “if (res.correct === false) tries++;”
- `g9/transformer/src/mechanics/debate.js` (129): “two tries, then the position is given and the task closes (the 3D build's release rule), so no reader is held here”
- `g9/transformer/src/quality/personas.js` (104): “right: (item) => ({ type: "reply", side: "A", answer: item.model_position”
- `othello-archive/server/tasks/close.mjs` (55): “The student must leave with an answer to the question.”
- `othello-archive/server/tasks/close.mjs` (72): “If it is not an attempt: do not quote it and do not comment on it.”
- `othello-course-renderer-draft/repo/docs/g5-static-scoring-audit.md` (19): “After the configured repeated infrastructure-failure limit (default two), the authored answer appears and the student can choose Move on.”
- `othello-course-renderer-draft/repo/docs/g5-static-scoring-audit.md` (19): “That releases the navigation gate but is not a successful assessment.”

Against: The debate itself says that after two tries the position is given and the task closes, "so no reader is held here", and that with no judge the model position closes the task; both hold only on its code path, for thin or bare answers, and in sessions, where the runtime counts the tries. No saved playtest includes the debate.

<sub>context · practice, feedback · universal · from g9 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### When a prerequisite may block a learner

What recall evidence a hard prerequisite should demand before it may block a learner is unsettled, since the single-check criterion in use is provisional and uncalibrated. One grade-5 course graph asks for unaided retrieval plus one correct application on a parallel prompt, and gates no learner until that is calibrated.

A grade-5 reading course graph sets the evidence for a hard prerequisite link as unaided point-of-use retrieval plus one correct application on a parallel prompt, with a failure running the named on-ramp and a recheck, and it activates no learner gate before that threshold is calibrated. The course's case for review lists calibrating this provisional criterion as a decision still to make before learner-gated delivery, because the graph can state the retrieval behaviour required but a universal one-check threshold is not empirical learner evidence.

Quoted:

- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/evidence/case-for-review.md` (132): “Calibrate the provisional point-of-use fluency criterion used by hard prerequisite edges.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/evidence/case-for-review.md` (132): “The graph can state the required retrieval behavior, but a universal one-check threshold is not empirical learner evidence.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/evidence/course-graph-guide.md` (196): “Unaided point-of-use retrieval plus one correct application on a parallel prompt; failure runs the named on-ramp and recheck.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/evidence/course-graph-guide.md` (196): “No learner gate is active before threshold calibration.”

Against: none found

<sub>context · evidence-of-learning, sequence, measurement · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### When a question and its text disagree

When a question and its text disagree, it is not settled which should change: one rule edits the passage for a vocabulary item, another bars editing it for a quotation.

The course-fix procedure repairs a vocabulary item whose word is not in the passage by editing the passage to use the word in context, never by rewording the stem or deleting the item (`grade3-reading/knowledge_bot/skills/timeback-course-fix/SKILL.md`). The content-integrity check says never to repair a missing quotation by changing the passage unless the passage's own authority is wrong (`grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md`). The second rule's exception, a passage that is itself wrong, may reconcile the two, but no ruling was found that says so.

Quoted:

- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md` (171): “Never repair a missing quote by changing the passage unless the passage authority itself is wrong.”
- `grade3-reading/knowledge_bot/skills/timeback-course-fix/SKILL.md` (46-47): “**Vocab word-not-in-passage (NN#5):** FIX by editing the PASSAGE — `PUT {QTI}/stimuli/{id}` to use the word in context. Never reword the stem to dodge it; never delete the item.”

Against: No ruling reconciling the two rules was found.

<sub>context · stimulus, alignment · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### When quiet reading stops counting as focus

How long a reader may go without interacting before time stops counting as focused is unsettled: real reading looks idle, and the window in use is an unvalidated guess. One reading course stops counting focus 25 seconds after the child's last action, a figure no observed session data set.

A grade-3 reading course's points rubric counts time as focused while the child has done something in the last 25 seconds, and arriving on a page counts as doing something, so quiet reading time counts. The rubric marks the 25 seconds as its own number rather than the live rules': nothing in the live rules fixes it, no observed session data set it, and it is a deliberate guess in the generous direction. An analysis of the points simulation names the trade-off: a child genuinely reading taps nothing for minutes at a time, so a tight window under-counts what a reading course wants to reward, while a loose one over-counts a child who has wandered off.

Quoted:

- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/XP-SIM.md` (418): “The 25s idle window is generous by design and unvalidated by data.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/XP-SIM.md` (418-419): “A child who is genuinely reading a passage taps nothing for minutes at a time”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/XP-SIM.md` (421-422): “Nothing in the rubric constrains it and no observed session data informed it.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/XP-RUBRIC.md` (108): “the child has done something in the last 25 seconds”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/XP-RUBRIC.md` (109-110): “Arriving on a page counts as doing something, so **quiet reading time does count**”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/XP-RUBRIC.md` (114-115): “Nothing in the live rules fixes it, and no observed session data set it.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/XP-RUBRIC.md` (115): “It is a deliberate guess in the generous direction, stated”

Against: none found

<sub>context · measurement, integrity, practice · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### When reference facts don't cover a claim

Whether a judge given reference facts should fail a claim the facts don't support, or only a claim they contradict.

The AP work's evaluator has two grounding designs that disagree. On an unmerged branch the judge is told that a claim no listed fact supports is unsupported, and the facts are capped at 30 per standard, taken in source-file order with no relevance ranking (`icloud-work/inceptbench/src/inceptbench/evaluators/base.py`). The fact audit and the reference-passage path on the main branch fail only a claim a passage directly contradicts, and say not to penalise correct content a passage doesn't mention (`icloud-work/inceptbench-main/src/inceptbench/tools/factual_accuracy_audit.py`, `icloud-work/inceptbench-main/src/inceptbench/evaluators/question.py`). With the cap, many true claims would have no matching fact, which argues for the contradiction-only reading, but neither reading has been tested.

Quoted:

- `icloud-work/inceptbench/src/inceptbench/evaluators/base.py` (620): “If a claim cannot be supported by an atom listed here, it is unsupported.”
- `icloud-work/inceptbench/src/inceptbench/evaluators/base.py` (622): “Cap at 30 atoms to keep prompt size bounded”
- `icloud-work/inceptbench/src/inceptbench/evaluators/base.py` (624-625): “Atoms are taken in … source-file order (no relevance ranking)”
- `icloud-work/inceptbench-main/src/inceptbench/tools/factual_accuracy_audit.py` (212): “3. Score **0.0** ONLY if a passage clearly and directly contradicts”
- `icloud-work/inceptbench-main/src/inceptbench/evaluators/question.py` (1241): “- Do NOT penalize correct content just because Wikipedia doesn't mention it.”
- `g9/transformer/src/mechanics/video-essay.js` (123): “two readings pose a question, which is neither true nor false: there, nothing said may go against the passage”
- `g9/transformer/src/mechanics/video-essay.js` (125): “Does narration_${k} avoid saying anything that passage contradicts?”
- `g9/transformer/src/mechanics/video-essay.js` (126): “Is everything narration_${k} says true to passage?”
- `g9-transformer-runs/decisions/4370894c30725db3.json` (837): “"value": 0.57,”
- `g9/transformer/v02/QA.md` (177): “an argument beat's narration that was not "true": it now has only to say nothing the text goes against;”
- `g9/transformer/src/mechanics/video-essay.js` (125): “narration says nothing the text goes against”
- `g9/transformer/src/mechanics/video-essay.js` (126): “narration is true to the text”

Against: none found; neither reading has been tested.

<sub>context · evaluation, integrity · universal · from ap · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### When review costs more than it saves

How low a pass rate can fall before reviewing generated items costs more time than it saves; one framing guesses below 60%, and nothing has measured it.

The AP question work's context document sets out quality bands and says that below 60% reviewing would take more time than the automation saves (`icloud-work/ML learnings/what_is_ap_and_why_it_matters.md`). The bands are framing: no review time was measured anywhere in the folder.

Quoted:

- `icloud-work/ML learnings/what_is_ap_and_why_it_matters.md` (114): “### Below 60%”
- `icloud-work/ML learnings/what_is_ap_and_why_it_matters.md` (115): “would spend more time reviewing than they'd save from automation.”

Against: none found

<sub>context · review, measurement · universal · from ap · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Where to centre a test's difficulty

Where a predictive test's difficulty should be centred: on the published norm, on the actual cohort or above grade. One blueprint centred its item difficulty at 200-210, so it measured most precisely well above where its students sat and an on-grade reader read as failing.

A measurement review found that centring item difficulty at 200-210 puts the most information ~+1.3 logits above where students sit, so an on-grade reader reads as failing; it asked to fail blueprints centred above the verified spring mean and to reconcile with the observed cohort mean of 206.4 (`grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd`). The staged assessment standard still says to centre above grade, because a test centred at the grade median is too easy to confirm above-grade reading (`grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md`). To settle it: the linking study that standard already calls for, in which students take this test and the published one.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd` (90-92): “centering item difficulty at 200-210 (our kb-0059 "by design") maximizes info ~+1.3 logits ABOVE where students sit → makes an on-grade reader read as failing and biases logit→RIT regression.”
- `grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd` (93-94): “FAIL blueprints centered above the verified spring mean; reconcile vs the observed cohort mean 206.4.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md` (91-92): “**Center above grade.** A test centered at the grade median is too easy to confirm above-grade reading.”

Against: none found

<sub>context · measurement, demand · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Whether a reading lesson takes speech

Whether a reading lesson should take spoken answers at all is unsettled: one course's lesson designs rule out voice input, while the engine it runs on asks for speech. Every one of the lesson designs' 20 structural gate checks repeats 'no voice input'.

The reading rule pack that the course renderer's authoring pipeline reads records a live conflict: the curriculum's master lesson spine says there is no speaking, and every one of its 20 structural gate checks repeats no voice input, while the engine ships speaking tasks, a say-back on every vocabulary card and speech-to-text scoring (`grade3-reading/course-renderer/authoring/inputs/rule-packs/reading-g3.json`, line 243). The pack follows the engine because that is what shipped, and records the conflict so the pipeline never presents it as settled. The curriculum's lesson-components sheet of 2026-08-06 says of its vocabulary step that there is no speaking and that understanding is checked by a multiple-choice question (`grade3-reading/course-renderer/docs/pedagogy/example-lesson-components-2026-08-06.md`, line 22).

Quoted:

- `grade3-reading/course-renderer/authoring/inputs/rule-packs/reading-g3.json` (243): “The team's master spine says 'there is no speaking' and every one of their 20 structural gate checks repeats 'no voice input'. This engine ships speak nodes, a say-back on every vocabulary card and STT scoring. That is a live CONFLICT, not a gap, and it needs a ruling.”
- `grade3-reading/course-renderer/authoring/inputs/rule-packs/reading-g3.json` (243): “recorded so the pipeline never presents the conflict as settled”
- `grade3-reading/course-renderer/docs/pedagogy/example-lesson-components-2026-08-06.md` (22): “There is no speaking; understanding is checked by the MCQ.”

Against: none found

<sub>context · format, accessibility, marking · universal · from g3 · open-question · open · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Whether to label machine-made media

Whether to label media as machine-made is unsettled: most teens say they want labels, but labels tend to lower trust in content presented as authoritative. In a national survey, 73% of US teens wanted AI-generated content clearly labelled or watermarked.

Research for the Grade 9 film found a nationally representative survey of US teens (January 2025) in which 73% wanted AI-generated content clearly labelled or watermarked (`grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd`). Experiments on disclosure point the other way: labelling content as AI-generated lowers perceived credibility and trust even when its quality is identical, and in the one field experiment with high-school students a simple label raised trust in a chatbot but lowered it for labelled news (the same file). The file's net read is that disclosure is not a free action: it can raise attention for a moment but tends to lower trust on reflection, most for content presented as authoritative, which the unit film is (the same file).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd` (224-225): “**73% of teens want AI-generated content clearly labeled or watermarked**”
- `grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd` (67): “labeling content as AI-generated **lowers perceived credibility/trust even when content quality is identical**”
- `grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd` (68): “Field experiment, **60 high-school students** in Henan, China”
- `grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd` (71-72): “disclosure/labeling is not a free action.”

Published: [Common Sense Media 2025, Research Reveals Teens' Distrust in Tech Companies and AI-Generated Content](https://www.commonsensemedia.org/press-releases/research-reveals-teens-distrust-in-tech-companies-and-ai-generated-content) · [AI labeling reduces the perceived accuracy of online content but has limited broader effects (arXiv:2506.16202)](https://arxiv.org/pdf/2506.16202) · [Chen, Lai, Liu, Li, Wang & Yan 2026, See, trust, and interact: how AI disclosure shapes high school students' trust](https://www.researchgate.net/publication/402930951_See_trust_and_interact_how_AI_disclosure_shapes_high_school_students'_trust) · [AI-Generated Content Disclosure and Prolonged Short-Video Engagement (Behavioral Sciences 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13405702/)

Against: Most of the disclosure experiments used adults, and the one with teenagers had 60 students at one school (`grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd`).

<sub>context · media, integrity · universal · from g9, research · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Who reads what students write

Who reads what students write, and what anyone learns from it, once their words are kept and never marked.

The film player saves the student's own words and the answer to its follow-up and never judges them
(`g9/player/README.md`); the film study leaves open who reads them and what they learn
(`othello-unit-video/research/FINDINGS.md`, "Open questions"), and one plan has them feed the next lesson's retrieval
(`g9/review/2026-10-07-act1-context-map/README.md`).

Quoted:

- `g9/transformer/src/mechanics/learning-question.js` (3): “saved beside the first and never marked (the 3D build's bookends); Jev may name what the second answer adds”
- `g9/transformer/src/mechanics/learning-question.js` (4): “in a line that quotes neither, and only when it is sure.”
- `g9/transformer/src/mechanics/learning-question.js` (89): “Code only: both answers are saved, never marked; the first is optional.”
- `g9/transformer/v04/README.md` (8): “paraphrase the line (saved, never marked)”
- `g9/player/content/archivist-checks-v7.json` (2): “Own-words steps are followed by one scripted probe in”
- `g9/library/text/L8ec9a0.txt` (14-16): “Playback continues only after a right answer, seeks are clamped to the first open check, own-words answers are saved and never scored, and one scripted follow-up asks "Why did you say that?".”
- `othello-course-renderer-draft/repo/public/design/grade-9/othello-film/README.md` (6): “own-words answers get one scripted follow-up, "Why did you say that?", never judged.”

Against: none found

<sub>context · marking, evidence-of-learning · universal · from g9 · open-question · open · found in [2026-10-12-2-round-1](../research/2026-10-12-2-round-1/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Words taught before reading

Whether a film before a reading should teach the text's words: one rule bans pre-teaching what the passage teaches, another calls the film the best place to teach a word.

One version of the intro-video rules says not to pre-teach vocabulary the passage is meant to teach (`downloads/BrainLift - What makes a good intro video.md`, line 932). The other says the video is ideally where a word gets taught, because a visual anchor, a spoken definition and later recurrence are worth considerably more than a definition on a card (line 301). The built Grade 3 lesson designs do some of both: a film stamps a few words, those are kept out of the lesson's vocabulary slot, and the lesson's taught word is a different one (`downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx`, line 13; `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 5. Feathers and Scales - CONNECT - Lesson Design (v3 - prototype-aligned).docx`, line 263). So part of the disagreement is about which words a film may teach.

Quoted:

- `downloads/BrainLift - What makes a good intro video.md` (932): “Do not pre-teach vocabulary that the passage is meant to teach.”
- `downloads/BrainLift - What makes a good intro video.md` (301): “Ideally the video is where a word gets taught, because a visual anchor plus a spoken definition plus later recurrence is worth considerably more than a definition on a card.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx` (13 (textutil text)): “Video-stamped words (off-limits for the vocab slot): magician, sultan.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 5. Feathers and Scales - CONNECT - Lesson Design (v3 - prototype-aligned).docx` (263 (textutil text)): “taught word (adaptation) distinct from the stamped words and cashed by the child in Part 3.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/video-scripts/U2.md` (11): “If the video says it first, cold, thirty seconds before the lesson teaches it, the lesson's Word Power step is teaching a word the child has already heard used as if it needed no explaining”

Against: none found

<sub>context · wording, media, sequence · universal · from g3 · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### World only, or the opening too

A film before a reading may show only the setting, or also the characters and the plot's opening: one rule bans plot, but previews measured to help included it.

One version of the intro-video rules shows only the world and none of the plot, "even when revealing plot would measurably improve comprehension" (`downloads/BrainLift - What makes a good intro video.md`, line 41). The other says a video that shows only scenery has built atmosphere rather than knowledge and missed the mark (line 291), and notes that the previews measured in the research contained plot, so a blanket ban is a position nobody has tested (line 422). The study it cites found that previews of the characters plus the opening of the plot produced sizeable comprehension gains, largest for lower-ability readers (line 447; Graves, Cooke and Laberge 1983).

Quoted:

- `downloads/BrainLift - What makes a good intro video.md` (41): “An intro video shows only the world² and none of the plot³, even when revealing plot would measurably improve comprehension.”
- `downloads/BrainLift - What makes a good intro video.md` (291): “A video that shows only scenery has built atmosphere rather than knowledge and has missed the mark.”
- `downloads/BrainLift - What makes a good intro video.md` (422): “A blanket ban on plot is a position nobody has tested, not a finding.”
- `downloads/BrainLift - What makes a good intro video.md` (447): “story previews consisting of characters plus the opening of the plot produced sizeable comprehension gains, largest for lower-ability readers.”
- `downloads/BrainLift - What makes a good intro video.md` (249): “no child has yet been observed watching one of our films.”
- `g9/sources/Othello Unit Video_ Info Sheet for Devfactory.md` (7): “The video tells students exactly where the story starts and exactly where it ends, then gives them the knowledge they need to make the journey between the two.”
- `g9/sources/Othello Unit Video_ Info Sheet for Devfactory.md` (20): “The pull comes from the story itself (A to B), told as fact.”
- `othello-archive/sources/act1/Othello Unit Video - Info Sheet for Devfactory.txt` (22): “The spoiler is deliberate. It moves the question from what happens to how it happens, which is the question the whole unit answers.”
- `othello-archive/sources/act1/Othello Unit Video - Info Sheet for Devfactory.txt` (23): “Direct instruction; Leavitt & Christenfeld (2011)”
- `grade3-reading/artifacts/video-briefs/PETER-PAN-BRIEF-RECONCILIATION-2026-08-31.md` (234): “agreed to reveal the plot and characters, and agreed to start exactly where”

Published: [Graves, Cooke and Laberge 1983, Effects of previewing difficult short stories on low ability junior high school students' comprehension, recall, and attitudes, Reading Research Quarterly 18(3)](https://doi.org/10.2307/747388)

Against: The world-only version calls itself internal doctrine, with no child yet observed watching one of its films (`downloads/BrainLift - What makes a good intro video.md`, line 249).

<sub>context · media, integrity · universal · from g3, research · open-question · open · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>
