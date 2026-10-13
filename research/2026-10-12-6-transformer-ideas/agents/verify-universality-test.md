# verify:universality-test

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  nono, analyse its ideas and fold them into the research results

## Result

```json
{
 "direction": "universality-test",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim and the counts match the 32 records: 12 ready on the poem and 11 on the speech. The word web, the video essay and the worked model each failed on one text. The first clause makes a sufficiency claim that the run contradicts. The debate, the open check and the worked model also drew everything from the text and checked each part, and they still failed. Some ready blocks also kept faults: position words, keys in the middle, and feedback that restates the key. I restated it as the measured result. It overlaps candidate 30 and could serve as its evidence.",
   "statement": "Run unchanged on a poem and a speech, 23 of the lesson engine's 32 blocks passed every check: 10 of its 16 kinds on both texts, while the film, the open check and the debate failed on both.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/learning-truths/research/2026-10-12-6-transformer-ideas/README.md",
     "lines": "9",
     "quote": "a universality test: all 16 blocks made for a poem and for prose on 12 October 2026",
     "verbatim": true
    },
    {
     "path": "~/Projects/learning-truths/research/2026-10-12-6-transformer-ideas/universality-test.py",
     "lines": "16",
     "quote": "b = post(\"/api/block\", {\"text\": texts[k], \"question\": out[\"questions\"][k], \"mechanic\": m, \"n\": 1})",
     "verbatim": true
    },
    {
     "path": "~/Projects/learning-truths/research/2026-10-12-6-transformer-ideas/universality-test.py",
     "lines": "21",
     "quote": "out[\"blocks\"] = list(ex.map(make, [(k, m) for k in texts for m in mechs]))",
     "verbatim": true
    }
   ],
   "against": "Ready means every check passed, not that the block teaches: \"No lesson has been reviewed by a person or used by a student.\" (~/Projects/g9/transformer/README.md line 120)",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep",
   "reason": "The quotes are verbatim; I narrowed the line numbers. I checked the counts. art/briefs.json has 14 briefs: 12 are scenes of the play and 2 show the book. The poem's essay picked shot24-book-open for its beat on the face. The animated build's lesson file is src/content/othello-1-1.json (ops/render-animated.sh line 12). The quote-card note is in animated.js line 212. More ties to the first text are patched at threejs-render.js lines 374-376. The claim holds as scoped and is not on record.",
   "statement": "Keep out of a universal block anything made for one text, such as a stored film, a set of pictures, or a slot or label named for that text, or else make it for each text and check that it fits before use.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/films.js",
     "lines": "11",
     "quote": "{ id: \"othello-opening\", title: \"Othello: the opening (unit film)\", file: \"Othello-opening-full.mp4\", vtt: \"Othello-opening-full.vtt\", poster: \"thumbnail-othello-love.jpg\" },",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "261",
     "quote": "// its key-word cards say \"Link to deceit\": our links go on them only when that is our centre too",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/README.md",
     "lines": "49",
     "quote": "- **Fixed in its component:** its apply page labels any scene \"Act 1, Scene 1\", so our exports leave the scene panel",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/ops/render-animated.sh",
     "lines": "12",
     "quote": "cp \"$1\" \"$WORK/src/content/othello-1-1.json\"",
     "verbatim": true
    }
   ],
   "against": "The ties follow a decision to reuse the existing builds unchanged: \"Their work is used as it is, never rewritten, and nothing is written into their repositories.\" (~/Projects/g9/transformer/DECISIONS.md line 18)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "The claim that the fit question was never asked on the poem is false. The block record keeps only its last attempt, which failed a code check (judge [] at line 161), and judgeCalls counts only the last try. The decision log runs/decisions/0419fc2dc6f6bacf.json holds three judged drafts. Each failed film_fits at 0.02 (lines 184, 791 and 1398), and in two of them every other answer passed. So the fit check ran on both texts, and I removed 'a fit check run only after the items pass may never run'. What holds: the picker returns the only film for any text, the writer drafted sound items on it for both texts, and only the fit question stopped the block. The poem's record also gives a feedback fault as its reason, which hides the real one. The claim is related to 4 but not a duplicate.",
   "statement": "Settle whether a stimulus belongs with the lesson's text before writing items on it: with one film on file, the writer drafted checks on a play's film for a poem and for a speech, the item judgments held, and only the fit question, asked after them, failed the block (0.02 and 0.01).",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/films.js",
     "lines": "55",
     "quote": "/** The film whose narration shares most words with the text and the question; null if there is none. */",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
     "lines": "184-187",
     "quote": "\"value\": 0.02,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/d2d7d0787d6754d9.json",
     "lines": "97",
     "quote": "The film belongs with this text: the judge found this does not hold",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/d2d7d0787d6754d9.json",
     "lines": "167",
     "quote": "\"p\": 0.01,",
     "verbatim": true
    }
   ],
   "against": "Where it ran, the fit question caught the mismatch at once: \"p\": 0.01 on the speech (~/Projects/g9/transformer/runs/blocks/d2d7d0787d6754d9.json line 167), and 0.02 on each of three poem drafts (~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json lines 184-187).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep",
   "reason": "The quotes are verbatim and I checked the counts against the records. On the speech, the top-ranked sentence is unit 7 at p 0.96 (focus file 08893615be5777b5, which matches the speech text). Six ready blocks of six kinds use it: the video essay's quote, direct the line, the evidence hunt (keyed [7]), the CER frame, compare two answers, and the quick check (in its evidence and its feedback). The quick check's wrong-option feedback quotes the sentence the evidence hunt keys. On the poem, the top line is unit 4 at p 0.96, and the evidence hunt, worked model, CER frame and compare two answers use it. Five of its 14 lines were ranked. This extends 48 to blocks of different kinds and adds a cross-block case to 29. It is not a duplicate.",
   "statement": "Check a lesson's blocks against each other, not only against earlier blocks of the same kind: blocks of different kinds made from one question converge on its top-ranked line, and one can show the line another asks the student to find.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "41",
     "quote": "The lines most relevant to the lesson question are ${top}. Prefer them, but use any line that fits the task.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/blocks.js",
     "lines": "67",
     "quote": "what the lesson's earlier blocks of this kind cover: those made or being made (a lone QC-3 makes no QC-1 first);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/9a28237802fccd82.json",
     "lines": "16",
     "quote": "will little note, nor long remember what we say here",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/focus/08893615be5777b5.json",
     "lines": "4-7",
     "quote": "\"p\": 0.96",
     "verbatim": true
    }
   ],
   "against": "Centring on the key line is intended inside a block, and the focus note allows any line: \"building an argument: the line that matters most, what it shows, and two readings a careful reader could\" (~/Projects/g9/transformer/src/mechanics/video-essay.js line 38); \"Prefer them, but use any line that fits the task.\" (util.js line 41)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, and 0.78 and 0.89 match the left-2 and right-2 verdicts. The film's own feedback on a wrong option (line 83) says both readings put the power on action, which confirms they are one claim. 'Rivals a reader must choose between' asks for more than the evidence or the design supports. The prompt asks for two readings a careful reader could defend, and those need not exclude each other. I restated it as distinct readings.",
   "statement": "When a block sets two readings side by side, check that they are two readings, not two halves of one claim: on a speech, 'Speech Is Weak' and 'Action Is Powerful' passed, because each was checked only for whether it could be defended.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "132",
     "quote": "Beat ${k + 1}: the first reading can be defended",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/34c293906aa945a2.json",
     "lines": "41",
     "quote": "\"label\": \"Speech Is Weak\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/34c293906aa945a2.json",
     "lines": "48",
     "quote": "\"label\": \"Action Is Powerful\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/34c293906aa945a2.json",
     "lines": "83",
     "quote": "Re-examine the two readings presented, which both place long term power on the side of physical action rather than speech.",
     "verbatim": true
    }
   ],
   "against": "The debate block does check that its two sides differ, but only in wording: \"norm(A.label) !== norm(B.label) && norm(A.counter) !== norm(B.counter)\" (~/Projects/g9/transformer/src/mechanics/debate.js line 72)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, and p 0.31 matches the wrong-0-1 verdict. The prescription, to check each wrong option on its own, is truth 31, and that check is what caught this. I kept it only for what it adds: parallel phrasing as a source of second right answers, with a case. The key-word part is overstated. 'consecrate' and 'hallow' do accept each other, as key-words.js line 3 allows, but nothing shows the deck would have failed without that, so I dropped 'passed only because'.",
   "statement": "Where a text says one thing twice in parallel words, a wrong option taken from it may be a second right answer: a rebuild keyed to 'little note' offered the parallel 'long remember' as wrong, and a judge found it did not make the sentence wrong (0.31).",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/be97f27fc4c4a65a.json",
     "lines": "120",
     "quote": "makes the rebuilt sentence wrong: the judge found this does not hold",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/be97f27fc4c4a65a.json",
     "lines": "58-62",
     "quote": "\"long remember\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/learning-truths/research/2026-10-12-6-transformer-ideas/universality-test-gettysburg.txt",
     "lines": "5",
     "quote": "The world will little note, nor long remember what we say here, but it can never forget what they did here.",
     "verbatim": true
    }
   ],
   "against": "The check this calls for already exists and fired (wrong-0-1 fails at 0.31, ~/Projects/g9/transformer/runs/blocks/be97f27fc4c4a65a.json line 120), and key-words.js line 3 already treats another deck word that fits a gap as no miss: \"another word of the deck that also fits the sentence is not a miss\"",
   "general": true,
   "duplicate_of": "31",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "drop",
   "reason": "The quotes are verbatim, and the debate's last drafts did use the text's words without quotation marks: a 12-word run in aeb043df247f1b45.json line 17. But the claim that the check tests a sign rather than its property fails. The house rule and the debate prompt define quoting as exact words in double quotes (util.js lines 9-10, debate.js lines 50-51), so unmarked words break the rule the check names. The decision logs also change the story. The first drafts on both texts did quote in marks (runs/decisions/f23aebacf033daa2.json and aeb043df247f1b45.json, lines 26-28) and reached the judge, which failed them: the poem's second push-back at 0.39, the speech's two unsure. Only the rewrites lost the marks. The earlier-run example (v01/QA.md lines 38-40) is about a word-count threshold, not a sign. What the evidence supports is a repair in code, which is candidate 7.",
   "statement": "Make a check test the property it names, not a sign of it: a check that a push-back quotes the text looked only for quotation marks, and failed push-backs on two texts that used the text's exact words without them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "71",
     "quote": "check(\"counters-quote\", \"Each push-back quotes the text\", item.sides.every((s) => quotesIn(s.counter).length > 0), \"a push-back quotes no words from the text\"),",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/aeb043df247f1b45.json",
     "lines": "17",
     "quote": "How can speech matter if the world will little note, nor long remember what we say here?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "39",
     "quote": "the exact-quotation check only accepted quotations of two or more words",
     "verbatim": true
    }
   ],
   "against": "Quotation marks also tell the student which words are the text's, so the convention matters in itself: \"marks is the text's own words, copied exactly, in double quotes: never put a paraphrase in quotes.\" (~/Projects/g9/transformer/src/mechanics/util.js line 10)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, and the statement stands. One correction: judgeCalls 0 counts only the last try. The decision logs hold one judged draft per text. Its push-backs were in quotation marks, and the judge failed them: the poem's at 0.39 (decisions/f23aebacf033daa2.json line 122), the speech's two unsure. The rewrites dropped the marks and never reached the judge again, and the last one failed only for the marks. Repairing the marks in code would have let those rewrites be judged, though whether they would pass is unknown. The engine already repairs leading verdicts, semicolons and dashes in code (house.js), and paragraph names (compare-paragraphs.js line 39). The failure message 'quotes no words from the text' was also untrue of the rewrites. Not on record.",
   "statement": "Repair in code what needs no judgment, such as quotation marks missing round words found verbatim in the text, and send back to the writer only what does.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/f23aebacf033daa2.json",
     "lines": "13",
     "quote": "How do the details of a wrinkled lip and sneer of cold command suggest a ruler who also possessed great passion?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/aeb043df247f1b45.json",
     "lines": "28",
     "quote": "\"counter_1\": \"How do you explain the claim that \\\"the world will little note, nor long remember what we say here\\\"?\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/f23aebacf033daa2.json",
     "lines": "119-122",
     "quote": "\"value\": 0.39,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "2",
     "quote": "judge checks the rest on positive evidence, and a failing draft gets exactly one correction pass with the reasons.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/house.js",
     "lines": "3",
     "quote": "leading verdict (\"Correct.\", \"This is incorrect;\") is dropped: both builds show the verdict themselves (YES, NOT THAT",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "39",
     "quote": "the reader sees \"Answer A\" and \"Answer B\", so the feedback names them that way (\"paragraph b\" -> \"Answer B\")",
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
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, and so is the five-of-nine count: the third rung on criterion 0, and the second and third rungs on criteria 1 and 2. 'Every hint that points to the place hands it over' overstates. The first rungs, such as 'Look at the fifth line for details about the mouth', pointed to the place without leaking and passed. The last rungs leaked because they named the words without quotation marks. If quoted, they would pass the leak check, since open-check.js line 65 strips quotations, yet they would quote the answer itself. The speech's last rung did exactly that with its own leak words (b5f74899349e1331.json lines 22-28). The speech's failure was a different fault, give-away wording (candidate 9). The claim is related to 14 but not a duplicate.",
   "statement": "Ask an open check for what the words show, not for the words themselves: when the answer is the text's own words, a hint that names the place names the answer, and on a poem five of nine hints, all three last rungs among them, were held for it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/d872bc1dfbda65fb.json",
     "lines": "8",
     "quote": "What facial expressions are visible on the broken statue's head?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/d872bc1dfbda65fb.json",
     "lines": "87",
     "quote": "a hint uses a word that hands the answer over, or the answer itself:",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "42",
     "quote": "\"third_nudge\": \"the words to read again, quoted exactly, still not the answer\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "65",
     "quote": "const unquoted = (t) => t.replace(/\"[^\"]*\"|“[^”]*”/g, \" \");",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/b5f74899349e1331.json",
     "lines": "22",
     "quote": "\"third_nudge\": \"Read the words \\\"little note, nor long remember\\\" alongside \\\"never forget\\\" to see the contrast.\",",
     "verbatim": true
    }
   ],
   "against": "The project lets the last hint quote the line by design: \"a hint may quote the text, even the line to\" (~/Projects/g9/transformer/src/mechanics/open-check.js line 63)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (lines narrowed), and 0.65 matches the verdict. 'Will find any answer obvious' overstates a single integration case, so I softened it. The test case fits the rule: the question's wording names 'the endurance of spoken words'. But one case cannot show whether the 0.65 came from the wording or from knowing the speech. The rule is adopted in code and is not a duplicate of 18.",
   "statement": "Judge whether a question gives its answer away from its own wording only: a judge that knows a famous work can answer from that knowledge, which is no give-away.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "139",
     "quote": "its give-away question was answered from general knowledge of Othello (now: the question's",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "87",
     "quote": "Judge only the wording of q, not what a reader may already know about the work.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/b5f74899349e1331.json",
     "lines": "130",
     "quote": "\"label\": \"The question does not give its answer away\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/b5f74899349e1331.json",
     "lines": "135",
     "quote": "\"value\": 0.65,",
     "verbatim": true
    }
   ],
   "against": "none found; one case on a famous speech cannot separate a give-away in the wording from one drawn from knowing the work",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, and the hint's count is wrong: the first sentence ends 'Stand in the desert.', and the face is in the second. 'A poem with one speaker' is inaccurate. Ozymandias has a narrator and a traveller, and the inscription speaks too. What the engine sees is a poem with no speaker labels. That the play framing caused the sentence count is an inference from one hint, so the statement now says what happened rather than why. The other play-framed prompts (quick check, direct the line, the word-in-focus scale) produced ready blocks on both texts, as the against notes. No check reads a hint for truth, which also bears on 14.",
   "statement": "Word a block meant for any text in terms every text has: on a poem with no speaker labels, a hint told to point to who speaks or what moment to look at sent the reader to 'the first sentence', and the face it meant is in the second.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
     "lines": "28",
     "quote": "- hint: one sentence that points to who speaks or what moment to look at, without quoting the line.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/963297774d627c12.json",
     "lines": "12",
     "quote": "Look at the description of the face's mouth and expression in the first sentence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/samples/ozymandias.md",
     "lines": "4",
     "quote": "Stand in the desert. Near them, on the sand,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/samples/ozymandias.md",
     "lines": "6",
     "quote": "And wrinkled lip, and sneer of cold command,",
     "verbatim": true
    }
   ],
   "against": "The play-framed blocks were still ready on both new texts, for example direct the line on the speech: \"The judge also picks delivery B, with a clear margin\" (~/Projects/g9/transformer/runs/blocks/e47511c58b5dd64c.json line 93, p 1).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, and the coverage claim holds. The film blocks have a code check and a judged truth check on feedback, the quick check has only the code check, and word in focus and direct the line have neither. But giving those blocks 'the same checks' would not have caught these lines. The shared-run test needs a shared run of at least three words, or of the whole key if it is longer. 'making land sacred' shares one word with its key, and 'the permanent claim of power' shares two with a 13-word key. The judged question asks only whether a line is true. I restated it as a check by meaning. It overlaps candidate 13 and supports 14.",
   "statement": "Check wrong-option feedback for giving the key away in other words, in every block that shows it: shipped feedback said 'making land sacred' for the key 'make sacred or declare holy', in a block with no such check, and a check for shared runs of words would have passed it too.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/a75bd9643fa602d9.json",
     "lines": "40",
     "quote": "Examine the sixth line again to consider how the text distinguishes ceremonial speech from making land sacred.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/5722a3741161394e.json",
     "lines": "57",
     "quote": "Re-read the tenth line to consider the permanent claim of power in the title.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "116",
     "quote": "sharedRun(f, c.options[c.answer]) >= Math.max(3, words(c.options[c.answer]).length)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "187",
     "quote": "- code: no \"beat\", \"cue\", \"caption\" or \"frame\", and no wrong-option feedback that names the answer;",
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
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. I confirmed the counts by searching the 32 records. Ready blocks hold 13 position lines: 1 in the evidence hunt's hint and 6 in each word-in-focus item. Five of them are in what a student sees, and the failed open check holds 5 more. I removed one claim: 'the sixth line of a speech points at nothing a reader can see'. The engine's own page draws each sentence as its own row, with a 'Line N' tooltip and screen-reader label (web/lesson.js lines 157-159). This refines 1 and 53 and is not a duplicate.",
   "statement": "Plant a check's faults in the forms a writer actually produces: a line-number check tested only on digits passed 13 lines in three ready blocks that pointed by position in words, such as 'the tenth line'.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "46",
     "quote": "const LINE_NUMBER = /\\b(?:L\\d+|lines?\\s+\\d+)/i;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "65",
     "quote": "assert.equal(houseChecks({ feedback: [\"Look again at line 12.\"] })[0].ok, false);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/a75bd9643fa602d9.json",
     "lines": "38",
     "quote": "Re-read the sixth line to see what spiritual quality the speaker says cannot be bestowed by speeches alone.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/5722a3741161394e.json",
     "lines": "57",
     "quote": "Re-read the tenth line to consider the permanent claim of power in the title.",
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
   "verdict": "keep",
   "reason": "The quotes are verbatim (narrowed to line 22 within 15-23). The threshold is confirmed: feedback is flagged only for a shared run of at least three words, or of the whole key if longer. A two-word key can share at most two words, so 'Around 1603' can never be flagged, while question 2's three-word key was. The quick check uses the same threshold (quick-check.js line 54). Not on record.",
   "statement": "A check that wrong-option feedback does not name the key must catch a key of one or two words: one that waits for a shared run of three words let feedback state a two-word key outright.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "116",
     "quote": "sharedRun(f, c.options[c.answer]) >= Math.max(3, words(c.options[c.answer]).length)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/0419fc2dc6f6bacf.json",
     "lines": "22",
     "quote": "Listen again to hear that the play was written around 1603.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/0419fc2dc6f6bacf.json",
     "lines": "146",
     "quote": "question 2, option A: its feedback names the right answer; question 2, option C: its feedback names the right answer",
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
   "reason": "The quotes are verbatim (lines narrowed). I recomputed the counts. The 9 October proof has 8 judged wrong options: 1 held (0.6), 3 unsure (0.53, 0.46, 0.44) and 4 not tempting (0.37, 0.37, 0.35, 0.2). The test has 8: 1 unsure (0.55) and 7 not tempting (0.18 to 0.37). All were in ready blocks, for a total of 1 held, 4 unsure and 11 not tempting. The claim holds, and the against is fair.",
   "statement": "Treat a check that keeps failing as a finding, not noise: a judge confirmed only one of sixteen wrong options in shipped choice items as tempting, and nothing was held, because that check only advises.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "74",
     "quote": "label: `Option ${letters[i]} would tempt a reader who skimmed`, required: false,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "43",
     "quote": "whether each wrong option would tempt a reader who skimmed; on Ozymandias it flagged two distractors as not tempting.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/5722a3741161394e.json",
     "lines": "203",
     "quote": "\"label\": \"Option A would tempt a reader who has not looked closely\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v01/proof-2026-10-09.json",
     "lines": "319-322",
     "quote": "\"p\": 0.6",
     "verbatim": true
    }
   ],
   "against": "The temptation judgments are themselves unmeasured: \"bounded questions with the evidence supplied; their precision is not yet measured (v04).\" (~/Projects/g9/transformer/v01/QA.md line 46)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. I reproduced the counts, measuring a delivery by its tone and stressed word together; by tone alone the poem's delivery adds a set, giving 13 of 19. The shipped key is 80 characters beside wrong options of 31 and 38. 'The only length rule is the quick check's' is not quite right: compare two answers limits its paragraphs (compare-paragraphs.js line 51). So the quick check's is the only option-length rule for three-option sets. The claim is related to 45, which is about position, and is not a duplicate.",
   "statement": "Check option lengths across a whole set, in every choice block: the right option was the longest in 12 of the 18 three-option sets that had a single longest, twice what chance gives, and only one block limits option length, item by item.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "55",
     "quote": "check(\"length-balanced\", \"No option stands out by length\", Math.max(...lens) <= 2.2 * Math.min(...lens), \"one option is much longer than the others\"),",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/5722a3741161394e.json",
     "lines": "50",
     "quote": "An absolute claim of supreme power and absolute authority over all other rulers.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "24",
     "quote": "rules them out. Keep the options a similar length.",
     "verbatim": true
    }
   ],
   "against": "none found; the counts come from one run with one block of each kind per text",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "keep",
   "reason": "The quotes are verbatim (lines narrowed). I recomputed the positions: over 24 sets the key was first 8 times, middle 13 and last 3, and it was in the middle in 9 of the 10 sets shown in ready blocks. The four personas are strong, a guesser who picks uniformly, stuck, and adversarial (the grader line); none uses position or length. Nothing in src or web shuffles options. This adds a persona to 43 and evidence to 45 and is not a duplicate.",
   "statement": "Give the scripted players a test-wise guesser who picks the middle or the longest option, since one who picks at random cannot expose a cue in the items.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/quality/personas.js",
     "lines": "47",
     "quote": "guess: (v, r) => ({ type: \"choose\", index: pick(r, v.active.view.options.length) }),",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/fa497dafbb0eb7c2.json",
     "lines": "14",
     "quote": "\"answer\": 1,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/e47511c58b5dd64c.json",
     "lines": "23",
     "quote": "\"best\": 1,",
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
   "reason": "The quotes are verbatim, with two corrections. First, the code list is a short pattern of terms from the first play, not that play's lines (threejs.js line 78), so on another text it catches only those terms. On the two test texts the code checks passed with nothing to find. Second, the judged guard (0.93 to 0.99) runs only in the three kinds that ask it: word in focus, direct the line and the worked model. It does not cover every line a student works with. The original's last clause restates 28, so I cut it. What stays adds the one-text-list point, a sibling of candidate 1, and evidence for 28.",
   "statement": "A guard written as a list from one text catches only that text's cases: back it with a judged check that reads each line.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs.js",
     "lines": "78",
     "quote": "Its lines never staged or voiced (scripts/check-moments.mjs SLUR, Othello's): read from the mirror at run time, so no",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs.js",
     "lines": "79",
     "quote": "Without the mirror there is none, and the Jev question carries the guard.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "106",
     "quote": "ships only on positive evidence that the line is clean.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep",
   "reason": "The quotes are verbatim, and it is a fair open question. The poem's web chose 'arrogance', the speech's web failed with no item, and nothing in the essays echoed the example point. One run per text neither shows nor rules out the pull.",
   "statement": "Do examples taken from the first text in a universal prompt pull drafts for other texts toward that text's themes?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "36",
     "quote": "lesson question: an abstract noun a Grade 9 reader knows or can learn (for example deceit, ambition, loyalty, grief).",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "47",
     "quote": "says what the lines show, close to their own words (for example \"He serves only to line his own coat\"), never an",
     "verbatim": true
    }
   ],
   "against": "The poem's web did not take the example theme: \"centre\": \"arrogance\", (~/Projects/g9/transformer/runs/blocks/4e79a689a9ff89da.json line 8)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep",
   "reason": "The quotes are verbatim, and I reproduced the count: 'Grade 9' appears on 43 lines in 16 files under src. The grade is taken at /api/transform (server.js line 171), set in ctx and stored in the lesson and scene meta, and nothing else reads it; calibrate.js fixes it at 9. The claim holds as a design rule; the against notes the engine's scope.",
   "statement": "Name the reader once and pass that name to every prompt and judge question: a grade typed into each prompt cannot be changed by the setting that claims to change it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "33",
     "quote": "const ctx = { text, question, grade: input.grade ?? 9, focus: [], avoid: avoid.filter(Boolean) };",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "6",
     "quote": "You write one activity for a Grade 9 English lesson.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "126",
     "quote": "Would a typical Grade 9 reader know what term_${k} means in line_${k} unaided?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/server.js",
     "lines": "171",
     "quote": "grade: body.grade ?? 9",
     "verbatim": true
    }
   ],
   "against": "The grade is fixed by decision: \"The mechanics and the animation are for Grade 9 and older readers, and the work lives in\" (~/Projects/g9/transformer/DECISIONS.md line 20)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep",
   "reason": "The quotes are verbatim (lines narrowed). The picks match: 0.91 and 1 for the deliveries, 0.99 and 0.99 for the paragraphs. The judge's state holds the material but not the key, so its pick is blind. Agreement is consistency rather than correctness (truth 5), and precision is unmeasured. The claim is related to 21 and 31 but not a duplicate.",
   "statement": "Where the key is a judgment call, such as the stronger of two answers or the best way to speak a line, have a judge pick blind from the same material and ship only when it picks the key by a clear margin.",
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
     "path": "~/Projects/g9/transformer/runs/blocks/e47511c58b5dd64c.json",
     "lines": "93",
     "quote": "\"label\": \"The judge also picks delivery B, with a clear margin\",",
     "verbatim": true
    }
   ],
   "against": "Judge precision is unmeasured: \"bounded questions with the evidence supplied; their precision is not yet measured (v04).\" (~/Projects/g9/transformer/v01/QA.md line 46)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "keep",
   "reason": "The quotes are verbatim (lines narrowed), and the numbers are confirmed: the poem's glossary kept 7 of 10 terms, 5 of them unsure, with 'read' at 0.41; the word class of 'little note' was unsure at 0.5. One minor point: the speech's worked model failed, so its blanked word class was never shown to a student, though the record's view has it blank. This refines 50 with a reasoned exception for glosses and is not a duplicate.",
   "statement": "When a judge is unsure, leave out what could mislead and keep what could only be unneeded: an unconfirmed word class or picture is dropped, while a gloss is dropped only when the judge is sure the reader knows the word.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "130",
     "quote": "the Grade 3 engine's judgeTerms rule: a drafted word Jev is sure a Grade 9 reader knows unaided is dropped, unless",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "112",
     "quote": "a word class is a judgment call on Shakespeare, so it never holds the block, but one Jev did not confirm is not shown",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "146",
     "quote": "a painting Jev did not find fitting is left out of the frame (the claims stay)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep",
   "reason": "The quotes are verbatim. The 3D build's own code marks a checkpoint secure once two attempts are spent (line 369), and the export patches it to 'given'. The hunt, the open check and the worked model each save a release flag. This extends 49 and 42 and is not a duplicate.",
   "statement": "When the answer is given after the last try, record the step as given, never as accepted, so a step finished that way is not counted as the student's success.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "366",
     "quote": "// two tries, then the answer is given and the step completes, but a given answer is not shown as \"Accepted\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "369",
     "quote": "if (v !== 'secure' && attempt >= 2) v = 'secure'",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
     "lines": "98",
     "quote": "done: true, released: true, saved: { released: true }",
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
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. Say-it-back tolerates a slip only in a word of five letters or more (say-it-back.js line 22), so I narrowed 'a slip in a sentence said back'. In the key-word deck, a near spelling gets the nudge 'Nearly. That is the word, but the spelling is not right yet.' (key-words.js line 119). This refines 25 and is not a duplicate.",
   "statement": "Count spelling only where the word itself is being learned: a taught word recalled into a gap must be spelled right, while a near spelling of a longer word in a sentence said back is named and not counted.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "4",
     "quote": "gets a nudge, since a taught word is spelled right; the second miss gives the word.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "3",
     "quote": "that every key word is there, and a near spelling of a long word is named but not counted as a miss (the 3D build's",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "22",
     "quote": "/** \"yes\", \"spelling\" (a slip in a word of five letters or more, named but not a miss) or \"no\". */",
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
   "reason": "The quotes are verbatim; this is an adopted rule in the 3D export. Not on record.",
   "statement": "Write a choice question's stem so it can be answered without its options, since a stem that only works beside them cannot be reused as an open question.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "33",
     "quote": "// a question that only works beside its options (\"Which of these…\") is not asked open",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "145",
     "quote": "skipped.push({ id: b.id, reason: \"its question only works beside its options\" })",
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
   "reason": "The quotes are verbatim. For the 3D build's own notes, the judged gloss check is not required (glossary.js line 125, required: drafted). Not on record.",
   "statement": "Where a text comes with its own authored notes, use them unchanged and draft none, and let a judge read them but never hold them back.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "5",
     "quote": "through unchanged, each where its line mark puts it, and nothing is drafted.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "121",
     "quote": "the 3D build's own notes are its content: Jev's reading of them is kept, and never holds them",
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
   "reason": "The quotes are verbatim. The guide boxes say who speaks, or ask the reader to read slowly with the question in mind, and never summarise the content. Not on record.",
   "statement": "Lines that code writes around any text should say only what code can know, such as who speaks or which section comes next, never what the passage means.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "114",
     "quote": "Plain lines of ours: who speaks, never the content.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "119",
     "quote": "return say(who ? `In this ${where}, ${who}.` : `In this ${where}, read slowly, with the question in mind.`);",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim and the statement holds. The project's own preflight note says some text passes the schema yet cannot fit, and beat 2's evidence lines (44 and 52 characters, under the 60 allowed) overflowed. One correction: beat 3's points (49, 51, 53 and 55 characters) mostly broke the prompt's 50-character limit, and both labels (25 characters) broke its 24-character limit. So they do not show text inside the limits overflowing. The evidence beat also carried a picture, and the speech's essay did not. The statement is unchanged and is related to 26.",
   "statement": "Check that every frame's text fits by rendering it, since text inside the stated character limits can still overflow.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/video/frames.js",
     "lines": "3",
     "quote": "state renders on the canvas (the host contract's preflight: some text passes the schema yet cannot fit).",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "43",
     "quote": "- \"evidence\": heading (at most 50 characters); claims: two or three, each at most 60 characters, each true to the text;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/7e771d331c6b4135.json",
     "lines": "120",
     "quote": "Every frame validates and fits its canvas: beat 2: render Evidence line exceeds two display rows | beat 3: render Point exceeds two display rows",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/7e771d331c6b4135.json",
     "lines": "32",
     "quote": "The sculptor captured passions that survive on stone",
     "verbatim": true
    }
   ],
   "against": "A passing render is not a good layout: \"The quote card leaves a one-word last line, and its underline starts on the\" (~/Projects/g9/transformer/README.md line 118)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep",
   "reason": "The quotes are verbatim (lines narrowed). The against holds. The poem's suggested question was narrower than the sample's own: 5 of its 14 lines were ranked for it, while 13 lines were judged relevant for the sample question in the 9 October proof (v01/QA.md line 32). The judge's question also asks two things at once. The practice is adopted and not on record.",
   "statement": "Suggest a lesson question from the text alone, keep it only on a judge's positive evidence that the text answers it, and cache it so the same text always gets the same question.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/question.js",
     "lines": "3",
     "quote": "positive evidence. Cached by text, so the same text is given the same question.",
     "verbatim": true
    },
    {
     "path": "~/Projects/learning-truths/research/2026-10-12-6-transformer-ideas/universality-test.json",
     "lines": "4",
     "quote": "\"gettysburg\": \"How does the speaker contrast the actions of the soldiers with the words spoken at the dedication?\"",
     "verbatim": true
    }
   ],
   "against": "The judge question asks two things at once: \"Can question_${i} be answered from passage alone, and is it worth a Grade 9 lesson of about an hour?\" (~/Projects/g9/transformer/src/question.js line 34); and the poem's suggested question was narrower than the one it came with: \"question\": \"What does the poem suggest about power and time?\" (~/Projects/g9/transformer/samples/index.json line 6)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 29,
   "verdict": "keep",
   "reason": "The quotes are verbatim, and it is a fair open question. The film's second check is keyed to the essay's own framing of two readings ('One reading stresses the weakness of speech while the other stresses the power of action'). Truth 4 is about questions on a text and does not settle this.",
   "statement": "Should a check inside a film about a text test the text, or may it test what the film itself argued?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/34c293906aa945a2.json",
     "lines": "75",
     "quote": "\"stem\": \"How do the two readings interpret the speaker's contrast?\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "55",
     "quote": "Each question is answered by the narration so far.",
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
   "reason": "The quotes are verbatim, and 9 of 32 failed. Two of the three holes the found_by credits to text kind could appear on the first play too: line positions spelled out in words, and a two-word key named in feedback. The third, 'quotation marks as the only sign of quoting', did not survive (see 6). The film mismatch does depend on the kind of text: the film block was ready on the play (v02/QA.md line 190). I restated the claim around that case. It overlaps candidate 0 and refines 1.",
   "statement": "Test every block on texts of each kind it claims to serve, not only the one it was built on: one run on a poem and a speech failed 9 of 32 blocks, among them a fault no run on the first play could show, its only film offered for any text.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/README.md",
     "lines": "99",
     "quote": "`test/fixtures/othello-items.json` and a play in `src/quality/personas.js`.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/films.js",
     "lines": "11",
     "quote": "{ id: \"othello-opening\", title: \"Othello: the opening (unit film)\", file: \"Othello-opening-full.mp4\", vtt: \"Othello-opening-full.vtt\", poster: \"thumbnail-othello-love.jpg\" },",
     "verbatim": true
    },
    {
     "path": "~/Projects/learning-truths/research/2026-10-12-6-transformer-ideas/universality-test.py",
     "lines": "21",
     "quote": "out[\"blocks\"] = list(ex.map(make, [(k, m) for k in texts for m in mechs]))",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "66",
     "quote": "assert.equal(houseChecks({ hint: \"Reread L7 and L8.\" })[0].ok, false);",
     "verbatim": true
    }
   ],
   "against": "A live proof on two kinds of text did exist for six blocks: \"- A proof on two public-domain texts of different kinds: Othello 1.1 (drama) and Ozymandias (poem).\" (~/Projects/g9/transformer/v01/README.md line 14)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
   "lines": "65",
   "quote": "assert.equal(houseChecks({ feedback: [\"Look again at line 12.\"] })[0].ok, false);",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/blocks/0419fc2dc6f6bacf.json",
   "lines": "13",
   "quote": "\"stem\": \"When was Shakespeare's play Othello written?\",",
   "ok": true
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/blocks/5722a3741161394e.json",
   "lines": "57",
   "quote": "Re-read the tenth line to consider the permanent claim of power in the title.",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/blocks/9a28237802fccd82.json",
   "lines": "16",
   "quote": "will little note, nor long remember what we say here",
   "ok": true
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/blocks/be97f27fc4c4a65a.json",
   "lines": "120",
   "quote": "makes the rebuilt sentence wrong: the judge found this does not hold",
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
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
   "lines": "130",
   "quote": "the Grade 3 engine's judgeTerms rule: a drafted word Jev is sure a Grade 9 reader knows unaided is dropped, unless",
   "ok": true
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/text.js",
   "lines": "2",
   "quote": "or a sentence (prose). Stage directions are kept for display but are never evidence.",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/DECISIONS.md",
   "lines": "29",
   "quote": "its model: the 3D build's paragraph coach (6.6 s through a second model) became a Jev choice of one next step (0.26 to",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/question.js",
   "lines": "34",
   "quote": "Can question_${i} be answered from passage alone, and is it worth a Grade 9 lesson of about an hour?",
   "ok": false
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Projects/g9/art/briefs.json",
   "lines": "186",
   "quote": "with a decorative woodcut border and a small woodcut picture of Venice on the left page",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/util.js",
   "lines": "135",
   "quote": "Words quoted or retold from the text, a character's commands among them, are part of an answer and do not count.",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "194",
   "quote": "the saved link's first six blocks, all made before the line-number rule, and played them; three cited line numbers.",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/README.md",
   "lines": "111",
   "quote": "Calibration has seed sets only: it proves the wiring and measures nothing until people label examples.",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/blocks/a75bd9643fa602d9.json",
   "lines": "39",
   "quote": "This definition correctly reflects the religious sense of declaring a physical place holy.",
   "ok": true
  }
 ]
}
```
