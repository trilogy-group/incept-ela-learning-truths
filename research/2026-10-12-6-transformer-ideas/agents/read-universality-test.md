# read:universality-test

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  nono, analyse its ideas and fold them into the research results

## Result

```json
{
 "direction": "universality-test",
 "coverage": {
  "read": [
   "~/Projects/learning-truths/research/2026-10-12-6-transformer-ideas/ (README.md, run.json, directions.json, existing-order.json, head of args.json, universality-test.json, universality-test.py, universality-test-gettysburg.txt)",
   "~/Projects/g9/transformer/runs/blocks/: all 32 records of the test (the 9 failed ones in full; for the 23 ready ones the item, every code check and every judge verdict)",
   "~/Projects/g9/transformer/runs/focus/08893615be5777b5.json and cafa551791ea3a78.json (line focus for the two texts); runs/decisions/focus-*.json only to tell which text each belongs to",
   "~/Projects/g9/transformer/src/mechanics/: all 16 block modules and util.js",
   "~/Projects/g9/transformer/src/: text.js, transform.js, blocks.js, judge.js, engine.js, house.js, analyse.js, question.js, films.js, and the mechanics and samples routes of server.js",
   "~/Projects/g9/transformer/src/video/art.js, frames.js, beats.js",
   "~/Projects/g9/transformer/src/glue/threejs-render.js (whole), threejs.js (quote helpers and slur list), animated.js (option passing, quote card, stage label)",
   "~/Projects/g9/transformer/src/quality/personas.js (lines 1-80)",
   "~/Projects/g9/transformer/ops/render-animated.sh",
   "~/Projects/g9/transformer/DECISIONS.md, README.md, v01/README.md, v01/QA.md, v01/proof-2026-10-09.json (temptation verdicts), v02/README.md (lines 1-60), v02/QA.md (passages found by search)",
   "~/Projects/g9/transformer/samples/index.json and samples/ozymandias.md",
   "~/Projects/g9/transformer/test/mechanics.test.mjs (lines 55-80); listings of test/ and test/fixtures/; searches of text.test.mjs and threejs-render.test.mjs",
   "~/Projects/g9/art/briefs.json (painting subjects offered to the video essay)",
   "~/Projects/shadow/animated-build/src and ~/Projects/shadow/3d-build/src: a filename search for option shuffling only"
  ],
  "skipped": [
   "v03/ to v11/ README.md: planned stages, another direction's scope; searched for universality words only",
   "src/video/produce.js, src/core/, src/quality/playtest.js and calibrate.js, src/glue/animated-judge.js, threejs-archivist.js, sources.js and web/: other directions' scope; grepped only where a claim needed it (no shuffling in web/lesson.js)",
   "runs/decisions/<block key>.json: the judge logs behind each block; the block records already carry every verdict",
   "the roughly 70 other block records in runs/blocks/ from 9 October: not part of the test",
   "samples/othello-1-1.md and test/fixtures/othello-items.json contents: the first text itself, not needed for any claim",
   "the 3D build's src/practice/text.ts, which mentions shuffle: outside g9 and not read",
   "no .env, key, token or credential file was opened; nothing was written"
  ],
  "notes": "Counts I computed from the records, not stated by the project: key positions (first 8, middle 13, last 3 over 24 three-option sets; middle in 9 of the 10 sets shown in ready blocks); the key was the strictly longest option in 12 of the 18 sets that had a single longest; position words in student text that passed the line-number check (13 lines in 3 ready blocks, 5 of them shown; 5 more in a failed open check); blocks of different kinds on each text's top-ranked line (6 ready on the speech, 4 on the poem); temptation verdicts across the 9 October proof and this test (1 held, 4 unclear, 11 not tempting of 16); 'Grade 9' on 43 lines in 16 src files. The word web on the speech failed with no item kept ('idea[1] must be a non-empty string' after two tries), so it yields no finding beyond a brittle reply shape. Each failed record keeps only its last attempt's reasons. The test script reads gettysburg.txt and writes result.json; the run folder holds them as universality-test-gettysburg.txt and universality-test.json. Every path contains the machine account's home-folder name; no file path otherwise names a person, so name_bearing_source is false throughout. No option shuffling exists in the engine's src or web or in the animated build's src, so stored order is what a student sees."
 },
 "candidates": [
  {
   "statement": "A block carries to any text when everything it shows is drawn from that text and each part is checked on its own: run unchanged on a poem and a speech, 10 of 16 block kinds were ready on both.",
   "kind": "measured",
   "found_by": "All 16 blocks were made through the composer's API for a poem and for a speech on 12 October 2026, one of each per text: 23 of 32 were ready (12 on the poem, 11 on the speech). The ten kinds ready on both take everything from the text and the question and check each part (glossary, key words, learning question, quick check, evidence hunt, word in focus, direct the line, claim-evidence-reasoning, compare two answers, say it back). The film block, the open check and the debate failed on both; the word web, the video essay and the worked model each failed on one. The other candidates here give the causes.",
   "evidence": [
    {
     "path": "~/Projects/learning-truths/research/2026-10-12-6-transformer-ideas/README.md",
     "lines": "9",
     "quote": "a universality test: all 16 blocks made for a poem and for prose on 12 October 2026"
    },
    {
     "path": "~/Projects/learning-truths/research/2026-10-12-6-transformer-ideas/universality-test.py",
     "lines": "16",
     "quote": "b = post(\"/api/block\", {\"text\": texts[k], \"question\": out[\"questions\"][k], \"mechanic\": m, \"n\": 1})"
    },
    {
     "path": "~/Projects/learning-truths/research/2026-10-12-6-transformer-ideas/universality-test.py",
     "lines": "21",
     "quote": "out[\"blocks\"] = list(ex.map(make, [(k, m) for k in texts for m in mechs]))"
    }
   ],
   "against": "Ready means every check passed, not that the block teaches, and there was one block of each kind per text: \"No lesson has been reviewed by a person or used by a student.\" (~/Projects/g9/transformer/README.md line 120)",
   "scope_note": "universal (shown on two literary texts in English, a poem and a speech)",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep out of a universal block anything made for one text, such as a stored film, a set of pictures, or a slot or label named for that text, or else make it for each text and check that it fits before use.",
   "kind": "measured",
   "found_by": "Where the engine is tied to its first text, blocks failed or degraded on new ones: its only film is that play's unit film, and the film block failed on both new texts; 12 of the 14 painting briefs are scenes of that play and 2 its frame story's book, and the poem's video essay picked the book for claims about a carved face; the 3D build lends one slot, whose key-word cards read 'Link to deceit'; the animated build's lesson file is named for the play's first scene and its quote card names one of its characters beside any reference; its apply page labelled any scene 'Act 1, Scene 1'.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/films.js",
     "lines": "10-12",
     "quote": "{ id: \"othello-opening\", title: \"Othello: the opening (unit film)\", file: \"Othello-opening-full.mp4\", vtt: \"Othello-opening-full.vtt\", poster: \"thumbnail-othello-love.jpg\" },"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "261-262",
     "quote": "// its key-word cards say \"Link to deceit\": our links go on them only when that is our centre too"
    },
    {
     "path": "~/Projects/g9/transformer/v02/README.md",
     "lines": "49-50",
     "quote": "- **Fixed in its component:** its apply page labels any scene \"Act 1, Scene 1\", so our exports leave the scene panel"
    }
   ],
   "against": "The ties follow a decision to reuse the existing builds unchanged: \"Their work is used as it is, never rewritten, and nothing is written into their repositories.\" (~/Projects/g9/transformer/DECISIONS.md line 18)",
   "scope_note": "universal",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Settle whether a stimulus belongs with the lesson's text before writing items on it: a writer will draft sound items on the wrong film, and a fit check run only after the items pass may never run.",
   "kind": "measured",
   "found_by": "With one film on file, the picker returned it for any text (it returns null only when there is no film at all). Given the lesson question and the film's captions, the writer drafted three checks on the play's film for the poem and for the speech. On the speech every item-level judgment held and only the fit question failed (p 0.01); on the poem a code check on feedback failed first, so the fit question was never asked.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/films.js",
     "lines": "55-64",
     "quote": "/** The film whose narration shares most words with the text and the question; null if there is none. */"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/0419fc2dc6f6bacf.json",
     "lines": "161",
     "quote": "\"judge\": [],"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/d2d7d0787d6754d9.json",
     "lines": "97",
     "quote": "The film belongs with this text: the judge found this does not hold"
    }
   ],
   "against": "Where it ran, the fit question caught the mismatch at once: \"p\": 0.01 (~/Projects/g9/transformer/runs/blocks/d2d7d0787d6754d9.json line 167).",
   "scope_note": "universal (any block built on a separate stimulus: a film, a picture, a second passage)",
   "adds_to_existing": [
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check a lesson's blocks against each other, not only against earlier blocks of the same kind: blocks of different kinds made from one question converge on its top-ranked line, and one can show the line another asks the student to find.",
   "kind": "measured",
   "found_by": "The engine ranks the lines that bear on the question once per text and tells every block to prefer them; only a second block of the same kind is told what an earlier one covered. On the speech, six ready blocks of six kinds (video essay, direct the line, evidence hunt, claim-evidence-reasoning, compare two answers, quick check) used its top-ranked sentence (p 0.96), and the quick check's feedback on a wrong option quotes the very sentence the evidence hunt keys. On the poem, four ready blocks of four kinds used its top-ranked line (p 0.96); its suggested question, about one detail, had 5 of its 14 lines ranked relevant.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "41",
     "quote": "The lines most relevant to the lesson question are ${top}. Prefer them, but use any line that fits the task."
    },
    {
     "path": "~/Projects/g9/transformer/src/blocks.js",
     "lines": "67",
     "quote": "what the lesson's earlier blocks of this kind cover: those made or being made (a lone QC-3 makes no QC-1 first);"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/9a28237802fccd82.json",
     "lines": "16",
     "quote": "will little note, nor long remember what we say here"
    }
   ],
   "against": "Centring on the key line is intended inside a block, and the focus note allows any line: \"building an argument: the line that matters most, what it shows, and two readings a careful reader could\" (~/Projects/g9/transformer/src/mechanics/video-essay.js line 38); \"Prefer them, but use any line that fits the task.\" (util.js line 41)",
   "scope_note": "universal",
   "adds_to_existing": [
    48,
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a block sets two readings side by side, check that they are rivals a reader must choose between, not only that each can be defended.",
   "kind": "measured",
   "found_by": "The video essay's argument frame is checked only for whether each reading can be defended. On the speech it shipped 'two readings' that are two halves of one claim (one that speech is weak, one that action is powerful; both held, 0.78 and 0.89), and its second question then asked the viewer how the two readings interpret the contrast.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "132-133",
     "quote": "Beat ${k + 1}: the first reading can be defended"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/34c293906aa945a2.json",
     "lines": "41-48",
     "quote": "\"label\": \"Speech Is Weak\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/34c293906aa945a2.json",
     "lines": "54",
     "quote": "We can read this contrast as a statement on the weakness of ceremony, or as a declaration that physical sacrifice permanently eclipses spoken words."
    }
   ],
   "against": "The debate block does check that its two sides differ, but only in wording: \"norm(A.label) !== norm(B.label) && norm(A.counter) !== norm(B.counter)\" (~/Projects/g9/transformer/src/mechanics/debate.js line 72)",
   "scope_note": "universal",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When wrong options or gap answers are taken from the text's own words, check that none means what the key means there: a text that says one thing twice in parallel words makes a second right answer easy to write.",
   "kind": "measured",
   "found_by": "The worked model on the speech rebuilt a sentence whose key was one of two parallel phrases in the same sentence and offered the other as a wrong option; a judge found it did not make the sentence wrong (p 0.31), and the block failed. The key-word deck on the same text drew two near-synonyms from a parallel triple and passed only because each was listed as acceptable in the other's gap, which its rules allow.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/be97f27fc4c4a65a.json",
     "lines": "120",
     "quote": "makes the rebuilt sentence wrong: the judge found this does not hold"
    },
    {
     "path": "~/Projects/learning-truths/research/2026-10-12-6-transformer-ideas/universality-test-gettysburg.txt",
     "lines": "5",
     "quote": "The world will little note, nor long remember what we say here, but it can never forget what they did here."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "3",
     "quote": "another word of the deck that also fits the sentence is not a miss"
    }
   ],
   "against": "none found",
   "scope_note": "universal; most likely in rhetoric and verse built on parallel phrasing",
   "adds_to_existing": [
    31,
    7
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make a check test the property it names, not a sign of it: a check that a push-back quotes the text looked only for quotation marks, and failed push-backs on two texts that used the text's exact words without them.",
   "kind": "measured",
   "found_by": "The debate block's last draft on each text, after a correction pass and a second try, failed on one reason, 'a push-back quotes no words from the text', though each push-back used a run of the text's exact words unmarked (a twelve-word run on the speech); the check counts only spans inside quotation marks. An earlier run held a good paragraph because the quotation check took only quotations of two or more words; it now accepts a single word that is in the text.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "71",
     "quote": "check(\"counters-quote\", \"Each push-back quotes the text\", item.sides.every((s) => quotesIn(s.counter).length > 0), \"a push-back quotes no words from the text\"),"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/aeb043df247f1b45.json",
     "lines": "17",
     "quote": "How can speech matter if the world will little note, nor long remember what we say here?"
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "38-40",
     "quote": "the exact-quotation check only accepted quotations of two or more words"
    }
   ],
   "against": "Quotation marks also tell the student which words are the text's, so the convention matters in itself: \"marks is the text's own words, copied exactly, in double quotes: never put a paraphrase in quotes.\" (~/Projects/g9/transformer/src/mechanics/util.js lines 9-10)",
   "scope_note": "universal",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Repair in code what needs no judgment, such as missing quotation marks round words found verbatim in the text, and send back to the writer only what does.",
   "kind": "measured",
   "found_by": "The debate block's last draft on both texts, after a correction pass and a second try, still failed for missing quotation marks alone and never reached the judge (judgeCalls 0), though code that finds the text's exact words could have marked them. The engine already repairs other mechanical slips in code: a leading verdict, a semicolon or dash for a comma, and paragraph names.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/f23aebacf033daa2.json",
     "lines": "13",
     "quote": "How do the details of a wrinkled lip and sneer of cold command suggest a ruler who also possessed great passion?"
    },
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "2",
     "quote": "judge checks the rest on positive evidence, and a failing draft gets exactly one correction pass with the reasons."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "39",
     "quote": "the reader sees \"Answer A\" and \"Answer B\", so the feedback names them that way (\"paragraph b\" -> \"Answer B\")"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Ask an open check for what the words show, not for the words themselves: when the answer is the text's own words, every hint that points to the place hands it over.",
   "kind": "measured",
   "found_by": "The open check on the poem asked which expressions a carved face shows; the answer was three phrases of one line, and five of its nine hints were flagged as handing the answer over, including all three last rungs, which are meant to quote the words to read again. The block failed. On the speech the open check failed the other way: a judge found the question's own wording gave its answer away (p 0.35 that it did not).",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/d872bc1dfbda65fb.json",
     "lines": "8",
     "quote": "What facial expressions are visible on the broken statue's head?"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "42",
     "quote": "\"third_nudge\": \"the words to read again, quoted exactly, still not the answer\""
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/d872bc1dfbda65fb.json",
     "lines": "87",
     "quote": "a hint uses a word that hands the answer over, or the answer itself:"
    }
   ],
   "against": "The project lets the last hint quote the line by design: \"a hint may quote the text, even the line to\" (~/Projects/g9/transformer/src/mechanics/open-check.js lines 63-64)",
   "scope_note": "universal (open questions on a text)",
   "adds_to_existing": [
    14
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge whether a question gives its answer away from its own wording only, since a judge that knows a famous work will find any answer obvious.",
   "kind": "adopted rule",
   "found_by": "In integration, the open check's give-away question was answered from general knowledge of the play, so its judge question now says to judge only the wording. On a famous speech in the test, the judge so restricted still failed a question whose wording named the dimension of its contrast (0.65 that it gave the answer away).",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "138-140",
     "quote": "its give-away question was answered from general knowledge of Othello (now: the question's"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "86-87",
     "quote": "its own words only: a famous text's answer is known to anyone who knows the work, which is no give-away of the question's"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/b5f74899349e1331.json",
     "lines": "129-133",
     "quote": "\"label\": \"The question does not give its answer away\","
    }
   ],
   "against": "none found",
   "scope_note": "universal; matters most for famous texts",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Ask each block for what every text has, not for one genre's features: a hint told to name who speaks or what moment to look at, on a poem with one speaker, pointed to a sentence by its count instead and got the count wrong.",
   "kind": "measured",
   "found_by": "The evidence hunt's hint is asked to point to who speaks or what moment; on the poem, spoken by one traveller, it said to look 'in the first sentence', but the face it meant is described in the poem's second sentence (the first ends 'Stand in the desert.'). No check reads a hint for truth. Other prompts carry the same play framing: the quick check asks who is speaking or how two characters relate, direct the line asks what an actor could do, and the word-in-focus scale asks whether 'the scene' can be understood.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
     "lines": "28",
     "quote": "- hint: one sentence that points to who speaks or what moment to look at, without quoting the line."
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/963297774d627c12.json",
     "lines": "12",
     "quote": "Look at the description of the face's mouth and expression in the first sentence."
    },
    {
     "path": "~/Projects/g9/transformer/samples/ozymandias.md",
     "lines": "4-5",
     "quote": "Stand in the desert. Near them, on the sand,"
    }
   ],
   "against": "The play-framed blocks were still ready on both new texts, for example direct the line on the speech: \"The judge also picks delivery B, with a clear margin\" (~/Projects/g9/transformer/runs/blocks/e47511c58b5dd64c.json line 93, p 1).",
   "scope_note": "universal",
   "adds_to_existing": [
    14
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give every block that shows feedback the same checks that it names no key and says only what is true: in blocks without them, shipped wrong-option feedback restated the key in other words.",
   "kind": "measured",
   "found_by": "The film blocks check every feedback line in code for naming the answer and with a judge for truth; the quick check has the code check only; word in focus and direct the line have neither. In the test both shipped word-in-focus items had wrong-option feedback echoing the key ('making land sacred' for the key 'make sacred or declare holy'; 'the permanent claim of power in the title' for 'An absolute claim of supreme power...'), and the speech's direct-the-line feedback gave the best delivery's reasoning after a wrong pick.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/a75bd9643fa602d9.json",
     "lines": "33-40",
     "quote": "Examine the sixth line again to consider how the text distinguishes ceremonial speech from making land sacred."
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/e47511c58b5dd64c.json",
     "lines": "15-28",
     "quote": "This delivery wrongly implies that the speaker is proud of the speech rather than deferent to the combatants who struggled on the field."
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "186-188",
     "quote": "- code: no \"beat\", \"cue\", \"caption\" or \"frame\", and no wrong-option feedback that names the answer;"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    14
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Plant a check's faults in the forms a writer actually produces: a line-number check tested only on digits passed thirteen lines in three shipped blocks that pointed by position in words.",
   "kind": "measured",
   "found_by": "The house check matches only 'L' or 'line' followed by digits, its tests plant only those forms, and the house prompt's own examples are 'L12' and 'line 12'. On the new texts the writer kept to the letter and wrote 'the tenth line', 'the sixth line', 'the opening line', 'the final sentence' and 'the first sentence': 13 such lines in three ready blocks (5 in what a student is shown) passed, and 5 more sat in a failed open check. In prose the engine's numbered unit is a sentence, so 'the sixth line' of a speech points at nothing a reader can see.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "46",
     "quote": "const LINE_NUMBER = /\\b(?:L\\d+|lines?\\s+\\d+)/i;"
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "65-66",
     "quote": "assert.equal(houseChecks({ feedback: [\"Look again at line 12.\"] })[0].ok, false);"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/a75bd9643fa602d9.json",
     "lines": "38",
     "quote": "Re-read the sixth line to see what spiritual quality the speaker says cannot be bestowed by speeches alone."
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    1,
    53
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A check that wrong-option feedback does not name the key must catch a key of one or two words: one that waits for a shared run of three words let feedback state a two-word key outright.",
   "kind": "measured",
   "found_by": "The shared check flags wrong-option feedback only when it shares a run of words as long as the whole key and never shorter than three. On the poem's film block it flagged the second question (a three-word key) but passed the first, where the feedback on both wrong options said the play was written 'around 1603', the key ('Around 1603'). The quick check uses the same threshold.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "116",
     "quote": "sharedRun(f, c.options[c.answer]) >= Math.max(3, words(c.options[c.answer]).length)"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/0419fc2dc6f6bacf.json",
     "lines": "15-23",
     "quote": "Listen again to hear that the play was written around 1603."
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/0419fc2dc6f6bacf.json",
     "lines": "146",
     "quote": "question 2, option A: its feedback names the right answer; question 2, option C: its feedback names the right answer"
    }
   ],
   "against": "none found",
   "scope_note": "universal (choice items)",
   "adds_to_existing": [
    14,
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat a check that keeps failing as a finding, not noise: a judge confirmed only one of sixteen wrong options in shipped choice items as tempting, and nothing was held, because that check only advises.",
   "kind": "measured",
   "found_by": "The temptation check was added, advisory, after a first live run shipped a distractor no reader would choose. Across the 9 October proof and the 12 October test, the shipped quick-check and word-in-focus items had 16 wrong options judged for temptation: 1 held (0.6), 4 unclear, 11 judged not tempting (as low as 0.18); every one of those blocks was ready.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "73-76",
     "quote": "label: `Option ${letters[i]} would tempt a reader who skimmed`, required: false,"
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "40-43",
     "quote": "whether each wrong option would tempt a reader who skimmed; on Ozymandias it flagged two distractors as not tempting."
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/5722a3741161394e.json",
     "lines": "202-206",
     "quote": "\"label\": \"Option A would tempt a reader who has not looked closely\","
    }
   ],
   "against": "The temptation judgments are themselves unmeasured: \"bounded questions with the evidence supplied; their precision is not yet measured (v04).\" (~/Projects/g9/transformer/v01/QA.md line 46)",
   "scope_note": "universal (choice items)",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check option lengths across a whole set and in every choice block, not with one ratio in one block: the right option was the longest in 12 of the 18 sets that had a single longest option.",
   "kind": "measured",
   "found_by": "Counted over the 24 three-option sets in the test's 32 records (film and essay checks, word-in-focus candidates, rebuild blanks, deliveries): 18 had a single longest option and in 12 it was the key, where chance gives 6. The only length rule is the quick check's, per item, allowing one option 2.2 times another; a shipped word-in-focus item, in a block with no length rule, had a key of 80 characters beside wrong options of 31 and 38.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "55",
     "quote": "check(\"length-balanced\", \"No option stands out by length\", Math.max(...lens) <= 2.2 * Math.min(...lens), \"one option is much longer than the others\"),"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/5722a3741161394e.json",
     "lines": "48-53",
     "quote": "An absolute claim of supreme power and absolute authority over all other rulers."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "24",
     "quote": "rules them out. Keep the options a similar length."
    }
   ],
   "against": "none found; the counts come from one run with one block of each kind per text",
   "scope_note": "universal (choice items)",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give the scripted players a test-wise guesser who picks the middle or the longest option, since one who picks at random cannot expose a cue in the items.",
   "kind": "measured",
   "found_by": "In the test's shipped blocks the right option was the middle one in 9 of the 10 three-option sets a student is shown (both quick checks, both chosen word-in-focus items, both deliveries, both of the speech's essay checks, one of the poem's rebuild blanks) and never the last; over all 24 sets it was first 8 times, middle 13, last 3. Nothing in the engine or the animated build shuffles options. The scripted guesser picks uniformly at random, so its score cannot show this; a reader always taking the middle option would have been right first time on 9 of 10.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/quality/personas.js",
     "lines": "45-47",
     "quote": "guess: (v, r) => ({ type: \"choose\", index: pick(r, v.active.view.options.length) }),"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/fa497dafbb0eb7c2.json",
     "lines": "14",
     "quote": "\"answer\": 1,"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/e47511c58b5dd64c.json",
     "lines": "23",
     "quote": "\"best\": 1,"
    }
   ],
   "against": "none found",
   "scope_note": "universal (choice items)",
   "adds_to_existing": [
    43,
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A guard written as a list for one text protects no other: pair it with a check that reads each line, and ship a line a student must perform only on that check's positive evidence.",
   "kind": "adopted rule",
   "found_by": "The slur guard's code list is the first play's never-staged lines, read from another build's mirror; on any other text it matches nothing and the guard is a judged question on each line. In the test the list checks passed vacuously on both new texts, and the judged guard held on every line a student works with (0.93 to 0.99).",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs.js",
     "lines": "78-79",
     "quote": "Without the mirror there is none, and the Jev question carries the guard."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "104-106",
     "quote": "ships only on positive evidence that the line is clean."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
     "lines": "3-4",
     "quote": "A student performs the line, so it is never one with a slur in it: never one the 3D build never stages, and only on"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Do examples taken from the first text in a universal prompt pull drafts for other texts toward that text's themes?",
   "kind": "open question",
   "found_by": "The word-web prompt's examples are the first play's theme and its words, and the video essay's example point paraphrases one of its lines; in the test no draft showed the pull, but one run per text cannot rule it out.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "36",
     "quote": "lesson question: an abstract noun a Grade 9 reader knows or can learn (for example deceit, ambition, loyalty, grief)."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "47",
     "quote": "says what the lines show, close to their own words (for example \"He serves only to line his own coat\"), never an"
    }
   ],
   "against": "The poem's web did not take the example theme: \"centre\": \"arrogance\", (~/Projects/g9/transformer/runs/blocks/4e79a689a9ff89da.json line 8)",
   "scope_note": "universal",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Name the reader once and pass that name to every prompt and judge question: a grade typed into each prompt cannot be changed by the setting that claims to change it.",
   "kind": "measured",
   "found_by": "The engine takes a grade into every lesson's context (default 9) and stores it, but no prompt or judge question reads it: 'Grade 9' is written out on 43 lines in 16 source files, from the house prompt to the judge's questions on temptation, need and voice, so a lesson for another grade would still be drafted and judged for this one.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "33",
     "quote": "const ctx = { text, question, grade: input.grade ?? 9, focus: [], avoid: avoid.filter(Boolean) };"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "6",
     "quote": "You write one activity for a Grade 9 English lesson."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "126",
     "quote": "Would a typical Grade 9 reader know what term_${k} means in line_${k} unaided?"
    }
   ],
   "against": "The grade is fixed by decision: \"The mechanics and the animation are for Grade 9 and older readers, and the work lives in\" (~/Projects/g9/transformer/DECISIONS.md lines 20-21)",
   "scope_note": "universal across grades; this engine was scoped to one grade",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Where the key is a judgment call, such as the stronger of two answers or the best way to speak a line, have a judge pick blind from the same material and ship only when it picks the key by a clear margin.",
   "kind": "adopted rule",
   "found_by": "Both blocks built this way were ready on the poem and the speech; the blind pick matched the key at 0.91 and 1 for the delivery and 0.99 and 0.99 for the stronger paragraph.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "1-2",
     "quote": "The judge must choose the same paragraph with a clear margin, so there is one defensible pick."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
     "lines": "1-2",
     "quote": "The judge, reading the same lines around it, must pick the same delivery."
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/e47511c58b5dd64c.json",
     "lines": "93-96",
     "quote": "\"label\": \"The judge also picks delivery B, with a clear margin\","
    }
   ],
   "against": "Judge precision is unmeasured: \"bounded questions with the evidence supplied; their precision is not yet measured (v04).\" (~/Projects/g9/transformer/v01/QA.md line 46)",
   "scope_note": "universal",
   "adds_to_existing": [
    21,
    31
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a judge is unsure, leave out what could mislead and keep what could only be unneeded: an unconfirmed word class or picture is dropped, while a gloss is dropped only when the judge is sure the reader knows the word.",
   "kind": "adopted rule",
   "found_by": "On the poem the glossary kept 7 of its 10 drafted terms, 5 of them ones the judge could not say a reader needs (for example 'read', unclear at 0.41); the speech's worked model showed no word class for a phrase whose class the judge could not confirm (0.5).",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "130-136",
     "quote": "the Grade 3 engine's judgeTerms rule: a drafted word Jev is sure a Grade 9 reader knows unaided is dropped, unless"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "112-115",
     "quote": "a word class is a judgment call on Shakespeare, so it never holds the block, but one Jev did not confirm is not shown"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "146-148",
     "quote": "a painting Jev did not find fitting is left out of the frame (the claims stay)"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When the answer is given after the last try, record the step as given, never as accepted, so a step finished that way is not counted as the student's success.",
   "kind": "adopted rule",
   "found_by": "The 3D build marked a checkpoint secure once two attempts were spent; the export patches it so the step completes but is recorded as given, and the engine's own blocks save a release flag whenever they give the answer.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "366-373",
     "quote": "two tries, then the answer is given and the step completes, but a given answer is not shown as \"Accepted\""
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
     "lines": "98",
     "quote": "done: true, released: true, saved: { released: true }"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    49,
    42
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count spelling only where the word itself is being learned: a taught word recalled into a gap must be spelled right, while a slip in a sentence said back is named and not counted.",
   "kind": "adopted rule",
   "found_by": "Both rules were carried over from the 3D build's marking: the key-word deck treats a near spelling as a miss with a nudge, while the say-it-back task names a slip in a long word and passes it.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "3-4",
     "quote": "gets a nudge, since a taught word is spelled right; the second miss gives the word."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "2-4",
     "quote": "that every key word is there, and a near spelling of a long word is named but not counted as a miss (the 3D build's"
    }
   ],
   "against": "none found",
   "scope_note": "vocabulary recall and repetition tasks",
   "adds_to_existing": [
    25
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write a choice question's stem so it can be answered without its options, since a stem that only works beside them cannot be reused as an open question.",
   "kind": "adopted rule",
   "found_by": "The 3D export asks quick checks open, the right option becoming what a secure answer shows, and skips any stem that only works beside its options.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "33-34",
     "quote": "// a question that only works beside its options (\"Which of these…\") is not asked open"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "145",
     "quote": "skipped.push({ id: b.id, reason: \"its question only works beside its options\" })"
    }
   ],
   "against": "none found",
   "scope_note": "universal (choice items)",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Where a text comes with its own authored notes, use them unchanged and draft none, and let a judge read them but never hold them back.",
   "kind": "adopted rule",
   "found_by": "The glossary block passes a 3D build section's own glossary through as it is; those notes are judged but not required, while every drafted note must be confirmed for its line.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "4-6",
     "quote": "through unchanged, each where its line mark puts it, and nothing is drafted."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "121",
     "quote": "the 3D build's own notes are its content: Jev's reading of them is kept, and never holds them"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Lines that code writes around any text should say only what code can know, such as who speaks or which section comes next, never what the passage means.",
   "kind": "adopted rule",
   "found_by": "The 3D export's guide boxes, written by code for any text, say who speaks in the next section, or to read slowly with the question in mind, and never summarise the content.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "112-114",
     "quote": "Plain lines of ours: who speaks, never the content."
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "119",
     "quote": "return say(who ? `In this ${where}, ${who}.` : `In this ${where}, read slowly, with the question in mind.`);"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check that every frame's text fits by rendering it, since text inside the stated character limits can still overflow.",
   "kind": "adopted rule",
   "found_by": "The video essay accepts a beat only if its fullest state renders on the canvas. On the poem it failed: evidence lines of 44 and 52 characters, inside the prompt's 60-character limit, and argument points of 49 to 55 characters overflowed two display rows; the speech's essay, with lines of 27 to 33 characters and no picture, fit and was made.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/video/frames.js",
     "lines": "1-3",
     "quote": "state renders on the canvas (the host contract's preflight: some text passes the schema yet cannot fit)."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "43",
     "quote": "- \"evidence\": heading (at most 50 characters); claims: two or three, each at most 60 characters, each true to the text;"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/7e771d331c6b4135.json",
     "lines": "120",
     "quote": "Every frame validates and fits its canvas: beat 2: render Evidence line exceeds two display rows | beat 3: render Point exceeds two display rows"
    }
   ],
   "against": "A passing render is not a good layout: \"The quote card leaves a one-word last line, and its underline starts on the\" (~/Projects/g9/transformer/README.md lines 118-119)",
   "scope_note": "video and other rendered media",
   "adds_to_existing": [
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Suggest a lesson question from the text alone, keep it only on a judge's positive evidence that the text answers it, and cache it so the same text always gets the same question.",
   "kind": "adopted rule",
   "found_by": "Both new texts got a usable open question this way, and every block on each was made from it.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/question.js",
     "lines": "1-3",
     "quote": "positive evidence. Cached by text, so the same text is given the same question."
    },
    {
     "path": "~/Projects/learning-truths/research/2026-10-12-6-transformer-ideas/universality-test.json",
     "lines": "2-5",
     "quote": "\"gettysburg\": \"How does the speaker contrast the actions of the soldiers with the words spoken at the dedication?\""
    }
   ],
   "against": "The judge question asks two things at once: \"Can question_${i} be answered from passage alone, and is it worth a Grade 9 lesson of about an hour?\" (~/Projects/g9/transformer/src/question.js line 34); and the poem's suggested question was narrower than the one it came with: \"question\": \"What does the poem suggest about power and time?\" (~/Projects/g9/transformer/samples/index.json line 6)",
   "scope_note": "universal",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Should a check inside a film about a text test the text, or may it test what the film itself argued?",
   "kind": "open question",
   "found_by": "The speech's video essay asked, after its argument frame, how the film's two readings interpret the contrast; the answer lies in the film's own framing, not in the speech, and its checks are asked to be answered by the narration.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/34c293906aa945a2.json",
     "lines": "75",
     "quote": "\"stem\": \"How do the two readings interpret the speaker's contrast?\","
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "55",
     "quote": "Each question is answered by the narration so far."
    }
   ],
   "against": "none found",
   "scope_note": "films and videos made from a text",
   "adds_to_existing": [
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Test every block on texts of each kind it claims to serve, not only the one it was built on: fixtures from one play missed faults that one run on a poem and a speech exposed.",
   "kind": "measured",
   "found_by": "Each block's offline fixture is an item on the first play, and the tests plant that build's forms. The first run of all 16 blocks on a poem and a speech failed 9 of 32 and surfaced holes in shared checks that no fixture had planted: line positions spelled in words, two-word keys named in feedback, quotation marks as the only sign of quoting.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/README.md",
     "lines": "98-99",
     "quote": "`test/fixtures/othello-items.json` and a play in `src/quality/personas.js`."
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "66",
     "quote": "assert.equal(houseChecks({ hint: \"Reread L7 and L8.\" })[0].ok, false);"
    },
    {
     "path": "~/Projects/learning-truths/research/2026-10-12-6-transformer-ideas/universality-test.py",
     "lines": "21",
     "quote": "out[\"blocks\"] = list(ex.map(make, [(k, m) for k in texts for m in mechs]))"
    }
   ],
   "against": "A live proof on two kinds of text did exist for six blocks: \"- A proof on two public-domain texts of different kinds: Othello 1.1 (drama) and Ozymandias (poem).\" (~/Projects/g9/transformer/v01/README.md line 14)",
   "scope_note": "universal",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
   "lines": "65",
   "quote": "assert.equal(houseChecks({ feedback: [\"Look again at line 12.\"] })[0].ok, false);"
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/blocks/0419fc2dc6f6bacf.json",
   "lines": "13",
   "quote": "\"stem\": \"When was Shakespeare's play Othello written?\","
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/blocks/5722a3741161394e.json",
   "lines": "57",
   "quote": "Re-read the tenth line to consider the permanent claim of power in the title."
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/blocks/9a28237802fccd82.json",
   "lines": "16",
   "quote": "will little note, nor long remember what we say here"
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/blocks/be97f27fc4c4a65a.json",
   "lines": "120",
   "quote": "makes the rebuilt sentence wrong: the judge found this does not hold"
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
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
   "lines": "130-131",
   "quote": "the Grade 3 engine's judgeTerms rule: a drafted word Jev is sure a Grade 9 reader knows unaided is dropped, unless"
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/text.js",
   "lines": "1-2",
   "quote": "or a sentence (prose). Stage directions are kept for display but are never evidence."
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/DECISIONS.md",
   "lines": "28-30",
   "quote": "its model: the 3D build's paragraph coach (6.6 s through a second model) became a Jev choice of one next step (0.26 to"
  },
  {
   "truth": 18,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/question.js",
   "lines": "34",
   "quote": "Can question_${i} be answered from passage alone, and is it worth a Grade 9 lesson of about an hour?"
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Projects/g9/art/briefs.json",
   "lines": "186",
   "quote": "with a decorative woodcut border and a small woodcut picture of Venice on the left page"
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/util.js",
   "lines": "132-135",
   "quote": "Words quoted or retold from the text, a character's commands among them, are part of an answer and do not count."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "192-194",
   "quote": "the saved link's first six blocks, all made before the line-number rule, and played them; three cited line numbers."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/README.md",
   "lines": "111",
   "quote": "Calibration has seed sets only: it proves the wiring and measures nothing until people label examples."
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/blocks/a75bd9643fa602d9.json",
   "lines": "39",
   "quote": "This definition correctly reflects the religious sense of declaring a physical place holy."
  }
 ]
}
```
