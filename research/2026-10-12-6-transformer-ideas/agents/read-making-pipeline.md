# read:making-pipeline

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  nono, analyse its ideas and fold them into the research results

## Result

```json
{
 "direction": "making-pipeline: how the lesson engine drafts, checks, corrects, keys and remakes a block, and how one judgment layer serves making, checking and play (transformer at commit 7acdba0)",
 "coverage": {
  "read": [
   "~/Projects/g9/transformer/src/transform.js",
   "~/Projects/g9/transformer/src/blocks.js",
   "~/Projects/g9/transformer/src/mechanics/util.js",
   "~/Projects/g9/transformer/src/house.js",
   "~/Projects/g9/transformer/src/judge.js",
   "~/Projects/g9/transformer/src/engine.js",
   "~/Projects/g9/transformer/src/question.js",
   "~/Projects/g9/transformer/src/text.js",
   "~/Projects/g9/transformer/src/analyse.js",
   "~/Projects/g9/transformer/DECISIONS.md",
   "~/Projects/g9/transformer/README.md",
   "~/Projects/g9/transformer/src/mechanics/index.js",
   "~/Projects/g9/transformer/src/store.js",
   "~/Projects/g9/transformer/src/glue/threejs.js",
   "~/Projects/g9/transformer/src/mechanics/quick-check.js",
   "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js (lines 1-12, 40-100)",
   "~/Projects/g9/transformer/src/mechanics/open-check.js (lines 1-30, 60-100)",
   "~/Projects/g9/transformer/src/mechanics/glossary.js (lines 1-90, 120-150)",
   "~/Projects/g9/transformer/src/mechanics/video-essay.js (lines 100-172)",
   "~/Projects/g9/transformer/src/mechanics/direct-the-line.js (lines 1-6, 59) and film-check.js (line 86), by grep",
   "~/Projects/g9/transformer/src/server.js (lines 110-135)",
   "~/Projects/g9/transformer/v01/README.md",
   "~/Projects/g9/transformer/v01/QA.md",
   "~/Projects/g9/transformer/v01/proof-2026-10-09.json (per-check verdicts summarised)",
   "~/Projects/g9/transformer/v02/README.md",
   "~/Projects/g9/transformer/v02/QA.md",
   "~/Projects/g9/transformer/test/transform.test.mjs",
   "~/Projects/g9/transformer/test/helpers.mjs",
   "~/Projects/g9/transformer/test/positive-evidence.test.mjs",
   "~/Projects/g9/transformer/test/quotes.test.mjs",
   "~/Projects/g9/transformer/test/text.test.mjs",
   "~/Projects/g9/transformer/test/laws.test.mjs"
  ],
  "skipped": [
   "transformer/src/mechanics: the other nine blocks in full (cer-frame, compare-paragraphs, debate, key-words, learning-question, say-it-back, word-in-focus, word-web, worked-model). Their rules belong to individual blocks, outside the making-pipeline direction; I only grepped their pipeline hooks (given, prepare, absorb, quotable, version).",
   "transformer/src/quality, src/core, src/video, src/films.js and src/glue other than threejs.js: playtest personas, runtime, film production and build adapters belong to other directions.",
   "transformer/src/providers.js and ops/: model routes, keys and the always-on service. These are infrastructure and vendor matters, excluded by the brief.",
   "transformer/v03-v11 READMEs: plans for stages not yet built, with no findings.",
   "transformer/runs/: git-ignored run outputs and decision logs (data dumps).",
   "transformer/node_modules, vendor/, web/, bin/, samples/, test/fixtures, test/calibration and the remaining test files: code, texts and fixtures with nothing for this direction beyond what I cite.",
   "~/Projects/grade3-reading/engine (the imported decide layer, where the support gates are defined): outside the transformer scope.",
   "~/Projects/learning-truths/.local/terms.txt: a list of people's names, not opened."
  ],
  "notes": "The working tree matched 7acdba0 for transformer/ (git diff was empty), so line numbers hold at that commit. Nothing was written. This subagent did not run mgr start, because that writes to the ledger and the parent session holds the task. Where tests, QA records or the v01 proof measure or exercise the making pipeline, I also cited files outside the named list: some block mechanics, server.js, glue/threejs.js, the tests, the v01 and v02 QA records and the v01 proof. Expect some overlap with the mechanics and quality directions. Two figures are my own counts from ~/Projects/g9/transformer/v01/proof-2026-10-09.json: 'one of eight' wrong options confirmed tempting (lines 53-62, 175-184, 313-322, 447-456) and 'three of eight' extra lines confirmed (lines 93-138, plus the second lesson's eight 'also' lines, all fails). I checked every quote with the normalisation used by ~/Projects/learning-truths/scripts/verify_quotes.py, and all were found. Where a JS comment wraps across lines, the quote joins the pieces with an ellipsis, which that checker accepts. Three quotes start near the end of a line, so the checker's line-proximity lookup misses them, but the quotes themselves match: v02/QA.md 64-65 'QC-2 was a copy of QC-1', DECISIONS.md 12-13 and v02/QA.md 126-127. Every cited path starts with the account's home directory. No other part of any path names a person, so name_bearing_source is false throughout. Some quotes name the judge model (Jev); it is a model, not a person, but add_records.py drops any quote that matches its names list, so check that Jev is not on it."
 },
 "candidates": [
  {
   "statement": "Settle in code every fact that code can settle, such as shape, exact quotations, lengths and give-aways, and send a draft to the judge only after it passes them, with one bounded question for each claim that code cannot settle.",
   "kind": "adopted rule",
   "found_by": "How the making loop is built. Code and house checks run first, and a draft that fails any of them is held and corrected without a judge call. Only the remaining checks go to the judge, as bounded yes-or-no questions with the evidence in their state.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "1-2",
     "quote": "For each step: the writer drafts, code checks the facts, the … judge checks the rest on positive evidence, and a failing draft gets exactly one correction pass with the reasons."
    },
    {
     "path": "~/Projects/g9/transformer/README.md",
     "lines": "56-59",
     "quote": "Code checks its shape and the facts code can settle: exact quotations, lengths, give-aways. … Jev answers one bounded yes-or-no question per remaining check, with the evidence in its state."
    }
   ],
   "against": "Checks still miss faults that reading a draft finds: \"A first live run on Othello showed two faults no check caught\" (v01/QA.md lines 40-41).",
   "scope_note": "universal",
   "adds_to_existing": [
    13,
    19
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give a failed draft one correction pass that lists every check it failed and asks for the whole draft again, run every check again on the result, start once more from a fresh draft if it still fails, and otherwise hold it with its reasons.",
   "kind": "adopted rule",
   "found_by": "The making loop. A transform makes two attempts: a draft, then one correction prompt that opens \"YOUR PREVIOUS DRAFT FAILED THESE CHECKS\" and lists each failed check's label and detail (transform.js line 20). A block runs that loop up to twice, the second time from a plain draft. Offline tests plant a failing required check (held after two attempts) and a fixable fault (ready on the second attempt). In the live v01 proof all twelve steps were ready on attempt 1. After a maker change, all six remade blocks were ready on the first or second try.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "2-3",
     "quote": "a failing draft gets exactly one correction pass with the reasons. … A step ships only as \"ready\"; otherwise it is \"held\" with what failed."
    },
    {
     "path": "~/Projects/g9/transformer/src/blocks.js",
     "lines": "1-2",
     "quote": "drafted, checked, … corrected, retried once more if it still fails, and cached"
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "70",
     "quote": "all six re-made, ready on the first or second try"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When the judge is unsure about a draft, ask for a version that plainly holds or a different choice, not for the opposite of what was written.",
   "kind": "adopted rule",
   "found_by": "Corrections after an unsure verdict used to say only \"unclear\", which gave the drafting model nothing to act on. The correction now tells a refuted check apart from one the judge could not confirm.",
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
   "scope_note": "universal",
   "adds_to_existing": [
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write every judged check as a typed question, yes or no, a choice or a score, with its passing answer fixed in advance, and let code read the verdict: it holds only when the answer clears the support gates and goes the expected way.",
   "kind": "adopted rule",
   "found_by": "The check format every block uses: an id, a label, a typed question and an expected answer. One verdict function reads each answer and returns holds, fails or unclear.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/judge.js",
     "lines": "1-2",
     "quote": "A check holds only on positive … evidence: an answer that fails the support gates is \"unclear\", never a pass."
    },
    {
     "path": "~/Projects/g9/transformer/src/judge.js",
     "lines": "20",
     "quote": "const verdict = !a.pass ? \"unclear\" : ok ? \"holds\" : \"fails\";"
    },
    {
     "path": "~/Projects/g9/transformer/README.md",
     "lines": "59-60",
     "quote": "Jev answers one bounded yes-or-no question per remaining check, with the evidence in its state. Only a confident answer the right way passes; an unsure Jev holds the block."
    }
   ],
   "against": "How sure counts as sure is untested. A required check held at p 0.6 in the first live proof (v01/proof-2026-10-09.json lines 259-262), and \"their precision is not yet measured (v04)\" (v01/QA.md line 46).",
   "scope_note": "universal",
   "adds_to_existing": [
    33,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Send every judgment, at making time and at play time, through one decision layer with the same gates, the same three verdicts and the same kept records, so that unsure means the same thing in a check, a choice and a mark.",
   "kind": "adopted rule",
   "found_by": "The engine imports the reading game engine's decide layer instead of copying it. One verdict function serves both the making checks and the runtime, and one play function serves both blocks and the lesson route. The same layer also picks the lines that matter and the lesson question.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/DECISIONS.md",
     "lines": "24-25",
     "quote": "The reading game engine's decide layer (typed decisions, support gates, logs for replay) is imported, not copied."
    },
    {
     "path": "~/Projects/g9/transformer/src/judge.js",
     "lines": "12",
     "quote": "One check's verdict from its typed answer (also used by the runtime, whose question ids are namespaced)."
    },
    {
     "path": "~/Projects/g9/transformer/DECISIONS.md",
     "lines": "26-27",
     "quote": "Every AI decision is a Jev question tailored to it, with the evidence in its state: choosing, marking, ranking and checking."
    }
   ],
   "against": "The line-focus pass keeps its own cut-off, \"a.pass && a.value >= 0.6\" (analyse.js line 16), while a yes check holds at \"a.value >= 0.5\" (judge.js line 17).",
   "scope_note": "universal",
   "adds_to_existing": [
    21,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Back every block's own handling of an unsure judge with one shared rule applied after it, so any response that would still mark a student wrong or finish a task on an unsure or absent verdict turns neutral.",
   "kind": "adopted rule",
   "found_by": "Each block says what an unsure check means for it, and a shared settle step then makes any marking or completing response neutral. An offline test plays every judged action of every block against four judges: none, one that cannot be reached, one that answers nothing usable, and one that is unsure.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/judge.js",
     "lines": "33-34",
     "quote": "A mechanic says what an unsure check means for it; any response that still … marks or completes turns neutral here: no verdict, not done, what the student gave kept."
    },
    {
     "path": "~/Projects/g9/transformer/test/positive-evidence.test.mjs",
     "lines": "1-2",
     "quote": "with no judge, a judge that cannot be … reached, or one that is unsure, no judged action of any mechanic is marked wrong or completes on the judge's word"
    },
    {
     "path": "~/Projects/g9/transformer/src/judge.js",
     "lines": "30",
     "quote": "That one could not be checked yet. It is kept, with no mark."
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    50,
    47
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Content made while its checker was absent, or from a checker that answered nothing, is unchecked: never shown as ready, never kept as a finding, and made again once the checker answers, with ready read from the checks actually run rather than from a saved label.",
   "kind": "adopted rule",
   "found_by": "Blocks made with no judge had been saved as ready. A ready block with no judge call now counts as unchecked, and an empty line focus from a judge that answered nothing is not cached. Offline tests cover each case.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/blocks.js",
     "lines": "3-4",
     "quote": "A block made with no judge is … \"unchecked\": never ready, never served as ready, and made again once a judge is present."
    },
    {
     "path": "~/Projects/g9/transformer/src/blocks.js",
     "lines": "29",
     "quote": "Ready means checked. A block saved as ready with no judge call (before \"unchecked\" existed) is unchecked too."
    },
    {
     "path": "~/Projects/g9/transformer/src/blocks.js",
     "lines": "47",
     "quote": "a judge that answered nothing found nothing: that empty focus is not kept as the text's"
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
   "statement": "Turn every fault found by reading a draft into a prompt rule and a check, with a test that the check catches it, and then make the affected blocks again.",
   "kind": "adopted rule",
   "found_by": "From the v01 and v02 QA records: a check that wrongly held a one-word quotation was fixed, with a test. A distractor no reader would choose, and a line number in student text, led to a prompt rule and an advisory check. Each held video-essay draft led to a change. An ungrammatical option led to a well-formedness check.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "39-40",
     "quote": "the exact-quotation check only accepted quotations of two or more words. The check now accepts a single word when that word is in the text, with a test for it."
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "42-43",
     "quote": "The house prompt now forbids L numbers in student-facing text, and an advisory check asks whether each wrong option would tempt a reader who skimmed"
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "176",
     "quote": "Earlier drafts that were held, and the change each led to:"
    }
   ],
   "against": "These faults are found by reading the drafts, and so far \"No lesson has been reviewed by a person or used by a student.\" (README.md line 120).",
   "scope_note": "universal",
   "adds_to_existing": [
    1,
    39
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Key every made piece by a hash of everything that shaped it, the text, the question, the kind, its place in the lesson and the version of its prompt and checks, and fetch it only by the key today's inputs give, never by a key a client sends.",
   "kind": "adopted rule",
   "found_by": "A playtest sent a saved link's first six blocks, all made before the line-number rule, and played them; three of them cited line numbers. Renders and playtests now recompute the key and take a block only if it matches.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/blocks.js",
     "lines": "17",
     "quote": "Bumped when what a maker produces changes (prompts, checks), so an old block is made again, not served."
    },
    {
     "path": "~/Projects/g9/transformer/src/server.js",
     "lines": "119-120",
     "quote": "a native render or a playtest takes a block only if it is checked under today's rules: ready, and kept under the key … this text, question, kind and number make now."
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "193-194",
     "quote": "A block made before a rule changed is not drawn, whatever key a client sends. Before this fix, a playtest sent the saved link's first six blocks, all made before the line-number rule, and played them; three cited line numbers."
    }
   ],
   "against": "The version is bumped by hand: \"Bump its version whenever its prompt or checks change, so its blocks are made again.\" (README.md lines 99-100).",
   "scope_note": "universal",
   "adds_to_existing": [
    39
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a block is made again, tie a student's saved progress to the new version's key, so progress on the old version does not carry over.",
   "kind": "adopted rule",
   "found_by": "Found and fixed in the other build's renderer: a block made again kept that build's saved progress, until the build's node ids were made to carry the block's key.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "65",
     "quote": "a block made again kept the build's saved progress (its node ids now carry the block's key)"
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
   "statement": "Make costly media such as narration and film only after a block's checks pass, only from the checked item and once per key, and fail the block if making it fails.",
   "kind": "adopted rule",
   "found_by": "The video essay's film is produced only after the block's checks pass. If production fails, the block is marked failed with the reason.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/README.md",
     "lines": "61",
     "quote": "A block with a film (the video essay) makes it only after its checks pass."
    },
    {
     "path": "~/Projects/g9/transformer/src/blocks.js",
     "lines": "85",
     "quote": "a block that makes something after it is checked (a video essay's film) makes it now, from the checked item only"
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "163",
     "quote": "The film is made only after the block passes, and once per key"
    }
   ],
   "against": "none found",
   "scope_note": "universal, wherever media is generated",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Send the student's page only the view of a checked block, never the answer key, the checks, the reasons or a model answer.",
   "kind": "adopted rule",
   "found_by": "Offline tests assert that no student view carries a key, feedback, evidence or a model answer. In play, one card showed a word's meaning before its question and another showed the speaker's aim before the pick; both were fixed.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/blocks.js",
     "lines": "127",
     "quote": "What the page receives: never the item, the checks or the reasons, and a view only for a ready (checked) block."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/index.js",
     "lines": "2",
     "quote": "view (what the student sees; never a key)"
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "6-7",
     "quote": "every mechanic's shape, code checks and judge questions, that no student view carries a key, feedback, evidence or a model answer"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Stamp every made lesson with the drafting model, the judge and the version of the judgment code that made it, so any result can be traced and re-judged.",
   "kind": "adopted rule",
   "found_by": "Each lesson records its providers and the decide layer's commit. The v01 proof names its judge and its writer, and records one judge sample per question.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "34",
     "quote": "providers: { judge: describe(judge), writer: describe(writer) }, engine: engineCommit()"
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "12-13",
     "quote": "Judge `jev-1.13.0` (Jev, through TypeSafe), writer `gemini-3.5-flash` through the TrueFoundry gateway, one sample per question."
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    37,
    21
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Put the evidence a judge may use into named fields and ask about those fields by name, such as using only the cited lines, so the question itself bounds what the judge may draw on.",
   "kind": "adopted rule",
   "found_by": "Every judge question in the blocks names the state fields it reads, such as the cited lines, the keyed option, or what the film has said by a given stop.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "68",
     "quote": "Using only evidence_lines, is the option named by keyed_answer a correct answer to the question?"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "138",
     "quote": "Given said_by_${k}, is the option named by keyed_${k} in options_${k} the right answer to question_${k}?"
    },
    {
     "path": "~/Projects/g9/transformer/src/analyse.js",
     "lines": "12",
     "quote": "Does line L${u.n} of text help a careful reader answer lesson_question?"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    18,
    19,
    2
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Have the drafting model reply in a fixed structure, with the exact number of options, a key that is an index into them and references to lines that exist, and reject a draft whose shape is off before checking what it says.",
   "kind": "adopted rule",
   "found_by": "Every block's normalize step throws on a wrong shape, and the error goes back to the drafting model as the correction's reason. An offline test plants an unusable reply.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "12",
     "quote": "Reply with JSON only, matching the shape you are given exactly."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/index.js",
     "lines": "1-2",
     "quote": "A mechanic is one module with seven parts: identity, a writer prompt, normalize (shape), … codeChecks (facts), judge (bounded questions with positive evidence), view (what the student sees; never a key)"
    },
    {
     "path": "~/Projects/g9/transformer/test/transform.test.mjs",
     "lines": "36",
     "quote": "an unusable reply is held with the reason, and no judge means unjudged, never ready"
    }
   ],
   "against": "An over-long field is cut, not rejected: \"return v.trim().slice(0, max);\" (util.js line 17).",
   "scope_note": "universal",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Draft every activity from the text in front of the student alone, and check what it claims against that text rather than against what is known of the work.",
   "kind": "adopted rule",
   "found_by": "This is in the house prompt every block starts with, and in the judge questions that test drafted narration and claims against the passage.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "7",
     "quote": "Use only what is in the text below."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "126",
     "quote": "Is everything narration_${k} says true to passage?"
    },
    {
     "path": "~/Projects/g9/transformer/src/question.js",
     "lines": "23",
     "quote": "answerable from the text alone"
    }
   ],
   "against": "Glosses add knowledge the text does not give: \"the words and short phrases a Grade 9 reader needs explained to follow it (a rank, a title, an older sense of a word, an idiom)\" (glossary.js lines 84-85).",
   "scope_note": "universal",
   "adds_to_existing": [
    4,
    14
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a draft misquotes the text, put the text's exact wording beside the misquotation in the correction, but tell a student who misquotes only that some of their words are not the text's own.",
   "kind": "adopted rule",
   "found_by": "The house quotation check uses a near-miss matcher, and each near miss carries the text's real wording into the correction. In play, a student who nearly quoted a line was asked which of their words was not the text's, was never given the wording, and their exact words were then accepted.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "87-88",
     "quote": "near finds quotations that are nearly, not exactly, the text's … get the text's wording for the correction; any other quotation that is not the text's is held too"
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs.js",
     "lines": "64",
     "quote": "line is the text's own wording, for a check or the judge, never shown to the student."
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "74-75",
     "quote": "got \"Nearly. Which of your words is not the text's own?\" (the wording is never given), then the exact words were accepted."
    }
   ],
   "against": "Without the other build's matcher there is no near miss to correct from: \"[] if its tools are absent.\" (glue/threejs.js line 64).",
   "scope_note": "universal",
   "adds_to_existing": [
    13,
    14
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Let a quotation be cut with an ellipsis only when every piece of it is the text's exact words, each checked on its own.",
   "kind": "adopted rule",
   "found_by": "The house quotation check splits an elided quotation at the ellipsis and matches each piece. Offline tests plant a fair elision, which passes, and one whose second piece is invented, which is held.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "63",
     "quote": "A quotation cut with an ellipsis whose every part is the text's own words is a fair elision, not a near miss."
    },
    {
     "path": "~/Projects/g9/transformer/test/quotes.test.mjs",
     "lines": "44",
     "quote": "each part of an elided quotation is checked on its own"
    }
   ],
   "against": "A quotation containing an editorial bracket is skipped, and spans under three words are not checked for invention: \"a span with an editorial [bracket] left alone\" (util.js line 66); \"two words are too few to call a quotation\" (test/quotes.test.mjs line 43).",
   "scope_note": "universal",
   "adds_to_existing": [
    13
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Inside quotation marks, a question's own stem and options may quote only the text, the lesson question or a source the block declares, while its feedback may also echo the item's own option or claim, so no string can vouch for its own quotation.",
   "kind": "adopted rule",
   "found_by": "Feedback that tells a student an option is not what the speaker says is quoting the option, not the text. So the check keeps a pool of the item's own wording that feedback lines may quote, and checks the item's own fields against the text alone. Offline tests: an option quoted in feedback passes, a declared narration source passes, and a stem that tries to pass its own invented quotation is held.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "57-58",
     "quote": "The item's own wording, which a line of its feedback may quote: its options, stem, claim and the like (the pool rule … These are checked against the text alone."
    },
    {
     "path": "~/Projects/g9/transformer/test/quotes.test.mjs",
     "lines": "48",
     "quote": "an item's own string is checked against the text, and cannot pass its own quotation"
    },
    {
     "path": "~/Projects/g9/transformer/test/quotes.test.mjs",
     "lines": "42",
     "quote": "a source the mechanic declares (a film's narration)"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    13
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Enforce the voice of what a student reads in code after the drafting model, dropping a leading verdict, praise and extra questions and replacing semicolons and dashes that stand in for commas, but leave every quotation exactly as the text has it.",
   "kind": "adopted rule",
   "found_by": "Feedback opened with \"This is correct;\" on a screen that already showed the verdict. Every line a student reads now passes through one cleaner, tested on the other build's own cases, including a quoted line whose exclamation mark must be kept.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/house.js",
     "lines": "3-4",
     "quote": "leading verdict (\"Correct.\", \"This is incorrect;\") is dropped: both builds show the verdict themselves (YES, NOT THAT … ONE). Quotations are left exactly as the text has them."
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "29-30",
     "quote": "praise and \"!\" removed, one question while a try remains, none on the final word, a quoted line's \"!\" kept."
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "66",
     "quote": "feedback opened with \"This is correct;\" under the build's own YES"
    }
   ],
   "against": "Without the other build's mirror, its cleaners do not run at all: \"if (!available) return text;\" (glue/threejs.js line 73).",
   "scope_note": "universal",
   "adds_to_existing": [
    32,
    13
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before drafting, ask of each line whether it helps answer the lesson question, rank the lines in code, and point the drafting model at the top ones as a preference, not a limit.",
   "kind": "adopted rule",
   "found_by": "The line-focus pass runs once per text and question. Its top eight lines go into every block's prompt, and its pool also feeds the search for other lines that prove a claim.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/analyse.js",
     "lines": "1-2",
     "quote": "One bounded yes/no per line, the whole text in the state for context, … at most 40 questions a call. Code ranks; only answers that pass the support gates count."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "41",
     "quote": "The lines most relevant to the lesson question are ${top}. Prefer them, but use any line that fits the task."
    }
   ],
   "against": "On short texts it barely narrowed anything: \"46 lines judged relevant to the question\" (v01/QA.md line 31) of a 75-line scene, and \"13 lines judged relevant to the question\" (line 32) of a 14-line poem (the line counts are asserted in test/text.test.mjs lines 11 and 17).",
   "scope_note": "universal",
   "adds_to_existing": [
    33
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check in code that a second block of a kind is not the same point as an earlier one, the same words or, for a sentence of four words or more, at least 60 percent of all their distinct words in common, besides telling the drafting model what the earlier one covers.",
   "kind": "adopted rule",
   "found_by": "A second quick check came out as a copy of the first. Each block now records what it is about; later blocks of the same kind are told those points and checked against them in code.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "49",
     "quote": "The same point, near enough: equal, or (for a sentence) most of its words shared."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "55",
     "quote": "return [...sa].filter((w) => sb.has(w)).length / new Set([...sa, ...sb]).size >= 0.6;"
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "64-65",
     "quote": "QC-2 was a copy of QC-1"
    }
   ],
   "against": "The code test only compares words, while the prompt asks for more: \"do not repeat or reword those\" (util.js line 141).",
   "scope_note": "universal",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Where vetted, authored material for the text already exists, use it unchanged instead of drafting it, and keep the judge's reading of it for review without letting that reading hold it back.",
   "kind": "adopted rule",
   "found_by": "A text that is a section of the other build carries its own glossary. The block passes those terms and notes through without drafting, still runs the judge over them, and requires only drafted notes to pass.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "4-5",
     "quote": "A section of the 3D build carries its own glossary: its terms and notes are passed … through unchanged, each where its line mark puts it, and nothing is drafted."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "121",
     "quote": "the 3D build's own notes are its content: Jev's reading of them is kept, and never holds them"
    },
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "56",
     "quote": "const given = attempt === 1 && mech.given ? mech.given(ctx) : null;"
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give every block in a lesson a short, stable label that anyone checking the lesson can cite, and show the lesson to them as a student meets it.",
   "kind": "adopted rule",
   "found_by": "The composer's surface decision: blocks are made out of sight, each carries a label such as QC-1, and the scripted playtest names any fault by block.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/DECISIONS.md",
     "lines": "12-13",
     "quote": "A reviewer sees the lesson as a student meets it, with a short identifier on every block (QC-1, EH-2) to cite"
    },
    {
     "path": "~/Projects/g9/transformer/README.md",
     "lines": "24-25",
     "quote": "four scripted personas (strong, guesser, stuck, adversarial) play the lesson, and any fault is named by block."
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    41,
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give every test run of a content maker its own empty store, or a test can pass on something an earlier run made instead of on what the maker makes now.",
   "kind": "adopted rule",
   "found_by": "The block caches of every test run went to one shared temp folder, so a test could read a block that an earlier run had made.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "5-6",
     "quote": "Each test now has its own store: before, the block caches of every test run went to one shared temp folder, so a test could read a block an earlier run had made."
    }
   ],
   "against": "none found",
   "scope_note": "universal",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check whether a question's own wording gives its answer away separately from whether someone who knows the work could answer it: a judge asked without that limit answered from general knowledge of a famous text.",
   "kind": "adopted rule",
   "found_by": "Found and fixed during integration: the open check's give-away question was answered from general knowledge of the work. It now tells the judge to judge only the question's wording.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "139-140",
     "quote": "its give-away question was answered from general knowledge of Othello (now: the question's own words only)"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "87",
     "quote": "Judge only the wording of q, not what a reader may already know about the work."
    }
   ],
   "against": "By design, the narrowed check passes a question that anyone who knows the work can answer: \"a famous text's answer is known to anyone who knows the work, which is no give-away of the question's\" (open-check.js line 86).",
   "scope_note": "universal; matters most for famous works",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Judge the keyed answer from the cited lines alone, so the cited evidence is enough by itself, and judge each wrong option against the whole text, so nothing elsewhere makes it right.",
   "kind": "adopted rule",
   "found_by": "The quick check's required judge checks: one that the key is right, judged from the cited lines, and one per wrong option, judged from the whole text.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "68",
     "quote": "The keyed answer is right, judged from the cited lines"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "70",
     "quote": "is wrong, judged from the whole text"
    }
   ],
   "against": "The judge is shown which option is keyed instead of finding the answer blind. Another block makes the judge pick for itself: \"The judge, reading the same lines around it, must pick the same delivery.\" (direct-the-line.js line 2).",
   "scope_note": "choice questions about a text",
   "adds_to_existing": [
    31,
    11
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make each wrong option believable to a reader who skimmed, yet ruled out by the text.",
   "kind": "adopted rule",
   "found_by": "A first live run produced a distractor no reader would choose. The prompt now asks for wrong options that would tempt a skimmer, and an advisory check asks whether each would seem believable rather than obviously absurd.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "23-24",
     "quote": "Exactly one is right given the text; the other two are tempting to a skimmer but the text rules them out."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "75",
     "quote": "seem believable to a Grade 9 reader who skimmed the text, rather than obviously absurd?"
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "40-41",
     "quote": "A first live run on Othello showed two faults no check caught: a quick-check distractor no reader would choose"
    }
   ],
   "against": "The judge's plausibility verdicts have not been calibrated: \"their precision is not yet measured (v04)\" (v01/QA.md line 46).",
   "scope_note": "choice questions",
   "adds_to_existing": [
    31
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A check that only advises does not stop its fault from shipping: in one live run the judge confirmed only one of eight wrong options as tempting, and all four choice blocks shipped as ready.",
   "kind": "measured",
   "found_by": "The v01 live proof: one judge sample per question, two texts, a quick check and a word-in-focus block on each. The advisory tempting-option verdicts were: first quick check, fails p 0.37 and unclear p 0.53; first word in focus, unclear p 0.46 and fails p 0.37; second quick check, unclear p 0.44 and holds p 0.6; second word in focus, fails p 0.35 and fails p 0.2 (v01/proof-2026-10-09.json lines 53-62, 175-184, 313-322, 447-456). Every block was ready on attempt 1, because only required checks hold a block (transform.js line 76).",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "43",
     "quote": "on Ozymandias it flagged two distractors as not tempting."
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "26",
     "quote": "| ozymandias | `word-in-focus` | ready | 1 | 5/5 | 4/4 | 0/2 | 4.1 |"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "74",
     "quote": "would tempt a reader who skimmed`, required: false"
    }
   ],
   "against": "Nobody knows whether the judge's \"not tempting\" verdicts are right: \"their precision is not yet measured (v04)\" (v01/QA.md line 46).",
   "scope_note": "choice questions; one live run of twelve blocks on two texts",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep the options a similar length, so none stands out: the longest at most 2.2 times the shortest.",
   "kind": "adopted rule",
   "found_by": "The quick check's prompt asks for options of similar length, and a code check holds any set whose longest option is more than 2.2 times its shortest, measured in characters.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "24",
     "quote": "Keep the options a similar length."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "55",
     "quote": "No option stands out by length\", Math.max(...lens) <= 2.2 * Math.min(...lens)"
    }
   ],
   "against": "none found",
   "scope_note": "choice questions (length measured in characters)",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check that every option is grammatical, well-formed English, since a drafted option can bend a quotation into broken grammar.",
   "kind": "adopted rule",
   "found_by": "The film-with-checks block gained a well-formedness question after a draft offered an ungrammatical option made from a reworded quotation.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "106",
     "quote": "every option is well formed (added after a draft offered \"he is not what he am\")"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/film-check.js",
     "lines": "86",
     "quote": "Is every option in options_${k} grammatical, well-formed English?"
    }
   ],
   "against": "none found",
   "scope_note": "choice questions",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Widen a key while making the item by asking the judge whether other likely lines prove the claim just as well and accepting those it confirms: in one live run it confirmed three of eight candidate lines for one claim and none of eight for another.",
   "kind": "measured",
   "found_by": "At making time the evidence hunt checks up to eight other lines from the line-focus pool, as advisory checks, and adds any it confirms to the accepted set. In the v01 proof, on one text three held (p 0.65, 0.62 and 0.65) and five failed (v01/proof-2026-10-09.json lines 93-138); on the other text all eight failed.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
     "lines": "1-2",
     "quote": "The judge confirms every keyed line … and also finds other lines that prove the claim just as well, so a fair answer is never marked wrong."
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "19",
     "quote": "| othello-1-1 | `evidence-hunt` | ready | 1 | 3/3 | 1/1 | 3/8 | 1.4 |"
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "25",
     "quote": "| ozymandias | `evidence-hunt` | ready | 1 | 3/3 | 3/3 | 0/8 | 1.5 |"
    }
   ],
   "against": "The pool is capped at eight lines, so a fair line outside it is left to the play-time check: \".filter((i) => !keyed.has(i)).slice(0, 8);\" (evidence-hunt.js line 53).",
   "scope_note": "questions where more than one line may be right",
   "adds_to_existing": [
    7
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Word a claim or question differently from the line that answers it, so it cannot be answered by matching words: hold a claim that shares five or more consecutive words with its keyed line.",
   "kind": "adopted rule",
   "found_by": "The evidence hunt's code checks hold a claim that copies its line (a shared run of five words or more) and a hint that quotes the line (a run of four or more).",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
     "lines": "46",
     "quote": "check(\"claim-no-copy\", \"The claim does not copy the line\", run < 5,"
    }
   ],
   "against": "none found",
   "scope_note": "questions that point to evidence in a text",
   "adds_to_existing": [
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "For a reading or an argument, which is neither true nor false, check that nothing it says goes against the text and that a careful reader could defend it from the passage as an answer to the question, and keep true-to-the-text checks for plain claims.",
   "kind": "adopted rule",
   "found_by": "Held video-essay drafts: an argument's narration failed a check that it was true, and one reading could not be defended from the lines. Argument beats now get a no-contradiction check, and their points keep close to the lines' own words.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "123",
     "quote": "two readings pose a question, which is neither true nor false: there, nothing said may go against the passage"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/video-essay.js",
     "lines": "132",
     "quote": "Could a careful reader defend left_${k} from passage, as an answer to lesson_question?"
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "177",
     "quote": "an argument beat's narration that was not \"true\": it now has only to say nothing the text goes against"
    }
   ],
   "against": "none found",
   "scope_note": "interpretive or argued content",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "What a student reads at a film's stops speaks of what the film said or showed, never of how it was made: no production words such as beat, cue, caption or frame.",
   "kind": "adopted rule",
   "found_by": "A drafted feedback line referred to \"the second frame\". A code check now holds any question, option or feedback at a stop that uses those words.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "111-112",
     "quote": "What a viewer reads at a film's stops (the questions, options and feedback) speaks of the film, never of how it is … made: no beat, cue, caption or frame."
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "179",
     "quote": "an untrue feedback line, \"the second frame\", and wrong-option feedback that named the answer: new checks, below;"
    }
   ],
   "against": "none found",
   "scope_note": "lessons with film or other produced media",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A guard against words aimed at the marker must count commands quoted or retold from the text as part of an answer, since characters give orders, and only a confident yes from it may set an answer aside.",
   "kind": "adopted rule",
   "found_by": "Plays are full of imperatives, so an answer that quotes a character's command could look like an instruction to the marker. The guard's question now says such words do not count, and an offline test shows that a confident yes leaves the words unmarked and unsaved.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "133-134",
     "quote": "only a confident yes acts, and then the words are not an answer. Plays are full of commands, so a command … quoted or retold from the text is said not to count."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "135",
     "quote": "Words quoted or retold from the text, a character's commands among them, are part of an answer and do not count."
    },
    {
     "path": "~/Projects/g9/transformer/test/positive-evidence.test.mjs",
     "lines": "118",
     "quote": "words aimed at the marker are no answer, and no verdict"
    }
   ],
   "against": "none found",
   "scope_note": "texts full of imperatives, such as plays",
   "adds_to_existing": [
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A gloss may name an offensive word as the insult it is, but never ask a student to say or perform a line that contains one: hold such a line by a known list where one exists and by a judged question for any text.",
   "kind": "adopted rule",
   "found_by": "One block has students perform a line. The guard reads the other build's list of lines it never stages at run time and adds a judge question with the line in its state. Tests plant a dirty verdict and the never-staged line.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "106-107",
     "quote": "A gloss may name an epithet as an insult, as the animated … build's gloss does; a student is never asked to perform one."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "105",
     "quote": "for any text, one Jev question with the line in the state, so a block"
    },
    {
     "path": "~/Projects/g9/transformer/test/laws.test.mjs",
     "lines": "153",
     "quote": "a line never staged holds a direct-the-line block, in code and on the judge's word; a word in focus may gloss the slur as an insult"
    }
   ],
   "against": "The list exists only where the other build's mirror is present: \"Without the mirror there is none, and the Jev question carries the guard.\" (glue/threejs.js line 79).",
   "scope_note": "texts that contain slurs or epithets",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Cut every text into the units a question can point at, a spoken line with its speaker in a play, a line in a poem, a sentence in prose, and in a play never count a stage direction as evidence or let a quotation run across one or across two speeches.",
   "kind": "adopted rule",
   "found_by": "The text parser maps every line pointer from the drafting model to spoken lines only, and the preferred quotation matcher refuses a quotation that crosses a stage direction or two speeches.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/text.js",
     "lines": "1-2",
     "quote": "A text becomes numbered units that mechanics can point at: a verse line with its speaker (drama), a line (poem), … or a sentence (prose). Stage directions are kept for display but are never evidence."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "28",
     "quote": "Writer line numbers (L numbers) -> unit indices, keeping only spoken lines."
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs.js",
     "lines": "53-54",
     "quote": "punctuation, case and apostrophes aside, never across a … stage direction or two speeches."
    }
   ],
   "against": "The fallback matcher, used when the other build's tools are absent, joins consecutive spoken lines with the directions left out: \"Find a quotation in the text. It may span consecutive lines.\" (text.js line 52).",
   "scope_note": "units: any text; directions and speeches: drama (the sources give no reason)",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A lesson's driving question is open, never yes or no, answerable from the text alone, about what the text shows or how it shows it, and short: draft several, keep the well-formed ones in code, and keep one the judge confirms.",
   "kind": "adopted rule",
   "found_by": "Texts dropped or pasted into the composer arrived without a question. The suggest-question route drafts three and filters them in code: each must end in a question mark, run to at most 26 words, not open with a yes-or-no word, and cite no line numbers. It then asks the judge whether each can be answered from the passage alone and is worth an hour's lesson.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/question.js",
     "lines": "22-23",
     "quote": "Each is open (never yes or no), answerable from the text alone, about what the text shows or how it shows it, at most 22 words, ending in \"?\"."
    },
    {
     "path": "~/Projects/g9/transformer/src/question.js",
     "lines": "1-2",
     "quote": "The writer drafts three; code keeps … the open, well-formed ones; the judge keeps the first it finds answerable from the text alone and worth a lesson"
    }
   ],
   "against": "The judge question joins two claims in one yes-or-no: \"Can question_${i} be answered from passage alone, and is it worth a Grade 9 lesson of about an hour?\" (question.js line 34). The prompt asks for at most 22 words while code allows 26 (lines 23 and 12), and the first confirmed question is kept, not the best one: \"question = qs.find((_, i) => results[i]?.verdict === \"holds\") ?? null;\" (line 35).",
   "scope_note": "a lesson's driving question for a text (here a Grade 9 lesson of about an hour)",
   "adds_to_existing": [
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write for the reader's age: for Grade 9 and older, adult and precise, with no games language and nothing that reads as written for young children.",
   "kind": "adopted rule",
   "found_by": "The house prompt every block starts with, plus an advisory judge check that a question is clear and not childish.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "6-7",
     "quote": "The tone is adult and precise: no games language, no exclamation marks, no \"Great job\", nothing that reads as written for young children."
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "78",
     "quote": "Is this question suitable for a Grade 9 student: clear, not childish, and answerable after one careful reading?"
    },
    {
     "path": "~/Projects/g9/transformer/DECISIONS.md",
     "lines": "20",
     "quote": "The mechanics and the animation are for Grade 9 and older readers"
    }
   ],
   "against": "none found",
   "scope_note": "Grade 9 and older readers",
   "adds_to_existing": [
    32
   ],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/laws.test.mjs",
   "lines": "27",
   "quote": "key shapes, each tried on a sample made here, so a law that could never fire fails too"
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/transform.test.mjs",
   "lines": "18",
   "quote": "a failing required check gets one correction pass with the reason, then the step is held"
  },
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/README.md",
   "lines": "59",
   "quote": "Jev answers one bounded yes-or-no question per remaining check, with the evidence in its state."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/README.md",
   "lines": "120",
   "quote": "No lesson has been reviewed by a person or used by a student."
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
   "lines": "77",
   "quote": "Does the wording of the question by itself reveal which option is correct, without reading the text?"
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
   "lines": "86",
   "quote": "a famous text's answer is known to anyone who knows the work, which is no give-away of the question's"
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/util.js",
   "lines": "132",
   "quote": "The Grade 3 engine's guard on a student's own words (its loop.js addresses_grader), asked beside every judgment of"
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "11-12",
   "quote": "At play time, a tapped line nobody keyed goes to the judge in one request. It is accepted only on positive evidence, and logged for review."
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
   "path": "~/Projects/g9/transformer/src/mechanics/util.js",
   "lines": "9-10",
   "quote": "so quote a few of the words instead. Anything in quotation marks is the text's own words, copied exactly, in double quotes: never put a paraphrase in quotes."
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/quotes.test.mjs",
   "lines": "59",
   "quote": "without the 3D build's mirror the quotation check still runs, on src/text.js findQuote, and never passes for lack of it"
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
   "lines": "47",
   "quote": "The hint does not quote the line"
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
   "lines": "63-64",
   "quote": "a hint may quote the text, even the line to … read (its third rung), but it uses no leak word and copies no four-word run of the reveal outside a quotation"
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/util.js",
   "lines": "122",
   "quote": "The feedback after each option, held to what the film has given by that stop"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "182-183",
   "quote": "a seek past an open question is pulled back."
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "184-185",
   "quote": "That view now stops the same way; before, the film played straight through with every question listed under it."
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/util.js",
   "lines": "122-123",
   "quote": "one Jev question a line, with the … question and the option picked beside it"
  },
  {
   "truth": 19,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/DECISIONS.md",
   "lines": "26",
   "quote": "Every AI decision is a Jev question tailored to it, with the evidence in its state"
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/README.md",
   "lines": "62",
   "quote": "Every draft, check, decision and film is kept under runs/, so any of it can be re-judged or replayed."
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/blocks.js",
   "lines": "93",
   "quote": "every try's decide records, as decide made them, so the block can be re-judged through a second judge"
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "13",
   "quote": "Own words are never marked. The claim-evidence-reasoning entity saves the answer, and the judge only shapes a note."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/blocks.js",
   "lines": "114-115",
   "quote": "with no judge, or an unsure one, a … judged action is neutral and kept for review."
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
   "lines": "100",
   "quote": "Any wording counts, and a short answer that says it is enough."
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "57",
   "quote": "a criterion met on an earlier try still counts."
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/laws.test.mjs",
   "lines": "162",
   "quote": "the judge's guard: the line is in the state, and the block ships only when the judge is sure it is clean"
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "63-64",
   "quote": "the word-in-focus card showed the meaning before the question; direct the line showed what the speaker wants before the pick"
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "135",
   "quote": "the one finding left is a gap (no idle nudge, v05)."
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/house.js",
   "lines": "1-2",
   "quote": "the 3D build's own rules (no gushing; at most one question, … none in a closing line)"
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/util.js",
   "lines": "10-11",
   "quote": "never put a paraphrase in quotes. Feedback never opens with a verdict (Correct, Incorrect, Yes, No): the lesson shows the verdict itself."
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/transform.test.mjs",
   "lines": "44",
   "quote": "word in focus takes the candidate the judge scores highest"
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/analyse.js",
   "lines": "1-2",
   "quote": "One bounded yes/no per line, the whole text in the state for context, … at most 40 questions a call. Code ranks; only answers that pass the support gates count."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/README.md",
   "lines": "111",
   "quote": "Calibration has seed sets only: it proves the wiring and measures nothing until people label examples."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/helpers.mjs",
   "lines": "1",
   "quote": "Offline stand-ins: a fixture writer and a scripted judge. They prove plumbing, never judgment quality."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v01/QA.md",
   "lines": "46",
   "quote": "bounded questions with the evidence supplied; their precision is not yet measured (v04)."
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "167",
   "quote": "WebVTT captions, a poster, and a manifest of module digests, narrator, renderer versions and file hashes."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "69-70",
   "quote": "saved blocks are shown at once and re-asked of the server, so a block an older maker made is made again"
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/blocks.js",
   "lines": "17",
   "quote": "Bumped when what a maker produces changes (prompts, checks), so an old block is made again, not served."
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "134-135",
   "quote": "its four scripted personas (strong, guesser, stuck, adversarial) play every scene headless; all four finish a 15-block Othello lesson"
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/positive-evidence.test.mjs",
   "lines": "71",
   "quote": "no judged action is marked wrong, or completes on the judge's word; each is put up for review"
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/blocks.js",
   "lines": "20-21",
   "quote": "QC-1 and QC-2 are two blocks: n is the number in the block's label, and block n is told what the blocks below it that … exist cover."
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "140-141",
   "quote": "the two-tries release did not fire in sessions (the runtime now passes the attempt count); the hunt and debate now release after two tries"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/judge.js",
   "lines": "2-3",
   "quote": "an answer that fails the support gates is \"unclear\", never a pass. Its band (the director's act, probe or … escalate) is kept, so an unsure answer can be told from a refuted one and put up for review."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "126-127",
   "quote": "an unsure Jev is never a pass and never a miss"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/positive-evidence.test.mjs",
   "lines": "121",
   "quote": "the hunt: an unsure judge gives the hint with no miss; a confident no is a miss"
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/util.js",
   "lines": "8-9",
   "quote": "Text a student reads never cites a line number (no \"L12\", no \"line 12\"): the lesson may show the text without numbers, so quote a few of the words instead."
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "64",
   "quote": "student text cited line numbers the build's reading does not show (\"in line 8\")"
  },
  {
   "truth": 54,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
   "lines": "3",
   "quote": "Jev checks every note fits its word as the line uses it, each one required, since a wrong gloss"
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/DECISIONS.md",
   "lines": "29-30",
   "quote": "the 3D build's paragraph coach (6.6 s through a second model) became a Jev choice of one next step (0.26 to 0.48 s live)."
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "99-100",
   "quote": "It is now a Jev choice among four authored steps, filled with the student's own words, and shown only when Jev is sure."
  }
 ]
}
```
