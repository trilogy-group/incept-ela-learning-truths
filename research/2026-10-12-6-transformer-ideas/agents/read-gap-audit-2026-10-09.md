# read:gap:audit-2026-10-09

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  nono, analyse its ideas and fold them into the research results

## Result

```json
{
 "direction": "audit-2026-10-09",
 "coverage": {
  "read": [
   "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json: the ranked object only (answers 3, plan 16, dropped 8, quickWins 6)",
   "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json: review.summary, review.ruleBreaks (13), review.failures (empty), and notDone for all 4 reports (fixes, kinds, threejs, quality)",
   "~/Projects/g9/transformer/v02/QA.md lines 100-150, checked line by line against 110-143",
   "~/Projects/g9/transformer/src: blocks.js, judge.js, house.js, transform.js, core/runtime.js and the mechanics quick-check, open-check, key-words, say-it-back, debate, word-web, word-in-focus, direct-the-line, compare-paragraphs, util and index, read in full; engine.js (head); server.js (render, playtest and play routes); learning-question, glossary and worked-model (headers and judge checks); glue/animated-judge.js and glue/threejs.js in full; glue/threejs-archivist.js lines 1-240; glue/threejs-render.js lines 360-380 plus greps; glue/animated.js (greps); quality/personas.js (PLAY), quality/playtest.js (header), quality/calibrate.js lines 1-140",
   "~/Projects/g9/transformer/web/lesson.js: text pane, options(), hunt(), the word and direct cards, the web chip",
   "~/Projects/g9/transformer/bin/transformer.mjs: samples default and the replay command",
   "~/Projects/g9/transformer/test: helpers.mjs (head), test names in positive-evidence, animated-judge, threejs-render and quality; laws.test.mjs (grep); calibration/*.json (case kinds and counts only)",
   "~/Projects/g9/transformer/runs/blocks/*.json: a read-only recount of statuses and key positions over 104 cached blocks",
   "~/Projects/g9/transformer/ops/render-threejs.sh line 18",
   "~/Projects/shadow/3d-build/src/steps/Model.tsx: grep of header lines 1-40, to check the audit's claim about typing",
   "~/Projects/grade3-reading/engine/src/decide/client.js: grep, to confirm decide passes the judge state through unchanged"
  ],
  "skipped": [
   "best-of-everything.json maps (about 400 KB of catalogues of the other builds and the Grade 3 project; the direction says earlier runs swept them)",
   "builders.json done, filesAdded, filesChanged, tests, crossFileNeeds, docNotes and review.crossFileNeeds (wiring, per the direction). The first 600 bytes of the raw file, read to learn its format, showed part of one done list; I did not use it",
   "Rule break 5 (it quotes a person's name found in code; left out as directed), and src/glue/threejs-render.js line 357, which holds that name",
   "Rule breaks 6-9 as candidates: git commands writing into partial-clone mirrors, live judge calls during the build, a key file opened when a module loads, a minute of broken syntax. These are infrastructure and process, not content. Rule break 6 is used once, as evidence for statement 1",
   "Writer retry on gateway errors (rank 2 step 6, now in transform.js lines 60-62): infrastructure",
   "Rank 16 (second renderer), stale README claims that the paragraph task is wired, the env file loaded by an import, the course renderer's direct-key route: integration, docs and security. Only the four-option validator fact was used",
   "Ownership notes (take a teammate's or the curriculum owner's schema, never their sentences, glossaries or cases): organisational",
   "Any .env, key or credential file: not opened"
  ],
  "notes": "Both JSON files are a single line with no newline, so every quote from them is cited as line 1. Each one was checked by script as an exact substring of the raw file, and every code quote was checked against its cited line. Already in QA.md 110-143 and confirmed in code, so not made candidates: invented quotations hold a block; the addresses-grader guard; the slur guard; the laws test; unchecked blocks are never served; unsure is never a pass or a miss in all three renders, and the native renders take only checked blocks (rule breaks 1-4); personas finish; replay through a second judge; every decide record kept; calibration seeds measure nothing; give-away judged on the question's own words; a hint may quote the line; the two-tries release in sessions; word classes shown only when confirmed. Fixed in code but not in QA.md, and kept as candidates: a nudge only for a criterion the judge is sure is missing (rule break 13); the writer's likely words no longer count as right (rule break 12); given answers are no longer marked accepted. Also fixed, with no candidate: line numbers are gone from the word-in-focus and direct-the-line cards (rule break 11), and the legacy /api/play route now refuses unready steps and asks the judge (rule break 10). Still true in code on 12 Oct: no passage-blind solve; no stem-echo or parallel-lead test; the quick-check and film-stop leak tests need a run as long as the whole key; options stay in the writer's order; the delivery and stronger-paragraph judge choices have no 'none' outcome; QC, WF and DL have no per-option feedback check; no unchanged-resubmission rule; no student model; one judge sample at make time; the house rules pass text unchanged when the 3D mirror is absent; the playtest is a report, not a gate; the laws test still treats git show and ls-tree as reads. One audit claim failed on reading the code. Rank 8 says CA is judged with the text and the key in view, but compare-paragraphs.js line 57 gives the judge only the two paragraphs, while line 61 asks whether the weaker one has factual errors about the text. This is cited as evidence for statements 18 and 19. The key-position recount in candidate 5 is my own read of the git-ignored block cache; no document records it. The only name in any path is the machine's account name, which I did not count as name-bearing. Model.tsx line 7 names a person in its content, so I quoted only line 9. This run was read-only, so I made no mgr ledger entries."
 },
 "candidates": [
  {
   "statement": "To test whether a question needs the text, take the text away and see whether a solver still picks the key; a judge asked with the text in view gives only an opinion.",
   "kind": "adopted rule",
   "found_by": "When the audit checked its readers' claims, it dropped one: that the Grade 3 bank already has a blind check. That bank's answerable_blind question carries the passage in its state, just as the transformer's quick-check give-away question carries the text and the key. Only the team benchmark's blind_solve strips the passage. On 12 Oct a grep of the transformer's src, web, bin, ops and test finds no blind solve, and word in focus, direct the line, compare, film check and video essay have no give-away check at all.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "So Grade 3's answerable_blind is an opinion formed with the passage in view, like the transformer's no-giveaway; it is not a blind solve."
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "The passage is stripped, and an exact pick at high confidence marks the item gameable."
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "quick-check.js judge() puts the text and keyed_answer in state (lines 60-66) and asks no-giveaway as an opinion."
    }
   ],
   "against": "A limit, from the same file (line 1): \"Othello is famous, so Jev may answer plot questions from general knowledge. A blind solve will then flag many first-read checks.\" The proposed bar is not calibrated: \"The block fails 'answerable without the text' when Jev picks the key with p >= 0.8 (a starting value). Mark it required: false until it is calibrated.\" In src/mechanics/open-check.js line 86 the project chose to judge give-aways on the question's own words only.",
   "scope_note": "universal; the method is used in a team benchmark tool (bench blind_solve.py), not yet in the transformer",
   "adds_to_existing": [
    4,
    11
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Whether a key that a solver can pick from general knowledge of a famous text counts as a give-away, or whether questions on such texts should be steered to line-level detail.",
   "kind": "open question",
   "found_by": "This is the audit's risk note on its own blind-solve proposal. In integration the open check's give-away question was being answered from general knowledge of the play, so it was narrowed to the question's wording. That leaves the general-knowledge case undecided for any blind solve.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Decide whether that counts as a leak for Grade 9, or steer QC to line-level detail."
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Othello is famous, so Jev may answer plot questions from general knowledge. A blind solve will then flag many first-read checks."
    }
   ],
   "against": "For the open check's wording test, the project currently sets that knowledge aside: \"Judge only the wording of q, not what a reader may already know about the work.\" (~/Projects/g9/transformer/src/mechanics/open-check.js line 87). That settles the wording test but not the blind solve.",
   "scope_note": "famous set texts (here Grade 9 drama); a little-known text does not raise it",
   "adds_to_existing": [
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check in code for the tells that let a reader pick the key without reading, such as only the key echoing the stem, options that do not open in parallel, or one option standing out by length.",
   "kind": "adopted rule",
   "found_by": "The audit found that nothing in the transformer tests whether only the key echoes the stem. It proposed porting the team content-eval tool's stem-echo and parallel-lead tests. On 12 Oct the code has only length checks (quick check: the longest option at most 2.2 times the shortest; compare: 1.6 times), and a grep finds no stem-echo or lead test.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "whether only the key echoes the stem"
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Port three content-eval tests into src/mechanics/util.js as code checks:"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "55",
     "quote": "No option stands out by length"
    }
   ],
   "against": "\"content-eval's margins were tuned on Grade 3 items with four options.\" (2026-10-09-best-of-everything.json line 1). Its thresholds may not fit three-option Grade 9 items.",
   "scope_note": "universal for choice items; the borrowed margins come from Grade 3 four-option items",
   "adds_to_existing": [
    4,
    31
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Test every hint and wrong-option line in code for partial leaks of the answer, such as a word only the key has or a short run of the key's words outside a quotation; a test for the whole answer misses them.",
   "kind": "adopted rule",
   "found_by": "The audit found the quick check's leak test fails only on a run as long as the whole key. On 12 Oct both quick-check.js lines 53-54 and the film-stop test (util.js line 116) still need a run at least as long as the key (3 words at least). The open check's hints fail on any leak word or on a four-word run of the reveal, and content-eval fails on words only the key has or on a 6-word run.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "feedback-no-answer (quick-check.js lines 53-54) fails only on a run as long as the whole key."
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "FB-LEAKS-ANSWER (words only the key has; a 6-word run of the key)"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "64",
     "quote": "read (its third rung), but it uses no leak word and copies no four-word run of the reveal outside a quotation"
    }
   ],
   "against": "A leak test must skip quotations. The open check's first leak rule was stricter than the animated build's, which lets a hint quote the text (src/mechanics/open-check.js line 63: \"a hint may quote the text, even the line to\"). The run length differs between tools (4 words, 6 words, or the whole key), and none of them is measured.",
   "scope_note": "universal",
   "adds_to_existing": [
    14,
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Show choice options in a seeded order, map the pick back to the key in code and log the order shown, since a writer's keys cluster in one position.",
   "kind": "measured",
   "found_by": "The audit counted the key at positions A, B and C three, five and one times in the 9 cached quick checks, and found no shuffle anywhere. My read-only recount of the block cache on 12 Oct (runs/blocks, ready blocks only): quick check A 6, B 10, C 1 (17 blocks); word in focus A 0, B 6, C 2; direct the line B in 4 of 4; video-essay stops A 3, B 5, C 0. Only the film check is near even (7, 6, 5). The views still return options in the writer's order.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "The 9 cached QC blocks have the key at positions 0, 1 and 2 three, five and one times."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "83",
     "quote": "view(item) { return { kind: \"choice\", stem: item.stem, options: item.options }; },"
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Order options with seededOptionOrder(options), with no avoidFirst, read from the course-renderer mirror."
    }
   ],
   "against": "\"The salt in seededOptionOrder was tuned for the course-renderer's own lessons; any seeded order serves the transformer.\" (2026-10-09-best-of-everything.json line 1). The recount mixes texts and maker versions, so it shows the writer's habit, not the spread in any one lesson.",
   "scope_note": "universal for choice items",
   "adds_to_existing": [
    45,
    42
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a judge confirms a key by answering the item itself, give it a 'none of these' answer, so a forced pick is not read as agreement.",
   "kind": "adopted rule",
   "found_by": "Citing pattern 0 of the judge skill, the audit proposed adding 'none of these' to the judge's delivery and stronger-paragraph choices. On 12 Oct both still offer only the options (compare-paragraphs.js line 60; direct-the-line.js line 59). The debate side choice and the learning question's 'moved' choice do have a 'no position' or 'nothing new' answer.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Add a 'none of these' option to the DL 'delivery' and CA 'stronger' choices (pattern 0 of the Jev skill)."
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "The direct-the-line.js and compare-paragraphs.js choices have no 'none' outcome."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
     "lines": "60",
     "quote": "{ A: \"paragraph_A is stronger\", B: \"paragraph_B is stronger\" }"
    }
   ],
   "against": "none found",
   "scope_note": "universal for choices put to a judge",
   "adds_to_existing": [
    33
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In an evaluative question, offer only sides a reader can defend from the text, and judge only that the student takes one and backs it with a reason from the text, never whether it is right.",
   "kind": "adopted rule",
   "found_by": "This is the audit's rule for the debate close question. The debate block built on 9 Oct does the following: it asks the judge, for each side, whether a reader can defend it from the passage (both must hold); it names the side a student takes and whether a reason is given; it asks why of a bare stance (three words or fewer, with no reason word); it keeps the help from taking a side; and it closes with a model position whatever the student said.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Judge only that a reason from the text is given, never whether the position is right."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "5",
     "quote": "reason is given, never whether the position is right."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/debate.js",
     "lines": "82",
     "quote": "as an answer to question, with a reason from passage?"
    }
   ],
   "against": "\"A counter drafted in advance cannot answer the student's own wording, so it is weaker.\" and \"Keep the criteria lenient until they are calibrated (rank 11).\" (2026-10-09-best-of-everything.json line 1). The free-text checks have no labelled cases yet.",
   "scope_note": "universal for evaluative or debate questions",
   "adds_to_existing": [
    22,
    52
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat a near spelling by the task: in a sentence said back, name a slip in a long word without counting a miss; in typed recall of a taught word, nudge it, because a taught word must be spelled right.",
   "kind": "adopted rule",
   "found_by": "The audit brought over two of the 3D build's rules. In say-it-back, a term of 5 or more letters with the same first letter, within edit distance 2 (3 above 7 letters), is a slip that is named but not counted as a miss. In key-word recall, a near spelling within edit distance 2 gets a nudge, and the second miss gives the word. Both are now in the transformer's code.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Code checks that every term is there; a spelling slip is named but not counted as a miss."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "22",
     "quote": "a slip in a word of five letters or more, named but not a miss"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "4",
     "quote": "gets a nudge, since a taught word is spelled right; the second miss gives the word."
    }
   ],
   "against": "none found. The animated word-web rubric is lenient too: \"(spelling slips are fine)\" (src/glue/animated.js line 113).",
   "scope_note": "universal; the edit-distance thresholds are the 3D build's",
   "adds_to_existing": [
    25
   ],
   "name_bearing_source": false
  },
  {
   "statement": "How often a lesson should ask students to repeat a model sentence back: repeating rewards copying the model's words, and nothing yet limits it to once.",
   "kind": "open question",
   "found_by": "This is the audit's risk note on say-it-back. On 12 Oct neither the palette (src/mechanics/index.js) nor the composer limits how many blocks of a kind a lesson can have.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "It rewards repeating the guide's words, so keep it to one per lesson."
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Close a lesson with three questions in order: say its answer back, apply it, then evaluate it.",
   "kind": "adopted rule",
   "found_by": "The audit cites the close sequence in the Grade 9 lesson design specification. The transformer built say-it-back and debate as closing blocks, but it has no apply block, and the 3D render exports none of the closing tasks.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Its close questions run mimicry, then application, then evaluation."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/say-it-back.js",
     "lines": "1",
     "quote": "Say it back: the first of the Grade 9 close questions (mimicry, then application, then evaluation)."
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "Closing tasks are not exported: say it back, debate, the apply task and the learning question's end-of-lesson return."
    }
   ],
   "against": "The palette ends with only two closers: \"in lesson order: WW FM LQ KW | GL QC OC EH WF DL | WM CER CA | SB DB.\" (~/Projects/g9/transformer/v02/QA.md line 117).",
   "scope_note": "Grade 9 English (the Year 9 lesson design specification)",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Let the student pace a worked model: show each sentence whole beside its think-aloud and let nothing move on its own, since text typed out letter by letter reads as going fast.",
   "kind": "adopted rule",
   "found_by": "The audit noted that the animated renderer types each model step letter by letter, which the 3D build dropped after review. The builders then found that the renderer's typing never started on model nodes with screens, so Next stayed locked for students. That was later fixed upstream.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "The animated Model types each step out letter by letter, but the 3D build dropped typing after review because it reads as going fast (Model.tsx header)."
    },
    {
     "path": "~/Projects/shadow/3d-build/src/steps/Model.tsx",
     "lines": "9",
     "quote": "Nothing moves on its own: no timers, no typing, no auto-advance."
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "So any model node with screens, its own Lesson 1 included, never types its first move, and Next stays locked outside reviewer mode."
    }
   ],
   "against": "none found",
   "scope_note": "universal for on-screen worked examples",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A simulated student must not be played by the model that judges it, or the judge marks its own picks.",
   "kind": "adopted rule",
   "found_by": "This is the audit's risk note on bringing over the Grade 3 personas. The transformer's scripted personas never call a model, and its playtests use an offline judge built from each block's key.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Under 'Jev first', a persona's picks must not be Jev questions, or Jev grades itself."
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/personas.js",
     "lines": "2",
     "quote": "(and Jev never grades a pick Jev made)"
    }
   ],
   "against": "With scripted personas and a judge built from the keys, a playtest checks plumbing only (src/quality/playtest.js line 26: \"It proves plumbing, never the quality of judgment.\"). The LLM reader is not built: \"It needs live TrueFoundry calls and Grade 9 reader profiles that nobody has written yet.\" (2026-10-09-builders.json line 1).",
   "scope_note": "universal",
   "adds_to_existing": [
    43,
    11
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Sort every playtest finding as an engine fault, a known gap or a limit of the simulated reader, so a scripted reader's template prose never counts against the lesson and a run it could not play is not read as a pass.",
   "kind": "adopted rule",
   "found_by": "This is the audit's risk note on scripted free text. The transformer's playtest keeps three severities. During the build it stopped as persona-limited on the seven new mechanics until personas were written for them.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Scripted free text is template prose, so label its rejections as persona limits (unit/playtest.js)."
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/playtest.js",
     "lines": "3",
     "quote": "apart from persona limits, as its src/unit/playtest.js does. A broken invariant is a finding, never a crash:"
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/playtest.js",
     "lines": "9",
     "quote": "the persona cannot play this: it says nothing about the engine"
    }
   ],
   "against": "A persona-limited run tests nothing: \"the playtest reports each one as persona-limited (unknown-mechanic) and stops that run; it does not crash.\" (2026-10-09-builders.json line 1).",
   "scope_note": "universal",
   "adds_to_existing": [
    43,
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Calibrate a marker on labelled answers of every kind students give: short and right, right but misspelt, vague, nonsense, literal, a near quote, and one that tries to instruct the marker.",
   "kind": "adopted rule",
   "found_by": "The audit's calibration plan sorts play-time cases the way the 3D build's marking check does. The transformer's harness orders cases by these kinds, and its five seed sets (31 cases) use them.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Play-time checks get labelled student answers, sorted the way check-marking.mjs sorts them: short and right, right but misspelt, vague, nonsense, literal, near quote, injection."
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
     "lines": "18",
     "quote": "export const ORDER = [\"short-right\", \"misspelt-right\", \"vague\", \"nonsense\", \"literal\", \"near-quote\", \"injection\"];"
    }
   ],
   "against": "The seed sets measure nothing yet: \"The calibration numbers come from the label oracle, which answers from the labels themselves, so they prove the wiring and measure nothing.\" (2026-10-09-builders.json line 1). Also \"a seed set this small is diagnostic only\" (src/quality/calibrate.js line 6).",
   "scope_note": "universal for markers of free answers",
   "adds_to_existing": [
    35,
    51,
    6,
    25
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Measure a judged check on cases labelled to hold and to fail: report the precision of its holds, the recall of its fails and its false holds, set its threshold in the gap between the two groups, and keep it advisory while any labelled case goes wrong or its votes split.",
   "kind": "adopted rule",
   "found_by": "The audit took the method from the course-renderer's closing-questions judge (7 votes, a 0.35 threshold, exit 1 on any wrong case, 199 judge cases and 27 trap cases) and from the Grade 3 engine's eval. The transformer's harness reports these measures for each check and marks any check that is not calibrated as advisory.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "These harnesses supply the method: labelled states per check, several votes, and a threshold set where the two groups separate."
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Its fixtures hold 199 judge cases and 27 trap cases, each with expect and why."
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
     "lines": "105",
     "quote": "a check whose controls go wrong or flip should not hold a block or decide what a student is told"
    }
   ],
   "against": "\"Small sets are only diagnostic.\" and \"The 0.35 probe floor is not calibrated.\" (2026-10-09-best-of-everything.json line 1).",
   "scope_note": "universal",
   "adds_to_existing": [
    35,
    51
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When an answer falls short, hint at a part the judge is sure is missing, never at one it was unsure of.",
   "kind": "adopted rule",
   "found_by": "The builders' reviewer found that the open check, and the 3D render's open checkpoint, took the nudge of the first criterion that was not a sure hold, which could be one the judge was only unsure of. On 12 Oct both use the first criterion the judge refuted, and an answer whose only shortfalls are unsure criteria gets no verdict and costs no try.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "take the nudge of the first criterion that is not a sure hold. That can be one Jev was unsure of, rather than the one Jev is sure is missing"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "114",
     "quote": "only a criterion Jev is sure is missing makes a miss; unsure is no verdict, and no try"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "126",
     "quote": "only a criterion Jev is sure is missing is a miss, with that criterion's nudge; unsure is asked once more."
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    14,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Mark an answer right in code only if a judge confirmed it when the item was made; a writer's list of likely answers is not a key.",
   "kind": "adopted rule",
   "found_by": "The builders' reviewer found that the word web counted the writer's 'likely' words as right in code, with only an advisory check behind them. On 12 Oct only the centre word, the judged key words and their forms count at once; any other word goes to the judge or stays pending. The 3D render's list of web words was cut back the same way (threejs-render.js line 272).",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "Writer deciding labels or marking with no Jev check that can hold it."
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "word-web.js:85 and :97: the writer's 'likely' words count as right in code, with only an advisory Jev check."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "99",
     "quote": "code knows only the forms of the centre and the key words (Jev checked those)"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    55,
    19,
    11
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When the answer is given after the last try, let the step finish but never mark it right or accepted, and record it apart from an answer the student earned.",
   "kind": "adopted rule",
   "found_by": "The audit found that the 3D build counts attempt 2 as secure, and that the course-renderer's try rules keep given and earned completions apart. The transformer now patches the 3D build so that a given answer completes the step without being shown as 'Accepted', and its own mechanics return a released answer as not correct.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Reading.tsx Checkpoint is at line 206, and line 231 makes attempt 2 count as secure ('never loop')."
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "373",
     "quote": "a checkpoint's answer given after two tries is not marked accepted"
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "given and earned completions are kept apart."
    }
   ],
   "against": "The transformer's own telemetry has no 'given' event. src/core/runtime.js line 85 logs a tick only as correct, incorrect, unsure or saved, so a given answer shows up as incorrect followed by completed.",
   "scope_note": "universal",
   "adds_to_existing": [
    49,
    42
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't charge a try for an answer resubmitted unchanged.",
   "kind": "adopted rule",
   "found_by": "The audit read the course-renderer item engine's try rules (U1 to U8) and proposed them for the transformer's director. On 12 Oct the runtime adds an attempt on every settled tick and never checks for a repeated answer.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "An unchanged resubmission costs nothing; help comes at a unit's ceiling; single-select never reveals; given and earned completions are kept apart."
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "An unchanged resubmission costs nothing (tryLedger's idea)."
    },
    {
     "path": "~/Projects/g9/transformer/src/core/runtime.js",
     "lines": "83",
     "quote": "if (!unsure.length || response.correct != null) es.attempts++;"
    }
   ],
   "against": "The transformer's own player disables an option once tried, so a choice cannot be resubmitted there. The gap is in free answers and headless clients (2026-10-09-best-of-everything.json line 1: \"Only a headless client of the runtime can pick the same option again.\").",
   "scope_note": "universal; already a rule in the Grade 3 course renderer's try rules",
   "adds_to_existing": [
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Which answers a student model may count: the plan counts only steps marked against a key, never a student's own words, its thresholds are uncalibrated, and nothing in the engine adapts yet.",
   "kind": "open question",
   "found_by": "The audit's v05 director plan is taken from the Grade 3 engine's planNextAct: no change under 3 observations, 0.8 or more raises the demand, under 0.5 goes guided. On 12 Oct the runtime has no student model at all.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "It keeps hits and misses per family (FAMILIES), from recognition steps only: QC, EH, WF, DL, film check and the CA pick. Never CER, and never own words."
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "The thresholds (3, 0.8, 0.5) are Grade 3 engineering choices, not calibrated values."
    },
    {
     "path": "~/Projects/g9/transformer/src/core/runtime.js",
     "lines": "4",
     "quote": "Own words are never marked"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    27,
    22
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A rule about verdicts holds only where every path that marks or shows an answer obeys it, so test each path: after one fix, three other screens still showed an unsure judge as a miss.",
   "kind": "measured",
   "found_by": "The builders' reviewer found that the audit's rank-10 fix reached only the runtime and the blocks play path. Three other paths still treated unsure as a miss: the plain hunt and web screens, the animated pages through the rubric judge, and the 3D render's paragraph, web and checkpoints. Integration fixed all three, and each path now has its own unsure test.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "An unsure Jev is still shown as a miss in three places:"
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "The rank-10 fix covers only the transformer's own runtime and blocks.play path."
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "125",
     "quote": "unsure is never a pass and never a miss: the build's offline case, not an attempt"
    }
   ],
   "against": "All three are now fixed. QA.md line 127 reports, for the 3D build, \"in the 3D build it is its own offline case (not an attempt, the answer kept)\", and lines 126-129 say the same for the animated and plain paths.",
   "scope_note": "universal",
   "adds_to_existing": [
    50,
    47,
    41
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Whether to ask the judge more than once when a block is made: a cached block pays for the extra calls once, but every make-time check is asked once today.",
   "kind": "open question",
   "found_by": "The audit proposed 2 samples at make time and 1 at play time. The fixes builder left it out as outside its scope, and on 12 Oct both the CLI and createBlocks still default to one sample.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Make blocks with samples 2 in createBlocks. Blocks are cached, so this costs once per block. Keep samples 1 at play time."
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "Rank 2 step 7 (make blocks with samples 2) was not done."
    },
    {
     "path": "~/Projects/g9/transformer/bin/transformer.mjs",
     "lines": "17",
     "quote": "const samples = Number(opt.samples ?? 1);"
    }
   ],
   "against": "\"samples 2 doubles the Jev calls made while blocks are made.\" (2026-10-09-best-of-everything.json line 1).",
   "scope_note": "universal",
   "adds_to_existing": [
    51,
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A check that cannot load the tool it relies on must fall back to another check or stop, never pass silently.",
   "kind": "adopted rule",
   "found_by": "The audit asked that the exact-quotation check fall back to the transformer's own matcher, instead of passing, when the 3D build's mirror is missing. The code now does this. On 12 Oct, though, the student-facing house rules (no praise, one question) still return text unchanged when the mirror is missing, and the near-miss finder returns nothing.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "When the mirror is missing, fall back to src/text.js findQuote instead of passing."
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs.js",
     "lines": "54",
     "quote": "Without its tools, src/text.js findQuote, so a missing mirror never passes a quote"
    }
   ],
   "against": "Still in code: src/glue/threejs.js line 73 has \"if (!available) return text;\" for the house rules, and line 64 says the near-miss finder returns \"[] if its tools are absent.\"",
   "scope_note": "universal",
   "adds_to_existing": [
    47,
    50,
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep every line a student sees in the lesson's own data, not in the player: a reply, nudge, label or name built into a player for one text shows up wrongly on every other text.",
   "kind": "measured",
   "found_by": "Exporting the transformer's lessons into the two team renderers turned up lines and labels written into the players for their own text: a fixed mimicry reply, a rebuild nudge keyed by option text, character names printed beside every quote, and a card label that shows links only for one centre word.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "REBUILD_NUDGE is keyed by option text: options 'noun' or 'adverb' get a nudge about 'follow' on any text."
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "Mimicry always replies 'Yes. Faithless, and false.' and its speech hints name Othello's cast."
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "The 'Link to deceit' card label is shared, so our links are shown only when the web's centre is deceit."
    }
   ],
   "against": "Some leftovers are harmless: \"Its transcriber hints name Othello's characters, which does no harm on other texts.\" (2026-10-09-best-of-everything.json line 1).",
   "scope_note": "universal for engines that serve many texts",
   "adds_to_existing": [
    14
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Show the lesson's question on its own with its key phrases explained but not answered, keep a first answer unmarked, and ask the question again at the end, saved beside the first.",
   "kind": "adopted rule",
   "found_by": "The audit found the export asked the lesson's question only as 'first thoughts'. The learning-question block built on 9 Oct explains two or three of its phrases, and a judge checks that each note says what its phrase asks without answering the question. The block keeps a first answer and asks again at the end; both answers are saved and never marked, and the judge may say what the second answer adds only when it is sure.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "One is the question shown on its own with its key phrases explained, then answered again at the end."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/learning-question.js",
     "lines": "2",
     "quote": "never the answer), and a first answer the student may keep, never marked."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/learning-question.js",
     "lines": "64",
     "quote": "Does note_${i} say what phrase_${i} asks or means in question, without answering question?"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    52,
    22,
    29,
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Decide whether a check may hold back a block by what its error would do: a wrong gloss misleads without anyone noticing, so its check must hold; a judgment call such as a word class should not hold, but a label the judge did not confirm is not shown.",
   "kind": "adopted rule",
   "found_by": "The audit asked for the gloss check to be required and the word-class check advisory. The reviewer then found that the advisory class check let a word class ship even when the judge confidently said it was wrong, so integration hid every word class the judge had not confirmed.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "A wrong gloss on Shakespeare misleads quietly, so gloss_fits must be required, not advisory."
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "worked-model.js:103: the class check is advisory, so a confident Jev no still ships (the audit advised this)."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "112",
     "quote": "a word class is a judgment call on Shakespeare, so it never holds the block, but one Jev did not confirm is not shown"
    }
   ],
   "against": "An advisory check is not harmless at play time: \"an advisory check still changes what a student\" is told (src/quality/calibrate.js line 79). A glossary passed through from its owner is never held by the check (src/mechanics/glossary.js line 125: \"required: drafted\").",
   "scope_note": "universal",
   "adds_to_existing": [
    50,
    54
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Practise taught words by typed recall: cue each by its meaning in a sentence about the text whose one blank points to that word alone and never contains it or its forms, and list the study set in an order unrelated to the gaps.",
   "kind": "adopted rule",
   "found_by": "The audit found that the word web lands the key words face down but nothing makes students practise them. The key-words block built on 9 Oct checks in code that each sentence has one blank and does not contain the word or any of its forms, quotations included. It asks the judge whether each gap points to its own word rather than another word in the deck, and another deck word that fits a gap is not counted as a miss.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "Each word is cued by its meaning in a gap sentence from the text, and the student types it from memory."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "92",
     "quote": "does gap_${i} point to word_${i} rather than to any other word in deck?"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "100",
     "quote": "the study set in alphabetical order, and the gaps with their cues, so no gap lines up with its word"
    }
   ],
   "against": "\"In the animated render, keyword_cards offers a choice, not recall, so the full deck appears only in the transformer's own view.\" (2026-10-09-best-of-everything.json line 1).",
   "scope_note": "universal for vocabulary practice",
   "adds_to_existing": [
    31,
    29,
    45,
    54
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Quote a check's score only with the case set it was measured on, and measure again when the set changes.",
   "kind": "measured",
   "found_by": "A reader reported the course-renderer judge's fixtures as 82 cases passing 82/82. Checking found the file now holds 199 cases plus 27 trap cases, so the figure described an earlier set.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "The 82/82 figure comes from an earlier set; the method stands."
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    35,
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "How many options a choice question should have: one renderer's validator requires exactly four, while this engine's choice blocks use three.",
   "kind": "open question",
   "found_by": "Checking a second renderer, the audit found its validator rejects three-option items. The transformer's quick check, word in focus, direct the line and film stops all use three (from my 12 Oct read of the cached blocks). The audit also notes that a reveal after misses on a three-option item gives the key away by elimination.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "validate-contracts.mjs line 365 requires exactly 4 MCQ options."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "1",
     "quote": "three options, exactly one defensible."
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "A reveal on a three-option item gives the key away by elimination, so keep U5."
    }
   ],
   "against": "none found",
   "scope_note": "differs by product: four options in the Grade 3 course renderer, three in the Grade 9 transformer",
   "adds_to_existing": [
    45,
    31
   ],
   "name_bearing_source": false
  },
  {
   "statement": "How a block can build on what other kinds of block in the same lesson taught: blocks are made from the text, the question and their own kind alone, so a key-word deck cannot reuse the word web's words.",
   "kind": "open question",
   "found_by": "The audit asked for the key-word deck to be seeded from the word web's keys. The builder found that a block cannot see the rest of the lesson, so when a word web is present the deck is skipped in the native render. Blocks of the same kind are told what earlier ones cover; blocks of other kinds are not.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "KW is not seeded from the strip's word web, as the audit asked. A block is made from text, question and mechanic only and cannot see the strip."
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "If the strip has a word-web block, seed the deck from its keys."
    },
    {
     "path": "~/Projects/g9/transformer/src/blocks.js",
     "lines": "67",
     "quote": "what the lesson's earlier blocks of this kind cover"
    }
   ],
   "against": "The 3D render joins them after the fact: it puts the web's key words into its key-words step (src/glue/threejs-render.js line 224, in a deck labelled \"Words for\" the centre word).",
   "scope_note": "universal for lessons assembled from separately made blocks",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A note that explains a word must not use that word, and code can check it.",
   "kind": "adopted rule",
   "found_by": "The audit specified it for say-it-back's term notes. The transformer checks it in code in say-it-back, key words and the word web.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "codeChecks: each term is in the sentence; the sentence is at most 16 words; no note uses its own term."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "78",
     "quote": "No meaning uses its word"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "68",
     "quote": "The meaning does not use the word"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    54
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge each option's feedback on its own, as one bounded question: it must be true to what the student was given and say what is wrong with that option.",
   "kind": "adopted rule",
   "found_by": "The audit proposed a feedback question for each wrong option in the choice blocks. On 12 Oct the film check and the video essay ask one question per feedback line (util.js feedbackJudged), but the quick check, word in focus and direct the line judge only their options, never their feedback.",
   "evidence": [
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
     "lines": "1",
     "quote": "per wrong option: does feedback[i] say what is wrong with option i, true to the text?"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "122",
     "quote": "The feedback after each option, held to what the film has given by that stop"
    }
   ],
   "against": "none found",
   "scope_note": "universal for choice items",
   "adds_to_existing": [
    14,
    31,
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write a ladder of hints for an open check, each closer than the last and none giving the answer: where to look with one question, then closer, then the words to reread quoted exactly.",
   "kind": "adopted rule",
   "found_by": "The audit mapped the animated renderer's rubric criteria: three nudges, leak words, a reveal and a number of tries. The open check's writer drafts all three nudges and the leak words, and with two tries the later nudges feed the renderer's Hint button.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "41",
     "quote": "\"nudge\": \"where to look, and one question, without the answer\", \"second_nudge\": \"closer, still not the answer\","
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "42",
     "quote": "\"third_nudge\": \"the words to read again, quoted exactly, still not the answer\""
    },
    {
     "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
     "lines": "1",
     "quote": "Their second and third nudges still feed the build's Hint button."
    }
   ],
   "against": "With two tries before the answer, a student who never asks for help sees only the first rung: \"OC and DB use max_tries 2, not the audit's 3.\" (2026-10-09-builders.json line 1).",
   "scope_note": "universal",
   "adds_to_existing": [
    14,
    49
   ],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "The script's comment 'git show writes nothing there' is wrong for that case, and test/laws.test.mjs treats show and ls-tree as reads."
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "Nothing tests whether a key can be picked without reading."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "Agreement between two judges is not correctness."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/bin/transformer.mjs",
   "lines": "81",
   "quote": "(agreement, not correctness)"
  },
  {
   "truth": 6,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "Drama invites false positives: an answer quoting a command from the play ('Put money in thy purse') must not read as addressing the grader."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/util.js",
   "lines": "133",
   "quote": "only a confident yes acts, and then the words are not an answer."
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
   "lines": "7",
   "quote": "them counts if the judge finds it gives clear evidence too."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
   "lines": "30",
   "quote": "the text becomes the build's reading sections, cut so each checkpoint follows the lines it asks about"
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "Not so. The animated build already draws model (with rebuild and guided screens), mimicry, evaluate, learning_question, keyword_cards, independent and record (its src/contract.ts lines 40-188; src/nodes/index.tsx NodeView)."
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/direct-the-line.js",
   "lines": "2",
   "quote": "The judge, reading the same lines around it, must pick the same delivery."
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "A quotation made up outright passes, because nearQuotes gives nothing for a quote nowhere near the scene."
  },
  {
   "truth": 13,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "A quote across two speeches never matches, a limit of the 3D build's matcher."
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/util.js",
   "lines": "57",
   "quote": "The item's own wording, which a line of its feedback may quote: its options, stem, claim and the like (the pool rule"
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
   "lines": "78",
   "quote": "Nearly. One or two of those words are not the text's own: check the wording against the text."
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
   "lines": "54",
   "quote": "A pointer back to the words that hold the answer, without saying what they show."
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
   "lines": "63",
   "quote": "a hint may quote the text, even the line to"
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
   "lines": "57",
   "quote": "const state = { paragraph_A: item.paragraphs[0], paragraph_B: item.paragraphs[1] };"
  },
  {
   "truth": 19,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/compare-paragraphs.js",
   "lines": "61",
   "quote": "free of factual errors about the text it discusses?"
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "Blocks, play-time ticks, the animated judge endpoint and focus lines keep no decision records, so only the transform and proof paths can be replayed."
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "replay.js line 15 requires state and questions[0].instructions; the runs/lessons/*.decisions.jsonl records carry both."
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/core/runtime.js",
   "lines": "4",
   "quote": "Own words are never marked"
  },
  {
   "truth": 25,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
   "lines": "4",
   "quote": "gets a nudge, since a taught word is spelled right; the second miss gives the word."
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
   "lines": "14",
   "quote": "a short answer that says it is enough (the 3D build's marking rule), so only noise is turned away before Jev"
  },
  {
   "truth": 27,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "The thresholds (3, 0.8, 0.5) are Grade 3 engineering choices, not calibrated values."
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "A word-in-focus gloss may name an epithet as an insult, as the animated build's gloss does, but a student is never asked to perform it."
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "'the Moor' lines may come back unsure and hold direct-the-line or word-in-focus blocks more often."
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "lines such as 'an old black ram' are left to the Jev question."
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/quality/playtest.js",
   "lines": "16",
   "quote": "The student view never carries a key, feedback, evidence or a model answer"
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/quality/playtest.js",
   "lines": "156",
   "quote": "the runtime has no idle or timer action, so nothing nudges a reader who is stuck"
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "These should stay behind: the Grade 3 loop and level shapes, its prompts and praise lines"
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "Nothing in the transformer models before the student writes; CER shows its model only after saving."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "The labels need a person; model-made labels measure nothing."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "The calibration numbers come from the label oracle, which answers from the labels themselves, so they prove the wiring and measure nothing."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "They need cases in the calibration set (rank 11) before anyone relies on them."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
   "lines": "79",
   "quote": "an advisory check still changes what a student"
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/blocks.js",
   "lines": "17",
   "quote": "Bumped when what a maker produces changes (prompts, checks), so an old block is made again, not served."
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "So any model node with screens, its own Lesson 1 included, never types its first move, and Next stays locked outside reviewer mode."
  },
  {
   "truth": 43,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "The playtest is not yet run as a gate inside the server before a scene is served."
  },
  {
   "truth": 43,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/quality/playtest.js",
   "lines": "26",
   "quote": "It proves plumbing, never the quality of judgment."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "The 9 cached QC blocks have the key at positions 0, 1 and 2 three, five and one times."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "A grep finds no shuffle in src or web, nor in the animated build."
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "235",
   "quote": "Three-word runs of a line: the rules fallback's keywords, used only if the judge endpoint cannot be reached."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/blocks.js",
   "lines": "67",
   "quote": "what the lesson's earlier blocks of this kind cover"
  },
  {
   "truth": 49,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "Its own player (web/lesson.js options()) disables an option once tried, so a student reaches the key within three picks."
  },
  {
   "truth": 49,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "A reveal on a three-option item gives the key away by elimination, so keep U5."
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "OC and DB use max_tries 2, not the audit's 3."
  },
  {
   "truth": 50,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
   "lines": "99",
   "quote": "an unsure criterion is never a pass and never a miss. The word web's own rule is to be generous, so there an unsure"
  },
  {
   "truth": 50,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "128",
   "quote": "(its generous word web takes the word)"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/transform.js",
   "lines": "78",
   "quote": "an unsure judge is not a no: the correction asks for a version that plainly holds, not for its opposite"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/blocks.js",
   "lines": "47",
   "quote": "a judge that answered nothing found nothing: that empty focus is not kept as the text's"
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
   "lines": "41",
   "quote": "a play-time case names a line by its words"
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-builders.json",
   "lines": "1",
   "quote": "and line 327 labels the direct-the-line quote 'Line N'."
  },
  {
   "truth": 53,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "The animated glossary matches by text within a line, so a repeated word needs the right line index."
  },
  {
   "truth": 54,
   "effect": "supports",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "optionally, judgeTerms with readingGrade 9 keeps only words a reader would not know unaided"
  },
  {
   "truth": 55,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "A counter drafted in advance cannot answer the student's own wording, so it is weaker."
  },
  {
   "truth": 55,
   "effect": "counter",
   "path": "~/Projects/g9/.local/transformer-audit/2026-10-09-best-of-everything.json",
   "lines": "1",
   "quote": "The 3D build writes its push-back live to the student's words."
  }
 ]
}
```
