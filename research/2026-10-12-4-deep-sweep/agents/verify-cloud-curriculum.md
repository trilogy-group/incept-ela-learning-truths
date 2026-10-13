# verify:cloud-curriculum

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "cloud-curriculum",
 "verified": [
  {
   "index": 0,
   "verdict": "keep",
   "reason": "All three quotes verbatim at the cited lines: Plants design line 10; walkthrough v2.1 line 36; consensus workbook V7.0 Executive Summary A75, where a review of a knowledge-item pilot balanced MCQ lengths. The built lesson also padded distractors so the key is never the longest (walkthrough v1 line 69). This is standard item-writing discipline. It is not a duplicate of 8, which covers only the key's position.",
   "statement": "Write multiple-choice options of equal length and register, never let the key be the longest, give at least four plausible options, and avoid yes/no items and options that echo the stem.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "10 (textutil text)",
     "quote": "Rule 2 — Multiple-choice discipline. The correct option rotates across A/B/C/D; all four options are the same length and register; each item carries one deliberate misconception distractor.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "36",
     "quote": "≥4 plausible options; no yes/no; no stem echo; key never the longest | Guessable items measure test-wiseness, not comprehension",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'V7.0 Executive Summary', cell A75",
     "quote": "Two fixes applied: em-dashes removed, MCQ lengths balanced.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep",
   "reason": "Quotes verbatim. Cross-Cutting Synthesis line 248 also names forced choice between the right answer and the most common misconception as the gold standard. Chemistry card line 240 is the card's AP exam-relevance note, a second-hand claim about the exam setter with no citation. Walkthrough v1 line 67 also verified. The against's scope holds but is not universal: the Plants design gives its quick reading checks a misconception distractor too (line 84).",
   "statement": "Build at least one distractor in each knowledge item from a known misconception, because a student who can state the right definition may still choose the misconception when it is offered.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "248 (textutil text)",
     "quote": "Assessment items should include distractors based on known misconceptions. A student who can state the correct definition but selects the misconception when presented as a plausible alternative does not truly hold the correct understanding.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "240 (textutil text)",
     "quote": "The College Board explicitly designs multiple-choice distractors around the \"bond breaking releases energy\" misconception and the teleological \"atoms want full shells\" reasoning.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "67",
     "quote": "Each distractor is a coded misconception (a happy place, a cheerful place, a cozy-ordinary thing) and its feedback names the mismatch",
     "verbatim": true
    }
   ],
   "against": "Quick are-you-reading checks are kept free of trick distractors: \"4 short plausible options, one stated in the text, no trick distractors.\" (3.1 - 3. Aladdin ... Part 3 design, line 97), so the rule is for knowledge items, not attention checks.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep",
   "reason": "Quotes verbatim: lesson-components spec line 20 (the summary gap-fill), Plants design line 141 (the why-wrong distractor) and walkthrough v1 line 151 (the retell). The statement is general distractor design and is not on the list.",
   "statement": "Include distractors that are true elsewhere in the text, or were true earlier, but do not answer this question, so the item tests relevance and tracking rather than spotting a falsehood.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
     "lines": "20 (textutil text)",
     "quote": "The taught word features in it, and “true-earlier-but-not-now” distractors test that the child tracked how things changed.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "141 (textutil text)",
     "quote": "a true fact, but not the job of a part.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "151",
     "quote": "Distractors are true-of-the-story-but-wrong-here, which is what separates a retrieval task from a guessing game.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep",
   "reason": "Quotes verbatim: walkthrough v2.1 line 46 and v1 line 337. Line 149 of v1 describes the maze mechanic: each trio comes from the same category, so the sentence stays grammatical whichever choice is picked and only meaning decides. The statement is general.",
   "statement": "In a gap-fill, draw every choice for a gap from the same category, so grammar or elimination cannot decide it and only understanding can.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "46",
     "quote": "Cloze retell; each gap opens exactly 3 same-category choices | Same-category trios kill syntax and elimination guessing — only the story model decides",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "337",
     "quote": "A cloze earns its keep when context genuinely forces the selection",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep",
   "reason": "Quotes verbatim: Aladdin Part 1 line 338 and Aladdin Part 2 line 179. This is truth 6 applied to true/false and sorting sets. It is kept because it adds the designs' sweep evidence and the point that a statement the text never mentions is not settled by the text. Part 1 marks each 'Not true' item with the text that contradicts it (lines 292 and 301).",
   "statement": "Make every false statement in a true/false or sorting task one the text directly shows to be false, not merely one the text does not mention.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
     "lines": "338 (textutil text)",
     "quote": "Each Refine step has exactly 6 statements, 4 true and 2 incorrect; the incorrect ones are falsifiable directly from the text.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "179 (textutil text)",
     "quote": "Note: the don't-fit words are exactly the things Aladdin does NOT ask for, which is what the text points out.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "6",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep",
   "reason": "Quotes verbatim: Aladdin Part 2 lines 354 and 217. Line 354 adds 'Neither reason is written out; both are inferred.' The second clause follows the designs' own split between INFER and FIND, where 'the answer is stated in the sentence just read' (line 89). Related to 5 but not a duplicate.",
   "statement": "For an inference question, the answer must be supported by the text but not written in it; if the text states the answer, the item only tests locating.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "354 (textutil text)",
     "quote": "Both answers supported by the text, not stated.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "217 (textutil text)",
     "quote": "spotted that the writer never tells us why. We work it out from the words Aladdin says and does.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep",
   "reason": "Quotes verbatim: Aladdin Part 2 line 350, walkthrough v1 line 261 and Plants line 189. Adds a rule about answer slots alongside 17 (exact quotation). Not a duplicate.",
   "statement": "Keep quoted evidence and the student's inference in separate slots: the quote slot holds only the text's exact words, and inference words never go inside it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "350 (textutil text)",
     "quote": "Inference words (safe, desperate, ambitious, determined) live only in the \"I know…\" / \"So I think…\" steps, never in \"The text says…\".",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "261",
     "quote": "the text’s words go inside quotation marks, and the mood word can never hide there — the inference has to be produced, not retrieved.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "189 (textutil text)",
     "quote": "Any inference sits in State/Refine/Extra thinking, never inside a \"the text says\" quote.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (Standard components D2 and E3); D3, the paired paraphrase component, is added. 'Needs understanding' overstated the failure note, which is about synonyms and rephrasing (its knowledge link is Vocabulary). The fix says the paraphrased question needs the student to match meaning rather than words.",
   "statement": "Decide on purpose whether a question repeats the text's wording or paraphrases it: a student who matches words can answer a mirrored question, while a paraphrased one needs them to match meaning.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
     "lines": "sheet 'Standard components', cell D2",
     "quote": "Find explicitly stated information when the question uses similar wording to the text",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
     "lines": "sheet 'Standard components', cell D3",
     "quote": "Find explicitly stated information when the question paraphrases or uses different words",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
     "lines": "sheet 'Standard components', cell E3",
     "quote": "Child can only find answers when the question words exactly match the text. Fails when synonyms or rephrasing are used.",
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
   "reason": "Quotes verbatim: walkthrough v1 line 241 and Aladdin Part 2 line 133 (the target-word mark is at line 134). The statement is general.",
   "statement": "Teach reading the question as a step of its own, marking the word that says what to do and the word that names the target, and build that step's wrong options from the usual misreadings.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "241",
     "quote": "Reading the question is a taught step, not a formality — the distractors are the exact ways a grade-3 reader misreads a question (answers the previous question; grabs a familiar name; answers about the wrong place).",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "133 (textutil text)",
     "quote": "PROCESS word: circle \"Why\" -> draw a line -> label \"Which words?\" (we hunt for the writer's actual words as evidence).",
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
   "verdict": "keep",
   "reason": "Quotes verbatim: Aladdin Part 2 lines 282-283, the independent KNOW step. The purpose of catching a student who copies the model is inferred. It follows from line 283 ('Here Aladdin is reaching for something new') and from the feedback that names the difference.",
   "statement": "In the independent task, use the worked example's answers as distractors, so a student who copies the model instead of reading the new section is caught.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "283 (textutil text)",
     "quote": "Note: the don't-fit words are the cave reasons from the Modelling Moment. Here Aladdin is reaching for something new.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "282 (textutil text)",
     "quote": "\"Getting home was why Aladdin acted in the cave. Is that what he is reaching for now that he wants to marry the princess?\"",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep",
   "reason": "Quotes verbatim: Animal Kingdom design lines 205 and 161. The trap cards (whale, jellyfish, bat) are at lines 157, 186 and 187. The statement is general.",
   "statement": "When students classify, include trap cases whose surface appearance points to the wrong group, so they must apply the deciding rule.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 3. The Animal Kingdom - SORT - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "205 (textutil text)",
     "quote": "The trap animals (whale, jellyfish, bat) force the child to apply the rule over appearance.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 3. The Animal Kingdom - SORT - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "161 (textutil text)",
     "quote": "Step 5 — Extra thinking (the trap beat): appearance can fool you.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep",
   "reason": "Quotes verbatim: Rainforests design line 221 (the first WEIGH lesson) and Whose World design line 217 (the second, modelled step only). The statement is general.",
   "statement": "When students first meet a distinction, use only clear-cut cases that carry a visible marker, and keep borderline cases for later.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 2. Should We Save the Rainforests - WEIGH - Lesson Design.docx",
     "lines": "221 (textutil text)",
     "quote": "each sentence sorted as OPINION carries a feeling-word (\"I feel,\" \"amazes me,\" \"I am worried,\" \"I believe\"). No borderline cases are used at first exposure.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 8. Whose World Is It - WEIGH - Lesson Design.docx",
     "lines": "217 (textutil text)",
     "quote": "No borderline cases are used in the modelled step.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep",
   "reason": "Quotes verbatim: Aladdin Part 2 lines 146 and 159, with separate feedback for each label at lines 161-163, and Standard components E7, the failure note for RL.3.1.f. The statement is general.",
   "statement": "Sort a student's evidence picks into the key clue, a relevant but weaker clue and an irrelevant one, give each its own feedback, and then ask which clue is strongest.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "146 (textutil text)",
     "quote": "Each phrase is labelled CLUE / INTERESTING / DISTRACTOR.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "159 (textutil text)",
     "quote": "\"Some evidence is better than others. Tap what you think best describes what Aladdin wants.\"",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
     "lines": "sheet 'Standard components', cell E7",
     "quote": "Child picks a random, interesting, or nearby detail instead of the one that is relevant to the question.",
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
   "reason": "Quotes verbatim: BrainLift intro video lines 339, 329, 430 and 493, repeated in the file's second copy at 586, 576, 677 and 740. The first half was already truth 48 ('a first-try answer shows the moment'). The fix leads with how to design retrieval practice, which 48 does not state. The source names its studies without DOI (Roediger and Karpicke 2006; Cepeda et al. 2006).",
   "statement": "Make retrieval practice ask about something taught earlier, after a gap, such as a question on the last lesson before new teaching; a check straight after teaching shows only that the student was following.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "339",
     "quote": "Real retrieval needs a gap the child fills.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "329",
     "quote": "That is real retrieval, because the child has to produce the answer across a gap of days. The sync check after a video is not.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "430",
     "quote": "The sync check after a video is a check on attention, not on memory.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "493",
     "quote": "retrieving strengthens retention more than re-reading.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim. Physics card line 125 is its AP exam-relevance note, an uncited assertion about the free-response format. WF brainlift line 30 comes from a PreK to Grade 2 source. The claim holds beyond both.",
   "statement": "Ask students to explain their reasoning as well as give an answer, because explanation exposes misconceptions that answer-only items let through.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx",
     "lines": "125 (textutil text)",
     "quote": "The free-response format specifically exposes conceptual misconceptions because students must explain their reasoning, not just calculate.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "30",
     "quote": "If a child never has to compose or explain an answer, the app cannot tell whether the child understood",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep-with-fix",
   "reason": "Quotes and numbers verbatim: WF brainlift lines 113, 119 and 23, with the DOI at line 199. The rates are 'commonly cited targets' from a 1987 practitioner source that the file knows only second-hand. Lines 120-121 give only 4 to 6 for new material and 'higher rates for review'. The fix therefore no longer presents the figures as the rate a type allows.",
   "statement": "Pick the response type a skill needs (recognise, complete or produce) before counting responses, and accept the rate that type allows instead of chasing a high count; the commonly cited targets are about 4 to 6 responses a minute for new material, 8 to 12 for review, and 1 or fewer for open answers.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "113",
     "quote": "The rule of thumb is to pick the type the skill actually requires, then accept the rate that type allows rather than chasing a high count.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "119",
     "quote": "The commonly cited targets are about four to six responses per minute when a child is learning something new, about eight to twelve per minute when practicing material already taught, and about one per minute or fewer for open responses that require composing or reasoning.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "23",
     "quote": "A high number of responses per minute is not evidence of quality if the app reached that number by asking only recognition questions.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "199",
     "quote": "https://doi.org/10.1353/etc.2015.0009",
     "verbatim": true
    }
   ],
   "against": "The targets are second-hand: \"Council for Exceptional Children (1987), as cited in MacSuga-Gage and Simonsen (2015).\" (same file, line 120); the source is written for a PreK to Grade 2 comprehension app (line 6).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim: WF brainlift lines 71, 87 and 18; the Shute 2008 DOI at line 204 is verified. The source calls such a reply 'not a third turn' and 'not a real response', not 'not feedback', so the wording is fixed. The source is about open answers in K-2 comprehension talk. The built lesson applies the same idea to choice questions, where each wrong option's feedback names its own mismatch (walkthrough v1 line 67).",
   "statement": "Make the reply to a student's answer depend on what the student said; a reply that would read the same whatever the answer is not a real response and should be rebuilt.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "71",
     "quote": "A reply that would read the same no matter what the child answered is not a third turn.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "87",
     "quote": "If the reply would be the same no matter what the child said, it is not a real response and should be rebuilt.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "18",
     "quote": "Most instruction, and most software, stops after the child answers and offers only a confirmation such as “good” before moving on, which is the weakest use of the moment (Shute, 2008).",
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
   "reason": "Quotes verbatim: WF brainlift line 90 (Zucker et al. 2020, DOI at line 209 verified) and walkthrough v2.1 line 47. The original stepped support down for every answer short of full. The source's table holds level on a correct but brief answer (line 99), so the statement is fixed. Also gives an answer to open question 55 for the silent child.",
   "statement": "Plan the follow-up for each kind of answer in advance (full, brief, partly right, off track, silent): challenge a full answer further, hold level on a brief one, and step support down for the others.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "90",
     "quote": "When a child answers easily, scaffold up by challenging for reasoning, alternatives, generalizing, or extending. When a child struggles, scaffold down by giving feedback, reframing, supplying an answer, offering a model to mimic, or simply keeping the child engaged (Zucker et al., 2020).",
     "verbatim": true
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "99",
     "quote": "Correct but brief: “She lost her mitten.” | Level",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "47",
     "quote": "Open answers route to full / brief / partial / off-track / silent paths | Every path teaches; the silent child is taught first, then re-asked easier",
     "verbatim": true
    }
   ],
   "against": "The research table plans the kinds of move in advance but composes the words in the moment: \"Decide the follow-up rule in advance, but compose the follow-up in the moment.\" (WF brainlift, line 86); the built lesson wrote every branch in advance (walkthrough v2.1, line 47).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep",
   "reason": "Quotes verbatim: walkthrough v1 line 311 and WF brainlift line 100, the 'partly right' row of its scaffold table. Refines 1 without duplicating it.",
   "statement": "When an answer is partly right, say which part is right and ask only for the missing part.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "311",
     "quote": "Feedback on a half-answer names the part the child *did* give and asks only for the missing one.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "100",
     "quote": "“The snow is part of it. Look at her hands in the picture. What is missing?”",
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
   "reason": "Quotes verbatim: WF brainlift lines 70 and 167; the Lyster and Saito 2010 DOI at line 198 is verified. The source's own limit (line 168) belongs in the statement, so it was added to the statement and the evidence.",
   "statement": "When a point must be learned exactly, prompt the student to produce it rather than restating it for them, because students often miss a restatement; the evidence comes from second-language classrooms.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "70",
     "quote": "because children often do not notice a recast, it does not reliably teach one specific point (Lyster & Saito, 2010). When something has to be learned exactly, prompting the child to say it again in their own words works better.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "167",
     "quote": "Prompts more often lead the child to produce a corrected response.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "168",
     "quote": "Drawn from second-language classrooms, so applied here by analogy to early oral language.",
     "verbatim": true
    }
   ],
   "against": "\"Drawn from second-language classrooms, so applied here by analogy to early oral language.\" (same file, line 168).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep",
   "reason": "Quotes verbatim: Aladdin Part 2 lines 311 and 313. The same ladder reveals the full words on the third fail (line 316), which is already listed as a counter to 4.",
   "statement": "Advance a hint ladder only when the answer has changed since the last try, so resubmitting the same answer cannot unlock more help.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "311 (textutil text)",
     "quote": "FEEDBACK LADDER (only advances if the answer changed since the last try):",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "313 (textutil text)",
     "quote": "Empty / unchanged: \"Have another go at your answer first, then tap I'm done again.\"",
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
   "reason": "Quotes verbatim: lesson-components spec line 20; Aladdin Part 1 line 44, where Form 2 follows a retried Form 1 (line 42); walkthrough v1 line 67. The against is verified (v1 line 155). Related to 48 (a later test on new items), but this is the version that runs inside the lesson.",
   "statement": "After a practice item with retries, measure on a fresh parallel item: the first form teaches, the second shows whether the correction took.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
     "lines": "20 (textutil text)",
     "quote": "Runs as two parallel forms; the second is shown if the first is wrong.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
     "lines": "44 (textutil text)",
     "quote": "FORM 2 (second chance / clean measure)",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "67",
     "quote": "form 1 corrects, form 2 gives a cleaner read on whether the correction took.",
     "verbatim": true
    }
   ],
   "against": "The platform could not always deliver it: \"The doc’s FORM 2 has no renderer slot — the retry ladder substitutes (accepted deviation, logged).\" (WITW walkthrough v1, line 155).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep",
   "reason": "Quotes verbatim: walkthrough v2.1 lines 33 and 50. Walkthrough v1 lines 251 and 353 say the same. The statement is general.",
   "statement": "When help or the answer is given after held tries, label it as help, and have the end screen claim completion, never mastery.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "33",
     "quote": "After held tries, help is offered and named as help | A reveal dressed as a win teaches that trying is optional",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "50",
     "quote": "The end screen claims completion, never mastery | False mastery claims teach children and parents to distrust the product",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "keep",
   "reason": "Quote verbatim: walkthrough v1 line 271; line 269 adds that 'any sensible rule earns full credit with no further ask'. One source, a standing feedback ruling.",
   "statement": "Score a stretch question that asks for thinking beyond the first answer generously, so going further is never punished.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "271",
     "quote": "Scoring is deliberately generous: this beat rewards thinking beyond the first answer; it must never punish it.",
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
   "reason": "Quotes verbatim: walkthrough v1 lines 303 and 305. Sits beside 13, which accepts an unplanned right answer only when the judge is sure. This rule judges coherence rather than whether the example is recognised, and it does not say how sure the judge must be.",
   "statement": "When students may bring their own example, judge whether it holds together rather than whether it matches the planned examples, and give credit for noticing differences.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "303",
     "quote": "the rubric judges whether the answer holds together, never whether we recognize the story",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "305",
     "quote": "the rubric rewards noticing differences above matching our list.",
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
   "reason": "Quotes verbatim: walkthrough v1 line 285, where the ask is word plus evidence so 'a bare echo of the definition does not pass', and v2.1 line 19. The rule is necessary, not sufficient: the same walkthrough says lasting ownership is a later question (v1 line 353).",
   "statement": "Count a taught word as owned only when the student uses it, with evidence, about new content; recognising it or echoing its definition does not count.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "285",
     "quote": "Vocabulary is only owned when it is produced about new content",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "19",
     "quote": "Recognition can be guessed; production shows the word or idea is owned",
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
   "verdict": "keep",
   "reason": "Quote verbatim: walkthrough v2.1 line 32. The against is real and sharper than it looks. Both walkthroughs are dated the same day and come from the same build, and v1's page-one feedback points ahead in the text (line 123). So the parameter v2.1 lists as checked was not fully met.",
   "statement": "Feedback must never reveal or point to parts of the text the student has not read yet.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "32",
     "quote": "Glossed words and sync-checked answers are never re-asked; no unread content in feedback | Spoilers turn reading into confirmation; re-asking stamps burns trust",
     "verbatim": true
    }
   ],
   "against": "The earlier walkthrough quotes a page-one wrong-answer reply that points ahead in the text: (“the river comes later, at the end of his wander…”) (WITW walkthrough v1, line 123).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep",
   "reason": "Quotes verbatim: walkthrough v1 line 127 and v2.1 line 30. Adds length and placement to truth 1, which covers what feedback says.",
   "statement": "Keep corrective feedback short (40 words or fewer), tied to the evidence, and placed directly under the option the student chose.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "127",
     "quote": "The feedback register is the corrective-feedback bar: ≤40 words, evidence-anchored, teaches without revealing.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "30",
     "quote": "Wrong-answer feedback lands directly under the option tapped | The correction attaches to the exact act, not to the screen in general",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep",
   "reason": "Quotes verbatim: Wind in the Willows Part 3 line 85, Aladdin Part 2 line 89 and walkthrough v2.1 line 41. Refines 7.",
   "statement": "Place quick are-you-reading checks at moments of change, keep them literal and answerable in about two seconds from the sentence just read, and give four short options that all look plausible to a drifting reader.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 10. The Wind in the Willows, Part 3 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "85 (textutil text)",
     "quote": "Pure literal retrieval, answered in about 2 seconds, placed at moments of CHANGE.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "89 (textutil text)",
     "quote": "Four short options, all plausible to a drifting child, only one stated in the text.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "41",
     "quote": "Drifting readers lose the thread at changes; look-back must be actually possible",
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
   "verdict": "keep",
   "reason": "Quotes verbatim: walkthrough v1 lines 125 and 13 and v2.1 line 40. The statement is general and complements 7.",
   "statement": "Keep questions off the screen while students read, bring the check in only after the reading stretch, and keep the text visible whenever a question asks them to look back.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "125",
     "quote": "your “we’ve overdone questions to the detriment of the mental model” note is why the question waits off-screen.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "40",
     "quote": "Story-only pages; the check appears only after “I’m done reading” | Reading needs stretches that are just reading; questions wait off-screen",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "13",
     "quote": "and the passage always visible whenever a question asks the child to look back at it.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 30,
   "verdict": "keep-with-fix",
   "reason": "Numbers verbatim: 38, about 31 and 55 (walkthrough v1 line 14; v2.1 lines 35 and 586). 'Hold them to a budget' overstated the evidence, because the ruling kept 38 answer moments against a target of about 31. The fix says the count was tracked and the overage recorded.",
   "statement": "Count the answer moments in each lesson and track them against a target, since checks that interrupt every paragraph become compliance; a rebuilt lesson carried 38 against a target of about 31, and the overage was recorded rather than cut cosmetically.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "14",
     "quote": "The lesson carries 38 discrete answer moments — in line with its unit neighbours and far below the 55-ask lessons your earlier review flagged.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "35",
     "quote": "38 discrete answer moments this lesson (target \\~31) | Checks that interrupt every paragraph become compliance theater",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "586",
     "quote": "L11–L14 ship a uniform 38 asks where per-part content varies (target \\~31).",
     "verbatim": true
    }
   ],
   "against": "The target itself was left open: \"Ruled: document, don’t cut cosmetically; revisit when canonical videos land.\" (walkthrough v2.1, line 586).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep",
   "reason": "Quotes verbatim: lesson-components spec lines 26 and 28 and walkthrough v1 line 207. The against is verified (v1 line 211). Refines 40.",
   "statement": "In a worked example, model every step except the final thinking move and let the student make that move with the modelled steps still visible.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
     "lines": "26 (textutil text)",
     "quote": "modelling every step except the final thinking move. It sounds like genuine thinking, not a lecture.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
     "lines": "28 (textutil text)",
     "quote": "The child completes the final step only — one typed gap that carries the inference (“…so I think ___”) — with the modelled steps kept visible beside it.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "207",
     "quote": "even in the I-do the last thinking move is the child’s, a small production that turns watching into doing",
     "verbatim": true
    }
   ],
   "against": "The per-lesson designs did the opposite: \"The design doc’s Modelling Moment ends with the full model answer typed to completion; we leave the last word to the child\" (WITW walkthrough v1, line 211).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 32,
   "verdict": "keep",
   "reason": "Quotes verbatim: walkthrough v1 line 197 and v2.1 line 16.",
   "statement": "Model the decision, not just the answer: show weaker options being weighed and rejected with reasons before the best one is chosen.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "197",
     "quote": "This is modelling the thinking, not the answer.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "16",
     "quote": "Scout weighs and rejects clues out loud | A model showing only the winning move teaches that reading is easy for other people",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 33,
   "verdict": "keep",
   "reason": "Quote verbatim (walkthrough v1 line 223) and the against verified (line 227). Refines 40.",
   "statement": "Make guided practice a partly done task the student finishes, not a hint and not a second demonstration.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "223",
     "quote": "A we-do is a partial the child completes — not a hint, and not a second demonstration.",
     "verbatim": true
    }
   ],
   "against": "The lesson designs had no guided stage at all: \"design docs go straight from Modelling Moment to Independent Task — they contain no we-do.\" (WITW walkthrough v1, line 227).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 34,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, but the cloze clause of Plants line 197 is stale: the gap-fill is now a whole-text summary (lines 121-128). It is replaced by line 130, which names the model and independent sections. Also added the walkthrough's guided station, set in a third place 'so it pre-answers neither the model nor the independent task' (v1 line 227).",
   "statement": "Run the worked example, guided practice and independent task on different sections or material, so no stage pre-answers another and the independent task is transfer rather than rehearsal.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
     "lines": "334 (textutil text)",
     "quote": "Same FIND rail, different section, fresh evidence.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "130 (textutil text)",
     "quote": "The teacher models the full FIND rail on the roots/stem/leaves section (the \"I do\"). Part 3 re-runs it independently on the seeds/flowers section.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "227",
     "quote": "so it pre-answers neither the model nor the independent task",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "34",
     "quote": "Repeating on the same evidence is rehearsal; new evidence is transfer",
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
   "verdict": "keep",
   "reason": "Quotes verbatim: lesson-components spec line 7, Aladdin Part 1 line 28 and curriculum map SC Coverage K3. Overlaps 41, which says to tell the writer what an earlier block covers, but adds that nothing may contradict the canonical piece.",
   "statement": "Once a component is canonical, nothing later may contradict it or re-ask its questions; keep an explicit off-limits list, and update the lessons when the canonical piece changes.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
     "lines": "7 (textutil text)",
     "quote": "The video is canonical: no later component may contradict it or re-ask its questions.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
     "lines": "28 (textutil text)",
     "quote": "Off-limits for re-asking: the two sync checks above; the sultan and magician stamped definitions; naming or ordering the story pattern in the abstract.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'SC Coverage', cell K3",
     "quote": "Extended 2 Jul 2026 to match the revised BG video, which tells the child Part 1 reaches the 'but'.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim: Aladdin Part 1 line 335 and BrainLift intro video lines 327 and 457; line 329 describes moving stated structure into retrieval questions. The source names Gurlitt and Renkl 2008 without DOI.",
   "statement": "Fade support in steps: highlight evidence in the worked example, withdraw it in the independent task, and across a unit replace restated structure with retrieval as students come to hold it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
     "lines": "335 (textutil text)",
     "quote": "The Modelling Moment guides (pre-glowed evidence, auto-highlighted Refine, teacher whiteboard); the Independent Task releases (unassisted hunt with feedback ladder, child-written 3-blank frame, judge-then-check Refine with retry ladder).",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "327",
     "quote": "The knowledge is permanent; the explaining is temporary.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "457",
     "quote": "This is the evidence base for fading: more structure early, less later (SPOV 8).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 37,
   "verdict": "keep-with-fix",
   "reason": "The Rainforests and Whose World quotes are verbatim and show the planned fade (line 8 of each). The Feathers and Scales quote is verbatim but points the other way: that lesson was built at full load with lightening optional ('easier to fade than to build up'). It moves to against.",
   "statement": "Make the first lesson on a new procedure lighter, with a smaller set, and build it so later lessons only widen the set instead of rebuilding the lesson.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 2. Should We Save the Rainforests - WEIGH - Lesson Design.docx",
     "lines": "8 (textutil text)",
     "quote": "This is the first WEIGH lesson in the unit, so the \"Find the opinions\" task is deliberately lightened: the child is shown a reduced set of three sentences (a mix of fact and opinion) rather than the whole text at once",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 2. Should We Save the Rainforests - WEIGH - Lesson Design.docx",
     "lines": "8 (textutil text)",
     "quote": "Everything below is written so that lightening later only means widening that set, not rebuilding the lesson.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 8. Whose World Is It - WEIGH - Lesson Design.docx",
     "lines": "8 (textutil text)",
     "quote": "This is the second WEIGH lesson in the unit (after Should We Save the Rainforests?), so the fade applies: the \"Find the opinions\" task is no longer reduced to three options — the child taps opinions straight from the whole section.",
     "verbatim": true
    }
   ],
   "against": "The first comparison lesson went the other way: \"Built here to the KB row as-is: the full compare (similarities and differences, then connect).\" with lightening left optional, \"(easier to fade than to build up)\" (Feathers and Scales design, line 8).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 38,
   "verdict": "keep",
   "reason": "Quotes verbatim: Fantasy Classics KB Overview B35 and Living World KB Overview B36. This is the first step of truth 40 (what students already know). Kept as added evidence from two unit knowledge bases.",
   "statement": "Open each lesson by having students recall the previous lesson's key idea, then thread it into the new one.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx",
     "lines": "sheet 'Overview', cell B35",
     "quote": "Each lesson opens by re-firing the previous part's key threshold, then threads it into the new one.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - The Living World - Complete KB.xlsx",
     "lines": "sheet 'Overview', cell B36",
     "quote": "Each lesson opens by recalling the prior part's knowledge, then threads it into the new threshold.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "40",
   "name_bearing_source": false
  },
  {
   "index": 39,
   "verdict": "keep",
   "reason": "Quotes verbatim: Fantasy Classics KB Overview A3 and B36 and walkthrough v1 line 345. The conformance finding is second-hand: the walkthrough reports a review's result.",
   "statement": "Give each lesson one key idea that the student restates with evidence at the close, and check built lessons for that closing statement: a conformance review found it missing from every lesson.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx",
     "lines": "sheet 'Overview', cell A3",
     "quote": "each lesson teaches ONE key threshold (in red) that the child should walk away knowing, with a second threshold carried subtly.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx",
     "lines": "sheet 'Overview', cell B36",
     "quote": "so each child leaves having restated the threshold with evidence.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "345",
     "quote": "your conformance review found it missing everywhere; it now lands in every lesson",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 40,
   "verdict": "keep",
   "reason": "Quotes verbatim: lesson-components spec line 11 and walkthrough v1 line 109.",
   "statement": "Before the first read, give one purpose for reading that points at the evidence the later task will use.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
     "lines": "11 (textutil text)",
     "quote": "One narrated sentence that focuses the child before the first read — the lesson's single watch-for.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "109",
     "quote": "Purpose-for-reading, set before the text and pointed at exactly the evidence the skill work will need.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 41,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, but 'keep it out of everything before the final task' contradicted the designs: the word is taught first, in the vocabulary component (Aladdin Part 1 lines 12 and 30, and the walkthrough's word card). The fix names the steps it is actually kept out of (line 336). Another design reserves a word that does occur in its text ('determined', Aladdin Part 2 line 15), so the reserving works either way.",
   "statement": "Choose a taught word that names something the text never names, teach it in the vocabulary step, keep it out of the video, the reading checks and the gap-fill, and require the student to produce it in the independent task.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
     "lines": "12 (textutil text)",
     "quote": "Vocabulary word (taught): betrayal / betrayed — the feeling when someone you trusted lets you down or tricks you. (Not in the text; encapsulating; reserved for the Independent Task.)",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
     "lines": "336 (textutil text)",
     "quote": "Betrayal / betrayed never appears in the video, the vocab-to-story bridge, the pauses, or the cloze bank; it is surfaced only in the Independent Task (Step 3 blank C and Step 5 help), where the child uses it to cash the answer.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "23",
     "quote": "*eerie* is deliberately absent from the passage | The child must produce the word to name a mood the writer never named",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 42,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The first half, defining a word in the sense the text uses it (lesson-components spec line 16), is already truth 18 ('each for its sense in its own line'). The fix keeps the new part: one identical definition everywhere, enforced by a validator.",
   "statement": "Give each taught word one definition, word for word the same on its card, in every glossary and in the wrap, and check that in code.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "79",
     "quote": "definition identical, word for word, on the card, in every passage glossary, and in the wrap — the one-definition rule from your reviews, enforced by a validator.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "37",
     "quote": "One definition per word, identical everywhere it appears | Definition drift makes the child re-learn the word each time",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 43,
   "verdict": "keep",
   "reason": "Quotes verbatim: BrainLift intro video line 338, coherence guidance line 14 and Cross-Cutting Synthesis line 31. The statement is general.",
   "statement": "Use the same words and framing for an idea every time it returns, in every subject, because loose wording in one place can re-teach a misconception another place fixed.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "338",
     "quote": "Always use the same vocabulary to talk about an idea already taught so as not to confuse.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md",
     "lines": "14",
     "quote": "the Read/Write lesson should be consistent with how it was framed in the subject app — vocabulary, level of nuance, framing.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "31 (textutil text)",
     "quote": "Even students who learned the correct chemistry are re-taught the misconception in biology class.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 44,
   "verdict": "keep",
   "reason": "Quotes and numbers verbatim: BrainLift intro video lines 428 and 487 (Beck and McKeown; Elleman et al. 2009; no DOI in the source) and walkthrough v2.1 line 22. Line 428 also says 'A word met once in a video is a first encounter, not the teaching of it.' Distinct from 18, which is about which words to teach.",
   "statement": "Plan around ten or more meaningful, spaced encounters with each word a student must own; one meeting is a first encounter, not teaching.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "428",
     "quote": "Around ten or more meaningful encounters are needed to own a word, and vocabulary gains appear far more strongly on custom measures than standardised ones.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "487",
     "quote": "vocabulary instruction helped comprehension on custom measures (d \\= 0.50) far more than on standardised ones (d \\= 0.10)",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "22",
     "quote": "Each word returns \\~10–12 times across the unit | One meeting never sticks; spaced returns in fresh contexts build ownership",
     "verbatim": true
    }
   ],
   "against": "Vocabulary gains carry only partly into comprehension: \"the correlation between a study's vocabulary gain and its comprehension gain was only modest (r \\= .43).\" (BrainLift intro video, line 487).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 45,
   "verdict": "keep",
   "reason": "Quote verbatim: four-tier threads line 396. It is a requirement on a fix list, not a measured result. Overlaps 18 and candidate 44 (spaced encounters).",
   "statement": "List each unit's technical terms in its knowledge base, teach them before reading, and carry them forward with spaced recall.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of G3-8_Threads_FourTier.docx",
     "lines": "396 (textutil text)",
     "quote": "Each unit's technical terminology (above) must be listed in the KB, taught before reading, and carried with spaced recall",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 46,
   "verdict": "keep",
   "reason": "Quote verbatim: Standard components E46, the failure note for RI.3.4.b. The prescription is inferred from the failure, and the inference is reasonable.",
   "statement": "Teach a domain word directly when the whole domain is new to the student, because surrounding text cannot reveal its meaning when the concepts around it are new too.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
     "lines": "sheet 'Standard components', cell E46",
     "quote": "Child can't use context when the whole domain is unfamiliar. The surrounding text doesn't help because the concepts are also new.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 47,
   "verdict": "keep",
   "reason": "Quotes verbatim: walkthrough v1 line 55 and v2.1 line 21. Line 89 of v1 gives the one word that does split into real parts, cheer + ful.",
   "statement": "Break a word into meaningful parts only where it really has them, because invented splits teach false parts.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "55",
     "quote": "The family stage teaches only real derivations — *eerily, eeriness* — never invented splits, because syllables are not morphemes.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "21",
     "quote": "Syllable breaks for saying; meaning-parts only when real | Inventing splits (ee+rie) would teach false word-parts",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 48,
   "verdict": "keep",
   "reason": "Quotes verbatim: walkthrough v1 line 77, v2.1 line 20 and Physics card line 93.",
   "statement": "Teach a concept with examples that differ on the surface but share its one deep feature, and with near-miss non-examples that each fail for one nameable reason.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "77",
     "quote": "three surface-different scenes, one deep feature, with near-miss words — *careful, tired, polite* — each wrong for exactly one nameable reason",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "20",
     "quote": "Each wrong option differs by one nameable feature | Discrimination teaches a concept’s edges; each feedback names the one mismatch",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx",
     "lines": "93 (textutil text)",
     "quote": "Do NOT demonstrate Newton's third law only with stationary examples (book on table). Include MOVING examples (collisions, pushing off a wall on roller skates).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 49,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, but the chemistry card's 'no framework' covers only the negative definition for particles (line 77), not negative definitions in general. 'With a counterexample' had no cited support; the biology card supplies it (line 210).",
   "statement": "Teach what a concept is not, as explicit instruction when the concept is introduced, with a counterexample; the chemistry guidance found no standards framework that states this negative definition for particles.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "244 (textutil text)",
     "quote": "Every concept area has things that students need to be told are NOT true. These are as important as the positive definitions.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "77 (textutil text)",
     "quote": "No framework currently includes this \"negative definition.\"",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx",
     "lines": "210 (textutil text)",
     "quote": "Provide counterexamples: \"Polydactyly (extra fingers) is dominant over five fingers.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Science_Curriculum_Review_Workbook.xlsx",
     "lines": "sheet 'G3', cell D3",
     "quote": "[New — D1 Section 2.1 negative definition; required at Grade 3]",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 50,
   "verdict": "keep",
   "reason": "Quote verbatim: Biology card line 206, for Grades 3-5. The card introduces the terms at Grades 6-8 and defines them at once against their everyday meaning (line 209). One example.",
   "statement": "Hold back a technical term whose everyday meaning misleads until the concept it names is actually needed.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx",
     "lines": "206 (textutil text)",
     "quote": "Do NOT introduce \"dominant\" and \"recessive\" at this level — the terms carry too much everyday baggage and the concepts are not needed yet.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 51,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim: Chemistry lines 76 and 199 and Cross-Cutting lines 64 and 220. The original called first introduction 'the riskiest point'. For particles, the card rates the gap highest and the moment of introduction second (lines 76-77), so the fix names both.",
   "statement": "Teach a concept correctly the first time it appears, and state its key constraint, such as conservation, at that moment rather than later: the misconception cards rate the first introduction, and the gap before a correct explanation, as the riskiest points.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "76 (textutil text)",
     "quote": "During this gap, students build macroscopic mental models that become the default.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "199 (textutil text)",
     "quote": "Highest risk: The moment bonding mechanisms are first taught (typically grades 9-10).",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "64 (textutil text)",
     "quote": "energy conservation must be taught at the SAME TIME energy is introduced (as the Franklin Standards do at grade 3), not as a later addition.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "220 (textutil text)",
     "quote": "Conservation: State conservation simultaneously with introducing the concept (energy, mass, charge).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 52,
   "verdict": "keep",
   "reason": "Quotes verbatim: Cross-Cutting lines 119 and 121 and Biology line 260. The statement is general.",
   "statement": "Present every simplified model or diagram with a short note that it is a simplification and what it leaves out.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "119 (textutil text)",
     "quote": "Every model should carry an explicit health warning",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "121 (textutil text)",
     "quote": "Whenever an LLM system presents a model (diagram, equation, simplified explanation), it MUST include a brief framing statement indicating that the model is a simplification.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx",
     "lines": "260 (textutil text)",
     "quote": "Every time a cell diagram is shown, include the explicit framing",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 53,
   "verdict": "keep",
   "reason": "Quotes verbatim: Chemistry line 124 and Cross-Cutting line 251.",
   "statement": "When a full answer is beyond a student's level, give a true partial answer and say more comes later, keeping the same conceptual foundation at every level rather than a false simplification.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "124 (textutil text)",
     "quote": "You'll learn more about what's inside atoms in later grades.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "251 (textutil text)",
     "quote": "The same question from a grade 3 student and a grade 8 student should receive different levels of detail and different mathematical framing, but the SAME conceptual foundation.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 54,
   "verdict": "keep",
   "reason": "Quotes verbatim: Chemistry lines 238 and 240. The AP evidence is the card's exam-relevance note, an uncited claim that questions on exceptions to the octet rule expose students who treat the pattern as a law. The statement generalises from one rule of thumb; reasonable.",
   "statement": "Teach a rule of thumb as a pattern that predicts, not as the reason something happens, because students who take a pattern for a law cannot handle its exceptions.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "238 (textutil text)",
     "quote": "The octet rule (having 8 electrons in the outer shell) is a useful PATTERN that helps predict which arrangements are stable, but it's not the REASON bonds form.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "240 (textutil text)",
     "quote": "Students who hold the teleological model cannot handle exceptions to the octet rule because they believe the octet is a law rather than a pattern.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 55,
   "verdict": "keep",
   "reason": "Quotes verbatim: Physics lines 257 and 250 and Chemistry line 207.",
   "statement": "Choose analogies whose obvious features match the concept, and drop or flag any analogy that suggests a false feature.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx",
     "lines": "257 (textutil text)",
     "quote": "Avoid the water pipe analogy without extreme care — it naturally suggests water (current) is consumed by components.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx",
     "lines": "250 (textutil text)",
     "quote": "But the SKIERS keep going around. The ski lift doesn't create new skiers.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "207 (textutil text)",
     "quote": "Use the analogy of magnets (carefully)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 56,
   "verdict": "keep-with-fix",
   "reason": "Quote verbatim (Physics line 105); line 122 prohibits skipping the first law. The original turned one example into a general claim ('the ideas experts find obvious are often the ones everyday experience contradicts most'). The fix keeps to what the source says.",
   "statement": "Do not skip an idea because it seems obvious: the physics guidance warns that the law most often skipped as obvious is the one everyday experience contradicts most.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx",
     "lines": "105 (textutil text)",
     "quote": "Do NOT skip the first law because it \"seems obvious.\" It is the LEAST obvious law and the one most contradicted by everyday experience.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx",
     "lines": "122 (textutil text)",
     "quote": "Skipping Newton's first law or treating it as trivial.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 57,
   "verdict": "keep",
   "reason": "Quotes verbatim: Physics line 330 and Standard components D39.",
   "statement": "Once two easily confused ideas have both been taught, distinguish them explicitly side by side.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx",
     "lines": "330 (textutil text)",
     "quote": "each pair explicitly distinguished when both have been introduced.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
     "lines": "sheet 'Standard components', cell D39",
     "quote": "Distinguish between a character's temporary feelings and stable traits",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 58,
   "verdict": "keep",
   "reason": "Quotes verbatim: Cross-Cutting line 196, four-tier threads line 400 and backward-design brief line 60.",
   "statement": "Check that students have the prerequisites, including any mathematics, before introducing a concept that depends on them, and sequence the units that supply terms before those that use them.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "196 (textutil text)",
     "quote": "Curriculum builders should check mathematical readiness before introducing concepts that depend on it.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of G3-8_Threads_FourTier.docx",
     "lines": "400 (textutil text)",
     "quote": "Sequence supplying units first so their terms are available",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx",
     "lines": "60 (textutil text)",
     "quote": "the contact means something because both sides have been built.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 59,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The synthesis accepts functional description and bans causal teleology (line 145). The original's 'purpose words applied to things without intentions' would also ban the acceptable functional wording. The cited sweep fixed one check option, not definitions, so that clause was trimmed; the definition fix is evidence for candidate 60.",
   "statement": "Explain how things happen, not what they want: say what a part does, but never that something exists or changed in order to reach a goal; one sweep reworded a check option to remove such wording.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "145 (textutil text)",
     "quote": "The distinction between functional description and causal teleology must be taught explicitly.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "203 (textutil text)",
     "quote": "No teleological language for atomic or molecular behaviour.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 3. The Animal Kingdom - SORT - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "209 (textutil text)",
     "quote": "One science fix was made: Sync check 2 option C changed from \"covered in feathers to fly\" to \"that are covered in feathers\" to remove purpose-implying (teleological) wording.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 60,
   "verdict": "keep",
   "reason": "Quotes verbatim: Plants line 191, Feathers and Scales line 259 and Microorganisms line 185. Confirmed that the fixed option was the keyed answer: Plants first-read MCQ 2 marks C correct (lines 86 and 90). The Mammals sweep also found nothing to fix (line 195). Distinct from 59.",
   "statement": "Run the misconception check on every option, definition and keyed answer, not only the passage: one sweep found the misconception inside a keyed answer.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "191 (textutil text)",
     "quote": "Misconception fix: first-read MCQ 2 option C changed from \"make energy from sunlight\" to \"make food from sunlight\" (plants make food, not energy)",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "90 (textutil text)",
     "quote": "C. food factories that make food from sunlight ✓ CORRECT",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 5. Feathers and Scales - CONNECT - Lesson Design (v3 - prototype-aligned).docx",
     "lines": "259 (textutil text)",
     "quote": "The taught word \"adaptation\" is now defined functionally (\"a feature that helps an animal live well where it lives\")",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 9. The Invisible World Microorganisms - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "185 (textutil text)",
     "quote": "Science-misconception sweep: no fixes were needed",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 61,
   "verdict": "keep-with-fix",
   "reason": "Re-checked in this pass: the two files are byte-identical, and line 27 says the rest of the energy is 'used up', which is a Tier 1 prohibition (Cross-Cutting line 205; Physics line 198). This sweep made the measurement, not the project. The fix adds the evidence for the ban and drops 'so-called'.",
   "statement": "Run every check a text must pass automatically, on rewrites as well as drafts: a draft science text and its 'rewrite' were byte-identical, and both still said energy is 'used up', which the guidance bans.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "243 (textutil text)",
     "quote": "The Tier 1 prohibitions should be implemented as automated checks on any content generated for the curriculum — whether by humans or AI.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "205 (textutil text)",
     "quote": "\"Energy is used up / lost / destroyed\" — Energy is conserved; always specify where it goes.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/G4 DRAFT/2. Ecosystems and Food Webs.docx",
     "lines": "27 (textutil text)",
     "quote": "The rest is lost as heat or used up by the plant's own processes.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/G4 DRAFT/Rewrites/2. Ecosystems and Food Webs - rewrite.docx",
     "lines": "27 (textutil text)",
     "quote": "The rest is lost as heat or used up by the plant's own processes.",
     "verbatim": true
    }
   ],
   "against": "Both files sit in a draft folder ('G4 DRAFT') and may not yet have reached the check.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 62,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. In the source, the preference applies to reading lessons that carry science or social studies content (line 25 sits under the science principles). Without that scope the rule would forbid teaching anything new, so the fix adds it.",
   "statement": "When a lesson carries another subject's content, prefer ideas students will have met before to ideas they would meet there first, and give each re-encounter a new angle rather than a repeat.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md",
     "lines": "25",
     "quote": "It is better to re-encounter ideas from earlier grades than to be the first place a student meets an idea.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md",
     "lines": "9",
     "quote": "are always fair game for re-encounter",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md",
     "lines": "11",
     "quote": "The aim is for the re-encounter to feel like a new angle, not a repeat.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 63,
   "verdict": "keep",
   "reason": "Quotes verbatim: coherence guidance lines 4 and 10.",
   "statement": "When you cannot know whether students have met a topic yet, write the lesson so that it works either way.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md",
     "lines": "4",
     "quote": "at any given moment we cannot be sure whether a student has studied a topic or not.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md",
     "lines": "10",
     "quote": "provided it is done in such a way that it doesn't matter whether the substantive science or social studies lesson has happened yet.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 64,
   "verdict": "keep",
   "reason": "Quotes verbatim: coherence guidance lines 21 and 26 and Rainforests design line 223.",
   "statement": "Do not present contested or open questions as settled, and frame students' conclusions so it is clear whether they are observations, guesses, interpretations or opinions.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md",
     "lines": "21",
     "quote": "the passage should not be presented as settled where this is unwarranted.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md",
     "lines": "26",
     "quote": "student writing should be framed so that it's clear which of these the student is doing.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 2. Should We Save the Rainforests - WEIGH - Lesson Design.docx",
     "lines": "223 (textutil text)",
     "quote": "Nothing is overclaimed beyond the passage.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 65,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim: reviewer notes on map export lines 79 and 89, and curriculum map Sources & Inspiration G9 (for a tale from an oral tradition). These are three notes on particular texts, so the fix limits the rule to the kinds of text they cover.",
   "statement": "In history and culture texts, show an achievement's limits, never play down the harm done to the people affected, and retell other peoples' traditional stories respectfully.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/_G3 curriculum Map.xlsx - Curric Map.csv",
     "lines": "79",
     "quote": "Ensure the limitations of Ancient Greek democracy are discussed.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/_G3 curriculum Map.xlsx - Curric Map.csv",
     "lines": "89",
     "quote": "Be really careful here to not downplay the tragedy of European arrival for those already in the Americas (ditto with texts below).",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'Sources & Inspiration', cell G9",
     "quote": "Ensure respectful retelling",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 66,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Counted in this verification on the map's Sources & Inspiration sheet. Of 47 non-fiction rows, 28 read 'AI-generated from general knowledge', 8 more are AI-generated (with a draft text or as persuasive writing), and 11 read 'Unknown'. None names a source that can be checked. The guidance's traceability rule answers the open question, so it is recast as a measured gap. Bears on 50 and 57.",
   "statement": "Give every non-fiction text a reputable source it can be checked against: in one curriculum map none of the 47 non-fiction texts named one, most being recorded as AI-generated from general knowledge.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md",
     "lines": "16",
     "quote": "Non-fiction passages should be factually accurate and traceable to reputable sources.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'Sources & Inspiration', cell D41",
     "quote": "AI-generated from general knowledge",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'Sources & Inspiration', cell E41",
     "quote": "General botanical knowledge (photosynthesis, plant parts, life cycles)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 67,
   "verdict": "keep",
   "reason": "Quotes verbatim: backward-design brief lines 3 and 111 and curriculum map Sources & Inspiration G27. Adds a point about rights beside 50, which says a source note is not a licence.",
   "statement": "Record each text's rights status, and check a translation's rights separately from the original's, because a modern translation carries its own copyright.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx",
     "lines": "3 (textutil text)",
     "quote": "[© model] = the example text is in copyright and shown only to illustrate the concept — find a free equivalent (or we license it).",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx",
     "lines": "111 (textutil text)",
     "quote": "For any translated classic (the Odyssey, Greek drama, Beowulf), use a public-domain translation — a modern translation carries its own fresh copyright.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'Sources & Inspiration', cell G27",
     "quote": "6-part retelling. Twain died 1910; globally public domain.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 68,
   "verdict": "keep",
   "reason": "Quotes verbatim: backward-design brief lines 5 and 110 and thematic map 'How to read this' A9.",
   "statement": "Build a curriculum thread backward from a demanding end-point text: name the concept it needs, then choose earlier texts that build the same concept in simpler form, keeping the idea constant and raising only the difficulty.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx",
     "lines": "5 (textutil text)",
     "quote": "We pick a Grade 8 destination, name the concept it demands, then choose earlier texts that build that same concept in simpler form every year.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx",
     "lines": "110 (textutil text)",
     "quote": "Keep the concept constant, raise the difficulty.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx",
     "lines": "sheet 'How to read this', cell A9",
     "quote": "Shakespeare is hard language over familiar ground.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 69,
   "verdict": "keep",
   "reason": "Quotes verbatim: consensus workbook V7.0 Executive Summary A30 and A33. The verb lifts are explain to evaluate and describe to evaluate (A31-A32).",
   "statement": "When a later stage covers the same content as an earlier one, make its demand strictly higher, for example from describing to evaluating.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'V7.0 Executive Summary', cell A30",
     "quote": "Two G8 History standards received verb lifts to ensure cognitive demand is strictly higher than their G7 equivalents:",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'V7.0 Executive Summary', cell A33",
     "quote": "This maintains the DOK progression principle that G8 standards must be higher-order than G7 equivalents covering the same content.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 70,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The found_by numbers are wrong. The SC Coverage tally lists 79 codes (11 None, 35 Low), while the sheet's own summary says 86 in total and 36 Low. At least two of the 11 zeros are stale: RL.3.3.e is placed at H36, J36 and K36, and RI.3.6.c at F48. The fix adds counting from the current placements.",
   "statement": "Audit coverage by counting, from the current placements, how many lessons serve each required component or text type, and treat a zero as a gap to close; a stored tally read zero for a component the same sheet had placed.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx",
     "lines": "69 (textutil text)",
     "quote": "Three text types currently return zero hits and must be covered — best homed in Science and Geography, not a separate strand:",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx",
     "lines": "62 (textutil text)",
     "quote": "Biography, memoir and autobiography currently return zero hits anywhere.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'SC Coverage', cell K36",
     "quote": "ONLY PLACEMENT OF RL.3.3.e.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'SC Coverage', cell O43 (the stored count on the RL.3.3.e row)",
     "quote": "0.0",
     "verbatim": true
    }
   ],
   "against": "\"Thin cells are where a thread rests at a grade and returns deeper later — a spiral, not a checklist.\" (Grade_3-12_Full_Thematic_Map.xlsx, sheet 'Coverage check', cell A13).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 71,
   "verdict": "keep",
   "reason": "Quotes verbatim: curriculum map SC Coverage T5, K45 and K52; K96 is the fourth correction. Close to 63 (check the labels), applied to skill tags.",
   "statement": "Tag a lesson with a skill only if its text actually affords that skill; reviews found tags the texts could not serve and reassigned them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'SC Coverage', cell T5",
     "quote": "the Phase 3 ladder assesses the HOW of the lamp-use change, and the text has no because/so/since signal words. Reassign RL.3.1.d to a lesson whose text genuinely signals cause-effect.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'SC Coverage', cell K45",
     "quote": "RL.3.6.d replaces mistagged RL.3.9.d.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'SC Coverage', cell K52",
     "quote": "WRITER'S COMPARISON — RI.3.3 not RI.3.9 (single text).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 72,
   "verdict": "keep",
   "reason": "Quotes verbatim: map export lines 46 and 76. This is a sequencing choice in one map; no outcome was measured.",
   "statement": "Before asking students to compare two texts, give them a single text that makes the comparison itself.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/_G3 curriculum Map.xlsx - Curric Map.csv",
     "lines": "46",
     "quote": "A scaffolded within-text comparison to build skills toward cross-text comparison later.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/_G3 curriculum Map.xlsx - Curric Map.csv",
     "lines": "76",
     "quote": "CROSS-TEXT COMPARISON (student writing) — RI.3.9 + W.3.2",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 73,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The found_by figures are verified: B2 gives 16,345 standards from 51 jurisdictions, and B10 includes only MODERATE and above. B3 answers 'Why not C3 alone' (A3), so the rule is not to rely on a skills-only framework alone, rather than not to build on one.",
   "statement": "Choose core content by how many independent sources include it, with a fixed inclusion threshold, settle conflicts in favour of the knowledge-rich, recently revised source, and do not rely on a skills-only framework alone for content.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'Methodology Notes', cell B9",
     "quote": "CORE 38+, HIGH 26-37, MODERATE 13-25, LOW <13",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'Methodology Notes', cell B8",
     "quote": "Knowledge-rich + recently revised wins.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'Methodology Notes', cell A3",
     "quote": "Why not C3 alone",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'Methodology Notes', cell B3",
     "quote": "Skills only - no content mandates, no assessments",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 74,
   "verdict": "keep",
   "reason": "Quotes verbatim: V7.0 Executive Summary A65 and Retired Standards X2. The summary's count of 11 does not match the Retired Standards tab, which holds 9 entries (rows 2-10). The summary has drifted from its own data, which bears on 24.",
   "statement": "Retire items instead of deleting them, and record what each was merged into or covered by, so every change stays traceable.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'V7.0 Executive Summary', cell A65",
     "quote": "- RETIRED standards: 11 (preserved for traceability)",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'Retired Standards', cell X2",
     "quote": "Cat 1: Merged into K.His.3",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 75,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim: Standard components D1, E32 and G1. The statement is unchanged, but the found_by count is wrong: the sheet has 86 components across 20 CCSS standards, not 36. Each component links to one of six knowledge categories.",
   "statement": "Break each standard into components that each name one point of failure, the specific error a student makes when it fails, and the kind of knowledge it depends on.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
     "lines": "sheet 'Standard components', cell D1",
     "quote": "(single point of failure)",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
     "lines": "sheet 'Standard components', cell E32",
     "quote": "Child picks an interesting or memorable detail and calls it the main idea. Drawn to vivid facts rather than the overarching point.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
     "lines": "sheet 'Standard components', cell G1",
     "quote": "Knowledge Category Link",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 76,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, and the totals verified (Summary B11: 1129 atoms; C11: 385 composites). 'Single-claim facts' contradicts the workbook, whose Summary sheet records 2.5 facts per atom at every grade (column G). The fix says small atoms of a few facts each.",
   "statement": "Write knowledge as small atoms of a few facts each, mark each as new or as a review that names where it was first taught and what is new, and add composite tasks that make students combine several atoms.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Science_Curriculum_Review_Workbook.xlsx",
     "lines": "sheet 'G3', cell D2",
     "quote": "[Spiral review of G2 Unit 2, A3-A4 — what is new: \"atoms\" replaces \"tiny pieces/particles\"; formal term introduced per D1 3-5 band]",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Science_Curriculum_Review_Workbook.xlsx",
     "lines": "sheet 'G3', cell D15",
     "quote": "[Multi-step: measure properties, classify by properties, connect to particle model with negative definition]",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Science_Curriculum_Review_Workbook.xlsx",
     "lines": "sheet 'Summary', cell G1 (2.5 in every grade row, G2:G10)",
     "quote": "Facts per atom",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'Methodology Notes', cell B14",
     "quote": "4-step expansion per grade: collect specifics, add context, break into micro-atoms, sequence for delivery.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 77,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The cited 'Seeds run forward' line describes the unit, not each lesson. The per-lesson record is the knowledge base's Prior Knowledge and Knowledge Seeds columns (Knowledge Base sheet E5 and T5), now cited.",
   "statement": "Record for every lesson what it builds on and what it seeds later, so the whole sequence can be checked for knowledge gaps.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/[WORKING DRAFT] AlphaRead_G3-8_Full_Curriculum_to_G9.xlsx",
     "lines": "sheet 'Overview (read across)', cell A2",
     "quote": "Goal: a child reaches Grade 9 with no knowledge gaps.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx",
     "lines": "sheet 'Knowledge Base', cell E5",
     "quote": "Prior Knowledge",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx",
     "lines": "sheet 'Knowledge Base', cell T5",
     "quote": "Knowledge Seeds",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx",
     "lines": "sheet 'Overview', cell B39",
     "quote": "Seeds run forward to 3.4 Folk Tales, 3.10 Myths, 3.12/3.15 Poetry, the Grade 4 units (4.1 Legends, 4.4 World Mythology, 4.9 Classic Novels), and cross-curricular Science/Geography and History.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 78,
   "verdict": "keep",
   "reason": "Quote verbatim: Living World KB Overview B35. This is a design mapping; no outcome was measured.",
   "statement": "Match the reading procedure to what the text is: locating for fact texts, comparing for comparison texts, sorting for classification texts and weighing for persuasive texts.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - The Living World - Complete KB.xlsx",
     "lines": "sheet 'Overview', cell B35",
     "quote": "FIND fits the fact-based texts (Plants, Mammals, Invertebrates, Microorganisms). The comparison texts (Feathers and Scales, Life in Water) use CONNECT - compare two groups, then draw the deeper link. The Animal Kingdom uses SORT (classify by shared features); the persuasion texts (Rainforests, Whose World Is It) need WEIGH / fact-vs-opinion.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 79,
   "verdict": "keep",
   "reason": "Quotes verbatim: walkthrough v1 lines 12 and 181 and Fantasy Classics KB 'Knowledge Base' A3.",
   "statement": "Teach one named procedure per lesson and keep its steps worded identically in the introduction, the worked example, guided and independent practice and the recap.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "12",
     "quote": "The steps are printed verbatim on the skill intro, the model, the guided try, the independent write, and the wrap recap — the rail never changes mid-lesson.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "181",
     "quote": "An advance organizer for a procedure: the child meets the rail once, cold, before watching it run — so the model that follows is recognition, not first contact.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx",
     "lines": "sheet 'Knowledge Base', cell A3",
     "quote": "Each lesson runs ONE reading PROCEDURE (FIND / CONNECT / INFER) on its key threshold (in RED): the teacher models it in the Modelling Moment, the child completes the final step, and Part Three re-runs the same procedure on fresh evidence.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 80,
   "verdict": "keep",
   "reason": "Quotes verbatim: walkthrough v2.1 line 42 and Ancient Civilisations KB Overview B7.",
   "statement": "Return to the unit's organising pattern in every lesson and fill in the part each text delivers, so the pattern builds up across the unit instead of being covered once.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "42",
     "quote": "The five-row pattern chart returns every lesson, filled row by row | Schema accumulates across the unit instead of being covered once",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.3 - Ancient Civilisations - Lesson Designs/3.3 Ancient Civilisations - Knowledge Base - Full.xlsx",
     "lines": "sheet 'Overview', cell B7",
     "quote": "Flood-fed farming → the first cities → writing → leaders & government → trade. Every text tests this pattern.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 81,
   "verdict": "keep",
   "reason": "Quotes verbatim: thematic map 'How to read this' A7 and A11.",
   "statement": "Track how complex each idea is separately from grade level, and mark the keystone items that much later material depends on so they are never dropped.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx",
     "lines": "sheet 'How to read this', cell A7",
     "quote": "Rung is the complexity of the IDEA, tracked alongside grade.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx",
     "lines": "sheet 'How to read this', cell A11",
     "quote": "KEYSTONE texts are the anchor of a rung — the one you would not drop, because so much above it depends on the concept it plants.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 82,
   "verdict": "keep",
   "reason": "Quotes and numbers verbatim: Fantasy Classics KB Overview A15 and thematic map 'Threads & Ladders' A2.",
   "statement": "Organise a whole course around a small fixed set of recurring concepts, and record which of them each lesson draws on.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx",
     "lines": "sheet 'Overview', cell A15",
     "quote": "CONCEPT MAP - which concepts each lesson draws on (from the fixed 14-pair bank)",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx",
     "lines": "sheet 'Threads & Ladders', cell A2",
     "quote": "Your 14 concept-pairs, consolidated into 7 course-long threads.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 83,
   "verdict": "keep",
   "reason": "Quotes verbatim, and the found_by counts verified (G3 Comparison B27: 23; B28: 1; B29: 3; B30: 19). Four folk tales are tagged as adaptations of public-domain sources (map export lines 14-17), and a fifth text is a proposed addition (line 37).",
   "statement": "When aligning to a required list of texts, match on the text itself, recording a different edition of the same story and a merely related topic separately from a true match.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/TEA Proposed Mandatory Literary Works (HB 1605).xlsx",
     "lines": "sheet 'G3 Comparison', cell E9",
     "quote": "Alpha has 'The Story of Icarus' in Unit 10 (Myths) — same myth, different source text/edition",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/TEA Proposed Mandatory Literary Works (HB 1605).xlsx",
     "lines": "sheet 'G3 Comparison', cell E13",
     "quote": "Alpha has 'Ancient Egypt — The Gift of the Nile' (Unit 3) — related topic, different text",
     "verbatim": true
    },
    {
     "path": "~/Downloads/_G3 curriculum Map.xlsx - Curric Map.csv",
     "lines": "14",
     "quote": "TEA HB 1605 (Alpha adaptation of PD source)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 84,
   "verdict": "keep",
   "reason": "Quotes verbatim: the archived note at line 9 and Thread Explorer A2. The reason for the move, appropriateness, appears only in the archived note, whose path carries a name. The maps record the move without a reason (Thread Explorer F104; working-draft map Grade 4 E78).",
   "statement": "Place a text by the maturity of its content as well as by its reading difficulty.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/G3/Grade 3 word docs/15 - Poetry (Criticism)/Archive/Claude Notes on Criticism poems_.docx",
     "lines": "9 (textutil text)",
     "quote": "So moving it to G5 is the right call on appropriateness alone.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/G3-8_Knowledge_Threads_to_G9.xlsx",
     "lines": "sheet 'Thread Explorer', cell A2",
     "quote": "RED note = a revision (e.g. The Highwayman moved to Grade 5).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 85,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim: the archived note at lines 3 and 6. The reasoning rests only on that note, whose path carries a name. The map kept the short-poem option (map export line 25 lists 'I'm Nobody! Who are you?' under Poetry for Criticism), though its poems differ from the note's trio. That line is added as evidence of what was adopted.",
   "statement": "Fill a curriculum slot with the text that gives a new capability later units build on, not one that repeats what the next stage already covers.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/G3/Grade 3 word docs/15 - Poetry (Criticism)/Archive/Claude Notes on Criticism poems_.docx",
     "lines": "3 (textutil text)",
     "quote": "The Pied Piper adds engagement but not a new capability.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/G3/Grade 3 word docs/15 - Poetry (Criticism)/Archive/Claude Notes on Criticism poems_.docx",
     "lines": "6 (textutil text)",
     "quote": "For foundational value, the trio wins.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/_G3 curriculum Map.xlsx - Curric Map.csv",
     "lines": "25",
     "quote": "Poetry for Criticism,I'm Nobody! Who are you?",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 86,
   "verdict": "keep-with-fix",
   "reason": "Re-verified in the G4 draft itself, whose path carries no name. Its teaching text says a poem 'can refuse to' rhyme (line 285), yet all five of its poems rhyme: The Highwayman, Lochinvar, My Shadow, Stopping by Woods and I Wandered Lonely as a Cloud (lines 216-217 are one rhyming pair). The archived note that first made the point is dropped as evidence because its path carries a name.",
   "statement": "Back every claim the materials make about a category with an example students actually meet: one draft unit teaches that a poem can refuse to rhyme, yet every poem in it rhymes.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/G4 DRAFT/12. Poetry - Narrative and Lyric.docx",
     "lines": "285 (textutil text)",
     "quote": "A poem can rhyme or it can refuse to.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/G4 DRAFT/12. Poetry - Narrative and Lyric.docx",
     "lines": "216 (textutil text)",
     "quote": "Whose woods these are I think I know.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/G4 DRAFT/12. Poetry - Narrative and Lyric.docx",
     "lines": "217 (textutil text)",
     "quote": "His house is in the village though;",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 87,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim: BrainLift intro video lines 455 and 319 (Ausubel 1968, no DOI). Ausubel states the limit for 'Elementary pupils and novices', so the fix adds that scope. Line 455 says never the term alone and line 319 says never the instance alone, so the fix keeps both.",
   "statement": "For young students and novices, name a term and show an instance of it together, never one without the other.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "455",
     "quote": "Elementary pupils and novices cannot process abstract propositions verbally without",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "455",
     "quote": "So the rule is name the term and show the instance, never the term alone.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "319",
     "quote": "Name the term, then show the instance — \"Every story happens somewhere. We call that the setting\" — never the instance alone.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 88,
   "verdict": "keep",
   "reason": "Quotes and the effect size verbatim: BrainLift intro video lines 129-130. The DOIs at lines 21, 129 and 130 are verified.",
   "statement": "Cut interesting but irrelevant material, above all at the start, because it lowers recall and transfer.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "129",
     "quote": "Interesting but irrelevant details reduced recall and transfer, and did the most damage placed at the start of the text.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "130",
     "quote": "Excluding extraneous material improves multimedia learning, median effect near d 0.70.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 89,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim: BrainLift intro video lines 446 and 421 (Bransford and Johnson 1972, no DOI). The study used opaque passages, so the fix limits the claim to a hard passage. Complements 20, which is about where background goes inside a text.",
   "statement": "Give the context a hard passage depends on before the reading, not after: in a classic study the same context given afterwards did not help.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "446",
     "quote": "giving readers the context before an opaque passage transformed comprehension and recall. The same context after did not.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "421",
     "quote": "Everything this document argues rests on the video sitting before the read.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 90,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim: BrainLift intro video line 439 (Recht and Leslie 1988), WF brainlift line 32 and thematic map A3. The original's 'far better than general reading ability' made one study into a law for any text. The fix states the finding.",
   "statement": "Build the topic knowledge a text assumes: in a classic study, prior knowledge of the topic predicted memory for the text, while general reading ability predicted almost none.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "439",
     "quote": "prior knowledge of baseball predicted memory for a baseball text on essentially every measure; general reading ability predicted almost none.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "32",
     "quote": "It is a complex activity that rests on language and, more than anything, background knowledge (Catts, 2021-2022).",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx",
     "lines": "sheet 'How to read this', cell A3",
     "quote": "This is the 'knowledge latches onto knowledge' principle applied to whole-school reading.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 91,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim: BrainLift intro video lines 427 and 470 (Chi, Roy and Hausmann 2008, no DOI) and walkthrough v1 line 197. The source says solo observation was 'weaker', not that it teaches nothing, so the statement is fixed.",
   "statement": "Watching someone else being taught substitutes for being taught only when the watcher is active, so in solo study embedded checks and pauses must do the work a discussion partner would.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "427",
     "quote": "Watching someone else be taught only substitutes for being taught when the watcher is active.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "470",
     "quote": "Solo observation was weaker, so in a solo app the checks and pauses have to do the work the partner did.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "197",
     "quote": "The taps are attention devices, not assessment — they keep a long model active without adding an ask.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 92,
   "verdict": "keep",
   "reason": "Quote and numbers verbatim: BrainLift intro video line 456, two experiments with 48 and 53 university students, far transfer rising from roughly 33% to 67%. One study, and the statement hedges as the source does.",
   "statement": "A preview organiser helps when it emphasises the key concepts, not only the structure; structure alone was not reliably better.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "456",
     "quote": "What carried it was the version that additionally emphasised the key concepts. Structure without emphasis was not enough.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 93,
   "verdict": "keep-with-fix",
   "reason": "Quotes and numbers verbatim: BrainLift intro video line 471 (Muller et al. 2008, no DOI). The fix takes a job role out of the statement, says it is one study, and carries the document's own limit for media under a minute (lines 307 and 426).",
   "statement": "Where there is time, prefer a dialogue that answers a learner's questions, or a refutation of the wrong idea, to straight exposition: in one study of 364 students both beat exposition, most for those with the least prior knowledge.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "471",
     "quote": "The tutor-student dialogue version beat straight exposition at d \\= 0.83; the refutation version at d \\= 0.79. Lowest-prior-knowledge students gained most.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "471",
     "quote": "364 students, the same physics content in four formats.",
     "verbatim": true
    }
   ],
   "against": "For media under a minute the same document prefers one narrator: \"(For short videos, just the narrator is preferable though \\-- see SPOV5).\" (BrainLift intro video, line 426), and \"Below that threshold, use a single knowledgeable narrator and put the modelled thinking in the lesson, where there is room for it.\" (line 307).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 94,
   "verdict": "keep",
   "reason": "Quotes verbatim: BrainLift intro video lines 315, 321 and 355. Truth 44 already holds that a quality call stays unjudged until a person has listened. Kept as added evidence for two failures that show only when a compressed script is spoken.",
   "statement": "Read every narration script aloud before release, because cutting removes the labels that name what the student is looking at first, and written-style sentences collapse when spoken.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "315",
     "quote": "It removes the connective words first — the ones that named what the child was looking at and what to call it — because on the page those words look like padding.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "321",
     "quote": "Colons, parenthetical asides, appositives and list constructions survive silently on the page and collapse in a voiceover.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "355",
     "quote": "A line that fails any of these usually reads perfectly well on the page. That is why the pass has to be spoken.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "44",
   "name_bearing_source": false
  },
  {
   "index": 95,
   "verdict": "keep",
   "reason": "Quotes verbatim: BrainLift intro video lines 349-351.",
   "statement": "In narration, name a representation as a representation, give the category before a proper name, and say when something shown is not an example of what is being taught.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "349",
     "quote": "Example: \"That is a statue of a pharaoh\", never \"that is a pharaoh\". A child otherwise takes the object for the person.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "350",
     "quote": "The name then lands as an instance of something already understood rather than as a new thing to hold.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "351",
     "quote": "If something on screen is not an example of what is being taught, say so.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 96,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim: BrainLift intro video line 269 and walkthrough v2.1 line 9. 'Edit or compress' collides with 23 (split, don't cut approved words). The fix keeps only what the evidence supports: work from reviewed material instead of regenerating it.",
   "statement": "Where reviewed material exists, work from it rather than regenerating it from source notes, because regeneration throws away the earlier review and brings back errors already caught.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "269",
     "quote": "Regenerating from the knowledge base discards all of that and reintroduces errors that were already caught once. Compression is a smaller, safer and more auditable job than generation.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "9",
     "quote": "Most of the content is your own work transferred, not re-generated",
     "verbatim": true
    }
   ],
   "against": "Compressing reviewed words is itself cutting approved words, which truth 23 found lost the style; and truth 42 asks for a remake when a rule changes.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 97,
   "verdict": "keep",
   "reason": "Quotes verbatim: BrainLift intro video lines 987, 992 and 59. Adds to 42.",
   "statement": "Fix each recurring character's and place's look once for the whole unit and reuse it everywhere; if the look must change, every piece made with the old look is wrong until remade.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "987",
     "quote": "A character has one appearance, decided once for the unit. It is not re-described per video and not per shot.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "992",
     "quote": "If an appearance has to change, it changes for the unit and every video already made against it is wrong until it is remade.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "59",
     "quote": "Characters and places keep one locked look across every video, because recognition is the memory system.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 98,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim: BrainLift intro video line 965, Aladdin Part 2 line 60 and Plants line 44. The second half, putting needed words in the interface, is not in any of the cited lines, so it was cut.",
   "statement": "Keep words and labels out of generated images and video frames.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "965",
     "quote": "No text in generated frames",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "60 (textutil text)",
     "quote": "no text or labels in the image",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "44 (textutil text)",
     "quote": "no text baked into the art.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 99,
   "verdict": "keep",
   "reason": "Quotes verbatim: BrainLift intro video lines 978-979. A house rule for generated video; no outcome was measured.",
   "statement": "Ask a video generator for one main action per clip with no cut inside it, because a clip asked to carry a sequence produces one that cannot be edited out.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "978",
     "quote": "One main action per clip.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "979",
     "quote": "No cut inside a clip. A clip asked to carry a sequence of events produces one, and it cannot be edited out afterwards.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 100,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The second clause, never mentioning what the shot does not show, is truth 21 (line 957 is already evidence for it), so it was cut. 'The name for what is on screen' comes from the same file's read-aloud rule (line 319); it stops the ban on captioning lines from also cutting the labels a child needs.",
   "statement": "Make each narration line add what the picture cannot show, such as a thought, a cause or the name for what is on screen, rather than describe what the frame already makes obvious.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "943",
     "quote": "Narration must add what the frame cannot say. It must not describe facts already obvious in the same frame.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "145",
     "quote": "A line that captions its own picture is rejected.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "319",
     "quote": "A scene of two animals reads as two animals, not as *the characters*, unless somebody says so.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 101,
   "verdict": "keep",
   "reason": "Quotes verbatim: walkthrough v2.1 line 39 and lesson-components spec line 14.",
   "statement": "When the voice reads printed text aloud, it must match the print word for word, with each word highlighted as it is read.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "39",
     "quote": "Read-to-me audio matches the printed words exactly, word-highlighted | Any mismatch breaks decoding support and the child’s trust in the voice",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
     "lines": "14 (textutil text)",
     "quote": "The full text read aloud with word-by-word highlighting at a fixed pace (110–120 wpm, no per-student speed).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 102,
   "verdict": "keep",
   "reason": "Quote verbatim: BrainLift intro video line 953. A single-source-of-truth rule; no outcome was measured. The banned phrase list lives in the writer's prompt, where truth 62 found warnings made a writer worse.",
   "statement": "Keep each banned-word or banned-punctuation list in one place that the generator reads, and never restate it elsewhere.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "953",
     "quote": "Neither list is restated anywhere else.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 103,
   "verdict": "keep",
   "reason": "Quotes verbatim: walkthrough v1 lines 15 and 387.",
   "statement": "Log every deliberate divergence from the design with the ruling that covers it, and state where the live build differs from the authored intent instead of reconciling it quietly.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "15",
     "quote": "Every knowing divergence is logged in a deviations ledger with the ruling that covers it; the open ones appear in this walkthrough as amber flags.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "387",
     "quote": "Where a screen’s behaviour on the live build differs from its authored intent, the difference is stated in the text rather than reconciled quietly.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 104,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim: walkthrough v2.1 line 38 and v1 line 181. 'Builder jargon' named a job role, so it is reworded. Extends 2.",
   "statement": "Write instructions, prompts and feedback at an easier reading level than the text they support, and keep internal design terms out of them.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "38",
     "quote": "Child-facing prose at 420–650L, below the passage; warm, no jargon | The scaffold must be easier to read than the thing it scaffolds",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "181",
     "quote": "No rail jargon reaches the child (“INFER” is for builders)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 105,
   "verdict": "keep",
   "reason": "Quotes verbatim: walkthrough v2.1 lines 27-28. Extends 26.",
   "statement": "Give each screen one primary thing to attend to, and bring in support at the step that uses it rather than stacking it on arrival.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "27",
     "quote": "Each screen has a single thing to attend to | Attention is the scarcest resource; split screens split learning",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "28",
     "quote": "Help appears at the step that uses it, never stacked upfront | Support on arrival is clutter; support at the point of use is scaffolding",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 106,
   "verdict": "keep",
   "reason": "Quotes verbatim: Aladdin Part 2 line 54 and Wind in the Willows Part 3 line 46. The designs dropped a reminder that the lesson-components spec still shows (line 11).",
   "statement": "Remove from the screen anything the current lesson does not teach or use, even a familiar reminder.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "54 (textutil text)",
     "quote": "The pattern is not taught here, so it is removed entirely.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 10. The Wind in the Willows, Part 3 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "46 (textutil text)",
     "quote": "The pattern is not taught here, so it is removed from the prompts. (It still lives in the video, Component 1.)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 107,
   "verdict": "keep",
   "reason": "Quotes verbatim: Aladdin Part 2 line 60 and Wind in the Willows Part 2 line 58.",
   "statement": "When a picture contrasts two states, keep framing and scale identical in both halves so that only the contrast changes.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "60 (textutil text)",
     "quote": "Identical framing and scale on both halves so the contrast in the boy's power reads instantly",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 9. The Wind in the Willows, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "58 (textutil text)",
     "quote": "Identical framing and scale on both halves so the contrast reads instantly: real trouble on one side, a happy daydream on the other.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 108,
   "verdict": "keep",
   "reason": "Quotes verbatim: Aladdin Part 2 lines 213 and 6.",
   "statement": "In independent practice, let students open a recap of what the worked example did at each step, drawn from the example's own material rather than the current answer.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "213 (textutil text)",
     "quote": "Every step carries a collapsible \"What the teacher did\" recap that references the cave model, plus contextual help.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "6 (textutil text)",
     "quote": "every Independent (Phase 3) step now carries a toggleable \"What the teacher did\" recap that references the cave model",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 109,
   "verdict": "keep",
   "reason": "Quote verbatim: walkthrough v1 line 241. One source.",
   "statement": "Have students find the part of the text where the evidence lives before hunting for the exact line.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "241",
     "quote": "locating the evidence neighborhood before hunting in it keeps the hunt a comprehension act rather than a scan-everything act.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 110,
   "verdict": "keep-with-fix",
   "reason": "Quote verbatim: BrainLift intro video line 311. The half about media under a minute is in the heading at line 309, now cited. The statement is unchanged. The source calls the rule an estimate from experience.",
   "statement": "Place a check embedded in media at a natural boundary, and for media under about a minute put the check just after rather than inside.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "309",
     "quote": "For videos under \\~60s, the sync check comes immediately after.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "311",
     "quote": "A check earns its interruption by landing on a boundary: it consolidates the thing just taught and clears working memory before the next arrives.",
     "verbatim": true
    }
   ],
   "against": "\"N.B. this is a sensible estimate based on experience.\" (BrainLift intro video, line 311).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 111,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, but the file's two versions disagree, so this is an open question, not a rule. One version bans addressing the audience and calls 'let's meet our characters' filler (lines 106 and 950). The other says such lines 'are the labels' (line 315), lets the narrator speak to the viewer (line 341), and ends its own worked script on 'As you read, notice…' (line 405).",
   "statement": "Should story narration ever turn to the student ('let's meet the characters', 'as you read, notice…'), or stay inside the story world?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "106",
     "quote": "Fillers like let's meet our characters feel engaging and do the opposite.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "950",
     "quote": "No student framing language such as \"in this lesson\" or \"you will learn\"",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "315",
     "quote": "They are not padding; they are the labels.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "341",
     "quote": "the narrator in shorter videos can just state the fact or speak to the viewer",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "405",
     "quote": "As you read, notice how each place makes you feel.",
     "verbatim": true
    }
   ],
   "against": "Neither side is tested: \"no child has yet been observed watching one of our films.\" (BrainLift intro video, line 249).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 112,
   "verdict": "keep",
   "reason": "Quotes verbatim: BrainLift intro video lines 41, 291 and 422. Added line 447, which describes the measured previews: characters plus the opening of the plot.",
   "statement": "Should pre-reading media show only the setting and mood, or also the characters, the text's structure and the opening events?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "41",
     "quote": "An intro video shows only the world² and none of the plot³, even when revealing plot would measurably improve comprehension.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "291",
     "quote": "A video that shows only scenery has built atmosphere rather than knowledge and has missed the mark.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "422",
     "quote": "A blanket ban on plot is a position nobody has tested, not a finding.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "447",
     "quote": "story previews consisting of characters plus the opening of the plot produced sizeable comprehension gains, largest for lower-ability readers.",
     "verbatim": true
    }
   ],
   "against": "\"no child has yet been observed watching one of our films.\" (same file, line 249).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 113,
   "verdict": "keep",
   "reason": "Quotes verbatim: BrainLift intro video lines 63 and 297, and the Aladdin Part 2 video outline line 3, under the heading 'Recap'.",
   "statement": "Should a later part's pre-reading media recap the earlier parts, or bring them back through recognition only?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "63",
     "quote": "When a later video must make the child remember, show the place as it now stands and never say what happened there.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "297",
     "quote": "Recapping consolidates; it does not reveal.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/G3/Grade 3 markdown/01 - Fantasy Classics/01 - Aladdin and the Wonderful Lamp/Video Outline - Aladdin and the Wonderful Lamp Part 2.docx",
     "lines": "3 (textutil text)",
     "quote": "Last time, Aladdin was tricked by a magician pretending to be his uncle.",
     "verbatim": true
    }
   ],
   "against": "\"Nobody has tested recognition against recap, on a story told in parts, for a child who has forgotten the earlier one\" (BrainLift intro video, line 62).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 114,
   "verdict": "keep",
   "reason": "Quotes verbatim: BrainLift intro video lines 932 and 301 and Aladdin Part 1 line 13. Part of the disagreement is about scope: one version bans pre-teaching the passage's own taught word, while the other wants the video to teach words.",
   "statement": "Should pre-reading media teach vocabulary that the text will use?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "932",
     "quote": "Do not pre-teach vocabulary that the passage is meant to teach.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "301",
     "quote": "Ideally the video is where a word gets taught, because a visual anchor plus a spoken definition plus later recurrence is worth considerably more than a definition on a card.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
     "lines": "13 (textutil text)",
     "quote": "Video-stamped words (off-limits for the vocab slot): magician, sultan.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 115,
   "verdict": "keep",
   "reason": "Quotes and times verbatim: BrainLift intro video lines 87 and 363 and walkthrough v1 line 25.",
   "statement": "How long should pre-reading media run?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "87",
     "quote": "An intro video is 30 to 40 seconds, and a longer one is weaker, not richer.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "363",
     "quote": "125 spoken words, \\~60 seconds, narrator only, no stamp, no embedded checks.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "25",
     "quote": "A 1:54 film of the riverbank world with captions available",
     "verbatim": true
    }
   ],
   "against": "The short rule is called \"because it is the least evidenced claim we hold.\" (BrainLift intro video, line 87).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 116,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The original misread two columns. The map rates each misconception's 'AP Impact', meaning what it costs on the exam, not how much the exam depends on it. It also gives each one's 'Typical Origin', such as textbooks or everyday language, not where in schooling it starts. The fix corrects both and adds the standards trace. Biology sets concept priority by exam weight (line 5) but chemistry by how foundational a concept is (line 15), so no ranking rule is claimed.",
   "statement": "For each concept, write the end-of-course target, map each known misconception with how persistent it is, what it costs on the exam and where it comes from, trace when each framework teaches the concept, and name the riskiest points in the teaching sequence.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "6 (textutil text)",
     "quote": "TARGET: What students must ultimately understand (the AP Chemistry benchmark)",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "7 (textutil text)",
     "quote": "MISCONCEPTION MAP: Each misconception, rated by persistence and impact, with its origin",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "8 (textutil text)",
     "quote": "STANDARDS TRACE: Comparative table of when/how the concept appears in each framework",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "9 (textutil text)",
     "quote": "RISK ASSESSMENT: The highest-risk points in the instructional sequence",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx",
     "lines": "12 (textutil text)",
     "quote": "AP Impact",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx",
     "lines": "13 (textutil text)",
     "quote": "Typical Origin",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 117,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim: Biology lines 140, 18 and 114 and Cross-Cutting line 31. The original chained two cases into one. The textbook origin belongs to the ATP case (line 140). The lost exam points belong to teleological wording about evolution, whose origin is everyday language and documentaries (line 18). The fix rewords to match. Overlaps candidates 43 and 60.",
   "statement": "Check the teaching materials' own wording for misconceptions: the guidance traces persistent misconceptions to textbook and everyday phrasing, and the end-of-course exam marks down answers that repeat them.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx",
     "lines": "140 (textutil text)",
     "quote": "Biology textbooks; \"high-energy bond\" language",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx",
     "lines": "18 (textutil text)",
     "quote": "Human cognitive architecture; everyday language; nature documentaries",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "31 (textutil text)",
     "quote": "Biology textbooks use \"high-energy phosphate bonds\" language that directly contradicts the correct chemistry.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx",
     "lines": "114 (textutil text)",
     "quote": "Students who write \"the organism evolved to survive\" or \"the species needed to adapt\" lose points.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 118,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, but the reader counted five designs. This pass found the stale line in six of the nine Living World designs: Plants (201), Animal Kingdom (211), Mammals (205), Feathers and Scales (263), Invertebrates (200) and Microorganisms (195). Close to 42. Kept as added evidence that a design's own sweep lines can survive a rule change unchanged.",
   "statement": "When a rule changes, re-run every check on every lesson made under the old rule: in six of nine lesson designs the closing check still described the old gap-fill rule after the rule had changed.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 4. Mammals - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "10 (textutil text)",
     "quote": "Instead of pulling from a section untouched by the other exercises, the cloze is now a SUMMARY of the whole text",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 4. Mammals - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "205 (textutil text)",
     "quote": "Rule 3: cloze on the untouched \"Why Mammals Need Protection\" section, tap-in-order not drag.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "201 (textutil text)",
     "quote": "Rule 3: cloze on the untouched \"Why Plants Matter\" section, tap-in-order not drag.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 7. Invertebrates - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "200 (textutil text)",
     "quote": "Rule 3: cloze on the untouched \"Staying Safe\" section, tap-in-order not drag.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 5. Feathers and Scales - CONNECT - Lesson Design (v3 - prototype-aligned).docx",
     "lines": "263 (textutil text)",
     "quote": "cloze drawn from the one untouched section",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "42",
   "name_bearing_source": false
  },
  {
   "index": 119,
   "verdict": "keep",
   "reason": "Quotes verbatim: lesson-components spec line 20; Plants line 12, with the summary forms at lines 126-128; walkthrough v1 line 151. The against is verified (Microorganisms line 195).",
   "statement": "Put gap-fill blanks on the causal links that hold the text together, spread across the whole text, not on incidental details.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
     "lines": "20 (textutil text)",
     "quote": "exactly four blanks that sit on the links in the child's mental model — so it checks that the child has followed the flow of the story, not incidental detail.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "12 (textutil text)",
     "quote": "It covers the whole text and teaches children what a summary is, instead of a section untouched by the other exercises.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "151",
     "quote": "each blank sits on a link in the mental model (the leaver, the friend, the refusal, the promise).",
     "verbatim": true
    }
   ],
   "against": "The whole-text rule was not applied consistently; a closing line still reads \"Rule 3: cloze on the untouched \"What Are Microorganisms?\" and \"Why They Matter\" sections, tap-in-order not drag.\" (Microorganisms design, line 195).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 120,
   "verdict": "keep",
   "reason": "Quotes verbatim: Chemistry line 88 and Biology lines 38 and 100. Truth 22 (check what a picture implies) covers this. Kept as added evidence that colouring and layout can teach a misconception.",
   "statement": "Check what a diagram's colouring, layout or ordering implies, because styling can teach a misconception the words never state.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "88 (textutil text)",
     "quote": "Do NOT use illustrations that color-code individual atoms to match the bulk substance (orange atoms for copper, blue atoms for water).",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx",
     "lines": "38 (textutil text)",
     "quote": "Scala naturae; popular culture; tree diagrams with humans at top",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx",
     "lines": "100 (textutil text)",
     "quote": "Do NOT oversimplify phylogenetic trees by placing humans at the top/right.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "22",
   "name_bearing_source": false
  },
  {
   "index": 121,
   "verdict": "keep",
   "reason": "Quotes verbatim: four-tier threads line 401 and thematic map 'How to read this' A15. Truth 24 already asks for an estimate to be labelled as one. Kept as added evidence from curriculum plans.",
   "statement": "Mark which entries in a curriculum plan are verified against built materials and which are still indicative.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of G3-8_Threads_FourTier.docx",
     "lines": "401 (textutil text)",
     "quote": "Grade 3 texts are folder-exact; G4–G8 texts and the upper-grade big-idea / vocabulary tiers come from the master sheet and are indicative until those units are built folder-first.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx",
     "lines": "sheet 'How to read this', cell A15",
     "quote": "Grades 7–12 draw on the list's thinner secondary section — those rungs are the first candidates for review.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "24",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
   "lines": "91 (textutil text)",
   "quote": "Wrong -> (1) \"Let's listen to that page again,\" replay the sentence; (2) \"Here is the part of the text with the answer,\" highlight the exact sentence; (3) \"Now choose again.\"",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
   "lines": "39",
   "quote": "the wrong-answer feedback teaches without revealing — it names what the child mixed up (flying belongs to a different story in this unit) and sends them back to the evidence they just heard, rather than printing the key.",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 2. Should We Save the Rainforests - WEIGH - Lesson Design.docx",
   "lines": "211 (textutil text)",
   "quote": "Nudges redirect without giving the answer",
   "ok": true
  },
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
   "lines": "20 (textutil text)",
   "quote": "No em dashes in child-facing wording; US English throughout; no voice input.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
   "lines": "195 (textutil text)",
   "quote": "because showing it inline would answer the question",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Downloads/BrainLift - What makes a good intro video.md",
   "lines": "340",
   "quote": "the video may set up but must not state.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
   "lines": "81 (textutil text)",
   "quote": "not the trust / FIND skill target, which is saved for the Modelling Moment and the Independent Task",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
   "lines": "18 (textutil text)",
   "quote": "two attempts, then reveal.",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
   "lines": "315 (textutil text)",
   "quote": "3rd try and beyond: \"The dashed red statements are the ones to fix. Read them slowly and check them against the text.\"",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
   "lines": "316 (textutil text)",
   "quote": "3rd fail: reveal the full words.",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
   "lines": "89 (textutil text)",
   "quote": "Pure literal FIND: the answer is stated in the sentence just read.",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
   "lines": "8 (textutil text)",
   "quote": "The two \"incorrect\" statements land in different positions in every REFINE, and the Modelling Moment set and the Part 3 set use different orders from each other.",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
   "lines": "271 (textutil text)",
   "quote": "Blank A: must match one of the 3 evidence quotes.",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
   "lines": "333 (textutil text)",
   "quote": "All re-checked against the story text.",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
   "lines": "9 (textutil text)",
   "quote": "Exactly one high-leverage word is taught — chosen to unlock this text and to feed the Phase 3 inference.",
   "ok": true
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
   "lines": "7 (textutil text)",
   "quote": "A short background-knowledge video plays first, building the knowledge the text takes for granted.",
   "ok": false
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Downloads/BrainLift - What makes a good intro video.md",
   "lines": "957",
   "quote": "Nothing is said that is not shown in the matching shot.",
   "ok": true
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Downloads/BrainLift - What makes a good intro video.md",
   "lines": "134",
   "quote": "Illustrations matching the inference a child must make helped, and illustrations conflicting with it hurt, strongest in the youngest readers.",
   "ok": true
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Downloads/BrainLift - What makes a good intro video.md",
   "lines": "352",
   "quote": "A narrator explaining one thing while the visual is still on the last one costs the child both.",
   "ok": true
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
   "lines": "111",
   "quote": "transferred with one split to keep sentences inside the grade-3 length ceiling.",
   "ok": true
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
   "lines": "586",
   "quote": "Ruled: document, don’t cut cosmetically; revisit when canonical videos land.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx",
   "lines": "sheet 'How to read this', cell A15",
   "quote": "417 enumerated titles (the list's own summary said 418; its Grade-5 tab actually enumerates 69, not 70).",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
   "lines": "sheet 'SC Coverage', cell K36 (the stored tally in cells N43, O43, P43 reads RL.3.3.e, 0.0, None for the same component)",
   "quote": "ONLY PLACEMENT OF RL.3.3.e.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.4 - Folk Tales of the World - Lesson Designs/3.4 - Folk Tales - Knowledge Base - Full.xlsx",
   "lines": "sheet 'Folk Tales', cell A2",
   "quote": "Stamped (hot) words are confirmed from the video scripts.",
   "ok": false
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
   "lines": "73 (textutil text)",
   "quote": "(Confirm each word appears in the final passage; drop any that do not and add any missed content words at the same reading level.)",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
   "lines": "39",
   "quote": "Your round-2 review caught nudges that could be clicked past; this one cannot.",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
   "lines": "340 (textutil text)",
   "quote": "every MCQ has one marked answer with both feedback branches.",
   "ok": false
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
   "lines": "86",
   "quote": "Plan which kinds of moves the app can make (build on the child’s idea, ask for evidence, offer another view, scaffold up or down), then choose the actual move from what the child said.",
   "ok": false
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
   "lines": "28 (textutil text)",
   "quote": "This is the first, most-supported turn at the skill before independent practice.",
   "ok": true
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
   "lines": "12",
   "quote": "and then runs that identical four-step rail four times at decreasing support",
   "ok": true
  },
  {
   "truth": 42,
   "effect": "counter",
   "path": "~/Downloads/BrainLift - What makes a good intro video.md",
   "lines": "269",
   "quote": "Regenerating from the knowledge base discards all of that and reintroduces errors that were already caught once.",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
   "lines": "387",
   "quote": "every capture in this document is from the deployed reviewer build, taken this week in student mode with read-to-me on, by walking each screen’s real interactions (including wrong answers).",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
   "lines": "176",
   "quote": "The goal is to measure whether a child’s comprehension and oral language are growing over time, not just whether the child answered one question.",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
   "lines": "353",
   "quote": "whether they own them durably is a different question the course answers with spaced returns, not with a medal.",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
   "lines": "sheet 'Standard components', cell E1",
   "quote": "(the error a Grade 3 child makes)",
   "ok": false
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Downloads/BrainLift - What makes a good intro video.md",
   "lines": "420",
   "quote": "A video that is enjoyed and teaches nothing has not done the job.",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Downloads/BrainLift - What makes a good intro video.md",
   "lines": "22",
   "quote": "Accepted as evidence, refused as advice. Enjoyment is not the reading, SPOV1",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
   "lines": "102",
   "quote": "No response or “I don’t know.” | Down (engage, mimic) | “Is Kitten happy or sad?”",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
   "lines": "327",
   "quote": "the rubric asks for the arc’s heart (the change and the how), not a checklist — a retell, not a quiz wearing a retell’s clothes.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
   "lines": "364 (textutil text)",
   "quote": "carried faithfully, not invented past the KB.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
   "lines": "sheet 'V7.0 Executive Summary', cell A57",
   "quote": "so the context window for Economics atom generation will rely entirely on state curricula and CEE.",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "counter",
   "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
   "lines": "250 (textutil text)",
   "quote": "Tier 1 (absolute prohibitions) should be hard constraints that the system cannot violate.",
   "ok": false
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
   "lines": "sheet 'SC Coverage', cell K96",
   "quote": "RI.3.8.c (paragraph relationships) replaces mistagged RI.3.9.b.",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
   "lines": "56 (textutil text)",
   "quote": "a single wide juxtaposition illustration that does this lesson's real work",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
   "lines": "243 (textutil text)",
   "quote": "If any prohibited phrase appears, it should be flagged and corrected before publication.",
   "ok": true
  }
 ]
}
```
