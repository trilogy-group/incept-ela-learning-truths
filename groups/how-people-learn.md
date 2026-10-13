# How people learn

169 learnings. Each says where it came from and what argues against it. [What a perfect question is](../PERFECT-QUESTION.md) collects the criteria by facet, and [How to generate perfect questions](../GENERATING.md) collects the methods by stage.

### A chained model starts from noticing

Start a modelled think-aloud that chains procedures by noticing something in the text and wondering about it, then work the procedures to answer that self-posed question.

The Grade 3 reading curriculum's procedure spec, quoted verbatim in the reading course renderer, says a modelling moment that chains procedures is not usually triggered by a question put to the one modelling: they notice something specific in the text, pose themselves a question about it, then work through the procedures to answer it (`grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md`, lines 685-695). The same spec runs the search for evidence inside the think-aloud, after the procedure's first step, because a reader does not find before they have a question (line 838). Both are design rules; nothing measured their effect.

Quoted:

- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (687): “Chains are not usually triggered by a question posed to the teacher. The teacher notices something in the text and wonders about it, then works through the procedures to answer their own self-question.”
- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (693): “Wonder - the teacher poses a question to themselves about it.”
- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (838): “A reader does not "find" before they have a question: the search runs inside the think-aloud, immediately after the procedure's Step 1.”

Against: none found

<sub>criterion · demand, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A chart is scaffolding, not the learning

Treat a chart or graphic organiser as scaffolding, not the learning: have the learner compose the sentence the lesson builds toward, and cut the chart first when time runs short. In a meta-analysis of 45 text-structure studies, graphic organisers appeared in 75% and correlated with effect size at r = .05.

A research brief for a reading lesson reports that a 2016 meta-analysis of text-structure instruction, 45 studies in grades 2-12, dropped graphic organisers as a moderator because they were in 75% of the studies and correlated with effect size at r = .05 (`othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md`, lines 81-85). The lesson plan decided on that basis that the child composes the sentence and the chart is recorded for them, and that if the lesson runs long the chart is cut, not the spoken answer (`othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l1.json`, line 460). The finding shows that organisers did not track effect size, not that they never help.

Quoted:

- `othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md` (82-85): “2016 meta-analysis of text-structure instruction (45 studies, grades 2-12), graphic organisers were dropped as a moderator because they "were included in an overwhelming majority of the studies (75%) and had a small and non-significant correlation with the effect sizes (r = .05)"”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md` (71): “The chart is scaffolding, and the sentence is the lesson”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l1.json` (460): “The child composes the sentence, the chart is recorded for them, and this is no longer a fifty-fifty call.”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l1.json` (460): “Graphic organisers appeared in three quarters of the studies in the text-structure meta-analysis and correlated at r = .05 with effect size, which is why that meta-analysis dropped them as a moderator: the organiser is not where the learning is.”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l1.json` (460): “Practical consequence: if this lesson runs long, the chart is the part that gets cut, not the speak node.”
- `othello-course-renderer-draft/repo/docs/pedagogy/epic-chart.md` (25-26): “A chart is the cheapest possible answer to it.”

Published: [The effects of text structure instruction on expository reading comprehension: A meta-analysis, Journal of Educational Psychology, 2016](https://doi.org/10.1037/edu0000082)

Against: The course's own design note defends a chart that grows across a unit as the cheapest answer to carrying knowledge from lesson to lesson: "A chart is the cheapest possible answer to it." (`othello-course-renderer-draft/repo/docs/pedagogy/epic-chart.md`, lines 25-26).

<sub>criterion · demand, practice · universal · from g3, research · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A cold text decides each step up

End each block with an unseen text running a known procedure on new content, with no model or sentence starters, and let it decide stepping up or re-modelling. One writing scheme ends units 5, 10 and 15 with milestone cold checks, the last a practice state-test essay with no support.

A model curriculum's fading rules end each block of units with a cold text: a known procedure on new content, at the current stage and inside the knowledge the course has built, with no model and no sentence stems. The cold text is its mastery diagnostic: a learner who fails it gets the model back in the next lesson, and one who aces it is ready to step up. A unit clock also guarantees every child meets the fully independent form before the state test.

Quoted:

- `grade3-reading/course-renderer/docs/extras/alpharead-fading-guidance.md` (62): “The cold text = the mastery diagnostic: known procedure + new content, current stage, inside the built knowledge web. Bomb it → restore / re-model next lesson; ace it → ready to step.”
- `grade3-reading/course-renderer/docs/extras/alpharead-fading-guidance.md` (32): “Last text = COLD Stage-1: known procedure, new content, no MM, no stems.”
- `grade3-reading/course-renderer/docs/extras/alpharead-fading-guidance.md` (35): “Cold Stage-3 = a practice STAAR essay, no support. END OF UNIT 15 = milestone.”
- `grade3-reading/course-renderer/docs/extras/alpharead-fading-guidance.md` (66): “Backstop: the unit clock guarantees every child meets the fully independent form before the STAAR.”
- `grade3-reading/ti-courseplans/docs/practice-layer-spec.md` (71): “The cold benchmark is **never a mastery gate and never teaching material**”
- `grade3-reading/ti-courseplans/docs/practice-layer-spec.md` (61): “sealed windowed diagnostic on never-taught topics”

Against: Another course design in the same project keeps its cold benchmark, a "sealed windowed diagnostic on never-taught topics", out of gating: "The cold benchmark is **never a mastery gate and never teaching material**" (`grade3-reading/ti-courseplans/docs/practice-layer-spec.md`, lines 61 and 71). Nothing in the sources measures whether the cold-text routing works.

<sub>criterion · evidence-of-learning, sequence, practice · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A few concepts every lesson returns to

Organise a unit and a course around a few fixed concepts that every lesson returns to and adds to, and record which of them each lesson draws on. One course consolidated 14 concept pairs into 7 course-long threads.

A lesson walkthrough, in a version since superseded, brings back a five-row pattern chart in every lesson of its unit and fills it row by row, so the schema accumulates instead of being covered once (`downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md`); another unit's knowledge base sets one pattern that every text tests (`downloads/5. Curriculum/Instruction/3.3 - Ancient Civilisations - Lesson Designs/3.3 Ancient Civilisations - Knowledge Base - Full.xlsx`). Across the course, a fixed bank of 14 concept pairs is consolidated into 7 threads (`downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx`), and a unit's concept map records which pairs each lesson draws on (`downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx`). These are design rules; no outcome was measured.

Quoted:

- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (42): “The five-row pattern chart returns every lesson, filled row by row | Schema accumulates across the unit instead of being covered once”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx` (sheet 'Overview', cell A15): “CONCEPT MAP - which concepts each lesson draws on (from the fixed 14-pair bank)”
- `downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx` (sheet 'Threads & Ladders', cell A2): “Your 14 concept-pairs, consolidated into 7 course-long threads.”
- `grade3-reading/course-renderer/docs/pedagogy/epic-chart.md` (16-21): “1. **Retrieval is built in, not bolted on.** The child sees last lesson's answer at the moment they need it, so the opening check has something real to activate. This is R-KC-5, activating prior knowledge without re-teaching it. 2. **The scaffold fades on a schedule that is visible to everyone.** Filled rows are the support. Each lesson removes one, because each lesson asks the child to write the row that used to be given.”
- `grade3-reading/course-renderer/docs/pedagogy/epic-chart.md` (34-37): “The row is completed by the child's own written or chosen answer on the same page, not by the guide writing it up afterwards. That is deliberate: a `frame` whose rows arrive already filled shows the child a finished summary and calls it modelling, which is exactly the failure `think_aloud` exists to prevent.”
- `grade3-reading/course-renderer/docs/pedagogy/epic-chart.md` (47): “| L3 Circe and the Lotus-Eaters | Lesson three, the island. What kind of trial was it? | target, L1 and L2 filled |”
- `othello-course-renderer-draft/repo/docs/pedagogy/epic-chart.md` (19-21): “**The scaffold fades on a schedule that is visible to everyone.** Filled rows are the support. Each lesson removes one, because each lesson asks the child to write the row that used to be given.”
- `othello-course-renderer-draft/repo/docs/pedagogy/epic-chart.md` (23): “**Knowledge accumulates somewhere the child can point at.**”
- `othello-course-renderer-draft/repo/docs/pedagogy/epic-chart.md` (34-35): “The row is completed by the child's own written or chosen answer on the same page, not by the guide writing it up afterwards.”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l1.json` (460): “Graphic organisers appeared in three quarters of the studies in the text-structure meta-analysis and correlated at r = .05 with effect size, which is why that meta-analysis dropped them as a moderator: the organiser is not where the learning is.”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l1.json` (460): “if this lesson runs long, the chart is the part that gets cut, not the speak node.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/SEQUENCING-BRIEF.md inside it) (53-54): “Chronology alone is insufficient. A lesson earns its place by adding a named mechanism or forcing a previous mechanism to explain new evidence.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/SEQUENCING-BRIEF.md inside it) (127-128): “**F1: Chronology dump.** Detection: lessons only follow dates and no recurring mechanism is reused. Recovery: add the missing revisit activation and make it do explanatory work.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (455-456): “A purely chronological outline can become a sequence of summaries with no compounding operation.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (83-85): “Maintain a region matrix across Chesapeake, New England, middle, and southern colonies. Every row must connect geography and economic purpose to labor, governance, and social order.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (103): “Build one cumulative imperial-crisis causal chain.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (142-143): “Maintain a sectional-conflict ledger linking land, labor, party systems, law, and violence.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (202): “Use a foreign/domestic consequence ledger.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (321-322): “Unit syntheses ask students to revise a causal or continuity model, not recopy a timeline.”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (27): “A star marks the lead pair: the one the learning question turns on. Every lesson uses all six pairs, because Act 1 sets up the whole play.”
- `othello-archive/sources/act1/KB - Overview.csv` (6): “SPINE HOOK, carried in every lesson.”
- `g9/library/text/L492d5c.txt` (27): “A star marks the lead pair: the one the learning question turns on. Every lesson uses all six pairs, because Act 1 sets up the whole play.”

Against: none found

<sub>criterion · sequence, alignment · domain · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A few named procedures, the same steps

Teach a small fixed set of named thinking procedures that covers every skill the course models, with identical steps each time, and say the procedure's name whenever it is modelled. Seven procedures cover every skill one grade 3 reading course models, so its students learn seven ways of thinking rather than dozens of isolated skills.

A grade 3 reading course built its modelling around seven procedures that together cover every skill component it models (`grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md`, line 22). A later rule has each lesson name the procedure it teaches, such as finding or inferring, and teach the identical steps every time that procedure appears. The course's modelling rule adds that the name is itself the tool: a child who watched one procedure four times without once hearing its name was given four demonstrations and no tool. The contract checks that a named procedure is one of the seven, though whether a lesson names one at all is still left to convention (`grade3-reading/course-renderer/docs/rules/pedagogy-and-lesson-structure.md`, lines 351-355).

Quoted:

- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (22): “Seven procedures cover every Standard Component used in this curriculum as a Modelling Moment target. Students learn seven ways of thinking, not dozens of isolated skills.”
- `grade3-reading/course-renderer/docs/rules/knowledge-and-curriculum.md` (190-192): “A lesson names the comprehension procedure it teaches, for example FIND or INFER, and the child is taught the identical sequential steps every time that procedure appears.”
- `grade3-reading/course-renderer/docs/rules/pedagogy-and-lesson-structure.md` (343-345): “Seven named procedures are the whole design: a child who has watched FIND four times without once hearing it called FIND has been given four demonstrations and no tool.”

Against: none found

<sub>criterion · sequence, practice, wording · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A later lesson must need the earlier one

Claim that a course builds knowledge only where a later activity needs what an earlier part added, so that taking the earlier part out would break it.

The reading project's course standard accepts a sequence only when it names its primary understanding, what each part adds, and a later activity that requires genuine recruitment of that knowledge, and it lists links based only on shared words and orphan lessons as failure signals (`grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd`, Q014). A source atom behind that standard claims compounding only when removing an earlier anchor removes a later explanatory, comparative, interpretive or decision resource (`grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json`). Feedback on the course plans asked for links between units about the big idea, not surface facts (`grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md`, item 19).

Quoted:

- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json` (344): “Claim knowledge compounding only when removing an earlier anchor removes a later explanatory, comparative, interpretive, or decision resource.”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (232): “Accept when: Each sequence names its primary understanding, what each part adds, and a later activity that requires genuine recruitment of that knowledge.”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (233): “- Failure signals: Topic list; links based only on shared words; orphan lessons; final recall of disconnected facts.”
- `grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md` (97-98): “19. **Cross-unit links about the BIG IDEA, not surface facts**”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “if lessons and questions can be freely reordered without changing assumptions or later work, the outline is a bank, not a curriculum.”
- `incept-package-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “if lessons and questions can be freely reordered without changing assumptions or later work, the outline is a bank, not a curriculum.”
- `incept-package-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “A later lesson must lose an explanatory, comparative, or decision resource if an earlier anchor is removed.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “remove a middle lesson; if no later explanation, comparison, interpretation, or decision loses a resource, the lesson is adjacent content.”
- `g9/sources/Othello Unit Video_ Info Sheet for Devfactory.md` (14): “Each thing we plant should change how students meet what comes later”
- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/COMPOUNDING-GATE.md` (55-56): “Only **one** of these needs to be true (the gate does **not** require the new idea to be logically impossible to teach alone):”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/README.md` (125-127): “(This is the compounding contract made falsifiable.”

Against: A later run found counter-evidence (`grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/COMPOUNDING-GATE.md`).

<sub>criterion · sequence, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A modelled answer answers its question

A modelled answer must answer the question asked, picking one of the choices an either-or question offers, never defining the question's words or answering a neighbouring question.

Reported live on a Grade 3 reading build: a modelled row asked whether characters were brave or reckless and its answer card gave two dictionary definitions, and another row asked about one character and answered about another. The build's schema calls both the same failure, the card written from the row's topic rather than from its question, so the child watches a model that never lands. Its rule now requires each modelled answer to answer its own question, name a character the question names, pick one of the choices an either-or question offers and not dodge into defining a word the question already used, and a gate pins it.

Quoted:

- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/CONTENT-SCHEMA.md` (554): “An I-do answer card answers its own question.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/CONTENT-SCHEMA.md` (558): “dodge into defining a word the question already used, it picks one of the choices an”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/CONTENT-SCHEMA.md` (565): “rather than from the question, so the child watches a model that never lands.”

Against: none found

<sub>criterion · practice, key · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A recall prompt that isn't assessment

Keep a commit-before-reveal prompt, such as saying a word's meaning before turning its card, as retrieval practice, but never count it as assessment, since nothing checks the answer.

When a review of a Grade 9 prototype cut a deck of word cards, it kept the deck's prompt to say what each word means before turning it over, and moved it into the word web. Its evidence note says attempting to retrieve before seeing the answer produces better retention than studying the answer alone, but that the prompt is unverifiable and so should not be counted as assessment; the note names no study. A lesson build for the play's next act asks learners to say a definition aloud before unsealing each term.

Quoted:

- `g9/sources/Othello_1_Feedback_DevFactory.md` (81): “Carry the commit-before-reveal beat — "say what each one means before you turn it over" — into the web.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (418): “Attempting to retrieve before seeing the answer produces better retention than studying the answer alone. It is worth keeping as a prompt in the word web, but it is unverifiable, so it should not be counted as assessment.”
- `g9/library/text/L36b8ba.txt` (215): “"Say what each one means before you turn it over" is commit-before-reveal, a retrieval attempt ahead of the answer.”
- `g9/library/text/L36b8ba.txt` (418): “Attempting to retrieve before seeing the answer produces better retention than studying the answer alone. It is worth keeping as a prompt in the word web, but it is unverifiable, so it should not be counted as assessment.”
- `g9/library/text/L36b8ba.txt` (81): “Carry the commit-before-reveal beat — "say what each one means before you turn it over" — into the web.”

Against: none found

<sub>criterion · practice, evidence-of-learning · universal · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A routine for a word's meaning

When a reader can decode a word but doesn't know its meaning, teach a routine: mark it, reread its sentence, reread around it, break it into parts.

An IES video on using context, quoted in a reading course's review standard, gives the first steps: mark the unknown word, reread the sentence it is in for clues, and if that doesn't work reread the surrounding sentences (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/word-solving-for-meaning.md`). The standard adds breaking the word into its parts and, for a child whose home language shares roots, a cognate check, and branches to decoding help only when a diagnostic shows decoding is the barrier. The learner says the meaning in their own words and names the clue that gave it away; the failure the standard names is the instant gloss, which teaches one word and no routine.

Quoted:

- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/word-solving-for-meaning.md` (18): “First is that when we come to that unknown tricky word, we need to mark it in some way. So we can highlight it, we can underline it. Second is we're going to reread the sentence that the unknown word is in and look for clues in that word... If that doesn't work, my third step is I can reread the surrounding sentences.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/word-solving-for-meaning.md` (10): “break the word into morphological parts (prefix/root/suffix)”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/word-solving-for-meaning.md` (11-12): “If diagnostics indicate a decoding barrier, the app may branch to decoding-specific support in a separate support path.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/word-solving-for-meaning.md` (33): “The child must produce a *meaning in their own words* and cite *which clue* gave it away”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/word-solving-for-meaning.md` (43-44): “The failure mode is the **instant gloss**: the tutor supplies the definition and skips transfer, teaching one word and zero routine”

Published: [Use Context (PRISMS), IES video](https://www.youtube.com/watch?v=iW2XtyDosRo)

Against: A curriculum map's note on a grade 3 standard says a child can't use context when the whole domain is unfamiliar, because the surrounding concepts are new too (`downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx`, sheet 'Standard components'), so the routine may fail on a new subject's own terms.

<sub>criterion · hints, practice · universal · from g3, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A staged course needs a placement step

A course whose learners climb stages needs a way to decide where each starts, or every learner defaults to the lowest stage and a stage ceiling never does any work.

A Grade 3 reading lesson design makes its writing stages available rather than assigned: each unit sets a ceiling, and a child works at whatever stage they can reach below it (`g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx`, lines 5-6). It notes that something has to decide where a child starts, that a short pre-reading placement is the obvious candidate but is not designed yet, and that without it every child defaults to the first stage and the ceiling never does any work (line 38). A Grade 9 lesson design specification lists how students reach their stage as a decision needed before build (`g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md`, line 303).

Quoted:

- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (5): “Stages are available, not assigned.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (6): “Each unit block sets a CEILING, and a child works at whatever stage they can reach below it.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (38): “Something has to decide where a child starts.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (38): “A short pre-reading placement is the obvious candidate, but it is not designed yet, and without it every child defaults to Stage 1 and the ceiling never does any work.”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (303): “How do students reach their stage”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (303): “Needed before build, because it drives the learning question screen.”

Against: Neither design has built the step: the Grade 3 placement is not designed yet, and the Grade 9 specification still lists assignment, a diagnostic or the student's own choice as options (`g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md`, line 303).

<sub>criterion · sequence, measurement · universal · from g3, g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A strategy the student owns

Name a strategy's steps in words that work on any text, not one app's mechanics, and present it as the student's own tool for when a text gets hard.

A content review of a reference reading lesson asked for a step's verb to change from 'tap' to 'find', because finding is what a student will do in any text, not just in the app (`grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt`, line 21), and the course's register lists the reworded steps as met (`grade3-reading/artifacts/criteria-register.csv`, line 115). A 285-criterion review profile asks that every strategy be framed as the student's to use when the text gets hard; on two lessons that framing was missing (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md`, lines 92-103).

Quoted:

- `grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt` (21): “because ‘find’ captures what they will need to do in any text (not just on this app)”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md` (98): “Every strategy is explicitly framed as 'yours to use when the text gets hard'”
- `g9/library/collections/research-pack-2026-10-02/full-source-site/sources/engine/kb0180--kb-0180-lesson-structure-procedure-rulings.qmd` (95-96): “retiring "hunt for keywords" (many texts have no clean keyword) and "reread and tap" -> "reread and find" ("find" names what a reader does, not what a finger does).”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (35): “INFER is framed exactly that way at its introduction in L2”

Against: The same review rated the framing criterion advisory, since students already run the steps alone in the independent task (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md`, line 103), and the gap was carried to a register as a note, not fixed (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/L5-REVIEW-GAPS-2026-09-17.md`, line 12).

<sub>criterion · wording · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A task that proves each step

In independent practice, still walk the taught procedure, giving each step a small task that shows the learner did it. Four small tasks walk one reading procedure: click what you are looking for, click the first line to reread, tap the evidence, then fill a gap as modelled.

A lesson review asked that the app support each step of the procedure in independent practice, with each step appearing with a task that demonstrates it was done (`othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md`, lines 141-143). The course renderer adopted this as a rule: independent practice still walks the procedure, and each step gets a task proving the child did it, ending in a gap fill as modelled (lines 137-139). It is followed by convention, carried by the frame node's modelled, shared and independent row states (lines 148-149).

Quoted:

- `othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md` (137-139): “**Rule.** Independent practice still walks the procedure. Each step gets a task proving the child did it: click the thing you are looking for, click the first line of the paragraph to reread, tap the evidence, then a gap fill as modelled.”
- `othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md` (141-143): “The app still needs to support students to do each of these steps. **Have each step appear with a task that demonstrates they have done the step.**”
- `othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md` (148-149): “Followed by convention; the `frame` node carries the modelled → shared → independent row state that makes this possible.”
- `othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md` (191-192): “Guide commentary before each part of a text, sentence starters and step-by-step guidance all fade.”
- `othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md` (207-208): “Only one lesson of the unit is authored, so nothing fades yet and no mechanism exists.”

Against: The same rules have step-by-step guidance fade across a unit: "Guide commentary before each part of a text, sentence starters and step-by-step guidance all fade." (`othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md`, lines 190-192). That rule is not yet applied, since only one lesson of the unit is authored (lines 207-208).

<sub>criterion · practice, evidence-of-learning · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A way out for readers above the band

Give learners who already read well above a course's band a test-out or measure-only path, instead of holding them on material they have outgrown. In one grade, 102 of 325 certified readers (31%) worked two to four grades above the course's band.

A deepening analysis of a second-grade reading cohort found 102 of 325 certified readers (31%) working two to four grades above the 420–650L band the course tops out at, 64 of them at about a sixth-grade frontier (`grade3-reading/ti-courseplans/courses/g2-reading/analysis/g2-deepening-addendum.md`, lines 36-38). It named two options: an explicit accelerate-out or test-out path, or accepting that the top band's value is coverage and measurement, not instruction (the same file, lines 43-45). A dropout analysis of the same grade found completion falling as starting ability rose, 32% of the highest scorers doing substantial work against 49–56% in the low and middle bands, and read it as boredom rather than frustration (`grade3-reading/ti-courseplans/courses/g2-reading/analysis/dropout-4-who.md`, lines 19 and 79).

Quoted:

- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/g2-deepening-addendum.md` (37-38): “So **102 of 325 certified G2 readers (31%) work two-to-four grades above the 420–650L band this course tops out at.**”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/g2-deepening-addendum.md` (36-37): “**The 64 students at the 90th+ percentile are reading at a ~6.6-grade instructional frontier — sixth-grade text, in second grade.**”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/g2-deepening-addendum.md` (43-45): “(a) an explicit accelerate-out / test-out path for the top band (consistent with the placement layer's existing test-out instrument), or (b) accept that the top band's value is *coverage/measurement*, not instruction, and don't pretend to teach them.”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/dropout-4-who.md` (19): “Among students *with* a starting MAP, **high-RIT (200+) students complete worst (32% substantial)** while low/mid-RIT complete best (49–56%).”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/dropout-4-who.md` (79): “Among MAP'd students, **higher starting ability → lower completion**. This supports **boredom / no-stretch** over frustration”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/dropout-4-who.md` (79): “Consistent with §2 (the 130 high-RIT students overlap the older off-grade remediation group placed below their level).”

Against: The highest-scoring group overlaps older learners placed below their level for remediation, so age and placement may explain part of the gradient (`grade3-reading/ti-courseplans/courses/g2-reading/analysis/dropout-4-who.md`, line 79).

<sub>criterion · sequence, demand · universal · from g3 · measured · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Advance on mastery, not completion

Move a learner on only when rigorous checks of independent, unprompted performance show mastery, never for time spent, finishing or saying they know it.

The delivery platform's non-negotiables require mastery gates at 90% accuracy or more and forbid advancing students on time, completion or self-report; its learning-science page says students do not progress without at least 90% accuracy on rigorous assessments, and its evaluation dimensions define mastery truthfulness as completed meaning mastered. The reading project adopted these as its bar. Recognising an answer with hints does not count as mastery either, so that completed means mastered.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd` (21): “2. **Enforce mastery gates at ≥90% accuracy.** Do not advance students based on time, completion, or self-report.”
- `grade3-reading/knowledge_bot/knowledge/kb-0026-evaluating-apps.qmd` (21): “| **Mastery truthfulness**       | "Completed" means mastered                         |”
- `grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd` (27): “Students do not progress without demonstrating ≥90% accuracy on rigorous assessments.”
- `grade3-reading/knowledge_bot/knowledge/kb-0006-beyond-alpharead-source.qmd` (55): “The **"mastery" metric (80% correct answers)** is accurately calculated on Dash.”
- `grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd` (123): “**Staged 90% gates** — Band A advisory, blocking from Band B, final gate at course end (only ~17% reach 90% today).”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/direct-instruction.md` (34): “Progression to the next lesson occurs only when students demonstrate mastery of current material.”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (75): “Incept defines mastery as the point at which a student can apply a skill or concept independently, accurately, and automatically.”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (380): “Every cycle ends with independent recall \- typing or saying the word without hints \- to confirm mastery.”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (399): “* **Recall** (independent response without prompts)”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (401): “This structured cycle ensures every new word moves from recognition to confident, fluent use.”
- `g9/transcript/chat-transcript.redacted.txt` (3111): “Coached completion, engagement and fluent writing matter, but none can substitute for that evidence.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (157): “Do not infer mastery from task completion, a self-reported spoken repetition, an elapsed audio clip, or agreement with an example.”

Against: The bar and its enforcement vary: one platform's mastery metric counts 80% correct (`grade3-reading/knowledge_bot/knowledge/kb-0006-beyond-alpharead-source.qmd`, line 55), and one course plan stages its 90% gates, advisory at first and blocking later, with only about 17% reaching 90% today (`grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd`, line 123). The same page records a criticism of the approach: '- Sometimes criticized for being too rigid or prescriptive, potentially limiting teacher creativity' (`icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/direct-instruction.md`, line 62).

<sub>criterion · evidence-of-learning, integrity · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Aim a prequestion at the main goal

A question asked before reading helps learners learn what it asks about and little else, so aim it at the lesson's most important goal. In one meta-analysis, questions asked before study had an effect size of .66 on the information they asked about and .01 on other information.

A research-boundary review checked the primary sources an outside review cited (`grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md`, section 3). The publisher confirms g=.66 for prequestioned information and g=.01 for other information (King-Shepard et al. 2025, https://doi.org/10.1007/s10648-025-10075-7), and a second meta-analysis confirms g=.54 targeted and .04 general (k97/91), with corrective feedback in the pre-study phase excluded (St. Hilaire, Chan & Ahn 2024, https://doi.org/10.3758/s13423-023-02353-8). The review's design conclusion is to target an important learning goal and resource other goals separately.

Quoted:

- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md` (37): “The publisher confirms **g=.66 for prequestioned information and g=.01 for other information**”
- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md` (43): “The **g=.54 targeted / .04 general** estimates are confirmed (k97/91).”
- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md` (39): “**Design conclusion:** target an important learning goal and resource other goals separately.”

Published: [King-Shepard et al. 2025](https://doi.org/10.1007/s10648-025-10075-7) · [St. Hilaire, Chan & Ahn 2024](https://doi.org/10.3758/s13423-023-02353-8)

Against: The child-specific targeted estimate was .22 against adults' .62, from few child effects (k20), and the general effect's confidence interval includes zero; the review warns against predicting a .66 effect for Grade 3, and notes that giving answers adds a learning opportunity of its own (the same file, lines 37-43).

<sub>criterion · alignment, sequence · universal · from g3, research · external-research · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### An organiser that matches the text

Give learners a graphic organiser matched to the text's structure, such as a Venn diagram for comparison or a timeline for sequence, and reuse it for their speaking and writing. One design maps 4 structures to organisers: comparison to a Venn diagram, cause to a chain, sequence to a timeline and narrative to a story map.

A reading course's review standard, citing IES videos on reading skills in grades 5 to 8 and on early reading outcomes for English learners, makes structure-matched organisers available as comprehension scaffolds (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/graphic-organizers-and-no-ability-label.md`). An organiser makes the text's relationships visible, so learners see them as well as read them, and the filled organiser becomes the source for speaking and writing. A mismatched organiser, such as a Venn diagram on a sequential text, misleads, so the standard checks that the organiser's type matches the passage's structure.

Quoted:

- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/graphic-organizers-and-no-ability-label.md` (21): “a graphic organizer is gonna help make those relationships clearer because they're not only going to read it in the graphic organizer, they're gonna see it in the graphic organizer. And that will make the content more comprehensible. And it also serves as a source for writing and speaking activities.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D10-delivery-ux-accessibility.md` (27): “Structure-matched graphic organizers (sequence, compare/contrast, cause-effect, Venn, story map) are available as comprehension scaffolds”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/graphic-organizers-and-no-ability-label.md` (12): “(a Venn diagram slapped on a sequential text) actively misleads”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/graphic-organizers-and-no-ability-label.md` (28): “compare→Venn, cause→cause-effect chain, sequence→timeline/steps, narrative→story map”

Published: [Reading Skills for Students in Grades 5 through 8, IES video](https://www.youtube.com/watch?v=nI-T6NA2d3w) · [Early Reading Outcomes: A Focus on English Learners, IES video](https://www.youtube.com/watch?v=K8XlGV8qCmE)

Against: none found

<sub>criterion · format, practice · universal · from g3, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Ask the lesson's question first and last

Ask the lesson's question at the start and again at the end, keeping both answers side by side and marking neither. One lesson engine opens the question with two or three of its phrases explained, keeps a first answer unmarked, and saves the end-of-lesson answer beside it.

An audit of the Grade 9 lesson engine found its export asked the lesson's question only as first thoughts, and proposed the bookends a 3D version draws: the question shown on its own with its key phrases explained, then answered again at the end (`g9-transformer-audit/2026-10-09-best-of-everything.json`). The learning-question block built on 9 October explains two or three phrases, and a judge checks that each note says what its phrase asks or means without answering the question. A first answer may be kept and is never marked; at the end the question is answered again and saved beside the first, also unmarked, and the judge may name what the second answer adds, in a line that quotes neither, only when it is sure (`g9/transformer/src/mechanics/learning-question.js`).

Quoted:

- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “One is the question shown on its own with its key phrases explained, then answered again at the end.”
- `g9/transformer/src/mechanics/learning-question.js` (2): “never the answer), and a first answer the student may keep, never marked.”
- `g9/transformer/src/mechanics/learning-question.js` (3): “again, saved beside the first and never marked (the 3D build's bookends)”
- `g9/transformer/src/mechanics/learning-question.js` (64): “Does note_${i} say what phrase_${i} asks or means in question, without answering question?”
- `g9/transformer/src/mechanics/learning-question.js` (99): “Saved, beside your first answer.”
- `g9/transformer/web/lesson.js` (468): “be kept, never marked; at the end of the lesson it is answered again, saved beside the first”
- `g9/transformer/src/glue/animated.js` (141): “Saved, beside your first thoughts from the start of the lesson.”
- `g9/transformer/web/lesson.js` (508): “One sentence. There is no wrong answer yet.”
- `g9/transformer/README.md` (120): “No lesson has been reviewed by a person or used by a student.”
- `g9/transformer/src/glue/threejs-render.js` (234): “the learning question's notes on its phrases; its return at the end of the lesson is a closing step, not exported”
- `g9/transformer/test/animated.test.mjs` (74): “the learning question opens the lesson after the openers, its phrases noted where the question has them, and is asked again, unmarked, before the end”
- `g9/transformer/src/mechanics/learning-question.js` (89): “Code only: both answers are saved, never marked; the first is optional.”
- `g9/transformer/test/animated.test.mjs` (85): “saved, never marked: the build's guards only”
- `g9/transformer/src/mechanics/learning-question.js` (3): “saved beside the first and never marked (the 3D build's bookends); Jev may name what the second answer adds”
- `g9/transformer/src/mechanics/learning-question.js` (4): “in a line that quotes neither, and only when it is sure.”
- `g9/transformer/src/mechanics/learning-question.js` (2-3): “At the end of the lesson it is answered … again, saved beside the first and never marked (the 3D build's bookends)”
- `g9/transformer/src/mechanics/learning-question.js` (96): “"Kept. You will come back to it at the end of the lesson."”
- `g9/transformer/src/mechanics/learning-question.js` (99): “"Saved, beside your first answer."”
- `grade3-reading/visual-findings-2026-09-08/grade5-book-flow/PR-BODY.md` (14): “The first lesson’s explicitly optional prediction receives a neutral acknowledgment without scoring; later required recall questions still gate Next.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/lesson-01.md` (9): “Accept all attempts. Do not mark missing theatre knowledge as failure. After reading, return to this prediction.”
- `grade3-reading/visual-findings-2026-09-08/grade5-book-flow/PRE-READING-FIX.md` (23): “Tier 1: source lesson explicitly makes L1 prediction ungated and non-evaluative.”
- `othello-archive/src/content/retrieval.ts` (201): “Your first answer, if you want one. One sentence. There is no wrong answer yet.”
- `othello-archive/src/steps/Close.tsx` (7): “The lesson's final closing task then returns to the learning question: first instinct beside the answer now.”

Against: The export to a 3D version leaves out the return at the end: "its return at the end of the lesson is a closing step, not exported" (`g9/transformer/src/glue/threejs-render.js`, line 234; `g9-transformer-audit/2026-10-09-builders.json`, line 1). The design comes from another build, and the sources give no measure of what the second answers add. The first answer is optional ("Code only: both answers are saved, never marked; the first is optional.", `g9/transformer/src/mechanics/learning-question.js`, line 89).

<sub>criterion · sequence, evidence-of-learning, marking · universal · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Assume only what every path guarantees

Assume only what every path guarantees: each branch teaches what later content uses and agrees on facts, and topics another course teaches work in either order, from a new angle.

A review of a reading course named its biggest problem: the child picks a character and the flow isn't fixed, so no one can be sure which knowledge or folktales a child has met, which undermines retrieval and sequencing (`grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md`). Guidance for the reading and writing courses that carry science and social studies makes the same point across courses: with no link to the subject courses, no one can be sure whether a student has studied a topic, so topics from earlier grades are always fair game, a same-grade topic has to work whether or not its subject lesson has happened, and a lesson keeps the vocabulary, nuance and framing the subject course gave it (`grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md`). A re-encounter should feel like a new angle, not a repeat, and in science it is better to re-meet an idea from an earlier grade than to be the first place a student meets it (the same file). When an idea may come back from another course, keep that course's framing and come at it from a new angle rather than repeat it.

Quoted:

- `grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md` (65): “because the child picks their character and flow isn't fixed, you can't be sure which knowledge/folktales they've met — undermines retrieval and sequencing.”
- `grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md` (4): “so at any given moment we cannot be sure whether a student has studied a topic or not.”
- `grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md` (14): “the Read/Write lesson should be consistent with how it was framed in the subject app — vocabulary, level of nuance, framing.”
- `grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md` (11): “The aim is for the re-encounter to feel like a new angle, not a repeat.”
- `grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md` (25): “It is better to re-encounter ideas from earlier grades than to be the first place a student meets an idea.”
- `grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd` (19): “There is currently no integration between the social studies/science apps and Alpha Read or Alpha Write, so at any given moment we cannot be sure whether a student has studied a topic.”
- `grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd` (30): “Topics taught in the same grade are potentially acceptable, provided the Read/Write treatment works whether or not the substantive science or social studies lesson has happened yet.”
- `grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd` (31): “Avoid sitting squarely on top of an identical topic. The re-encounter should feel like a new angle rather than a repeat: use a different subtopic, example, lens, or question.”
- `grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd` (36): “Where a topic has already been covered, the Read/Write lesson should be consistent with how it was framed in the subject app, including its vocabulary, level of nuance, and framing.”
- `grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd` (81): “As a general rule, avoid implicitly introducing scientific concepts that students may not have encountered. It is better to re-encounter ideas from earlier grades than for Alpha Read or Alpha Write to be the first place a student meets an idea.”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md` (54): “no cross-grade science first introduction disguised as Reading background;”
- `grade3-reading/knowledge_bot/knowledge/kb-0150-science-g6-atom-composite-ledger.qmd` (20): “Use this ledger mainly to check whether G3-G5 materials introduce Grade 6 concepts too early.”
- `grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd` (19): “so at any given moment we cannot be sure whether a student has studied a topic.”
- `grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd` (31): “The re-encounter should feel like a new angle rather than a repeat”
- `grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd` (36): “the Read/Write lesson should be consistent with how it was framed in the subject app”
- `grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd` (75): “must go through the misconception-check process.”
- `grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd` (81): “It is better to re-encounter ideas from earlier grades than for Alpha Read or Alpha Write to be the first place a student meets an idea.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md` (4): “at any given moment we cannot be sure whether a student has studied a topic or not.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md` (9): “are always fair game for re-encounter”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md` (10): “provided it is done in such a way that it doesn't matter whether the substantive science or social studies lesson has happened yet.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md` (11): “The aim is for the re-encounter to feel like a new angle, not a repeat.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md` (25): “It is better to re-encounter ideas from earlier grades than to be the first place a student meets an idea.”
- `grade3-reading/knowledge_bot/knowledge/kb-0149-draft-grade-5-science-ledger.qmd` (37-39): “a same-grade reading treatment must work whether the science lesson happened before or after it and should use a fresh angle rather than duplicate the proposed science treatment.”
- `grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` (45): “use prior-grade or sequencing-safe fresh-angle re-encounters;”
- `shadow-content-eval/reports/G3-U1-L12-review.md` (103): “Students on `partial`/`off`/`silent` never see it, yet p25 (*"how an obsession can take control"*) and p26 (*"The obsession made him reckless"*) use it.”
- `shadow-content-eval/reports/G3-U1-L12-review.md` (103): “**"Obsession" is only defined on two of the five dialogue branches.**”
- `shadow-content-eval/reports/G3-U1-L13-review.md` (81): “9. **p23 dialogue `silent` follow-up — the key contradicts the other branches.**”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-main-checkout-jul-work.patch` (20718): “| **Novel-concept-first (vs re-encounter)** | the reading app is the FIRST place a child meets a science concept | prefer re-encounter of earlier-grade ideas; reinforce-don't-redefine (consistent with the subject app's framing) |”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/docs/SCIENCE_MISCONCEPTION_CHECK.md inside it) (64-65): “3. **Prefer a re-encounter over a novel first encounter.** The passage should reinforce the subject framing from a fresh reading angle rather than silently redefine a science concept.”
- `grade3-reading/ti-courseplans/courses/g5-reading-v2/docs/SCIENCE_MISCONCEPTION_CHECK.md` (64-65): “3. **Prefer a re-encounter over a novel first encounter.** The passage should reinforce the subject framing from a fresh reading angle rather than silently redefine a science concept.”
- `grade3-reading/course-renderer/docs/pedagogy/misconceptions/social-science-coherence.md` (40): “**Prefer re-encounters over novel concepts.** As a general rule in science, avoid implicitly introducing scientific concepts students may not have encountered yet. It is better to re-encounter ideas from earlier grades than to be the first place a student meets an idea.”
- `grade3-reading/course-renderer/docs/pedagogy/misconceptions/social-science-coherence.md` (29): “Where a topic has already been covered, the Read/Write lesson should be consistent with how it was framed in the subject app — vocabulary, level of nuance, framing.”
- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/U1L1-SIGNOFF.md` (19): “Reactivation frame (re-encounter phrasing, enrollment-safe — NOT "last year you learned"):”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/SEQUENCING-BRIEF.md` (83): “a child without G3 gets the scaffold, not a lock-out.”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/SEQUENCING-BRIEF.md` (79): “U1 L1 reactivates, never re-teaches.”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/references/social-science-coherence-brainlift.md inside it) (13): “**Reinforce, don't redefine**”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/references/social-science-coherence-brainlift.md inside it) (14): “the Read/Write lesson should be consistent with how it was framed in the subject app — vocabulary, level of nuance, framing.”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/misconception-check.md inside it) (22-23): “The *intent* is a re-encounter — reinforcing how the science app already framed a topic, same vocabulary, same level of nuance.”
- `incept-package-hub/course-packages/courses/g5-reading/review/evidence/science-process.md` (64-65): “The passage should reinforce the subject framing from a fresh reading angle rather than silently redefine a science concept.”
- `othello-course-renderer-draft/repo/docs/video/u1-course-plan-notes.md` (392): “13. Re-encounter phrasing only. "In one well-known myth" is safe. "Last year you learned" is not.”
- `othello-course-renderer-draft/repo/authoring/inputs/rule-packs/reading-g3.json` (32): “It may reference NOTHING earlier: no 'remember when', no 'last time', no earlier text, character, tool or word treated as known.”
- `othello-course-renderer-draft/repo/docs/pedagogy/misconceptions/social-science-coherence.md` (19): “There is currently no integration between the social studies/science apps and Alpha Read / Alpha Write, so at any given moment we cannot be sure whether a student has studied a topic or not.”
- `othello-course-renderer-draft/repo/docs/pedagogy/misconceptions/social-science-coherence.md` (40): “It is better to re-encounter ideas from earlier grades than to be the first place a student meets an idea.”
- `othello-course-renderer-draft/repo/docs/pedagogy/misconceptions/social-science-coherence.md` (29): “Where a topic has already been covered, the Read/Write lesson should be consistent with how it was framed in the subject app — vocabulary, level of nuance, framing.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (86): “The unit-opener VIDEO does not count on its own — it is skippable, so a prompt”
- `grade3-reading/course-renderer/docs/pedagogy/misconceptions/social-science-coherence.md` (25-26): “**Topics taught in the same grade** are potentially OK to cover, provided it is done in such a way that it doesn't matter whether the substantive science or social studies lesson has happened yet. - **Avoid sitting squarely on top of an identical topic.**”
- `g9/library/text/Lfd669d.txt` (98): “After 90 seconds, the Archivist adds any of the six key words that are still missing, so every student's web ends with the full key word set.”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/misconception-check.md inside it) (22-23): “**Assume no prior exposure; introduce carefully and accurately.**”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/RESPONSE-MATRIX.md inside it) (5): “so 54 of 55 (98%) are lenses or re-encounters”
- `othello-course-renderer-draft/repo/authoring/peter-pan/fill/PEDAGOGY-FIXES-SPEC-2026-09-05.md` (29): “Receipt is universal (every child sees it regardless of dialogue branch),”
- `grade3-reading/course-renderer/authoring/peter-pan/fill/PEDAGOGY-FIXES-SPEC-2026-09-05.md` (29-30): “Receipt is universal (every child sees it regardless of dialogue branch), mirroring how L10's narration lands "brains beat strength".”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/subjects/science.md` (23-25): “Where a correction needs a home and no single item can carry it, put it in the guide's own voice as a plain statement near the vocabulary work ("say it here"), not buried in feedback.”

Against: A push for much more fiction sits against the knowledge-first plan these re-encounters serve; the response to it expects the re-encounter framing to reconcile the two but logged it as an open question, "Log as a question, not a silent rebalance." (`grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md`). The guidance accepts a same-grade topic as long as the lesson works whether or not the subject lesson has happened yet, so a student may still meet an idea there first (`grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd`).

<sub>criterion · sequence, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Assume only what was taught and kept

A lesson may assume only what earlier lessons taught and the learner still holds fluently, so record what each lesson assumes and adds, and check the whole sequence in code.

The reading project's instruction spec makes it a code-checked invariant that a lesson assumes only what earlier lessons taught, and counts an anchor as available only after a delayed ≥24h retest passed on new parallel items, so one first taught the same day, or present but not fluent, is not met (`grade3-reading/ti-courseplans/docs/instruction-modes-spec.md`, section 4). A committed negative fixture, a lesson assuming knowledge no earlier lesson added, was scored as individually fine by the per-lesson quality evaluator and was caught only by the cross-lesson invariant (`grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md`). The course standard asks that each prerequisite be established, activated, retaught, newly introduced or routed through a tested on-ramp (`grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd`, Q015); the curriculum BrainLift says a prerequisite that is met but not automated enough to free working memory makes the target skill unteachable (`grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md`), and the project's curriculum reference gives soft prerequisites a fluency threshold rather than a binary met or unmet (`grade3-reading/ti-courseplans/skills/train-teacher/references/curriculum-architecture.md`). Fluently here means well enough on a later day to leave working memory free. To hold a course to this, record what each lesson builds on and seeds, keep every keystone later lessons need, and check the whole sequence in code, failing any lesson the check can't find.

Quoted:

- `grade3-reading/ti-courseplans/docs/instruction-modes-spec.md` (61-62): “The default bar for "available to a new lesson" is E2-cleared (delayed ≥24h retest passed on new parallel items — practice spec P2)”
- `grade3-reading/ti-courseplans/docs/instruction-modes-spec.md` (63-64): “an anchor first taught the same day never satisfies an `assumes` edge, and an anchor that is present-but-not-fluent is treated as not met.”
- `grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (103-104): “IB scores each of those two lessons as individually fine; only the cross-lesson invariant separates them.”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd` (42): “Each prerequisite is established, activated, retaught, newly introduced, or routed through a tested on-ramp.”
- `grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md` (37): “A prerequisite that is technically met but not automated enough to free working memory makes the target skill unteachable.”
- `grade3-reading/ti-courseplans/skills/train-teacher/references/curriculum-architecture.md` (78-80): “**soft prereqs carry a fluency-threshold** (not binary met/unmet: "fluent enough not to consume working memory"), and **every edge carries a warrant tag** (logical / empirical / conventional).”
- `grade3-reading/ti-courseplans/docs/instruction-modes-spec.md` (59-60): “supplements, never replaces, human sequence review”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md` (16): “| L5 | spine check | `lesson.assumes` is a subset of the union of prior lessons' `adds`, in unit order. |”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/tools/course_validate.py` (592): “lesson '%s'%s assumes %s not added by any prior lesson in the unit”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/tools/course_validate.py` (578): “# A missing lesson must fail here too; skipping it would make the spine check vacuous.”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (123): “N2: relational-reference factuality. "As you saw last lesson" claims must be true against order.”
- `grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd` (60): “`exposure_justification` is factually wrong against the lesson's own U1-L6 lineage.”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md` (67-68): “no cross-unit baseline exists in the contract, so a unit's first lesson must have empty `assumes`”
- `grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd` (63): “A prerequisite that is technically met but not automated enough to free working memory makes the target skill unteachable.”
- `grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd` (62): “Splitting a restricted case from a general case (e.g., same-denominator before unlike-denominator fractions) causes students to build predictive models that become entrenched and must be actively undone.”
- `grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd` (76): “(1) hard prerequisites at fluency”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx` (196 (textutil text)): “If students haven't learned ratios (grade 6), they cannot meaningfully understand density or concentration.”
- `downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of G3-8_Threads_FourTier.docx` (400 (textutil text)): “Sequence supplying units first so their terms are available”
- `downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx` (60 (textutil text)): “the contact means something because both sides have been built.”
- `downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/[WORKING DRAFT] AlphaRead_G3-8_Full_Curriculum_to_G9.xlsx` (sheet 'Overview (read across)', cell A2): “Goal: a child reaches Grade 9 with no knowledge gaps.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx` (sheet 'Knowledge Base', cell E5): “Prior Knowledge”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx` (sheet 'Knowledge Base', cell T5): “Knowledge Seeds”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx` (sheet 'Overview', cell B39): “Seeds run forward to 3.4 Folk Tales, 3.10 Myths, 3.12/3.15 Poetry, the Grade 4 units (4.1 Legends, 4.4 World Mythology, 4.9 Classic Novels), and cross-curricular Science/Geography and History.”
- `downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx` (sheet 'How to read this', cell A11): “KEYSTONE texts are the anchor of a rung — the one you would not drop, because so much above it depends on the concept it plants.”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (100-101): “on the demo, `assumes (subset-of) prior adds` holds in unit order across l0..l4 (op-lint exit 0).”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (101-103): “The negative control is the committed fixture `fixtures/fail-l5-spine-gap.json` (lesson 2 assumes knowledge no prior lesson added) -> L5 FAIL.”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (103-104): “IB scores each of those two lessons as individually fine; only the cross-lesson invariant separates them.”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (87-88): “relational-reference factuality: "as you saw last lesson" claims must be true against order”
- `ti-courseplans-audit/skills/train-teacher/references/gauntlet-spec.md` (14): “Relational-reference truth check ("last lesson" must be factually last).”
- `ti-courseplans-audit/docs/instruction-modes-spec.md` (62-64): “so an anchor first taught the same day never satisfies an `assumes` edge, and an anchor that is present-but-not-fluent is treated as not met.”
- `ti-courseplans-audit/docs/instruction-modes-spec.md` (59-60): “a machine-checkable spine invariant that supplements, never replaces, human sequence review”
- `ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (106-107): “Theme Ledger completeness is still proposed.”
- `grade3-reading/artifacts/demo-unit-2026-07-10/00-knowledge-inventory.md` (8): “Proposed adds / assumes per text, with carrying spans.”
- `grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/01-course-graph.md` (87): “- What later text depends on this beat?”
- `grade3-reading/artifacts/g5-course/GAP-ANALYSIS-2026-08-18.md` (51): “There is no G3→G5 or G4→G5 transfer arc encoded anywhere in the canon.”
- `grade3-reading/artifacts/g5-course/CURRICULUM-REVIEW-STANDING-2026-08-17.md` (66): “G3→G4: 9 arcs, 28/49 lessons (57%) citing G3 content.”
- `grade3-reading/artifacts/g5-course/CURRICULUM-REVIEW-STANDING-2026-08-17.md` (67): “G4→G5: 7 arcs, 7/55 lessons (13%) citing G4 content — a real 7x drop in citation density.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D9-science-content-integrity.md` (41): “Concepts not introduced ahead of their math prerequisite; G3 energy stays qualitative”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/integration/check-before-final-content.txt` (330): “Earlier vocabulary placement does not establish prior teaching in this new unit.”
- `g9/library/text/L492d5c.txt` (40): “CARRIED THRESHOLD KNOWLEDGE - short and catchy, said back in mimicry”

Against: The same spec says the code check supplements, never replaces, human sequence review (`grade3-reading/ti-courseplans/docs/instruction-modes-spec.md`, lines 59-60). The check runs only within a unit and has no baseline across units, so a unit's first lesson must assume nothing (`grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md`, lines 67-68). These are the doctrine's positions, with worked examples, not results measured here. The check supplements, never replaces, a person's review of the sequence (`ti-courseplans-audit/docs/instruction-modes-spec.md`), and the record of what each text introduces is still proposed (`ti-courseplans-audit/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md`). The drop was disclosed as a deliberate design choice: the later grade's lessons were written to stand alone rather than build on the grade before (`grade3-reading/artifacts/g5-course/CURRICULUM-REVIEW-STANDING-2026-08-17.md`, line 70).

<sub>criterion · sequence, alignment, evaluation · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Basics before optimisations

No optimisation, whether spacing, interleaving, multimedia or game elements, makes up for missing basics: unambiguous instruction, retrieval practice and mastery gating.

The delivery platform ranks learning mechanisms in tiers: faultless communication, retrieval practice and mastery gating at 90% accuracy or more come first; spacing, interleaving, worked examples and feedback amplify them once that foundation is solid; novelty, multimedia and gamification help only under specific conditions (`grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd`, `grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd`). It calls the first tier binary: no amount of the other tiers can compensate for a broken foundation, and features are liabilities where mechanisms are assets.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd` (77): “**Tip:** Tier 0 is binary. You either have faultless communication, retrieval practice, and mastery gating, or you do not. No amount of Tier 1 or 2 optimizations can compensate for a broken foundation. Features are liabilities; mechanisms are assets.”
- `grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd` (54): “Students do not progress without demonstrating ≥90% accuracy on rigorous assessments.”
- `g9/library/collections/codex-2026-10-02-curriculum-research/COVID-ERA-TEACHING-EVIDENCE.md` (13): “The Education Endowment Foundation's April 2020 rapid review drew on 60 systematic reviews and meta-analyses.”
- `g9/library/collections/codex-2026-10-02-curriculum-research/COVID-ERA-TEACHING-EVIDENCE.md` (13): “It found teaching quality, clear explanations, scaffolding and feedback more consequential than the delivery clock; no clear difference between synchronous and asynchronous teaching emerged in the reviewed evidence.”
- `g9/library/collections/codex-2026-10-02-curriculum-research/COVID-ERA-TEACHING-EVIDENCE.md` (13): “The EEF says the underlying research did not measure learning during a global pandemic and was often drawn from contexts unlike 2020 closures.”

Against: The ranking is the platform's own doctrine; nothing in these sources measures it.

<sub>criterion · practice, wording, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Block first, mix after a later retest

Practise a new skill on its own while it is being learned, and mix it into review only after it passes a retest on new items on a later day. A skill becomes eligible for mixing only after a retest at least 24 hours later on new parallel items.

The reading project's practice spec keeps a skill in blocked practice while it is being acquired and makes it eligible for interleaving only after a delayed (≥24h) retest passed on new parallel items; completion on the day of release never qualifies, because same-day testing measures working memory, not learning (`grade3-reading/ti-courseplans/docs/practice-layer-spec.md`). The course standard draws the same boundary, introducing interleaving only after prerequisite acquisition is secure and listing same-day success called durable as a failure signal (`grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd`, Q024). In mixed review, no two items in a row are on the same skill.

Quoted:

- `grade3-reading/ti-courseplans/docs/practice-layer-spec.md` (37-40): “**Interleaving eligibility = E2-cleared**: a delayed (≥24h) retest passed on *new* parallel items — release-day completion never qualifies”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (433): “- Claim boundary: Interleaving is introduced only after prerequisite acquisition is secure.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (160): “- Interleaving is only appropriate after the skill is ready; massed/blocked first, interleaved later.”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (37): “Blocked practice while a skill is in acquisition.”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (38-40): “a delayed (≥24h) retest passed on *new* parallel items — release-day completion never qualifies (Practice BrainLift: same-day testing measures working memory, not learning)”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (40-41): “Cumulative interleaved review keeps every cleared track alive, no two consecutive items on the same skill”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D6-practice-durable-mastery.md` (17): “An item joins cumulative review only after a delayed (≥24h) retest passed on NEW parallel items; release-day success never qualifies”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D6-practice-durable-mastery.md` (18): “Practice is blocked while a skill is in acquisition; interleave only post-E4; no two consecutive same-skill items”
- `grade3-reading/knowledge_bot/knowledge/kb-0122-g3-reading-course-graph.qmd` (53): “**Gateway discriminations** (taught explicitly, interleaved after both learned)”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (605): “### G5-POL-PRA-010: Admit an operation to interleaved review only after a delayed retest on new parallel items has cleared it, and never place two consecutive review items on the same operation.”

Against: The Grade 3 criteria differ on the stage: one row admits an item to mixed review after the delayed retest, another interleaves only after the later mastery stage (`ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D6-practice-durable-mastery.md`, D6.6 and D6.7). These are design rules, not results: nothing here measured the effect of the order, and the course graph is a draft pending rulings (`grade3-reading/knowledge_bot/knowledge/kb-0122-g3-reading-course-graph.qmd`).

<sub>criterion · practice, sequence, evidence-of-learning · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Bounded choices in every lesson

Build a few bounded, meaningful choices into every lesson, such as which text or question comes first and how to respond, so learners bring their interests into it. The video's guidance is five choices in every lesson, not once a day.

An IES video on improving reading comprehension from kindergarten to grade 3, quoted in a reading course's review standard, recommends five choices every lesson rather than once a day, because choice brings the student's interests, competencies and self into the lesson (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/motivation-levers.md`). The standard's design gives each lesson a fixed set of bounded choices, which text from a curated set, which part to read first and how to respond, so their presence can be audited, and never offers a free choice of anything to read. It is practice guidance in a video, not a trial result.

Quoted:

- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/motivation-levers.md` (17): “Good teachers are giving five choices every lesson; not just once a day, but every lesson five choices brings the student's interests, the student's competencies, the student's self into the lesson.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/motivation-levers.md` (41): “every lesson exposes a fixed set of bounded choices — which text (from a curated set), which part to read first, response mode (say / draw / type)”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/motivation-levers.md` (41): “choice is constrained, never "read anything."”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (110): “A meta-analysis of 41 studies found choice raised intrinsic motivation, effort, task performance and perceived competence.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (110): “The effect was strongest with 2–4 successive choices and weaker for adults than for children.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (113): “Offer a small number of meaningful choices: which text or question first, typed or spoken answer, hint now or later, audio on or off.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (32): “Give students real decisions: which question to tackle, when to move on, whether to hear audio.”

Published: [Improving Reading Comprehension in Kindergarten Through 3rd Grade, Part 5, IES video](https://www.youtube.com/watch?v=YatVvz66jPs) · [Patall, Cooper & Robinson 2008](https://doi.org/10.1037/0033-2909.134.2.270) · [Eccles, Midgley, Wigfield et al. 1993](https://doi.org/10.1037/0003-066X.48.2.90)

Against: The effect was weaker for adults than for children, and the stage-environment-fit source was read only as an abstract summary because its full text was blocked (`othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md`, lines 110 and 30).

<sub>criterion · practice · universal · from g3, g9, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Build up to the target's length

Build practice up to the length and load of the performance it prepares for, because mastering short pieces one at a time does not build sustained work. One course's passages ran 58 to 217 words, while the test it prepared for presents up to roughly 2,740 words.

A course review found a Grade 3 course's passages ran 58 to 217 words, while the state test it prepares for presents up to roughly 2,740 words across two single passages and one paired set, so a child could master the whole course one short snippet at a time and never sustain attention across a multi-passage block (`grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md`). It asked for longer passages and paired-text sets that build toward test length and real-world reading.

Quoted:

- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (69): “A child can master the whole course one short snippet at a time and never once sustain attention across a multi-passage block.”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (71): “***To change this:*** Add longer passages and paired-text sets that build toward test-length and real-world reading.”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (69): “Course passages run 58 to 217 words, averaging about 166”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (67): “STAAR presents up to roughly 2,740 words across two single passages and one paired set”
- `grade3-reading/course-renderer/docs/feedback/academics-review-2026-06-29.md` (72): “Course passages run 58 to 217 words, averaging about 166. A child can master the whole course one short snippet at a time and never once sustain attention across a multi-passage block.”
- `g9/sources/Cutting-a-Scene-Othello-1.1.pdf` (17-19): “The arc of the Folger Method builds from individual words and lines to longer texts, like speeches and scenes.”
- `grade3-reading/ti-courseplans/courses/g6-reading/G6-FORK-DECISION-BRIEF.md` (15): “median **272 words** (range 227–301) vs an 800–1200-word target.”
- `othello-course-renderer-draft/repo/docs/feedback/academics-review-2026-06-29.md` (72): “Course passages run 58 to 217 words, averaging about 166.”

Against: This is a review's judgment; nothing in these sources measured stamina.

<sub>criterion · practice, stimulus, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Check a meaning by swapping it in

Have learners check a meaning they worked out from context by swapping it into the sentence: if the sentence no longer makes sense, the meaning is wrong. One five-step procedure for working out a word's meaning ends on the swap-in check, done by the learner.

The Grade 3 reading curriculum's procedure for working out a word or phrase, quoted in the reading course renderer, has five student-facing steps: spot the word, look inside it, look around it, try a meaning, then check by swapping the meaning into the sentence to see whether it still makes sense, a step the child does (`grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md`, lines 417-423). Its correction route sends a learner back to the swap, and if the sentence doesn't make sense the meaning is wrong and they try again from the fourth step (lines 497-499). The curriculum's rulings kept all five steps because the swap-in check is real work (line 860). It is a design rule; nothing measured its effect.

Quoted:

- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (423): “| 5 | Check by swapping in (CHILD) | "I swap my meaning into the sentence. Does the sentence still make sense?" |”
- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (497): “Return to Step 5: "Swap your meaning in. Does the sentence still make sense?"”
- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (499): “If it doesn't make sense, the meaning is wrong - try again from Step 4.”
- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (860): “DECODE keeps its five steps (its Step 5, the swap-in check, is real work).”

Against: none found

<sub>criterion · practice, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Check understanding with a task

Decide whether a learner has understood from what they do on a task, not from their own sense of it, because readers judge their own comprehension poorly.

A reading project's research synthesis quotes the RAND Reading Study Group: most child and adult readers have a poor ability to calibrate the success of their comprehension (App. A, pp. 108-109) (`ti-courseplans-audit/docs/reading-science/SYNTHESIS.qmd`). The project's practice criteria schedule review on accuracy and latency, not self-report (`ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D6-practice-durable-mastery.md`, D6.14).

Quoted:

- `ti-courseplans-audit/docs/reading-science/SYNTHESIS.qmd` (180-181): “"most child and adult readers have a poor ability to calibrate the success of their comprehension"”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D6-practice-durable-mastery.md` (25): “schedule on accuracy+latency, not self-report”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (164): “Students in both AI groups overestimated how much they had learned.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (167): “Don't treat students' own reports of learning as a success metric.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/SHARED-DECISIONS.md` (14): “A minimum dwell is a software prerequisite, not proof the child understood.”

Published: [RAND Reading Study Group 2002, Reading for Understanding: Toward an R&D Program in Reading Comprehension (MR-1465)](https://www.rand.org/pubs/monograph_reports/MR1465.html)

Against: none found

<sub>criterion · evidence-of-learning, practice · universal · from research, g3 · external-research · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Coherent texts to learn, cold texts to test

Sequence the texts learners study so taught knowledge recurs and builds, and base every scored test and transfer item on unseen, unrelated texts whose answers were never taught. Readers of a coherent text set gained 5.59 concept idea-units against 2.63 for unrelated texts over six texts in three days.

An outside review of a Grade 3 reading course found it sequenced as a Lexile staircase rather than a knowledge progression, with assessment passages kept off the taught topics by design, so knowledge was engineered out; it asked for learning texts in which taught knowledge recurs and compounds, with cold, non-overlapping passages kept for the test. In a randomised study, readers of a coherent text set gained 5.59 vs 2.63 concept idea-units (η²=.32) over six texts in three days. In a test or transfer item the same overlap would be a leak.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (70): “Sequence the learning texts so taught knowledge recurs and compounds, and reserve cold, non-overlapping passages for the test only, where that property belongs.”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (68): “by design ensures assessment passages never overlap taught topics so a student "can't pass on recall."”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (66): “Coherent-set readers gained 5.59 vs 2.63 concept idea-units (η²=.32) over six texts in three days”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (68): “The course is sequenced as a Lexile staircase, not a knowledge progression, and by design ensures assessment passages never overlap taught topics”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (68): “A child can find the main idea fifty times on fifty disconnected passages and never accumulate the knowledge that makes main ideas easy to find.”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (54): “Conceptually coherent text sets outperform unrelated texts for both knowledge and vocabulary growth”
- `grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd` (82): “use the curriculum to keep generative knowledge warm by use; use spaced practice for the residue.”
- `grade3-reading/knowledge_bot/knowledge/kb-0098-incept-service-coe-catchup-2026-07-09.qmd` (38-39): “knowledge-building can be gamed if later questions become answerable from earlier lessons without proving true comprehension”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (48): “knowledge transfer is near-domain at best … η²=.09”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (45): “***To change this:*** Sequence the learning texts so taught knowledge recurs and compounds, and reserve cold, non-overlapping passages for the test only, where that property belongs.”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (43): “by design ensures assessment passages never overlap taught topics so a student “can’t pass on recall.””
- `grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md` (66): “Whether dose-item overlap is teaching or leaking depends on item class — the same overlap is legitimate in an in-lesson knowledge check and a leak in a comprehension/transfer item”
- `grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md` (67): “It took five adversarial rounds to isolate this.”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (70): “Sequence the learning texts so taught knowledge recurs and compounds, and reserve cold, non-overlapping passages for the test only”
- `grade3-reading/knowledge_bot/knowledge/kb-0074-g3-reviewer-feedback-distilled-for-g5-2026-06-30.qmd` (81-82): “"Independent item claim_ids must be a subset of independent_claim_ids and disjoint from teaching_claim_ids"”
- `grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd` (32): “choice-hottext-20: plain-blind 0/3 but 3/3 with prior-lesson corpus”
- `grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd` (33): “Current Gemini 3.5 replay: 3/3 in both conditions - direct blind leak; old lift is historical.”
- `grade3-reading/knowledge_bot/knowledge/kb-0074-g3-reviewer-feedback-distilled-for-g5-2026-06-30.qmd` (87-88): “so whether it executes correctly at runtime is unverified, not just unapproved.”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (45): “Sequence the learning texts so taught knowledge recurs and compounds, and reserve cold, non-overlapping passages for the test only, where that property belongs.”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (43): “by design ensures assessment passages never overlap taught topics”
- `grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt` (25): “The passages jumped from e.g. the axolotl to shadows with no visible link, there is no pre-teaching of key ideas, and no strategy is revisited at greater depth.”
- `grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/03-transfer-practice-layer.md` (59): “do not use cold passages as the main teaching surface;”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (296): “is the last scaffold, and like every other scaffold it fades gradually”
- `ti-courseplans-audit/docs/teaching-reading-comprehension-brainlift.md` (130-131): “Coherent-set readers gained 5.59 vs 2.63 concept idea-units (η²=.32) over six texts in three days (Cervetti 2016, pp. 769–771).”
- `ti-courseplans-audit/docs/teaching-reading-comprehension-brainlift.md` (132-133): “The largest Cervetti effect was *incidental* vocabulary: η²=.625, no meanings taught, target words recurring ~6× across the set (pp. 766–772).”
- `ti-courseplans-audit/docs/course-formula-agents.md` (166): “Cold plain text belongs at the *test*, not throughout learning; sequence passages so knowledge recurs and compounds”
- `ti-courseplans-audit/docs/reading-science/sources.qmd` (18): “DOI: 10.1007/s11145-016-9628-x”
- `ti-courseplans-audit/docs/reading-science/SYNTHESIS.qmd` (186-188): “N=59, one rural school, on-grade readers, 3-day intervention, null (unreliable) comprehension-questions measure, and "it is not clear whether the same effects would be observed using texts that merely cohered around the same topic"”
- `ti-courseplans-audit/docs/teaching-reading-comprehension-brainlift.md` (89-90): “knowledge transfer is near-domain at best (Cervetti η²=.09)”
- `grade3-reading/ti-courseplans/docs/course-formula-agents.md` (166): “then made passages cold and non-overlapping *throughout learning*”
- `grade3-reading/ti-courseplans/docs/course-formula-agents.md` (166): “Cold plain text belongs at the *test*, not throughout learning; sequence passages so knowledge recurs and compounds”
- `grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd` (62-65): “59 fourth graders randomly assigned to read six texts that either cohered around bird concepts or spanned six unrelated topics — matched for total words, readability, and embedded target words.”
- `grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd` (69-70): “"For the total concept units, the main effect of treatment is significant in favor of the CC group, F(1, 56) = 26.84, p = .000, partial g2 = .324"”
- `grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd` (73-75): “the main effect of treatment is significant, F(1, 56) = 93.16, p = .000, partial g2 = .625." (p. 772) — despite the CC words being *rarer* in English.”
- `grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md` (132): “The largest Cervetti effect was *incidental* vocabulary”
- `grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd` (186-187): “N=59, one rural school, on-grade readers, 3-day intervention, null (unreliable) comprehension-questions measure”
- `grade3-reading/ti-courseplans/docs/practice-layer-spec.md` (127-128): “Topic knowledge is the vehicle, never the cargo.”
- `grade3-reading/knowledge_bot/knowledge/kb-0074-g3-reviewer-feedback-distilled-for-g5-2026-06-30.qmd` (79-80): “The **scored `item_bank`/independent claims stay disjoint from that on-ramp and from every teaching claim**”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (71): “The cold benchmark is **never a mastery gate and never teaching material**”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (71-72): “v1 is observe-only (results route to humans, not automated adaptation)”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (61): “sealed windowed diagnostic on never-taught topics, burn-after-serve”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (61): “a transfer *read*, not an impact claim”
- `ti-courseplans-audit/docs/instruction-modes-spec.md` (68-69): “Cold passages are never taught from — they are the practice layer's sealed benchmark.”
- `ti-courseplans-audit/skills/train-assessor/SKILL.md` (27-28): “passages with ZERO overlap with instruction (verified, the G4/G5 cold-finals property); parallel forms, disjoint.”
- `grade3-reading/ti-courseplans/docs/practice-layer-spec.md` (71): “The cold benchmark is **never a mastery gate and never teaching material**”
- `grade3-reading/ti-courseplans/docs/practice-layer-spec.md` (148-149): “a **contamination ledger** keeping cold-pool topics out of every lane's generation prompts is required tooling”
- `grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md` (71-72): “A model trained on a cold topic cannot be evaluated on it.”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json` (470): “Keep held-out assessment sources separate from lesson-visible teaching and practice sources.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md` (18): “| 10 | The public no-login test URL allows anonymous farming of the item bank |”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/05_LIMITATIONS.md` (118): “- Item security is weaker: students who take the test multiple times will see repeated items (mean pairwise between-session overlap 29.4%)”
- `grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/review/history/2026-07-27-review-preparation-projections.md` (17-18): “All 120 assessment candidates and 182 assessment/retry-only sources remain out of the learner projection.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (311): “use **original/obscure passages for *assessment*** (famous sources stay for *teaching*); and”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “transfer requires cold passages on never-taught topics and remains separate from course mastery or an impact claim.”
- `grade3-reading/ti-courseplans/handoff/timeback-course-explorer/brainlift/amalgamation-v2.md` (110): “So **"you always know what topic you're reading" is the last scaffold, and like every other scaffold it fades gradually, not at a cliff**”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/v0.2.md` (37): “MAP Science at G7 tests all four MS NGSS domains back-to-back without warning.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/v0.2.md` (40): “**Implication:** Units are domain-coherent for *acquisition*, but every weekly retrieval queue pulls items from ALL domains touched so far.”
- `g9/transcript/chat-transcript.redacted.txt` (2888): “Independent practice asks the student to evaluate a competing reading using textual evidence, followed later by an unfamiliar passage without the scaffold.”
- `grade3-reading/edullm-review-hub/course-packages/courses/apush/review/brainlift.html` (157-158): “held-out assessment sources remain separate from lesson-visible sources, keys remain reviewer-only, and retries require a different”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-3-feasibility.md` (116-117): “A passage a student decoded aloud in Band A/B is, by definition, **not cold** when it reappears in the Band-C”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/pedagogy-policy.json` (1789-1790): “Teaching from or gating on the cold pool contaminates the benchmark and turns transfer evidence into rehearsal evidence.”
- `othello-course-renderer-draft/repo/docs/extras/alpharead-fading-guidance.md` (62): “The cold text = the mastery diagnostic: known procedure + new content, current stage, inside the built knowledge web.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT1-VERTICAL-SLICE.md inside it) (38): “five scored MCQ/SAQ sources withheld from Lessons 1-7 so the checkpoint measures source transfer rather than recall of a modeled analysis;”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (417-418): “If a review lesson repeats assessment wording or shows the exact evidence path before a checkpoint, the score measures recognition.”

Published: [Cervetti, Wright & Hwang 2016](https://doi.org/10.1007/s11145-016-9628-x)

Against: The study took place in one rural school with fourth graders reading on grade level, and its gains were in topic knowledge, vocabulary and retelling of a new text; its comprehension-question scores were not significant. a project note warned that knowledge-building can be gamed if later questions become answerable from earlier lessons, and the store rates the transfer of knowledge as near-domain at best (η²=.09). Knowledge carried forward can answer a test item: in one historical gate run, an item no blind solver answered (0/3) was answered every time with the earlier lessons' texts (3/3) and was swapped, though a later replay with a newer model answered it blind as well. The later design's separation was verified only at design level, so whether it holds at run time was unverified. When the target test mixes unrelated texts, topic coherence is itself a scaffold to fade before the test, gradually rather than at a cliff (`grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md`). The study had 59 readers in one rural school over a 3-day intervention, its comprehension-question measure was null and unreliable, and it is not clear whether texts that merely share a topic would do the same (`ti-courseplans-audit/docs/reading-science/SYNTHESIS.qmd`); the BrainLift itself notes that knowledge transfer is near-domain at best (η²=.09). The study had 59 on-grade readers in one rural school over a three-day intervention, its comprehension-question measure was unreliable, and it is unclear whether texts that merely share a topic work the same way (`grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd`, lines 186-189). The course plans add that what carries over to a cold text is operations, vocabulary and format fluency, not topic knowledge: "Topic knowledge is the vehicle, never the cargo" (`grade3-reading/ti-courseplans/docs/practice-layer-spec.md`, lines 125-128). knowledge-building can be gamed if later questions become answerable from earlier lessons without proving comprehension, a concern raised at a meeting on 2026-07-09 (`grade3-reading/knowledge_bot/knowledge/kb-0098-incept-service-coe-catchup-2026-07-09.qmd`, lines 38-39). none found; the spec itself calls the benchmark a transfer read, not an impact claim (`ti-courseplans-audit/docs/practice-layer-spec.md`). A later run found counter-evidence (`othello-course-renderer-draft/repo/docs/extras/alpharead-fading-guidance.md`).

<sub>criterion · sequence, stimulus · universal · from g3, research · external-research · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Compare answers, catch a planted error

Give guided practice that compares and corrects: students pick the better of two responses and say why, or stop a model answer at a planted error and fix it. A replication with 390 students confirmed a delayed-test advantage for erroneous examples.

The Grade 9 lesson design specification has two such modes of guided practice: comparative judgement, where students see two responses side by side, pick the one that better answers the learning question and explain why, and an intercept mode, where a model answer writes itself out until the student stops it at the error, highlights the mistake and corrects it; it proposes recording each planted error so that errors are designed on purpose, not improvised (`grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd`). Its reading list grounds the first in adaptive comparative judgement (Pollitt 2012) and the second in studies of erroneous examples, whose larger follow-up with 390 students confirmed their delayed-test advantage (McLaren, Adams & Mayer 2015) (`grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd`).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (250): “Students see two responses side by side, pick the one that better answers the learning question, and explain why.”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (252): “The student stops it at the error, highlights the mistake and corrects it.”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (391): “So that errors are designed on purpose, not improvised.”
- `grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd` (305): “confirms the delayed-test advantage of erroneous examples.”
- `grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd` (305): “Follow-up/larger-N replication of the paper above (390 students)”
- `grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd` (306): “Underpins guided-practice mode 2, "comparative judgement" — pairwise pick-and-justify, exactly Pollitt's ACJ method”
- `g9/transformer/src/mechanics/compare-paragraphs.js` (1-2): “Compare two answers: comparative judgement. Two Grade 9 paragraphs answer the same question; the reader picks the … stronger and says why. The judge must choose the same paragraph with a clear margin, so there is one defensible pick.”
- `g9/transformer/src/mechanics/compare-paragraphs.js` (25): “other is weaker but honest: it retells or quotes without explaining. Neither contains a factual error about the text.”
- `g9/transformer/src/mechanics/compare-paragraphs.js` (15): “The reason is saved and never marked.”
- `g9/transformer/src/mechanics/compare-paragraphs.js` (57): “const state = { paragraph_A: item.paragraphs[0], paragraph_B: item.paragraphs[1] };”
- `g9/transformer/src/mechanics/compare-paragraphs.js` (61): “free of factual errors about the text it discusses?”
- `g9/transformer/v01/proof-2026-10-09.json` (259-262): “"id": "weaker-honest", "required": true, "verdict": "holds", "p": 0.6”
- `g9/transformer/v01/proof-2026-10-09.json` (531-534): “"id": "weaker-honest", "required": true, "verdict": "holds", "p": 0.72”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (170): “The student stops it at the error, highlights the mistake and corrects it. The model then carries on from the corrected version.”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (309): “And a column for the planted error in faded examples?”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (309): “So that errors are designed on purpose, not improvised.”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (310): “In the research, "faded examples" usually means steps removed for the learner to complete.”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (310): “mode is closest to "erroneous examples"”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (528): “Add "Lesson profile" and "Guided practice mode" columns? And a column for the planted error in faded examples?”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (529): “So that errors are designed on purpose, not improvised.”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (532): “In the research, "faded examples" usually means steps removed for the learner to complete.”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (168): “Students see two responses side by side, pick the one that better answers the learning question, and explain why.”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (306): “The model answer writes itself out with an "intercept" button. The student stops it at the error, highlights the mistake and corrects it. The model then carries on from the corrected version.”
- `g9/library/text/L9b6d99.txt` (309): “So that errors are designed on purpose, not improvised.”

Published: [McLaren, Adams & Mayer 2015](https://doi.org/10.1007/s40593-015-0064-x) · [Pollitt 2012](https://doi.org/10.1080/0969594X.2012.665354)

Against: The erroneous-examples studies taught decimals with a web-based tutoring system, not writing about a text (`grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd`), and the specification notes that in the research 'faded examples' usually means steps removed for the learner to complete, so its intercept mode is closer to erroneous examples (`grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd`).

<sub>criterion · practice, format · universal · from g9, research · external-research · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Compare two cases side by side

Teach a relationship by presenting two cases together with an explicit prompt to compare them; two cases met in turn without the prompt work no better than one.

Lesson research on teaching two episodes together found strong evidence that comparing two cases produces relational learning that one case does not. In the core study, children shown one standard took the object match, while those shown two standards together with a prompt to compare them took the relational match; those shown the two in sequence without a prompt preferred object matches, like those shown only one. The research cites a further study in which comparison training beat matched single-item training on learning and far transfer of relational categories, and concludes that a lesson built page by page must put both cases on one page with an explicit instruction to compare.

Quoted:

- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (413-418): “"preschoolers who were shown the two standards sequentially without a prompt to compare them preferred object matches, as did those who viewed only one standard. In contrast, those who saw the exemplars together, with a prompt to compare them, showed the same elevated relational responding" (Christie and Gentner 2010, https://cogdevsoc.org/wp-content/uploads/2016/12/Christie-Gentner-2010.pdf, journal version https://doi.org/10.1080/15248371003700015).”
- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (426-427): “The condition is the load-bearing part. Two cases read one after another, with no prompt to compare, performed no better than one case.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (419-420): “comparison training beat matched single-item training on both learning and far transfer of relational categories”
- `grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (409-411): “Christie and Gentner had preschoolers extend a label from a standard to either an object match or a relational match”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (409): “Comparing two cases produces relational learning that one case does not.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (413-416): “preschoolers who were shown the two standards sequentially without a prompt to compare them preferred object matches, as did those who viewed only one standard. In contrast, those who saw the exemplars together, with a prompt to compare them, showed the same elevated relational responding”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (418-420): “The general result holds beyond preschoolers: comparison training beat matched single-item training on both learning and far transfer of relational categories”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (426-427): “The condition is the load-bearing part. Two cases read one after another, with no prompt to compare, performed no better than one case.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (429-431): “What is needed is one page where both cases are present at once with an explicit instruction to compare”

Published: [Christie & Gentner 2010](https://doi.org/10.1080/15248371003700015) · [Comparison-training study on learning and transfer of relational categories, cited by DOI in the lesson research](https://doi.org/10.1037/a0031847)

Against: The core study, including its no-prompt condition, used preschoolers (`grade3-reading/course-renderer/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md`, lines 409-418); the wider claim rests on the comparison-training study the research cites.

<sub>criterion · format, sequence, demand · universal · from g3, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Compare within one text first

Before asking students to compare two texts, give them a single text that makes the comparison itself.

A curriculum map describes a compare-contrast text on birds and reptiles as a scaffolded within-text comparison that builds toward cross-text comparison later, and tags another lesson, in which students write their own comparison of four civilisations they have read about, as cross-text comparison (`downloads/_G3 curriculum Map.xlsx - Curric Map.csv`). This is a sequencing choice in one map; no outcome was measured.

Quoted:

- `downloads/_G3 curriculum Map.xlsx - Curric Map.csv` (46): “A scaffolded within-text comparison to build skills toward cross-text comparison later.”
- `downloads/_G3 curriculum Map.xlsx - Curric Map.csv` (76): “CROSS-TEXT COMPARISON (student writing) — RI.3.9 + W.3.2”
- `incept-package-hub/course-packages/courses/g5-reading/review/evidence/course-graph-guide.md` (177): “A reader needs a bounded account of each source's main ideas before combining contributions without blending them.”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures-g4-g5.md` (229): “Teach COMPARE here first, so the only new load is the compare move.”

Against: none found

<sub>criterion · sequence, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Condense a procedure used as a tool

When one procedure is used as a tool inside another's step, condense it to one sentence, and run it in full only when it is the procedure being modelled. Called inside a comparison step, a four-step main-idea procedure collapses to one sentence per text.

The procedure spec of a grade 3 reading course names two ways to combine procedures: a sequential chain, where one runs to its final step before the next starts, and a nested call, where a procedure used inside another's step collapses to a single sentence (`grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md`, line 30). Its example is a cross-text comparison step that calls the main-idea procedure, which then gives one sentence per text rather than its four steps. The rule sits among the spec's design principles.

Quoted:

- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (30): “The rule: if the whole procedure has its own modelling moment, run it in full. If it is a tool inside another procedure's step, condense to one sentence.”
- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (30): “CONNECT Step 2 for cross-text says "use MAIN IDEA" - the MAIN IDEA collapses to one sentence per text, not four steps.”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md` (30): “The rule: if the whole procedure has its own modelling moment, run it in full. If it is a tool inside another procedure's step, condense to one sentence.”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md` (30): “NESTED CALL: within a single procedure's step, another procedure is called as a micro-tool. Here, the called procedure collapses to a single sentence - do not run it in full.”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md` (30): “CONNECT Step 2 for cross-text says "use MAIN IDEA" - the MAIN IDEA collapses to one sentence per text, not four steps.”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md` (22): “Seven procedures cover every Standard Component used in this curriculum as a Modelling Moment target.”

Against: none found

<sub>criterion · sequence, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Count a reading already done

When a page repeats word for word a text the learner just finished reading, count that reading toward the page's reading hold rather than impose a second wait. After the fix, a page repeating a 203-word text armed its reading claim 3,414 ms after Next, where its source had set a separate 60-second hold.

In a Grade 5 lesson, a page with a 203-word passage held the learner for a reading time its source sets at 81 seconds, and the next page repeated the same text as a reference behind a separate 60-second hold; both figures came from the source, not from timing in a browser. The fix, scoped to Grade 5, lets a reading the learner actually completed earlier in the same lesson arm the repeated page's claim, matching only text of the same type with exactly the same words, and still requires the claim and the answer. A page visit, review-mode activity, a model button or a stored acknowledgment earns nothing, and a fresh direct visit or a new passage keeps its ordinary hold. After the fix the claim armed 3,414 ms after Next, and a fresh direct visit stayed held.

Quoted:

- `grade3-reading/ui-audit-2026-09-08/round-1/g5-u9/PROPOSALS.md` (43): “p5 contains203 words and a required reading gate, so self-read dwell is81seconds.”
- `grade3-reading/ui-audit-2026-09-08/round-1/g5-u9/PROPOSALS.md` (43): “p6 repeats the exact203-word text as a silent reference and adds a separate60second claim timer before its question.”
- `grade3-reading/ui-audit-2026-09-08/round-1/g5-u9/PROPOSALS.md` (43): “These are source-derived values, not measured elapsed browser results.”
- `grade3-reading/ui-audit-2026-09-08/round-1/g5-u9/PROPOSALS.md` (48): “For Grade5 only, arm a silent reference claim without a second dwell when the learner has actually completed the matching earlier reading in the current student lesson state.”
- `grade3-reading/ui-audit-2026-09-08/round-1/g5-u9/PROPOSALS.md` (49): “Do not derive it from visiting a page, the final receipt, unit completion, a model button, reviewer activity, or persisted walk acknowledgments alone.”
- `grade3-reading/ui-audit-2026-09-08/round-1/g5-u9/PROPOSALS.md` (50): “Start with exact same-type, same-text matching.”
- `grade3-reading/ui-audit-2026-09-08/round-1/g5-u9/PROPOSALS.md` (52): “A fresh direct p6 visit keeps the normal timer. A new passage, even if silent, keeps the normal timer.”
- `grade3-reading/ui-audit-2026-09-08/round-1/g5-u9/PROPOSAL-REVIEW-by-unit1.md` (39): “Eligibility must represent normal reading completion, not any generic done bit that could be set by review mode, a model, a page visit or persistence.”
- `grade3-reading/ui-audit-2026-09-08/round-4/CURRENT-RESULTS.md` (20): “G5 earned reading: actual U9 L1 p5 completion allowed the p6 claim without a second full dwell”
- `grade3-reading/ui-audit-2026-09-08/round-4/CURRENT-RESULTS.md` (20): “an armed claim 3,414 ms after Next”
- `grade3-reading/ui-audit-2026-09-08/round-4/CURRENT-RESULTS.md` (20): “Claim and independent answer were still required.”
- `grade3-reading/ui-audit-2026-09-08/round-4/CURRENT-RESULTS.md` (20): “Fresh direct p6 remained held.”

Against: A second reading can be intended: 'The choice to require rereading must be deliberate.' (`grade3-reading/ui-audit-2026-09-08/round-1/g5-u9/PROPOSALS.md`, line 41), and a review of the proposal noted that 'the explicit source-first claim contract can intentionally ask for rereading' (`grade3-reading/ui-audit-2026-09-08/round-1/g5-u9/PROPOSAL-REVIEW-by-unit1.md`, line 35).

<sub>criterion · sequence, integrity · universal · from g3 · measured · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Cut a scene to read it closely

Have learners cut a scene to half its length and defend the most important line they kept and the most useless one they cut: deciding what stays forces close reading. In one guide, groups cut a scene of roughly 200 lines to around 100.

A published classroom guide from the Folger Shakespeare Library, kept in the Grade 9 sources, holds that students asked to cut lines from any text must read closely to decide what stays and what goes (`g9/sources/Cutting-a-Scene-Othello-1.1.pdf`, pdftotext lines 3-4). Its groups read a scene aloud and cut it in half, from roughly 200 lines to around 100, keeping what they judge most important, and each student then writes a reflection defending the most important line saved and the most useless line cut (lines 45-54, 69-75 and 104-109). It is a practice guide, not a study, and gives no web address or DOI of its own.

Quoted:

- `g9/sources/Cutting-a-Scene-Othello-1.1.pdf` (3-4): “When students are asked to cut (omit, scratch out) lines from any text, they must do all kinds of close reading in order to make their decisions about what stays and what goes.”
- `g9/sources/Cutting-a-Scene-Othello-1.1.pdf` (45-46): “Explain that their job is to cut the scene in half: to shorten the scene without losing what is most important in the scene.”
- `g9/sources/Cutting-a-Scene-Othello-1.1.pdf` (52-54): “This complex scene, which opens the play Othello, is roughly 200 lines. Students’ cut scenes should be around 100 lines.”
- `g9/sources/Cutting-a-Scene-Othello-1.1.pdf` (105-107): “What is the most important line they saved? What makes this line so important to your scene? What is the most useless line they cut? Why was it useless in this scene?”
- `g9/sources/Cutting-a-Scene-Othello-1.1.pdf` (108-109): “Get students defending specific choices in this informal reflection”

Against: The guide reports no measured effect.

<sub>criterion · practice, demand · universal · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Dates limit what can cause what

Treat dates as limits on cause: mark each period, count a date usable only when its position matters to an argument, and use later events only for change or significance. A unit ending in 1607 had records carrying later events, which made items look plausible while testing the next unit.

An AP history course's design document calls chronology a reasoning constraint: dates bound what can cause what, and context may reach outside a prompt's period only if the response explains the relationship instead of smuggling later knowledge into the claim. It marks period boundaries on every lesson and assessment object and teaches three uses of time: evidence from inside the period, prior context, and later consequence only when the prompt calls for change over time or significance. Because students often know events as isolated cards, it builds timelines around what existed before, what operated during and what followed, and counts a date usable when the student can explain why its position matters to an argument. The course's audit of inherited records found a unit's records carrying events from after its end date, and ruled that later context be labelled and never required for the key.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (156-159): “Dates matter because they bound what can cause what. ... Context can reach outside a prompt period, but the response must explain the relationship instead of smuggling later knowledge into the claim.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (161-166): “The course makes period boundaries visible in every lesson and assessment object. It also teaches students to distinguish three uses of time: ... later consequence used only when the prompt calls for change over time or significance.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (316): “Students often know events as isolated cards.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (318-319): “The course builds timelines around relationships: what conditions existed before a development, what mechanism operated during it, and what consequences followed.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (322-323): “A date is considered usable when the student can explain why its position matters to an argument.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (52): “Propagated Unit 1 records include post-1607 events ... This creates period drift and can make an item look plausible while testing Unit 2 content. ... later context must be labeled and never required for the Unit 1 key.”

Against: none found

<sub>criterion · demand, alignment, sequence · domain · from ap · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Decoding first, comprehension by listening

For learners who can't yet decode, spend reading time on decoding and fluency and build comprehension by listening, since reading comprehension is decoding times language comprehension. One grade-1 plan set the typical reader's 60 words correct per minute against a threshold of 90, below which comprehension is very difficult.

A pedagogy red team on a second-grade plan applied the Simple View of Reading: reading comprehension is decoding times language comprehension, so when decoding is near zero, comprehension-item instruction multiplies against a near-zero factor and yields near-zero transfer (`grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md`, line 34). It called decode-first the correct sequence and fluency the mechanism that frees working memory for comprehension (the same file, lines 28 and 60). A grade-1 plan set the typical grade-1 rate of 60 words correct per minute against a threshold of 90 below which comprehension is very difficult, and concluded that its comprehension course must be led by oral language and listening comprehension, not cold text, and must size its claims to the learners decoding doesn't hold back (`grade3-reading/ti-courseplans/courses/g1-reading/brainlifts/v0.1.md`, line 40).

Quoted:

- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md` (34): “Reading Comprehension = Decoding × Language Comprehension. It is a *product*, not a sum. When decoding ≈ 0, the product ≈ 0 **regardless of language comprehension**.”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md` (34): “Adding comprehension-item instruction multiplies against a near-zero decoding factor and yields near-zero transfer.”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md` (28): “decode-first is correct science-of-reading sequencing”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md` (60): “Fluency is not a "strength to coast on"; it is the *mechanism* by which decoding stops consuming working memory so that comprehension becomes possible.”
- `grade3-reading/ti-courseplans/courses/g1-reading/brainlifts/v0.1.md` (40): “Comprehension is *"very difficult below 90 words correct per minute"*”
- `grade3-reading/ti-courseplans/courses/g1-reading/brainlifts/v0.1.md` (40): “but the G1 norm is only **60 WCPM**”
- `grade3-reading/ti-courseplans/courses/g1-reading/brainlifts/v0.1.md` (40): “so much of the typical G1 cohort sits *below the fluency at which cold-text comprehension instruction is even effective*”
- `grade3-reading/ti-courseplans/courses/g1-reading/brainlifts/v0.1.md` (40): “Consequence: a G1 comprehension course must be **oral-language / listening-comprehension-led**, not cold-text-led, and **size its MAP-reach claim to the non-decoding-gated fraction**.”
- `grade3-reading/ti-courseplans/courses/g1-reading/brainlifts/v0.1.md` (30): “**Note an unreconciled internal discrepancy:**”
- `grade3-reading/ti-courseplans/courses/g1-reading/brainlifts/v0.1.md` (43): “Audio supports learning; it never reads the scored item aloud.”

Published: [Decoding, Reading, and Reading Disability, Remedial and Special Education 7(1) (1986)](https://doi.org/10.1177/074193258600700104) · [The simple view of reading, Reading and Writing 2 (1990)](https://doi.org/10.1007/BF00401799)

Against: The grade-1 plan flags its own fluency targets as unreconciled across its references (`grade3-reading/ti-courseplans/courses/g1-reading/brainlifts/v0.1.md`, line 30), and it keeps audio off the scored check, so listening carries the teaching while the scored reading stays in print (the same file, line 43).

<sub>criterion · demand, accessibility, stimulus · universal · from research, g3 · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Develop ideas before polishing conventions

Where a writing rubric gives an undeveloped response no credit for conventions, teach learners to develop and organise ideas before polishing conventions. In one state test's Grade 3 essay rubric, scored 0 to 3 for development and 0 to 2 for conventions, a 0 for development forces a 0 for conventions.

A research report on a state reading test's Grade 3 writing task, kept in a reading course's documentation, quotes the scoring guide's interaction rule: a response scored 0 for development and organisation of ideas also earns 0 for conventions (`othello-course-renderer-draft/repo/docs/extras/alpharead-staar-writing-research.md`, line 102). The course's Grade 3 writing scaffold, grounded in that report, makes development the gatekeeper: build ideas first, conventions last (`othello-course-renderer-draft/repo/docs/extras/alpharead-writing-scaffold-overview.md`, line 20). The order follows from how that rubric scores, and nothing here measured what teaching in this order does.

Quoted:

- `othello-course-renderer-draft/repo/docs/extras/alpharead-staar-writing-research.md` (102): “> "…if a response receives a score point 0 in the Development and Organization of Ideas trait, the response will also earn 0 points in the Conventions trait."”
- `othello-course-renderer-draft/repo/docs/extras/alpharead-staar-writing-research.md` (28): “Development & Organization of Ideas (0–3) + Conventions (0–2) = 0–5 per scorer”
- `othello-course-renderer-draft/repo/docs/extras/alpharead-writing-scaffold-overview.md` (20): “with **Development as the gatekeeper** — build ideas first, conventions last.”
- `othello-course-renderer-draft/repo/docs/extras/alpharead-staar-writing-research.md` (104): “a fully developed essay (Dev 3) can still earn Conventions 0 if it's one giant run-on”
- `grade3-reading/course-renderer/docs/extras/alpharead-staar-writing-research.md` (102): “if a response receives a score point 0 in the Development and Organization of Ideas trait, the response will also earn 0 points in the Conventions trait.”
- `grade3-reading/course-renderer/docs/extras/alpharead-staar-writing-research.md` (104): “The reverse is not true: a fully developed essay (Dev 3) can still earn Conventions 0 if it's one giant run-on; a thin essay (Dev 1) can earn Conventions 2 if clean. **Development is the gatekeeper.**”
- `grade3-reading/course-renderer/docs/extras/alpharead-writing-scaffold-overview.md` (20): “Grounded in the Grade 3 STAAR RLA research: the essay rewards **Development & Organisation of Ideas (0–3) + Conventions (0–2)**, with **Development as the gatekeeper** — build ideas first, conventions last.”
- `grade3-reading/course-renderer/docs/extras/alpharead-staar-writing-research.md` (12): “Not our course, and Texas-specific.”

Published: [Texas Education Agency 2025, STAAR Grade 3 RLA Constructed-Response Scoring Guide, Spring 2025](https://tea.texas.gov/student-assessment/staar/2025-staar-rla-3-released-test-scoring-guide.pdf)

Against: The rule runs one way only: the same report notes that a fully developed essay can still earn 0 for conventions if it is one long run-on (`othello-course-renderer-draft/repo/docs/extras/alpharead-staar-writing-research.md`, line 104), so conventions still need teaching once ideas are developed. The rubric is one state's, and the report calls itself Texas-specific (line 12).

<sub>criterion · sequence, scoring-guide · domain · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Dialogue and refutation beat exposition

Where there is time, explain through a dialogue that answers a learner's questions, or by refuting the wrong idea, rather than by straight exposition. In one study of 364 students, a dialogue version beat straight exposition by an effect size of 0.83 and a refutation version by 0.79.

An intro-video BrainLift for a Grade 3 reading course reports Muller, Bewes, Sharma and Reimann (2008): 364 students met the same physics content in four formats, a dialogue version beat straight exposition at d = 0.83 and a refutation version at d = 0.79, and the lowest-prior-knowledge students gained most (`downloads/BrainLift - What makes a good intro video.md`, line 471). The same document calls two voices, one asking as a learner and one answering, the gold standard for its videos (lines 303 to 305). The source names the study without a link; its DOI was found on Crossref.

Quoted:

- `downloads/BrainLift - What makes a good intro video.md` (471): “dialogue version beat straight exposition at d \= 0.83; the refutation version at d \= 0.79. Lowest-prior-knowledge students gained most.”
- `downloads/BrainLift - What makes a good intro video.md` (471): “364 students, the same physics content in four formats.”
- `downloads/BrainLift - What makes a good intro video.md` (307): “Below that threshold, use a single knowledgeable narrator and put the modelled thinking in the lesson, where there is room for it.”

Published: [Muller, Bewes, Sharma & Reimann 2008](https://doi.org/10.1111/j.1365-2729.2007.00248.x)

Against: For media under a minute the same document prefers a single voice, since a dialogue needs three turns for one idea and is too rushed below about 60 seconds (`downloads/BrainLift - What makes a good intro video.md`, lines 307 and 426).

<sub>criterion · format, media · universal · from g3, research · external-research · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Distinct AI roles, one moderator

Give each AI voice in a multi-voice discussion a distinct role and put one moderator in charge of turn order, since extra voices helped only once their roles differed. Removing the AI classmates from one moderated classroom system cut student participation by a reported 26.5% and 45.2% on two engagement measures.

Notes on a proposed discussion with several AI voices found that distinct agent roles beat a single generic agent or an undifferentiated panel: earlier multi-agent work found more agents helped only once roles differed, and a 2025 small RCT again found role identity, not agent count, drove the effect (`g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/idea-02-ai-classmates-multi-agent-debate.md`, lines 15-23). In an LLM classroom of teacher, assistant and classmate agents tested online with 400+ students, removing the classmates cut participation by a reported 26.5% and 45.2% on two engagement metrics, in a system that also has a moderator governing turn order so classmates don't crowd the student out (lines 34-39). The project's synthesis concluded that gains come from distinct roles plus a moderator, not from more voices (`g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/IDEA-SYNTHESIS.md`, line 16).

Quoted:

- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/idea-02-ai-classmates-multi-agent-debate.md` (15): “**1. Distinct agent *roles* beat a single generic agent or an undifferentiated panel.**”
- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/idea-02-ai-classmates-multi-agent-debate.md` (20-21): “A 2025 ACM study retesting this with modern conversational agents again finds role identity, not agent count, drives the effect **(small RCT)**.”
- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/idea-02-ai-classmates-multi-agent-debate.md` (21-23): “Earlier multi-agent work ("Togetherness," 2014) found *more* agents helped only once roles differed — extra undifferentiated voices did not reproduce the gain **(small observational study)**.”
- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/idea-02-ai-classmates-multi-agent-debate.md` (36-38): “Removing the classmate agents cut student participation substantially (reported 26.5%/45.2% drops on two engagement metrics) — but the system also has an explicit "class control mechanism" (a moderator governing turn order) so classmates don't crowd the student out”
- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/IDEA-SYNTHESIS.md` (16): “Gains come from **distinct roles plus a moderator**, not from more voices”

Published: [Togetherness: Multiple Pedagogical Conversational Agents (2014)](https://link.springer.com/chapter/10.1007/978-3-319-07221-0_14) · [Do Pedagogical Agent Roles Matter? (2025)](https://doi.org/10.1145/3806774.3827972) · [Zhang et al. 2025, SimClass](https://arxiv.org/abs/2406.19226)

Against: The moderator half is a design inference: the ablation removed the classmate agents, not the moderator, and the notes tag the result as a field study and ablation in a preprint, not independently replicated (`g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/idea-02-ai-classmates-multi-agent-debate.md`, lines 36-39). No study tests a live, voice-based debate among several AI voices about literature with learners aged 13 to 18 directly (the same file, line 146).

<sub>criterion · format, practice · universal · from research, g9 · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Drama work as a sustained sequence

Run drama-based literacy work as a sustained, guided sequence over several hours rather than a single task, since its measured effects are larger that way. A meta-analysis of 42 reports and 200+ effect sizes found larger effects when the work was teacher-led over multiple hours.

Notes on a proposed student performance task found most support for performance pedagogy institutional or self-reported, and named as the strongest evidence a meta-analysis of 30 years of research on drama-based pedagogies and K-12 literacy outcomes: 42 reports, 200+ effect sizes and a significant positive effect on achievement, attitude and motivation, larger when teacher-led over multiple hours than as a single task (`g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/video-04-student-performance-gallery.md`, lines 15-30). A Readers' Theatre meta-analysis of 11 studies with ages 6-12 found a large effect on reading skills (lines 30-33). The notes therefore made a one-off performance task an optional extension that earns a bigger role over several lessons (lines 99-101).

Quoted:

- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/video-04-student-performance-gallery.md` (29-30): “significant positive effect on achievement/attitude/motivation, **larger when teacher-led over multiple hours, not a single task** — strength: **meta-analysis** ([ERIC](https://eric.ed.gov/?id=EJ1275486)).”
- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/video-04-student-performance-gallery.md` (100-101): “favors sustained, repeated performance practice over a single one-off task”

Published: [Lee, Enciso & Brown 2020, The Effect of Drama-Based Pedagogies on K-12 Literacy-Related Outcomes](https://eric.ed.gov/?id=EJ1275486) · [Mastrothanasis, Kladaki & Andreou 2023, Readers' Theatre meta-analysis](https://www.sciencedirect.com/science/article/pii/S2666374023000183)

Against: "No Shakespeare-specific or Grade-9-specific trial of a filmed-performance-gallery task was found." (`g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/video-04-student-performance-gallery.md`, line 128), and the Readers' Theatre evidence is elementary-age, so transfer to Grade 9 is an inference (lines 31-33).

<sub>criterion · sequence, practice · universal · from research, g9 · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Each stage on fresh material

Run the worked example, the guided practice and the independent task on different material, so no stage answers another and the last one tests transfer, not rehearsal.

The lesson-components spec sets independent practice on a different, later passage than the worked example used, and the lesson designs check it in their soundness sweeps: one runs the same procedure on a different section of a story, with fresh evidence, and a science lesson models on one section and re-runs the procedure on another. A rebuilt lesson placed its added guided station in a third setting so that it pre-answers neither the model nor the independent task, and its walkthrough gives the reason: repeating on the same evidence is rehearsal, and new evidence is transfer. A history lesson adds that independent practice is released only once the worked model and its completed analysis are taken away.

Quoted:

- `downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx` (31 (textutil text)): “Independent practice on a different, later passage than the Modelling Moment used.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx` (334 (textutil text)): “Same FIND rail, different section, fresh evidence.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx` (130 (textutil text)): “The teacher models the full FIND rail on the roots/stem/leaves section (the "I do"). Part 3 re-runs it independently on the seeds/flowers section.”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (227): “so it pre-answers neither the model nor the independent task”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (34): “Repeating on the same evidence is rehearsal; new evidence is transfer”
- `grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/lesson-01.json` (127): “Release only after the worked model and its completed analysis are removed.”
- `grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/lesson-01.json` (128): “The model uses a cross-period timeline and the guided task uses an imperial comparison; independent work shifts to a regional matrix that has not been modeled.”
- `grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md` (26): “The I-do/we-do/you-do routine is misapplied: I-do reveals the answer instead of modeling thought; we-do is only a hint; you-do sometimes switches to a different skill.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (60): “The I-do/we-do/you-do routine is misapplied: I-do reveals the answer instead of modeling thought; we-do is only a hint; you-do sometimes switches to a different skill.”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (57): “the we-do walks the same steps with immediate feedback, the you-do releases the same skill”
- `g9/transformer/test/threejs-render.test.mjs` (79): “never the model's quote or a guided one”
- `g9/transformer/test/threejs-render.test.mjs` (186): “never the model's quote”
- `g9/transformer/src/glue/threejs-render.js` (207): “the student's quote: lines the lesson's blocks found for the question, never the model's or a guided quote”
- `g9/transformer/src/glue/threejs-render.js` (212): “Quote options (not locked)”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/INTEGRATION-LESSONS.md` (21): “Change the evidence or problem so independent work requires transfer; label invented scenes separately from literary quotations.”
- `grade3-reading/curriculum-gen/audits/PETER-PAN-AUDIT-2026-08-24.md` (287-288): “The skill is related, but the named independent target is over-scaffolded.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/provenance/DECISIONS.md` (40): “Model INFER on London/Lost Boys; guide on fresh evidence; independently infer Neverland/Hook.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/TEACHING-ASSESSMENT-CONTRACT.md inside it) (41-44): “5. **Independent application:** Give new evidence and require the student to perform the named move, not copy the model's conclusion or locate a paraphrase. The independent evidence span, row, case, or source must differ from the completed model and guided answer; merely changing the prompt over the same solved evidence does not count as release.”
- `g9/transcript/chat-transcript.redacted.txt` (4386): “Independent writing introduced as “Now you think alone,” with the model’s quotation locked so the student chooses another.”
- `g9/transcript/chat-transcript.redacted.txt` (3103): “Mimicry: the Expert models how delivery and context affect meaning using a separate short exchange.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/UNIT.md` (269-270): “Six of the seven lessons had some form of it;”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/CONTENT-SCHEMA.md` (536-537): “So the row the child fills is a row Scout never filled, and the fact they must produce was never on the screen.”
- `g9/sources/_KB_Othello_1_1_Lesson_View.md` (8): “Stems available, but students are locked out of writing about the guided practice quote.”
- `othello-archive/sources/l1-script/Othello Lesson 1 (1.1)_ Lesson Script v3, Stage 1.txt` (143): “The stems stay available, but the guided practice quote is locked.”
- `g9/library/text/L02a442.txt` (8): “Stems available, but students are locked out of writing about the guided practice quote.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (411): “The guided model and independent task use different evidence.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (516-517): “Models and guided practice may show complete reasoning on teaching evidence. Independent work must not be a keyed paraphrase of that model.”
- `grade3-reading/artifacts/pp3-v3-design.txt` (301): “Merciless is the Independent-Task payoff (Hook), never the model (children being brave), so it does not pre-answer the model.”
- `grade3-reading/artifacts/Peter-Pan-L4-review-response-2026-08-25.pdf` (p.4 (pdftotext line 205)): “So the I-do models on London and the you-do transfers to Neverland by design.”
- `grade3-reading/.claude/skills/one-perfect-lesson/SKILL.md` (50-51): “answer-distance, verbatim-quote, and fresh-evidence-Phase-3 rules”

Against: The spec is a design: its package says it does not establish runtime verification, student readiness or evidence of learning outcomes (`grade3-reading/edullm-review-hub/course-packages/courses/apush/review/evidence/case-for-review.md`).

<sub>criterion · practice, integrity, sequence · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Each text builds on the last

Each text in a unit should need only knowledge an earlier text added or the unit states as entry knowledge. In one four-text unit the last text assumes four knowledge items, all added by the three texts before it.

A four-text knowledge-building unit was designed from an inventory of what each text assumes and adds, each item tied to the words that carry it, with the entry knowledge the theme assumes and a check that every text's assumptions are covered by earlier texts or entry knowledge, with no forward references (`grade3-reading/artifacts/demo-unit-2026-07-10/00-knowledge-inventory.md`). Its texts ramp from primer to build to deepen to a transfer text with less topical overlap and the same schema (`grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md`), and the unit is assessed on an unseen text that exercises the schema, teaches nothing new and avoids the curriculum-staple example (`grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/passage.md`). A review of a story course checks the same thing for characters and places, each introduced before its first use (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-arc-continuity.md`). The unit's test should be an unseen text that uses the same knowledge on a new surface and teaches nothing new; in that unit the transfer text adds four knowledge items on the same schema and the test text adds none.

Quoted:

- `grade3-reading/artifacts/demo-unit-2026-07-10/00-knowledge-inventory.md` (8): “Proposed adds / assumes per text, with carrying spans.”
- `grade3-reading/artifacts/demo-unit-2026-07-10/00-knowledge-inventory.md` (20): “## Entry knowledge (theme assumes; no text teaches these)”
- `grade3-reading/artifacts/demo-unit-2026-07-10/00-knowledge-inventory.md` (95-96): “Compounding check: every text's assumes are covered by earlier texts' adds or entry knowledge; no forward references.”
- `grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md` (17): “Ladder note: the ramp is primer -> build -> deepen -> transfer-neighbor.”
- `grade3-reading/artifacts/demo-unit-2026-07-10/00-knowledge-inventory.md` (83): “Adds (cluster 1, transfer rung -- reduced topical overlap, same schema):”
- `grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/passage.md` (8): “- role: capstone-unseen (assessment text; NOT a teaching text -- exercises the acquired schema, teaches no new KC)”
- `grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/passage.md` (14): “P6 (an invented flood-plain farm town, not the curriculum-staple Nile/Mississippi delta)”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-arc-continuity.md` (32): “### L5 characters and places — introduced before first use?”
- `grade3-reading/artifacts/demo-unit-2026-07-10/00-knowledge-inventory.md` (5-6): “do not promote candidate IDs or the sandbox spine into approved curriculum doctrine.”

Against: A sandbox design, not approved doctrine: the inventory says not to promote its candidate ids or sandbox spine into approved curriculum doctrine (`grade3-reading/artifacts/demo-unit-2026-07-10/00-knowledge-inventory.md`).

<sub>criterion · sequence, evidence-of-learning, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Early practice doesn't look like the test

Spend most of a course teaching and building knowledge rather than drilling the final test, keeping test-format practice to set points late in the sequence.

The evaluation gauntlet in one course-plan program runs a marathon-rule probe on reading courses: early practice should mostly not look like the test but be vocabulary in context, monitoring prompts and knowledge work, with test-format practice concentrated late and timed conditions last (`ti-courseplans-audit/skills/train-teacher/references/gauntlet-spec.md`). The reading-comprehension BrainLift in the same work holds that assessment format is not instruction format (`ti-courseplans-audit/docs/teaching-reading-comprehension-brainlift.md`). The Grade 3 reading criteria require knowledge-building activity that looks nothing like the paragraph-plus-questions test (`ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D7-knowledge-first-curriculum.md`), and the practice-layer spec has format fluency taught as the operations each format demands of the text, never drilled (`ti-courseplans-audit/docs/practice-layer-spec.md`). Timed conditions come last, and test-format practice is framed as practice, never as instruction.

Quoted:

- `ti-courseplans-audit/skills/train-teacher/references/gauntlet-spec.md` (32-34): “**Marathon-rule probe** (reading): does early practice look like the test? (It mostly shouldn't — vocabulary-in-context, monitoring prompts, knowledge work; test-format practice concentrated late, timed conditions last.)”
- `ti-courseplans-audit/docs/teaching-reading-comprehension-brainlift.md` (119-120): “Assessment format is not instruction format (the marathon rule), and acquisition mastery is not durable mastery — they need different instruments”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D7-knowledge-first-curriculum.md` (18): “Knowledge-building activity looks nothing like the paragraph-plus-questions test (marathon-training analogy)”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (12-13): “format fluency **taught** through the instruction modes as named cognitive operations (what work each format demands of the text), never drilled.”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (366-367): “verdict = "a well-built MAP-practice engine, **not** a comprehension curriculum."”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (227-229): “G3 course strategy is **teaching-based, not drill-based** — practice tests only at specific intervals;”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (290-291): “MAP/practice apps must stay framed as practice/assessment, not instruction.”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (50): “Assessment format is not instruction format (the marathon rule), and acquisition mastery is not durable mastery — they need different instruments”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/COURSE-PLAN.md inside it) (67): “Units 6-8: visual and quantitative evidence, full LEQ/DBQ practice, and timed mixed work.”
- `grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/prompts/u08.md` (116): “U8·L19 — Period 8 Synthesis: Continuity, Change, and a Complete Timed LEQ”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT1-VERTICAL-SLICE.md inside it) (37): “three required sourced SAQs, nine scored parts total: secondary text, primary text, and primary non-text;”

Against: A later run found counter-evidence (`grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz`).

<sub>criterion · practice, format, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### End each reading by using its meaning

End each reading with a task that does something with the meaning, such as applying it, critiquing it or taking a position, not only with answering items.

A reading quality canon of 518 rules makes it one of its 13 priority-one rules that each reading ends in a task that does something with the meaning: apply it, critique it, make or solve something, or take a position, not only answer items. Its reason is that comprehension is not finished until the reader has done something with what was understood. Applied to a grade 5 lesson, the canon notes that the bar rises there to taking a position, critiquing and applying.

Quoted:

- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (110): “Each reading ends in a task that *does something* with the meaning — apply it, critique it, make/solve something, take a position — not only answer items ("comprehension is not finished until the reader has done something with what was understood").”
- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (109): “**RULE_G3_D13.1** (P1, READING_G3)”
- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (3): “the 518-rule canon per `MANIFEST.json`: 13 priority-1 + 505 priority-2 rules”
- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (111): “The reading should end in doing something with the meaning; at G5 the bar rises (take a position, critique, apply).”

Against: none found

<sub>criterion · format, demand, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Every task adds to one visible piece

Make every small task visibly add to one artifact the learner is building, such as a paragraph that fills as they work, so no step feels like a separate task. In one prototype, three quote break-down conversations finished and left no artifact.

A review of a Grade 9 lesson prototype named a lot of little tasks that never came together as its most persistent finding across two units, and traced it to tasks that end without producing anything the learner can see. It set as a rule that every small task should visibly be part of one thing being built. In its rebuild of independent practice the paragraph fills as the learner works and stays visible throughout, which it names as what makes the small tasks cohere. The prototype's modelled-paragraph screen, which visibly builds a paragraph, was already the working case.

Quoted:

- `g9/sources/Othello_1_Feedback_DevFactory.md` (23): “This pass identifies the mechanism: tasks end without producing anything the child can see.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (25): “Every small task should visibly be part of one thing being built. If a step produces nothing the child can point at, it will feel like a task rather than part of a lesson, however good the step is.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (333): “The paragraph fills as the student works, and is visible throughout. This is what makes the small tasks cohere.”
- `g9/library/text/L36b8ba.txt` (25): “Every small task should visibly be part of one thing being built. If a step produces nothing the child can point at, it will feel like a task rather than part of a lesson, however good the step is.”
- `g9/library/text/L36b8ba.txt` (23): “This pass identifies the mechanism: tasks end without producing anything the child can see.”
- `g9/library/text/L36b8ba.txt` (125): “Make the paragraph visible as it fills, so the task produces one artifact.”
- `g9/library/text/L36b8ba.txt` (333): “The paragraph fills as the student works, and is visible throughout.”

Against: none found

<sub>criterion · sequence, practice · universal · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Example and non-example differ once

Pair an example with a non-example that differs only in the defining feature, and say why the non-example fails by naming that feature, never an incidental property. In one course, 53 of 58 vocabulary non-examples gave no reason why they were not examples.

The reading course's static content audit found 53 of 58 vocabulary non-examples stating no reason they were not examples (`grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md`, line 396). A red-team addendum made the very different second example required, because the minimally different pair marks the boundary but only the very different example stops the over-generalisation the pair invites, and required a non-example's reason to name the defining method after one non-example made being big disqualifying (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md`, lines 150-170). A generic instruction BrainLift gives the variation rule behind it: vary surface features with the distinction held constant, or the distinction with surface features held constant, never both on one item. Choose the examples and non-examples so that only one rule fits. Add genuinely different examples and a boundary case that show where the concept stops applying.

Quoted:

- `grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md` (396): “| **S1** | Every vocab `non_example` states **why** it is not an example | 53 / 58 cards state no reason |”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (158-159): “the minimally-different pair marks the boundary, but only the max-different example *kills the over-generalisation the pair invites*.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (164): “**A3b — the non-example's stated reason must name the METHOD, never a property.**”
- `grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md` (81): “vary surface features holding the distinction constant; vary the distinction holding surface features constant; never both on one item.”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (33-34): “example and non-example differ in only the one defining feature, and the non-example states why it fails”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (35-36): “pair must be a genuine minimal pair, same length band, **without a giveaway**.”
- `grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd` (83): “If the learner can logically infer the wrong rule from the examples provided, the fault lies with the instruction, not the learner.”
- `grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd` (88): “**Near-misses** that differ only in the critical feature”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (35-36): “pair must be a genuine minimal pair, same length band, **without a giveaway**”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (37): “Every example and non-example states its "why"”
- `grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd` (87-88): “**Contrastive examples** that show what counts and what does not * **Near-misses** that differ only in the critical feature”
- `grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd` (27): “5. **Make misconceptions hard to form.** Use clear examples, non-examples, and fast error correction.”
- `grade3-reading/knowledge_bot/knowledge/kb-0147-draft-grade-3-science-ledger.qmd` (42): “State that an atom of a substance is NOT a tiny version of that substance — a gold atom is not a tiny shiny gold speck.”
- `grade3-reading/knowledge_bot/knowledge/kb-0147-draft-grade-3-science-ledger.qmd` (42): “[New — D1 Section 2.1 negative definition; required at Grade 3]”
- `grade3-reading/knowledge_bot/knowledge/kb-0147-draft-grade-3-science-ledger.qmd` (41): “[Spiral review of G2 Unit 2, A3-A4 — what is new: "atoms" replaces "tiny pieces/particles"; formal term introduced per D1 3-5 band]”
- `grade3-reading/knowledge_bot/knowledge/kb-0147-draft-grade-3-science-ledger.qmd` (27): “Every `Reviewer Comments` cell is blank; the source contains no completed reviewer feedback,”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (144): “- Start with clear examples/non-examples and systematically vary examples using set-up/difference/sameness principles.”
- `grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd` (47): “imprecise oral definitions receive concrete examples and non-examples; strong answers are extended by asking for an original example.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (66): “**At least 1 boundary case** — makes the concept boundary visible so the student does not overgeneralize.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (299): “**3. At least 2 positive examples**”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (300): “Distinct concrete instances where the KC applies. Must be genuinely distinct — two examples of the same instance rephrased do not count.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (305): “draws the same line using only true statements, without ever voicing the misconception.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (305): “AlphaTok and the course's locked script skill use positive-only framing, so a contrastive true-fact pair COUNTS as the boundary.”
- `grade3-reading/course-renderer/docs/rules/vocabulary.md` (286-288): “A definition is ONE sentence, 20 words at the outside. An example is at most two sentences and 30 words; a non-example at most two and 35, the extra five being the "because" R-VOC-4 requires.”
- `grade3-reading/course-renderer/docs/rules/vocabulary.md` (306-308): “Every extra clause is another place the two sides differ, so a long pair is a weaker contrast, not a more thorough one. The child then has to find the difference instead of being unable to miss it.”
- `grade3-reading/course-renderer/docs/rules/vocabulary.md` (316-318): “A 52-word non-example, which is what the `epic` card carried, is past the point where a nine-year-old can still hold the example it is supposed to be compared against.”
- `grade3-reading/course-renderer/docs/rules/vocabulary.md` (329-331): “The wording principle itself is not machine checkable and stays a review question: read the pair aloud and hear whether the two sides say the same thing until the moment they differ.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (572-575): “The test each candidate has to pass is R-VOC-3, an Engelmann minimal pair where the example and the non-example are the same situation with one feature changed, and R-VOC-4, a because-clause on the non-example saying why it is not an instance. If I cannot write that pair, the word is wrong for this lesson.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (648-650): “It appears in the CKLA extract itself ("no man can easily resist" the wine) so it is textually present, and a pair is writable. Two reasons against.”
- `othello-course-renderer-draft/repo/docs/rules/vocabulary.md` (302-303): “juxtaposed items should use the same wording, or wording as close to it as possible”
- `othello-course-renderer-draft/repo/docs/rules/vocabulary.md` (306-307): “Every extra clause is another place the two sides differ, so a long pair is a weaker contrast, not a more thorough one.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/integration/check-before-final-content.txt` (219): “non_example has no "because" clause explaining why it fails — minimal pairs should say why”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/CODEX-HISTORY-EVERYTHING-OUT.md` (74): “bar too): ≤3 vocab words, no close synonyms, every non-example needs the why-it-fails sentence;”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/generated/feedback-2026-08-11-crosswalk.json` (51): “Explain why the mouse does not outwit the cat, and require an explanation for every non-example.”
- `grade3-reading/course-renderer/authoring/inputs/rule-packs/reading-g3.json` (196): “The live defect was a tiny spider fooling a leopard versus a lion winning a fight, which changes the animal, the size and the method at once and so isolates nothing.”
- `g9/sources/Othello Unit Video_ Info Sheet for Devfactory.md` (25): “Terms are defined and shown with an example and a non-example (dramatic irony: the audience hears "I am not what I am"; Othello does not).”
- `othello-archive/sources/act1/Othello Unit Video - Info Sheet for Devfactory.txt` (31): “Terms are defined and shown with an example and a non-example (dramatic irony: the audience hears "I am not what I am"; Othello does not).”
- `g9/library/text/Lbde498.txt` (25): “Terms are defined and shown with an example and a non-example (dramatic irony: the audience hears "I am not what I am"; Othello does not).”
- `othello-course-renderer-draft/repo/authoring/inputs/rule-packs/reading-g3.json` (196): “The live defect was a tiny spider fooling a leopard versus a lion winning a fight, which changes the animal, the size and the method at once and so isolates nothing.”
- `grade3-reading/.claude/skills/one-perfect-lesson/SKILL.md` (53): “≤3 non-synonym vocab words with why-the-non-example-fails”

Against: The same BrainLift exempts wrong-rule comparisons from the one-difference rule, since their asymmetry is the point (`grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md`, line 81). that every example and non-example states its reason is a convention; nothing checks it. The ledger is an unreviewed draft: every reviewer-comment cell in it is blank (`grade3-reading/knowledge_bot/knowledge/kb-0147-draft-grade-3-science-ledger.qmd`).

<sub>criterion · wording, sequence · universal · from ap, g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Experiment with the text before interpreting it

Let students try contrasting readings or change one element of a scene, predict what changes for characters and audience, and explain why, before any finished interpretation is given.

A published teaching pack, chosen as the central reference for the Grade 9 unit's teaching approach, has students explore punctuation through movement, relationships through rhythm and unresolved problems through passing an object between speakers, which makes aspects of the text available for investigation before a finished interpretation is supplied (`g9/transcript/chat-transcript.redacted.txt`, lines 2978 and 3073). The unit's design brief turns this into rehearsal as investigation: students try contrasting readings or staging choices, predict their effects and explain what changed (line 3091). An advanced-learning resource, written after the first plan was found too basic beside the Grade 3 lessons, proposes changing who hears an aside, removing a line or altering a performance choice, then predicting what changes for each character and the audience and defending the causal explanation (lines 2534-2626). That resource was endorsed as the basis for the build (line 2705).

Quoted:

- `g9/transcript/chat-transcript.redacted.txt` (3073): “The RSC pack has students explore punctuation through movement, relationships through rhythm, and unresolved problems through passing an object between speakers.”
- `g9/transcript/chat-transcript.redacted.txt` (3073): “These activities make aspects of the text available for investigation before a finished interpretation is supplied.”
- `g9/transcript/chat-transcript.redacted.txt` (3091): “Students try contrasting readings or staging choices, predict their effects and explain what changed.”
- `g9/transcript/chat-transcript.redacted.txt` (2626): “Change who hears an aside, remove a line, or alter a performance choice.”
- `g9/transcript/chat-transcript.redacted.txt` (2626): “Students predict what changes for each character and the audience, then defend the causal explanation.”
- `g9/transcript/chat-transcript.redacted.txt` (2705): “ok, I relly love what we assembled, lets kinda prepare to buiold our app”

Published: [RSC Othello teaching pack (2024)](https://www.rsc.org.uk/learn/schools-and-teachers/teacher-resources/othello-teacher-pack-2024)

Against: Untested with students: both are designs, and the brief adds: "Peer rehearsal remains valuable; an AI response is not an equivalent replacement." (`g9/transcript/chat-transcript.redacted.txt`, line 3091).

<sub>criterion · format, demand, sequence · domain · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Fade guidance as expertise grows

Fade guidance for each skill across a unit as learners gain expertise, because heavy guidance helps novices but slows learners who already know the material. One lesson design specification gives guided practice 30% of a first-encounter lesson and 5% of an expert one.

A Year 9 lesson design specification cites the expertise reversal effect (Kalyuga et al.): heavy guidance helps novices but slows down learners who already know the material. So as students gain expertise, new knowledge and guided practice shrink and independent practice grows, from 30% of a first-encounter lesson to 5% of an expert one. The reading project's rulings likewise call for scaffolds to fade across a unit. Guidance moves from full modelling to independent work. A student who already shows the skill may skip the full model, and when each scaffold retires is recorded.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (284): “The expertise reversal effect (Kalyuga et al.): heavy guidance helps novices but slows down learners who already know the material.”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (281): “As students gain expertise, new knowledge and guided practice shrink and independent practice grows.”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (300): “| **A. First encounter** | 1.1 | 10 | 30 | 30 | 20 | 10 |”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (304): “| **E. Expert** | Whole-text argument | 10 | 5 | 5 | 65 | 15 |”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (41): “scaffolds fade across a unit”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (42-43): “never got past one lesson per scaffold level, so this stayed unimplemented”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (306): “In review lessons (Profile D), guided practice grows again but changes form: worked examples and comparative judgement, rather than first-time modeling.”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (284): “heavy guidance helps novices but slows down learners who already know the material.”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (280): “Early in a text, guided practice is essential while students get to know the text.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (161): “Too much feedback can reduce active processing; feedback timing should shift as proficiency improves.”
- `grade3-reading/knowledge_bot/knowledge/kb-0157-mastery-signal-evidence-base.qmd` (437): “Explains why simply increasing support (hints/steps) can raise short-term success without improving learning, and why too little support produces floundering.”
- `grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd` (239): “Too much guidance can mask misconceptions; too little creates failure loops”
- `grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd` (72-73): “exposure-based fade progression per skill (heavy model 5/2/1 → shift 3/2/3 → hand-over 1/2/5)”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (41-42): “scaffolds fade across a unit (a procedure "collapses into a two-step option after five successful uses,"”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (326): “A quick check at the start of guided practice lets confident students move straight on.”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (18): “exposure-based scaffold fade (5/2/1 → 3/2/3 → 1/2/5)”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (288-289): “use explicit instruction with worked examples and fading”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (30): “named inference routines as *fading scaffolds* retired on a stated condition … vs. scheduled recurring retrieval of the routine (a plain reading of practice-architecture doctrine).”
- `grade3-reading/knowledge_bot/knowledge/kb-0226-g3-pre-submission-closure-audit-2026-09-24.qmd` (40): “3. Independent Find pre-glows candidates and states the count (L5-L7), where the design wants an open hunt”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md` (139-140): “But the same scaffolding can harm relative experts (expertise reversal) [12].”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (233-234): “Prose in an authoring note does not satisfy D1.13, and a gate must fail **by name** on a scaffold that has no fade record”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (238-239): “"states a condition" is satisfiable by a sentence in a document nothing reads, so nothing ever fades.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (248): “- **Counts are monotonically non-increasing across the unit.**”
- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (669): “Worked example → completion (last steps blanked) → independent; every scaffold states a fade/retirement condition.”
- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (675): “Model in full, then omit steps progressively (often last-first) to independence.”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (224): “In review lessons (Profile D), guided practice grows again but changes form: worked examples and comparative judgement, rather than first-time modeling.”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (216): “| Profile | Example | Retrieval | New knowledge | Guided | Independent | Close |”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (220): “| **C. Revisit / comparison** | Iago's soliloquies side by side | 15 | 10 | 10 | 50 | 15 |”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (221): “| **D. Review** | Before an assessment | 20 | 5 | 25 | 40 | 10 |”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (399): “In review lessons (Profile D), guided practice grows again but changes form: worked examples and comparative judgement, rather than first-time modeling.”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (300-302): “Occasionally; mainly in review lessons.”
- `g9/library/text/L9b6d99.txt` (199): “As students gain expertise, new knowledge and guided practice shrink and independent practice grows.”
- `g9/library/text/L8d5159.txt` (40): “The rule is that a child gets a compulsory full model the FIRST time they meet a stage. If stages are available rather than assigned, that first time is a per-child event, not a date in the scheme.”
- `g9/library/text/L8d5159.txt` (41): “Nine rails by four stages is 36 cells. A child who climbs all four stages could meet up to 36 compulsory models across roughly 96 lessons, which is more than a third of them running the long path.”
- `g9/library/text/L8d5159.txt` (41): “That is the real cost of making stages available, and it is worth knowing before it is built rather than after.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/strategy/grade-9-strategy.md` (158): “| Skipping the modelled turn skips learning | Skip only after a first-try pass on a parallel item; the walkthrough stays reachable | Transfer scores of skippers vs non-skippers |”
- `othello-course-renderer-draft/repo/docs/qa/peter-pan-readventure-2026-09-29/REPORT.md` (25): “**Live per-child skipping is not enabled**: `/book` has no trusted child identity or placement owner to bind the stored record. The current lesson gives every child the full authored model.”
- `grade3-reading/.claude/skills/one-perfect-lesson/SKILL.md` (89-90): “exposure-counted scaffold progression (heavy 5/2/1 → shift 3/2/3 → hand-over 1/2/5) against the course graph”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (207-208): “the verbatim fade table (≤10 exposures → heavy_model 5/2/1; 11–20 → shift 3/2/3; 21+ → hand_over 1/2/5)”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (108-109): “claims zero prior exposure to the operation, but canon records a U1·L6 lineage (deepen, not introduce) — the justification is factually wrong, not just an omission.”
- `grade3-reading/.claude/skills/one-perfect-lesson/SKILL.md` (81): “The three response plans (cherry-pick;”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (721): “`prior_exposure_count` 0→1”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (722): “`rendered_item_counts` 1/1/3→1/3/2”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (758-759): “The residual heavy_model 5/2/1 gap stays declared, not force-fit, per the audit's instruction.”
- `grade3-reading/incept-read-app/NOTE-dose-teach-sections.md` (93): “Band A shows full Scout narration + all support; B/C progressively strip it.”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/HUMAN-g3r-2026-07-27T08-38-36-019fa24b-fb42-7e61-a954-216db3ef77a4.md` (1112): “The teacher models how to find and re-read the right part of the text — the locate-the-evidence moves and a pause — running inside the think-aloud, right after the procedure's first step. This modelling never fades.”
- `g9/transcript/chat-transcript.redacted.txt` (2628): “Feedback becomes less explicit as they improve.”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (202): “The expertise reversal effect (Kalyuga et al.): heavy guidance helps novices but slows down learners who already know the material.”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (342): “Research. The expertise reversal effect (Kalyuga et al.): heavy guidance helps novices but slows down learners who already know the material.”
- `g9/library/text/L9b6d99.txt` (202): “**Research.** The expertise reversal effect (Kalyuga et al.): heavy guidance helps novices but slows down learners who already know the material.”
- `grade3-reading/ti-courseplans/courses/g7-science/analysis/video-pipeline-conformance-audit-v0.2.md` (48): “Every video renders at identical scaffolding density.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (153): “Gradual release should adapt to the student, not run on a fixed schedule.”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md` (824): “this table describes the spaced-practice system, NOT the in-lesson Modelling Moment, which never tapers: the MM is always a full model with the child doing only the final step”

Published: [Kalyuga, Ayres, Chandler & Sweller 2003](https://doi.org/10.1207/S15326985EP3801_4) · [Koedinger & Aleven 2007](https://doi.org/10.1007/s10648-007-9049-0)

Against: The Grade 3 course never got past one lesson per scaffold level, so fading was never built or measured there, and the specification has guided practice grow again in review lessons, as worked examples and comparative judgement. the five-use fade was never built in the Grade 3 course, which never got past one lesson per scaffold level (`grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd`, lines 42-44), and in review lessons guided practice grows again, as worked examples and comparative judgement rather than first-time modelling (`grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd`, line 306). The project's comprehension doctrine holds an open dispute over whether named inference routines should fade and retire on a stated condition or be retrieved again on a schedule (`grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd`, line 30). The fade was never built past one lesson per scaffold level, so it stayed unimplemented (`grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd`, lines 42-43). A reading BrainLift holds as an open dispute whether named inference routines should fade on a stated condition or be retrieved again on a schedule (`grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md`, T2). A later run found counter-evidence (`grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/HUMAN-g3r-2026-07-27T08-38-36-019fa24b-fb42-7e61-a954-216db3ef77a4.md`). A later run found counter-evidence (`othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md`).

<sub>criterion · sequence, hints, practice · universal · from g3, g9, research · external-research · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Few questions during reading

Keep questions during reading few and at natural breaks, because frequent ones can cut young readers' recall of what they don't ask about. In one study, Grade 4 recall of untargeted information fell from .30 with no questions to .07 with questions during reading.

A research-boundary review checked a cited experiment in which 240 students, 60 each in Grades 4/7/10 and college, met 14 written causal questions per story during reading, after reading or not at all (Van den Broek et al. 2001, https://doi.org/10.1037/0022-0663.93.3.521; `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md`, section 2). The quoted fall from .30 to .07 is Grade 4 recall of untargeted information, not overall comprehension, and the college benefits concerned targeted information. The review concludes that frequent unsupported interruptions can be costly for younger readers, and that a change of timing should compare equal-content versions and measure both whole-story understanding and targeted learning.

Quoted:

- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md` (27): “**14 written causal questions per story** appeared during reading, after reading, or not at all.”
- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md` (29): “The quoted **.30 control → .07 during-reading** result is Grade4 recall of **untargeted information**, not overall comprehension.”
- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md` (31): “**Design conclusion:** frequent unsupported interruptions can be costly for younger readers.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (322-326): “Van den Broek and colleagues tested 240 children in the equivalents of Year 4, Year 7, Year 10 and undergraduates, asking questions during and immediately after reading, and found that "it was the youngest pupils whose comprehension and recall suffered the most from questions asked both during and immediately after reading."”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/03-INSTRUCTION-DESIGN.md` (196-197): “Are we asking so many questions that the kids are kind of missing the point?”

Published: [Van den Broek et al. 2001](https://doi.org/10.1037/0022-0663.93.3.521)

Against: After-reading questions also lowered that recall (.16 against .30), readers could not look back while answering, and the review says the study does not establish a ban on every mid-text check, especially sparse checks at coherent boundaries with the text available (the same file, lines 27-31).

<sub>criterion · sequence, measurement · universal · from g3, research · external-research · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Film checks feed later retrieval

Feed students' answers to a film's in-video checks into the next lesson's retrieval, designing film and lesson together, without repeating what the current lesson's retrieval asks. One unit's video design asks for three pause-answer-resume checks whose answers feed its second lesson's retrieval.

Review of one unit's design material found it specifies a teaching sequence in which answers at the film's checks feed later retrieval, and its video brief asks for three pause, answer and resume checks whose responses feed the second lesson's retrieval. The page built for the film left those checks to the interface, so the review asked that the cue points, response handling and retrieval handoff be agreed together.

Quoted:

- `g9/transcript/chat-transcript.redacted.txt` (4142): “It specifies a teaching sequence, including video-check answers feeding later retrieval”
- `g9/transcript/chat-transcript.redacted.txt` (5038): “three pause–answer–resume checks, with responses feeding Lesson 2 retrieval”
- `g9/transcript/chat-transcript.redacted.txt` (5038): “Agree the final cue points, response handling and retrieval handoff together.”
- `g9/library/text/Lbde498.txt` (78): “The answers feed Lesson 2 retrieval.”
- `g9/library/TIMELINE.md` (95): “check answers must feed Lesson 2 retrieval (`lesson_2_payload`); de-duplicate against Lesson 1 retrieval; dramatic irony expected known”
- `g9/library/text/Lbde498.txt` (48): “Lesson 1 retrieval (word web: deceit) follows.”
- `g9/library/text/Lbde498.txt` (77): “the unit video plays at the very start of Lesson 1, before retrieval.”

Against: It is specified in one unit's video design and not shown working: the hand-off was still listed as open on 6 October (`g9/library/TIMELINE.md`, line 95).

<sub>criterion · sequence, practice, media · domain · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Fixed components, flexible time

Keep every component in every lesson and vary only its time, by lesson type and learner, with floors: support shrinks but never vanishes, and retrieval keeps about a tenth. Retrieval never falls below about 10% of a lesson, and at least one quick check comes before students write alone.

A Grade 9 lesson design specification fixes the components and lets their time change: every lesson contains every component, each lesson row takes a timing profile, and the time is then adjusted by stage and by results. Its floors keep retrieval at about a tenth of the lesson or more, at least one quick check before students write alone, and a close however short. Stage 1 students get more guided practice in the same lesson and Stage 3 students move to independent practice sooner; if students struggled in independent practice last lesson, the next lesson's guided practice expands, and a quick check at its start lets confident students move straight on. Guided practice can be fast-tracked but never removed.

Quoted:

- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (338): “Every lesson contains every component, but the time each one gets changes with the lesson.”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (348-349): “Never below about 10% of the lesson.”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (352-353): “At least one quick check before students write alone.”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (354-355): “Always included, even if short.”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (418): “Each lesson row gets a "Lesson profile" column (A–E), which sets the default timing.”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (420): “In the same lesson, Stage 1 students get more guided practice, and Stage 3 students move to independent practice sooner.”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (422): “If students struggled in independent practice last lesson, the next lesson's guided practice expands. A quick check at the start of guided practice lets confident students move straight on.”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (500): “Guided practice can be fast-tracked with a quick check, but never removed.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (94): “The principle behind all of these, carried over from the fading rules: support gets SHORTER, not removed.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (94): “A child who needs help should land at the same place on the clock as a child who does not, because the help was quicker, not because we took it away.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (111): “serve the 1:30 refresher before the 4:30 full model”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (293): “Guided practice can be fast-tracked with a quick check, but never removed.”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (244): “A quick check at the start of guided practice lets confident students move straight on.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (285): “The rule in one line: the child may skip the Modelling Moment, but not step 4.”
- `g9/library/text/L9b6d99.txt` (293): “Guided practice can be fast-tracked with a quick check, but never removed.”
- `g9/library/text/L9b6d99.txt` (244): “A quick check at the start of guided practice lets confident students move straight on.”
- `g9/library/text/L8d5159.txt` (94): “The principle behind all of these, carried over from the fading rules: support gets SHORTER, not removed.”
- `g9/library/text/L8d5159.txt` (94): “A child who needs help should land at the same place on the clock as a child who does not, because the help was quicker, not because we took it away.”
- `g9/library/text/L9b6d99.txt` (211): “At least one quick check before students write alone.”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (209): “Never below about 10% of the lesson.”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (204): “Minimum for each component”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (34): “Strengthens key knowledge from previous lessons. Later, it interleaves across units and texts.”

Against: How a learner reaches a stage is still undecided in the specification (`othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt`, line 510). Expanding the next lesson's guided practice on one lesson's results can mean adapting on fewer observations than the three another engine requires (Never adapt on one observation), and nothing here measured the floors or the adjustments. The same Grade 3 design removes the earlier modelled steps once a procedure is known, keeping only the step that models the write-up (`g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx`, line 285). A unit's first lesson has nothing earlier to retrieve: one draft said "because this is the first lesson, there is no retrieval practice." (`g9/sources/meeting-notes/ELA - CNU + Academics - 2026_10_01 20_30 IST - Notes by Gemini.md`, line 272), though the later video sheet gives the first lesson a retrieval, a word web on the unit's key concept (`g9/sources/Othello Unit Video_ Info Sheet for Devfactory.md`, line 48).

<sub>criterion · sequence, practice · domain · from g3, g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Free reading time is not instruction

Don't rely on unguided independent reading time to raise reading outcomes, since a meta-analysis found that simply encouraging more independent reading did not improve them.

The RAND Reading Study Group's 2002 report, in a reading course's digest of it, reports a National Reading Panel meta-analysis in which encouraging students to read more on their own, as in Sustained Silent Reading, did not result in improved reading (p. 32; `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd`, lines 473-475). The same report notes that the panel found no compelling evidence that independent-reading programmes promoted vocabulary growth, while direct instruction of vocabulary did improve comprehension (p. 36). The vocabulary finding is an absence of evidence rather than a measured lack of effect.

Quoted:

- `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd` (475): “did not result in improved reading, according to the findings of a meta-analysis”
- `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd` (473): “A National Reading Panel meta-analysis found that simply encouraging students to read more independently (e.g., Sustained Silent Reading) did not improve reading outcomes.”
- `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd` (523): “The NRP did not find compelling evidence that programs that are designed to increase independent reading, such as Sustained Silent Reading, promoted vocabulary growth.”
- `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd` (517): “The NRP (2000) found that direct instruction of vocabulary improved reading comprehension.”

Published: [RAND Reading Study Group 2002, Reading for Understanding (MR-1465)](https://www.rand.org/pubs/monograph_reports/MR1465.html)

Against: none found

<sub>criterion · practice · universal · from research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Guided practice is shared work

In guided practice the lesson supplies part of the answer, never the conclusion, and the learner finishes the reasoning; after one miss rephrase, after two offer a choice. One lesson supplied two clues, a spoken line and a careful movement, and left the learner to say what an audience would wonder if the action contradicted them.

Earlier feedback on the course objected to students copying completed answers and to independent work assigned under a shared-work label. The rebuild's teaching contract then defined shared work as a real partial response from the lesson that the learner completes with the reasoning step, and called a new question with hints insufficient. The lessons follow it: in one, the lesson supplies the evidence and the learner completes the implication.

Quoted:

- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/README.md` (58): “The guide contributes a real partial response and the child completes the reasoning step. A new question with hints is insufficient.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/lesson-01.md` (45): “The line about the path and the careful movement work together. If the second performer ran confidently, the audience might wonder ___.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/lesson-01.md` (45): “Guide supplies the evidence, child completes the implication.”
- `grade3-reading/ti-courseplans-wiki/Perfect-Course-Rulebook.md` (116-117): “the we-do gives a genuine partial that the child completes through a blocking response”
- `grade3-reading/ti-courseplans-wiki/Perfect-Course-Rulebook.md` (124): “fake we-do hints”
- `grade3-reading/ti-courseplans-wiki/Perfect-Course-Rulebook.md` (157): “the prompt supplies the inference”
- `grade3-reading/ti-courseplans-wiki/Anatomy-of-a-Perfect-Course.md` (53-54): “A hint is not a we-do, and a prompt that supplies the thought is not support.”
- `grade3-reading/ti-courseplans-wiki/Perfect-Course-Rulebook.md` (248): “Conceptual slots persist while supplied content fades.”
- `grade3-reading/ti-courseplans-wiki/Perfect-Course-Rulebook.md` (248): “The frame supplies the conclusion or becomes a filled answer sheet.”
- `grade3-reading/ti-courseplans-wiki/Perfect-Course-Rulebook.md` (194-195): “interpretation embedded in the frame”
- `grade3-reading/ti-courseplans-wiki/Peter-Pan-Quality-Case-Study-2026-08-24.md` (303-304): “Scaffolding that performs the cognition destroys evidence of learning. Support can narrow where to look or how to combine; it cannot provide the thought being assessed.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/FEEDBACK-RESPONSES.md` (68): “I don't see a partial answer anywhere here — I just see a you-do arriving early, on the hardest”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/FEEDBACK-RESPONSES.md` (74): “There is now a partial answer in every one of the 18 lessons.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/FEEDBACK-RESPONSES.md` (76): “because she hands over the part that needs thinking and keeps the part that needs remembering.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/FEEDBACK-RESPONSES.md` (78): “If the child misses, she rephrases the question rather than giving the answer. If they miss again, they get”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/BRAINLIFT.md` (92): “18/18 end in `?`.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/BRAINLIFT.md` (94): “quote-coherent with the completion so the two rungs are the same move.”

Against: none found

<sub>criterion · practice, hints, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Keep knowledge warm by using it

Keep earlier knowledge alive by making later lessons need it, and send to separate spaced review only what nothing later can honestly use.

The curriculum architecture BrainLift argues that knowledge kept warm by isolated spaced practice costs time and stays compartmentalised, and that a platform should not compensate for a poorly connected curriculum by drilling everything forever (`grade3-reading/ti-courseplans/feedback/feedback2/WF - Curriculum Architecture Br - 260713-123107.md`). The reading project's practice spec adopted the theme sequence as the first spaced-practice system, with separate review as the backstop that keeps warm exactly the residue the sequence cannot honestly recruit downstream, and it treats the size of that residue as a design metric (`grade3-reading/ti-courseplans/docs/practice-layer-spec.md`). Knowledge kept warm this way is recalled through use rather than recognised, and the separate review is mixed across units.

Quoted:

- `grade3-reading/ti-courseplans/feedback/feedback2/WF - Curriculum Architecture Br - 260713-123107.md` (55): “A platform should not compensate for a poorly connected curriculum by drilling everything forever.”
- `grade3-reading/ti-courseplans/docs/practice-layer-spec.md` (35-36): “it keeps warm exactly the residue the ladder cannot honestly recruit downstream, and the size of that residue is a design metric on theme”
- `grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd` (82): “use the curriculum to keep generative knowledge warm by use; use spaced practice for the residue.”
- `grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd` (131): “The strong version is a learning progression: each revisit adds a real upgrade”
- `grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd` (132): “Earlier knowledge stays warm because later lessons use it to do new work.”
- `grade3-reading/knowledge_bot/knowledge/kb-0147-draft-grade-3-science-ledger.qmd` (41): “[Spiral review of G2 Unit 2, A3-A4 — what is new:”
- `grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd` (29): “6. **Build in retrieval practice and spaced review.** Practice must require recall, not just recognition.”
- `grade3-reading/knowledge_bot/CHECKLIST.md` (45): “cross-unit **interleaved** review present (not massed single-passage); recall/production-format items present (not recognition-only).”
- `grade3-reading/knowledge_bot/CHECKLIST.md` (45): “(new — NN#6 was missing; the `kb-0057` V1 gap)”
- `grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd` (35): “Distribute practice over time. Cramming creates temporary performance.”
- `grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd` (36): “Mix problem types to prevent context-dependency.”
- `grade3-reading/knowledge_bot/ROUTER.md` (64): “"use the curriculum to keep generative knowledge warm by use; use spaced practice for the residue."”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (270-271): “the curriculum is the FIRST spaced-practice system.”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (38): “**The text set IS the practice schedule.** Engineered recurrence across a coherent text set is simultaneously vocabulary instruction (DOK1-2), spaced retrieval”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/pedagogy-policy.json` (1039): “Keep generative knowledge warm through honest downstream use and send only unrecruitable residue to isolated spaced review.”

Against: The ledger is a draft planning map, not approved curriculum (`grade3-reading/knowledge_bot/knowledge/kb-0147-draft-grade-3-science-ledger.qmd`).

<sub>criterion · sequence, practice · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Keep practice apart from assessment

Keep practice apart from assessment: checks during teaching give feedback and support without a mastery bar, and only a later scored assessment, with supports off, holds students to it. In one demo unit, the teaching lessons' checks gave feedback without gating progress, and only the 15-item assessment kept its mastery threshold of 90.

In a reading demo unit, a decision not to conflate teaching with assessment made the four teaching lessons non-gating: their checks are scored for immediate feedback but do not gate progress, and only the 15-item interval assessment keeps its 90 gate (`grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md`, lines 134-137; `grade3-reading/artifacts/demo-unit-2026-07-10/publish/README.md`, lines 23-25). Later lessons in the same course limited a copied pattern, one tap and one affirming clip at the end of independent work, to practice pages, never assessments (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/PARITY-PLAN-2026-09-14.md`, line 12). Engagement supports are faded before that assessment.

Quoted:

- `grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md` (135): “conflated): l0-l3 are now non-gating formative”
- `grade3-reading/artifacts/demo-unit-2026-07-10/publish/README.md` (24): “Teaching checks are scored for immediate feedback but do not gate lesson progression; only the”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/PARITY-PLAN-2026-09-14.md` (12): “practice pages only, never assessments, #488”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (330): “### Insight 7 — Word Assist boundary: practice on, scored off”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (332): “is available in dose steps 1–4 (hook, teach, guided, read) and OFF in steps 5–6 (the scored check / CFU)”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (332): “every scored item is a clean cold-condition measure”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (147): “• Permanent illustration/character wrapper — engagement scaffolds must fade to cold plain text or they teach dependency.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/BRAINLIFT.md` (132-133): “the 9–10-item graded bank at the end of each lesson is convergent right/wrong marking. That is correct for assessment and wrong for teaching”
- `grade3-reading/course-renderer/docs/rules/questions-and-assessment.md` (149-150): “**Rule.** The items that measure the child are the same activity as the teaching, in the same lesson, not a separate measure afterwards.”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/pedagogy-policy.json` (1521): “Declare each check-bearing lesson resource as teaching-check, interval-assessment, or benchmark, with gating allowed only for interval-assessment.”
- `othello-course-renderer-draft/repo/docs/rules/questions-and-assessment.md` (149-150): “**Rule.** The items that measure the child are the same activity as the teaching, in the same lesson, not a separate measure afterwards.”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (756-758): “the receipt's you-do lines count only the trap item, the two formative beats tally as generic "answers found" practice, and nothing presents them as release items.”

Against: Gating means different things in the course's two renderers: the book renderer's checklist makes every gate unskippable, "No trap (child can always proceed by doing the work) and no leak (cannot proceed without it)", and makes every check a gate except the first check of a unit's opening lesson (`grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md`, lines 126 and 129), while the demo unit dropped the mastery threshold from its teaching lessons. The rule on support rests on one plan line. Only loosely against: whether a film belongs in such a course at all was left unresolved, one source avoiding video because the target is plain text and the course's own rules treating an opening film as essential, "a genuine, load-bearing tension" (`grade3-reading/artifacts/wiki-research/cross-cutting.md`, line 141). A later run found counter-evidence (`grade3-reading/course-renderer/docs/rules/questions-and-assessment.md`). A later run found counter-evidence (`othello-course-renderer-draft/repo/docs/rules/questions-and-assessment.md`).

<sub>criterion · practice, evidence-of-learning, feedback · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Keep sounding out apart from word parts

Keep sounding a word out and splitting it into meaningful parts as separate steps: one teaches how the word is said, the other what its parts mean.

Two rulings in a reading course agree. The course's rulebook puts syllables first and the meaning-part split second, as a separate, later move, because meaningful parts and spoken parts are different things and must never share one tile (`grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md`, lines 407-410). A later ruling on the vocabulary card's sound-it-out clips says that step teaches pronunciation, not partitioning, with every chunk pronounced as it sounds inside the word, while the printed meaning parts are a different step and stay as they are (`grade3-reading/.claude/skills/sound-out-respell/SKILL.md`, lines 12-14).

Quoted:

- `grade3-reading/.claude/skills/sound-out-respell/SKILL.md` (12-14): “the beat teaches pronunciation, not partitioning — every chunk is pronounced exactly as it sounds inside that word. The printed morphemes (morph.parts, the word-parts stage) are a different beat and stay as they are.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (409-410): “the morpheme split is a separate, later move. "Morphemes are meaningful elements, syllables are spoken parts" — the two must never be conflated on one tile.”

Against: none found

<sub>criterion · sequence, wording, media · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Keep the demand, add support

For learners who are behind, keep the task's demand and add support, such as guided reading, vocabulary support and targeted practice, instead of giving easier material.

A pedagogy framework's guidance for students behind grade level says not to lower the cognitive demand of material but to scaffold it (`icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md`). It is a rule of the framework, with no measurement in the project.

Quoted:

- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (143): “Do not lower the cognitive demand of material. Instead, scaffold with guided reading, vocabulary support, and targeted practice.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (60): “This also gives a route DOWN.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (60): “A child who is struggling can be given the simplified wording of the same question rather than an easier question, which keeps the class on one piece of knowledge.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (111): “let the simplified question wording stand in for the Stage 1 question”
- `g9/library/text/L8d5159.txt` (60): “A child who is struggling can be given the simplified wording of the same question rather than an easier question, which keeps the class on one piece of knowledge.”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (221-223): “Beginner: simpler and accessible”
- `g9/library/text/L9b6d99.txt` (133): “Beginner: simpler and accessible”
- `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd` (371): “they can generate instruction in which very simple purposes for reading are defined, such as finding particular words or answering low-level questions.”

Against: A later run found counter-evidence (`othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt`). A later run found counter-evidence (`g9/library/text/L9b6d99.txt`).

<sub>criterion · demand, accessibility · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Knowledge before the text

Build the topic knowledge a hard text assumes, and give it before the reading, not after.

An intro-video BrainLift for a Grade 3 reading course rests on two classic studies (`downloads/BrainLift - What makes a good intro video.md`): prior knowledge of baseball predicted memory for a baseball text on essentially every measure while general reading ability predicted almost none (Recht and Leslie 1988, line 439), and context given before an opaque passage transformed comprehension and recall while the same context given after did not (Bransford and Johnson 1972, line 446). Everything that document argues rests on its video sitting before the read (line 421). A BrainLift on early reading comprehension says comprehension rests on language and, more than anything, background knowledge (Catts 2021-2022; `downloads/WF - Brainlift Opportunities to - 260724-110911.md`, line 32), and the course's Grade 3 to 12 thematic map orders its texts so that earlier ones build the knowledge later ones need (`downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx`, sheet 'How to read this', cell A3). The sources give no links for these studies; the DOIs and the article's address were found on Crossref and the publisher's site.

Quoted:

- `downloads/BrainLift - What makes a good intro video.md` (439): “prior knowledge of baseball predicted memory for a baseball text on essentially every measure; general reading ability predicted almost none.”
- `downloads/BrainLift - What makes a good intro video.md` (446): “giving readers the context before an opaque passage transformed comprehension and recall. The same context after did not.”
- `downloads/BrainLift - What makes a good intro video.md` (421): “Everything this document argues rests on the video sitting before the read.”
- `downloads/WF - Brainlift Opportunities to - 260724-110911.md` (32): “It is a complex activity that rests on language and, more than anything, background knowledge (Catts, 2021-2022).”
- `downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx` (sheet 'How to read this', cell A3): “This is the 'knowledge latches onto knowledge' principle applied to whole-school reading.”
- `g9/sources/Othello Unit Video_ Info Sheet for Devfactory.md` (23): “Pre-train names, relationships, setting and key terms before the first reading, so working memory is free for the language when students read.”
- `othello-archive/sources/act1/Othello Unit Video - Info Sheet for Devfactory.txt` (25-26): “Pre-train names, relationships, setting and key terms before the first reading, so working memory is free for the language when students read.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (119): “The material should orient them well enough to encounter Shakespeare’s language without turning the opening into a dense lecture.”

Published: [Bransford & Johnson 1972](https://doi.org/10.1016/S0022-5371(72)80006-9) · [Recht & Leslie 1988](https://doi.org/10.1037/0022-0663.80.1.16) · [Catts 2021-2022](https://www.aft.org/ae/winter2021-2022/catts)

Against: Each finding is one classic study, and the Bransford and Johnson passages were written to be opaque without their context. Inside a text not all background has to come first: in the film study behind Background at the line that needs it, only 6 of 26 background points had to come before the first line.

<sub>criterion · sequence, stimulus · universal · from g3, research · external-research · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Knowledge units teach something new

Count a unit as building knowledge only when it teaches something about the world learners don't already know; familiar themes such as family or pets give practice, not knowledge.

A pedagogy red team on a second-grade reading plan found that its knowledge units, re-scoped to themes drawn from the passages it reused, such as family and friends, nature, animals and pets and everyday life, build essentially no new background knowledge: a child gains no new schema from another story about a family or a pet (`grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md`, lines 74-80). It grounds this in the knowledge thesis, which asks courses to teach children what they don't yet know about the world so that later texts on those topics are comprehensible, and calls the themed units comprehension practice on familiar content: fine, but not knowledge-first (the same file, line 80). The narrowed plan that followed made no knowledge-building claim (`grade3-reading/ti-courseplans/courses/g2-reading/analysis/optionB-prime-narrow-rebuild.md`).

Quoted:

- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md` (74): “"family/friends 92, nature/outdoors 65, building/making 57, animals/pets 41, everyday life 32, adventure 17."”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md` (80): “A child gains no new schema from another story about a family or a pet. So the "Knowledge Expeditions," as re-scoped to corpus themes, **build essentially no new background knowledge**”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md` (80): “*teach children what they don't yet know about the world (the water cycle, ancient Rome, insects) so that future texts on those topics are comprehensible.*”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md` (80): “they are comprehension *practice* on familiar content, which is fine, but it is not "knowledge-first"”

Against: none found

<sub>criterion · stimulus, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Leave a pretest on new content ungated

Never gate a check on untaught content: a pretest often helps even when most answers are wrong, but only if learners meet the right answers afterwards.

A reading engine rules that the first check of a knowledge-building lesson opening a unit activates and does not gate, since nothing has been taught to gate against, while every later check in the lesson still gates. The lesson research behind it rests on a 2023 review finding that pretesting on content not yet taught helps even when nearly every answer is wrong, but only if there is an opportunity to study the correct answers afterwards, which a gate would withhold. The research adds that the answer may arrive through the text or film that follows rather than as feedback on the item, as it does in this course's passages.

Quoted:

- `grade3-reading/course-renderer/AGENTS.md` (62-65): “Pretesting on content not yet taught helps even when nearly every answer is wrong, but only where the child then meets the correct answer, which on our pages arrives through the passage that follows: a gate is exactly what would withhold it.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l1-what-is-an-epic.md` (187-192): “The condition worth designing around: Pan and Carpenter's 2023 review finds pretesting on not-yet-taught content helps **even when nearly every answer is wrong**, but only "if there is an opportunity to study the correct answers afterwards" — which is exactly what a gate would withhold. So the ungated opener is not a relaxation of rigour; gating it would remove the mechanism that makes it work.”
- `grade3-reading/course-renderer/authoring/inputs/rule-packs/reading-g3.json` (31): “On a unit-opening lesson the first check ACTIVATES and does not gate (AGENTS.md, R-KC-5): there is nothing taught yet to gate against.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md` (188-190): “pretesting on not-yet-taught content helps **even when nearly every answer is wrong**, but only "if there is an opportunity to study the correct answers afterwards" — which is exactly what a gate would withhold.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md` (194-196): “The correct answer may arrive **implicitly**, through the text or video that follows, rather than as item-level feedback”
- `othello-course-renderer-draft/repo/AGENTS.md` (58-60): “**On a knowledge-building lesson that opens a unit, that first check activates and does not gate.**”
- `othello-course-renderer-draft/repo/AGENTS.md` (62-65): “Pretesting on content not yet taught helps even when nearly every answer is wrong, but only where the child then meets the correct answer, which on our pages arrives through the passage that follows: a gate is exactly what would withhold it.”
- `othello-course-renderer-draft/repo/AGENTS.md` (67-68): “Every later check in the lesson still gates.”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l1.json` (435): “gating this question would not make the lesson stricter, it would remove the mechanism that makes an opener work at all”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l1.json` (442): “An activation question that locks the child out on a miss does neither.”

Published: [Pan & Carpenter 2023](https://doi.org/10.1007/s10648-023-09814-5)

Against: The review's own claim is hedged, "can often enhance learning", so the research brief calls this a defensible design rather than a guaranteed gain (`grade3-reading/course-renderer/docs/research/g4-u1-l1-what-is-an-epic.md`, lines 196-197). The course records the rule, not its effect.

<sub>criterion · sequence, practice, feedback · universal · from g3, research · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Leave out what the lesson doesn't teach

Leave out anything the lesson does not teach or use, however interesting or familiar, above all at the start: irrelevant material lowers recall and transfer. Excluding extraneous material improves multimedia learning, with a median effect of about 0.70 standard deviations.

An intro-video BrainLift for a Grade 3 reading course records two findings: interesting but irrelevant details reduced recall and transfer and did the most damage at the start of a text (Harp and Mayer 1998), and excluding extraneous material improves multimedia learning, median effect near d 0.70 (Mayer's coherence principle, with Sundararajan and Adesope 2020) (`downloads/BrainLift - What makes a good intro video.md`, lines 129 and 130). Two version-3 inference lesson designs for the course apply it to a familiar reminder: the five story-pattern labels were deleted from the reading-goal panel because the pattern is not taught in that lesson (`downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx`, line 54 of its text; `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 10. The Wind in the Willows, Part 3 (FICTION, INFER) — v3 (new INFER design).docx`, line 46). The source names Sundararajan and Adesope without a link; its DOI was found on Crossref.

Quoted:

- `downloads/BrainLift - What makes a good intro video.md` (129): “Interesting but irrelevant details reduced recall and transfer, and did the most damage placed at the start of the text.”
- `downloads/BrainLift - What makes a good intro video.md` (130): “Excluding extraneous material improves multimedia learning, median effect near d 0.70.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (54 (textutil text)): “The pattern is not taught here, so it is removed entirely.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 10. The Wind in the Willows, Part 3 (FICTION, INFER) — v3 (new INFER design).docx` (46 (textutil text)): “The pattern is not taught here, so it is removed from the prompts. (It still lives in the video, Component 1.)”
- `downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx` (11 (textutil text)): “The five story-pattern labels (We meet / They want / But / So / Then) are shown as a visual reminder.”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (147): “video for exploration, where it serves the Spotlight. Video is a teaching aid here, not a fixture in every lesson.”
- `g9/sources/Othello Unit Video_ Info Sheet for Devfactory.md` (26): “Venice, the Turks, Cyprus, military rank. No general Elizabethan history.”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (57): “Only context students will need in Act 1, not general history.”
- `othello-archive/sources/act1/Othello Unit Video - Info Sheet for Devfactory.txt` (34-35): “Venice, the Turks, Cyprus, military rank. No general Elizabethan history.”
- `g9/library/text/Lbde498.txt` (26): “Venice, the Turks, Cyprus, military rank. No general Elizabethan history.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-visuals-human-v0.1.md` (120-122): “The seductive-details effect reliably harms learning across 58 studies and more than 7,500 learners, especially when decoration sits beside the instructional diagram or remains on screen [9].”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/02-LESSON-STRUCTURE.md` (96-99): “a Word Power page whose only job is announcing that words are coming … is deleted; the lesson flows directly from the preceding page into the first word card.”

Published: [Harp & Mayer 1998](https://doi.org/10.1037/0022-0663.90.3.414) · [Mayer 2009, coherence principle](https://doi.org/10.1017/cbo9780511811678.007) · [Sundararajan & Adesope 2020](https://doi.org/10.1007/s10648-020-09522-4)

Against: The course's lesson-components spec still shows the story-pattern labels as a visual reminder (`downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx`, line 11 of its text).

<sub>criterion · alignment, media, stimulus · universal · from g3, research · external-research · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Leave the hunt to the learner

In independent practice, leave the search to the learner: don't pre-mark candidates, name where to look, or say how many to find in an open hunt. One audit found an independent hunt that pre-highlighted 8 segments and told the child to tap the three clues.

A curriculum adherence audit (`grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md`, 2026-09-24) compared served independent tasks with designs that ask for an open hunt in which nothing is pre-highlighted. In three lessons the served hunts pre-highlighted their candidates and said how many to find, one with 8 highlighted segments and "Tap the three clues", and a multiple-choice zoom step named the evidence region first, which the audit says undoes the open hunt. The lesson-components list describes independent practice as clicking the evidence in the passage rather than choosing from options (`grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/procedures/Example_Lesson_Components.txt`).

Quoted:

- `grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md` (45): “**3. Independent Find is assisted, not an open hunt (core; L5, L6, L7; supporting in L4).**”
- `grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md` (47): “L6 p16/step3 hot_text, 8 glowing segments, "Tap the three clues ... Not all the glowing clues are useful"”
- `grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md` (135): “the Zoom MCQ pre-names the evidence region and undoes the open hunt”
- `grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/procedures/Example_Lesson_Components.txt` (31): “usually by clicking the evidence in the shown passage (click-to-highlight) rather than choosing from options”
- `grade3-reading/ui-audit-2026-09-08/round-5/open-hunt/CAUSE-PROPOSAL-IMPLEMENTATION.md` (24): “Root approved the existing book story target treatment: six authored candidate fragments glow, including decoys.”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (1350): “Do not glow the answer or tell the child which line to tap.”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md` (184-185): “independent hunts pre-glow and state the count (L5–L7; open-hunt itself = engine ruling)”
- `grade3-reading/course-renderer/docs/extras/alpharead-lesson-design-witw-part-1.md` (337): “Progress message after a find: **"{n} of 4 found. Keep going!"** (with a magnifier icon).”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (71): “The "n of 3 found" tracker keeps the goal visible; hints escalate.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-4/feedback-on-iteration-4/feedback-0806-pedagogy.md` (45): “Making all sentences tappable removes a cue and is right.”
- `grade3-reading/artifacts/pp4-v4-design.txt` (223): “Unlike the MM, evidence does not pre-glow.”
- `grade3-reading/artifacts/pp2-v3-design.txt` (246): “After a find, a tracker appears: "{n} of 2 found. Keep going!" (with a magnifier icon).”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/05-UI-UX-PRINCIPLES.md` (137-139): “the open hunt keeps its prose deliberately unmarked — in both cases marking the candidate spans would redraw the answer key, so the finger alone is the whole cue there.”

Against: One governing design itself shows a count, a tracker reading "{n} of 2 found", and whether a hunt can run with nothing pre-highlighted was left to a ruling on the engine (the same report, lines 46 and 48). A later run found counter-evidence (`grade3-reading/ui-audit-2026-09-08/round-5/open-hunt/CAUSE-PROPOSAL-IMPLEMENTATION.md`). A later run found counter-evidence (`grade3-reading/course-renderer/docs/extras/alpharead-lesson-design-witw-part-1.md`). A later run found counter-evidence (`g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx`). A later run found counter-evidence (`grade3-reading/artifacts/pp2-v3-design.txt`).

<sub>criterion · hints, practice · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Leave the last move to the student

In a worked example, model every step up to the final thinking move and leave that move to the student, with the modelled steps still in view.

The reading project fixed the split of its modelling moment across all lessons: the lesson models every step up to but not including the final substantive thinking move, and the child does that move (`grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd`, lines 83-84). A later closure audit flagged worked examples that handed an earlier step's conclusion to the child as a clause to complete, instead of a complete modelled sentence (`grade3-reading/knowledge_bot/knowledge/kb-0226-g3-pre-submission-closure-audit-2026-09-24.qmd`, lines 38-39).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (83-84): “the teacher models every step up to but not including the final substantive thinking move; the child does that move”
- `grade3-reading/knowledge_bot/knowledge/kb-0226-g3-pre-submission-closure-audit-2026-09-24.qmd` (38): “FIND I-do State hands the conclusion to the child”
- `downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx` (26 (textutil text)): “modelling every step except the final thinking move. It sounds like genuine thinking, not a lecture.”
- `downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx` (28 (textutil text)): “The child completes the final step only — one typed gap that carries the inference (“…so I think ___”) — with the modelled steps kept visible beside it.”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (207): “even in the I-do the last thinking move is the child’s, a small production that turns watching into doing”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (211): “The design doc’s Modelling Moment ends with the full model answer typed to completion; we leave the last word to the child”
- `grade3-reading/artifacts/qc-2026-09-30-staging/SPEC-find-infer-procedures.md` (28): “When the final step is a verification rather than a thinking move (MAIN IDEA Step 4 "Check coverage" is the clearest example), the child does the step BEFORE the verification - because composing the summary is the real cognitive work and "yes it covers the passage" can be rubber-stamped.”
- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (28): “When the final step is a verification rather than a thinking move (MAIN IDEA Step 4 "Check coverage" is the clearest example), the child does the step BEFORE the verification - because composing the summary is the real cognitive work and "yes it covers the passage" can be rubber-stamped.”
- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (28): “The teacher performs the verification aloud to close the moment.”
- `grade3-reading/course-renderer/docs/pedagogy/lesson-architecture.md` (35-36): “MAIN IDEA's Step 3 in Lesson 1, where the guide keeps the coverage check because a verification can be rubber-stamped.”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md` (28): “When the final step is a verification rather than a thinking move (MAIN IDEA Step 4 "Check coverage" is the clearest example), the child does the step BEFORE the verification - because composing the summary is the real cognitive work and "yes it covers the passage" can be rubber-stamped.”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md` (28): “performs the verification aloud to close the moment”
- `grade3-reading/artifacts/pp4-v4-design.txt` (320): “MM State is the teacher's typed whiteboard; Independent State is the child's 3-blank frame.”
- `grade3-reading/knowledge_bot/knowledge/kb-0231-pp-depth-6h-doc-diffs.qmd` (54-56): “the MM (modelled-model) Step 3 "State" ends in a child-completed `write_slot` rather than the doc's fully auto-typed whiteboard model, partially breaking the doc's explicit MM-vs-IT (independent-task) gradual-release contrast.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (54): “D1.3 We-do is a completed partial — pages[17].nodes[6] (finish-the-writeup, type=speak) gives the child a sentence starter ('I start, you finish: The story says ... so my answer is that flying feels…') after the coach has walked steps 1-3”
- `grade3-reading/visual-findings-2026-09-08/grade5-book-flow/PR-BODY.md` (12): “Present one model part or vocabulary stage at a time, retain earlier material in disclosures, and focus the productive response after a model.”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/CODEX-HISTORY-EVERYTHING-OUT.md` (65-66): “**teacher models all steps except the final substantive move — the child does the final step**”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/procedures/find.md` (18-20): “Never put an `scr`, `msq` or other child-answered item on a modelling page: the whole point of "I do" is that the guide does it, and a gated question here reverses the release.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md` (91-93): “Backward-fading designs have the learner "complete the last step themselves", fading until "full problems with no steps completed by the instructor are presented".”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (54): “D1.3 We-do is a completed partial”
- `grade3-reading/.claude/skills/one-perfect-lesson/SKILL.md` (48-49): “teacher models everything except the final substantive move — the child does the final step”
- `grade3-reading/artifacts/u4l2-build/BEAT-SPEC.md` (304): “auto-pacer never fills the child's row”

Against: The rulings make one exception, where the child composes a summary and the lesson verifies it aloud, because composing is the real cognitive work (`grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd`, lines 84-86). The lesson's own design did the opposite: "The design doc’s Modelling Moment ends with the full model answer typed to completion; we leave the last word to the child", and the build called its choice a deliberate divergence in emphasis. A later run found: More of the reading course's designs keep the model fully worked and leave completion to later turns: one contrasts the model's fully typed whiteboard with the child's three-blank frame in the independent task, and a line-by-line diff registered a built model that ends in a child-completed slot as partly breaking that contrast, a judgment call rather than a fix. A later simulated review credited the guided turn as the completed partial, a sentence starter the child finishes after three walked steps. A conformance audit still marked a model ending in a child-completed slot as delivered (`grade3-reading/artifacts/arc-audit/L7.md`, line 37), so the course holds both positions (`grade3-reading/artifacts/pp4-v4-design.txt`). A later run found counter-evidence (`grade3-reading/visual-findings-2026-09-08/grade5-book-flow/PR-BODY.md`). A later run found counter-evidence (`grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/procedures/find.md`). A later run found counter-evidence (`grade3-reading/artifacts/pp4-v4-design.txt`).

<sub>criterion · demand, practice · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Let learners teach an AI peer

Let learners teach an AI peer, explaining or defending a position to it, since expecting to explain to someone else produces deeper processing than studying to be tested. In a 5th-grade classroom study, teaching an agent with self-regulation feedback beat both being taught by the agent and teaching it without that feedback.

Notes on a proposed discussion with AI voices treat teachable agents, where the student teaches and the AI is taught, as a separate, well-evidenced mechanism: in a 5th-grade classroom study a teach-with-self-regulation-feedback condition beat both an agent-teaches-student condition and a bare teach-the-agent baseline (`g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/idea-02-ai-classmates-multi-agent-debate.md`, lines 25-28). The protégé-effect programme, a review of several studies, is cited for why: expecting to explain or defend a position to someone else produces deeper processing than studying to be tested (lines 28-30). The notes add that this inverts the risk of AI voices dominating, since the AI cannot out-argue a student it was designed not to out-know, and recommend trying a teachable-agent variant in at least one unit (lines 30-32 and 136).

Quoted:

- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/idea-02-ai-classmates-multi-agent-debate.md` (28-30): “The "protégé effect" research program (Chase, Biswas, Schwartz) is the standard citation for why: expecting to explain/defend a position to someone else produces deeper processing than studying to be tested **(review of a multi-study program)**.”
- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/idea-02-ai-classmates-multi-agent-debate.md` (26-28): “a 5th-grade classroom study found a "teach-with-self-regulation-feedback" condition beat both an agent-teaches-student condition and a bare teach-the-agent baseline **(field study, one domain)**”
- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/idea-02-ai-classmates-multi-agent-debate.md` (136): “Consider a **teachable-agent variant** for at least one unit: student explains/defends a reading to a deliberately under-informed AI peer, instead of or alongside experts challenging the student.”

Published: [Leelawong & Biswas 2008, Betty's Brain](https://www.researchgate.net/publication/220049808)

Against: "No direct evidence on whether **teachable-agent** or **expert-panel** is the better fit specifically for literary interpretation, versus the ecosystem/CS/math domains both research lines were built on." (`g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/idea-02-ai-classmates-multi-agent-debate.md`, lines 156-157). The classroom study is a field study in one domain (line 28), and in it the bare teach-the-agent baseline did worse than teaching with self-regulation feedback.

<sub>criterion · practice, format · universal · from research, g9 · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Literal checks until the skill is modelled

Until a skill has been modelled, checks on the reading ask only what the text states; independent use of the skill comes after the model. Checks on pages 6 to 12 stayed literal because inference was first modelled on page 19, and independent inference was then asked four times.

An external audit of a Grade 3 lesson found that all eight reading checks during the story were literal retrieval, with inference only inside guided steps. The ruling kept them literal: they come before the worked model of inference, so an independent inference item there would break the gradual-release order, and the lesson asks for independent inference four times after its independent step. A later review listed the retrieval-only checks in four lessons for a last look that none reads as a 'why do you think' question.

Quoted:

- `grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md` (26): “an independent inference item there would break the gradual-release order”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md` (26): “L4 asks independent inference four times after the you-do”
- `grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21.md` (27): “The retrieval-only reading checks (L4–L7 p6–p12)”
- `grade3-reading/artifacts/sim-review-2026-09-24/PRE-BRIEF.md` (18): “**Reading checks stay literal retrieval** like his (ruling 20.09); inference lives after the you-do.”
- `g9/library/collections/research-pack-2026-10-02/full-source-site/sources/engine/kb0180--kb-0180-lesson-structure-procedure-rulings.qmd` (121-123): “Practical rule: pre-modelling comprehension checks stay pure retrieval (what/who/where, tap-the-line, sequence); never move a check earlier to satisfy an aggregate percentage from a reviewing tool.”
- `grade3-reading/artifacts/red-team-2026-09-23/PRE-BRIEF.md` (27): “Reading checks stay literal retrieval; inference comes after the you-do”
- `grade3-reading/artifacts/arc-audit/L5.md` (36): “this doesn't just trim the count, it changes what's being assessed at two of the four checkpoints, encroaching on inference territory the doc reserves for Phase 3/MM.”
- `grade3-reading/engine/reports/PETER-PAN-IMPROVEMENTS-2026-09-28.md` (33-34): “(all seven comprehension questions literal) is by design: the 2026-09-20 ruling keeps Peter Pan reading checks literal, with inference after the you-do.”

Against: The audit's verdict was "Reasoning happens, but the method never lets go of the student's hand" (`grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md`, line 12), and the same row notes that keeping the checks literal also kept the lesson in the shape of an earlier lesson in the course.

<sub>criterion · demand, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Many encounters for each taught word

Plan many meaningful, spaced encounters with each taught word across the unit, adding them in the lesson's own activities where a text can't carry them, because one meeting teaches little. The check was built after 7 of 9 taught words were found appearing only once.

A reading course's rulebook holds that a word needs 10 to 12 encounters across the unit or course to be retained. Its validator fails a taught word never met again in a later lesson of its unit and reports the shortfall against ten; the gate came from 7 of 9 taught words appearing only once. Because the story text cannot be edited to insert a word, the rule was amended: a word the passage carries fewer than twice still counts if the lesson's own questions, options, feedback, frames, retell and recap use it at least 3 times. A key word is first taught with a definition and its use in context, and is assessed by its use rather than by recognition.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd` (65-66): “from 7/9 taught words appearing only once”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (69): “A word needs **10 to 12 encounters** across the unit/course to be retained”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (70-71): “fails a word never met again in any later authored lesson of its unit, and reports (rather than hard-fails) the shortfall against ten”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (46): “cannot be edited to insert a word”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (46-48): “a word not carried twice by the passage is still "earned" if the lesson's own activities (questions, options, feedback, frames, retell, recap) use it at least 3 times”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (69): “Only \~5–15 of 100 unfamiliar words met in natural reading are learned; misdirective contexts teach approximately zero”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (67): “*incidental* vocabulary: η²=.625, no meanings taught, target words recurring \~6× across the set”
- `grade3-reading/artifacts/criteria-register.csv` (12): “A taught word appears at least twice in its own passage and is met again in a later authored lesson”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md` (71): “| D4.7 | Use not recognition | PASS |”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-C-D7-D8-D10-D12.md` (29): “Deliberate absence from the passage (confirmed: zero occurrences in passage text) forces the child to supply it as evidence of comprehension.”
- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/G3-APPLICABILITY.md` (24): “`validate-vocab-earned.mjs:198–220` explicitly exempts encapsulating words from own-passage/later-lesson recurrence rules”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (45): “Tier-2 vocabulary requires direct robust instruction plus engineered re-encounters; incidental context is an unreliable acquisition channel”
- `grade3-reading/knowledge_bot/skills/reading-science/PRIORITIES.qmd` (56-57): “Vocabulary recipe: definitional + contextual, multiple encounters, morphology (~60% of meanings predictable), taught words chosen for generative value.”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (58): “Only \~5–15 of 100 unfamiliar words met in natural reading are learned; misdirective contexts teach approximately zero”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (60): “Sentences students write from dictionary definitions are unacceptable 60–63% of the time”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (56): “*incidental* vocabulary: η²=.625, no meanings taught, target words recurring \~6× across the set”
- `downloads/BrainLift - What makes a good intro video.md` (428): “Around ten or more meaningful encounters are needed to own a word, and vocabulary gains appear far more strongly on custom measures than standardised ones.”
- `downloads/BrainLift - What makes a good intro video.md` (428): “A word met once in a video is a first encounter, not the teaching of it.”
- `downloads/BrainLift - What makes a good intro video.md` (487): “vocabulary instruction helped comprehension on custom measures (d \= 0.50) far more than on standardised ones (d \= 0.10)”
- `downloads/BrainLift - What makes a good intro video.md` (487): “the correlation between a study's vocabulary gain and its comprehension gain was only modest (r \= .43).”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (22): “Each word returns \~10–12 times across the unit | One meeting never sticks; spaced returns in fresh contexts build ownership”
- `downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of G3-8_Threads_FourTier.docx` (396 (textutil text)): “Each unit's technical terminology (above) must be listed in the KB, taught before reading, and carried with spaced recall”
- `shadow-content-eval/SKILL.md` (68): “R-VOC-7: count the visible uses of each Word Power word **after its card** — story, questions, models, frames. Zero is `med`; fewer than 3 is `low`.”
- `shadow-content-eval/SKILL.md` (288): “| `VOCAB-UNTESTED` | med | a taught word that no Word Power question (and not the card's own check) tests (B4) |”
- `grade3-reading/ti-courseplans-wiki/Peter-Pan-Quality-Case-Study-2026-08-24.md` (240-241): “The recurrence metric rewarded a whole-corpus count without protecting the semantic and narrative ownership of the lesson being edited.”
- `grade3-reading/ti-courseplans-wiki/Peter-Pan-Quality-Case-Study-2026-08-24.md` (250-251): “natural-use adjudication for every recurrence hit”
- `grade3-reading/ti-courseplans-wiki/Perfect-Course-Rulebook.md` (355): “Recurrence counts do not prove word learning”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/review/evidence/course-graph-guide.md` (40): “RECURRENCE FLOOR: every Tier-2 word appears >=4x across the unit's passages, engineered toward ~6x -- emphasis on DOMAIN-SPECIFIC words (not just argument-core), which under-recur if unchecked.”
- `grade3-reading/course-renderer/docs/rules/vocabulary.md` (264-267): “The count is reported rather than failed because most of a word's encounters are owed by lessons that are not written yet, and failing on it would block authoring lesson four until lesson eight existed. The shortfall is the number a later lesson has to pay back.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/vocabulary-use-routine-and-volume.md` (15): “We might do 22 or more touches on that word during this short 7-minute lesson”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/vocabulary-use-routine-and-volume.md` (13): “I probably end the lesson with the kids saying admire at least 20 or so times.”
- `incept-package-hub/course-packages/courses/g7-reading/review/evidence/course-graph-guide.md` (40): “RECURRENCE FLOOR: every Tier-2 word appears >=4x across the unit's passages, engineered toward ~6x -- emphasis on DOMAIN-SPECIFIC words (not just argument-core), which under-recur if unchecked.”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/markdown/UNIT-SPECS.md inside it) (413-414): “Recurrence engineered ≥5× in a 4-lesson unit; sub-6× flagged honestly”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/BRAINLIFT.md inside it) (247-248): “a domain needs enough related-text volume (~6× vocabulary recurrence, multiple texts) to compound.”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/markdown/generation-contract.md inside it) (91-92): “domain words firmed in-lesson, not counted as Tier-2”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/CODEX-HISTORY-EVERYTHING-OUT.md` (78-79): “taught vocab must be recycled into Scout's speech and the show-what-you-know question”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/generated/feedback-2026-08-11-crosswalk.json` (347): “Reuse taught vocabulary meaningfully after the vocabulary cards instead of letting it disappear.”
- `grade3-reading/course-renderer/docs/rules/vocabulary.md` (146-149): “When the passage does not carry the word twice, the word is still earned if the lesson's own activities use it: the questions, answer options, feedback, sentence frames, the retelling cloze and the recap.”
- `grade3-reading/course-renderer/docs/rules/vocabulary.md` (254-256): “"students require 10 to 12 implicit or explicit encounters with a new vocabulary word across texts to successfully retain it, making standalone, disconnected lessons ineffective."”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (75): “Word,Class,Meaning (student-facing),Introduced,Stage,Linked to,Revisit in”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_08 10_30 CEST - Notes by Gemini.md` (490): “here's 30 hinge concept words that we want students to revisit over the course of a period of time.”
- `othello-course-renderer-draft/repo/docs/rules/vocabulary.md` (155-157): “When that check was first written, seven of the unit's nine taught words appeared exactly once in the passage they were taught for.”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (530-531): “say-it asking the child to say how they *reconciled* the sources, gloss restated, and to fit in evidence / decomposer / correspond”
- `grade3-reading/.claude/skills/one-perfect-lesson/SKILL.md` (55): “vocab recycled into speech + SWYK question”

Published: [Elleman, Lindo, Morphy & Compton 2009](https://doi.org/10.1080/19345740802539200)

Against: the rulebook gives the 10 to 12 figure as a ruling with no study beside it, and the shortfall against ten is only reported, since most encounters are owed by lessons not yet written. In a coherent text set, target words that recurred about 6 times were learned incidentally (η²=.625) with no meanings taught, so 10 to 12 is a ruling, not a measured threshold. The rule is only partly met: the exempt words and later lessons not yet built sit on a debt list (`grade3-reading/artifacts/criteria-register.csv`). The same doctrine reports that the largest effect in one coherent-text study was incidental vocabulary, with no meanings taught, when target words recurred about 6 times across the set (`grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd`, line 56), so planned recurrence alone can teach a lot. Vocabulary gains carry only partly into comprehension: in the Elleman et al. (2009) meta-analysis, vocabulary instruction helped comprehension on custom measures (d = 0.50) far more than on standardised ones (d = 0.10), and a study's vocabulary gain correlated only modestly with its comprehension gain (r = .43). The summary credits the figure of ten encounters to two authors without naming a study.

<sub>criterion · sequence, wording · universal · from g3, research · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Many strands, one of them new

Keep several strands of practice running across lessons, with only one bringing in new material while the rest review. One lesson-writing workflow composes lessons as interleaved tracks at about 90:10 review to new.

The direct-instruction rules a second-round review applied to the reading course say to keep multiple tracks alive over time, with only one introducing new material while the rest is review. The reading project's lesson-writing workflow builds this in, composing lessons as interleaved tracks at about 90:10 review to new.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (145): “- Keep multiple tracks alive over time; only one track should introduce new material while the rest is review.”
- `grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd` (43): “lesson composition as interleaved tracks at ~90:10 review:new”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-main-checkout-jul-work.patch` (20676): “| **All-new lesson composition** | lessons ~100% new content, review quarantined in a separate unit — DI track design says ~90:10 review:new, interleaved | per-lesson review:new census; does taught material keep returning? |”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v2/authoring/prompts/README.md` (37): “Every non-opener lesson is **majority review**:”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v2/authoring/prompts/README.md` (39): “Target by lesson role — **middle lessons ~70:30** (review:new), **unit openers”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v2/authoring/prompts/README.md` (40): “~50:50** (little prior to review; say so), **synthesis/cold lessons ~90:10**.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v2/authoring/prompts/README.md` (41): “Do NOT claim a flat 90:10”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v2/authoring/prompts/README.md` (42): “passage is always new, so a literal 90% review starves content.”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/markdown/generation-contract.md inside it) (86-88): “Middle lessons ~70:30 (review:new); openers/BUILD ~50:50 (little prior; say so); synthesis/transfer ~90:10.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/BRAINLIFT.md inside it) (176-178): “A literal 90:10 counts *information*; a reading dose can't hit that without starving content, so we count the *new operation/column* as the "new."”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/README.md` (42): “passage is always new, so a literal 90% review starves content.”

Against: A design rule, not a result: nothing here measured what the ratio does for learning, and the skill that uses it was unpromoted when it was recorded (`grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd`).

<sub>criterion · sequence, practice · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Model again when the genre changes

When the genre changes or texts get harder, model a strategy again with coached practice before independent use, rather than assuming what was learned on stories carries over.

An IES video on the gradual release of responsibility, quoted in a reading course's review standard, says the model is gone through back and forth many times and that a new genre may mean starting again with more of the responsibility on the teaching side (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/gradual-release-as-a-loop.md`). It places growth in the coached middle, where the student applies the strategy with plenty of guidance, and calls the big leap from explicit teaching straight to independent use the habit of less effective teaching. A second video, on informational text, asks for instruction in narrative and informational texts kept separate and very clear. The standard therefore tracks a strategy's release for each genre and difficulty band, not once for all texts.

Quoted:

- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/gradual-release-as-a-loop.md` (15): “if we introduce a new genre, we may need to start back up with the teacher having more responsibility.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/gradual-release-as-a-loop.md` (22): “less effective teachers will often make a big leap in their strategy instruction. They'll explicitly teach a strategy, and then they send kids off to use it on their own.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/gradual-release-as-a-loop.md` (14): “We go back and forth through this model many times.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/gradual-release-as-a-loop.md` (18): “And then the important middle is where the student is applying it, but the teacher is still there giving lots of support, lots of guidance, lots of coaching.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/gradual-release-as-a-loop.md` (29): “you really need to give students instruction in narrative and in informational texts, and those really have to be separate and very, very clear.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/gradual-release-as-a-loop.md` (33): “A strategy's release state is tracked *per genre/difficulty band*, not globally.”

Published: [A Gradual Release of Responsibility, IES video](https://www.youtube.com/watch?v=T-e6uHBDdNk) · [What are key considerations in teaching reading comprehension with informational text?, REL West video](https://www.youtube.com/watch?v=mYVKd_mog4M)

Against: none found

<sub>criterion · sequence, practice · universal · from g3, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Model beside the text

Model a reading only after students have read the whole text, and do it beside the text rather than after it.

Rulings on lesson structure (2026-07-16) say the child reads the whole passage before anything is modelled, and the modelling happens beside the passage, showing how to locate, re-read and reject candidate evidence on the actual text; a later ruling (2026-07-24) says it models the thinking, why this detail and not that one and what was rejected, never just a filled-in organiser (`grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd`). A review of showcase lessons found a model that treated picking the right animal as easy when the text also mentions two others, and asked that it show the choice is genuinely difficult (`grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd`). The modelling should also never make the thinking look easier than it is.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (28-29): “the child reads the *whole* passage before anything is modelled, and the modelling moment happens *beside* the passage”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (31-32): “the I-do must model *thinking* — why this detail and not that one, what was rejected and why — never just reveal a filled-in organiser.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (64): “The model should show that selecting the relevant animal and adaptation is genuinely difficult.”
- `g9/library/text/L36b8ba.txt` (286): “As built, the quote has been lifted out of the script, which means the app has already done the locating for the child.”
- `g9/library/text/L36b8ba.txt` (286): “Marking it in place shows where the evidence came from — and locating evidence in the text is the SEARCH and FIND skill.”
- `g9/library/text/L36b8ba.txt` (109): “Do not lift the quote out of the script. Extracting it performs the locating step for the child.”
- `g9/library/text/L36b8ba.txt` (108): “Keep the script on the left in guided practice. Mark the key quote in place within it.”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/generation-contract.md inside it) (62-64): “The student reads the complete passage (with a **read-aloud option** available — "hear it") *before any modeling*.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (142): “The five source-reading sections precede interpretation.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (57): “D1.9 Read before model — the full 4-part story (p6/p8/p10/p12) is read in its entirety before the I-do (p19); order confirmed by page sequence.”

Against: Rereading is a different matter: a later review said not to make whole-text repetition a universal ritual, and to reread the parts that serve the lesson's knowledge objective (`grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd`).

<sub>criterion · sequence, stimulus · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Model only what real readers do

In a modelled reading, show only actions a real reader takes on a text, such as rereading or highlighting, never crossing out or otherwise altering the passage.

Review feedback of 11 August 2026 on a Grade 5 reference lesson asked the modelling step not to cross out passage text, since that is not an authentic reading action, and to model instead rereading each candidate, explaining why weaker evidence falls short, checking the rest of the text and selecting the best evidence. The course's criterion for narrated models asks that each highlight or visible action come with the spoken reasoning, and rejects text altered in a way readers would not normally use. The mapping implies no verdict on the current course.

Quoted:

- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/generated/feedback-2026-08-11-crosswalk.json` (203): “Do not cross out passage text when that is not an authentic reading action.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/generated/feedback-2026-08-11-crosswalk.json` (211): “Model rereading each candidate, explaining why weaker evidence is insufficient, checking the remaining text, and selecting the best evidence.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/generated/instruction-review-profile.json` (283): “Where a narrated model changes the text, does each highlight or visible action occur with the spoken reasoning while only essential durable cues remain onscreen?”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/generated/instruction-review-profile.json` (287): “text is altered in a way readers would not normally use”

Against: none found

<sub>criterion · demand, stimulus · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Model the bridge to the text's wording

When the words a lesson tells learners to search for differ from the text's own wording, model the link between them before asking learners to search.

A case study of one Grade 3 reading lesson found that the lesson named one word as the search keyword while the passage expressed the same idea in a different phrase; the two had been treated as obviously equivalent, and learners were never shown that bridge before using the search term (`grade3-reading/ti-courseplans-wiki/Peter-Pan-Quality-Case-Study-2026-08-24.md`, lines 312-316). The repair had the model connect the search language to the passage wording before asking the child to use it, and the durable rule is that when procedure language and source language differ the synonymy must be modelled, or the course hides a required operation inside assumed knowledge (same file, lines 318-322). The prevention it names is a review of each search term against its source span and a locate trace played as the learner (same file, line 324).

Quoted:

- `grade3-reading/ti-courseplans-wiki/Peter-Pan-Quality-Case-Study-2026-08-24.md` (315-316): “The learner had not been shown that semantic bridge before using the search term.”
- `grade3-reading/ti-courseplans-wiki/Peter-Pan-Quality-Case-Study-2026-08-24.md` (318-319): “The model explicitly connected the search language to the passage wording before asking the child to use it.”
- `grade3-reading/ti-courseplans-wiki/Peter-Pan-Quality-Case-Study-2026-08-24.md` (321-322): “When procedure language and source language differ, expert synonymy must be modelled. Otherwise the course hides a required operation inside assumed knowledge.”

Against: The evidence is one lesson's case study, which says it is not a standard and is no evidence about lessons not inspected (`grade3-reading/ti-courseplans-wiki/Peter-Pan-Quality-Case-Study-2026-08-24.md`, lines 4-5).

<sub>criterion · demand, wording, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Model the side the learner didn't pick

In an argument task, let the worked example argue the side the learner did not pick, so it models the reasoning without handing over their case. The model case has three parts, an answer, its proof and why the proof proves it, and the learner's own case uses the same three.

The Grade 9 prototype has the learner pick a side after reading, then shows the guide's own case, a worked example in three parts (an answer, the proof and why it proves it) that argues the side the learner did not pick, and closes it by inviting the learner to beat it with a case of the same three parts built from two of their own marked lines. An earlier design canvas offers the same move as on-demand help, a strong reader arguing the opposite case for one paragraph, and the research brief behind the design suggests a rival reader whose weaker claim the student beats as a plausible way to build confidence, which it marks as its own inference. Nothing in the sources measures the effect.

Quoted:

- `othello-course-renderer-draft/repo/docs/design/grade-9/prototype/README.md` (28): “4. **Pick a side**, after reading, with the marked lines in view.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/prototype/README.md` (29): “a worked example in three parts (my answer, my proof, why it proves it), arguing the side the student did not pick.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/prototype/src/content/othello-3-3.json` (426): “That’s my case. I picked the other side on purpose, so now you get to beat it. Yours has the same three parts.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/prototype/README.md` (30): “**Your case**: the same three parts. Proof is two of the student's own marked lines.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/canvases/02-case-files.html` (47): “Show me how a strong reader starts”
- `othello-course-renderer-draft/repo/docs/design/grade-9/canvases/02-case-files.html` (47): “argues the opposite case for one paragraph.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (72): “A "rival reader" who sometimes makes a weaker claim for the student to beat is a plausible way to build confidence (that is my inference).”

Against: none found

<sub>criterion · practice, integrity · universal · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Model the thinking, not the answer

A worked example shows the reasoning, not just the answer: it thinks aloud where to look and why each tempting wrong choice is rejected, never making the thinking look easy.

The reading project's lesson-structure rulings say the modelling step must show thinking, why this detail and not that one and what was rejected and why, and never just reveal a filled-in organiser; one ruling likened a reveal-only model to copying a neighbour's work. A July 2026 review of the rebuilt course asked the same: the model should show that choosing the relevant detail is hard when the text offers several, and sound like an adult explaining their thinking, not a drill of questions. The worked example works on the source in view, weighs the tempting wrong choice and other plausible options, and rejects each for a reason that does not apply as well to the answer it keeps.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (32): “one, what was rejected and why — never just reveal a filled-in organiser.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (64): “Do not model the thinking as if it is easy.”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (24): “so the model never demonstrates the step it teaches”
- `grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md` (14): “model's "I know" repeats the conclusion”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (53): “The lesson defines a trait as repeated action, not a passing feeling”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md` (21): “a rejected think-aloud candidate whose aside argues for it”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md` (25): “| D1.10 | Model the hard part | PASS | States 4-7 show 4 plausible-but-wrong clues each weighed and rejected with genuine reasoning before the strongest is named |”
- `grade3-reading/artifacts/feedback-content-review-2026-09-20/REGISTER.md` (14): “Modeled answer must SHOW the choice when more clues are found than written”
- `grade3-reading/artifacts/feedback-content-review-2026-09-20/REGISTER.md` (16): “Avoid modeling "always exactly two"”
- `ti-courseplans-audit/docs/instruction-quality-standard.md` (16-17): “Revealing the answer is not modelling.”
- `ti-courseplans-audit/skills/course-red-team/SKILL.md` (163-164): “the screen says "watch" but only shows the organizer filled with the finished right answer.”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D1-gradual-release-explicit-instruction.md` (13): “The I-do models the reasoning step-by-step (where to look, what to weigh, what was almost picked and rejected); revealing/stating the answer is not modeling”
- `ti-courseplans-audit/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd` (52): “Visible evidence, a plausible alternative, the reason it is rejected, and construction of the answer are synchronized and semantically sound.”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (197): “This is modelling the thinking, not the answer.”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (16): “Scout weighs and rejects clues out loud | A model showing only the winning move teaches that reading is easy for other people”
- `grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md` (83): “think-aloud prose that **includes the explicitly rejected alternative** from `decision_point`”
- `grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md` (83): “pre-modeling the rejected alternative is canonical design, not a leak — the release re-elicits it cold”
- `grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md` (54): “Worked examples assemble the known — a novel step must be taught before it appears inside one.”
- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md` (179): “water is not evidence from this text") is exactly the epistemic move the unit”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md` (40): “3. I-do on the visible text, exposing the genuinely difficult judgment;”
- `grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd` (78-79): “(I-do models the rejected hunter-to-prey alternative; You-do re-elicits cold with `attempt_first:true` and "no hints before you try" — canonical, not a leak;”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd` (52): “Visible evidence, a plausible alternative, the reason it is rejected, and construction of the answer are synchronized and semantically sound.”
- `grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md` (77-78): “G3 iter-3's real "reject-the-alternative" modeling held in 1 of 18 lessons; the reviewed lesson (U2·L1) was that one.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (324-325): “every I-do step carried its span anchor and its rationale, and the screen performed none of them.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (325-326): “Modelling must *do* the step visually on the text at the moment it is narrated”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (191): “iter-3's real "reject-the-alternative" think-aloud existed in **3 of 18** lessons”
- `shadow-content-eval/reports/G3-U1-L11-review.md` (34): “The rule the student is shown doesn't separate the two lines.”
- `shadow-content-eval/reports/G3-U1-L14-review.md` (46): “6. **p19b think-aloud: the write-up uses lines the student just saw rejected.**”
- `shadow-content-eval/reports/G3-U2-L1-review.md` (86): “the stem and leaves evidence is marked `rejected`, then used”
- `g9/transformer/src/mechanics/worked-model.js` (1-3): “One quotation unpicked (the moment it comes from, what … it means, two or three of its words with their word class), then a model paragraph, one sentence per move with a … think-aloud beside each”
- `g9/transformer/src/mechanics/worked-model.js` (36): “how to answer the lesson question before the student writes, as a strong Grade 9”
- `g9/transformer/src/mechanics/worked-model.js` (46): “one sentence in the first person on why I write it”
- `g9/transformer/src/mechanics/worked-model.js` (107): “label: "Each think-aloud says what its sentence does", required: false”
- `g9/transformer/src/glue/animated.js` (226): “Watch how I answer today's learning question: I find a quotation, unpick its words, then write my answer one move at a time.”
- `g9/transformer/test/mechanics.test.mjs` (18): “at("worked-model") < at("cer-frame")”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v2/authoring/prompts/README.md` (62): “labels answers, it does not model thinking.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v2/authoring/prompts/README.md` (62-63): “At least one step must show the model *almost* taking the obvious-but-wrong path and catching it”
- `grade3-reading/artifacts/qc-2026-09-30-staging/FINDINGS.md` (38): “**M4. p19 model: the "I know" repeats the conclusion.** "I know a place like that feels gloomy and miserable, so I think the writer gives London a gloomy and miserable mood."”
- `grade3-reading/artifacts/qc-2026-09-30-staging/FINDINGS.md` (39): “I know it is unpleasant when it is cold and dark outside, so I think”
- `grade3-reading/artifacts/qc-2026-09-30-staging/SPEC-find-infer-procedures.md` (147): “What do I know about this - from vocabulary, real life, or earlier in the text?”
- `grade3-reading/artifacts/qc-2026-09-30-staging/SPEC-find-infer-procedures.md` (165): “I know that cold, dark places feel gloomy, unpleasant, and miserable”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (452-454): “Second, its evidence is degenerate. If the question is where the text shows Odysseus is clever, the answer is the wine and the name, one obvious stretch, and the rejections a modelling moment needs become fake.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (455-456): “a hunt with nothing genuinely rejected is a reveal, which is why `validate-contracts.mjs` requires a rejection at all.”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/judge/think-aloud-quality.md` (17-18): “Pass a think-aloud where a capable child could honestly have picked the rejected candidate, and the aside would change their mind using the text.”
- `grade3-reading/ti-courseplans/courses/g7g8-prealgebra/brainlifts/v0.1.md` (32): “The failure mode of prealgebra instruction is procedure-mimicry that collapses on transfer ("keep-change-flip" without why). Every KC is taught via gradual release with a **structural** worked example (why the manipulation preserves equality), then faded.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/MISCONCEPTION-COMPLIANCE-LOG.md inside it) (21): “a further 5 reintroduced during the teaching-move rework (U4-L6, U5-L4, U5-L7, U6-L1, U6-L2, where the "model-hard-thinking" rewrite voiced a misconception to reject it)”
- `othello-course-renderer-draft/repo/authoring/inputs/prompt-packs/reading-g3/judge/model-against-text.md` (7-8): “the narration reaches its conclusion BEFORE engaging the quoted lines, so the quotes decorate a conclusion reached elsewhere instead of producing it;”
- `othello-course-renderer-draft/repo/authoring/inputs/prompt-packs/reading-g3/judge/model-against-text.md` (9-10): “the write-up's conclusion does not follow from the chosen quote (a child granting the quote could still reasonably deny the conclusion);”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/README.md` (57): “Show exact evidence, a plausible alternative, why it fails, and how the selected evidence supports the interpretation.”
- `grade3-reading/ti-courseplans-wiki/Perfect-Course-Rulebook.md` (149-150): “The model considers and rejects at least one plausible alternative for a text-grounded reason”
- `grade3-reading/ti-courseplans-wiki/Reviewer-Feedback-2026-08-18.md` (16): “**The MCQ for the fix is already authored** — every `decision_point` has `plausible_alternatives` + `rationale`, just never shown”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-main-checkout-jul-work.patch` (20660): “| **Modeling the easy part** | round-3: "Which animal? — the Arctic hare" modeled as obvious when the text also names a fox + tree frog | does the modeled step have plausible wrong choices in the passage? is the hard selection actually modeled, adult-thinking-aloud not a question drill? |”
- `g9/transcript/chat-transcript.redacted.txt` (2628): “The mentor first demonstrates a genuinely difficult interpretive decision, including rejected alternatives.”
- `grade3-reading/edullm-review-hub/course-packages/quality/golden-student-course/versions/1.0.0/STANDARD.qmd` (335): “Narrating steps is not modeling unless the decision process is visible.”
- `grade3-reading/course-renderer/docs/rules/pedagogy-and-lesson-structure.md` (58-61): “a `think_aloud` node must carry at least two candidate sentences, exactly one marked chosen, every rejection must give a reason ("`.aside` must say WHY, or a rejection teaches nothing"), and it must have a `write_up`.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (303): “runs the Archivist’s reasoning beside each sentence rather than instead of it, so the child sees the decision”
- `g9/library/text/L36b8ba.txt` (303): “**The "My thinking" column** runs the Archivist’s reasoning beside each sentence rather than instead of it, so the child sees the decision — "I choose a short quote that proves my point" — not just the output.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/RESPONSE-MATRIX.md inside it) (45): “Every I-do now weighs and **rejects a real alternative**”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (58): “D1.10 Model the hard part — the I-do's candidates array shows 3 real near-miss distractor clues ('could not sleep', 'wide awake', 'bear clutched to his chest') genuinely weighed and rejected, not a trivial pick.”
- `grade3-reading/artifacts/u4l2-build/BEAT-SPEC.md` (343): “each is rejected (dims) as Scout's think-aloud dismisses it”

Against: Another file from the same review counts the move in 3 of 18 lessons, not 1 (`grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md`, line 191).

<sub>criterion · demand, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Name the next idea, not its slot

Link to what comes next by naming the next idea and why it follows, never by position such as 'in the next video', because the order can change.

The video-script rubric's bridge must name the actual next idea and the hinge between the two, anchored to the concept relationship rather than the playlist slot, so it stays coherent when the review queue reorders lessons (`shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt`). Positional references to a neighbouring lesson assert a teaching-order fact that can't be checked, since under batched or parallel generation the true neighbour is unknown (`shadow-bench`, git commit a8818e0). A high-precision detector in code now flags such references and downgrades the script's structure score. Numbered references such as 'lesson 7' are positional too, and the same commit asserts, without a count, that a named neighbour is often wrong.

Quoted:

- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (52): “- **Phrasing rule:** anchor the bridge to the concept relationship ("now that you know X, Y follows because…"), NOT to the UI or playlist slot ("in the next video…"). This keeps the bridge coherent even when the retrieval queue reorders review.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (51): “The bridge must be specific: it names the actual next idea and states the conceptual hinge between them.”
- `shadow-bench/` (commit a8818e0) (5-8): “Positional / UI-coupled references to a specific neighbouring lesson ("in the last video", "coming up next", "Lesson 7", "two lessons ago") assert an unverifiable teaching-order fact. Under batched/parallel generation the true neighbour is unknown, so a confidently-named one is frequently wrong”
- `shadow-bench/` (commit a8818e0) (9-10): “Safely-vague forms ("earlier in the course") are fine.”
- `shadow-bench/` (commit a8818e0) (12-14): “tools/relational_reference.py (shared): high-precision detector — flags only clearly positional/UI-coupled/numbered references, so it can drive a downgrade with a low false-positive rate; soft "an earlier lesson" is left to the LLM.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/v0.2.md` (93): “The first pilot videos were technically accurate but felt "random"”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/v0.2.md` (93): “began mid-explanation and switched concepts with no marker”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-generation-v0.1.md` (60): “At every concept boundary the **spoken narration itself must introduce the next concept with a smooth, natural connective bridge**”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-generation-v0.1.md` (60): “no silent jumps”

Against: Vague references are allowed: 'Safely-vague forms ("earlier in the course") are fine.' (`shadow-bench`, git commit a8818e0, lines 9-10). That a named neighbour is 'frequently wrong' is asserted from an internal guide, not counted (the same commit, lines 8-9).

<sub>criterion · sequence, wording, integrity · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Name the parts before the process

Teach the names of a system's parts before explaining how they work together, so learners are not identifying parts while following their relations. Teaching the part names first has a median effect size of about 0.75 to 0.92.

The grade-7 science visual design guide pre-trains names before teaching a process, because a learner cannot follow relations among parts while also identifying those parts for the first time, and naming first reduces the processing the later explanation needs (`grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-visuals-human-v0.1.md`, lines 156-165). It cites pre-training effects with a median around d=0.75–0.92 (Mayer & Pilegard), and its example identifies the cell membrane, nucleus and mitochondrion before explaining how the membrane controls exchange. Its storyboard rules split naming from the process explanation whenever more than about three to five new labels would appear at once (line 259).

Quoted:

- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-visuals-human-v0.1.md` (161): “**Evidence.** Pre-training effects have a median around *d*=0.75–0.92 [18].”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-visuals-human-v0.1.md` (157-158): “A learner cannot follow relations among parts while also trying to identify those parts for the first time.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-visuals-human-v0.1.md` (259): “Show about 3–5 concurrent new labels at most; otherwise split naming from process explanation.”

Published: [Mayer & Pilegard, Cambridge Handbook of Multimedia Learning](https://www.cambridge.org/core/books/cambridge-handbook-of-multimedia-learning/principles-for-managing-essential-processing-in-multimedia-learning-segmenting-pretraining-and-modality-principles/4110A2275F6DCD02DAB1F8B37BA7E5CE)

Against: The guide expects pre-training, like signalling and segmenting, to add most when prior knowledge is low (`grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-visuals-human-v0.1.md`, lines 244-245), and its three-to-five-label limit is an operating heuristic.

<sub>criterion · sequence, media · universal · from g3, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Name the term and show the instance

For young students and novices, say the term and show a concrete instance of it together, never one without the other.

An intro-video BrainLift for a Grade 3 reading course cites Ausubel (1968): elementary pupils and novices cannot process abstract propositions verbally without concrete and specific exemplars available at the same time or just before, and teaching that ignores this produces "rotely memorized and empty verbalisms" (`downloads/BrainLift - What makes a good intro video.md`, line 455). Its narration rule is to name the term and show the instance together, and never the instance alone either, because compression strips the terms first and a scene of two animals is not yet the characters until somebody says so (line 319). The source gives no DOI or link for the 1968 work.

Quoted:

- `downloads/BrainLift - What makes a good intro video.md` (455): “Elementary pupils and novices cannot process abstract propositions verbally without”
- `downloads/BrainLift - What makes a good intro video.md` (455): “So the rule is name the term and show the instance, never the term alone.”
- `downloads/BrainLift - What makes a good intro video.md` (319): “Name the term, then show the instance — "Every story happens somewhere. We call that the setting" — never the instance alone.”
- `grade3-reading/course-renderer/docs/video/u1-script-and-visual-plan.md` (81-82): “two beats gesture at xenia, treating a stranger who knocks as its own test, without using the word "xenia" itself, since the word is not introduced until `U1T6`”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (598-601): “One decision this raises: do not give the child the Greek word xenia at L2. The graph reserves the naming for L6, and R-KC-5 wants prior knowledge reused rather than re-taught, which works better if L6 gets to attach a new name to a concept the child already holds.”
- `g9/film/v07/README.md` (12): “Define with an example: we hear "I am not what I am", Othello does not”
- `g9/film/v07/README.md` (12): “a step between the quote and the definition: "Othello never hears it · We do"”
- `g9/script/v04/Othello-Opening-Recording-Manifest.json` (70): “Othello never hears this. We do. That is dramatic irony: the audience knows something a character doesn’t.”
- `g9/library/text/L30b6dc.txt` (12): “| Define with an example: we hear "I am not what I am", Othello does not | a step between the quote and the definition: "Othello never hears it · We do" |”

Against: A later run found: A reading unit's opening film shows an idea in two beats without its technical term, on purpose, because a later lesson names it, and lesson research for the unit held that the later lesson attaches the name better to a concept learners already hold. That is the instance before the term, which this record rules out; the new record Teach the idea before its name carries the rule (`grade3-reading/course-renderer/docs/video/u1-script-and-visual-plan.md`).

<sub>criterion · wording, media · universal · from g3, research · external-research · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### No false rejections in a modelled hunt

In a modelled evidence hunt, never reject a line that is true evidence of something nearby: say what it shows and why the question asks for something else.

Planning the think-aloud for an evidence question, a lesson's research note kept one candidate line instead of rejecting it: the line shows a character breaking a rule, while the question asks what he thought of the rule, and the guide says so aloud. The note calls this the genuinely hard move the course's modelling rule asks for, and safer than rejecting the line outright, which would teach a false rejection (`grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md`, lines 746-750). The decided lesson plan carries the same ruling (`grade3-reading/course-renderer/content/lesson-plans/g4-u1-l2.json`, line 483).

Quoted:

- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (746-750): “Considered and kept, not rejected: the line where he eats two of the men. The guide says aloud that this shows he broke the rule, and that the question asks what he thought of it, which is why the two chosen lines are the answer. This is the genuinely hard move R-PED-5 asks for, and it is safer than rejecting the eating outright, which would be teaching a false rejection.”
- `grade3-reading/course-renderer/content/lesson-plans/g4-u1-l2.json` (483): “Rejecting the eating outright would be teaching a false rejection, since it is evidence, just not for this question, and holding it is the genuinely hard move R-PED-5 asks for.”

Against: none found

<sub>criterion · demand, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Notice a breakdown, then reread to repair

Teach comprehension monitoring as two steps, noticing a breakdown by trying to say what the part is about, then rereading to repair it, not as an abstract instruction to monitor.

A reading course's review standard, citing IES videos on monitoring comprehension and on self-monitoring and self-correcting, makes monitoring a concrete routine: flag the breakdown with a confusion signal or the paraphrase test, then reread to repair it and retest (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D3-reading-architecture.md`, line 21). An instruction to monitor your understanding names a goal, not a behaviour, so a reader who is lost has no procedure to run (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/comprehension-monitoring-repair-routine.md`). Prediction items follow the same pattern: once the evidence arrives the learner updates the guess, rather than guessing once.

Quoted:

- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D3-reading-architecture.md` (21): “Comprehension-monitoring is a concrete two-move routine — flag the breakdown (a confusion signal or the paraphrase test 'say it in your own words or you didn't get it') then reread-to-repair — not an abstract 'monitor your understanding'”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D3-reading-architecture.md` (24): “Prediction items force an *update* after evidence ('I predicted a doctor… my prediction was wrong — what is he?'), not one-shot guessing”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/comprehension-monitoring-repair-routine.md` (10): “it names a goal, not a behavior, so a child who is failing to comprehend has no procedure to invoke”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/comprehension-monitoring-repair-routine.md` (7): “when a prediction was involved — explicitly update the wrong guess”

Published: [Monitor Comprehension (PRISMS), IES video](https://www.youtube.com/watch?v=TB_dW-BJg_Q) · [Self-Monitor Understanding and Self-Correct Word-Reading Errors, REL Southeast video](https://www.youtube.com/watch?v=biZE2DPyiDU)

Against: none found

<sub>criterion · practice, demand · universal · from g3, research · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### One focus per screen

Give each screen one primary thing to attend to.

The walkthrough of a built Grade 3 lesson applies an attention standard distilled from reviews: each screen has a single thing to attend to, because attention is the scarcest resource and split screens split learning, and help appears at the step that uses it, never stacked upfront, because support on arrival is clutter and support at the point of use is scaffolding (`downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md`, lines 27 and 28; `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md`, line 13). No outcome was measured.

Quoted:

- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (27): “Each screen has a single thing to attend to | Attention is the scarcest resource; split screens split learning”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (28): “Help appears at the step that uses it, never stacked upfront | Support on arrival is clutter; support at the point of use is scaffolding”
- `grade3-reading/ui-audit-2026-09-08/gold-standard/aladdin-p1-ui-review.reference.md` (19): “Pick one forward control, keep it bottom right, and make it the only filled button on the screen.”
- `grade3-reading/_archive/2026-08-13-consolidation/orientation-sweep-digest/workspace-docs.md` (8): “the original course experience opened by dumping authored diagram prose, repeated labels, a "look closely" guide, and mismatched narration instead of one obvious Grade 5 action”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/BRAINLIFT.md` (112): “One ask at a time. Screen clutter is a pedagogical defect, not a cosmetic one.”
- `grade3-reading/course-renderer/docs/process/ATTENTION-HIERARCHY.md` (15-16): “**Name the ONE primary.** Every screen has exactly one thing the child must attend to. If you cannot name it, the page is two pages — split it.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md` (340): “So the student shouldn't be seeing too many things on the screen at once.”
- `othello-archive/src/steps/Guided.tsx` (5): “Only the quote and one word are in focus at a time.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (75): “Keep one primary learning action in focus at a time.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/05-UI-UX-PRINCIPLES.md` (207-209): “When a video checkpoint surfaces, the video disappears entirely and the question takes the stage alone, with a Watch again pill on the check card so the child can re-view before answering.”

Against: none found

<sub>criterion · demand, hints · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### One hard prerequisite per lesson

Let a lesson depend on at most one hard prerequisite, and treat needing more as a sign the lesson is oversized and should be split, not given more gates.

Sequencing briefs for a Grade 3 and a Grade 6 reading course cap hard prerequisites at one per lesson. In the Grade 3 brief a hard prerequisite is an earlier lesson in the unit without which the lesson's task breaks, and each lesson teaches exactly one new operation and depends on what at most one earlier lesson added. Exceeding the cap is read as an oversized lesson, not as a need for more gating; the Grade 6 brief ties the cap to a test of whether the earlier knowledge can be retrieved at the point of use. It is a declared rule for lightly gated reading courses; no outcome was measured.

Quoted:

- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/SEQUENCING-BRIEF.md inside it) (91-92): “**Max hard prereqs per lesson: 1.** Each dose teaches exactly one new operation and depends on at most one prior within-unit column. Exceeding this signals an oversized lesson, not a gating need.”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/sequencing-brief.md inside it) (139-140): “**Max hard prereqs per lesson: 1** (point-of-use retrievability test — the curriculum-graph guidance). Exceeding it signals an oversized KC, not more gating.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/SEQUENCING-BRIEF.md inside it) (87-88): “a lesson whose task breaks if the prior lesson is deleted.”

Against: none found

<sub>criterion · sequence, demand · domain · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### One idea per teaching piece

Give each short teaching piece exactly one idea: something that can be stated as a single testable sentence. A well-sized idea can be explained in under 60 words and tested by a single multiple-choice question.

The evaluator's check for short instructional video scripts treats one knowledge component per video as critical: an idea that can't be stated as a single testable proposition is likely two (`shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt`). Its test asks whether two independent multiple-choice questions could be written from the script, each on a different core concept, with a student able to answer one without knowing the other. A well-sized idea can be expressed in under 60 words and tested by a single question.

Quoted:

- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (22): “If a KC cannot be stated as a single testable proposition, it is likely two KCs.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (233): “**The two-MCQ test:** Could you write two independent MCQs from this script, each testing a different core concept, where a student could answer one without knowing the other? If yes, the script is teaching two KCs.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (229): “**What this checks:** Whether the script teaches exactly one KC — one idea that can be expressed in under 60 words and tested by a single MCQ.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (252): “- Explaining all steps of a single multi-step process (depth within one KC is allowed)”

Against: Depth within one idea is allowed: '- Explaining all steps of a single multi-step process (depth within one KC is allowed)' (`shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt`, line 252).

<sub>criterion · alignment, sequence, media · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### One key idea, restated at the close

Give each lesson one key idea and close on it, with the student restating it, finding evidence for it in the text and applying it as support fades.

A unit knowledge base gives each lesson one key threshold the child should walk away knowing, with a second carried subtly, and has every child leave having restated that threshold with evidence. A walkthrough of a rebuilt lesson reports that a conformance review found the closing statement missing everywhere, and that it now lands in every lesson. Built lessons are checked for that close.

Quoted:

- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx` (sheet 'Overview', cell A3): “each lesson teaches ONE key threshold (in red) that the child should walk away knowing, with a second threshold carried subtly.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx` (sheet 'Overview', cell B36): “so each child leaves having restated the threshold with evidence.”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (345): “your conformance review found it missing everywhere; it now lands in every lesson”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (133-134): “The pattern, novice-to-expert on one idea moved three times, production only, no MCQ / word bank / tap-to-fill anywhere in the closing three:”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (268): “moving from mimicry, to application to the text, to evaluation at the end.”
- `grade3-reading/knowledge_bot/knowledge/kb-0225-g3-closing-questions-adoption-2026-09-24.qmd` (35): “support fades and never returns (max→frame→none)”
- `grade3-reading/knowledge_bot/knowledge/kb-0225-g3-closing-questions-adoption-2026-09-24.qmd` (38-39): “**rule 10** — the Name-it sentence recurs at the start of the next part, produced not shown, on a "Look back" page.”
- `g9/transformer/src/mechanics/say-it-back.js` (10): “const MAX_WORDS = 16;”
- `g9/transformer/src/mechanics/say-it-back.js` (52): “true to the text, answering the question, plain enough to”
- `g9/transformer/src/mechanics/say-it-back.js` (86-87): “Is sentence true to passage? … Does sentence answer lesson_question?”
- `g9/transformer/src/mechanics/say-it-back.js` (104): “That is the sentence. Keep it: you will need it again.”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (268): “moving from mimicry, to application to the text, to evaluation at the end”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (272): “Use the modeled method in a structured way.”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (273): “Apply the method to new evidence from the text.”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (274): “Make and justify a judgement on the learning question.”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (268): “They are developed separately and are not held in the knowledge base.”
- `g9/transformer/src/mechanics/say-it-back.js` (1): “Say it back: the first of the Grade 9 close questions (mimicry, then application, then evaluation).”
- `g9/transformer/src/mechanics/say-it-back.js` (2): “the lesson's answer in one sentence, its key words defined on hover; the student says or types it back.”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “It rewards repeating the guide's words, so keep it to one per lesson.”
- `g9/transformer/v02/QA.md` (117): “in lesson order: WW FM LQ KW | GL QC OC EH WF DL | WM CER CA | SB DB.”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (40): “CARRIED THRESHOLD KNOWLEDGE - short and catchy, said back in mimicry”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (41): “Threshold knowledge (full),Catchy version (students say it),Tested in,Carried forward to”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (42): “L1 Task 1 mimicry; L2 retrieval,Every Iago lesson”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (140): “says the sentence; the student repeats it”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (140): “TASK 1 mimicry (the Archivist says the sentence; the student repeats it). TASK 2 apply to the extract. TASK 3 evaluate (""X or Y?"").”
- `grade3-reading/artifacts/arc-audit/L5.md` (87): “The wants/feelings threshold appears 3 times; the repeated-action framing appears 6+ times and owns the subtitle and the closing receipt — i.e., it's not a minor gloss, it's the thing the child actually walks away remembering.”
- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L4-2026-09-05.md` (144-145): “"the closing screen is where the threshold lands or dies"”
- `grade3-reading/.claude/skills/lesson-build/SKILL.md` (70-71): “The closing screen must land the lesson's KB threshold verbatim — it is where the threshold lands or dies (L5 shipped with it displaced by a sub-heuristic).”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (241-242): “the Wrap restates it FOR the child (line 495) instead of eliciting it.”

Against: The conformance finding is second-hand: the walkthrough reports another review's result.

<sub>criterion · evidence-of-learning, alignment, sequence · universal · from g3, g9 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### One process, falling support

Modelling, guided practice and independent practice should run the same skill under the same step names, with support that only falls, so they read as one process with labels stripped. A check in code catches all three ways this failed in one review round: the answer shown as the model, a hint as the guided step, and a switch of skill as the independent one.

The reading course standard calls the I-do, we-do, you-do routine one process practised three ways, never three activities, and its acceptance test is that with the labels stripped the three still teach the same process at decreasing support (`grade3-reading/ti-courseplans/docs/instruction-quality-standard.md`, lines 13-25). A review round found all three ways this fails, and a deterministic lint now catches them, among 6 of the 10 failure shapes that round found (`grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md`, lines 69-71). A clean-room review found independent work returning to the model's own example and evidence instead of new evidence (`grade3-reading/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-ENTRYPOINT-CLEAN-ROOM-G3-U4-L1-2026-08-06.qmd`, lines 57-58). Guided work leaves the substantive step unfinished (`grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json`, line 245), and the independent step is never more scaffolded than the guided one by default: extra help there is offered after a first miss (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md`, lines 332-337). The same skill and step names run through to the recap. The model shows the thinking rather than the answer, guided practice is a part-finished task the student completes rather than a hint, and independent work does the same operation on new material with the least help.

Quoted:

- `grade3-reading/ti-courseplans/docs/instruction-quality-standard.md` (13-14): “The I-do / we-do / you-do routine is **one process practiced three ways**, never three different activities”
- `grade3-reading/ti-courseplans/docs/instruction-quality-standard.md` (16-17): “Revealing the answer is not modelling.”
- `grade3-reading/ti-courseplans/docs/instruction-quality-standard.md` (20): “A hint is not a we-do.”
- `grade3-reading/ti-courseplans/docs/instruction-quality-standard.md` (22): “Switching to a different skill is not a you-do.”
- `grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md` (70-71): “including all three gradual-release exploits (answer-reveal I-do, hint-style we-do, skill-switch you-do)”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json` (245): “Guided work leaves the substantive learner move genuinely unfinished and increases support without completing it for the learner.”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-ENTRYPOINT-CLEAN-ROOM-G3-U4-L1-2026-08-06.qmd` (57-58): “You-do returns to the model's animal, evidence, and constructed answer instead of requiring the same operation on new evidence.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (332): “The gradient half: a you-do step may never be more scaffolded than the corresponding we-do step.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (335-337): “a scaffold added at the released end is offered **after a first miss**, not imposed as the default — available rather than mandatory.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (342-343): “U1-L1's step-4 gap-fill ships as the default, so the lesson carries a known and deliberate D1.15 inversion”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (317): “Claim boundary: Surface format may change only when the target operation remains demonstrably stable.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (60): “I-do reveals the answer instead of modeling thought; we-do is only a hint; you-do sometimes switches to a different skill.”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (31-32): “the I-do must model *thinking* — why this detail and not that one, what was rejected and why — never just reveal a filled-in organiser.”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (34-36): “the we-do gives a *partial* answer the child completes (a hint is not a we-do, a fresh question is not a we-do); I-do, we-do and you-do must run the *same skill*, never switch mid-lesson.”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (83-84): “the teacher models every step up to but not including the final substantive thinking move; the child does that move”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (84-86): “exception: MAIN IDEA step 4 "Check coverage," where the child composes the summary and the teacher verifies aloud, because composing is the real cognitive work”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-1/teacher-skill/candidate/brainlifts/core/gradual-release.md` (17): “Acceptance test: strip the I-do/we-do/you-do labels; a reviewer must still see one process at decreasing support (standard §1).”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-1/teacher-skill/candidate/brainlifts/core/gradual-release.md` (21): “The labels are where generators fail: round-2 found correctly-labeled sections with wrong substance (answer-reveal I-do, hint we-do, skill-switch you-do). Test substance, never labels.”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (136): “gradual-release fidelity: labels alone are insufficient;”
- `grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd` (43-44): “gradual-release doses that survive the strip-the-labels test”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (34): “the we-do gives a *partial* answer the child completes (a hint is not a”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (35): “we-do, a fresh question is not a we-do); I-do, we-do and you-do must run the *same skill*, never”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (60): “The I-do/we-do/you-do routine is misapplied: I-do reveals the answer instead of modeling thought; we-do is only a hint; you-do sometimes switches to a different skill.”
- `grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd` (55): “**MAJOR — we-do renames three of the four I-do step labels (R-KC-11).**”
- `grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd` (56): “agree verbatim on all four step labels”
- `grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd` (58): “we-do (`p21`) diverges on all four”
- `grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd` (44): “that survive the strip-the-labels test”
- `grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt` (14): “the "I do" only reveals the answer instead of modelling the thought process; the "we do" only offers a hint; the "you do" switches to a different skill (supporting details).”
- `grade3-reading/artifacts/arc-audit/SIM-REVIEW-D1-D4.md` (29): “- **Criterion:** D1.6 (Triple-presence: model/guide/release share an identical ordered step list),”
- `grade3-reading/artifacts/arc-audit/SIM-REVIEW-D1-D4.md` (27): “L5 you-do drops Step 1 and Step 3 of its own four-step rail”
- `grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md` (94): “Never rename a step mid-lesson. The names must survive the strip-the-labels test (they describe”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md` (12): “| L1 | triple-presence | model, guide, release atoms exist for the lesson's operation_id, with one identical, non-empty ordered step list. Catches the round-2 answer-reveal I-do (payload only the answer = empty steps). |”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (280-281): “I-do/we-do/you-do is misapplied (answer reveal / hint / different skill)”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (46): “Gradual release is one process at decreasing support: the I-do models *thinking*, the we-do walks the same steps with immediate feedback, the you-do releases the same skill”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md` (21-23): “The two **semantic** checks in section 5 -- think-aloud authenticity (reasoning trace vs answer reveal) and release-item operation classification -- are advisory until an LLM-judge calibration pass and are deliberately NOT implemented here.”
- `ti-courseplans-audit/docs/course-creation-spovs.md` (106-109): “round 2 found our gradual release **misapplied**: the I-do revealed answers instead of modelling the thought process, the we-do gave hints instead of walking the same steps with immediate corrective feedback, and the you-do switched skills.”
- `ti-courseplans-audit/docs/instruction-quality-standard.md` (24-25): “strip the labels; a reviewer must still be able to say "these three artifacts teach the same process at decreasing support."”
- `ti-courseplans-audit/skills/course-red-team/SKILL.md` (159-160): “the RECURRING rejection theme "poor instructional decision making"”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (142): “- Gradual release means model the thought process, let the student practice the same process with guidance, then release the same process to independent work.”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (35-36): “I-do, we-do and you-do must run the *same skill*, never switch mid-lesson.”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md` (17): “every non-review atom carries exactly the lesson's one `operation_id`.”
- `grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd` (80-82): “a lesson teaches ONE procedure across three stages (modelling / we-do / you-do); RULE 1 (STEP LABEL DRIFT, shipped) requires the step be named identically at all three stages”
- `grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd` (55): “MAJOR — we-do renames three of the four I-do step labels (R-KC-11).”
- `grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd` (65): “NO-GO stands; semantic lints remain advisory.”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/L6-VALUE.md` (23): “so what is modeled matches what is asked.”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAP-CLOSURE-PLAN-2026-09-15.md` (46): “The detector's census found one more SHIPPED defect of the class: L5 p16 `youdo-clue-hunt` "Step 2: Find the clues" vs the model's and the we-do's "Look for clues"”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (114): “The we-do write-up frame has only one quote blank, while the I-do models two pieces of evidence and the you-do (p16) asks for two”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md` (34): “child the six-statement judging task cold”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/L6-VALUE.md` (36): “Refine arrives unmodeled”
- `shadow-content-eval/reports/G3-U1-L14-review.md` (6): “the lesson teaches a two-line "then line + now line" method, but the model, the guided practice and the solo practice all use one "now" line, and the recap then says the student found both.”
- `shadow-content-eval/reports/G3-U1-L12-review.md` (30): “In the one guided rehearsal, the student never practises "Find what it caused".”
- `shadow-content-eval/reports/G3-U1-L11-review.md` (44): “5. **p20 `finish-the-writeup` and p21 `step4`: the sentence frames leave out Step 4's "I know" part, although the lesson teaches it and the recap says the student did it.**”
- `shadow-content-eval/reports/G3-U1-L14-review.md` (56): “9. **p20 we-do step names don't match the four steps taught on p18-intro.**”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (223): “A we-do is a partial the child completes — not a hint, and not a second demonstration.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx` (335 (textutil text)): “The Modelling Moment guides (pre-glowed evidence, auto-highlighted Refine, teacher whiteboard); the Independent Task releases (unassisted hunt with feedback ladder, child-written 3-blank frame, judge-then-check Refine with retry ladder).”
- `downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx` (28 (textutil text)): “The child completes the final step only — one typed gap that carries the inference (“…so I think ___”) — with the modelled steps kept visible beside it.”
- `downloads/BrainLift - What makes a good intro video.md` (327): “The knowledge is permanent; the explaining is temporary.”
- `downloads/BrainLift - What makes a good intro video.md` (329): “A pattern the narrator used to state can become a retrieval question before the video.”
- `downloads/BrainLift - What makes a good intro video.md` (457): “This is the evidence base for fading: more structure early, less later (SPOV 8).”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (227): “design docs go straight from Modelling Moment to Independent Task — they contain no we-do.”
- `downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx` (24 (textutil text)): “This modelling never fades.”
- `shadow-content-eval/references/closing_questions_pattern.md` (72): “3. Support fades and never returns.”
- `shadow-content-eval/references/closing_questions_pattern.md` (87): “| Expertise reversal / fading guidance | well evidenced |”
- `shadow-content-eval/reports/G3-U2-L1-review.md` (51): “- The cloze is also selection (`inline_choice`), which is support coming back after Q3 had none. That breaks "support fades and never returns".”
- `shadow-content-eval/reports/G3-U2-L1-review.md` (165): “Q3 carries a `nudge`, a keyword-triggered `nudge_if` (#13), a `hint` and a `second_hint`. That is more scaffolding than Q2's slots have. The spec says Q3 has none.”
- `shadow-content-eval/reports/G3-U1-L2-main-review.md` (12): “- **New high:** the p24b tap-to-fill cloze comes after Use it (CLOSE-AFTER-USE). That's the same problem as G3-U2-L1 high #2.”
- `g9/transformer/web/lesson.js` (583): “Practice.tsx Model, plainly: the quotation unpicked (GuidedScreens), the sentence rebuilt blank by blank (Rebuild:”
- `g9/transformer/web/lesson.js` (584): “a wrong pick goes red and stays out), then the paragraph with the guide's thinking beside each move”
- `g9/transformer/src/glue/threejs-render.js` (331): “Now the model is hidden. Rebuild sentence”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (350): “In the we-do the teacher starts the work, thinks aloud through part of it, and the child finishes that same step with support. A hint is not a we-do, and asking a fresh question is not a we-do.”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants-draft-v2.dom.txt` (93): “Every we-do must start the work for the student (a partial answer, guided steps, immediate corrective feedback) rather than handing over a fresh question — that is a you-do arriving early.”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (366): “Independent practice still walks the procedure. Each step gets a task proving the child did it”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (389): “### G5-POL-INS-003: Make every We-do one genuine shared answer: the teacher authors a content-bearing opening clause, the learner finishes that same answer while the opening and passage evidence remain visible, and misconception-specific support increases without completing the learner's contribution.”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (392): “- **Rationale:** Doing one operation step and assigning the next is still sequential independent work. Guided practice requires teacher and learner to co-construct one response before independent release.”
- `grade3-reading/_archive/2026-08-13-consolidation/council-human-handover-2026-08-13/04_HUMAN_CHECK_LESSONS.md` (29): “**What went right:** Grade 3's map/explorer/retrieval/writing strengths were preserved as explicit requirements while fake I-do, fake We-do, passive vocabulary, missing oral production, copy-first writing, clutter, and weak responsibility transfer became explicit defects.”
- `grade3-reading/_archive/2026-08-13-consolidation/adversarial-course-council/initiatives/02-g5-feedback-and-teaching-flow-hardening/HANDOVER.md` (84): “- Cosmetic labels for I-do/We-do/You-do are insufficient without observable passage/task state changes.”
- `grade3-reading/_archive/2026-08-13-consolidation/orientation-sweep-digest/agent-damage.md` (63): “prior round: RT-R2 NEW-4 found teaching-move claims with 0/48 lessons carrying the moves”
- `grade3-reading/_archive/2026-08-13-consolidation/orientation-sweep-digest/agent-damage.md` (18): “EV: Same RT-R3 report, section 2: find-then-write went 0/48 → 45/48 generated lessons; feedback median 24 words (old ~91-word lineage gone); verified by independent recomputation”
- `grade3-reading/course-renderer/docs/rules/pedagogy-and-lesson-structure.md` (106-108): “In the we-do the teacher starts the work, thinks aloud through part of it, and the child finishes that same step with support. A hint is not a we-do, and asking a fresh question is not a we-do.”
- `grade3-reading/course-renderer/docs/rules/pedagogy-and-lesson-structure.md` (117-118): “Enforced for plans by `scripts/validate-lesson-plans.mjs` (exactly one procedure step belongs to the child).”
- `grade3-reading/course-renderer/docs/pedagogy/lesson-architecture.md` (63-65): “So the we-do here is a started sentence with the evidence slot filled and one gap left, in the procedure's own frame, not a fresh multiple-choice question with a hint bolted to its stem.”
- `grade3-reading/course-renderer/docs/extras/alpharead-fading-guidance.md` (64): “The sentence stems never fade (DI step language) — only their pre-fill does.”
- `grade3-reading/course-renderer/docs/extras/alpharead-writing-scaffold-overview.md` (31): “The stems themselves are permanent (like the DI step language) — only their *pre-fill* fades.”
- `grade3-reading/course-renderer/docs/extras/alpharead-writing-scaffold-overview.md` (29): “how much of the frame is *pre-filled* shrinks — full echo → clause starter → bare stem → blank box (entry 5) — and how much help the child gets *finding the evidence* shrinks — passage shown → region only → nothing (entry 2).”
- `grade3-reading/course-renderer/docs/extras/alpharead-fading-guidance.md` (32): “Last text = COLD Stage-1: known procedure, new content, no MM, no stems.”
- `grade3-reading/course-renderer/docs/rules/pedagogy-and-lesson-structure.md` (137-139): “**Rule.** Independent practice still walks the procedure. Each step gets a task proving the child did it: click the thing you are looking for, click the first line of the paragraph to reread, tap the evidence, then a gap fill as modelled.”
- `grade3-reading/course-renderer/docs/rules/pedagogy-and-lesson-structure.md` (141-143): “The app still needs to support students to do each of these steps. **Have each step appear with a task that demonstrates they have done the step.**”
- `grade3-reading/course-renderer/docs/rules/pedagogy-and-lesson-structure.md` (148): “Followed by convention”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (45): “Independent practice that changes interface removes the scaffold and the shape of the task at the same time, so the student has nothing left to imitate. Gradual release should remove support and keep structure.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (47): “"Hide the model, I’ll try" keeps the grid and empties it. That is the pattern to apply at every handover in the app.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (321): “The model was one quote, two words, five stem-built sentences. The independent practice is three quotes, conversational, with no stems and no sentence count. Nothing a child learned on the modeled screen transfers to this one.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (122): “Rebuild independent practice to replicate guided practice: text visible, the same stem grid, the same five-sentence shape.”
- `g9/sources/_KB_Othello_1_1_Lesson_View.md` (8): “Stems available, but students are locked out of writing about the guided practice quote.”
- `g9/library/text/L36b8ba.txt` (45): “Independent practice that changes interface removes the scaffold and the shape of the task at the same time, so the student has nothing left to imitate. Gradual release should remove support and keep structure.”
- `g9/library/text/L36b8ba.txt` (47): “The prototype already contains the correct mechanism. "Hide the model, I’ll try" keeps the grid and empties it. That is the pattern to apply at every handover in the app.”
- `g9/library/text/L9b6d99.txt` (308): “The app decides when and where extra guidance is given.”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/pedagogy-policy.json` (1179): “Make every we-do a step handoff in which the learner completes omitted steps through blocking responses with explicit acceptance rules.”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/pedagogy-policy.json` (1180): “A hint followed by passive continuation is not guided practice.”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/README.md` (65-66): “each is a real blocking response with an acceptance rule;”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/generation-contract.md inside it) (76-77): “each a blocking response with an acceptance rule;”
- `othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md` (107-108): “the child finishes that same step with support. A hint is not a we-do, and asking a fresh question is not a we-do.”
- `othello-course-renderer-draft/repo/docs/pedagogy/lesson-architecture.md` (60-61): “says the we-do starts the work and hands the child the rest of the SAME step to finish”
- `othello-course-renderer-draft/repo/docs/pedagogy/lesson-architecture.md` (63-65): “So the we-do here is a started sentence with the evidence slot filled and one gap left, in the procedure's own frame, not a fresh multiple-choice question with a hint bolted to its stem.”
- `othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md` (117-118): “Enforced for plans by `scripts/validate-lesson-plans.mjs` (exactly one procedure step belongs to the child). Not checked in the authored lesson.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/README.md` (56): “I-do/We-do/You-do differ in support, not in what thinking counts. Strip the labels and verify the same process remains.”
- `grade3-reading/curriculum-gen/checks/check-cross-stage.mjs` (42-44): “"Add what I know" is modelled, "Add what we know" is done together, "Add what you know" is done alone. That is the same step name, correctly authored.”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-main-checkout-jul-work.patch` (20658): “| **Gradual release misapplied** | I-do revealed the answer (not the thinking); we-do was a hint; you-do switched skills | strip labels from a sampled dose: do the three artifacts teach ONE process at decreasing support? |”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “strip the labels; if one ordered process cannot be recovered, the release is not genuine.”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/procedures/infer.md` (74-75): “Support is removed, never merely repeated: what the guide did with named clues, the child does by finding clues on their own.”
- `g9/library/text/L36b8ba.txt` (321): “The model was one quote, two words, five stem-built sentences. The independent practice is three quotes, conversational, with no stems and no sentence count. Nothing a child learned on the modeled screen transfers to this one.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-4/feedback-on-iteration-4/feedback-0806-pedagogy.md` (289): “A gap-fill at step 4 makes the you-do less demanding than the we-do's step 4, which is already a gap-fill — that inverts the release gradient (D1.15)”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/README.md` (29-30): “if you stripped the I-do / we-do / you-do labels, the three steps would be indistinguishable.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-15.md` (48): “so the child literally reads "Step 2: Zoom in" above the clue-tap they were taught as Step 3, and "Step 3: Read it closely" above the write task they were taught as Step 4.”
- `grade3-reading/artifacts/Peter-Pan-L4-review-response-2026-08-25.pdf` (p.4 (pdftotext lines 187-189)): “the skill introduction folds 'find the clues' and 'pick the best one' into a single Step 2, and both practice pages then split that across two panels, each labelled Step 2.”
- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L5-2026-09-05.md` (239-242): “This is a softer instantiation of Step 3 than either the modelled version (p14, testing 9 candidate trait words against the clues) or the independent version (p17, typed trait-word hunt against an accept-list).”
- `grade3-reading/.claude/skills/one-perfect-lesson/SKILL.md` (54): “identical step names across I/We/You-do”

Published: [Shanahan, T., et al. (2010). Improving reading comprehension in kindergarten through 3rd grade (NCEE 2010-4038). IES practice guide.](https://ies.ed.gov/ncee/wwc/practiceguide/14) · [Gurlitt & Renkl 2008](https://doi.org/10.1111/j.1365-2729.2008.00277.x)

Against: One lesson ships a gap-fill on its independent step by default, a known inversion accepted on instruction after it was argued (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md`, lines 340-345). The standard also lets the surface format change between stages only while the operation stays demonstrably the same (`grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd`, line 317). These are one project's rulings and design standard, not a measured effect on learning, and the modelling split has one exception, where composing a summary is itself the child's work. A later ruling accepted keeping the same question from the model to the guided step, against a claim that each stage needs a different question, with only the independent step moving to a fresh one: "The I-do→we-do handoff keeping the same question is the house release pattern; the" (`grade3-reading/artifacts/g5-course/G3-U1-L4-RESIDUAL-ADJUDICATION-2026-08-21.md`, line 24). The lint checks only the declared structure; whether a model's trace is a real think-aloud rather than an answer reveal is a judged check, advisory until it is calibrated (`grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md`, lines 21-23). the Grade 9 design specification lets confident students skip ahead: a quick check at the start of guided practice lets them move straight on (`grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd`, line 326). Only the shape is checked in code: the reading project's semantic lints stayed advisory after a judge trial ended NO-GO, so whether a think-aloud shows real thinking is not checked by machine. In that case the unmodelled task was objective, had a three-try ladder and revealed its answer at the floor, which the register counts as mitigation (`GAPS-2026-09-11.md`, lines 34-35); and the value analysis says none of it is evidence from a child (`L6-VALUE.md`, lines 3-5). The lesson designs had no guided stage of their own: "design docs go straight from Modelling Moment to Independent Task — they contain no we-do." The rebuilt lesson added one, and the spec keeps one modelled move for good: "This modelling never fades." The study compared less and more experienced learners, not the same learners over time.

<sub>criterion · practice, sequence, hints · universal · from g3, research · measured · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### One skill per lesson

Teach at most one well-defined new skill or named procedure per lesson, remove anything that doesn't serve it, and let its review steps use only skills already taught.

A pedagogy framework's first attribute of a good lesson is a single objective, and its path to mastery focuses each lesson 'on a single, well-defined skill' (`icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md`). Its cognitive-load rule removes the rest: lessons 'eliminate unnecessary complexity, visuals, and multitasking'. It is an adopted rule, with no measurement in the project.

Quoted:

- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (208): “Each lesson targets one skill or concept only. Students should know exactly what they are learning and why it matters.”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (91): “Each focuses on a single, well-defined skill.”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (223): “Lessons eliminate unnecessary complexity, visuals, and multitasking. Students focus on one process at a time.”
- `grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd` (25): “4. **Design for cognitive load limits.** Keep granularity tight, reduce noise, avoid bundling multiple new skills in one lesson.”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md` (17): “| L6 | one new operation per dose | every non-review atom carries exactly the lesson's one `operation_id`. Catches the round-2 skill-switching you-do (together with L1). |”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/lesson-schema.md` (72): “(an undeclared new operation cannot be smuggled in as phase:"review").”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/lesson-schema.md` (73-74): “Spec is silent on cross-unit review identity - recorded as an open question.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - The Living World - Complete KB.xlsx` (sheet 'Overview', cell B35): “FIND fits the fact-based texts (Plants, Mammals, Invertebrates, Microorganisms). The comparison texts (Feathers and Scales, Life in Water) use CONNECT - compare two groups, then draw the deeper link. The Animal Kingdom uses SORT (classify by shared features); the persuasion texts (Rainforests, Whose World Is It) need WEIGH / fact-vs-opinion.”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (12): “The steps are printed verbatim on the skill intro, the model, the guided try, the independent write, and the wrap recap — the rail never changes mid-lesson.”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (181): “An advance organizer for a procedure: the child meets the rail once, cold, before watching it run — so the model that follows is recognition, not first contact.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT1-VERTICAL-SLICE.md inside it) (1): “Demonstrate one complete APUSH unit contract before scaling: exact CED knowledge, one explicit historical operation per lesson, verified source provenance, AP-format evidence, scoring keys, and correction routes.”

Against: The project's own page on direct instruction records a criticism of the approach: '- May not fully encourage critical thinking or open-ended exploration' (`icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/direct-instruction.md`, line 63). Review across units is unsettled: the lint's lesson contract records cross-unit review identity as an open question (`grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/lesson-schema.md`, lines 73-74).

<sub>criterion · alignment, demand · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### One understanding per unit, linked by ideas

Give each unit one explicit primary understanding with its likely misconceptions, and link units by the ideas they share rather than by shared words or names.

The course-plan quality standard asks whether a sequence builds and reuses knowledge deliberately; it accepts one that names its primary understanding, what each part adds and a later activity that needs that knowledge, and lists links based only on shared words among its failure signals (`ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd`, Q014). Its obligations include giving every unit one primary understanding and using conceptual rather than surface cross-unit links. The Grade 3 reading criteria require cross-unit links stated as the big idea, not as surface facts such as matching names (`ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D10-delivery-ux-accessibility.md`). Done this way, the build-up of knowledge across units can be seen.

Quoted:

- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (237): “J16-CUR-003: Give every unit one primary understanding.”
- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (237): “J16-CUR-004: Use conceptual rather than surface cross-unit links.”
- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (232): “Each sequence names its primary understanding, what each part adds, and a later activity that requires genuine recruitment of that knowledge.”
- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (233): “Topic list; links based only on shared words; orphan lessons; final recall of disconnected facts.”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D10-delivery-ux-accessibility.md` (22): “Cross-unit links are stated as the big idea, not as surface facts (not "matching gods' names")”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (91-92): “add unit key understandings, conceptual cross-unit links, and misconception sets;”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (281): “knowledge sequencing is not observable”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/curriculum-agent.md` (41): “Unit ledger showing key understanding, misconceptions, fiction/nonfiction role, and cross-unit use.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (228): “"you met this word before" is a stronger move than showing it as one node among six.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/RESPONSE-MATRIX.md inside it) (34): “every cross-unit link is recast as a big-idea statement”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (190-191): “A theme is valuable when it carries a mechanism across periods, not when it simply appears in metadata.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/COURSE-PLAN.md inside it) (88): “Does each unit have a coherent explanatory center rather than a list of topics?”

Against: none found

<sub>criterion · sequence, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Open a cold domain with an ungated build

When learners arrive with no usable background in a unit's domain, make its first lesson an ungated knowledge build, say so, and start comprehension gates in the next lesson. Three breadth units in one course, on space, ancient Rome and the United States, each opened with a gate-free build.

Archived prompts for a Grade 3 reading course mark three breadth units as pre-teach-heavy, because a Grade 3 reader arrives with no usable astronomy, ancient-history or U.S. geography and civics base (`incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts`, units 7, 8 and 9). In each, the first lesson is a gate-free knowledge build that lays the base before any comprehension gate, and gates start in the second lesson; the space unit's prompt says that without the build the second lesson's gate would sit on nothing, and tells the writer to state plainly in the lesson that the build is gate-free and that gates begin next lesson. The course's authoring preamble and a later Grade 6 contract keep the rule for a cold-domain opener: the on-ramp expands into a gate-free knowledge build, and the lesson says so.

Quoted:

- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u07.md` (16-18): “L1 is a **gate-free knowledge-build** that front-loads the Earth/sun/moon/star base and the frame's first two columns before any gate; comprehension gates start at L2.”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u07.md` (47-48): “A G3 has no usable astronomy, so without this build L2's "the planets orbit the sun" and its gate would sit on nothing.”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u07.md` (56): “plainly in the lesson that this build is gate-free and that gates begin next lesson.”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u08.md` (5-7): “so **L1 is a gate-free pre-teach build**: it lays time-depth and the Mediterranean map before any comprehension gate, and the gates start at L2.”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u09.md` (7-8): “U.S. geography/civics arrives **cold**, so L1 is a **gate-free pre-teach build** (gates start at L2).”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/README.md` (46-47): “(For a **pre-teach-build** lesson, this expands into the whole lesson — a gate-free knowledge build; say so.)”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/generation-contract.md inside it) (60-61): “(For a **pre-teach-build** lesson — a cold-domain opener — this expands into a gate-free knowledge build; say so.)”

Against: The prompts are archived and record no results for these lessons.

<sub>criterion · sequence, evidence-of-learning · domain · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Open a unit through its key concept

In a course's first lesson, call up prior knowledge through the unit's key concept, such as a word web hinting at last year's text, not straight retrieval from it. A Grade 9 first lesson that tried retrieval from a play studied in Grade 8 found it confusing and opened with a word web on the unit's key concept instead.

At a planning meeting on 1 October 2026, a draft first lesson for a Grade 9 unit was described: retrieval from a play the learners read the year before had come across as confusing, so the lesson put the unit's key concept, deceit, on screen for a word web, with a hint asking what words would describe a character from that earlier play, so that the unit's words link back to it (`g9/sources/meeting-notes/ELA - CNU + Academics - 2026_10_01 20_30 IST - Notes by Gemini.md`, line 272). The later video sheet hands over to that word web as the first lesson's retrieval (`g9/sources/Othello Unit Video_ Info Sheet for Devfactory.md`, line 48).

Quoted:

- `g9/sources/meeting-notes/ELA - CNU + Academics - 2026_10_01 20_30 IST - Notes by Gemini.md` (272): “I kind of played with the idea of putting McBTH retrieval because they will have done McBTH in grade eight but it was coming across quite confusing.”
- `g9/sources/meeting-notes/ELA - CNU + Academics - 2026_10_01 20_30 IST - Notes by Gemini.md` (272): “So what I've done because it's the first unit is put the word deceit up and I want them to create a word web around that word and then there's a hint there of like what kind of words would you use to describe Lady McBth.”
- `g9/sources/meeting-notes/ELA - CNU + Academics - 2026_10_01 20_30 IST - Notes by Gemini.md` (272): “it's trying to recognize that the words that we need around deceits are words that we've used for Lady McBth”
- `g9/sources/Othello Unit Video_ Info Sheet for Devfactory.md` (48): “Lesson 1 retrieval (word web: deceit) follows.”

Against: It is one lesson draft's choice, untested with learners.

<sub>criterion · sequence, practice · domain · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Open each part from what just happened

Open each part of a lesson, and each video, with a line that links it to what the learner has just done.

A lesson review found that a second video did not show how its characters related to the first, so a learner coming to it cold would not make the connection, and it wrote the rule out as always situating the learner by linking to what has just happened (`othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md`, lines 215-218). The course renderer adopted it for every part of a lesson and every video (lines 212-213). It is followed by convention; no check enforces it (line 223).

Quoted:

- `othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md` (212-213): “**Rule.** Open each part of a lesson, and each video, with a bridging line that connects it to what the child has just done.”
- `othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md` (216-217): “Imagine a student coming at this cold: they won't make the connection.”
- `othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md` (218): “**Rule: always situate the learner by linking to what has just happened.**”

Against: none found

<sub>criterion · sequence, wording · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Open on the question the text answers

Build a pre-reading opening around the question the text will answer: pose it early, give the knowledge the reading needs, and close on it to send students into the text. One opening named four pieces of knowledge the reading needs: the world, the people, the kind of story and the words to write about it.

The handover's eight-scene opening for a play ends by returning to the central transformation and leading into the first scene, and the narration handoff asks that the final question invite the learner into the reading. The recorded script sets the unit's job in its first scene, to trace how the hero gets from one state to the other, names four pieces of knowledge the reading needs (the world of the play, the people in it, the kind of story it is and the words to write about it), and closes by telling students to open the book. The film treatment's last scene returns to the opening question before the play's first scene.

Quoted:

- `g9/script/v04/Othello-Opening-Recording-Manifest.json` (30): “Your job, across this whole unit, is to trace how a man gets from one to the other. From A to B.”
- `g9/script/v04/Othello-Opening-Recording-Manifest.json` (40): “To see how, you need four pieces of knowledge: the world of the play, the people in it, the kind of story it is, and the words you will use to write about it. Knowledge first. Then the reading.”
- `g9/script/v04/Othello-Opening-Recording-Manifest.json` (100): “A man who loves his wife. A man who hates him. Five acts between them. Now you know the world. Open the book.”
- `g9/prototypes/app-narrated/AUDIO-HANDOFF.md` (7): “Start with place, then intimacy, then the tragic reversal. Let the final question invite the learner into the reading.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (131): “8. Begin with Iago. Return to the central transformation and lead into reading Act 1 Scene 1.”
- `g9/film/TREATMENT.md` (22): “Return to the opening question before Act 1, Scene 1.”

Against: How much of that knowledge belongs before the reading is disputed: in the film study, "Only 6 are needed before the play's first line: the setting and who is who, 35 seconds of narration." (othello-unit-video/research/FINDINGS.md, lines 87-88), while another 11 of its 26 points could go in at the line that first needs them.

<sub>criterion · sequence, alignment · universal · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Order a history unit toward its synthesis

Order a history unit as context, the minimum model, complications that defeat an over-simple account, source work, argument, and a synthesis that answers the unit's question. All 9 of the course's authored units open with a context lesson and close on a checkpoint, synthesis, argument or timed essay.

An AP history course's sequencing brief gives every unit one functional order: locate the period in inherited conditions, teach the minimum factual and chronological model needed, introduce differences that defeat an over-simple account, model and then release source analysis, require a claim with selected evidence, and answer the unit question. The final topic of each unit stays its synthesis destination and is never reduced to a vocabulary review, and units follow the order without identical lesson templates. All nine authored unit indexes open with a context lesson and close on a checkpoint, synthesis, argument or timed essay; the steps between cannot be read from lesson titles, and no outcome was measured.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/SEQUENCING-BRIEF.md inside it) (89): “Each unit follows the same functional order without forcing identical lesson templates:”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/SEQUENCING-BRIEF.md inside it) (91): “Locate the period in inherited conditions, geography, and prior-unit mechanisms.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/SEQUENCING-BRIEF.md inside it) (92): “Teach the minimum factual and chronological model needed to explain the unit.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/SEQUENCING-BRIEF.md inside it) (93-94): “Introduce regional, social, political, or interpretive differences that defeat an over-simple account.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/SEQUENCING-BRIEF.md inside it) (97): “Answer the unit question and reactivate at least one long-range revisit edge.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/SEQUENCING-BRIEF.md inside it) (99-100): “The final topic in every local unit is already a reasoning-oriented period synthesis. It remains the unit's synthesis destination; it is not reduced to a vocabulary review.”
- `grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/prompts/u02.md` (8): “U2·L1 — Contextualizing Colonial North America”
- `grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/prompts/u02.md` (62): “U2·L10 — Period 2 Comparison Synthesis”
- `grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/prompts/u06.md` (104): “U6·L17 — Period 6 Synthesis: Change, Continuity, and Unequal Power”

Against: none found

<sub>criterion · sequence, demand · domain · from ap · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Order a lesson

Order a lesson: what students already know, the source, a worked example, guided tries, their own explanation, a check, and a later transfer.

The reading project's lesson flow prepares knowledge, meets the text, models the thinking, then gives guided practice
of the same process, the student's own explanation, an evidence check, and a delayed, varied transfer
(`grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd`), drawing on Rosenshine's
principles of instruction (https://www.aft.org/sites/default/files/periodicals/Rosenshine.pdf). Its engine's model act is
"I do, then you try" (`grade3-reading/engine/src/goal/lesson.js`). The lesson engine's palette runs in that order: what
students know and a film, the question and key words, reading checks, a worked model, writing and comparing, then
saying back and debate (`g9/transformer/README.md`, "Blocks").

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (40): “Reading Explorers v2 is a well-built, MAP-styled practice-and-assessment engine, not a comprehension curriculum, and on its current form it should not be approved as one.”
- `grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd` (56): “| `V0_skill_drill_practice_engine` | 0 | 0 | 12 |”
- `grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd` (57): “| `V1_question_bank_plus_thin_instruction` | 0 | 0 | 12 |”
- `grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd` (60): “| `V4_full_student_ready_candidate` | 12 | 0 | 0 |”
- `grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd` (70): “Strong questions do not become a course unless they sit inside this flow and the actual app proves students can experience it.”
- `grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd` (23): “not student outcome evidence”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (40): “If it is decided that this should be a MAP practice app, the recommendations below would be different.”
- `grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md` (35): “restates and tests the prior lesson's narrative state, always using a question that requires the”
- `grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md` (153): “Dimension criterion: a visible overarching purpose-question frames a multi-lesson text set from”
- `grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md` (495): “Reading-goal page comes AFTER vocabulary instruction in L5–L7 (vocab gates orientation)”
- `grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md` (432): “the design made deliberately (vocabulary first so the word is ready for the read)”
- `grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md` (170): “**Why it is a NOTE, not a finding:** The canopy deficiency is real at the arc-text level (four”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D6-practice-durable-mastery.md` (27): “A lesson may only assume knowledge earlier lessons taught AND the child proved fluent a day later (anchor E2-cleared)”
- `ti-courseplans-audit/docs/instruction-modes-spec.md` (62-64): “so an anchor first taught the same day never satisfies an `assumes` edge, and an anchor that is present-but-not-fluent is treated as not met.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (118): “- Build a real curriculum, not a library of components or a standards-aligned item bank.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (87): “No model of a strong response is shown.”
- `grade3-reading/knowledge_bot/knowledge/kb-0203-g9-ela-cnu-academics-meeting-2026-10-01.qmd` (86-87): “**three exemplar responses** at different levels.”
- `grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd` (64): “Replace independent tasks that reuse answer-bearing modeled evidence”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (61): “Children need a reason to read before they start”
- `downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx` (26 (textutil text)): “modelling every step except the final thinking move. It sounds like genuine thinking, not a lecture.”
- `downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx` (28 (textutil text)): “This is the first, most-supported turn at the skill before independent practice.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx` (sheet 'Overview', cell B35): “Each lesson opens by re-firing the previous part's key threshold, then threads it into the new one.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - The Living World - Complete KB.xlsx` (sheet 'Overview', cell B36): “Each lesson opens by recalling the prior part's knowledge, then threads it into the new threshold.”
- `grade3-reading/ti-courseplans/docs/course-creation-spovs.md` (90-91): “every dosed lesson still ships an explicit **gradual-release teaching step** (I-do worked example → we-do guided → you-do) with **corrective feedback** (why an answer is right/wrong).”
- `grade3-reading/ti-courseplans/docs/course-creation-spovs.md` (92): “A read-then-test loop with binary "good try" is not a course; it's an assessment engine.”
- `grade3-reading/ti-courseplans/docs/course-creation-spovs.md` (94-95): “The first G3 build read "no reading-strategy atoms" as license to omit teaching and shipped a MAP-practice engine mislabeled as a comprehension curriculum”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json` (398): “Do not ship an assessment layer ahead of the instruction and knowledge-compounding layer that prepares learners for it.”
- `grade3-reading/ti-courseplans/docs/course-creation-spovs.md` (114-115): “carve-out (MAPS-practice courses defer teaching to the spine course) stands, but the deferral must name a concrete spine plan — deferring to a course that doesn't exist failed review.”
- `grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md` (21): “1. **Set a purpose for reading BEFORE reading.**”
- `grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md` (25): “**Read the text BEFORE modeling.** The child reads (or hears) the whole text first;”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json` (317): “Complete a first encounter with the whole text before close modelling or analysis.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (299): “**C1 · Situate the learner: every section opens with a bridge to the one before.**”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (302-303): “the defect it catches is a section that is individually well-written and contextually cold”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/article/evaluation.txt` (616): “- **Guided → Independent sequence**: Is there progression from modeling to practice?”
- `icloud-work/incept/inceptbench/src/inceptbench/prompts/article/evaluation.txt` (521): “Both are valuable but serve different purposes. An article can have excellent worked examples but still lack independent practice.”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/direct-instruction.md` (48): “1. **Review and warm-up** - Recall prior knowledge”
- `icloud-work/inceptbench-main/website/Incept Pedagogy & Learning Science Overview.md` (87): “Students see exactly how to perform the skill before trying it themselves. This is followed by short, guided practice and then independent work where students apply what they’ve learned.”
- `grade3-reading/edullm-review-hub/course-packages/courses/apush/review/start-here.md` (13): “- seven progressively revealed phases: retrieval, teaching dose, model, guided response, independent response, feedback and different-evidence retry, and checkpoint;”
- `grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd` (67): “Prepare knowledge -> encounter text -> model thinking -> guided same-process practice -> student articulation -> evidence check -> delayed/varied transfer”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (62): “Students need to read the text first”
- `grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md` (28): “All 14 article stimuli rebuilt: Get ready > The text > Watch me think > Your turn > Say it with evidence > Our river map”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md` (26): “an independent inference item there would break the gradual-release order”
- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md` (225): “- **W-9. WORTH-FIXING — gradual release runs backwards, only here.** p14's chart”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md` (59): “Do not model analysis before the learner encounters the text.”
- `grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd` (493): “"Explicit instruction provides a clear explanation of the criterion task, encourages students to pay attention, activates prior knowledge, breaks the task into small steps, provides sufficient practice at every step"”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (77): “camouflage lesson modeled BEFORE the child read the text and set no reading purpose”
- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (643): “J16-LES-002: Provide a complete first encounter before close analysis.”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (12): “and then runs that identical four-step rail four times at decreasing support”
- `grade3-reading/ti-courseplans/docs/academics-alignment-plan.md` (46-48): “→ one prerequisite retrieval prompt. Never lead with vocabulary or an unrelated hook.”
- `g9/transformer/src/mechanics/word-web.js` (1-2): “Word web: the big idea that runs through the text, as one word at the centre of a web the reader builds from memory; … then the lesson's key words for it land face down, and each is said before it is turned.”
- `g9/transformer/src/mechanics/word-web.js` (94): “Some of these words you brought with you, and some are new. The new ones are this lesson's key words for ${item.centre}.”
- `g9/transformer/src/glue/animated.js` (108): “Before we read, show me what you already know. Build me a web for this one word.”
- `g9/transformer/src/mechanics/index.js` (24): “wordWeb, filmCheck, videoEssay, learningQuestion, keyWords,”
- `g9/transformer/README.md` (114): “Key words are not seeded from the word web's words.”
- `g9/transformer/src/mechanics/worked-model.js` (1): “the guide's "I do", before the student writes.”
- `g9/transformer/src/glue/animated.js` (193): “debate (the Grade 9 close: mimicry, then evaluation), then the learning question again”
- `g9/transformer/v02/QA.md` (116-117): “The palette runs in lesson order: WW FM LQ KW | GL QC OC EH WF DL | WM CER CA | SB DB.”
- `g9/transformer/test/threejs-render.test.mjs` (182): “the worked model is the model; CER is the student's paragraph”
- `g9/transformer/src/mechanics/index.js` (22): “// the palette in the order a lesson runs: openers, the reading, practice, closers”
- `g9/sources/Othello Unit Video_ Info Sheet for Devfactory.md` (77): “House order: unit video → retrieval → learning question → new knowledge → guided practice → independent practice → closing questions.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (87): “Lesson 1 includes retrieval, a learning question, new knowledge, five reading sections, guided modelling, independent writing, and closing Mimicry, Application, and Evaluation.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (89-91): “A lesson exists only when it teaches a bounded idea, models a move, hands that move to the learner, and gathers evidence of independent use.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/SEQUENCING-BRIEF.md inside it) (129-130): “**F2: Item-bank course.** Detection: a lesson begins with independent questions before a content or reasoning model. Recovery: author the model and guided handoff before retaining the check.”

Published: [Rosenshine 2012](https://www.aft.org/sites/default/files/periodicals/Rosenshine.pdf)

Against: this is design and research, not a result of
ours; the reading project calls its own evidence design stress, not proof of outcomes. A later run found: a practice-only course may leave its teaching to a named spine course, though deferring to a course that doesn't exist failed review (`grade3-reading/ti-courseplans/docs/course-creation-spovs.md`).

<sub>criterion · sequence · universal · from g3, research · external-research · held · found in [2026-10-12-2-round-1](../research/2026-10-12-2-round-1/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Pair knowledge with a reasoning operation

Plan content knowledge and the named reasoning operations applied to it as two progressions that lessons join: content alone is exposure, and a content-free skill is a generic worksheet.

A Grade 5 reading course's BrainLift holds as a core position that comprehension needs knowledge and an analytical toolkit, and names its falsifier: if either layer can be removed without changing instruction or integration, the two-layer model is decorative. The same document lists a skills-only reading spine among the approaches it dropped, because generic operations without knowledge do not support text-specific comprehension, and keeps content knowledge and analytical operations as two visible structures, modelled separately and then coordinated in named integration lessons. It adds the other half to teaching strategies inside the content they serve: time spent building knowledge still needs an operation. The position is adopted; no test of its falsifier is recorded.

Quoted:

- `incept-package-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “Content without a reasoning operation is exposure; an operation without content becomes a generic worksheet.”
- `incept-package-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “Generic operations without knowledge do not support text-specific comprehension.”
- `incept-package-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “if either layer can be removed without changing instruction or integration, the two-layer model is decorative.”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (125): “### G5-POL-ARC-002: Represent Grade 5 comprehension with a content-knowledge layer and a distinct analytical-toolkit layer, joined by integrative application relations.”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (128): “- **Rationale:** English analytical operations have their own progression and are applied to content rather than replacing it.”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (133): “graph declares content_knowledge and analytical_toolkit node layers plus at least one typed cross-layer application relation”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/docs/BRAINLIFT.md inside it) (214-217): “2. **Comprehension needs knowledge and an analytical toolkit.** Content without a reasoning operation is exposure; an operation without content becomes a generic worksheet. **Falsifier:** if either layer can be removed without changing instruction or integration, the two-layer model is decorative.”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/docs/BRAINLIFT.md inside it) (242): “| Learning architecture | Content knowledge plus analytical toolkit plus named integration | Keeps topic knowledge, reading operations, and coordination separately inspectable. |”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (95-97): “Sourcing, comparison, causation, contextualization, and argumentation are not content-free verbs. A student cannot evaluate a source's purpose without knowing the historical situation and likely audience.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (97): “A student cannot explain causation by attaching the word "because" to an event list.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (101): “The plan therefore teaches a historical mechanism and a disciplinary move together.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/SEQUENCING-BRIEF.md inside it) (112-113): “Source analysis is not a detachable generic skill. Every model names what the source contributes to a specific historical claim and how authorship, audience, purpose, or situation affects that use.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (216-217): “Naming "purpose" earns no value if the student cannot explain why that purpose makes the source useful or limited for a specific claim.”

Against: It is a design rule with no learning measure, and the Grade 5 generation contract leaves its content domains and exact analytical progression as curriculum decisions without external approval (`grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz`, member `g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md`, line 135).

<sub>criterion · demand, alignment · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Practise facts and schemas differently

Practise a stable fact with brief, frequent retrieval that tapers off, and understanding that depends on a schema by retrieval, feedback, then use in a new task.

The practice BrainLift in the reading project's course plans proposes two routes to durable mastery (`grade3-reading/ti-courseplans/feedback/feedback1/Practice BrainLift.md`). Fixed retrieval, for knowledge with a stable target response, is frequent and brief early on, then tapered, with errors met by targeted firming rather than full reteaching; transformation retrieval, for knowledge that has to travel across a family of tasks, runs retrieval, then feedback, then an update task such as an explanation, comparison, boundary case or application in a new context. The project's practice spec builds its studio for schema-dependent knowledge on that sequence (`grade3-reading/ti-courseplans/docs/practice-layer-spec.md`). The new task can be explaining, comparing or placing what was retrieved.

Quoted:

- `grade3-reading/ti-courseplans/feedback/feedback1/Practice BrainLift.md` (19): “Practice is frequent and brief early on, then tapered, with occasional maintenance checks. Errors are met with targeted firming, not full reteaching.”
- `grade3-reading/ti-courseplans/feedback/feedback1/Practice BrainLift.md` (20): “The sequence is: retrieval → feedback → update task (explanation, comparison, discrimination, boundary case, application in a new context).”
- `ti-courseplans-audit/docs/instruction-quality-standard.md` (66-69): “Classify KCs into **Fixed Retrieval** (stable canonical response → frequent brief early practice, tapered, targeted firming on error) vs **Transformation Retrieval** (schema-dependent → retrieval → feedback → update task that widens deployment conditions).”
- `ti-courseplans-audit/docs/instruction-quality-standard.md` (62-64): “a single binary mastery gate collapses acquisition mastery (a gate) with durable mastery (a rolling state) — and over-reteaches or under-practises”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (44-46): “retrieval → feedback → **update task** (explain, compare, or place on the Theme Ledger) over taught-spine content with varied surface texts. Fixed retrieval is reserved for the anchor class; comprehension KCs never run as bare recall.”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D6-practice-durable-mastery.md` (22): “Transformation/comprehension KCs run retrieval → feedback → an UPDATE task; they never run as bare recall”

Against: none found

<sub>criterion · practice, feedback · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Practise the formats before they count

Let learners practise the formats and interactions of the test that counts before it counts, because meeting an unfamiliar interface on the scored test adds noise to the score. One reading course runs a 43-item practice lane for format exposure that never feeds a mastery gate.

A reading assessment's position is that learners who practised only single-select items met multi-select and two-part evidence items for the first time on the scored official test, and that interface novelty is construct-irrelevant variance, citing the testing standards (`grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md`). A Grade 8 reading course runs a 43-item practice lane in three formats for format exposure, never routed through a mastery gate (`incept-package-hub/course-packages/courses/g8-reading/review/evidence/case-for-review.md`).

Quoted:

- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md` (55): “Alpha students practice on 100% MCQ material; their first multi-select or two-part evidence item is on the scored official MAP. Interface novelty is construct-irrelevant variance (AERA/APA/NCME Standard 1.13).”
- `incept-package-hub/course-packages/courses/g8-reading/review/evidence/case-for-review.md` (48-49): “a **43-item non-gating practice lane** (multi_select, hot_text, match) for format exposure, never routed through a mastery gate”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md` (36): “| 11 | Format-familiarization benefit implied for all six formats | **Bounded** — one-line scope added: strongest for the 3 Reading-2–5-confirmed formats; the other 3 are low-harm additional practice |”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RED_TEAM_FINDINGS.md` (21): “if familiarity moves scores at all, it moves the official ones.”
- `grade3-reading/artifacts/g5_build_2026_07_02/mapproxy_clean.md` (179): “Interface novelty is construct-irrelevant variance (AERA/APA/NCME Standard 1.13).”
- `grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md` (47): “B is the only one to flag that live course is 100% MCQ while MAP is >30% tech-enhanced”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (321): “so a rise isn't format-practice inflation.”
- `grade3-reading/_archive/2026-08-13-consolidation/top-level-docs/HANDOFF_3_KEY_ISSUES.md` (25): “MAP-equiv forms hot-text-heavy vs real MAP's MCQ mix”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (59): “the line range goes from "5-8" to "5 through 8", which is how the released tests write it”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md` (55): “Interface novelty is construct-irrelevant variance (AERA/APA/NCME Standard 1.13).”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (301-302): “If all SAQs become sourced, students need repeated instruction in reading different source modalities under short-answer timing.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_CASE_FOR_APPROVAL.md` (183): “format familiarity is measurement hygiene, not test prep”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/MAP_PROXY_VALIDITY_CASE.md` (105): “One scope note on format familiarization: the benefit is strongest for the three formats confirmed in Reading 2–5 specifically (MCQ, multi-select, EBSR/composite); the other three are low-harm additional practice, not a claimed MAP-preparation benefit.”

Published: [AERA, APA & NCME 2014, Standards for Educational and Psychological Testing](https://www.testingstandards.net/open-access-files.html)

Against: The package's own audit later bounded the benefit: strongest for the three formats confirmed for the official reading test, low-harm extra practice for the other three (`grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md`). An adversarial review added that if familiarity moves scores at all, it moves the official ones, which matters when the practice doubles as a validation study (`grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RED_TEAM_FINDINGS.md`). Format practice can inflate an internal growth reading, so one course measures growth on a held-out instrument it never teaches to or gates on (`grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md`).

<sub>criterion · practice, format · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Previews that stress the key concepts

A preview given before new material helps when it stresses the key concepts, not only their structure. In two experiments, with 48 and 53 students, well-structured organisers raised far transfer from roughly 33% to 67%, yet structure on its own was not reliably better.

An intro-video BrainLift for a Grade 3 reading course reports Gurlitt, Dummel, Schuster and Nückles (2012): in two experiments, with 48 psychology and 53 mathematics students, well-structured advance organisers beat less-structured ones on the schemata learners formed, the posttest, and near and far transfer, with far transfer rising from roughly 33% to 67% (`downloads/BrainLift - What makes a good intro video.md`, line 456). A well-structured organiser on its own was not reliably better (p = .10 in the first experiment, and no far-transfer gain in the second); what carried it was the version that also emphasised the key concepts. The source names the study without a link; its DOI was found on Crossref.

Quoted:

- `downloads/BrainLift - What makes a good intro video.md` (456): “What carried it was the version that additionally emphasised the key concepts. Structure without emphasis was not enough.”
- `grade3-reading/artifacts/g9-prep-pack-2026-10-02/03-research/MANIFEST.md` (28): “Spec §3.3 cites Stone (1983) directly for the linked advance-organizer video: "modest but reliable gains, strongest for long-term retention."”
- `g9/library/text/L9b6d99.txt` (77): “They give modest but reliable gains, strongest for long-term retention (Stone, 1983).”

Published: [Gurlitt, Dummel, Schuster & Nückles 2012](https://doi.org/10.1007/s11251-011-9180-7)

Against: One study, with psychology and mathematics students rather than young readers.

<sub>criterion · sequence, media · universal · from g3, research · external-research · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Produce it, don't just pick it

Anything taught needs graded work where learners produce it, as picking, recognising, mentioning or echoing it never counts, and no earlier check may use a taught word as its answer. One taught word was checked only by two multiple-choice questions and never had to be produced.

An audit found two taught words that had been acquired but that no graded task ever required using. The reading project then ruled that every taught word needs a graded point where the child produces it in an evaluative sentence of their own, and that recognition in a multiple-choice question never counts, however many options it has. Its item rules say not to certify productive knowledge with recognition alone, and its lesson rulings judge a lesson by what students produce over what they click. Response counts must leave out one-word echoes.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (134-136): “Taught word never cashed in L6/L7 — merciless/triumphant were acquired but no graded surface required using them”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (138-139): “a cash point is graded usage, not mention — the child must produce the word themselves in an evaluative sentence”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (143-144): “MCQ recognition alone — however many options — never counts as a cash point”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (144): “never got one beyond two MCQs”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md` (64): “Do not certify productive or integrative knowledge with recognition alone.”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (38-39): “judge a lesson by *production* (say/write/type) over *selection* (click)”
- `grade3-reading/knowledge_bot/knowledge/kb-0160-multiple-choice-questions-evidence-base.qmd` (129): “MC practice tests showed a larger effect size (g = +0.70) than short-answer tests (g = +0.48)”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (183): “but 2–3 were trivial *say-backs* (repeat a word) and the real generative-comprehension production was ~2”
- `grade3-reading/ti-courseplans/feedback/feedback 4/WF - Brainlift Opportunities to - 260724-110911.md` (23): “A high number of responses per minute is not evidence of quality if the app reached that number by asking only recognition questions.”
- `grade3-reading/ti-courseplans/feedback/feedback 4/WF - Brainlift Opportunities to - 260724-110911.md` (30): “If a child never has to compose or explain an answer, the app cannot tell whether the child understood”
- `grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md` (212): “students learn from what they produce (saying, writing, typing) in multiple representations, not what they click.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (354): “For diagnostic assessment, the much-maligned MCQ is not a compromise — it is the optimal format.”
- `grade3-reading/ti-courseplans/feedback/feedback 4/WF - Brainlift Opportunities to - 260724-110911.md` (23): “Neither type is better than the other; each belongs to a different job.”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (135-136): “merciless/triumphant were acquired but no graded surface required using them”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (138): “a cash point is **graded usage, not mention**”
- `downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx` (9 (textutil text)): “Exactly one high-leverage word is taught — chosen to unlock this text and to feed the Phase 3 inference.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx` (12 (textutil text)): “Vocabulary word (taught): betrayal / betrayed — the feeling when someone you trusted lets you down or tricks you. (Not in the text; encapsulating; reserved for the Independent Task.)”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx` (336 (textutil text)): “Betrayal / betrayed never appears in the video, the vocab-to-story bridge, the pauses, or the cloze bank; it is surfaced only in the Independent Task (Step 3 blank C and Step 5 help), where the child uses it to cash the answer.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx` (124 (textutil text)): “The taught word is never blanked.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (107 (textutil text)): “The taught word determined is never blanked.”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (23): “*eerie* is deliberately absent from the passage | The child must produce the word to name a mood the writer never named”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx` (64 (textutil text)): “The Component 2 word (determined) is NOT clickable, even though it appears in the text: it is handled in the vocabulary slot and reserved as the Phase 3 payoff / magic word.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/INTEGRATION-LESSONS.md` (11): “New vocabulary meaning rubrics were ignored by the old say/type card”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/INTEGRATION-LESSONS.md` (11): “A successful pronunciation or copied spelling is not evidence of word meaning. Invoke the authored criterion and preserve typed access.”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/HUMAN-g3r-2026-07-27T08-38-36-019fa24b-fb42-7e61-a954-216db3ef77a4.md` (1097): “Exactly one high-leverage word is taught — chosen to unlock this text and to feed the Phase 3 inference. The child gets a student-friendly definition and one usage check (MCQ), then a plain statement bridging the word to the story. There is no speaking; understanding is checked by the MCQ.”
- `grade3-reading/_archive/2026-08-13-consolidation/council-human-handover-2026-08-13/04_HUMAN_CHECK_LESSONS.md` (38): “Vocabulary required meaningful oral/morphological use rather than passive definition display.”
- `grade3-reading/_archive/2026-08-13-consolidation/orientation-sweep-digest/kb-authorities.md` (4): “oral turn-taking vocabulary + meaningful morphology (not phonics)”
- `grade3-reading/course-renderer/docs/handover/closing-questions/design-mock-l1.html` (210): “Our turn is unmarked and never the test; the test is the hidden recall and the Part 2 recall.”
- `grade3-reading/curriculum-gen/audits/PETER-PAN-AUDIT-2026-08-24.md` (57): “There is no speaking; understanding is checked by the MCQ.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/FEEDBACK-RESPONSES.md` (92): “type the word — production tasks, not recognition tasks.”
- `grade3-reading/course-renderer/docs/pedagogy/example-lesson-components-2026-08-06.md` (22): “There is no speaking; understanding is checked by the MCQ.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (171): “Three core words, verbatim, tap in order. Taught word never blanked.”
- `g9/library/text/L8d5159.txt` (171): “Three core words, verbatim, tap in order. Taught word never blanked.”
- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L6-2026-09-05.md` (72-74): “L10 additionally gates **every vocab word** behind a `say_back_line` + `assessment.rubric` ("A parroted repeat of the card's definition does not count as their own words")”
- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L6-2026-09-05.md` (110-114): “This is graded usage, not mention: the child must produce the word themselves in an evaluative sentence about Hook's order to lock every prisoner below, immediately after quoting the verbatim evidence line — i.e., word + evidence + judgment fused in one required output, which is a real cash, not a drive-by reference.”
- `grade3-reading/.claude/skills/lesson-build/SKILL.md` (29-30): “one cash point for the taught word — name the page where the magic word is used, usually the retell criterion”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (155-156): “the row is never student-produced language, just a tap-to-reveal”
- `grade3-reading/.claude/skills/one-perfect-lesson/SKILL.md` (46): “comprehension lives in *generate*”

Against: A meta-analysis summarised in the reading project found multiple-choice practice tests had a larger effect than short-answer ones (g = +0.70 against g = +0.48), so picking can still be good practice; the rule is about what counts as evidence of learning. For diagnosis, the course's assessment brainlift calls multiple choice the optimal format, for its speed and its isolation of one piece of knowledge (`grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md`, SPOV 10), and the brainlift on opportunities to respond itself says neither response type is better, each belonging to a different job. The designs differ on whether the word should be one the text never uses: two lessons choose such a word, and a third holds back a word that appears in its text. A later run found: A lesson-component spec for the reading course teaches one high-leverage word with a student-friendly definition and checks it with one usage multiple-choice question and no speaking, so recognition is the only check on the taught word (`grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/HUMAN-g3r-2026-07-27T08-38-36-019fa24b-fb42-7e61-a954-216db3ef77a4.md`). A later run found counter-evidence (`grade3-reading/curriculum-gen/audits/PETER-PAN-AUDIT-2026-08-24.md`). A later run found counter-evidence (`grade3-reading/course-renderer/docs/pedagogy/example-lesson-components-2026-08-06.md`).

<sub>criterion · evidence-of-learning, format, alignment · universal · from g3, research · adopted-rule · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Put a text's parts together at the end

When one text runs across several lessons, give the last one a task where learners retell or connect the whole, since closing each part alone never asks for it. In the last of four lessons on one story, no rubric criterion across all 21 pages asked for the four parts together.

An audit of the last lesson in a four-lesson reading of one story found that no earlier lesson applied the story pattern to all four parts, each lesson only retrieving from the one before, so the last lesson was the only place the whole could come together (`grade3-reading/artifacts/arc-audit/PEDAGOGY-L7-2026-09-05.md`, lines 170-173). Its retell asked for the last part only, and no criterion in any rubric across all 21 pages asked for the four parts together (lines 175-176 and 257). The audit put the fix at one rubric criterion, a retell extended to the whole story (lines 184-187), and a re-verification confirmed the gap as real, a value-add beyond the design rather than a breach of it, and left the change for a ruling (`grade3-reading/artifacts/arc-audit/REGISTER-PEDAGOGY-2026-09-05.md`, line 19).

Quoted:

- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L7-2026-09-05.md` (170-173): “No prior lesson in the arc explicitly synthesizes the full "we-meet / they-want / but / so / then" pattern against all four parts (only p0 of each lesson retrieves from the prior one). L7 is the only lesson that *could* deliver this whole-arc synthesis.”
- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L7-2026-09-05.md` (175-176): “the child never produces a whole-arc synthesis. The retell (p19) asks for Part 4, not all four parts.”
- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L7-2026-09-05.md` (257): “no criterion in any rubric across all 21 pages asks for Parts 1-4 synthesis”
- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L7-2026-09-05.md` (186-187): “would cost one rubric criterion change and deliver the full arc-closure payoff”
- `grade3-reading/artifacts/arc-audit/REGISTER-PEDAGOGY-2026-09-05.md` (19): “REAL, value-add not doc-violation.”

Against: The design never asked for a whole-text task, only that the pattern's labels show on screen as a reminder, and a film covers the whole: "The video carries the arc framing." (`grade3-reading/artifacts/arc-audit/PEDAGOGY-L7-2026-09-05.md`, lines 180-183). The audit rated the gap minor, and nothing measured whether learners join the parts without such a task.

<sub>criterion · sequence, demand, evidence-of-learning · universal · from g3 · measured · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Question kinds by where the answer lives

Sort reading questions by where the answer lives, in one sentence, across several or with the reader's knowledge, and teach them in that order, each mastered before the next. One design unlocks the 3 kinds strictly in that order and keeps kinds already mastered in the practice mix.

An IES video on asking and answering questions, quoted in a reading course's review standard, sorts text-dependent questions into three kinds: right there, answered in one sentence; think and search, put together across several sentences; and author and me, which joins the text to the reader's own experience or learning and is also called inferential (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/qar-evidence-source-taxonomy.md`). It recommends starting with right-there questions, moving on only once students show mastery of each kind, and having students find and highlight the supporting sentences. The standard's design tags every item with its kind, unlocks the kinds in that order while mastered kinds stay in the mix, and accepts no answer without the highlighted evidence. It is classroom guidance from a video, not a trial.

Quoted:

- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/qar-evidence-source-taxonomy.md` (21): “When we teach students to answer questions, we should start with right there questions, then move to think and search questions, and finally author and me questions. Students should demonstrate mastery of each question type before they move to the next.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/qar-evidence-source-taxonomy.md` (15): “The simplest questions are right there questions — a type of text-dependent question for which the answer is stated in one sentence of the text.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/qar-evidence-source-taxonomy.md` (17): “This type of question is still text-dependent, but to answer it, a reader must put multiple pieces of information together across several sentences.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/qar-evidence-source-taxonomy.md` (19): “They require the reader to connect information in the text they have just read to their own prior experience or learning. Author and me questions are also known as inferential questions.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/qar-evidence-source-taxonomy.md` (23): “Find these sentences from the text. And when you find them, I want you to highlight them.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/qar-evidence-source-taxonomy.md` (26): “The mastery graph unlocks them strictly in that order”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/qar-evidence-source-taxonomy.md` (26): “but previously-mastered types keep appearing in the mix (spaced practice) rather than disappearing”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/qar-evidence-source-taxonomy.md` (26): “the answer cannot be submitted with an empty citation”

Published: [Ask and Answer Questions (PRISMS, question-answer relationships), IES video](https://www.youtube.com/watch?v=BXmrpFK_d08)

Against: none found

<sub>criterion · sequence, demand · universal · from g3, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Raise one demand at a time

Raise one demand at a time: bring in a harder text only once its reading move is known, and withdraw supports singly, so a failed check points to one change. One course plans its texts to climb from 740 to 940 on a text-difficulty scale, within units as well as across them, so a harder text never arrives with a new move.

The Grade 4 course rationale has text difficulty climb inside a unit as well as across the course, so the harder text arrives after the reading move is known and never at the same time (`othello-course-renderer-draft/repo/content/course-rationale.json`, line 17); its climb, 740L to 940L, is a set of authoring targets rather than measurements (line 13). A research brief applied the rule when sizing a lesson's second passage, since doubling it would add reading load at the same time as a new reading move (`othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md`, lines 446-448). A Grade 3 writing scaffold keeps its two fades in step, so a child is never asked to find evidence unaided and organise the essay unaided in the same jump (`othello-course-renderer-draft/repo/docs/extras/alpharead-writing-scaffold-overview.md`, line 31).

Quoted:

- `othello-course-renderer-draft/repo/content/course-rationale.json` (17): “Lexile climbs inside a unit as well as across the course, so the harder text arrives after the move is already known and never at the same time as it.”
- `othello-course-renderer-draft/repo/content/course-rationale.json` (13): “740L to 940L, authoring targets rather than measurements”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l3-circe-and-the-lotus-eaters.md` (446-448): “Doubling the second narrative does not add alignment, it adds reading load at the same time as a new reading move, which is what the graph's own reading order tries to avoid.”
- `othello-course-renderer-draft/repo/docs/extras/alpharead-writing-scaffold-overview.md` (31): “The two fades stay in step: a child is never asked to self-source evidence *and* self-organise the essay in the same jump.”
- `grade3-reading/course-renderer/content/course-rationale.json` (17): “Lexile climbs inside a unit as well as across the course, so the harder text arrives after the move is already known and never at the same time as it.”
- `grade3-reading/course-renderer/content/course-rationale.json` (13): “740L to 940L, authoring targets rather than measurements”
- `grade3-reading/course-renderer/content/course-rationale.json` (6): “Draft for review”
- `grade3-reading/course-renderer/content/course-rationale.json` (21): “It is what this repo now follows”
- `grade3-reading/course-renderer/docs/extras/alpharead-writing-scaffold-overview.md` (31): “The two fades stay in step: a child is never asked to self-source evidence *and* self-organise the essay in the same jump.”
- `grade3-reading/course-renderer/docs/extras/alpharead-writing-scaffold-overview.md` (29): “how much of the frame is *pre-filled* shrinks — full echo → clause starter → bare stem → blank box (entry 5) — and how much help the child gets *finding the evidence* shrinks — passage shown → region only → nothing (entry 2).”
- `grade3-reading/course-renderer/docs/extras/alpharead-writing-scaffold-overview.md` (12): “Not our course.”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md` (134): “Fading nine dimensions (illustration → cast → tone → audio → schema-load → length → syntax → inference → topic-predictability) simultaneously means that when a Band-B student fails the sequence gate, you cannot tell *which* faded support caused it.”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md` (134): “as an *automated* per-student adaptation it is too many confounded knobs for a population this young and a signal this noisy.”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-2-pedagogy.md` (134): “picture support is a legitimate comprehension scaffold at this age (dual-coding; the picture-walk tradition), and fading it as if it were decoration may remove a real comprehension support, not just training wheels.”
- `grade3-reading/ti-courseplans/courses/g2-reading/analysis/skeleton-v2.md` (133-134): “the **9-dimension fade dial** (illustration → cast → tone → audio → schema-load → length → syntax → inference → topic-predictability)”
- `grade3-reading/ti-courseplans/handoff/timeback-course-explorer/brainlift/amalgamation-v2.md` (289): “Engagement scaffold must fade to cold plain text or it teaches dependency”

Against: It is a design rule, not a measured result, and the source is another course's design ("Not our course.", `grade3-reading/course-renderer/docs/extras/alpharead-writing-scaffold-overview.md`, line 12). The plan under review used the nine-dimension fade dial (`grade3-reading/ti-courseplans/courses/g2-reading/analysis/skeleton-v2.md`, lines 133-134), and a grade-3 synthesis dropped a permanent picture wrapper because an engagement scaffold "must fade to cold plain text or it teaches dependency" (`grade3-reading/ti-courseplans/handoff/timeback-course-explorer/brainlift/amalgamation-v2.md`, line 289).

<sub>criterion · sequence, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Raise the level by handing over thinking

Raise a course's level by handing students more of the thinking, such as framing questions, choosing evidence, handling ambiguity and repairing their own reasoning, not by harder vocabulary alone.

Review found the first conventional Grade 9 plan basic beside the Grade 3 work (`g9/transcript/chat-transcript.redacted.txt`, lines 2534 and 2555), and inspection confirmed that the Grade 3 lessons already teach children to weigh competing clues, justify the strongest evidence, combine quotation with knowledge, predict consequences and transfer a rule from one story to another (line 2620). The plan was rebuilt around increasingly independent intellectual work, and that resource was endorsed (lines 2622 and 2705). The later design brief defines advanced learning as greater responsibility for framing questions, choosing evidence and handling ambiguity, adds that more difficult vocabulary alone does not raise the level of thinking, and has students formulate questions, distinguish plausible explanations, test counterfactuals, respond to counterevidence and repair their own reasoning (lines 2884 and 3085).

Quoted:

- `g9/transcript/chat-transcript.redacted.txt` (3085): “Advanced learning means greater responsibility for framing questions, choosing evidence and handling ambiguity. More difficult vocabulary alone does not raise the level of thinking.”
- `g9/transcript/chat-transcript.redacted.txt` (2884): “Students formulate questions, distinguish plausible explanations, test counterfactuals, respond to counterevidence and repair their own reasoning.”
- `g9/transcript/chat-transcript.redacted.txt` (2620): “they already teach children to weigh competing clues, justify the strongest evidence, combine quotation with knowledge, predict consequences, and transfer a rule”
- `g9/transcript/chat-transcript.redacted.txt` (2555): “I focused too much on a conventional Grade 9 course.”

Against: It has not been tested with students.

<sub>criterion · demand, sequence · universal · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Recall aloud before the options appear

In a retrieval warm-up, have learners answer aloud before any options appear, and show the options only afterwards as a check, so they recall rather than recognise.

A review of a Grade 3 reading build welcomed starting with retrieval from the last lesson but said it would be better done with an oral response than a multiple-choice question; the redesign brief records the defect, that the warm-up was a choice question, so the child recognised instead of retrieving. The rebuilt warm-up asks its question alone and the child answers out loud, and only on the next screen do the options appear, under a heading telling the child to check, with a written response for each choice. The build's principle is that the child speaks before they choose.

Quoted:

- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v3/UX-REDESIGN-BRIEF.md` (59): “The retrieval warm-up was an MCQ, so the child recognised instead”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/FEEDBACK-RESPONSES.md` (266): “Only on the next screen do the options appear”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/BRAINLIFT.md` (98-99): “the retrieval warm-up asks its question **alone** with a speak gate and only then shows options”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v3/UX-REDESIGN-BRIEF.md` (56): “The child speaks before they choose”

Against: none found

<sub>criterion · practice, format, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Reread in passes that go deeper

Have a text read more than once, in parts, each pass with its own deeper purpose, rather than read once and quizzed. Across 18 lessons of one course, each text was read once with every question after it and 0 stops inside it.

An audit of the third iteration of one Grade 3 reading course found each passage read once as a single block with every question after it, with 0 stops inside the text across 18 lessons (`ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md`). The course's criteria ask for the passage chunked and reread with each pass going deeper, from facts to inference to the author's purpose, each pass opened with a one-sentence purpose (`ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D3-reading-architecture.md`). The same criteria build knowledge through a set of related texts, not by rereading the same text start to finish every day. Set the purpose before reading, aim each pass at the parts that serve it, and don't reread the whole text by habit.

Quoted:

- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (204): “G3 iter-3: the passage is one block read ONCE, all questions after it (0 mid-passage stops across 18 lessons)”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D3-reading-architecture.md` (12): “The passage is chunked and reread with each pass going deeper (Read 1 facts → Read 2 inference → Read 3 deeper meaning / author's purpose); not read-once-then-quiz”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D3-reading-architecture.md` (20): “Repeated reads escalate by named tier — on-the-surface → below-the-surface → deeper-dive (author's purpose) → an affective 'connect-to-your-life' tier — each pass opened with a one-sentence escalating purpose”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D3-reading-architecture.md` (15): “not by rereading the same text start-to-finish every day”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (61): “The camouflage lesson has no pre-read to activate or build knowledge and no stated purpose for reading.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (61): “Children need a reason to read before they start”
- `grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd` (93): “4. Rereads point to a text subset for a declared knowledge purpose rather than replaying a whole text by habit.”
- `grade3-reading/artifacts/edullm-agent-entrypoint-g3-practical-test-2026-08-06/REPORT.qmd` (39): “- 48/48 lessons use a single explicit read pass.”
- `grade3-reading/artifacts/wiki-research/redteam-standard.md` (137): “5. How the text is READ is instruction, not delivery”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/g3-reading-standard.md` (95): “the passage is read more than once, with questions that deepen across readings”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/g3-reading-standard.md` (95): “not read-once-then-quiz”
- `g9/sources/Act 1 reading texts/Act 1/4. 1.3 - Desdemona - Text.docx` (14): “You have read this scene before, for Othello and Iago. This time, you will read it for Desdemona.”
- `g9/sources/3-D-Shakespeare-Othello-1.1.pdf` (94-95): “When this third round is done, ask again what their comprehension level was. The numbers will go up significantly.”
- `othello-archive/sources/act1/3. 1.3 - Othello & Iago - Text.txt` (5): “The play text is the same in Lesson 3 and Lesson 4; only the Archivist narration changes.”

Against: The test shows that rereads were missing, not that adding them raised scores; nothing here measured their effect.

<sub>criterion · sequence, stimulus · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Respond to a gap by its kind

Respond to an unmet prerequisite by its kind: reteach a conceptual gap, give targeted practice for a fluency gap, and give a brief orientation for missing context.

Sequencing briefs for a Grade 3 and a Grade 6 reading course set the same default response to an unmet prerequisite: a conceptual gap is retaught, a fluency gap gets targeted practice, and a gap in context gets a brief orientation at the lesson's on-ramp. Both courses gate lightly, so even a genuine prerequisite is met by reteaching or scaffolding rather than by locking the learner out. It is a declared default; neither brief reports how learners fared under it.

Quoted:

- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/SEQUENCING-BRIEF.md inside it) (89-90): “**Default response per unmet prereq:** conceptual gap → reteach (M7 correction); fluency gap → targeted practice; contextual gap → brief M1 orientation.”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/sequencing-brief.md inside it) (137-138): “**Default response per unmet prereq:** conceptual gap → reteach; fluency gap → targeted practice; contextual gap → brief on-ramp orientation.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/SEQUENCING-BRIEF.md inside it) (88): “Even these gate *lightly* — reteach/scaffold, not lock-out.”

Against: It is a declared default: neither brief reports how learners fared under it.

<sub>criterion · sequence, practice · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Reteach, then retest on new items

After a miss, reteach what failed, retest on new parallel items or a fresh test form, never the same ones, check again later, and send repeated failure to placement review. An evaluation of a reading course asked for 2-3 parallel forms of each lesson test so a three-state retry could work.

The reading project's mastery doctrine gives a gate three outcomes, promote, keep practising or switch to corrective instruction, because a student who can pass by sampling similar items again and again shows persistence or luck, not mastery. Its adopted obligations map wrong answers to corrective feedback, alternate instruction and a new parallel check, escalate after repeated non-progress instead of allowing endless retries, and require parallel forms with no shared items for a retry. A simulated course design named its retry path reteach-first, no-escalation, and a second round of course findings asked for intensive instruction and a delayed test on new items when the 90% bar is not met. Send a second failure to a review of placement or sequence instead of an endless loop.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd` (63): “The system needs three outcomes, not two: promote, keep practising, or switch to corrective instruction.”
- `grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd` (90): “If learners can eventually pass by repeatedly sampling similar items, the gate is measuring persistence (or luck) rather than acquisition mastery.”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/feedback-obligations.jsonl` (48): “Map high-value wrong responses to bounded corrective feedback, alternate instruction, and a new parallel check; repeated non-progress must trigger an explicit escalation rather than endless retries.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md` (56): “(≥2, zero shared items) are required for three-state retry”
- `grade3-reading/knowledge_bot/knowledge/kb-0011-run6-amalgamation-v2-engine-output.qmd` (121): “`retry_path_reteach_first_no_escalation` mitigates after 2”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (141): “Require 90% to advance; if not met, give intensive instruction and a delayed test with new items.”
- `grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd` (60): “2-3 forms each so three-state retry works”
- `grade3-reading/knowledge_bot/knowledge/kb-0022-incept-team-sync-2026-06-17.qmd` (63): “same test re-shown (small chance of variety)”
- `grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd` (252-253): “repeated items on retake”
- `grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd` (43): “neither the exact count nor an exception policy was finalized.”
- `grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd` (65): “A mastery system that lacks an explicit “switch mode” state will inevitably turn persistence into the hidden criterion for passing.”
- `grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd` (66): “Therefore the stopping policy must include an escalation trigger (“practice isn’t working”) and a designed corrective response (what to restudy and how to verify recovery).”
- `grade3-reading/knowledge_bot/knowledge/kb-0157-mastery-signal-evidence-base.qmd` (430): “when a learner is failing, we currently just let them keep attempting items.”
- `grade3-reading/knowledge_bot/knowledge/kb-0157-mastery-signal-evidence-base.qmd` (433): “Formalises “wheel-spinning” as the case where additional practice yields diminishing probability of mastery”
- `grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd` (230): “After corrective instruction, the system should re-check using near-miss and transfer variants to confirm the misconception was actually repaired, not merely coached.”
- `grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd` (67-68): “Rebuild every assessment and writing criterion as failed function -> relevant taught check -> different-evidence retry.”
- `grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd` (86): “Commit `2056514` closes the six repair buckets recorded in kb-0167”
- `grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd` (88): “criterion-level correction mappings”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (143): “- Error correction should be immediate and brief: correct, test, give intervening items, then retest later.”
- `grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd` (67-68): “4. Rebuild every assessment and writing criterion as failed function -> relevant taught check -> different-evidence retry.”
- `grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md` (46): “Data-derived: the incumbent's harder-on-retry drops supporting-details 64%→41% (−22.6pt)”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (310): “**Never re-serve the identical item; never hand a harder item after failure.**”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (314): “The incumbent's retry path escalates difficulty and measurably destroys attempt-2 accuracy (supporting-details 64% → 41%). Reteach-first protects confidence AND dosage.”
- `grade3-reading/knowledge_bot/knowledge/kb-0031-how-it-works.qmd` (156): “When a student scores below mastery on a standardized test (less than 90%), the platform analyzes which standards were missed and generates a **targeted remediation course** containing just the lessons needed to fill the specific gaps. The student completes the hole-filling content, retests, and only advances once mastery is demonstrated.”
- `grade3-reading/knowledge_bot/knowledge/kb-0026-evaluating-apps.qmd` (24): “| **Hole-filling compatibility** | Targeted remediation is possible when gaps show up |”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (72-74): “D15 failure routing: reteach via M7 → one delayed retest on new items → a second failure routes to placement/sequence review. No infinite retest loop”
- `ti-courseplans-audit/docs/instruction-modes-spec.md` (36): “A second consecutive failed delayed retest routes to placement/sequence review — never an infinite loop.”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D6-practice-durable-mastery.md` (16): “≥90% acquisition gate; failure → intensive instruction → delayed (~24h) retest on NEW items, never an endless loop”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D1-gradual-release-explicit-instruction.md` (35): “a second consecutive failed delayed retest routes to placement/sequence review, never an infinite loop”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (141): “- Require 90% to advance; if not met, give intensive instruction and a delayed test with new items.”
- `grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd` (76): “97/172 items can't populate disjoint parallel forms without overlap.”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd` (56): “The trace shows correction, an alternate explanation or representation, a parallel new attempt, a delayed recheck where claimed, retry bounds, and escalation after non-progress.”
- `grade3-reading/ti-courseplans/docs/instruction-modes-spec.md` (36): “A second consecutive failed delayed retest routes to placement/sequence review — never an infinite loop.”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json` (461): “Route historical-thinking feedback to the failed function, then reassess with a parallel task that uses different evidence.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (769): “**SPOV 3 – The system needs three outcomes, not two: promote, keep practising, or switch to corrective instruction.**”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (771): “A mastery system that lacks an explicit “switch mode” state will inevitably turn persistence into the hidden criterion for passing.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (796): “If learners can eventually pass by repeatedly sampling similar items, the gate is measuring persistence (or luck) rather than acquisition mastery.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (797): “To prevent grind-through, mastery evidence must include breadth (multiple item families / near-miss contrasts) and recovery verification after any corrective branch.”
- `grade3-reading/ti-courseplans/docs/instruction-quality-standard.md` (114): “On a miss: **Correct** (answer + brief why) → **Test** (re-ask immediately) →”
- `grade3-reading/ti-courseplans/handoff/timeback-course-explorer/references/eval-analysis.md` (96): “the student re-attempts until 100%, which is *stricter* than a 90% gate”
- `downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx` (20 (textutil text)): “Runs as two parallel forms; the second is shown if the first is wrong.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx` (44 (textutil text)): “FORM 2 (second chance / clean measure)”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (67): “form 1 corrects, form 2 gives a cleaner read on whether the correction took.”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (155): “The doc’s FORM 2 has no renderer slot — the retry ladder substitutes (accepted deviation, logged).”
- `grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/assessment-set.json` (26): “Score atomically, record the first failed historical function, teach through its resolved local check, and administer its parallel retry with different evidence before reassessment.”
- `grade3-reading/edullm-review-hub/course-packages/courses/apush/review/evidence/incept-acceptance.json` (37): “Unit 1 exposes targeted feedback, correction, and different-evidence retry.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md` (39-40): “**Two parallel forms (A + B) sharing ZERO items.** Parallel forms are required for retry without answer leakage (a student who retests sees the other form).”
- `grade3-reading/knowledge_bot/knowledge/kb-0022-incept-team-sync-2026-06-17.qmd` (63-64): “**Reattempt:** same test re-shown (small chance of variety); randomizing via multiple tests is TBD (check PowerPath docs).”
- `grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd` (37): “two 4-5 item tests are un-gateable (no "90% of 4"); no three-state retry / parallel forms.”
- `grade3-reading/knowledge_bot/BRIEFING.md` (32): “single static form (gameable)”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (461): “### G5-POL-INS-010: Cap error-correction interrupts at two per lesson dose and route a second consecutive failed delayed retest to placement or sequence review.”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (464): “- **Rationale:** Infinite retry loops confuse persistence with instruction and hide a likely prerequisite or sequence failure.”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (469): “per_dose_interrupt_cap == 2 and second_failed_delayed_retest_route in {placement_review,sequence_review}”
- `grade3-reading/_archive/2026-08-13-consolidation/tmp-g5-r8-src-scripts.tar.gz` (scripts/lane-tools/drafts/xp-dose-mapping.md inside it) (55): “- **In-dose interrupts** (cap 2/dose): correction + immediate retest happen inside the segment”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/docs/BRAINLIFT.md inside it) (250): “| Miss flow | Correction, parallel check, delayed retest, spaced return, capped retry | A wrong response must reopen instruction, not produce feedback-plus-lockout. |”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (405): “## Dropped approaches (inherited from G3; confirmed apply at G7)”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (408): “difficulty escalation after failure (measurably destroyed attempt-2 accuracy”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (372): “three-state retry (mastered/developing/not-yet; never escalate difficulty on failure)”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md` (223-224): “Three outcomes at every gate: promote / keep practising / SWITCH TO CORRECTIVE — never just pass/fail.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md` (224-225): “Guard grind-through: a stretch changes the evidence slice (item families, near-miss contrasts, recovery verification), never more-of-the-same.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md` (221-222): “Error correction: Correct → Test → Retest → spaced re-appearance; interrupt cap 2/dose; a second consecutive failed delayed retest routes to placement review, never a loop.”
- `grade3-reading/course-renderer/authoring/inputs/rule-packs/reading-g3.json` (33): “exactly one taught word, then two parallel usage forms. Form 1 teaches (retry until correct); Form 2 is the clean measure.”
- `grade3-reading/course-renderer/docs/pedagogy/example-lesson-components-2026-08-06.md` (28): “Runs as two parallel forms; the second is shown if the first is wrong.”
- `grade3-reading/ti-courseplans/handoff/timeback-course-explorer/brainlift/amalgamation-v2.md` (127): “The incumbent's retry path escalates difficulty and measurably destroys attempt-2 accuracy (supporting-details 64% → 41%).”
- `grade3-reading/ti-courseplans/handoff/timeback-course-explorer/brainlift/amalgamation-v2.md` (176): “Supporting-details attempt-1: 64%”
- `grade3-reading/ti-courseplans/handoff/timeback-course-explorer/brainlift/amalgamation-v2.md` (177): “Supporting-details attempt-2 (under escalation): 41%”
- `grade3-reading/ti-courseplans/courses/g4g5-math-checkpoints/brainlifts/v0.1.md` (38): “Cycles here: fail → re-teach (routed) → **parallel same-difficulty form**.”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/pedagogy-policy.json` (1419): “Cap error-correction interrupts at two per lesson dose and route a second consecutive failed delayed retest to placement or sequence review.”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/pedagogy-policy.json` (1420): “Infinite retry loops confuse persistence with instruction and hide a likely prerequisite or sequence failure.”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/showcase-selection.json` (19): “"second_error_action": "stop independent progression and route to operation-step review or placement review",”
- `incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (372): “never escalate difficulty on failure”
- `incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (408-409): “difficulty escalation after failure (measurably destroyed attempt-2 accuracy”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (503-508): “A route has four parts: 1. evidence of the failure; 2. the exact taught check to revisit; 3. a parallel task with a different source or case; 4. a pass condition that describes the corrected function.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (404-406): “The correction route targets the function that failed. A missing second example receives an evidence-selection task. Two examples with no relationship receive a reasoning task. A broad thesis receives a claim-boundary task. This is more useful than returning one total score.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT1-VERTICAL-SLICE.md inside it) (41): “criterion-level routes for all 32 scored components: eight MCQs, nine SAQ parts, ten writing-task criteria, and five mini-DBQ criteria. Each names the failed function, exact taught check, and a parallel retry with different evidence; and”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT1-VERTICAL-SLICE.md inside it) (42): “an 18-function correction registry with observable failure evidence, retry selection rules, prompts, and pass conditions.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/FULL-COURSE-AUTHORING-STATUS.md inside it) (51): “Target-runtime mastery, XP, event, and accessibility behavior | Contracted, not run”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/05_LIMITATIONS.md` (118): “Item security is weaker: students who take the test multiple times will see repeated items (mean pairwise between-session overlap 29.4%)”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/ADDRESS_STATUS.md` (40): “**retest-overlap exclusion** — items a candidate answered in their last 2 sessions are excluded from selection, with a three-stage starvation fallback (relax to last-1, then off, plus a mid-session unfiltered retry) so exposure control can never prevent a session from starting or end one early”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/ADDRESS_STATUS.md` (40): “Both new mechanisms ship **off by default** — pre-committed for the calibration ("regular use") stage, not the pilot.”
- `grade3-reading/curriculum-gen/audits/PETER-PAN-AUDIT-2026-08-24.md` (98-99): “provide a second parallel form after an error”
- `grade3-reading/ti-courseplans-wiki/Perfect-Course-Rulebook.md` (381-382): “a later task asks the learner to update, transfer, or reapply the corrected thinking”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/TEACHING-ASSESSMENT-CONTRACT.md inside it) (118-123): “Correction follows one inspectable chain: `observed failed function -> relevant taught check -> parallel retry with different evidence` Topic-level remediation, a link to an entire lesson, or a retry over the same assessed stimulus does not satisfy the contract.”
- `grade3-reading/edullm-review-hub/course-packages/courses/apush/review/brainlift.html` (152-153): “A failed function routes to a concrete taught check and a parallel retry with different evidence.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_08 10_30 CEST - Notes by Gemini.md` (342): “Now those kids between 60 and 80% they didn't know what they didn't know. So they failed it the first time and then they failed it the second time they kept failing it again and again and again.”
- `g9/library/text/L612555.txt` (342): “Now those kids between 60 and 80% they didn't know what they didn't know. So they failed it the first time and then they failed it the second time they kept failing it again and again and again.”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/markdown/PLAN-EVALUATION.md inside it) (112-114): “never an immediate same-item retry”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (134-135): “Showing the correct answer and repeating the same item is not evidence that a misconception was repaired. It may show recognition or memory for feedback.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/MAP_PROXY_VALIDITY_CASE.md` (76): “3. Track growth meaningfully when the same items are administered repeatedly”

Published: [Beck & Gong 2013](https://link.springer.com/chapter/10.1007/978-3-642-39112-5_44)

Against: an earlier design simply re-showed the same test, a small item bank means repeated items on a retake, and the number of misses that should trigger reteaching was never settled; the rule is adopted, not measured here. A harder retry will score lower anyway, so the fall shows more failure on the retry, not lost learning; and after two failed cycles the same plan does change the level, stepping the difficulty down (`grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md`, line 310). The evidence is the platform's own description of its rule, not a measured result. The project's direct-instruction protocol gives the answer and re-asks the same item at once, then re-serves the miss (`grade3-reading/ti-courseplans/docs/instruction-quality-standard.md`, line 114), and a course evaluation counted re-attempting lesson tests until 100% as stricter than a 90% gate (`grade3-reading/ti-courseplans/handoff/timeback-course-explorer/references/eval-analysis.md`, line 96). The platform could not always show the second form: the built lesson's first walkthrough records "The doc’s FORM 2 has no renderer slot — the retry ladder substitutes (accepted deviation, logged)." One platform's guide reuses the same item in instruction and review and treats the risk of cueing as a medium-to-low concern, because courses rotate a large deck of questions; that guide is not cited because its file's path carries a person's name. A small clean bank may not fill disjoint forms: one Grade 5 build noted that 97/172 items can't populate disjoint parallel forms without overlap (`grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd`).

<sub>criterion · practice, sequence, evidence-of-learning · universal · from ap, g3, research · adopted-rule · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Retrieval needs a gap

Make retrieval ask for something taught earlier after a gap, with it hidden, because a check straight after teaching shows only that the student was following.

A BrainLift on intro videos for a reading course separates retrieval from re-exposure. A question asked before the video about an earlier lesson is real retrieval, because the child has to produce the answer across a gap of days, while the sync check after a video comes too soon after the teaching and checks attention, not memory. It rests the rule on retrieval and spacing research: retrieving strengthens retention more than re-reading (Roediger and Karpicke 2006), and knowledge revisited across spaced intervals is retained far better than knowledge massed (Cepeda et al. 2006). For example, ask for a lesson's key idea from memory at the start of the next part and again later in the unit, instead of restating it.

Quoted:

- `downloads/BrainLift - What makes a good intro video.md` (339): “Real retrieval needs a gap the child fills.”
- `downloads/BrainLift - What makes a good intro video.md` (329): “That is real retrieval, because the child has to produce the answer across a gap of days. The sync check after a video is not.”
- `downloads/BrainLift - What makes a good intro video.md` (430): “The sync check after a video is a check on attention, not on memory.”
- `downloads/BrainLift - What makes a good intro video.md` (493): “retrieving strengthens retention more than re-reading.”
- `downloads/BrainLift - What makes a good intro video.md` (494): “knowledge revisited across spaced intervals is retained far better than knowledge massed.”
- `grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt` (54): “The sentence must not be visible when the child produces it.”
- `grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt` (118): “recur as something the child is asked to produce, not something restated at them”
- `grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt` (118): “the sentence taught in Part 1 is the sentence asked for at the start of Part 2, and again in Part 3, without being shown”
- `grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt` (119): “If a threshold sentence appears once and never again, we have taught a slogan.”
- `grade3-reading/artifacts/feedback-closing-questions-2026-09-24/REGISTER.md` (104): “sentence not printed”
- `shadow-content-eval/references/closing_questions_pattern.md` (79): “It is asked for (produced, not restated) at the start of the next part and again later in the unit, **without being shown first**. A sentence that appears once is a slogan.”
- `shadow-content-eval/references/closing_questions_pattern.md` (86): “| Spaced, repeated retrieval | well evidenced |”
- `shadow-content-eval/reports/G3-U1-L2-main-review.md` (52): “| The Q1 sentence recurs later without being shown | **Pass.** It is asked for from memory in G3-U1-L7 p0b and G3-U1-L14 p0b. |”
- `shadow-content-eval/SKILL.md` (201): “a reworded recall is not recognised, so check `CLOSE-RECUR-MISSING` by eye before reporting it.”
- `grade3-reading/course-renderer/docs/handover/closing-questions/design-mock-l1.html` (210): “Choral repetition is weak evidence, kept for language and motivation, which is why the sentence is hidden and must recur”
- `grade3-reading/course-renderer/docs/handover/closing-questions/design-mock-l1.html` (210): “Our turn is unmarked and never the test; the test is the hidden recall and the Part 2 recall.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (106-107): “The canonical M1 on-ramp (blocking U4L1 retrieval — "sugar made by a producer stores ___" plus a kelp node-select, said aloud) is not rendered anywhere in the build.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (108-109): “canon records a U1·L6 lineage (deepen, not introduce) — the justification is factually wrong, not just an omission.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (113): “on-ramp answers said aloud before selection”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (724-725): “the U4·L1 retrieval ("sugar made by a producer stores ____") runs aloud-first through `buildGate`”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (726-727): “a miss re-presents the fact via the fixture's own `on_error` and re-asks — blocking retrieval, no release valve”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (92): “after 2 failed retries the release valve opens”
- `grade3-reading/ui-audit-2026-09-08/round-1/g3/PROPOSALS.md` (44): “The question can be answered from its introduction rather than prior teaching.”
- `g9/transcript/chat-transcript.redacted.txt` (6356): “Retrieval stays free of visual hints; reading, independent writing and saved progress are preserved.”
- `g9/player/design/assets/our-build-intro-checks.json` (107): “"carry_to_lesson_2_retrieval": true”
- `g9/sources/Othello Unit Video_ Info Sheet for Devfactory.md` (78): “the three checks pause the video; the student answers, then the video continues. The answers feed Lesson 2 retrieval.”
- `g9/library/text/Lb9608f.txt` (135-137): “Subramaniam criticized the associated questions for being overly literal, requiring students to repeat exact wording from five seconds prior rather than engaging in critical introspection (00:06:28”
- `othello-course-renderer-draft/repo/docs/handover/closing-questions/HANDOVER.md` (90-92): “**Your turn** (sentence removed **everywhere**: the card goes, earlier beats fold with no sentence text, no "See the whole ask again", no tap-to-hear, Read to me does not replay it).”

Published: [Roediger & Karpicke 2006](https://doi.org/10.1111/j.1467-9280.2006.01693.x) · [Cepeda et al. 2006](https://doi.org/10.1037/0033-2909.132.3.354)

Against: none found; the design rates its basis well evidenced but quotes no studies or effect sizes (the same file, line 172). Matching by text misses a reworded recall: "a reworded recall is not recognised, so check `CLOSE-RECUR-MISSING` by eye before reporting it." (`shadow/content-eval/SKILL.md`, line 201), and recurrence can't be checked when the later lessons are missing (`shadow/content-eval/reports/G3-U2-L1-review.md`, line 229).

<sub>criterion · practice, sequence, evidence-of-learning · universal · from g3, research · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Retrieval questions teach, not just measure

Use low-stakes retrieval questions as learning events, not only as measures, because practising recall beats restudying. In one meta-analysis, practice testing beat restudying at g = +0.51.

An assessment BrainLift in the reading course's feedback treats multiple-choice questions as learning events first and puts the testing effect for multiple-choice practice at g = +0.70 against restudying; its own notes on the meta-analysis behind the figure give g = +0.51 for practice testing against restudying, g = +0.93 against no activity, and g = +0.70 for multiple-choice practice tests against g = +0.48 for short-answer ones. The course's evaluation criteria make active recall the primary learning event, not passive consumption (`grade3-reading/ti-courseplans/skills/timeback-course-eval/references/eval-criteria.md`, line 38).

Quoted:

- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (1989): “The testing effect for MCQ-based practice (g = +0.70 vs. restudying) is one of the largest effect sizes in educational psychology.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (2203): “Practice testing produced moderate effect sizes vs. restudying (g = +0.51) and large effect sizes vs. no activity (g = +0.93).”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (2204): “MC practice tests showed a larger effect size (g = +0.70) than short-answer tests (g = +0.48)”
- `grade3-reading/ti-courseplans/skills/timeback-course-eval/references/eval-criteria.md` (38): “Active recall is the primary learning event, not passive consumption.”
- `g9/transformer/src/mechanics/key-words.js` (1-2): “Key words: study a set, then recall each word into a gap. Each word comes back in a sentence about the text with a … blank where it goes, cued by its meaning, and the student types it from memory.”
- `g9/transformer/web/lesson.js` (541): “Study each word and what it means. Then put them away, and put each back into its sentence from memory.”
- `g9/transformer/src/mechanics/key-words.js` (93): “Is filled_${i} true to passage?”

Published: [Adesope, Trevisan & Sundararajan 2017](https://doi.org/10.3102/0034654316689306) · [Roediger & Karpicke 2006](https://doi.org/10.1111/j.1467-9280.2006.01693.x) · [Butler & Roediger 2008](https://doi.org/10.3758/MC.36.3.604)

Against: The same BrainLift warns that plausible wrong options can implant false knowledge when no feedback follows, a risk that feedback largely removes (`grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md`, line 1991).

<sub>criterion · practice, evidence-of-learning · universal · from g3, research · external-research · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Reveal in order, keep everything shown

Reveal a screen's parts in order, never take away anything that has appeared, and offer the way on only once everything on the page has been seen.

The Grade 9 prototype reveals each screen's parts in order, each when the student asks for it, with nothing on a timer; nothing that has appeared goes away, Next appears only once everything on the page has been seen, and because the reveal count lives in the session, a refresh resumes on the same part and coming back shows everything already seen. A younger-grade checklist of lesson invariants has every step, chart row, hint rung and sub-thought arrive on exactly one Next tap, checked by a scripted walk, and the younger-grade audio rules hide the Next button while the voice is sounding. No source measures the effect on learners.

Quoted:

- `othello-course-renderer-draft/repo/docs/design/grade-9/prototype/README.md` (37): “Every screen reveals its parts in order, and the student asks for each one ("Then what happened?", "Show her proof").”
- `othello-course-renderer-draft/repo/docs/design/grade-9/prototype/README.md` (37): “Nothing is on a timer, nothing that has appeared goes away, and Next only appears once everything on the page has been seen.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/prototype/README.md` (37): “so a refresh resumes on the same part and coming Back shows everything already seen.”
- `othello-course-renderer-draft/repo/docs/qa/new-lesson-qa-invariants.md` (135-137): “**E1. Reveal on Next, everywhere, both modes.** Every step, chart row, ladder rung and sub-thought arrives on exactly one Next tap; the voice never reveals or advances.”
- `othello-course-renderer-draft/repo/docs/rules/audio-and-voiceover.md` (216-217): “The same button must not exist while the voice is sounding, and neither must an armed microphone.”

Against: No source measures the effect on learners.

<sub>criterion · sequence · universal · from g9, g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Revisit a topic only with an upgrade

Bring early ideas and skills back later, but only with a real upgrade, because a return at the same depth adds practice but no new demand.

The curriculum architecture BrainLift separates a strong spiral, where each revisit adds a real upgrade (a new representation, wider scope, greater abstraction, stronger warrant or more demanding transfer), from a weak one of annual re-coverage with tiny increments that wastes time rebuilding context (`grade3-reading/ti-courseplans/feedback/feedback2/WF - Curriculum Architecture Br - 260713-123107.md`). The reading project's failure taxonomy lists a throughline that doesn't spiral as a failure class: claimed throughlines must recur at greater depth, not just be labelled (`grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md`). An upgrade can be more depth, a new representation or domain, wider scope, more abstraction, harder transfer or a combination with earlier skills.

Quoted:

- `grade3-reading/ti-courseplans/feedback/feedback2/WF - Curriculum Architecture Br - 260713-123107.md` (104): “each revisit adds a real upgrade — a new representation, wider scope, greater abstraction, stronger warrant, or more demanding transfer.”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (125): “claimed throughlines (adaptation, power) must recur at greater depth, not just be labeled”
- `grade3-reading/ti-courseplans/feedback/feedback2/WF - Curriculum Architecture Br - 260713-123107.md` (108): “use blocks where coherence and immersion are essential”
- `grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md` (115): “Evidence: L6 p12 and L7 p12 contain verbatim-identical skill-intro text:”
- `grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md` (140): “skill identically, not cumulatively. The deeper coordination (e.g., "find the evidence, then”
- `grade3-reading/artifacts/g5-course/G5-CURRICULUM-OUTLINE.md` (44): “(29 lessons), then at `deepen` phase in a new knowledge domain (26 lessons — the canon's”
- `shadow-bench/docs/brainlift.md` (197): “Early course builds left out compounding. Concepts introduced early were never brought back later at higher difficulty.”
- `shadow-bench/docs/brainlift.md` (145): “That defect was an absence: concepts introduced early were never brought back at higher difficulty, and nothing was wrong inside any single lesson.”
- `shadow-bench/docs/brainlift.md` (74): “on early course structure, which produced the compounding requirement (DOK1-8).”
- `shadow-bench/docs/brainlift.md` (35): “Prerequisite order, spacing, compounding, repetition and difficulty progression all need at least two lessons in view.”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/foundations.md` (22-23): “A topic is taught once, at the right grade, by one owner. Re-teaching the same content at a higher grade forces the deeper pass to re-teach the basics.”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/foundations.md` (23-24): “Grade 4 deepens Grade 3's domains and hands off cleanly to Grade 5.”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/load-bearing-rubric.md` (100): “R2. Score above the boundary but an adjacent grade owns the era/domain (the one-grade-owns-a-topic rule from the Curriculum Architecture BrainLift)”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/load-bearing-rubric.md` (100): “Revolution 8.90 → ceded to G5”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/SEQUENCING-BRIEF.md inside it) (62-64): “A linked earlier concept must appear in the later unit's retrieval, model, guided analysis, or synthesis; merely naming the old unit in metadata does not count. Revisit links are never graded before they are reactivated.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/SEQUENCING-BRIEF.md inside it) (135-136): “**F5: Fake cumulative review.** Detection: a revisit appears only as a label or recall question. Recovery: require the earlier mechanism to explain new evidence.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/COURSE-PLAN.md inside it) (53-54): “A revisit is not justified by shared vocabulary alone. It must make a prior mechanism useful in a new historical problem.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/SEQUENCING-BRIEF.md inside it) (45-46): “Overlapping boundaries are intentional; they let the next unit reinterpret transitions rather than create an artificial clean break.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (265-268): “The overlap among official periods is productive. Reconstruction can be studied as the culmination of Civil War change in Unit 5 and as a starting condition for the New South and industrial order in Unit 6. The course marks the purpose of a revisit so repetition compounds knowledge instead of merely presenting the same label twice.”
- `grade3-reading/course-renderer/docs/extras/g4-crosswalk-2026-08-17.md` (51): “the Grade-3 course already teaches body systems at the same depth — a repeat, not a ladder”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/BRAINLIFT.md` (61): “A candidate that could not declare a ▸Adds was cut (World Folktales II, Ecosystems II).”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/markdown/PLAN-EVALUATION.md inside it) (159-160): “Two candidates that *couldn't* declare a ▸Adds (World Folktales II, Ecosystems II) were cut in `topic-selection.md`, the check working as intended.”
- `othello-course-renderer-draft/repo/docs/extras/g4-crosswalk-2026-08-17.md` (51): “the Grade-3 course already teaches body systems at the same depth — a repeat, not a ladder”

Against: The same BrainLift keeps blocks rather than spirals where coherence and immersion are essential (`grade3-reading/ti-courseplans/feedback/feedback2/WF - Curriculum Architecture Br - 260713-123107.md`, line 108). The same review's refutation defends the repeat as deliberate practice for automaticity: "**Adversarial refutation attempt:** This is by design — the FIND skill is practiced in two" (`grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md`, line 129); the finding was graded major, not failing. One case only: 'This is the only cross-lesson defect on record.' (shadow-bench/docs/brainlift.md line 197), and it comes from the source's recollections rather than records (line 181).

<sub>criterion · sequence, demand · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Route by the need, not the level

Route learners who need more comprehension help by their specific need, vocabulary and background knowledge, strategy or text structure, not by a global reading level.

An IES video on when to use small groups in teaching reading comprehension, quoted in a reading course's review standard, notes that a recent meta-analysis found no research to support level-based grouping and advises grouping by students' specific assessed needs: some need more work on vocabulary and background knowledge, others more strategy instruction or attention to text structure (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/branch-by-need-profile.md`). The standard's design infers that need from the learner's errors, so two learners who missed the same item can go down different tracks, and it never answers a miss by pushing an easier passage on the same skill. The video does not name the meta-analysis.

Quoted:

- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/branch-by-need-profile.md` (13): “It's important to note that in a recent meta-analysis, there was no research found to support level-based grouping.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/branch-by-need-profile.md` (15): “Rather, when you're grouping students for reading comprehension or for anything, you want to look at their specific assess needs.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/branch-by-need-profile.md` (17): “some students are likely to need more work on vocabulary and background knowledge building, whereas other students might benefit from more strategy instruction or more attention to text structure.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/branch-by-need-profile.md` (20): “When a child fails a comprehension item, the router does not push an easier passage on the same skill”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/branch-by-need-profile.md` (20): “two children who both missed the same item can be sent down *different* tracks”

Published: [When should teachers use small groups in teaching reading comprehension?, REL West video](https://www.youtube.com/watch?v=iA2tiv5mSec)

Against: The same standard's curriculum criteria say the course does not rely on a diagnostic test to find knowledge or comprehension gaps, since a valid one does not exist, and build breadth of knowledge instead (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D7-knowledge-first-curriculum.md`, line 35).

<sub>criterion · practice, evidence-of-learning · universal · from g3, research · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Say each new term aloud

Have learners say each newly taught term aloud as unscored practice, since clicking a word doesn't build command of it. One course gave all 165 academic terms and 124 blocking words a spoken prompt, and captured and scored none of the speech.

A Grade 5 reading course's pedagogy policy requires spoken production for every pre-taught term: an academic term carries a say-it prompt answered aloud, a blocking word a say-back prompt after its model pronunciation, and on-ramp answers are said aloud before they are selected (`incept-package-hub/course-packages/courses/g5-reading/source/canonical/pedagogy-policy.json`, line 999). Its rationale is that students learn from what they produce, saying, writing or typing it, not from what they click, and the rule rests on review feedback rather than a measurement. A later refresh gave all 165 academic terms and 124 blocking words productive oral prompts, and every articulation selects evidence, rehearses aloud, then types an own-words explanation. Its review notes also require an unscored spoken rehearsal of claim and evidence before typing (`incept-package-hub/course-packages/courses/g5-reading/review/start-here.md`, line 70).

Quoted:

- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/pedagogy-policy.json` (999): “Every pre-taught term requires spoken production”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/pedagogy-policy.json` (1000): “Students learn from what they produce - saying it, writing it, typing it - not from what they click; recognition-only vocabulary contact does not build expressive command of a term.”
- `incept-package-hub/.worktrees/codex-g5-july27-publish/course-packages/courses/g5-reading/review/start-here.md` (79): “all 165 academic terms and 124 blocking words have productive oral prompts;”
- `incept-package-hub/.worktrees/codex-g5-july27-publish/course-packages/courses/g5-reading/review/start-here.md` (81): “every articulation selects evidence, rehearses aloud, then types an own-words explanation;”
- `incept-package-hub/course-packages/courses/g5-reading/review/start-here.md` (70): “articulation requires an unscored spoken rehearsal of claim and evidence before typing;”
- `incept-package-hub/.worktrees/codex-g5-july27-publish/course-packages/courses/g5-reading/review/start-here.md` (90-91): “Spoken production remains prompted and self-checked only: no speech is captured, scored, or used in progression.”

Against: No speech is captured, scored or used in progression (`incept-package-hub/.worktrees/codex-g5-july27-publish/course-packages/courses/g5-reading/review/start-here.md`, lines 90-91), so the effect was never measured. Counted as evidence of production, single-word say-backs are discounted as trivial by a red-team taxonomy in the reading project (`grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md`, line 183).

<sub>criterion · practice, format · domain · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Say what will be learned, then teach

Early in a teaching script, state what will be learned as one testable sentence and go straight into teaching; a hook or topic label doesn't count. The target sentence must come within about the first 30% of the script, and an opening hook does not count.

The video-script check asks for an orientation beat: one sentence that states the learning target as a testable proposition, in the first ~30% of the script, followed straight away by teaching rather than a multi-step roadmap or a series of questions (`shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt`). A sentence that only names a topic fails, and so does a script whose first substantive statement is a hook, unless a clear orientation beat also appears within the first 30%.

Quoted:

- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (204): “- One sentence that explicitly states the learning target as a testable proposition”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (206): “- Must appear in the first ~30% of the script”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (207): “- Immediately followed by teaching (not by a multi-step roadmap or a series of questions)”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (221): “If the first substantive statement is a hook, the script fails proposition_clarity unless a clear orientation beat also appears within the first 30%.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (218): “- "Today we're going to learn about cells and what makes them special." → Describes a topic, not a testable proposition.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (201): “cognitive load research is unambiguous that learners encode better when they know the learning target before the details arrive.”
- `shadow-bench/` (commit bfc4165) (19): “genuine rubric ambiguity — the opening hook vs orientation-beat distinction”
- `g9/sources/Othello Unit Video_ Info Sheet for Devfactory.md` (20): “Every sentence carries knowledge. No puzzle hooks, rhetorical teasers or openings that are only atmosphere.”

Against: The rationale is uncited: 'cognitive load research is unambiguous that learners encode better when they know the learning target before the details arrive.' (`shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt`, line 201). The hook-versus-target line is also the one distinction that still flipped after the judge was made more consistent: 'genuine rubric ambiguity — the opening hook vs orientation-beat distinction' (`shadow-bench`, git commit bfc4165, line 19).

<sub>criterion · sequence, alignment, wording · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Select the evidence first

Have students pick out the evidence before they put it in their own words or write about it.

Review feedback on a grade 3 course listed evidence-first articulation among the repairs it asked for. The lesson packet written in response puts evidence selection before paraphrase or written articulation in its required lesson sequence; it is a rule adopted from review, not a result measured here.

Quoted:

- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md` (42): “5. evidence selection before paraphrase or written articulation;”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (94): “evidence-first articulation”
- `grade3-reading/ti-courseplans-wiki/Perfect-Course-Rulebook.md` (172-173): “The learner rereads and locates source evidence before interpreting, rehearsing, or composing from it.”
- `grade3-reading/_archive/2026-08-13-consolidation/orientation-sweep-digest/agent-damage.md` (18): “EV: Same RT-R3 report, section 2: find-then-write went 0/48 → 45/48 generated lessons; feedback median 24 words (old ~91-word lineage gone); verified by independent recomputation”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (387-391): “First, copy-delete is the default a grade 4 child returns to under load, so a task that lets a child paste a long stretch will get a long stretch. Second, and this is the one that bears on our design: the copying is not laziness, it is what the child does when asked to produce prose about a text before the selection has been made.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l2-the-cyclops.md` (389-391): “the copying is not laziness, it is what the child does when asked to produce prose about a text before the selection has been made.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (38): “p23 is not an evidence task in the D5.37 sense; it is the unaided synthesis half of a two-item Show-what-you-know bundle.”

Against: A later run found counter-evidence (`grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md`).

<sub>criterion · sequence, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Sequence by knowledge and by difficulty

Sequence a course so knowledge and difficulty both progress, since ordering by standard or by readability alone left one of them flat. A course organised by standard had all four units flat at about 900 to 913 on a reading-level scale.

A coherence check on one course plan found no cross-unit difficulty escalation: all four units sat at about 900-913L because they were organised by standard (`grade3-reading/artifacts/LANE1_COURSE.md`). In another build, the assembly script grouped items by readability band and no knowledge progression existed (`grade3-reading/artifacts/g5_build_2026_07_02/g5_analysis_digest.md`), and a review called one course a readability staircase rather than a knowledge progression (`grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md`).

Quoted:

- `grade3-reading/artifacts/LANE1_COURSE.md` (208): “All 4 units are flat at ~900-913L average.”
- `grade3-reading/artifacts/LANE1_COURSE.md` (208): “Units are organized by CCSS domain, not by difficulty progression.”
- `grade3-reading/artifacts/g5_build_2026_07_02/g5_analysis_digest.md` (40): “groups by LEXILE band (830/920/1010L), not topic coherence; no knowledge progression exists”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (43): “The course is sequenced as a Lexile staircase, not a knowledge progression”
- `grade3-reading/_archive/2026-08-13-consolidation/top-level-docs/HANDOFF_3_KEY_ISSUES.md` (25): “flat Lexile ~900-913L (no cross-unit ramp, Gate 4C)”

Against: none found

<sub>criterion · sequence, demand, alignment · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Show how taught words relate

Introduce related new words as the structure they form, such as a web showing the concept and how the rest relate to it, not as a deck of equal cards. One review cut a 6-card deck whose words formed one concept, three words for a person and two for a mechanism.

The review of a Grade 9 prototype dropped a deck of six tap-to-reveal word cards, since the word web already introduced the words and could show how they relate (`g9/library/text/L36b8ba.txt`, line 80). Its note argues that the six were not a list but a structure, a concept, three words describing the person and two naming the mechanism, which equal cards hide and the web shows (line 215). The review offers such notes as rationale that has not been confirmed (line 13).

Quoted:

- `g9/library/text/L36b8ba.txt` (215): “These six are not a list, they are a structure: betrayal is the concept, deceitful and untrustworthy and disloyal describe the person, and pretense and façade name the mechanism.”
- `g9/library/text/L36b8ba.txt` (80): “Drop the six-word card deck. The web already introduces the words and can show how they relate.”
- `g9/library/text/L36b8ba.txt` (13): “Anything under "Note" is an observation made during the review rather than part of that feedback — it is offered as rationale and has not been confirmed.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (80): “Drop the six-word card deck. The web already introduces the words and can show how they relate.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (215): “These six are not a list, they are a structure: betrayal is the concept, deceitful and untrustworthy and disloyal describe the person, and pretense and façade name the mechanism.”

Against: The same note doubts the load: "Six words may also be too many for one pre-reading beat, and they are not of equal difficulty — façade and pretense are a long way harder than disloyal." (`g9/library/text/L36b8ba.txt`, line 215). The same note warns the set may be too large and uneven: "Six words may also be too many for one pre-reading beat, and they are not of equal difficulty — façade and pretense are a long way harder than disloyal." (`g9/sources/Othello_1_Feedback_DevFactory.md`, line 215).

<sub>criterion · format, media · universal · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Some scaffolds end at a grade boundary

Remove a scaffold outright at a grade boundary, rather than fading it, when the skill it supports is expected as a matter of course from then on. One course makes quote insertion a grade 4 expectation rather than a supported step.

Guidance on what changes from grade 3 to grade 4 lists seven deliberate departures, one of them that some scaffolds are removed outright, not faded, such as help putting quotes in, because children are expected to do it as a matter of course. So quote insertion becomes a grade 4 expectation, not a supported step, and sentence starters are named as something to reduce. Lesson research for a grade 4 evidence lesson draws the consequence that starters of the 'According to the text' kind are the wrong direction: the quote goes in because the child puts it in.

Quoted:

- `grade3-reading/course-renderer/docs/pedagogy/grade-4-vs-grade-3.md` (44-47): “**6. Some scaffolds are removed outright, not faded.** "We will want to absolutely remove scaffolding around like putting quotes in and stuff like that, which is things that we want them to be doing just as a matter of course." So quote insertion is a Grade 4 expectation, not a supported step.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (436-438): “So sentence starters of the "According to the text" family, which dominate the practitioner material found, are the wrong direction for us. The quote goes in because the child puts it in.”
- `grade3-reading/course-renderer/docs/pedagogy/grade-4-vs-grade-3.md` (47-48): “Sentence starters are named in the same breath as something to reduce.”
- `grade3-reading/course-renderer/docs/pedagogy/grade-4-vs-grade-3.md` (80): “| Remove quote scaffolds | Not applicable yet, no quote scaffold built | Do not build one for Grade 4 |”

Against: Nothing is built yet: the repo's own table reads "| Remove quote scaffolds | Not applicable yet, no quote scaffold built | Do not build one for Grade 4 |" (`grade3-reading/course-renderer/docs/pedagogy/grade-4-vs-grade-3.md`, line 80).

<sub>criterion · sequence, hints, demand · domain · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Source work from evidence to use

Teach source analysis in five steps: what it shows, the bounded claim this supports, the outside knowledge needed, how its maker and purpose matter, and what needs corroboration. Feedback that says only 'use the source' is replaced with one of 3 diagnostics: missing evidence, an unsupported inference or an irrelevant sourcing claim.

An AP history course's design document orders source work from evidence to historical use in five questions: what is visible or stated, what bounded claim that evidence supports, what outside knowledge is needed, how creator, audience, purpose or situation affect its use, and what remains unresolved and needs corroboration. It says the order guards against two opposite errors, treating a source as transparent truth and dismissing it as biased without extracting any evidence. Its lesson routine has students name the evidence first, then make a bounded inference, and replaces feedback that says only 'use the source' with a diagnostic of what was missing.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (219-225): “The instructional sequence therefore moves from source evidence to historical use: 1. What exactly is visible or stated? 2. What bounded claim does that evidence support? 3. What outside knowledge is needed to interpret it? 4. How does creator, audience, purpose, or situation affect its use? 5. What remains unresolved and requires corroboration?”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (227-228): “That sequence protects against two opposite errors: treating a source as transparent truth, and dismissing it as "biased" without extracting any evidence.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (391-394): “The lesson routine requires students to name the visible or stated evidence first. They then make a bounded inference and identify what requires corroboration. Feedback that merely says "use the source" is replaced with a diagnostic: missing evidence identification, unsupported inference, or irrelevant sourcing claim.”

Against: It is a declared design in a document since marked historical, and no outcome was measured.

<sub>criterion · sequence, stimulus, feedback · domain · from ap · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Space practice and mix in old items

Revisit each skill at growing intervals on a schedule and mix earlier skills into later practice, so learners must tell which skill an item calls for.

A pedagogy framework behind one project's evaluators makes spaced practice a step on its path to mastery, revisiting key skills 'after a day, a few days, a week, and beyond', and lists cumulative reinforcement among the attributes of a good question: later questions revisit earlier concepts 'to test retention and fluency' (`icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md`). It was adopted without a measurement in the project. Mixed, spaced practice checks what was kept, not only first success.

Quoted:

- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (99): “Students revisit key skills at increasing intervals \- after a day, a few days, a week, and beyond.”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (272): “Later questions intentionally revisit earlier concepts to test retention and fluency.”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/WHY_V2_WINS.md` (44): “so the student must *discriminate* schemas, not pattern-match one per lesson”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/KB_FURTHER_IMPROVEMENTS.md` (75): “Spaced review is a single static pass, not a schedule (#11).”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/KB_FURTHER_IMPROVEMENTS.md` (75): “kb-0027 names this as cramming, not distributed practice”
- `grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd` (35): “Distribute practice over time. Cramming creates temporary performance.”
- `grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd` (36): “Mix problem types to prevent context-dependency.”
- `grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md` (48): “MAP **0/313** → no RIT, no "proven growth."”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/v0.2.md` (37): “MAP Science at G7 tests all four MS NGSS domains back-to-back without warning.”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md` (832): “The child identifies which procedure to use AND completes all the steps independently.”

Against: The effect is unmeasured here: there was no outside test result for the cohort (0 of 313), so no growth is claimed (`grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md`).

<sub>criterion · sequence, practice, evidence-of-learning · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Stage a high mastery bar

Bring in a high mastery bar in stages, advisory at first and blocking later, because a flat high bar from the start can leave most learners no way in. Only about 17% of one cohort cleared a 90% bar.

Under the existing course's design only about 17% of students cleared a 90% mastery bar (`grade3-reading/artifacts/wiki-research/cross-cutting.md`). The approved plan for a new course therefore makes the first band's gates advisory and starts blocking 90% gates in the second band, because a flat wall at the start has no path for the other 83% (`grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md`).

Quoted:

- `grade3-reading/artifacts/wiki-research/cross-cutting.md` (147): “- **Only ~17% of students clear a 90% mastery bar** under the incumbent design (page 2). Our”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (271): “Band A gates are advisory (no hard wall on the on-ramp).”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (273): “a flat wall on the on-ramp has no path for the other 83%.”
- `grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md` (47): “Three difficulty bands (not five stages); staged 90% gates (not flat-90%) — only ~17% of cohort clears 90% today, so a flat wall has no on-ramp.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-1/brainlifts/amalgamation-v2-published-2026-07-02.md` (57): “Band A gates are advisory (no hard wall on the on-ramp). Blocking ≥90% gates begin in Band B, where each schema's enforced mastery checkpoint also lives. Final 90% gate is the course-end mastery test.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-1/brainlifts/amalgamation-v2-published-2026-07-02.md` (59): “today only ~17% of the cohort clears 90% on any equivalent instrument; a flat wall on the on-ramp has no path for the other 83%.”
- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/PEDAGOGY.md` (163-164): “gate-free BUILD opener where the domain is cold (you cannot fail your first encounter with a new world)”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/SEQUENCING-BRIEF.md` (113): “**Cold units (gate-free knowledge-build L1; gates start L2):**”
- `g9/library/text/L612555.txt` (346): “So you have we had cases of kids at alpha who were uh you know very young kids who were just going oh you failed that unit um you need to hit the mastery target again and they were just in this doom loop of doing it over and over again.”
- `incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (203): “### SPOV6 — Staged mastery gates with an on-ramp, not a flat 90% wall”

Against: The staging answers the 17% figure; nothing here measured whether a staged bar lets more students through. The sources give that measured share as the reason; none of them reports staged gates raising learning.

<sub>criterion · sequence, practice · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Start easy, then raise difficulty in steps

Open a course with material students can handle and raise its difficulty in steps. One course ramps through three bands of reading level, starting at 400 to 460 on a reading-level scale.

At a team sync on the reading course, its opening was found too hard, and the decision was to start easier and calibrate up (`grade3-reading/knowledge_bot/knowledge/kb-0057-incept-team-sync-2-2026-06-18.qmd`). The course structure ramps band by band: a hook band at 400-460L, a bridge band at 480-540L and a transfer band at 560-600L (`grade3-reading/knowledge_bot/knowledge/kb-0014-course-structure-manifest.qmd`).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0057-incept-team-sync-2-2026-06-18.qmd` (45-46): “**Lexile start too hard** — course opens on "vertebrates and invertebrates"; start easier and calibrate up.”
- `grade3-reading/knowledge_bot/knowledge/kb-0014-course-structure-manifest.qmd` (33): “**A · Hook (400-460L)** → **B · Bridge (480-540L)** → **C · Transfer (560-600L)**.”

Against: none found

<sub>criterion · sequence, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Structured talk, then a synthesis alone

Structure discussion: give thinking or writing time before calling on anyone, prefer a scripted argue-both-sides sequence to open debate, and have each student produce the final synthesis alone.

Research for the Grade 9 lesson ideas found the strongest causal evidence on participation in a longitudinal study of cold-calling, where comfort participating rose in high-cold-call classes and was unchanged in low ones (Dallimore, Hertenstein & Platt 2013), and guidance for remote classes converging on think or write time before calling on anyone and tracking who has been called against the roster (`grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd`). A synthesis of structured academic controversy, where students research a side, present it, argue the opposite side, drop advocacy and synthesize to consensus, found higher achievement and more higher-level reasoning than debate or individual work (Johnson & Johnson 2009) (the same file). A systematic review and a field study of over-reliance on AI dialogue found reduced engagement and worse unaided performance, which the file reads as an argument for a synthesis turn the student produces alone (the same file).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd` (124-125): “(1) think/write time before calling on anyone; (2) track who's been called against the roster”
- `grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd` (122): “comfort participating rose in high-cold-call classes, unchanged in low-cold-call classes”
- `grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd` (263): “**4. Structured, scripted argument beats open debate; open debate beats none.**”
- `grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd` (265-266): “research a side, present it, argue the opposite side, drop advocacy, synthesize to consensus”
- `grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd` (320-322): “A 2024 systematic review found over-reliance on AI dialogue systems associated with reduced engagement and weaker independent learning”
- `grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd` (324-325): “both argue for a mandatory "you-do" synthesis turn the student alone produces.”
- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/idea-01-pandemic-shakespeare-teaching.md` (102-103): “**Structured cold-calling measurably raises voluntary participation over time — the strongest causal evidence here, though not from a remote or teen setting.**”
- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/idea-01-pandemic-shakespeare-teaching.md` (106): “**comfort participating rose in high-cold-call classes, unchanged in low-cold-call classes**”
- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/IDEA-SYNTHESIS.md` (18): “**structured cold-calling** over open floor”
- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/idea-01-pandemic-shakespeare-teaching.md` (109): “(3) "raise hand" as default queue”
- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/IDEA-SYNTHESIS.md` (17): “| Live debate | **Structured Academic Controversy** (argue a side, switch sides, drop advocacy, synthesise) beats open debate, and fits the spec's evaluative close questions.”

Published: [Dallimore, Hertenstein & Platt 2013](https://journals.sagepub.com/doi/abs/10.1177/1052562912446067) · [Johnson & Johnson 2009](https://doi.org/10.3102/0013189x08330540) · [Over-reliance on AI dialogue systems, systematic review 2024](https://link.springer.com/article/10.1186/s40561-024-00316-7) · [Student-ChatGPT field study 2025](https://arxiv.org/abs/2508.20244)

Against: The cold-calling effect is quasi-experimental and comes from adult students, not remote ones, and the remote adaptations are practitioner guidance; the controversy synthesis covers its authors' own program, strong within it and less independently replicated outside it; and neither over-reliance study tests multi-agent debate, so the synthesis-alone turn rests on an inferred risk (`grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd`).

<sub>criterion · format, practice · universal · from g9, research · external-research · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Summarise each chunk by fixed steps

Teach summarising as a fixed routine for each chunk: mark the key who or what, keep what matters, write one new short sentence, and check it against the marks. A narrative version retells one to two paragraphs at a time with a Somebody-Wanted-But-So-Then frame.

A reading course's review standard, drawing on IES videos on a gist routine and on summarising narrative texts in third grade, makes summarising a modelled routine with fixed steps, retold chunk by chunk and not only at the end (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D3-reading-architecture.md`, line 22). The expository version marks the most important who or what, keeps the important information and drops the rest, puts it into a new short sentence rather than a reworded paragraph, and checks that sentence against the marks. Without the steps a learner tends to copy one sentence or reword the whole paragraph, and a chunk whose gist can't be said signals a breakdown (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/gist-summarizing-routine.md`).

Quoted:

- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D3-reading-architecture.md` (22): “Summarizing is a modeled routine with fixed steps (mark who/what → keep-important/discard-unnecessary → synthesize in own words, not a reworded paragraph → check against the marks; or a 'Somebody-Wanted-But-So-Then' frame), retold per chunk not only at the end”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/gist-summarizing-routine.md` (7): “it into your own words (a new short sentence, not a reworded paragraph)”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/gist-summarizing-routine.md` (7): “retold one to two paragraphs at a time”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/gist-summarizing-routine.md` (10): “a child who copies a sentence verbatim (no comprehension) or one who rewords the whole paragraph (no compression)”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/gist-summarizing-routine.md` (10): “if you can't produce the gist of the chunk you just read, that is the breakdown signal”

Published: [Gist Routine (PRISMS), IES video](https://www.youtube.com/watch?v=L9qcScOP4J4) · [Teaching Summarizing with Narrative Texts in Third Grade, REL West video](https://www.youtube.com/watch?v=Sem09tfYL2E)

Against: none found

<sub>criterion · practice, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Syllables, word parts, definition, then example

Teach a new multi-syllable word in a fixed order: hear it in syllables, break it into meaningful parts where it has them, give its definition, then an example.

A ruling for a Grade 3 reading course extended an earlier rule that put syllables before word parts into a fixed four-step sequence for every taught word: syllable highlighting so the child hears how the word is spoken, then the word-part breakdown that unlocks meaning, then the definition, then an example. Syllables are spoken parts and word parts are meaningful elements, so the split into word parts is a separate, later move, taught as a strategy for deriving meaning only where a word breaks into meaningful parts. It is a course ruling, and no outcome was measured.

Quoted:

- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (415-417): “the full instruction sequence for a vocabulary word is syllable highlighting (hear how the word is spoken) → morpheme breakdown (unlock meaning) → definition → example, in that order”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (417-418): “this confirms and extends R-VOC-14a (which already ordered syllables before morphemes) by fixing the full four-step sequence”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (409): “the morpheme split is a separate, later move.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (409-410): “"Morphemes are meaningful elements, syllables are spoken parts" — the two must never be conflated on one tile.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (400-401): “where a word breaks into meaningful parts, teach the split as a strategy for deriving meaning”

Against: none found

<sub>criterion · sequence, wording · domain · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Teach a claim a question can check

Instruction must contain at least one concrete claim from which a check question with a definite answer and plausible wrong options can be written; otherwise no retrieval can follow it. To pass, at least one question must be writable with a definite answer and at least 2 plausible wrong options.

The video-script check fails a script so vague, hedged or opinion-based that no single unambiguous multiple-choice question can be derived from it (`shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt`). To pass, at least one question must be writable with a definite correct answer and at least 2 plausible wrong options. The rubric justifies the check by the testing effect, citing Roediger & Butler 2011 by author and year only: retrieval right after instruction, it says, turns short-term exposure into durable memory.

Quoted:

- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (431): “The CFU is the primary encoding event — retrieval immediately after instruction is what converts short-term exposure to durable memory (testing effect; Roediger & Butler, 2011).”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (440): “**Fail:** The script is so vague, so hedged, or so opinion-based that no single unambiguous MCQ can be derived from it.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (436): “- A definite correct answer (not "it depends" or "both could be right")”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (437): “- At least 2 plausible but wrong distractors”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (433): “**This is a low bar.**”

Published: [Roediger & Butler 2011](https://doi.org/10.1016/j.tics.2010.09.003)

Against: Deliberately lenient: '**This is a low bar.**' (`shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt`, line 433).

<sub>criterion · practice, alignment · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Teach a procedure once, then recall it

Teach a procedure in full once, and open each later lesson that uses it by recalling it rather than teaching it again from zero.

A review of a Grade 3 reading course objected that a skill already taught several times was being introduced again in detail. The ruling keeps each procedure's first teaching as the one full teach and has every later lesson open on recall of the procedure rather than re-defining it. It is a course ruling, and no outcome was measured.

Quoted:

- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (192-193): “A skill or tool page after its procedure's first teaching opens on recall, not re-teaching from zero.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (193-194): “infer has already been taught multiple times. We don't need to introduce the infer skill in so much detail.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (195-196): “stay untouched as the one full teach; every later lesson recalls the procedure rather than re-defining it”

Against: none found

<sub>criterion · sequence, practice · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Teach a step before an example uses it

Teach every new step before a worked example uses it, because a worked example should put together only what is already known.

A candidate BrainLift of the reading team on gradual release holds that worked examples assemble the known, so a novel step must be taught before it appears inside one (`grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md`). The audit of the team's BrainLifts records it as borrowed from a general instruction framework and from a finding in a second round of review.

Quoted:

- `grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md` (54): “Worked examples assemble the known — a novel step must be taught before it appears inside one.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v2/authoring/prompts/README.md` (53): “The reader must never meet a structure mid-lesson that was never named.”

Against: It is a borrowed rule; nothing in these sources measures it.

<sub>criterion · sequence, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Teach and test the same thinking

Model, practise and test the same thinking step, so every skill a gate tests has been practised before the gate.

A second round of findings on a reading course found the modelled step revealing the answer instead of the thinking, the guided step reduced to a hint, and the independent step sometimes switching to a different skill; one main-idea lesson served an inference item. The adopted rule keeps instruction, practice and assessment on the same cognitive operation, and the reading store's evaluator gap analysis counts coverage as false when an "analyze" standard is assessed by an "identify" item. Label each item with the skill it actually asks for.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (60): “I-do reveals the answer instead of modeling thought; we-do is only a hint; you-do sometimes switches to a different skill.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (92): “a main-idea lesson served an inference/evidence item.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (132): “Preserve coherence across instruction, practice, and assessment; do not teach one cognitive operation and assess another.”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (122): “Coverage is false if an "analyze" standard is assessed by "identify."”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (61): “Assessment format is not instruction format (the marathon rule)”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/FEEDBACK_RESPONSE.md` (167): “layer has **zero main-idea (KCT1) drill and zero inference (KCT5) drill**”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/FEEDBACK_RESPONSE.md` (168): “So a student practicing in this layer gets no repeated main-idea or”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CASE-FOR-PLAN-REVIEW.md inside it) (46): “An item cannot count as course evidence unless the demanded knowledge and move were taught.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (61-62): “If any link is absent, a generated question may still look plausible while the course fails to teach what the question demands.”

Against: the same store holds that assessment format is not instruction format, so the form of a task may differ while the thinking step may not.

<sub>criterion · alignment, demand, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Teach confusable pairs explicitly

Teach confusable ideas as a pair: start with clear-cut examples that tell them apart, keep borderline cases for later, contrast them explicitly, and mix them only once both are learned. One reading course's knowledge graph had 1 confusable link among 47 components.

The reading project's alignment plan types discriminations as gateway hard prerequisites and records that they are chronically under-modelled: its Grade 5 graph had 1 confusable edge among 47 knowledge components (`grade3-reading/ti-courseplans/docs/academics-alignment-plan.md`). The generic instruction BrainLift says students don't reliably discover discriminations alone, so the contrast is taught explicitly with near-miss pairs (`grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md`), and the curriculum BrainLift says the graph should encode confusable pairs, since interleaving after both are learned builds discrimination (`grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md`). Record each pair, choose those first examples so the confusion doesn't form, and teach the contrast side by side (`grade3-reading/knowledge_bot/knowledge/kb-0116-graph-architecture-brainlift-core.qmd`).

Quoted:

- `grade3-reading/ti-courseplans/docs/academics-alignment-plan.md` (24-25): “Discriminations are gateway hard prerequisites and chronically under-modelled (G5 graph: 1 confusable edge / 47 KCs).”
- `grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md` (1286): “interleaving after both are learned builds discrimination”
- `grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md` (57): “Students don't reliably discover discriminations alone.”
- `grade3-reading/knowledge_bot/knowledge/kb-0116-graph-architecture-brainlift-core.qmd` (80): “where example selection can prevent confusion from forming, and scheduling decisions, where interleaving after both are learned builds discrimination”
- `grade3-reading/knowledge_bot/knowledge/kb-0119-curriculum-architecture-brainlift-evidence.qmd` (240): “Novices may need initial blocked exposure before productive interleaving.”
- `grade3-reading/knowledge_bot/knowledge/kb-0119-curriculum-architecture-brainlift-evidence.qmd` (242): “but only after students have enough initial understanding to make the contrast meaningful.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (160): “Interleaving is only appropriate after the skill is ready; massed/blocked first, interleaved later.”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/g3-course-graph.qmd` (42): “**Gateway discriminations** (taught explicitly, interleaved after both learned): narrator vs author; main idea vs supporting detail; fact vs author's claim/opinion”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/g3-course-graph.qmd` (15): “near-neighbor discriminations driving example selection”
- `grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd` (36): “Mix problem types to prevent context-dependency.”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/g3-course-graph.qmd` (1): “G3 Reading Course Graph v1.0 (2026-07-13). DRAFT pending academics ruling.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx` (330 (textutil text)): “Distinguish related quantities explicitly: Force/energy, velocity/acceleration, weight/mass, current/voltage, momentum/impulse — each pair explicitly distinguished when both have been introduced.”
- `downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx` (sheet 'Standard components', cell D39): “Distinguish between a character's temporary feelings and stable traits”
- `downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx` (sheet 'Standard components', cell E39): “Confuses state and trait.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 2. Should We Save the Rainforests - WEIGH - Lesson Design.docx` (221 (textutil text)): “each sentence sorted as OPINION carries a feeling-word ("I feel," "amazes me," "I am worried," "I believe"). No borderline cases are used at first exposure.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 8. Whose World Is It - WEIGH - Lesson Design.docx` (217 (textutil text)): “No borderline cases are used in the modelled step.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (652-654): “Worse, R-VOC-2: tempt and resist are near-inverses of each other and either one is hard to define without the other, so they should be taught together, in the lesson that needs both.”
- `incept-package-hub/course-packages/courses/g5-reading/review/evidence/course-graph-guide.md` (92): “Time order and causation share signals but make different claims; juxtaposition builds discrimination.”
- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L5-2026-09-05.md` (214-215): “"which show what Peter is like, rather than how he felt for a moment" — tests the trait-vs-mood distinction directly with per-option reasoning”

Published: [Rohrer 2012](https://doi.org/10.1007/s10648-012-9201-3)

Against: Interleaving helps mainly where telling the two apart is part of the learning problem (`grade3-reading/knowledge_bot/knowledge/kb-0119-curriculum-architecture-brainlift-evidence.qmd`). The course graph is a draft awaiting academic review (`grade3-reading/knowledge_bot/skills/reading-science/applied/g3-course-graph.qmd`).

<sub>criterion · sequence, practice · universal · from g3, research · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Teach dramatic irony through a line

Teach dramatic irony through a line the audience hears and the deceived character does not, keeping what the audience knows apart from what each character knows.

The handover's opening introduces the audience's knowledge of the deceiver's lies while keeping apart what the audience knows and what the hero knows, and its fifth scene sets the deceiver's private line against his public name before defining the term, with a factual check after. A later review asked for the definition to come with an example, and the film added a step between the quote and the definition saying the hero never hears the line while the audience does. The recorded script makes the same move in speech just before it defines the term.

Quoted:

- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (117): “It introduces the audience’s knowledge of Iago’s deceit while preserving the distinction between what the audience knows and what Othello knows.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (128): “5. What Iago says. Contrast “I am not what I am” with “Honest Iago” and define dramatic irony. A factual check follows.”
- `g9/film/v07/README.md` (12): “Define with an example: we hear "I am not what I am", Othello does not”
- `g9/film/v07/README.md` (12): “a step between the quote and the definition: "Othello never hears it · We do"”
- `g9/script/v04/Othello-Opening-Recording-Manifest.json` (70): “Othello never hears this. We do. That is dramatic irony: the audience knows something a character doesn’t.”

Against: none found

<sub>criterion · wording, sequence · domain · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Teach it right the first time

Teach a concept correctly when it first comes up, never skipping it as obvious, and at once state its key constraint and what it is not, with a counterexample.

The science misconception cards rate first introductions as the riskiest points: in the gap before particles are explained, students build macroscopic mental models that become the default, and the highest risk for bonding is the moment it is first taught. Their synthesis asks for conservation to be stated together with the concept it governs, and for negative definitions, things students must be told are not true, to be taught explicitly; the chemistry card found no standards framework that gives the one for particles, and the science review workbook adds it as required at Grade 3. The biology card pairs its negative definition with a counterexample, and the physics card forbids skipping a law of motion because it seems obvious, since it is the one everyday experience contradicts most.

Quoted:

- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx` (76 (textutil text)): “During this gap, students build macroscopic mental models that become the default.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx` (199 (textutil text)): “Highest risk: The moment bonding mechanisms are first taught (typically grades 9-10).”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx` (220 (textutil text)): “Conservation: State conservation simultaneously with introducing the concept (energy, mass, charge).”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx` (244 (textutil text)): “Every concept area has things that students need to be told are NOT true. These are as important as the positive definitions.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx` (77 (textutil text)): “The moment particles ARE introduced, if instruction fails to explicitly state that particles do NOT have bulk properties.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx` (77 (textutil text)): “No framework currently includes this "negative definition."”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Science_Curriculum_Review_Workbook.xlsx` (sheet 'G3', cell D3): “[New — D1 Section 2.1 negative definition; required at Grade 3]”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx` (210 (textutil text)): “Provide counterexamples: "Polydactyly (extra fingers) is dominant over five fingers.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx` (105 (textutil text)): “Do NOT skip the first law because it "seems obvious." It is the LEAST obvious law and the one most contradicted by everyday experience.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-generation-v0.1.md` (65): “a true, positively-stated contrast that draws the concept's edge ("a cell is alive; an atom is a smaller, non-living piece")”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-generation-v0.1.md` (65): “It is NOT a negation of the student misconception and NOT a "what X is NOT" line.”
- `grade3-reading/course-renderer/docs/pedagogy/misconceptions/cross-cutting-synthesis.md` (106): “The key cross-cutting insight: energy conservation must be taught at the SAME TIME energy is introduced (as the Franklin Standards do at grade 3), not as a later addition.”

Against: none found

<sub>criterion · sequence, integrity, wording · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Teach parts in dependency order

Teach the parts of a complex performance in the order they depend on each other, not exam order, so every rubric row is taught before a full task scores it. One history course teaches six part-skills before its first complete essay, from a bounded claim with accurate evidence to qualification and corroboration.

An AP history course orders its writing progression by cognitive dependency rather than exam order: a bounded claim with accurate evidence, then evidence relevance, reasoning chains, context, source value and qualification, before the complete essays and timed mixed practice. The stated aim is that every rubric row has a taught history, so a student who misses one can be routed to the responsible knowledge or reasoning function instead of reteaching the whole essay. The functions are taught separately and then combined, each kept tied to historical content.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (630): “The writing sequence follows cognitive dependency rather than exam order:”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (632-638): “1. bounded claim and accurate evidence; 2. explanation of evidence relevance; 3. comparison, causation, and continuity/change chains; 4. context linked to the target development; 5. source value and limitation for a precise claim; 6. qualification and corroboration; 7. complete LEQ;”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (642): “This progression ensures that a rubric row has a taught history.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (643-644): “route to the responsible knowledge or reasoning function instead of reteaching the entire essay.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (234-235): “The course teaches those functions separately and then combines them. Each step remains connected to historical content: a strong sentence frame without accurate evidence is still empty.”

Against: none found

<sub>criterion · sequence, alignment, scoring-guide · universal · from ap · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Teach revision, not just prompts to write

Teach writing through explicit, form-focused revision, such as worked revisions of a weak answer into a full-marks one against named criteria, rather than by prompting students to write. In a writing meta-analysis, sentence combining, a structured form-focused revision, showed an effect size of 0.75.

A grade 4-5 writing module's evidence base takes from a writing meta-analysis that sentence combining, a structured form-focused revision, had a discrete effect of d = 0.75, and reads it as explicit, form-focused revision beating general 'revise it' feedback. Its BrainLift holds that prompting a child to write is elicitation, not instruction, and makes revision the taught layer: worked examples of a 0-point response becoming a 2-point one, named against rubric criteria and gradually released. Its generation contract ships that layer with the written-response bank, never elicitation without instruction, a rejection lesson from an earlier reading build.

Quoted:

- `grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/sources/EVIDENCE-BASE.md` (22): “**Sentence-combining d = 0.75** (structured form-focused revision — a discrete reported ES).”
- `grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/sources/EVIDENCE-BASE.md` (24-25): “Interpretation: explicit, form-focused revision beats general "revise it" feedback — argues for *worked 0→1→2-point revision examples*, not open prompts.”
- `grade3-reading/ti-courseplans/courses/g4g5-writing/brainlifts/v0.1.md` (35): “Prompting a child to write is elicitation, not instruction.”
- `grade3-reading/ti-courseplans/courses/g4g5-writing/brainlifts/v0.1.md` (35): “worked examples of a 0-point response becoming a 2-point response, named against rubric criteria, gradually released”
- `grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/sources/GENERATION-CONTRACT.md` (87-88): “The revision teaching layer (`WAR-I2`) ships in step with the SCR bank — never elicitation without instruction (G3's whole verdict).”

Published: [Writing Next: Effective Strategies to Improve Writing of Adolescents in Middle and High Schools (Carnegie Corporation of New York and Alliance for Excellent Education, 2007)](https://carnegie.org/publication/writing-next-effective-strategies-to-improve-writing-of-adolescents-in-middle-and-high-schools/)

Against: The strategy-instruction effect of about 0.50 is only a cluster estimate, not a single reported effect (`grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/sources/EVIDENCE-BASE.md`, lines 20-21), and the contrast with general 'revise it' feedback is the module's reading of the meta-analysis, not a reported comparison.

<sub>criterion · practice, feedback, format · universal · from g3, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Teach strategies briefly, then build knowledge

Teach comprehension strategies briefly and explicitly, inside the content they serve, and spend the rest of the time building knowledge through coherent sets of related texts. Across eight quantitative reviews, about 10 strategy sessions gave the same comprehension benefit as about 50.

The reading course's synthesis of five primary sources, every quote in it checked by script against the full texts, reports that across eight quantitative reviews more practice with a comprehension strategy gave no added benefit, ten sessions yielding the same as fifty, and that its authors concluded strategy instruction should be explicit and brief (`grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd`, lines 1-7 and 45-48). A research report it draws on adds that unless strategies are closely linked with knowledge in a content area, students are unlikely to learn them fully (the same file, lines 55-58).

Quoted:

- `grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md` (134-135): “Across eight quantitative reviews, ~10 strategy-instruction sessions produce the same comprehension benefit as ~50 — no dose-response”
- `grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd` (48): “RCS instruction should be explicit and brief.”
- `grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd` (55-57): “"Unless the strategies are closely linked with knowledge and understanding in a content area, students are unlikely to learn the strategies fully”
- `grade3-reading/knowledge_bot/knowledge/kb-0110-can-reading-comprehension-be-taught.qmd` (45): “Ten sessions yield the same benefit as fifty sessions. The implication seems obvious; RCS instruction should be explicit and brief.”
- `grade3-reading/knowledge_bot/knowledge/kb-0110-can-reading-comprehension-be-taught.qmd` (47): “strategy instruction may have an upper limit, but building background knowledge does not”
- `grade3-reading/knowledge_bot/knowledge/kb-0104-comprehension-research-agenda.qmd` (80-81): “fosters deeper comprehension development than strategies taught in isolation”
- `grade3-reading/knowledge_bot/knowledge/kb-0104-comprehension-research-agenda.qmd` (82-83): “too-wide content/text range = strategies not fully learned; too-narrow = transfer fails”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (57): “Across eight quantitative reviews, \~10 strategy-instruction sessions produce the same comprehension benefit as \~50 — no dose-response”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (44): “Strategy instruction works but saturates quickly — teach routines briefly and explicitly, then reinvest the time in knowledge and reading”
- `grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd` (529): “"Unless the strategies are closely linked with knowledge and understanding in a content area, students are unlikely to learn the strategies fully, may not perceive the strategies as valuable tools"”
- `grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd` (535): “"If comprehension strategies are taught with an array of content and a range of texts that are too wide, then students will not fully learn them."”
- `grade3-reading/knowledge_bot/skills/reading-science/README.md` (34-36): “What compounds is knowledge: reading conceptually coherent text sets measurably builds topic knowledge, accelerates incidental vocabulary acquisition, and transfers to comprehension of novel related texts”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (55): “Coherent-set readers gained 5.59 vs 2.63 concept idea-units (η²=.32) over six texts in three days”
- `grade3-reading/knowledge_bot/skills/reading-science/sources.qmd` (17): “DOI: 10.1007/s11145-016-9628-x”
- `grade3-reading/knowledge_bot/skills/reading-science/SKILL.md` (40): “N=59, exploratory, comprehension-questions measure null;”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (37): “knowledge transfer is near-domain at best”
- `grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd` (499): “"Explicit instruction generates the immediate use of comprehension strategies, but there is less evidence that students continue to use the strategies in the classroom and outside of school after instruction ends"”
- `ti-courseplans-audit/docs/teaching-reading-comprehension-brainlift.md` (134-135): “Across eight quantitative reviews, ~10 strategy-instruction sessions produce the same comprehension benefit as ~50 — no dose-response (Willingham 2014, p. 2).”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D7-knowledge-first-curriculum.md` (15): “Strategies are a one-time "bag of tricks," taught explicitly then stopped; no strategy-mastery gating (added practice confers no advantage)”
- `ti-courseplans-audit/docs/reading-science/sources.qmd` (17): “Author's copy: http://www.danielwillingham.com/ (TCR commentary)”
- `ti-courseplans-audit/docs/reading-science/SYNTHESIS.qmd` (172): “**Strategies genuinely work**”
- `ti-courseplans-audit/docs/reading-science/SYNTHESIS.qmd` (175-176): “The claim is *bounded value*, not *no value*.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md` (66): “**One lesson is below the dose that worked.**”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md` (67-69): “main-idea questioning does not transfer; the successful studies taught "explicitly, took place daily for considerable amounts of time, and continued across several weeks."”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md` (60): “**It is an intervention guide, not core instruction.**”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md` (54-55): “Recommendation 3 carries **"a strong level of evidence"**, from 34 studies, 23 meeting WWC standards without reservations.”
- `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd` (535): “If comprehension strategies are taught with an array of content and a range of texts that are too wide, then students will not fully learn them.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/BRAINLIFT.md inside it) (93-96): “**conceptual coherence** ("repetition, elaboration, and examples provided across the texts," not merely sharing a topic) produced a large knowledge gain”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (137): “- Direct, explicit comprehension-strategy instruction: strong.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (70): “the 4-step INFER frame is walked exactly once (p17 skill-steps, p18 infer-steps, both 'walk:true') then immediately used on story content across I-do/we-do/you-do, never re-drilled as an abstract skill.”

Published: [Willingham & Lovette 2014](http://www.danielwillingham.com/) · [RAND Reading Study Group 2002](https://www.rand.org/pubs/monograph_reports/MR1465.html) · [Willingham & Lovette 2014](http://www.danielwillingham.com/uploads/5/0/0/7/5007325/willingham&lovette_2014_can_reading_comprehension_be_taught_.pdf) · [Conceptual coherence, comprehension, and vocabulary acquisition: A knowledge effect? Reading and Writing 29 (2016)](https://doi.org/10.1007/s11145-016-9628-x)

Against: The same synthesis holds that strategies genuinely work and that the claim is bounded value, not no value (`grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd`, lines 172-176). The same synthesis warns that too wide a range of content and texts leaves strategies not fully learned, and too narrow a range makes transfer fail. The study was small and exploratory (N=59), its comprehension-questions measure was null, and knowledge transfer was near-domain at best (η²=.09) (`grade3-reading/knowledge_bot/skills/reading-science/SKILL.md`, `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd`). Explicit strategy instruction produces immediate use, but there is less evidence that students keep using the strategies after instruction ends (`grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd`). Strategies do work: the reading-science synthesis calls the claim bounded value, not no value (`ti-courseplans-audit/docs/reading-science/SYNTHESIS.qmd`).

<sub>criterion · sequence, alignment · universal · from g3, research · external-research · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Teach the general case first

Teach the general case before a restricted one, because splitting off the restricted case and teaching it first builds a rule that later has to be undone.

The curriculum BrainLift in the reading project's course plans names wrong atom boundaries as one way a curriculum graph goes wrong: splitting a restricted case from a general case, such as same-denominator before unlike-denominator fractions, makes students build predictive models that become entrenched and must be actively undone (`grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md`). Its prescription is to teach the most general case first and use carefully chosen examples to prevent induction of restricted rules.

Quoted:

- `grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md` (36): “Splitting a restricted case from a general case (e.g., same-denominator before unlike-denominator fractions) causes students to build predictive models that become entrenched and must be actively undone.”
- `grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md` (1262): “teach the most general case first, use carefully chosen examples to prevent induction of restricted rules.”

Against: none found

<sub>criterion · sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Test a reading against the next passage

Have students commit to one of two plausible explanations, predict what the next passage will show, then read it and revise their account.

An advanced-learning resource written for the Grade 9 unit proposes that students construct competing explanations, predict what each would imply, then confront new evidence that may undermine their preferred reading, with teaching that shows how to tell apart explanations that both sound convincing at first (`g9/transcript/chat-transcript.redacted.txt`, line 2624). Its worked lesson starts with two plausible explanations of a character's changing trust, requires predictions about the next exchange, reveals the passage and makes students revise their account (line 2630). The resource was endorsed as the basis for the build (line 2705).

Quoted:

- `g9/transcript/chat-transcript.redacted.txt` (2624): “Students construct competing explanations, predict what each would imply, then confront new evidence that may undermine their preferred reading.”
- `g9/transcript/chat-transcript.redacted.txt` (2630): “start with two plausible explanations of his changing trust, require predictions about the next exchange, reveal the passage, and make students revise their account.”

Against: It is untested with students, and the resource says the new evidence "may" undermine the preferred reading, so a revision follows only where the reading fails (`g9/transcript/chat-transcript.redacted.txt`, line 2624).

<sub>criterion · demand, sequence · universal · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### The conclusion comes out of the quotes

In a modelled reading, the conclusion must emerge from the quoted lines step by step and follow from them, never be reached first and decorated with quotes.

A reading course's judge for modelled reasoning fails a think-aloud whose narration reaches its conclusion before engaging the quoted lines, so the quotes decorate a conclusion reached elsewhere, and a write-up whose conclusion does not follow from the chosen quote, tested by whether a child granting the quote could still reasonably deny the conclusion. It passes one where a child following the narration would see the answer emerge from the quoted lines, step by step, in the procedure's own order (`grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/judge/model-against-text.md`, lines 6-17). The same judge fails narration that asserts a fact the passage on the page does not contain, and a sentence frame whose 'so' step is a leap the guide never explains.

Quoted:

- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/judge/model-against-text.md` (7-10): “the narration reaches its conclusion BEFORE engaging the quoted lines, so the quotes decorate a conclusion reached elsewhere instead of producing it; - the write-up's conclusion does not follow from the chosen quote (a child granting the quote could still reasonably deny the conclusion);”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/judge/model-against-text.md` (16-17): “Pass when a child following the narration would see the answer EMERGE from the quoted lines, step by step, in the procedure's own order.”

Against: none found

<sub>criterion · demand, evaluation · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Think aloud, then show, then check

When modelling, say what you will do, show it done, then check, putting nothing on screen before it is thought aloud and keeping one target of attention at a time.

Review feedback on one lesson asked for a set choreography for modelling: say what will be done, let it be seen done, then the check, with nothing on screen before it is thought aloud, feedback finished before the next step renders, one target of attention at a time and only the current sentence highlighted. An earlier review found the steps and the question being answered scrolling away during modelling, so the student lost the thread, and asked for both to stay visible with one thing surfacing at a time.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd` (61): “says what he will do, then it is seen done (ideally silently),”
- `grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd` (62-63): “then the check; nothing on screen before it is thought aloud; feedback finishes before the next step renders; one attention target at a time; only the current sentence highlighted.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (84): “scroll away, so the child loses the thread”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (84): “The steps and live question must remain visible, and the model should surface one thing at a time”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (18): “modeling choreography (say → see it done → check, one attention target)”
- `grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd` (61-63): “Scout says what he will do, then it is seen done (ideally silently), then the check; nothing on screen before it is thought aloud; feedback finishes before the next step renders; one attention target at a time; only the current sentence highlighted.”
- `grade3-reading/.claude/skills/lesson-build/SKILL.md` (65-66): “think_aloud candidate quotes: every quote spoken in the narration”
- `grade3-reading/.claude/skills/one-perfect-lesson/SKILL.md` (83): “say → see it done (silently) → check”

Against: none found

<sub>criterion · sequence, media · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Unpack a hard sentence by fixed questions

Teach learners to unpack a hard sentence by fixed questions: who or what, doing what, to whom, and why that word.

A reading course's review standard, citing an IES video on scaffolding emergent reading for dual-language learners, has a hard sentence unpacked by a scripted routine that names its connectives and that-phrases and chunks it physically, rather than only flagging it as hard (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D8-text-quality.md`, lines 26-27). A second IES video, on foundational reading skills, supplies the cohesion devices to teach by name: pronoun referents, connectives, substitution, repetition and ellipsis, nominalisation and deixis. A reader who can decode every word can still lose the thread in one long sentence, and naming each device makes it teachable.

Quoted:

- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D8-text-quality.md` (26): “Troublemaker sentences are unpacked with a scripted routine that names connectives/that-phrases and physically chunks the sentence (who/what → doing → to whom → why that word), not just flagged”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D8-text-quality.md` (27): “Cohesion instruction covers the specific devices — pronoun referents, connectives, substitution, repetition/ellipsis, nominalization ('this question' pointing back), deixis (me/here), analogies”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/sentence-unpacking-and-cohesion.md` (10): “a Grade-3 reader who can decode every word can still drown in one long sentence full of subordinate clauses, connectives, and a "she" three lines back”

Published: [Scaffolding Emergent Reading, Oral Language, & Writing for DLLs/ELs in PreK–Grade 1, REL West video](https://www.youtube.com/watch?v=eIm5PVoAKt0) · [Overview of the Foundational Reading Skills Practice Guide, REL Southeast video](https://www.youtube.com/watch?v=xdGMRJSEjzU)

Against: none found

<sub>criterion · practice, stimulus · universal · from g3, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Weight review toward weak skills

Weight spaced review toward the skills learners are weakest on, giving them at least half of it, interleaved with the rest. One Grade 3 course found its spaced review under-weighted weak skills and reweighted it to at least 50% weak-skill items, interleaved.

A Grade 3 reading course's handoff lists among its verified fixes that spaced review under-weighted weak skills; it was reweighted to at least 50% weak-skill items, interleaved, and an extra lesson on one standard (RI.3.9) was added. The one-shot script that made the change is listed with the same 50% figure. No effect on learning was measured: this is a recorded design fix, not a tested one.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/top-level-docs/HANDOFF_3_KEY_ISSUES.md` (47): “- **Spaced review under-weighted weak skills** → reweighted ≥50% weak-skill, interleaved; extra RI.3.9 lesson added.”
- `grade3-reading/_archive/2026-08-13-consolidation/top-level-docs/HANDOFF_2_EXISTING_MATERIALS.md` (38): “`v2_reweight_spaced.py` (≥50% weak-skill)”

Against: none found

<sub>criterion · sequence, practice · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### What each source gave, before modelling

After the first read and before any modelling, have students say what each source contributed, unscored if need be but never accepting a blank.

An audit of a Grade 5 reading lesson that pairs an article with a diagram found no completion check before the worked example, although the course's design required students to state what the prose contributes, what the diagram contributes and why its dashed connector differs before the model. The audit allowed the check to be unscored but not a no-op. The fix added one typed box per source and one for the visual difference, unscored and unrecorded, and refuses any empty box with a nudge.

Quoted:

- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (125-127): “Canon requires the student to state what the prose contributes, what the diagram contributes, and why the dashed connector differs — before the I-do models the move.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (136): “but must not be a static-recast no-op”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (734-736): “unscored (`complete(...,null)` — no tally) per the I09 pattern, but never a no-op: every box must carry ≥1 word (F7's empty-input rule) or the submit bounces with a nudge”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (782): “"just for you; nothing is recorded or graded"”

Against: The check refuses only empty boxes: "every box must carry ≥1 word (F7's empty-input rule)" (`grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md`, line 735). The model answer shown straight after it states what later steps ask the student to produce, "the article gave you the rule for reading any arrow, the map gave you this kelp forest's actual arrows, and the dashed line is different because it marks a habitat, not a meal" (`grade3-reading/artifacts/u4l2-build/content/u4l2-content.json`, line 311), and a later gate accepts the same content (`grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md`, lines 694-695). That sits against the record dont-spend-a-later-steps-evidence-early.

<sub>criterion · sequence, evidence-of-learning, stimulus · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Write about what was read

Have students write about what they read, since writing about a text raises reading comprehension, most for lower-achieving readers. A meta-analysis found d = 0.40 across 11 studies, and d = 0.63 for lower-achieving students across 12.

A grade 4-5 writing module rests on a meta-analysis that found writing about text raised reading comprehension by d = 0.40 over 11 studies, and by d = 0.63 for lower-achieving students over 12. Its BrainLift therefore treats writing about reading as a comprehension amplifier first and a writing product second, attaching short written responses to the reading lessons' own passages and vocabulary. The module records no outcome for its own students yet.

Quoted:

- `grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/sources/EVIDENCE-BASE.md` (9-10): “Meta-analysis: **writing about text → reading comprehension d = 0.40** (11 studies); **d = 0.63 for lower-achieving students** (12 studies).”
- `grade3-reading/ti-courseplans/courses/g4g5-writing/brainlifts/v0.1.md` (28): “Writing-about-reading is a comprehension amplifier first, a writing product second”

Published: [Writing to Read, Harvard Educational Review 81(4):710-744 (2011)](https://www.harvardeducationalreview.org/content/81/4/710) · [Writing to Read, Carnegie Corporation of New York report (2010)](https://media.carnegie.org/filer_public/9d/e2/9de20604-a055-42da-bc00-77da949b29d7/ccny_report_2010_writing.pdf)

Against: none found

<sub>criterion · practice, format · universal · from g3, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Young learners don't choose what to skip

Don't let young learners skip or speed up instruction on their own judgment, but let them move through each modelled step with a tap rather than on a timer.

A walkthrough of a Grade 3 reading course summed up its points as no child control over pace or skipping, since children are poor judges of what they can skip (`grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md`), and the course removed audio-speed control because children rush (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md`, C2). The same ruling put staged reveals on a tap, never a timer, because a timer cannot pace itself to a slow reader, and a later walkthrough asked for a next button between modelled steps so learners can take each one in before the next.

Quoted:

- `grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md` (58): “- No child control over pace or skipping (children are poor judges of what they can skip).”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (309-310): “the same reasoning that removed audio-speed control, because children rush.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (310-311): “A timer also cannot pace itself to a slow reader. Tap-to-continue satisfies both.”
- `grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md` (390): “between each step have a ‘next’ button so they can pause a moment themselves after each step to take it in before having to listen to the next step.”
- `grade3-reading/ti-courseplans/feedback/feedback1/Direct Instruction BrainLift.md` (19): “**Require students to earn Test Out through repeated mastery on prior lessons**”
- `othello-archive/src/steps/Model.tsx` (9): “Nothing moves on its own: no timers, no typing, no auto-advance.”
- `g9-transformer-audit/2026-10-09-builders.json` (1): “never types its first move, and Next stays locked”
- `g9-transformer-audit/2026-10-09-builders.json` (1): “The animated build's model typing gate is now fixed upstream; the mirror is at 9dc95fb.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/06-AUDIO-NARRATION.md` (22-23): “No user speed control (2026-08-04: kids max the slider) EXCEPT the single "Slower" pill (≈0.85× → ~111 wpm heard)”
- `grade3-reading/artifacts/u4l2-build/METHODS-CHECKLIST.md` (93-95): “Read-to-me playback exposes no control that lets the child rush the sequence faster than an age-appropriate rate (kb-0172 active-screen rule); a slow-down option is permitted”
- `grade3-reading/artifacts/qc-2026-09-30-staging/contradictions.md` (14): “Settled in practice as normal-and-slower, never formally withdrawn.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/06-AUDIO-NARRATION.md` (30-31): “110–120 wpm (R-AUD-3), which ~111 wpm Slower meets and ~131 wpm Normal exceeds — an open tension, not a settled equivalence.”
- `grade3-reading/course-renderer/docs/qa/new-lesson-qa-invariants.md` (135-137): “**E1. Reveal on Next, everywhere, both modes.** Every step, chart row, ladder rung and sub-thought arrives on exactly one Next tap; the voice never reveals or advances.”
- `grade3-reading/course-renderer/docs/rules/pedagogy-and-lesson-structure.md` (382-384): “Acting on the 2026-08-11 review, the build "Added a 'Next' button between steps" and "reduced text on screen" in the modelling moment”
- `grade3-reading/course-renderer/docs/rules/audio-and-voiceover.md` (228-230): “`useStageProgress` in `src/components/lesson/StageNext.tsx`, used by `VocabNode` and `ThinkAloudNode`: a stage is reached by whichever came first, the voice or the tap, and the button hides while `isPlaying`.”
- `grade3-reading/course-renderer/docs/rules/audio-and-voiceover.md` (210-211): “Anything a page reveals as the narration reaches it must also be reachable by the child's own tap.”
- `grade3-reading/course-renderer/docs/rules/pedagogy-and-lesson-structure.md` (381-382): “component sheet has the modelling moment as one continuous block (R-PED-18, 2026-08-06)”
- `grade3-reading/course-renderer/docs/rules/pedagogy-and-lesson-structure.md` (386-388): “One thing at a time (R-UI-4) pushes towards stepping; one continuous block pushes against it. Needs a decision on whether stepping inside one page counts as one block.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (285): “The rule in one line: the child may skip the Modelling Moment, but not step 4.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (303): “Every other lesson. The default once a procedure has been modeled once.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (304): “The child skips straight to step 4, which plays in full.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (87): “Auto-restore fires next time. The choice is removed.”
- `othello-archive/README.md` (86): “Nothing auto-advances. The student makes every move.”
- `othello-archive/scripts/check-stillness.mjs` (3): “Rule: with NO click or key press, no step may (1) move on to another step, (2) change its visible text after it has”
- `othello-archive/scripts/check-stillness.mjs` (5): “Loads every step of every lesson as a student AND as a reviewer, waits for it to settle, then watches it untouched.”
- `othello-archive/scripts/check-stillness.mjs` (7): “the word web's 90 s auto-add”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (294): “Text writes out progressively, with narrated thinking alongside.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/prototype/README.md` (37): “Every screen reveals its parts in order, and the student asks for each one ("Then what happened?", "Show her proof").”
- `othello-course-renderer-draft/repo/docs/design/grade-9/prototype/README.md` (37): “Nothing is on a timer, nothing that has appeared goes away, and Next only appears once everything on the page has been seen.”
- `othello-course-renderer-draft/repo/docs/qa/new-lesson-qa-invariants.md` (135-137): “**E1. Reveal on Next, everywhere, both modes.** Every step, chart row, ladder rung and sub-thought arrives on exactly one Next tap; the voice never reveals or advances.”
- `othello-course-renderer-draft/repo/docs/rules/content-and-copy.md` (287): “**Rule.** Long teaching text arrives in step with the voice, not as a wall.”
- `othello-course-renderer-draft/repo/docs/rules/content-and-copy.md` (289-290): “Reveal each section of text in this vocab section on a timer so it doesn't all appear at once.”
- `othello-course-renderer-draft/repo/docs/rules/audio-and-voiceover.md` (229-230): “a stage is reached by whichever came first, the voice or the tap, and the button hides while `isPlaying`.”
- `othello-course-renderer-draft/repo/docs/rules/audio-and-voiceover.md` (86-89): “a tap on a line is a rewind, never a skip. Only lines the voice has already reached are tappable (`reachedIndex` in `useAudioNarration.ts`), "because a child who can tap ahead can clear a page's gate without hearing the part that teaches it".”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (302): “A modelling moment says which of the seven procedures it is running and shows the step the guide is on, advancing as the voice reaches it.”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (1044): “Anything a page reveals as the narration reaches it must also be reachable by the child's own tap.”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/CODEX-HISTORY-EVERYTHING-OUT.md` (75-76): “Next button between modelling steps; identical step names across I-do/we-do/you-do ("Step 2: HUNT FOR KEYWORDS");”
- `grade3-reading/course-renderer/AGENTS.md` (304-307): “Clicking a line of text is a REWIND, never a skip. Only lines the voice has already reached are tappable (`reachedIndex` in `useAudioNarration`), because a child who can tap ahead can clear a page's gate without hearing the part that teaches it.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (295): “The child was not secure on this procedure last time. The choice is removed.”
- `othello-archive/sources/Year 9 ELA- Lesson Design Specification for Devfactory.txt` (525): “The app decides when and where extra guidance is given.”
- `g9/library/text/L8d5159.txt` (285): “The rule in one line: the child may skip the Modelling Moment, but not step 4.”
- `grade3-reading/artifacts/Peter-Pan-L4-review-response-2026-08-25.pdf` (p.4 (pdftotext lines 169-170)): “the modelling page now advances through states instead of autoplaying one clip over a bare passage.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/06-AUDIO-NARRATION.md` (248-250): “While a line sounds the way-on is held, same rule as every sibling state, so a line can never be skipped”
- `grade3-reading/artifacts/u4l2-build/BEAT-SPEC.md` (93): “is the only clock — no idle watchdog on this branch (it would make the button decorative).”

Against: Skipping can be earned: the course's direct instruction brainlift allows testing out of a lesson only after repeated mastery on earlier ones (`grade3-reading/ti-courseplans/feedback/feedback1/Direct Instruction BrainLift.md`). A later run found: Other parts of the same renderer pull the other way. Its narrated stages are reached by whichever comes first, the voice or the tap, with the button hidden while the voice plays, so with the voice on the narration paces each reveal (`grade3-reading/course-renderer/docs/rules/audio-and-voiceover.md`, lines 208-232). A lesson component sheet of 2026-08-06 has the modelling moment as one continuous block, and the renderer records whether stepping inside one page still counts as one block as awaiting a decision (`grade3-reading/course-renderer/docs/rules/pedagogy-and-lesson-structure.md`, lines 379-388) (`grade3-reading/course-renderer/docs/rules/audio-and-voiceover.md`). A later run found: A Grade 3 reading lesson design lets a child skip the first three modelled steps by default once a procedure has been modelled, removes that choice only when the child was not secure on the procedure last time, and never lets the write-up step be skipped (`g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx`). A later run found: The same younger-grade rules also let the voice pace reveals: long teaching text arrives in step with the voice, after a review asked for a section to be revealed on a timer, and staged pages reach a stage by whichever comes first, the voice or the tap (`othello-course-renderer-draft/repo/docs/rules/content-and-copy.md`). A later run found counter-evidence (`grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt`). A later run found counter-evidence (`g9/library/text/L8d5159.txt`).

<sub>criterion · sequence, accessibility · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### About five turns on one idea

Keep a comprehension exchange on one idea for about five turns, each reply building on the learner's answer rather than only judging it, and measure turns per conversation. One rulebook asks for at least 5 turns on one idea: open question, child, challenge, child, then a recast or extension to close.

A grade-3 reading rulebook's law on the third turn says evaluation-only replies end the conversation and asks for at least five turns on one idea, and a reading quality canon applied in a grade-5 audit gives the shape: open question, child, challenge, child, then a recast or extension to close. The audit's notes trace the structure to a brief on opportunities to respond, which also sorts the second turn by the kind of answer, from a full and correct one to no response.

Quoted:

- `grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md` (23): “Evaluation-only replies end the conversation. Strive-for-Five: ≥5 turns on one idea.”
- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (445): “The conversation follows the Strive-for-Five shape: open question → child → challenge → child → recast/extend close (~5 turns).”
- `grade3-reading/artifacts/u4l2-build/g5-audit/KB-NOTES.md` (135): “Structure: open question → child → scaffolded challenge → child → recast/extend close”
- `grade3-reading/artifacts/u4l2-build/g5-audit/KB-NOTES.md` (136): “**five-branch turn-2 triage**”
- `grade3-reading/artifacts/u4l2-build/g5-audit/KB-NOTES.md` (139): “OTR BrainLift via kb-0175 §2”
- `grade3-reading/course-renderer/docs/pedagogy/otr-brainlift-2026-07-24.md` (84): “A single question and answer is one exchange, not comprehension. Following *Strive-for-Five*, the app should treat about five turns as the shape of a comprehension conversation, which is also what the Speaking and Listening standards ask of young children (for example, “continue a conversation through multiple exchanges,” SL.K.1b and SL.1.1b).”
- `grade3-reading/course-renderer/docs/pedagogy/otr-brainlift-2026-07-24.md` (106): “Measure with three signals, not one: responses per minute, turns per conversation, and how much language the child produces, along with whether the app actually used the child’s answer.”
- `grade3-reading/course-renderer/docs/pedagogy/otr-brainlift-2026-07-24.md` (12): “Written for PreK to Grade 2 and stated as out of scope for "grades 3 and above"”
- `grade3-reading/course-renderer/docs/pedagogy/otr-brainlift-2026-07-24.md` (200): “Choose which measures to operationalize in the app.”

Published: [Cabell & Zucker 2024, Using Strive-for-Five conversations to strengthen language comprehension in preschool through Grade One, The Reading Teacher](https://doi.org/10.1002/trtr.2266)

Against: Its source covers only the earliest grades: "written for K–2; use as design principle for G5, not age authority." (`grade3-reading/artifacts/u4l2-build/g5-audit/KB-NOTES.md`, lines 140-141). The grade-3 rulebook also rules that full credit carries no further ask, "A passed answer never renders "Make it even stronger" / "One more thing" / "Try this"." (`grade3-reading/artifacts/judgment-corpus/distilled-src/01-NON-NEGOTIABLES.md`, lines 32-33), which a challenge after a passed answer would break. The synthesis was "Written for PreK to Grade 2 and stated as out of scope for "grades 3 and above"" (`grade3-reading/course-renderer/docs/pedagogy/otr-brainlift-2026-07-24.md`, line 12), and which measures to build is left open: "Choose which measures to operationalize in the app." (line 200).

<sub>criterion · practice, feedback, format · domain · from g3, research · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Don't ask for the same production twice

Don't ask young learners for the same production twice in one word activity, aloud and then typed; let writing happen once, where it must carry evidence and meaning. One course built a written turn for all 46 taught words and withdrew it the same day.

A Grade 3 reading build added the written vocabulary turn a review asked for, one beat for each of the 46 taught words, gated at 199 assertions, and removed it the same day on the ruling that a word turn should not ask for the same production twice, aloud and typed. The build's BrainLift argues that the repeat spends the child's most expensive minutes on redundancy, since the lesson's typed production already exists in the independent task, where it must carry evidence and meaning, so the vocabulary ladder is hear, then say. The content stays authored, voiced and dormant, held by two gates, so reinstating it is a player change.

Quoted:

- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/BRAINLIFT.md` (102-103): “wired for all 46 words, gated at 199 assertions, and removed it the same day.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/BRAINLIFT.md` (105): “same production aloud and then typed spends the child's most expensive minutes on redundancy”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/CASE-FOR-APPROVAL.md` (233): “same production twice, aloud and typed.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/CASE-FOR-APPROVAL.md` (234): “The content is authored, voiced and dormant, held by two gates.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/CASE-FOR-APPROVAL.md` (235): “reinstating it is a player change, not a content project.”

Against: The review that prompted the turn asked for both: "Have them say the word back, write the word in a sentence," (`grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/FEEDBACK-RESPONSES.md`, line 91), and the build's approval case still lists that ask as decided, not closed.

<sub>criterion · practice, format · domain · from g3 · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Hold the check until the text is read

Hold the question until a learner reading alone could plausibly have read the text, timed from its word count at a generous reading rate for their age. One review got past a non-blocking reading nudge by clicking Next twice.

A content review of a Grade 3 reading build found that timers on the text could still be clicked through, that a non-blocking reminder to read was skipped by clicking Next twice, and that a main-idea pass could be earned with every answer wrong. Matching a reference player, the reading engine now withholds Next on its book pages until the longer of 4 seconds and the time its words take at 150 words a minute has passed when the learner reads alone, or until the narration ends when the page is read aloud, with the dwell kept as a backstop. The hold is a floor, not a pace: once it has passed, the learner moves on with Next.

Quoted:

- `grade3-reading/course-renderer/docs/feedback/g3-parity-audit.md` (41): “Self-read dwell door: `max(4s, words/150wpm)` before the check | yes | **BUILT** — book-layout pages withhold Next until the dwell elapses (self-read) or the narration completes (read-to-me, dwell as an untrappable backstop)”
- `grade3-reading/course-renderer/docs/feedback/academics-review-2026-07-08.md` (31): “Whilst there were timers on text reading before the question appeared, it still seems possible to just click through, and where a "not so fast — read, read" nudge appeared it was non-blocking and skipped by clicking Next twice.”
- `grade3-reading/course-renderer/docs/feedback/academics-review-2026-07-08.md` (36): “The read-gate is bypassed by clicking Next a second time (the "not so fast — read" step is skipped), and in a main-idea task we earned the pass while answering every question incorrectly.”
- `grade3-reading/artifacts/u4l2-build/BEAT-SPEC.md` (98-100): “in read-myself mode the chunk's Quick-check door arms no earlier than `hold_s = clamp(round(60 * chunk_word_count / WPM_MAX), 10, 60)` with `WPM_MAX = 230` (a generous Grade-5 silent-reading ceiling — a faster finish is not a plausible read).”
- `grade3-reading/artifacts/u4l2-build/BEAT-SPEC.md` (96-97): “replaces the reference's flat 20-second silent-reader clock on chunk beats”
- `grade3-reading/artifacts/u4l2-build/BEAT-SPEC.md` (102): “mode checked at fire time, so flipping modes mid-beat cannot bypass the hold”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (73-74): “Tapping a sentence in read-myself speaks that one line and never arms the door.”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (71): “Per chunk, not global.”
- `grade3-reading/artifacts/u4l2-build/BEAT-SPEC.md` (101-102): “In read-to-me mode the clock is unchanged from the reference: the read-along's natural end arms the door”
- `grade3-reading/.claude/skills/one-perfect-lesson/SKILL.md` (85): “WPM-based self-read hold (derive from word count × grade WPM norms)”
- `grade3-reading/artifacts/u4l2-build/METHODS-CHECKLIST.md` (83-85): “**B1. WPM-plausibility hold on self-reading.** In "I'll read it myself" mode, the advance control for each chunk is disabled until a minimum time derived from that chunk's word count at an age-plausible WPM has elapsed; a learner cannot scroll-and-skip to the question.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/02-LESSON-STRUCTURE.md` (106-108): “Each chunk ends in a RECALL-ONLY stop behind a door that arms when read-aloud ends or after the self-read dwell (`max(4s, words/150wpm)`, PRA-146).”
- `grade3-reading/artifacts/qc-2026-09-30-staging/LIVE-WALK.md` (58): “The coach line says "Listen to the story to the end first." The button arms only after a silent timer of about 60 s.”

Against: Neighbouring rulings in the same project pull the other way: a review asking that modelled thinking not be clicked past named "no timers, no disabled Next, no yes/no gates" as anti-patterns (`grade3-reading/artifacts/feedback-devfactory-2026-09-10/REGISTER.md`, line 29), and another put staged reveals on a tap because "A timer also cannot pace itself to a slow reader." (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md`, lines 310-311). The sources record the hold as built, not whether it makes students read rather than wait. The ceiling of 230 words a minute is stated without a source, and the 60-second cap opens any part longer than 230 words sooner than that ceiling allows. The build shows the wait as a "countdown shown on the door" (`grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md`, lines 70-71), a visible clock that sits uneasily with keeping clocks off untimed reading (the record no-clock-unless-speed-counts). On a page holding a passage that is silent by design, the hold kept a learner waiting about 60 s while the guide's line said to listen to the story, and the walk asked for such text to be exempt or for a line saying to take one's time (`grade3-reading/artifacts/qc-2026-09-30-staging/LIVE-WALK.md`, lines 56-60).

<sub>criterion · integrity, sequence, practice · universal · from g3 · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Meaning first, the word last

Introduce a new word by giving its meaning first and its label last, never by asking learners to guess what it means.

A grade-3 reading rulebook's vocabulary routine orders each word meaning first, a description with the label at the end, before an example and non-example pair, the word's parts where it splits, and a say-it-back. A reading quality canon applied in a grade-5 audit adds that an unfamiliar word is never introduced with a guess-opener such as 'who can tell me what X means?'. The rulebook says it is grounded in BrainLifts on direct instruction, practice and knowledge and a reading-science corpus.

Quoted:

- `grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md` (164): “Per word, in order: MEANING FIRST (description → label at the END)”
- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (303): “An unfamiliar word is never introduced with a guess-opener ("who can tell me what X means?").”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md` (3-4): “BrainLifts (Direct Instruction, Practice, Curriculum & Knowledge), the reading-science corpus”

Against: A later card design for the same course opens with the word itself, "1. **Word** — "Our word today is nursery. Listen to me say this word: nursery."" (`grade3-reading/artifacts/feedback-vocab-design-2026-09-21/PETER-PAN-CARDS-SIX-BEATS.md`, line 13), and gives the meaning fourth, after the learner says the word and hears its parts.

<sub>criterion · wording, sequence · universal · from g3 · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Model a step in its own interaction

Model each step in the interaction learners will later use for it, because a step only narrated in the model leaves them performing a move they have never seen. One design's model glowed 4 of 8 word tiles for the learner to tap and lock in, where the built model only narrated which words fit.

A response to a review of a reading lesson found that its distinctive knowledge step was a tap-to-choose item in the independent task but only spoken narration in the model, so the child was modelled on prose and then asked to perform an interaction they had not seen (`grade3-reading/artifacts/Peter-Pan-L4-review-response-2026-08-25.pdf`, p.2). It called this the single change most likely to make the lesson feel like the skill it teaches, and committed to reusing the independent task's item in the model so that the model rehearses the move. The lesson's design had specified exactly that: its model has the learner tap each of 4 glowing words to lock it in (`grade3-reading/artifacts/pp1-v3-design.txt`, lines 157-159). A later gap register in the same course found two lessons handing the child a six-statement judging task cold, because the model's version of it had no engine primitive, and called the gap pedagogically real though mitigated (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md`, lines 32-36).

Quoted:

- `grade3-reading/artifacts/Peter-Pan-L4-review-response-2026-08-25.pdf` (p.2 (pdftotext lines 74-76)): “Our lesson has the KNOW bank in the child's independent task (p22, node step3, as an msq) but delivers it as spoken narration during the modelling. So the child is modelled on prose and then asked to perform an interaction they have not seen.”
- `grade3-reading/artifacts/Peter-Pan-L4-review-response-2026-08-25.pdf` (p.2 (pdftotext lines 93-94)): “primitive already working at p22 step3, so the modelling rehearses the move the child must then make.”
- `grade3-reading/artifacts/pp1-v3-design.txt` (159): “Correct / glowing set (4, auto-glow one by one; child taps each to lock it in): gloomy, miserable, unpleasant, strict.”
- `grade3-reading/artifacts/pp1-v3-design.txt` (157): “Vocabulary chips (8, rendered as word tiles): gloomy · sunny · unpleasant · joyful · miserable · free · strict · exciting.”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md` (33-34): “No engine primitive exists, so L6 and L7 hand the child the six-statement judging task cold.”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md` (35-36): “but pedagogically real in the two lessons that carry the procedure.”

Against: Audits of later lessons in the same unit accepted narrated think-aloud models in place of the designs' interactive ones: "The doc's interactive-tap-to-find spec for the MM was already adapted to think_aloud convention arc-wide." (`grade3-reading/artifacts/arc-audit/PEDAGOGY-L7-2026-09-05.md`, lines 25-26). The course standard lets the surface format change between stages while the operation stays the same: "Surface format may change only when the target operation remains demonstrably stable." (`grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd`, line 317). No learner outcome was measured either way.

<sub>criterion · practice, format, sequence · universal · from g3 · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Model first, then on demand

Make a procedure's full model compulsory the first time it appears at each stage, then available on request, and shown again automatically after a wrong answer on it. One writing scheme gives each procedure one mandatory model at each of its three stages.

A model curriculum's fading rules for its grade 3 writing scaffold, written in answer to a request to fade scaffolds as children succeed, use one rule: the first time a procedure appears at a stage its model is mandatory, and every lesson after is on demand with auto-restore. On demand, the model is hidden by default and the child may open it; auto-restore shows it automatically, with the choice removed, when the child got the previous task with the same procedure wrong. Each procedure runs this ladder on its own schedule.

Quoted:

- `grade3-reading/course-renderer/docs/extras/alpharead-fading-guidance.md` (18): “***ONE unified rule: the first time a procedure appears at a stage → MANDATORY model. Every lesson after → on demand + auto-restore. Each procedure carries its own “one model per stage.”***”
- `grade3-reading/course-renderer/docs/extras/alpharead-fading-guidance.md` (24): “the model is hidden by default; the child can choose to open it”
- `grade3-reading/course-renderer/docs/extras/alpharead-fading-guidance.md` (26): “**Auto-restore —** on top of on-demand — if the child got the previous same-procedure task wrong, the model is shown automatically next time (the choice is removed). This is “the scaffold reappears when struggling.””
- `grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md` (58): “No child control over pace or skipping (children are poor judges of what they can skip).”
- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (824): “the MM is always a full model with the child doing only the final step”
- `othello-course-renderer-draft/repo/docs/extras/alpharead-fading-guidance.md` (18): “***ONE unified rule: the first time a procedure appears at a stage → MANDATORY model. Every lesson after → on demand + auto-restore. Each procedure carries its own “one model per stage.”***”
- `othello-course-renderer-draft/repo/docs/extras/alpharead-fading-guidance.md` (22): “Fires on a procedure’s FIRST appearance at each stage (Stage 1, then Stage 2, then Stage 3).”
- `othello-course-renderer-draft/repo/docs/extras/alpharead-fading-guidance.md` (26): “if the child got the previous same-procedure task wrong, the model is shown automatically next time (the choice is removed).”
- `othello-course-renderer-draft/repo/docs/extras/alpharead-fading-guidance.md` (64): “The sentence stems never fade (DI step language) — only their pre-fill does.”
- `othello-course-renderer-draft/repo/docs/extras/alpharead-fading-guidance.md` (62): “The cold text = the mastery diagnostic: known procedure + new content, current stage, inside the built knowledge web.”
- `othello-course-renderer-draft/repo/docs/extras/alpharead-writing-scaffold-overview.md` (29): “full echo → clause starter → bare stem → blank box”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md` (824): “NOT the in-lesson Modelling Moment, which never tapers: the MM is always a full model with the child doing only the final step”
- `othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md` (191-192): “Guide commentary before each part of a text, sentence starters and step-by-step guidance all fade.”
- `othello-course-renderer-draft/repo/docs/pedagogy/grade-4-vs-grade-3.md` (67): “Nothing in this repo fades anything yet.”

Against: A walkthrough of another grade 3 build ruled out child choice: "No child control over pace or skipping (children are poor judges of what they can skip)." (`grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md`, line 58), while the on-demand default lets a child leave the model unopened. The procedure specification the renderer follows says the in-lesson modelling moment "never tapers" and is always a full model with the child doing only the final step (`grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` and `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md`, line 824), and the renderer's own rules have sentence starters fade across a unit (`othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md`, lines 190-192). Nothing in the renderer fades anything yet (`othello-course-renderer-draft/repo/docs/pedagogy/grade-4-vs-grade-3.md`, line 67).

<sub>criterion · sequence, hints, practice · universal · from g3 · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Model the rejection, then retest it cold

Model rejecting a known misconception in the worked example, then retest it cold on a new tempting case, with no hints before the attempt and the repair only in feedback.

An audit's verification pass attacked a Grade 5 lesson's misconception design as a possible leak and upheld it against the live build: the worked example pre-models the rejected hunter-to-prey reading, and the independent trap item is attempt-first, with no hints before the try and the repair only in post-attempt feedback. The course's bar pins the pre-modelling at the worked example and a cold re-elicitation at release. The worked example works the first arrow on the map and the release item asks about the second, so the retest is on a new case.

Quoted:

- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (566-567): “Misconception pre-teach design (I-do models, You-do re-elicits cold) is canonical, not a leak.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (568-570): “supposed to pre-model the rejected hunter-to-prey alternative; the You-do's `trap_item` is `attempt_first: true` with "No hints before you try" and the repair appearing only in post-attempt feedback.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (517): “canon pins pre-modeling at M2, re-elicits cold at release”
- `grade3-reading/artifacts/g5-deploy/audio/GENERATION-REPORT.md` (57): “I'm going to work the very first solid arrow on the map, the one between kelp and sea urchin”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (290-291): “Look at the second solid arrow on the map, the one between the sea urchin and the sea otter.”
- `grade3-reading/artifacts/u4l2-build/content/u4l2-content.json` (519): “The misconception is elicited, never pre-taught”
- `grade3-reading/artifacts/g5-deploy/EVALUATION-API.md` (93-94): “hunter→prey is THE misconception, elicited and repaired only AFTER an attempt.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (518): “this note's wording mischaracterizes the design as elicit-only”

Against: The lesson's design note and its evaluation document describe the design as elicit-only, "The misconception is elicited, never pre-taught" (grade3-reading/artifacts/u4l2-build/content/u4l2-content.json, line 519) and "hunter→prey is THE misconception, elicited and repaired only AFTER an attempt." (grade3-reading/artifacts/g5-deploy/EVALUATION-API.md, lines 93-94), which the audit calls a mislabel. The record refute-the-misconception-learners-bring draws the belief out first, as a prediction, before refuting it. The audit shows the design is canonical and not a leak, not that it teaches better.

<sub>criterion · sequence, feedback · universal · from g3 · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Name the steps, never number them

Name each procedure step in its own words, on screen and aloud, never by a number, which only signals unseen steps, and say the procedure's name whenever it runs.

The course renderer's pedagogy rules require a modelling moment to say which of its seven procedures it is running and to show the step it is on, named and never numbered, on screen or aloud (`othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md`, lines 327-345). A label such as "Step two, part a" tells a child only that unseen steps are coming, while the step's own words are the teaching. The procedure specification behind the rule treats steps as student-facing, to be displayed, spoken and internalised (`othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md`, line 24). The same rules also have the procedure's name said each time it runs, since a child who watched one procedure four times without once hearing its name had four demonstrations and no tool.

Quoted:

- `othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md` (333): “The step is named, never numbered, on screen or aloud.”
- `othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md` (333-335): “"Step two, part a" tells a child only that steps they have not seen are coming and that they cannot see how many”
- `othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md` (343-345): “Seven named procedures are the whole design: a child who has watched FIND four times without once hearing it called FIND has been given four demonstrations and no tool.”
- `othello-course-renderer-draft/repo/docs/rules/pedagogy-and-lesson-structure.md` (329-330): “**Rule.** A modelling moment says which of the seven procedures it is running and shows the step the guide is on, advancing as the voice reaches it.”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md` (24): “Steps are student-facing. They can be displayed on screen, spoken aloud, and internalised.”
- `othello-course-renderer-draft/repo/docs/qa/new-lesson-qa-invariants.md` (34-35): “**A3. Step numbering is sequential and unique per beat.** Never two "Step 2" blocks; never a Step 3 numbered 2.”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md` (838): “voiced once inside the think-aloud with the step numbers”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md` (840): “("Step 1, Read the question…")”
- `grade3-reading/course-renderer/docs/rules/pedagogy-and-lesson-structure.md` (333): “The step is named, never numbered, on screen or aloud.”
- `grade3-reading/course-renderer/docs/rules/pedagogy-and-lesson-structure.md` (333-336): “"Step two, part a" tells a child only that steps they have not seen are coming and that they cannot see how many; the step's own words, "What is the main thing in each part?", are the whole of the teaching.”

Against: The same repository's QA invariants require step numbers that are sequential and unique per beat, with never two "Step 2" blocks (`othello-course-renderer-draft/repo/docs/qa/new-lesson-qa-invariants.md`, lines 34-35), and the procedure specification voices the search with the step numbers, as in "Step 1, Read the question…" (`othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md`, lines 838 and 840). The course's QA invariants check numbers: "**A3. Step numbering is sequential and unique per beat.** Never two "Step 2" blocks; never a Step 3 numbered 2." (`grade3-reading/course-renderer/docs/qa/new-lesson-qa-invariants.md`, lines 34-35), and a built lesson decided on "One ladder everywhere, matching the p17 chart and the p25 recap: Step 1 Read the question, Step 2 Find it in the text, Step 3 State the answer, Step 4 Refine the concept, Step 5 Let's try extra thinking." (`grade3-reading/course-renderer/content/lesson-plans/g3-u2-l1.json`, line 760).

<sub>criterion · wording, sequence · universal · from g3 · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Never skip the modelled write-up

Once a procedure has been modelled in full, let learners skip its earlier modelled steps, but always play the step that models the written answer in full. In one design the write-up is the fourth step in all nine of its procedures, so the skip rule needs no exceptions.

A Grade 3 reading lesson design's skip rule is that the child may skip the modelling moment but not its fourth step, the write-up, which plays in full until the modelled response has been read aloud, because the written expectation is the thing being modelled (`g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx`, lines 285 and 415). Skipping the first three steps is the default once a procedure has been modelled once (line 303). One procedure's steps were reorganised, adding a search step and retiring a refining one, so that the write-up is the fourth step in all nine of the design's procedures and the rule needs no exceptions (line 307).

Quoted:

- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (285): “The rule in one line: the child may skip the Modelling Moment, but not step 4. Step 4 is the write-up on every rail, and it plays in full, unskippable, until the modeled response has been read aloud.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (415): “New rule. Step 4 is the write-up, and the written expectation is the thing being modeled.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (303): “Every other lesson. The default once a procedure has been modeled once.”
- `g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx` (307): “Step 4 is the write-up on all nine rails, so the rule needs no exceptions.”

Against: Another record bars young learners from skipping instruction on their own judgment; this design makes skipping the first three modelled steps the default once a procedure is known and frames it as the child's option, removing the choice only after a lesson where the child was not secure (`g9/sources/Readventure - Lesson Design and Scaffolding - Updated.docx`, lines 285, 303 and 87).

<sub>criterion · sequence, practice · domain · from g3 · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### No live self-view while learning

Keep a live view of the learner's own face out of a lesson, because seeing oneself can raise appearance anxiety and lower recall. Across 3 experiments with university students, self-view raised appearance anxiety, and that anxiety lowered lecture recall.

The Grade 9 idea research reports a peer-reviewed paper of 3 experiments with 171, 124 and 224 university students in which camera-on with self-view raised social appearance anxiety most, and that anxiety, not camera status itself, mediated lower lecture recall. It concludes that an audio-only lesson with no camera removes this failure mode rather than designing around it.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd` (96-97): “3 experiments, 171/124/224 university students. Camera-on with self-view raised social appearance anxiety most; that anxiety, not camera status itself, mediated lower lecture recall.”
- `grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd` (98): “(university sample; generalization to 14–15s is inferential)”
- `grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd` (144-145): “An audio-only, no-camera format structurally removes this failure mode rather than needing to design around it.”

Published: [Tien, Imundo & Bjork 2023, Viewing oneself during synchronous online learning increases appearance anxiety and decreases memory for lecture content, Applied Cognitive Psychology](https://doi.org/10.1002/acp.4048) · [Austin, Fogler & Daniel 2021, Seeing self and others on-screen does not negatively impact learning in virtual classrooms, Scholarship of Teaching and Learning in Psychology](https://doi.org/10.1037/stl0000303)

Against: The study's sample was university students, so applying it to 14- and 15-year-olds is an inference; and a 2021 study by Austin, Fogler and Daniel reports in its title that seeing self and others on screen does not negatively impact learning in virtual classrooms (https://doi.org/10.1037/stl0000303).

<sub>criterion · media · universal · from g9, research · external-research · contested · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Refute the misconception learners bring

When learners bring a common wrong belief, draw it out once at the start as a prediction and refute it, since a clear explanation alone can leave it standing. In one study, refuting the misconception beat a concise correct explanation on immediate gains by an effect size of about 0.79.

A short-video BrainLift in the course plans holds that a clear explanation can produce the feeling of understanding while the misconception survives, and that a video should open by confronting a documented misconception when it is central, citing refutation ≈ d 0.79 and dialogue ≈ d 0.83 over concise correct exposition on immediate conceptual gains (Muller 2008) (`grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md`, lines 113-118). A generic instruction BrainLift sorts misconceptions by source: instinctive ones are taught explicitly with contrastive material and revisited, while ones produced by poor instruction are not foregrounded but designed out of the explanation (`grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md`, lines 60-61). The wrong belief is drawn out as a prediction on the same question the lesson answers, and is not voiced again once refuted (`ti-courseplans-audit/skills/video-red-team/references/rubric.md`, lines 63-73; `ti-courseplans-audit/skills/course-red-team/SKILL.md`, lines 201-202).

Quoted:

- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md` (113): “When a documented misconception is central, open by confronting it.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md` (114-115): “A clear explanation can produce the feeling of understanding while the misconception survives.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md` (116-118): “concise correct exposition on immediate conceptual gains (Muller 2008: refutation ≈ d 0.79, dialogue ≈ d 0.83) [20]. Scope: immediate, undergraduate, misconception-central”
- `grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md` (60): “teach explicitly with contrastive material; expect to revisit.”
- `grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md` (61): “don't foreground — fix the explanation so it isn't produced.”
- `ti-courseplans-audit/skills/train-teacher/SKILL.md` (72): “A clear explanation that never engages the prior belief produces confident non-learning (Muller: clear-only exposition barely moved scores; misconception-first nearly doubled the gain).”
- `ti-courseplans-audit/skills/course-red-team/SKILL.md` (201-202): “The wrong belief is voiced at most once, at the open, and never rehearsed/scolded in the body”
- `ti-courseplans-audit/skills/video-red-team/references/rubric.md` (63-65): “where the teaching atom owns a named misconception, the opener must ELICIT the intuitive wrong belief ONCE (as an invited prediction / reasonable guess), then resolve it against that tension.”
- `ti-courseplans-audit/skills/video-red-team/references/rubric.md` (71-73): “They must be the same conceptual question, and the positive body must explicitly resolve the prediction raised at the open.”
- `ti-courseplans-audit/skills/video-red-team/references/rubric.md` (74-75): “If deleting the hook leaves the body teaching an unrelated objective unchanged, the hook is misaligned.”
- `ti-courseplans-audit/skills/video-red-team/references/rubric.md` (69): “Intro/overview atoms are exempt (curiosity hook ok).”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-qc-evidence-v0.1.md` (167-169): “thing the learner reads and encodes as the section title, so a negative card **frames the whole lesson via the wrong belief** even when the narration is clean.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-qc-evidence-v0.1.md` (223): “**Positive on-screen `[CARD]` labels** — cards must be positive schema labels, never "what X is NOT" / "Not a…"; rewrite negation-phrased catalog cells positively.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-generation-v0.1.md` (46): “Refutation-text research puts the harm in *dwelling on / repeating* the wrong belief, not in *naming it once* to build the boundary.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-generation-v0.1.md` (63): “In the **body** (everything after the hook) **never** narrate the wrong belief ("you might think the sun feeds the plant, but…") — repeating it aloud rehearses it.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-generation-v0.1.md` (43): “A version that first surfaces the intuitive wrong idea, lets the learner feel it is wrong, then resolves it, nearly doubled the gain.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-qc-evidence-v0.1.md` (635): “but **never engaged the learner's prior belief** — the exact Muller failure.”

Published: [Muller et al. 2008](https://doi.org/10.1111/j.1365-2729.2007.00248.x) · [Schroeder et al. 2022](https://doi.org/10.1177/07356331211070534)

Against: The BrainLift scopes the evidence to immediate gains in undergraduates where the misconception is central, not a proven delayed-retention benefit (`grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md`, lines 117-119); and in a study of short narrated videos, refutation text structures largely made no significant difference against an expository one (Schroeder et al. 2022, https://doi.org/10.1177/07356331211070534). The study is cited as a dissertation with no DOI or URL in these files, and introductory or overview lessons are exempt and may open on plain curiosity (`ti-courseplans-audit/skills/video-red-team/references/rubric.md`).

<sub>criterion · sequence · universal · from g3, research · external-research · contested · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Release runs both ways

When a learner stumbles in independent work, step back to shared work on the same content rather than moving on, since gradual release runs both ways.

One of a grade-3 reading rulebook's five laws calls release a loop: when the child stumbles unaided, step back to shared work on the same content. Its acceptance test is that, with the I-do, we-do and you-do labels stripped, the work still shows modelling, shared work and independent work of the same skill. A reading quality canon applied in a grade-5 audit adds re-entering modelling on a new genre or a harder text and calls the coached middle stage where growth happens, so release is not a one-way ratchet.

Quoted:

- `grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md` (16-17): “Release is a LOOP: when the child stumbles unaided, step back to shared work on the same content.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md` (17-19): “Acceptance test: strip the I-do/we-do/you-do labels and the artifact must still show modelling → shared work → independent work of the SAME skill.”
- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (693): “Re-enter I-do on a new genre or harder text; the coached we-do 'middle' is where growth happens — release is not a one-way ratchet.”

Against: Another record, one-process-falling-support, holds that support across modelling, guided and independent practice only falls, and a closing-question pattern it cites says "3. Support fades and never returns." (`shadow-content-eval/references/closing_questions_pattern.md`, line 72); a review there counted support coming back as a fault (`shadow-content-eval/reports/G3-U2-L1-review.md`, line 51).

<sub>criterion · sequence, practice, hints · universal · from g3 · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Something to do on every screen

Give every screen a response that does the teaching work, and let no passive stretch of watching, hearing or reading run past about a minute without one. In a published study, memory tests inserted into recorded lectures cut mind-wandering by roughly a third.

The reading project's course feedback made a response on every screen the default, because passive listening or text-only screens invite click-through rather than attention, and its rulings require a specific interaction on every screen. The interaction must be substantive to the teaching move: a decorative tap control does not count. In a published study, memory tests inserted into recorded lectures cut mind-wandering by roughly a third and improved recall against uninterrupted video (Szpunar, Khan & Schacter 2013). The response is preferably one the learner produces. Watching teaches only an active watcher, and a decorative tap or a word said back doesn't count.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd` (27): “students should do something on every screen: passive listening or text-only screens invite click-through rather than attention.”
- `grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd` (27): “The interaction must be substantive to the teaching move; a decorative tap control does not satisfy the concern.”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (37): “every screen requires a specific interaction (no passive screens”
- `grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd` (211-212): “Interpolated memory tests inserted into recorded lectures cut mind-wandering by roughly a third and improved recall versus uninterrupted video.”
- `grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd` (119-120): “sync checks becoming compliance checks... too much with texts that are too short”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (37): “every screen requires a specific interaction (no passive screens,”
- `grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd` (27): “passive listening or text-only screens invite click-through rather than attention. The interaction must be substantive to the teaching move; a decorative tap control does not satisfy the concern.”
- `grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd` (31): “If video carries essential context, interrupt it with mandatory quick checks so the learner does not watch a long unexamined clip.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (130): “Keep passive episodes short and make active checks consequential;”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (128): “N7: active-check cadence. No long passive segment without a non-bypassable check.”
- `grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd` (27): “a decorative tap control does not satisfy the concern”
- `grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd` (27): “do not expose student-controlled playback speed that lets a child rush the sequence without listening at an age-appropriate rate.”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (23): “each screen earns a purposeful response; knowledge building avoids redundant prose and interleaves quick checks”
- `grade3-reading/knowledge_bot/ROUTER.md` (68): “every screen needs meaningful student engagement; knowledge building should be focused and checked;”
- `grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd` (39): “remove Scout's interjections at the top of each page. They take away from the reading flow.”
- `grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` (86-87): “match the task family to the knowledge: recognition is not enough for productive, representational, justificatory, or integrative constructs;”
- `grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` (38-39): “judge a lesson by *production* (say/write/type) over *selection* (click)”
- `ti-courseplans-audit/docs/instruction-modes-spec.md` (49): “a consequential check at least every 60s of passive content (Generic Instruction SS6)”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D10-delivery-ux-accessibility.md` (23): “No continuous passive segment beyond ~60s; a consequential check appears at least every 60s”
- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (349): “Passive content is interrupted by consequential identify, complete, generate, explain, or represent responses chosen for the target construct.”
- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (350): “Clicks counted as production; authored prompts never render; long passive stretches; redundant low-value questions.”
- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (351): “Response count alone is not quality; demand and follow-up matter.”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (183): “G3 iter-3 claimed "7–8 generate/lesson, over-delivered" — but 2–3 were trivial *say-backs* (repeat a word) and the real generative-comprehension production was ~2”
- `ti-courseplans-audit/skills/course-red-team/SKILL.md` (83-85): “Iter-3's "7–8 generate, over-delivered" was true by count and misleading by quality (2–3 trivial say-backs; 5 of 7 spoken moments canned). Verify the number AND what it measures.”
- `ti-courseplans-audit/skills/course-red-team/references/opportunities-to-respond-brainlift.md` (23): “A high number of responses per minute is not evidence of quality if the app reached that number by asking only recognition questions.”
- `grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md` (35): “No continuous passive segment beyond ~60s.”
- `grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md` (37): “they can be broken up by inserting MCQs at pause points within the video.”
- `grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md` (57): “No screens with nothing for the child to do (except perhaps the very intro)”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (308): “A timed reveal is a passive segment”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/meetings/incept-service-coe-2026-08-10/MEETING-EXCERPTS.qmd` (32-33): “required learner work must be meaningful and non-bypassable, while reading, listening, transition, and accessibility steps use task-appropriate completion evidence rather than decorative clicks.”
- `shadow-bench/` (commit cebac33) (5-9): “No passive segment should run beyond ~60-90s without an active check (Generic §6; DI 9-12 responses/min). A single AlphaTok atom's CFU is a separate atom (SPOV3), so short scripts are fine as continuous narration — the checkable slice is the EXTENDED script that lacks an in-script pause/check point (Generic §9: break extended explanations with MCQ pause points).”
- `shadow-bench/` (commit cebac33) (11-12): “tools/active_check.py (shared): estimate_seconds (~130 wpm), has_active_check, active_check_warnings — warns only for scripts > ~90s with no check/pause marker.”
- `shadow-bench/` (commit cebac33) (17): “Report-only and high-threshold by design.”
- `downloads/BrainLift - What makes a good intro video.md` (427): “Watching someone else be taught only substitutes for being taught when the watcher is active.”
- `downloads/BrainLift - What makes a good intro video.md` (470): “Solo observation was weaker, so in a solo app the checks and pauses have to do the work the partner did.”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (197): “The taps are attention devices, not assessment — they keep a long model active without adding an ask.”
- `grade3-reading/ti-courseplans-wiki/Perfect-Course-Rulebook.md` (160-161): “Interaction count is not evidence of cognitive ownership. A click is evidence only when its alternatives and consequences expose the target operation.”
- `grade3-reading/ti-courseplans-wiki/Perfect-Course-Rulebook.md` (157): “tap count presented as production”
- `grade3-reading/ti-courseplans-wiki/Anatomy-of-a-Perfect-Course.md` (51-52): “A click can be decorative, answer-revealing, or unrelated to the thinking being taught.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_08 10_30 CEST - Notes by Gemini.md` (446): “Like, it's not going to be enough for them just to watch it.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_08 10_30 CEST - Notes by Gemini.md` (450): “They're going to have to kind of actively respond to it in some way.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_08 10_30 CEST - Notes by Gemini.md` (446): “Watch the scene, answer questions. That's still an open question for us about how we would design that.”
- `grade3-reading/ti-courseplans-wiki/Reviewer-Feedback-2026-08-18.md` (16): “the student takes no action until we_do”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md` (255): “or are unsubstantiated (G4 roots boundary, 60 s passive ceiling, abstract-image rule, end-of-unit good/bad ban).”
- `grade3-reading/_archive/2026-08-13-consolidation/tmp-g5-r8-src-scripts.tar.gz` (scripts/lane-tools/drafts/xp-dose-mapping.md inside it) (15): “the >=1 consequential check per 60s of passive content is what makes this XP verified, not watched”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/FEEDBACK-RESPONSES.md` (189): “'Keep this big idea in mind as we explore' is easy for kids to skip right past.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md` (104-106): “**A think-aloud is a fully-open modelled beat; it has nothing for the child to answer.** The child can advance as soon as the model is on screen; requiring an explicit gate action (e.g. a closed Next button) on a think-aloud is a defect”
- `grade3-reading/course-renderer/docs/rules/pedagogy-and-lesson-structure.md` (164-166): “`LessonRenderer` gates the Next button on every required node, so a page with a gated node cannot be skipped, but a page with no gated node passes every validator.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-qc-evidence-v0.1.md` (638-640): “v1.1 had inserted ~124 "Quick check: … Get ready. …" prompts to satisfy a passive-segment cadence sub-bar; the **promoted** JSONs carry none. Decision: remove all cadence prompts”
- `grade3-reading/.claude/skills/one-perfect-lesson/SKILL.md` (66): “purposeful response every screen; hint only after an attempt”

Published: [Szpunar, Khan & Schacter 2013](https://www.pnas.org/doi/pdf/10.1073/pnas.1221764110) · [Chi, Roy & Hausmann 2008](https://doi.org/10.1080/03640210701863396)

Against: A later concern that the checks were becoming compliance checks, too many for texts that are too short, was held for a ruling rather than settled. The course's every-screen rule is stricter than the standard it drew on, which asks only that passive episodes be short, and none of it was measured on students. One round of feedback raised the worry of checks becoming compliance checks and left it for a ruling; its source is not cited here. Additions meant to focus the reader can break the flow: a later request removed the guide's interjections at the top of each page because they took away from the reading flow (`grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd`, line 39). a review still counted the range of technology-enhanced item types as a real benefit and the clearest advantage over the incumbent course (`grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd`, line 108). Meeting notes kept with the course standard limit the rule: required work must be meaningful and can't be bypassed, but reading, listening, transition and accessibility steps use completion evidence that fits the task rather than decorative clicks (`grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/meetings/incept-service-coe-2026-08-10/MEETING-EXCERPTS.qmd`). Not enforced: 'Report-only and high-threshold by design.' (`shadow-bench`, git commit cebac33, line 17). The 60-90 s figure comes from an internal guide, not a measurement. The source gives no size for how much weaker solo observation was. A later run found counter-evidence (`grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md`). A later run found counter-evidence (`grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md`). A later run found counter-evidence (`grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-qc-evidence-v0.1.md`).

<sub>criterion · practice, format, media · universal · from ap, g3, research · adopted-rule · contested · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Start a new procedure light

Make the first lesson on a new procedure lighter, with a smaller set to work on, built so later lessons only widen the set instead of rebuilding it. The first lesson on one procedure showed students three sentences to choose from; the second had them pick from the whole section.

Two persuasive-text lesson designs plan a fade across a unit. The first deliberately lightens its find-the-opinions task to a reduced set of three sentences, written so that lightening later only means widening that set, and the second applies the fade: the child taps opinions straight from the whole section. Both are design notes logged for confirmation.

Quoted:

- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 2. Should We Save the Rainforests - WEIGH - Lesson Design.docx` (8 (textutil text)): “This is the first WEIGH lesson in the unit, so the "Find the opinions" task is deliberately lightened: the child is shown a reduced set of three sentences (a mix of fact and opinion) rather than the whole text at once”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 2. Should We Save the Rainforests - WEIGH - Lesson Design.docx` (8 (textutil text)): “Everything below is written so that lightening later only means widening that set, not rebuilding the lesson.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 8. Whose World Is It - WEIGH - Lesson Design.docx` (8 (textutil text)): “This is the second WEIGH lesson in the unit (after Should We Save the Rainforests?), so the fade applies: the "Find the opinions" task is no longer reduced to three options — the child taps opinions straight from the whole section.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 5. Feathers and Scales - CONNECT - Lesson Design (v3 - prototype-aligned).docx` (8 (textutil text)): “Built here to the KB row as-is: the full compare (similarities and differences, then connect).”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 5. Feathers and Scales - CONNECT - Lesson Design (v3 - prototype-aligned).docx` (8 (textutil text)): “(easier to fade than to build up)”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 5. Feathers and Scales - CONNECT - Lesson Design (v3 - prototype-aligned).docx` (8 (textutil text)): “Everything below is written so that lightening only means trimming the Compare step, not rebuilding the lesson.”
- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (866): “in early texts the change compares TWO points only (first↔last, or one part↔another); drop other parts' evidence from the MM - multi-part evidence is a later step (scaffolds entry 8).”
- `grade3-reading/artifacts/arc-audit/L6.md` (104): “The delivered approach is arguably cleaner for the unit's first FIND lesson, reducing the evidence set from 3 to 1 to limit cognitive load in the modelled walk-through.”

Against: The first comparison lesson went the other way: "Built here to the KB row as-is: the full compare (similarities and differences, then connect)." It left lightening optional "(easier to fade than to build up)", though it too was written so that lightening only means trimming one step, not rebuilding the lesson.

<sub>criterion · sequence, demand, practice · universal · from g3 · adopted-rule · contested · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Teach the idea before its name

When a later lesson owns a concept's technical name, teach the idea first in plain words and hold the term back, so the name attaches to an idea already held.

Lesson research for a unit's second lesson ruled against giving learners a technical term that the course plan reserves for a later lesson, because the course's knowledge rules want prior knowledge reused rather than re-taught, which works better if the later lesson attaches a new name to a concept already held. The unit's opening film followed the same line: two beats show the idea, how a stranger who knocks is treated, without using the term, and the course plan notes say the film does not have to use the word.

Quoted:

- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (598-601): “One decision this raises: do not give the child the Greek word xenia at L2. The graph reserves the naming for L6, and R-KC-5 wants prior knowledge reused rather than re-taught, which works better if L6 gets to attach a new name to a concept the child already holds.”
- `grade3-reading/course-renderer/docs/video/u1-script-and-visual-plan.md` (81-82): “two beats gesture at xenia, treating a stranger who knocks as its own test, without using the word "xenia" itself, since the word is not introduced until `U1T6`”
- `grade3-reading/course-renderer/docs/video/u1-course-plan-notes.md` (193): “the xenia thread the unit names in lesson 5. The video does not have to use the word.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l2-the-cyclops.md` (598-601): “The graph reserves the naming for L6, and R-KC-5 wants prior knowledge reused rather than re-taught, which works better if L6 gets to attach a new name to a concept the child already holds.”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l2.json` (216): “Do NOT give the child the Greek word xenia at L2.”

Against: Two rules point the other way. The same engine names procedures from the first demonstration, since "a child who has watched FIND four times without once hearing it called FIND has been given four demonstrations and no tool." (`grade3-reading/course-renderer/docs/rules/pedagogy-and-lesson-structure.md`, lines 343-345), and the intro-video rule recorded in name-the-term-and-show-the-instance says to name a term together with its instance, never the instance alone. The sources give no measure of which order teaches better.

<sub>criterion · sequence, wording · universal · from g3 · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Teach word parts by meaning, not sound

Once learners decode fluently, as expected from grade 3, leave phonics out of vocabulary teaching and break taught words into the parts that carry meaning.

A Grade 3 reading course's published rules say not to teach phonics or phonemic awareness at Grade 3 and above: leave decoding out and teach morphology, breaking words into meaningful units, since its readers have mastered phonics. A mechanical rule requires vocabulary cards to break words by meaning parts, not sounds, though its detector for phonetic splits is still owed. The same course's recorded decisions keep a sound-it-out and say-it stage in its vocabulary sequence as an intentional audio action, so the sources disagree on whether a card may also break a word by sound.

Quoted:

- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (115): “Do not teach phonics or phonemic awareness at Grade 3 and above”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (118): “Leave decoding out. Teach morphology instead: break words into meaningful units.”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (392): “Morphological teaching, never phonetics. G3 has mastered phonics; cards break words by meaning parts (`morph.parts`), not sounds.”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (393): “phonetic-split detector OWED”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/SHARED-DECISIONS.md` (17): “Vocabulary follows the current sound/say/teach/example/type sequence, with genuine attempt handling and later inability fallback.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/SHARED-DECISIONS.md` (19): “explicit sound-out remains an intentional audio action”
- `grade3-reading/course-renderer/docs/rules/knowledge-and-curriculum.md` (211-212): “**Rule.** Leave decoding out. Teach morphology instead: break words into meaningful units.”
- `grade3-reading/course-renderer/docs/qa/new-lesson-qa-invariants.md` (61-62): “**B2. Morphological teaching, never phonetics.** G3 has mastered phonics; cards break words by meaning parts (`morph.parts`), not sounds.”
- `grade3-reading/course-renderer/docs/rules/knowledge-and-curriculum.md` (214-215): “are expected to have already acquired these foundational decoding skills”
- `grade3-reading/course-renderer/docs/rules/knowledge-and-curriculum.md` (215-216): “with a reading fluency baseline of approximately 110 words per minute”
- `grade3-reading/course-renderer/docs/qa/new-lesson-qa-invariants.md` (63-64): “OWED: fail phonetic-split content”
- `othello-course-renderer-draft/repo/docs/rules/knowledge-and-curriculum.md` (211-212): “**Rule.** Leave decoding out. Teach morphology instead: break words into meaningful units.”
- `othello-course-renderer-draft/repo/docs/rules/knowledge-and-curriculum.md` (216-218): “Instead, teach morphemes: "the word 'transportation', where isolating the root 'port' (travel) and the prefix 'trans' (across) provides a systematic strategy for deriving word meaning."”
- `othello-course-renderer-draft/repo/docs/rules/knowledge-and-curriculum.md` (215-216): “with a reading fluency baseline of approximately 110 words per minute”
- `othello-course-renderer-draft/repo/docs/qa/new-lesson-qa-invariants.md` (61-62): “**B2. Morphological teaching, never phonetics.** G3 has mastered phonics; cards break words by meaning parts (`morph.parts`), not sounds.”

Against: The same course keeps a sound-out stage: 'Vocabulary follows the current sound/say/teach/example/type sequence, with genuine attempt handling and later inability fallback.' (grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/SHARED-DECISIONS.md, line 17), and 'explicit sound-out remains an intentional audio action' (the same file, line 19). It is followed by convention, and the check that would fail phonetic splits in child-facing text is still owed: "OWED: fail phonetic-split content" (`grade3-reading/course-renderer/docs/qa/new-lesson-qa-invariants.md`, lines 63-64). It is followed by convention rather than enforced (`othello-course-renderer-draft/repo/docs/rules/knowledge-and-curriculum.md`, line 224), and the check that would fail phonetic splits in learner-facing text is still owed (`othello-course-renderer-draft/repo/docs/qa/new-lesson-qa-invariants.md`, lines 62-64).

<sub>criterion · wording, alignment · domain · from g3 · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Acquisition, durability and transfer are separate claims

Treat acquisition, durable mastery and transfer as three claims, each needing its own evidence, and never let a check built for one stand in for another. One course set acquisition at 90% on 15 distinct new feedback-free items, and durable mastery at 80% or more on a different day.

A Grade 5 reading course's BrainLift states that acquisition, durable mastery and transfer are different claims, and that a same-session checkpoint cannot establish durability (`incept-package-hub/course-packages/courses/g5-reading/review/brainlift.html`). Its policy builds each theme checkpoint from fifteen distinct new certified items, at least three of them integrative, with no feedback and a ninety-percent acquisition threshold, and reserves durable-mastery claims for a different-day, feedback-free assessment on novel items at or above eighty percent (`incept-package-hub/course-packages/courses/g5-reading/source/canonical/pedagogy-policy.json`, lines 1719 and 1754). Transfer requires cold passages on never-taught topics and stays separate from course mastery or an impact claim. The scheme ties together three narrower rules: a later test on new items, a delay that is proven, and cold texts kept for testing.

Quoted:

- `incept-package-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “Acquisition, durable mastery, and transfer are different claims.”
- `incept-package-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “A same-session checkpoint cannot establish durability”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/pedagogy-policy.json` (1719): “Build each theme checkpoint from fifteen distinct new certified items, including at least three integrative items, with no feedback and a ninety-percent acquisition threshold.”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/pedagogy-policy.json` (1754): “Reserve durable-mastery claims for a different-day, feedback-free assessment on novel items at or above eighty percent.”
- `incept-package-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “transfer requires cold passages on never-taught topics and remains separate from course mastery or an impact claim.”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u01.md` (193): “This is the unit exit gate (≥90%): passing means the child owns the tool,”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/ASSESSMENT-QUALITY-MEMO.md inside it) (56): “The real high-dependency gates are **not** the in-lesson 90%; they are the **cold-transfer exit lessons** enforced by the compounding gate”

Against: A Grade 3 course's archived prompts made its cold-transfer lessons, on unseen texts within the unit's own topic, the unit exit gates: 'This is the unit exit gate (≥90%): passing means the child owns the tool,' (`incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u01.md`, line 193), and the same course's assessment memo named those cold-transfer exit lessons as its real high-dependency gates. The Grade 5 scheme is a design: at its red-team review, all 550 of its items were still not certified.

<sub>method · stage: measure · evidence-of-learning, measurement, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Build each thread backward

Build each concept thread backward from a demanding end point, keeping the concept constant and raising the difficulty, so a later stage on the same content always asks for more. One standards set lifted two Grade 8 history standards from explain and describe to evaluate, so they ask more than the Grade 7 standards on the same content.

A text-sourcing brief builds each thread from a Grade 8 destination: it names the concept that text demands, chooses earlier texts that build the same concept in simpler form every year, and keeps the concept constant while the difficulty rises (`downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx`). A whole-course thematic map tracks the complexity of each idea on rungs alongside grade (`downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx`). A social studies standards set lifted two Grade 8 history standards, explain to evaluate and describe to evaluate, so their demand is strictly higher than that of the Grade 7 standards on the same content (`downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx`). These are design rules; no outcome was measured.

Quoted:

- `downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx` (5 (textutil text)): “We pick a Grade 8 destination, name the concept it demands, then choose earlier texts that build that same concept in simpler form every year.”
- `downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx` (110 (textutil text)): “Keep the concept constant, raise the difficulty.”
- `downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx` (sheet 'How to read this', cell A7): “Rung is the complexity of the IDEA, tracked alongside grade.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx` (sheet 'V7.0 Executive Summary', cell A30): “Two G8 History standards received verb lifts to ensure cognitive demand is strictly higher than their G7 equivalents:”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx` (sheet 'V7.0 Executive Summary', cell A33): “This maintains the DOK progression principle that G8 standards must be higher-order than G7 equivalents covering the same content.”

Against: none found

<sub>method · stage: ground · sequence, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Knowledge taught together moves together

What was taught together tends to be known or missing together, so in a course with few prerequisites, sample a diagnostic by teaching unit rather than testing every component. At 3 items for each of 400-600+ components, testing every component of an AP course would take 1,200-1,800 items, roughly 10-15 hours.

The diagnostic BrainLift argues that components taught in the same unit and the same week have correlated mastery, not because they depend on each other but because the causes of knowing them are shared, so two failed items from one unit should lower the estimate for the whole unit (`grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md`). It calls this instructional clustering and leans on it in subjects with many components and sparse prerequisite structure, where prerequisite chains cannot carry the inference. A well-decomposed AP course might hold 400-600+ components, and at 3 items each that is 1,200-1,800 items, roughly 10-15 hours of testing.

Quoted:

- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (349): “KCs taught in the same unit, by the same teacher, in the same week, will be correlated in their mastery status — not because the KCs are logically related, but because the *causes* of knowing or not knowing them are shared.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (380): “instructional clustering, which exploits shared exposure history rather than logical dependencies”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (351): “A well-decomposed AP course might contain 400-600+ knowledge components. At 3 items per KC (a bare minimum for defensible inference), that's 1,200-1,800 items — roughly 10-15 hours of testing.”

Against: This is the BrainLift's statistical argument; nothing in the evidence measures how strongly mastery moves together within a unit.

<sub>method · stage: measure · evidence-of-learning, measurement · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Placement and gap-finding are different diagnostics

Treat placement and gap-finding as different diagnostics: placement in an ordered course needs only a short binary search, while finding gaps needs sampling across the course. A binary search finds the starting unit of a 9-unit course in 3-4 items.

A diagnostic BrainLift written around AP courses, one of the assessment BrainLifts given to the reading course plans, separates placement, a search for one cut-point on a roughly ordered course, from hole-filling, which assumes no order and needs the full knowledge-mapping machinery at 40-60+ items and 15-30 minutes (`grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md`). For a 9-unit course the search takes 3-4 items (log₂(9) ≈ 3.2). For gaps it advises finding one, sizing it, filling it and repeating, instead of mapping every hole at once.

Quoted:

- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (370): “A placement diagnostic can be done in 10-15 items and 5 minutes.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (418): “This typically takes 3-4 items for a 9-unit course (log₂(9) ≈ 3.2).”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (373): “**Insight 6: You don't need to find all the holes at once — find a hole, size it, fill it, repeat.**”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (420): “Total items: typically 7-10 items. Total time: 3-5 minutes.”
- `grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md` (414): “If the course genuinely lacks sequential structure (e.g., a collection of independent topics with no progression), this diagnostic is inappropriate — go straight to full knowledge-mapping.”

Against: The same BrainLift rules the search out for a course with no sequential structure, which goes straight to full knowledge-mapping, and it sizes a placement two ways: 10-15 items and 5 minutes in one place, 7-10 items and 3-5 minutes in another.

<sub>method · stage: measure · evidence-of-learning, measurement, sequence · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Record speed with every answer

Record how long each answer took as well as whether it was right, since a fast wrong answer marks a confident misconception and a slow right one fragile knowledge.

A practice BrainLift in the reading course's feedback sorts answers into four cells: fast and correct is fluent, slow and correct is fragile and calls for a shorter interval, fast and incorrect is a confident misconception that needs discrimination practice, and slow and incorrect is not yet acquired; platforms that rely on accuracy alone will systematically misclassify learners. The course's instruction standard adopted the four-cell diagnostic to drive scheduling (`grade3-reading/ti-courseplans/docs/instruction-quality-standard.md`, line 125).

Quoted:

- `grade3-reading/ti-courseplans/feedback/feedback1/Practice BrainLift.md` (35): “slow correct (fragile, shorten interval), fast incorrect (confident misconception, needs discrimination practice)”
- `grade3-reading/ti-courseplans/feedback/feedback1/Practice BrainLift.md` (35): “Platforms that rely on accuracy alone will systematically misclassify learners”
- `grade3-reading/ti-courseplans/docs/instruction-quality-standard.md` (125): “The four-cell diagnostic (fast/slow × correct/incorrect) drives scheduling.”
- `g9/transformer/v09/README.md` (8): “Telemetry: time to answer, hesitation, glossary taps, replays.”

Against: none found

<sub>method · stage: measure · evidence-of-learning, measurement, practice · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### The kind of knowledge sets the method

Choose how to teach by what the knowledge is like, rather than by the habits of its subject, since no method is good or bad in general.

The curriculum BrainLift that the reading project's course plans align with holds that subjects don't tell us how to teach, the knowledge type does: profile what the knowledge is like and let that drive the choices rather than subject stereotypes (`grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md`). It adds that methods aren't universally good or bad but conditionally apt given a knowledge component's evaluability, decomposability and representation profile. Kinds of knowledge include a fact to recall fluently, a concept, a procedure, a distinction and a causal explanation (the same BrainLift).

Quoted:

- `grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md` (1732): “**SPOV1 - Subjects don’t tell us how to teach; the knowledge type does.”
- `grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md` (1735): “Methods aren’t universally good or bad; they’re conditionally apt given the KC’s evaluability, decomposability, and representation profile.”

Against: none found

<sub>method · stage: ground · format, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Vocabulary gaps show before comprehension falls

Track word knowledge with its own periodic check outside passage questions, because comprehension scores can hold for about two years while a vocabulary gap widens. In the original fourth-grade-slump study, low-income children's word-meaning scores slowed from grade 4 while their comprehension held for about two more years.

A grade-4 pedagogy definition cites the original fourth-grade-slump study: low-income children's word-meaning scores decelerated from grade 4, but their comprehension held up for about two more years because they compensated with context, and fell once the gap grew too large to cover. It concludes that vocabulary should be tracked as its own measure, apart from comprehension-item pass rates, with a light periodic word-meaning check outside the passage items, and records that check as a gap not yet built.

Quoted:

- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/PEDAGOGY.md` (98-99): “**Vocabulary debt is a LEADING indicator, invisible in comprehension scores until it isn't**”
- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/PEDAGOGY.md` (100-101): “children's word-meaning scores decelerated starting grade 4, but comprehension scores held up fine for ~2 more years because students compensated with context”
- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/PEDAGOGY.md` (102-103): “**Implication: track vocabulary knowledge as its OWN metric, separate from comprehension-item pass rate**”
- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/PEDAGOGY.md` (105-107): “A lightweight periodic out-of-context word-meaning check (not folded into passage comprehension items) is the cheap fix; this is a genuine gap in the current lesson design, not yet implemented.”

Published: [Poor Children's Fourth-Grade Slump, American Educator (2003)](https://eric.ed.gov/?id=EJ672463)

Against: The same definition warns that the grade-4 slump has a rival vocabulary account and that knowledge and vocabulary are entangled, so the decline should not be over-attributed (`grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/PEDAGOGY.md`, lines 194-195).

<sub>method · stage: measure · evidence-of-learning, measurement · universal · from g3, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A passed gate is not learning

A lesson that passes every check is well formed, and a first-try answer shows the moment; whether anyone learned needs a later test on new items.

The reading project's quality gate certifies form, not outcome, by construction
(`grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd`); its engine's README says passing tests
proves plumbing, not learning (`grade3-reading/engine/README.md`); and a rise in completion alone was ruled
insufficient (`grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md`). First-try answers show the
moment: on a final test 5 minutes later restudying won, but after 2 days and a week prior testing gave much greater
retention (Roediger & Karpicke 2006, https://doi.org/10.1111/j.1467-9280.2006.01693.x).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (149): “A same-day lesson gate proves at most "I can do it now," not "I can still do it later under changed conditions."”
- `grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd` (238): “**The first gate should test the intended generalisation.** If the KC is meant to transfer across surface forms, then first-exposure gating must include surface variation and near-miss contrasts—not only isomorphic items.”
- `grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd` (237): “mastery gates should include items that require the learner to generate, select, or justify without the scaffold.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (158): “E4 mastery gate: no feedback, delayed, varied, independent.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (159): “Same-day testing after practice measures working memory more than long-term memory.”
- `grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd` (60): “**Author parallel forms per lesson test** (BLOCKING for hole-filling) — 2-3 forms each so three-state retry works”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (141): “- Require 90% to advance; if not met, give intensive instruction and a delayed test with new items.”
- `grade3-reading/artifacts/calibration/ROUNDS.md` (60): “26 findings landed on lessons whose gate was green at review time”
- `grade3-reading/artifacts/cert-layer/AUTOMATED-CHECKS-ROADMAP-2026-08-31.md` (56): “JSON/JSX text**, and the findings that keep recurring are ones only visible”
- `grade3-reading/artifacts/cert-layer/CONTRACT-v0-2026-08-31.md` (223): “A perfectly-transferred bad design passes every gate.”
- `grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/PRIOR-curriculum-verification-2026-09-10.md` (3): “do not replace student text, regenerate media, or claim curricular approval from source equality or passing technical tests”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/V2_MONSTER_DOSSIER.md` (109): “completion-up-while-construct-accuracy-flat is the named failure, not a win.”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/V2_MONSTER_DOSSIER.md` (109): “Pre-register every dosage claim as a PAIRED metric (completion delta + same-student near-neighbour construct-accuracy delta, leak-probe ON).”
- `grade3-reading/artifacts/g5-merged-course/VERDICT_TEMPLATE.md` (70): “2. **KCT1 Domain-knowledge ≈ 0 — by design.** Domain-recall items are passage-independent → removed”
- `grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md` (22): “was 0/3 plain-blind and 3/3 spine-conditioned”
- `grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md` (22): “Decertified `certified -> spine_leaky`”
- `grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/04-evidence-contract.md` (11): “Improvement from pre-unit to post-unit student explanation of the unit concept.”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (318): “A v1 seam the adversarial review found: the same instrument was being used as both the mastery gate and the growth measure. Rev 2 separates them.”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (321): “built from a held-out pool of un-practiced, un-gated items.”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (321): “We never teach to or gate on it”
- `grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md` (53): “Platforms that collapse the two masteries (acquisition vs durable) into one binary gate either over-reteach or under-practise”
- `grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md` (130): “old: no bridge possible (0/313 overlap). Current: 409 real G3 MAP RIT records”
- `grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md` (131): “for 173 students in TimeBack OneRoster; blocker is UUID crosswalk.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md` (135-136): “The predictive claim ("does well here → does well on MAP") is **a design intent, not a measured result**, until the linking study runs.”
- `grade3-reading/knowledge_bot/CHECKLIST.md` (31): “the 24-item mastery GATE (`masteryThreshold:90`) is DISTINCT from the MAP-equivalent proxy (cold passages, raw/40+band, `gating=false`, no 90 threshold). Don't conflate.”
- `grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd` (74): “Running 100K simulated students yields **zero new information** — outputs are determined by the imposed math models + pre-training.”
- `grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd` (76): “100K-LLM-agent AP simulator (AP-score-from-pre-training artefact problem)”
- `grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd` (84): “no self-validation (outputs must be validated against real student outcomes — Phase 6).”
- `grade3-reading/knowledge_bot/skills/reading-science/PRIORITIES.qmd` (81-83): “this corpus grounds DESIGN, it does not prove OUR implementation works. Never cite it as evidence about our courses' outcomes.”
- `grade3-reading/knowledge_bot/ROUTER.md` (126): “Do not claim RIT/proven impact before a real linked/piloted outcome source exists.”
- `grade3-reading/knowledge_bot/knowledge/kb-0031-how-it-works.qmd` (138): “**Curriculum issues** (students complete content but scores don't improve): your instruction needs work”
- `grade3-reading/knowledge_bot/knowledge/kb-0016-timeback-alpharead-publishing-playbook.qmd` (62-65): “pre/post tests are assigned **separately from the course** and surface on the TimeBack UI dashboard as a pending test. **PowerPath is only for serving questions natively — not for pre/post gating.** Pilot: select a cohort, assign the test before + after the learning app to measure growth.”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (38-40): “release-day completion never qualifies (Practice BrainLift: same-day testing measures working memory, not learning).”
- `ti-courseplans-audit/docs/practice-layer-spec.md` (38-40): “a delayed (≥24h) retest passed on *new* parallel items — release-day completion never qualifies (Practice BrainLift: same-day testing measures working memory, not learning)”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D6-practice-durable-mastery.md` (13): “Same-day testing after practice is invalid (measures working memory) — non-negotiable”
- `ti-courseplans-audit/docs/standards/course-quality.qmd` (61): “A fully green build gate proves the course is well-built. It does not prove the course works.”
- `ti-courseplans-audit/docs/standards/course-quality.qmd` (65): “A green gate with no outcome measure is reported as built, not effective.”
- `grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd` (35-36): “these are not rushed-tree findings, they are findings the team's OWN passing gate missed.”
- `grade3-reading/knowledge_bot/knowledge/kb-0127-incept-service-coe-catchup-2026-07-14.qmd` (94): “pedagogical-knowledge benchmark performance is not proof of teaching quality.”
- `grade3-reading/knowledge_bot/knowledge/kb-0130-incept-service-coe-catchup-2026-07-15.qmd` (136-137): “Neither dataset size nor CDPK performance establishes effective generated instruction or student learning.”
- `downloads/BrainLift - What makes a good intro video.md` (430): “The sync check after a video is a check on attention, not on memory.”
- `downloads/BrainLift - What makes a good intro video.md` (329): “That is real retrieval, because the child has to produce the answer across a gap of days. The sync check after a video is not.”
- `grade3-reading/ti-courseplans/docs/practice-layer-spec.md` (37-40): “**Interleaving eligibility = E2-cleared**: a delayed (≥24h) retest passed on *new* parallel items — release-day completion never qualifies”
- `grade3-reading/ti-courseplans/docs/instruction-modes-spec.md` (63-64): “an anchor first taught the same day never satisfies an `assumes` edge, and an anchor that is present-but-not-fluent is treated as not met.”
- `grade3-reading/ti-courseplans/skills/video-red-team/references/finding-taxonomy.md` (98-99): “GREEN is only "no defect found on the checked dimensions".”
- `grade3-reading/ti-courseplans/docs/standards/course-quality.qmd` (81): “Synthetic prediction, IB scores, or reviewer approval are not outcome evidence.”
- `icloud-work/ML learnings/evaluation_methodology.md` (187): “- It doesn't test "student experience" — a confusing but technically correct question can pass”
- `icloud-work/incept/sat-reading-generation/SAT_Question_Generation_Replication_Guide.md` (462): “- **Student Testing**: Test questions with actual target audience when possible”
- `grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md` (35): “Acquisition mastery and durable mastery are different. A same-day lesson gate proves at most 'I can do it now,' not 'I can still do it later under changed conditions.'”
- `grade3-reading/edullm-review-hub/course-packages/courses/apush/review/evidence/case-for-review.md` (10): “The nine assessment sets preserve held-out source use, function-level scoring, correction routes,”
- `grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd` (19): “In-app success must predict performance on credible external assessments.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/achieved.md` (69): “Root cause: paqpgdst's MCQ_SET pass rate on HOLDOUT prompts is **0%** (0/176 K=3 attempts), vs ~20% on eval baseline.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (159): “- Same-day testing after practice measures working memory more than long-term memory.”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/WHY_V2_WINS.md` (14): “practiced certifies *familiarity*, not reading ability”
- `grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md` (188): “Receipt claims completion/practice, never mastery”
- `grade3-reading/artifacts/cert-layer/CONTRACT-v0-2026-08-31.md` (53): “"this lesson will not waste a child's time or lie to them," not”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md` (48): “"Is it adding value" cannot improve past "the design says so and the shape is coherent"”
- `grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/03-transfer-practice-layer.md` (95): “It proves assessment integrity, not curriculum quality.”
- `grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md` (9): “It is item-quality-against-a-rubric, NOT learning”
- `grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd` (120): “| High in-app accuracy, low test scores | In-app tasks are not testing transfer |”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/AUDIT_ACTIONS.md` (22): “Until it exists, "certified" ≠ "works";”
- `grade3-reading/knowledge_bot/BRIEFING.md` (84): “**Mastery now requires COLD / unseen-passage transfer** — the fix for "in-app high, MAP flat."”
- `ti-courseplans-audit/docs/instruction-quality-standard.md` (120): “Durable mastery requires a **delayed”
- `downloads/WF - Brainlift Opportunities to - 260724-110911.md` (176): “The goal is to measure whether a child’s comprehension and oral language are growing over time, not just whether the child answered one question.”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (353): “whether they own them durably is a different question the course answers with spaced returns, not with a medal.”
- `grade3-reading/ti-courseplans/docs/standards/course-quality.qmd` (61): “A fully green build gate proves the course is well-built. It does not prove the course works.”
- `grade3-reading/ti-courseplans/docs/academics-alignment-plan.md` (71-72): “Serving mastery forms same-session with feedback measures acquisition and calls it mastery”
- `ap-helpers-data-agent-memory/feedback_eval_contamination_check_all_eval_files.md` (20): “Had I trained on those rows, v54 would have learned its eval set verbatim → fake pass rate, contamination, useless iteration. Caught before training; saved the cycle.”
- `shadow-bench/docs/brainlift.md` (143): “and nothing flows back from the classroom to reveal whether they missed any.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (249): “The next proof must be a fresh dynamic generation run using the patched pipeline, followed by the prior n=30 regression gate and eventually the full failed-export replay.”
- `aptraining-local/parallel-ideas-lab/reports/rubber_ducks/promotion_gate_20260525.md` (47): “- Failed re-validation/cherry-pick artifacts including old Den 50/50 proof and EXPLOIT-003.”
- `g9/transformer/README.md` (120): “No lesson has been reviewed by a person or used by a student.”
- `g9/transformer/v04/README.md` (12): “- **Transfer:** unseen lines, key quotations.”
- `g9/tools/unit-video-essay/INTEGRATION.md` (40): “A successful render is technical proof only, not academic approval.”
- `g9/tools/unit-video-essay/QA.md` (19): “The generated voice and assembled scene have **not** been heard or approved by a human reviewer, academically signed off, or tested with students.”
- `g9/transformer/v01/QA.md` (40-41): “A first live run on Othello showed two faults no check caught”
- `g9-transformer-runs/blocks/856ace1aed960671.json` (8, 14): “"stem": "Who is the person actually speaking the words that describe the ruined statue and the surrounding desert?",”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/STUDENT_READY_CRITICISM_FRAMEWORK.qmd inside it) (172): “BrainLift in `kb-0086` separates E1 acquisition, E2 fluency, E3 generalization, and E4 delayed independent mastery. Same-day gates prove little durable mastery. | Add delayed, varied, independent mastery gates using new items and no immediate feedback; distinguish acquisition checks from durable mastery in docs. |”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (581): “### G5-POL-PRA-008: Reserve durable-mastery claims for a different-day, feedback-free assessment on novel items at or above eighty percent.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “Acquisition, durable mastery, and transfer are different claims.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “an acquisition checkpoint requires a substantial set of distinct, certified, feedback-free items, including integrative work, at the declared high-accuracy threshold;”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “durable mastery requires a different-day, feedback-free check on novel forms; and”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “transfer requires cold passages on never-taught topics and remains separate from course mastery or an impact claim.”
- `g9/transcript/chat-transcript.redacted.txt` (3111): “Can the student make and defend a thoughtful interpretive judgment on unfamiliar material after the support has gone?”
- `grade3-reading/course-renderer/content/course-rationale.json` (891): “Every per-unit gate was the unit's own TRANSFER lesson, taken in the same session with feedback on. That measures acquisition, not durable mastery, and a failed gate routed straight to a retry rather than to reteaching and a delayed retest.”
- `othello-course-renderer-draft/repo/content/course-rationale.json` (939): “a delayed, feedback-off instrument that can draw on any unit, not the next thing taught.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (36-37): “It does not present eight planned units as if they were authored lessons, and it does not convert a clean package into evidence about classroom results.”

Published: [Roediger & Karpicke 2006](https://doi.org/10.1111/j.1467-9280.2006.01693.x)

Against: no outside measure was
available to test it with, since the usual external test was not available for the cohort (`grade3-reading/NORTH_STAR.md`). A later run found: lessons the calibration log had marked green still drew 26 findings in one review round, findings the team's own passing gate missed, so passing every check shows good form only as far as the checks reach (`grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd`). A later run found counter-evidence (`g9/transformer/v01/QA.md`). A later run found counter-evidence (`g9-transformer-runs/blocks/856ace1aed960671.json`).

<sub>context · evidence-of-learning, measurement · universal · from g3, research · adopted-rule · held · found in [2026-10-12-2-round-1](../research/2026-10-12-2-round-1/), [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Judged failures are not learner difficulty

Read the failure rates of generated items as evidence about the writer and the judge, not about what learners find hard. From a topic where 3 of 6 generated items failed, an analysis wrote what students confuse, though no student had answered any item.

From topic-level failure rates of generated questions, such as 3 failures among 6 items on one topic, an analysis agent wrote what 'students confuse' on that topic and set a 15-25% selection-rate target for each wrong option (`icloud-work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md`). The topic table comes from code over the judge's verdicts, and no learner had answered any of the items.

Quoted:

- `icloud-work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md` (603): “| Spread of Communism after 1900... | 3 | 6 | 50.0% |”
- `icloud-work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md` (126): “- Students confuse different communist movements (Russian, Chinese, Cuban)”
- `icloud-work/evaluator/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md` (345): “- Validate distractors represent 15-25% selection rate each”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md` (255): “The 14-dimension evaluation cannot assess Rasch model fit, item discrimination, or guessing behavior — these require empirical response data.”

Against: none found

<sub>context · evidence-of-learning, measurement · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Learners judge an agent by its persona

Learners can take a scripted teaching agent for an adaptive one and judge it by its persona.

A paper on scripted pedagogical agents, pasted into the Grade 9 unit's design chat, reports from its authors' earlier work that learners assume such agents give dynamically generated, adaptive responses even when they do not, and, citing an earlier suggestion, that learners deal with an agent through its interface and persona rather than its algorithms (`g9/transcript/chat-transcript.redacted.txt`, lines 2761-2763). Its authors recommend an expert agent to introduce new content or demonstrate a procedure in a well-defined subject, and a peer-like motivating agent for ill-structured domains and low-achieving students (lines 2753-2759). The advice on domains and low-achieving students comes from the paper's discussion, not from a comparison across them. The unit's design brief took the agent roles and their looks as hypotheses to test with its own students (line 3075).

Quoted:

- `g9/transcript/chat-transcript.redacted.txt` (2761): “learners assume agents such as these are providing dynamically-generated and adaptive responses, even when they are not”
- `g9/transcript/chat-transcript.redacted.txt` (2763): “learners interact with agents as represented through their interface (e.g., persona), not through their underlying algorithms.”
- `g9/transcript/chat-transcript.redacted.txt` (2757): “The Expert would be appropriate to introduce new content or demonstrate a procedure within a well-defined subject area”
- `g9/transcript/chat-transcript.redacted.txt` (2759): “The Motivator may be more appropriate in ill-structured domains or constructivist learning environments, where learners’ voluntary engagement is more critical than their knowledge acquisition.”
- `g9/transcript/chat-transcript.redacted.txt` (2759): “Also, the Motivator may work more effectively with low achieving students, who are sometimes motivated by working with those who are of a similarly competency level”
- `g9/transcript/chat-transcript.redacted.txt` (2753): “we operationalized a motivator agent with a peer-like image of a casually-dressed student in his twenties”

Published: [Simulating instructional roles through pedagogical agents (International Journal of Artificial Intelligence in Education, 2005)](https://doi.org/10.3233/IRG-2005-15(2)02)

Against: The study used scripted agents with college students, and the unit's design brief adds: "Their work supports investigating different instructional functions; it does not validate three conversational agents working together." (`g9/transcript/chat-transcript.redacted.txt`, line 3075). The claim about persona is a cited suggestion, not a measured result.

<sub>context · media, feedback · universal · from g9, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Liking is not learning

Don't read liking as learning: in one study every kind of picture raised satisfaction, but only instructive ones raised recall.

In a published study, every kind of graphic raised satisfaction ratings over no graphics, but only the instructive
graphics raised recall (Sung & Mayer 2012, https://doi.org/10.1016/j.chb.2012.03.026). No student has used any version
of my film (`g9/README.md`), so how much anyone liked it says nothing yet about what it teaches.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0202-g9-othello-video-research-fake-ai-attention.qmd` (39): “AI presenters show no reliable learning loss, but a real engagement and comfort loss”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/LOAD-BEARING-METRIC.md` (132): “interest tested flat as a learning driver, so it was struck from the record (Honesty log).”
- `grade3-reading/knowledge_bot/knowledge/kb-0119-curriculum-architecture-brainlift-evidence.qmd` (226): “restudy feels productive, but retrieval produces stronger delayed learning.”
- `grade3-reading/knowledge_bot/knowledge/kb-0033-problem.qmd` (88): “Gamification often rewards *completion* rather than *mastery*.”
- `grade3-reading/knowledge_bot/knowledge/kb-0162-assessment-item-difficulty-evidence.qmd` (140): “Warns us not to rely on students’ subjective ease or fluency as indicators of mastery”
- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/VERIFICATION-PROPOSALS.md` (11): ““Looks more animated” alone is not evidence of better teaching.”
- `grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md` (59): “A visual preference alone cannot establish comprehension gains.”
- `grade3-reading/artifacts/g5-course/G5-CURRICULUM-ONE-PAGER.md` (35): “noted, not treated as approval.”
- `grade3-reading/knowledge_bot/knowledge/kb-0026-evaluating-apps.qmd` (26): “If an app performs well on engagement but poorly on externally validated outcomes, the closed loop forces the conversation back to instruction, mastery, and signal integrity.”
- `grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd` (547): “"the most predictive statistical models show that engagement is a mediator of the effects of instruction on reading achievement"”
- `ti-courseplans-audit/docs/generator-insights.md` (143): “A generator optimizing for pass-rates or engagement will quietly lower rigor”
- `grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd` (45): “**No significant difference in academic performance** between AI and human instructor conditions. **Video engagement was higher with the human instructor.**”
- `downloads/BrainLift - What makes a good intro video.md` (420): “A video that is enjoyed and teaches nothing has not done the job.”
- `downloads/BrainLift - What makes a good intro video.md` (22): “Accepted as evidence, refused as advice. Enjoyment is not the reading, SPOV1”
- `grade3-reading/ti-courseplans/docs/generator-insights.md` (143-144): “**A generator optimizing for pass-rates or engagement will quietly lower rigor and destroy the very thing that works.**”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0172-g3-reading-course-feedback-2026-08-04.qmd` (101): “That is encouragement, not acceptance, certification, or proof of learning.”
- `uae-education-ai/data/development_cases.json` (22): “A claim that learners achieved an objective should be supported by an observable student action that demonstrates that objective; task completion or engagement alone does not establish it.”
- `g9/transcript/chat-transcript.redacted.txt` (3084): “An engaging performance without intellectual follow-through is insufficient.”

Published: [Sung & Mayer 2012](https://doi.org/10.1016/j.chb.2012.03.026)

Against: liking still
matters for whether anyone watches at all, and nothing here measures that. A later run found counter-evidence (`grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd`).

<sub>context · evidence-of-learning, media · universal · from research · external-research · held · found in [2026-10-12-2-round-1](../research/2026-10-12-2-round-1/), [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Research sets direction, not results

Use published research, judgment-set values and simulated students to direct and stress-test a design, never as proof of whether or how well it works, which only real learners' outcomes show.

The reading course plans' research priorities say their corpus grounds design and does not prove that their implementation works, and is never to be cited as evidence about the courses' outcomes (`grade3-reading/ti-courseplans/docs/reading-science/PRIORITIES.qmd`); their quality standard adds that synthetic prediction, benchmark scores and approval on review are not outcome evidence (`grade3-reading/ti-courseplans/docs/standards/course-quality.qmd`). After an assessment's baseline from a biased slice was replaced by the full population's 196.0, the 46th percentile (n=915), its approval case was held to direction, not magnitude, with no growth number before its pilot (`grade3-reading/ti-courseplans/docs/course-formula-agents.md`), and an audit relabelled a simulation presented as agreement with the real test as internal cross-bank consistency (synthetic) (`grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md`). A video BrainLift tags each rule as learning evidence, an accessibility requirement, a platform constraint or an operating heuristic, never cites a heuristic as a proven threshold, cites conservative independent numbers because effect sizes inflate when a principle's originator is an author, and lets its own delayed-recall data overrule a cited effect (`grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md`, `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md`). Tag every rule with its evidence. Research and simulation give neither the size of an effect nor a prediction of an outside score.

Quoted:

- `grade3-reading/ti-courseplans/docs/reading-science/PRIORITIES.qmd` (81-83): “this corpus grounds DESIGN, it does not prove OUR implementation works. Never cite it as evidence about our courses' outcomes.”
- `grade3-reading/ti-courseplans/docs/standards/course-quality.qmd` (81): “Synthetic prediction, IB scores, or reviewer approval are not outcome evidence.”
- `grade3-reading/ti-courseplans/docs/course-formula-agents.md` (262): “the real figure was **196.0 / 46th pctile (n=915)**. No RIT/growth number pre-pilot; direction, not magnitude”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md` (34): “now "internal cross-bank consistency (synthetic)," explicitly not MAP agreement”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md` (19): “- `[OH]` operating heuristic (current guess; has owner + validation experiment; NEVER cite as a proven learning threshold).”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md` (293): “- **Effect sizes inflate when a principle's originator is an author;** we cite conservative independent numbers and treat any single effect as a direction.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md` (306-307): “when our own delayed-recall data contradicts a cited effect, our data wins and this document is edited.”
- `grade3-reading/knowledge_bot/knowledge/kb-0010-amalgamation-v2-engine-results.qmd` (57): “All numbers are point estimates against a 5-student synthetic profile dataset.”
- `grade3-reading/knowledge_bot/knowledge/kb-0010-amalgamation-v2-engine-results.qmd` (57): “Direction is the trustworthy signal; magnitudes are not.”
- `grade3-reading/knowledge_bot/knowledge/kb-0010-amalgamation-v2-engine-results.qmd` (110): “2 of 5 recs delivered as predicted, 3 backfired”
- `grade3-reading/knowledge_bot/knowledge/kb-0010-amalgamation-v2-engine-results.qmd` (124): “individual-level r ≈ 0.42”
- `grade3-reading/knowledge_bot/knowledge/kb-0010-amalgamation-v2-engine-results.qmd` (124): “Cohort-run outcomes are the only authoritative measure.”
- `grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd` (94-95): “item difficulties are expert-assigned, not estimated from student responses”
- `grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd` (96): “Each simulation writeup carries an explicit "What This Does Not Prove" section”
- `grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd` (157-158): “SE(b-hat) <= 0.30 logits needs N >= 200 responses/item”
- `grade3-reading/knowledge_bot/knowledge/kb-0010-amalgamation-v2-engine-results.qmd` (41): “The engine also identified one specific structural cliff in v2 that the BrainLift doesn't yet address”
- `grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md` (51): “LLM as expert-predictor not student-simulator”
- `grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md` (131): “expert-predictor not student-simulator. Six of eight (A–F) sit inside this cluster.”
- `grade3-reading/artifacts/X1_staar_map_overlap_probe_2026_06_16.md` (13): “The repo confirms **0 of 313 overlap**”
- `grade3-reading/artifacts/X1_staar_map_overlap_probe_2026_06_16.md` (17): “it's a measured void, not an assumed one”
- `grade3-reading/artifacts/team-direction-2026-09-09/DIRECTION-2026-09-09.md` (88): “the 0/313 STAAR×MAP join that killed any RIT”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (259): “refuse to put a number on RIT until an in-cohort MAP pilot exists”
- `ti-courseplans-audit/docs/reading-science/PRIORITIES.qmd` (82-83): “corpus grounds DESIGN, it does not prove OUR implementation works. Never cite it as evidence about our courses' outcomes.”
- `grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd` (64-65): “the 200-210 claim is by-design **pre-pilot** and confirms only after a linking study”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (40): “no RIT output; engine physically will not emit RIT until linked to real MAP scores.”
- `grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd` (61-62): “MAP is 0/313 in-cohort — no RIT claim, no "proven", no growth multiples”
- `grade3-reading/knowledge_bot/knowledge/kb-0010-amalgamation-v2-engine-results.qmd` (110): “2 of 5 recs delivered as predicted, 3 backfired — engine flagged why”
- `grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd` (74): “Running 100K simulated students yields **zero new information** — outputs are determined by the imposed math models + pre-training.”
- `grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd` (23): “This is a deterministic design stress test and reproduction packet.”
- `grade3-reading/knowledge_bot/knowledge/kb-0010-amalgamation-v2-engine-results.qmd` (120): “**No numerical claim in this document should be trusted as a magnitude.**”
- `ti-courseplans-audit/skills/train-teacher/references/gauntlet-spec.md` (50-51): “**All results labeled SIMULATED**; calibrate against real-student data as pilots run.”
- `ti-courseplans-audit/docs/generator-insights.md` (123-124): “LLM student role-play is structurally flawed and caps ~67% accuracy; teacher-as-predictor reaches r≈0.72–0.79 population-level”
- `ti-courseplans-audit/skills/train-teacher/SKILL.md` (119-121): “Simulated-student results are predictions, never outcomes — label them as such everywhere; Tier-3 proof is standardized-score movement only.”
- `grade3-reading/_archive/2026-08-13-consolidation/top-level-docs/HANDOVER_COURSE_EXPERIENCE_PREFLIGHT_2026-08-11.qmd` (325): “actual developmental suitability remains `VERIFY` until human learner evidence exists.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/03_SIMULATION_EVIDENCE.md` (103): “**Key assumption:** All simulations use b_provisional values as true item difficulties.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/03_SIMULATION_EVIDENCE.md` (103): “True concurrent validity requires field data — simulations validate algorithm behavior, not scale accuracy [AERA-2014].”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_CASE_FOR_APPROVAL.md` (198): “If the Rasch model is misspecified for our items, every simulated figure is optimistic.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/04_CONCURRENT_VALIDITY_PLAN.md` (23): “Even if it were, simulations assume the Rasch model is correctly specified — that all items discriminate equally and no guessing occurs.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/03_SIMULATION_EVIDENCE.md` (84): “the first passage is identical in 100% of sessions, an exposure/security issue.”
- `grade3-reading/_archive/2026-08-13-consolidation/top-level-docs/HANDOVER_COURSE_EXPERIENCE_PREFLIGHT_2026-08-11.qmd` (255): “- Human-only semantic judgments cannot be minted by a simulated character.”
- `g9/transcript/chat-transcript.redacted.txt` (4946): “The research supports readable text, clear labels and optional help; it doesn’t prove one layout best for learning.”
- `grade3-reading/edullm-review-hub/course-packages/quality/golden-student-course/versions/1.0.0/STANDARD.qmd` (588): “A reviewer walkthrough can diagnose this requirement but cannot substitute for learner evidence.”
- `g9/library/text/L88a690.txt` (58): “How students look at or learn from any of the three. There is no eye-tracking or outcome data.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_CASE_FOR_APPROVAL.md` (198): “**None of it is yet empirical.**”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_CASE_FOR_APPROVAL.md` (230): “• We will not claim: that a proxy score equals a MAP score (Open — that is the linking study's job); that simulated reliability is operational reliability; a RIT gain, a growth multiple, or "proven."”

Against: the same engine found a real structural cliff in a course design, so a simulation is useful for finding structure, not size. Later, 409 real external test records for 173 students turned up, blocked only by an ID crosswalk (`grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md`). Scripted walks still play a lesson as a student, to catch defects in its flow rather than to measure learning (`grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md`). self-reported simulation over about 17,900 sessions gave ability recovery of r = 0.967 and reliability of 0.931, which is simulation rather than a link to real scores (`grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd`, line 39). The same summary reports that a model asked to predict where students will struggle, instead of acting as a student, does better: "Teacher-as-predictor instead reaches r ≈ 0.72–0.79 population-level prediction across three independent research groups" (`grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd`, line 75). the 67% and r≈0.72–0.79 figures are cited second-hand in the notes, without a DOI or URL, and the notes were written while there was no real-student data to calibrate against (`ti-courseplans-audit/docs/generator-insights.md`).

<sub>context · measurement, evidence-of-learning, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Screen reading trails paper for information

Expect comprehension of on-screen informational text to trail paper, more under time pressure, so keep time pressure off on-screen reading and ask for a self-check before showing answers. A meta-analysis of 54 studies found paper beat screen by an effect size of 0.21, with the gap only for expository text.

The Grade 9 desktop design brief cites two meta-analyses. Across 54 studies paper beat screen (g = −0.21), the gap appearing only for expository text and growing under time pressure, with no advantage for digital natives; across 33 studies the gap was g = −0.25 overall, −0.32 for expository text and −0.04 for narrative, and screen readers judged their own understanding less accurately. The brief's implication is to assume informational texts suffer most on screen, remove time pressure and ask for a self-check before showing answers.

Quoted:

- `othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md` (97): “Delgado et al. (2018) meta-analysis, 54 studies: paper beats screen, g = −0.21.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md` (97): “The gap appears only for expository text, grows under time pressure, and digital natives show no advantage.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md` (98): “Clinton (2019), 33 studies: g = −0.25 overall, −0.32 for expository text, −0.04 for narrative.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md` (98): “Screen readers also judged their own understanding less accurately.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md` (99): “Remove time pressure and ask for a self-check before showing answers.”

Published: [Delgado et al. 2018](https://www.edtech.tum.de/dont-throw-away-your-printed-books-why-reading-performance-is-better-on-paper-than-on-screens/) · [Clinton 2019](https://eric.ed.gov/?id=EJ1212958)

Against: The second meta-analysis was read from its indexed abstract after the fetch failed (`othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md`, line 186), and for narrative text the gap was close to zero (−0.04).

<sub>context · stimulus, format · universal · from g9, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Unguarded AI help can harm learning

Unrestricted AI help can raise practice scores while lowering later unaided performance, and in one high-school mathematics experiment guardrails reduced that harm.

The Grade 9 unit's design brief cites a high-school mathematics experiment in which unrestricted GPT assistance improved practice performance while reducing later unaided performance, and in which guardrails mitigated the harm (`g9/transcript/chat-transcript.redacted.txt`, line 3077). The brief reads it as a warning to test independent learning. Its plan for independent practice keeps agents from suggesting interpretations, selecting evidence or improving the answer during the attempt, and records any requested help as assisted before offering a fresh independent attempt (line 2881).

Quoted:

- `g9/transcript/chat-transcript.redacted.txt` (3077): “A high-school mathematics experiment found that unrestricted GPT assistance improved practice performance while reducing subsequent unaided performance.”
- `g9/transcript/chat-transcript.redacted.txt` (3077): “guardrails mitigated the harm.”
- `g9/transcript/chat-transcript.redacted.txt` (2881): “Agents do not suggest interpretations, select evidence or improve the answer during the independent attempt.”
- `g9/transcript/chat-transcript.redacted.txt` (2881): “If the student requests instructional help, we record the attempt as assisted and later offer a fresh independent opportunity.”

Published: [Generative AI without guardrails can harm learning: Evidence from high school mathematics (PNAS, 2025)](https://doi.org/10.1073/pnas.2422633122)

Against: The brief calls it "a warning to test independent learning, not proof of the same effect in English" (`g9/transcript/chat-transcript.redacted.txt`, line 3077): it was measured in mathematics only.

<sub>context · hints, practice, evidence-of-learning · universal · from g9, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>
