# read:cloud-curriculum

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "cloud-curriculum",
 "coverage": {
  "read": [
   "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/ (all 7 files: the coherence .md and the Biology, Chemistry, Physics and Cross-Cutting Synthesis .docx in full; Science_Curriculum_Review_Workbook.xlsx Summary, G3 sheet and tag tallies across all grade sheets; Consensus social science standards.xlsx Methodology Notes, V7.0 Executive Summary, Retired Standards, Social Studies Skills and national-standards headers)",
   "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx (full)",
   "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/ (Aladdin Parts 1 and 2 in full; rules, change notes and sweep sections of the other 9 designs; knowledge base Overview, header rows and first lesson row)",
   "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/ (Plants and Rainforests designs in full; rules and sweep sections of the other 7; knowledge base Overview)",
   "~/Downloads/5. Curriculum/Instruction/3.3 - Ancient Civilisations - Lesson Designs/ and 3.4 - Folk Tales of the World - Lesson Designs/ (knowledge base Overview sheets; Folk Tales header and first row)",
   "~/Downloads/5. Curriculum/Instruction/1. Procedures (MM and P3)/1. HTML Structures/ (decoded bundled templates of the FIND, DECODE and MAIN IDEA modelling pages and Magic Doors)",
   "~/Downloads/5. Curriculum/Curriculum maps/ (_G3 curriculum Map.xlsx all five sheets; G3 Standards and Standard components.xlsx in full; ' K-8 curriculum map.xlsx' Overview, Grade 3 sheet and Knowledge Threads; Archive/_OLD G3 map coverage tally; G4 map sheet list)",
   "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/ (both .docx in full; Grade_3-12 thematic map explanatory and coverage sheets; G3-8 knowledge threads descriptions; TEA G3 Comparison; working-draft overview and sheet headers)",
   "~/Downloads/5. Curriculum/Texts/G3/ (markdown texts scanned for metadata, word counts and banned misconception phrasing; archived vs current history texts diffed; three video outlines; one compiled PDF sampled; unit workbook sheet lists; Prince and the Pauper KB overviews compared; Archive 'Claude Notes on Criticism poems_.docx' in full)",
   "~/Downloads/5. Curriculum/Texts/G4 DRAFT/ (word counts, rationale-note scan and banned-phrase scan of all drafts and rewrites; Ecosystems draft compared with its rewrite)",
   "~/Downloads/BrainLift - What makes a good intro video.md (full, both versions and the definition tabs)",
   "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md (full)",
   "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md (full text, embedded images stripped)",
   "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md (full text, embedded images stripped)",
   "~/Downloads/_G3 curriculum Map.xlsx - Curric Map.csv (header and note columns)"
  ],
  "skipped": [
   "~/Downloads/5-Curriculum/ — older copy, excluded by the task",
   "Consensus social science standards.xlsx Raw Standards, State Detail, State Supplement and CKHG Reference sheets and the 2.8 MB comments part — data dumps",
   "Science_Curriculum_Review_Workbook.xlsx per-grade atom rows beyond the G3 sample and the tag counts — data",
   "' K-8 curriculum map.xlsx' grade sheets other than Grade 3 — data rows",
   "Texts/G3/Grade 3 word docs/*.docx and Grade 3 markdown/PDF/*.pdf — duplicates of the markdown texts (one PDF sampled to confirm)",
   "Texts/G4 DRAFT prose — curriculum content rather than findings; scanned, not read in full",
   "Procedure HTML independent-task bundles — same rails and content as the lesson designs",
   "Other files in ~/Downloads (zips, review PDF, Maps of the Market export) — outside this direction's scope"
  ],
  "notes": "Line references: .docx = line number in textutil -convert txt -stdout output; .xlsx = sheet and cell; .md and .csv = raw file line (walkthrough lines are raw-file lines with embedded images left in place). Several files carry team members' names inside the text but not in their paths; quotes were trimmed to leave names out. The only name-like path is the archived 'Claude Notes on Criticism poems_.docx' (the assistant's name); the three candidates that rely on it are flagged name_bearing_source. Contradictions inside the sources: the intro-video rules file holds two versions that disagree on plot, recap, vocabulary, runtime and audience address (logged as open questions); five Living World designs state a new whole-text gap-fill rule in the header but an old 'untouched section' rule in their closing check; a static coverage tally reads zero for components the same sheet assigns to lessons; the mandated-text comparison predates folk tales later added; a G4 'rewrite' file is word-for-word identical to its draft and keeps banned energy wording. AP evidence in this scope is limited to the science misconception guidance (exam weights, exam-setter distractor design, examiner-report errors). Measurements made by this sweep rather than by the project (banned-phrase scan, rewrite comparison, stale rule lines, component and coverage tallies) are labelled as such in found_by."
 },
 "candidates": [
  {
   "statement": "Write multiple-choice options of equal length and register, never let the key be the longest, give at least four plausible options, and avoid yes/no items and options that echo the stem.",
   "kind": "adopted rule",
   "found_by": "House multiple-choice discipline in every science lesson design; the built lesson padded distractors so the key was never longest; a review of a knowledge-item pilot fixed unbalanced option lengths.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "10 (textutil text)",
     "quote": "Rule 2 — Multiple-choice discipline. The correct option rotates across A/B/C/D; all four options are the same length and register; each item carries one deliberate misconception distractor."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "36",
     "quote": "≥4 plausible options; no yes/no; no stem echo; key never the longest | Guessable items measure test-wiseness, not comprehension"
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'V7.0 Executive Summary', cell A75",
     "quote": "Two fixes applied: em-dashes removed, MCQ lengths balanced."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    8
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Build at least one distractor in each knowledge item from a known misconception, because a student who can state the right definition may still choose the misconception when it is offered.",
   "kind": "adopted rule",
   "found_by": "Implementation recommendation in the cross-subject misconception synthesis; exam notes record that the exam setter builds distractors around the same misconceptions; built vocabulary checks code each distractor as a misconception.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "248 (textutil text)",
     "quote": "Assessment items should include distractors based on known misconceptions. A student who can state the correct definition but selects the misconception when presented as a plausible alternative does not truly hold the correct understanding."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "240 (textutil text)",
     "quote": "The College Board explicitly designs multiple-choice distractors around the \"bond breaking releases energy\" misconception and the teleological \"atoms want full shells\" reasoning."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "67",
     "quote": "Each distractor is a coded misconception (a happy place, a cheerful place, a cozy-ordinary thing) and its feedback names the mismatch"
    }
   ],
   "against": "Quick are-you-reading checks are kept free of trick distractors: \"4 short plausible options, one stated in the text, no trick distractors.\" (3.1 - 3. Aladdin ... Part 3 design, line 97), so the rule is for knowledge items, not attention checks.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Include distractors that are true elsewhere in the text, or were true earlier, but do not answer this question, so the item tests relevance and tracking rather than spotting a falsehood.",
   "kind": "adopted rule",
   "found_by": "Specified for the summary gap-fill in the lesson-components spec, used as the why-wrong distractor in an evidence hunt, and adopted for the retell in the built lesson.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
     "lines": "20 (textutil text)",
     "quote": "The taught word features in it, and “true-earlier-but-not-now” distractors test that the child tracked how things changed."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "141 (textutil text)",
     "quote": "a true fact, but not the job of a part."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "151",
     "quote": "Distractors are true-of-the-story-but-wrong-here, which is what separates a retrieval task from a guessing game."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "In a gap-fill, draw every choice for a gap from the same category, so grammar or elimination cannot decide it and only understanding can.",
   "kind": "adopted rule",
   "found_by": "Maze-format retell adopted in the built lesson, with the rationale that same-category choices block syntax and elimination guessing.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "46",
     "quote": "Cloze retell; each gap opens exactly 3 same-category choices | Same-category trios kill syntax and elimination guessing — only the story model decides"
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "337",
     "quote": "A cloze earns its keep when context genuinely forces the selection"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make every false statement in a true/false or sorting task one the text directly shows to be false, not merely one the text does not mention.",
   "kind": "adopted rule",
   "found_by": "Mandatory accuracy-and-soundness sweep in the lesson designs checks each incorrect statement against the text.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
     "lines": "338 (textutil text)",
     "quote": "Each Refine step has exactly 6 statements, 4 true and 2 incorrect; the incorrect ones are falsifiable directly from the text."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "179 (textutil text)",
     "quote": "Note: the don't-fit words are exactly the things Aladdin does NOT ask for, which is what the text points out."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "For an inference question, the answer must be supported by the text but not written in it; if the text states the answer, the item only tests locating.",
   "kind": "adopted rule",
   "found_by": "Soundness sweep of the inference lesson designs checks that each answer is supported, not stated.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "354 (textutil text)",
     "quote": "Both answers supported by the text, not stated."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "217 (textutil text)",
     "quote": "spotted that the writer never tells us why. We work it out from the words Aladdin says and does."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep quoted evidence and the student's inference in separate slots: the quote slot holds only the text's exact words, and inference words never go inside it.",
   "kind": "adopted rule",
   "found_by": "House verbatim rule in every lesson design's production note and sweep, rebuilt as a two-blank write frame in the live lesson.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "350 (textutil text)",
     "quote": "Inference words (safe, desperate, ambitious, determined) live only in the \"I know…\" / \"So I think…\" steps, never in \"The text says…\"."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "261",
     "quote": "the text’s words go inside quotation marks, and the mood word can never hide there — the inference has to be produced, not retrieved."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "189 (textutil text)",
     "quote": "Any inference sits in State/Refine/Extra thinking, never inside a \"the text says\" quote."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Decide on purpose whether a question repeats the text's wording or paraphrases it: a mirrored question can be answered by matching words, while a paraphrased one needs understanding.",
   "kind": "adopted rule",
   "found_by": "The locating standard was split into two components, each naming the failure it catches.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
     "lines": "sheet 'Standard components', cell D2",
     "quote": "Find explicitly stated information when the question uses similar wording to the text"
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
     "lines": "sheet 'Standard components', cell E3",
     "quote": "Child can only find answers when the question words exactly match the text. Fails when synonyms or rephrasing are used."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Teach reading the question as a step of its own, marking the word that says what to do and the word that names the target, and build that step's wrong options from the usual misreadings.",
   "kind": "adopted rule",
   "found_by": "First step of every reading procedure in the designs; in the built lesson its distractors were taken from how students misread questions.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "241",
     "quote": "Reading the question is a taught step, not a formality — the distractors are the exact ways a grade-3 reader misreads a question (answers the previous question; grabs a familiar name; answers about the wrong place)."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "133 (textutil text)",
     "quote": "PROCESS word: circle \"Why\" -> draw a line -> label \"Which words?\" (we hunt for the writer's actual words as evidence)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "In the independent task, use the worked example's answers as distractors, so a student who copies the model instead of reading the new section is caught.",
   "kind": "adopted rule",
   "found_by": "Inference lesson design: the independent word bank's wrong options are the modelled section's right answers, with feedback naming the difference.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "283 (textutil text)",
     "quote": "Note: the don't-fit words are the cave reasons from the Modelling Moment. Here Aladdin is reaching for something new."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "282 (textutil text)",
     "quote": "\"Getting home was why Aladdin acted in the cave. Is that what he is reaching for now that he wants to marry the princess?\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When students classify, include trap cases whose surface appearance points to the wrong group, so they must apply the deciding rule.",
   "kind": "adopted rule",
   "found_by": "Classification lesson design and its soundness sweep.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 3. The Animal Kingdom - SORT - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "205 (textutil text)",
     "quote": "The trap animals (whale, jellyfish, bat) force the child to apply the rule over appearance."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 3. The Animal Kingdom - SORT - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "161 (textutil text)",
     "quote": "Step 5 — Extra thinking (the trap beat): appearance can fool you."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When students first meet a distinction, use only clear-cut cases that carry a visible marker, and keep borderline cases for later.",
   "kind": "adopted rule",
   "found_by": "Fact/opinion checks in both persuasive-text lesson sweeps.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 2. Should We Save the Rainforests - WEIGH - Lesson Design.docx",
     "lines": "221 (textutil text)",
     "quote": "each sentence sorted as OPINION carries a feeling-word (\"I feel,\" \"amazes me,\" \"I am worried,\" \"I believe\"). No borderline cases are used at first exposure."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 8. Whose World Is It - WEIGH - Lesson Design.docx",
     "lines": "217 (textutil text)",
     "quote": "No borderline cases are used in the modelled step."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Sort a student's evidence picks into the key clue, a relevant but weaker clue and an irrelevant one, give each its own feedback, and then ask which clue is strongest.",
   "kind": "adopted rule",
   "found_by": "Open clue-hunt design in the inference lessons; the standard component for choosing evidence names an interesting or nearby detail as the typical wrong pick.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "146 (textutil text)",
     "quote": "Each phrase is labelled CLUE / INTERESTING / DISTRACTOR."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "159 (textutil text)",
     "quote": "\"Some evidence is better than others. Tap what you think best describes what Aladdin wants.\""
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
     "lines": "sheet 'Standard components', cell E7",
     "quote": "Child picks a random, interesting, or nearby detail instead of the one that is relevant to the question."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A check given straight after teaching shows the student was following, not that they remember; retrieval needs a gap the student fills from memory, such as a question on an earlier lesson asked before new teaching.",
   "kind": "adopted rule",
   "found_by": "Media-design synthesis drawing on retrieval research (Roediger and Karpicke 2006; Cepeda et al. 2006; no DOI or URL given in the source).",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "430",
     "quote": "The sync check after a video is a check on attention, not on memory."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "339",
     "quote": "Real retrieval needs a gap the child fills."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "493",
     "quote": "retrieving strengthens retention more than re-reading."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Ask students to explain their reasoning as well as give an answer, because explanation exposes misconceptions that answer-only items let through.",
   "kind": "adopted rule",
   "found_by": "Exam-relevance note in the physics misconception guidance; response-type synthesis for comprehension.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx",
     "lines": "125 (textutil text)",
     "quote": "The free-response format specifically exposes conceptual misconceptions because students must explain their reasoning, not just calculate."
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "30",
     "quote": "If a child never has to compose or explain an answer, the app cannot tell whether the child understood"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Pick the response type a skill needs (recognise, complete or produce) before counting responses, and accept the rate it allows: about 4 to 6 a minute for new learning, 8 to 12 for review, and 1 or fewer for open answers.",
   "kind": "external research",
   "found_by": "Research synthesis citing MacSuga-Gage and Simonsen (2015), https://doi.org/10.1353/etc.2015.0009, with the per-minute targets from the Council for Exceptional Children (1987) as cited there.",
   "evidence": [
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "119",
     "quote": "The commonly cited targets are about four to six responses per minute when a child is learning something new, about eight to twelve per minute when practicing material already taught, and about one per minute or fewer for open responses that require composing or reasoning."
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "23",
     "quote": "A high number of responses per minute is not evidence of quality if the app reached that number by asking only recognition questions."
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "199",
     "quote": "https://doi.org/10.1353/etc.2015.0009"
    }
   ],
   "against": "The targets are second-hand: \"Council for Exceptional Children (1987), as cited in MacSuga-Gage and Simonsen (2015).\" (same file, line 120).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make the reply to a student's answer build on what the student said; a reply that would read the same whatever the answer was is not feedback and should be rebuilt.",
   "kind": "external research",
   "found_by": "Synthesis on the third turn of classroom talk citing Nystrand et al. (1997, no DOI) and Shute (2008), https://doi.org/10.3102/0034654307313795.",
   "evidence": [
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "71",
     "quote": "A reply that would read the same no matter what the child answered is not a third turn."
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "87",
     "quote": "If the reply would be the same no matter what the child said, it is not a real response and should be rebuilt."
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "18",
     "quote": "Most instruction, and most software, stops after the child answers and offers only a confirmation such as “good” before moving on, which is the weakest use of the moment (Shute, 2008)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    11
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write the follow-up in advance for each kind of answer (full, brief, partly right, off track and silent), challenging a full answer further and stepping support down for the others.",
   "kind": "adopted rule",
   "found_by": "Two independent sources reach the same five branches: a research-based conversation table (Zucker et al. 2020, https://doi.org/10.1002/trtr.1943) and the built lesson's standing dialogue rule.",
   "evidence": [
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "90",
     "quote": "When a child answers easily, scaffold up by challenging for reasoning, alternatives, generalizing, or extending. When a child struggles, scaffold down by giving feedback, reframing, supplying an answer, offering a model to mimic, or simply keeping the child engaged (Zucker et al., 2020)."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "47",
     "quote": "Open answers route to full / brief / partial / off-track / silent paths | Every path teaches; the silent child is taught first, then re-asked easier"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    55
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When an answer is partly right, say which part is right and ask only for the missing part.",
   "kind": "adopted rule",
   "found_by": "Feedback rule for the built lesson's two-part rubric; the same move appears in the research-based conversation table.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "311",
     "quote": "Feedback on a half-answer names the part the child *did* give and asks only for the missing one."
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "100",
     "quote": "“The snow is part of it. Look at her hands in the picture. What is missing?”"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a point must be learned exactly, prompt the student to produce it rather than restating it for them, because students often miss a restatement.",
   "kind": "external research",
   "found_by": "Synthesis citing Lyster and Saito (2010), https://doi.org/10.1017/S0272263109990520, and Lyster and Ranta (1997).",
   "evidence": [
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "70",
     "quote": "because children often do not notice a recast, it does not reliably teach one specific point (Lyster & Saito, 2010). When something has to be learned exactly, prompting the child to say it again in their own words works better."
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "167",
     "quote": "Prompts more often lead the child to produce a corrected response."
    }
   ],
   "against": "\"Drawn from second-language classrooms, so applied here by analogy to early oral language.\" (same file, line 168).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Advance a hint ladder only when the answer has changed since the last try, so resubmitting the same answer cannot unlock more help.",
   "kind": "adopted rule",
   "found_by": "Feedback ladder specified for the typed sentence frame in the inference lesson design.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "311 (textutil text)",
     "quote": "FEEDBACK LADDER (only advances if the answer changed since the last try):"
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "313 (textutil text)",
     "quote": "Empty / unchanged: \"Have another go at your answer first, then tap I'm done again.\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "After a practice item with retries, measure on a fresh parallel item: the first form teaches, the second shows whether the correction took.",
   "kind": "adopted rule",
   "found_by": "Two-form design for vocabulary checks and the summary gap-fill in the components spec and every lesson design, carried into the built lesson.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
     "lines": "20 (textutil text)",
     "quote": "Runs as two parallel forms; the second is shown if the first is wrong."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
     "lines": "44 (textutil text)",
     "quote": "FORM 2 (second chance / clean measure)"
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "67",
     "quote": "form 1 corrects, form 2 gives a cleaner read on whether the correction took."
    }
   ],
   "against": "The platform could not always deliver it: \"The doc’s FORM 2 has no renderer slot — the retry ladder substitutes (accepted deviation, logged).\" (WITW walkthrough v1, line 155).",
   "adds_to_existing": [
    4,
    14
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When help or the answer is given after held tries, label it as help, and have the end screen claim completion, never mastery.",
   "kind": "adopted rule",
   "found_by": "Review-standards rule enforced by a validator in the built lesson.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "33",
     "quote": "After held tries, help is offered and named as help | A reveal dressed as a win teaches that trying is optional"
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "50",
     "quote": "The end screen claims completion, never mastery | False mastery claims teach children and parents to distrust the product"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Score a stretch question that asks for thinking beyond the first answer generously, so going further is never punished.",
   "kind": "adopted rule",
   "found_by": "Standing feedback ruling applied to the 'and what else?' beat in the built lesson.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "271",
     "quote": "Scoring is deliberately generous: this beat rewards thinking beyond the first answer; it must never punish it."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When students may bring their own example, judge whether it holds together rather than whether it matches the planned examples, and give credit for noticing differences.",
   "kind": "adopted rule",
   "found_by": "Cross-text transfer rubric in the built lesson.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "303",
     "quote": "the rubric judges whether the answer holds together, never whether we recognize the story"
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "305",
     "quote": "the rubric rewards noticing differences above matching our list."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    13,
    56
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count a taught word as owned only when the student uses it, with evidence, about new content; recognising it or echoing its definition does not count.",
   "kind": "adopted rule",
   "found_by": "Show-what-you-know station design in the built lesson.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "285",
     "quote": "Vocabulary is only owned when it is produced about new content"
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "19",
     "quote": "Recognition can be guessed; production shows the word or idea is owned"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Feedback must never reveal or point to parts of the text the student has not read yet.",
   "kind": "adopted rule",
   "found_by": "Spoiler discipline listed among the parameters checked in the built lesson.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "32",
     "quote": "Glossed words and sync-checked answers are never re-asked; no unread content in feedback | Spoilers turn reading into confirmation; re-asking stamps burns trust"
    }
   ],
   "against": "The earlier walkthrough quotes a page-one wrong-answer reply that points ahead in the text: (“the river comes later, at the end of his wander…”) (WITW walkthrough v1, line 123).",
   "adds_to_existing": [
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep corrective feedback short (40 words or fewer), tied to the evidence, and placed directly under the option the student chose.",
   "kind": "adopted rule",
   "found_by": "House corrective-feedback bar; the placement came from a review note and was made engine-wide.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "127",
     "quote": "The feedback register is the corrective-feedback bar: ≤40 words, evidence-anchored, teaches without revealing."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "30",
     "quote": "Wrong-answer feedback lands directly under the option tapped | The correction attaches to the exact act, not to the screen in general"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Place quick are-you-reading checks at moments of change, keep them literal and answerable in about two seconds from the sentence just read, and give four short options that all look plausible to a drifting reader.",
   "kind": "adopted rule",
   "found_by": "First-read check layer added to every inference lesson design and kept in the built lesson.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 10. The Wind in the Willows, Part 3 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "85 (textutil text)",
     "quote": "Pure literal retrieval, answered in about 2 seconds, placed at moments of CHANGE."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "89 (textutil text)",
     "quote": "Four short options, all plausible to a drifting child, only one stated in the text."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "41",
     "quote": "Drifting readers lose the thread at changes; look-back must be actually possible"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    7
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep questions off the screen while students read, bring the check in only after the reading stretch, and keep the text visible whenever a question asks them to look back.",
   "kind": "adopted rule",
   "found_by": "A review note said questions had been overdone to the detriment of the mental model; the build made story-only pages and checks beside the still-visible text engine-wide.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "125",
     "quote": "your “we’ve overdone questions to the detriment of the mental model” note is why the question waits off-screen."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "40",
     "quote": "Story-only pages; the check appears only after “I’m done reading” | Reading needs stretches that are just reading; questions wait off-screen"
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "13",
     "quote": "and the passage always visible whenever a question asks the child to look back at it."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    7
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count the answer moments in each lesson and hold them to a budget; a built lesson carried 38 against a target of about 31, after a review had flagged lessons with 55.",
   "kind": "measured",
   "found_by": "Reviews counted discrete answer moments per lesson.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "14",
     "quote": "The lesson carries 38 discrete answer moments — in line with its unit neighbours and far below the 55-ask lessons your earlier review flagged."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "35",
     "quote": "38 discrete answer moments this lesson (target \\~31) | Checks that interrupt every paragraph become compliance theater"
    }
   ],
   "against": "The target stayed open and items were not cut to meet it: \"Ruled: document, don’t cut cosmetically; revisit when canonical videos land.\" (WITW walkthrough v2, line 586).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "In a worked example, model every step except the final thinking move and let the student make that move with the modelled steps still visible.",
   "kind": "adopted rule",
   "found_by": "Lesson-components spec for the modelling block; the built lesson kept it and diverged from per-lesson designs that typed the full answer.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
     "lines": "26 (textutil text)",
     "quote": "modelling every step except the final thinking move. It sounds like genuine thinking, not a lecture."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
     "lines": "28 (textutil text)",
     "quote": "The child completes the final step only — one typed gap that carries the inference (“…so I think ___”) — with the modelled steps kept visible beside it."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "207",
     "quote": "even in the I-do the last thinking move is the child’s, a small production that turns watching into doing"
    }
   ],
   "against": "The per-lesson designs did the opposite: \"The design doc’s Modelling Moment ends with the full model answer typed to completion; we leave the last word to the child\" (WITW walkthrough v1, line 211).",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Model the decision, not just the answer: show weaker options being weighed and rejected with reasons before the best one is chosen.",
   "kind": "adopted rule",
   "found_by": "Worked-example design in the built lesson, citing the rule that revealing an answer is not modelling.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "197",
     "quote": "This is modelling the thinking, not the answer."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "16",
     "quote": "Scout weighs and rejects clues out loud | A model showing only the winning move teaches that reading is easy for other people"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make guided practice a partly done task the student finishes, not a hint and not a second demonstration.",
   "kind": "adopted rule",
   "found_by": "Guided station added to the built lesson under its gradual-release standard.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "223",
     "quote": "A we-do is a partial the child completes — not a hint, and not a second demonstration."
    }
   ],
   "against": "The lesson designs had no guided stage at all: \"design docs go straight from Modelling Moment to Independent Task — they contain no we-do.\" (WITW walkthrough v1, line 227).",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Run the worked example, guided practice and independent task on different sections or material, so no stage pre-answers another and the independent task is transfer rather than rehearsal.",
   "kind": "adopted rule",
   "found_by": "Checked in every lesson design's soundness sweep and listed as a checked parameter in the built lesson.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
     "lines": "334 (textutil text)",
     "quote": "Same FIND rail, different section, fresh evidence."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "197 (textutil text)",
     "quote": "MM = roots/stem/leaves; IP = seeds/flowers; cloze = \"Why Plants Matter\" — three different parts of the text."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "34",
     "quote": "Repeating on the same evidence is rehearsal; new evidence is transfer"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    41,
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Once a component is canonical, nothing later may contradict it or re-ask its questions; keep an explicit off-limits list, and update the lessons when the canonical piece changes.",
   "kind": "adopted rule",
   "found_by": "Lesson-components spec; every design lists what is off-limits for re-asking; the map records a lesson extended to match a revised video.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
     "lines": "7 (textutil text)",
     "quote": "The video is canonical: no later component may contradict it or re-ask its questions."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
     "lines": "28 (textutil text)",
     "quote": "Off-limits for re-asking: the two sync checks above; the sultan and magician stamped definitions; naming or ordering the story pattern in the abstract."
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'SC Coverage', cell K3",
     "quote": "Extended 2 Jul 2026 to match the revised BG video, which tells the child Part 1 reaches the 'but'."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    41
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Fade support in steps: highlight evidence in the worked example, withdraw it in the independent task, and across a unit replace restated structure with retrieval as students come to hold it.",
   "kind": "adopted rule",
   "found_by": "Lesson-design sweep of guided versus released steps; media rule on fading citing Gurlitt and Renkl (2008) on expertise reversal (no DOI given).",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
     "lines": "335 (textutil text)",
     "quote": "The Modelling Moment guides (pre-glowed evidence, auto-highlighted Refine, teacher whiteboard); the Independent Task releases (unassisted hunt with feedback ladder, child-written 3-blank frame, judge-then-check Refine with retry ladder)."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "327",
     "quote": "The knowledge is permanent; the explaining is temporary."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "457",
     "quote": "This is the evidence base for fading: more structure early, less later (SPOV 8)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make the first lesson on a new procedure lighter, with a smaller set, and build it so later lessons only widen the set instead of rebuilding the lesson.",
   "kind": "adopted rule",
   "found_by": "Design notes in the first and second persuasive-text lessons and in a comparison lesson; the second lesson applied the planned fade.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 2. Should We Save the Rainforests - WEIGH - Lesson Design.docx",
     "lines": "8 (textutil text)",
     "quote": "This is the first WEIGH lesson in the unit, so the \"Find the opinions\" task is deliberately lightened: the child is shown a reduced set of three sentences (a mix of fact and opinion) rather than the whole text at once"
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 8. Whose World Is It - WEIGH - Lesson Design.docx",
     "lines": "8 (textutil text)",
     "quote": "This is the second WEIGH lesson in the unit (after Should We Save the Rainforests?), so the fade applies: the \"Find the opinions\" task is no longer reduced to three options — the child taps opinions straight from the whole section."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 5. Feathers and Scales - CONNECT - Lesson Design (v3 - prototype-aligned).docx",
     "lines": "8 (textutil text)",
     "quote": "(easier to fade than to build up)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Open each lesson by having students recall the previous lesson's key idea, then thread it into the new one.",
   "kind": "adopted rule",
   "found_by": "Unit knowledge-base overviews.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx",
     "lines": "sheet 'Overview', cell B35",
     "quote": "Each lesson opens by re-firing the previous part's key threshold, then threads it into the new one."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - The Living World - Complete KB.xlsx",
     "lines": "sheet 'Overview', cell B36",
     "quote": "Each lesson opens by recalling the prior part's knowledge, then threads it into the new threshold."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give each lesson one key idea that the student restates with evidence at the close, and check built lessons for that closing statement: a conformance review found it missing from every lesson.",
   "kind": "measured",
   "found_by": "Conformance review of built lessons against the knowledge base.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx",
     "lines": "sheet 'Overview', cell A3",
     "quote": "each lesson teaches ONE key threshold (in red) that the child should walk away knowing, with a second threshold carried subtly."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx",
     "lines": "sheet 'Overview', cell B36",
     "quote": "so each child leaves having restated the threshold with evidence."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "345",
     "quote": "your conformance review found it missing everywhere; it now lands in every lesson"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Before the first read, give one purpose for reading that points at the evidence the later task will use.",
   "kind": "adopted rule",
   "found_by": "Lesson-components spec and the built lesson's reading-goal screen.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
     "lines": "11 (textutil text)",
     "quote": "One narrated sentence that focuses the child before the first read — the lesson's single watch-for."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "109",
     "quote": "Purpose-for-reading, set before the text and pointed at exactly the evidence the skill work will need."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Choose a taught word that names something the text never names, keep it out of everything before the final task, and require the student to produce it there.",
   "kind": "adopted rule",
   "found_by": "Vocabulary choice in the lesson designs, checked in their sweeps and kept in the built lesson.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
     "lines": "336 (textutil text)",
     "quote": "Betrayal / betrayed never appears in the video, the vocab-to-story bridge, the pauses, or the cloze bank; it is surfaced only in the Independent Task (Step 3 blank C and Step 5 help), where the child uses it to cash the answer."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "23",
     "quote": "*eerie* is deliberately absent from the passage | The child must produce the word to name a mood the writer never named"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Define each word in the sense the text uses it, and use one identical definition wherever the word appears, checked automatically.",
   "kind": "adopted rule",
   "found_by": "Lesson-components spec; a review rule enforced by a validator in the built lesson.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
     "lines": "16 (textutil text)",
     "quote": "Tappable words in the passage, each giving a student-friendly definition in the sense used here."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "79",
     "quote": "definition identical, word for word, on the card, in every passage glossary, and in the wrap — the one-definition rule from your reviews, enforced by a validator."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "37",
     "quote": "One definition per word, identical everywhere it appears | Definition drift makes the child re-learn the word each time"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Use the same words and framing for an idea every time it returns, in every subject, because loose wording in one place can re-teach a misconception another place fixed.",
   "kind": "adopted rule",
   "found_by": "Media compression rule, cross-subject coherence guidance, and the misconception synthesis tracing a misconception re-taught by another subject's materials.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "338",
     "quote": "Always use the same vocabulary to talk about an idea already taught so as not to confuse."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md",
     "lines": "14",
     "quote": "the Read/Write lesson should be consistent with how it was framed in the subject app — vocabulary, level of nuance, framing."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "31 (textutil text)",
     "quote": "Even students who learned the correct chemistry are re-taught the misconception in biology class."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Plan around ten or more meaningful, spaced encounters with each word a student must own; one meeting is a first encounter, not teaching.",
   "kind": "external research",
   "found_by": "Research summary citing Beck and McKeown and the Elleman et al. (2009) meta-analysis (no DOI or URL given); the built lesson tracks about 10–12 returns per word.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "428",
     "quote": "Around ten or more meaningful encounters are needed to own a word, and vocabulary gains appear far more strongly on custom measures than standardised ones."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "487",
     "quote": "vocabulary instruction helped comprehension on custom measures (d \\= 0.50) far more than on standardised ones (d \\= 0.10)"
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "22",
     "quote": "Each word returns \\~10–12 times across the unit | One meeting never sticks; spaced returns in fresh contexts build ownership"
    }
   ],
   "against": "Vocabulary gains carry only partly into comprehension: \"the correlation between a study's vocabulary gain and its comprehension gain was only modest (r \\= .43).\" (BrainLift intro video, line 487).",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "List each unit's technical terms in its knowledge base, teach them before reading, and carry them forward with spaced recall.",
   "kind": "adopted rule",
   "found_by": "Fix list in the four-tier curriculum thread map.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of G3-8_Threads_FourTier.docx",
     "lines": "396 (textutil text)",
     "quote": "Each unit's technical terminology (above) must be listed in the KB, taught before reading, and carried with spaced recall"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Teach a domain word directly when the whole domain is new to the student, because surrounding text cannot reveal its meaning when the concepts around it are new too.",
   "kind": "adopted rule",
   "found_by": "Failure note for the domain-vocabulary component of the reading standards.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
     "lines": "sheet 'Standard components', cell E46",
     "quote": "Child can't use context when the whole domain is unfamiliar. The surrounding text doesn't help because the concepts are also new."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18,
    20
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Break a word into meaningful parts only where it really has them, because invented splits teach false parts.",
   "kind": "adopted rule",
   "found_by": "Vocabulary card spec applied in the built lesson.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "55",
     "quote": "The family stage teaches only real derivations — *eerily, eeriness* — never invented splits, because syllables are not morphemes."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "21",
     "quote": "Syllable breaks for saying; meaning-parts only when real | Inventing splits (ee+rie) would teach false word-parts"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Teach a concept with examples that differ on the surface but share its one deep feature, and with near-miss non-examples that each fail for one nameable reason.",
   "kind": "adopted rule",
   "found_by": "Minimal-pair discrimination in the built lesson's vocabulary checks; physics guidance on varying demonstrations.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "77",
     "quote": "three surface-different scenes, one deep feature, with near-miss words — *careful, tired, polite* — each wrong for exactly one nameable reason"
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "20",
     "quote": "Each wrong option differs by one nameable feature | Discrimination teaches a concept’s edges; each feedback names the one mismatch"
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx",
     "lines": "93 (textutil text)",
     "quote": "Do NOT demonstrate Newton's third law only with stationary examples (book on table). Include MOVING examples (collisions, pushing off a wall on roller skates)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Teach what a concept is not, explicitly and at the moment it is introduced, with a counterexample; the guidance found no standards framework that does this.",
   "kind": "adopted rule",
   "found_by": "Cross-subject misconception synthesis; the science knowledge items carry the required negative definition from Grade 3.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "244 (textutil text)",
     "quote": "Every concept area has things that students need to be told are NOT true. These are as important as the positive definitions."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "77 (textutil text)",
     "quote": "No framework currently includes this \"negative definition.\""
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Science_Curriculum_Review_Workbook.xlsx",
     "lines": "sheet 'G3', cell D3",
     "quote": "[New — D1 Section 2.1 negative definition; required at Grade 3]"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Hold back a technical term whose everyday meaning misleads until the concept it names is actually needed.",
   "kind": "adopted rule",
   "found_by": "Early-grade guidance in the biology misconception card.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx",
     "lines": "206 (textutil text)",
     "quote": "Do NOT introduce \"dominant\" and \"recessive\" at this level — the terms carry too much everyday baggage and the concepts are not needed yet."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Get a concept right the first time it appears, because the gap before a correct explanation lets a wrong default form and first introduction is the riskiest point.",
   "kind": "adopted rule",
   "found_by": "Risk assessments in the misconception prevention cards.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "76 (textutil text)",
     "quote": "During this gap, students build macroscopic mental models that become the default."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "199 (textutil text)",
     "quote": "Highest risk: The moment bonding mechanisms are first taught (typically grades 9-10)."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "64 (textutil text)",
     "quote": "energy conservation must be taught at the SAME TIME energy is introduced (as the Franklin Standards do at grade 3), not as a later addition."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Present every simplified model or diagram with a short note that it is a simplification and what it leaves out.",
   "kind": "adopted rule",
   "found_by": "Cross-subject misconception synthesis and the biology card.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "119 (textutil text)",
     "quote": "Every model should carry an explicit health warning"
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "121 (textutil text)",
     "quote": "Whenever an LLM system presents a model (diagram, equation, simplified explanation), it MUST include a brief framing statement indicating that the model is a simplification."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx",
     "lines": "260 (textutil text)",
     "quote": "Every time a cell diagram is shown, include the explicit framing"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When a full answer is beyond a student's level, give a true partial answer and say more comes later, keeping the same conceptual foundation at every level rather than a false simplification.",
   "kind": "adopted rule",
   "found_by": "Grade-adapted model answers in the misconception cards; implementation recommendation in the synthesis.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "124 (textutil text)",
     "quote": "You'll learn more about what's inside atoms in later grades."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "251 (textutil text)",
     "quote": "The same question from a grade 3 student and a grade 8 student should receive different levels of detail and different mathematical framing, but the SAME conceptual foundation."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Teach a rule of thumb as a pattern that predicts, not as the reason something happens, because students who take a pattern for a law cannot handle its exceptions.",
   "kind": "adopted rule",
   "found_by": "Chemistry card, with exam evidence on questions about exceptions.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "238 (textutil text)",
     "quote": "The octet rule (having 8 electrons in the outer shell) is a useful PATTERN that helps predict which arrangements are stable, but it's not the REASON bonds form."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "240 (textutil text)",
     "quote": "Students who hold the teleological model cannot handle exceptions to the octet rule because they believe the octet is a law rather than a pattern."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Choose analogies whose obvious features match the concept, and drop or flag any analogy that suggests a false feature.",
   "kind": "adopted rule",
   "found_by": "Physics and chemistry misconception cards.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx",
     "lines": "257 (textutil text)",
     "quote": "Avoid the water pipe analogy without extreme care — it naturally suggests water (current) is consumed by components."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx",
     "lines": "250 (textutil text)",
     "quote": "But the SKIERS keep going around. The ski lift doesn't create new skiers."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "207 (textutil text)",
     "quote": "Use the analogy of magnets (carefully)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Do not skip an idea because it seems obvious; the ideas experts find obvious are often the ones everyday experience contradicts most.",
   "kind": "adopted rule",
   "found_by": "Physics misconception card.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx",
     "lines": "105 (textutil text)",
     "quote": "Do NOT skip the first law because it \"seems obvious.\" It is the LEAST obvious law and the one most contradicted by everyday experience."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Once two easily confused ideas have both been taught, distinguish them explicitly side by side.",
   "kind": "adopted rule",
   "found_by": "Physics constraint summary; a reading-standard component built around one confusable pair.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Physics Misconception Prevention Guidance.docx",
     "lines": "330 (textutil text)",
     "quote": "each pair explicitly distinguished when both have been introduced."
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
     "lines": "sheet 'Standard components', cell D39",
     "quote": "Distinguish between a character's temporary feelings and stable traits"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check that students have the prerequisites, including any mathematics, before introducing a concept that depends on them, and sequence the units that supply terms before those that use them.",
   "kind": "adopted rule",
   "found_by": "Misconception synthesis; curriculum thread fix list; backward-design brief.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "196 (textutil text)",
     "quote": "Curriculum builders should check mathematical readiness before introducing concepts that depend on it."
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of G3-8_Threads_FourTier.docx",
     "lines": "400 (textutil text)",
     "quote": "Sequence supplying units first so their terms are available"
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx",
     "lines": "60 (textutil text)",
     "quote": "the contact means something because both sides have been built."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Explain how things happen rather than what they want, because purpose words applied to things without intentions plant a misconception; sweeps removed such wording from options and definitions.",
   "kind": "adopted rule",
   "found_by": "Cross-subject synthesis prohibitions and per-lesson science sweeps.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "145 (textutil text)",
     "quote": "The distinction between functional description and causal teleology must be taught explicitly."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 3. The Animal Kingdom - SORT - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "209 (textutil text)",
     "quote": "One science fix was made: Sync check 2 option C changed from \"covered in feathers to fly\" to \"that are covered in feathers\" to remove purpose-implying (teleological) wording."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "203 (textutil text)",
     "quote": "No teleological language for atomic or molecular behaviour."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Run the misconception check on every option, definition and keyed answer, not only the passage: one sweep found the misconception inside a keyed answer.",
   "kind": "measured",
   "found_by": "Per-lesson science sweeps recorded their fixes: a keyed answer in one lesson, a sync-check option in another, a taught word's definition in a third; two sweeps found nothing to fix.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "191 (textutil text)",
     "quote": "Misconception fix: first-read MCQ 2 option C changed from \"make energy from sunlight\" to \"make food from sunlight\" (plants make food, not energy)"
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 5. Feathers and Scales - CONNECT - Lesson Design (v3 - prototype-aligned).docx",
     "lines": "259 (textutil text)",
     "quote": "The taught word \"adaptation\" is now defined functionally (\"a feature that helps an animal live well where it lives\")"
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 9. The Invisible World Microorganisms - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "185 (textutil text)",
     "quote": "Science-misconception sweep: no fixes were needed"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Automate any check that every text must pass and run it on rewrites too: in this sweep a drafted text and its so-called rewrite, word-for-word identical, both kept phrasing the misconception guidance bans.",
   "kind": "measured",
   "found_by": "This sweep: phrase scan of the draft texts against the guidance's banned list, and a text comparison showing the rewrite file identical to the draft; the coherence guidance requires all science-related text to pass the misconception check.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "243 (textutil text)",
     "quote": "The Tier 1 prohibitions should be implemented as automated checks on any content generated for the curriculum — whether by humans or AI."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/G4 DRAFT/2. Ecosystems and Food Webs.docx",
     "lines": "27 (textutil text)",
     "quote": "The rest is lost as heat or used up by the plant's own processes."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/G4 DRAFT/Rewrites/2. Ecosystems and Food Webs - rewrite.docx",
     "lines": "27 (textutil text)",
     "quote": "The rest is lost as heat or used up by the plant's own processes."
    }
   ],
   "against": "Both files sit in a draft folder ('G4 DRAFT') and may not yet have reached the check.",
   "adds_to_existing": [
    28,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Prefer letting students re-encounter ideas met earlier over being the first place they meet an idea, and give each re-encounter a new angle rather than a repeat.",
   "kind": "adopted rule",
   "found_by": "Coherence guidance for lessons that carry other subjects' content.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md",
     "lines": "25",
     "quote": "It is better to re-encounter ideas from earlier grades than to be the first place a student meets an idea."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md",
     "lines": "11",
     "quote": "The aim is for the re-encounter to feel like a new angle, not a repeat."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When you cannot know whether students have met a topic yet, write the lesson so that it works either way.",
   "kind": "adopted rule",
   "found_by": "Coherence guidance, written because the subject apps and the reading lessons share no record of what a student has studied.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md",
     "lines": "4",
     "quote": "at any given moment we cannot be sure whether a student has studied a topic or not."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md",
     "lines": "10",
     "quote": "provided it is done in such a way that it doesn't matter whether the substantive science or social studies lesson has happened yet."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Do not present contested or open questions as settled, and frame students' conclusions so it is clear whether they are observations, guesses, interpretations or opinions.",
   "kind": "adopted rule",
   "found_by": "Coherence guidance; persuasive-text lesson sweep.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md",
     "lines": "21",
     "quote": "the passage should not be presented as settled where this is unwarranted."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md",
     "lines": "26",
     "quote": "student writing should be framed so that it's clear which of these the student is doing."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 2. Should We Save the Rainforests - WEIGH - Lesson Design.docx",
     "lines": "223 (textutil text)",
     "quote": "Nothing is overclaimed beyond the passage."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When a text celebrates an achievement, include its limits and costs, never play down the harm done to the people affected, and retell traditional stories respectfully.",
   "kind": "adopted rule",
   "found_by": "Reviewer notes on the curriculum map's history texts and its source records.",
   "evidence": [
    {
     "path": "~/Downloads/_G3 curriculum Map.xlsx - Curric Map.csv",
     "lines": "79",
     "quote": "Ensure the limitations of Ancient Greek democracy are discussed."
    },
    {
     "path": "~/Downloads/_G3 curriculum Map.xlsx - Curric Map.csv",
     "lines": "89",
     "quote": "Be really careful here to not downplay the tragedy of European arrival for those already in the Americas (ditto with texts below)."
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'Sources & Inspiration', cell G9",
     "quote": "Ensure respectful retelling"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Is a record that a non-fiction text was generated from general knowledge enough, when the rule is that non-fiction must be traceable to reputable sources?",
   "kind": "open question",
   "found_by": "This sweep compared the coherence guidance with the curriculum map's source records.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Brainlift social science and science coherence.md",
     "lines": "16",
     "quote": "Non-fiction passages should be factually accurate and traceable to reputable sources."
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'Sources & Inspiration', cell D41",
     "quote": "AI-generated from general knowledge"
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'Sources & Inspiration', cell E41",
     "quote": "General botanical knowledge (photosynthesis, plant parts, life cycles)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Record each text's rights status, and check a translation's rights separately from the original's, because a modern translation carries its own copyright.",
   "kind": "adopted rule",
   "found_by": "Text-sourcing brief and the curriculum map's sources sheet.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx",
     "lines": "3 (textutil text)",
     "quote": "[© model] = the example text is in copyright and shown only to illustrate the concept — find a free equivalent (or we license it)."
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx",
     "lines": "111 (textutil text)",
     "quote": "For any translated classic (the Odyssey, Greek drama, Beowulf), use a public-domain translation — a modern translation carries its own fresh copyright."
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'Sources & Inspiration', cell G27",
     "quote": "6-part retelling. Twain died 1910; globally public domain."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Build a curriculum thread backward from a demanding end-point text: name the concept it needs, then choose earlier texts that build the same concept in simpler form, keeping the idea constant and raising only the difficulty.",
   "kind": "adopted rule",
   "found_by": "Backward-design brief and the whole-course thematic map.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx",
     "lines": "5 (textutil text)",
     "quote": "We pick a Grade 8 destination, name the concept it demands, then choose earlier texts that build that same concept in simpler form every year."
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx",
     "lines": "110 (textutil text)",
     "quote": "Keep the concept constant, raise the difficulty."
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx",
     "lines": "sheet 'How to read this', cell A9",
     "quote": "Shakespeare is hard language over familiar ground."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When a later stage covers the same content as an earlier one, make its demand strictly higher, for example from describing to evaluating.",
   "kind": "adopted rule",
   "found_by": "Change log of the consensus standards, version 7.0.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'V7.0 Executive Summary', cell A30",
     "quote": "Two G8 History standards received verb lifts to ensure cognitive demand is strictly higher than their G7 equivalents:"
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'V7.0 Executive Summary', cell A33",
     "quote": "This maintains the DOK progression principle that G8 standards must be higher-order than G7 equivalents covering the same content."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Audit coverage by counting how many lessons serve each required component or text type and treat a zero as a gap to close, while allowing a thin count where a thread deliberately rests and returns.",
   "kind": "measured",
   "found_by": "Curriculum audits counted hits: three text types and the biography strand returned zero; the map's component tally shows 11 of 85 components with no lesson and 35 low (tallied in this sweep).",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx",
     "lines": "69 (textutil text)",
     "quote": "Three text types currently return zero hits and must be covered — best homed in Science and Geography, not a separate strand:"
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of DevFactory_Example_Backward-Design_Threads.docx",
     "lines": "62 (textutil text)",
     "quote": "Biography, memoir and autobiography currently return zero hits anywhere."
    }
   ],
   "against": "\"Thin cells are where a thread rests at a grade and returns deeper later — a spiral, not a checklist.\" (Grade_3-12_Full_Thematic_Map.xlsx, sheet 'Coverage check', cell A13).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Tag a lesson with a skill only if its text actually affords that skill; reviews found tags the texts could not serve and reassigned them.",
   "kind": "measured",
   "found_by": "Review notes in the curriculum map's coverage sheet record four tag corrections (cells T5, K45, K52, K96).",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'SC Coverage', cell T5",
     "quote": "the Phase 3 ladder assesses the HOW of the lamp-use change, and the text has no because/so/since signal words. Reassign RL.3.1.d to a lesson whose text genuinely signals cause-effect."
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'SC Coverage', cell K45",
     "quote": "RL.3.6.d replaces mistagged RL.3.9.d."
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
     "lines": "sheet 'SC Coverage', cell K52",
     "quote": "WRITER'S COMPARISON — RI.3.3 not RI.3.9 (single text)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before asking students to compare two texts, give them a single text that makes the comparison itself.",
   "kind": "adopted rule",
   "found_by": "Sequencing tags in the curriculum map.",
   "evidence": [
    {
     "path": "~/Downloads/_G3 curriculum Map.xlsx - Curric Map.csv",
     "lines": "46",
     "quote": "A scaffolded within-text comparison to build skills toward cross-text comparison later."
    },
    {
     "path": "~/Downloads/_G3 curriculum Map.xlsx - Curric Map.csv",
     "lines": "76",
     "quote": "CROSS-TEXT COMPARISON (student writing) — RI.3.9 + W.3.2"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Choose core content by how many independent sources include it, with a fixed inclusion threshold, break conflicts in favour of the knowledge-rich and recently revised source, and do not build on a framework that sets skills but no content.",
   "kind": "adopted rule",
   "found_by": "Methodology of the consensus standards: 16,345 standards from 51 jurisdictions, only MODERATE and above included (cells B2, B10).",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'Methodology Notes', cell B9",
     "quote": "CORE 38+, HIGH 26-37, MODERATE 13-25, LOW <13"
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'Methodology Notes', cell B8",
     "quote": "Knowledge-rich + recently revised wins."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'Methodology Notes', cell B3",
     "quote": "Skills only - no content mandates, no assessments"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Retire items instead of deleting them, and record what each was merged into or covered by, so every change stays traceable.",
   "kind": "adopted rule",
   "found_by": "Consensus standards version 7.0.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'V7.0 Executive Summary', cell A65",
     "quote": "- RETIRED standards: 11 (preserved for traceability)"
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'Retired Standards', cell X2",
     "quote": "Cat 1: Merged into K.His.3"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Break each standard into components that each name one point of failure, the specific error a student makes when it fails, and the kind of knowledge it depends on.",
   "kind": "adopted rule",
   "found_by": "The Grade 3 standards were split into 86 components across 36 standards (counted in this sweep), each linked to one of six knowledge categories.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
     "lines": "sheet 'Standard components', cell D1",
     "quote": "(single point of failure)"
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
     "lines": "sheet 'Standard components', cell E32",
     "quote": "Child picks an interesting or memorable detail and calls it the main idea. Drawn to vivid facts rather than the overarching point."
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
     "lines": "sheet 'Standard components', cell G1",
     "quote": "Knowledge Category Link"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write knowledge as single-claim facts, each marked as new or as a review that names where it was first taught and what is new, plus composite tasks that make students combine several facts.",
   "kind": "adopted rule",
   "found_by": "Science review workbook (1129 atoms and 385 composites across Grades K–8, Summary cells B11 and C11) and the four-step expansion method in the consensus standards.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Science_Curriculum_Review_Workbook.xlsx",
     "lines": "sheet 'G3', cell D2",
     "quote": "[Spiral review of G2 Unit 2, A3-A4 — what is new: \"atoms\" replaces \"tiny pieces/particles\"; formal term introduced per D1 3-5 band]"
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Science_Curriculum_Review_Workbook.xlsx",
     "lines": "sheet 'G3', cell D15",
     "quote": "[Multi-step: measure properties, classify by properties, connect to particle model with negative definition]"
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
     "lines": "sheet 'Methodology Notes', cell B14",
     "quote": "4-step expansion per grade: collect specifics, add context, break into micro-atoms, sequence for delivery."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Record for every lesson what it builds on and what it seeds later, so the whole sequence can be checked for knowledge gaps.",
   "kind": "adopted rule",
   "found_by": "Working-draft curriculum map and the unit knowledge bases' prior-knowledge and knowledge-seed columns.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/[WORKING DRAFT] AlphaRead_G3-8_Full_Curriculum_to_G9.xlsx",
     "lines": "sheet 'Overview (read across)', cell A2",
     "quote": "Goal: a child reaches Grade 9 with no knowledge gaps."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx",
     "lines": "sheet 'Overview', cell B39",
     "quote": "Seeds run forward to 3.4 Folk Tales, 3.10 Myths, 3.12/3.15 Poetry, the Grade 4 units (4.1 Legends, 4.4 World Mythology, 4.9 Classic Novels), and cross-curricular Science/Geography and History."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Match the reading procedure to what the text is: locating for fact texts, comparing for comparison texts, sorting for classification texts and weighing for persuasive texts.",
   "kind": "adopted rule",
   "found_by": "Unit knowledge-base overview.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - The Living World - Complete KB.xlsx",
     "lines": "sheet 'Overview', cell B35",
     "quote": "FIND fits the fact-based texts (Plants, Mammals, Invertebrates, Microorganisms). The comparison texts (Feathers and Scales, Life in Water) use CONNECT - compare two groups, then draw the deeper link. The Animal Kingdom uses SORT (classify by shared features); the persuasion texts (Rainforests, Whose World Is It) need WEIGH / fact-vs-opinion."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Teach one named procedure per lesson and keep its steps worded identically in the introduction, the worked example, guided and independent practice and the recap.",
   "kind": "adopted rule",
   "found_by": "Built lesson and unit knowledge base.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "12",
     "quote": "The steps are printed verbatim on the skill intro, the model, the guided try, the independent write, and the wrap recap — the rail never changes mid-lesson."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "181",
     "quote": "An advance organizer for a procedure: the child meets the rail once, cold, before watching it run — so the model that follows is recognition, not first contact."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx",
     "lines": "sheet 'Knowledge Base', cell A3",
     "quote": "Each lesson runs ONE reading PROCEDURE (FIND / CONNECT / INFER) on its key threshold (in RED): the teacher models it in the Modelling Moment, the child completes the final step, and Part Three re-runs the same procedure on fresh evidence."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Return to the unit's organising pattern in every lesson and fill in the part each text delivers, so the pattern builds up across the unit instead of being covered once.",
   "kind": "adopted rule",
   "found_by": "Built lesson; unit knowledge base.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "42",
     "quote": "The five-row pattern chart returns every lesson, filled row by row | Schema accumulates across the unit instead of being covered once"
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.3 - Ancient Civilisations - Lesson Designs/3.3 Ancient Civilisations - Knowledge Base - Full.xlsx",
     "lines": "sheet 'Overview', cell B7",
     "quote": "Flood-fed farming → the first cities → writing → leaders & government → trade. Every text tests this pattern."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Track how complex each idea is separately from grade level, and mark the keystone items that much later material depends on so they are never dropped.",
   "kind": "adopted rule",
   "found_by": "Whole-course thematic map.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx",
     "lines": "sheet 'How to read this', cell A7",
     "quote": "Rung is the complexity of the IDEA, tracked alongside grade."
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx",
     "lines": "sheet 'How to read this', cell A11",
     "quote": "KEYSTONE texts are the anchor of a rung — the one you would not drop, because so much above it depends on the concept it plants."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Organise a whole course around a small fixed set of recurring concepts, and record which of them each lesson draws on.",
   "kind": "adopted rule",
   "found_by": "Unit knowledge bases and the whole-course thematic map.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - Fantasy Classics - Knowledge Base (Complete).xlsx",
     "lines": "sheet 'Overview', cell A15",
     "quote": "CONCEPT MAP - which concepts each lesson draws on (from the fixed 14-pair bank)"
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx",
     "lines": "sheet 'Threads & Ladders', cell A2",
     "quote": "Your 14 concept-pairs, consolidated into 7 course-long threads."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When aligning to a required list of texts, match on the text itself, recording a different edition of the same story and a merely related topic separately from a true match.",
   "kind": "measured",
   "found_by": "Comparison against a required Grade 3 list: 23 required texts, 1 full match, 3 partial or near, 19 missing (cells B27–B30); four of the missing tales were later added as adaptations of public-domain sources.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/TEA Proposed Mandatory Literary Works (HB 1605).xlsx",
     "lines": "sheet 'G3 Comparison', cell E9",
     "quote": "Alpha has 'The Story of Icarus' in Unit 10 (Myths) — same myth, different source text/edition"
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/TEA Proposed Mandatory Literary Works (HB 1605).xlsx",
     "lines": "sheet 'G3 Comparison', cell E13",
     "quote": "Alpha has 'Ancient Egypt — The Gift of the Nile' (Unit 3) — related topic, different text"
    },
    {
     "path": "~/Downloads/_G3 curriculum Map.xlsx - Curric Map.csv",
     "lines": "14",
     "quote": "TEA HB 1605 (Alpha adaptation of PD source)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Place a text by the maturity of its content as well as by its reading difficulty.",
   "kind": "adopted rule",
   "found_by": "An archived review note argued for moving a dark narrative poem up a grade on appropriateness; the thread map records the move.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/G3/Grade 3 word docs/15 - Poetry (Criticism)/Archive/Claude Notes on Criticism poems_.docx",
     "lines": "9 (textutil text)",
     "quote": "So moving it to G5 is the right call on appropriateness alone."
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/G3-8_Knowledge_Threads_to_G9.xlsx",
     "lines": "sheet 'Thread Explorer', cell A2",
     "quote": "RED note = a revision (e.g. The Highwayman moved to Grade 5)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Fill a curriculum slot with the text that gives a new capability later units build on, not one that repeats what the next stage already covers.",
   "kind": "adopted rule",
   "found_by": "Archived review note comparing two candidate texts against the next grade's unit; the recommended text set is the one now in the map.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/G3/Grade 3 word docs/15 - Poetry (Criticism)/Archive/Claude Notes on Criticism poems_.docx",
     "lines": "3 (textutil text)",
     "quote": "The Pied Piper adds engagement but not a new capability."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/G3/Grade 3 word docs/15 - Poetry (Criticism)/Archive/Claude Notes on Criticism poems_.docx",
     "lines": "6 (textutil text)",
     "quote": "For foundational value, the trio wins."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Back every claim the materials make about a category with an example students actually meet; an audit found a unit asserting a property that none of its texts showed.",
   "kind": "measured",
   "found_by": "Archived review note auditing the next grade's poetry unit.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/G3/Grade 3 word docs/15 - Poetry (Criticism)/Archive/Claude Notes on Criticism poems_.docx",
     "lines": "4 (textutil text)",
     "quote": "But every poem in the G4 unit rhymes — so G4 asserts \"poems don't have to rhyme\" without a single poem to demonstrate it, and it never frames poetry as criticism at all."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Name a term and show a concrete instance of it together, because a term taught alone produces empty verbal knowledge.",
   "kind": "external research",
   "found_by": "Media-design synthesis citing Ausubel (1968); no DOI or URL given in the source.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "455",
     "quote": "So the rule is name the term and show the instance, never the term alone."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "319",
     "quote": "Name the term, then show the instance — \"Every story happens somewhere. We call that the setting\" — never the instance alone."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Cut interesting but irrelevant material, above all at the start, because it lowers recall and transfer.",
   "kind": "external research",
   "found_by": "Research table citing Harp and Mayer (1998), https://doi.org/10.1037/0022-0663.90.3.414, and Mayer's coherence principle, https://doi.org/10.1017/cbo9780511811678.007.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "129",
     "quote": "Interesting but irrelevant details reduced recall and transfer, and did the most damage placed at the start of the text."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "130",
     "quote": "Excluding extraneous material improves multimedia learning, median effect near d 0.70."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Give background context before a text rather than after it; the same context given afterwards did nothing for comprehension.",
   "kind": "external research",
   "found_by": "Media-design synthesis citing Bransford and Johnson (1972); no DOI or URL given in the source.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "446",
     "quote": "giving readers the context before an opaque passage transformed comprehension and recall. The same context after did not."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "421",
     "quote": "Everything this document argues rests on the video sitting before the read."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    20
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Build the topic knowledge a text assumes, because prior knowledge predicts understanding of a text far better than general reading ability.",
   "kind": "external research",
   "found_by": "Syntheses citing Recht and Leslie (1988) and Catts (2022); no DOI or URL given in the sources.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "439",
     "quote": "prior knowledge of baseball predicted memory for a baseball text on essentially every measure; general reading ability predicted almost none."
    },
    {
     "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "32",
     "quote": "It is a complex activity that rests on language and, more than anything, background knowledge (Catts, 2021-2022)."
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx",
     "lines": "sheet 'How to read this', cell A3",
     "quote": "This is the 'knowledge latches onto knowledge' principle applied to whole-school reading."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    20
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Watching a model teaches only when the watcher is active, so in solo study embedded checks and pauses must supply the activity a partner would.",
   "kind": "external research",
   "found_by": "Media-design synthesis citing Chi, Roy and Hausmann (2008); no DOI given; the built lesson uses taps to keep a long model active.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "470",
     "quote": "Solo observation was weaker, so in a solo app the checks and pauses have to do the work the partner did."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "197",
     "quote": "The taps are attention devices, not assessment — they keep a long model active without adding an ask."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A preview organiser helps when it emphasises the key concepts, not only the structure; structure alone was not reliably better.",
   "kind": "external research",
   "found_by": "Media-design synthesis citing Gurlitt, Dummel, Schuster and Nückles (2012), no DOI given: two experiments with 48 and 53 students, far transfer rising from roughly 33% to 67%.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "456",
     "quote": "What carried it was the version that additionally emphasised the key concepts. Structure without emphasis was not enough."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Prefer a tutor–learner dialogue or a refutation of the wrong idea over straight exposition; both beat exposition, most of all for students with the least prior knowledge.",
   "kind": "external research",
   "found_by": "Media-design synthesis citing Muller, Bewes, Sharma and Reimann (2008), 364 students; no DOI given.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "471",
     "quote": "The tutor-student dialogue version beat straight exposition at d \\= 0.83; the refutation version at d \\= 0.79. Lowest-prior-knowledge students gained most."
    }
   ],
   "against": "For media under a minute the same document prefers one narrator: \"(For short videos, just the narrator is preferable though \\-- see SPOV5).\" (BrainLift intro video, line 426).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Read every narration script aloud before release, because cutting removes the labels that name what the student is looking at first, and written-style sentences collapse when spoken.",
   "kind": "adopted rule",
   "found_by": "Media-design rule from compressing reviewed scripts.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "315",
     "quote": "It removes the connective words first — the ones that named what the child was looking at and what to call it — because on the page those words look like padding."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "321",
     "quote": "Colons, parenthetical asides, appositives and list constructions survive silently on the page and collapse in a voiceover."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "355",
     "quote": "A line that fails any of these usually reads perfectly well on the page. That is why the pass has to be spoken."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44,
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In narration, name a representation as a representation, give the category before a proper name, and say when something shown is not an example of what is being taught.",
   "kind": "adopted rule",
   "found_by": "Read-aloud checklist for narration scripts.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "349",
     "quote": "Example: \"That is a statue of a pharaoh\", never \"that is a pharaoh\". A child otherwise takes the object for the person."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "350",
     "quote": "The name then lands as an instance of something already understood rather than as a new thing to hold."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "351",
     "quote": "If something on screen is not an example of what is being taught, say so."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Where reviewed material exists, edit or compress it rather than regenerate it, because regeneration throws away the earlier review and brings back errors already caught.",
   "kind": "adopted rule",
   "found_by": "Media-design rule; the built lesson transferred designed content rather than regenerating it.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "269",
     "quote": "Regenerating from the knowledge base discards all of that and reintroduces errors that were already caught once. Compression is a smaller, safer and more auditable job than generation."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "9",
     "quote": "Most of the content is your own work transferred, not re-generated"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Fix each recurring character's and place's look once for the whole unit and reuse it everywhere; if the look must change, every piece made with the old look is wrong until remade.",
   "kind": "adopted rule",
   "found_by": "Media look rules, grounded in recognition memory being cheap and recall costly.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "987",
     "quote": "A character has one appearance, decided once for the unit. It is not re-described per video and not per shot."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "992",
     "quote": "If an appearance has to change, it changes for the unit and every video already made against it is wrong until it is remade."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "59",
     "quote": "Characters and places keep one locked look across every video, because recognition is the memory system."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    42
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep words out of generated images and video frames, and put any needed words in the interface instead.",
   "kind": "adopted rule",
   "found_by": "Media look rules and every image prompt in the lesson designs.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "965",
     "quote": "No text in generated frames"
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "60 (textutil text)",
     "quote": "no text or labels in the image"
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "44 (textutil text)",
     "quote": "no text baked into the art."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    22
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Ask a video generator for one main action per clip with no cut inside it, because a clip asked to carry a sequence produces one that cannot be edited out.",
   "kind": "adopted rule",
   "found_by": "Motion rules for generated media.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "978",
     "quote": "One main action per clip."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "979",
     "quote": "No cut inside a clip. A clip asked to carry a sequence of events produces one, and it cannot be edited out afterwards."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make narration add what the picture cannot say rather than describe what the frame already shows, while never mentioning anything the matching shot does not show.",
   "kind": "adopted rule",
   "found_by": "Language rules for narration: the line-not-caption test and read-along alignment.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "943",
     "quote": "Narration must add what the frame cannot say. It must not describe facts already obvious in the same frame."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "959",
     "quote": "A line may not mention details missing from its shot."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    21,
    53
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When the voice reads printed text aloud, it must match the print word for word, with each word highlighted as it is read.",
   "kind": "adopted rule",
   "found_by": "House delivery rule in the built lesson and the lesson-components spec.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "39",
     "quote": "Read-to-me audio matches the printed words exactly, word-highlighted | Any mismatch breaks decoding support and the child’s trust in the voice"
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
     "lines": "14 (textutil text)",
     "quote": "The full text read aloud with word-by-word highlighting at a fixed pace (110–120 wpm, no per-student speed)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    17,
    53
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep each banned-word or banned-punctuation list in one place that the generator reads, and never restate it elsewhere.",
   "kind": "adopted rule",
   "found_by": "Language rules for generated narration.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "953",
     "quote": "Neither list is restated anywhere else."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Log every deliberate divergence from the design with the ruling that covers it, and state where the live build differs from the authored intent instead of reconciling it quietly.",
   "kind": "adopted rule",
   "found_by": "Deviations ledger and method note of the built lesson's walkthrough.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "15",
     "quote": "Every knowing divergence is logged in a deviations ledger with the ruling that covers it; the open ones appear in this walkthrough as amber flags."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "387",
     "quote": "Where a screen’s behaviour on the live build differs from its authored intent, the difference is stated in the text rather than reconciled quietly."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Write instructions, prompts and feedback at an easier reading level than the text they support, and keep builder jargon out of them.",
   "kind": "adopted rule",
   "found_by": "Register parameter of the built lesson (child-facing prose at 420–650L).",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "38",
     "quote": "Child-facing prose at 420–650L, below the passage; warm, no jargon | The scaffold must be easier to read than the thing it scaffolds"
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "181",
     "quote": "No rail jargon reaches the child (“INFER” is for builders)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    2
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give each screen one primary thing to attend to, and bring in support at the step that uses it rather than stacking it on arrival.",
   "kind": "adopted rule",
   "found_by": "Attention standard distilled from reviews and applied in the built lesson.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "27",
     "quote": "Each screen has a single thing to attend to | Attention is the scarcest resource; split screens split learning"
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
     "lines": "28",
     "quote": "Help appears at the step that uses it, never stacked upfront | Support on arrival is clutter; support at the point of use is scaffolding"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Remove from the screen anything the current lesson does not teach or use, even a familiar reminder.",
   "kind": "adopted rule",
   "found_by": "Change notes in the version-3 inference lesson designs.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "54 (textutil text)",
     "quote": "The pattern is not taught here, so it is removed entirely."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 10. The Wind in the Willows, Part 3 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "46 (textutil text)",
     "quote": "The pattern is not taught here, so it is removed from the prompts. (It still lives in the video, Component 1.)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    26,
    64
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a picture contrasts two states, keep framing and scale identical in both halves so that only the contrast changes.",
   "kind": "adopted rule",
   "found_by": "Image prompts for the juxtaposition illustrations in the inference lesson designs.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "60 (textutil text)",
     "quote": "Identical framing and scale on both halves so the contrast in the boy's power reads instantly"
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 9. The Wind in the Willows, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "58 (textutil text)",
     "quote": "Identical framing and scale on both halves so the contrast reads instantly: real trouble on one side, a happy daydream on the other."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    21
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In independent practice, let students open a recap of what the worked example did at each step, drawn from the example's own material rather than the current answer.",
   "kind": "adopted rule",
   "found_by": "Version-3 change to the inference lesson design.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "213 (textutil text)",
     "quote": "Every step carries a collapsible \"What the teacher did\" recap that references the cave model, plus contextual help."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
     "lines": "6 (textutil text)",
     "quote": "every Independent (Phase 3) step now carries a toggleable \"What the teacher did\" recap that references the cave model"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Have students find the part of the text where the evidence lives before hunting for the exact line.",
   "kind": "adopted rule",
   "found_by": "Review suggestion applied to the independent task's second step in the built lesson.",
   "evidence": [
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "241",
     "quote": "locating the evidence neighborhood before hunting in it keeps the hunt a comprehension act rather than a scan-everything act."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Place a check embedded in media at a natural boundary, and for media under about a minute put the check just after rather than inside.",
   "kind": "adopted rule",
   "found_by": "Media-design rule on sync checks.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "311",
     "quote": "A check earns its interruption by landing on a boundary: it consolidates the thing just taught and clears working memory before the next arrives."
    }
   ],
   "against": "\"N.B. this is a sensible estimate based on experience.\" (same line).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep 'in this lesson you will learn' framing and audience-addressed filler out of story narration.",
   "kind": "adopted rule",
   "found_by": "Banned language shapes and insight list in the intro-video rules.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "950",
     "quote": "No student framing language such as \"in this lesson\" or \"you will learn\""
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "106",
     "quote": "Fillers like let's meet our characters feel engaging and do the opposite."
    }
   ],
   "against": "The other version in the same file allows direct address: \"the narrator in shorter videos can just state the fact or speak to the viewer\" (line 341).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Should pre-reading media show only the setting and mood, or also the characters, the text's structure and the opening events?",
   "kind": "open question",
   "found_by": "The two versions of the intro-video rules take opposite positions, and the measured preview effects came from previews that included plot.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "41",
     "quote": "An intro video shows only the world² and none of the plot³, even when revealing plot would measurably improve comprehension."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "291",
     "quote": "A video that shows only scenery has built atmosphere rather than knowledge and has missed the mark."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "422",
     "quote": "A blanket ban on plot is a position nobody has tested, not a finding."
    }
   ],
   "against": "\"no child has yet been observed watching one of our films.\" (same file, line 249).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Should a later part's pre-reading media recap the earlier parts, or bring them back through recognition only?",
   "kind": "open question",
   "found_by": "The two versions of the intro-video rules disagree, and the produced video outlines open with a recap.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "63",
     "quote": "When a later video must make the child remember, show the place as it now stands and never say what happened there."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "297",
     "quote": "Recapping consolidates; it does not reveal."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/G3/Grade 3 markdown/01 - Fantasy Classics/01 - Aladdin and the Wonderful Lamp/Video Outline - Aladdin and the Wonderful Lamp Part 2.docx",
     "lines": "3 (textutil text)",
     "quote": "Last time, Aladdin was tricked by a magician pretending to be his uncle."
    }
   ],
   "against": "\"Nobody has tested recognition against recap, on a story told in parts, for a child who has forgotten the earlier one\" (BrainLift intro video, line 62).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Should pre-reading media teach vocabulary that the text will use?",
   "kind": "open question",
   "found_by": "The two versions of the intro-video rules disagree, and the lesson designs rely on words taught in the video.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "932",
     "quote": "Do not pre-teach vocabulary that the passage is meant to teach."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "301",
     "quote": "Ideally the video is where a word gets taught, because a visual anchor plus a spoken definition plus later recurrence is worth considerably more than a definition on a card."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
     "lines": "13 (textutil text)",
     "quote": "Video-stamped words (off-limits for the vocab slot): magician, sultan."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "How long should pre-reading media run?",
   "kind": "open question",
   "found_by": "Three sources give three lengths: a 30–40 second rule, a compressed 60-second worked example and a 1:54 film in the built lesson.",
   "evidence": [
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "87",
     "quote": "An intro video is 30 to 40 seconds, and a longer one is weaker, not richer."
    },
    {
     "path": "~/Downloads/BrainLift - What makes a good intro video.md",
     "lines": "363",
     "quote": "125 spoken words, \\~60 seconds, narrator only, no stamp, no embedded checks."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "25",
     "quote": "A 1:54 film of the riverbank world with captions available"
    }
   ],
   "against": "The short rule is called \"because it is the least evidenced claim we hold.\" (BrainLift intro video, line 87).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "For each concept, write the end-point target, map each known misconception with how persistent it is, how much the final exam depends on it and where in schooling it starts, and find the riskiest points in the teaching sequence.",
   "kind": "adopted rule",
   "found_by": "Card format used across the biology, chemistry and physics misconception guidance, prioritised by exam weight.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "7 (textutil text)",
     "quote": "MISCONCEPTION MAP: Each misconception, rated by persistence and impact, with its origin"
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "9 (textutil text)",
     "quote": "RISK ASSESSMENT: The highest-risk points in the instructional sequence"
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx",
     "lines": "5 (textutil text)",
     "quote": "Priority: 1 (Highest — up to 20% of AP exam; most extensively documented biology misconceptions)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check the wording of the teaching materials themselves, because textbooks and everyday phrasing seed misconceptions that students then repeat in scored exam answers.",
   "kind": "adopted rule",
   "found_by": "Misconception maps record each misconception's typical origin and its exam impact.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx",
     "lines": "140 (textutil text)",
     "quote": "Biology textbooks; \"high-energy bond\" language"
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
     "lines": "31 (textutil text)",
     "quote": "Biology textbooks use \"high-energy phosphate bonds\" language that directly contradicts the correct chemistry."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx",
     "lines": "114 (textutil text)",
     "quote": "Students who write \"the organism evolved to survive\" or \"the species needed to adapt\" lose points."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When a rule changes, re-run the whole checklist on every affected lesson: in five lesson designs the closing 'rules honoured' line still described the old rule after the rule itself had changed.",
   "kind": "measured",
   "found_by": "This sweep cross-read each design's rule header against its closing sweep line; the Plants, Animal Kingdom, Mammals, Microorganisms and Feathers and Scales designs contradict themselves on the gap-fill rule.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 4. Mammals - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "10 (textutil text)",
     "quote": "Instead of pulling from a section untouched by the other exercises, the cloze is now a SUMMARY of the whole text"
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 4. Mammals - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "205 (textutil text)",
     "quote": "Rule 3: cloze on the untouched \"Why Mammals Need Protection\" section, tap-in-order not drag."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "201 (textutil text)",
     "quote": "Rule 3: cloze on the untouched \"Why Plants Matter\" section, tap-in-order not drag."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    42
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Put gap-fill blanks on the causal links that hold the text together, spread across the whole text, not on incidental details.",
   "kind": "adopted rule",
   "found_by": "Lesson-components spec, the revised gap-fill rule in the science designs, and the built retell.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
     "lines": "20 (textutil text)",
     "quote": "exactly four blanks that sit on the links in the child's mental model — so it checks that the child has followed the flow of the story, not incidental detail."
    },
    {
     "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
     "lines": "12 (textutil text)",
     "quote": "It covers the whole text and teaches children what a summary is, instead of a section untouched by the other exercises."
    },
    {
     "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
     "lines": "151",
     "quote": "each blank sits on a link in the mental model (the leaver, the friend, the refusal, the promise)."
    }
   ],
   "against": "The whole-text rule was not applied consistently; a closing line still reads \"Rule 3: cloze on the untouched \"What Are Microorganisms?\" and \"Why They Matter\" sections, tap-in-order not drag.\" (Microorganisms design, line 195).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check what a diagram's colouring, layout or ordering implies, because styling can teach a misconception the words never state.",
   "kind": "adopted rule",
   "found_by": "Chemistry and biology misconception cards trace misconceptions to illustration styling and diagram layout.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Chemistry Misconception Prevention Guidance.docx",
     "lines": "88 (textutil text)",
     "quote": "Do NOT use illustrations that color-code individual atoms to match the bulk substance (orange atoms for copper, blue atoms for water)."
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx",
     "lines": "38 (textutil text)",
     "quote": "Scala naturae; popular culture; tree diagrams with humans at top"
    },
    {
     "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Biology Misconception Prevention Guidance.docx",
     "lines": "100 (textutil text)",
     "quote": "Do NOT oversimplify phylogenetic trees by placing humans at the top/right."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    22
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Mark which entries in a curriculum plan are verified against built materials and which are still indicative.",
   "kind": "adopted rule",
   "found_by": "Scope note in the four-tier thread map and caveats in the thematic map.",
   "evidence": [
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Copy of G3-8_Threads_FourTier.docx",
     "lines": "401 (textutil text)",
     "quote": "Grade 3 texts are folder-exact; G4–G8 texts and the upper-grade big-idea / vocabulary tiers come from the master sheet and are indicative until those units are built folder-first."
    },
    {
     "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx",
     "lines": "sheet 'How to read this', cell A15",
     "quote": "Grades 7–12 draw on the list's thinner secondary section — those rungs are the first candidates for review."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
   "lines": "91 (textutil text)",
   "quote": "Wrong -> (1) \"Let's listen to that page again,\" replay the sentence; (2) \"Here is the part of the text with the answer,\" highlight the exact sentence; (3) \"Now choose again.\""
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
   "lines": "39",
   "quote": "the wrong-answer feedback teaches without revealing — it names what the child mixed up (flying belongs to a different story in this unit) and sends them back to the evidence they just heard, rather than printing the key."
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 2. Should We Save the Rainforests - WEIGH - Lesson Design.docx",
   "lines": "211 (textutil text)",
   "quote": "Nudges redirect without giving the answer"
  },
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
   "lines": "20 (textutil text)",
   "quote": "No em dashes in child-facing wording; US English throughout; no voice input."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
   "lines": "195 (textutil text)",
   "quote": "because showing it inline would answer the question"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Downloads/BrainLift - What makes a good intro video.md",
   "lines": "340",
   "quote": "the video may set up but must not state."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
   "lines": "81 (textutil text)",
   "quote": "not the trust / FIND skill target, which is saved for the Modelling Moment and the Independent Task"
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
   "lines": "18 (textutil text)",
   "quote": "two attempts, then reveal."
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
   "lines": "315 (textutil text)",
   "quote": "3rd try and beyond: \"The dashed red statements are the ones to fix. Read them slowly and check them against the text.\""
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
   "lines": "316 (textutil text)",
   "quote": "3rd fail: reveal the full words."
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
   "lines": "89 (textutil text)",
   "quote": "Pure literal FIND: the answer is stated in the sentence just read."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
   "lines": "8 (textutil text)",
   "quote": "The two \"incorrect\" statements land in different positions in every REFINE, and the Modelling Moment set and the Part 3 set use different orders from each other."
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
   "lines": "271 (textutil text)",
   "quote": "Blank A: must match one of the 3 evidence quotes."
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
   "lines": "333 (textutil text)",
   "quote": "All re-checked against the story text."
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
   "lines": "9 (textutil text)",
   "quote": "Exactly one high-leverage word is taught — chosen to unlock this text and to feed the Phase 3 inference."
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
   "lines": "7 (textutil text)",
   "quote": "A short background-knowledge video plays first, building the knowledge the text takes for granted."
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Downloads/BrainLift - What makes a good intro video.md",
   "lines": "957",
   "quote": "Nothing is said that is not shown in the matching shot."
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Downloads/BrainLift - What makes a good intro video.md",
   "lines": "134",
   "quote": "Illustrations matching the inference a child must make helped, and illustrations conflicting with it hurt, strongest in the youngest readers."
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Downloads/BrainLift - What makes a good intro video.md",
   "lines": "352",
   "quote": "A narrator explaining one thing while the visual is still on the last one costs the child both."
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
   "lines": "111",
   "quote": "transferred with one split to keep sentences inside the grade-3 length ceiling."
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Downloads/SUPERSEDED — see v2.1_ WITW Lesson 1 learning walkthrough v2 (table format).md",
   "lines": "586",
   "quote": "Ruled: document, don’t cut cosmetically; revisit when canonical videos land."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Curriculum maps/1. Mapping Docs/Grade_3-12_Full_Thematic_Map.xlsx",
   "lines": "sheet 'How to read this', cell A15",
   "quote": "417 enumerated titles (the list's own summary said 418; its Grade-5 tab actually enumerates 69, not 70)."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
   "lines": "sheet 'SC Coverage', cell K36 (the stored tally in cells N43, O43, P43 reads RL.3.3.e, 0.0, None for the same component)",
   "quote": "ONLY PLACEMENT OF RL.3.3.e."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.4 - Folk Tales of the World - Lesson Designs/3.4 - Folk Tales - Knowledge Base - Full.xlsx",
   "lines": "sheet 'Folk Tales', cell A2",
   "quote": "Stamped (hot) words are confirmed from the video scripts."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.2 - The Living World - Lesson Designs/3.2 - 1. The Wonderful World of Plants - FIND - Lesson Design (v2 - MCQ pauses + science sweep).docx",
   "lines": "73 (textutil text)",
   "quote": "(Confirm each word appears in the final passage; drop any that do not and add any missed content words at the same reading level.)"
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
   "lines": "39",
   "quote": "Your round-2 review caught nudges that could be clicked past; this one cannot."
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 1. Aladdin and the Wonderful Lamp, Part 1 (FICTION, FIND) — v3 (order + MCQ QA).docx",
   "lines": "340 (textutil text)",
   "quote": "every MCQ has one marked answer with both feedback branches."
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
   "lines": "86",
   "quote": "Plan which kinds of moves the app can make (build on the child’s idea, ask for evidence, offer another view, scaffold up or down), then choose the actual move from what the child said."
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/2. Example lesson structure/Example Lesson Components.docx",
   "lines": "28 (textutil text)",
   "quote": "This is the first, most-supported turn at the skill before independent practice."
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
   "lines": "12",
   "quote": "and then runs that identical four-step rail four times at decreasing support"
  },
  {
   "truth": 42,
   "effect": "counter",
   "path": "~/Downloads/BrainLift - What makes a good intro video.md",
   "lines": "269",
   "quote": "Regenerating from the knowledge base discards all of that and reintroduces errors that were already caught once."
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
   "lines": "387",
   "quote": "every capture in this document is from the deployed reviewer build, taken this week in student mode with read-to-me on, by walking each screen’s real interactions (including wrong answers)."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
   "lines": "176",
   "quote": "The goal is to measure whether a child’s comprehension and oral language are growing over time, not just whether the child answered one question."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
   "lines": "353",
   "quote": "whether they own them durably is a different question the course answers with spaced returns, not with a medal."
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Curriculum maps/G3 Standards and Standard components.xlsx",
   "lines": "sheet 'Standard components', cell E1",
   "quote": "(the error a Grade 3 child makes)"
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Downloads/BrainLift - What makes a good intro video.md",
   "lines": "420",
   "quote": "A video that is enjoyed and teaches nothing has not done the job."
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Downloads/BrainLift - What makes a good intro video.md",
   "lines": "22",
   "quote": "Accepted as evidence, refused as advice. Enjoyment is not the reading, SPOV1"
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Downloads/WF - Brainlift Opportunities to - 260724-110911.md",
   "lines": "102",
   "quote": "No response or “I don’t know.” | Down (engage, mimic) | “Is Kitten happy or sad?”"
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Downloads/SUPERSEDED — see v2 (table format)_ WITW Lesson 1 learning walkthrough.md",
   "lines": "327",
   "quote": "the rubric asks for the arc’s heart (the change and the how), not a checklist — a retell, not a quiz wearing a retell’s clothes."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
   "lines": "364 (textutil text)",
   "quote": "carried faithfully, not invented past the KB."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Social studies/Consensus social science standards.xlsx",
   "lines": "sheet 'V7.0 Executive Summary', cell A57",
   "quote": "so the context window for Economics atom generation will rely entirely on state curricula and CEE."
  },
  {
   "truth": 62,
   "effect": "counter",
   "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
   "lines": "250 (textutil text)",
   "quote": "Tier 1 (absolute prohibitions) should be hard constraints that the system cannot violate."
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Curriculum maps/_G3 curriculum Map.xlsx",
   "lines": "sheet 'SC Coverage', cell K96",
   "quote": "RI.3.8.c (paragraph relationships) replaces mistagged RI.3.9.b."
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Instruction/3.1 - Fantasy Classics - Lesson Designs/3.1 - 2. Aladdin and the Wonderful Lamp, Part 2 (FICTION, INFER) — v3 (new INFER design).docx",
   "lines": "56 (textutil text)",
   "quote": "a single wide juxtaposition illustration that does this lesson's real work"
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Downloads/5. Curriculum/Texts/Misconception and alignment checks/Science/Cross-Cutting Synthesis.docx",
   "lines": "243 (textutil text)",
   "quote": "If any prohibited phrase appears, it should be flagged and corrected before publication."
  }
 ]
}
```
