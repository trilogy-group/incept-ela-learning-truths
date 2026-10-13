# read:blocks-media

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  nono, analyse its ideas and fold them into the research results

## Result

```json
{
 "direction": "blocks-media",
 "coverage": {
  "read": [
   "~/Projects/g9/transformer/src/mechanics/film-check.js",
   "~/Projects/g9/transformer/src/mechanics/video-essay.js",
   "~/Projects/g9/transformer/src/films.js",
   "~/Projects/g9/transformer/src/video/ (art.js, beats.js, frames.js, produce.js)",
   "~/Projects/g9/transformer/src/mechanics/util.js (house prompt, stopChecks, feedbackJudged, quotation checks)",
   "~/Projects/g9/transformer/src/blocks.js, src/transform.js, src/house.js",
   "Parts of ~/Projects/g9/transformer/src/text.js (norm, words, sharedRun), src/providers.js (narrator, wavSeconds), src/core/runtime.js (tick and completion), src/glue/animated.js (film export and lesson order), src/glue/threejs-render.js (grep), src/quality/personas.js (film plays), web/lesson.js (film player), src/mechanics/quick-check.js and word-in-focus.js (grep for the tempting check)",
   "~/Projects/g9/transformer/README.md, DECISIONS.md, v01/README.md, v01/QA.md, v02/README.md, v02/QA.md, v03-v10/README.md",
   "~/Projects/g9/transformer/test/video.test.mjs, test/runtime.test.mjs (oracle), test/fixtures/othello-items.json (film and video-essay fixtures), test/quotes.test.mjs (grep), test/calibration/ (listing)",
   "~/Projects/g9/transformer/vendor/unit-video/artifact-manifest.json",
   "~/Projects/g9/transformer/node_modules/@unit-video/{core,quote-card,evidence-plate,argument-map,annotated-asset,verse-overlay}/README.md; argument-map/src/index.js and quote-card/src/index.js (colour lines only)",
   "~/Projects/g9/transformer/runs/films/ (all five manifest.json; two captions.vtt read in full, all five measured for line length)",
   "~/Projects/g9/transformer/runs/blocks/ (the 16 film-check and video-essay block records)",
   "~/Projects/g9/transformer/runs/decisions/ (judge answers for d2d7d0787d6754d9, 0e36e4f6c770a7b1, 4370894c30725db3, 34c293906aa945a2, bf53179f4d5d0451, 7e771d331c6b4135)",
   "~/Projects/g9/transformer/runs/playtest/*.json (summaries and faults, scanned for film blocks: none)",
   "~/Projects/g9/player/media/Othello-opening-full.vtt",
   "~/Projects/g9/tools/unit-video-essay/README.md, INTEGRATION.md, QA.md, HANDOFF.md"
  ],
  "skipped": [
   "tools/unit-video-essay Python sources and JSON specs (render-essay.py, bind-essay.py, tool.py, spec.schema.json, tool-contract.json, study*.json, tests): pilot code whose checks its README, QA and INTEGRATION docs already state",
   "unit-video module sources beyond the colour lines, their fixtures and the vendored tarballs: the READMEs state the host contract",
   "runs/playtest/*.decisions.jsonl and other run logs: data dumps",
   "media binaries (mp4, jpg, png, wav) and runs/art-cache: not documents",
   "art/briefs.json and the finish-b manifest, the shadow mirrors, the unit-video-modules and othello-unit-video repositories, player/ docs: outside this direction's scope",
   "other mechanics' sources: outside this direction (one grep for the tempting-distractor check only)",
   ".env, key and token files: never opened"
  ],
  "notes": "All paths sit under the user's home folder; no file relied on carries another person's name in its path, so name_bearing_source is false throughout. Project numbers are quoted as written; word counts (59 to 80 words of narration per made film) and caption line lengths (longest line 71 to 160 characters per film) were counted from the files with read-only commands. No calibration seed in test/calibration/ (five files) covers any film or video-essay check, so none of the judged film checks has a measured precision. runs/ is git-ignored local state from 9 and 12 October; some block records there (for example bf53179f4d5d0451, 683479ffa581cd45) were made under older mechanic versions and are kept on disk with keys that predate the current versions. The task forbids writes, so no mgr ledger entry was made from this read-only subagent."
 },
 "candidates": [
  {
   "statement": "A length target set in the writer's prompt is met only if code measures the made thing against it.",
   "kind": "measured",
   "found_by": "The video essay prompt asks for 60 to 100 seconds and the student is told it is a minute of film; the five films made ran 26.2, 33.92, 34.04, 36.76 and 38.04 seconds (durations in ~/Projects/g9/transformer/runs/films/*/manifest.json), with 59 to 80 words of narration each (counted), and no check compares a made film's length with the target.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "37",
     "quote": "TASK: a short video essay (60 to 100 seconds) that opens the lesson: three or four beats, each one frame with narration"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "26",
     "quote": "Watches a minute of film made from the text; it stops at each question, and goes on after the right answer."
    },
    {
     "path": "~/Projects/g9/transformer/runs/films/7fc2d6f7b8e85a6b/manifest.json",
     "lines": "5",
     "quote": "\"duration\": 36.76,"
    }
   ],
   "against": "The narration rule is a ceiling, not a floor: \"Each beat's narration is at most 45 words, the whole at most 180\" (~/Projects/g9/transformer/src/mechanics/video-essay.js line 104).",
   "scope_note": "universal",
   "adds_to_existing": [
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "If each question must matter for the lesson's question, have a judge check that with the lesson question in front of it; asking the writer for it is not enough.",
   "kind": "measured",
   "found_by": "The film block's prompt asks for questions that matter for the lesson question, but its judge's state never includes the lesson question; a ready film block that passed all 25 of its judged checks opened by asking what the student is expected to trace across the unit.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "34",
     "quote": "Each checks one fact or idea the narration has just given that matters for the"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "80",
     "quote": "const state = { passage, film_narration: film.captions.map((c) => c.line).join(\" \"),"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/c36730609689f122.json",
     "lines": "13",
     "quote": "\"stem\": \"What is the student expected to trace across this unit?\","
    }
   ],
   "against": "The video essay's judge does see the lesson question, but only for its two readings: \"Could a careful reader defend left_${k} from passage, as an answer to lesson_question?\" (~/Projects/g9/transformer/src/mechanics/video-essay.js line 132).",
   "scope_note": "universal",
   "adds_to_existing": [
    19,
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A check that wrong-option feedback does not give the answer away must catch short answers: one that needs three shared words in a row never sees a one- or two-word answer.",
   "kind": "measured",
   "found_by": "On a held film block, two wrong-option lines named the two-word keyed answer 'Around 1603' (line 15 of the same record) and the code check flagged only the next question, whose answer had three words; the test that proves the check plants a five-word answer whole.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "116",
     "quote": "sharedRun(f, c.options[c.answer]) >= Math.max(3, words(c.options[c.answer]).length)"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/0419fc2dc6f6bacf.json",
     "lines": "22",
     "quote": "Listen again to hear that the play was written around 1603."
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/0419fc2dc6f6bacf.json",
     "lines": "97",
     "quote": "Wrong-option feedback does not name the answer: question 2, option A: its feedback names the right answer; question 2, option C: its feedback names the right answer"
    }
   ],
   "against": "The same rule needs the whole answer once it is longer than three words, so a line repeating most of a long answer also passes; the planted case repeats it whole: \"`No: the answer is ${right}.`\" (~/Projects/g9/transformer/test/video.test.mjs line 55).",
   "scope_note": "universal",
   "adds_to_existing": [
    14,
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check that every wrong option is the same kind of thing as the answer and believable to a reader who skimmed, because nothing else catches an absurd one.",
   "kind": "measured",
   "found_by": "A first live run found a quick-check distractor no reader would choose, and the advisory check added for it flagged two more on another text; the film blocks have no such check, and three ready film blocks (06ff2f628b44b1fe, 78add75261da1298 and da0b6b23a9525bfa under ~/Projects/g9/transformer/runs/blocks/) offered the military rank 'Ensign' as a wrong option for the name of a literary device.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "41",
     "quote": "a quick-check distractor no reader would choose (\"he hopes to eventually become the Moor\")"
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "43",
     "quote": "whether each wrong option would tempt a reader who skimmed; on Ozymandias it flagged two distractors as not tempting."
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/06ff2f628b44b1fe.json",
     "lines": "45-49",
     "quote": "\"stem\": \"What term describes the situation where the audience knows Iago is lying but Othello does not?\","
    }
   ],
   "against": "Where the check exists it is advisory, so a flagged option still ships: \"id: `tempting-${letters[i]}`, label: `Option ${letters[i]} would tempt a reader who skimmed`, required: false,\" (~/Projects/g9/transformer/src/mechanics/quick-check.js line 74).",
   "scope_note": "universal (choice questions)",
   "adds_to_existing": [
    31
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check every option, the key included, for being well-formed English on its own and different from the other options.",
   "kind": "adopted rule",
   "found_by": "A film block saved as ready had the keyed option 'He says that he is not what he am', a quotation forced into the third person; a judged check that every option is grammatical was added after it, beside the code check that no two options are the same.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "106",
     "quote": "every option is well formed (added after a draft offered \"he is not what he am\"). In the animated build's film"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/683479ffa581cd45.json",
     "lines": "48",
     "quote": "He says that he is not what he am"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "86",
     "quote": "Is every option in options_${k} grammatical, well-formed English?"
    }
   ],
   "against": "Grammar is one judged question over all three options at once (film-check.js line 86), and options count as different once case and punctuation are stripped: \"new Set(c.options.map(norm)).size === 3\" (~/Projects/g9/transformer/src/mechanics/film-check.js line 69).",
   "scope_note": "universal (choice questions)",
   "adds_to_existing": [
    31
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Nothing from how a piece was made may reach the student: no internal label on screen, and no maker's words such as beat, cue, caption or frame in what they read.",
   "kind": "adopted rule",
   "found_by": "A held video-essay draft told the viewer 'The second frame showed...' in all three feedback lines of a question, and a frame review of the pilot film found an internal script label on a student-facing frame; the film blocks now hold any question, option or feedback line that uses those words.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "111-113",
     "quote": "What a viewer reads at a film's stops (the questions, options and feedback) speaks of the film, never of how it is"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/7388ea11514d7e6d.json",
     "lines": "83",
     "quote": "This is incorrect. The second frame showed that Iago compares the loyal servant to an ass."
    },
    {
     "path": "~/Projects/g9/tools/unit-video-essay/QA.md",
     "lines": "15",
     "quote": "Text now draws on a separate transparent overlay, and the internal script label for scene 5 has been removed from the student-facing frame."
    }
   ],
   "against": "The code check knows four words only, \"const MAKING = /\\b(beat|cue|caption|frame)s?\\b/i;\" (~/Projects/g9/transformer/src/mechanics/util.js line 113), and a block saved as ready before the rule still says \"Review the narration of the first beat, which focuses on exploitation rather than learning.\" (~/Projects/g9/transformer/runs/blocks/bf53179f4d5d0451.json line 69).",
   "scope_note": "universal",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Accept words on a frame only after drawing its fullest state at the size it will be shown, because text inside its character limit can still overflow.",
   "kind": "measured",
   "found_by": "A live video-essay draft was held when its frames were drawn: claims of 44 and 52 characters beside a picture (inside the prompt's 60 and the module's 64) and reading points of 49 to 55 characters (inside the module's 70) each exceeded two display rows.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/video/frames.js",
     "lines": "2-3",
     "quote": "state renders on the canvas (the host contract's preflight: some text passes the schema yet cannot fit)."
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/7e771d331c6b4135.json",
     "lines": "120",
     "quote": "Every frame validates and fits its canvas: beat 2: render Evidence line exceeds two display rows | beat 3: render Point exceeds two display rows"
    },
    {
     "path": "~/Projects/g9/transformer/node_modules/@unit-video/core/README.md",
     "lines": "26",
     "quote": "`wrapText` is a soft character-count helper, not a font metric; modules must independently check their own text bounds and layout."
    }
   ],
   "against": "The check draws each part at a nominal length of narration, not its real one: \"const NOMINAL = 10; // seconds of narration a beat is checked at before its real length is known\" (~/Projects/g9/transformer/src/mechanics/video-essay.js line 17).",
   "scope_note": "universal (any generated slide, card or frame with text)",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make a film only from the plan that passed its checks, and draw the checked frames and the filmed ones with the same function, so what was checked is what is shown.",
   "kind": "adopted rule",
   "found_by": "Built into the video essay block: the film is made only once every code and judged check has passed, from the checked item; one function turns each part into the frame modules' props for both the checks and the film; and what is drawn is part of the film's key, so a change to the drawing makes the film again.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/video/beats.js",
     "lines": "1-2",
     "quote": "the film (at the narration's real timing), so what is checked is what is drawn."
    },
    {
     "path": "~/Projects/g9/transformer/src/blocks.js",
     "lines": "85",
     "quote": "// a block that makes something after it is checked (a video essay's film) makes it now, from the checked item only"
    },
    {
     "path": "~/Projects/g9/transformer/src/video/produce.js",
     "lines": "24",
     "quote": "// what is drawn is in the key (each beat's props), so a change to the drawing makes the film again"
    }
   ],
   "against": "The spoken take is made after the checks and used as returned, with no check of its words: \"const { wav } = await narrator.speak(b.narration);\" (~/Projects/g9/transformer/src/video/produce.js line 63).",
   "scope_note": "universal (generated media)",
   "adds_to_existing": [
    39
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Gate a film's questions in the lesson's own logic, where answers are recorded, not in the film or in one player.",
   "kind": "measured",
   "found_by": "While the stops lived in the players, one view played the film straight through with every question listed under it; the engine still completes a film block on a right answer to its last question alone, which is how its own runtime test finishes films (~/Projects/g9/transformer/test/runtime.test.mjs line 19).",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "184-185",
     "quote": "film played straight through with every question listed under it."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "105",
     "quote": "return { correct, feedback: c.feedback[i], done: correct && k === item.checks.length - 1 };"
    },
    {
     "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
     "lines": "46",
     "quote": "The transformer's runtime remains the owner of student answer scoring and mechanic gates; a visual module must not unlock a lesson step or rewrite approved copy."
    }
   ],
   "against": "In the page a student cannot skip, since a seek is pulled back: \"/** Films.tsx UnitFilm, plainly: the film stops at each of its questions, a seek past the next one comes back to it,\" (~/Projects/g9/transformer/web/lesson.js line 378).",
   "scope_note": "universal (media with questions in it)",
   "adds_to_existing": [
    17,
    41
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Settle whether a ready-made film or picture fits the text before drafting anything on it, since a correction pass cannot fix a mismatch the writer did not make.",
   "kind": "measured",
   "found_by": "The only film on the machine was attached to an unrelated text; the judge gave 0.01 to its belonging on each of four drafts (two tries, each a draft and a correction, four records in the same decision log), and every draft was held for it, because the fit was asked only together with the drafted questions.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/d2d7d0787d6754d9.json",
     "lines": "184-187",
     "quote": "\"value\": 0.01,"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/d2d7d0787d6754d9.json",
     "lines": "97",
     "quote": "The film belongs with this text: the judge found this does not hold"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "82",
     "quote": "Is film_narration about the same work as passage, so that it can open a lesson on it?"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Choose a ready-made film for a lesson explicitly, by an id bound to its file's hash, not by the words its narration shares with the text.",
   "kind": "adopted rule",
   "found_by": "The picker returns the film with the most shared words even when none are shared, and it attached the unit film to an unrelated text; the video tool's handoff also warns that a reused id could pair changed media with cached captions and misplace a stop.",
   "evidence": [
    {
     "path": "~/Projects/g9/tools/unit-video-essay/HANDOFF.md",
     "lines": "33",
     "quote": "When a full film is ready for that mechanic, select it explicitly by immutable ID/hash."
    },
    {
     "path": "~/Projects/g9/transformer/src/films.js",
     "lines": "62",
     "quote": "if (!best || shared > best.shared) best = { film: f, shared };"
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/d2d7d0787d6754d9.json",
     "lines": "20",
     "quote": "\"passage\": \"Four score and seven years ago our fathers brought forth on this continent,"
    }
   ],
   "against": "A judge confirms the fit before a block ships, so the wrong pick was held, not shown: \"a text by the words its narration shares with the text and the question; the judge then confirms it fits.\" (~/Projects/g9/transformer/src/films.js line 2).",
   "scope_note": "universal (any stock asset chosen for a lesson)",
   "adds_to_existing": [
    37
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Never loosen a check to let a sample through; a sample that fails it is not yet the thing the check is for.",
   "kind": "adopted rule",
   "found_by": "A 22-second pilot film could not be a checked lesson film: its first and last stops would be 19.88 seconds apart, under the 20-second rule, and the handoff forbids registering it or weakening the rule to fit.",
   "evidence": [
    {
     "path": "~/Projects/g9/tools/unit-video-essay/HANDOFF.md",
     "lines": "31",
     "quote": "Do not register this sample as a checked lesson film or weaken the check rule to fit the sample."
    },
    {
     "path": "~/Projects/g9/tools/unit-video-essay/README.md",
     "lines": "22",
     "quote": "the current 22-second example is too short for the transformer's checked-film rules."
    },
    {
     "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
     "lines": "56",
     "quote": "this 22-second excerpt does not satisfy its check spacing."
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When a judge is unsure about a draft, send it back asking for a version that plainly holds, not for its opposite and not with a bare 'unclear'.",
   "kind": "adopted rule",
   "found_by": "Held video-essay drafts once came back with reasons such as 'the judge found this unclear', and a draft that glossed a word wrongly needed a correction it could act on; the correction now asks the writer to rewrite so the point plainly holds, or to choose another.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "78",
     "quote": "// an unsure judge is not a no: the correction asks for a version that plainly holds, not for its opposite"
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "191",
     "quote": "it now asks for a version that plainly holds; before, it only said \"unclear\"."
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/0e36e4f6c770a7b1.json",
     "lines": "120",
     "quote": "Beat 3: the first reading can be defended: the judge found this unclear"
    }
   ],
   "against": "none found",
   "scope_note": "universal (draft, judge and revise loops)",
   "adds_to_existing": [
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Ask a film's questions only about what both the writer and the judge can check; when only its words are known, ask only about what was said.",
   "kind": "adopted rule",
   "found_by": "The film block's writer and judge get only the film's timed captions, never its pictures, so each question is drafted from the narration and judged against what had been said by its stop.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "3",
     "quote": "The writer drafts the questions from the captions;"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "33-34",
     "quote": "below is known (the pictures are not)."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "11",
     "quote": "const said = (film, upto) => film.captions.filter((c) => c.to <= upto + 0.01).map((c) => c.line).join(\" \");"
    }
   ],
   "against": "For the films the engine makes, the judge reads each frame as text but a painting only by its written subject, never its pixels: \"is offered an image by id and subject only\" (~/Projects/g9/transformer/src/video/art.js line 2).",
   "scope_note": "universal (questions on films, audio or pictures)",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Choose a mark's colour from what it means, never from its order or position.",
   "kind": "adopted rule",
   "found_by": "The style notes for the unit videos say to use red and green to mark meaning, but the engine colours a quotation's marked words red, ochre and green in turn, and its two-readings frame always edges the left reading in red and the right in green, though both readings are meant to be defensible.",
   "evidence": [
    {
     "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
     "lines": "21",
     "quote": "Use red and green to mark the *meaning* of a word or claim, and keep marks and arrows quiet enough that the source remains legible."
    },
    {
     "path": "~/Projects/g9/transformer/src/video/beats.js",
     "lines": "16",
     "quote": "tone: [\"red\", \"ochre\", \"green\"][i % 3]"
    },
    {
     "path": "~/Projects/g9/transformer/node_modules/@unit-video/argument-map/src/index.js",
     "lines": "68",
     "quote": "const accent = left ? '#db796f' : '#8bbf9a';"
    }
   ],
   "against": "The two-column module says its colours are backed by position, labels and a text description: \"Color is reinforced by position, labels, and full `accessibilityText`.\" (~/Projects/g9/transformer/node_modules/@unit-video/argument-map/README.md line 3).",
   "scope_note": "universal (visual media)",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Review what each mark, arrow and reveal implies, not only the words, because placing one says something of its own.",
   "kind": "adopted rule",
   "found_by": "A frame review of the pilot film removed a long crossing arrow and labels placed on the wrong figure; the style notes ask that both the words and what each reveal implies be reviewed, and the quotation card asks that a mark carry its meaning, not just a colour.",
   "evidence": [
    {
     "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
     "lines": "22",
     "quote": "Check the rhythm by watching it at normal speed, then have both the words and what each reveal implies reviewed."
    },
    {
     "path": "~/Projects/g9/tools/unit-video-essay/QA.md",
     "lines": "14",
     "quote": "The earlier long crossing arrow and Roderigo-side placement were removed."
    },
    {
     "path": "~/Projects/g9/transformer/node_modules/@unit-video/quote-card/README.md",
     "lines": "31",
     "quote": "Use `meaning` to describe why a span is marked, not just its color."
    }
   ],
   "against": "The engine's own films have had no such review: \"No lesson has been reviewed by a person or used by a student.\" (~/Projects/g9/transformer/README.md line 120).",
   "scope_note": "universal (visual media)",
   "adds_to_existing": [
    36,
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Pin the fonts and renderer a film is drawn with and review the delivered video at its delivery size, because the same frame can look different on another machine and frames that pass every check can still look wrong.",
   "kind": "adopted rule",
   "found_by": "The frame modules' contract says font rasterisation varies by host and asks for pinned fonts and a review of the actual video; the engine's film manifests record fonts as not packaged, and a look at its frames found a one-word last line and an underline starting on the space before a marked word, which no check caught.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/node_modules/@unit-video/quote-card/README.md",
     "lines": "35",
     "quote": "SVG markup is deterministic for a fixed input and context, but font rasterization can vary by host. Pin fonts and SVG renderer versions in a production render manifest and review the actual video at its delivery size."
    },
    {
     "path": "~/Projects/g9/transformer/runs/films/7fc2d6f7b8e85a6b/manifest.json",
     "lines": "123",
     "quote": "\"fonts\": \"the modules' font stacks as Chrome resolves them on this machine (not packaged)\""
    },
    {
     "path": "~/Projects/g9/transformer/README.md",
     "lines": "117-119",
     "quote": "The quote card leaves a one-word last line, and its underline starts on the"
    }
   ],
   "against": "none found",
   "scope_note": "universal (rendered media)",
   "adds_to_existing": [
    24,
    37
   ],
   "name_bearing_source": false
  },
  {
   "statement": "How to catch wrong-option feedback that gives the answer in other words, which a word-overlap check cannot see and a check of the line's truth does not ask about.",
   "kind": "open question",
   "found_by": "A ready film block's wrong-option line told the viewer that both readings put lasting power on action rather than speech, which is the keyed answer reworded; it passed the overlap check and the judged check that it is true.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/34c293906aa945a2.json",
     "lines": "83",
     "quote": "Re-examine the two readings presented, which both place long term power on the side of physical action rather than speech."
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/34c293906aa945a2.json",
     "lines": "78",
     "quote": "One reading stresses the weakness of speech while the other stresses the power of action"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "128",
     "quote": "Is everything feedback_${k}_${letters[i]} says true to ${upto} and passage?"
    }
   ],
   "against": "Pointing back to what was shown is what the prompt asks for, so the line may count as a hint rather than a give-away: \"wrong option's sends the viewer back to what was said without using the right option's words\" (~/Projects/g9/transformer/src/mechanics/video-essay.js line 54).",
   "scope_note": "universal",
   "adds_to_existing": [
    14
   ],
   "name_bearing_source": false
  },
  {
   "statement": "What a made film must pass before a student sees it: in one engine nothing checks its sound against the script, its length against its target, or how it looks once it is made.",
   "kind": "open question",
   "found_by": "After encoding, the engine's film maker checks only that each frame was drawn; the planned voice pipeline wants every line checked by a transcriber that has not seen the script and by a second recogniser, and the pilot's sound check was a technical mux check only.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/video/produce.js",
     "lines": "87",
     "quote": "throw new Error(`Chrome drew no frame for beat ${k + 1}`);"
    },
    {
     "path": "~/Projects/g9/transformer/v06/README.md",
     "lines": "7-8",
     "quote": "- Voice: lines generated through the TrueFoundry route, each checked by a transcriber that has not seen the script"
    },
    {
     "path": "~/Projects/g9/tools/unit-video-essay/QA.md",
     "lines": "9",
     "quote": "This is a technical mux check, not a listening review."
    }
   ],
   "against": "The engine's test does compare an encoded film with its manifest, with a silent stand-in narrator: \"assert.ok(Math.abs(Number(probe.format.duration) - m.duration) < 0.3,\" (~/Projects/g9/transformer/test/video.test.mjs line 70).",
   "scope_note": "universal (generated media)",
   "adds_to_existing": [
    11,
    24,
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "What a film should show while it waits for an answer, since stopping just after a part's narration leaves that part's fullest frame, often with the answer, on screen.",
   "kind": "open question",
   "found_by": "Made films stop 0.3 seconds after a part's narration, inside its 0.8-second tail, where its last frame holds; in one film the first question, keyed to 'To serve his own turn upon him' (~/Projects/g9/transformer/runs/blocks/bf53179f4d5d0451.json line 62), was asked over the quotation it paraphrases.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/video/produce.js",
     "lines": "110",
     "quote": "at: +(beats[c.after].start + LEAD + beats[c.after].audio_seconds + 0.3).toFixed(2)"
    },
    {
     "path": "~/Projects/g9/transformer/src/video/produce.js",
     "lines": "88",
     "quote": "hold: +((states[j + 1] ?? b.duration) - s).toFixed(3)"
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/bf53179f4d5d0451.json",
     "lines": "13",
     "quote": "\"quote\": \"I follow him to serve my turn upon him\","
    }
   ],
   "against": "The questions are meant to be answered from what was just said and shown, so the frame repeats what the viewer has just met: \"Each question is answered by the narration so far.\" (~/Projects/g9/transformer/src/mechanics/video-essay.js line 55).",
   "scope_note": "films and slides with questions in them",
   "adds_to_existing": [
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Time every reveal and caption from when the voice actually says the words, using an aligned take, not by spreading them evenly or by sentence length.",
   "kind": "adopted rule",
   "found_by": "The pilot bound 14 animation cues to 62 aligned words of a measured take and checked each cue's word and time; the engine's films instead spread each part's reveals evenly over its narration and time captions by each sentence's share of characters.",
   "evidence": [
    {
     "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
     "lines": "20",
     "quote": "Let measured speech times drive the cue IDs. Edit the visual sequence to the voice before adding motion."
    },
    {
     "path": "~/Projects/g9/transformer/src/video/beats.js",
     "lines": "2-3",
     "quote": "element appears in step with the voice, spread across the narration that follows the beat's lead-in."
    },
    {
     "path": "~/Projects/g9/transformer/src/video/produce.js",
     "lines": "43",
     "quote": "/** Captions for one beat: its narration's sentences, timed by their share of its length. */"
    }
   ],
   "against": "Alignment proves timing, not that the take says the script: \"matched alignment flags are not such proof.\" (~/Projects/g9/tools/unit-video-essay/INTEGRATION.md line 44).",
   "scope_note": "narrated media",
   "adds_to_existing": [
    15,
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check captions in code against the script: they must put it back together exactly, keep each line short (one pilot held every line to 42 characters), and end within the narration.",
   "kind": "measured",
   "found_by": "The pilot's captions were checked to reassemble to the script exactly, with no line over 42 characters and the last ending inside the narration; the engine's own films put whole sentences in single cues, the longest line in each film running 71 to 160 characters (counted from the five captions.vtt files).",
   "evidence": [
    {
     "path": "~/Projects/g9/tools/unit-video-essay/QA.md",
     "lines": "10",
     "quote": "has 10 cues, no line longer than 42 characters, and reassembles to the source script exactly."
    },
    {
     "path": "~/Projects/g9/transformer/runs/films/7fc2d6f7b8e85a6b/captions.vtt",
     "lines": "13",
     "quote": "This division allows us to read Iago either as a pragmatist seeking material wealth or as a deeper strategist whose primary goal is absolute self-determination."
    }
   ],
   "against": "Short lines split sentences across cues, and the unit film's captions end mid-sentence, so a stop placed after a caption still needs its own sentence-end check: \"in love with his wife, Desdemona,\" (~/Projects/g9/player/media/Othello-opening-full.vtt line 27).",
   "scope_note": "captioned media",
   "adds_to_existing": [
    10,
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Bind each marked word in a quotation to its exact place, and refuse a word that occurs more than once rather than guess which one is meant.",
   "kind": "adopted rule",
   "found_by": "The quotation-card module binds each mark to a code-point range with the exact text expected, so either occurrence of a repeated word can be targeted, and its notes on the older pilot, which highlighted the first matching substring, say to reject ambiguous repeated words; the engine's own binder still takes the first whole-word match.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/node_modules/@unit-video/quote-card/README.md",
     "lines": "37",
     "quote": "It should reject ambiguous repeated words instead of guessing an occurrence."
    },
    {
     "path": "~/Projects/g9/transformer/node_modules/@unit-video/quote-card/README.md",
     "lines": "31",
     "quote": "`expectedText` must exactly match the selected range; editing the quote without rebinding the mark fails validation."
    },
    {
     "path": "~/Projects/g9/transformer/src/video/frames.js",
     "lines": "37",
     "quote": "/** Unicode code-point offsets of a word in a quotation, as the quote card wants them; null if it is not there whole. */"
    }
   ],
   "against": "The engine marks a repeated word at its first occurrence without warning: \"const m = re.exec(q);\" (~/Projects/g9/transformer/src/video/frames.js line 42).",
   "scope_note": "annotated quotations in any subject",
   "adds_to_existing": [
    13
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Space a film's questions out: in one engine no two stops may come less than 20 seconds apart or after neighbouring parts.",
   "kind": "adopted rule",
   "found_by": "Both film blocks enforce spacing in code; with three parts the rule leaves one legal placement, so all five films made stop after their first and last parts, and the second question comes in each film's last half-second (stops and durations in ~/Projects/g9/transformer/runs/films/*/manifest.json).",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "70",
     "quote": "check(\"spaced\", \"Stops at least 20 seconds apart\", gaps.every((g) => g >= 20), \"two stops are less than 20 seconds apart\"),"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "105",
     "quote": "check(\"checks-apart\", \"The checks follow different beats, not one after the other\","
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "174",
     "quote": "Film `7fc2d6f7b8e85a6b`: 36.8 s, stops at 10.82 s and 36.26 s."
    }
   ],
   "against": "No source gives a reason for 20 seconds; the video tool's handoff only restates it: \"That mechanic requires two to four stops spaced at least 20 seconds apart\" (~/Projects/g9/tools/unit-video-essay/HANDOFF.md line 31).",
   "scope_note": "films with questions in them; the 20-second figure is this engine's own",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Hold narration that sets out readings to saying nothing the text contradicts, not to being true, because a reading poses a question that is neither true nor false.",
   "kind": "adopted rule",
   "found_by": "Narration offering two readings could not be confirmed as true to the text (0.57, under the 0.6 gate) and held its block; for such parts the judged check became whether the text contradicts anything said.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "123",
     "quote": "// two readings pose a question, which is neither true nor false: there, nothing said may go against the passage"
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "177",
     "quote": "an argument beat's narration that was not \"true\": it now has only to say nothing the text goes against;"
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/4370894c30725db3.json",
     "lines": "834-837",
     "quote": "\"value\": 0.57,"
    }
   ],
   "against": "Narration that states what the text says is still held to being true: \"Is everything narration_${k} says true to passage?\" (~/Projects/g9/transformer/src/mechanics/video-essay.js line 126).",
   "scope_note": "interpretive subjects (literature, history, the arts)",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "State each side of an interpretation close to the text's own words, never as an abstraction the text does not state.",
   "kind": "adopted rule",
   "found_by": "A reading built on abstractions ('Pragmatic Survival', 'material well-being') got 0.52 on whether a careful reader could defend it from the passage (~/Projects/g9/transformer/runs/decisions/0e36e4f6c770a7b1.json line 334) and held its block, while the other reading passed at 0.91; the prompt then asked for points close to the lines' own words.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "46-48",
     "quote": "says what the lines show, close to their own words (for example \"He serves only to line his own coat\"), never an"
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "178",
     "quote": "a reading Jev could not defend from the lines: points now keep close to the lines' own words;"
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/0e36e4f6c770a7b1.json",
     "lines": "29",
     "quote": "\"left_2\": \"Pragmatic Survival: He protects himself from being discarded; He secures his own material well-being\","
    }
   ],
   "against": "Each reading is judged alone, so nothing checks that the two differ: \"Could a careful reader defend right_${k} from passage, as an answer to lesson_question?\" (~/Projects/g9/transformer/src/mechanics/video-essay.js line 133).",
   "scope_note": "interpretive subjects",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "How to check that two readings set side by side are two readings and not one said twice, when each is checked only for being defensible.",
   "kind": "open question",
   "found_by": "A ready film's two readings were 'Speech Is Weak' and 'Action Is Powerful', each judged defensible (0.78 and 0.89 in ~/Projects/g9/transformer/runs/decisions/34c293906aa945a2.json), and the block's own feedback said both put lasting power on action rather than speech.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/34c293906aa945a2.json",
     "lines": "83",
     "quote": "Re-examine the two readings presented, which both place long term power on the side of physical action rather than speech."
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/34c293906aa945a2.json",
     "lines": "41",
     "quote": "\"label\": \"Speech Is Weak\","
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "132",
     "quote": "Could a careful reader defend left_${k} from passage, as an answer to lesson_question?"
    }
   ],
   "against": "In other films the two readings did differ: \"This division allows us to read Iago either as a pragmatist seeking material wealth or as a deeper strategist whose primary goal is absolute self-determination.\" (~/Projects/g9/transformer/runs/films/7fc2d6f7b8e85a6b/manifest.json line 34).",
   "scope_note": "interpretive subjects",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Build a short explanatory film as an argument with one visible claim at a time, paced by the voice: the key line quoted exactly first, then what it shows, then two readings a careful reader could defend.",
   "kind": "adopted rule",
   "found_by": "Taken from frames sampled from a reference unit video and adopted as the video essay's structure; the block checks in code that it opens on an exact quotation.",
   "evidence": [
    {
     "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
     "lines": "14",
     "quote": "The repeatable pattern is **one visible claim at a time, paced by voice**."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "38",
     "quote": "read over it, building an argument: the line that matters most, what it shows, and two readings a careful reader could"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "100",
     "quote": "check(\"opens-with-quote\", \"The first beat is a quotation\""
    }
   ],
   "against": "It is \"a design inference from the sampled motifs\" (~/Projects/g9/tools/unit-video-essay/INTEGRATION.md line 14), drawn from \"A 144-frame storyboard sampled at about 4.9-second intervals\" (same file, line 3); nothing measures what students learn from it.",
   "scope_note": "short explanatory films on a text",
   "adds_to_existing": [
    15
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't let a held picture stand in for a performance, because replacing a performed passage with a still changes what the passage is.",
   "kind": "adopted rule",
   "found_by": "The reference unit video includes a long passage of a performer speaking; the pilot and the engine use paintings as stand-ins, and the engine leaves its verse-over-footage frame unused until approved footage exists.",
   "evidence": [
    {
     "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
     "lines": "19",
     "quote": "The sampled reference includes a long speaking-performer passage; replacing that passage with a held painting would change its character."
    },
    {
     "path": "~/Projects/g9/transformer/README.md",
     "lines": "117-118",
     "quote": "and verse-overlay needs approved footage."
    },
    {
     "path": "~/Projects/g9/tools/unit-video-essay/README.md",
     "lines": "22",
     "quote": "The example uses G9 paintings as stand-ins and has no performer footage."
    }
   ],
   "against": "It is a design inference from sampled frames, not a measured effect: \"That is a design inference from the sampled motifs.\" (~/Projects/g9/tools/unit-video-essay/INTEGRATION.md line 14).",
   "scope_note": "drama and other performed texts",
   "adds_to_existing": [],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
   "lines": "40",
   "quote": "A successful render is technical proof only, not academic approval."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/QA.md",
   "lines": "19",
   "quote": "The generated voice and assembled scene have **not** been heard or approved by a human reviewer, academically signed off, or tested with students."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/video/produce.js",
   "lines": "110",
   "quote": "const stops = plan.checks.map((c) => ({ after: c.after, at: +(beats[c.after].start + LEAD + beats[c.after].audio_seconds + 0.3).toFixed(2) }));"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
   "lines": "36",
   "quote": "- cue: the number of the caption whose words answer it (the film stops right after that caption)."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/g9/player/media/Othello-opening-full.vtt",
   "lines": "26-27",
   "quote": "in love with his wife, Desdemona,"
  },
  {
   "truth": 9,
   "effect": "counter",
   "path": "~/Projects/g9/player/media/Othello-opening-full.vtt",
   "lines": "64",
   "quote": "Knowledge first. Then the reading."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/video/produce.js",
   "lines": "108",
   "quote": "const captions = beats.flatMap((b) => captionsFor(b.narration, b.start + LEAD, b.audio_seconds));"
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v06/README.md",
   "lines": "7-8",
   "quote": "- Voice: lines generated through the TrueFoundry route, each checked by a transcriber that has not seen the script"
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
   "lines": "38",
   "quote": "It does **not** independently recognize the spoken WAV, check educational accuracy, guarantee fit on every font/platform, or provide reduced-motion behavior."
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/README.md",
   "lines": "117",
   "quote": "- The video essay uses three of the six frame modules: annotated-asset needs arrow positions read from the picture,"
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/annotated-asset/README.md",
   "lines": "43",
   "quote": "The host should still render a review frame at its target size and check text placement before publishing a video."
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
   "lines": "25",
   "quote": "// the film's own words may be quoted (houseChecks: a quotation is the text's, the item's own, or one of these)"
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/QA.md",
   "lines": "16",
   "quote": "The Shakespeare quotations and Act/Scene labels match"
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "188",
   "quote": "Jev, one question a line: every line is true to what the film has said (and shown) by its stop, and to the text."
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "190",
   "quote": "Film with checks was made again under these checks: ready, with all 9 lines confirmed."
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
   "lines": "38-39",
   "quote": "what was just said, without naming the answer; say only what the film has said by then)."
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
   "lines": "14",
   "quote": "The repeatable pattern is **one visible claim at a time, paced by voice**."
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "181-183",
   "quote": "the right one gets \"Keep watching\", and a seek past an open question is pulled"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "184-185",
   "quote": "film played straight through with every question listed under it."
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/video/beats.js",
   "lines": "35",
   "quote": "/** What a frame shows, as text: for the judge to check the narration against it. */"
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/providers.js",
   "lines": "71-72",
   "quote": "The text goes alone, with no style instruction (a 3.8 voice read its instruction aloud, 6 Oct)."
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "164",
   "quote": "narration per beat: Gacrux on gemini-3.1-flash-tts-preview through the TrueFoundry route, with no style instruction;"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/core/README.md",
   "lines": "24",
   "quote": "Visual descriptions still need editorial review."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/README.md",
   "lines": "22",
   "quote": "The generated narration has machine checks but no human listening or academic sign-off."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/INTEGRATION.md",
   "lines": "44",
   "quote": "The generated voice has **not** received human listening or curriculum sign-off; matched alignment flags are not such proof."
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/video/produce.js",
   "lines": "66",
   "quote": "takes.push({ file: f, seconds: wavSeconds(wav), sha256: sha(wav) });"
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/QA.md",
   "lines": "8",
   "quote": "`ffprobe` reports 22.125 seconds for the container versus 22.120 seconds for the source WAV."
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/films.js",
   "lines": "35",
   "quote": "duration: captions.at(-1)?.to ?? 0"
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "103",
   "quote": "the v07 Othello film (2:54, timed captions)"
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/QA.md",
   "lines": "15",
   "quote": "At 09.80 seconds the evidence plate contains no ghosted future lines."
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "105",
   "quote": "question is answered by what has been said by its stop, that the keyed option is right, the others wrong, and that"
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/README.md",
   "lines": "111",
   "quote": "- Calibration has seed sets only: it proves the wiring and measures nothing until people label examples."
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
   "lines": "49",
   "quote": "Every beat has narration: one or two sentences, at most 40 words, saying what its frame shows."
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
   "lines": "127",
   "quote": "Does narration_${k} talk about what frame_${k} shows?"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/video/art.js",
   "lines": "1-3",
   "quote": "// is offered an image by id and subject only; its bytes are checked against the finish's manifest before every use, and"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/evidence-plate/README.md",
   "lines": "3",
   "quote": "The source note records provenance but does not establish reuse rights."
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/g9/tools/unit-video-essay/README.md",
   "lines": "20",
   "quote": "Validation refuses changed input bytes and overlong text; verification rejects changed output bytes."
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/core/README.md",
   "lines": "32",
   "quote": "The host should pin package versions and record installed package and font hashes for reproducible renders."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/core/README.md",
   "lines": "26",
   "quote": "Use `motion: 'reduced'` for the same information without fades, pans, or fast motion."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/argument-map/README.md",
   "lines": "3",
   "quote": "Color is reinforced by position, labels, and full `accessibilityText`."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/evidence-plate/README.md",
   "lines": "18",
   "quote": "The returned `accessibilityText` includes every line regardless of animation time so the host can expose the full meaning to assistive technology."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "192-193",
   "quote": "A block made before a rule changed is not drawn, whatever key a client sends."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/video/produce.js",
   "lines": "24",
   "quote": "// what is drawn is in the key (each beat's props), so a change to the drawing makes the film again"
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/evidence-plate/README.md",
   "lines": "20",
   "quote": "Split longer copy into another beat."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/node_modules/@unit-video/quote-card/README.md",
   "lines": "33",
   "quote": "use a progressive verse or evidence module for longer passages."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
   "lines": "22",
   "quote": "// what this block is about, so a second block of the same kind on the same text is told to differ"
  },
  {
   "truth": 49,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
   "lines": "21",
   "quote": "Watches the film; it stops at each question, and goes on after the right answer."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
   "lines": "146",
   "quote": "// a painting Jev did not find fitting is left out of the frame (the claims stay)"
  },
  {
   "truth": 54,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "180",
   "quote": "\"follow\" glossed as loyal: the writer now gets a correction it can act on, below."
  },
  {
   "truth": 54,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
   "lines": "128",
   "quote": "In frame_${k}, is what is said of \"${a.word}\" true of that word in the quotation?"
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
   "lines": "60",
   "quote": "PAINTINGS (id: subject), for evidence beats:"
  }
 ]
}
```
