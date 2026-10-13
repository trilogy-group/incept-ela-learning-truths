# read:glue-surface

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  nono, analyse its ideas and fold them into the research results

## Result

```json
{
 "direction": "glue-surface",
 "coverage": {
  "read": [
   "~/Projects/g9/transformer/src/glue/ (animated.js, animated-judge.js, sources.js, threejs.js, threejs-render.js, threejs-archivist.js, each in full)",
   "~/Projects/g9/transformer/src/server.js (in full)",
   "~/Projects/g9/transformer/web/ (index.html, lesson.html, app.js and lesson.js in full; styles.css comments and its strip, quality-line and lesson-frame rules)",
   "~/Projects/g9/transformer/v03/README.md through v11/README.md (all nine planned stages)",
   "~/Projects/g9/transformer/v02/QA.md (in full; cited for its glue, composer and integration records)",
   "~/Projects/g9/transformer/DECISIONS.md",
   "~/Projects/g9/transformer/README.md (use, blocks, how a block is made, improve it, known gaps)",
   "~/Projects/g9/transformer/ops/judge-table.sh (header)",
   "~/Projects/g9/transformer/test/animated.test.mjs, animated-judge.test.mjs, threejs-render.test.mjs, server.test.mjs (titles and the assertions cited)",
   "~/Projects/g9/transformer/test/glue.test.mjs, positive-evidence.test.mjs, laws.test.mjs, quality.test.mjs, sources.test.mjs (titles only)"
  ],
  "skipped": [
   "src/mechanics/, src/quality/, src/video/, src/core/ and the other src/*.js modules: outside this direction; other directions cover the block makers, the playtest and the video",
   "v01/ and v02/README.md, v01/QA.md: other stages, outside this direction",
   "runs/ (marking logs, renders, films): generated data and .jsonl dumps",
   "node_modules/ and vendor/: third-party code",
   "~/Projects/shadow/ mirrors of the two players: other repositories; only what the glue states about them was used",
   "ops/ scripts other than the judge-table header: infrastructure",
   "samples/: lesson texts, not findings",
   "every .env, key or token file: never opened"
  ],
  "notes": "Every candidate comes from this repo's own code comments, string literals, tests and QA notes. This scope holds no external research. README.md line 120 says \"No lesson has been reviewed by a person or used by a student.\", so each rule here is a design rule or a machine-checked result, never a learning result. The two players disagree on several marking rules (how many tries, what to do with an unsure word, whether earlier tries count); these appear as 'against' items, as counters in evidence_for_existing, and as one open question. Planned stages v03 to v11 are all entered as open questions; v11 (platform, sign-in, hosting) is organisational and yielded nothing. Every path includes the account's home folder name, but no file in scope is named for a person, so name_bearing_source is false throughout. Each JavaScript quote is an exact substring of one line, either comment text or a string literal. Markdown quotes that wrap across lines are joined with single spaces. This was a read-only run: nothing was written and no ledger entry was made."
 },
 "candidates": [
  {
   "statement": "A choice question can be asked open only if its stem stands without its options; the options then leave the page, the right one said in any words is the answer, and an answer that gives a wrong option gets that option's own feedback.",
   "kind": "adopted rule",
   "found_by": "The transformer's quick checks were asked as the 3D player's open reading checkpoints. A stem that depends on its options is listed instead, and a test asserts that no options reach the page.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "33",
     "quote": "a question that only works beside its options (\"Which of these…\") is not asked open"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "7",
     "quote": "a reading checkpoint, asked open: the options go, the right one is what a secure answer shows"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "82",
     "quote": "A quick check asked open: the right option in meaning is secure; a wrong option gets that option's own feedback."
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    25,
    31
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Hold back anything made while no judge could check it: mark it unchecked, keep it out of the lesson, and make it again once a judge is back.",
   "kind": "adopted rule",
   "found_by": "Blocks were made while the judge was unavailable. Such blocks are now 'unchecked': muted on the strip, never drawn in either player or the stand-in view, and made again when a judge returns.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/web/app.js",
     "lines": "363",
     "quote": "A block made with no judge to check it: muted on the strip, kept out of the lesson, made again once a judge is back."
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "61",
     "quote": "made, but not yet checked: it is shown once the judge has checked it"
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "126",
     "quote": "a block made with no judge is \"unchecked\", never shown;"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    47,
    50,
    39
   ],
   "name_bearing_source": false
  },
  {
   "statement": "An item is good only for the text and the lesson question it was made from: key it on both, together with its kind and position, and refuse any older key a page sends.",
   "kind": "adopted rule",
   "found_by": "A playtest sent a saved link's first six blocks, all made before the line-number rule, and played them. Three of them cited line numbers.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/web/app.js",
     "lines": "38",
     "quote": "A short fingerprint of the source. A block is good only for the text and question it was made from."
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "193-194",
     "quote": "A block made before a rule changed is not drawn, whatever key a client sends. Before this fix, a playtest sent the saved link's first six blocks, all made before the line-number rule, and played them; three cited line numbers."
    },
    {
     "path": "~/Projects/g9/transformer/test/server.test.mjs",
     "lines": "112",
     "quote": "made for another question: not played"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    39
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep the item, its checks and its feedback lines off the student's page: the page gets only what it shows, and the server marks the answer.",
   "kind": "adopted rule",
   "found_by": "In both renders, the server answers each page's marking call from lines kept beside the render. Tests assert that the page never receives the item, the checks or the feedback lines.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/server.test.mjs",
     "lines": "36",
     "quote": "blocks: made invisibly, cached, played; the page never sees the item or the checks"
    },
    {
     "path": "~/Projects/g9/transformer/src/server.js",
     "lines": "80",
     "quote": "Each keeps its marking (the authored lines, the text's key) beside its folder, never in it, so the"
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "59",
     "quote": "the feedback lines are not shipped"
    }
   ],
   "against": "The animated player's own pages carry the rubric: \"Its pages POST `api/judge` (relative to the page) with an authored rubric and\" (~/Projects/g9/transformer/src/glue/animated-judge.js line 1). The 3D page's checkpoint table still holds the expected answer: \"assert.deepEqual(check.expects, [qc.options[qc.answer]]);\" (~/Projects/g9/transformer/test/threejs-render.test.mjs line 57).",
   "scope_note": "universal for lessons delivered in a browser",
   "adds_to_existing": [
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Key a student's saved progress to the exact version of each question, so a remade question starts fresh and two renders of a lesson never share progress.",
   "kind": "adopted rule",
   "found_by": "A block made again kept the animated player's saved progress, because that player keeps progress by node id. Node ids now carry the block's key, and each 3D render gets a progress key of its own.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "65",
     "quote": "a block made again kept the build's saved progress (its node ids now carry the block's key);"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "71",
     "quote": "build keeps a student's progress by node id, and a block made again is a new question, not one already answered"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "365",
     "quote": "a progress of its own, apart from the build's and every other render"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    39,
    42
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a quotation is nearly the text's words, say it is nearly right and ask which word is not the text's own, giving the exact wording only on the last try.",
   "kind": "adopted rule",
   "found_by": "Played in the animated player's pages: a near quotation got 'Nearly. Which of your words is not the text's own?', with the wording withheld, and the exact words were then accepted. A test keeps the wording out until the last try.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "74-75",
     "quote": "\"I follow him to serve my turn on him\" got \"Nearly. Which of your words is not the text's own?\" (the wording is never given), then the exact words were accepted."
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
     "lines": "77",
     "quote": "nearly the text's words (the 3D build's matcher): say so, without giving the wording; the build checks the reply"
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "144",
     "quote": "never the wording before the last try"
    }
   ],
   "against": "none found",
   "scope_note": "universal for quotation tasks",
   "adds_to_existing": [
    13,
    14,
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A quotation counts as evidence only when it is at least three words of the text or a whole short line.",
   "kind": "adopted rule",
   "found_by": "Both marking adapters apply this length rule before they accept a quotation as evidence.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
     "lines": "33",
     "quote": "The units a quotation covers, if it is long enough to count: three words, or a whole short line."
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "39",
     "quote": "The units a quotation covers, if it is long enough to count: three words, or a whole short line."
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs.js",
     "lines": "63",
     "quote": "Quotations of three or more words that are nearly, not exactly, the text's (its nearQuotes)"
    }
   ],
   "against": "The 3D paragraph task counts shorter and inexact quotations: \"The quoted spans in a string, two words or more (its quotesIn: double, curly or single quotes).\" (~/Projects/g9/transformer/src/glue/threejs.js line 45), and its evidence is \"the text, exactly or nearly: the page puts its own wording note on a near one), the rest Jev; one sentence's job is a\" (~/Projects/g9/transformer/src/glue/threejs-archivist.js line 207).",
   "scope_note": "universal for quoted evidence",
   "adds_to_existing": [
    13
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Match a quotation to the text with punctuation, case and apostrophes set aside, but never across a stage direction or from one speech into another, and never let a missing matcher pass a quotation unchecked.",
   "kind": "adopted rule",
   "found_by": "The 3D player's quotation matcher is used as it is. When it is absent, the transformer's own matcher runs, so no quotation passes unchecked.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs.js",
     "lines": "53",
     "quote": "Is this quotation the text's exact words? Its quotedLines: punctuation, case and apostrophes aside, never across a"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs.js",
     "lines": "54",
     "quote": "stage direction or two speeches. Without its tools, src/text.js findQuote, so a missing mirror never passes a quote"
    }
   ],
   "against": "none found",
   "scope_note": "universal; the stage-direction and speech rule applies to drama",
   "adds_to_existing": [
    13,
    47
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Cleaning rules for the lines a student reads must leave words quoted from the text untouched: an exclamation mark inside a quoted line stays.",
   "kind": "adopted rule",
   "found_by": "Before every line a student reads went through the 3D player's reply cleaners, those cleaners were tested on that player's own cases.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "29-30",
     "quote": "Tested on its own cases: praise and \"!\" removed, one question while a try remains, none on the final word, a quoted line's \"!\" kept."
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    32,
    13
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A guard against answers aimed at the marker must not catch a command that the student quotes or retells from the text.",
   "kind": "adopted rule",
   "found_by": "Tested: an answer quoting a command from the play kept its met criterion. An answer telling the marker to mark it correct met nothing and was off task.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/animated-judge.test.mjs",
     "lines": "60",
     "quote": "an answer aimed at the marker meets nothing and is off task; a command quoted from the play is still an answer"
    },
    {
     "path": "~/Projects/g9/transformer/test/animated-judge.test.mjs",
     "lines": "71",
     "quote": "the question says a command from the text does not count"
    }
   ],
   "against": "none found",
   "scope_note": "universal for judged answers about a text",
   "adds_to_existing": [
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Call an answer off task only when the judge is sure it is, and never when any criterion was met or left unsure.",
   "kind": "adopted rule",
   "found_by": "Answering the animated player's marking contract: off task requires a confident no with nothing met and nothing unsure.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/animated-judge.test.mjs",
     "lines": "53",
     "quote": "a criterion in meaning goes to Jev; off task only on a confident no, and never with a criterion met"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
     "lines": "105",
     "quote": "const offTask = !met.size && !unsure.length && results.find((r) => r.id === \"on-task\")?.verdict === \"fails\";"
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
   "statement": "The quotation offered for a student's own paragraph is never one that a worked model or guided screen has already used; when no other line can be offered, the paragraph task is left out.",
   "kind": "adopted rule",
   "found_by": "Exporting the claim-evidence-reasoning block to the 3D player's own-paragraph step, which comes after its model.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "207",
     "quote": "the student's quote: lines the lesson's blocks found for the question, never the model's or a guided quote"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "213",
     "quote": "your paragraph: no other line of the text to offer as its quote (the model's own is never offered)"
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "186",
     "quote": "never the model's quote"
    }
   ],
   "against": "none found",
   "scope_note": "universal for independent practice after a model",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When offering quotations, prefer a whole clause (a line and the rest of its sentence, at most three lines of one speech) over a fragment, and show them in the text's order.",
   "kind": "adopted rule",
   "found_by": "Choosing which lines to offer as quotations in the 3D player's paragraph step.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "85",
     "quote": "Up to n quotes from a ranked pool of units, the best first, shown in the text's order: whole clauses first (a line and"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "86",
     "quote": "the rest of its sentence, three lines of one speech at most), then single lines; never a line in `taken` or one the"
    }
   ],
   "against": "none found",
   "scope_note": "universal; 'one speech' applies to drama",
   "adds_to_existing": [
    8
   ],
   "name_bearing_source": false
  },
  {
   "statement": "End each reading section just after the lines its question needs, run on to the end of that speech by a few lines at most but never into the lines the next question asks about, and fold a short leftover into the last section.",
   "kind": "adopted rule",
   "found_by": "Cutting a text into the 3D player's reading sections, each of which asks one checkpoint. A test checks that every keyed line is read before its checkpoint.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "45",
     "quote": "Cut the text so that each checkpoint comes right after the lines its answer is in (the build asks one checkpoint per"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "57",
     "quote": "a cut moves on to the end of its speech, a few lines at most, and never into the lines the next checkpoint asks about"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "62",
     "quote": "a short tail joins the last section rather than standing alone, a section with nothing to ask"
    }
   ],
   "against": "A question whose evidence sits at the very end is dropped: \"the build asks one checkpoint per section, and no lines are left after its evidence for one more\" (~/Projects/g9/transformer/src/glue/threejs-render.js line 162).",
   "scope_note": "reading lessons with questions placed inside the text; the speech rule applies to drama",
   "adds_to_existing": [
    8
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A line that introduces a section of text says who speaks in it, never what happens in it.",
   "kind": "adopted rule",
   "found_by": "Writing the guide's boxes that sit before and after each of the 3D player's reading sections.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "114",
     "quote": "the build's own marker for the half it shows before a section). Plain lines of ours: who speaks, never the content."
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "43",
     "quote": "the half before a section is the build's \"In this next section\"; the half after it is ours, never the content"
    }
   ],
   "against": "none found",
   "scope_note": "guided reading",
   "adds_to_existing": [
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Once a question is answered, mark in the text the lines that prove the answer and bring them into view.",
   "kind": "adopted rule",
   "found_by": "The stand-in lesson view follows the animated player's reading page and marks the proving lines after a right answer.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "167",
     "quote": "reveal.units: the build's margin line (.marked) on the lines that prove the answer, brought into view."
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "242",
     "quote": "if (res.reveal?.units?.length) markLines(res.reveal.units);"
    }
   ],
   "against": "none found",
   "scope_note": "universal for questions about a text",
   "adds_to_existing": [
    14,
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Order cards and options by a neutral rule such as the alphabet, so the answer is not first just because it was written first.",
   "kind": "adopted rule",
   "found_by": "A key-word deck was exported whose first word was the gap's word. A test now checks that the first card is not that word.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "146",
     "quote": "in alphabetical order, so neither the first card nor the first option is the gap's word"
    },
    {
     "path": "~/Projects/g9/transformer/test/animated.test.mjs",
     "lines": "94",
     "quote": "in alphabetical order: the first card is not the gap's word"
    }
   ],
   "against": "none found",
   "scope_note": "universal for choice sets",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Even where answers are kept and never marked, refuse noise: gibberish, the question given back, or a copied line gets a plain request for an answer of the student's own.",
   "kind": "adopted rule",
   "found_by": "The animated player's guards on unmarked answers. Played: a keyboard-mash answer to the claim-evidence-reasoning page was refused.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "31",
     "quote": "lesson question for first thoughts: the build's guards refuse noise, and the answer is kept, not marked."
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "252",
     "quote": "gibberish: \"That is not an answer yet. Write a sentence of your own.\", echo: \"That is the question. What is your answer to it?\","
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "61",
     "quote": "CER-1 refused \"asdf qwer zxcv\""
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    22,
    52
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Show a model answer only after the student's own attempt is in.",
   "kind": "adopted rule",
   "found_by": "Played in the animated player: the claim-evidence-reasoning page accepted the exact quotation, kept the reasoning, and only then showed a model answer.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "8",
     "quote": "build's guards pass (never marked), the evidence must be the text's own words; then a model answer"
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "340",
     "quote": "Practice.tsx: the writing composer with its stem chip, the answer checked, then the model's sheet of rows"
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "62",
     "quote": "accepted the exact quotation, kept the reasoning and showed a model answer."
    }
   ],
   "against": "none found",
   "scope_note": "written answers",
   "adds_to_existing": [
    29,
    22
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a lesson's driving question has to be generated, draft several, keep the open ones by rule, and keep the first one a judge finds answerable from the text.",
   "kind": "adopted rule",
   "found_by": "Texts were arriving without a question. Tests assert that a yes-or-no draft is dropped and that the choice is cached by text.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "90-91",
     "quote": "the writer drafts three, code keeps the open ones, Jev keeps the first answerable from the text"
    },
    {
     "path": "~/Projects/g9/transformer/test/server.test.mjs",
     "lines": "87",
     "quote": "a text without a question is given one: open, well formed, answerable on the judge's word, the same next time"
    },
    {
     "path": "~/Projects/g9/transformer/test/server.test.mjs",
     "lines": "94",
     "quote": "the yes-or-no draft is dropped"
    }
   ],
   "against": "none found",
   "scope_note": "universal for a lesson's driving question",
   "adds_to_existing": [
    4,
    33
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check that every option is well formed, as well as checking that the key is right and the others are wrong.",
   "kind": "adopted rule",
   "found_by": "A pause-to-check draft offered an ungrammatical option, so a check on every option's form was added.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "105-106",
     "quote": "that the keyed option is right, the others wrong, and that every option is well formed (added after a draft offered \"he is not what he am\")"
    }
   ],
   "against": "none found",
   "scope_note": "universal for choice questions",
   "adds_to_existing": [
    31
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Ask a give-away check only about the words the student is given, not about what the judge knows of the work.",
   "kind": "adopted rule",
   "found_by": "The give-away check was answered from general knowledge of the play rather than from the question's own words.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "139-140",
     "quote": "its give-away question was answered from general knowledge of Othello (now: the question's own words only)"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    18,
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a check holds a draft, tell the writer which part fails and what would plainly hold, so the correction can act on it.",
   "kind": "adopted rule",
   "found_by": "Three failures during integration: a hint check did not say which word to take out; a wrong gloss needed a correction the writer could act on; and after an unsure judge, the correction only said 'unclear'.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "140",
     "quote": "the word web's hint check did not say which word to take out;"
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "180",
     "quote": "\"follow\" glossed as loyal: the writer now gets a correction it can act on, below."
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "191",
     "quote": "it now asks for a version that plainly holds; before, it only said \"unclear\"."
    }
   ],
   "against": "none found",
   "scope_note": "universal for generate, check and correct loops",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Store a judgment that shapes what students see, such as a word's class, once it is made, so the same lesson comes out the same each time.",
   "kind": "adopted rule",
   "found_by": "In the 3D export a word's class is a judged choice. It is kept so that the same lesson exports the same files and its render is reused.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/server.js",
     "lines": "108",
     "quote": "a word in focus keeps the class Jev gave it, so the same lesson exports the same files and its render is reused"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    51,
    21
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When the answer is given after two misses, let the step finish but record and show it as given, never as accepted.",
   "kind": "adopted rule",
   "found_by": "The 3D player's reading step turned a missed checkpoint 'secure' after two attempts, so a given answer would have shown as accepted. The export patches in a separate 'given' state.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "366",
     "quote": "two tries, then the answer is given and the step completes, but a given answer is not shown as \"Accepted\""
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "373",
     "quote": "a checkpoint's answer given after two tries is not marked accepted"
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
   "statement": "Give a model or revealed answer as one way to see it, not as the only right answer.",
   "kind": "adopted rule",
   "found_by": "The wording of every reveal and model in both players' marking and in the stand-in view.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "7",
     "quote": "two tries, then the answer is given (\"Here is one way to see it:\"),"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "174",
     "quote": "Here is one position you could defend:"
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "713",
     "quote": "One strong answer"
    }
   ],
   "against": "none found",
   "scope_note": "open and written questions",
   "adds_to_existing": [
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give feedback on a piece of writing as one next step: the first part the judge is sure is missing, filled with the student's own words, and no step at all when the judge is unsure.",
   "kind": "measured",
   "found_by": "The 3D player's paragraph coach was brought over as its rules and wording. It had been a second model taking 6.6 s; it became a choice among four authored steps, which took 0.34 s, 0.48 s and 0.26 s live.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "208",
     "quote": "Secure only when all four hold; a job is called missing only on a confident no. One next step, ours."
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "99-100",
     "quote": "It is now a Jev choice among four authored steps, filled with the student's own words, and shown only when Jev is sure."
    },
    {
     "path": "~/Projects/g9/transformer/DECISIONS.md",
     "lines": "29-30",
     "quote": "the 3D build's paragraph coach (6.6 s through a second model) became a Jev choice of one next step (0.26 to 0.48 s live)."
    }
   ],
   "against": "The two versions disagree when every part holds. The 3D paragraph gives \"Zoom in on a second word from the quotation and say what it adds.\" (~/Projects/g9/transformer/src/glue/threejs-archivist.js line 240), while the claim-evidence-reasoning block gave \"a paragraph doing all three got no step (0.26 s)\" (~/Projects/g9/transformer/v02/QA.md line 102).",
   "scope_note": "written answers (claim, evidence and reasoning; analytical paragraphs)",
   "adds_to_existing": [
    55,
    50,
    14
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a lesson goes to another player, give each part that player's own screen where one exists, and list each part it cannot show, with the reason, rather than forcing it onto a screen built for something else.",
   "kind": "adopted rule",
   "found_by": "One lesson was exported to two existing players. Blocks with no native screen were listed with a reason: at first the evidence hunt and the comparison in the animated player; later compare, film, say it back and debate in the 3D player.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "2",
     "quote": "Blocks map to its native nodes where one exists; the rest are listed, not forced."
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "18",
     "quote": "The rest are listed, not forced."
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "40-41",
     "quote": "The evidence hunt and the comparison were listed, not forced, as they have no screen of their own yet."
    }
   ],
   "against": "One block was put on another kind's screen anyway: \"a key-term page used as a choice card (the line as the term, the lines before it under it), until\" / \"it has a screen of its own\" (~/Projects/g9/transformer/src/glue/animated.js lines 15-16).",
   "scope_note": "lessons drawn by more than one player",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A stand-in view that plays a part another player cannot draw must keep the same gates: one played a film straight through with every question listed under it.",
   "kind": "adopted rule",
   "found_by": "On the 3D tab, the film played in the stand-in view under the frame straight through, with every question listed beneath it. That view now stops at each question.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "184-185",
     "quote": "That view now stops the same way; before, the film played straight through with every question listed under it."
    },
    {
     "path": "~/Projects/g9/transformer/web/app.js",
     "lines": "580",
     "quote": "draws the rest: blocks the chosen build has no screen for, blocks still being made, and everything while a render"
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "378",
     "quote": "Films.tsx UnitFilm, plainly: the film stops at each of its questions, a seek past the next one comes back to it,"
    }
   ],
   "against": "none found",
   "scope_note": "lessons drawn by more than one player; any fallback view",
   "adds_to_existing": [
    17,
    41
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Another player may wrap content in fixed labels of its own, such as a speaker, an act and scene, or a theme word; show each only where it is true of the lesson being shown.",
   "kind": "adopted rule",
   "found_by": "Lessons were rendered in two players that were built for one play. One player's quote card names its own play's speaker beside any reference; the other's pages printed its own act and scene, its big-idea label, and its theme word on the key-word cards.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "212",
     "quote": "the build's quote card names Iago beside any reference."
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "374",
     "quote": "no act and scene for a text that has none"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "261",
     "quote": "its key-word cards say \"Link to deceit\": our links go on them only when that is our centre too"
    }
   ],
   "against": "none found",
   "scope_note": "lessons drawn by more than one player",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Test a marker that replaces another on the old marker's own labelled answers, run through the same page code students use; count must-pass misses apart from soft ones, and run the answers again when the player changes.",
   "kind": "measured",
   "found_by": "The animated player's own answer table was run through its own page code with the new judge answering: 43 answers, 0 hard fails, 1 soft miss. After the player moved commits, it was run again: 0 hard fails, 1 soft miss.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/ops/judge-table.sh",
     "lines": "2",
     "quote": "The animated build's own answer table (its scripts/judge-test.ts), run through its own page code"
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "54",
     "quote": "43 answers, 0 hard fails, 1 soft miss. 31 reached the judge, median 266 ms, slowest 437 ms"
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "77-78",
     "quote": "its answer table still gave 0 hard fails, 1 soft miss, median 261 ms."
    }
   ],
   "against": "The one soft miss came from a criterion that asked for one detail: \"came back not met where the table wants partial; the criterion asks for \"in secret\".\" (~/Projects/g9/transformer/v02/QA.md line 56).",
   "scope_note": "universal when one marker replaces another",
   "adds_to_existing": [
    35,
    51,
    41
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check every exported lesson against the receiving player's own schema, and stop the export, naming what each edit was for, when the player has changed under it.",
   "kind": "measured",
   "found_by": "The animated export was type-checked against that player's own contract, with 0 errors in the exported lesson. The 3D export's exact edits each fail by name if the player's code has changed.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "41-42",
     "quote": "Type-checked against its own `src/contract.ts` with the TypeScript compiler: **0 errors in the exported lesson**."
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "357",
     "quote": "Exact edits in the scratch copy, each found as many times as it says or the export fails, naming it (the build"
    },
    {
     "path": "~/Projects/g9/transformer/v08/README.md",
     "lines": "13",
     "quote": "**Exit criteria:** each export validates against its target's schema; an imported lesson round-trips."
    }
   ],
   "against": "The 3D player's own content checks are not yet run on exports: \"a student's words, run its checks on exports, and a screen for compare two answers.\" (~/Projects/g9/transformer/v02/QA.md line 203, under 'Still to do').",
   "scope_note": "lessons exported to other players",
   "adds_to_existing": [
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give every block a short label that is never renumbered or reused, name every automatic finding by that label, and show which labels are on screen without putting them on the student's page.",
   "kind": "adopted rule",
   "found_by": "The composer's review surface. Blocks are cited by label, the playtest line names each fault by label, and an 'On screen' line names what the players' unlabelled pages are showing.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/web/app.js",
     "lines": "87",
     "quote": "the highest number ever given per code: numbers are never renumbered or reused"
    },
    {
     "path": "~/Projects/g9/transformer/src/server.js",
     "lines": "234",
     "quote": "The composer shows the result as one line; an engine finding is named with its block's label"
    },
    {
     "path": "~/Projects/g9/transformer/web/app.js",
     "lines": "639",
     "quote": "The block labels on the build's page now on screen, over the frame and on the strip (its pages carry none)."
    }
   ],
   "against": "none found",
   "scope_note": "tools for checking lessons",
   "adds_to_existing": [
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A lesson shown in another player speaks in that player's own generic lines, read from that player, and falls back only to plain lines that never give the answer.",
   "kind": "adopted rule",
   "found_by": "Exporting to the animated player, whose lessons speak through a guide. The guide's generic lines are read live from that player's first lesson.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/sources.js",
     "lines": "50",
     "quote": "read live from its Lesson 1 so an exported lesson speaks in the build's own words."
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "249",
     "quote": "Used only where the build's own lines cannot be read (no mirror): plain, and never the answer."
    }
   ],
   "against": "none found",
   "scope_note": "lessons drawn by more than one player",
   "adds_to_existing": [
    32
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Mark an analytical paragraph on four jobs, each judged on its own: a claim that answers the question, words quoted from the text, a quoted word examined for what it suggests, and a closing link back to the question.",
   "kind": "adopted rule",
   "found_by": "The 3D player's paragraph task was brought over as its rules and wording. Evidence is settled in code; each other job is a separate judged question.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "206",
     "quote": "The student's paragraph, the build's four jobs (point, evidence, analysis, link): evidence is code (words quoted from"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "201",
     "quote": "analysis: zooms in on a word or phrase from a quotation and says what it suggests or shows"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "202",
     "quote": "link: a closing sentence that ties the paragraph back to question"
    }
   ],
   "against": "none found",
   "scope_note": "Grade 9 English analytical paragraphs (point, evidence, analysis, link)",
   "adds_to_existing": [
    33
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In a vocabulary task, accept a one-letter slip of an expected word and show the word back spelled correctly.",
   "kind": "adopted rule",
   "found_by": "Word-web and say-it-back marking. Tested: a misspelled key word is accepted and spelled back.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "176",
     "quote": "count at once, a one-letter slip of them too (spelled right back); any other word goes to Jev, generously."
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "151",
     "quote": "a slip is spelled back"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "113",
     "quote": "One real English word or short phrase (spelling slips are fine)"
    }
   ],
   "against": "none found",
   "scope_note": "vocabulary tasks; in the code the slip rule applies only to words of five or more letters",
   "adds_to_existing": [
    25
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In a word web, count any word a reader could reasonably link to the centre word (a kind of it, a sign of it, a word for someone who shows it, or what it does to people), but not a random word or a name.",
   "kind": "adopted rule",
   "found_by": "The word web's judged rule. Played in the animated player: linked words went in, and an unrelated word was struck through as 'Not about' the centre.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "187",
     "quote": "Could a Grade 9 reader reasonably link word to centre: a kind of it, a sign of it, a word for someone who shows it, or what it does to people? A random word, a name, or a word with no link does not count."
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "86-87",
     "quote": "\"two-faced\", \"liar\", \"dissembling\" and \"hypocrite\" went in (Jev through `api/judge`, or a family form), \"football\" was struck through \"Not about duplicity\""
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
     "lines": "99",
     "quote": "an unsure criterion is never a pass and never a miss. The word web's own rule is to be generous, so there an unsure"
    }
   ],
   "against": "The 3D player does not let an unsure word in: \"a confident no gets the page's own line; an unsure one is the build's offline case, never a miss\" (~/Projects/g9/transformer/src/glue/threejs-archivist.js line 190).",
   "scope_note": "vocabulary warm-ups (word web), Grade 9",
   "adds_to_existing": [
    25,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Teach key words by study first; then hide them and have each word typed back into its sentence from memory, cued by its meaning, with a nudge on the first miss and the word given on the second.",
   "kind": "adopted rule",
   "found_by": "The key-words block combines the animated player's keyword cards with the 3D player's recall.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "514",
     "quote": "memory, cued by its meaning; a miss gets a nudge, the second gives the word"
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "541",
     "quote": "Study each word and what it means. Then put them away, and put each back into its sentence from memory."
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "12",
     "quote": "a key-words deck: study the set, then each word into its gap, cued by its meaning"
    }
   ],
   "against": "none found",
   "scope_note": "vocabulary teaching",
   "adds_to_existing": [
    49,
    54
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In a worked model, show the thinking beside each move, and have the student rebuild one of its sentences blank by blank, with a wrong pick staying out.",
   "kind": "adopted rule",
   "found_by": "The worked-model block, as it appears in the stand-in view and in both players.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "583",
     "quote": "Practice.tsx Model, plainly: the quotation unpicked (GuidedScreens), the sentence rebuilt blank by blank (Rebuild:"
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "584",
     "quote": "a wrong pick goes red and stays out), then the paragraph with the guide's thinking beside each move"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "331",
     "quote": "Now the model is hidden. Rebuild sentence"
    }
   ],
   "against": "none found",
   "scope_note": "worked examples",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In a debate, push back once on the side the student took, only when the judge is sure which side that is, then offer a position they could defend, without a grade.",
   "kind": "adopted rule",
   "found_by": "The debate block in the stand-in view and its export to the animated player.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "642",
     "quote": "Practice.tsx Evaluate: the question, a position and a reason; one push-back for the side taken, then a position"
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "663",
     "quote": "a side Jev is sure of gets its push-back, which the next answer replies to"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "172",
     "quote": "Answers the other reading: says why someone could see it the other way, and answers them. One clause is enough."
    }
   ],
   "against": "In the animated player the debate is judged on three criteria, with nudges and two tries: \"You took a side, gave a reason from the text, and answered the other reading.\" (~/Projects/g9/transformer/src/glue/animated.js line 174).",
   "scope_note": "argument and evaluation tasks",
   "adds_to_existing": [
    22,
    25
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Leave a line with a slur out of everything staged or voiced, including the context shown around a quotation and any card built on that line.",
   "kind": "adopted rule",
   "found_by": "The 3D player's list of lines that are never staged or voiced, read at run time. Such lines are left out of a model's context lines and out of word-in-focus cards.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "211",
     "quote": "line never staged is left out), the moment, the meaning and the words"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "183",
     "quote": "the 3D build never stages this line"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs.js",
     "lines": "79",
     "quote": "Without the mirror there is none, and the Jev question carries the guard."
    }
   ],
   "against": "The transformer's own word in focus may still explain the slur: \"a word in focus may gloss the slur as an insult\" (~/Projects/g9/transformer/test/laws.test.mjs line 153).",
   "scope_note": "texts that contain slurs",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Ask the lesson's question at the start for first thoughts, which are kept and never marked, and ask it again at the end, saving the second answer beside the first.",
   "kind": "adopted rule",
   "found_by": "The learning-question block, as it appears in the animated player and the stand-in view.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "468",
     "quote": "be kept, never marked; at the end of the lesson it is answered again, saved beside the first"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "141",
     "quote": "Saved, beside your first thoughts from the start of the lesson."
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "508",
     "quote": "One sentence. There is no wrong answer yet."
    }
   ],
   "against": "The 3D export leaves out the return at the end: \"the learning question's notes on its phrases; its return at the end of the lesson is a closing step, not exported\" (~/Projects/g9/transformer/src/glue/threejs-render.js line 234).",
   "scope_note": "universal",
   "adds_to_existing": [
    22,
    52
   ],
   "name_bearing_source": false
  },
  {
   "statement": "One block can become a different task in each player (a choice asked open, a tapped line asked as a written quotation), and whether results from different players can be compared item for item is not known.",
   "kind": "open question",
   "found_by": "Reading how the two players and the stand-in view draw the same blocks.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "8",
     "quote": "a reading checkpoint: which words show the claim, quoted (settled on the quotation in code)"
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "260",
     "quote": "Tap the line in the text, on the left."
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "7",
     "quote": "a reading checkpoint, asked open: the options go, the right one is what a secure answer shows"
    }
   ],
   "against": "none found",
   "scope_note": "lessons drawn by more than one player",
   "adds_to_existing": [
    42,
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "One lesson can follow different marking rules in different players (how many tries, whether earlier tries count, what an unsure judge does), and one rule set across players is not yet in place.",
   "kind": "open question",
   "found_by": "Reading both players' marking adapters side by side.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "68",
     "quote": "source, max_tries: 3, criteria, misreadings: [], lines:"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "130",
     "quote": "Taking answer on its own, does the student say this, in meaning? Any wording counts, and a short answer that says it is enough:"
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "127-129",
     "quote": "in the 3D build it is its own offline case (not an attempt, the answer kept), in the animated build's pages the student is told it could not be checked (its generous word web takes the word), in our view it stays pending."
    }
   ],
   "against": "The written checks that the animated export adds do follow the 3D player's release rule: \"two tries, then the answer (the 3D build's release rule), for the written checks this file adds\" (~/Projects/g9/transformer/src/glue/animated.js line 42).",
   "scope_note": "lessons drawn by more than one player",
   "adds_to_existing": [
    49,
    25,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A rubric can list a question's likely misreadings, each checked on its own and answered when nothing else is met, but no exported question lists any yet.",
   "kind": "open question",
   "found_by": "The animated player's rubric format carries misreadings, but every rubric the transformer exports leaves them empty.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
     "lines": "87",
     "quote": "Does answer show this misreading:"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
     "lines": "104",
     "quote": "const misreading = met.size || unsure.length ? null :"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "68",
     "quote": "misreadings: [],"
    }
   ],
   "against": "none found",
   "scope_note": "open questions marked with a rubric",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A step a person edits by hand should be checked again before it plays, just like a made step; the editor that does this is planned, not built.",
   "kind": "open question",
   "found_by": "The planned editor stage.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v03/README.md",
     "lines": "8",
     "quote": "- Undo and redo; scene files saved and versioned; edit a baked step by hand and re-check only that step."
    }
   ],
   "against": "none found",
   "scope_note": "universal for authoring tools",
   "adds_to_existing": [
    39
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A new kind of block should count as ready only when it is made and passes on more than one sample text, or is held with its reason, and every kind should be shown made on the same text side by side; this is planned, not built.",
   "kind": "open question",
   "found_by": "The planned component-library stage.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v04/README.md",
     "lines": "17",
     "quote": "**Exit criteria:** every component is ready on both samples, or held with a reason; the gallery renders them all."
    },
    {
     "path": "~/Projects/g9/transformer/v04/README.md",
     "lines": "15",
     "quote": "A gallery shows every component baked on the same text."
    },
    {
     "path": "~/Projects/g9/transformer/v04/README.md",
     "lines": "14",
     "quote": "Each component carries: a data schema, editor hints, a writer prompt, code checks, judge checks, runtime behaviour"
    }
   ],
   "against": "none found",
   "scope_note": "universal for generators of question types",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A student model should learn only from recognition steps, never from a student's own words, and should adapt only after three observations; this is planned, not built.",
   "kind": "open question",
   "found_by": "The planned director stage.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v05/README.md",
     "lines": "10",
     "quote": "- Own words are never marked; the director reads only recognition steps."
    },
    {
     "path": "~/Projects/g9/transformer/v05/README.md",
     "lines": "5",
     "quote": "A student model: demonstrated accuracy per skill, with confidence; never adapt on fewer than three observations"
    }
   ],
   "against": "none found",
   "scope_note": "adaptive lessons",
   "adds_to_existing": [
    22,
    27,
    52
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Reading lessons may follow a fixed sequence written as a ruleset (first-read checks, then close reading, then analysis, then writing), measured with scripted readers before any student sees it; this is planned, not built.",
   "kind": "open question",
   "found_by": "The planned director stage.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v05/README.md",
     "lines": "9",
     "quote": "reading sequences (first-read checks, close reading, analysis, writing)"
    },
    {
     "path": "~/Projects/g9/transformer/v05/README.md",
     "lines": "12",
     "quote": "**Exit criteria:** sequencing measured with personas before any student sees it."
    }
   ],
   "against": "none found",
   "scope_note": "reading lessons (Grade 9 English)",
   "adds_to_existing": [
    34,
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Full modelling, comparative judgement and faded non-examples are planned as lesson procedures; of these, only comparing two answers exists as a block.",
   "kind": "open question",
   "found_by": "The planned director and component-library stages.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v05/README.md",
     "lines": "8",
     "quote": "Procedures as rulesets: full teacher modelling, comparative judgement and faded non-examples"
    },
    {
     "path": "~/Projects/g9/transformer/v04/README.md",
     "lines": "11",
     "quote": "- **Judge:** compare two answers ✓, faded non-example, rank the evidence."
    }
   ],
   "against": "none found",
   "scope_note": "Grade 9 lessons",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a text is imported, map where each question's evidence lies, rank glossary candidates by the knowledge they carry, and note the context the first lines need; this is planned, not built.",
   "kind": "open question",
   "found_by": "The planned asset-pipeline stage.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v06/README.md",
     "lines": "5-6",
     "quote": "evidence maps per question; glossary candidates ranked by knowledge carried; context points (what the first lines need)."
    }
   ],
   "against": "none found",
   "scope_note": "universal for text-based lessons",
   "adds_to_existing": [
    54,
    9,
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In read-aloud, light each line as it is heard, under one play-pause control fixed at the top, and make the page read well with reduced motion on; this is planned, not built.",
   "kind": "open question",
   "found_by": "The planned timeline and animation stage.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v07/README.md",
     "lines": "5",
     "quote": "- Audio-synced reading: one play and pause control fixed at the top, text moving under it, each line lit as it is"
    },
    {
     "path": "~/Projects/g9/transformer/v07/README.md",
     "lines": "11",
     "quote": "**Exit criteria:** a scene plays with synced audio and its animations, and reads well with reduced motion on."
    }
   ],
   "against": "none found",
   "scope_note": "audio-supported reading",
   "adds_to_existing": [
    15,
    38,
    10
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Bind every shipped file to the checks it passed, and refuse the file if its bytes change; this is planned for the web player.",
   "kind": "open question",
   "found_by": "The planned build-targets stage.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v08/README.md",
     "lines": "5-6",
     "quote": "a standalone bundle with a manifest that binds the files to their checks (the engine's bundle rule: changed bytes are refused)."
    }
   ],
   "against": "none found",
   "scope_note": "universal for delivery",
   "adds_to_existing": [
    37,
    39
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every judged check should show its measured precision beside it, using labels people gave turned into test cases; today the seed sets measure nothing.",
   "kind": "open question",
   "found_by": "The planned quality stage; today calibration has seed sets only.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v09/README.md",
     "lines": "6",
     "quote": "- Calibration: reviewer labels become test cases; every judged check gets a measured precision and recall."
    },
    {
     "path": "~/Projects/g9/transformer/v09/README.md",
     "lines": "10",
     "quote": "**Exit criteria:** every judged check reports its measured precision beside it."
    }
   ],
   "against": "\"- Calibration has seed sets only: it proves the wiring and measures nothing until people label examples.\" (~/Projects/g9/transformer/README.md line 111).",
   "scope_note": "universal",
   "adds_to_existing": [
    35
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Re-run saved lessons as a regression suite whenever a prompt or a model changes, with a report card per lesson; this is planned, not built.",
   "kind": "open question",
   "found_by": "The planned quality stage.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v09/README.md",
     "lines": "7",
     "quote": "- Regression suites of saved scenes, re-run when a prompt or a model changes; a report card per lesson."
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    51,
    39
   ],
   "name_bearing_source": false
  },
  {
   "statement": "It is not yet known whether any play signals (time to answer, hesitation, glossary taps, replays) say anything about a reader; they are planned but not collected.",
   "kind": "open question",
   "found_by": "The planned quality stage.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v09/README.md",
     "lines": "8",
     "quote": "- Telemetry: time to answer, hesitation, glossary taps, replays."
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    30,
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep each decision a person makes on a lesson (approve, edit or hold) together with its reason, and keep versions and diffs for each lesson; this is planned, not built.",
   "kind": "open question",
   "found_by": "The planned scale stage.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v10/README.md",
     "lines": "6",
     "quote": "- Versions and diffs per scene; an educator review queue (approve, edit or hold, with the reason kept)."
    }
   ],
   "against": "\"- No lesson has been reviewed by a person or used by a student.\" (~/Projects/g9/transformer/README.md line 120).",
   "scope_note": "universal",
   "adds_to_existing": [
    24,
    21
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Sweep a whole unit for consistent terms, glossary priorities and key quotations; today each lesson keeps one set of key words, and a second set is left out rather than reconciled.",
   "kind": "open question",
   "found_by": "The planned scale stage. Today the animated player keeps one set of key words per lesson and lists a second set.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v10/README.md",
     "lines": "7",
     "quote": "- Consistency sweeps across a unit: terms, glossary priorities, key quotations."
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "101",
     "quote": "the build keeps one web per lesson (its words and its key words are the lesson's), so a second is listed"
    },
    {
     "path": "~/Projects/g9/transformer/README.md",
     "lines": "114",
     "quote": "- Key words are not seeded from the word web's words."
    }
   ],
   "against": "none found",
   "scope_note": "units of lessons",
   "adds_to_existing": [],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
   "lines": "6",
   "quote": "its reading sections, cut so that each checkpoint comes right after the lines it asks about"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "105",
   "quote": "question is answered by what has been said by its stop"
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
   "lines": "182",
   "quote": "its word is not in its line as written"
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/server.js",
   "lines": "211",
   "quote": "the text is kept by its hash, so the judge endpoint can settle quotations against it in code"
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "136",
   "quote": "the build marks a phrase where the question has it, word for word"
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
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "138-139",
   "quote": "the open check's leak rule was stricter than the animated build's (a hint may quote the line to read);"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "182-183",
   "quote": "a seek past an open question is pulled back."
  },
  {
   "truth": 19,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "32",
   "quote": "Rubrics carry source \"transformer:<text key>\" so the judge endpoint (animated-judge.js) can find the text."
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
   "lines": "11",
   "quote": "Every decision is appended to runs/marking/<rubric id>.jsonl, for replay."
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "32-33",
   "quote": "Only that step is used, never its verdict, so the answer stays unmarked."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/README.md",
   "lines": "167",
   "quote": "a console of judgments, a profiler, for whoever builds the engine; never shown to reviewers"
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
   "lines": "83",
   "quote": "Taking answer together with earlier_answers, does the student say this, in meaning (any wording counts):"
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "56-57",
   "quote": "Its ladder runs on its authored lines, and a criterion met on an earlier try still counts."
  },
  {
   "truth": 25,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
   "lines": "130",
   "quote": "Taking answer on its own, does the student say this, in meaning? Any wording counts, and a short answer that says it is enough:"
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "131-132",
   "quote": "a slur guard on lines a student is asked to perform (the 3D build's own list, read at run time; a Jev question);"
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "29",
   "quote": "Nothing a student needs to work out is on screen before they answer: the key-term card's \"meaning\" holds the context."
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "63-64",
   "quote": "the word-in-focus card showed the meaning before the question; direct the line showed what the speaker wants before the pick;"
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs.js",
   "lines": "4",
   "quote": "its house rules for every line a student reads (no praise, no \"!\", one question while the student still"
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "66",
   "quote": "feedback opened with \"This is correct;\" under the build's own YES;"
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/animated-judge.test.mjs",
   "lines": "95",
   "quote": "a reading check's reply is a question, as the build requires"
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
   "lines": "31",
   "quote": "One batched Jev decision; per question id: the answer when it passes the support gates, else null (unsure)."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "193",
   "quote": "debate (the Grade 9 close: mimicry, then evaluation), then the learning question again"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v04/README.md",
   "lines": "12",
   "quote": "- **Transfer:** unseen lines, key quotations."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "136",
   "quote": "Calibration harness and seed sets (test/calibration/, seed only: they prove the wiring, measure nothing);"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v07/README.md",
   "lines": "8-9",
   "quote": "reduced motion respected everywhere."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "69-70",
   "quote": "saved blocks are shown at once and re-asked of the server, so a block an older maker made is made again (all six re-made, ready on the first or second try)."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/web/app.js",
   "lines": "832",
   "quote": "when nothing changed, and a block made by an older maker is made again"
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/DECISIONS.md",
   "lines": "12-13",
   "quote": "A reviewer sees the lesson as a student meets it, with a short identifier on every block (`QC-1`, `EH-2`) to cite;"
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "46-47",
   "quote": "speaker names only where a speech starts, fixed after the first render showed them on every line"
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "173",
   "quote": "its evaluate node shows the last try's reply and not the reveal, so the model position is in that reply too"
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/web/lesson.js",
   "lines": "4",
   "quote": "Class names and nesting follow the build's src/nodes (Reading, Practice, Opening) and src/components; no style of ours."
  },
  {
   "truth": 41,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/web/app.js",
   "lines": "626",
   "quote": "the 3D build's app takes its route in the hash; review=1 opens every step, so a chip can go straight to its block"
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/web/app.js",
   "lines": "692",
   "quote": "Once the blocks settle, the four personas play the strip headless against an oracle built from each block's key (no"
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v05/README.md",
   "lines": "12",
   "quote": "**Exit criteria:** sequencing measured with personas before any student sees it."
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "124-125",
   "quote": "Under the strip, one line: the four personas' playtest (\"Played by 4 personas: all finished · no faults\")."
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "235",
   "quote": "Three-word runs of a line: the rules fallback's keywords, used only if the judge endpoint cannot be reached."
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "35",
   "quote": "Tested offline with a stand-in model, including a slow or failed task, which adds nothing."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/web/app.js",
   "lines": "544",
   "quote": "the number in the label tells the server which of its kind this is (QC-2 is told what QC-1 covers)"
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "64-65",
   "quote": "QC-2 was a copy of QC-1;"
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "42",
   "quote": "two tries, then the answer (the 3D build's release rule), for the written checks this file adds"
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "140-141",
   "quote": "the two-tries release did not fire in sessions (the runtime now passes the attempt count); the hunt and debate now release after two tries;"
  },
  {
   "truth": 49,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "68",
   "quote": "source, max_tries: 3, criteria, misreadings: [], lines:"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
   "lines": "9",
   "quote": "An unsure Jev is never a pass and never a miss: like no judge at all, it is the build's offline case"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
   "lines": "229",
   "quote": "developing only on a job Jev is sure is missing: unsure jobs alone are the offline case, so no revision is used up"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "141-142",
   "quote": "word classes are shown only where Jev confirmed them."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v06/README.md",
   "lines": "9",
   "quote": "Images through the TrueFoundry image route, shown only on positive evidence."
  },
  {
   "truth": 50,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "128",
   "quote": "(its generous word web takes the word)"
  },
  {
   "truth": 52,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v04/README.md",
   "lines": "8",
   "quote": "paraphrase the line (saved, never marked)"
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "64",
   "quote": "student text cited line numbers the build's reading does not show (\"in line 8\");"
  },
  {
   "truth": 54,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
   "lines": "432",
   "quote": "The word class of each word in focus as it is used in its line, for its 3D card: one Jev choice per word, and \"\""
  },
  {
   "truth": 54,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "83-84",
   "quote": "The first draft's key words were hard words from the text (\"obsequious\", \"homage\", \"peculiar\") for \"resentment\", and Jev held it;"
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
   "lines": "4",
   "quote": "evidence only, and writes no reply of its own: every word the student reads stays the rubric's."
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
   "lines": "5",
   "quote": "Jev only decides. Every reply is an authored line (the block's own feedback,"
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/DECISIONS.md",
   "lines": "29-30",
   "quote": "the 3D build's paragraph coach (6.6 s through a second model) became a Jev choice of one next step (0.26 to 0.48 s live)."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
   "lines": "9",
   "quote": "Beside the criteria Jev is asked whether the answer is aimed at whoever marks it (the Grade 3 engine's guard); a"
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "130-131",
   "quote": "a guard on answers that address the grader in every play-time Jev decision over a student's words;"
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
   "lines": "102",
   "quote": "a real line outside those goes to Jev, which must find it clear evidence on its own."
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "60",
   "quote": "\"In following him, I follow but myself\", a fair line nobody keyed, on Jev's decision;"
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/web/lesson.js",
   "lines": "684",
   "quote": "A line with each term made a hover word where it first appears, as the build's withGloss and Mimicry do."
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v06/README.md",
   "lines": "7-8",
   "quote": "each checked by a transcriber that has not seen the script and by a second recogniser before it ships."
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v07/README.md",
   "lines": "5",
   "quote": "one play and pause control fixed at the top, text moving under it, each line lit as it is"
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v05/README.md",
   "lines": "5",
   "quote": "never adapt on fewer than three observations"
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/web/lesson.js",
   "lines": "203",
   "quote": "reason under it and stays out; the right pick folds the options to that answer, with his Yes."
  }
 ]
}
```
