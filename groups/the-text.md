# The text and its sources

109 learnings. Each says where it came from and what argues against it. [What a perfect question is](../PERFECT-QUESTION.md) collects the criteria by facet, and [How to generate perfect questions](../GENERATING.md) collects the methods by stage.

### A definition in the word's own form

A definition gives the word's general meaning in the word's own grammatical form, without using the word itself or carrying over details from the text where it appears. Two reviews found an adverb glossed as a verb phrase, a word-form error.

An external audit found one word defined on every visible passage of a lesson as 'very fast and full of anger', with 'fast', it said, borrowed from the story rather than part of the word's meaning (`grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md`). Two reviews found an adverb glossed as a verb phrase, a word-form error (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/PP-STANDING.md`), and a review profile checks that a definition doesn't use the word it defines (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md`, D4.17).

Quoted:

- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (83): “'Furious' is defined wrongly on every visible passage ('very fast and full of anger')”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/PP-STANDING.md` (34): “is a word-form error”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md` (79): “| D4.17 | Distinct target words | PASS | Only 1 word; definition uses "dangerous" (different word); morph gloss uses "menace/harm" (different words). No circular definition. |”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (153): “is PRESCRIBED by the PP3 design DOCX”
- `g9/transformer/src/mechanics/say-it-back.js` (79): “No note uses its own word”
- `g9/transformer/src/mechanics/say-it-back.js` (34): “x.startsWith(norm(w).slice(0, -2))”
- `g9/transformer/src/mechanics/say-it-back.js` (56): “note: its plain meaning here, at most 10 words, without”
- `g9/transformer/src/mechanics/say-it-back.js` (57): “using the word.”
- `g9/transformer/src/mechanics/glossary.js` (87-88): “"note": "what it means in this line, at most 15 words, without using the term"”
- `g9/transformer/src/mechanics/glossary.js` (109): “const usesTerm = (e) => norm(e.note).split(" ").includes(norm(e.term).split(" ")[0]);”
- `g9/transformer/src/mechanics/key-words.js` (78): “check("meanings-no-word", "No meaning uses its word",”
- `g9/transformer/src/mechanics/word-web.js` (68): “check("meaning-no-word", "The meaning does not use the word", !norm(item.meaning).split(" ").includes(norm(item.centre)), "the meaning uses the centre word"),”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “codeChecks: each term is in the sentence; the sentence is at most 16 words; no note uses its own term.”
- `g9/transformer/src/mechanics/key-words.js` (78): “No meaning uses its word”
- `g9/transformer/src/mechanics/word-web.js` (68): “The meaning does not use the word”
- `g9/transformer/src/mechanics/word-web.js` (71): “No key word's meaning uses the word”
- `g9/transformer/src/mechanics/glossary.js` (115): “No note uses its term”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (345-348): “**R-VOC-14b — a morpheme gloss is the morpheme's OWN meaning, not the target word's**: nurse glosses "to care for others" (not "someone who cares for young children" — that imports the target word's context into the part); -ry glosses "a place" (not "a place for it"). The gloss must survive transplanting the morpheme into a different word”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (349): “fixed in `5a48791`”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/INTEGRATION-DISPOSITIONS.md` (18): “Two independent reviewers confirmed that “triumphantly → won with great effort” is a definite word-form error.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/family/meaning-correction/PROPOSAL.md` (7): “That is a past-tense verb phrase, whereas the adverb describes a victorious manner.”
- `grade3-reading/ui-audit-2026-09-08/round-1/g5-u1/PROPOSALS.md` (17): “Define the inflected sense naturally (for example, concealed = kept hidden), or deliberately retain a base-word reference in the definition.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-15.md` (29): “The definition "when you are triumphant, you win a great victory after a hard struggle" is not an authoring error — it is the exact KB-sourced stamp specified in the design document.”

Against: The definition the audit faulted is the one the governing design prescribes, and it was put back to the design's wording until a ruling (`grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md`). A later run found counter-evidence (`grade3-reading/artifacts/arc-audit/REGISTER-2026-09-15.md`).

<sub>criterion · wording · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### A fixed set of must-teach quotations

In a literature unit, fix a set of must-teach quotations, mark them in the reading text, and build each lesson's guided practice on them.

The Grade 9 unit's reading texts mark its must-teach quotations, which it calls store-cupboard quotes, in red bold (`g9/sources/Act 1 reading texts/Act 1/1. 1.1 - Iago_s Introduction - Text.docx`, line 3). A later lesson build's knowledge organiser says its red quotes are each lesson's guided practice quotes and glosses each one as must-know evidence for the unit (`g9/sources/Othello Act 2 Lesson.html`, line 382). No outcome was measured.

Quoted:

- `g9/sources/Act 1 reading texts/Act 1/1. 1.1 - Iago_s Introduction - Text.docx` (3): “Words in red bold are store-cupboard quotes: the must-teach quotes for this unit.”

Against: none found

<sub>criterion · stimulus, practice, alignment · domain · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A glossary pop-up isn't teaching

Don't count a glossary pop-up as teaching a word.

A grade-3 reading rulebook's vocabulary routine says never to target a word the passage explains in place and that a glossary pop-up is never instruction, beside rules to prefer generative words and never to assess a word the turn it was taught. The same routine asks for about 12 productions of each target word per lesson, where a recognition click is not a production. The rulebook says it is grounded in BrainLifts on direct instruction, practice and knowledge, a reading-science corpus and five rounds of rulings from review.

Quoted:

- `grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md` (178-180): “Open frames end in BECAUSE / SO THAT; contrast near-neighbours; never assess a word the turn you taught it; a glossary pop-up is never instruction; prefer generative words; never target a word the passage explains in place.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md` (162-163): “~12 productions per target word per lesson (a recognition click is not a production; speaking counts and beats writing).”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/03-INSTRUCTION-DESIGN.md` (3-4): “BrainLifts (Direct Instruction, Practice, Curriculum & Knowledge), the reading-science corpus”

Against: A content audit of the same course counts a glossary as introducing a word: "The **video transcript counts as delivered instruction** — anything the narration says is introduced, on equal footing with a vocab card or glossary." (`shadow-content-eval/SKILL.md`, line 63), cited on the record teach-a-word-before-using-it. That check asks whether a word was introduced before it was used, not whether it was taught.

<sub>criterion · wording, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A pattern is not a reason

Teach a rule of thumb as a pattern that predicts, not as the reason something happens, because students who take a pattern for a law cannot handle its exceptions.

The chemistry misconception card's model answer calls the octet rule a useful pattern that helps predict which arrangements are stable, but not the reason bonds form, which is always about energy. Its note on exam relevance says students who hold the teleological model cannot handle exceptions to the octet rule, because they believe the octet is a law rather than a pattern.

Quoted:

- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx` (238 (textutil text)): “The octet rule (having 8 electrons in the outer shell) is a useful PATTERN that helps predict which arrangements are stable, but it's not the REASON bonds form.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx` (240 (textutil text)): “Students who hold the teleological model cannot handle exceptions to the octet rule because they believe the octet is a law rather than a pattern.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l1-what-is-an-epic.md` (170-171): “The honest replacement is that the pattern recurs and is worth testing”

Against: One example, and the exam note cites no study for its claim.

<sub>criterion · wording, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A source rich enough for its task

A source must be rich enough for its task, with a distinct part for each question and, when paired, distinct evidence; any false detail or failing question fails the set. One rubric's own case: a 50-word passage cannot support a 4-paragraph argumentative essay.

The evaluator's extended-writing rubric fails a source that is too short, too simple or too similar to the other text to support the evidence the essay needs, and asks that paired texts be substantive and distinct enough to give different evidence perspectives (`shadow/bench/src/inceptbench/prompts/question/ecr_evaluation.txt` lines 157-163). Its reading-level notes add a per-grade minimum length for passages shared by several questions, documented by NWEA for grades 2–5 and advisory for other grades (`shadow/bench/docs/internals/lexile_evaluation.md` lines 47-48). One false detail or one failing question fails the whole set.

Quoted:

- `shadow-bench/src/inceptbench/prompts/question/ecr_evaluation.txt` (157-158): “- The provided source text(s) must be rich enough to support the required essay — a 50-word passage cannot support a 4-paragraph argumentative essay.”
- `shadow-bench/src/inceptbench/prompts/question/ecr_evaluation.txt` (162-163): “- Stimulus fails if it is too short, too simple, or too similar to the other provided text to support the required evidence differentiation.”
- `shadow-bench/src/inceptbench/prompts/question/ecr_evaluation.txt` (160-161): “- For Grade 6–English II (requires both texts): both texts must be substantive and distinct enough to provide different evidence perspectives.”
- `shadow-bench/docs/internals/lexile_evaluation.md` (47-48): “3. **Length floor.** Common-stimulus passages below the NWEA per-grade minimum (grades 2–5 are NWEA-documented; others advisory) fail `length_appropriateness`.”
- `icloud-work/ML learnings/evaluation_methodology.md` (107): “A well-written, historically accurate stimulus can still fail stimulus_quality if it doesn't have enough substance for 3 different questions to reference. The 3 questions must all trace back to specific elements of the stimulus.”
- `icloud-work/ML learnings/evaluation_methodology.md` (54): “One bad detail in the stimulus fails the entire 3-question set.”
- `icloud-work/inceptbench/docs/AP_EVALUATION.md` (141): “Questions must require the stimulus”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq_set.md` (86): “3. **Stimulus too thin**: 30-word stimulus + 4 questions = no question can actually require it. Match stimulus depth to set size.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/services-ib-generator/runtime_assets/ib_satisfaction_kit_v1/generator_prompts/system_prompt_mcq_set.md` (74): “- The set fails if ANY single question fails any metric.”
- `icloud-work/aptraining/artifacts/pending_review/2026-05-22T211855Z_exploits_EXPLOIT-003-mcqset-phrase-anchor/source_report.md` (66-68): “The single failing critical metric is `educational_accuracy`, driven by ≥1 of 3 child questions failing its own MCQ-level checks”
- `icloud-work/aptraining/artifacts/pending_review/2026-05-22T211855Z_exploits_EXPLOIT-003-mcqset-phrase-anchor/source_report.md` (65-66): “Both score exactly at the C=1 N=0 ceiling of 0.84 (rubric INFERIOR range 0.70-0.84).”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_set_evaluation.txt` (163): “If the provided `factual_accuracy failures` count is > 0 → MCQ set factual_accuracy = 0.0”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/mcq_set_evaluation.txt` (164): “If the provided `educational_accuracy failure percentage` is > 20% → MCQ set educational_accuracy = 0.0”
- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md` (101): “- Parent factual accuracy fails if any child has a factual failure.”

Against: The length floor holds only where it is documented: standalone single-item passages have no documented floor and are exempt (`shadow/bench/src/inceptbench/evaluators/guards.py` lines 2586-2587). It was once applied to ordinary standalone passages by mistake, forcing a short at-grade passage of about 66 words to 0.0, and was then limited to passages positively detected as shared (git commit 3c78f22 in `shadow/bench`, lines 29-38). the evaluator's published spec states only that the questions must require the source, and the notes don't record what failure led to the rule. Only factual accuracy is all-or-nothing across the set: its educational accuracy fails only when more than 20% of the questions fail, and shared measures such as stimulus quality pass at an 80% rate (`icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-inceptbench-prompt-audit.md`, lines 102-103).

<sub>criterion · stimulus, demand · universal · from ap · adopted-rule · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### A taught word appears and recurs

Teach only words the learner's own text uses more than once and that come back later in the unit. Before a gate required it, 7 of 9 taught words appeared only once.

A QC week found a Grade 3 lesson assessing the child on a taught word that never appears in its passage (`grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd`, lines 74-76). The project's draft certification standard then made an earned word a build gate, recurring in the passage and in a later unit, after 7/9 taught words had appeared only once (`grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd`, lines 65-66). Review feedback on an earlier version asked for distinct target words, since one lesson's three overlapped and one even appeared inside another's definition, and for support for difficult words beyond the three designated ones (`grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd`, lines 105-106). A word should also be taught in the first lesson that leans on it heavily, not a later one (`grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md`, lines 66-71). Words picked because they look hard mostly fail the recurrence test (`grade3-reading/artifacts/g5-course/VOCAB-DECISIONS-U1.md`, lines 13-25).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd` (74-76): “**Taught word "betrayal" never appears in the L1 passage**”
- `grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd` (65-66): “vocab-earned (taught word recurs in-passage + later unit, from 7/9 taught words appearing only once)”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (106): “Handle difficult words beyond the three designated vocabulary words.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (105): “Choose distinct vocabulary words. In the camouflage lesson, *camouflage*, *adapt*, and *blend* overlap too much; *blend* even appears inside the definition of *camouflage*.”
- `grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md` (69): “unit, counted by word family (R-VOC-7/13 — written after seven of nine taught words turned out”
- `grade3-reading/artifacts/g5-course/VOCAB-DECISIONS-U1.md` (19): “| U1L1 | atmosphere, hydrosphere, geosphere, biosphere | **0 of 4** — each appears once |”
- `grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md` (87): “Across the arc, each target word gets approximately 4–5 exposures, not 6+, and drops out after”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md` (53): “12 of 46 taught words appeared nowhere in their own lesson's”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md` (56): “`oxygen` appears **8× in U3-L1's passage** and 48× in its”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md` (66): “**Teach-before-use:** no word a passage leans on (≥5 hits) may be first taught in a later lesson.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md` (71): “The rule is **first heavy use**, not peak use.”
- `grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md` (62): “self-check: no target word appears inside another target word's definition.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/provenance/DECISIONS.md` (30): “Teach enchanting, menacing, merciless and triumphant as words children use to express an interpretation.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/provenance/DECISIONS.md` (30): “They are deliberately absent from the original prose. Do not insert them into the story to satisfy an encounter-count rule.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/provenance/DECISIONS.md` (30): “Current use appears in independent work, retelling and receipts”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/provenance/DECISIONS.md` (30): “that is not evidence of uniform oral elaboration”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/glossary/HINT-AND-MORPHOLOGY-TRIAGE.md` (30): “Preserve the chosen word and its deliberate absence from the story.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/glossary/HINT-AND-MORPHOLOGY-TRIAGE.md` (31): “Keep the absence-from-passage exemption and pronunciation flow”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (75-76): “**Taught vocabulary sits IN the passage, not drilled into it**: a taught word appears once or twice, in the sentence where it does actual work, never five times for repetition's sake”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (79-80): “This is the passage-side half of vocabulary rule R-VOC-7 below (the word must also recur ≥2x by word family; see §7).”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (270-271): “a taught word must appear in its own lesson's passage more than once, counted by word family; once is a mention, not a meeting”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (273-274): “If the story does not want the word twice, the word is wrong for the story: never bend the story around the card.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (77-78): “a G4 rewrite went from 470 words / FK 4.4 with vocabulary inflation to 793 words / FK 5.6 by removing the inflation and adding subordination instead”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (29): “teach their word as an encapsulating word that is deliberately kept out of the passage so the child is the one who supplies it”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (29): “each carries a named design document waiving this rule on that basis”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/vocabulary-selection-and-generative-items.md` (17): “there are six key word characteristics that should be considered when selecting target words for instruction … Centrality to understanding a text, frequency of use in a text, likelihood of appearing in other content areas, having multiple meanings, containing affixes, and having cross-language potential.”
- `grade3-reading/artifacts/red-team-2026-09-23/PRE-BRIEF.md` (29): “A taught word absent from the passage carries `encapsulating {reason, authority}` | Sanctioned exemption; `validate-vocab-earned` honours it”
- `grade3-reading/artifacts/pp2-v3-design.txt` (40): “Word chosen: MENACING — an encapsulating character word (not in the text), chosen per the KB. It gives the child the language they reach for in Phase 3 to describe Captain Hook, and it is the mandatory magic word in the Phase 3 build.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (29): “Two later lessons in the same arc, L5 ('menacing') and L6 ('merciless'), teach their word as an encapsulating word that is deliberately kept out of the passage so the child is the one who supplies it, and each carries a named design document waiving this rule on that basis;”
- `grade3-reading/artifacts/arc-audit/L5.md` (22): “Encapsulating-word metadata block cites the design doc as authority directly (`"authority": "pp2-v3-design.txt Component 2"`)”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (27): “author it into the passage twice per R-VOC-7, which forces a re-cut of the passage voiceovers because the prose change invalidates the `audio_of` hashes on the story nodes”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (33): “Words live in the passage: taught words appear inside the passage where”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/integration/check-before-final-content.txt` (339): “Vocabulary validation passed: 76 taught word(s), each met more than once in its own passage and again later in its unit.”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (896): “A taught word must appear in the passage the child then reads, more than once, and be reachable there.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/FEEDBACK-RESPONSES.md` (113): “Twelve of the 46 words never actually appeared in their own story, so we wrote”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (272-273): “7 of 9 taught words appeared exactly once when this was first checked”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (29): “Two later lessons in the same arc, L5 ('menacing') and L6 ('merciless'), teach their word as an encapsulating word that is deliberately kept out of the passage so the child is the one who supplies it, and each carries a named design document waiving this rule on that basis”
- `grade3-reading/course-renderer/AGENTS.md` (115-117): “seven of the unit's nine taught words appeared exactly once in the passage they were taught for, and every other validator passed.”
- `grade3-reading/course-renderer/authoring/inputs/rule-packs/reading-g3.json` (281): “R-VOC-7 requires a taught word to appear in its own lesson's passage, and the academics team's design docs deliberately teach ENCAPSULATING words that appear nowhere in the text (the word names what happens, and the child reaches for it in the independent task).”
- `othello-course-renderer-draft/repo/authoring/inputs/rule-packs/reading-g3.json` (281): “the academics team's design docs deliberately teach ENCAPSULATING words that appear nowhere in the text (the word names what happens, and the child reaches for it in the independent task).”
- `othello-course-renderer-draft/repo/docs/rules/vocabulary.md` (147-149): “When the passage does not carry the word twice, the word is still earned if the lesson's own activities use it: the questions, answer options, feedback, sentence frames, the retelling cloze and the recap.”
- `grade3-reading/artifacts/red-team-2026-09-23/PRE-BRIEF.md` (29): “A taught word absent from the passage carries `encapsulating {reason, authority}`”
- `grade3-reading/artifacts/pp1-v3-design.txt` (31): “Word chosen: ENCHANTING — an encapsulating mood word (not in the text), chosen per the KB.”
- `grade3-reading/.claude/skills/lesson-build/SKILL.md` (36-38): “a taught word NOT in the passage gets the sanctioned "encapsulating": {reason, authority} field on the vocab node — validate-vocab-earned honours it and fails loud if the claim is false.”

Against: The gate allows exceptions: a taught word absent from the passage may carry an exemption that names its reason and authority (`grade3-reading/knowledge_bot/knowledge/kb-0224-g3-dialogue-branches-pace-gate-roll-forward-2026-09-22-23.qmd`, lines 89-90). Some designs keep a taught word out of the passage on purpose: the same review's refutation attempt noted words chosen to sum the passage up, absent from it by design and used in the student's own task, with repeated use coming from other activities (`grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md`, line 91). An audit of the same course judged two pairs with heavily overlapping definitions to be deliberate contrast pairs, opposites taught in parallel, and good teaching rather than a defect (`grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/VOCAB-AUDIT.md`, line 51). A later run found: A Grade 3 course's decision record teaches four words for putting an interpretation of a story into words, about a character's manner or a mood, that are deliberately absent from the original prose, and forbids inserting them into the story to satisfy an encounter-count rule; their use comes in independent work, retelling and receipts, which the record says is not evidence of uniform oral elaboration. The same course's published rule says a taught word must appear in the passage more than once (`grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt`, line 896), so for words taught to express an interpretation the two disagree (`grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/provenance/DECISIONS.md`). A later run found: Two later lessons in one arc teach their word as an encapsulating word kept out of the passage on purpose, so the child is the one who supplies it, and each carries a named design document waiving the rule (`grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md`). A later run found counter-evidence (`grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/provenance/DECISIONS.md`). A later run found counter-evidence (`grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md`). A later run found counter-evidence (`grade3-reading/course-renderer/authoring/inputs/rule-packs/reading-g3.json`). A later run found counter-evidence (`othello-course-renderer-draft/repo/authoring/inputs/rule-packs/reading-g3.json`). A later run found counter-evidence (`othello-course-renderer-draft/repo/docs/rules/vocabulary.md`). A later run found counter-evidence (`grade3-reading/artifacts/red-team-2026-09-23/PRE-BRIEF.md`). A later run found counter-evidence (`grade3-reading/artifacts/pp1-v3-design.txt`). A later run found counter-evidence (`grade3-reading/.claude/skills/lesson-build/SKILL.md`).

<sub>criterion · wording, alignment, sequence · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A word card short enough to hold

Keep a word card short: a one-sentence everyday definition of at most 20 words, and a short example and non-example, since each extra clause weakens the contrast. The rule caps a definition at 20 words, an example at 30 and a non-example at 35.

A Grade 3 reading course's published vocabulary rule keeps a card short enough to hold both halves at once: a definition is one sentence of 20 words at most, an example at most two sentences and 30 words, and a non-example at most two and 35, its extra five words for the 'because' another rule requires. Sentences sit in the grade's own band, 11 to 16 words at Grade 4, and a validator checks the limits. The rule adds that when a pair will not fit, the problem is almost never the budget but two sides that have drifted into different scenarios and started explaining themselves.

Quoted:

- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (845): “Keep the card short enough to hold both halves at once”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (848): “A definition is ONE sentence, 20 words at the outside. An example is at most two sentences and 30 words; a non-example at most two and 35”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (848): “Sentences sit in the grade's own band, which is 11 to 16 words at Grade 4.”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (848): “Where a pair will not fit, the problem is almost never the budget: it is that the two sides have drifted into different scenarios and each has started explaining itself.”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (849): “checked by scripts/validate-contracts.mjs”
- `othello-course-renderer-draft/repo/docs/rules/vocabulary.md` (286): “**Rule.** A definition is ONE sentence, 20 words at the outside.”
- `othello-course-renderer-draft/repo/docs/rules/vocabulary.md` (286-288): “An example is at most two sentences and 30 words; a non-example at most two and 35”
- `othello-course-renderer-draft/repo/docs/rules/vocabulary.md` (296-297): “capture the essence of the word and say it in everyday language the child already has.”
- `othello-course-renderer-draft/repo/docs/rules/vocabulary.md` (306-307): “Every extra clause is another place the two sides differ, so a long pair is a weaker contrast, not a more thorough one.”
- `othello-course-renderer-draft/repo/docs/rules/vocabulary.md` (316-318): “A 52-word non-example, which is what the `epic` card carried, is past the point where a nine-year-old can still hold the example it is supposed to be compared against.”
- `othello-course-renderer-draft/repo/docs/rules/vocabulary.md` (327-329): “which fails a definition over one sentence or 20 words, an example over two sentences or 30 words, and a non-example over two or 35.”

Against: The wording principle itself is not machine checkable and stays a review question (`othello-course-renderer-draft/repo/docs/rules/vocabulary.md`, lines 329-331), and no outcome of the limits was measured.

<sub>criterion · wording, accessibility · domain · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Adapt by declared cuts, keep hard facts

When adapting a text for young readers, leave unsuitable material out by declared selection, never silent rewriting, and keep hard facts such as coercion or racism visible without endorsing them.

The rebuilt drama unit retold its play for Grade 5 and recorded that threatened punishments and the inner play's deaths are not dramatized in its selected scenes, a selection it said needs age and content review rather than a hidden rewrite. It kept facts the original leaves uncomfortable, such as a spell never shown removed and one character manipulating another, and its lessons preserve the coercion and uncertainty rather than claiming every character freely chooses the ending. The course's release checklist asks every adaptation for exact provenance, declared changes and an explicit age-appropriate treatment of harmful or dated material. A source audit of another grade adds that leaving chapters out of a short adaptation does not show that a specified cut was carried out.

Quoted:

- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/README.md` (38): “The retelling preserves those limits and avoids presenting coercion as healthy relationship advice.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/README.md` (39): “The introductory unit is not the full play. Threatened punishments and the inner play's deaths are not dramatized in the selected Grade5 scenes. This selection requires age/content review, not a hidden rewrite”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/lesson-02.md` (3): “Preserve the coercion and uncertainty rather than claiming every character freely chooses the ending.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/README.md` (104): “Every adaptation has exact provenance and declared changes; every quote is present; potentially harmful or dated source material has an explicit age-appropriate editorial treatment.”
- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE3.md` (91): “Current short adaptations cannot be claimed to have executed those cuts merely because they omit the corresponding chapters.”
- `g9/sources/Act 1 reading texts/Act 1/1. 1.1 - Iago_s Introduction - Text.docx` (1): “This is the reading text exactly as students see it.”
- `g9/sources/Act 1 reading texts/Act 1/1. 1.1 - Iago_s Introduction - Text.docx` (97): “[Hidden in the dark, Iago shouts crude, racist insults about Othello and Desdemona. Brabantio is horrified. Before he can be seen, Iago tells Roderigo he must leave.]”
- `g9/sources/Act 1 reading texts/Act 1/1. 1.1 - Iago_s Introduction - Text.docx` (266): “a racist insult about Othello. Roderigo will not even use his name.”

Against: A classroom guide in the sources wants the real language confronted as a group: "For this particular scene from Othello, it is important to confront and discuss the racial and racist language as a community of learners. Students need and deserve the chance to tackle the real thing." (`g9/sources/Cutting-a-Scene-Othello-1.1.pdf`, pdftotext lines 34-36). It also expects groups that keep the slurs to treat them seriously rather than make light of them (lines 113-115).

<sub>criterion · stimulus, integrity · universal · from g3, g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Assign a whole text from its lessons

Assign a whole text part by part from the lessons that use it, since a text left in a reader isn't delivered and opening it isn't reading it. A 27-chapter novel sat in one course's reader, assigned from no lesson, until assignment groups in its lessons 1 to 4 covered every chapter exactly once.

An integration review of a rebuilt Grade 5 unit found the complete novel available in the course's reader but assigned from no lesson, and drew a rule from it: availability is not delivery, so lessons link exact chapter assignments and later revisits, the student's work stays in the lesson, and a bookmark never counts as reading completion (`grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/INTEGRATION-LESSONS.md`, line 16). After the repair, assignment groups in lessons 1 to 4 cover chapters 1 to 27 exactly once (`grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/INTEGRATED-READINESS-REVIEW.md`, line 33). The restoration plan and the unit's review both say that access to the full text and recorded assignments are no evidence that a student read it, and a passing navigation test checks that the end of a chapter group returns to the lesson rather than recording completion (`grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/RESTORATION-PLAN.md`, line 80; `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/INTEGRATED-READINESS-REVIEW.md`, line 38; `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/integration/check-before-final-content.txt`, line 689).

Quoted:

- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/INTEGRATION-LESSONS.md` (16): “Full-novel text existed but was not assigned from lessons”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/INTEGRATION-LESSONS.md` (16): “Availability is not delivery. Link exact chapter assignments and later source revisits, preserve work in the lesson tab, and never count a bookmark as reading completion.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/INTEGRATED-READINESS-REVIEW.md` (33): “Assignment groups L1–L4 cover Chapters 1–27 exactly once.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/RESTORATION-PLAN.md` (80): “This is access to the full text, not proof a student read it. No new mastery claim is inferred from opening a chapter.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit1/INTEGRATED-READINESS-REVIEW.md` (38): “Complete source access and recorded assignments are not evidence that a student has finished the novel.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/integration/check-before-final-content.txt` (689): “group boundaries return to the lesson rather than inventing reading completion”

Against: The integration notes say their rules are inferred from reproducible failures in this one rebuild, and that applying them elsewhere is a production judgment (`grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/INTEGRATION-LESSONS.md`, line 30).

<sub>criterion · sequence, stimulus, evidence-of-learning · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Back each category claim with an example

Back every claim a lesson makes about a category with an example the students actually meet in it. One draft unit teaches that a poem can refuse to rhyme, yet all 5 of its poems rhyme.

A draft Grade 4 poetry unit tells students that a poem can rhyme or can refuse to (`downloads/5. Curriculum/Texts/G4 DRAFT/12. Poetry - Narrative and Lyric.docx`, line 285 of its text), yet all five of its poems rhyme: The Highwayman, Lochinvar, My Shadow, Stopping by Woods on a Snowy Evening and I Wandered Lonely as a Cloud (lines 216 and 217 are one rhyming pair). The unit's own texts give students no instance of half of what it teaches. It was first noticed in a review of the unit; the draft itself is the evidence here.

Quoted:

- `downloads/5. Curriculum/Texts/G4 DRAFT/12. Poetry - Narrative and Lyric.docx` (285 (textutil text)): “A poem can rhyme or it can refuse to.”
- `downloads/5. Curriculum/Texts/G4 DRAFT/12. Poetry - Narrative and Lyric.docx` (216 (textutil text)): “Whose woods these are I think I know.”
- `downloads/5. Curriculum/Texts/G4 DRAFT/12. Poetry - Narrative and Lyric.docx` (217 (textutil text)): “His house is in the village though;”
- `grade3-reading/course-renderer/docs/extras/g3-internal-review-2026-08-05.md` (55): “**Which sounds more like a trickster vs being quick or strong**”

Against: none found

<sub>criterion · alignment, stimulus · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Background at the line that needs it

Give background at the line that needs it. Only 6 of 26 background points in my film had to come before the first line.

Finding 7 of the film study (`othello-unit-video/research/FINDINGS.md`): of 26 background points in the script, 6 were
needed before the first line (35 seconds of narration), 11 could go in as notes at the line that first needs them, and
9 only frame the unit; the reading texts already carry all or part of 18 of the 26
(`othello-unit-video/research/data/context-map-totals.json`).

Quoted:

- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md` (54): “no cross-grade science first introduction disguised as Reading background;”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (139): “Only context students will need in Act 1, not general history.”
- `downloads/BrainLift - What makes a good intro video.md` (446): “giving readers the context before an opaque passage transformed comprehension and recall. The same context after did not.”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (28): “Help appears at the step that uses it, never stacked upfront | Support on arrival is clutter; support at the point of use is scaffolding”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/knowledge-scaffolds-bridge-canopy-cap.md` (23): “"At the same time, activating or building background knowledge should take 10 minutes or so."”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/knowledge-scaffolds-bridge-canopy-cap.md` (25): “spent 35 minutes activating and building background knowledge, and then 10 minutes where the kids actually read.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/knowledge-scaffolds-bridge-canopy-cap.md` (27): “"So we really need to be spending the bulk of the time reading."”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/knowledge-scaffolds-bridge-canopy-cap.md` (19): “"asking students to read an easier brief passage before presenting the higher-level text on the same topic"”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (399): “**Pass:** Every technical term used in the script is either (a) defined within the script, or (b) something a typical G7 student would know from general K-6 schooling.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (403): “**Do not fail for:** Terms that the script defines when it introduces them.”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (342): “Vocabulary is taught explicitly and revisited frequently to connect decoding with comprehension, while background knowledge is deliberately built into texts to support understanding and schema formation.”
- `icloud-work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx` (sheet 'Unit 1 Nodes', cell M91): “A short definition of feudalism should be included here.”
- `icloud-work/k_12_social_studies/ap_files/Articles Tracker.xlsx` (sheet 'Sheet9', cell C43): “Not sure if non-religious/non-Protestant students know what this means.”
- `icloud-work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx` (sheet 'Unit 7 Nodes', cell M53): “context for the Senate's vote needs to be included for this to make sense”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (139): “| **Context must be what the text uses.** | Recht & Leslie (1988); Smith et al. (2021) | Only context students will need in Act 1, not general history. |”
- `grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md` (70): “Hard words in passages carry glossary affordance at first occurrence”
- `grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/procedures/Example_Lesson_Components.txt` (7): “A short background-knowledge video plays first, building the knowledge the text takes for granted.”
- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-25-R10.md` (88): “Harm: the lesson's single most title-central term has a definition a child can never tap on the”
- `grade3-reading/ti-courseplans/skills/video-red-team/references/finding-taxonomy.md` (39): “| Term before taught | technical term used before defined | 01_script sequencing |”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (249): “- Failure signals: Unverified exposure assumption; accidental first instruction; support arrives after it is needed.”
- `g9/transformer/src/mechanics/worked-model.js` (39): “context: one sentence on the moment it comes from (who says it, to whom, just after what), without quoting it.”
- `g9/transformer/web/lesson.js` (684): “A line with each term made a hover word where it first appears, as the build's withGloss and Mimicry do.”
- `g9/player/media/Othello-opening-full.vtt` (64): “Knowledge first. Then the reading.”
- `g9/transformer/test/animated.test.mjs` (104): “a glossary exports as lesson.glossary: each term at its script line, matched as the line has it; one per lesson”
- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE5.md` (34): “Current `reader_notice` names racial/class prejudice, disability and health in general, but is inside collapsed details on the reader index. Direct assigned chapters bypass it.”
- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE5.md` (36): “The direct renderer prints it without a preceding contextual component.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/README.md` (104): “Every adaptation has exact provenance and declared changes; every quote is present; potentially harmful or dated source material has an explicit age-appropriate editorial treatment.”
- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE5.md` (43): “Both call for named framing, but their rationale is not identical.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md` (25): “Flagged the need to balance pre-reading context because 10-minute summary videos proved too dense.”
- `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md` (26): “Proposed drip-feeding contextual points dynamically through highlighted info snippets during student reading.”
- `g9/library/text/L37d14b.txt` (13): “The first line of the play text (a character's line or a bracketed stage direction), in lesson order 1.1, 1.2, 1.3, whose sense depends on the point.”
- `g9/library/curation/2026-10-07-marking-test-and-context-map.json` (64): “26 points covering all 434 words: 6 needed before reading (35.0 s), 11 that could move into reading-time notes (66.9 s), 9 framing (58.9 s); without the movable points the film would run about 1:48 (arithmetic, not a render).”
- `g9/library/text/L37d14b.txt` (61): “| film v07 | 26 | 174.542 |”
- `g9/library/text/Lbde498.txt` (23): “Pre-train names, relationships, setting and key terms before the first reading, so working memory is free for the language when students read.”
- `g9/library/text/L37d14b.txt` (5): “The classes describe; they do not recommend.”
- `g9/library/text/L64fb8b.txt` (26): “Proposed drip-feeding contextual points dynamically through highlighted info snippets during student reading.”

Published: [Mayer, Mathias & Wetzell 2002](https://doi.org/10.1037/1076-898X.8.3.147)

Against: learning the names of the key parts first helps
people follow an explanation (Mayer, Mathias & Wetzell 2002, https://doi.org/10.1037/1076-898X.8.3.147), which argues
for at least the names up front. A later run found counter-evidence (`grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/procedures/Example_Lesson_Components.txt`). A later run found counter-evidence (`g9/player/media/Othello-opening-full.vtt`). A later run found: The unit film's brief asks for names, relationships, setting and key terms to be pre-trained before the first reading, citing pre-training research, and the context map says its classes describe and do not recommend (`g9/library/text/Lbde498.txt`).

<sub>criterion · sequence, stimulus · universal · from g9, research · measured · held · found in [2026-10-12-1-seed](../research/2026-10-12-1-seed/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Bound each historical claim

Bound every historical claim by actor, region, period, institution and source function, and say for whom and how far it held, rather than flattening history into a generic narrative.

An AP US History course's BrainLift bounds historical claims by actor, region, period, institution and source function rather than flattening them into generic narratives, as part of a source discipline in which source records keep identity, repository, edition, rights notes and content digests. It reports that the source system was independently audited during authoring for false identities, edition drift, transfer leakage, answer truth, correction routes and alignment to the official course description. It adds that those audits are strong evidence for review but do not close the remaining source-line, rights or academic dispositions, so the rule is adopted, not measured.

Quoted:

- `grade3-reading/edullm-review-hub/course-packages/courses/apush/review/brainlift.html` (164-165): “Historical claims are bounded by actor, region, period, institution, and source function rather than flattened into generic narratives.”
- `grade3-reading/edullm-review-hub/course-packages/courses/apush/review/brainlift.html` (162): “Source records preserve identity, repository, edition or representation boundaries,”
- `grade3-reading/edullm-review-hub/course-packages/courses/apush/review/brainlift.html` (166-167): “The source system was independently audited during authoring for false identities, edition drift, transfer leakage, answer truth, correction-route semantics, and official CED alignment.”
- `grade3-reading/edullm-review-hub/course-packages/courses/apush/review/brainlift.html` (168-169): “Those authoring audits are strong evidence for review; they do not close the remaining named source-line, rights, or academic dispositions.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (71-72): “Do not use a later event as period evidence, invent a direct quotation, treat Indigenous societies as interchangeable, or make the stimulus itself reveal the answer.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (90-91): “Do not imply uniform dependence on slavery, uniform colonial self-government, or one undifferentiated Native response to European settlement.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (110-111): “Do not equate stated ideals with realized rights, collapse Articles and Constitutional powers, or treat ratification as the end of debate about federal authority.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (130-131): “Do not use "democracy expanded" without naming for whom; do not present reform as one unified movement or the Market Revolution as an automatic, single-cause transformation.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (149-150): “Do not reduce the war to a cause-free chronology, treat emancipation as immediate equality, or frame Reconstruction's failure as proof that its legal changes were meaningless.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (169-170): “Do not equate industrial growth with shared prosperity, treat the West as empty land, or describe government as simply absent from the economy.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (189-190): “Do not narrate foreign policy separately from domestic consequences, present the 1920s as uniformly prosperous, or treat the New Deal as either total recovery or no change.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (209-210): “Do not reduce civil rights to one leader or tactic, treat the Cold War as only foreign policy, or infer equal access to postwar prosperity from aggregate growth.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (327): “Unit 1 carries a high risk of flattening distinct Indigenous societies into one culture.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (378): “Each case is bounded to an actor and action.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (380): “This does not replace power analysis with a claim that every actor had equal power.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/SEQUENCING-BRIEF.md inside it) (80): “Evaluate gaps between legal change, political power, and lived conditions.”
- `grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/prompts/u04.md` (56): “U4·L9 — Mass Democracy for Whom?”

Against: none found

<sub>criterion · wording, stimulus, integrity · domain · from ap · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Cap passage sentences near 35 words

Cap a passage sentence for young readers at about 35 words, and build complexity from subordinate clauses rather than from longer or rarer words. Past roughly 30 words, a nine-year-old loses the subject before reaching the verb.

The grade-3 authoring rules cap a single prose sentence at 35 words: past roughly 30 words a nine-year-old loses the subject before reaching the verb, so length stops being complexity and becomes an obstacle. Complexity is to come from subordinate clauses, not longer or rarer words. A grade 4 rewrite went from 470 words at FK 4.4 with vocabulary inflation to 793 words at FK 5.6 by removing the inflation and adding subordination instead.

Quoted:

- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (71): “**A single prose sentence is capped at 35 words**”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (72-74): “past roughly 30 words a nine-year-old loses the subject before reaching the verb, so length stops being complexity and becomes an obstacle. Complexity comes from subordinate clauses, not longer or rarer words.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (77-78): “a G4 rewrite went from 470 words / FK 4.4 with vocabulary inflation to 793 words / FK 5.6 by removing the inflation and adding subordination instead”
- `grade3-reading/artifacts/u4l2-build/g5-audit/G5-BAR.md` (77-78): “G5 complexity in this lesson is NOT long sentences. The FK 4.23 is deliberate — the text reads easy so the *task* can be hard.”

Against: A grade 5 design put its difficulty in the task and the text's structure rather than in its sentences: 'G5 complexity in this lesson is NOT long sentences. The FK 4.23 is deliberate — the text reads easy so the *task* can be hard.' (grade3-reading/artifacts/u4l2-build/g5-audit/G5-BAR.md, lines 77-78).

<sub>criterion · stimulus, wording, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Choose a text that needs the skill

Choose each practice text after the skill it is for, so that the skill is the only way through it, never a text the learner already knows or can guess.

A Grade 3 reading course's teaching-move note, drawn from IES and What Works Clearinghouse practice-guide videos, says to pick the passage after the target strategy and so that the strategy is the only way through, since on a text whose ending the child already knows a prediction lesson measures familiarity, not the skill (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/strategy-text-fit.md`). One of its checks gives the passage to a fresh model with the strategy stripped out: if it still answers the item, the text does not make the strategy necessary.

Quoted:

- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/strategy-text-fit.md` (7): “Pick the passage *after* you pick the target strategy, and pick it so the strategy is the only way through.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/strategy-text-fit.md` (19): “we really want to select a text for teaching that strategy where using that strategy is going to really help you understand the text”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/strategy-text-fit.md` (10): “the item measures familiarity, not the skill”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/strategy-text-fit.md` (27): “if it answers the target item correctly without applying the strategy, the text does not make the strategy necessary.”

Published: [IES practice-guide video, Improving Reading Comprehension in Kindergarten Through 3rd Grade, part 4](https://www.youtube.com/watch?v=ooEq08Gs1IU)

Against: none found

<sub>criterion · stimulus, demand, alignment · universal · from g3, research · external-research · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Claims stay with their speaker

Relay what a speaker in a text claims, insults included, as that speaker's account or prejudice, never as established fact in the lesson's own voice.

The 6 October handover for a Grade 9 unit requires a deceiving character's claim about another character's experience to be identified as his account, not an objectively established narrator fact, and racist insults to be framed as the speakers' prejudice, not adopted by the narrator (line 142); its academic acceptance list repeats that the allegations are not narrated as established truth (line 439). The film treatment lets captions identify only people, place or established facts (`g9/film/TREATMENT.md`, line 7). The rule matters wherever speakers make claims that may be false or self-serving, as in drama and fiction, and plausibly in primary sources.

Quoted:

- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (142): “Iago’s claim about Cassio’s experience must be identified as Iago’s account, not an objectively established narrator fact.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (142): “Racist insults must be framed as the speakers’ prejudice, not adopted by the narrator.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (439): “Iago’s allegations are not narrated as established truth.”
- `g9/film/TREATMENT.md` (7): “Faces and surroundings carry meaning; captions identify only people, place, or established facts.”

Against: none found

<sub>criterion · wording, integrity · universal · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Context on the way into the passage

Show an older text's context note on the route learners actually take, before the passage, and leave the original text unaltered.

In a Grade 5 course built on an older novel, assigned-reading links went straight into a chapter whose original text shows racial prejudice, skipping the course's context notice, which appeared only in a collapsed disclosure on the book's index page. The repair placed the unchanged notice inside each assigned entry, before the original text, and the audit's proposal ruled out silently censoring the original. A browser review then saw the notice above the first selected reading.

Quoted:

- `grade3-reading/ui-audit-2026-09-08/round-1/g5-u1/PROPOSALS.md` (63): “As the student reads beyond the unmarked selection endpoint, the original's racial prejudice appears without the app's existing context notice.”
- `grade3-reading/ui-audit-2026-09-08/round-1/g5-u1/PROPOSALS.md` (65): “renders reader_notice only in the index's collapsed About this older book disclosure.”
- `grade3-reading/ui-audit-2026-09-08/round-1/g5-u1/PROPOSALS.md` (67): “make the already-authored concise reader_notice visible on the actual assigned entry before the learner proceeds into the original.”
- `grade3-reading/ui-audit-2026-09-08/round-1/g5-u1/PROPOSALS.md` (71): “Do not silently censor the original or author that frame as though approved.”
- `grade3-reading/ui-audit-2026-09-08/round-2/g5-u1/IMPLEMENTATION.md` (13): “The unchanged `reader_notice` appears inside the actual selected `p-N` anchor before its original text.”
- `grade3-reading/ui-audit-2026-09-08/round-3/g5-u1/READER-PATH-ACCEPTANCE-by-unit9.md` (13): “The existing older-book notice is visible above selected moment 1 of 6, Chapter 4 paragraphs 18–25.”

Against: A general notice is not preparation for a particular passage: 'The general Secret Garden notice is present, including anchored entries; the remaining gap is specific advance teaching, not a total absence of context.' (`grade3-reading/ui-audit-2026-09-08/round-5/curriculum-verification-2026-09-10/README.md`, line 31).

<sub>criterion · stimulus, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Cut hedges, keep needed quantifiers

Cut vague hedges such as 'maybe' from teaching text but keep the precise quantifiers accuracy needs, such as 'most' or 'some', checking each against the facts.

The grade-7 science script rules separate two kinds of qualifier: vague epistemic hedges such as 'maybe', 'might', 'sort of' and 'kind of' signal uncertainty and add no information, so they are removed, while precise scope quantifiers such as 'most', 'some', 'about a tenth' and 'nearly all' stay wherever accuracy requires them (`grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-generation-v0.1.md`, lines 180-186). Removing a needed quantifier creates a false absolute, and the test given is to delete the word: if the claim becomes false or over-general, the word was required; if only a note of doubt goes, it was a hedge (lines 188-191). In one fix, 'A few, like bacteria, are a single cell' became 'Some, like bacteria, are a single cell', since single-celled life is abundant, not rare, and a sweep of every unit for similar slips found no others needing correction (`grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-qc-evidence-v0.1.md`, lines 445-449).

Quoted:

- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-generation-v0.1.md` (182-185): “REMOVE **vague epistemic hedges** ("maybe", "might", "sort of", "probably", "a little", "kind of") — they signal uncertainty and add no information; KEEP **precise scope quantifiers** ("most", "some", "roughly", "about a tenth", "nearly all", "almost every") that are factually REQUIRED for accuracy”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-generation-v0.1.md` (188-189): “removing a precise quantifier creates a **false absolute** and fails `factual_accuracy`”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-generation-v0.1.md` (190-191): “delete the word — if the claim becomes false or over-general, it was a required quantifier (keep it); if nothing changes but a note of doubt, it was a hedge (cut it).”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-qc-evidence-v0.1.md` (445-447): “`g7-cells-01` "A few, like bacteria, are a single cell" → **"Some, like bacteria, are a single cell"** (single-celled life is abundant, not rare).”

Against: none found

<sub>criterion · wording, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Data keeps its units, kind and precision

Label invented data as invented, keep its units and scale, tell counts, rates, percentages and indices apart, and never let a qualitative model become a number it can't support.

A Grade 5 reading course's generation contract makes this a cross-unit rule for four of its units: a qualitative model cannot silently become a quantitative claim, and invented classroom indices cannot be presented as measurements. The course's passages do use invented data, such as an invented climate-normal table set beside two reports and a relief map, so the rule governs real material. It goes beyond labelling an invented source: the units, the scale and the kind of number stay as stated, and no figure claims more precision than its source supports.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (659): “| XCUT-003 | U1, U2, U4, U9 | A qualitative model cannot silently become a quantitative claim, and invented classroom indices cannot be presented as measurements. | Label invented data, preserve units and scale, distinguish count, rate, percentage, and index, and refuse unsupported precision. |”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/plan-evaluation.md inside it) (44): “original multi-source informational data feature with a separate solved calibration, two reports, invented climate-normal table, and relief map”

Against: none found

<sub>criterion · stimulus, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Deep word teaching only for new targets

Spend taught-word slots only on words new at the learners' grade, not words graded lists put a grade or more below; give others at most a one-line gloss. An audit found two words outside a lesson's pinned target getting the full four-part cycle, one of them a kindergarten-to-grade-3 science word, and both became one-line glosses.

An audit of a Grade 5 reading lesson found two words getting the full deep-teach cycle of example, non-example, word parts and saying it back, though neither was the pinned target word, and one was a K-3 science word a Grade 5 reader almost certainly already knows. The rules it applied say not to pick a word the child already knows, to judge whether a word is new against a reader of the target grade, and to keep light glossing apart from the few words taught for use. The fix demoted both words to one-line tap glosses rather than removing all support.

Quoted:

- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (86-89): “`producer` and `habitat` receive the full blocking-word-style deep-teach cycle (example/non-example/morphology/say-back), but neither is the pinned canonical blocking word — only `decomposer` is — and `habitat` is a K-3 science word a G5 reader almost certainly already knows.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (93-94): “RULE_G3_D4.2 (don't pick a word the child already knows), RULE_G3_D7.11 ("new" judged against a G5 reader), RULE_G3_D4.23 (light glossing vs. the few words taught to production)”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (100-101): “downgrade them to a light non-card gloss (tooltip only, no example/non-example/morphology/say-back cycle) rather than removing all support”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (547-549): “one-line comprehension-support definitions for producer and habitat plus a `_rule` note naming the demotion; only decomposer keeps the full example/non-example/ morphology/say-back cycle (G5-BAR §4 pins exactly one blocking word)”
- `grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md` (101-102): “but that is optional polish, not required by this fix.”
- `grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md` (520-521): “The three word-card slots carry **evidence** and **correspond** as full cards alongside **decomposer**”
- `grade3-reading/course-renderer/docs/rules/vocabulary.md` (28-30): “Where the choice is otherwise free, prefer a word the sheet already tests at this grade, and never spend a card on one it places a grade or more below.”
- `grade3-reading/course-renderer/AGENTS.md` (117-120): “It also reads `content/vocab-word-lists.json`, another curriculum's graded word lists kept as a REFERENCE and not as our scope, and fails a word those lists place a grade or more below this one unless the lesson plan records an `off_list_reason`.”
- `grade3-reading/course-renderer/docs/research/g4-u1-l2-the-cyclops.md` (657-660): “They are words a grade 4 child already holds well enough to read this passage, L1 already used them structurally in the five parts, and neither unlocks a sentence of this text. Teaching them would spend one of three gates on recognition rather than on the words the episode actually turns on.”
- `grade3-reading/course-renderer/docs/rules/vocabulary.md` (24-25): “It belongs to a DIFFERENT curriculum, so it is a reference and not our scope.”
- `othello-course-renderer-draft/repo/docs/rules/vocabulary.md` (28-30): “Where the choice is otherwise free, prefer a word the sheet already tests at this grade, and never spend a card on one it places a grade or more below.”
- `othello-course-renderer-draft/repo/AGENTS.md` (118-120): “fails a word those lists place a grade or more below this one unless the lesson plan records an `off_list_reason`.”
- `othello-course-renderer-draft/repo/docs/rules/vocabulary.md` (24-25): “It belongs to a DIFFERENT curriculum, so it is a reference and not our scope.”
- `othello-course-renderer-draft/repo/docs/rules/vocabulary.md` (34-35): “a taught word that the reference lists place a grade or more below this one fails.”

Against: The audit calls even the light gloss optional: "but that is optional polish, not required by this fix." (`grade3-reading/artifacts/u4l2-build/GRADE5-AUDIT.md`, lines 101-102). How many words get the full cycle stays open: the course's bar pins exactly one, while the shipped lesson carries three full word cards (`grade3-reading/artifacts/g5-deploy/BUILD-NOTES.md`, lines 520-521 and 548-549); see how-many-words-a-lesson-teaches. The lists set a floor, not the choice: "A word earns its place here by unlocking our text (R-VOC-7), which is why `trial`, `departure` and `hospitality` are taught although that sheet lists none of them" (`grade3-reading/course-renderer/docs/rules/vocabulary.md`, lines 25-27). The grading comes from another curriculum. Which words are general academic words (Tier 2), and whether a word unlocks the text, stays a judgement (`othello-course-renderer-draft/repo/docs/rules/vocabulary.md`, lines 35-36). The sources record no measure of what the rule changes for learners, nor of what teaching an easy word costs.

<sub>criterion · wording, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Describe function, never purpose

In science content, say what a thing does and how it happens, never that it exists, acts or changed in order to reach a goal. One lesson's check option changed from 'covered in feathers to fly' to 'that are covered in feathers'.

A cross-subject science synthesis accepts functional description, what a part does, and bans causal teleology, the claim that something exists because of its function; its absolute prohibitions include purpose language for atoms and molecules (`downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx`). One lesson's science sweep reworded a check option to remove purpose-implying wording (`downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 3. The Animal Kingdom - SORT - Lesson Design (v2 - MCQ pauses + science sweep).docx`), and another redefined a taught word in functional terms (`downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 5. Feathers and Scales - CONNECT - Lesson Design (v3 - prototype-aligned).docx`). This is guidance and its fixes; no outcome was measured.

Quoted:

- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx` (145 (textutil text)): “The distinction between functional description and causal teleology must be taught explicitly.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx` (203 (textutil text)): “No teleological language for atomic or molecular behaviour.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 3. The Animal Kingdom - SORT - Lesson Design (v2 - MCQ pauses + science sweep).docx` (209 (textutil text)): “One science fix was made: Sync check 2 option C changed from "covered in feathers to fly" to "that are covered in feathers" to remove purpose-implying (teleological) wording.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 5. Feathers and Scales - CONNECT - Lesson Design (v3 - prototype-aligned).docx` (259 (textutil text)): “The taught word "adaptation" is now defined functionally ("a feature that helps an animal live well where it lives")”
- `grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/sources/GENERATION-CONTRACT.md` (50): “**Functional description OK; causal teleology NOT**”
- `grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/sources/GENERATION-CONTRACT.md` (51-52): “Prompt-design rule: ask "*How* does X help…?" never "*Why did* X develop…?".”
- `grade3-reading/_archive/2026-08-13-consolidation/redteam-g3-round3-report-and-evidence.tar.gz` (RED_TEAM_ROUND3.md inside it) (93-94): “- Showcase U4-L2 defines mimicry as copying "on purpose"; U4-L3 defines adaptation as an individual growing a trait to survive and calls a cactus an animal.”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/subjects/science.md` (10-12): “**No teleology.** Never write purpose into nature: not "feathers to fly," not "in order to survive," not "wants to," not "is designed to." Structures HAVE effects; they were not made FOR them.”

Against: none found

<sub>criterion · wording, stimulus, options · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Exact quotations

Quote exactly, and check every quotation against the text in code.

Every block also gets a house check that every quotation is the text's exact words; a near miss is matched with a 3D
version's own matcher and given the text's wording for the correction (`g9/transformer/src/mechanics/util.js`,
`houseChecks`; `g9/transformer/src/glue/threejs.js`). The film kit's plates quote the text word for word
(`othello-unit-video/kit/docs/STANDARDS.md`).

Quoted:

- `icloud-work/ML learnings/mcq_set_journey.md` (63): “primary source passage attributed to the historical author in the plan”
- `icloud-work/ML learnings/evaluation_methodology.md` (102): “Stimulus doesn't sound like a period-authentic primary source”
- `icloud-work/ML learnings/mcq_set_journey.md` (112): “The training data (raft_combined) itself has fabricated attributions.”
- `grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd` (96): “a 30-char substring "verbatim" check (defeated by paraphrase)”
- `icloud-work/ML learnings/mcq_set_journey.md` (63): “- Output: primary source passage attributed to the historical author in the plan”
- `icloud-work/ML learnings/mcq_set_journey.md` (169): “3. **Attribution is the trap.** Every MCQ_SET needs a historical author and date. The model learned to generate plausible-sounding attributions. Plausible ≠ accurate.”
- `icloud-work/ML learnings/research_rag_factual_grounding.md` (200): “Rather than generating claims freely and optionally citing afterward, the "cite first" constraint forces the model to locate supporting evidence before committing to a claim. This exploits the autoregressive structure: once the model has emitted a citation token pointing to a specific fact, the conditional probability of hallucinating a different fact drops sharply.”
- `icloud-work/ML learnings/research_rag_factual_grounding.md` (204): “Results: Citation grounding improved by **13.83%** on production benchmarks versus standard RAG prompting. However, only ~50% of sentences achieved perfect citation coverage without fine-tuning, suggesting a ceiling that requires SFT to overcome fully.”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (107): “1. Forces explicit selection commitment (anchor_fact in plan JSON = traceable)”
- `icloud-work/ML learnings/prompt_engineering_deep_dive.md` (108): “2. The verbatim copy creates a ground truth to compare against”
- `icloud-work/ML learnings/master_strategy_apr24.md` (34-35): “Before writing any specific date, name, treaty, or event in scoring notes, first write:
[FACT: <copy the exact phrase from VERIFIED FACTS above that supports this claim>]”
- `icloud-work/incept/inceptbench/src/inceptbench/tools/factual_accuracy_audit.py` (132-134): “- Claims that a specific passage, quote, or description is "not found in" or
    "does not match" a named primary source. You do not have reliable verbatim
    recall of historical texts and cannot verify what a source does or does not say.”
- `icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-04T1430Z_v40h_spot_verify.md` (116): “The model appears to have **appended a sentence designed to align the source content with the lesson topic**.”
- `icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-04T1507Z_v40h_mcq_set_n30_fabrication_audit.md` (51): “**Zero rows** in either model produced verifiable, unmodified primary-source stimuli.”
- `icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-04T1507Z_v40h_mcq_set_n30_fabrication_audit.md` (38): “29 of 30 v40h rows are IB false-positives.”
- `icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-04T1507Z_v40h_mcq_set_n30_fabrication_audit.md` (61): “Paraphrase presented as direct quote.”
- `icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-04T1507Z_v40h_mcq_set_n30_fabrication_audit.md` (76): “Under a more lenient reading where "directionally accurate paraphrase = fine," the rate would be lower”
- `icloud-work/auto-memory-backup/project_dbq_floor_is_data_veracity.md` (44): “- 50/50 have exactly 7 documents (100% structural compliance)”
- `icloud-work/auto-memory-backup/project_dbq_floor_is_data_veracity.md` (47): “- **Document TEXT is unverified.** The teacher generation pipeline (`raft_combined.jsonl`) is itself LLM-produced; the quoted content from real authors is **plausible-but-likely-fabricated**.”
- `icloud-work/auto-memory-backup/project_dbq_floor_is_data_veracity.md` (20): “| **factual_accuracy** | **28** | **56%** |”
- `icloud-work/auto-memory-backup/project_dbq_floor_is_data_veracity.md` (27): “| **factual_accuracy** | **26** | **62%** |”
- `icloud-work/auto-memory-backup/feedback_no_hallucination_in_training_data.md` (25): “1. **Document text** must be verbatim or near-verbatim quotation from a citable primary source.”
- `grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd` (96): “`word_count`/Lexile and a 30-char substring "verbatim" check (defeated by paraphrase).”
- `grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd` (97-98): “independently recompute Lexile, word_count, hot-text/EBSR spans (NFKC exact-match against the tokenized passage)”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md` (14): “every quoted span in think-aloud states / write_up / extra-thinking / frames must be a verbatim story slice”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md` (57): “checkStagedModel requires `beats[2].reveal[1]` wrapped whole in curly quotes”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md` (57): “is a CONTRADICTION, not a fix”
- `grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd` (95-99): “they trusted generator-asserted `word_count`/Lexile and a 30-char substring "verbatim" check (defeated by paraphrase). Our contract has the same shape. Action: independently recompute Lexile, word_count, hot-text/EBSR spans (NFKC exact-match against the tokenized passage), answer-checkability at intake; any self-reported field used as a gate is UNVERIFIED.”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (393): “All quotes need checking against the chosen edition.”
- `grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd` (39): “Pin the edition to Folger.”
- `grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd` (330-332): “General citation-fabrication research found roughly two-thirds of ChatGPT-generated bibliographic citations invented or wrong (Nature Sci Rep, 2023, ~400-paper audit)”
- `grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd` (335-336): “**This is the single highest-confidence risk in this file** — a general, high-base-rate LLM property, not a possibility.”
- `grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd` (358): “Add a **mandatory quote/claim verification step** — anything voiced as a quotation or historical fact from the text is checked against the actual Othello text every time, not spot-checked.”
- `grade3-reading/ti-courseplans/docs/reading-science/EXTRACTION_EVIDENCE.qmd` (32): “230/230 extracted quotes verified verbatim at extraction time”
- `grade3-reading/ti-courseplans/docs/reading-science/EXTRACTION_EVIDENCE.qmd` (36): “Zero fabricated quotes survived the pipeline.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/IES-CORPUS-REVIEW-2026-08-05.md` (25-26): “every distinct source attribution was **grep-verified against the actual transcript on disk**”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/IES-CORPUS-REVIEW-2026-08-05.md` (29): “**~49 distinct sources checked; 49 verified.** Zero fabrications.”
- `grade3-reading/ti-courseplans/docs/reading-science/EXTRACTION_EVIDENCE.qmd` (34-35): “The four EduQwen checks establish presence in the scoped extraction only, not full-paper coverage.”
- `grade3-reading/ti-courseplans/docs/reading-science/EXTRACTION_EVIDENCE.qmd` (39): “**Boundary spot-checks** (does each extraction reach the document's true end?):”
- `ap-helpers-data-agent-memory/recipe_track_a_b_kc_pack_substitution.md` (11): “Even when grounded in a real OpenStax `_GROUND_TRUTH_SOURCE_` excerpt in the prompt, output documents are stylistic-real not literal-real.”
- `ap-agent-memory/feedback_d13_inference_injection_partial_fix_2026_05_12.md` (26): “- Success rate at "use docs literally" is ~20% on v43-soup (1 of 5 graded)”
- `icloud-work/incept/inceptbench/src/inceptbench/tools/factual_accuracy_audit.py` (133-134): “You do not have reliable verbatim
    recall of historical texts and cannot verify what a source does or does not say.”
- `icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_oracle/2026-05-04T1507Z_v40h_mcq_set_n30_fabrication_audit.md` (38): “29 of 30 v40h rows are IB false-positives. The IB grader passes essentially every MCQ_SET row regardless of stimulus authenticity.”
- `icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-05T1225Z_v41_d13_stimulus_provenance_audit.md` (21): “**30/30 v41-d13 MCQ_SET stimuli (100% of BAML≥0.85 filtered set) classify FABRICATION_OR_NOVEL_SOURCE** against Atlas's 569-doc primary-source corpus pool.”
- `icloud-work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md` (83): “While Ricci's journals are real, this stimulus is a paraphrase/reconstruction rather than a direct quotation.”
- `icloud-work/ap-social-studies-generator/python/CLAUDE.md` (130): “Fabricated poem falsely attributed to Wilfred Owen”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt` (54-55): “answer choices must be verbatim spans from the stimulus. Ellipses are allowed only for shortening; paraphrased or fabricated options fail `specification_compliance`”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md` (246): “| Dim 14: EBSR Part B verbatim | Part B options are verbatim passage sentences (EBSR only) | Hard gate |”
- `grade3-reading/knowledge_bot/knowledge/kb-0115-reading-science-folder-2026-07-10.qmd` (58-59): “Full texts attached by file copy, never re-emitted through a model”
- `icloud-work/aptraining/helpers/data/output/v18_rebuild_scope.md` (54-55): “4. **Atlas verify** (free) — every source URL must 200; every passage must substring-match the verified URL's body.”
- `grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd` (67): “the model fabricated a second occurrence it then quoted back verbatim”
- `grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md` (58): “Quoted spans verbatim in the passage”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (87): “Nudge quotes words not in the story”
- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R3.md` (10): “193 paragraphs, 1 deviation”
- `grade3-reading/artifacts/decision-matrix/slices/07-SCORING-FEEDBACK-XP.csv` (20): “ScrItem's quote gate requires 95% token-window similarity against candidate lines”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md` (163-164): “Treat lifecycle `quote-integrity` findings as blocking. A prompt that asks for a quotation requires one unique contiguous passage match after only Unicode, whitespace, and punctuation normalization.”
- `grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd` (95-96): “they trusted generator-asserted `word_count`/Lexile and a 30-char substring "verbatim" check (defeated by paraphrase).”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/IES-CORPUS-REVIEW-2026-08-05.md` (121): “116 of 116 confirmed as real substrings, zero invented.”
- `ti-courseplans-audit/docs/reading-science/EXTRACTION_EVIDENCE.qmd` (32): “230/230 extracted quotes verified verbatim at extraction time”
- `grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd` (70): “exact-quote grading must fail closed (a botched quote was accepted)”
- `grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd` (330-331): “roughly two-thirds of ChatGPT-generated bibliographic citations invented or wrong”
- `grade3-reading/knowledge_bot/knowledge/kb-0067-g5-generator-pilot-intake-and-team-async-2026-06-23.qmd` (275): “The adapter only marks Part B as evidence if the option text resolves against the stimulus text.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx` (271 (textutil text)): “Blank A: must match one of the 3 evidence quotes.”
- `downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx` (333 (textutil text)): “All re-checked against the story text.”
- `grade3-reading/ti-courseplans/docs/reading-science/EXTRACTION_EVIDENCE.qmd` (32-36): “230/230 extracted quotes verified verbatim at extraction time”
- `shadow-content-eval/README.md` (61): “every visible passage is the fixed source text word for word”
- `shadow-curriculum/.agents/skills/curriculum-pr-review/SKILL.md` (58): “check the literal characters around the suspect position with `python3 -c` and `repr()` if needed (e.g. confirming a space is `U+0020`, not `U+00A0` NBSP — that one bit us in a real review).”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (105): “- `dynamic_source_gate_mcqset_v2`: MCQ_SET regressed to 0.0 because generated questions referenced phrases not present in the enforced stimulus (`system of checks and balances`, `supreme law of the land`).”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (98): “- MCQ_SET validator now rejects quoted phrases in child questions/explanations when those phrases are absent from the enforced stimulus.”
- `g9/transformer/src/glue/threejs.js` (53): “Is this quotation the text's exact words? Its quotedLines: punctuation, case and apostrophes aside, never across a”
- `g9/transformer/src/glue/threejs.js` (54): “stage direction or two speeches.”
- `g9/transformer/src/mechanics/worked-model.js` (75): “the quote is not an exact quotation from the text (within one speech)”
- `g9/transformer/src/text.js` (52): “Find a quotation in the text. It may span consecutive lines.”
- `g9-transformer-runs/blocks/f23aebacf033daa2.json` (13): “How do the details of a wrinkled lip and sneer of cold command suggest a ruler who also possessed great passion?”
- `g9/transformer/samples/ozymandias.md` (6): “And wrinkled lip, and sneer of cold command,”
- `g9-transformer-runs/blocks/f23aebacf033daa2.json` (28): “Each push-back quotes the text: a push-back quotes no words from the text”
- `g9-transformer-runs/blocks/aeb043df247f1b45.json` (17): “How can speech matter if the world will little note, nor long remember what we say here?”
- `g9-transformer-runs/blocks/be97f27fc4c4a65a.json` (8): “The world will little note, nor long remember what we say here, but it can never forget what they did here.”
- `g9/transformer/src/mechanics/debate.js` (51): “24 words, that quotes a few exact words from the text in double quotes”
- `g9/transformer/src/mechanics/util.js` (63): “A quotation cut with an ellipsis whose every part is the text's own words is a fair elision, not a near miss.”
- `g9/transformer/test/quotes.test.mjs` (44): “each part of an elided quotation is checked on its own”
- `g9/transformer/src/mechanics/util.js` (57-58): “The item's own wording, which a line of its feedback may quote: its options, stem, claim and the like (the pool rule … These are checked against the text alone.”
- `g9/transformer/test/quotes.test.mjs` (48): “an item's own string is checked against the text, and cannot pass its own quotation”
- `g9/transformer/test/quotes.test.mjs` (42): “a source the mechanic declares (a film's narration)”
- `g9/transformer/src/mechanics/util.js` (66): “a span with an editorial [bracket] left alone”
- `g9/transformer/test/quotes.test.mjs` (43): “two words are too few to call a quotation”
- `g9/transformer/src/glue/animated-judge.js` (33): “The units a quotation covers, if it is long enough to count: three words, or a whole short line.”
- `g9/transformer/src/glue/threejs-archivist.js` (39): “The units a quotation covers, if it is long enough to count: three words, or a whole short line.”
- `g9/transformer/src/mechanics/util.js` (65): “Quotations that are neither the text's exact words nor the item's own: a span of three words or more in quotation”
- `g9/transformer/src/glue/threejs-archivist.js` (226): “evidence: exact.length > 0 || near.length > 0”
- `g9/transformer/src/glue/threejs-archivist.js` (207): “the text, exactly or nearly: the page puts its own wording note on a near one), the rest Jev; one sentence's job is a”
- `g9/transformer/src/glue/threejs.js` (45): “The quoted spans in a string, two words or more (its quotesIn: double, curly or single quotes).”
- `g9/transformer/src/glue/threejs.js` (63): “Quotations of three or more words that are nearly, not exactly, the text's (its nearQuotes): [{ wrote, line }].”
- `g9/transformer/src/glue/threejs.js` (54): “stage direction or two speeches. Without its tools, src/text.js findQuote, so a missing mirror never passes a quote”
- `g9/transformer/src/text.js` (52): “Find a quotation in the text. It may span consecutive lines. Returns the unit indices it covers, or null.”
- `g9/transformer/src/text.js` (56): “const ls = spoken(text);”
- `g9/transformer/test/quotes.test.mjs` (28): “quoting one of its options passes”
- `g9/transformer/src/mechanics/util.js` (9-10): “so quote a few of the words instead. Anything in quotation marks is the text's own words, copied exactly, in double quotes: never put a paraphrase in quotes.”
- `g9/transformer/test/quotes.test.mjs` (59): “without the 3D build's mirror the quotation check still runs, on src/text.js findQuote, and never passes for lack of it”
- `g9/transformer/src/glue/threejs-render.js` (182): “its word is not in its line as written”
- `g9/transformer/src/server.js` (211): “the text is kept by its hash, so the judge endpoint can settle quotations against it in code”
- `g9/transformer/src/glue/animated.js` (136): “the build marks a phrase where the question has it, word for word”
- `g9/transformer/src/mechanics/film-check.js` (25): “// the film's own words may be quoted (houseChecks: a quotation is the text's, the item's own, or one of these)”
- `g9/tools/unit-video-essay/QA.md` (16): “The Shakespeare quotations and Act/Scene labels match”
- `g9/transformer/test/quotes.test.mjs` (28): “an invented quotation holds a quick check; an exact one passes; quoting one of its options passes”
- `g9/transformer/src/mechanics/util.js` (9-10): “Anything in quotation marks is the text's own words, copied exactly, in double quotes: never put a paraphrase in quotes.”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “A quotation made up outright passes, because nearQuotes gives nothing for a quote nowhere near the scene.”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “A quote across two speeches never matches, a limit of the 3D build's matcher.”
- `g9/transformer/src/mechanics/util.js` (57): “The item's own wording, which a line of its feedback may quote: its options, stem, claim and the like (the pool rule”
- `grade3-reading/curriculum-gen/checks/KNOWN-LIMITS.md` (15-16): “the check cannot tell a faithful paraphrase from an invented claim — both fail the string match.”
- `grade3-reading/curriculum-gen/checks/KNOWN-LIMITS.md` (18-19): “This is the limit, not a bug to fix: loosening the match to fuzzy similarity would let through exactly the defect the class exists for.”
- `grade3-reading/curriculum-gen/checks/KNOWN-LIMITS.md` (21-22): “a two-word difference that a similarity threshold generous enough to admit real paraphrase would also admit.”
- `grade3-reading/curriculum-gen/checks/check-claim-fidelity.mjs` (29-30): “The content mixes curly and straight quotes, en/em dashes and unicode ellipses, so a naive === comparison fails on correct content.”
- `grade3-reading/curriculum-gen/checks/check-key-integrity.mjs` (30-31): “The content uses curly apostrophes and smart quotes. Every comparison in this file runs on normalised text; naive comparison silently fails on them.”
- `grade3-reading/curriculum-gen/test/run.mjs` (51): “Normalisation must not turn a correct quote into a finding.”
- `incept-package-hub/.artifacts/source/Grade 5 Reading - Complete Course Review.zip` (Grade 5 Reading - Complete Course Review/audit/full-course-review-red-team-interim-2026-07-20.md inside it) (40): “The downstream Course JSON quote-integrity gate exposed and rejected one exact-quote collision in `G5-U7L3-I05`”
- `incept-package-hub/.artifacts/source/Grade 5 Reading - Complete Course Review.zip` (Grade 5 Reading - Complete Course Review/audit/full-course-review-red-team-interim-2026-07-20.md inside it) (40): “`U7L3-S23` (`then stops.`) was duplicated inside `U7L3-S30`.”
- `incept-package-hub/.artifacts/source/Grade 5 Reading - Complete Course Review.zip` (Grade 5 Reading - Complete Course Review/audit/full-course-review-red-team-interim-2026-07-20.md inside it) (40): “The source was repaired without changing the keyed span”
- `incept-package-hub/.artifacts/source/Grade 5 Reading - Complete Course Review.zip` (Grade 5 Reading - Complete Course Review/audit/full-course-review-red-team-interim-2026-07-20.md inside it) (40): “the bound quote now occurs exactly once”
- `grade3-reading/ti-courseplans-wiki/Peter-Pan-Quality-Case-Study-2026-08-24.md` (151-152): “A think-aloud presented a quotation that was not the exact printed sentence. Capitalization and sentence boundaries made the paraphrase look verbatim.”
- `grade3-reading/_archive/2026-08-13-consolidation/council-human-handover-2026-08-13/03_AUDIT_FINDINGS_AND_OPEN_RISKS.md` (19): “Earlier validation checked the shape of a SHA-256 and a non-empty quote but did not prove that the reference resolved to exactly one frozen evidence item or that the quote existed in those bytes. A reproduction using an invented path/hash/quote produced no validation error.”
- `g9/sources/Othello Unit Video_ Info Sheet for Devfactory.md` (64): “All quotes are word for word from the Folger Shakespeare text (CC BY-NC 3.0). Please do not paraphrase them on screen.”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (142): “Every quote in this workbook was checked word for word against the Folger text of 1.1–1.3.”
- `othello-archive/sources/act1/KB - Overview.csv` (142): “Every quote in this workbook was checked word for word against the Folger text of 1.1–1.3.”
- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/research/IDEA-SYNTHESIS.md` (26-27): “2. **Invented quotes.** Near-certain without a check: every quote an AI voice speaks must be verified against the edition's text before it is voiced.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (410): “Shakespeare’s quotation text is read-only, accurately attributed, and complete.”
- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L6-2026-09-05.md` (37-38): “matches passage p11 exactly, and is validated by `kind: "quote"` (forces literal match), not free text.”
- `grade3-reading/.claude/skills/lesson-build/SKILL.md` (66-67): “quotes verbatim from the passage — paraphrase fails validate-passage-refs.”
- `grade3-reading/artifacts/g5-deploy/EVALUATION-API.md` (39): “`quote_tap` fails closed — only an exact, unmangled quote is accepted”

Against: A later run found: In the reading engine a contract requires a modelled inference in a reveal beat to be wrapped whole in curly quotes; the clash with exact quotation was recorded as a contradiction awaiting a ruling, and the lessons kept the quote marks (`grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md`). A later run found counter-evidence (`grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md`). A later run found: in a 3D version's paragraph task the lesson engine counts as evidence an exact quotation of two words or more, or one of three words or more that is only nearly the text's (`g9/transformer/src/glue/threejs-archivist.js`). A later run found counter-evidence (`g9/transformer/test/quotes.test.mjs`). A later run found counter-evidence (`g9-transformer-audit/2026-10-09-best-of-everything.json`).

<sub>criterion · stimulus, integrity · universal · from g9 · adopted-rule · held · found in [2026-10-12-1-seed](../research/2026-10-12-1-seed/), [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Examples easier than the word

Teach a new word with examples from outside the text, easier than the word itself, that don't give away what happens in the text.

A review profile checks that a vocabulary card's examples go beyond the story (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md`, D4.6). A card's example that told the ending before the part was read was rewritten as an everyday one (`grade3-reading/artifacts/feedback-vocab-design-2026-09-21/REGISTER.md`; `grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21/index.html`), and a live walkthrough found example words sharing the taught word's ending that were harder than the word, and called for easier ones (`grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md`).

Quoted:

- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md` (70): “| D4.6 | Examples beyond story | PASS |”
- `grade3-reading/artifacts/feedback-vocab-design-2026-09-21/REGISTER.md` (20): “told the ending before the part is read”
- `grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md` (25): “same-ending examples harder than the word”

Against: none found

<sub>criterion · wording, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Examples the learners already know

Use examples, units and references the target learners know, or explain them; universal experiences and widely used teaching cases are fine anywhere.

The evaluator's script rubric fails examples or cultural references likely to be unfamiliar or inappropriate for the stated grade and subject, among them units of measurement used without explanation where the lesson has no international context, and examples that assume a heavily urban or heavily rural setting (`shadow/bench/src/inceptbench/prompts/video_script/evaluation.txt` lines 461-466). It doesn't fail references to universal human experiences or internationally recognised teaching cases (lines 468-471).

Quoted:

- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (461): “**Fail:** Examples or cultural references are likely unfamiliar or culturally inappropriate for the stated grade/subject context.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (464): “- Using a non-US unit of measurement (e.g., stones for weight, kilometres when the lesson has no international context) without explanation”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (466): “- Examples that assume a specific regional context (heavily urban or heavily rural) in a way that excludes large portions of the student population”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (470): “- References to universal human experiences (eating, breathing, growing, seeing the sun)”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (471): “Standard curriculum examples that are internationally recognised teaching cases”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (92): “it may not name an unintroduced PERSON”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (93): “teaches them they missed something.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (94): “Introducing a name inline ("a doom called Ragnarok") is fine and is how to do it deliberately.”

Against: none found

<sub>criterion · wording, accessibility · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Fit a text's cohesion to what readers know

Match how explicit and connected a text is to its readers' knowledge: highly cohesive texts help readers new to a topic but can lower deeper understanding for knowledgeable readers.

The reading project's evidence base lists the interaction of text coherence and prior knowledge in its authoring tier, for designing a ladder of text difficulty (`grade3-reading/knowledge_bot/skills/reading-science/PRIORITIES.qmd`). Its digest of the RAND Reading Study Group's 2002 report quotes both halves: for readers with little knowledge of the topic, texts with high coherence consistently produced higher scores than texts with low coherence, while for readers with much knowledge a coherent text base slightly enhanced recall but lowered performance on tests that tapped the mental model (`grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd`, claims 69 and 70, pp. 107-108).

Quoted:

- `grade3-reading/knowledge_bot/skills/reading-science/PRIORITIES.qmd` (58-59): “The coherence x knowledge text-tuning interaction (high-coherence texts help low-knowledge readers; can under-stretch high-knowledge readers on deep measures).”
- `grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd` (425): “For these readers, texts with high coherence consistently produced higher performance scores than texts with low coherence.”
- `grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd` (431): “A coherent text base slightly enhanced recall, but actually lowered performance on tests that tapped the mental model.”

Published: [RAND Reading Study Group 2002, Reading for Understanding (MR-1465)](https://www.rand.org/pubs/monograph_reports/MR1465.html)

Against: none found

<sub>criterion · stimulus, demand · universal · from research, g3 · external-research · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Fit each course to its grade and test

Set a course's passage lengths, genre mix and demands from its own grade and test, building toward that test's reading load, rather than porting a sibling course's harder texts. One course's practice passages ran 58 to 217 words where its test presents about 2,740 across several passages.

The course plans' rejection lessons record that a third-grade course's passages ran 58–217 words when the test is multi-passage at about 2,740 words, so length has to ramp toward test stamina, and that its texts were flagged at about 22% literary against a target of about 40% because they were picked on Lexile alone, so genre balance is a design commitment, not a backfill (`grade3-reading/ti-courseplans/docs/course-formula-agents.md`). Their grade-band register requires a course to be demonstrably different from its siblings on text band, stamina, genre split, item formats, rigor, gate design and other dimensions, with grade-specific sources (`grade3-reading/ti-courseplans/docs/grade-band-profiles.md`), and a rule from a seventh-grade BrainLift differentiates adjacent grades by the knowledge and operation learners must master rather than cloning a sibling course with harder text (`grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json`, RHBL-023). Its reading lengthens from the start toward the test's load, long and paired passages included, because short passages alone do not build sustained reading.

Quoted:

- `grade3-reading/ti-courseplans/docs/course-formula-agents.md` (224): “G3 passages were 58–217w when the test reality is multi-passage (~2,740w); ramp length toward test stamina”
- `grade3-reading/ti-courseplans/docs/course-formula-agents.md` (166): “G3 was flagged at **~22% literary vs ~40% target** because texts were picked on Lexile alone”
- `grade3-reading/ti-courseplans/docs/grade-band-profiles.md` (8-9): “> A course for grade N must be **demonstrably different** from its siblings on the > dimensions below”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json` (416): “Differentiate adjacent grades by the knowledge and operation learners must master rather than cloning a sibling course with harder text.”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (69): “Course passages run 58 to 217 words, averaging about 166”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (69): “A child can master the whole course one short snippet at a time and never once sustain attention across a multi-passage block.”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (67): “STAAR presents up to roughly 2,740 words across two single passages and one paired set”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (71): “Add longer passages and paired-text sets that build toward test-length and real-world reading.”
- `grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md` (67): “poetry/drama and reading-stamina strands”
- `ti-courseplans-audit/docs/course-formula-agents.md` (224): “G3 passages were 58–217w when the test reality is multi-passage (~2,740w); ramp length toward test stamina”
- `ti-courseplans-audit/docs/course-formula-agents.md` (223): “correct grade setting, age screen, WCAG, genre/domain balance, stamina lengths, tag audit.”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (94): “Practising only on very short texts does not build that stamina.”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (94): “Course passages run 58 to 217 words, averaging about 166.”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (92): “STAAR presents up to roughly 2,740 words across two single passages and one paired set”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md` (114): “The CCSS emphasis on informational text applies to classroom reading volume, not assessment blueprint.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/skill/SKILL.md` (53): “**Passage lengths to MAP spec:** literary 400–600 words · informational 250–500 words”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/skill/SKILL.md` (53): “KNOWN CURRENT VIOLATION: all 460 bank passages are ~¼ target length”
- `grade3-reading/course-renderer/docs/rules/content-and-copy.md` (255-258): “"A child can master the whole course one short snippet at a time and never once sustain attention across a multi-passage block." STAAR Grade 3 "presents up to roughly 2,740 words across two single passages and one paired set."”

Against: The same register still marks the stamina rows for grades 2 to 5 [TO SOURCE], so the target lengths themselves are not yet set (`grade3-reading/ti-courseplans/docs/grade-band-profiles.md`). The evidence is one course's gap; nothing here measures what longer passages did for scores.

<sub>criterion · stimulus, alignment, sequence · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Fit the documents to the question

Every document in a set bears on its question, together they cover the time and place it asks about, and their differing viewpoints support more than one defensible argument.

Failures of document tasks in public runs were repaired by adding missing decades and dissenting documents to foreign-policy rows, and by replacing documents on the wrong aspect of a question, such as social and global legacy documents on a route about why one side won (delivery notes of 24 May 2026). One task rose from 0.55 to 0.70 to 1.0 after, among other changes, documents from an under-represented perspective were added (23 May 2026). Their distinct provenance and opposing points of view, dissent included, are what make more than one argument possible, since a redundant, one-sided or neutral, list-like set fails.

Quoted:

- `icloud-work/aptraining/workspace/comms/from_den/2026-05-24T0208Z_DELIVERED_unit4_dbq_solver_v1_candidate.md` (30): “foreign-policy rows lacked 1830s/1840s coverage and dissenting documents”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-24T0102Z_DELIVERED_unit3_dbq_solver_v1_candidate.md` (29): “American-victory hard route used social/global legacy docs”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T1958Z_DELIVERED_unit1_dbq_solver_v1_candidate.md` (73): “Cultural perspective row improved 0.55 -> 0.70 -> 1.0 after replacing summary docs with source-like excerpts and adding Indigenous-perspective documents.”
- `icloud-work/aptraining/workspace/comms/from_data/2026-05-07T1130Z_v45_failure_analysis.md` (77): “5 items are chronic across v29, v43, and v45 (all < 0.85 or majority fail in every model tested).”
- `icloud-work/aptraining/workspace/comms/from_data/2026-05-07T1130Z_v45_failure_analysis.md` (84): “| 60433 | c_01hF | Documents only cover 1960-1966 but prompt asks 1960-1980 (missing 14 years) | 0.55 | 0.49 | 0.26 |”
- `icloud-work/aptraining/workspace/comms/from_data/2026-05-07T1130Z_v45_failure_analysis.md` (87): “**Pattern:** Every chronic fail is a DBQ with either (a) fabricated primary-source attribution/date, or (b) severe temporal/geographic omission in the document set. These are data-veracity bound — the model invents or truncates documents.”
- `icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-04T1430Z_v40h_spot_verify.md` (138): “Doc 4 alone is sufficient to fail this DBQ.”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/dbq_evaluation.txt` (54): “- Score 1.0: Every document can be used to support, complicate, or inform an analysis related to the prompt”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/dbq_evaluation.txt` (60): “- Score 0.0: All documents point to one obvious conclusion; no real analysis or argumentation is possible”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/raw_rubrics/dbq_evaluation.txt` (44): “- Score 1.0: Multiple documents have clear perspective, purpose, or context that students can analyze; sourcing/analysis opportunities exist”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (448): “- DBQ `medium-7`: individual-liberties document pack was accurate but redundant and one-sided.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (450): “- Targeted proof: `dynamic_32b_full_failed_export_v1_dbq_medium7_repaired_v28` scored 1.0.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md` (2008): “rows 61-62 DBQ hard/medium failed because the documents were too neutral and list-like for sourcing analysis,”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/production_all_units/RUNNING_SUMMARY.md` (2010): “- Source commit `2d07c05` (`Repair Unit 1 environment DBQ and MCQ set`) changes the environment DBQ documents into sourceable accounts with distinct provenance and rewrites the c_9eQY MCQ_SET route away from direct artifact matching.”
- `aptraining-local/parallel-ideas-lab/reports/ultimate_v80chain_pipeline_20260525T0945Z.md` (97): “- source-role diversity for demographic/disease prompts;”

Against: The repairs were checked on the same public items they were made against: "Public failures were repaired before delivery, including Second Great Awakening causation routing, foreign-policy coverage/dissent" (aptraining-local/den-of-ideation/to_main/2026-05-24T0208Z_DEN_REQUEST_validate_unit4_dbq_solver_v1.md, line 30). Only five items, and a spot check of the set with the 14-year gap found that an invented document alone failed it in another model's run: "Doc 4 alone is sufficient to fail this DBQ." (icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-04T1430Z_v40h_spot_verify.md, 138)

<sub>criterion · stimulus, alignment · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Historical terms defined briefly, said plainly

Define a historical term for a group of people briefly at its first use, and say it plainly and respectfully, with no caricature, stereotype or exoticised accent.

The 6 October handover's content cautions for a Grade 9 unit single out the play's historical term for its hero: the script gives a short definition for orientation, and the term is to be said plainly and respectfully, with no exoticised accent and no reduction of the character to an ethnic stereotype (line 166). Its pronunciation notes keep the term's delivery plain and respectful (line 300), and its academic acceptance list asks for historical language to be contextualised respectfully (line 438).

Quoted:

- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (166): “The current script gives a short definition for orientation.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (166): “Say the term plainly and respectfully; do not create an exoticized accent or reduce Othello to an ethnic stereotype.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (300): “The current script uses “Moor” in its historical context; keep delivery plain and respectful.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (438): “Historical language is contextualized respectfully.”
- `g9/script/v02/Othello-Opening-Recording-Manifest.json` (16): “Say lieutenant, ensign, Moor, dramatic irony, and tragic hero distinctly. Do not use an exoticized accent for any character or historical term.”
- `g9/script/v02/Othello-Opening-Recording-Manifest.json` (120): “Give each person’s name space. Speak the historical term “Moor” plainly and respectfully.”
- `g9/script/v02/Othello-Opening-Recording-Manifest.json` (118): “The play calls him a Moor, a historical term used for a North African or Black African man.”
- `g9/score/SOUND-DESIGN.md` (17): “speak “Moor” plainly and respectfully.”

Against: The wording itself is open: the handover asks for the definition's wording to be approved for the cohort, and no approved wording is recorded (line 166). The evidence covers one term in one unit, so widening the rule to other sensitive terms is a reading of it, not a finding.

<sub>criterion · wording, media · universal · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Hold back a misleading term

Hold back a technical term whose everyday meaning misleads until the concept it names is needed, then define it at once against that everyday meaning. One card keeps two genetics terms out of grades 3-5, then defines them at once against their everyday sense in grades 6-8.

The biology misconception card keeps 'dominant' and 'recessive' out of grades 3-5, because the terms carry too much everyday baggage and the concepts are not needed yet. When the terms arrive in grades 6-8, it defines them immediately with the anti-misconception framing that dominant does not mean stronger, better or more common.

Quoted:

- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx` (206 (textutil text)): “Do NOT introduce "dominant" and "recessive" at this level — the terms carry too much everyday baggage and the concepts are not needed yet.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx` (207 (textutil text)): “Grades 6-8 (when dominant/recessive is introduced)”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx` (209 (textutil text)): “Define the terms IMMEDIATELY with the anti-misconception framing”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/media-spec.md` (63): “The word mechanicals refers to this group of craftspeople. It does not mean that they are machines.”

Against: One example: the card says this of one pair of terms.

<sub>criterion · wording, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Keep a levelled source's first-person voice

When levelling a primary source for younger readers, keep its first-person voice, the property that justifies using it, so the firsthand and secondhand contrast survives.

A grade-4 reading plan uses period letters and logs as primary sources, and its plan evaluation found that their authentic 18th-century syntax would exceed the band's 940L ceiling unless adapted. Its generation contract adapts such sources to the band while keeping the first-person source voice, because the standard being taught, contrasting firsthand and secondhand accounts, depends on that property surviving the levelling.

Quoted:

- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/generation-contract.md` (26-28): “**Where the spec calls for a primary source (U5 log, U6 letter), adapt to band while preserving the first-person source voice**, the firsthand/secondhand contrast (RI.4.6) must survive the leveling.”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/PLAN-EVALUATION.md` (127-128): “authentic 18th-century syntax will exceed 940L unless adapted”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/PLAN-EVALUATION.md` (129): “must preserve the firsthand-source property (RI.4.6) that justifies using them.”

Against: none found

<sub>criterion · stimulus, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Keep excerpts in the text's order

List excerpts from a text in the order they occur in it, since a reordered list can make a line seem to belong to the wrong speaker or moment. A story-order check found three tap lists out of order across three lessons.

An outside quick-check audit of four reading lessons rated high a tap list that was out of story order: the keyed line sat after a non-evidence line from another character, so it read as the wrong speaker (`grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md`, L6-H4). The project encoded the class as a story-order check in its passage-reference validator, which found three such lists across three lessons, and a tool reordered them (`grade3-reading/artifacts/feedback-inceptbench-2026-09-30/BUILD-SPEC-batch.md`).

Quoted:

- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (81): “Tap list is out of story order”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (81): “so the keyed line reads as the wrong speaker.”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/BUILD-SPEC-batch.md` (180): “STORY-ORDER (validate-passage-refs.mjs)”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/BUILD-SPEC-batch.md` (180): “L5 p16 youdo-clue-hunt [6], L6 p16 step3 [8], L7 p9 item-2-check-2 [3]”
- `grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd` (39-40): “a `hot_text` question's tappable sentence list must be offered in the same order those sentences occur in the passage”
- `g9/transformer/src/glue/threejs-render.js` (85): “Up to n quotes from a ranked pool of units, the best first, shown in the text's order: whole clauses first (a line and”
- `g9/transformer/src/glue/threejs-render.js` (106): “return runs.sort((x, y) => x[0] - y[0]);”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md` (306): “Still present and serious: 29 (8 Highs: leak/echo feedback L4 p8, L5 p13, L6 p15b, L7/L6 p12 skill-check echo, L6 p3b mercy-root, L5 p15b nudges name the key, L6 p16 tap list out of story order; plus story-truth mediums and acceptance-rule conflicts).”
- `grade3-reading/course-renderer/docs/feedback/g3-parity-audit.md` (42): “evidence lists stay in passage order on purpose”

Against: none found

<sub>criterion · options, stimulus · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Keep fact, interpretation and opinion apart

Keep fact, interpretation, opinion and uncertainty distinct in what learners read and in the conclusions they frame, so they can tell what kind of claim each statement is.

The course-plan quality standard lists preserving the distinctions among fact, interpretation, opinion and uncertainty among its obligations for domain-bearing content (`ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd`, Q047). It accepts such content only when fact-versus-interpretation labels and epistemic review cover every governed claim, chart, item and feedback line, and counts a contested view presented as fact among its failure signals. Present a contested matter as open, never as settled, and keep a made-up teaching case apart from real evidence. In history, bound each claim by who, where, when and which source.

Quoted:

- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (805): “J16-SOC-002: Preserve distinctions among fact, interpretation, opinion, and uncertainty.”
- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (800): “Exact-byte source maps, applicable misconception rules, fact-versus-interpretation labels, epistemic review, and dependency digests cover every governed claim, chart, item, and feedback line.”
- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (801): “Unsupported claim; teleology; redefined terminology; contested view presented as fact; stale review after change.”
- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (798): “Externally checkable domain claims appear.”
- `grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd` (58): “A passage should not present a matter as settled where that is unwarranted. Distinguishing fact, interpretation, and opinion is part of the discipline itself.”
- `grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd` (85): “The scientific process distinguishes observation, hypothesis, theory, consensus, measurement, and related categories; student writing should make clear which of these the student is doing.”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md` (53): “no model presented as literal reality;”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md` (58): “no contested interpretation presented as settled fact.”
- `grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd` (57-59): “the coach coaches, the book reader reads, and keeping the two voices distinct is how a student hears 'the story' and 'the teaching' as separate things.”
- `grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd` (61-62): “its first unit mixes a made-up teaching case with real evidence and the two must be audibly distinguishable.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md` (21): “the passage should not be presented as settled where this is unwarranted.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md` (26): “student writing should be framed so that it's clear which of these the student is doing.”
- `downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 2. Should We Save the Rainforests - WEIGH - Lesson Design.docx` (223 (textutil text)): “Nothing is overclaimed beyond the passage.”
- `grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md` (21): “In social studies we teach students the disciplinary skills of evaluating situations where a topic is contested or evolving, and so the passage should not be presented as settled where this is unwarranted.”
- `grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md` (21): “distinguishing fact, interpretation, and opinion is part of what social studies *is*.”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json` (488): “Bound historical claims by actor, region, period, institution, and source function rather than flattening them into generic narratives.”
- `incept-package-hub/course-packages/courses/g5-reading/review/evidence/science-process.md` (66-67): “Observation, measurement, hypothesis, model, theory, consensus, and student conclusion must not be collapsed into one kind of claim.”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/misconception-check.md inside it) (34-35): “Mark observation vs. hypothesis vs. established fact; don't present the contested as settled, or the settled as opinion.”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/references/social-science-coherence-brainlift.md inside it) (26): “student writing should be framed so that it's clear which of these the student is doing.”
- `incept-package-hub/course-packages/courses/g5-reading/review/evidence/science-process.md` (69-70): “Rules 1, 3, and 4 require semantic review. The deterministic gate records that boundary instead of pretending to automate it.”
- `g9/transcript/chat-transcript.redacted.txt` (2863): “Confidence must remain compatible with uncertainty where the text permits multiple readings.”
- `g9/transcript/chat-transcript.redacted.txt` (3094): “Its confidence comes from a stable method, while its conclusions remain open to challenge.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/evidence/science-process.md` (66-67): “Observation, measurement, hypothesis, model, theory, consensus, and student conclusion must not be collapsed into one kind of claim.”
- `othello-archive/src/content/cast.ts` (8-9): “Iago's motive stays OPEN (dossier D3/D4): his reasons are given as his”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (222-223): “Separate documented consequence from present-day political judgment.”
- `grade3-reading/artifacts/arc-audit/PEDAGOGY-L7-2026-09-05.md` (239-241): “SWYK (p17): msq distinguishes actions ("worked at the ropes... in the story's own words") from inferences ("was probably relieved" / "bravest of all"). Feedback names the distinction.”

Against: none found; the standard applies it only where externally checkable domain claims appear (`ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd`).

<sub>criterion · wording, integrity, stimulus · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Keep the science plain beside a personified story

When a story personifies a natural process, keep the informational text paired with it in plain mechanism language, and make the difference between them explicit.

A grade-4 geology unit's misconception guards, drawn from cross-subject science guidance, reject agentive language such as the Earth being angry and let literary texts personify, but require the informational texts to keep mechanism language clean, with the pairing making the difference explicit. Its language rule separates observation ('the ground shook') from mechanism ('plates slipped'). A body unit's pairing of a literal and a figurative text must likewise mark which sense is in play, so that the pairing teaches the distinction instead of risking the misconception.

Quoted:

- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/key-understandings-and-misconceptions.md` (55-57): “Watch personification in disaster narratives — literary texts may personify, but the informational spine must keep mechanism language clean, and the pairing must make the difference explicit.”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/key-understandings-and-misconceptions.md` (59-60): “distinguish observation ("the ground shook") from mechanism ("plates slipped") — don't let narrative texts blur them.”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/key-understandings-and-misconceptions.md` (78-80): “the pairing is the vehicle for teaching the distinction, not a misconception risk, provided the marking is taught.”

Against: none found

<sub>criterion · stimulus, wording · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Keep the text still as teaching appears

Keep the passage still while teaching appears around it, reserving the space from the start, because text that shifts when modelling begins is jarring.

A review of a Grade 3 reading build said that when the modelling starts and the text shifts left, it is jarring. The rebuild reserves the space the teaching will use from the beginning of the lesson, so the text never moves out from under the child. A later course standard accepts a student-facing checkpoint only when its layout remains stable as content is revealed, and lists layout shift among its failure signals.

Quoted:

- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/FEEDBACK-RESPONSES.md` (206): “when the modeling starts and the text shifts left, it's jarring.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/FEEDBACK-RESPONSES.md` (212-213): “the space the teaching will use is reserved from the beginning of the lesson, so the text never moves out from under the child.”
- `grade3-reading/edullm-review-hub/course-packages/quality/golden-student-course/versions/1.0.0/STANDARD.qmd` (298): “layout remains stable as content is revealed.”
- `grade3-reading/edullm-review-hub/course-packages/quality/golden-student-course/versions/1.0.0/STANDARD.qmd` (299): “Failure signals: Dense diagnostic panels; multiple primary actions; long passive blocks; layout shift; decorative complexity.”

Against: none found

<sub>criterion · stimulus, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Keep verse line breaks everywhere

Show verse in its authored lines wherever it appears, in passages, pictures or films and at any screen width, never joined or re-wrapped, since its line breaks carry meaning.

A poetry and drama unit contrasts blank verse with a rhymed passage and asks why a voice should carry a sentence on past a line break, so its rules bar any visual asset from erasing lineation and keep the full verse lineation visible while a speech is modelled. The book renderer at first did not render verse at all, and the fix added real verse support rather than flattening verse into prose.

Quoted:

- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/README.md` (37): “No visual asset may erase lineation to make this distinction disappear.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/lesson-06.md` (45): “Keep full verse lineation visible.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/lesson-04.md` (52): “the sentence is incomplete at the line break”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/laptop-review/README.md` (19): “The staging book dispatcher did not render verse nodes.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/laptop-review/README.md` (19): “implemented proper verse support rather than flattening verse into prose.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (131): “Verse renders as verse: one authored line per block element, never joined, never re-wrapped,”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (134): “Verse lines carry a HANGING INDENT”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (135): “re-measures the verse at 390x844 to pin it.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (136): “so every verse assertion passed while the phone rendered 4 of the 19 lines”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (137-138): “a flush-left continuation row is indistinguishable from the next verse line, so a child counting the poem gets 21 lines”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (141-142): “pinned at one viewport certifies one viewport, and verse is the one content type where line breaks ARE the meaning.”

Against: Not every excerpt keeps its line breaks: a dialogue excerpt in the same unit was kept with "original punctuation and word sequence retained, line wrapping normalized." (grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/lesson-07.md, line 3), and the record does not say whether it holds verse.

<sub>criterion · stimulus, media · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Labels that match their sources

Make every source's label, which work, by whom, where, when and what kind of document, match the source text, in generated items and in the source bank. An audit of one bank of real sources found 198 of 436 era tags wrong.

AP judges failed generated items whose document labels contradicted their content: one document was labelled a manuscript illustration but described as a map, and others carried primary-source titles and dates their text did not match (`icloud-work/aptraining/.agent/research/failure_taxonomy.md`). An audit of the project's bank of real source documents caught 198 of 436 era tags wrong and 4 catalogue entries that pointed to a different work from the one named, errors that would have baked fabrication into the next model's training, and audit gates became mandatory before the next stage (`icloud-work/aptraining/.agent/memory/MEMORY.md`). Check each label against the source text as a claim of its own, and audit the source bank before anything is built from it. Generated source sets fail more on attribution than on their sentences.

Quoted:

- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (296): “Document 1 contradicts itself: it is labeled as a manuscript illustration of a dhow but described as a historical map with shaded regions and arrows.”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (248): “Several documents are labeled with specific primary-source titles and dates that do not match what the text says”
- `icloud-work/aptraining/.agent/memory/MEMORY.md` (72): “F-D13-12 caught 198/436 era misclassifications.”
- `icloud-work/aptraining/.agent/memory/MEMORY.md` (72): “F-D13-18 caught 4 wrong-work Gutenberg IDs in Branch C”
- `home-agent-memory/findings_sftv7_20260424.md` (64): “15 DBQ failures across 6 units. Dim hits:”
- `home-agent-memory/findings_sftv7_20260424.md` (65): “- `factual_accuracy`: 9”
- `home-agent-memory/findings_sftv7_20260424.md` (70): “**NOT failing on document text sentences — failing on attribution and structure.**”
- `home-agent-memory/findings_sftv7_20260424.md` (73): “Model names real explorers but assigns wrong geographic scope.”
- `home-agent-memory/sft_v4_prompt_engineering.md` (12): “- Removes source attribution from stimulus (main hallucination source)”
- `home-agent-memory/sft_v4_prompt_engineering.md` (18): “**Failure pattern:** Model fabricates specific source attributions and dates. SFT training examples should favor general historical description stimuli, not attributed documents.”
- `home-agent-memory/sft_v4_prompt_engineering.md` (22): “2. no_source: 50% pass, 70% factual_accuracy (best factual dim)”
- `home-agent-memory/sft_v4_prompt_engineering.md` (16): “**Why: `no_source` wins on factual_accuracy (70%) but `no_source_facts` wins on pass rate (60%).**”
- `home-agent-memory/findings_sftv7_20260424.md` (138): “3. **DBQ 12%** — all 4 fixes just applied; need fresh benchmark to measure impact”

Against: The bank audit was an agent's audit of a training corpus with spot checks, not a full review by a person, and the two judge rationales are single items. Dropping attributions trades one score for another: the variant without them had the best factual accuracy (70%), but the best pass rate (60%) came from the one that also added curriculum facts (`sft_v4_prompt_engineering.md`, line 16). The attribution fixes for document-based items were never re-measured (`findings_sftv7_20260424.md`, line 138).

<sub>criterion · stimulus, integrity · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Limits and harms in history texts

In history texts, show an achievement's limits and never play down the harm done to the people it affected.

Notes on a curriculum map's history texts ask that a text on the birth of democracy discuss its limitations, and that a text on the first peoples of the Americas, and those after it, not downplay the tragedy of European arrival (`downloads/_G3 curriculum Map.xlsx - Curric Map.csv`). The map's source record for a folk tale from an oral tradition asks for a respectful retelling (`downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx`). These are notes on particular texts, so the rule covers only the kinds of text they concern. A second learning sits in the same notes: retell other peoples' traditional stories with respect.

Quoted:

- `downloads/_G3 curriculum Map.xlsx - Curric Map.csv` (79): “Ensure the limitations of Ancient Greek democracy are discussed.”
- `downloads/_G3 curriculum Map.xlsx - Curric Map.csv` (89): “Be really careful here to not downplay the tragedy of European arrival for those already in the Americas (ditto with texts below).”
- `downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx` (sheet 'Sources & Inspiration', cell G9): “Ensure respectful retelling”
- `incept-package-hub/course-packages/courses/g5-reading/review/evidence/case-for-review.md` (129): “A single triumphant account would be historically and pedagogically defective”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (130-131): “Do not use "democracy expanded" without naming for whom; do not present reform as one unified movement or the Market Revolution as an automatic, single-cause transformation.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (169-170): “Do not equate industrial growth with shared prosperity, treat the West as empty land, or describe government as simply absent from the economy.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (358-359): “The feedback gate rejects claims that turn unequal consequences into a neutral swap.”

Against: none found

<sub>criterion · stimulus, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Literary forms inside the knowledge units

Teach poetry, drama and classic tales on texts inside the knowledge units, not in separate genre units, and check that every form the standards name appears.

A Grade 3 reading course's BrainLift holds that genre and structure are best taught on the text being read, since a genre unit divorces form from content and uses up a slot that would otherwise build knowledge. An adversarial review of its draft found every literary unit was narrative prose, which left drama and poetry with no place, a hard fail against standards that name scenes and stanzas. The fix put a readers' theatre play, and a poem tied to each unit's knowledge, inside the knowledge units; the rule is the course's own position, with no measured outcome.

Quoted:

- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/BRAINLIFT.md inside it) (130): “poetry, drama, and classic tales belong inside the knowledge units, taught on the text at hand — not in genre units of their own.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/BRAINLIFT.md inside it) (133-134): “A genre unit divorces form from content and burns the knowledge slot.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/BRAINLIFT.md inside it) (136-137): “all literary units were narrative prose, leaving **drama and poetry orphaned — a hard CCSS fail**”

Against: none found

<sub>criterion · stimulus, sequence, alignment · domain · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Log an adaptation's changed facts

When an adaptation changes a fact of the original, such as a count, record the change, keep it consistent everywhere, and never assess it as true of the original. One retelling's changed count of four losses was repeated in a reveal, a later lesson's frame and a chart.

A source audit of a Grade 4 retelling found that it changed how many companions went and how many were lost, with no adaptation change register attached to the student passage. The changed count was reinforced in feedback, a reveal, later lesson frames and a chart, and the lesson's own assessment grounding contradicted the passage about who was counted. The audit asked that any count changed for adaptation be logged and never presented as a fact about the original, and that the contradictory grounding be resolved in any case.

Quoted:

- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE4.md` (56): “If loss counts are changed for adaptation, log the decision and never present that count as a fact about the original epic; resolve the contradictory grounding in any case.”
- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE4.md` (56): “The p17 reveal at `:3196`, L3 p16 frame at `:4559` and p18 chart at `:4723` reinforce four losses.”
- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE4.md` (42): “Retelling status is explicit in the plan; no exact translator, edition, source passage or adaptation change register is attached to the student passage. Changes the party/loss counts and carries them into graded work.”
- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE4.md` (42): “Numeric alterations are reinforced in feedback and later L3 frames.”

Against: none found

<sub>criterion · stimulus, integrity, key · universal · from g3 · measured · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Mark the evidence where it sits

In guided practice, mark the key quote in place in the text rather than lifting it out, since extracting it does the locating step for the learner, out of sight.

As built, a Grade 9 prototype lifted the key quote out of the script and set it full-width in guided practice. Its review made keeping the script on the left with the quote marked in place a priority item, with the unpicking on the right. Its reason is that marking in place shows where the evidence came from, and locating evidence in the text is the skill being taught, while extracting the quote performs that step invisibly and leaves only the analysis.

Quoted:

- `g9/sources/Othello_1_Feedback_DevFactory.md` (108): “Keep the script on the left in guided practice. Mark the key quote in place within it.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (109): “Do not lift the quote out of the script. Extracting it performs the locating step for the child.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (286): “Marking it in place shows where the evidence came from — and locating evidence in the text is the SEARCH and FIND skill. Extracting the quote performs that step invisibly and leaves the child only the analysis.”

Against: none found

<sub>criterion · stimulus, demand · universal · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Mark where an assigned reading ends

When assigning part of a longer text, mark where the part ends as well as where it starts, so the learner need not work out the end from paragraph numbers. An assigned reading in a Grade 5 novel unit ran from its last paragraph, 25, straight into 26 with no end label.

An audit of a Grade 5 course built on a full novel found that the link to an assigned reading marked where it started, but the chapter ran on past its last assigned paragraph with no end label, and the assignment list gave only start points. The accepted repair names each selected part with its paragraph range, puts an end marker after its last paragraph with a link to the next selected part, and leaves the whole original chapter in place. A browser review then saw a visible ending and a next-part link on the selected range.

Quoted:

- `grade3-reading/ui-audit-2026-09-08/round-1/g5-u1/REPORT.md` (25): “normal Lesson5 reader entry marks the selected start, but paragraph25 flows directly into26+ with no end label.”
- `grade3-reading/ui-audit-2026-09-08/round-1/g5-u1/REPORT.md` (25): “The assignment list also provides only starts.”
- `grade3-reading/ui-audit-2026-09-08/round-1/g5-u1/PROPOSALS.md` (53): “the student should not need to infer an end from paragraph numbers alone.”
- `grade3-reading/ui-audit-2026-09-08/round-2/g5-u1/IMPLEMENTATION.md` (11): “the exact final paragraph is followed by an end marker and the next source-selected moment.”
- `grade3-reading/ui-audit-2026-09-08/round-3/g5-u1/READER-PATH-ACCEPTANCE-by-unit9.md` (14): “The selected range has a visible ending and a next-selected-moment link.”

Against: A marked range shows where to read, not that it was read: 'Neither link traversal nor the returned context establishes that the child read the assigned text.' (`grade3-reading/ui-audit-2026-09-08/round-3/g5-u1/READER-PATH-ACCEPTANCE-by-unit9.md`, line 25).

<sub>criterion · stimulus, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Moderate line length for screen passages

Keep an on-screen reading passage's lines to about 55–75 characters, even on a wide screen. One study found 55 characters per line gave better comprehension than 100.

The Grade 9 desktop design brief gathers studies on screen text. Lines of 55 characters gave better comprehension than lines of 100, so it caps the reading column at about 55–75 characters even on a wide screen, and for 28 readers with dyslexia readability improved up to 18 pt, so 18 px or more is its floor for the passage. Each reader's fastest font was 35% faster than their slowest with no loss of comprehension, and a dyslexia font gave 12 students in grades 3–6 no gain in speed or accuracy, so it offers a small font chooser instead of one dyslexia font. The voice and interface brief adds that light mode reads better for normal vision and that dark mode belongs as an option for long-form reading, not the default.

Quoted:

- `othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md` (103): “Dyson & Haselgrove (2001): 55 characters per line gave better comprehension than 100.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md` (105): “*Implication:* cap the reading column at about 55–75 characters even on a 1536-wide screen.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md` (106): “Rello et al. (2013), 28 readers with dyslexia: readability improved up to 18 pt, and line spacing had no significant effect. *Implication:* body text of 18 px or more is a reasonable floor for the passage.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md` (107): “Wallace, Bylinskii et al. (2022, ACM TOCHI): each reader's fastest font was 35% faster than their slowest, with no loss of comprehension.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md` (108): “Wery & Diliberto (2017), n = 12, grades 3–6: OpenDyslexic gave no gain in speed or accuracy, and no student preferred it.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (105): “Light mode reads better for normal vision; offer dark mode as an option.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md` (105): “NN/g recommends offering dark mode optionally, especially for long-form reading, rather than making it the default.”

Published: [Dyson & Haselgrove 2001](https://stu.westga.edu/~ssynan1/literacy/Dyson.pdf) · [Rello et al. 2013](https://pielot.org/pubs/Rello2013-W4A-SizeMatters.pdf) · [Wallace, Bylinskii et al. 2022](https://readabilitymatters.org/articles/towards-individuated-reading-experiences) · [Wery & Diliberto 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5629233/) · [Budiu 2020](https://www.nngroup.com/articles/dark-mode/)

Against: Longer lines are read faster, although readers prefer moderate lengths (`othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md`, line 104); light mode's advantage shrinks with larger fonts and brighter rooms (`othello-course-renderer-draft/repo/docs/design/grade-9/research/learners-voice-guide.md`, line 105); and the type-size and dyslexia-font studies are small, with 28 and 12 readers.

<sub>criterion · accessibility, stimulus · universal · from g9, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Motives, capabilities and choices together

Explain a historical development as conditions, motives, capabilities and choices working together, keeping what made it desirable apart from what made it possible, never one cause alone.

An AP history course's design document names two predictable misconceptions: a motive slogan for exploration that confuses goals with the capabilities that made voyages possible, and environmental determinism, in which geography automatically produces one social form. Its model has a valid explanation combine a motive, an institution that supplied resources and authority, a capability that solved a concrete problem, and information that changed later decisions, and it sets a multicausal boundary: neither a ship design nor an instrument began exploration by itself. The course's unit specifications warn in the same way against presenting a transformation as automatic and single-cause.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (340-341): “Students frequently explain European exploration with a slogan such as God, gold, and glory. That list confuses goals with the capabilities that made sustained voyages possible.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (345-348): “A valid explanation shows combination: a motive made a voyage desirable; a state, commercial, or religious institution supplied resources and authority; a maritime capability addressed a concrete navigation or vessel problem; and information from voyages changed later decisions. The model also sets a multicausal boundary. A caravel or astrolabe did not initiate exploration by itself.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (327-330): “A second risk is environmental determinism: stating that geography automatically produced a single social form. The course teaches bounded regional cases and the interaction of constraint, opportunity, knowledge, technology, coordination, and choice.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (130-131): “do not present reform as one unified movement or the Market Revolution as an automatic, single-cause transformation.”

Against: Both cited documents are marked "Historical / superseded" and record an earlier plan-review phase of the course (`grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz::apush/docs/BRAINLIFT.md` and `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz::apush/docs/UNIT-SPECS.md`, line 5). The position is a design choice, not a measured result.

<sub>criterion · stimulus, demand · domain · from ap · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Never present an invented source as real

Never pass an invented text or source off as real: use real ones, copied word for word with checkable attribution, and plainly label anything constructed, adapted, retold or machine-written.

A question benchmark's rules for document-based questions score factual accuracy 0.0 when any document contains fabricated content presented as real without pedagogical justification, or an incorrect attribution (`icloud-work/incept/inceptbench/src/inceptbench/prompts/question/dbq_evaluation.txt`, line 17). The same benchmark's fact audit forbids its judge to fail a document as fabricated, or a quotation as not matching its source, because it cannot reliably tell whether specific historical items exist and has no reliable verbatim recall of historical texts (`icloud-work/incept/inceptbench/src/inceptbench/tools/factual_accuracy_audit.py`, lines 129-134). One reading generator asks its writer for an excerpt from a named literary work, with no stored text to check the excerpt against (`icloud-work/incept/sat-reading-generation/sat-prompts.json`, line 5). So only a stored copy can catch an invented or misattributed source. Every source learners work with should be a real document, copied word for word from a verified collection into the item in code, with a specific, checkable attribution of who made it and when. A writer model invents plausible sources that a judge without a stored copy cannot reliably catch.

Quoted:

- `icloud-work/incept/inceptbench/src/inceptbench/prompts/question/dbq_evaluation.txt` (17): “- Score 0.0: Any document contains fabricated content presented as real without pedagogical justification, incorrect attributions, or factual errors in the prompt”
- `icloud-work/incept/inceptbench/src/inceptbench/tools/factual_accuracy_audit.py` (129-131): “- Claims that a specific document, artwork, engraving, manuscript, or edition
    "does not exist" or "is fabricated" or "is not canonical." You cannot reliably
    determine whether specific historical items exist in archives or collections.”
- `icloud-work/incept/inceptbench/src/inceptbench/tools/factual_accuracy_audit.py` (132-134): “- Claims that a specific passage, quote, or description is "not found in" or
    "does not match" a named primary source. You do not have reliable verbatim
    recall of historical texts and cannot verify what a source does or does not say.”
- `icloud-work/incept/sat-reading-generation/sat-prompts.json` (5): “Generate a new question with an excerpt from the following work: {work}.”
- `icloud-work/incept/sat-reading-generation/sat-prompts.json` (5): “Select a new excerpt the specified work that is at least as complex as the example passage, preferably more complex.”
- `icloud-work/evaluator/docs/reports/LATEST.md` (75): “document_authenticity | 1 | 109 | 0.9%”
- `icloud-work/evaluator/docs/reports/LATEST.md` (77): “sourcing_opportunity | 11 | 99 | 10.0%”
- `icloud-work/evaluator/docs/reports/evaluation_20260225_095143_49918efd.md` (171): “This appears to be a fictional source rather than an authentic historical document”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-008-dbq-7doc-generic-attrib.md` (28-29): “28/36 fails on factual_accuracy”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-008-dbq-7doc-generic-attrib.md` (32): “v2 lift: 19.4% → 65.7% on the same KCs.”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-008-dbq-7doc-generic-attrib.md` (94-96): “"pedagogical adaptation" rather than fabrication, even though no such specific editorial existed.”
- `icloud-work/ap-social-studies-generator/docs/08-AP-SOCIAL-STUDIES-SPEC.md` (152): “Primary source excerpts must be authentic or authentically styled”
- `icloud-work/aptraining/apllm-history/runtime_assets/ib_satisfaction_kit_v1/raw_rubrics/dbq_evaluation.txt` (17): “Any document contains fabricated content presented as real without pedagogical justification”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-008-dbq-7doc-generic-attrib.md` (93-96): “The judge interprets generic role-based attributions ("Editorial in a Midwestern newspaper, 1885") as "pedagogical adaptation" rather than fabrication, even though no such specific editorial existed.”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-008-dbq-7doc-generic-attrib.md` (27-29): “which triggered the judge's biographical fact-checking — 28/36 fails on factual_accuracy.”
- `icloud-work/aptraining/Cheater/exploits/EXPLOIT-008-dbq-7doc-generic-attrib.md` (53): “v2 generic-attribution + qualitative-claims + difficulty="easy" → 23/35 = 65.7%”
- `icloud-work/aptraining/workspace/comms/from_main/2026-05-29T1456Z_calibration_finding_DBQ_synthetic_docs_Gemini_strict.md` (18): “| **DBQ** | **16.7%** | Gemini rejects 15/18 — **synthetic-source attribution** ("Speech by Iroquois leader c.1570" etc.) violates Gemini contract rule "Do not fabricate real attributions" |”
- `icloud-work/aptraining/workspace/comms/from_cheater/2026-05-29T1843Z_3ch_DBQ_realsource_E1_DELIVERED.md` (90-93): “my E1 prompt explicitly instructs Claude to use the d13 pack as KC scope hints but write FRESH period-authentic excerpts from genuine works in its knowledge.”
- `icloud-work/aptraining/workspace/comms/from_cheater/2026-05-29T1843Z_3ch_DBQ_realsource_E1_DELIVERED.md` (10): “**18/18 U1 KCs = 100.0% JOINT IB v2.5.11 + Gemini deterministic judge PASS.**”
- `icloud-work/evaluator/docs/reports/evaluation_20260225_081919_0909a798.md` (82): “| document_authenticity     |   28 |  163 |     14.7% |      0.15 |”
- `icloud-work/evaluator/docs/reports/LATEST.md` (75): “| document_authenticity     |    1 |  109 |      0.9% |      0.59 |”
- `icloud-work/evaluator/docs/reports/LATEST.md` (169): “This document has no attribution whatsoever and risks misleading students.”
- `icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-pass-contract-matrix.md` (32): “- fabricated documents presented as real,”
- `icloud-work/evaluatorML/.agent/memory/e2e_pipeline/generate_apush_unit1_openapi_poc.py` (136): “Avoid fake verbatim quotations; for uncertain source text, write paraphrased source-style excerpts with clear generic attribution.”
- `icloud-work/ap-social-studies-generator/data/model_findings.md` (520): “3/5 = fabricated stimulus”
- `icloud-work/ap-social-studies-generator/data/model_findings.md` (521): “constraint eliminated format-fabrication but not content-fabrication”
- `icloud-work/ap-social-studies-generator/python/CLAUDE.md` (130): “Fabricated poem falsely attributed to”
- `icloud-work/ap-social-studies-generator/python/CLAUDE.md` (591): “- Think: "What WOULD they have written?" not "What DID they write?"”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt` (19-23): “Fail `factual_accuracy` for a false, fabricated, or materially misleading claim in the stimulus, key, or explanation. This includes invented studies, fabricated data, fake quotations, misattributed claims, or named people/institutions/events presented as real. Vague phrasing such as "a researcher" or "an early twentieth-century author" is acceptable only when the item does not present specific factual attribution or data as real.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/saq_evaluation.txt` (68): “- Score 0.0: Stimulus is fabricated/irrelevant/unattributed, OR harmful (wrong, misleading, contradictory, distracting), OR Mode A and stimulus is not core, OR Mode B and no stimulus present”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/dbq_evaluation.txt` (17): “- Score 0.0: Any document contains fabricated content presented as real without pedagogical justification, incorrect attributions, or factual errors in the prompt”
- `icloud-work/inceptbench-main/src/inceptbench/tools/factual_accuracy_audit.py` (117): “You MUST NOT score 0.0 based on:”
- `icloud-work/inceptbench-main/src/inceptbench/tools/factual_accuracy_audit.py` (118-120): “Claims that a specific document, artwork, engraving, manuscript, or edition "does not exist" or "is fabricated" or "is not canonical." You cannot reliably determine whether specific historical items exist in archives or collections.”
- `APinceptbench/docs/reports/evaluation_20260225_081919_0909a798.md` (67): “- (3x) Some documents appear to be simulated rather than authentic historical sources”
- `APinceptbench/docs/reports/evaluation_20260225_081919_0909a798.md` (82): “| document_authenticity     |   28 |  163 |     14.7% |      0.15 |”
- `APinceptbench/docs/reports/evaluation_20260225_081919_0909a798.md` (63): “- (8x) Document 1 lacks specific attribution (author, date, source)”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md` (9): “DBQ is structurally zero on the current InceptBench path because the generator emits DBQ "documents" that are visual artifact descriptions or fabricated source descriptions, not usable source text.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md` (111): “The contrast is the whole story: normal generation without real source injection sits at DBQ 0%; D13 source injection immediately produces non-zero DBQ, but the current naive retrieval/prompting still fails often.”
- `icloud-work/aptraining/helpers/data/output/d13_corpus_v5_inventory.md` (68): “1. **DBQ inference-time RAG** — D13 docs are retrieved at runtime to ground DBQ generation. Pipeline-on-v80b uses this and scores **87.9% DBQ** (vs 67% v80b standalone). This is the biggest measured lift in the project per v91 ABORT_DEAD doc.”
- `icloud-work/aptraining/helpers/shadow/output/ib_satisfaction_kit_v1/generator_prompts/system_prompt_dbq.md` (129-130): “1. Copy each document's source/content/metadata verbatim from the retrieval. 2. Do NOT rewrite or summarize the source attribution — keep it exactly as retrieved.”
- `icloud-work/aptraining/handover/2026-05-01T1039Z_main_session_close/01_HANDOVER.md` (89): “**No mock data.** Every text field traces to a primary source. LLMs are tools (search/OCR/reformat), not content authors. Drop-don't-patch when sources fail.”
- `icloud-work/aptraining/helpers/data/output/v18_rebuild_scope.md` (15-17): “D8b confirmed plausible-but-fictional content (real attributions, unverified text) — fine for ≤95% but the floor at 99%.”
- `icloud-work/aptraining/.agent/memory/MEMORY.md` (80): “v29 fabricates MCQ_SET stimuli at 95% under BAML rubric; IB passes at ~100%.”
- `icloud-work/aptraining/.agent/memory/MEMORY.md` (75): “MCQ_SET fab rate 100% across v25b/v29/v40h; recipe variations don't fix it.”
- `icloud-work/aptraining/.agent/memory/BEADS.md` (177): “SAQ/LEQ 0% fab; MCQ/MCQ_SET/DBQ 100% fab”
- `icloud-work/aptraining/.agent/memory/MEMORY.md` (81): “Oracle's BAML-rubric rescore: -13.3pp aggregate Goodhart gap; SAQ 4/6 not 6/6; **2 fabricated primary sources in MCQ_SET**”
- `icloud-work/aptraining/.agent/research/failure_taxonomy.md` (244): “Several documents present historically unreliable information (notably the Declaratory Act excerpt and other implausible or likely fabricated source content), which could directly misteach students about key events and policies.”
- `icloud-work/aptraining/.agent/memory/STATE_CURRENT_2026_05_12T0805Z.md` (88): “### D13 inference injection: 4/6 = 66.7% DBQ (was 0%)”
- `icloud-work/aptraining/.agent/memory/STATE_CURRENT_2026_05_12T0805Z.md` (90): “Model uses docs verbatim → stim_q=1.0 → pass”
- `icloud-work/aptraining/.agent/memory/PILLARS_2026_05_12.md` (64): “- Stimulus matches /search hit? (else drop)”
- `icloud-work/aptraining/.agent/memory/MEMORY.md` (187): “every text field in any new corpus must trace to a primary source; LLMs are tools (search/OCR/reformat) not content authors; drop-don't-patch when sources fail.”
- `ap-helpers-data-agent-memory/recipe_track_a_b_kc_pack_substitution.md` (11): “the `documents` array is **synthesized** — Gemini invents author names + dates + content.”
- `ap-helpers-data-agent-memory/recipe_track_a_b_kc_pack_substitution.md` (11): “Even when grounded in a real OpenStax `_GROUND_TRUTH_SOURCE_` excerpt in the prompt, output documents are stylistic-real not literal-real.”
- `ap-agent-memory/feedback_dbq_stimulus_v2.5.6_root_cause.md` (3): “PILLAR 1 confirmed dbq stimulus_quality zeroed 98-100% across v43-soup + v50 + v51 on IB v2.5.6 (n=270 dbq attempts × 3 models, σ=0). Only real-source documents bypass the rubric.”
- `ap-helpers-data-agent-memory/project_v50_v56_strategy_with_numbers_2026_05_12.md` (32): “- Hot-patch full validation n=30: **10/30 = 33.3% locked rate**”
- `ap-agent-memory/feedback_d13_inference_injection_partial_fix_2026_05_12.md` (26): “- Success rate at "use docs literally" is ~20% on v43-soup (1 of 5 graded)”
- `icloud-work/aptraining/.agent/memory/MEMORY.md` (129): “DBQ remains data-veracity bound — D13 real-source corpus is the unique remaining lever.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/experiments/failed_export_replay/RUNNING_SUMMARY.md` (88): “- Dynamic DBQ cannot be allowed to invent source documents. It needs retrieved vetted documents or document-bank retrieval by standard. Source retrieval fixed the focused institution DBQ slice: `dynamic_source_gate_dbq_mcqset_v1` DBQ scored 0.98.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/parallel-ideas-lab/reports/pil_monitor/inbox/2026-05-19T1456Z_den_unit1_trap_verifier.md` (58): “Prefer generic-safe attributions over fancy named sources unless the person/date pair is verified.”
- `icloud-work/aptraining/workspace/comms/to_conscience/2026-05-29T1840Z_dream_sequence_sync.md` (16): “- **Gemini-vs-IB calibration** 14:55Z: 81.1% overall; DBQ 16.7% (Gemini correctly catches synthetic-source pattern; LEQ/MCQ_SET/SAQ 100%)”
- `icloud-work/aptraining/workspace/comms/to_conscience/2026-05-30T0640Z_dream_sequence_2_sync.md` (8): “Gemini-vs-IB calibration 97.8% on n=90 post-DBQ-realsource-swap (was 81.1% pre-swap)”
- `aptraining-local/parallel-ideas-lab/reports/rubber_ducks/killer_pipeline_atomic_ducks_20260525.md` (98): “Role-based source descriptions can avoid hallucinated names; use carefully because real source packs are preferable.”
- `aptraining-local/parallel-ideas-lab/reports/deep_repo_extraction_20260525.md` (138): “Generic fabricated documents can reduce obvious fact-check failures, but may conflict with source authenticity expectations.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md` (56): “The generator emitted fake maps, charts, photographs, and cartoon descriptions as if they were documents.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md` (57): “InceptBench hard-zeroed those because the stimulus was not real analyzable source material.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_structural_takeaways.md` (72): “DBQ needs source ownership outside the model. The model can frame prompt/rubric, but source documents must come from retrieval or locked artifacts.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/aptraining-root/den-of-ideation/reports/parallel_ideas_lab_distilled.md` (10): “DBQ moved from structural 0% in v50/v52-era model-only runs to 29/30 in the best-worlds wrapper run. The winning lever was source/prompt pipeline behavior, not another DPO tweak.”
- `aptraining-local/den-of-ideation/reports/validation_triage/20260527T132917Z_2026-05-27T1330Z_bm0zjn5z_n100_unit1_RAW_PROBE_REPORT.md.md` (129): “`stimulus_quality=0` on 75% of DBQ fails — primary-source documents are synthetic”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T1958Z_DELIVERED_unit1_dbq_solver_v1_candidate.md` (74): “Native environment row failed on fake `1491` source dates; honest modern/ethnohistorical attribution fixed it.”
- `aptraining-local/den-of-ideation/reports/validation_triage/20260527T220400Z_2026-05-28T0008Z_track_A_30row_sample_INVALID_TEST_RECOVERY.md.md` (96): “PIL still owes the a/b decision on the honesty flag (89% subject-period-dated).”
- `grade3-reading/knowledge_bot/knowledge/kb-0198-meetings-decisions-timeline-0819-1001.qmd` (29-30): “LLM-generated fiction "is never going to be great"; real, split-into-parts texts are the priority”
- `grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd` (44-45): “don't relabel machine-authored cold passages as "real."”
- `grade3-reading/knowledge_bot/knowledge/kb-0198-meetings-decisions-timeline-0819-1001.qmd` (29): “**Authentic fiction only.**”
- `grade3-reading/knowledge_bot/knowledge/kb-0198-meetings-decisions-timeline-0819-1001.qmd` (30-31): “Our canon's synthetic-prose literary units are flagged as rebuild risk.”
- `grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd` (24): “Phase A: 4 original passages ... review verdict "GREAT"”
- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R17.md` (140): “written and labeled an adaptation, not a quotation or original chapter.”
- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R18.md` (73): “an explicit attribution `booktag` on the reading page itself (not only on a later evidence/reference”
- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R17.md` (144): “No child is actively misled by this gap (L1 establishes context; meaning is preserved); no CRITICAL”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/showcase-source-packet.json` (12): “Treat a constructed table or index as a hypothetical instructional scenario, not observed scientific data.”
- `incept-package-hub/course-packages/courses/g5-reading/source/canonical/showcase-source-packet.json` (297): “Do not reuse reported percentage changes as general constants; any showcase numbers must be source-specific or explicitly hypothetical.”
- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE3.md` (68): “Current passage booktags such as “Part 1 of 4” and “Page 1 of 4” do not themselves label an adaptation or establish an original edition.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/integration/unscored-continuation.txt` (3): “paragraph: Original teaching vignette, not a scene from Shakespeare”
- `grade3-reading/ui-audit-2026-09-08/round-3/g5-u1/REPORT.md` (11): “Lesson 6 clearly labels Burnett's original, an adaptation and the invented first-person experiment.”
- `grade3-reading/ui-audit-2026-09-08/round-3/g5-u9/REPORT.md` (24): “The comedy transfer scene is labelled as an original vignette.”
- `grade3-reading/course-renderer/artifacts/listen-qa/G5-U1-L5/p6-section-1.txt` (2-3): “Sheet 12 is an invented classroom file. Its walls and numbers are not a real National Park Service measurement.”
- `g9/sources/Act 1 reading texts/Act 1/1. 1.1 - Iago_s Introduction - Text.docx` (5): “Text: abridged from the Folger Shakespeare edition (CC BY-NC 3.0).”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (116-118): “Course-authored explanation remains legitimate, but it calls itself course-authored and cites the factual authority behind it. The course does not manufacture a quotation when a clear paraphrase will do.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (663-664): “Its role must be explicit, its factual authorities must be cited, and it cannot masquerade as a primary source.”

Against: The rule leaves room for a justified invention: it fails fabricated content presented as real only "without pedagogical justification" (`icloud-work/incept/inceptbench/src/inceptbench/prompts/question/dbq_evaluation.txt`, line 17). one generator's spec accepts primary-source excerpts that are authentic or authentically styled, and the outside judge's rubric fails invented content only when it is presented as real without a pedagogical justification. A specific attribution is not enough on its own: a later rebuild had a model write excerpts credited to real works from memory, and both judges passed all 18 sets with no word-for-word check against the works (`icloud-work/aptraining/workspace/comms/from_cheater/2026-05-29T1843Z_3ch_DBQ_realsource_E1_DELIVERED.md`, lines 10 and 90-93). The project's own rules disagree on constructed documents. One spec requires '- ALL documents MUST be authentic historical sources or clearly adapted from authentic sources' (`icloud-work/evaluator/docs/GENERATOR_API_SPEC.md`, line 294). The pass contract allows '- retrieve or construct real-source-mirroring documents with period-plausible language and attribution; do not invent unsupported facts.' (`icloud-work/evaluatorML/.agent/memory/analysis/2026-05-25-ib-pass-contract-matrix.md`, line 39). The later repair rules say "Prefer generic but plausible attributions such as 'Spanish colonial account, early 1500s' over fake named precision." (`icloud-work/evaluatorML/.agent/memory/e2e_pipeline/iterate_repair_to_100.py`, line 155), with no label that the text is constructed. The subject spec allowed invented sources ('Primary source excerpts must be authentic or authentically styled', `icloud-work/ap-social-studies-generator/docs/08-AP-SOCIAL-STUDIES-SPEC.md`), and the copyright filter blocks verbatim recall ('The model tries to reproduce actual quotes and triggers copyright filters.', `icloud-work/ap-social-studies-generator/python/CLAUDE.md`), so real excerpts have to come from a vetted bank, not from the model. The document-based rubric fails fabricated content presented as real only when it has no pedagogical justification (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/dbq_evaluation.txt`, L17), and the fact audit forbids failing a document only because the judge believes it does not exist or is fabricated (`icloud-work/inceptbench-main/src/inceptbench/tools/factual_accuracy_audit.py`, L117-120). Real sources were necessary but not enough: a naive retrieval patch reached only 33.3%, with 64% of items still scoring zero on source quality (icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md, line 137). The live service turned a described visual document into a generated image the grader could score (icloud-work/aptraining/apllm-history/main.py, lines 532-533), and one criteria pack advised 'plausible attribution lines (author/date/source citation)' (icloud-work/aptraining/helpers/data/output/ib_pass_criteria_pack/README.md, line 23). The invention verdicts came from another model-based rubric, not from a person checking each source; that rubric was later retired from promotion decisions (`icloud-work/aptraining/.agent/memory/MEMORY.md`, line 76), and the calibration gap's investigation was 'deferred until D13 ships + v41-d13 eval.' (the same file, line 80). The general judge did catch some invented sources (`icloud-work/aptraining/.agent/research/failure_taxonomy.md`, line 244), and a later version of it hard-failed fabricated documents (`icloud-work/aptraining/.agent/memory/feedback_curriculum_api_mandatory_2026_05_11.md`, line 9). A later forensic put 26 of 30 document-based failures down to prose descriptions of visuals that weren't there (`icloud-work/aptraining/.agent/memory/state_training_chain_2026_05_12T1300Z.md`, line 54), so part of the lift may come from dropping described visuals, and the injection result rests on 6 items. Training the writer on a real-source corpus did not stop invention ('D13 source-grounded hypothesis falsified.', `icloud-work/aptraining/.agent/memory/MEMORY.md`, line 67), and matched documents plus extra curriculum guidance backfired ('counterproductive (context overload)', `icloud-work/aptraining/.agent/memory/BEADS.md`, line 388). Placing documents in code was designed but had not run in production when the recipe was written (`recipe_track_a_b_kc_pack_substitution.md`, line 74); the measured rise came from putting real documents in the writer's request. A different, grounded writer's own document sets passed a later judge version 139 of 154 times (`recipe_track_b_openstax_pair_generation.md`, line 67), so the near-total failure belongs to one judge version and to writers working without a source excerpt, and the case for real excerpts rests on authenticity. Substituted documents kept the question's theme only about 85% of the time in spot-checks (`recipe_track_a_b_kc_pack_substitution.md`, line 52), so they still need checking against the question. Role-only attributions are a fallback: the lab's notes prefer real source packs and warn that generic fabricated documents may conflict with source-authenticity expectations. The rise in agreement is between two judges, which shows consistency, not correctness. This lineage's own "validated" document lane served normalized excerpts, and the grader passed them: "Source packs use normalized excerpts and should receive provenance spot-check before promotion." (icloud-work/aptraining/workspace/comms/from_den/2026-05-23T2115Z_DELIVERED_unit8_dbq_solver_v1_candidate.md, line 55). The attribution case is one task, and what the later honesty flag measured is not spelled out in the sources read. machine-written passages still have a place: the reading project's cold tests use machine-authored passages, checked item by item as non-leaking and labelled as machine-authored, and the claim that real passages raised an AP generator's scores was refuted, the lever being an unseen, non-leaky passage (`grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd`). It is a judgement, not a measured comparison, and it covers fiction only: four original informational passages written for a demo unit passed review with the verdict "GREAT" (`grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd`). The review judged the gap minor: no child is actively misled, since the first lesson sets the context and the meaning is preserved (`grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R17.md`).

<sub>criterion · stimulus, integrity · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### No framing traps in history content

History and technology content avoids known framing traps, such as monolithic groups, events as destiny, contested readings as settled fact, one side without agency, lone-genius invention and unexamined sources.

A Grade 4 reading course's generation contract makes misconception screening a gate on generation and runs its history and social-studies texts through checks for settled-fact framing of contested interpretation, inevitability and monolithic groups. A Grade 6 course's misconception check bans, in passages on design and invention, invention as a lone flash of genius, a design as perfect or finished, and technology as inevitable progress. A Grade 3 unit on Native nations names treating them as one group, or as a people who exist only in the past, as the misconception to guard against, and requires its content to be checked for nation names, present-tense framing and respectful, accurate traditions. The first trap is also part of keeping fact and interpretation apart.

Quoted:

- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/markdown/generation-contract.md inside it) (118-119): “(no settled-fact framing of contested interpretation; no inevitability; no monolithic groups)”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/misconception-check.md inside it) (72-73): “invention as a lone flash of genius; a design as "perfect"/finished; technology as inevitable progress.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/UNIT-FRAMING.md inside it) (128): “Native nations are **many distinct, present-day peoples** — not one single group, and not a people who exist only in the past.”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u09.md` (73-74): “verify nation names, present-tense framing, and that traditions are represented respectfully and accurately.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/TEACHING-ASSESSMENT-CONTRACT.md inside it) (160-161): “5. **Representation gate:** A group is not treated as internally uniform when the lesson's own scope depends on regional, political, class, racial, gender, religious, or strategic differences.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-1-REVIEW.md inside it) (35-45): “The unit explicitly checks recurring high-risk simplifications: - treating Indigenous societies as one culture; - turning environmental constraint into destiny; - reducing exploration to motives without capabilities; - presenting the Columbian Exchange as a balanced list; - treating encomienda as land ownership or all coerced labor as identical; - presenting caste categories as a perfectly rigid universal hierarchy; - explaining conquest as a single European action without Indigenous diplomacy, alliance, or resistance; - treating a source as transparent narration or dismissing it with an unsupported "bias" label.”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/key-understandings-and-misconceptions.md` (87-88): “Inevitability framing ("the colonies were always going to become America") — history as choices under uncertainty, not destiny.”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/key-understandings-and-misconceptions.md` (89-90): “Monolithic groups ("the colonists thought… the Native peoples believed…") → specific peoples, specific colonies, specific voices.”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/key-understandings-and-misconceptions.md` (85-86): “The paired colonist-vs-Native accounts are the guard: two positioned sources, neither presented as the neutral truth.”

Against: The unit review is marked historical and superseded as a review request, though nothing withdraws its controls (`grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz::apush/docs/UNIT-1-REVIEW.md`, line 5).

<sub>criterion · stimulus, integrity, wording · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### No single cause for a many-cause system

In science content, never present one factor as the sole driver or fix of a system with several causes; name the other causes and the uncertainty.

A red-team factual pass of a Grade 3 reading corpus, checked against agency sources, found lessons that made one factor the whole story: returning wolves said to have reversed and fixed a forest's damage, where the park service describes wolves as one contributor in a debated, multi-factor system, and the sun called the single engine of the water cycle, where the geological survey says solar energy and gravity drive water's movement. A Grade 5 generation contract's science rule says one local food-web pattern or intervention does not guarantee a universal population response, biodiversity effect or recovery, and asks for the condition, the direct and indirect pathways, alternative stressors, site scope and uncertainty to be stated. No effect on learners is recorded.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/redteam-g3-round3-report-and-evidence.tar.gz` (RED_TEAM_ROUND3.md inside it) (100-103): “- U5-L5 says returning Yellowstone wolves "reversed" and "fixed" the damage and proves one predator keeps a forest healthy. NPS describes wolves as one contributor in a debated, multi-factor system involving other predators, hunting, water, drought, and climate ([NPS](https://www.nps.gov/yell/learn/nature/cyclesprocesses.htm)).”
- `grade3-reading/_archive/2026-08-13-consolidation/redteam-g3-round3-report-and-evidence.tar.gz` (RED_TEAM_ROUND3.md inside it) (106-107): “- U6-L2 calls the sun the single water-cycle engine and wind the single force. USGS says solar energy **and gravity** drive water's movement ([USGS](https://www.usgs.gov/faqs/what-earths-water-cycle)).”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/package/Grade 5 Reading - Review Evidence/markdown/generation-contract.md inside it) (656): “| BIO-003 | U4, U9 | One local food-web pattern or intervention does not guarantee a universal population response, biodiversity effect, or recovery amount. | State the condition, direct and indirect pathway, source-bounded evidence, alternative stressors, site scope, and uncertainty. |”

Against: none found

<sub>criterion · stimulus, integrity, wording · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### No slurs to perform

Never ask a student to say or perform a line with a slur in it: a line a student performs ships only when a judge confirms it is clean.

A line a student is asked to work with or perform goes to the judge with one question, whether it is free of any
racist or sexual slur or epithet, and the block ships only on a confident yes; a gloss may name an epithet as an
insult, but a student is never asked to perform one (`g9/transformer/src/mechanics/util.js`, `cleanLine`;
`g9/transformer/test/laws.test.mjs`). A 3D version's list of lines it never stages is used as well, when its code is on
the machine.

Quoted:

- `g9/transformer/src/mechanics/util.js` (106-107): “A gloss may name an epithet as an insult, as the animated … build's gloss does; a student is never asked to perform one.”
- `g9/transformer/src/mechanics/util.js` (105): “for any text, one Jev question with the line in the state, so a block”
- `g9/transformer/test/laws.test.mjs` (153): “a line never staged holds a direct-the-line block, in code and on the judge's word; a word in focus may gloss the slur as an insult”
- `g9/transformer/src/glue/threejs.js` (79): “Without the mirror there is none, and the Jev question carries the guard.”
- `g9/transformer/src/glue/animated.js` (211): “line never staged is left out), the moment, the meaning and the words”
- `g9/transformer/src/glue/threejs-render.js` (183): “the 3D build never stages this line”
- `g9/transformer/test/laws.test.mjs` (173): “word in focus: another word in that line is held; the slur itself, glossed as the insult it is, is left to the judge”
- `g9/transformer/test/laws.test.mjs` (153): “a word in focus may gloss the slur as an insult”
- `g9/transformer/test/laws.test.mjs` (168): “the 3D build's mirror is not on this machine: the judge's question carries the guard”
- `g9/transformer/src/mechanics/word-in-focus.js` (3-4): “The line shown must be clean: a slur in … it is allowed only as the word in focus itself, glossed as the insult it is (as the animated build glosses it).”
- `g9/transformer/src/mechanics/word-in-focus.js` (58): “check("not-never-staged", "No candidate's line is one the 3D build never stages, unless the word is that slur",”
- `g9/transformer/src/mechanics/word-in-focus.js` (73): “// the highest gain among the candidates the judge is sure are clean; with none, the highest, which the judge holds”
- `g9/transformer/test/laws.test.mjs` (173): “// word in focus: another word in that line is held; the slur itself, glossed as the insult it is, is left to the judge”
- `g9/transformer/test/laws.test.mjs` (168): “if (!banned) return; // the 3D build's mirror is not on this machine: the judge's question carries the guard”
- `g9/transformer/src/glue/threejs.js` (78): “Its lines never staged or voiced (scripts/check-moments.mjs SLUR, Othello's): read from the mirror at run time, so no”
- `g9/transformer/src/mechanics/util.js` (106): “ships only on positive evidence that the line is clean.”
- `g9-transformer-runs/blocks/5722a3741161394e.json` (238): “"p": 0.93,”
- `g9-transformer-runs/blocks/e47511c58b5dd64c.json` (129): “"p": 0.99,”
- `g9/transformer/src/mechanics/direct-the-line.js` (3): “A student performs the line, so it is never one with a slur in it”
- `g9/transformer/test/laws.test.mjs` (162): “the judge's guard: the line is in the state, and the block ships only when the judge is sure it is clean”
- `g9/transformer/v02/QA.md` (131-132): “a slur guard on lines a student is asked to perform (the 3D build's own list, read at run time; a Jev question);”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “A word-in-focus gloss may name an epithet as an insult, as the animated build's gloss does, but a student is never asked to perform it.”
- `g9-transformer-audit/2026-10-09-builders.json` (1): “'the Moor' lines may come back unsure and hold direct-the-line or word-in-focus blocks more often.”
- `g9-transformer-audit/2026-10-09-builders.json` (1): “lines such as 'an old black ram' are left to the Jev question.”
- `g9/sources/Cutting-a-Scene-Othello-1.1.pdf` (113-115): “Point out that the original version of this scene is full of racial language and even slurs. As a class we expect that groups keeping these words will not make light of them but rather treat them with the seriousness they deserve.”

Against: the guard is asked in three blocks (direct the line, word in focus, worked model); the
say-it-back block, whose sentence a student says aloud, doesn't ask it yet. A later run found counter-evidence (`g9-transformer-audit/2026-10-09-builders.json`). A later run found counter-evidence (`g9-transformer-audit/2026-10-09-builders.json`). A later run found counter-evidence (`g9/sources/Cutting-a-Scene-Othello-1.1.pdf`).

<sub>criterion · wording, integrity · universal · from g9 · adopted-rule · held · found in [2026-10-12-2-round-1](../research/2026-10-12-2-round-1/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Nonfiction needs its own hook

Judge engagement separately for fiction and nonfiction, and give nonfiction its own hook rather than a lower bar, since readers' motivation for the two was not highly associated.

A grade-4 pedagogy definition cites a 2007 study of reading motivation in the later elementary years, which found that students' reading motivations for narrative and information texts were not highly associated, so skill at hooking readers on a story need not carry over to informational text. Because the course is anchored in nonfiction in five of its units, it asks that engagement and craft be scored by genre rather than as one craft score, and that a nonfiction passage get its own hook, such as a real stake, a genuine question or a surprising fact.

Quoted:

- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/PEDAGOGY.md` (112-113): “"students' reading motivations for narrative and information texts were not highly associated."”
- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/PEDAGOGY.md` (116): “should be checked SEPARATELY by genre, not as one undifferentiated craft score”
- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/PEDAGOGY.md` (116-118): “a nonfiction passage needs its own hook (a real stake, a genuine question, a surprising fact), not a lower engagement bar”

Published: [Reading motivation and reading comprehension growth in the later elementary years, Contemporary Educational Psychology 32:282-313 (2007)](https://doi.org/10.1016/j.cedpsych.2006.05.004)

Against: none found

<sub>criterion · stimulus, evaluation · universal · from g3, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### One name, one kind of thing

Never reuse a name for a different kind of thing across lessons read in sequence.

A review of a Grade 5 unit found the same names used for a person in one lesson and for a source or record in the next, so that, read in order, the same tokens kept changing what kind of thing they named; it called the fix cheap and the confusion high if left (`grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md`). It rests on that one finding.

Quoted:

- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md` (105): “same tokens keep changing referent class. Cheap to fix (rename L6's sources or L4's”
- `grade3-reading/artifacts/qc-2026-09-30-staging/LIVE-WALK.md` (116): “"Mood" here means a character's passing feeling, while L4 taught mood as how a place feels.”

Against: none found

<sub>criterion · wording, sequence · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### One typeface for the text, one for teaching

Set the studied text in one typeface and all instructions, definitions and feedback in another, used the same way throughout, so learners can tell the text from the teaching. Definitions and example sentences appeared in a third typeface, with nothing to signal why.

A supplied UI review of a Grade 3 lesson found definitions and example sentences set in a serif while everything else used a rounded sans, with nothing to signal why that content was different (`grade3-reading/ui-audit-2026-09-08/gold-standard/aladdin-p1-ui-review.reference.md`, line 34). The project kept the literary serif for the passage, verse and quoted evidence and set definitions and examples in the instructional sans throughout (`grade3-reading/ui-audit-2026-09-08/gold-standard/REVIEW-MAPPING.md`, line 19; `grade3-reading/ui-audit-2026-09-08/gold-standard/STYLE-IMPLEMENTATION-by-residual.md`, line 17). A rendered fixture checks the distinction between instructional and source fonts (the same file, line 28). It is the visual counterpart of reading the text in one voice and the teaching in another.

Quoted:

- `grade3-reading/ui-audit-2026-09-08/gold-standard/aladdin-p1-ui-review.reference.md` (34): “The definitions and example sentences are set in a serif while everything else uses the rounded sans, with nothing to signal why that content is different.”
- `grade3-reading/ui-audit-2026-09-08/gold-standard/REVIEW-MAPPING.md` (19): “Book story serif remains for literary passage; definitions/examples use the instructional display sans consistently.”
- `grade3-reading/ui-audit-2026-09-08/gold-standard/STYLE-IMPLEMENTATION-by-residual.md` (17): “Passage, verse and evidence quotations retain literary serif.”
- `grade3-reading/ui-audit-2026-09-08/gold-standard/STYLE-IMPLEMENTATION-by-residual.md` (28): “It also checks computed palette, contrast, instructional/source font distinction, vocabulary underline versus actual spoken wash, feedback rule and focus outline.”

Against: The change is a source candidate only: "This is a source candidate, not a deployed or final browser-accepted state." (`grade3-reading/ui-audit-2026-09-08/gold-standard/STYLE-IMPLEMENTATION-by-residual.md`, line 3).

<sub>criterion · stimulus, wording · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Only the text while reading

While students read, show only the text; bring questions only after the reading, take reading help away once a question appears, and let students look back at the text anytime.

A content review of a reference reading lesson asked for only the story on screen while reading, the question after the timer or read-aloud ends, the reading guide's commentary gone once a quick-check question appears, since it scaffolds the text and not the question, and a back button while reading, since free movement is what a screen loses against a book (`grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt`, lines 6-7). The course encoded each as a criterion, and its register lists them as met in the renderer (`grade3-reading/artifacts/criteria-register.csv`, lines 110-112). Let the student go back at any time while reading.

Quoted:

- `grade3-reading/artifacts/criteria-register.csv` (110): “Only the passage on screen during reading; the question appears after the timer/read-aloud ends and the child clicks next”
- `grade3-reading/artifacts/criteria-register.csv` (111): “Scout's reading commentary is a scaffold for the TEXT; it disappears when a quick-check question is on screen”
- `grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt` (7): “Lack of free movement around the book is one of the major drawbacks of not having a physical book”
- `grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd` (39): “interjections at the top of each page. They take away from the reading flow.”
- `grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd` (41): “the `passage.purpose` line printed and spoken above every story part”
- `grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd` (45-46): “nine `purpose` + `purpose_voiceover` fields deleted per lesson across L4-L7 + G5-U1-L1, nine clips retired,”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (92): “conceptual cross-unit links, and misconception sets; rebuild reading purpose,”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (125): “your “we’ve overdone questions to the detriment of the mental model” note is why the question waits off-screen.”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (40): “Story-only pages; the check appears only after “I’m done reading” | Reading needs stretches that are just reading; questions wait off-screen | 25.08 item 4, engine-wide”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (13): “and the passage always visible whenever a question asks the child to look back at it.”
- `grade3-reading/course-renderer/AGENTS.md` (275-279): “A passage page offers back every EARLIER part of its story, never a later one (`readingsBefore` in `derive-layout.ts`, rendered by `PassageNode`). A story arrives one part per page and the child's only control is Next, so by part two part one is gone: holding it in their head while answering about part two is the split-attention cost the split layout exists to remove.”
- `grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md` (866): “the child never goes back to earlier parts' text. Step 2's THEN evidence = a plain description of Part 1 plus at most one carried quote from the continuity brief; only the current part's text is quoted on screen.”
- `g9/library/text/L36b8ba.txt` (99): “Keep all previously unlocked text accessible. Gating forward is fine; nothing may lock behind the student.”
- `g9/library/text/L36b8ba.txt` (249): “Regressions in reading are genuine re-reading rather than memory checks (Booth & Weger, 2013), and a trailing mask that allowed forward reading but blocked regressions measurably impaired comprehension — not only on ambiguous sentences (Schotter, Tran & Rayner, 2014).”
- `g9/library/text/L36b8ba.txt` (101): “Give the audio per-section replay and scrub-back, so the reading is as re-hearable as the text is re-readable.”
- `g9/library/text/L36b8ba.txt` (399): “This is the strongest evidence cited in this document, and it moves backward locking from a preference to a defect.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (399): “Schotter, Tran & Rayner (2014) used a trailing mask that permitted forward reading but blocked regressions and found measurably impaired comprehension, not only on ambiguous sentences.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (249): “Locking backward removes re-reading, and re-reading is how comprehension gets repaired.”
- `othello-archive/BRIEF.md` (40): “Questions come after reading, not during it.”
- `othello-archive/src/steps/Reading.tsx` (38): “read first, undistracted; then the active part”
- `g9/library/collections/research-pack-2026-10-02/full-source-site/sources/engine/kb0180--kb-0180-lesson-structure-procedure-rulings.qmd` (61-63): “A passage page offers back every *earlier* part of the story only (`story_so_far`/`readingsBefore`), never a later one — the split-attention cost of holding an earlier part in mind is what the fold removes.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D3-reading-architecture.md` (13): “Questions are posed at key points *inside* the text, not only at the end”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/05-UI-UX-PRINCIPLES.md` (47-49): “Remove non-essential chrome (status labels, timers, and similar meta-indicators) from reading surfaces specifically — the reading experience itself should read like a book, not an instrumented app.”
- `grade3-reading/artifacts/u4l2-build/BEAT-SPEC.md` (159-160): “video first, question only after viewing (options must not be readable mid-video)”

Against: An earlier review's repair list asked to "rebuild reading purpose" (`grade3-reading/knowledge_bot/HOTBUCKET.md`, line 92), so a reading purpose is still wanted somewhere. A later run found: For one modelling routine the Grade 3 procedure spec plans the opposite: the learner never goes back to earlier parts' text, and the lesson gives a plain description of the first part with at most one carried quote, quoting only the current part on screen (`grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md`, line 866) (`grade3-reading/course-renderer/docs/pedagogy/modelling-moment-procedures.md`). A later run found counter-evidence (`grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D3-reading-architecture.md`).

<sub>criterion · stimulus, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Only what the student has read

Questions, hints, feedback and rubrics may use only the student's version of the text so far; a word asked about must be in it, exactly or as a family form.

Hand reviews of reading lessons found feedback that referred to parts of the story the student had not read yet, and a speaking task whose hints and rubric leaned on details found only in the previous lesson's text, so a student who followed the re-read hint found nothing to re-read. One rubric used a detail found only in the original book, not in the retelling the students read. That rules out later pages, another lesson's text treated as if it were this one, and the original a retelling was adapted from.

Quoted:

- `shadow-content-eval/reports/G3-U1-L11-review.md` (68): “9. **p10 `check` option 3 feedback: it refers to part of the story the student hasn't read yet.**”
- `shadow-content-eval/reports/G3-U1-L14-review.md` (32): “A student who follows "Re-read" finds nothing to re-read.”
- `shadow-content-eval/reports/G3-U1-L11-review.md` (90): “Winter is in the original book, not this retelling.”
- `shadow-content-eval/reports/G3-U1-L14-review.md` (99): “the lantern feedback *"They feel their way in the dark"* describes p10's text, which the student hasn't read yet.”
- `grade3-reading/artifacts/criteria-register.csv` (100): “A taught key word must actually occur in the passage or the hunt degrades into glowing-line tapping”
- `grade3-reading/artifacts/criteria-register.csv` (100): “shipped bug: 'wrong to trust' unhuntable in L1”
- `grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md` (45): “A hunted key word must occur in the passage, by exact word or word family”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/SUMMARY_AGENT.qmd` (99): “~53 vocab-not-in-passage”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/MCQ_REGEN_PROMPT.md` (94): “Never test a word not in the passage; never key a sense the passage does not license.”
- `othello-course-renderer-draft/repo/content/lesson-plans/g4-u1-l3.json` (308): “Do not ask where either episode comes in the voyage. It is answerable from canon by a child who has read a retelling and unanswerable from our passage unless we state it, which is a reason not to ask rather than a reason to state it.”
- `othello-course-renderer-draft/repo/docs/research/g4-u1-l2-the-cyclops.md` (788-789): “no item's answer may be a canon fact”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (29): “Two later lessons in the same arc, L5 ('menacing') and L6 ('merciless'), teach their word as an encapsulating word that is deliberately kept out of the passage so the child is the one who supplies it, and each carries a named design document waiving this rule on that basis;”
- `grade3-reading/artifacts/red-team-2026-09-23/PRE-BRIEF.md` (29): “A taught word absent from the passage carries `encapsulating {reason, authority}` | Sanctioned exemption; `validate-vocab-earned` honours it”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/integration/validate-passage-refs.txt` (6): “glossary term "narration" appears nowhere in the story or in this node's own printed text”
- `grade3-reading/ti-courseplans-wiki/Peter-Pan-Quality-Case-Study-2026-08-24.md` (126-127): “A true statement about a whole story may still be false at the learner’s current point. Claims are bounded to the text and chronology available at that beat.”
- `grade3-reading/ti-courseplans-wiki/Anatomy-of-a-Perfect-Course.md` (55-56): “A plausible statement fails when the attributed source does not say it or has not said it yet.”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-16.md` (54): “"enchanting" appears zero times in L4's passages p6/p8/p10/p12 (L1/L2 4-for-4; L5/L6 carry signed waivers).”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/CASE-FOR-APPROVAL.md` (144-145): “It had been receiving the full passage and marking children down for not quoting a text they had not been allowed to read yet”
- `othello-archive/scripts/build_content.py` (145): “Locate each Appendix A term, in order, in the text the student sees.”

Against: none found

<sub>criterion · stimulus, feedback, sequence · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Pair texts only for a named purpose

Pair two texts only for a named comparison or synthesis purpose, not merely to set them side by side.

Three reading-course packages state it. A Grade 5 course plan's case for review lists, as resolved for bounded plan review, that paired-text placements name a shared comparison or synthesis purpose rather than merely placing two texts together. The Grade 4 and Grade 6 generation contracts define paired texts as two related but separate texts, such as a poem beside an informational passage, read and compared, not one passage with an inserted stanza. It is a planning rule the packages adopted, not an outcome measured with learners.

Quoted:

- `incept-package-hub/course-packages/courses/g5-reading/review/evidence/case-for-review.md` (60): “Paired-text placements name a shared comparison or synthesis purpose rather than merely placing two texts together.”
- `incept-package-hub/.artifacts/source/g4-reading-approval-package.zip` (g4-reading-approval-package/markdown/generation-contract.md inside it) (113): “Paired texts are two related but ultimately separate texts.”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/generation-contract.md inside it) (172-173): “**Paired texts are two separate texts** (e.g. a poem beside an informational passage), related by theme,”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/generation-contract.md inside it) (173): “read and compared — not one passage with an inserted stanza.”

Against: none found

<sub>criterion · stimulus, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Rereads with a stated purpose

Every reread sends the student back to a chosen part of the text for a purpose they are told.

A review meeting on a grade 3 course asked that rereads return to selected text for a declared knowledge purpose, and the project's router records the meeting's rule that targeted rereads serve the knowledge objective. It is a rule adopted from review, not a result measured here.

Quoted:

- `grade3-reading/knowledge_bot/HOTBUCKET.md` (23): “rereads return to selected text for a declared knowledge purpose.”
- `grade3-reading/knowledge_bot/ROUTER.md` (68): “targeted rereads serve the knowledge objective;”
- `grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd` (39): “remove Scout's interjections at the top of each page. They take away from the reading flow.”
- `grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd` (41): “the `passage.purpose` line printed and spoken above every story part”

Against: Telling the purpose can cost flow: a purpose line printed and spoken above every story part was later removed because it took away from the reading flow (`grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd`, lines 39-41).

<sub>criterion · stimulus, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Same words every time

Give each taught word or concept one complete definition of its real meaning, not an incidental property, used word for word wherever it returns, keeping words taught together distinct.

A rebuilt lesson keeps each word's definition identical, word for word, on its card, in every passage glossary and in the wrap, under a one-definition rule that a validator enforces, because definition drift makes the child re-learn the word each time. A research summary on intro videos says to use the same vocabulary for an idea already taught, and the curriculum's coherence guidance asks a reading lesson to stay consistent with how the subject app framed a topic: vocabulary, level of nuance and framing. The science misconception synthesis shows what loose wording costs: biology's "high-energy phosphate bonds" language contradicts the chemistry and re-teaches the misconception even to students who learned the chemistry correctly. The definition gives the word's real meaning, and the wording carries from card, glossary, narration, feedback and review to other lessons, units and courses, checked in code. Words taught together are kept distinct, with none inside another's definition.

Quoted:

- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (79): “definition identical, word for word, on the card, in every passage glossary, and in the wrap — the one-definition rule from your reviews, enforced by a validator.”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (37): “One definition per word, identical everywhere it appears | Definition drift makes the child re-learn the word each time”
- `downloads/BrainLift - What makes a good intro video.md` (338): “Always use the same vocabulary to talk about an idea already taught so as not to confuse.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md` (14): “the Read/Write lesson should be consistent with how it was framed in the subject app — vocabulary, level of nuance, framing.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx` (31 (textutil text)): “Biology textbooks use "high-energy phosphate bonds" language that directly contradicts the correct chemistry.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx` (31 (textutil text)): “Even students who learned the correct chemistry are re-taught the misconception in biology class.”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (38-39): “One definition per word, used everywhere it recurs — reading goal, passage glossary, feedback”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (39-40): “choose the best definition and make sure your LLM uses the same one throughout”
- `grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd` (157-158): “fixed by using one card definition everywhere the word recurs”
- `grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd` (34): “Reinforce, do not redefine”
- `grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd` (36): “Where a topic has already been covered, the Read/Write lesson should be consistent with how it was framed in the subject app, including its vocabulary, level of nuance, and framing.”
- `grade3-reading/knowledge_bot/knowledge/kb-0238-l4-baseline-submission-and-signoff-packet-2026-08-31.qmd` (65): “3,003 child-facing strings”
- `grade3-reading/knowledge_bot/knowledge/kb-0238-l4-baseline-submission-and-signoff-packet-2026-08-31.qmd` (65-66): “regex-hunting for number-word/countable-noun mismatches, same-term double-meanings”
- `grade3-reading/knowledge_bot/knowledge/kb-0238-l4-baseline-submission-and-signoff-packet-2026-08-31.qmd` (67): “Result: 0 live contradictions”
- `grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` (132): “sometimes testing whether students can transfer across surface variation is the point”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (38): “One definition per word, used everywhere it recurs — reading goal, passage glossary,”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (30-31): “Taught words in one lesson must be distinct — never overlapping in meaning, never one appearing inside another's own definition”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (32): “Not enforced.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (105): “*blend* even appears inside the definition of *camouflage*.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (105): “- Choose distinct vocabulary words.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (105): “overlap too much; *blend* even appears inside the definition of *camouflage*”
- `grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md` (43): “One definition per word, verbatim everywhere”
- `grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md` (19): “three different trait rules; feelings keyed as traits; invented "again and again"”
- `grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md` (24): “"triumphant" two meanings”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/KB_FURTHER_IMPROVEMENTS.md` (46): “Canonical hinge proposition per weak skill** propagated verbatim teach→CFU→review”
- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md` (217): “subject and verb" fails the rubric for being right. If the card must exist, define”
- `grade3-reading/artifacts/g5-course/VOCAB-DECISIONS-U1.md` (31): “the canon defines `evidence` three different ways”
- `grade3-reading/artifacts/wiki-research/redteam-standard.md` (186): “A2 one verbatim definition per concept”
- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (805): “J16-SCI-003: Reinforce rather than silently redefine established domain knowledge.”
- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (805): “J16-SCI-006: Keep cross-domain terminology and mechanisms consistent.”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (148): “energy language in one unit contradicting another (ATP archetype)”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (148): “scan all units together; flag conflicting framings of energy/conservation”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (149): “reinforce-don't-redefine (consistent with the subject app's framing)”
- `shadow-content-eval/reports/G3-U1-L2-review.md` (95): “The glossary and the video also define things differently: jewels are "Rare stones" vs "precious stones", and the glossary adds that a genie "lives in a lamp or ring".”
- `shadow-content-eval/SKILL.md` (281): “the card, glossary, review frame and meaning lines define the word differently (stemmed word overlap under 0.34)”
- `shadow-content-eval/SKILL.md` (280): “| `VOCAB-DEF-CIRCULAR` | med | the definition uses the word itself |”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (106-107): “A taught concept has exactly **one** authored definition string, and every surface that defines it uses that string verbatim.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (111-113): “A definition that omits the load-bearing part of the concept teaches a wrong one even though every word in it is true.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (137-138): “Prefer a definition by **method** (what the character *does*) over one by **property** (what they *are*).”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (126): “*trickster* carried **four** definitions in one lesson”
- `g9/transformer/v10/README.md` (7): “Consistency sweeps across a unit: terms, glossary priorities, key quotations.”
- `grade3-reading/course-renderer/docs/video/u1-script-critique.md` (94-98): “Distractor 3 is the only one that already contains the word "poem", so it is the one distractor a child picks *because* they heard the video say poem and reached for the vocabulary. The correction they read answers a length objection and drops the genus, so the child who was closest to right is the only one whose feedback never tells them an epic is a poem.”
- `grade3-reading/course-renderer/docs/video/u1-script-critique.md` (101): “Rewrite feedback[3] so it carries the genus”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/methodology/README.md` (41): “maintain one definition across cards, text, feedback and media.”
- `grade3-reading/ui-audit-2026-09-08/feedback-reconciliation/invariants.dom.txt` (880): “Choose one definition for a taught word and use exactly it in every later mention, including the reading goal, the passage glossary and any feedback.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/glossary/VOCABULARY-CONSISTENCY-PROPOSAL.md` (16): “That depicts anticipation in their fight; it does not establish a particular plan or prove that nobody notices it.”
- `grade3-reading/course-renderer/authoring/inputs/prompt-packs/reading-g3/subjects/reading.md` (34-36): “**Define by method, not by property.** Define the word by what the thing DOES ("wins by using smart tricks, not by fighting"), never by a property ("wins because he is small and clever") that excludes cases that fit.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-4/feedback-on-iteration-4/feedback-0806-pedagogy.md` (32): “The reviewer found two definitions. There are **four**:”
- `othello-course-renderer-draft/repo/docs/rules/vocabulary.md` (104-106): “It caught one the day it was written: shortening `trial`'s card left the story's glossary still handing a child the old three-sentence version.”
- `othello-course-renderer-draft/repo/authoring/inputs/rule-packs/reading-g3.json` (194): “define the word by what the thing DOES, never by what it IS. 'wins by using smart tricks, not by fighting' is right; 'wins because he is small and clever' is wrong, because it makes a property part of the meaning and excludes cases that genuinely fit.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-15.md` (152): “validate-vocab-earned.mjs requires every instance of a term to agree word for word, so all seven must change together or the check goes red”

Against: Keeping the same words is not always the aim: sometimes testing whether students can transfer across surface variation is the point. The lesson engine glosses each word for the sense its own line uses (see 'Words that carry the knowledge'), so one fixed definition could be wrong where a word changes sense. whether taught words are distinct is not checked in code. One wording used everywhere spreads its errors too: one wrong definition sat on every visible passage of a lesson (`grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md`). The comparison needs stemming: "Without stemming, L5 *menacing* was a false positive." (`shadow/content-eval/SKILL.md`, lines 314-315). A later run found counter-evidence (`grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/glossary/VOCABULARY-CONSISTENCY-PROPOSAL.md`).

<sub>criterion · wording, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Show every text the lesson points to

Put every text a learner must read in the lesson's main path, never only behind a control they must notice, and show any text the passage alludes to.

In a Grade 3 reading build, one lesson carried a second, real published text paired with its story for weeks, but the player never read that field, so all of it was inert while the passage alluded to it. The rules that followed give the second text its own steps at the head of the reading phase, before the story, and keep the toggle between the two only as the way back, because a text reachable only from a control a child has to notice is one most children never read. An earlier fix that shipped the toggle alone was judged half the fix. The rules add that an allusion to nothing is worse than none, since it punishes the child who notices it.

Quoted:

- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (121-122): “U1-L5 was authored with one for weeks and the v4 player never read the key, so all of it was inert — and the passage ALLUDES to it”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (124-125): “An allusion to nothing is worse than no allusion: the child who does the work of noticing it is the one who gets punished for it.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (126-127): “The poem gets its OWN beats at the head of Phase B, before the story.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (128-129): “a second text reachable only from a control a child has to notice is a second text most children never read.”
- `grade3-reading/edullm-review-hub/course-packages/archive/g3-reading-v4/content-for-analysis/BUILD-RULES.md` (130): “on its own it is half the fix.”

Against: none found

<sub>criterion · stimulus, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Show the source; don't describe it

Give students the source itself to analyse, the excerpt, map, picture or chart the item says it rests on, never a prose description, summary or note about it. One model's document-based items, built on descriptions of absent maps and invented sources, scored 0.0% in all three runs.

An autopsy found one AP model's document-based items structurally at zero because its documents were descriptions of visual artifacts or invented sources, not usable source text, and the evaluator's source check failed them even when the rest looked plausible (`dbq_structural_zero.md`, line 9). Its first example described a map in prose, with no map, no extractable text and nothing for the student to analyse, and the item type stayed at 0.0% across three runs (lines 55 and 107). The rule it set: every document carries analysable text, and a visual is allowed only when the real image or a faithful caption comes from retrieval, never invented by the model (line 122). A description is not a source, and a note on a source's purpose or significance does the analysis for the student.

Quoted:

- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md` (55): “Why it fails: the model describes an absent map.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md` (55): “There is no actual map, no extractable source text, and no real primary-source passage for the student to analyze.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md` (9): “DBQ is structurally zero on the current InceptBench path because the generator emits DBQ "documents" that are visual artifact descriptions or fabricated source descriptions, not usable source text.”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md` (107): “| v52 3-seed | IB v2.5.7 | 0.0% | r1/r2/r3 all zero; v52 aggregate only 57.57% |”
- `icloud-work/aptraining-crystal-copy-20260521/full-copy/parallel-ideas-lab/reports/dbq_structural_zero.md` (122): “If a visual source is ever allowed, the actual visual or a faithful OCR/caption payload must be supplied by retrieval, not invented by the model.”
- `icloud-work/aptraining/.agent/research/gate1_decision.md` (35): “`passage_reference` failing in 33% of fails is the second pattern: the model writes stimulus passages that reference content the stimulus doesn't actually contain.”
- `icloud-work/aptraining/.agent/memory/BEADS.md` (99): “factual_accuracy 32/43 = 74%, passage_reference 14/43 = 33%, clarity_precision 6/43, curriculum_alignment 3/43, others <5%.”
- `icloud-work/aptraining/.agent/memory/state_training_chain_2026_05_12T1300Z.md` (51): “DBQ 0/30 = 0% on IB v2.5.7 is STRUCTURAL not knowledge”
- `icloud-work/aptraining/.agent/memory/state_training_chain_2026_05_12T1300Z.md` (52): “26 of 30 failures (87%) flag visual artifact promise/deliver mismatch”
- `icloud-work/aptraining/.agent/memory/state_training_chain_2026_05_12T1300Z.md` (53): “Model promises "Document 1: [a map of X]" but only writes prose description”
- `icloud-work/aptraining/.agent/memory/state_training_chain_2026_05_12T1300Z.md` (54): “IB rule: prose description of absent visual = stimulus_quality 0 hard”
- `icloud-work/aptraining/.agent/research/inference_clean.md` (35): “IB flags these as poor stimulus quality since they describe images rather than containing text”
- `icloud-work/aptraining/.agent/research/inference_clean.md` (402): “rubric grader does NOT see the image bytes (or at most sees URLs)”
- `aptraining-local/den-of-ideation/to_main/2026-05-24T1059Z_DEN_REQUEST_validate_unit1_dbq_solver_v2_source_text_repair.md` (20): “The shared failure class was analysis leakage in DBQ document text: summaries gave away source purpose/significance instead of making students infer it.”
- `aptraining-local/den-of-ideation/to_main/2026-05-24T1059Z_DEN_REQUEST_validate_unit1_dbq_solver_v2_source_text_repair.md` (22): “v2 keeps the same routing and source-pack boundary, but repairs the document text for the failure topics and strips analysis-giveaway sentences.”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T1958Z_DELIVERED_unit1_dbq_solver_v1_candidate.md` (73): “Cultural perspective row improved 0.55 -> 0.70 -> 1.0 after replacing summary docs with source-like excerpts and adding Indigenous-perspective documents.”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-24T0255Z_DELIVERED_unit9_dbq_solver_v1_candidate.md` (29): “Migration/immigration hard row initially scored `0.675 INFERIOR` because the documents read like summaries rather than source excerpts.”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-24T0255Z_DELIVERED_unit9_dbq_solver_v1_candidate.md` (33): “result: `1.0 SUPERIOR`”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T2115Z_DELIVERED_unit8_dbq_solver_v1_candidate.md` (46): “Initial U8 DBQ smoke failed because documents were summaries/meta-commentary.”
- `g9/player/design/ARCHIVIST-DESIGN.md` (353): “The card is a record with a small keeper, not a keeper with a small record.”

Against: The reading of the passage-reference failures is the analysis's gloss on the judge's dimension; the failing items are not quoted, and both counts come from one model and one judge. That judge reads text and sees at most an image's address, so it cannot tell whether a real picture would have served (`icloud-work/aptraining/.agent/research/inference_clean.md`). The repaired packs were themselves "normalized excerpts/source summaries" (icloud-work/aptraining/workspace/comms/from_den/2026-05-23T2009Z_DELIVERED_unit8_dbq_source_pack_gate.md, line 36), the replacements were "source-like" rather than verbatim excerpts, and each gain was measured on the rows that defined the failure.

<sub>criterion · stimulus, media, integrity · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Show the text the task needs

Whenever a task, prompt or feedback asks a student to find or cite evidence or sends them back to the text, keep the text on screen.

An outside review of a course found prompts asking students to cite the text while the passage was hidden, so they were told to look back at a text that was gone (`grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt`). A walkthrough of a later course found the transfer items of most lessons shown beside the wrong pinned passage, with the open-response marker handed that same wrong text (`grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md`), and an earlier review found a pinned excerpt that held only the lines of wrong answers (`grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md`). The text sits beside the live question and steps, showing the part that holds the evidence.

Quoted:

- `grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt` (45): “Prompts ask students to cite text evidence, but the passage is hidden at that point ("try looking back at the text" — but the text is gone).”
- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md` (76): “WRONG pinned passage, and the open-response scorer is handed that wrong text.**”
- `grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md` (124): “the pin shows only wrong”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (86): “- Prompts ask for textual evidence, but the passage is hidden when the student needs to cite it.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (56): “## Feedback table: direct blockers”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md` (13): “| L2 | passage visibility | `cites_text` implies `passage_visible` on every atom. |”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (281-282): “evidence-writing hides the passage”
- `grade3-reading/knowledge_bot/knowledge/kb-0191-g3-book-lesson-anatomy.qmd` (70-73): “A page's own passage wins over an earlier one — this was a real, fixed bug: the renderer used to pin whichever passage came last in the whole lesson and drop the page's own passage on the floor, which could show a different part of the story than the one a proof-question was asking about.”
- `grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd` (86): “Prompts ask for textual evidence, but the passage is hidden when the student needs to cite it.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (84): “The steps and live question must remain visible, and the model should surface one thing at a time; the current screen contains too much at once.”
- `grade3-reading/ti-courseplans/docs/instruction-quality-standard.md` (38-39): “Whenever feedback or a prompt asks the student to cite or look back at the text, the text must be visible.”
- `grade3-reading/ti-courseplans/docs/instruction-quality-standard.md` (39-40): “"Try looking back at the text" with the passage hidden is a defect class, not a UX nit.”
- `grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md` (140): “15. Put the check **next to** the text, not below (below = split attention, scrolling up to find the answer).”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd` (90): “A complete encounter precedes close analysis; evidence remains available;”
- `grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md` (112-113): “6. Corrective feedback must be short, misconception-naming, evidence-anchored, and delivered with the text visible”
- `g9/player/design/ARCHIVIST-DESIGN.md` (356): “**6.2 previous text stays accessible while answering**”
- `g9/film/v06/README.md` (20-21): “Also: the unit words are bold in the captions, and the player blurs the film while a check is open, because two checks now pause over plates that show their answer.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/IMPLEMENTATION-HANDOFF.md` (11): “Fifteen added silent source copies fix the incorrect assumption that /book carried preceding text forward.”
- `grade3-reading/visual-findings-2026-09-08/grade5-book-flow/README.md` (10): “Practice keeps the source text beside the task.”
- `grade3-reading/incept-read-app/docs/G4-SCR-example-native-qti.md` (53): “links the passage so the child can read it while writing.”
- `grade3-reading/ui-audit-2026-09-08/round-1/g3/findings.json` (145): “grounding sent to a grader is not text visible to the learner.”
- `grade3-reading/ui-audit-2026-09-08/round-1/g3/REPORT.md` (10): “L7 p17 asks for the story’s own words but provides neither text nor reread access.”
- `g9/player/design/ARCHIVIST-DESIGN.md` (246): “text persists while the child answers" rule (6.2) carried to the film”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (334): “The invariant is that the text stays visible; its position follows its length.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (116): “Keep the Check Part 1 pattern: text and question on screen together, text persists, answer in the student’s own words.”
- `g9/library/text/L36b8ba.txt` (334): “The invariant is that the text stays visible; its position follows its length.”
- `othello-course-renderer-draft/repo/docs/design/grade-9/research/edtech-desktop-design.md` (101): “Ginns (2006) meta-analysis of 50 studies: spatial contiguity effect about d = 0.72, larger for complex material.”
- `grade3-reading/artifacts/u4l2-build/BEAT-SPEC.md` (254-255): “The story stays beside the check (split-attention fix) — never scrolled away.”

Against: What stays in view is what has been read: the project's engine offers back only the earlier parts of a story on a passage page, never a later one (`grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd`, lines 61-62); and a film is a different case, where few words on screen help (see the record on few words on screen).

<sub>criterion · stimulus, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Show who wrote a source and why

When a question rests on a primary source, show students who wrote it and why, and cite it accurately. Correcting one source's citation and showing another's purpose was one of six repairs an audit required before a unit could be copied.

An independent semantic audit of an AP history unit found no wrong or ambiguous key but blocked the unit from being replicated on six repair buckets. One bucket was to correct a source's citation to the right chapters and collection, and to add the reform-advocate purpose behind another source to the citation context students see. A later commit closed all six, after which the unit's validator passed with zero errors and zero warnings.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd` (59): “no wrong or ambiguous MCQ key”
- `grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd` (65): “chapters I, III, and V and Library of Congress General Collections”
- `grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd` (66): “reform-advocate purpose to student-visible citation context.”
- `grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd` (86): “closes the six repair buckets recorded in kb-0167”
- `grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd` (89-90): “passed with zero errors and zero warnings”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (110-112): “The identity of the creator, date, repository, edition, excerpt boundary, adaptation, rights basis, and content digest determine what the student is actually reading. Those facts also shape the historical interpretation.”

Against: none found

<sub>criterion · stimulus, integrity · domain · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Simplify without saying anything false

Simplify without saying or implying anything false, keeping the same conceptual foundation at every level and presenting every model or diagram as a simplification, never as literal reality. The same question from a grade 3 and a grade 8 student gets different detail but the same conceptual foundation.

The science misconception synthesis has every model carry an explicit health warning that it is a simplified picture and leaves out a lot of detail, and makes a framing statement mandatory whenever an AI system presents a diagram, equation or simplified explanation; the biology card repeats it for every cell diagram. When a question goes beyond a student's level, the chemistry card's answer for grades K-2 gives a true partial account and says more comes in later grades, and the synthesis asks that the same question from a grade 3 and a grade 8 student get different detail but the same conceptual foundation. Check what wording implies as well as what it says.

Quoted:

- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx` (119 (textutil text)): “Every model should carry an explicit health warning: "This is a simplified picture that helps us understand one thing. It leaves out a lot of detail.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx` (121 (textutil text)): “Whenever an LLM system presents a model (diagram, equation, simplified explanation), it MUST include a brief framing statement indicating that the model is a simplification.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx` (260 (textutil text)): “Every time a cell diagram is shown, include the explicit framing”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx` (124 (textutil text)): “You'll learn more about what's inside atoms in later grades.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx` (251 (textutil text)): “The same question from a grade 3 student and a grade 8 student should receive different levels of detail and different mathematical framing, but the SAME conceptual foundation.”
- `grade3-reading/knowledge_bot/knowledge/kb-0141-cross-cutting-science-misconception-synthesis.qmd` (140): “**Every model should carry an explicit health warning:**”
- `grade3-reading/knowledge_bot/knowledge/kb-0141-cross-cutting-science-misconception-synthesis.qmd` (144): “it MUST include a brief framing statement indicating that the model is a simplification.”
- `grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` (66): “diagrams or models presented as literal reality;”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (135-136): “A reading passage that embeds folk science is not neutral prose — it actively undoes correct science instruction”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (145): “"the plant grows by taking food from the soil" implies plants-eat-soil without the literal phrase”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (147): “a food chain / atom / cell diagram presented as literal reality”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (147): “is a "this is a simplification" note present when a model appears?”
- `ti-courseplans-audit/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (802): “Simplification is acceptable only when it remains accurate and does not create a later-blocking misconception.”
- `grade3-reading/course-renderer/docs/pedagogy/misconceptions/cross-cutting-synthesis.md` (311): “The same question from a grade 3 student and a grade 8 student should receive different levels of detail and different mathematical framing, but the SAME conceptual foundation.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-qc-evidence-v0.1.md` (237-239): “Human eye color is really polygenic; the single-gene B/b cross is the standard G7 classroom simplification for a *first* Punnett square. **Accepted.**”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/misconception-check.md inside it) (36-40): “must be framed as a simplified representation, not literal reality”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (352-354): “The Columbian Exchange is often reduced to arrows showing crops, animals, and disease moving both ways. That representation can hide radically unequal demographic effects, coercion, and the role of existing Indigenous and Atlantic systems.”

Against: A later run found counter-evidence (`grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-qc-evidence-v0.1.md`).

<sub>criterion · integrity, wording, media · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Speaker names only where speeches start

In a play's text on screen, show a speaker's name only where a speech starts, as a printed script does, not on every line. A test checks that of a scene's first four lines only the first and the fourth carry a speaker's name.

Another build's renderer drew this engine's play text in its own script layout, and its first render showed a speaker's name on every line. It was fixed so that a name appears only where a speech starts, and a test on the exported lesson checks the speakers of the first four lines: a name, none, none, a name.

Quoted:

- `g9/transformer/v02/QA.md` (46-47): “(speaker names only where a speech starts, fixed after the first render showed them on every line)”
- `g9/transformer/test/animated.test.mjs` (21): “a name only where a speech starts”

Against: none found

<sub>criterion · stimulus · universal · from g9 · adopted-rule · held · found in [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Staged text never locks behind the reader

When a text is released in stages, add each part to one continuous column, and keep everything already unlocked there to reread and its audio to replay.

A review of a Grade 9 prototype accepted staged unlocking forward, which paces the reading, but ruled that nothing already unlocked may become inaccessible and that new text should append to one scrolling column, so it reads as continuous rather than as a series of cards. It extended the rule to the audio, with per-section replay and scrub-back. It rests the rule on two eye-movement studies it names, which found that regressions in reading are genuine rereading and that blocking them impaired comprehension, and calls this its strongest evidence, moving backward locking from a preference to a defect.

Quoted:

- `g9/sources/Othello_1_Feedback_DevFactory.md` (99): “Keep all previously unlocked text accessible. Gating forward is fine; nothing may lock behind the student.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (100): “Append new text to one scrolling column so the script reads as continuous rather than as a series of cards.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (101): “Give the audio per-section replay and scrub-back, so the reading is as re-hearable as the text is re-readable.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (249): “Gating forward is legitimate: it stops a child racing ahead of comprehension. Locking backward removes re-reading, and re-reading is how comprehension gets repaired.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (399): “Booth & Weger (2013) found that regressions during reading are genuine re-reading rather than memory checks.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (399): “Schotter, Tran & Rayner (2014) used a trailing mask that permitted forward reading but blocked regressions and found measurably impaired comprehension, not only on ambiguous sentences.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (399): “This is the strongest evidence cited in this document, and it moves backward locking from a preference to a defect.”

Published: [Booth & Weger 2013, The function of regressions in reading: Backward eye movements allow rereading, Memory & Cognition 41, 82-97](https://doi.org/10.3758/s13421-012-0244-y) · [Schotter, Tran & Rayner 2014, Don't believe what you read (only once): Comprehension is supported by regressions during reading, Psychological Science 25, 1218-1226](https://doi.org/10.1177/0956797614531148)

Against: The prototype revealed the text one tap at a time ("So you know we show a starting line and then the student taps next to show the next thing and and so on.", `g9/sources/meeting-notes/Incept Service CoE Catchup - 2026_10_07 10_30 CEST - Notes by Gemini.md`, line 356), which is the forward gating the review allows.

<sub>criterion · stimulus, sequence, media · universal · from g9, research · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Support every hard word in a passage

Let students hear every hard word in a passage and see what it means, not only the taught words, so no question turns on a word they were never given. A review found hard passage words left undefined beyond a lesson's three taught words.

A review of a Grade 3 reading course asked for difficult words beyond the three designated vocabulary words to be handled, since passage words were left undefined, and for hard words to be tappable and read aloud for students who cannot yet decode them. The course's rulebook adopted it: hard passage words, even untaught ones, are tappable and read aloud. An evaluator gap analysis names the same risk for questions: untaught vocabulary or syntax can create construct-irrelevant difficulty.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (106): “Handle difficult words beyond the three designated vocabulary words.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (107): “- Make difficult words tappable and readable aloud—"hear it, say it, map it"—for students who cannot yet decode them.”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (41): “Hard *passage* words, even untaught ones, are tappable and read aloud”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (43): “which words must be in it is not checked”
- `grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd` (126): “- N5: linguistic validity. Untaught vocabulary or syntax can create construct-irrelevant difficulty.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (271): “bold plus a dotted underline, available on demand, not interrupting the reading line.”
- `g9/sources/Act 1 reading texts/Act 1/1. 1.1 - Iago_s Introduction - Text.docx` (2): “Words in bold are hover targets (Appendix A).”
- `g9/sources/3-D-Shakespeare-Othello-1.1.pdf` (102): “Let the students work out the meanings.”
- `g9/sources/3-D-Shakespeare-Othello-1.1.pdf` (101-104): “Invite students to share any words that they didn’t understand, and resist telling the class any answers. Let the students work out the meanings. Getting the basic gist of a word or phrase on their own is better than having the teacher give a precise definition.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (75): “vocabulary used in assessment stems (seized, untamed, mischief, daring, hovered, breathless, gust) is all glossary-listed on p19/p21/p22 (glossary object present on every passage node) or directly contextualized”

Against: a validator checks that the glossary is there, not which words it must hold. A later run found: A classroom guide in the sources takes the opposite line for a class working out a scene it has never read: learners share the words they didn't understand and work out the meanings themselves, which it holds is better than being given a precise definition (`g9/sources/3-D-Shakespeare-Othello-1.1.pdf`). A later run found counter-evidence (`g9/sources/3-D-Shakespeare-Othello-1.1.pdf`).

<sub>criterion · accessibility, wording, demand · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Teach a word before using it

Use no word students may not know before the lesson teaches it, narration counting as teaching, and teach technical words directly, since context fails when the subject is new. Counting only formal definitions, one checker reported three words as untaught that a lesson's narration defined outright.

The content audit for Grade 3 reading lessons flags a word used on an earlier page than the one that introduces it, unless it is in the grade's known-word baseline, and counts the video narration as instruction on a par with a vocabulary card or glossary; counting only formal definitions had reported three words as untaught that the first lesson's narration defined outright (`shadow/content-eval/SKILL.md`). Hand reviews still found untaught words where students meet them: a recap that uses "catalyst", and three unexplained words in a passage, a model answer and a reveal (`shadow/content-eval/reports/G3-U1-L14-review.md`, `shadow/content-eval/reports/G3-U1-L2-review.md`).

Quoted:

- `shadow-content-eval/SKILL.md` (63): “The **video transcript counts as delivered instruction** — anything the narration says is introduced, on equal footing with a vocab card or glossary.”
- `shadow-content-eval/SKILL.md` (63): “Counting only formal definitions reported `sultan`/`stranger`/`magic` as untaught when the L1 narration defines them outright”
- `shadow-content-eval/reports/G3-U1-L14-review.md` (81): “It uses *"that is how actions are a **catalyst** for change"*, which isn't a grade-3 word and isn't taught.”
- `shadow-content-eval/reports/G3-U1-L2-review.md` (94): “- **Words:** `revenge` (p6 passage, which the think-aloud relies on; not in L1 or the glossary), `desperate` (the model answer) and `ambitious` (the step4 reveal, which the student sees) are all unexplained.”
- `downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx` (sheet 'Standard components', cell D46): “Use context to work out the meaning of a domain-specific word”
- `downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx` (sheet 'Standard components', cell E46): “Child can't use context when the whole domain is unfamiliar. The surrounding text doesn't help because the concepts are also new.”
- `downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of G3-8_Threads_FourTier.docx` (396 (textutil text)): “Each unit's technical terminology (above) must be listed in the KB, taught before reading, and carried with spaced recall”
- `g9/sources/Cutting-a-Scene-Othello-1.1.pdf` (162): “Did you, the teacher, resist defining or explaining words?”

Against: The thread map's line sits on its list of things to fix or consider, so it is a plan rather than a measured result. A later run found counter-evidence (`g9/sources/Cutting-a-Scene-Othello-1.1.pdf`).

<sub>criterion · wording, sequence · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Teaching fiction must be a real story

Write teaching fiction as a real story, with a want, an obstacle and a turn shown in scenes, and let its theme be acted out rather than stated.

A grade-4 definition of good reading material asks for fiction that is actually fiction: dramatized scenes rather than summarized events, with the theme enacted and never stated, and the same definition rules out moral-stating closers, checked by a show-don't-tell critic. It notes outside feedback that fiction needs room to tell a story, and the course's length ladder lets fiction run longer than its informational siblings, up to about 600-750 words in the last units.

Quoted:

- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/PEDAGOGY.md` (139-140): “**Fiction that is actually fiction**: a want, an obstacle, a turn — dramatized scenes, not summarized events; theme enacted, never stated”
- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/PEDAGOGY.md` (130-131): “no AI slop — no throat-clearing openers, no moral-stating closers, no encyclopedic drone”
- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/LENGTH-RATIONALE.md` (13): “| U1–U2 | ~350–450 | fiction runs longer than its informational siblings |”
- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/LENGTH-RATIONALE.md` (15): “| U6–U7 | ~600–750 | a story needs room; poems exempt |”

Against: none found

<sub>criterion · stimulus, wording · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Text within the grade's reading band

Keep every passage students must read suited to their age and within, or only just above, their grade's reading band. Adult-register passages had been passing evaluation at 0.95 before the rule was added.

The AP work's evaluator asks, in its English rubric for grades 3 to 8, that the passage, transcript or writing samples a student must read sit within, or only modestly above, the typical reading band for the grade, and flags a stimulus whose college or adult-professional words run across the passage when a same-skill version could be written in grade-band words (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/ela_evaluation.txt`). It does not flag a single domain term, or a term the targeted standard names or teaches. The rule was added after adult-register passages had been passing evaluation at 0.95 despite real grade-band problems (`icloud-work/inceptbench-main/tests/test_evaluator_prompt_rules_411_418.py`). The closed-ended rubric likewise flags words well above the grade's reading level when a simpler word exists and the word is not a curriculum term being taught (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt`). Flag a sustained adult register rather than a single hard term or a word the lesson teaches. Check the grade level the code is set to: an early plan for a reading course added an age check to its rubric and fixed a grade-11-to-grade-3 setting found in the code (`grade3-reading/knowledge_bot/knowledge/kb-0221-early-planning-history-and-sep22-snapshots.qmd`).

Quoted:

- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/ela_evaluation.txt` (43-45): “For ELA items targeting grades 3–8, the passage, transcript, or writing samples that the student must read should sit within (or only modestly above) the typical reading band for the target grade.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/ela_evaluation.txt` (52-54): “Do NOT flag because a single domain term appears once; the failure is a sustained register mismatch across the passage.”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/ela_evaluation.txt` (54-56): “Do NOT flag a science or social-studies term that the targeted standard itself names or that is part of the skill being taught.”
- `icloud-work/inceptbench-main/tests/test_evaluator_prompt_rules_411_418.py` (10-11): “adult-register passages were passing evaluation at 0.95 ACCEPTABLE despite real grade-band problems”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/closed_ended_evaluation.txt` (427): “- **Grade-inappropriate vocabulary**: Uses words or phrases significantly above the target grade's reading level when a simpler, grade-appropriate alternative exists AND the word is NOT a curriculum term being taught in the referenced standard (see Checklist D)”
- `icloud-work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt` (131-132): “task demand matters more than prose complexity. Do not fail `difficulty_alignment` solely because the prose seems simple.”
- `grade3-reading/knowledge_bot/knowledge/kb-0221-early-planning-history-and-sep22-snapshots.qmd` (76-77): “add an age-appropriateness check to the team rubric, fix a grade-11-to-grade-3 setting found in the code;”
- `grade3-reading/knowledge_bot/knowledge/kb-0008-alpha-courses-repo.qmd` (147): “fluency passages regenerated after a first pass leaked Tier-3 vocabulary”
- `grade3-reading/knowledge_bot/knowledge/kb-0215-g5-media-recovery-plan-and-edullm-entrypoint-test.qmd` (83-84): “43/48 passages mechanically fail the G3 text screen”
- `othello-course-renderer-draft/repo/authoring/inputs/rule-packs/reading-g3.json` (39): “A band for MEASURING a passage, and for gating one only when we wrote it. gen_v3 spent whole refine budgets enforcing a Lexile target on folktales that were never going to reach it”
- `othello-course-renderer-draft/repo/content/lesson-plans/g3-u2-l1.json` (159): “The rule pack does not gate corpus text on readability, so 620 is an authoring reference carried from the shipped Grade-3 plans, not a measurement of this text.”
- `grade3-reading/_archive/2026-08-13-consolidation/orientation-sweep-digest/beads-ledger.md` (4): “reading-bth 43/48 passages hard-FAIL the G3 text screen (40/48 >1 grade above band, only 3/48 in 1.5-4.5 band);”
- `grade3-reading/course-renderer/docs/extras/g4-crosswalk-2026-08-17.md` (82): “Their 84 texts average Flesch-Kincaid grade 9.7; seven of their units run 10.5–11.9 — high-school prose in Grade-4 folders, at roughly 540 words against our 340–390-word slots.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/PLAN-EVALUATION.md inside it) (105-106): “presence of a poem ≠ a grade-appropriate poem.”
- `othello-course-renderer-draft/repo/docs/extras/g4-crosswalk-2026-08-17.md` (82): “Their 84 texts average Flesch-Kincaid grade 9.7; seven of their units run 10.5–11.9 — high-school prose in Grade-4 folders, at roughly 540 words against our 340–390-word slots.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (44): “p12 (the final story passage, 'the flight to Neverland') sits above the G3 readability ceiling: Flesch-Kincaid grade 6.0, driven by a 34-word cumulative sentence.”

Against: The standardized-test reading rubric puts task demand ahead of prose complexity and does not fail an item's difficulty only because its prose seems simple (`icloud-work/inceptbench-main/src/inceptbench/prompts/question/sat_rw_evaluation.txt`, L131-132). A later run found counter-evidence (`grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md`).

<sub>criterion · stimulus, wording, demand · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Texts chosen for more than readability

Choose a course's texts for their purpose, the knowledge they build in sequence, a balance of genres and their quality, judged by reading them, not by a readability score alone. One course chosen mainly by readability had essentially no poetry and no drama, short of its own roughly 40/40/20 target.

A course review found a Grade 3 course's texts chosen mainly by Lexile: overwhelmingly informational, with essentially no poetry and no drama, short of the course's own roughly 40/40/20 literary, informational and vocabulary target; Lexile alone, it noted, mishandles poetry and narrative and cannot tell whether a text is worth reading (`grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md`). It asked for texts chosen for a coherent knowledge sequence and a genre balance, with complexity judged qualitatively as well as by Lexile. The reading team's insights BrainLift holds that text difficulty is a match among text, reader knowledge and task that no single readability number can gate (`grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd`).

Quoted:

- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (51): “Lexile alone also mishandles poetry and narrative and cannot tell you whether a text is worth reading.”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (53): “***To change this:*** Choose texts for a coherent knowledge sequence and a genre balance that includes poetry, drama and more literary work, and judge complexity qualitatively as well as by Lexile.”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (51): “with literary text a minority and essentially no poetry and no drama. That falls short of even the course’s own roughly 40/40/20 literary/informational/vocabulary target.”
- `grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd` (59): “Text difficulty is a match among text factors, reader knowledge, and task — no single readability number can gate a text”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (78): “Choose texts for a coherent knowledge sequence and a genre balance that includes poetry, drama and more literary work, and judge complexity qualitatively as well as by Lexile.”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (94): “Course passages run 58 to 217 words, averaging about 166.”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (92): “STAAR presents up to roughly 2,740 words across two single passages and one paired set”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (94): “Practising only on very short texts does not build that stamina.”
- `ti-courseplans-audit/docs/course-formula-agents.md` (166): “G3 was flagged at **~22% literary vs ~40% target** because texts were picked on Lexile alone”
- `ti-courseplans-audit/skills/g3-reading-red-team/references/dimensions/D8-text-quality.md` (22): “No rigid monotonic Lexile laddering is imposed, since prior knowledge can make a harder text accessible”
- `ti-courseplans-audit/skills/timeback-course-eval/references/eval-criteria.md` (115): “complexity judged qualitatively, not by Lexile alone”
- `ti-courseplans-audit/docs/redteam-sources/g5-reading-redteam-round1-2026-07-06.md` (31): “the ~40/40/20 composition target is admitted as "an assumption with an open source ask"”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (76): “Lexile alone also mishandles poetry and narrative and cannot tell you whether a text is worth reading.”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (76): “Selection is driven mainly by Lexile.”
- `grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd` (76): “with literary text a minority and essentially no poetry and no drama. That falls short of even the course's own roughly 40/40/20 literary/informational/vocabulary target.”
- `grade3-reading/course-renderer/docs/rules/knowledge-and-curriculum.md` (120-122): “"Students will study science and social studies, so some of the knowledge will be covered there. You can factor in much more fiction."”
- `grade3-reading/course-renderer/docs/rules/knowledge-and-curriculum.md` (129-130): “Followed by convention; the genre mix is visible in `content/course-map.json` but nothing checks it.”
- `grade3-reading/course-renderer/docs/feedback/academics-review-2026-06-29.md` (54): “Selection is driven mainly by Lexile. The build is overwhelmingly informational (the heaviest standards tags are RI.3.1, RI.3.3, RI.3.2, RI.3.8, RI.3.4), with literary text a minority and essentially no poetry and no drama.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/GENRE-BALANCE.md inside it) (13): “**Genre = the FORM of the main text the student reads**, on the literary-vs-informational axis MAP/STAAR use — not the subject matter.”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/plan-evaluation.md inside it) (162-163): “this is still a **text-count**, not a word-count on sourced material — fiction runs longer, so a word-count balance will tilt further toward literary than the text-count shows.”
- `incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (351): “at ~22% literary vs ~40% target by picking texts on Lexile alone)”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (351): “at ~22% literary vs ~40% target by picking texts on Lexile alone”

Against: Another review notes that the 40% target was itself admitted as an assumption with an open source ask (`ti-courseplans-audit/docs/redteam-sources/g5-reading-redteam-round1-2026-07-06.md`).

<sub>criterion · stimulus, sequence, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Texts in which learners see themselves

Choose texts whose names, characters and cultures let learners see themselves, since culturally familiar material is read faster, recalled more accurately and understood with fewer errors.

The reading course plans' digest of a national reading report records that students reading culturally familiar material read it faster, recalled it more accurately and made fewer comprehension errors than with unfamiliar material, and draws the reverse risk for tests: assessments built on culturally narrow content disadvantage students unfamiliar with it. A teaching move in a Grade 3 reading red-team standard, drawn from a regional education laboratory video, makes identity-affirming selection a text-quality criterion, choosing texts whose content, names and characters can affirm the learner's identity, culture and language. The evidence is a cited report and a video, not a measurement in these courses.

Quoted:

- `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd` (63): “Students reading culturally familiar material read it faster, recalled it more accurately, and made fewer comprehension errors than when reading unfamiliar material.”
- `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd` (65): “when students read culturally familiar material, they read it faster, recalled it more accurately, and made fewer comprehension”
- `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd` (67): “assessments built on culturally narrow content will systematically disadvantage students unfamiliar with that content.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/read-graphics-and-identity-affirming-text.md` (7): “texts are chosen so their content, names, and characters can affirm the learner's identity, culture, and language”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/read-graphics-and-identity-affirming-text.md` (19): “children of color, when they go through school, the books that they read, they don't really see themselves in those books.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/read-graphics-and-identity-affirming-text.md` (21): “Books that reflect and respect their cultures, languages, and communities were of much better service to their language, literacy, and human development.”

Published: [RAND Reading Study Group 2002, Reading for Understanding (MR-1465)](https://www.rand.org/pubs/monograph_reports/MR1465.html) · [REL West video, Joyful reading at school and at home](https://www.youtube.com/watch?v=4mK9pQG7Pz8)

Against: The record no-local-knowledge-the-course-doesnt-teach keeps items solvable without local or cultural knowledge the course doesn't teach, in neutral settings; that limits what an item may require rather than which texts are chosen, but the digest's own note warns that content familiar to one group is unfamiliar to another.

<sub>criterion · stimulus, accessibility · universal · from g3, research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### True explanations that still mislead

A true explanation can still teach wrongly: check it for circular definitions, misleading analogies, contradictions, unconnected facts and wording that invites a misconception, allowing simplification normal for the level.

The video-script check separates factual accuracy from educational accuracy: a script can be factually correct and still fail if its explanation creates or reinforces misconceptions or its teaching arc fails to build understanding (`shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt`). It names the faults that pass a fact check: circular definitions, misleading analogies, internal contradictions, facts listed without the relationship between them, and explanations that make a common misconception more likely. Grade-appropriate simplification is expected and is not a factual error. A misleading analogy is one whose obvious features suggest something false.

Quoted:

- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (180): “A script can be factually correct and still fail educational accuracy if the explanation creates or reinforces misconceptions, or if the teaching arc fails to build understanding.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (187): “- **Circular definition:** uses the term being taught to define itself.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (188): “- **Misleading analogy:** an analogy that installs a wrong mental model.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (189): “- **Internal contradiction:** the script states X in one place and not-X elsewhere.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (190): “- **Missing teaching arc:** facts are listed without explaining the relationship between them. A student hears isolated facts but cannot reconstruct the mechanism or apply the KC.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (191): “- **Misconception scaffolding:** the explanation makes a common misconception more likely.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (174): “Grade-appropriate simplification is expected and not a factual error”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx` (257 (textutil text)): “Avoid the water pipe analogy without extreme care — it naturally suggests water (current) is consumed by components.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx` (250 (textutil text)): “But the SKIERS keep going around. The ski lift doesn't create new skiers.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx` (207 (textutil text)): “Use the analogy of magnets (carefully)”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-qc-evidence-v0.1.md` (220): “"a drop of water … cut down to an atom" (water's smallest piece is a molecule).”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-15.md` (161): “It states direction toward Earth's center and universality without the "no gravity in space" trap.”

Against: none found

<sub>criterion · wording, integrity · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Whole passages with their items together

Give a reading test whole, coherent passages rather than simplified summaries, and serve all the items on one passage together. One reading test's specification sets 2–4 items per passage, all given consecutively.

A reading assessment's passage requirements ask for authentic or authentic-style texts with no simplified summaries: a literary excerpt with a clear beginning, middle and end, or an informational text with an introduction, 2–3 body paragraphs and a conclusion (`grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md`). Each passage carries 2–4 items, and all of a passage's items are given one after another. These are requirements of a specification; nothing in it measures what fragmentary passages or scattered items do to scores.

Quoted:

- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md` (340): “- Authentic or authentic-style — no simplified summaries”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md` (343): “- Literary: coherent excerpt with clear beginning/middle/end”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md` (344): “- Informational: introduction + 2–3 body paragraphs + conclusion”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md` (346): “- Items per passage: 2–4 items; all passage items administered consecutively”

Against: none found

<sub>criterion · stimulus, sequence · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Words that carry the knowledge

Teach and gloss the words that carry what a reader needs to know, not the rarest ones, each for its sense in its own line.

The word in focus is chosen by the knowledge it carries, not by difficulty
(`g9/transformer/src/mechanics/word-in-focus.js`). A first word-web draft's key words were the passage's hard words,
and the judge held it; with the prompt sharpened, the next draft passed on its first try (`g9/transformer/v02/QA.md`,
"Word web"). Every gloss must fit its word as its own line uses it, since a wrong gloss misleads quietly
(`g9/transformer/src/mechanics/glossary.js`).

Quoted:

- `grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md` (44): “REVISE cannot swap payload words out”
- `grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md` (46): “FLAG -> SCAFFOLD: vocabulary_support pre-teach for "erosion" and "gorge" (pronunciation + meaning) before the reading dose”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md` (52): “Vocabulary ledger: target word, blocking words, disposition, audio/definition requirement.”
- `grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd` (59): “| F3 | major | "producer"/"habitat" are deep-taught as if they were blocking vocabulary (they aren't). |”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (352): “Apposition in the prose is **not** a gloss until it is verified to read as one.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md` (355): “the gloss has failed by demonstration; make it explicit.”
- `shadow-bench/src/inceptbench/prompts/video_script/evaluation.txt` (399): “**Pass:** Every technical term used in the script is either (a) defined within the script, or (b) something a typical G7 student would know from general K-6 schooling.”
- `icloud-work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md` (384): “By **mastering roughly 300–400 high-utility academic words per grade level**, students gain the linguistic precision needed for strong reading comprehension and confident written expression.”
- `icloud-work/k_12_social_studies/ap_files/Articles Tracker.xlsx` (sheet 'ReadabilityExperiment-dev-inter', cell L10): “Prefer the term, 'factor' over 'trend' because the exam will use the word 'factor' in questions”
- `grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/procedures/Example_Lesson_Components.txt` (9): “Exactly one high-leverage word is taught — chosen to unlock this text and to feed the Phase 3 inference.”
- `grade3-reading/artifacts/g5-course/VOCAB-DECISIONS-U9.md` (68): “all clear the counting rule and are still wrong to teach: a Grade-5 card is spent on a word”
- `ti-courseplans-audit/skills/course-red-team/references/finding-taxonomy.md` (210): “iter-3: 12 of 46 taught words never occur in their own passage, so they can't be met in context or tapped there”
- `grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd` (59): “"producer"/"habitat" are deep-taught as if they were blocking vocabulary (they aren't).”
- `downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx` (9 (textutil text)): “Exactly one high-leverage word is taught — chosen to unlock this text and to feed the Phase 3 inference.”
- `grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md` (136-137): “4. Only ~5–15 of 100 unfamiliar words met in natural reading are learned; misdirective contexts teach approximately zero (Beck et al. 2013, pp. 5–8).”
- `shadow-content-eval/reports/G3-U1-L12-review.md` (105): “`theft` and `charge` (legal sense) carry p14, p21 and p23 and aren't glossed. p14 `check` tests them.”
- `g9/transformer/src/mechanics/word-in-focus.js` (10): “const GAIN = ["almost none: an everyday word", "a little", "some: an older sense or an idiom", "a lot: a rank, a title or a historical idea", "essential: the scene cannot be understood without it"];”
- `g9/transformer/src/mechanics/word-in-focus.js` (17): “summary: "The word that carries the most knowledge, glossed for this line and asked about. Chosen by knowledge carried, not by difficulty.",”
- `g9/transformer/src/mechanics/word-in-focus.js` (67): “How much does knowing what "${c.word}" means in this passage (gloss: ${c.gloss}) help a Grade 9 reader understand it?”
- `g9/transformer/src/mechanics/glossary.js` (3): “Jev checks every note fits its word as the line uses it, each one required”
- `g9/transformer/src/mechanics/glossary.js` (125): “label: `The note fits "${e.term}" as its line uses it`, required: drafted,”
- `g9-transformer-runs/decisions/366b8d2c7104a608.json` (307-310): “"gloss_fits_9": { "id": "gloss_fits_9", "type": "noul", "value": 0.59,”
- `g9-transformer-runs/decisions/366b8d2c7104a608.json` (319-321): “"pass": false, "gate_reasons": [ "top<0.6"”
- `g9-transformer-runs/decisions/366b8d2c7104a608.json` (47): “"term_9": "owe",”
- `g9-transformer-runs/decisions/366b8d2c7104a608.json` (544): “"term_9": "peculiar end",”
- `g9/transformer/src/mechanics/glossary.js` (85-86): “Not words a Grade 9 reader already knows, and never a name.”
- `g9/transformer/src/mechanics/glossary.js` (130-131): “a drafted word Jev is sure a Grade 9 reader knows unaided is dropped, unless … that would leave nothing”
- `g9/transformer/src/mechanics/glossary.js` (136): “return kept.length && kept.length < item.entries.length ? { ...item, entries: kept } : item;”
- `g9-transformer-runs/blocks/839053e70062cbb5.json` (352-354): “"label": "A Grade 9 reader needs \"proposition\" explained", "required": false, "verdict": "fails",”
- `g9/transformer/src/mechanics/word-web.js` (41-43): “each clearly part of a web for the centre (a kind of it, a sign of it, a word for someone who shows it, or what it does to people), such as "betrayal" or "duplicity" for deceit. Not a hard word from the text that is only loosely linked.”
- `g9/transformer/v02/QA.md` (83-84): “The first draft's key words were hard words from the text ("obsequious", "homage", "peculiar") for "resentment", and Jev held it;”
- `g9-transformer-runs/blocks/9bce29e80207fd23.json` (90): “belongs in a web for the centre: the judge found this does not hold”
- `g9/transformer/src/mechanics/say-it-back.js` (55): “the words that carry the answer”
- `g9/transformer/src/mechanics/glossary.js` (3): “Jev checks every note fits its word as the line uses it, each one required, since a wrong gloss”
- `g9/transformer/src/glue/threejs-render.js` (432): “The word class of each word in focus as it is used in its line, for its 3D card: one Jev choice per word, and ""”
- `g9/transformer/v02/QA.md` (180): “"follow" glossed as loyal: the writer now gets a correction it can act on, below.”
- `g9/transformer/src/mechanics/video-essay.js` (128): “In frame_${k}, is what is said of "${a.word}" true of that word in the quotation?”
- `g9/transformer/v02/QA.md` (83-85): “The first draft's key words were hard words from the text ("obsequious", "homage", "peculiar") for "resentment", and Jev held it; with the prompt sharpened, the block was ready on the first try”
- `g9/transformer/src/mechanics/key-words.js` (49): “about it (a rank, an older sense, a word for what a character does or is), to study and then recall from memory.”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “optionally, judgeTerms with readingGrade 9 keeps only words a reader would not know unaided”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (233-236): “`content/vocab-word-lists.json` (the Alpha 2026 Vocabulary sheet) is a REFERENCE from a different curriculum, not this course's scope: prefer a word the sheet tests at this grade where choice is free, and never teach a word it places a grade or more below without a recorded `off_list_reason`”
- `grade3-reading/artifacts/u4l2-build/GRADE5-DECISION-LOG.md` (43): “`producer` and `habitat` receive the full blocking-word-style deep-teach cycle, though habitat is a K-3 science word and neither is the pinned blocking word.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-DECISION-LOG.md` (43): “RULE_G3_D4.2 (don't pick a word the child already knows), RULE_G3_D7.11 ("new" judged against a G5 reader)”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/vocabulary-selection-and-generative-items.md` (17): “there are six key word characteristics that should be considered when selecting target words for instruction … Centrality to understanding a text, frequency of use in a text, likelihood of appearing in other content areas, having multiple meanings, containing affixes, and having cross-language potential.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/vocabulary-selection-and-generative-items.md` (19): “some words that are important to understanding a text may not be bolded, but they may be good choices for target instructional words as well.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/vocabulary-selection-and-generative-items.md` (21): “sometimes those words, they're not conceptually central and they don't need to be taught. Or they may be words that your students already know. So you may just wanna review them rather than teach them in-depth.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/integration/check-before-final-content.txt` (330): “Domain-specific theatre/literary meaning is required here. Earlier vocabulary placement does not establish prior teaching in this new unit.”
- `g9/sources/Act 1 reading texts/Act 1/1. 1.1 - Iago_s Introduction - Text.docx` (176): “"in truth", said sarcastically here”

Against: whether a reader needs a word is only an advisory check (the
same file).

<sub>criterion · wording, alignment · universal · from g9 · adopted-rule · held · found in [2026-10-12-2-round-1](../research/2026-10-12-2-round-1/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Words, not line numbers

Point at a text by its words, never its line numbers: editions number lines differently, and a lesson may show none. Three of six early blocks of mine cited them.

Every block gets a house check that no student text cites a line number
(`g9/transformer/src/mechanics/util.js`, `houseChecks`). The sample text is numbered as in one edition and notes that
other editions number some lines differently (`g9/transformer/samples/othello-1-1.md`); a planning note cited a line by
one edition's number, which another edition gives two lower (`grade3-reading/artifacts/g9-prep-pack-2026-10-02/INDEX.md`).
Three of six blocks made before the rule cited line numbers, and the engine now refuses to draw blocks made under older
rules (`g9/transformer/v02/QA.md`, "Video essay and the unit-video modules").

Quoted:

- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/VISUAL-QA-2026-09-11.md` (34): “so the candidate `"So these are Peter Pan's precious friends," he said.` also lit the `he said.` fragment of the unrelated `"Hook," he said.` a whole part earlier”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/VISUAL-QA-2026-09-11.md` (34): “marks are bound to the sentences where the WHOLE clue occurs”
- `grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd` (38-39): “Open Source Shakespeare numbers it 43, and Gutenberg and MIT have no numbers.”
- `grade3-reading/knowledge_bot/knowledge/kb-0191-g3-book-lesson-anatomy.qmd` (150-152): “The step id is the page's own authored id, never its position (a position rots the moment the lesson's shape changes; five probes pinned to `?page=<n>` broke the day L1 grew an opening video).”
- `shadow-content-eval/reports/G3-U1-L12-review.md` (46): “The last word of that sentence is "magistrate", not "fined".”
- `shadow-content-eval/reports/G3-U1-L12-review.md` (49): “**Fix:** *"Look at the word just before 'by the magistrate'."*”
- `g9/transformer/src/mechanics/util.js` (46): “const LINE_NUMBER = /\b(?:L\d+|lines?\s+\d+)/i;”
- `g9-transformer-runs/lessons/20261009-085057-why-does-iago-say-he-follows-oth.json` (806): “Review lines 34 to 36, where Iago explains that traditional promotion by”
- `g9/transformer/test/laws.test.mjs` (2): “They are heuristics: they catch the plain ways of breaking a rule, not every way.”
- `g9/transformer/v01/QA.md` (41-42): “and "L42" written in a student paragraph. The house prompt now forbids L numbers in student-facing text”
- `g9/transformer/src/question.js` (12): “!/\b(?:L\d+|lines?\s+\d+)/i.test(q)”
- `g9-transformer-runs/blocks/d872bc1dfbda65fb.json` (35): “"nudge": "Look at the fifth line for details about the mouth.",”
- `g9-transformer-runs/blocks/d872bc1dfbda65fb.json` (36): “"second_nudge": "Examine the start of line five to see how the lip is described.",”
- `g9-transformer-runs/blocks/d872bc1dfbda65fb.json` (96-98): “"id": "no-line-numbers", "label": "No student text cites a line number", "ok": true,”
- `g9/transformer/src/mechanics/util.js` (8): “Text a student reads never cites a line number (no "L12",”
- `g9-transformer-runs/blocks/a75bd9643fa602d9.json` (38): “Re-read the sixth line to see what spiritual quality the speaker says cannot be bestowed by speeches alone.”
- `g9-transformer-runs/blocks/5722a3741161394e.json` (57): “Re-read the tenth line to consider the permanent claim of power in the title.”
- `g9/transformer/src/mechanics/util.js` (8-9): “Text a student reads never cites a line number (no "L12", no "line 12"): the lesson may show the text without numbers, so quote a few of the words instead.”
- `g9/transformer/v02/QA.md` (64): “student text cited line numbers the build's reading does not show ("in line 8")”
- `g9/transformer/v02/QA.md` (64): “student text cited line numbers the build's reading does not show ("in line 8");”
- `g9/transformer/test/calibration/evidence-hunt.tapped-proves.json` (5): “Lines are named by their words, never by number.”
- `g9-transformer-runs/playtest/2026-10-09T12-25-25-328Z.json` (248): “Review lines 7 and 8 to see who was recommending Iago for this permanent post.”
- `g9/transformer/src/mechanics/glossary.js` (16): “/** The words of `term` as they are written in `text` (case, curly apostrophes, spacing), or null. */”
- `g9/transformer/src/text.js` (2): “or a sentence (prose). Stage directions are kept for display but are never evidence.”
- `g9/transformer/src/quality/calibrate.js` (41): “a play-time case names a line by its words”
- `g9-transformer-audit/2026-10-09-best-of-everything.json` (1): “The animated glossary matches by text within a line, so a repeated word needs the right line index.”
- `grade3-reading/ui-audit-2026-09-08/round-5/final-standard-verification/generated-feedback-locator-99/CAUSE-AND-PROPOSAL.md` (7): “H1's third actual miss says to look at “the very first line of the story” for Peter's offer. The displayed story begins “The Darling children could not sleep”; the offer is later.”
- `grade3-reading/ui-audit-2026-09-08/round-5/final-standard-verification/generated-feedback-locator-99/CAUSE-AND-PROPOSAL.md` (7): “The second reply similarly generated a first-page direction.”
- `grade3-reading/ui-audit-2026-09-08/round-5/final-standard-verification/generated-feedback-locator-99/CAUSE-AND-PROPOSAL.md` (9): “It does not supply the full ordered story or page/line coordinates.”
- `grade3-reading/ui-audit-2026-09-08/round-5/final-standard-verification/generated-feedback-locator-99/CAUSE-AND-PROPOSAL.md` (9): “The excerpt order is a plausible contributing ambiguity, not proof of model-internal reasoning.”
- `grade3-reading/ui-audit-2026-09-08/round-5/final-standard-verification/generated-feedback-locator-99/CAUSE-AND-PROPOSAL.md` (15): “the supplied items are selected supporting excerpts, not an ordered story or page/line map.”
- `grade3-reading/ui-audit-2026-09-08/round-5/final-standard-verification/generated-feedback-locator-99/CAUSE-AND-PROPOSAL.md` (15): “Point to actual supplied words or an identified event instead.”
- `grade3-reading/ui-audit-2026-09-08/round-5/final-standard-verification/generated-feedback-locator-99/CAUSE-AND-PROPOSAL.md` (22): “Blanket first/last replacement was rejected because chronology and grounded quotations can legitimately use those words.”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (136): “Act.Scene.Line, as printed on folger.edu (for example 1.3.208–209).”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (136): “Earlier drafts used Folger through-line numbers (FTLN), which only match in 1.1.”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (143): “FTLN references in 1.2 and 1.3 were converted to Act.Scene.Line, which is what students see on folger.edu.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (354): “"1.1.171–174 · Iago" teaches the citation convention and names who is speaking.”
- `othello-archive/sources/act1/KB - Overview.csv` (143): “FTLN references in 1.2 and 1.3 were converted to Act.Scene.Line, which is what students see on folger.edu.”
- `othello-course-renderer-draft/repo/docs/pedagogy/modelling-moment-procedures.md` (842): “recalled as CONTENT - what happened, what the character was like - never as a position like 'in the middle'”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (170): “Quote references and line numbering may depend on the chosen edition.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (170): “Verify line references against the edition actually being used rather than assuming that a familiar number is universal.”
- `grade3-reading/.claude/skills/one-perfect-lesson/SKILL.md` (49-50): “Locate Routine v2 (evidence as content never position, 60–120-word zoom, pause narration until re-read)”

Against: A later run found: the house check's pattern matches only forms like L12 or line 12, so a held open-check draft whose hints said "the fifth line" and "line five" passed it; that draft was held for another reason, so the hints did not ship (`g9-transformer-runs/blocks/d872bc1dfbda65fb.json`). A later run found counter-evidence (`g9-transformer-audit/2026-10-09-best-of-everything.json`). A later run found: A Grade 9 unit's knowledge base gives line references in act, scene and line as printed where students read the play, after converting through-line numbers that matched only in the first scene, and the first-pass prototype review kept a line citation with its speaker because it teaches the citation convention. The conversion also bears out this record's reason that numbering systems differ (`g9/sources/1. Act 1 - Knowledge Base - Overview.csv`). A later run found counter-evidence (`g9/sources/Othello_1_Feedback_DevFactory.md`). A later run found counter-evidence (`g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip`).

<sub>criterion · wording, stimulus · universal · from g9, g3 · adopted-rule · held · found in [2026-10-12-1-seed](../research/2026-10-12-1-seed/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Write a hard passage closer to speech

To ease a hard passage written for learners, write it closer to how people talk, packing fewer idea units into each clause.

The RAND Reading Study Group's 2002 report, in a reading course's digest of it, says it can simplify comprehension challenges if writers write the way they talk (p. 96), and the digest gives the reason: printed text packs more idea units into each clause than speech (`grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd`, lines 351-353). The claim before it names the sentences that cause trouble: embedded, dense, ambiguous or ungrammatical ones. The digest offers it as a drafting heuristic for reducing syntactic load without stripping content knowledge.

Quoted:

- `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd` (353): “Thus, it can simplify comprehension challenges if writers write the way they talk.”
- `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd` (351): “Because printed text packs more idea units per clause than spoken language, comprehension can be eased by writing passages closer to how people actually talk.”
- `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd` (347): “This occurs when a sentence is embedded, dense, ambiguous, or ungrammatical.”
- `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd` (355): “Gives passage authors a concrete drafting heuristic for reducing syntactic load in G3/G5 texts without stripping content knowledge.”

Published: [RAND Reading Study Group 2002, Reading for Understanding (MR-1465)](https://www.rand.org/pubs/monograph_reports/MR1465.html)

Against: none found

<sub>criterion · stimulus, wording · universal · from research · external-research · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Above-level text when read aloud

A text read aloud in full may sit above the learners' reading level, up to what they understand by listening, so decoding doesn't cap what they learn. One review let a 35-word sentence stand above the Grade 3 band, recording a note instead of a failure, because every passage was fully voiced.

A Grade 3 review criterion lets read-aloud and think-aloud texts sit above the decoding band at listening-comprehension level, so that knowledge-building is not capped by decoding, and names the IES guide on improving reading comprehension in kindergarten to grade 3 as its source. A simulated review applied it to a 35-word sentence in a story passage and recorded a note rather than a failure, because all passages carried full voiceovers.

Quoted:

- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-C-D7-D8-D10-D12.md` (31): “D8.20 permits above-band text at listening-comprehension level; all passages carry full voiceovers.”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-C-D7-D8-D10-D12.md` (31): “G3 readability band | NOTE | Chunk-4 contains a 35-word sentence”
- `grade3-reading/artifacts/edullm-standards-centralization-2026-08-05/runs/G3-CURRENT-CRITERIA.csv` (207): “Read-aloud / think-aloud texts may sit above the G3 decoding band at listening-comprehension level, so knowledge-building is not capped by decoding”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (172-173): “Audio = pronunciation/gloss that fades; the transfer target is cold plain text.”
- `incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (172-173): “Audio = pronunciation/gloss that fades; the transfer target is cold plain text.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-16.md` (44): “D8.20 explicitly permits above-band text at listening-comprehension level when read-aloud is supported”

Against: A blocking row of the course's quality checklist requires "Every passage slice inside the teaching band" (`grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md`, line 64) and names no exception for text that is read aloud. A later run found counter-evidence (`grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md`). A later run found counter-evidence (`incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md`).

<sub>criterion · stimulus, accessibility · universal · from g3 · adopted-rule · contested · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Cite each play extract by speaker and line

Show each extract from a play with its speaker and its line reference, in the numbering of the edition learners see, converting any other numbering first. One cited line is 1.3.208–209 in the act, scene and line numbering students see, but 537–538 in through-line numbers.

A Grade 9 unit's knowledge base gives line references in act, scene and line as printed on the website edition students read, and sets speaker labels in capitals and bold in its reading texts (`g9/sources/1. Act 1 - Knowledge Base - Overview.csv`, lines 135-136). Its quality pass found earlier drafts using the edition's through-line numbers, which match only in the first scene, and converted every later reference, recording the offsets (lines 136 and 143). The first-pass review of the lesson prototype singled out a line citation with its speaker as work to keep, because it teaches the citation convention and names who is speaking, which matters in drama (`g9/sources/Othello_1_Feedback_DevFactory.md`, lines 288 and 354).

Quoted:

- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (136): “Act.Scene.Line, as printed on folger.edu (for example 1.3.208–209).”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (136): “Earlier drafts used Folger through-line numbers (FTLN), which only match in 1.1.”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (136): “All 1.2 and 1.3 references have been converted: 1.2 = FTLN − 206; 1.3 = FTLN − 329.”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (143): “FTLN references in 1.2 and 1.3 were converted to Act.Scene.Line, which is what students see on folger.edu.”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (143): “is 1.3.208–209, not 537–538. Fixed.”
- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (135): “Speaker labels in capitals and bold.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (354): “"1.1.171–174 · Iago" teaches the citation convention and names who is speaking.”
- `g9/sources/Othello_1_Feedback_DevFactory.md` (288): “teaches the citation convention and names who is speaking, which matters in drama.”

Against: Another record holds the opposite for any text: point at a text by its words, never its line numbers, since editions number lines differently and a lesson may show none.

<sub>criterion · stimulus, wording · domain · from g9 · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Keep the text apart from the inference

Keep what the text says apart from what the student infers: an inference never fills the slot for the text's words and never sits inside quotation marks.

The reading course's criteria register keeps inferred mood words in the 'I know' step of its reasoning frame, never inside 'The text says' (`grade3-reading/artifacts/criteria-register.csv`, line 72). Two external audits of its lessons found modelled inferences wrapped in quotation marks as if they were the text's words, against the lessons' own rule that quote marks mean the text's exact words (`grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md`, line 14; `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md`, line 113).

Quoted:

- `grade3-reading/artifacts/criteria-register.csv` (72): “Inferred mood words (gloomy, enchanting, etc.) live only in the 'I know' step, never inside 'The text says'”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md` (14): “quote marks around words the writer never wrote”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (113): “puts quotation marks around the model's own inferential words”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (1175): “Saved original46/47 show tomorrow night / thy father’s house running directly into their explanation.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (1175): “BookClassicModel.renderBeat joins every narration line with inline spaces.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (3437): “What the clues show runs directly into the explanation in one paragraph.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (1187): “frozen original48pass/15fail→63pass/0fail with original47 cases identical and all28 quote excerpts across14 models.”
- `othello-course-renderer-draft/repo/authoring/inputs/prompt-packs/reading-g3/procedures/infer.md` (16-18): “The inference itself NEVER sits inside the "the text says" part — the quote is evidence, the "So I think" part is the built meaning, and collapsing them models circular reasoning.”
- `othello-course-renderer-draft/repo/authoring/inputs/prompt-packs/reading-g3/procedures/infer.md` (19-21): “The "I know that" move supplies WORLD knowledge (what anyone knows about being trapped, being tired, wanting to be safe), never a second quote and never a fact the text already states.”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md` (278): “NOT applied: M3 (quote marks around the model's inference) — `validate-contracts` requires them; contradiction row 10 recorded.”
- `grade3-reading/artifacts/qc-2026-09-30-staging/contradictions.md` (21): “REQUIRES the pulled-out line wrapped whole in curly quotes "so the child reads it as the writer's message"; the InceptBench quick-check of L1 (29.09, M3) calls the same quote marks a defect because the lesson teaches that quote marks mean the text's exact words”
- `othello-course-renderer-draft/repo/docs/rules/contradictions.md` (21): “`validate-contracts` (checkStagedModel, since the L1 FIND rebuild) REQUIRES the pulled-out line wrapped whole in curly quotes "so the child reads it as the writer's message"”
- `grade3-reading/artifacts/pp2-v3-design.txt` (205): “(Text-says holds only verbatim quotes; every trait word sits in the "I know" / "So" part, never in "The text says.")”

Against: A contract in the same engine requires the modelled inference in a reveal beat to be wrapped whole in curly quotes; the clash was recorded as a contradiction awaiting a ruling, and the lessons kept the quote marks as the contract demands (`grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md`, line 57). A later run found counter-evidence (`grade3-reading/artifacts/qc-2026-09-30-staging/contradictions.md`). A later run found counter-evidence (`othello-course-renderer-draft/repo/docs/rules/contradictions.md`).

<sub>criterion · integrity, stimulus · universal · from g3 · adopted-rule · contested · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Pre-teach only the words that block reading

Pre-teach only words without which comprehension breaks down; support the rest in place, replace them or teach them after reading, and never introduce a word by asking what it means. In one audited grade-5 lesson, one pinned blocking word was pre-taught, and two other words given the same full cycle were ruled a violation.

A reading quality canon applied in a grade-5 audit pre-teaches only the words needed to prevent comprehension breakdown and teaches the rest after reading, and its word-audit rule assigns every likely blocker to pre-teaching, inline support, replacement or review, with meanings that are not circular. In the audited lesson the pinned blocking word was pre-taught before the first read with pronunciation support and a say-back, which conformed, while two other words, one of them a K-3 science word, got the same full cycle and were ruled a violation.

Quoted:

- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (300): “Only the words needed to prevent comprehension breakdown are pre-taught; the rest are taught after reading.”
- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (381): “A word audit assigns every likely blocker to preteach, inline support, replacement, or review; meanings are non-circular; pronunciation and active use work in the rendered context.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-DECISION-LOG.md` (41): “`decomposer` pre-taught before first read with syllable pronunciation support and say-back.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-DECISION-LOG.md` (41): “**conforms**”
- `grade3-reading/artifacts/u4l2-build/GRADE5-DECISION-LOG.md` (43): “`producer` and `habitat` receive the full blocking-word-style deep-teach cycle, though habitat is a K-3 science word and neither is the pinned blocking word.”
- `grade3-reading/artifacts/u4l2-build/GRADE5-DECISION-LOG.md` (43): “CONFIRMED VIOLATION → F3”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D4-vocabulary.md` (3): “*Bringing Words to Life* (round 2)”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D4-vocabulary.md` (21): “Only the words needed to prevent comprehension breakdown are pre-taught; the rest are taught after reading”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D4-vocabulary.md` (22): “An unfamiliar word is never introduced with a guess-opener ("who can tell me what X means?")”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D4-vocabulary.md` (34): “Distinguish light in-text glossing ('pause and punch', keep reading) from the few words taught to production after the read — not uniform deep treatment for every taught word”

Against: The record teach-a-word-before-using-it holds that no word students may not know is used before the lesson teaches it, and a curriculum thread map it cites wants each unit's technical terms taught before reading, so the two disagree on words students first meet in the passage. The open record words-taught-before-reading holds a rule for opening films that calls the film the best place to teach a word, which would teach words before the reading whether or not they block understanding.

<sub>criterion · wording, sequence, accessibility · universal · from g3 · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A failed source fails what depends on it

When a text or specification fails a check, carry the failure to every lesson, item, chart and piece of feedback built on it.

The reading project's review packet for science, social-studies and passage integrity ends its work order by propagating any upstream failure through every declared dependent lesson, item, chart and feedback object (`grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md`). It also requires a list of stale dependents after every failed upstream specification (the same file).

Quoted:

- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md` (34-35): “6. Propagate any upstream failure through every declared dependent lesson, item, chart, and feedback object.”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md` (45): “A stale-dependency list after every failed upstream specification.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/integration/validate-passage-refs.txt` (11): “A node is quoting passage text that no longer exists. Rewriting a passage means updating everything that points at it.”
- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE3.md` (89): “Replacing readings alone would invalidate many current exact-evidence questions, vocabulary bindings, models and narration.”
- `grade3-reading/artifacts/qc-2026-09-30-staging/SPEC-find-infer-procedures.md` (167): “The text says that London is "cold and dark," and the children "could not sleep" at bedtime because they are bored”
- `grade3-reading/.claude/skills/tts-clips/SKILL.md` (166-167): “being cached by sha1(VOICE|STYLE|text), it shipped identically into every node that speaks that sentence”
- `grade3-reading/.claude/skills/art-qa/SKILL.md` (102-103): “For video, a check-8 FAIL on a still is a blocker on the film until a re-render clears it.”

Against: none found

<sub>method · stage: review · stimulus, review · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Audit a source pool's coverage

Before generating from a source pool or declaring a topic short of material, audit what the pool really holds for each curriculum topic, counting only after normalising its labels. One collection of oral histories made up 46 rows, 37%, of one unit's topic cluster.

Topic scans of an AP history source corpus found required topics such as slavery and labour or Jamestown with one row each, four others with none, and 37% of one unit's cluster drawn from a single collection of oral histories with an elite foreign-policy skew. A later ingest added 648 documents for the units that had been missing or sparse, bringing the corpus to 1,385 documents and 5.8M characters. The audit covers the voices the pool draws on as well as its topics.

Quoted:

- `icloud-work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md` (38): “Slavery/labor = 1 row, Jamestown = 1 row (critical under-rep).”
- `icloud-work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md` (39): “Sectionalism/slave-revolts/2nd Awakening/transcendentalism = 0 each.”
- `icloud-work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md` (41): “ADST oral histories = 46 rows / 37% (elite foreign-policy skew confirmed).”
- `icloud-work/aptraining/helpers/data/output/d13_corpus_v5_inventory.md` (8): “v3 ingest added **648 new docs** across Units 1/2/4/6/9 (the units missing or sparse in v2), bringing the combined v2+v3 corpus to **1,385 docs / 5.8M chars**.”
- `ap-helpers-data-agent-memory/feedback_audit_normalization_before_declaring_gap_2026_05_22.md` (7): “When an inventory scanner reports a unit/era below threshold, audit the normalization layer before doing more gathering.”
- `ap-helpers-data-agent-memory/feedback_audit_normalization_before_declaring_gap_2026_05_22.md` (9): “Adding an `ERA_LABEL_TO_UNIT` dict moved Unit 7 from gap-status to +361k margin and Unit 8 from gap to +482k margin — without ingesting a single new token.”
- `ap-helpers-data-agent-memory/feedback_verify_subset_exists_before_filter.md` (12): “The implied assumption: fewshot_bank's 3,806 rows contain a U1 slice. **It does not.** Unit distribution audit:”
- `ap-helpers-data-agent-memory/feedback_verify_subset_exists_before_filter.md` (23): “Had I scripted on the assumption, the consolidator would have silently produced ~468 rows (Track B only) but reported the manifest as if it included fewshot_bank”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/TOPIC-SELECTION.md inside it) (168-169): “"Belonging (5/7)" as a single topic — an **invented grouping** merging 5 unlike SEL units under one”
- `incept-package-hub/.artifacts/source/g6-reading-approval-package.zip` (g6-reading-approval-package/markdown/topic-selection.md inside it) (294-295): “so the real frequency ceiling is **6/7**, not 7/7; don't treat /7 denominators as if all 7 could score.”

Against: Coverage counts can mislead: one keyword cluster had 21 of 34 false positives (icloud-work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md, line 128), and one inventory's per-unit totals were not deduplicated (icloud-work/aptraining/helpers/data/output/v93_data_inventory.md, line 24). None found. The normalization note is inconsistent about which units were short: it names 8 and 9, then reports the fix for 7 and 8 (line 9).

<sub>method · stage: ground · stimulus, alignment · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Bind each mark to its place

Bind each marked word in a quotation to its exact position, and refuse a mark named only by a word that recurs there rather than guess which one.

The quotation-card frame module marks a span by its code-point offsets together with the exact text expected there, so either occurrence of a repeated word can be targeted, and editing the quotation without rebinding the mark fails validation (`g9-unit-video-packages/quote-card/README.md`). Its notes say the older pilot highlighted the first matching substring, and that a migration should reject ambiguous repeated words instead of guessing an occurrence. The lesson engine's own binder still takes the first whole-word match, ignoring case (`g9/transformer/src/video/frames.js`); no stored block marks a word that occurs twice in its quotation, so no wrong highlight has been seen.

Quoted:

- `g9-unit-video-packages/quote-card/README.md` (31): “`expectedText` must exactly match the selected range; editing the quote without rebinding the mark fails validation.”
- `g9-unit-video-packages/quote-card/README.md` (31): “This makes either occurrence of a repeated word independently targetable.”
- `g9-unit-video-packages/quote-card/README.md` (37): “The older Python pilot names this block `quote_card` and highlights the first matching substring.”
- `g9-unit-video-packages/quote-card/README.md` (37): “It should reject ambiguous repeated words instead of guessing an occurrence.”
- `g9/transformer/src/video/frames.js` (37): “/** Unicode code-point offsets of a word in a quotation, as the quote card wants them; null if it is not there whole. */”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (2389): “native Enter on earlier quoted Captain Hook banks later Captain Hook was watching.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (2389): “Proposal: pure ordered paragraph/sentence occurrence mapping”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (2400): “Native wrong occurrence denied, actual clues/best gate and L7 opening retained.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (382): “Current sentence replay resolves text only. Actual G3L7p8 has two Tap. marks and p9 three Tick. marks; string-first lookup rewinds all identical targets to the first occurrence.”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (382): “bind repeated printed occurrences to their actual mark indices”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.json` (394): “verifies twoTap/threeTick distinct boundaries and single highlights”
- `grade3-reading/ui-audit-2026-09-08/BEAD-REGISTER.md` (56): “| reading-9ur.49 | closed | Prevent clue credit and found marks on unrelated repeated name fragments |”
- `grade3-reading/ui-audit-2026-09-08/round-5/gold-standard/clue-location/CLUE-LOCATION-PROPOSAL.md` (7): “banks **“Captain Hook was watching”** as one of the two clues, without activating the actual occurrence later in the passage.”
- `grade3-reading/ui-audit-2026-09-08/round-5/gold-standard/clue-location/CLUE-LOCATION-PROPOSAL.md` (9): “`partOfLine` accepts the normalized12-character name by containment.”
- `grade3-reading/ui-audit-2026-09-08/round-5/gold-standard/clue-location/CLUE-LOCATION-PROPOSAL.md` (19): “Use ordered sentence positions, not bare containment or a claim that the clue appears somewhere in that paragraph.”
- `grade3-reading/course-renderer/docs/ui-audit/2026-09-08/README.md` (53): “Global short-fragment matching could bind an earlier name/whisper to a later authored clue. Two exact PP owners now bind whole clue occurrences to their printed source positions.”
- `grade3-reading/course-renderer/docs/ui-audit/2026-09-09/README.md` (22): “Split quote heads/tails did not individually match their measured sentence; repeated “Tap.”/“Tick.” used the first matching text and could wash the wrong occurrence.”
- `grade3-reading/course-renderer/authoring/peter-pan/fill/l5-l7-parity/batch-2026-09-18/DECISIONS.md` (133-134): “straddles two printed units (core.tsx unitsOf only re-joins a cut at a mid-sentence closing quote), so it never glows.”
- `grade3-reading/course-renderer/authoring/peter-pan/fill/l5-l7-parity/batch-2026-09-18/DECISIONS.md` (136): “every hot_text span must resolve to exactly one printed unit (the census script lives in this record; validate-passage-refs only proves substrings).”
- `othello-course-renderer-draft/repo/docs/ui-audit/2026-09-08/README.md` (53): “A short repeated phrase grants or spends the wrong clue evidence”
- `othello-course-renderer-draft/repo/docs/ui-audit/2026-09-08/README.md` (53): “Global short-fragment matching could bind an earlier name/whisper to a later authored clue.”
- `othello-course-renderer-draft/repo/docs/ui-audit/2026-09-08/README.md` (53): “Two exact PP owners now bind whole clue occurrences to their printed source positions.”

Against: The lesson engine's binder marks a repeated word at its first occurrence without a warning: "const m = re.exec(q);" (g9/transformer/src/video/frames.js line 42).

<sub>method · stage: settle · stimulus, media, integrity · universal · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Bind each question to its text

Bind each question to the exact text it was written and checked against, and confirm that pairing on the delivered form as a blocking check of its own. In one delivered quiz all 25 questions asked about a different text from the one it showed, and all 25 passed all seven checks.

When no example question matched the chosen passage's type, an AP Literature quiz generator silently regenerated its questions against a different passage, while the explanation step and the saved quiz kept the first one. In the saved hard-level quiz the passage is a play, all 25 stems ask about a road-building satire, and all 25 pass all seven checks in their final verdicts. Of 74 double-quoted strings in those verdicts, the only ones found in the saved passage are the bare word 'to', against 35 of 51 and 26 of 49 in the two quizzes without a swap, and the converted delivery file names the play as the source of all 25 items. A text swapped mid-run can ship questions about a text the learner never sees.

Quoted:

- `icloud-work/incept/aplit-quiz-generation/main.py` (1494): “return await self.generate_questions(different_passage, question_distribution, recursion_depth + 1)”
- `icloud-work/incept/aplit-quiz-generation/main.py` (513): “explanations = await self.generate_explanations_for_quiz(passed_questions, passage)”
- `icloud-work/incept/aplit-quiz-generation/quiz_an_artful_arrangement_of_incidents_diff3_2025-10-20_12-21-58.json` (53): “while paragraph 7 heightens this into buffoonish spectacle (dropping scissors, sycophants tussling, fingers stuck)”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (215-216): “4 of 5 items are unanswerable as rendered”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (217): “the exact class meeting #10 calls "passes item evaluations but fails the holistic course”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (224): “**rock-bottom outlier at ratio 0.091** vs a normal real-assessment-passage floor of ~0.47”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (230): “aggregate first returned a false all-clear”
- `grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md` (265-266): “never assume an IB pass means the passage and the question are about the same thing”
- `grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd` (38-39): “whose water-cycle items were bound to an unrelated pistol-shrimp passage, plus an EBSR Part-B quoting a passage that was never persisted”
- `grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd` (39-40): “the class of defect that "passes item evals but fails the holistic course eval."”
- `grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd` (41-42): “each independently re-verified by a fresh read-only GET”
- `grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd` (25-26): “hands each child question the parent passage as `full_context`”
- `grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd` (26): “so topic mismatches are visible to the judge”
- `g9/transformer/web/app.js` (38): “A short fingerprint of the source. A block is good only for the text and question it was made from.”
- `g9/transformer/test/server.test.mjs` (112): “made for another question: not played”
- `g9/transformer/src/films.js` (55): “/** The film whose narration shares most words with the text and the question; null if there is none. */”
- `g9-transformer-runs/blocks/d2d7d0787d6754d9.json` (97): “The film belongs with this text: the judge found this does not hold”
- `g9-transformer-runs/blocks/d2d7d0787d6754d9.json` (167): “"p": 0.01,”
- `g9-transformer-runs/decisions/0419fc2dc6f6bacf.json` (184-187): “"value": 0.02,”
- `g9-transformer-runs/decisions/0419fc2dc6f6bacf.json` (60, 667, 1274): “"instructions": "Is film_narration about the same work as passage, so that it can open a lesson on it?"”
- `g9-transformer-runs/decisions/0419fc2dc6f6bacf.json` (187, 794, 1401): “"value": 0.02,”
- `g9-transformer-runs/decisions/0419fc2dc6f6bacf.json` (23): “"question_0": "When was the play written?",”
- `g9/transcript/chat-transcript.redacted.txt` (1507): “One detail is flagged for your review: the script still refers to reading text v2.”

Against: The item-quality judge did catch this blatant mismatch, scoring the rendered form inferior on 9 of 9 draws; the report credits the defect's blatancy rather than the judge's design and expects subtler topic drift to slip through (`grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md`, lines 247-256). the item evaluator studied in the same record hands each question of a decomposed reading resource its parent passage, so a topic mismatch is visible to its judge (`grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd`, lines 24-26).

<sub>method · stage: settle · stimulus, alignment, integrity · universal · from ap, g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Bracket a summary where lines are cut

Abridge by cutting sections, keep the author's words for what stays, bridge each cut with a bracketed summary, and say the text is abridged and from which edition. A planning meeting put the full opening scene at 15 minutes of reading.

A Grade 9 unit plans one reading text per lesson, abridged from a named edition, with bracketed stage directions summarising the cut lines, and each reading text carries a line naming the edition it is abridged from and its licence. A planning meeting gave the reason: reading the full opening scene takes the full 15 minutes.

Quoted:

- `g9/sources/1. Act 1 - Knowledge Base - Overview.csv` (132): “One reading doc per lesson, abridged from the Folger text, with stage directions in square brackets for the cut lines”
- `g9/sources/Act 1 reading texts/Act 1/1. 1.1 - Iago_s Introduction - Text.docx` (5): “Text: abridged from the Folger Shakespeare edition (CC BY-NC 3.0).”
- `g9/sources/meeting-notes/ELA - CNU + Academics - 2026_10_01 20_30 IST - Notes by Gemini.md` (224): “it takes the full 15 minutes to read the full act one, scene one.”
- `g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/MEETING-2026-10-01.md` (53-54): “the full scene takes 15 minutes to read, so sections are cut and the Archivist bridges them.”
- `g9/library/collections/codex-2026-10-02-curriculum-research/Othello-1.1-Student-Reading-Text-v6.txt` (3): “The Archivist narrates between sections of the text: feeding forward before a section, reviewing back after it, and summarizing at the end.”
- `g9/library/collections/codex-2026-10-02-curriculum-research/Othello-1.1-Student-Reading-Text-v6.txt` (4): “Text: abridged; Folger edition.”

Against: A classroom guide in the sources has learners do the cutting themselves, as close reading, and holds that "Students need and deserve the chance to tackle the real thing." (`g9/sources/Cutting-a-Scene-Othello-1.1.pdf`, pdftotext line 36). How far segments are abridged was left open in the planning meeting (`g9/library/collections/g3-repo-initiative-g9-othello-2026-10-01/MEETING-2026-10-01.md`, lines 49-50), and the draft abridgement still needed "edition attribution and non-commercial terms" confirmed (`g9/library/text/L7f7ca8.txt`, line 1).

<sub>method · stage: write · stimulus, integrity · domain · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Build tested texts from particulars

When questions test a text, build it from particulars that only it supplies and no student of the topic could already know, with every claim about the world still true. Multiple-choice questions on passages that restated well-documented curriculum facts were answered without the passage 99.5% of the time.

Blind-solving a generated reading bank found multiple-choice questions leaking at 99.5% and traced it to passages that described well-documented curriculum facts, so asking what a passage says about something asked what any educated reader already knew from school (`grade3-reading/artifacts/LANE2_GENERATOR.md`). The fix it set was passages about specific events, character decisions, arguments or surprising claims that cannot be known without reading that passage. A later generation run still saw multiple-choice items leak through ordinary school knowledge (`grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md`). Such particulars include a specific event, decision, stance, reversal or causal chain, or invented people, places and quantities. When questions leak, change the text rather than the questions or distractors, because a text that restates widely known facts can be answered from general knowledge.

Quoted:

- `grade3-reading/artifacts/LANE2_GENERATOR.md` (15): “| MCQ | 200 | **99.5%** | 7 of 1,473 |”
- `grade3-reading/artifacts/LANE2_GENERATOR.md` (21): “**Root cause: passages describe well-documented curriculum facts.**”
- `grade3-reading/artifacts/LANE2_GENERATOR.md` (29): “The generator asks "what does the passage say about X?" — but X is something any educated reader already knows from school.”
- `grade3-reading/artifacts/LANE2_GENERATOR.md` (33): “passages must describe specific events, character decisions, author arguments, or surprising/counterintuitive claims that are genuinely unknowable without reading this specific passage.”
- `grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md` (269): “MCQ leaked through ordinary school knowledge”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (43): “by design ensures assessment passages never overlap taught topics”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (45): “reserve cold, non-overlapping passages for the test only, where that property belongs.”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/PASSAGE_DESIGN_RULES.md` (5): “The fix is not to write harder distractors; it is to write passages that carry information the student cannot have encountered before opening this specific text.”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/PASSAGE_DESIGN_RULES.md` (11): “If the answer is YES for any item, the passage is leaking. Do not patch the item — fix the passage first.”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md` (45-46): “invented entities/quantities/relations, story-specific event order rather than canonical process order, passage-defined categories rather than natural-kind categories”
- `grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md` (17): “| sequence | 185 | **58.4%** | 3.0% | **~19×** | adjacent-pair order 85.2% |”
- `grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md` (100-101): “It carries the true cargo; it asserts nothing about the real world.”
- `grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd` (37-38): “regeneration was abandoned — the root cause is passage design (encyclopedic passages), not item quality.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd` (50-52): “4 encyclopedic passage types to **avoid**: curriculum-fact, headline-figure, biography, generic-process … 6 cold passage types to **use**: decision-reaction, argument-stance, obscure-consequence, surprising-reversal, specific-comparison, causal-chain … The passage-necessity test: "Could a student who studied this topic but did NOT read this passage answer correctly?"”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/passage_blind_verdicts.json` (90): “General-knowledge leak (trophic cascade): the item mirrors the well-known Yellowstone wolf”
- `grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd` (119-120): “cold-solvable ~0.8 because camel adaptations are world-famous general knowledge; distractor surgery can't close it, needs full content replacement”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (302): “argument-atom slice on famous primary sources leaked **~98.6%** (66/69 blind-solvable”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (304-305): “the leak is the reasoning, not the wording; re-anchoring rewrites converted only 1/11”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (294-295): “choice-family items on famous/transferable sources blind-solve near-totally, and *argument*-analysis items are the worst offenders because the reasoning itself leaks.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (305-306): “The one converting rewrite was a **text_entry item whose answer is a verbatim passage phrase**”
- `grade3-reading/edullm-review-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (311): “use **original/obscure passages for *assessment*** (famous sources stay for *teaching*); and”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/load-bearing-rubric.md` (45-47): “High-allusion topics are kept for the *teaching* value but carry a mandatory design consequence: items must anchor to passage-specific particulars, never canon facts”
- `grade3-reading/ti-courseplans/courses/g4-reading/approval-package/load-bearing-rubric.md` (43-45): “Extremely high allusion density means the knowledge saturates children's media and LLM pretraining — so assessment items over it become answerable *without the passage* (the measured Magellan failure).”
- `incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (302): “choice/EBSR/MSQ-only argument-atom slice on famous primary sources leaked **~98.6%**”
- `incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (302-303): “(66/69 blind-solvable by gpt-4.1; 97.1% by claude-haiku-4-5)”
- `incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (303-304): “items testing transferable argument-structure reasoning on famous primary sources are blind-solvable by construction”
- `incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (304): “the leak is the reasoning, not the wording;”
- `incept-package-hub/course-packages/courses/g7-reading/releases/2026-07-26/artifacts/Grade 7 Reading - BrainLift.md` (311): “use **original/obscure passages for *assessment*** (famous sources stay for *teaching*)”
- `incept-package-hub/course-packages/courses/g8-reading/review/evidence/case-for-review.md` (51-52): “each through 3 gates + the anti-memorization / invented-particulars screen.”
- `incept-package-hub/course-packages/courses/g8-reading/review/evidence/case-for-review.md` (55-56): “The redesign defeats the G8 POC's 98.6%-leak failure.”
- `grade3-reading/_archive/2026-08-13-consolidation/top-level-docs/HANDOFF_3_KEY_ISSUES.md` (11): “6. **Generator 480-item bundle FAILED binding Gate 1** (blind recovery 58–86% vs chance; encyclopedic content).”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-untracked.tar.gz` (courses/g5-reading/QUESTION_CONVERSION_RETROSPECTIVE.qmd inside it) (349-351): “Arbitrary in-text specifics worked for some formerly leaky items: names, titles, similes, counts, or local details with plausible alternates. These forced passage consultation when the detail was not common knowledge.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g8-reading/review/evidence/case-for-review.md` (51-52): “each through 3 gates + the anti-memorization / invented-particulars screen.”
- `incept-package-hub/course-packages/courses/g7-reading/review/evidence/validation/standards-coverage-gate.json` (69): “never the fully-arbitrary invented sense that let single-text interpret items certify at 0.00.”

Against: Learning texts are the exception: an external review faulted a course for keeping its passages from overlapping taught topics, so knowledge could not pay off, and asked for cold passages only in the test (`grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md`). Making a passage needed does not make it true: the generator's guide says the anti-leak rule "does NOT mean the passage's own facts are sourced or true" (`grade3-reading/artifacts/alpha-read-packager/generator/GENERATOR.md`, line 160). The Grade 5 passage generator also blocks curriculum topics such as the water cycle for leak risk (`grade3-reading/artifacts/alpha-read-packager/generator/g5/PASSAGE_GENERATOR.md`, lines 23-25), which a course built to teach those topics cannot do. Familiar topics are wanted in teaching material: the course's guidance for science and social-studies content holds that topics taught in an earlier grade are always fair game for re-encounter (`grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd`, line 29), so the rule is for questions that test reading, not for what is taught. the rule is for texts a test rests on: texts on one topic are meant to build knowledge during learning, so one project's reconciliation was cold texts at the gate and test and topic-coherent ones during learning (`grade3-reading/knowledge_bot/knowledge/kb-0074-g3-reviewer-feedback-distilled-for-g5-2026-06-30.qmd`, lines 42-43).

<sub>method · stage: write · stimulus, integrity · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Build the student view from an allowlist

Build what a student sees from an allowlist of the fields meant for students, and test that view for answer leaks. An independent read held back copying an AP course's first unit until six repairs were made, this allowlist among them.

An independent read of an AP course's first unit blocked copying it forward on six repairs, one of them a student-only source view holding the student material and approved citation details, with the answer-bearing fields left out (`grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd`). A later commit closed all six with an explicit student-source allowlist, and the unit's validator passed with zero errors and zero warnings (`grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd`). Mutation tests for student-answer leakage were still listed as work to do at that pause (the same file).

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd` (60): “It still issued **BLOCKED FOR REPLICATION** on six repair buckets:”
- `grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd` (71-72): “Define a student-only source projection containing `student_material` plus approved citation metadata,”
- `grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd` (88-89): “the explicit student-source allowlist”
- `grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd` (126): “mutation tests for student-answer leakage”
- `g9/transformer/src/mechanics/quick-check.js` (83): “view(item) { return { kind: "choice", stem: item.stem, options: item.options }; },”
- `g9/transformer/test/mechanics.test.mjs` (9): “The student view must never carry a key, feedback, evidence or a model answer.”
- `g9/transformer/test/mechanics.test.mjs` (30): “const leaked = keysDeep(m.view(item, ctx)).filter((k) => FORBIDDEN.includes(k));”
- `g9/transformer/v01/QA.md` (6-7): “every mechanic's shape, code checks and judge questions, that no student view carries a key, feedback, evidence or a model answer”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/TEACHING-ASSESSMENT-CONTRACT.md inside it) (125): “Student source projection is allowlisted, not subtractive. It copies only source ID, kind, creator,”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/review-evidence/README.md inside it) (23-24): “The student view is built from an explicit allowlist and omits keys, rubrics, diagnostics, correction routes, models, evaluation state, and internal evidence.”

Against: At that pause the leak tests were not yet written, and a later record of 13/13 projection tests passing doesn't say whether they cover leaks (`grade3-reading/knowledge_bot/knowledge/kb-0171-apush-full-course-local-authoring-review-hub-archive.qmd`).

<sub>method · stage: settle · integrity, stimulus · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Check every world claim

Check every claim a text presents as true about the world at the precision its grade needs. One ledger lists 32 claims across four short informational stories for an independent check.

A factuality ledger written while four informational stories were being drafted lists every claim they present as true about the world, to be checked at Grade 3 precision (short causal statements, qualitative magnitudes) rather than journal precision, and sets a fiction boundary around invented particulars (`grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md`). Invented numbers carry no claim except where they embed a real rate or magnitude, which then gets its own row; a misconception a character voices is planted to be refuted, so the check is that the refutation is clear, and a character's absolute ("never") is that character's stance, not a taught universal. The ledger also checks that a text's claim about one river's delta does not become "every river builds a delta", and a film script's notes forbid claiming that all of London had no cars or electricity (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md`). Nothing may be overgeneralized, invented details count as fiction unless they carry a real rate, and every misconception a character voices must be clearly corrected.

Quoted:

- `grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md` (17): “Every row below is a claim the texts present as TRUE about the world, at Grade-3 precision.”
- `grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md` (18): “Verify each at that precision (short causal statements, qualitative magnitudes) -- not at”
- `grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md` (72): “it does NOT overgeneralize to "every river builds a delta." Verify no reader-facing overgeneralization.”
- `grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md` (98): “Fiction boundary -- NOT world claims (do not fact-check as facts)”
- `grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md` (113): “Where an invented number embeds a real-world RATE or MAGNITUDE claim, it”
- `grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md` (115): “Character misconceptions are deliberately planted and refuted; verify the REFUTATION is clear,”
- `grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md` (120): “Stance/rhetoric riding a character voice is not a taught universal”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md` (41): “Do not claim that all London had no cars or electricity.”
- `g9/sources/Othello Unit Video_ Info Sheet for Devfactory.md` (72): “Not "the richest": by 1603 Venice was past its peak.”
- `g9/sources/Year 9 ELA_ Lesson Design Specification for Devfactory.md` (311): “By 1603 Venice was past its peak, so "one of the richest" is safer. All quotes need checking against the chosen edition.”
- `othello-archive/sources/act1/Othello Unit Video - Info Sheet for Devfactory.txt` (133): “Not "the richest": by 1603 Venice was past its peak.”
- `g9/library/text/Lbde498.txt` (72): “Not "the richest": by 1603 Venice was past its peak.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-15.md` (163): “Do not touch the passage prose "For one breathless instant, gravity let go of him." — figurative narration, correctly not challenged by the finding.”

Against: The ledger is a handoff written during drafting; it records the drafting loop's own verdicts, and the binding ones belong to a separate check it does not record (the same file, lines 3-6 and 11-13).

<sub>method · stage: review · stimulus, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Check the sequence, not only the parts

Check a sequence of texts or lessons as a whole: a fact must agree from one to the next, and true steps must not misteach in the order given. A continuity review of 2 consecutive lessons found one place put on the way to an island in the first and on the island in the second.

A factuality ledger for four informational texts asks its independent check to sign the causal model they build, not only the separate claims: no step of the chain, as sequenced across the four texts, may misteach the standard account (`grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md`, fc-32). A continuity review of two consecutive lessons, run over the raw lesson data, found a place that the first lesson put on the flight path to an island and the second showed as part of the island, a factual story-world inconsistency it rated minor (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-arc-continuity.md`). Checking each text or lesson only one at a time is not enough.

Quoted:

- `grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md` (96): “QC should sign the MODEL, not only the atoms: confirm no step of the chain as sequenced across texts 01->04 misteaches the standard account.”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-arc-continuity.md` (67): “## MINOR-1 — Mermaid Lagoon geographical inconsistency”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-arc-continuity.md` (84): “This is a factual story-world inconsistency.”
- `grade3-reading/_archive/handovers/HANDOVER-2026-09-24.md` (253): “(2) Part 1 stages all three Darling children rising together while the canonical passage and L4 p10 FIND say Michael jumps first”
- `grade3-reading/course-renderer/docs/video/u1-script-and-visual-plan.md` (87-88): “Otherwise the video showed Penelope keeping people out and then, six seconds later, taught that keeping people out is the failure.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-qc-evidence-v0.1.md` (196-197): “meadow "feeds plants" **contradicts the producer model** taught two atoms earlier”
- `othello-course-renderer-draft/repo/docs/video/u1-script-critique.md` (239-240): “The video is the more accurate of the two and this is not the script's fault, but a child meets both within a few minutes.”

Against: none found

<sub>method · stage: review · sequence, stimulus · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Check the sources before the task

Check the sources a task rests on before building or grading it, for the right period, real text and distinct documents counted by content. Of 244 parsed document packs, 12 fit the unit and none passed strict validation.

A permissive scout filled each document task with seven documents by pulling in material from after the period asked about; once the validator was tightened, the strict scout passed 0/10 (a note of 23 May 2026). An audit of 244 parsed document packs found 12 that fit the unit and 0 that passed strict validation, and set the rule that seven returned documents are not enough; the task type passed only after its source packs and topics were repaired. Later gates asked for two valid packs per topic, but this sweep compared titles and content hashes in the nine repaired pack files and found that in all 43 topics with two packs, both held the same seven texts under relabelled IDs, so one unit's 70 document slots held 32 distinct titles. Real text means text-bearing sources, not a summary or a missing image, and distinct documents are counted by content rather than by label. A count of documents returned is not a check.

Quoted:

- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T0913Z_BLOCKED_dbq_doclock_scout.md` (45): “The earlier permissive scout showed chunk fallback could produce 7 documents, but inspection exposed false positives:”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T0913Z_BLOCKED_dbq_doclock_scout.md` (37): “scout_passed: 0/10”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T1825Z_BLOCKED_dbq_source_pack_repair_list.md` (31): “Parsed DBQ packs inspected: 244”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T1825Z_BLOCKED_dbq_source_pack_repair_list.md` (32): “Unit-1-like DBQ packs found: 12”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T1825Z_BLOCKED_dbq_source_pack_repair_list.md` (33): “Unit-1-like packs passing strict doc-lock validation: 0”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T1825Z_BLOCKED_dbq_source_pack_repair_list.md` (61): “The old failure mode was treating "7 returned docs" as enough; it is not enough.”
- `icloud-work/aptraining/workspace/comms/from_den/2026-05-23T2000Z_DELIVERED_objective_completion_audit.md` (30): “Unit-1 DBQ passed only after source-pack and topic repair. Extending DBQ blindly to Units 2-9 would repeat the same source-integrity failure.”
- `icloud-work/aptraining/helpers/data/output/d13_unit2_dbq_source_packs_v1.jsonl` (1): “"doc_id": "unit2_regions_a_doc1_virginia_charter_1606"”
- `icloud-work/aptraining/helpers/data/output/d13_unit2_dbq_source_packs_v1.jsonl` (2): “"doc_id": "unit2_regions_b_doc1_virginia_charter_1606"”
- `aptraining-local/den-of-ideation/reports/unit2_dbq_source_pack_gate_20260524T030000Z.md` (18): “| colonial_regions | 2 | 2 |”
- `g9/transformer/src/mechanics/film-check.js` (82): “Is film_narration about the same work as passage, so that it can open a lesson on it?”
- `g9-transformer-runs/decisions/d2d7d0787d6754d9.json` (187): “"value": 0.01,”
- `g9-transformer-runs/blocks/d2d7d0787d6754d9.json` (97): “The film belongs with this text: the judge found this does not hold”
- `g9/transformer/src/films.js` (55): “/** The film whose narration shares most words with the text and the question; null if there is none. */”
- `g9/transformer/src/films.js` (62): “if (!best || shared > best.shared) best = { film: f, shared };”
- `g9/transformer/src/films.js` (11): “{ id: "othello-opening", title: "Othello: the opening (unit film)", file: "Othello-opening-full.mp4", vtt: "Othello-opening-full.vtt", poster: "thumbnail-othello-love.jpg" },”

Against: Passing the strict structural gate did not establish provenance: "It does not independently fetch every URL or certify that normalized excerpts are acceptable for training." (aptraining-local/den-of-ideation/to_main/2026-05-23T1831Z_DEN_REQUEST_validate_unit1_dbq_source_packs_v1.md, line 52). The uniqueness check inside each pack did not catch the same texts repeated across packs.

<sub>method · stage: ground · stimulus, integrity · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Choose the texts before the questions

Choose a unit's texts before its questions, each with a stated role in building knowledge of its topic, so that no text could be swapped out without changing the unit.

The reading course's plan asks for a planned set of texts chosen before any question is written, each with a role such as introducing the concept, adding background, complicating it, contrasting with an earlier text, shifting genre or raising vocabulary demand, and calls it a bad sign when any text could be swapped out without changing the unit. Written feedback on an earlier build, whose texts were chosen mainly by Lexile, asked for a coherent knowledge sequence and a genre balance instead. The plan's outside orientation describes knowledge-building curricula as going deep on a topic with sets of texts and spiralling back to it in later grades with more sophistication. A proposed unit was declined because an earlier grade's unit already covered both angles it claimed as new, the mistake for which a similar unit in another grade had been retired. No unit should repeat what an earlier grade taught.

Quoted:

- `grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/01-course-graph.md` (63): “A planned set of texts selected before questions are written.”
- `grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/01-course-graph.md` (75): “Bad sign: any text can be swapped out without changing the unit.”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (53): “Choose texts for a coherent knowledge sequence and a genre balance that includes poetry, drama and more literary work, and judge complexity qualitatively as well as by Lexile.”
- `grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/13-candidate-themes-and-selection-rubric.md` (5): “spiraling back to topic areas with more sophistication.”
- `grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/13-candidate-themes-and-selection-rubric.md` (7): “Source: https://knowledgematters.org/curriculum-directory/”
- `grade3-reading/artifacts/g5-course/HUMAN-BODY-III-DECISION.md` (10): “exact mistake for which G4's Human Body II was retired, and the G4 crosswalk already”

Published: [Knowledge Matters, Curriculum Directory](https://knowledgematters.org/curriculum-directory/)

Against: none found

<sub>method · stage: ground · stimulus, sequence, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Cut the text into units to point at

Cut each text into units a question can point at, a spoken line with its speaker, a verse line or a sentence, and never count stage directions as evidence.

The lesson engine parses every text into numbered units its blocks point at, a verse line with its speaker in a play, a line in a poem and a sentence in prose, and keeps stage directions for display but never as evidence (`g9/transformer/src/text.js`, lines 1-2). Line numbers from the writer are mapped to spoken lines only (`g9/transformer/src/mechanics/util.js`, line 28). The preferred quotation matcher, a 3D version's own, refuses a quotation that runs across a stage direction or across two speeches (`g9/transformer/src/glue/threejs.js`, lines 53-54). The code gives no reason for the drama rules.

Quoted:

- `g9/transformer/src/text.js` (1-2): “A text becomes numbered units that mechanics can point at: a verse line with its speaker (drama), a line (poem), … or a sentence (prose). Stage directions are kept for display but are never evidence.”
- `g9/transformer/src/mechanics/util.js` (28): “Writer line numbers (L numbers) -> unit indices, keeping only spoken lines.”
- `g9/transformer/src/glue/threejs.js` (53-54): “punctuation, case and apostrophes aside, never across a … stage direction or two speeches.”
- `incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u02.md` (187): “item requiring the student to use a stage direction — not a spoken line — to answer (distractor:”

Against: Without the 3D version's tools, the fallback matcher joins consecutive spoken lines with the directions left out, so a quotation can then run across a direction or two speeches: "Find a quotation in the text. It may span consecutive lines." (`g9/transformer/src/text.js`, line 52). A later run found: Where a lesson teaches play conventions, a stage direction is the evidence: an archived Grade 3 drama lesson requires an item that only a stage direction, not a spoken line, answers. The rule never to count stage directions as evidence holds only where they are not what is taught (`incept-package-hub/course-packages/archive/g3-reading-v2/authoring/prompts/u02.md`).

<sub>method · stage: ground · stimulus, integrity · universal · from g9 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/), [2026-10-12-6-transformer-ideas](../research/2026-10-12-6-transformer-ideas/)</sub>

### Drop, don't patch

Drop an item whose fact can't be traced to a cited source rather than patching the gap with a generated claim.

Adopted for new AP training sets after model-written source text was blamed for most factual failures of document-based items (`icloud-work/auto-memory-backup/feedback_no_hallucination_in_training_data.md`, lines 15-19). The project judged that allowing generated text anywhere in a curated set would recreate the same failure, and ruled that a record with a fact that can't be cited to a primary source is dropped, not patched (line 33). The rule still allows prompts, reference answers and connecting text written by hand (lines 27-29). Handovers from the same work extend the rule to any source or data row that fails an audit: drop it rather than rework it until it passes.

Quoted:

- `icloud-work/auto-memory-backup/feedback_no_hallucination_in_training_data.md` (33): “**Drop-don't-patch rule:** if a fact in a candidate record can't be cited to a primary source, the record gets dropped from the corpus, not patched with a synthesized claim.”
- `icloud-work/auto-memory-backup/feedback_no_hallucination_in_training_data.md` (19): “If we curate a "real-source corpus" but allow LLM-generated content anywhere in it (gold responses, glue text, paraphrased document text), we recreate the same failure mode. **The point of curation is verified facts; hallucination defeats the purpose.**”
- `icloud-work/auto-memory-backup/reference_curriculum_api_lan.md` (85): “- v29 SFT data: pull all KCs per course, generate one MCQ + one SAQ per KC using the bundled scaffolding as the prompt context, IB-grade, keep ≥0.85”
- `icloud-work/aptraining/handover/2026-05-01T1039Z_main_session_close/01_HANDOVER.md` (89): “Drop-don't-patch when sources fail.”
- `icloud-work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md` (359): “- **Drop-don't-patch** on any audit failure.”

Against: The same project later had a model write items from verified facts and kept those the grader passed: "- v29 SFT data: pull all KCs per course, generate one MCQ + one SAQ per KC using the bundled scaffolding as the prompt context, IB-grade, keep ≥0.85" (`icloud-work/auto-memory-backup/reference_curriculum_api_lan.md`, line 85). No result of applying the rule is recorded. The later generation service repaired rather than dropped: when the model returns malformed JSON, the route repairs the schema from the retrieved context (the generation service's `README.md`, line 30), and a later spec mutates a failing candidate to address the criterion it failed (`99stack_layer4_repair_spec.md`, line 14). Both repair generated items, not sources or data rows.

<sub>method · stage: ground · integrity, generation · universal · from ap · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Excerpt a coherent span, boundary recorded

Cut every excerpt students analyse as a coherent span re-extracted from the original document, record its exact boundary, and reject scanned-text fragments, added modern text, arbitrary cuts and truncations.

An audit of an AP history course's local source packs found OCR fragments, modern editorial text, arbitrary cuts and false classifications, so students could be asked to source a fragment that is not what its label says, and its stimulus bank held exact truncations, duplicated passages and mismatched topic assignments. The packs were rejected as excerpts: every adopted source is re-extracted as a coherent span from the underlying archive, or replaced by an original, cited course synthesis, and its format, answerability and independence checks are rerun. Each accepted source's ledger row records its exact excerpt boundary beside its title, date, edition, stable link, rights basis and content digest.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (50): “D13 v2 contains OCR fragments, modern curator text, arbitrary cuts, and false classifications.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (50): “Students could be asked to source a fragment that is not what its label says.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (50): “Re-retrieve coherent spans from the underlying archive or use an original, cited course synthesis.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (51): “The stimulus bank contains exact truncations, duplicated passages, and mismatched KC assignments.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (47): “Re-extract every adopted source and rerun current-format, answerability, and independence checks.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/CED-LOCAL-RECONCILIATION.md inside it) (57): “Its ledger row must include canonical title, creator, original date, edition or translator, stable URL, retrieval date, exact excerpt boundary, rights basis, content digest, KC alignment, and a label distinguishing quotation, adaptation, and original course narration.”

Against: An alternative, not a counter: where no coherent span can be retrieved, the course allows "an original, cited course synthesis" instead (grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz:apush/docs/CED-LOCAL-RECONCILIATION.md, line 50).

<sub>method · stage: ground · stimulus, integrity · universal · from ap · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Fix the lesson, never the source

When a lesson's passage and its fixed source text disagree, change the lesson, never the source.

A content audit for Grade 3 reading lessons holds every visible passage to the fixed source text, rates an added, removed or replaced word as high severity, and says to update a text by replacing its file, never by editing it to match a lesson (`shadow/content-eval/SKILL.md`, `shadow/content-eval/README.md`). Aligning whole nodes reported legitimate excerpts as rewrites, so it compares each paragraph against its own window of the source.

Quoted:

- `shadow-content-eval/README.md` (110-111): “To update a text, replace its file. Don't edit it to match a lesson: the lesson is what gets fixed.”
- `shadow-content-eval/SKILL.md` (242): “Whole-node alignment reported both as rewrites.”
- `shadow-content-eval/SKILL.md` (227): “| `PASSAGE-TEXT-CHANGED` | high | a word is added, removed or replaced relative to the fixed text |”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/RESTORATION-PLAN.md` (80): “Only semicolons inside exact registered quotations are exempt; unrelated authored prose remains checked. Negative regression tests cover a changed quotation and an extra semicolon.”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/unit9/lesson-04.md` (3): “Quotation fidelity takes precedence in this source packet”
- `grade3-reading/visual-findings-2026-09-07/review-readiness/curriculum-alignment/rebuild/integration/test-source-quotations.txt` (5): “Literary quotations: exact edition verified; altered quotes and authored semicolons remain rejected.”
- `grade3-reading/curriculum-gen/audits/PETER-PAN-AUDIT-2026-08-24.md` (393-394): “Record one sequence-wide policy for assigned words absent from source prose. Do not mutate story text or silently substitute a validator-friendly word.”
- `grade3-reading/curriculum-gen/HANDOVER-2026-08-25-PR27.md` (185-186): “Rewriting the story, swapping the assigned word, or enlarging generic known debt are all wrong.”
- `grade3-reading/artifacts/Peter-Pan-L4-review-response-2026-08-25.pdf` (p.5 (pdftotext line 226)): “We have not written around this and we have not edited the story to host the word.”

Against: A house style can require a change: the audit treats a source dash replaced by other punctuation as information, mandated by a rule against dashes in text shown to children, not a defect (`shadow/content-eval/SKILL.md`).

<sub>method · stage: settle · stimulus, integrity · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Guard each unit against misconceptions

List the misconceptions each unit must guard against, and screen every text carrying a subject's content for them, even outside that subject's course, by meaning as well as phrase. A later full-course evaluation counted 22 hits on its list of banned misconception phrasings across 8 lessons.

A review of the reading course asked for unit-level misconceptions to guard against alongside each unit spine, including science misconceptions. The routing contract built from that review applies the misconception-check process to every science-bearing reading or writing text and asks that observation, hypothesis, theory, consensus, measurement, interpretation and opinion be distinguished accurately. A later full-course evaluation counted 22 Tier-1 misconception hits across 8 lessons. Simplify only where the text stays accurate and blocks no later learning.

Quoted:

- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (53): “- Add unit-level misconceptions to guard against alongside each unit spine, including the science misconceptions discussed below.”
- `grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` (48): “4. apply the misconception-check process to every science-bearing Read/Write text;”
- `grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` (49-50): “5. distinguish observation, hypothesis, theory, consensus, measurement, interpretation, and opinion accurately.”
- `grade3-reading/knowledge_bot/knowledge/kb-0215-g5-media-recovery-plan-and-edullm-entrypoint-test.qmd` (61): “course `courses/g3-reading-v2/reapproval-package`”
- `grade3-reading/knowledge_bot/knowledge/kb-0215-g5-media-recovery-plan-and-edullm-entrypoint-test.qmd` (84-85): “22 Tier-1 misconception hits across 8 lessons”
- `grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` (48): “apply the misconception-check process to every science-bearing Read/Write text;”
- `grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` (66): “- diagrams or models presented as literal reality;”
- `grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` (393): “By 1603 Venice was past its peak, so "one of the richest" is safer.”
- `grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md` (24): “Good science instruction is undone by encounters with folk science that is intuitively appealing but scientifically incorrect.”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (145): “"the plant grows by taking food from the soil" implies plants-eat-soil without the literal phrase”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (147): “a food chain / atom / cell diagram presented as literal reality”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (146): “a comprehension MCQ whose "correct" answer or distractors reward the folk belief”
- `grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md` (136-137): “it actively undoes correct science instruction (the ATP case: even students who learned it right get re-taught the error).”
- `grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd` (802): “- Claim boundary: Simplification is acceptable only when it remains accurate and does not create a later-blocking misconception.”
- `grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md` (20): “**Language risk is low.** There is little risk of misconceptions developing through inappropriate use of language.”
- `grade3-reading/_archive/2026-08-13-consolidation/dirty-state/ti-courseplans-main-checkout-jul-work.patch` (20713): “| **Tier-2 missing framing** | an adaptation text that never says variation is random + pre-existing; an energy text that never frames conservation | scan --topic flags the required framing's absence |”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/docs/SCIENCE_MISCONCEPTION_CHECK.md inside it) (99-100): “A missing Tier-2 framing now blocks the bounded content-review PASS; it cannot be carried as a harmless warning merely because the Tier-1 literal scan is clean.”
- `grade3-reading/ti-courseplans/courses/g5-reading-v2/docs/SCIENCE_MISCONCEPTION_CHECK.md` (99-100): “A missing Tier-2 framing now blocks the bounded content-review PASS; it cannot be carried as a harmless warning merely because the Tier-1 literal scan is clean.”
- `grade3-reading/_archive/2026-08-13-consolidation/g5-full-course-worktree-full-tree.tar.gz` (g5-reading-v2/docs/SCIENCE_MISCONCEPTION_CHECK.md inside it) (102): “Tier-2 flags and implied folk models block review publication and release until repaired.”
- `grade3-reading/ti-courseplans/courses/g5-reading-v2/docs/SCIENCE_MISCONCEPTION_CHECK.md` (102): “Tier-2 flags and implied folk models block review publication and release until repaired.”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/HUMAN-g3r-2026-07-20T11-20-06-019f7ed3-5205-72f0-a25a-caf13bf2a620.md` (84-88): “- The Jul-16 feedback is explicit and binding: "all text that relates to science must go through the misconception check process." - The package has no science-passage misconception screen, no scoping doc, and doesn't claim one exists — it only handles misconceptions inside item feedback routes.”
- `grade3-reading/_archive/2026-08-13-consolidation/redteam-g3-round3-report-and-evidence.tar.gz` (RED_TEAM_ROUND3.md inside it) (91-92): “A `make` → `release` word swap would leave the underlying model wrong.”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “Four science-heavy units had no passage-level misconception gate.”
- `grade3-reading/course-renderer/docs/pedagogy/misconceptions/cross-cutting-synthesis.md` (70): “Even students who learned the correct chemistry are re-taught the misconception in biology class. This is the most damaging cross-disciplinary failure.”
- `incept-package-hub/course-packages/courses/g5-reading/review/brainlift.html` (1): “Item feedback cannot repair a misconception already taught by the passage.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/MISCONCEPTION-COMPLIANCE-LOG.md inside it) (36): “so the rule **missed a required catch**”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/BRAINLIFT.md inside it) (309-311): “The course anticipates errors at three levels: knowledge structure, source reasoning, and task performance. Naming those errors before authoring improves models, distractors, feedback, and correction.”
- `grade3-reading/artifacts/arc-audit/REGISTER-2026-09-15.md` (146): “Every passage node in L4 carries a shared glossary that defines gravity as 'Gravity is the force that pulls everything down toward the ground.' This is the exact folk-physics framing D9.19 prohibits;”
- `grade3-reading/.claude/skills/sim-review/SKILL.md` (24-25): “D9 (science integrity) is fiction-arc out-of-scope: have C confirm in one line no science claims pull it in.”

Against: there was no settled consensus science curriculum to check against, so a draft science ledger could not establish canonical scope or treatment (`grade3-reading/knowledge_bot/knowledge/kb-0149-draft-grade-5-science-ledger.qmd`). The same brainlift rates the risk of misconceptions from wording as low in social studies, so the check bears hardest on science (`grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md`).

<sub>method · stage: ground · stimulus, integrity · universal · from g3, g9 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Insert whole sentences, then recheck references

Edit a passage that questions, quotes or clips point into only by inserting whole sentences, never by altering existing ones, and recheck every reference afterwards. Before the reference check existed, one rewrite broke six things no validator could see.

The grade-3 authoring rules pin passage edits: insert whole sentences and never extend existing ones, because clip keys, span groups and candidate matches all break on extension. A rewrite must also pass a reference check confirming that quoted sentences, dialogue evidence, reread excerpts and glossary terms still exist verbatim in the rewritten story. One rewrite broke six things no validator could see before that check existed.

Quoted:

- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (66-67): “Passage edits are pinned: INSERT whole sentences, never extend existing ones (clip keys, span groups, and candidate matches all break on extension).”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (81-83): “**A passage rewrite must not break existing references**: run `validate-passage-refs.mjs`, which checks that quoted sentences, dialogue evidence, reread excerpts, and glossary terms still exist verbatim in the rewritten story”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (83-84): “a rewrite once broke six things no validator could see before this check existed”
- `grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd` (111-113): “**Root cause:** `validate-passage-refs` only proves the span text is a SUBSTRING of the passage; it does not run the engine's own unit-boundary logic (`unitsOf`/`partOfLine`), so a span that is textually valid but unit-misaligned passes the validator and silently fails the student experience.”
- `grade3-reading/course-renderer/docs/extras/alpharead-lesson-design-plants-l1.md` (22): “Eight sentences were ADDED, never lengthened, and no existing sentence was edited, so every quote, hot-text target, think-aloud candidate, dialogue evidence line and cloze answer bound to the text is unchanged.”
- `grade3-reading/course-renderer/docs/extras/alpharead-lesson-design-plants-l1.md` (22): “Each addition elaborates what its own section already says”

Against: The reference check proves only that a span's text is a substring of the passage, not that it lines up with the units the engine prints, so a textually valid but misaligned span passes it and silently fails the student (grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd, lines 111-113). One lesson's passage, expanded by adding eight whole sentences and editing none, was recorded as still pending review (`grade3-reading/course-renderer/docs/extras/alpharead-lesson-design-plants-l1.md`, line 22), so nothing yet shows the longer text was accepted.

<sub>method · stage: improve · stimulus, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Keep objectives and cited facts

Keep learning objectives and cited facts as two levels of a single store, since either source alone can lose much of what the other holds. In one course, 39% of the objective-level entries had no match among the facts, and 99.8% of the facts had no match among the objectives.

Comparing two AP curriculum sources for one course showed they sat at different levels of the official hierarchy: 39% of objective-level entries had no match among the facts, and 99.8% of the facts had no match among the objectives (`icloud-work/auto-memory-backup/feedback_oracle_source_reconciliation.md`, line 44). One source alone lost 1,049 cited facts; the other alone lost 838 sub-objective breakdowns with misconceptions (line 30). Tagging to the objectives with the facts beneath is the note's plan, not a tested result.

Quoted:

- `icloud-work/auto-memory-backup/feedback_oracle_source_reconciliation.md` (44): “The two sets are at different tiers of the CB hierarchy.”
- `icloud-work/auto-memory-backup/feedback_oracle_source_reconciliation.md` (44): “39% of curriculum repo APUSH has no InceptBench match; 99.8% of InceptBench's atomic facts have no curriculum match. **Best path: merge them — use curriculum repo as the canonical tagging skeleton, layer InceptBench's atomic facts as the evidence tier underneath.**”
- `icloud-work/auto-memory-backup/feedback_oracle_source_reconciliation.md` (30): “- **APUSH with either alone**: curriculum-only loses 1,049 atomic facts; InceptBench-only loses 838 sub-KC pedagogical decompositions with common-misconceptions. Single-source halves the pedagogy.”
- `icloud-work/auto-memory-backup/feedback_oracle_source_reconciliation.md` (40): “78% of curriculum repo APWH content is already in InceptBench (with matching CB-format KC IDs).”
- `icloud-work/auto-memory-backup/feedback_oracle_source_reconciliation.md` (8): “Histories (APUSH, APWH, APEURO) only — non-history AP subjects not analyzed.”

Against: In another course one source was kept as primary and backfilled, and there the sources overlapped heavily: "78% of curriculum repo APWH content is already in InceptBench (with matching CB-format KC IDs)." (`icloud-work/auto-memory-backup/feedback_oracle_source_reconciliation.md`, line 40). The analysis covered "Histories (APUSH, APWH, APEURO) only — non-history AP subjects not analyzed." (line 8), and the merge has no recorded result.

<sub>method · stage: ground · alignment, stimulus · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Make a scored selection recomputable

Choose topics or texts by an open score whose factors, weights and totals anyone can recompute, and let a person override it only with a recorded reason.

In its queue of work after feedback on the reading course, the project made two things preserve-obligations: a topic scorecard whose every topic record exposes factor values, weights, total and verdict, so the verdict can be recomputed, and a visible human override where a person can keep or reject a topic against the score with a recorded reason (`grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/feedback-obligations.jsonl`). The curriculum packet requires a topic score replay showing factors, weights, formula result, human override and final verdict (`grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/curriculum-agent.md`).

Quoted:

- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/feedback-obligations.jsonl` (2): “Every topic record exposes factor values, weights, total, and verdict.”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/feedback-obligations.jsonl` (3): “Retain a visible human override path where a person can keep or reject a topic against the score with a recorded reason.”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/feedback-obligations.jsonl` (3): “Human override is a governance control, not evidence that the selected topic is effective.”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/curriculum-agent.md` (38): “Topic score replay showing factors, weights, formula result, human override, and final verdict.”
- `grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` (9): “praises the transparent scorecard, human override”
- `grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` (26): “transparent plan-first topic scoring, reasoned human override”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (17): “They can challenge the weightings, inspect what falls out, and push on a decision they disagree with.”
- `grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` (18): “A person overrode the score and gave a reason rather than allowing the number to decide.”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/TOPIC-SELECTION.md inside it) (10): “portfolio-level deficit the per-topic scorecard structurally could not see”
- `incept-package-hub/.artifacts/source/g3-reading-approval-package.zip` (reapproval-package/sources/LOAD-BEARING-METRIC.md inside it) (121): “**Override** = a keep that contradicts the score, justified by a *limitation of the scorecard itself*.”

Against: The same obligations say the praise applied to the approach, not to the metric's calibration, and that a human override is a governance control, not evidence that the chosen topic is effective (`grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/feedback-obligations.jsonl`). It rests on one review's endorsement, not on a measured outcome. the same review could not yet follow one factor of the score, a load-bearing metric, and asked for it to be explained, so a formula is only open to challenge once its factors are (the same file).

<sub>method · stage: ground · stimulus, review · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Map every fact to the curriculum

Map every fact taken from a source to the part of the curriculum it serves, and drop or review the ones that fit none. In one unit's build, 437 of 1,194 facts extracted from source texts mapped to no part of the curriculum.

One unit's knowledge build had a model generate facts from source texts and then map each one to the curriculum (`icloud-work/k_12_social_studies/ap_files/Knowledge Schema Generator - AP USH Unit 1 - Instructions.csv`, line 16). In its mapping output, 437 of 1,194 facts carried 'None' in the cluster column, against 757 mapped to a topic, and the refinement step set facts on whole civilisations aside as out of scope (`icloud-work/k_12_social_studies/ap_files/Knowledge Schema Generator - AP USH Unit 1.xlsx`, sheets '2. Mapping Output' and '6. Fact Refinement Output').

Quoted:

- `icloud-work/k_12_social_studies/ap_files/Knowledge Schema Generator - AP USH Unit 1.xlsx` (sheet '6. Fact Refinement Output', cell F2): “3. Out of Scope (Mesoamerican civilizations):”
- `icloud-work/k_12_social_studies/ap_files/Knowledge Schema Generator - AP USH Unit 1 - Instructions.csv` (16): “7. In the main.py script, run steps 1 and 2 (generate facts + map facts to curriculum).”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/SEQUENCING-BRIEF.md inside it) (131-132): “**F3: Scope drift.** Detection: a lesson cannot map to a local topic ID/KC or crosses its period without explicit context. Recovery: remap, move, or remove the unsupported material.”

Against: An unmapped fact may still be background students need: the reviews kept asking for added definitions and context, so dropping every one could remove support students need (see the record on background at the line that needs it).

<sub>method · stage: ground · alignment, stimulus, generation · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Match the required text itself

When a course must cover a required list of texts, count a match only for the text itself, and record another edition or a merely related topic apart from it. Against a required list of 23 texts, one course had only 1 in full, 3 more only as another edition or a related topic, and 19 not at all.

A comparison of a Grade 3 course against a state's proposed list of mandatory literary works marked each required text as a full match, partial, near or missing, and kept "same myth, different source text/edition" and "related topic, different text" apart from a full match (`downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/TEA Proposed Mandatory Literary Works (HB 1605).xlsx`, sheet 'G3 Comparison', cells E9 and E13). Its summary counts 23 required texts: 1 full match, 3 partial or near, and 19 missing (cells B27 to B30). The course map tags four of the missing folk tales as the course's own adaptations of public-domain sources, marked for the required list, and one more required text as a proposed addition (`downloads/_G3 curriculum Map.xlsx - Curric Map.csv`, lines 14 to 17 and 37).

Quoted:

- `downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/TEA Proposed Mandatory Literary Works (HB 1605).xlsx` (sheet 'G3 Comparison', cell E9): “in Unit 10 (Myths) — same myth, different source text/edition”
- `downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/TEA Proposed Mandatory Literary Works (HB 1605).xlsx` (sheet 'G3 Comparison', cell E13): “(Unit 3) — related topic, different text”
- `downloads/_G3 curriculum Map.xlsx - Curric Map.csv` (14): “TEA HB 1605 (Alpha adaptation of PD source)”
- `grade3-reading/ui-audit-2026-09-08/WORKFLOW.md` (26): “A complete reader, opened link, bookmark or finished short adaptation does not prove full-book reading.”
- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE3.md` (64): “a matching folktale motif is not exact source identity.”
- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/PLAN.md` (25): “Adversarial review: a work title match is not an edition match; a sourced badge is not proof the lesson uses that source; an adaptation is not a complete core work; portal unit numbers may differ from runtime IDs.”

Against: none found

<sub>method · stage: ground · alignment, stimulus · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Pin the edition of every text

Pin the exact edition or translation of every source text, since its reading level and its rights can differ from one edition to the next. One translation of a book is documented at 800L, while other translations run 1200L.

Research into public-domain books for the reading course found one translation of a book documented at 800L while other translations run 1200L, and pinned that translation by its year. It also found that for some series only the original edition's text is in the public domain, while the revised editions everyone knows are still under copyright.

Quoted:

- `grade3-reading/artifacts/g5-course/PD-FICTION-RESEARCH-2026-08-19.md` (25): “translation specifically (others run 1200L)”
- `grade3-reading/artifacts/g5-course/PD-FICTION-RESEARCH-2026-08-19.md` (13): “only the ORIGINAL edition text is PD — the revised editions everyone knows are still”
- `g9/transcript/chat-transcript.redacted.txt` (1242): “I’m looking for it and including the full Folger text as a clearly labelled reference.”
- `g9-archive/handover-2026-10-06/Othello-handover-docs-and-transcript-2026-10-06.zip` (Othello-handover/Othello-project-handover.txt inside it) (172): “Do not infer that the play’s public-domain status resolves every edition, illustration, recording, or packaging right.”

Against: none found

<sub>method · stage: ground · stimulus, integrity · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Plan the text in layers

Plan each text in layers before writing it: what it states, what it implies with support, and plausible neighbouring ideas it does not support, kept for the wrong options.

In a Grade 3 demonstration unit, passages carry a header that plans their layers before the text: what is stated and what is implied with support, and for the unseen capstone passage also plausible neighbouring ideas the text does not support, listed for use as distractors. A primer passage's header lists its stated and implied layers, including one implied point the text raises but does not settle.

Quoted:

- `grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/passage.md` (18): “unsupported-plausible neighbors (for distractors; NOT in the text)”
- `grade3-reading/artifacts/demo-unit-2026-07-10/passages/kingfisher-bend-01.md` (10): “layers: stated = photo figure, both jar results, current definition, muddy-means-carrying; implied = high water carries more than low water”

Against: Planning layers did not by itself make items need the text: none of the 10 selected-response items written on the capstone passage passed its anti-leak gate, 8 of them answerable without any passage and 2 from the taught texts alone (`grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/gate-capstone-summary.json`, lines 12-16).

<sub>method · stage: write · stimulus, distractors · universal · from g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Read a simplified text against its original

Check a simplified text by reading it against its original, because a better reading-level score can hide a changed meaning, lost key terms and mechanical prose. Simplified versions read at a lower grade in 68 of 71 pairs, yet one sentence split re-paired ideas and changed a paragraph's meaning.

In a readability trial, a prompted model simplified articles, and the simplified version had a lower reading grade than the original in 68 of 71 rows, for example 16.1 to 11.9 (`icloud-work/k_12_social_studies/ap_files/Articles Tracker.xlsx`, sheet 'ReadabilityExperiment-dev-inter'). Reading the pairs line by line found a sentence split that paired the wrong ideas and changed a paragraph's meaning (cell N13), and splits that gave the prose a predictable, mechanical pattern (cell N8). Review of another simplified run found curriculum terms replaced by everyday words and asked for them to stay (sheet 'APUSH Articles-readable-exp', cell M2).

Quoted:

- `icloud-work/k_12_social_studies/ap_files/Articles Tracker.xlsx` (sheet 'ReadabilityExperiment-dev-inter', cell N8): “Some of these changes give the flow an overly predictable pattern. That's not always a bad thing, but it can feel very mechanical and repetitive, which is not ideal.”
- `grade3-reading/visual-findings-2026-09-08/all-grades-source-audit/GRADE3.md` (60): “Part 4 is especially concrete: its specified “squared his shoulders” evidence becomes “stood up tall” on the first read and the later model source.”

Against: The simplified version was still preferred in most pairs (sheet 'ReadabilityExperiment-dev-inter', column K 'final preference': 23 'New' against 7 'Old', with 41 left blank), so on balance simplifying helped.

<sub>method · stage: review · wording, stimulus, generation · universal · from ap · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Reading level measures complexity only

Strip markup, tables and equations before estimating reading level, and check mechanical faults such as merged words or stray symbols separately, because a readability estimate measures only complexity.

An AP evaluator estimates reading level in code from average sentence length and how common the words are, and strips formatting such as markup, tables and equations before measuring, so layout is never mistaken for difficulty. Its reading rubric keeps automatic fails for merged non-words and confusing symbols whatever the computed level, because the estimate measures complexity, not mechanical defects, and the estimate may clear a judge's failure only when that failure was about complexity.

Quoted:

- `shadow-bench/docs/brainlift.md` (203): “An open estimate is derived from two inputs, average sentence length and how common the words are, which are the two drivers of the proprietary Lexile Framework.”
- `shadow-bench/docs/brainlift.md` (203): “Formatting such as markup, tables and equations is stripped before measuring, so layout is never mistaken for difficulty.”
- `shadow-bench/src/inceptbench/prompts/fiction_reading/evaluation.txt` (400-402): “The automatic-fail readability patterns (merged non-words, confusing symbols) ALWAYS apply regardless of the computed Lexile — the estimate measures complexity, not mechanical defects.”
- `shadow-bench/docs/internals/lexile_evaluation.md` (41-43): “**Up-override (conservative):** reliable estimate comfortably in band AND the LLM's failure was about complexity (not a mechanical defect like merged words) → un-fail to 1.0.”
- `shadow-bench/` (commit 3c78f22) (7-8): “Global across grades; built and calibrated on Grade 3 reading.”
- `shadow-bench/docs/internals/lexile_evaluation.md` (73-74): “Calibration outside the G3 range is approximate and pilot-tunable”

Against: The estimate was built and calibrated on Grade 3 reading; outside that range it is approximate and pilot-tunable.

<sub>method · stage: settle · stimulus, measurement, wording · universal · from ap, g3 · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Real word parts, checked against a reference

Check every word-part split, affix meaning and pronunciation against a dictionary or rule-based reference, never intuition, because invented splits teach false word-parts. Checked against a rule-based reference, 5 of 23 authored word-part splits were flagged, two of them teaching a flatly wrong rule.

Verifying a course's 23 authored word-part splits against a rule-based reference flagged 5 for review: two taught a flatly wrong rule on screen, two were folk splits and one was defensible but non-standard (`grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd`, lines 49-66). The course's QC checklist, which counts all 5 as wrong, now requires every split checked that way, never by intuition, with words that don't decompose taught as word families (`grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md`, row L2). Reviews found affix glosses that over-generalise, such as '-ing means it is happening right now' for two descriptive words, and a gloss built on a verb that doesn't exist, 'one who stranges' (`grade3-reading/artifacts/peter-pan-standing-2026-09-11/PP-STANDING.md`; `grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md`), and an audit found a suffix printed without its hyphen, which a young reader takes for the insect (`grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md`). A calibration log ranks this class, content correctness against an outside authority, as the most frequent judgment machines couldn't make: 4 hits across all 9 logged rounds (`grade3-reading/artifacts/cert-layer/AUTOMATED-CHECKS-ROADMAP-2026-08-31.md`). Teach only real word parts: print each affix with its hyphen, and teach a word that doesn't split as a word family.

Quoted:

- `grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md` (224): “5 of 23 authored splits wrong”
- `grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md` (224): “Morph splits verified against a rule-generated reference”
- `grade3-reading/artifacts/peter-pan-standing-2026-09-11/PP-STANDING.md` (37): “("-ing means it is happening right now" for enchanting / menacing, whose definitions are descriptive)”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md` (28): “morpheme gloss inaccurate (stranger ≠ "one who stranges")”
- `grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md` (132): “the morpheme gloss writes "the suffix ant" without a hyphen (reads as the insect to a grade-3 student)”
- `grade3-reading/artifacts/cert-layer/AUTOMATED-CHECKS-ROADMAP-2026-08-31.md` (266): “judgment across all 9 logged rounds (4 hits, the top-ranked residue class).”
- `grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd` (49): “rule-generated not looked-up”
- `grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd` (50): “to all 23 authored vocab decompositions; 5 flagged for review”
- `grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd` (65-66): “merciless and stranger are the two teaching a flatly wrong rule on screen”
- `grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` (96-97): “look up dictionary IPA (Wiktionary + Merriam-Webster), never guess”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (55): “The family stage teaches only real derivations — *eerily, eeriness* — never invented splits, because syllables are not morphemes.”
- `downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md` (21): “Syllable breaks for saying; meaning-parts only when real | Inventing splits (ee+rie) would teach false word-parts”
- `downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md` (89): “Only *cheerful* of the three genuinely decomposes, so only *cheerful* gets a meaning-parts stage — the others get word families instead.”
- `grade3-reading/artifacts/judgment-corpus/distilled-src/04-CONTENT-AUTHORING.md` (340-341): “the morpheme split is a separate, later move. "Morphemes are meaningful elements, syllables are spoken parts" — the two must never be conflated on one tile.”
- `grade3-reading/artifacts/contract-drafts/DICTIONARY-TILE-PROPOSAL-2026-08-31.md` (43-45): “That fallback is why syllables and morphemes are already conflated in code: today, if a word has no `morph`, the pronunciation hyphens are pressed into service as if they were morpheme chips.”
- `grade3-reading/artifacts/feedback-vocab-design-2026-09-21/REGISTER.md` (10): “say the WHOLE word, highlighted as spoken ("not be-tray-al"), then the child says it”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (420-423): “prefix/suffix reference list covers ~90% of multisyllabic words the course will teach; the remaining ~10% (and judgment calls even within the covered 90%) require HUMAN judgment — morpheme analysis has no formulaic AI approach, because Latin, Greek, and Old English root patterns vary in ways a fixed rule set will not reliably catch.”
- `grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/04-CONTENT-AUTHORING.md` (423-425): “Do not attempt to fully automate morpheme-split generation; treat the prefix/suffix list as the high-coverage starting reference, not a replacement for a human pass.”
- `grade3-reading/ui-audit-2026-09-08/round-5/peter-pan-evidence-repairs-2026-09-10/glossary/HINT-AND-MORPHOLOGY-TRIAGE.md` (29): ““The suffix ing means it is happening right now.””
- `grade3-reading/ui-audit-2026-09-08/round-5/final-standard-verification/SEMANTIC-FIVE-FLAG-DISPOSITION-by-residual.md` (16): “the taught `-less` is a suffix, not the model's claimed prefix.”
- `grade3-reading/course-renderer/authoring/peter-pan/fill/EIGHT-GAP-ROUND-SPEC-2026-09-11.md` (32): “"The suffix ing means it is happening right now."”
- `grade3-reading/.claude/skills/sound-out-respell/SKILL.md` (16-20): “Look the word up, never guess … Write the IPA into the record before touching anything.”

Against: No verified morpheme reference was in the repository to diff against, so the class was judged not automatable honestly (`grade3-reading/artifacts/cert-layer/AUTOMATED-CHECKS-ROADMAP-2026-08-31.md`). the word-part tool generates its splits by rule rather than looking them up, so its own verdicts need the same check. One lesson's rule, recorded in walkthroughs that have since been superseded.

<sub>method · stage: ground · wording, integrity · universal · from g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Recent claims need a current source

Re-verify every dated claim and source on recent events against a current source before release: a curriculum bundle is no authority on what happened after its build date.

The final unit specification of an AP history course warns that recent-history claims are especially drift-prone: every dated claim and source needs current verification before release, and the local curriculum bundle is a scope substrate, not perpetual authority for events after its build date. That unit's writing progression includes a current-source provenance check. It is a declared rule, not a measured one.

Quoted:

- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (228-230): “Recent-history claims are especially drift-prone. Every dated claim and source needs current verification before release; the local bundle is a scope substrate, not perpetual authority for events after its build date.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (225-226): “Causation with multiple time horizons; current-source provenance check; cumulative argument using evidence from at least three periods.”
- `grade3-reading/_archive/2026-08-13-consolidation/apush-corpus-hardening-20260731-tip.tar.gz` (apush/docs/UNIT-SPECS.md inside it) (5): “This file records the earlier plan-review and Unit 1 phase. It is not an active review request, build instruction, or submission contract.”

Against: The specification is marked historical and superseded as a build instruction (UNIT-SPECS.md line 5), and the course's design documents record no run of the check.

<sub>method · stage: review · stimulus, integrity, review · universal · from ap · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Relabel a hard word, keep the idea

Judge a technical term by whether learners can build its concept now, and where only the word is too hard, give it a plain label and keep the idea.

The grade-7 science script rules replace a banned-word list with one question asked of every term the central idea touches, whether a learner of the grade can build the concept right now, and scripts are drafted from the result (`grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-generation-v0.1.md`, lines 68 and 88). A term in reach, or load-bearing and teachable in plain words, is kept; one whose idea belongs but whose word is too technical is simplified by leading with a plain label and naming the precise term once; and a term is dropped only when it is both above grade and unnecessary to the central idea. Coverage wins over vocabulary: a load-bearing idea is never dropped because its usual word is hard.

Quoted:

- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-generation-v0.1.md` (68): “SIMPLIFY if the idea belongs but the word is too technical (lead with a plain label, name the precise term once); DROP only if above grade AND unnecessary to land the hinge. Coverage wins over vocabulary — never drop a load-bearing idea because its usual word is hard; relabel and keep the idea.”
- `grade3-reading/ti-courseplans/courses/g7-science/brainlifts/script-generation-v0.1.md` (88): “run KEEP/SIMPLIFY/DROP over every term the hinge touches; draft from the *result*, not the raw topic.”

Against: none found

<sub>method · stage: write · wording, alignment · universal · from g3 · adopted-rule · held · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### Source every factual claim

Back every real-world claim, and every non-fiction text, with a recorded, reputable source, and check each claim against that source, never against what sounds plausible.

The course content-integrity skill ranks sources for every external-world claim (an official agency, standards body, museum, university or primary research first, then a domain reference chosen for the course, then a named fallback) and records each one's title, publisher, URL, retrieval date, exact locator, bounded fact, scope boundary and content digest; search snippets, unsourced summaries, blogs and model memory cannot support a pass (`grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md`). The cross-subject guidance warns that a vivid but factually loose passage risks embedding misconceptions that are hard to undo (`grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd`), and the reading project requires reputable sources for every science-bearing object (`grade3-reading/knowledge_bot/HOTBUCKET.md`). The source is of the strongest kind available, and checking each claim against it is a check of its own.

Quoted:

- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md` (115): “official agency, standards body, museum, university, or primary research;”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md` (119-121): “Record source title, publisher, direct URL, retrieval date, exact locator, bounded fact, scope boundary, and content digest when bytes are available. Search snippets, unsourced summaries, blogs, and model memory cannot support `PASS`.”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md` (11-12): “use sources rather than model memory as authority, and never turn missing evidence into `PASS`.”
- `grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd` (40): “Nonfiction passages should be factually accurate and traceable to reputable sources. A vivid but factually loose passage creates downstream work for the subject team and risks embedding misconceptions that are hard to undo.”
- `grade3-reading/knowledge_bot/HOTBUCKET.md` (96): “every science-bearing Read/Write object must use reputable sources and pass”
- `grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd` (41): “CRITICAL — fabricated claim printed as textual fact.”
- `grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd` (76-77): “anything a lesson presents to the child as being IN the story must actually be in that lesson's own passage text”
- `grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd` (79): “the shape that hides the worst defects, since unquoted claims look like nothing”
- `grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd` (65-66): “merciless and stranger are the two teaching a flatly wrong rule on screen.”
- `grade3-reading/knowledge_bot/knowledge/kb-0141-cross-cutting-science-misconception-synthesis.qmd` (140): “Every model should carry an explicit health warning”
- `grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd` (73-74): “not referenced by `npm run check` or any other known gate”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md` (135-138): “test definitions for missing categories and qualifiers; - test ontology/category mistakes, unsupported mechanisms, causal overclaims, and contradictions; - flag teleology or conscious intent attributed to evolved traits or impersonal processes; - compare the claim with the frozen source boundary, not with what sounds plausible.”
- `grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md` (140-142): “Examples of blocking shapes include defining a broad category as only one subtype, calling a process a body part, treating an animal as a producer, or replacing a causal definition with "most connected."”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (267-269): “Anti-leak (kb-0064) means "you must read the passage to answer" — it does NOT mean the passage's own facts are sourced or true. A perfectly anti-leak item can sit on an unsourced machine-authored passage.”
- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md` (186): “**Note:** you grade **anti-leak + G5 compliance**, not source truth.”
- `downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md` (16): “Non-fiction passages should be factually accurate and traceable to reputable sources.”
- `downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx` (sheet 'Sources & Inspiration', cell D41): “AI-generated from general knowledge”
- `downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx` (sheet 'Sources & Inspiration', cell E41): “General botanical knowledge (photosynthesis, plant parts, life cycles)”
- `grade3-reading/_archive/2026-08-13-consolidation/codex-history-extract/HUMAN-g3r-2026-07-20T16-21-46-019f7fe7-80b5-7e61-bdfc-c5a7748f703b.md` (16): “- 8 disclosed science failures remain, plus additional errors verified against [USGS](https://www.usgs.gov/faqs/what-earths-water-cycle), [NOAA](https://www.nesdis.noaa.gov/about/k-12-education/atmosphere/what-the-coriolis-effect), and [NPS](https://www.nps.gov/yell/learn/nature/cyclesprocesses.htm).”

Against: The claim checker was not referenced by any known gate when it was found, so nothing enforced the rule.

<sub>method · stage: ground · stimulus, integrity, generation · universal · from g3 · adopted-rule · held · found in [2026-10-12-3-round-2](../research/2026-10-12-3-round-2/), [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### The stored text is the claimed work

Before a writer or learner sees a source, verify that its link opens the claimed work and that the stored text is that whole work run to its end. An audit found all 6 stored texts it checked cut at exactly 50,000 characters.

A spike report found that a pull list's identifiers for three famous speeches pointed to entirely different works in the library they named. A fetch audit found all 6 rows it checked truncated at exactly 50,000 characters, cutting 62%-96% of the primary-source content, with library preambles or scanning noise in three of them, and an earlier audit could verify none of 870 sourced rows, because their links reached blocked pages or landing pages rather than texts. In a source pack whose attributions were real, the text field held OCR of a modern museum tour transcript. Copy the text in by file rather than having a model retype it (`grade3-reading/ti-courseplans/skills/knowledge-ingest/SKILL.md`). The stored text must not be empty, a landing page, a metadata stub or a capped excerpt, and must be free of catalogue notes, library boilerplate and scanning noise.

Quoted:

- `icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-01T1314Z_u8_pd_status_spike_BOMBSHELL.md` (15): “**the Gutenberg IDs point to ENTIRELY DIFFERENT WORKS**”
- `icloud-work/aptraining/workspace/comms/_deprecated/outboxes/from_atlas/2026-05-01T0911Z_d13_u1_quality_audit_t3.md` (12): “**6 of 6 rows truncated at exactly 50,000 chars.** Real fulltext sizes: 50KB to 1.3MB. **Quill is capping at 50KB**, cutting **62%-96% of primary-source content**. Three rows have **library-copy preamble / OCR garbage in the first 5KB**”
- `icloud-work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md` (150): “### 2.4 D13 primary-source pipeline — 0/870 verified”
- `icloud-work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md` (156): “| LoC APUSH | 436 | **0** | Cloudflare 403 on `www.loc.gov/item/<id>/` |”
- `icloud-work/aptraining/workspace/comms/from_shadow/2026-04-30T1700Z_comprehensive_lessons_learned.md` (158): “| Gutenberg | 109 | **0** | `source_url` points to landing page, not fulltext |”
- `icloud-work/aptraining/workspace/comms/from_cheater/2026-05-29T1605Z_DBQ_realsource_smoke_FAIL_pack_content_issue_E2.md` (27-28): “But the `content` field is OCR text from a modern museum tour transcript”
- `icloud-work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md` (43): “**F-D13-13**: all 6 rows truncated at exactly 50,000 chars, losing 85-96% of fulltext. 5 of 6 rows reject (Spanish library preamble, BYU bookplate, Newberry Library + Latin OCR garbage, PG header pollution).”
- `icloud-work/aptraining/helpers/shadow/SHADOW_HANDOFF.md` (36): “D13 pipeline broken (322/761 LoC URLs Cloudflare-blocked, 109/109 Gutenberg URLs are landing pages).”
- `icloud-work/aptraining/helpers/data/output/d13_corpus_v5_inventory.md` (28): “- v3 has 648 docs: **92 fulltext + 556 metadata_only** (LoC frequently has metadata but not transcribed fulltext for newer/obscure items)”
- `ti-courseplans-audit/docs/reading-science/EXTRACTION_EVIDENCE.qmd` (39): “(does each extraction reach the document's true end?)”
- `ti-courseplans-audit/docs/reading-science/EXTRACTION_EVIDENCE.qmd` (50): “the full texts here were never re-typed through a model.”
- `ti-courseplans-audit/skills/knowledge-ingest/SKILL.md` (41-42): “a scanned PDF yielding whitespace is `skipped: needs-manual-export`, never ingested empty.”
- `grade3-reading/ti-courseplans/skills/knowledge-ingest/SKILL.md` (68): “a source is largely copyrighted prose (the model re-emitting the full text trips it).”
- `grade3-reading/ti-courseplans/skills/knowledge-ingest/SKILL.md` (71): “never re-type source text through a model.”
- `grade3-reading/ui-audit-2026-09-08/WORKFLOW.md` (111): “A matching line count and HTTP200 can still deliver the wrong book.”
- `grade3-reading/ui-audit-2026-09-08/bead-specs/workflow.md` (3): “verify source work/edition/ranges/anchors/hash instead of line counts alone.”

Against: The 870 rows were unverifiable, not shown to be wrong: their links reached blocked pages or landing pages. A content hash shows a stored text is unchanged, not that it is whole: one handover counted 8 hashed documents as needing no re-fetch (icloud-work/aptraining/handover/2026-05-01T1039Z_data_session/HANDOVER.md, line 275).

<sub>method · stage: ground · stimulus, integrity · universal · from ap, g3 · measured · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### File a source by when it was made

File each primary source under the period in which it was made, not the period it mentions, and check every period label against the source's date in code. A tagger that filed by topic put 76 of 96 documents in one unit's cluster outside that unit's period.

A source-ingest audit found 79% of one unit's 96-row topic cluster tagged to the wrong era, 76 dated outside 1800-1860 and mostly 1904 exposition commemoratives, because the era tagger worked by topic association rather than date of creation. A later re-audit by date found the 211 gross mismatches quarantined and 23 subject-level mismatches still in place. It holds wherever dated primary sources stand in for their period, as in the AP history courses.

Quoted:

- `icloud-work/aptraining/handover/2026-05-01T1039Z_atlas_session/HANDOVER.md` (39): “U4 LoC 96-row topic cluster. **79% era-mistag** (76/96 dates outside 1800-1860, mostly 1904 Louisiana Purchase Expo commemoratives). **F-D13-12** = era-tagger doing semantic-association not date-of-creation.”
- `icloud-work/aptraining/helpers/shadow/output/2026-05-22T2308Z_v93_phase3_reaudit_VERDICT_ADJUST.md` (28): “- **0 gross anachronisms** (>50-year mismatch) — the 211 gross violations were successfully quarantined.”
- `icloud-work/aptraining/helpers/shadow/output/2026-05-22T2308Z_v93_phase3_reaudit_VERDICT_ADJUST.md` (29): “- **23 subject-level anachronisms** remain (±20-year or subject-obvious mismatches).”

Against: The same re-audit kept later commemorative documents under the era they are about, as date-mismatched but subject-correct (icloud-work/aptraining/helpers/shadow/output/2026-05-22T2308Z_v93_phase3_reaudit_VERDICT_ADJUST.md, line 42).

<sub>method · stage: ground · stimulus, alignment · universal · from ap · measured · contested · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/)</sub>

### Gate reading level only on your texts

Gate a reading-level band only on texts you wrote; on published texts you chose, measure and report it, since they are not yours to rewrite to a number.

A reading engine's rule pack gives its reading-level band two uses, measuring any passage and gating one only when the course wrote it, after an earlier generator spent whole refine budgets enforcing a Lexile target on folktales that were never going to reach it. Its copy rules exempt story prose from the 25-word sentence ceiling for the same reason, since editing a narrative sentence down to hit a number is the Lexile-driven editing its knowledge rules forbid. It matches the rule that a lesson changes to fit its fixed source text, never the reverse (fix-the-lesson-never-the-source).

Quoted:

- `grade3-reading/course-renderer/authoring/inputs/rule-packs/reading-g3.json` (39): “A band for MEASURING a passage, and for gating one only when we wrote it. gen_v3 spent whole refine budgets enforcing a Lexile target on folktales that were never going to reach it; a published text the academics team chose is not ours to rewrite to a number.”
- `grade3-reading/course-renderer/docs/rules/content-and-copy.md` (74-76): “**Story prose.** Literature at grades 4 to 6 runs longer than anything else a child reads. Editing a narrative sentence down to hit a number is exactly the Lexile-driven editing R-KC-6 forbids.”

Against: A crosswalk for adopting a partner's texts took the other line after finding that they averaged Flesch-Kincaid grade 9.7: "Every prose text we adopted therefore carries a logged commitment: re-leveled to the Grade-4 band before authoring, with the original kept as the source." (`grade3-reading/course-renderer/docs/extras/g4-crosswalk-2026-08-17.md`, line 82). The record text-within-the-grades-reading-band also asks that every passage sit within or just above its grade's band.

<sub>method · stage: settle · stimulus, measurement, wording · universal · from g3 · adopted-rule · contested · found in [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>

### A readability score is not difficulty

A readability score is not a text's difficulty: judge difficulty from the exact excerpt students read, by reading it as well as by formula.

The staged assessment standard flags a readability score as a secondary proxy, not item difficulty itself (`grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md`). The project's reading-science summary holds that text difficulty is a match among the text, the reader's knowledge and the task, so no single readability number can gate a text (`grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd`). Its digest of a national reading study records that readability estimates disagree with one another and give no diagnostic information for individualizing instruction (`grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd`; RAND Reading Study Group 2002, https://www.rand.org/pubs/monograph_reports/MR1465.html). Weigh the new knowledge the excerpt carries, the reader's knowledge and the task. Rate decoding and understanding separately, gate no text on one number, and never swap out the words that carry its knowledge to lower a score.

Quoted:

- `grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md` (97-98): “Lexile is a readability proxy, **not** item difficulty itself — flag it `[SECONDARY]`.”
- `grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd` (48): “Text difficulty is a match among text factors, reader knowledge, and task — no single readability number can gate a text”
- `grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd` (705): “different readability estimates don't agree with each other and provide no diagnostic information for individualizing instruction.”
- `grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md` (18): “measures lexically simpler than the primer (FK 3.5) because its sentences are short; its”
- `grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md` (19): “step up is carried by conceptual load (five new knowledge ids, two taught terms) and by”
- `grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md` (20): “denser stated/implied layering, which the FK heuristic does not see.”
- `grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md` (44): “REVISE cannot swap payload words out”
- `grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md` (46): “FLAG -> SCAFFOLD: vocabulary_support pre-teach for "erosion" and "gorge" (pronunciation + meaning) before the reading dose”
- `grade3-reading/artifacts/g5-course/pd-texts/winnie-the-pooh-onepager.md` (28): “Chapter range FK 4.84 (ch VI) to”
- `grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md` (53): “Choose texts for a coherent knowledge sequence and a genre balance that includes poetry, drama and more literary work, and judge complexity qualitatively as well as by Lexile.”
- `grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd` (107-108): “For these readers, texts with high coherence consistently produced higher performance scores than texts with low coherence.”
- `grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd` (109-110): “A coherent text base slightly enhanced recall, but actually lowered performance on tests that tapped the mental model.”
- `grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md` (114-115): “7. Text difficulty is a match among text factors, reader knowledge, and task — no single readability number can gate a text”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/strategy-text-fit.md` (13): “but also the comprehension demands of the text how hard is it to understand this text these two things are not always aligned”
- `grade3-reading/artifacts/u4l2-build/g5-audit/P2-RULESET.md` (58): “Word-reading demand and comprehension demand are rated separately ('not always aligned'); a text can be easy to decode and hard to understand.”
- `grade3-reading/artifacts/u4l2-build/g5-audit/G5-BAR.md` (77-78): “G5 complexity in this lesson is NOT long sentences. The FK 4.23 is deliberate — the text reads easy so the *task* can be hard.”
- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/QUALITY-UPDATE-2026-07.md` (18-19): “poetry deliberately excluded since Lexile is unreliable for verse”
- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/LENGTH-RATIONALE.md` (15): “| U6–U7 | ~600–750 | a story needs room; poems exempt |”
- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/QUALITY-UPDATE-2026-07.md` (39-40): “The A3/Lexile figures use InceptBench's wordfreq estimator, which runs ~85L lower than an FK-based proxy; neither is real MetaMetrics Lexile.”
- `grade3-reading/ti-courseplans/courses/g4-reading/showcase-lessons/docs/QUALITY-UPDATE-2026-07.md` (40-41): “Treat as directional, confirm with a MetaMetrics tool before any external Lexile claim.”
- `grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/dimensions/D8-text-quality.md` (30): “Word-reading demand and comprehension demand are rated separately ('not always aligned'); a text can be easy to decode and hard to understand”
- `grade3-reading/edullm-review-hub/course-packages/courses/g5-reading/review/evidence/validation/full-course-validation.json` (215): “Passage cleared machine rejection but carries specialist flags: FK=2.83 (target 3.5-6.5)”
- `grade3-reading/ti-courseplans/docs/reading-science/DIGEST-rand-mr1465-2002.qmd` (329): “texts are not difficult or easy in and of themselves, but they become difficult or easy at the interface with readers and the purpose of the activity”
- `incept-package-hub/course-packages/courses/g5-reading/review/evidence/case-for-review.md` (127): “No official Lexile-certified build target is licensed, and text difficulty depends on reader, text, and task.”
- `grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/01_PSYCHOMETRIC_DESIGN.md` (279): “The uncertainty in b_provisional is estimated at σ ≈ 0.5–1.0 logits (5–10 RIT) based on the typical discrepancy between Lexile-derived difficulty estimates and empirically calibrated Rasch b values [AUTHORING-DECISION; DERIVED from literature on Lexile→IRT mapping].”

Published: [RAND Reading Study Group 2002](https://www.rand.org/pubs/monograph_reports/MR1465.html) · [What Works Clearinghouse video, Select texts purposefully to support comprehension development](https://www.youtube.com/watch?v=V4atucROaSQ)

Against: The measure is a heuristic: the notes call the FK-to-band reading "a judgment call, not a psychometric fact" and say the bands are not to be reused as policy (the same file, lines 4 and 15). For that same book, a documented whole-book Lexile measure was kept as the better evidence of its band, ahead of the formula's own figures (`grade3-reading/artifacts/g5-course/pd-texts/winnie-the-pooh-onepager.md`, line 27).

<sub>context · stimulus, measurement, demand · universal · from g3, research · adopted-rule · held · found in [2026-10-12-4-deep-sweep](../research/2026-10-12-4-deep-sweep/), [2026-10-12-5-full-crawl](../research/2026-10-12-5-full-crawl/)</sub>
