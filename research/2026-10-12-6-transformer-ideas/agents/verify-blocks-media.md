# verify:blocks-media

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  nono, analyse its ideas and fold them into the research results

## Result

```json
{
 "direction": "blocks-media",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (video-essay.js lines 37 and 104, manifests line 5). The five durations (26.2, 33.92, 34.04, 36.76, 38.04 s) and the 59 to 80 words of narration match the manifests. 'Met only if code measures it' turns one missed target into a law, so the statement now says what was measured. The 'a minute of film' line (line 26) is the mechanic's description of what the student does, served in the mechanics list (src/mechanics/index.js line 38), not text a student is shown. The writers used 59 to 80 words where three or four beats of up to 40 allowed 120 to 160: the prompt gives a ceiling and no floor. Adds to 26; overlaps candidate 18 here.",
   "statement": "Measure what was made against its length target in code: a prompt asked for films of 60 to 100 seconds, and the five made ran 26.2 to 38.04 seconds with nothing comparing them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "37",
     "quote": "TASK: a short video essay (60 to 100 seconds) that opens the lesson: three or four beats, each one frame with narration",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/films/a2189e24065794e4/manifest.json",
     "lines": "5",
     "quote": "\"duration\": 26.2,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/films/f13d567b87dac256/manifest.json",
     "lines": "5",
     "quote": "\"duration\": 38.04,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "104",
     "quote": "Each beat's narration is at most 45 words, the whole at most 180",
     "verbatim": true
    }
   ],
   "against": "The code check on narration is a ceiling with no floor (video-essay.js line 104), and the only length comparison anywhere is the test's, between an encoded film and its own manifest, with a silent stand-in narrator: \"assert.ok(Math.abs(Number(probe.format.duration) - m.duration) < 0.3,\" (~/Projects/g9/transformer/test/video.test.mjs line 70).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep",
   "reason": "Quotes verbatim (film-check.js lines 34 and 80; block c36730609689f122 line 13, status ready, 25 judged checks all holding: one fit check and eight per question). The film block's judge state holds the passage, the narration, what was said by each stop, the questions, options, keys and feedback, never the lesson question, and no check asks whether a question bears on it. One case, but the gap is in the code. Applies 19 and adds that a requirement given only to the writer goes unchecked.",
   "statement": "If each question must matter for the lesson's question, have a judge check that with the lesson question in front of it; asking the writer for it is not enough.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "34",
     "quote": "Each checks one fact or idea the narration has just given that matters for the",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "80",
     "quote": "const state = { passage, film_narration: film.captions.map((c) => c.line).join(\" \"),",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/c36730609689f122.json",
     "lines": "13",
     "quote": "\"stem\": \"What is the student expected to trace across this unit?\",",
     "verbatim": true
    }
   ],
   "against": "The video essay's judge does see the lesson question, but only for its two readings: \"Could a careful reader defend left_${k} from passage, as an answer to lesson_question?\" (~/Projects/g9/transformer/src/mechanics/video-essay.js line 132).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep",
   "reason": "Quotes verbatim. sharedRun (text.js lines 68-78) returns the longest run of shared words, at most two for a one- or two-word answer, under the floor of three, so such an answer can never be flagged: two wrong-option lines naming 'Around 1603' passed while the three-word 'The Ottoman Empire' was caught (block 0419fc2dc6f6bacf, held). The test plants 'To serve his own turn', five words, whole (test/video.test.mjs line 55; fixture test/fixtures/othello-items.json). Adds to 1 and 14.",
   "statement": "A check that wrong-option feedback does not give the answer away must catch short answers: one that needs three shared words in a row never sees a one- or two-word answer.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "116",
     "quote": "sharedRun(f, c.options[c.answer]) >= Math.max(3, words(c.options[c.answer]).length)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/text.js",
     "lines": "68",
     "quote": "Longest run of consecutive words two strings share (a give-away measure).",
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
     "lines": "97",
     "quote": "Wrong-option feedback does not name the answer: question 2, option A: its feedback names the right answer; question 2, option C: its feedback names the right answer",
     "verbatim": true
    }
   ],
   "against": "The same rule needs the whole answer once it is three words or longer, so a line repeating most of a long answer also passes; the planted case repeats it whole: \"`No: the answer is ${right}.`\" (~/Projects/g9/transformer/test/video.test.mjs line 55).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep",
   "reason": "Quotes verbatim (v01/QA.md lines 41 and 43). Three ready film blocks (06ff2f628b44b1fe, 78add75261da1298, da0b6b23a9525bfa) offer 'Ensign' among names for a dramatic device, and one block's own feedback calls it a military rank rather than a literary device (line 54, added). Film blocks check only that each wrong option is wrong; quick-check's tempting check is advisory. No statement on record covers the kind or plausibility of wrong options (31 covers each option's correctness).",
   "statement": "Check that every wrong option is the same kind of thing as the answer and believable to a reader who skimmed, because nothing else catches an absurd one.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "41",
     "quote": "a quick-check distractor no reader would choose (\"he hopes to eventually become the Moor\")",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "43",
     "quote": "whether each wrong option would tempt a reader who skimmed; on Ozymandias it flagged two distractors as not tempting.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/06ff2f628b44b1fe.json",
     "lines": "45",
     "quote": "\"stem\": \"What term describes the situation where the audience knows Iago is lying but Othello does not?\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/06ff2f628b44b1fe.json",
     "lines": "54",
     "quote": "The film defines an ensign as the officer who carries the flag, which is a military rank rather than a literary device.",
     "verbatim": true
    }
   ],
   "against": "Where the check exists it is advisory, so a flagged option still ships: \"id: `tempting-${letters[i]}`, label: `Option ${letters[i]} would tempt a reader who skimmed`, required: false,\" (~/Projects/g9/transformer/src/mechanics/quick-check.js line 74).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep",
   "reason": "Quotes verbatim. 683479ffa581cd45 is ready, made at 11:11 on 9 October, before the grammar check that v02/QA.md line 106 records. The check is one judged question over all three options; distinctness is equality after normalising, in code. Holds as an adopted rule for choice questions.",
   "statement": "Check every option, the key included, for being well-formed English on its own and different from the other options.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "106",
     "quote": "every option is well formed (added after a draft offered \"he is not what he am\"). In the animated build's film",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/683479ffa581cd45.json",
     "lines": "48",
     "quote": "He says that he is not what he am",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "86",
     "quote": "Is every option in options_${k} grammatical, well-formed English?",
     "verbatim": true
    }
   ],
   "against": "Grammar is one judged question over all three options at once (film-check.js line 86), and options count as different once case and punctuation are stripped: \"new Set(c.options.map(norm)).size === 3\" (~/Projects/g9/transformer/src/mechanics/film-check.js line 69).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep",
   "reason": "Quotes verbatim (util.js line 111; block 7388ea11514d7e6d line 83, held, with 'The second frame showed' in all three lines 83 to 85; pilot QA line 15). The against is right: the check knows four words, and a ready block made before the rule still says 'the first beat'.",
   "statement": "Nothing from how a piece was made may reach the student: no internal label on screen, and no maker's words such as beat, cue, caption or frame in what they read.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "111",
     "quote": "What a viewer reads at a film's stops (the questions, options and feedback) speaks of the film, never of how it is",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/7388ea11514d7e6d.json",
     "lines": "83",
     "quote": "This is incorrect. The second frame showed that Iago compares the loyal servant to an ass.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/tools/unit-video-essay/QA.md",
     "lines": "15",
     "quote": "Text now draws on a separate transparent overlay, and the internal script label for scene 5 has been removed from the student-facing frame.",
     "verbatim": true
    }
   ],
   "against": "The code check knows four words only, \"const MAKING = /\\b(beat|cue|caption|frame)s?\\b/i;\" (~/Projects/g9/transformer/src/mechanics/util.js line 113), and a block saved as ready before the rule still says \"Review the narration of the first beat, which focuses on exploitation rather than learning.\" (~/Projects/g9/transformer/runs/blocks/bf53179f4d5d0451.json line 69).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep",
   "reason": "Quotes verbatim. Numbers match block 7e771d331c6b4135: claims of 44 and 52 characters beside a painting (prompt 60, evidence plate 64) and points of 49, 51, 53 and 55 characters (argument map 70) each broke the two-row layout at 1280x720; three of the four points were also over the prompt's own 50, which the engine does not enforce. Added the module's own render check.",
   "statement": "Accept words on a frame only after drawing its fullest state at the size it will be shown, because text inside its character limit can still overflow.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/video/frames.js",
     "lines": "3",
     "quote": "state renders on the canvas (the host contract's preflight: some text passes the schema yet cannot fit).",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/7e771d331c6b4135.json",
     "lines": "120",
     "quote": "Every frame validates and fits its canvas: beat 2: render Evidence line exceeds two display rows | beat 3: render Point exceeds two display rows",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/node_modules/@unit-video/core/README.md",
     "lines": "26",
     "quote": "`wrapText` is a soft character-count helper, not a font metric; modules must independently check their own text bounds and layout.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/node_modules/@unit-video/argument-map/src/index.js",
     "lines": "61",
     "quote": "throw new RangeError('Point exceeds two display rows');",
     "verbatim": true
    }
   ],
   "against": "The check draws each part at a nominal length of narration, not its real one: \"const NOMINAL = 10; // seconds of narration a beat is checked at before its real length is known\" (~/Projects/g9/transformer/src/mechanics/video-essay.js line 17).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep",
   "reason": "Quotes verbatim (beats.js line 2; blocks.js line 85; produce.js line 24). The checks draw each frame's fullest state at a nominal 10 seconds of narration and the film at the take's real length, through the same beatProps. The against is right: the take is made after the checks and its words are never checked.",
   "statement": "Make a film only from the plan that passed its checks, and draw the checked frames and the filmed ones with the same function, so what was checked is what is shown.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/video/beats.js",
     "lines": "2",
     "quote": "the film (at the narration's real timing), so what is checked is what is drawn.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/blocks.js",
     "lines": "85",
     "quote": "// a block that makes something after it is checked (a video essay's film) makes it now, from the checked item only",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/video/produce.js",
     "lines": "24",
     "quote": "// what is drawn is in the key (each beat's props), so a change to the drawing makes the film again",
     "verbatim": true
    }
   ],
   "against": "The spoken take is made after the checks and used as returned, with no check of its words: \"const { wav } = await narrator.speak(b.narration);\" (~/Projects/g9/transformer/src/video/produce.js line 63).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep",
   "reason": "Quotes verbatim. respond() marks a film block done on a right answer to its last question whatever happened to the earlier ones (film-check.js line 105), the runtime completes the entity on done (src/core/runtime.js lines 86-87), and the runtime test's oracle finishes film blocks that way (test/runtime.test.mjs line 19, added). The page's player does gate (web/lesson.js line 378), so the gap is in the logic, not the page. Adds where the gate must live to 17 and 41.",
   "statement": "Gate a film's questions in the lesson's own logic, where answers are recorded, not in the film or in one player.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "185",
     "quote": "film played straight through with every question listed under it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "105",
     "quote": "return { correct, feedback: c.feedback[i], done: correct && k === item.checks.length - 1 };",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
     "lines": "46",
     "quote": "The transformer's runtime remains the owner of student answer scoring and mechanic gates; a visual module must not unlock a lesson step or rewrite approved copy.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/runtime.test.mjs",
     "lines": "19",
     "quote": "if (type === \"film-check\") return { type: \"choose\", check: item.checks.length - 1, index: item.checks.at(-1).answer };",
     "verbatim": true
    }
   ],
   "against": "In the page a student cannot skip, since a seek is pulled back: \"/** Films.tsx UnitFilm, plainly: the film stops at each of its questions, a seek past the next one comes back to it,\" (~/Projects/g9/transformer/web/lesson.js line 378).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; all four judge records in the decision log (two tries, each a draft and a correction) give film_fits 0.01, and the block was held on it. Fit is asked only beside the drafted questions (film-check.js line 82), so the corrections were spent on a film no rewrite could change. 'Or picture' went beyond the evidence: a video essay's painting is the writer's own pick and is dropped when not confirmed, so the statement is narrowed to an asset the writer did not choose. Same incident as candidate 10.",
   "statement": "Settle whether a ready-made film, or any asset the writer did not choose, fits the text before drafting on it: a correction pass cannot fix a mismatch the writer did not make.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/d2d7d0787d6754d9.json",
     "lines": "187",
     "quote": "\"value\": 0.01,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/d2d7d0787d6754d9.json",
     "lines": "97",
     "quote": "The film belongs with this text: the judge found this does not hold",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "82",
     "quote": "Is film_narration about the same work as passage, so that it can open a lesson on it?",
     "verbatim": true
    }
   ],
   "against": "The judge held the block, so no student saw the mismatch; the cost was four drafts and their judge calls: \"a text by the words its narration shares with the text and the question; the judge then confirms it fits.\" (~/Projects/g9/transformer/src/films.js line 2).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep",
   "reason": "Quotes verbatim. films.js line 62 takes the first film when nothing has been picked yet, so a film sharing no words is still chosen, and with one film listed every text gets it: both texts in the universality test (a poem and a speech) got the Othello unit film. The handoff's warning that a reused ID could pair changed media with cached captions is on line 33 too (added). Adds to 37.",
   "statement": "Choose a ready-made film for a lesson explicitly, by an id bound to its file's hash, not by the words its narration shares with the text.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/tools/unit-video-essay/HANDOFF.md",
     "lines": "33",
     "quote": "When a full film is ready for that mechanic, select it explicitly by immutable ID/hash.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/tools/unit-video-essay/HANDOFF.md",
     "lines": "33",
     "quote": "Reusing an ID for changed media could serve stale captions and misplace a stop.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/films.js",
     "lines": "62",
     "quote": "if (!best || shared > best.shared) best = { film: f, shared };",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/d2d7d0787d6754d9.json",
     "lines": "20",
     "quote": "\"passage\": \"Four score and seven years ago our fathers brought forth on this continent,",
     "verbatim": true
    }
   ],
   "against": "A judge confirms the fit before a block ships, so the wrong pick was held, not shown: \"a text by the words its narration shares with the text and the question; the judge then confirms it fits.\" (~/Projects/g9/transformer/src/films.js line 2).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 2.28 and 22.16 seconds, 19.88 apart, match HANDOFF.md line 31. 'Never' softened: the engine itself rewrote a check after drafts failed it, because the check was wrong for that kind of beat (v02/QA.md line 177). The rule is against loosening a check for one sample, not against ever revising a check.",
   "statement": "Don't loosen a check to let a sample through: a sample that fails it is not yet the thing the check is for.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/tools/unit-video-essay/HANDOFF.md",
     "lines": "31",
     "quote": "Do not register this sample as a checked lesson film or weaken the check rule to fit the sample.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/tools/unit-video-essay/HANDOFF.md",
     "lines": "31",
     "quote": "Its first and last caption-derived stops would be 2.28 and 22.16 seconds, only 19.88 seconds apart",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
     "lines": "56",
     "quote": "this 22-second excerpt does not satisfy its check spacing.",
     "verbatim": true
    }
   ],
   "against": "A check that is wrong for a whole kind of content does get changed: \"an argument beat's narration that was not \"true\": it now has only to say nothing the text goes against;\" (~/Projects/g9/transformer/v02/QA.md line 177). And no source gives a reason for the 20-second spacing the sample failed: \"That mechanic requires two to four stops spaced at least 20 seconds apart\" (~/Projects/g9/tools/unit-video-essay/HANDOFF.md line 31).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep",
   "reason": "Quotes verbatim (transform.js line 78; v02/QA.md line 191; block 0e36e4f6c770a7b1 line 120, held on a 0.52 'unclear' with the old wording). The correction now reads 'the judge could not confirm this; rewrite it so that it plainly holds, or choose another' (transform.js line 79, added). Adds the correction step to 50.",
   "statement": "When a judge is unsure about a draft, send it back asking for a version that plainly holds, not for its opposite and not with a bare 'unclear'.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "78",
     "quote": "// an unsure judge is not a no: the correction asks for a version that plainly holds, not for its opposite",
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
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/0e36e4f6c770a7b1.json",
     "lines": "120",
     "quote": "Beat 3: the first reading can be defended: the judge found this unclear",
     "verbatim": true
    }
   ],
   "against": "none found; no run compares redrafts made under the old and the new wording.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (film-check.js lines 3, 34 and 11). Reworded only: the writer drafts, it does not check. This is the other side of 18: when the judge cannot be given what the student sees, narrow the questions to what it is given.",
   "statement": "Ask a film's questions only about what the writer and the judge are both given: when they have only its words, ask only about what was said.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "3",
     "quote": "The writer drafts the questions from the captions;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "34",
     "quote": "below is known (the pictures are not).",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "11",
     "quote": "const said = (film, upto) => film.captions.filter((c) => c.to <= upto + 0.01).map((c) => c.line).join(\" \");",
     "verbatim": true
    }
   ],
   "against": "For the films the engine makes, the judge reads each frame as text but a painting only by its written subject, never its pixels: \"is offered an image by id and subject only\" (~/Projects/g9/transformer/src/video/art.js line 2).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (INTEGRATION.md line 21; beats.js line 16). A quotation's marks take red, ochre and green by index, whatever each word does (in the speech's film 'say' is red and 'did' ochre). The 'never by position' half went too far: the reference's argument map and the module colour by column on purpose, and that red on one of two defensible readings reads as the wrong one is not measured, so it moves to against. Swapped the argument-map colour line for the quote card's own rule on meaning. Distinct from 38.",
   "statement": "Choose a mark's colour for what the mark means, not by its order in a list: one engine coloured a quotation's marked words red, ochre and green in turn, whatever each word did.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
     "lines": "21",
     "quote": "Use red and green to mark the *meaning* of a word or claim, and keep marks and arrows quiet enough that the source remains legible.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/video/beats.js",
     "lines": "16",
     "quote": "tone: [\"red\", \"ochre\", \"green\"][i % 3]",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/node_modules/@unit-video/quote-card/README.md",
     "lines": "31",
     "quote": "Use `meaning` to describe why a span is marked, not just its color.",
     "verbatim": true
    }
   ],
   "against": "Colouring by column is the reference's design and the module's: \"A two-column red/green argument map.\" (~/Projects/g9/tools/unit-video-essay/INTEGRATION.md line 12), \"The left and right columns have stable semantic colors\" (~/Projects/g9/transformer/node_modules/@unit-video/argument-map/README.md line 3), and the engine's first reading always gets the red edge, \"const accent = left ? '#db796f' : '#8bbf9a';\" (~/Projects/g9/transformer/node_modules/@unit-video/argument-map/src/index.js line 68); whether that reads as a verdict on it is not measured.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep",
   "reason": "Quotes verbatim (INTEGRATION.md line 22; pilot QA line 14; quote-card README line 31). Holds as an adopted rule from the style notes and the pilot's frame review; the engine's own films have had no such review. Adds to 36 and 24.",
   "statement": "Review what each mark, arrow and reveal implies, not only the words, because placing one says something of its own.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
     "lines": "22",
     "quote": "Check the rhythm by watching it at normal speed, then have both the words and what each reveal implies reviewed.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/tools/unit-video-essay/QA.md",
     "lines": "14",
     "quote": "The earlier long crossing arrow and Roderigo-side placement were removed.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/node_modules/@unit-video/quote-card/README.md",
     "lines": "31",
     "quote": "Use `meaning` to describe why a span is marked, not just its color.",
     "verbatim": true
    }
   ],
   "against": "The engine's own films have had no such review: \"No lesson has been reviewed by a person or used by a student.\" (~/Projects/g9/transformer/README.md line 120).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "keep",
   "reason": "Quotes verbatim (quote-card README line 35; manifest line 123; README line 118). Both flaws passed every check, the render preflight included (v02/QA.md lines 198-199). Adds render provenance to 37 and the look-at-it step to 24.",
   "statement": "Pin the fonts and renderer a film is drawn with and review the delivered video at its delivery size, because the same frame can look different on another machine and frames that pass every check can still look wrong.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/node_modules/@unit-video/quote-card/README.md",
     "lines": "35",
     "quote": "SVG markup is deterministic for a fixed input and context, but font rasterization can vary by host. Pin fonts and SVG renderer versions in a production render manifest and review the actual video at its delivery size.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/films/7fc2d6f7b8e85a6b/manifest.json",
     "lines": "123",
     "quote": "\"fonts\": \"the modules' font stacks as Chrome resolves them on this machine (not packaged)\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/README.md",
     "lines": "118",
     "quote": "The quote card leaves a one-word last line, and its underline starts on the",
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
   "verdict": "keep",
   "reason": "Quotes verbatim (34c293906aa945a2 lines 83 and 78; util.js line 128). The block is ready: the judged truth check on that line held at 0.82 and the code overlap check passed. The line tells a viewer who picked the first option that both readings put lasting power on action rather than speech, which is the keyed option in other words. The open question stands; it complements candidate 2.",
   "statement": "How to catch wrong-option feedback that gives the answer in other words, which a word-overlap check cannot see and a check of the line's truth does not ask about.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/34c293906aa945a2.json",
     "lines": "83",
     "quote": "Re-examine the two readings presented, which both place long term power on the side of physical action rather than speech.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/34c293906aa945a2.json",
     "lines": "78",
     "quote": "One reading stresses the weakness of speech while the other stresses the power of action",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "128",
     "quote": "Is everything feedback_${k}_${letters[i]} says true to ${upto} and passage?",
     "verbatim": true
    }
   ],
   "against": "Pointing back to what was shown is what the prompt asks for, so the line may count as a hint rather than a give-away: \"wrong option's sends the viewer back to what was said without using the right option's words\" (~/Projects/g9/transformer/src/mechanics/video-essay.js line 54).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep",
   "reason": "Quotes verbatim (produce.js line 87; v06/README.md line 7; pilot QA line 9). Correction to how it was found: the frame check runs while frames are drawn, before encoding; after encoding nothing is checked. The v06 voice check is a plan, not built. Also, the listed unit film's length is its captions' last cue (src/films.js line 35, 172.19 s) while ffprobe gives the file 174.54 s. Overlaps candidate 0; touches 11, 24 and 26.",
   "statement": "What a made film must pass before a student sees it: in one engine nothing checks its sound against the script, its length against its target, or how it looks once it is made.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/video/produce.js",
     "lines": "87",
     "quote": "throw new Error(`Chrome drew no frame for beat ${k + 1}`);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v06/README.md",
     "lines": "7",
     "quote": "- Voice: lines generated through the TrueFoundry route, each checked by a transcriber that has not seen the script",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/tools/unit-video-essay/QA.md",
     "lines": "9",
     "quote": "This is a technical mux check, not a listening review.",
     "verbatim": true
    }
   ],
   "against": "The engine's test does compare an encoded film with its manifest, with a silent stand-in narrator: \"assert.ok(Math.abs(Number(probe.format.duration) - m.duration) < 0.3,\" (~/Projects/g9/transformer/test/video.test.mjs line 70).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep",
   "reason": "Quotes verbatim (produce.js line 110; beats.js line 7, added; bf53179f4d5d0451 lines 13 and 62). A lead of 0.4 s and a tail of 0.8 s put each stop 0.5 s before its part ends, on the part's last frame, which produce.js line 88 holds; in film cd48a45d510f4e3e the first stop at 9.46 s shows 'I follow him to serve my turn upon him' while asking for 'To serve his own turn upon him'. A case of 29 in the engine's own films, kept for that evidence and for the open part: what to show at a stop when 8 puts the question right after the part that answers it.",
   "statement": "What a film should show while it waits for an answer, since stopping just after a part's narration leaves that part's fullest frame, often with the answer, on screen.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/video/produce.js",
     "lines": "110",
     "quote": "at: +(beats[c.after].start + LEAD + beats[c.after].audio_seconds + 0.3).toFixed(2)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/video/beats.js",
     "lines": "7",
     "quote": "export const LEAD = 0.4, TAIL = 0.8;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/bf53179f4d5d0451.json",
     "lines": "13",
     "quote": "\"quote\": \"I follow him to serve my turn upon him\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/bf53179f4d5d0451.json",
     "lines": "62",
     "quote": "\"To serve his own turn upon him\",",
     "verbatim": true
    }
   ],
   "against": "The questions are meant to be answered from what was just said and shown, so the frame repeats what the viewer has just met: \"Each question is answered by the narration so far.\" (~/Projects/g9/transformer/src/mechanics/video-essay.js line 55).",
   "general": true,
   "duplicate_of": "29",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep",
   "reason": "Quotes verbatim (INTEGRATION.md line 20; beats.js line 3; produce.js line 43). The pilot bound 14 cues to 62 aligned words (pilot README line 18); the engine spreads cues evenly (beats.js line 9) and times captions by characters (produce.js lines 46-48). The module contract expects aligned times as well (core README line 26, added). No harm from the even spread is recorded, so this is an adopted rule. Adds the method to 15 and 26.",
   "statement": "Time every reveal and caption from when the voice actually says the words, using an aligned take, not by spreading them evenly or by sentence length.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
     "lines": "20",
     "quote": "Let measured speech times drive the cue IDs. Edit the visual sequence to the voice before adding motion.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/video/beats.js",
     "lines": "3",
     "quote": "element appears in step with the voice, spread across the narration that follows the beat's lead-in.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/video/produce.js",
     "lines": "43",
     "quote": "/** Captions for one beat: its narration's sentences, timed by their share of its length. */",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/node_modules/@unit-video/core/README.md",
     "lines": "26",
     "quote": "The host maps word-alignment cues to these relative times.",
     "verbatim": true
    }
   ],
   "against": "Alignment proves timing, not that the take says the script: \"matched alignment flags are not such proof.\" (~/Projects/g9/tools/unit-video-essay/INTEGRATION.md line 44).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "keep",
   "reason": "Quotes verbatim. The QA's 10 cues and 42 characters match; the engine's longest caption lines are 148, 160, 71, 151 and 122 characters, one sentence a cue (counted from the five captions.vtt files). Added the pilot's code, which makes 'in code' true: reassembly raises an error (render-essay.py line 656) and line length is held by wrapping at 42 (line 652). Adds to 10.",
   "statement": "Check captions in code against the script: they must put it back together exactly, keep each line short (one pilot held every line to 42 characters), and end within the narration.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/tools/unit-video-essay/QA.md",
     "lines": "10",
     "quote": "has 10 cues, no line longer than 42 characters, and reassembles to the source script exactly.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/tools/unit-video-essay/render-essay.py",
     "lines": "656",
     "quote": "raise RuntimeError(\"caption text differs from aligned script\")",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/tools/unit-video-essay/render-essay.py",
     "lines": "652",
     "quote": "textwrap.wrap(phrase, width=42, break_long_words=False, break_on_hyphens=False)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/films/7fc2d6f7b8e85a6b/captions.vtt",
     "lines": "13",
     "quote": "This division allows us to read Iago either as a pragmatist seeking material wealth or as a deeper strategist whose primary goal is absolute self-determination.",
     "verbatim": true
    }
   ],
   "against": "Short lines split sentences across cues, and the unit film's captions end mid-sentence, so a stop placed after a caption still needs its own sentence-end check: \"in love with his wife, Desdemona,\" (~/Projects/g9/player/media/Othello-opening-full.vtt line 27).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep",
   "reason": "Quotes verbatim (quote-card README lines 37 and 31; frames.js lines 37 and 42). wordSpan returns the first case-insensitive whole-word match. No run here marked a repeated word, so this is an adopted rule, not a measured fault. Adds to 13.",
   "statement": "Bind each marked word in a quotation to its exact place, and refuse a word that occurs more than once rather than guess which one is meant.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/node_modules/@unit-video/quote-card/README.md",
     "lines": "37",
     "quote": "It should reject ambiguous repeated words instead of guessing an occurrence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/node_modules/@unit-video/quote-card/README.md",
     "lines": "31",
     "quote": "`expectedText` must exactly match the selected range; editing the quote without rebinding the mark fails validation.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/video/frames.js",
     "lines": "37",
     "quote": "/** Unicode code-point offsets of a word in a quotation, as the quote card wants them; null if it is not there whole. */",
     "verbatim": true
    }
   ],
   "against": "The engine marks a repeated word at its first occurrence without warning: \"const m = re.exec(q);\" (~/Projects/g9/transformer/src/video/frames.js line 42).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim and numbers match, but the statement merged two rules: the film-check block needs stops 20 seconds apart (line 70), the video essay needs its questions after parts that are not neighbours (line 105), and neither block has both. No source gives a reason for either. What was measured is the consequence: with three parts the video essay's rule leaves one placement, so all five films stopped after their first and last parts, the second stop 0.5 s before the end and none after the middle part. Engine-specific, hence general false.",
   "statement": "Space a film's questions apart, and check where the rule leaves them: one engine's rule that two questions follow parts not next to each other left its three-part films one placement, after the first and last parts, with the second question in the last half-second.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "105",
     "quote": "check(\"checks-apart\", \"The checks follow different beats, not one after the other\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "174",
     "quote": "Film `7fc2d6f7b8e85a6b`: 36.8 s, stops at 10.82 s and 36.26 s.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "70",
     "quote": "check(\"spaced\", \"Stops at least 20 seconds apart\", gaps.every((g) => g >= 20), \"two stops are less than 20 seconds apart\"),",
     "verbatim": true
    }
   ],
   "against": "No source gives a reason for either rule; the video tool's handoff only restates the first: \"That mechanic requires two to four stops spaced at least 20 seconds apart\" (~/Projects/g9/tools/unit-video-essay/HANDOFF.md line 31). A four-part film would leave three placements.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 0.57 at decisions line 837 is under the 0.6 'top' gate (grade3-reading engine, src/decide/questions.js line 5), and the same block's earlier draft scored 0.61. Added the second half, which the engine does (video-essay.js lines 132-133) and without which 'nothing contradicted' is a weak bar.",
   "statement": "Hold narration that sets out two readings to saying nothing the text contradicts, not to being true, and check each reading on its own for whether it can be defended from the text: a reading poses a question, which is neither true nor false.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "123",
     "quote": "// two readings pose a question, which is neither true nor false: there, nothing said may go against the passage",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "177",
     "quote": "an argument beat's narration that was not \"true\": it now has only to say nothing the text goes against;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/4370894c30725db3.json",
     "lines": "837",
     "quote": "\"value\": 0.57,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "132",
     "quote": "Could a careful reader defend left_${k} from passage, as an answer to lesson_question?",
     "verbatim": true
    }
   ],
   "against": "Narration that states what the text says is still held to being true: \"Is everything narration_${k} says true to passage?\" (~/Projects/g9/transformer/src/mechanics/video-essay.js line 126).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 25,
   "verdict": "keep",
   "reason": "Quotes verbatim (video-essay.js line 47; v02/QA.md line 178; decisions 0e36e4f6c770a7b1 line 29, 0.52 at line 334, the other reading 0.91). Caveat: the passing reading's label ('Malicious Deception') was as abstract as the held one's; the difference was in the points, which is what the rule names. The record states the change after a held draft, not a before-and-after measurement.",
   "statement": "State each side of an interpretation close to the text's own words, never as an abstraction the text does not state.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "47",
     "quote": "says what the lines show, close to their own words (for example \"He serves only to line his own coat\"), never an",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "178",
     "quote": "a reading Jev could not defend from the lines: points now keep close to the lines' own words;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/0e36e4f6c770a7b1.json",
     "lines": "29",
     "quote": "\"left_2\": \"Pragmatic Survival: He protects himself from being discarded; He secures his own material well-being\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/0e36e4f6c770a7b1.json",
     "lines": "334",
     "quote": "\"value\": 0.52,",
     "verbatim": true
    }
   ],
   "against": "Each reading is judged alone, so nothing checks that the two differ: \"Could a careful reader defend right_${k} from passage, as an answer to lesson_question?\" (~/Projects/g9/transformer/src/mechanics/video-essay.js line 133).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "keep",
   "reason": "Quotes verbatim (34c293906aa945a2 lines 83 and 41; video-essay.js line 132). A ready block; the readings scored 0.78 and 0.89 in its decision log, each judged alone, with nothing comparing them. The open question stands; it pairs with candidates 24 and 25.",
   "statement": "How to check that two readings set side by side are two readings and not one said twice, when each is checked only for being defensible.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/34c293906aa945a2.json",
     "lines": "83",
     "quote": "Re-examine the two readings presented, which both place long term power on the side of physical action rather than speech.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/34c293906aa945a2.json",
     "lines": "41",
     "quote": "\"label\": \"Speech Is Weak\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "132",
     "quote": "Could a careful reader defend left_${k} from passage, as an answer to lesson_question?",
     "verbatim": true
    }
   ],
   "against": "In other films the two readings did differ: \"This division allows us to read Iago either as a pragmatist seeking material wealth or as a deeper strategist whose primary goal is absolute self-determination.\" (~/Projects/g9/transformer/runs/films/7fc2d6f7b8e85a6b/manifest.json line 34).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep",
   "reason": "Quotes verbatim (INTEGRATION.md line 14; video-essay.js lines 38 and 100). A design adopted from 144 sampled frames of a reference, which its own source calls a design inference; nothing measures its effect on learning. Adds to 15.",
   "statement": "Build a short explanatory film as an argument with one visible claim at a time, paced by the voice: the key line quoted exactly first, then what it shows, then two readings a careful reader could defend.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
     "lines": "14",
     "quote": "The repeatable pattern is **one visible claim at a time, paced by voice**.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "38",
     "quote": "read over it, building an argument: the line that matters most, what it shows, and two readings a careful reader could",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "100",
     "quote": "check(\"opens-with-quote\", \"The first beat is a quotation\"",
     "verbatim": true
    }
   ],
   "against": "It is \"a design inference from the sampled motifs\" (~/Projects/g9/tools/unit-video-essay/INTEGRATION.md line 14), drawn from \"A 144-frame storyboard sampled at about 4.9-second intervals\" (same file, line 3); nothing measures what students learn from it.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep",
   "reason": "Quotes verbatim (INTEGRATION.md line 19; README.md line 118; pilot README line 22). An adopted rule from the style research, itself an inference from sampled frames; scoped to performed texts.",
   "statement": "Don't let a held picture stand in for a performance, because replacing a performed passage with a still changes what the passage is.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
     "lines": "19",
     "quote": "The sampled reference includes a long speaking-performer passage; replacing that passage with a held painting would change its character.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/README.md",
     "lines": "118",
     "quote": "and verse-overlay needs approved footage.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/tools/unit-video-essay/README.md",
     "lines": "22",
     "quote": "The example uses G9 paintings as stand-ins and has no performer footage.",
     "verbatim": true
    }
   ],
   "against": "It is a design inference from sampled frames, not a measured effect: \"That is a design inference from the sampled motifs.\" (~/Projects/g9/tools/unit-video-essay/INTEGRATION.md line 14).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
   "lines": "40",
   "quote": "A successful render is technical proof only, not academic approval.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/QA.md",
   "lines": "19",
   "quote": "The generated voice and assembled scene have **not** been heard or approved by a human reviewer, academically signed off, or tested with students.",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/video/produce.js",
   "lines": "110",
   "quote": "const stops = plan.checks.map((c) => ({ after: c.after, at: +(beats[c.after].start + LEAD + beats[c.after].audio_seconds + 0.3).toFixed(2) }));",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
   "lines": "36",
   "quote": "- cue: the number of the caption whose words answer it (the film stops right after that caption).",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/g9/player/media/Othello-opening-full.vtt",
   "lines": "27",
   "quote": "in love with his wife, Desdemona,",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "counter",
   "path": "~/Projects/g9/player/media/Othello-opening-full.vtt",
   "lines": "64",
   "quote": "Knowledge first. Then the reading.",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/video/produce.js",
   "lines": "108",
   "quote": "const captions = beats.flatMap((b) => captionsFor(b.narration, b.start + LEAD, b.audio_seconds));",
   "ok": true
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v06/README.md",
   "lines": "7",
   "quote": "- Voice: lines generated through the TrueFoundry route, each checked by a transcriber that has not seen the script",
   "ok": true
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
   "lines": "38",
   "quote": "It does **not** independently recognize the spoken WAV, check educational accuracy, guarantee fit on every font/platform, or provide reduced-motion behavior.",
   "ok": true
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/README.md",
   "lines": "117",
   "quote": "- The video essay uses three of the six frame modules: annotated-asset needs arrow positions read from the picture,",
   "ok": false
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/annotated-asset/README.md",
   "lines": "43",
   "quote": "The host should still render a review frame at its target size and check text placement before publishing a video.",
   "ok": true
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
   "lines": "25",
   "quote": "// the film's own words may be quoted (houseChecks: a quotation is the text's, the item's own, or one of these)",
   "ok": true
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/QA.md",
   "lines": "16",
   "quote": "The Shakespeare quotations and Act/Scene labels match",
   "ok": true
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "188",
   "quote": "Jev, one question a line: every line is true to what the film has said (and shown) by its stop, and to the text.",
   "ok": true
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "190",
   "quote": "Film with checks was made again under these checks: ready, with all 9 lines confirmed.",
   "ok": true
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
   "lines": "39",
   "quote": "what was just said, without naming the answer; say only what the film has said by then).",
   "ok": true
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
   "lines": "14",
   "quote": "The repeatable pattern is **one visible claim at a time, paced by voice**.",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "182",
   "quote": "the right one gets \"Keep watching\", and a seek past an open question is pulled",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "185",
   "quote": "film played straight through with every question listed under it.",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/video/beats.js",
   "lines": "35",
   "quote": "/** What a frame shows, as text: for the judge to check the narration against it. */",
   "ok": true
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/providers.js",
   "lines": "72",
   "quote": "The text goes alone, with no style instruction (a 3.8 voice read its instruction aloud, 6 Oct).",
   "ok": true
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "164",
   "quote": "narration per beat: Gacrux on gemini-3.1-flash-tts-preview through the TrueFoundry route, with no style instruction;",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/core/README.md",
   "lines": "24",
   "quote": "Visual descriptions still need editorial review.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/README.md",
   "lines": "22",
   "quote": "The generated narration has machine checks but no human listening or academic sign-off.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
   "lines": "44",
   "quote": "The generated voice has **not** received human listening or curriculum sign-off; matched alignment flags are not such proof.",
   "ok": true
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/video/produce.js",
   "lines": "66",
   "quote": "takes.push({ file: f, seconds: wavSeconds(wav), sha256: sha(wav) });",
   "ok": true
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/QA.md",
   "lines": "8",
   "quote": "`ffprobe` reports 22.125 seconds for the container versus 22.120 seconds for the source WAV.",
   "ok": true
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/films.js",
   "lines": "35",
   "quote": "duration: captions.at(-1)?.to ?? 0",
   "ok": false
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "103",
   "quote": "the v07 Othello film (2:54, timed captions)",
   "ok": false
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/QA.md",
   "lines": "15",
   "quote": "At 09.80 seconds the evidence plate contains no ghosted future lines.",
   "ok": false
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "105",
   "quote": "question is answered by what has been said by its stop, that the keyed option is right, the others wrong, and that",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/README.md",
   "lines": "111",
   "quote": "- Calibration has seed sets only: it proves the wiring and measures nothing until people label examples.",
   "ok": true
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
   "lines": "49",
   "quote": "Every beat has narration: one or two sentences, at most 40 words, saying what its frame shows.",
   "ok": true
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
   "lines": "127",
   "quote": "Does narration_${k} talk about what frame_${k} shows?",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/video/art.js",
   "lines": "2",
   "quote": "// is offered an image by id and subject only; its bytes are checked against the finish's manifest before every use, and",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/evidence-plate/README.md",
   "lines": "3",
   "quote": "The source note records provenance but does not establish reuse rights.",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/README.md",
   "lines": "20",
   "quote": "Validation refuses changed input bytes and overlong text; verification rejects changed output bytes.",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/core/README.md",
   "lines": "32",
   "quote": "The host should pin package versions and record installed package and font hashes for reproducible renders.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/core/README.md",
   "lines": "26",
   "quote": "Use `motion: 'reduced'` for the same information without fades, pans, or fast motion.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/argument-map/README.md",
   "lines": "3",
   "quote": "Color is reinforced by position, labels, and full `accessibilityText`.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/evidence-plate/README.md",
   "lines": "18",
   "quote": "The returned `accessibilityText` includes every line regardless of animation time so the host can expose the full meaning to assistive technology.",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "193",
   "quote": "A block made before a rule changed is not drawn, whatever key a client sends.",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/video/produce.js",
   "lines": "24",
   "quote": "// what is drawn is in the key (each beat's props), so a change to the drawing makes the film again",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/evidence-plate/README.md",
   "lines": "20",
   "quote": "Split longer copy into another beat.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/quote-card/README.md",
   "lines": "33",
   "quote": "use a progressive verse or evidence module for longer passages.",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
   "lines": "22",
   "quote": "// what this block is about, so a second block of the same kind on the same text is told to differ",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
   "lines": "21",
   "quote": "Watches the film; it stops at each question, and goes on after the right answer.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
   "lines": "146",
   "quote": "// a painting Jev did not find fitting is left out of the frame (the claims stay)",
   "ok": true
  },
  {
   "truth": 54,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "180",
   "quote": "\"follow\" glossed as loyal: the writer now gets a correction it can act on, below.",
   "ok": true
  },
  {
   "truth": 54,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
   "lines": "128",
   "quote": "In frame_${k}, is what is said of \"${a.word}\" true of that word in the quotation?",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
   "lines": "60",
   "quote": "PAINTINGS (id: subject), for evidence beats:",
   "ok": true
  }
 ]
}
```
