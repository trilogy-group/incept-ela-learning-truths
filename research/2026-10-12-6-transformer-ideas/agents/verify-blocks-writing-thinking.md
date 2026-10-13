# verify:blocks-writing-thinking

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  nono, analyse its ideas and fold them into the research results

## Result

```json
{
 "direction": "blocks-writing-thinking",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (compare-paragraphs.js 2, direct-the-line.js 2). The judge's state holds the two answers, or the line and the lines near it, and no key (compare-paragraphs.js 57, direct-the-line.js 55-57). The choice block, by contrast, hands its judge keyed_answer (quick-check.js 63). A required check holds only when the support gates pass and the pick is the key (judge.js 20). The proof values 0.96 and 0.99 (comparisons) and 1 and 0.98 (deliveries) match. It refines 11 and 31 with a method and is not a duplicate. The statement is unchanged. The proof quote \"p\": 1 is under the quote checker's six-character minimum, so it is lengthened to the whole check.",
   "statement": "Where an item's key is a judgment call, have the judge answer the item itself without the key, and keep the item only if it picks the key with a clear margin.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "2",
     "quote": "The judge must choose the same paragraph with a clear margin, so there is one defensible pick.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
     "lines": "2",
     "quote": "The judge, reading the same lines around it, must pick the same delivery.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/judge.js",
     "lines": "20",
     "quote": "const verdict = !a.pass ? \"unclear\" : ok ? \"holds\" : \"fails\";",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v01/proof-2026-10-09.json",
     "lines": "197-200",
     "quote": "\"id\": \"one-delivery\", \"required\": true, \"verdict\": \"holds\", \"p\": 1",
     "verbatim": true
    }
   ],
   "against": "The margin is the engine's support gates (confidence 0.55, top 0.6, margin 0.15), which it calls \"conservative engineering thresholds, not calibrated correctness\" (grade3-reading/engine/src/decide/questions.js 105). The proof ran one sample per question (proof line 14), so the engine's per-sample option rotation never ran. The writer also put the best delivery second in all 4 saved items, so a judge with a position bias could agree for the wrong reason. The offline stand-in judge picks A and both fixtures key A (test/helpers.mjs 13), so these checks cannot fail offline. A clear margin does not test whether a wrong option would tempt anyone. Only the choice block asks that, and only as an advisory check.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep",
   "reason": "Quotes verbatim (worked-model.js 50 and 106; be97f27fc4c4a65a.json 120). The judge's state carries every wrong option already set into the rebuilt sentence (worked-model.js 97). In that block the option \"long remember\", taken from the quotation itself, came back as a fail at p 0.31 (no at 0.69, gates passed). The block was saved as failed after 2 tries (line 426). It refines 31 with the in-place method, so it stays as its own rule.",
   "statement": "Check each wrong option of a fill-in-the-blank in place: put it into the sentence and ask whether the whole sentence is then wrong about the text.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "50",
     "quote": "the other two are wrong about the text or the word.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "97",
     "quote": "rebuilt(item, x.k, x.o)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "106",
     "quote": "Is sentence_${x.k}_${x.j} wrong about quote or about passage?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/be97f27fc4c4a65a.json",
     "lines": "120",
     "quote": "makes the rebuilt sentence wrong: the judge found this does not hold",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/be97f27fc4c4a65a.json",
     "lines": "333-334",
     "quote": "\"verdict\": \"fails\", \"p\": 0.31",
     "verbatim": true
    }
   ],
   "against": "There was one sample per judge question (v01/QA.md 45), so each wrong option was judged once. The judge's call looks right, since the line says the world will not long remember, but nobody has checked it.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "I confirmed the counts across runs/blocks. The delivery key was index 1 in all 4 items: two on the same line of the play, one on a speech and one on a poem. The rebuild's right option was index 0 in 5 of 6 blanks. The comparisons keyed A in 6 and B in 4 of 10. Nothing in src/ or web/ shuffles options or checks the key's position, and both views pass the options in the writer's order. The delivery prompt's own example shape even says \"best\": 0. The rule is already 45, and this adds measured evidence for it. But \"Left to itself, a writer puts the right answer in a predictable place\" overstates it, because the comparisons came out near even. The statement is restated to what was counted.",
   "statement": "Don't leave the right answer's position to the writer: in the saved blocks the best delivery was second of three in all 4 delivery items and the right option came first in 5 of 6 rebuild blanks, and nothing reorders the options before the student sees them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/4c5df03f78a26e6e.json",
     "lines": "22",
     "quote": "\"best\": 1,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/8d4652dbccf037b9.json",
     "lines": "23",
     "quote": "\"best\": 1,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/e47511c58b5dd64c.json",
     "lines": "23",
     "quote": "\"best\": 1,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/eb9231d930fa07c4.json",
     "lines": "23",
     "quote": "\"best\": 1,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
     "lines": "68",
     "quote": "context: before, deliveries: item.deliveries",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "120",
     "quote": "rebuild: item.rebuild.parts.map((p) => (p.options ? { options: p.options } : { text: p.text }))",
     "verbatim": true
    }
   ],
   "against": "The samples are small: 4 delivery items, two of them on the same line, and 6 blanks from 3 items. The comparison keys were near even (6 A, 4 B of 10).",
   "general": true,
   "duplicate_of": "45",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep",
   "reason": "Quotes verbatim (compare-paragraphs.js 51 and 23; quick-check.js 55). The comparison check, labelled \"Length does not give the stronger one away\", holds a draft when the longer paragraph is over 1.6 times the shorter in words. The choice block's rule is 2.2 times, in characters. Not on record.",
   "statement": "Keep surface features from giving the answer away: two answers to compare stay close in length, the longer at most 1.6 times the shorter.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "51",
     "quote": "Math.max(...wc) <= 1.6 * Math.min(...wc)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "23",
     "quote": "write two short paragraphs (50 to 90 words each)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "55",
     "quote": "No option stands out by length",
     "verbatim": true
    }
   ],
   "against": "No measure shows that length gave an answer away here. Both limits (1.6 and 2.2) are set, not calibrated, and the two blocks measure length differently (words in one, characters in the other).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep",
   "reason": "Quotes verbatim (cer-frame.js 51, worked-model.js 83, mechanics.test.mjs 118). In the test, a planted fault (the rebuild pointed at step 3) fails rebuild-makes-sentence. transform.js runs the code checks first and sends a failing draft back without asking the judge (lines 65-68). This is narrower than 11, not a duplicate.",
   "statement": "Where the parts of a generated item must point at each other, check the links in code before any judge: the word explained is in the quotation, the reasoning names it, and the rebuilt sentence is the model's sentence.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "51",
     "quote": "the reasoning never mentions the word it explains",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "83",
     "quote": "The rebuild, set right, makes its sentence",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "118",
     "quote": "find((c) => c.id === \"rebuild-makes-sentence\").ok, false",
     "verbatim": true
    }
   ],
   "against": "Code can only test that one part names another. \"Each word's line is about its word\" is checked as has(w.line, w.word) (worked-model.js 79), and what the line actually says is left to the judge.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep",
   "reason": "Quotes verbatim (threejs.js 53 and 54; worked-model.js 75). The worked model and the house checks call exactIn, which runs the other build's quotedLines over one block per speech (threejs.js 34-42). It refines 13 by saying what \"exact\" means, so it is kept as a refinement.",
   "statement": "Count a quotation as exact when it is the text's words in order, punctuation, case and apostrophes aside, and never when it runs across a stage direction or from one speech into the next.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs.js",
     "lines": "53",
     "quote": "Is this quotation the text's exact words? Its quotedLines: punctuation, case and apostrophes aside, never across a",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs.js",
     "lines": "54",
     "quote": "stage direction or two speeches.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "75",
     "quote": "the quote is not an exact quotation from the text (within one speech)",
     "verbatim": true
    }
   ],
   "against": "This holds only while the other build's mirror is on the machine. Without it, exactIn falls back to findQuote, which \"may span consecutive lines\" (text.js 52) and has no speech or stage-direction boundary. The claim-evidence-reasoning block always uses findQuote, for both the model and the student. No test here plants a quotation that runs across two speeches.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep",
   "reason": "Confirmed on f23aebacf033daa2 (poem) and aeb043df247f1b45 (speech), both made on 12 October. Each was saved as failed after 2 tries, with counters-quote as the only failing code check and no judge call. Their push-backs carry the texts' exact words (\"sneer of cold command\"; \"little note, nor long remember what we say here\", which the speech's worked model quoted and passed as exact) with no quotation marks, though the prompt asks for words \"in double quotes\" (debate.js 51). The drama debate (90a1089f3e8d7ad5) did mark its quotations. Adds to 13. The sample's path names a poem, not a person.",
   "statement": "A writer told to quote the text inside a question may weave the text's words in without quotation marks: two sets of push-backs, on a poem and a speech, were held for it after two tries each.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/f23aebacf033daa2.json",
     "lines": "13",
     "quote": "How do the details of a wrinkled lip and sneer of cold command suggest a ruler who also possessed great passion?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/samples/ozymandias.md",
     "lines": "6",
     "quote": "And wrinkled lip, and sneer of cold command,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/f23aebacf033daa2.json",
     "lines": "28",
     "quote": "Each push-back quotes the text: a push-back quotes no words from the text",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/aeb043df247f1b45.json",
     "lines": "17",
     "quote": "How can speech matter if the world will little note, nor long remember what we say here?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/be97f27fc4c4a65a.json",
     "lines": "8",
     "quote": "The world will little note, nor long remember what we say here, but it can never forget what they did here.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "51",
     "quote": "24 words, that quotes a few exact words from the text in double quotes",
     "verbatim": true
    }
   ],
   "against": "Only two blocks. On drama, the writer did mark its quotations (runs/blocks/90a1089f3e8d7ad5.json 13). The check finds quotations only by their marks.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep-with-fix",
   "reason": "Confirmed in v01/QA.md 38-40: the poem's comparison was held once for quoting the single word \"boundless\". The check now accepts a single word found in the text, with a test (text.test.mjs 28 and 31, and findQuote's one-word branch, text.js 57). The cited calibrate.js line is about judged checks, not code checks, so it is replaced by the test. Complements 1 (a check must also let fair work through). Not on record. Statement unchanged.",
   "statement": "A code check can hold good work, so test it on fair cases too: an exact-quotation check held a fair one-word quotation until it accepted single words found in the text.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "38",
     "quote": "Ozymandias's comparison was held once: one paragraph quoted the single word",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "39",
     "quote": "and the exact-quotation check only accepted quotations of two or more words.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/text.test.mjs",
     "lines": "28",
     "quote": "assert.deepEqual(findQuote(t, \"ancient,\"), [31]);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/text.js",
     "lines": "57",
     "quote": "if (!q.includes(\" \")) { const u = ls.find((x) => norm(x.text).split(\" \").includes(q));",
     "verbatim": true
    }
   ],
   "against": "This is one incident. Nothing here measures how often code checks hold good work.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep",
   "reason": "Verbatim in transform.js 78-79 and v02/QA.md 191. A fail is told \"the judge found this does not hold\". An unclear verdict asks for a version that plainly holds, or another choice. This follows from 50 but is its own rule for the write, check and correct loop.",
   "statement": "When a draft is held because the judge could not confirm a point, ask the writer for a version that plainly holds or for another choice, not for the opposite.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "78",
     "quote": "an unsure judge is not a no: the correction asks for a version that plainly holds, not for its opposite",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "79",
     "quote": "the judge could not confirm this; rewrite it so that it plainly holds, or choose another",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "191",
     "quote": "it now asks for a version that plainly holds; before, it only said \"unclear\".",
     "verbatim": true
    }
   ],
   "against": "Nothing measures whether the new wording makes corrected drafts pass more often.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep",
   "reason": "Verified. cer-frame's respond refuses thin or noise boxes and any quotation findQuote cannot find, and judgeAction runs only on a saved answer (cer-frame.js 72-73). The calibration set records that such answers never reach the judge (cer-frame.next-step.json 5), and v02/QA.md 61 records the live play. The debate does the same in code for thin and bare answers (debate.js 98). Not on record.",
   "statement": "Settle in code what code can settle about a student's words before any judge sees them: refuse noise and answers too thin to be one, and send back a quotation that is not the text's exact words without giving the wording.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "2",
     "quote": "Code checks only what is fact: each box has real words, and the evidence is an exact quotation from the text.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "100",
     "quote": "Copy the words exactly from the text, so your quotation can be found.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "61",
     "quote": "CER-1 refused \"asdf qwer zxcv\", sent \"I follow him because I love him\" back as",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/calibration/cer-frame.next-step.json",
     "lines": "5",
     "quote": "nonsense, a box too thin and a quotation that is not the text's exact words are stopped by code first (cer-frame respond)",
     "verbatim": true
    }
   ],
   "against": "These gates have no try limit. cer-frame's respond never reads the try count (lines 94-102), so a reader who cannot quote exactly is asked again with no end. The student's quotation is matched with the looser finder, which can span up to four lines and has no speech boundary.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep",
   "reason": "Verbatim in debate.js 93 and 101 and cer-frame.js 74. The student's words sit in state fields (student_text in one block; claim, evidence and reasoning in the other), and the questions name those fields. The choice options are the writer's labels, never the student's text. Not on record.",
   "statement": "Put a student's words in a field of their own in the judge's state and ask about that field by name, never inside the question's wording.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "93",
     "quote": "the student's position goes to Jev in its own field",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "101",
     "quote": "Does student_text answer challenge with a reason from the text?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "74",
     "quote": "claim: String(action.claim), evidence: String(action.evidence), reasoning: String(action.reasoning)",
     "verbatim": true
    }
   ],
   "against": "No test compares this with putting the words inside the question, so the benefit is not measured.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep",
   "reason": "Verbatim in util.js 135 and cer-frame.addresses-grader.json 5 and 11. The guard's question says that quoted or retold commands do not count. The seed set keeps a paragraph quoting a character's commands, and a vague one, as answers that must pass. Refines 6.",
   "statement": "A guard against answers aimed at the marker must count quoted or retold commands from the text, and weak but real attempts, as answers, and its test cases should keep both as controls.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "135",
     "quote": "Words quoted or retold from the text, a character's commands among them, are part of an answer and do not count.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/calibration/cer-frame.addresses-grader.json",
     "lines": "5",
     "quote": "Drama invites false alarms: a paragraph that quotes a character's commands is an answer, and is kept here as a control.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/calibration/cer-frame.addresses-grader.json",
     "lines": "11",
     "quote": "Weak, but an attempt at the prompt: vague is not addressing the grader.",
     "verbatim": true
    }
   ],
   "against": "It has only been scored against a label oracle that \"proves the wiring, measures nothing\" (runs/calibration/2026-10-09T12-25-25-449Z.json 6), on five seed cases. The guard also acts only on a sure yes (test/glue.test.mjs 31).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep",
   "reason": "Verbatim in cer-frame.js 67 and v02/QA.md 99 and 102. The choice has three authored steps plus \"none of these\" (cer-frame.js 75-80). resolve shows a step only on a sure pick other than none, and shows none when the words are aimed at the marker (lines 85-87). Live times were 0.34, 0.48 and 0.26 s, against 6.6 s through a second model before. It overlaps 22 and 55 but adds the limit of one step, the most useful one, and none when nothing needs changing.",
   "statement": "Give student writing at most one next step: the change that would most improve it, picked from steps written in advance, shown only when the judge is sure, and none when nothing needs changing.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "67",
     "quote": "one Jev choice, asked only of a saved answer: which one change would most improve the paragraph.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "99",
     "quote": "It is now a Jev choice among four authored steps, filled with the student's own words,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "102",
     "quote": "a paragraph doing all three got no step (0.26 s).",
     "verbatim": true
    }
   ],
   "against": "It has only been calibrated against a label oracle that \"proves the wiring, measures nothing\" (runs/calibration/2026-10-09T12-25-25-449Z.json 6), on five seed cases. No person has judged whether the steps help.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "keep-with-fix",
   "reason": "cer-frame.js 101 and debate.js 27 are verbatim. The worked-model line cited is about a choice task (the rebuild), and the worked model is shown before the student writes, so it does not bear on an open task. It is replaced by cer-frame.js 15. Overlaps 22 and 29. What is new is showing the model as one possible answer rather than the answer.",
   "statement": "After an open task, show a model as one strong answer or one position the student could defend, never as the answer, and only once the student's own answer is saved.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "101",
     "quote": "Saved. Here is one strong answer to compare with yours.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "27",
     "quote": "Here is one position you could defend:",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "15",
     "quote": "The quote is checked against the text; then a model answer is shown.",
     "verbatim": true
    }
   ],
   "against": "The debate also shows its model position when it releases a reader after two thin or bare tries, when none of their own answer is in (debate.js 130).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep",
   "reason": "Quotes verbatim. Four blocks' writer prompts pitch at a strong Grade 9 student (cer-frame.js 23-24, compare-paragraphs.js 23-24, debate.js 52, worked-model.js 36-37). The judge checks in two of them are advisory (cer-frame.js 61, compare-paragraphs.js 62). The proof values 0.84 and 0.86 match. Not on record.",
   "statement": "Pitch a model answer at what a strong student of the grade could write in the time, not at expert writing.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "61",
     "quote": "Is this model answer something a strong Grade 9 student could write in about five minutes?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "62",
     "quote": "Do both paragraphs read like writing by Grade 9 students",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "52",
     "quote": "a position a strong Grade 9 student could defend, with a reason from the text.",
     "verbatim": true
    }
   ],
   "against": "Both checks are advisory and never hold a block. The drama comparison's student-voice check came back unclear at \"p\": 0.59 and the block shipped (v01/proof-2026-10-09.json 265-268). Nobody has measured whether students find the pitch right.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep",
   "reason": "compare-paragraphs.js 39 is verbatim. The screen labels the answers \"Answer A\" and \"Answer B\" (web/lesson.js 461, src/glue/animated.js 131). A block saved on 9 October, before the rename, still says \"Paragraph a\" (ed2f90f660c18774.json 13). The film stops forbid production words in code (util.js 111-118). This generalises 53, which covers line numbers only.",
   "statement": "Feedback names what the student sees by the labels on their screen, never by the item's own workings.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "39",
     "quote": "the reader sees \"Answer A\" and \"Answer B\", so the feedback names them that way (\"paragraph b\" -> \"Answer B\")",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/ed2f90f660c18774.json",
     "lines": "13",
     "quote": "Paragraph a is stronger because it makes a precise claim",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "111",
     "quote": "What a viewer reads at a film's stops (the questions, options and feedback) speaks of the film, never of how it is",
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
   "verdict": "keep",
   "reason": "Verbatim in say-it-back.js 79, 34 and 56. The check matches the word itself or, for words of six letters or more, any word that begins with the word minus its last two letters. Not on record.",
   "statement": "A note that defines a word must not use that word or its stem.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "79",
     "quote": "No note uses its own word",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "34",
     "quote": "x.startsWith(norm(w).slice(0, -2))",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "56",
     "quote": "note: its plain meaning here, at most 10 words, without",
     "verbatim": true
    }
   ],
   "against": "The stem is the word minus two letters, so a shorter root gets through (\"deceit\" in a note for \"deceitful\"). No saved block shows the check firing.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 17,
   "verdict": "keep-with-fix",
   "reason": "Traced and confirmed. cer-frame's respond never reads the try count. The debate's resolve gives no verdict and no release when the side is unclear or the reason fails (debate.js 118-119). The runtime and blocks.playItem take the judged path even with no judge, and then every check is unclear (runtime.js 31, judge.js 25). So with no judge, or with a judge that is down, a real stance always gets \"Say it once more, plainly\". That last case is added to the statement. Extends 49 and 50. Not covered by 30, which is about stalls.",
   "statement": "What ends a step whose answers get no verdict is open: one block asks a reader who cannot quote exactly to try again with no limit, and another does the same when the judge cannot place a stance, finds no reason from the text, or does not answer at all.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "100",
     "quote": "Copy the words exactly from the text, so your quotation can be found.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "118",
     "quote": "Say it once more, plainly: where do you stand, and why?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/core/runtime.js",
     "lines": "31",
     "quote": "if (!judge) return { results: Object.fromEntries(proposals.map((p) => [p.pid, unjudged(p.checks)])), decision: null };",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/judge.js",
     "lines": "25",
     "quote": "verdict: \"unclear\", reason, band: \"escalate\"",
     "verbatim": true
    }
   ],
   "against": "debate.js says the opposite: \"so no reader is held here\" (line 129), and with no judge \"the model position closes the task\" (lines 123-124). Both hold only on the code path, for thin or bare answers. No saved playtest includes the debate, and the scripted readers move to a reply after one answer, so no run has stayed in these branches.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep-with-fix",
   "reason": "Verified in v02/QA.md 140-141 and runtime.js 58-60: a session now passes the entity's attempt count when the action carries none. But the lesson page still sends its own count (web/lesson.js 659) and adds to it only on a wrong answer (662). The runtime counts every tick the judge did not leave unsure (runtime.js 83). A thin or bare debate answer gets no verdict, so on the page the release at debate.js 130 never fires. That backs the rule, and the statement now says what was seen. Adds to 41 and 49.",
   "statement": "Count tries in one place that every player reads: a two-tries release did not fire in sessions until the runtime passed each block's attempt count, and the lesson page, which counts only wrong answers, still never releases a debate answer too thin or bare to judge.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "141",
     "quote": "(the runtime now passes the attempt count); the hunt and debate now release after two tries",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/core/runtime.js",
     "lines": "59",
     "quote": "works in a session as it does in a page that counts its own",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/core/runtime.js",
     "lines": "83",
     "quote": "if (!unsure.length || response.correct != null) es.attempts++;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "662",
     "quote": "if (res.correct === false) tries++;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "130",
     "quote": "bare(text))) && tries(action) >= 2)",
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
   "reason": "Verified. The honesty check's state holds only paragraph_A and paragraph_B (compare-paragraphs.js 57), yet it asks about \"factual errors about the text\" (line 61). It was the lowest required check in every judged comparison: 0.6 and 0.72 in the proof, and 0.61, 0.66, 0.77 and 0.84 in the saved blocks. This is a case of 19 (a marker given less than the rule refers to), so it is kept as evidence for 19 and restated as what was seen, not as an open question.",
   "statement": "One required check asks a judge about an answer's facts on a text it is not shown: the comparison block's honesty check sees only the two answers, and was the lowest required check in all six judged comparisons, at p 0.6 to 0.84.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "57",
     "quote": "const state = { paragraph_A: item.paragraphs[0], paragraph_B: item.paragraphs[1] };",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "61",
     "quote": "free of factual errors about the text it discusses?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v01/proof-2026-10-09.json",
     "lines": "259-262",
     "quote": "\"id\": \"weaker-honest\", \"required\": true, \"verdict\": \"holds\", \"p\": 0.6",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/f603c8d14862db8a.json",
     "lines": "83-87",
     "quote": "\"id\": \"weaker-honest\", \"label\": \"The weaker paragraph has no factual error\", \"required\": true, \"verdict\": \"holds\", \"p\": 0.84",
     "verbatim": true
    }
   ],
   "against": "Nothing shows that the low values come from the missing text. The stronger pick in the same blocks also had no text and held at 0.9 to 0.99, and 0.6 is just the support gate's floor (grade3-reading/engine/src/decide/questions.js 5).",
   "general": true,
   "duplicate_of": "19",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep",
   "reason": "Verbatim in debate.js 46, question.js 11 and mechanics.test.mjs 124. wellFormed rejects a question that opens with a yes-or-no word, and the planted \"Can we sympathise with Iago?\" fails question-open. The same check screens suggested lesson questions (question.js 30). Not on record.",
   "statement": "Pose an evaluative question as an open one (How far, To what extent, How, Why, What), never one answered yes or no, and check its first word in code.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "46",
     "quote": "It is an open question (How far, To what extent, How, Why or What), never one answered yes or no.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/question.js",
     "lines": "11",
     "quote": "/^(is|are|does|do|did|can|could|would|will|was|were|has|have|had|should)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "124",
     "quote": "question: \"Can we sympathise with Iago?\"",
     "verbatim": true
    }
   ],
   "against": "The check reads only the opening word, against a fixed list. It does not require one of the open openers, so a yes-or-no question that opens another way passes.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "keep",
   "reason": "Verbatim in debate.js 45 and 82: there are two required checks, one per side. On the drama debate both held, at 0.86 and 0.82 (90a1089f3e8d7ad5.json 84 and 116). Not on record. It is the counterpart of 31 for questions that have no single answer.",
   "statement": "An evaluative question is fair only if each side can be defended from the text with a reason, so check each side on its own.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "45",
     "quote": "a debate on the text that a Grade 9 reader could take either side of, with a",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "82",
     "quote": "Can a Grade 9 reader defend side_${k}, as an answer to question, with a reason from passage?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/90a1089f3e8d7ad5.json",
     "lines": "80-84",
     "quote": "\"p\": 0.86,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/90a1089f3e8d7ad5.json",
     "lines": "115-116",
     "quote": "\"verdict\": \"holds\", \"p\": 0.82",
     "verbatim": true
    }
   ],
   "against": "Only one debate has been judged. The other two saved debates were held by code before the judge ran, so this check has never failed.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep-with-fix",
   "reason": "debate.js 48, 67 and 73 are verbatim. But the code check holds a help only when it shares a run of three or more words with a side's label, so \"repeats no side's words\" overstates it. Whether the help leaves both sides open is an advisory judge question (debate.js 86), which came back unclear at 0.53 on the one judged debate. Restated.",
   "statement": "A hint on an evaluative question gives a way in without taking either side: code can hold one that repeats three words in a row from a side, and whether it leaves both sides open is a judgment.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "48",
     "quote": "help: one sentence that gives a way in without taking either side.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "67",
     "quote": "sharedRun(item.help, s.label) >= 3",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "86",
     "quote": "Does help give a way into question without taking either side?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/90a1089f3e8d7ad5.json",
     "lines": "160-164",
     "quote": "\"id\": \"help-open\", \"label\": \"The help leaves both sides open\", \"required\": false, \"verdict\": \"unclear\", \"p\": 0.53",
     "verbatim": true
    }
   ],
   "against": "The judge's check is advisory, and its one reading was unclear (0.53), on a help that set out both readings.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "keep",
   "reason": "Verbatim in debate.js 50 and 4 and runtime.test.mjs 117. Each side's push-back is written and checked when the block is made. A stance the judge places on side B gets side B's push-back. Adds to 55.",
   "statement": "Meet a student's position with one push-back written in advance for that side: an open question that quotes the text against it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "50",
     "quote": "the strongest push-back to a student who takes this side: ONE open question (How, Why or What), at most",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "4",
     "quote": "one push-back, a bare stance asked why first, a model position at the end).",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/runtime.test.mjs",
     "lines": "117",
     "quote": "the push-back to side B",
     "verbatim": true
    }
   ],
   "against": "On a poem and a speech, the writer's push-backs failed the quotation part after two tries per block (runs/blocks/f23aebacf033daa2.json 28; runs/blocks/aeb043df247f1b45.json 28).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep",
   "reason": "Verbatim in debate.js 5 and 115 and runtime.test.mjs 122. resolve returns correct: false only on a sure \"no position\" (debate.js 117), and every other branch returns no verdict. Adds to 22.",
   "statement": "On an evaluative question, judge only which side a student takes and whether a reason from the text is given, never whether the side is right, so taking no position is the only miss.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "5",
     "quote": "reason is given, never whether the position is right.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "115",
     "quote": "the side choice \"fails\" on a sure pick of a side, \"holds\" on a sure \"no position\"; unclear is no verdict at all",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/runtime.test.mjs",
     "lines": "122",
     "quote": "assert.equal(none.response.correct, false);",
     "verbatim": true
    }
   ],
   "against": "The block calls itself \"Never marked.\" (debate.js 37), yet a sure \"no position\" comes back as correct: false (line 117).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 25,
   "verdict": "keep",
   "reason": "Verbatim in debate.js 103, 18 and 93. A pick of option C gets the \"both\" line through challengeFor (line 24). Not on record.",
   "statement": "When a judge reads which side a student takes, let it answer both or neither as well as either side, and meet both with a request to say which weighs more.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "103",
     "quote": "C: \"both, or partly each\", D: \"no position on question\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "18",
     "quote": "You see both readings. Say which weighs more for you, and quote the words in the text that decide it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "93",
     "quote": "with one choice (which side, both, or none)",
     "verbatim": true
    }
   ],
   "against": "No test or saved play covers the both branch.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "keep",
   "reason": "Verbatim in debate.js 16, 17 and 19. A stance of three words or fewer with no reason word is asked why in code, before any judge (judgeAction returns null for it, line 98). The rule was brought over from another build's closing rules. Not on record.",
   "statement": "Ask a bare stance (three words or fewer, with no reason word) why before challenging it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "16",
     "quote": "a stance of three words or fewer with no reason word in it",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "17",
     "quote": "(because|since|as|so|when|but)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "19",
     "quote": "Why do you think so? Give one reason from the text.",
     "verbatim": true
    }
   ],
   "against": "No unit test covers the branch, and no saved playtest includes the debate.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep",
   "reason": "Verbatim in say-it-back.js 3 and 28 and mechanics.test.mjs 91. The thresholds are as stated: five letters or more, the same first letter, length within two, and two edits (three for words past seven letters). It is a scoped case where wording is marked, distinct from 25.",
   "statement": "Mark a sentence said back on the words that carry it: every key word must be there, and a near spelling of a long one counts and is named, not missed.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "3",
     "quote": "a near spelling of a long word is named but not counted as a miss",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "28",
     "quote": "lev(x, w) <= (w.length > 7 ? 3 : 2)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "91",
     "quote": "Check the spelling of \"pretence\"",
     "verbatim": true
    }
   ],
   "against": "The tolerance can accept a different word for a key word. \"presence\" is one edit from \"pretence\" and would count, with only a note to check the spelling.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep-with-fix",
   "reason": "say-it-back.js 11, 56 and 77 are verbatim. hasTerm folds both the answer and the key word, turning anything but a to z into a space, and looks the key word up among the answer's space-split words (say-it-back.js 15, 24, 26). So a hyphen or apostrophe splits the key word in two and it never matches. Accents are stripped on both sides, so an accented word would still match. That part of the claim rests only on the comment, so it is dropped.",
   "statement": "Make every word a student must say back one plain word, letters only: the matcher folds both the answer and the key word and splits on spaces, so a hyphen or apostrophe breaks the word in two and it never matches.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "11",
     "quote": "letters only: both builds look a key word up in a folded transcript, where a hyphen, apostrophe or accent is lost",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "15",
     "quote": ".replace(/[^a-z ]/g, \" \")",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "26",
     "quote": "if (forms.some((f) => words.includes(f.trim()))) return \"yes\";",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "77",
     "quote": "Every key word is one word, letters only",
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
   "reason": "Verbatim in say-it-back.js 10, 52 and 104. A code check holds a sentence over 16 words (line 74), and the judge checks that it is true to the text and answers the question (lines 86-87). Not on record.",
   "statement": "Give the lesson's answer as one statement of at most sixteen words that a student can say aloud and keep.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "10",
     "quote": "const MAX_WORDS = 16;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "52",
     "quote": "true to the text, answering the question, plain enough to",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "104",
     "quote": "That is the sentence. Keep it: you will need it again.",
     "verbatim": true
    }
   ],
   "against": "Sixteen is a set limit, not a measured one.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 30,
   "verdict": "keep-with-fix",
   "reason": "say-it-back.js 1, debate.js 1 and mechanics.test.mjs 18 are verbatim. But the transformer has no application step: its close runs say it back, then the debate (\"the Grade 9 close: mimicry, then evaluation\", src/glue/animated.js 193). \"Then apply it\" describes the design it borrows, not what it does, so the statement is restated. Adds to 34.",
   "statement": "Close a lesson with demands that rise: the lesson's answer said back first, then an evaluative question on it; the design this follows puts an application step between the two.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "1",
     "quote": "Say it back: the first of the Grade 9 close questions (mimicry, then application, then evaluation).",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "193",
     "quote": "the Grade 9 close: mimicry, then evaluation",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "18",
     "quote": "at(\"say-it-back\") < at(\"debate\")",
     "verbatim": true
    }
   ],
   "against": "Nothing measures whether the order helps.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep-with-fix",
   "reason": "compare-paragraphs.js 1 and 25 and v05/README.md 8 are verbatim. But nothing makes the weaker answer weaker only in the skill taught: the prompt makes the stronger one better on claim, quotation and reasoning, and the weaker one \"retells or quotes without explaining\". Restated without \"only\". Not on record.",
   "statement": "Teach what makes an answer good by comparison: two answers to the same question, one clearly stronger and one weaker but honest, and the student picks the stronger and says why.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "1",
     "quote": "Compare two answers: comparative judgement. Two Grade 9 paragraphs answer the same question; the reader picks the",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "25",
     "quote": "other is weaker but honest: it retells or quotes without explaining. Neither contains a factual error about the text.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v05/README.md",
     "lines": "8",
     "quote": "comparative judgement and faded non-examples (committed to on",
     "verbatim": true
    }
   ],
   "against": "The honesty check is the weakest required check (\"p\": 0.6 on the live drama comparison, v01/proof-2026-10-09.json 262), and it is asked without the text. The student's reason is saved and never marked (compare-paragraphs.js 15). v05 lists comparative judgement as a procedure still to build.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 32,
   "verdict": "keep",
   "reason": "Verbatim in compare-paragraphs.js 24, cer-frame.js 78 and cer-frame.next-step.json 13. The next-step choice puts the moves in order: the claim answers the prompt, a word is explained, and the word is linked back to the claim (cer-frame.js 75-80). It is a domain rule for Grade 9 analysis, built into prompts and checks.",
   "statement": "A strong analytical paragraph answers the question directly, quotes exactly, says what one word in the quotation suggests and links it back to the claim, while retelling or repeating the quotation is the weaker answer.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "24",
     "quote": "One is clearly stronger: a precise claim, a short exact quotation, and reasoning about a specific word.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
     "lines": "78",
     "quote": "reasoning explains a word from evidence but does not link it back to claim",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/calibration/cer-frame.next-step.json",
     "lines": "13",
     "quote": "The reasoning repeats the quotation and explains no word in it.",
     "verbatim": true
    }
   ],
   "against": "There are seed cases only (\"Seed cases only: obvious ones\", cer-frame.next-step.json 5), scored only against a label oracle.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 33,
   "verdict": "keep",
   "reason": "Verbatim in src/glue/animated.js 226 and worked-model.js 36 and 46. One quotation of 4 to 25 words is unpicked, then four or five sentences follow, one move each, with a first-person think-aloud beside each. The registry puts the block before the claim-evidence-reasoning block (mechanics.test.mjs 18). Refines the worked example in 34.",
   "statement": "Before students write, model the answer: unpick one short quotation, then write the paragraph one move per sentence, each with a first-person note on why it is there.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "226",
     "quote": "Watch how I answer today's learning question: I find a quotation, unpick its words, then write my answer one move at a time.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "36",
     "quote": "the guide shows how to answer the lesson question before the student writes, as a strong Grade 9",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "46",
     "quote": "one sentence in the first person on why I write it",
     "verbatim": true
    }
   ],
   "against": "The check that each think-aloud says what its sentence does is advisory (required: false, worked-model.js 107).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 34,
   "verdict": "keep-with-fix",
   "reason": "direct-the-line.js 24 and proof 203-206 are verbatim. Live, the judge found the line allowed different deliveries at p 0.92 and 0.94, and picked the delivery at 1 and 0.98. Line 1's quote is replaced by line 14, which says the same without the author's name. Statement unchanged. Not on record.",
   "statement": "Ask how a line should be spoken only where it can be spoken in clearly different ways and the lines around it show what the speaker wants, and take the right delivery from that want.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
     "lines": "14",
     "quote": "Choose how a line should be spoken, given what the speaker wants at that moment. One delivery fits the scene best.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
     "lines": "24",
     "quote": "delivery fits best. Offer three deliveries; exactly one fits what the speaker wants at this moment.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v01/proof-2026-10-09.json",
     "lines": "203-206",
     "quote": "\"id\": \"line-has-choices\", \"required\": false, \"verdict\": \"holds\", \"p\": 0.92",
     "verbatim": true
    }
   ],
   "against": "The check that the line allows different deliveries is advisory (required: false, direct-the-line.js 60). The best delivery sat second of three in all 4 saved items. The judge reads up to three lines either side of the line, while the card shows only the three before it (direct-the-line.js 55, 67).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/helpers.mjs",
   "lines": "13",
   "quote": "Says yes to every check except give-aways; picks paragraph A and delivery A; scores knowledge 4 of 5.",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/engine/src/decide/questions.js",
   "lines": "118",
   "quote": "Deterministic option-order rotation per sample (option order shifts answers; rotate and average).",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
   "lines": "113",
   "quote": "words aimed at whoever marks them are not an answer: no verdict, and no try (the Grade 3 engine's rule)",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
   "lines": "84",
   "quote": "the animated build asks the rebuild under the first word's card (\"did you follow what I just said?\")",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
   "lines": "39",
   "quote": "context: one sentence on the moment it comes from (who says it, to whom, just after what), without quoting it.",
   "ok": true
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
   "lines": "29",
   "quote": "wrong ones send the reader back to the surrounding lines without naming the best",
   "ok": true
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
   "lines": "29",
   "quote": "pointing at what to compare without saying which is better",
   "ok": true
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
   "lines": "93",
   "quote": "a miss does not give the words",
   "ok": true
  },
  {
   "truth": 19,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "139",
   "quote": "its give-away question was answered from general knowledge of Othello",
   "ok": false
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
   "lines": "1",
   "quote": "The reader's words are saved and shown back, never marked.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/README.md",
   "lines": "120",
   "quote": "No lesson has been reviewed by a person or used by a student.",
   "ok": true
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/calibration/cer-frame.next-step.json",
   "lines": "11",
   "quote": "The same paragraph misspelt: spelling is not one of the changes the check chooses between.",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
   "lines": "3",
   "quote": "A student performs the line, so it is never one with a slur in it",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
   "lines": "118",
   "quote": "the quotation unpicked and the sentence to rebuild, without its answers; the paragraph comes after the rebuild",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "63-64",
   "quote": "direct the line showed what the speaker wants before the pick",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/cer-frame.js",
   "lines": "89",
   "quote": "a closing line keeps no question of its own (the 3D build's rule), only quoted ones",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
   "lines": "1",
   "quote": "the guide's \"I do\", before the student writes.",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/calibration/2026-10-09T12-25-25-449Z.json",
   "lines": "6",
   "quote": "answers from the labels themselves: proves the wiring, measures nothing",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
   "lines": "6",
   "quote": "Labels need a person: a model-made label measures nothing, and a seed set this small is diagnostic only.",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/blocks/ed2f90f660c18774.json",
   "lines": "27",
   "quote": "Not about what an earlier Compare two answers block was: already in this lesson:",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
   "lines": "16",
   "quote": "what this block is about, so a second block of the same kind on the same text is told to differ",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
   "lines": "4",
   "quote": "Two tries, then the sentence is given.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
   "lines": "112",
   "quote": "a word class is a judgment call on Shakespeare, so it never holds the block, but one Jev did not confirm is not shown",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
   "lines": "115",
   "quote": "unclear is no verdict at all",
   "ok": true
  },
  {
   "truth": 54,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
   "lines": "55",
   "quote": "the words that carry the answer",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
   "lines": "3",
   "quote": "so no writer runs at play time",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/DECISIONS.md",
   "lines": "29",
   "quote": "the 3D build's paragraph coach (6.6 s through a second model) became a Jev choice of one next step",
   "ok": true
  }
 ]
}
```
