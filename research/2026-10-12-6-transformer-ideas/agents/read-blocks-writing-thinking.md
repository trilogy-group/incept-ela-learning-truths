# read:blocks-writing-thinking

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  nono, analyse its ideas and fold them into the research results

## Result

```json
{
 "direction": "blocks-writing-thinking",
 "coverage": {
  "read": [
   "~/Projects/g9/transformer/src/mechanics/worked-model.js, cer-frame.js, compare-paragraphs.js, say-it-back.js, debate.js, direct-the-line.js (all, line by line)",
   "~/Projects/g9/transformer/src/mechanics/util.js and index.js (shared house rules, quotation and grader guards); one line of quick-check.js (its length rule, for comparison)",
   "~/Projects/g9/transformer/src/engine.js, judge.js, house.js, question.js, text.js, transform.js, blocks.js, core/runtime.js, glue/threejs.js, glue/animated.js (header, block mapping, model node)",
   "~/Projects/g9/transformer/src/quality/personas.js, calibrate.js, playtest.js",
   "~/Projects/g9/transformer/web/lesson.js (the six blocks' views and the player)",
   "~/Projects/g9/transformer/test/mechanics.test.mjs, helpers.mjs, runtime.test.mjs, laws.test.mjs, quality.test.mjs, glue.test.mjs, animated.test.mjs (the parts on these blocks); test/fixtures/othello-items.json (the six fixtures); test/calibration/cer-frame.next-step.json and cer-frame.addresses-grader.json",
   "~/Projects/g9/transformer/README.md, DECISIONS.md, v01/QA.md, v01/README.md, v01/proof-2026-10-09.json, v02/QA.md, v02/README.md, v04/README.md, v05/README.md, v09/README.md",
   "~/Projects/g9/transformer/runs/blocks/ (the 32 saved blocks of these six mechanics summarised by status, reasons, judge verdicts and key positions; 12 opened in detail)",
   "~/Projects/g9/transformer/runs/calibration/*.json and runs/playtest/*.json (summaries only)",
   "~/Projects/g9/transformer/samples/ozymandias.md (one line checked against a held push-back)",
   "~/Projects/grade3-reading/engine/src/decide/questions.js (support gates and option-order rotation the judge layer uses)",
   "git log and commit message for transformer/src/mechanics (one commit, no history of these files)"
  ],
  "skipped": [
   "The other ten mechanics (quick-check apart from one line, evidence-hunt, word-in-focus, word-web, glossary, key-words, open-check, learning-question, film-check, video-essay): outside this direction",
   "runs/decisions/*.jsonl and runs/playtest/*.decisions.jsonl: decision logs, data dumps",
   "runs/lessons, runs/marking, runs/scenes, runs/sessions, runs/films, runs/render, runs/art-cache: not about these blocks, or media and renders",
   "src/glue/threejs-render.js, src/glue/animated-judge.js, src/server.js, src/video/: render, serving and film plumbing",
   "~/Projects/shadow/3d-build/server/tasks/close.mjs: opened to see where the debate's rules came from, then not used or cited: it mirrors a teammate's repository and its comments name a person; the g9 block carries the same rules",
   ".agent/ operating files: session orientation, not findings for this direction"
  ],
  "notes": "Every path holds the owner's account name in its home directory; no other person's name is in any cited path, so name_bearing_source is false throughout. runs/ is git-ignored output of the always-on composer: a block remade later can change those files and their line numbers (cited as they stood on 12 October). The counts in the key-position candidate are mine, made across runs/blocks; nothing in the repo writes them down. Every saved calibration run of the claim-evidence-reasoning checks used the label oracle, so no judged check in these six blocks has been measured on the real judge against labelled cases. The delivery block's judge reads up to three lines either side of the target (direct-the-line.js line 55) while its own view shows only the three lines before (line 67): the judge can see lines the block's card does not show. No consequence was seen, so it is noted here and not used as evidence. The debate's comment on its code path (lines 123-124) says that with no judge the model position closes the task. But the runtime and blocks.playItem take the judged path whether or not a judge is present, so a real stance with no judge gets 'Say it once more, plainly' (line 118). That is recorded as the open question on steps with no verdict. Gettysburg-speech blocks in runs/ came from the composer's shelf; only the Ozymandias line was checked against a sample file."
 },
 "candidates": [
  {
   "statement": "Where an item's key is a judgment call, have the judge answer the item itself without the key, and keep the item only if it picks the key with a clear margin.",
   "kind": "adopted rule",
   "found_by": "Built into the comparison and delivery blocks. The judge is given the two answers, or the line with up to three lines either side, and must pick the writer's key. On the live proof it did so at p 0.96 and 0.99 for the comparisons and p 1 and 0.98 for the deliveries.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "2",
     "quote": "The judge must choose the same paragraph with a clear margin, so there is one defensible pick."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
     "lines": "2",
     "quote": "The judge, reading the same lines around it, must pick the same delivery."
    },
    {
     "path": "~/Projects/g9/transformer/v01/proof-2026-10-09.json",
     "lines": "197-200",
     "quote": "\"p\": 1"
    }
   ],
   "against": "The margin is the engine's support gates, \"conservative engineering thresholds, not calibrated correctness\" (grade3-reading/engine/src/decide/questions.js line 105). The offline stand-in judge \"picks paragraph A and delivery A\" (test/helpers.mjs line 13) while the fixtures key A, so these checks cannot fail offline. A clear margin also passes wrong options nobody would pick. The choice block met that with an advisory check of \"whether each wrong option would tempt a reader who skimmed\" (v01/QA.md line 43); the comparison and delivery blocks have no such check.",
   "scope_note": "universal: items whose key is a judgment call (which answer is stronger, which delivery fits)",
   "adds_to_existing": [
    11,
    31
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check each wrong option of a fill-in-the-blank in place: put it into the sentence and ask whether the whole sentence is then wrong about the text.",
   "kind": "adopted rule",
   "found_by": "The worked model's judge is given each wrong option already put into the rebuilt sentence. On a speech, a wrong option taken from the quotation itself was judged to leave the sentence true (p 0.31 that it was wrong), and the block was held after two tries.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "50",
     "quote": "the other two are wrong about the text or the word."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "106",
     "quote": "Is sentence_${x.k}_${x.j} wrong about quote or about passage?"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/be97f27fc4c4a65a.json",
     "lines": "120",
     "quote": "makes the rebuilt sentence wrong: the judge found this does not hold"
    }
   ],
   "against": "\"One sample per judge question.\" (v01/QA.md line 45): each wrong option is judged once.",
   "scope_note": "universal: fill-in-the-blank and drop-down items",
   "adds_to_existing": [
    31
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Left to itself, a writer puts the right answer in a predictable place, so the position needs setting in code: the best delivery was second of three in all 4 saved delivery items, and the right option came first in 5 of 6 saved rebuild blanks.",
   "kind": "measured",
   "found_by": "Counted across the saved blocks under runs/blocks: the delivery key was index 1 in 4 of 4 items (three texts), and the rebuild's right option was index 0 in 5 of 6 blanks. Neither block reorders its options before the student sees them, and no code check looks at the key's position.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/4c5df03f78a26e6e.json",
     "lines": "22",
     "quote": "\"best\": 1,"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/eb9231d930fa07c4.json",
     "lines": "23",
     "quote": "\"best\": 1,"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
     "lines": "68",
     "quote": "context: before, deliveries: item.deliveries"
    }
   ],
   "against": "Comparison keys came out closer to even (A in 6 and B in 4 of 10 saved blocks), and the samples are small (4 delivery items, 6 rebuild blanks).",
   "scope_note": "universal: generated choice items",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep surface features from giving the answer away: two answers to compare stay close in length, the longer at most 1.6 times the shorter.",
   "kind": "adopted rule",
   "found_by": "A code check in the comparison block, labelled \"Length does not give the stronger one away\". The choice block has the same rule at 2.2 times.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "51",
     "quote": "Math.max(...wc) <= 1.6 * Math.min(...wc)"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "23",
     "quote": "write two short paragraphs (50 to 90 words each)"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "55",
     "quote": "No option stands out by length"
    }
   ],
   "against": "none found",
   "scope_note": "universal: comparison and choice items",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Where the parts of a generated item must point at each other, check the links in code before any judge: the word explained is in the quotation, the reasoning names it, and the rebuilt sentence is the model's sentence.",
   "kind": "adopted rule",
   "found_by": "Code checks in the claim-evidence-reasoning and worked-model blocks. A planted fault (the rebuild pointed at the wrong sentence) fails the rebuild check in the tests.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "51",
     "quote": "the reasoning never mentions the word it explains"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "83",
     "quote": "The rebuild, set right, makes its sentence"
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "118",
     "quote": "find((c) => c.id === \"rebuild-makes-sentence\").ok, false"
    }
   ],
   "against": "Code can only test that one part names another: \"Each word's line is about its word\" is checked as has(w.line, w.word) (worked-model.js line 79), and what the line says is left to the judge.",
   "scope_note": "universal: generated items with several linked parts",
   "adds_to_existing": [
    11
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count a quotation as exact when it is the text's words in order, punctuation, case and apostrophes aside, and never when it runs across a stage direction or from one speech into the next.",
   "kind": "adopted rule",
   "found_by": "The worked model and the house checks use another build's quotation matcher, brought over as it is.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs.js",
     "lines": "53",
     "quote": "Is this quotation the text's exact words? Its quotedLines: punctuation, case and apostrophes aside, never across a"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs.js",
     "lines": "54",
     "quote": "stage direction or two speeches."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "75",
     "quote": "the quote is not an exact quotation from the text (within one speech)"
    }
   ],
   "against": "The claim-evidence-reasoning block checks with the looser finder, which \"may span consecutive lines\" (src/text.js line 52) and has no speech boundary.",
   "scope_note": "universal; the speech boundary matters in drama",
   "adds_to_existing": [
    13
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A writer told to quote the text inside a question may weave the text's words in without quotation marks: two sets of push-backs, on a poem and a speech, were held for it after two tries each.",
   "kind": "measured",
   "found_by": "Two debate blocks made on 12 October, on a poem and a speech, failed only the code check that each push-back quotes the text, after two tries each. Their push-backs used the text's exact words with no quotation marks.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/f23aebacf033daa2.json",
     "lines": "13",
     "quote": "How do the details of a wrinkled lip and sneer of cold command suggest a ruler who also possessed great passion?"
    },
    {
     "path": "~/Projects/g9/transformer/samples/ozymandias.md",
     "lines": "6",
     "quote": "And wrinkled lip, and sneer of cold command,"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/f23aebacf033daa2.json",
     "lines": "28",
     "quote": "Each push-back quotes the text: a push-back quotes no words from the text"
    }
   ],
   "against": "The drama debate's push-backs marked the text's words as quotations (\"How do you explain his admission that he will throw\", runs/blocks/90a1089f3e8d7ad5.json line 13), and two blocks are a small sample.",
   "scope_note": "generated questions that quote a text; seen on a poem and a speech",
   "adds_to_existing": [
    13
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A code check can hold good work, so test it on fair cases too: an exact-quotation check held a fair one-word quotation until it accepted single words found in the text.",
   "kind": "measured",
   "found_by": "A live comparison on a poem was held because a paragraph quoted one word of the text. The check was widened to accept a single word found in the text, with a test.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "38",
     "quote": "Ozymandias's comparison was held once: one paragraph quoted the single word"
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "39",
     "quote": "and the exact-quotation check only accepted quotations of two or more words."
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
     "lines": "4",
     "quote": "false holds (good cases the check would hold back)"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When a draft is held because the judge could not confirm a point, ask the writer for a version that plainly holds or for another choice, not for the opposite.",
   "kind": "adopted rule",
   "found_by": "Before the change, a draft held by an unsure judge was told only that the check was unclear.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "78",
     "quote": "an unsure judge is not a no: the correction asks for a version that plainly holds, not for its opposite"
    },
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "79",
     "quote": "the judge could not confirm this; rewrite it so that it plainly holds, or choose another"
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "191",
     "quote": "it now asks for a version that plainly holds; before, it only said \"unclear\"."
    }
   ],
   "against": "none found",
   "scope_note": "universal: write, check and correct loops",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Settle in code what code can settle about a student's words before any judge sees them: refuse noise and answers too thin to be one, and send back a quotation that is not the text's exact words without giving the wording.",
   "kind": "adopted rule",
   "found_by": "Played live in another build's renderer, the block refused a keyboard-mash answer, sent a misquotation back as not the text's words, and saved the exact quotation. Its calibration set notes that such answers are stopped by code first and never reach the judge.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "2",
     "quote": "Code checks only what is fact: each box has real words, and the evidence is an exact quotation from the text."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "100",
     "quote": "Copy the words exactly from the text, so your quotation can be found."
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "61",
     "quote": "CER-1 refused \"asdf qwer zxcv\", sent \"I follow him because I love him\" back as"
    }
   ],
   "against": "These gates have no try limit: the block's response never reads the try count (cer-frame.js lines 94-102), so a reader who cannot quote exactly is asked again with no end.",
   "scope_note": "universal: student free text",
   "adds_to_existing": [
    13,
    14
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Put a student's words in a field of their own in the judge's state and ask about that field by name, never inside the question's wording.",
   "kind": "adopted rule",
   "found_by": "Both blocks that judge a student's words at play time put them in named fields of the state and ask about those fields, beside a guard on words aimed at the marker.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "93",
     "quote": "the student's position goes to Jev in its own field"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "101",
     "quote": "Does student_text answer challenge with a reason from the text?"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "74",
     "quote": "claim: String(action.claim), evidence: String(action.evidence), reasoning: String(action.reasoning)"
    }
   ],
   "against": "none found",
   "scope_note": "universal: any judgment of a student's words",
   "adds_to_existing": [
    6,
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A guard against answers aimed at the marker must count quoted or retold commands from the text, and weak but real attempts, as answers, and its test cases should keep both as controls.",
   "kind": "adopted rule",
   "found_by": "The guard comes from the Grade 3 engine and is asked beside every play-time judgment of a student's words. Its seed set keeps a paragraph that quotes a character's commands, and a vague one, as answers that must pass.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "135",
     "quote": "Words quoted or retold from the text, a character's commands among them, are part of an answer and do not count."
    },
    {
     "path": "~/Projects/g9/transformer/test/calibration/cer-frame.addresses-grader.json",
     "lines": "5",
     "quote": "Drama invites false alarms: a paragraph that quotes a character's commands is an answer, and is kept here as a control."
    },
    {
     "path": "~/Projects/g9/transformer/test/calibration/cer-frame.addresses-grader.json",
     "lines": "11",
     "quote": "Weak, but an attempt at the prompt: vague is not addressing the grader."
    }
   ],
   "against": "Measured only against a label oracle that \"proves the wiring, measures nothing\" (runs/calibration/2026-10-09T12-25-25-449Z.json line 6). The guard also acts only on a sure yes: \"the guard acts only when Jev is sure\" (test/glue.test.mjs line 31).",
   "scope_note": "universal for judged student text; matters most where the text is full of commands, as drama is",
   "adds_to_existing": [
    6,
    35
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give student writing at most one next step: the change that would most improve it, picked from steps written in advance, shown only when the judge is sure, and none when nothing needs changing.",
   "kind": "adopted rule",
   "found_by": "An audit found the step came from another build's paragraph coach through a second model (6.6 s). It became a choice among four authored steps (0.26 to 0.48 s live). Live, a paragraph explaining no word got the word step, a claim off the question got the claim step, and a full paragraph got none.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "67",
     "quote": "one Jev choice, asked only of a saved answer: which one change would most improve the paragraph."
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "99",
     "quote": "It is now a Jev choice among four authored steps, filled with the student's own words,"
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "102",
     "quote": "a paragraph doing all three got no step (0.26 s)."
    }
   ],
   "against": "Its only calibration runs used a label oracle, \"answers from the labels themselves: proves the wiring, measures nothing\" (runs/calibration/2026-10-09T12-25-25-449Z.json line 6), on five seed cases.",
   "scope_note": "feedback on student writing; built for Grade 9 claim-evidence-reasoning paragraphs",
   "adds_to_existing": [
    22,
    55
   ],
   "name_bearing_source": false
  },
  {
   "statement": "After an open task, show the model as one strong answer or one position the student could defend, never as the answer, and only once the student's own answer is in.",
   "kind": "adopted rule",
   "found_by": "Three blocks do this. The model paragraph is revealed only once the student's answer is saved. The debate closes on a model position whatever was said. The worked model's paragraph comes after the rebuild.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "101",
     "quote": "Saved. Here is one strong answer to compare with yours."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "27",
     "quote": "Here is one position you could defend:"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "118",
     "quote": "the paragraph comes after the rebuild"
    }
   ],
   "against": "none found",
   "scope_note": "open writing and evaluative tasks",
   "adds_to_existing": [
    22,
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Pitch a model answer at what a strong student of the grade could write in the time, not at expert writing.",
   "kind": "adopted rule",
   "found_by": "Writer prompts in four blocks and advisory judge checks in two. On the live proof the grade check held at p 0.84 and 0.86.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "61",
     "quote": "Is this model answer something a strong Grade 9 student could write in about five minutes?"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "62",
     "quote": "Do both paragraphs read like writing by Grade 9 students"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "52",
     "quote": "a position a strong Grade 9 student could defend, with a reason from the text."
    }
   ],
   "against": "These checks are advisory (required: false), so they never hold a block. On the live drama comparison the student-voice check came back \"unclear\" at \"p\": 0.59 and the block shipped (v01/proof-2026-10-09.json lines 265-268).",
   "scope_note": "model answers at any grade; set here for Grade 9",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Feedback names what the student sees by the labels on their screen, never by the item's own workings.",
   "kind": "adopted rule",
   "found_by": "Feedback the writer drafted named the answers \"Paragraph a\" while the screen showed \"Answer A\". The comparison block now renames them, and film stops have a code check against production words.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "39",
     "quote": "the reader sees \"Answer A\" and \"Answer B\", so the feedback names them that way (\"paragraph b\" -> \"Answer B\")"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/ed2f90f660c18774.json",
     "lines": "13",
     "quote": "Paragraph a is stronger because it makes a precise claim"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "111",
     "quote": "What a viewer reads at a film's stops (the questions, options and feedback) speaks of the film, never of how it is"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    53
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A note that defines a word must not use that word or its stem.",
   "kind": "adopted rule",
   "found_by": "A code check in the say-it-back block. It matches the word itself or, for words of six letters or more, its stem.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "79",
     "quote": "No note uses its own word"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "34",
     "quote": "x.startsWith(norm(w).slice(0, -2))"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "56",
     "quote": "note: its plain meaning here, at most 10 words, without"
    }
   ],
   "against": "none found",
   "scope_note": "universal: definitions and glosses",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "What ends a step whose answers get no verdict: one block asks a reader who cannot quote exactly to try again with no limit, and another does the same when the judge cannot place a stance or finds no reason from the text.",
   "kind": "open question",
   "found_by": "Traced the response paths. The claim-evidence-reasoning response never reads the try count. The debate's judged branches, for a stance the judge cannot place or one with no reason from the text, return no verdict and no release. The scripted readers never write a real stance (the strong one replies straight to a push-back), so the playtest does not reach these branches.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "100",
     "quote": "Copy the words exactly from the text, so your quotation can be found."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "118",
     "quote": "Say it once more, plainly: where do you stand, and why?"
    },
    {
     "path": "~/Projects/g9/transformer/src/core/runtime.js",
     "lines": "82",
     "quote": "A tick the judge could not settle is no attempt."
    }
   ],
   "against": "The debate says otherwise of its code path: \"two tries, then the position is given and the task closes (the 3D build's release rule), so no reader is held here\" (debate.js line 129), and \"with no judge the answer is saved, never marked, and the model position closes the task\" (lines 123-124). But any answer that is not thin or bare takes the judged path, with or without a judge.",
   "scope_note": "universal",
   "adds_to_existing": [
    49,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep the try count in one place that every player reads: a two-tries release worked where a page counted its own tries and did not fire in sessions until the runtime passed the count.",
   "kind": "measured",
   "found_by": "Found in integration: the two-tries release did not fire in sessions until the runtime passed each entity's attempt count to the block.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "141",
     "quote": "(the runtime now passes the attempt count); the hunt and debate now release after two tries"
    },
    {
     "path": "~/Projects/g9/transformer/src/core/runtime.js",
     "lines": "59",
     "quote": "works in a session as it does in a page that counts its own"
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "662",
     "quote": "if (res.correct === false) tries++;"
    }
   ],
   "against": "The fix reached sessions. The composer's lesson view still keeps its own count and adds to it only on a wrong answer, so in that view a debate answer that gets no verdict (a thin or bare one) never counts toward its release.",
   "scope_note": "universal: any lesson played by more than one player",
   "adds_to_existing": [
    41,
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Whether a judge can vouch for an answer's facts about a text it is not shown is open: one required check asks just that, and passed at p 0.6 and 0.72.",
   "kind": "open question",
   "found_by": "The comparison block's required honesty check is asked with only the two answers in its state, no text and no question. On the live proof it held at p 0.6 and 0.72, the lowest required check in the block.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "57",
     "quote": "const state = { paragraph_A: item.paragraphs[0], paragraph_B: item.paragraphs[1] };"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "61",
     "quote": "free of factual errors about the text it discusses?"
    },
    {
     "path": "~/Projects/g9/transformer/v01/proof-2026-10-09.json",
     "lines": "259-262",
     "quote": "\"p\": 0.6"
    }
   ],
   "against": "Later saved blocks held the same check at p 0.61 to 0.84 (\"p\": 0.84 in runs/blocks/f603c8d14862db8a.json line 87), and nothing shows the low values come from the missing text. 0.6 is the support gate's floor (top 0.6, grade3-reading/engine/src/decide/questions.js line 5).",
   "scope_note": "universal",
   "adds_to_existing": [
    18,
    19
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Pose an evaluative question as an open one (How far, To what extent, How, Why, What), never one answered yes or no, and check its first word in code.",
   "kind": "adopted rule",
   "found_by": "The debate's prompt and its code check, which lesson questions share. A planted yes-or-no question fails it in the tests.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "46",
     "quote": "It is an open question (How far, To what extent, How, Why or What), never one answered yes or no."
    },
    {
     "path": "~/Projects/g9/transformer/src/question.js",
     "lines": "11",
     "quote": "/^(is|are|does|do|did|can|could|would|will|was|were|has|have|had|should)"
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "124",
     "quote": "question: \"Can we sympathise with Iago?\""
    }
   ],
   "against": "The code check reads only the opening word, against a list of yes-or-no openers (question.js line 11).",
   "scope_note": "universal: evaluative and lesson questions",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "An evaluative question is fair only if each side can be defended from the text with a reason, so check each side on its own.",
   "kind": "adopted rule",
   "found_by": "Two required judge checks in the debate block, one per side. On the saved drama debate both held, at p 0.86 and 0.82.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "45",
     "quote": "a debate on the text that a Grade 9 reader could take either side of, with a"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "82",
     "quote": "Can a Grade 9 reader defend side_${k}, as an answer to question, with a reason from passage?"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/90a1089f3e8d7ad5.json",
     "lines": "80-84",
     "quote": "\"p\": 0.86,"
    }
   ],
   "against": "none found",
   "scope_note": "evaluative questions on a text; the counterpart of a choice question, which needs one answer the text settles",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A hint on an evaluative question gives a way in without taking either side, and code can check that it repeats no side's words.",
   "kind": "adopted rule",
   "found_by": "The debate's prompt, a code check for a run of three words shared with either side's label, and an advisory judge check.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "48",
     "quote": "help: one sentence that gives a way in without taking either side."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "67",
     "quote": "sharedRun(item.help, s.label) >= 3"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "73",
     "quote": "The help takes no side"
    }
   ],
   "against": "On the one judged debate, a help that set out both sides passed the code check, and the advisory judge check that it leaves both sides open was unclear at \"p\": 0.53 (runs/blocks/90a1089f3e8d7ad5.json lines 160-164).",
   "scope_note": "evaluative questions",
   "adds_to_existing": [
    14
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Meet a student's position with one push-back written in advance for that side: an open question that quotes the text against it.",
   "kind": "adopted rule",
   "found_by": "Rules brought over from another build's evaluate task, with each side's push-back written in advance so no writer runs at play time. A test shows a stance on one side gets that side's push-back.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "50",
     "quote": "the strongest push-back to a student who takes this side: ONE open question (How, Why or What), at most"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "4",
     "quote": "one push-back, a bare stance asked why first, a model position at the end)."
    },
    {
     "path": "~/Projects/g9/transformer/test/runtime.test.mjs",
     "lines": "117",
     "quote": "the push-back to side B"
    }
   ],
   "against": "On a poem and a speech, the writer's push-backs failed the quotation part after two tries per block (runs/blocks/f23aebacf033daa2.json line 28; runs/blocks/aeb043df247f1b45.json line 28).",
   "scope_note": "evaluative and debate tasks",
   "adds_to_existing": [
    55
   ],
   "name_bearing_source": false
  },
  {
   "statement": "On an evaluative question, judge only which side a student takes and whether a reason from the text is given, never whether the side is right, so taking no position is the only miss.",
   "kind": "adopted rule",
   "found_by": "The debate's play-time judgment is a choice of side and a yes-or-no on a reason. In the tests, an answer with no position is the one returned as wrong.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "5",
     "quote": "reason is given, never whether the position is right."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "115",
     "quote": "the side choice \"fails\" on a sure pick of a side, \"holds\" on a sure \"no position\"; unclear is no verdict at all"
    },
    {
     "path": "~/Projects/g9/transformer/test/runtime.test.mjs",
     "lines": "122",
     "quote": "assert.equal(none.response.correct, false);"
    }
   ],
   "against": "The block calls itself \"Never marked.\" (debate.js line 37), yet a sure \"no position\" comes back as correct: false (line 117).",
   "scope_note": "evaluative questions",
   "adds_to_existing": [
    22
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a judge reads which side a student takes, let it answer both or neither as well as either side, and meet both with a request to say which weighs more.",
   "kind": "adopted rule",
   "found_by": "The debate's side choice has four options, and a student who takes both sides gets a line asking which reading weighs more.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "103",
     "quote": "C: \"both, or partly each\", D: \"no position on question\""
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "18",
     "quote": "You see both readings. Say which weighs more for you, and quote the words in the text that decide it."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "93",
     "quote": "with one choice (which side, both, or none)"
    }
   ],
   "against": "none found",
   "scope_note": "judging a student's stance on an evaluative question",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Ask a bare stance (three words or fewer, with no reason word) why before challenging it.",
   "kind": "adopted rule",
   "found_by": "A rule brought over from another build's evaluate task: a bare stance is asked why before it is tested, in code, with no judge.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "16",
     "quote": "a stance of three words or fewer with no reason word in it"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "17",
     "quote": "(because|since|as|so|when|but)"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "19",
     "quote": "Why do you think so? Give one reason from the text."
    }
   ],
   "against": "none found",
   "scope_note": "argument and evaluative tasks",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Mark a sentence said back on the words that carry it: every key word must be there, and a near spelling of a long one counts and is named, not missed.",
   "kind": "adopted rule",
   "found_by": "The say-it-back block marks in code with another build's matcher: a word of five letters or more, same first letter, length within two, and at most two edits (three for words past seven letters). A test shows a near spelling named, not missed.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "3",
     "quote": "a near spelling of a long word is named but not counted as a miss"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "28",
     "quote": "lev(x, w) <= (w.length > 7 ? 3 : 2)"
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "91",
     "quote": "Check the spelling of \"pretence\""
    }
   ],
   "against": "none found",
   "scope_note": "saying or typing back key words",
   "adds_to_existing": [
    25
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make every word a student must say back one plain word, letters only, because the transcript it is matched against loses hyphens, apostrophes and accents.",
   "kind": "adopted rule",
   "found_by": "Both builds match key words in a folded transcript of what was said or typed. The prompt asks for plain words, and a code check holds any other.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "11",
     "quote": "letters only: both builds look a key word up in a folded transcript, where a hyphen, apostrophe or accent is lost"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "56",
     "quote": "written exactly as it is in the sentence, letters only."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "77",
     "quote": "Every key word is one word, letters only"
    }
   ],
   "against": "none found",
   "scope_note": "spoken or typed recall matched against a transcript",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Give the lesson's answer as one statement of at most sixteen words that a student can say aloud and keep.",
   "kind": "adopted rule",
   "found_by": "The say-it-back prompt and a code check on the sentence's length. The judge checks that it is true to the text and answers the lesson question.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "10",
     "quote": "const MAX_WORDS = 16;"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "52",
     "quote": "true to the text, answering the question, plain enough to"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "104",
     "quote": "That is the sentence. Keep it: you will need it again."
    }
   ],
   "against": "none found",
   "scope_note": "a lesson's closing say-it-back step",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Close a lesson with demands that rise: say the lesson's answer back, then apply it, then evaluate it.",
   "kind": "adopted rule",
   "found_by": "The close blocks were brought over from another build and are ordered in the palette and the export: say it back first, then the debate.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "1",
     "quote": "Say it back: the first of the Grade 9 close questions (mimicry, then application, then evaluation)."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "1",
     "quote": "Debate: the evaluative close question"
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "18",
     "quote": "at(\"say-it-back\") < at(\"debate\")"
    }
   ],
   "against": "The transformer's own close runs two of the three steps: \"the Grade 9 close: mimicry, then evaluation\" (src/glue/animated.js line 193).",
   "scope_note": "Grade 9 English lesson close",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Teach what makes an answer good by comparison: two answers to the same question, the weaker honest and weaker only in the skill being taught, and the student picks the stronger and says why.",
   "kind": "adopted rule",
   "found_by": "The comparison block's prompt and its required honesty check. Comparative judgement and faded non-examples were among the procedures committed to on 8 October.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "1",
     "quote": "Compare two answers: comparative judgement. Two Grade 9 paragraphs answer the same question; the reader picks the"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "25",
     "quote": "other is weaker but honest: it retells or quotes without explaining. Neither contains a factual error about the text."
    },
    {
     "path": "~/Projects/g9/transformer/v05/README.md",
     "lines": "8",
     "quote": "comparative judgement and faded non-examples (committed to on"
    }
   ],
   "against": "The honesty check is the weakest required check in the block: \"p\": 0.6 on the live drama comparison (v01/proof-2026-10-09.json line 262), the gate's floor. The student's sentence on why \"is saved and never marked\" (compare-paragraphs.js line 15).",
   "scope_note": "comparison tasks on written answers; Grade 9 English",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A strong analytical paragraph answers the question directly, quotes exactly, says what one word in the quotation suggests and links it back to the claim, while retelling or repeating the quotation is the weaker answer.",
   "kind": "adopted rule",
   "found_by": "Taken from the comparison block's stronger and weaker answers, the claim-evidence-reasoning block's ordered next steps (claim, word, link back), and that block's seed cases.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "24",
     "quote": "One is clearly stronger: a precise claim, a short exact quotation, and reasoning about a specific word."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "78",
     "quote": "reasoning explains a word from evidence but does not link it back to claim"
    },
    {
     "path": "~/Projects/g9/transformer/test/calibration/cer-frame.next-step.json",
     "lines": "13",
     "quote": "The reasoning repeats the quotation and explains no word in it."
    }
   ],
   "against": "The calibration has seed cases only (\"Seed cases only: obvious ones\", test/calibration/cer-frame.next-step.json line 5), run only against a label oracle.",
   "scope_note": "Grade 9 English literary analysis",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Before students write, model the answer: unpick one short quotation, then write the paragraph one move per sentence, each with a first-person note on why it is there.",
   "kind": "adopted rule",
   "found_by": "The worked model block, brought over from another build's model step. It unpicks one quotation (its moment, its plain meaning, two or three of its words), then writes a paragraph of four or five moves with a think-aloud beside each. It is placed before the claim-evidence-reasoning block.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "226",
     "quote": "Watch how I answer today's learning question: I find a quotation, unpick its words, then write my answer one move at a time."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "36",
     "quote": "the guide shows how to answer the lesson question before the student writes, as a strong Grade 9"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "46",
     "quote": "one sentence in the first person on why I write it"
    }
   ],
   "against": "The check that each think-aloud says what its sentence does is advisory (required: false, worked-model.js line 107).",
   "scope_note": "Grade 9 English analytical writing",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Ask how a line should be spoken only where it can be spoken in clearly different ways and the lines around it show what the speaker wants, and take the right delivery from that want.",
   "kind": "adopted rule",
   "found_by": "The delivery block's idea and prompt. On the live proof the judge found the lines allowed different deliveries at p 0.92 and 0.94, and picked the writer's delivery at p 1 and 0.98.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
     "lines": "1",
     "quote": "Direct the line: Shakespeare is meant to be performed and heard."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
     "lines": "24",
     "quote": "delivery fits best. Offer three deliveries; exactly one fits what the speaker wants at this moment."
    },
    {
     "path": "~/Projects/g9/transformer/v01/proof-2026-10-09.json",
     "lines": "203-206",
     "quote": "\"p\": 0.92"
    }
   ],
   "against": "The check that the line allows different deliveries is advisory (required: false, direct-the-line.js line 60). In all 4 saved delivery items the right delivery sat second of three.",
   "scope_note": "drama and other texts meant to be spoken",
   "adds_to_existing": [],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/helpers.mjs",
   "lines": "13",
   "quote": "Says yes to every check except give-aways; picks paragraph A and delivery A; scores knowledge 4 of 5."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/engine/src/decide/questions.js",
   "lines": "118",
   "quote": "Deterministic option-order rotation per sample (option order shifts answers; rotate and average)."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
   "lines": "113",
   "quote": "words aimed at whoever marks them are not an answer: no verdict, and no try (the Grade 3 engine's rule)"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
   "lines": "84",
   "quote": "the animated build asks the rebuild under the first word's card (\"did you follow what I just said?\")"
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
   "lines": "39",
   "quote": "context: one sentence on the moment it comes from (who says it, to whom, just after what), without quoting it."
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
   "lines": "29",
   "quote": "wrong ones send the reader back to the surrounding lines without naming the best"
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
   "lines": "29",
   "quote": "pointing at what to compare without saying which is better"
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
   "lines": "93",
   "quote": "a miss does not give the words"
  },
  {
   "truth": 19,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "139",
   "quote": "its give-away question was answered from general knowledge of Othello"
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
   "lines": "1",
   "quote": "The reader's words are saved and shown back, never marked."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/README.md",
   "lines": "120",
   "quote": "No lesson has been reviewed by a person or used by a student."
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/calibration/cer-frame.next-step.json",
   "lines": "11",
   "quote": "The same paragraph misspelt: spelling is not one of the changes the check chooses between."
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
   "lines": "3",
   "quote": "A student performs the line, so it is never one with a slur in it"
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
   "lines": "118",
   "quote": "the quotation unpicked and the sentence to rebuild, without its answers; the paragraph comes after the rebuild"
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "63-64",
   "quote": "direct the line showed what the speaker wants before the pick"
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
   "lines": "89",
   "quote": "a closing line keeps no question of its own (the 3D build's rule), only quoted ones"
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
   "lines": "1",
   "quote": "the guide's \"I do\", before the student writes."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/calibration/2026-10-09T12-25-25-449Z.json",
   "lines": "6",
   "quote": "answers from the labels themselves: proves the wiring, measures nothing"
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
   "lines": "6",
   "quote": "Labels need a person: a model-made label measures nothing, and a seed set this small is diagnostic only."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/blocks/ed2f90f660c18774.json",
   "lines": "27",
   "quote": "Not about what an earlier Compare two answers block was: already in this lesson:"
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
   "lines": "16",
   "quote": "what this block is about, so a second block of the same kind on the same text is told to differ"
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
   "lines": "4",
   "quote": "Two tries, then the sentence is given."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
   "lines": "112",
   "quote": "a word class is a judgment call on Shakespeare, so it never holds the block, but one Jev did not confirm is not shown"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
   "lines": "115",
   "quote": "unclear is no verdict at all"
  },
  {
   "truth": 54,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
   "lines": "55",
   "quote": "the words that carry the answer"
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
   "lines": "3",
   "quote": "so no writer runs at play time"
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/DECISIONS.md",
   "lines": "29",
   "quote": "the 3D build's paragraph coach (6.6 s through a second model) became a Jev choice of one next step"
  }
 ]
}
```
