# verify:gap:audit-2026-10-09

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  nono, analyse its ideas and fold them into the research results

## Result

```json
{
 "direction": "audit-2026-10-09",
 "verified": [
  {
   "index": 0,
   "verdict": "keep",
   "reason": "All three quotes are verbatim in the audit file (ranked.dropped[7], plan[7].from, plan[7].verified). quick-check.js lines 60-66 do give the judge the text and keyed_answer, and on 12 Oct a grep of src, web, bin, ops and test finds no blind solve. The method itself is already #4's evidence (a solver from another family with the passage withheld), so this is a duplicate of #4; kept because it adds the correction that the Grade 3 bank's answerable_blind is an opinion formed with the passage in view, not a blind solve, and that the engine's give-away checks are the same kind of opinion. The bench probe's own header says the same (shadow/bench/src/inceptbench/tools/blind_solve.py lines 3-8) but sits outside the registered sources.",
   "statement": "To test whether a question needs the text, take the text away and see whether a solver still picks the key; a judge asked with the text in view gives only an opinion.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "So Grade 3's answerable_blind is an opinion formed with the passage in view, like the transformer's no-giveaway; it is not a blind solve.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "The passage is stripped, and an exact pick at high confidence marks the item gameable.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "quick-check.js judge() puts the text and keyed_answer in state (lines 60-66) and asks no-giveaway as an opinion.",
     "verbatim": true
    }
   ],
   "against": "On a famous text a solver may pick the key from what it knows of the work: \"Othello is famous, so Jev may answer plot questions from general knowledge. A blind solve will then flag many first-read checks.\" (2026-10-09-best-of-everything.json line 1). The proposed bar is uncalibrated: \"Mark it required: false until it is calibrated.\" (same file). The engine judges its open check's give-away on the question's own words only (src/mechanics/open-check.js lines 86-87).",
   "general": true,
   "duplicate_of": "#4",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep",
   "reason": "Both quotes are verbatim (plan[7].risk). #4 already records that the engine's give-away question was answered from general knowledge of a famous text until it was narrowed (v02/QA.md line 139), and its against notes near misses where world knowledge tempts; so this is a duplicate of #4. Kept for what it adds to #4's against: the audit's prediction that a blind solve will flag many first-read checks on a famous text, and the undecided choice between counting that as a leak and steering such questions to line-level detail.",
   "statement": "Whether a key that a solver can pick from general knowledge of a famous text counts as a give-away, or whether questions on such texts should be steered to line-level detail.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Decide whether that counts as a leak for Grade 9, or steer QC to line-level detail.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Othello is famous, so Jev may answer plot questions from general knowledge. A blind solve will then flag many first-read checks.",
     "verbatim": true
    }
   ],
   "against": "For the open check's wording test the engine sets that knowledge aside: \"Judge only the wording of q, not what a reader may already know about the work.\" (src/mechanics/open-check.js line 87). That settles the wording test, not a blind solve.",
   "general": false,
   "duplicate_of": "#4",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (plan[7].what and .how; quick-check.js line 55). On 12 Oct the only tells checked in code are length (quick-check.js line 55: the longest option at most 2.2 times the shortest; compare-paragraphs.js line 51: 1.6 times); there is no stem-echo or lead-class test. No record covers option tells: #4 is the criterion they break, and #45 covers only key position. Fix: evidence only, adding the definitions from the content-eval copy vendored in the Grade 3 engine, which say why each tell works.",
   "statement": "Check in code for the tells that let a reader pick the key without reading, such as only the key echoing the stem, options that do not open in parallel, or one option standing out by length.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "whether only the key echoes the stem",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Port three content-eval tests into src/mechanics/util.js as code checks:",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "55",
     "quote": "No option stands out by length",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/engine/.vendor/lesson-content-eval/SKILL.md",
     "lines": "53",
     "quote": "word-matching finds the answer without comprehension",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/engine/.vendor/lesson-content-eval/SKILL.md",
     "lines": "41",
     "quote": "one option breaks the others' grammatical form — visible odd-one-out",
     "verbatim": true
    }
   ],
   "against": "\"content-eval's margins were tuned on Grade 3 items with four options.\" (2026-10-09-best-of-everything.json line 1), so they may not fit three-option items. The content-eval copy cited is vendored and untracked inside the Grade 3 engine.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (plan[7].verified and .how; open-check.js line 64). quick-check.js lines 53-54 and util.js line 116 fail a wrong option's feedback only on a shared run of at least max(3, the key's word count); open-check.js line 66 fails a hint on any leak word or a four-word run of the reveal outside quotation marks. #14's detail already covers the engine's leak checks, so this is a duplicate of #14; kept because it adds the limit that whole-key tests miss partial leaks, and content-eval's rule on words only the key has. Fix: evidence only, citing that rule from its vendored copy. The audit's 'FB-LEAKS-ANSWER (words only the key has; a 6-word run of the key)' merges two content-eval checks: FB-LEAKS-ANSWER for distinctive words and FB-COPIES-ANSWER for the 6-word run.",
   "statement": "Test every hint and wrong-option line in code for partial leaks of the answer, such as a word only the key has or a short run of the key's words outside a quotation; a test for the whole answer misses them.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "feedback-no-answer (quick-check.js lines 53-54) fails only on a run as long as the whole key.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "FB-LEAKS-ANSWER (words only the key has; a 6-word run of the key)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "64",
     "quote": "read (its third rung), but it uses no leak word and copies no four-word run of the reveal outside a quotation",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/engine/.vendor/lesson-content-eval/SKILL.md",
     "lines": "60",
     "quote": "feedback on a *wrong* option names the answer's own distinctive vocabulary — picking that wrong option reveals the right one",
     "verbatim": true
    }
   ],
   "against": "A leak test must skip quotations: the open check's first rule was stricter than the animated build's, which lets a hint quote the text (src/mechanics/open-check.js line 63: \"a hint may quote the text, even the line to\"). The run length differs by tool (4 words, 6 words, or the whole key), and none is measured.",
   "general": true,
   "duplicate_of": "#14",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (plan[7].verified and .how); quick-check.js line 83 serves options in the writer's order. A read-only recount of runs/blocks on 12 Oct matches the reader's figures (ready quick checks A 6, B 10, C 1; word in focus A 0, B 6, C 2; direct the line B in 4 of 4; essay stops A 3, B 5, C 0; film check 7, 6, 5), but no document records it, so it is not cited. The skew is the ground of #45, and the 9-block count is already offered to #45, so this is a duplicate of #45; kept because it adds the serving remedy (a seeded order, mapped back and logged) and a red-team note that a skew is exploitable only where authored order is served, yet still reveals the generator's bias. Fix: 'writer model' for 'writer', and that note added.",
   "statement": "Serve choice options in a seeded order, map the pick back to the key in code and log the order shown, since a writer model's keys cluster at one position.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "The 9 cached QC blocks have the key at positions 0, 1 and 2 three, five and one times.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "83",
     "quote": "view(item) { return { kind: \"choice\", stem: item.stem, options: item.options }; },",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Order options with seededOptionOrder(options), with no avoidFirst, read from the course-renderer mirror.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "19",
     "quote": "79% of MCQ corrects at Choice A",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "19",
     "quote": "skew is only exploitable if a renderer serves authored order; either way it fingerprints generator bias",
     "verbatim": true
    }
   ],
   "against": "\"The salt in seededOptionOrder was tuned for the course-renderer's own lessons; any seeded order serves the transformer.\" (2026-10-09-best-of-everything.json line 1). A shuffle removes the tell but not the skew, which \"either way it fingerprints generator bias\" (finding-taxonomy.md line 19), so the census in #45 is still needed.",
   "general": true,
   "duplicate_of": "#45",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (plan[7].how and .verified; compare-paragraphs.js line 60); direct-the-line.js line 59 likewise offers only the three deliveries, while debate.js line 103 and learning-question.js line 77 carry a 'no position' or 'nothing new' outcome. #33's detail already says a remaining choice carries a none-of-these option, so this is a duplicate of #33; kept because it adds the Jev skill's pattern 0 with its failure (a text that taught none of five procedures was labelled with the nearest) and the two engine choices still without one. Fix: stated as pattern 0 states it, for every choice put to a judge, not only key confirmations.",
   "statement": "Give every choice put to a judge a 'none of these' outcome: without one the judge labels an input with the nearest option, and a forced pick that confirms a key reads as agreement.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Add a 'none of these' option to the DL 'delivery' and CA 'stronger' choices (pattern 0 of the Jev skill).",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "The direct-the-line.js and compare-paragraphs.js choices have no 'none' outcome.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/engine/skills/jev/SKILL.md",
     "lines": "50",
     "quote": "options might not cover the input, or the model is forced to pick the closest wrong one.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/engine/skills/jev/SKILL.md",
     "lines": "52",
     "quote": "none of our five procedures was being labelled with the nearest.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "103",
     "quote": "D: \"no position on question\"",
     "verbatim": true
    }
   ],
   "against": "none found. Two of the engine's judge choices still lack one: the delivery choice (src/mechanics/direct-the-line.js line 59) and the stronger-paragraph choice (src/mechanics/compare-paragraphs.js line 60).",
   "general": true,
   "duplicate_of": "#33",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (plan[4].risk; debate.js lines 5 and 82). debate.js holds a block unless both sides can be defended from the passage (line 82, required), asks a bare stance why (line 17: three words or fewer, no reason word), checks the help takes no side (line 73) and closes with a model position whatever was said (lines 26-28). Fix: the side choice counts 'both, or partly each' as a position (line 103), so 'takes one' is too narrow. #22 bars a grade but says nothing about defensible sides, so not a duplicate.",
   "statement": "In an evaluative question, offer only sides a reader can defend from the text, and judge only that the student takes a position, one side or partly both, and backs it with a reason from the text, never whether it is right.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Judge only that a reason from the text is given, never whether the position is right.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "5",
     "quote": "reason is given, never whether the position is right.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "82",
     "quote": "as an answer to question, with a reason from passage?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "103",
     "quote": "C: \"both, or partly each\"",
     "verbatim": true
    }
   ],
   "against": "\"A counter drafted in advance cannot answer the student's own wording, so it is weaker.\" and \"Keep the criteria lenient until they are calibrated (rank 11).\" (2026-10-09-best-of-everything.json line 1). The free-text checks have no labelled cases yet.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep",
   "reason": "Quotes verbatim (plan[2].what; say-it-back.js line 22; key-words.js line 4). say-it-back.js line 28 names a slip in a term of five letters or more (same first letter, length within 2, edit distance at most 2, or 3 above seven letters) and still marks the sentence right (line 104); key-words.js line 119 nudges an answer within edit distance 2, and the second miss gives the word (line 118). It refines #25, which tolerates wording, by naming the task where spelling must be right; not a duplicate.",
   "statement": "Treat a near spelling by the task: in a sentence said back, name a slip in a long word without counting a miss; in typed recall of a taught word, nudge it, because a taught word must be spelled right.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Code checks that every term is there; a spelling slip is named but not counted as a miss.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "22",
     "quote": "a slip in a word of five letters or more, named but not a miss",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "4",
     "quote": "gets a nudge, since a taught word is spelled right; the second miss gives the word.",
     "verbatim": true
    }
   ],
   "against": "A near spelling in key-word recall costs a try (src/mechanics/key-words.js line 122 returns correct: false), and the edit-distance limits are the 3D build's, not measured. The animated word web is lenient too: \"(spelling slips are fine)\" (src/glue/animated.js line 113).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim (plan[2].risk), and nothing in src/mechanics/index.js or blocks.js caps blocks of a kind (blocks.js line 58 allows up to 20). As written, 'how often' is mostly settled by the Grade 9 design specification, whose close has one mimicry step. The open point that survives is that the specification's mimicry is the modelled method used in a sentence frame (kb-0204 line 272), while the engine's say-it-back has the student repeat the guide's sentence (say-it-back.js lines 1-2), the task the audit says rewards copying. Restated as that question, with the specification cited.",
   "statement": "Whether saying a model sentence back word for word makes a good first close question: it rewards copying the model's words, and one Grade 9 design specification asks instead for the modelled method used in a structured frame.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "It rewards repeating the guide's words, so keep it to one per lesson.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "2",
     "quote": "the lesson's answer in one sentence, its key words defined on hover; the student says or types it back.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "272",
     "quote": "Use the modeled method in a structured way.",
     "verbatim": true
    }
   ],
   "against": "none found. Both team builds draw mimicry as a sentence said back: \"Mimicry always replies 'Yes. Faithless, and false.'\" (2026-10-09-builders.json line 1).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "reason": "The audit (plan[2].from) and say-it-back.js line 1 are quoted verbatim, but 'say its answer back' misstates the source. The specification's first close step is mimicry, 'Use the modeled method in a structured way', with a sentence frame to complete as its example (kb-0204 line 272), then application to new evidence from the text and a justified judgement (lines 273-274). Corrected to the specification and cited to it. #34's order ends with a check and a later transfer, so not a duplicate; scoped to Grade 9 English.",
   "statement": "Close a lesson with a short run of questions on its learning question: use the modelled method in a structured frame, apply it to new evidence from the text, then make and justify a judgement.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "268",
     "quote": "moving from mimicry, to application to the text, to evaluation at the end",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "272",
     "quote": "Use the modeled method in a structured way.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "274",
     "quote": "Make and justify a judgement on the learning question.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Its close questions run mimicry, then application, then evaluation.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "1",
     "quote": "Say it back: the first of the Grade 9 close questions (mimicry, then application, then evaluation).",
     "verbatim": true
    }
   ],
   "against": "The engine has no apply block, and the 3D render exports none of its closing tasks: \"Closing tasks are not exported: say it back, debate, the apply task and the learning question's end-of-lesson return.\" (2026-10-09-builders.json line 1); its palette ends with two closers (v02/QA.md line 117). The specification calls its examples illustrative and says close questions are developed separately (kb-0204 line 268).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (plan[0].risk; reports[1].notDone[0]; Model.tsx line 9). Fix: cite the 3D build's Model step in the registered fork (othello-archive/src/steps/Model.tsx, the same line 9) instead of the unregistered mirror, and add line 8, which gives the reason; other lines of that header name a person and are left out. The builders' finding (typing that never started kept Next locked for students) shows the second cost of tying progress to an animation. On no record.",
   "statement": "Let the student pace a worked model: show each sentence whole beside its think-aloud and let nothing move on its own, since text typed out letter by letter reads as going fast.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "The animated Model types each step out letter by letter, but the 3D build dropped typing after review because it reads as going fast (Model.tsx header).",
     "verbatim": true
    },
    {
     "path": "~/Projects/othello-archive/src/steps/Model.tsx",
     "lines": "8",
     "quote": "typed text moves under the reader's eye and reads as \"going fast\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/othello-archive/src/steps/Model.tsx",
     "lines": "9",
     "quote": "Nothing moves on its own: no timers, no typing, no auto-advance.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "So any model node with screens, its own Lesson 1 included, never types its first move, and Next stays locked outside reviewer mode.",
     "verbatim": true
    }
   ],
   "against": "none found. The specification's live-modelling mode is \"Text writes out progressively\" (quoted in the header of othello-archive/src/steps/Model.tsx, line 1), which the 3D build reads as one whole sentence per Next.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep",
   "reason": "Quotes verbatim (plan[3].risk; personas.js line 2: the scripted readers never call a model). The rule is #11 applied to playtests: a judge marking picks it made checks against something that assumes the answer. So a duplicate of #11 (and close to #43), kept for this evidence. A team benchmark goes further and takes its blind solver from another model family, since one from the same family would tend to share the generator's and evaluator's blind spots (shadow/bench/src/inceptbench/tools/blind_solve.py lines 10-12, outside the registered sources).",
   "statement": "A simulated student must not be played by the model that judges it, or the judge marks its own picks.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Under 'Jev first', a persona's picks must not be Jev questions, or Jev grades itself.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/personas.js",
     "lines": "2",
     "quote": "(and Jev never grades a pick Jev made)",
     "verbatim": true
    }
   ],
   "against": "With scripted personas and a judge built from the keys, a playtest checks plumbing only (src/quality/playtest.js line 26: \"It proves plumbing, never the quality of judgment.\"). The model-played reader is not built: \"It needs live TrueFoundry calls and Grade 9 reader profiles that nobody has written yet.\" (2026-10-09-builders.json line 1).",
   "general": true,
   "duplicate_of": "#11",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep",
   "reason": "Quotes verbatim (plan[3].risk; playtest.js lines 3 and 9). playtest.js lines 4-9 define the three severities, and lines 107, 121 and 157 file a run the persona cannot play as persona-limited. #43 already rests on these personas and this playtest, so this is a duplicate of #43; kept because it adds how to read a playtest's findings.",
   "statement": "Sort every playtest finding as an engine fault, a known gap or a limit of the simulated reader, so a scripted reader's template prose never counts against the lesson and a run it could not play is not read as a pass.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Scripted free text is template prose, so label its rejections as persona limits (unit/playtest.js).",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/playtest.js",
     "lines": "3",
     "quote": "apart from persona limits, as its src/unit/playtest.js does. A broken invariant is a finding, never a crash:",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/playtest.js",
     "lines": "9",
     "quote": "the persona cannot play this: it says nothing about the engine",
     "verbatim": true
    }
   ],
   "against": "A persona-limited run tests nothing: \"the playtest reports each one as persona-limited (unknown-mechanic) and stops that run; it does not crash.\" (2026-10-09-builders.json line 1).",
   "general": true,
   "duplicate_of": "#43",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "keep",
   "reason": "Quotes verbatim (plan[10].how; calibrate.js line 18). The five seed sets hold 31 cases: the four play-time sets use these kinds (none has a near-quote case yet) and the bake set uses keyed-right and keyed-wrong. The 3D build's marking check sorts its cases short-right, misspelt-right, vague, nonsense, literal and near-quote; the injection kind comes from the Grade 3 engine's adversarial line, so 'the way check-marking.mjs sorts them' is loose. This says what the person-labelled cases of #35 should cover, so a duplicate of #35, kept for that evidence.",
   "statement": "Calibrate a marker on labelled answers of every kind students give: short and right, right but misspelt, vague, nonsense, literal, a near quote, and one that tries to instruct the marker.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Play-time checks get labelled student answers, sorted the way check-marking.mjs sorts them: short and right, right but misspelt, vague, nonsense, literal, near quote, injection.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
     "lines": "18",
     "quote": "export const ORDER = [\"short-right\", \"misspelt-right\", \"vague\", \"nonsense\", \"literal\", \"near-quote\", \"injection\"];",
     "verbatim": true
    }
   ],
   "against": "The seed sets measure nothing yet: \"The calibration numbers come from the label oracle, which answers from the labels themselves, so they prove the wiring and measure nothing.\" (2026-10-09-builders.json line 1), and \"a seed set this small is diagnostic only\" (src/quality/calibrate.js line 6).",
   "general": true,
   "duplicate_of": "#35",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (plan[10].what and .verified; calibrate.js line 105, already in the detail of #35). score() in calibrate.js, from line 84, computes precision of holds, recall of fails, false holds and the gap with its midpoint threshold, and marks every check that is not 'calibrated' advisory; the course renderer's fixtures do hold 199 judge cases and 27 trap cases. This is the method of #35, so a duplicate of #35, kept for that evidence. Fix: the against quoted 'The 0.35 probe floor is not calibrated', which is about the Grade 3 director's probe band (plan[9]), not this harness; replaced, and calibrate.js line 4 added for the measures.",
   "statement": "Measure a judged check on cases labelled to hold and to fail: report the precision of its holds, the recall of its fails and its false holds, set its threshold in the gap between the two groups, and keep it advisory while any labelled case goes wrong or its votes split.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "These harnesses supply the method: labelled states per check, several votes, and a threshold set where the two groups separate.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Its fixtures hold 199 judge cases and 27 trap cases, each with expect and why.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
     "lines": "105",
     "quote": "a check whose controls go wrong or flip should not hold a block or decide what a student is told",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
     "lines": "4",
     "quote": "recall of fails, and false holds (good cases the check would hold back)",
     "verbatim": true
    }
   ],
   "against": "\"Small sets are only diagnostic.\" (2026-10-09-best-of-everything.json line 1), and no check has been measured yet: the seed numbers \"prove the wiring and measure nothing\" (2026-10-09-builders.json line 1).",
   "general": true,
   "duplicate_of": "#35",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep",
   "reason": "Quotes verbatim (review.ruleBreaks[12]; open-check.js line 114; threejs-archivist.js line 126). On 12 Oct open-check.js line 115 gives no verdict and no try when nothing is refuted, and line 116 takes the first criterion that fails; threejs-archivist.js lines 138-139 do the same. #50 says unsure is never a miss but not which hint a partial miss gets; this adds that rule, from a bug found in review and fixed.",
   "statement": "When an answer falls short, hint at a part the judge is sure is missing, never at one it was unsure of.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "take the nudge of the first criterion that is not a sure hold. That can be one Jev was unsure of, rather than the one Jev is sure is missing",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "114",
     "quote": "only a criterion Jev is sure is missing makes a miss; unsure is no verdict, and no try",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "126",
     "quote": "only a criterion Jev is sure is missing is a miss, with that criterion's nudge; unsure is asked once more.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (review.ruleBreaks[11]; word-web.js line 99). On 12 Oct only the centre, the key words and their forms count in code (word-web.js lines 17 and 98-101); any other word goes to the judge or stays pending, and the 3D render's marking list is cut back the same way (threejs-render.js line 272). Fix: forms enter in code by sharing their word's first four letters (word-web.js lines 59-60), with no judge question, so the statement must allow them; 'writer model' for 'writer'. Related to #55 and #19, but neither says a writer's guesses are not a key.",
   "statement": "Mark an answer right in code only if it is a key a judge confirmed when the item was made, or a form of one; a writer model's list of likely answers is not a key.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "Writer deciding labels or marking with no Jev check that can hold it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "word-web.js:85 and :97: the writer's 'likely' words count as right in code, with only an advisory Jev check.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "99",
     "quote": "code knows only the forms of the centre and the key words (Jev checked those)",
     "verbatim": true
    }
   ],
   "against": "A form counts in code once it shares its word's first four letters (src/mechanics/word-web.js lines 59-60), with no judge question about it.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 17,
   "verdict": "keep-with-fix",
   "reason": "threejs-render.js line 373 is verbatim. The patch it labels (lines 366-372) finds the 3D build's own line that makes attempt 2 'secure' (line 369), records the answer as 'given', completes the step and never shows it as accepted; the engine's own mechanics never return a released answer as correct and flag it released: true. Fix: the audit's quote placing that rule at Reading.tsx lines 206 and 231 no longer matches the 3D build (the rule has since moved), so it is replaced by the patch itself, and the course renderer's item engine is cited directly (a given unit is worn as given and suppresses praise). Not covered by #49 or #42.",
   "statement": "When the answer is given after the last try, let the step finish but never mark it right or accepted, and record it apart from an answer the student earned.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "369",
     "quote": "if (v !== 'secure' && attempt >= 2) v = 'secure'",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "366",
     "quote": "two tries, then the answer is given and the step completes, but a given answer is not shown as \"Accepted\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/course-renderer/src/lib/scoring/item-engine.ts",
     "lines": "12",
     "quote": "U4 at the unit's ceiling, support fires for THAT UNIT ONLY, worn as given",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/course-renderer/src/lib/scoring/item-engine.ts",
     "lines": "14",
     "quote": "U6 any given unit suppresses the praise verdict",
     "verbatim": true
    }
   ],
   "against": "The engine's tick events have no 'given' type: src/core/runtime.js line 85 logs a tick as correct, incorrect, unsure or saved, though a released answer's saved record carries released: true (line 84). The 3D build's own rule still counts attempt 2 as secure; only the engine's patched export changes it.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (plan[14].from; runtime.js line 83, which adds an attempt on every settled tick with no check for a repeat). Fix: cite the rule where it is code, the course renderer's item engine (U1 at line 9; its try ledger skips a repeated signature at line 44). On no record.",
   "statement": "Don't charge a try for an answer resubmitted unchanged.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "An unchanged resubmission costs nothing; help comes at a unit's ceiling; single-select never reveals; given and earned completions are kept apart.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/course-renderer/src/lib/scoring/item-engine.ts",
     "lines": "9",
     "quote": "U1 an UNCHANGED submission is a noop and costs nothing",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/core/runtime.js",
     "lines": "83",
     "quote": "if (!unsure.length || response.correct != null) es.attempts++;",
     "verbatim": true
    }
   ],
   "against": "The engine's own player disables an option once tried, so a choice cannot be resubmitted there; the gap is in free answers and headless clients (2026-10-09-best-of-everything.json line 1: \"Only a headless client of the runtime can pick the same option again.\").",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "drop",
   "reason": "Quotes verbatim (plan[14].how and .risk; runtime.js line 4), but nothing here is a finding. The uncalibrated thresholds are already in the against of #27 ('three is not calibrated', and the same quote is offered to #27 as existing evidence); counting no student's own words follows from #22; the rest describes a director that is not built. A duplicate that adds no evidence.",
   "statement": "Which answers a student model may count: the plan counts only steps marked against a key, never a student's own words, its thresholds are uncalibrated, and nothing in the engine adapts yet.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "It keeps hits and misses per family (FAMILIES), from recognition steps only: QC, EH, WF, DL, film check and the CA pick. Never CER, and never own words.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "The thresholds (3, 0.8, 0.5) are Grade 3 engineering choices, not calibrated values.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/core/runtime.js",
     "lines": "4",
     "quote": "Own words are never marked",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "#27",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (review.summary item 2; review.ruleBreaks[2]; threejs-render.test.mjs line 125). The three places were the plain hunt and web screens, the animated build's pages through judgeRubric, and the 3D render's paragraph and web word; integration fixed all three, each with its own unsure test (v02/QA.md lines 126-129). Fix: 'paths' for 'screens', since two of the three were marking code, not screens. Broader than #47 (the slow or down path) and #41 (reviewer mode); not a duplicate.",
   "statement": "A rule about verdicts holds only where every path that marks or shows an answer obeys it, so test each path: after one fix, three other paths still showed an unsure judge as a miss.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "An unsure Jev is still shown as a miss in three places:",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "The rank-10 fix covers only the transformer's own runtime and blocks.play path.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "125",
     "quote": "unsure is never a pass and never a miss: the build's offline case, not an attempt",
     "verbatim": true
    }
   ],
   "against": "All three are now fixed: v02/QA.md lines 126-129 report unsure as neither pass nor miss in the 3D build, the animated pages and the engine's own view.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "keep",
   "reason": "Quotes verbatim (plan[1].how; reports[0].notDone[1]; transformer.mjs line 17); server.js line 58 and createBlocks (blocks.js line 33) use the same single sample for making and playing. #51 already says the same marker can give different verdicts on one answer, so this is a duplicate of #51; kept because it adds the limit that every make-time check is asked once, though a cached block would pay for a second ask only once (the against of #5 notes the same default in the Grade 3 engine).",
   "statement": "Whether to ask the judge more than once when a block is made: a cached block pays for the extra calls once, but every make-time check is asked once today.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Make blocks with samples 2 in createBlocks. Blocks are cached, so this costs once per block. Keep samples 1 at play time.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "Rank 2 step 7 (make blocks with samples 2) was not done.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/bin/transformer.mjs",
     "lines": "17",
     "quote": "const samples = Number(opt.samples ?? 1);",
     "verbatim": true
    }
   ],
   "against": "\"samples 2 doubles the Jev calls made while blocks are made.\" (2026-10-09-best-of-everything.json line 1).",
   "general": true,
   "duplicate_of": "#51",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep",
   "reason": "Quotes verbatim (plan[5].how; threejs.js line 54). exactIn falls back to findQuote without the mirror (threejs.js lines 56-61), while houseRules returns text unchanged (line 73) and nearMisses returns [] (lines 63-68). The against of #32 already notes the house rules don't run without the mirror; the general rule, that a missing tool must fail closed, is on no record, and #47 and #1 say to test such paths, not how they must fail.",
   "statement": "A check that cannot load the tool it relies on must fall back to another check or stop, never pass silently.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "When the mirror is missing, fall back to src/text.js findQuote instead of passing.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs.js",
     "lines": "54",
     "quote": "Without its tools, src/text.js findQuote, so a missing mirror never passes a quote",
     "verbatim": true
    }
   ],
   "against": "Still in code: src/glue/threejs.js line 73 (\"if (!available) return text;\") skips the house rules without the mirror, already in the against of #32, and line 64 says the near-miss finder returns \"[] if its tools are absent.\" A team benchmark's blind-solve probe fails open on purpose, recording the error, because it can only tighten a score (shadow/bench/src/inceptbench/tools/blind_solve.py lines 19-21, outside the registered sources).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (reports[1].notDone[6]; reports[2].notDone[2]). Fix: evidence added from the engine's own code: the 3D render patches the build's text-specific strings for other texts (threejs-render.js lines 374-375: an act and scene, the play's big idea), and the export sends web links only when the centre is deceit (line 262). On no record.",
   "statement": "Keep every line a student sees in the lesson's own data, not in the player: a reply, nudge, label or name built into a player for one text shows up wrongly on every other text.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "REBUILD_NUDGE is keyed by option text: options 'noun' or 'adverb' get a nudge about 'follow' on any text.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "Mimicry always replies 'Yes. Faithless, and false.' and its speech hints name Othello's cast.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "The 'Link to deceit' card label is shared, so our links are shown only when the web's centre is deceit.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "374",
     "quote": "no act and scene for a text that has none",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "262",
     "quote": "webLinks: ww?.item.centre === \"deceit\" ? Object.fromEntries(ww.item.keys.map((k) => [k.word, k.link])) : {},",
     "verbatim": true
    }
   ],
   "against": "Some leftovers are harmless: \"Its transcriber hints name Othello's characters, which does no harm on other texts.\" (2026-10-09-best-of-everything.json line 1).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep",
   "reason": "Quotes verbatim (plan[13].what; learning-question.js lines 2 and 64). respond() saves both answers and marks neither (lines 89-99), and what the second answer adds is named only on a sure pick, never as a mark (lines 71-86). #22 and #52 cover keeping words unmarked; the question's bookends are on no record.",
   "statement": "Show the lesson's question on its own with its key phrases explained but not answered, keep a first answer unmarked, and ask the question again at the end, saved beside the first.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "One is the question shown on its own with its key phrases explained, then answered again at the end.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/learning-question.js",
     "lines": "2",
     "quote": "never the answer), and a first answer the student may keep, never marked.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/learning-question.js",
     "lines": "64",
     "quote": "Does note_${i} say what phrase_${i} asks or means in question, without answering question?",
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
   "reason": "Quotes verbatim (plan[13].risk; review.ruleBreaks[11]; worked-model.js line 112). worked-model.js line 103 makes the class check advisory and absorb() (lines 113-116) blanks any class the judge did not confirm; glossary.js line 125 makes gloss_fits required for drafted notes. #54 gives the quiet-misleading reason for glosses and #50 that unconfirmed classes are hidden, but neither gives the rule for deciding which checks may hold a block.",
   "statement": "Decide whether a check may hold back a block by what its error would do: a wrong gloss misleads without anyone noticing, so its check must hold; a judgment call such as a word class should not hold, but a label the judge did not confirm is not shown.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "A wrong gloss on Shakespeare misleads quietly, so gloss_fits must be required, not advisory.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "worked-model.js:103: the class check is advisory, so a confident Jev no still ships (the audit advised this).",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "112",
     "quote": "a word class is a judgment call on Shakespeare, so it never holds the block, but one Jev did not confirm is not shown",
     "verbatim": true
    }
   ],
   "against": "An advisory check is not harmless at play time: \"an advisory check still changes what a student\" is told (src/quality/calibrate.js line 79). A glossary passed through from its owner is never held by the check (src/mechanics/glossary.js line 125: \"required: drafted\"). By #35 a check that holds a block should first be scored on person-labelled cases, and the gloss check has none yet.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "keep",
   "reason": "Quotes verbatim (plan[11].what; key-words.js lines 92 and 100). Code holds a sentence without exactly one blank, or with the word or a form of it anywhere, quotations included (key-words.js lines 26-31 and 75-76), and another deck word the writer lists as fitting is not a miss (line 117). Applies #29 and #54 to practice, but typed recall is on no record.",
   "statement": "Practise taught words by typed recall: cue each by its meaning in a sentence about the text whose one blank points to that word alone and never contains it or its forms, and list the study set in an order unrelated to the gaps.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Each word is cued by its meaning in a gap sentence from the text, and the student types it from memory.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "92",
     "quote": "does gap_${i} point to word_${i} rather than to any other word in deck?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "100",
     "quote": "the study set in alphabetical order, and the gaps with their cues, so no gap lines up with its word",
     "verbatim": true
    }
   ],
   "against": "\"In the animated render, keyword_cards offers a choice, not recall, so the full deck appears only in the transformer's own view.\" (2026-10-09-best-of-everything.json line 1).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep",
   "reason": "The quote is verbatim (ranked.dropped[6]), and the course renderer's fixture files do hold 199 judge cases and 27 trap cases. The detail of #35 already says a change measured on a different set must not be called lift, so this is a duplicate of #35; kept for the case it adds, a score (82/82) that outlived the set it was measured on.",
   "statement": "Quote a check's score only with the case set it was measured on, and measure again when the set changes.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "The 82/82 figure comes from an earlier set; the method stands.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "#35",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (plan[15].verified, plan[14].risk; quick-check.js line 1). Every choice block normalises to exactly three options (quick-check.js line 39, word-in-focus.js line 45, film-check.js line 57, video-essay.js line 87; three deliveries in direct-the-line.js line 39). Fix: cite the four-option rule in the registered course-renderer checkout too (validate-contracts.mjs line 366). Open, and on no record.",
   "statement": "How many options a choice question should have: one renderer's validator requires exactly four, while this engine's choice blocks use three.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "validate-contracts.mjs line 365 requires exactly 4 MCQ options.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/course-renderer/scripts/validate-contracts.mjs",
     "lines": "366",
     "quote": "mcq must have exactly 4 options",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "1",
     "quote": "three options, exactly one defensible.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "A reveal on a three-option item gives the key away by elimination, so keep U5.",
     "verbatim": true
    }
   ],
   "against": "none found. The against of #49 already notes that with three options elimination ends an item in three picks.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 29,
   "verdict": "keep",
   "reason": "Quotes verbatim (reports[1].notDone[1]; plan[11].how; blocks.js line 67). blockKey hashes only the maker version, text, question, mechanic and number (blocks.js line 25), and lines 69-74 gather what earlier blocks of the same kind cover. #48 covers blocks of one kind; across kinds is open.",
   "statement": "How a block can build on what other kinds of block in the same lesson taught: blocks are made from the text, the question and their own kind alone, so a key-word deck cannot reuse the word web's words.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "KW is not seeded from the strip's word web, as the audit asked. A block is made from text, question and mechanic only and cannot see the strip.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "If the strip has a word-web block, seed the deck from its keys.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/blocks.js",
     "lines": "67",
     "quote": "what the lesson's earlier blocks of this kind cover",
     "verbatim": true
    }
   ],
   "against": "The 3D render joins them after the fact: it puts the web's key words into its key-words step (src/glue/threejs-render.js line 224, in a deck labelled \"Words for\" the centre word).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 30,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (plan[2].how; key-words.js line 78; word-web.js line 68, which checks the centre's meaning, while line 71 checks the key words'). Fix: add say-it-back.js line 79, which implements the audit's rule for term notes; glossary.js line 115 does the same for drafted notes. On no record; #54 is about which words to gloss.",
   "statement": "A note that explains a word must not use that word, and code can check it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "codeChecks: each term is in the sentence; the sentence is at most 16 words; no note uses its own term.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "79",
     "quote": "No note uses its own word",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "78",
     "quote": "No meaning uses its word",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "68",
     "quote": "The meaning does not use the word",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "drop",
   "reason": "util.js line 122 and the audit quote are verbatim, but the detail of #14 already cites feedbackJudged and the film-stop truth check. That check asks only whether everything a feedback line says is true to what the film has given (util.js line 128), not whether it says what is wrong with the option, which is the audit's unbuilt proposal; and 'say what is wrong with that option' cannot apply to the right option's line, which the check also asks. What is left, that the quick check, word in focus and direct the line never judge their feedback, is a limit for #14, not a new learning.",
   "statement": "Judge each option's feedback on its own, as one bounded question: it must be true to what the student was given and say what is wrong with that option.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "per wrong option: does feedback[i] say what is wrong with option i, true to the text?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "122",
     "quote": "The feedback after each option, held to what the film has given by that stop",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "#14",
   "name_bearing_source": false
  },
  {
   "index": 32,
   "verdict": "keep",
   "reason": "Quotes verbatim (open-check.js lines 41-42; reports[1].notDone[4]). Code holds any rung that uses a leak word or copies a four-word run of the reveal outside quotation marks (open-check.js lines 63-66 and 71), and the animated export passes all three rungs (animated.js line 160) with two tries (line 43). #14 covers what a hint may say; the graded ladder is on no record.",
   "statement": "Write a ladder of hints for an open check, each closer than the last and none giving the answer: where to look with one question, then closer, then the words to reread quoted exactly.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "41",
     "quote": "\"nudge\": \"where to look, and one question, without the answer\", \"second_nudge\": \"closer, still not the answer\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "42",
     "quote": "\"third_nudge\": \"the words to read again, quoted exactly, still not the answer\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "Their second and third nudges still feed the build's Hint button.",
     "verbatim": true
    }
   ],
   "against": "With two tries before the answer, a student who never asks for help sees only the first rung (\"OC and DB use max_tries 2, not the audit's 3.\", 2026-10-09-builders.json line 1), and the engine's own view only ever shows the first nudge (src/mechanics/open-check.js line 117).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "The script's comment 'git show writes nothing there' is wrong for that case, and test/laws.test.mjs treats show and ls-tree as reads.",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "Nothing tests whether a key can be picked without reading.",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports (not used: about two judges agreeing, not one judge's samples; the against of record 21 already says it)",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "Agreement between two judges is not correctness.",
   "ok": false
  },
  {
   "truth": 5,
   "effect": "supports (not used: the replay compares a second judge, not one judge's samples)",
   "path": "~/Projects/g9/transformer/bin/transformer.mjs",
   "lines": "81",
   "quote": "(agreement, not correctness)",
   "ok": false
  },
  {
   "truth": 6,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "Drama invites false positives: an answer quoting a command from the play ('Put money in thy purse') must not read as addressing the grader.",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/util.js",
   "lines": "133",
   "quote": "only a confident yes acts, and then the words are not an answer.",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
   "lines": "7",
   "quote": "them counts if the judge finds it gives clear evidence too.",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
   "lines": "30",
   "quote": "the text becomes the build's reading sections, cut so each checkpoint follows the lines it asks about",
   "ok": true
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "Not so. The animated build already draws model (with rebuild and guided screens), mimicry, evaluate, learning_question, keyword_cards, independent and record (its src/contract.ts lines 40-188; src/nodes/index.tsx NodeView).",
   "ok": true
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
   "lines": "2",
   "quote": "The judge, reading the same lines around it, must pick the same delivery.",
   "ok": true
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "A quotation made up outright passes, because nearQuotes gives nothing for a quote nowhere near the scene.",
   "ok": true
  },
  {
   "truth": 13,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "A quote across two speeches never matches, a limit of the 3D build's matcher.",
   "ok": true
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/util.js",
   "lines": "57",
   "quote": "The item's own wording, which a line of its feedback may quote: its options, stem, claim and the like (the pool rule",
   "ok": true
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
   "lines": "78",
   "quote": "Nearly. One or two of those words are not the text's own: check the wording against the text.",
   "ok": true
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
   "lines": "54",
   "quote": "A pointer back to the words that hold the answer, without saying what they show.",
   "ok": true
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
   "lines": "63",
   "quote": "a hint may quote the text, even the line to",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports (not used: this judge is given the two paragraphs the student sees; the fault is that its factual-error question needs the text, which goes to record 19 with line 61)",
   "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
   "lines": "57",
   "quote": "const state = { paragraph_A: item.paragraphs[0], paragraph_B: item.paragraphs[1] };",
   "ok": false
  },
  {
   "truth": 19,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
   "lines": "61",
   "quote": "free of factual errors about the text it discusses?",
   "ok": true
  },
  {
   "truth": 21,
   "effect": "supports (not used: outdated; blocks, plays, focus lines and the animated judge now keep their decide records, blocks.js lines 4-5 and 94, animated-judge.js line 11)",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "Blocks, play-time ticks, the animated judge endpoint and focus lines keep no decision records, so only the transform and proof paths can be replayed.",
   "ok": false
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "replay.js line 15 requires state and questions[0].instructions; the runs/lessons/*.decisions.jsonl records carry both.",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/core/runtime.js",
   "lines": "4",
   "quote": "Own words are never marked",
   "ok": true
  },
  {
   "truth": 25,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
   "lines": "4",
   "quote": "gets a nudge, since a taught word is spelled right; the second miss gives the word.",
   "ok": true
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
   "lines": "14",
   "quote": "a short answer that says it is enough (the 3D build's marking rule), so only noise is turned away before Jev",
   "ok": true
  },
  {
   "truth": 27,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "The thresholds (3, 0.8, 0.5) are Grade 3 engineering choices, not calibrated values.",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "A word-in-focus gloss may name an epithet as an insult, as the animated build's gloss does, but a student is never asked to perform it.",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "'the Moor' lines may come back unsure and hold direct-the-line or word-in-focus blocks more often.",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "lines such as 'an old black ram' are left to the Jev question.",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/quality/playtest.js",
   "lines": "16",
   "quote": "The student view never carries a key, feedback, evidence or a model answer",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/quality/playtest.js",
   "lines": "156",
   "quote": "the runtime has no idle or timer action, so nothing nudges a reader who is stuck",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "These should stay behind: the Grade 3 loop and level shapes, its prompts and praise lines",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports (not used: outdated; the worked-model block, placed before CER, now models before the student writes)",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "Nothing in the transformer models before the student writes; CER shows its model only after saving.",
   "ok": false
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "The labels need a person; model-made labels measure nothing.",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "The calibration numbers come from the label oracle, which answers from the labels themselves, so they prove the wiring and measure nothing.",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "They need cases in the calibration set (rank 11) before anyone relies on them.",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
   "lines": "79",
   "quote": "an advisory check still changes what a student",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/blocks.js",
   "lines": "17",
   "quote": "Bumped when what a maker produces changes (prompts, checks), so an old block is made again, not served.",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "So any model node with screens, its own Lesson 1 included, never types its first move, and Next stays locked outside reviewer mode.",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "The playtest is not yet run as a gate inside the server before a scene is served.",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/quality/playtest.js",
   "lines": "26",
   "quote": "It proves plumbing, never the quality of judgment.",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "The 9 cached QC blocks have the key at positions 0, 1 and 2 three, five and one times.",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "A grep finds no shuffle in src or web, nor in the animated build.",
   "ok": true
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "235",
   "quote": "Three-word runs of a line: the rules fallback's keywords, used only if the judge endpoint cannot be reached.",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/blocks.js",
   "lines": "67",
   "quote": "what the lesson's earlier blocks of this kind cover",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "Its own player (web/lesson.js options()) disables an option once tried, so a student reaches the key within three picks.",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "A reveal on a three-option item gives the key away by elimination, so keep U5.",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "OC and DB use max_tries 2, not the audit's 3.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
   "lines": "99",
   "quote": "an unsure criterion is never a pass and never a miss. The word web's own rule is to be generous, so there an unsure",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "128",
   "quote": "(its generous word web takes the word)",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/transform.js",
   "lines": "78",
   "quote": "an unsure judge is not a no: the correction asks for a version that plainly holds, not for its opposite",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/blocks.js",
   "lines": "47",
   "quote": "a judge that answered nothing found nothing: that empty focus is not kept as the text's",
   "ok": true
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
   "lines": "41",
   "quote": "a play-time case names a line by its words",
   "ok": true
  },
  {
   "truth": 53,
   "effect": "supports (not used: outdated; the 'Line N' card labels are gone from web/lesson.js)",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "and line 327 labels the direct-the-line quote 'Line N'.",
   "ok": false
  },
  {
   "truth": 53,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "The animated glossary matches by text within a line, so a repeated word needs the right line index.",
   "ok": true
  },
  {
   "truth": 54,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "optionally, judgeTerms with readingGrade 9 keeps only words a reader would not know unaided",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "A counter drafted in advance cannot answer the student's own wording, so it is weaker.",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "The 3D build writes its push-back live to the student's words.",
   "ok": true
  }
 ]
}
```
