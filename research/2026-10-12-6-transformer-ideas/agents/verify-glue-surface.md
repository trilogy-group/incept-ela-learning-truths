# verify:glue-surface

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  nono, analyse its ideas and fold them into the research results

## Result

```json
{
 "direction": "glue-surface",
 "verified": [
  {
   "index": 0,
   "verdict": "keep",
   "reason": "All three quotes are verbatim at the cited lines, and the code agrees. Stems that match the phrase list on threejs-render.js line 34 are skipped (line 145). The right option is judged in meaning, in any wording (threejs-archivist.js line 86). A wrong option the judge is sure of gets its own feedback (lines 95-96). A test asserts that no options reach the page (added). Not a duplicate: #31 is about building a choice question, and this is about asking one open.",
   "statement": "A choice question can be asked open only if its stem stands without its options; the options then leave the page, the right one said in any words is the answer, and an answer that gives a wrong option gets that option's own feedback.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "33",
     "quote": "a question that only works beside its options (\"Which of these…\") is not asked open",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "7",
     "quote": "a reading checkpoint, asked open: the options go, the right one is what a secure answer shows",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "82",
     "quote": "A quick check asked open: the right option in meaning is secure; a wrong option gets that option's own feedback.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "58",
     "quote": "no options in the page",
     "verbatim": true
    }
   ],
   "against": "None found. The open-stem test is a phrase list (threejs-render.js line 34), and on the last try the answer is given in place of a wrong option's feedback (threejs-archivist.js line 94).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep",
   "reason": "The quotes are verbatim. ~/Projects/g9/transformer/src/blocks.js lines 3-4 (added) state the same rule at its source, and line 62 serves an unchecked block only while there is still no judge. It is close to the last clause of #50, but it adds the case of no judge at all and the remake. There is one gap against 'anything': the question suggester (see against).",
   "statement": "Hold back anything made while no judge could check it: mark it unchecked, keep it out of the lesson, and make it again once a judge is back.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/web/app.js",
     "lines": "363",
     "quote": "A block made with no judge to check it: muted on the strip, kept out of the lesson, made again once a judge is back.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "61",
     "quote": "made, but not yet checked: it is shown once the judge has checked it",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "126",
     "quote": "a block made with no judge is \"unchecked\", never shown;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/blocks.js",
     "lines": "3-4",
     "quote": "A block made with no judge is \"unchecked\": never ready, never served as ready, and made again once a judge is present.",
     "verbatim": true
    }
   ],
   "against": "With no judge, the question suggester takes the first well-formed draft unchecked (~/Projects/g9/transformer/src/question.js line 31, \"let question = qs[0] ?? null;\") and caches it (line 37). So it serves an unchecked question, and keeps serving it after a judge is back.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, but 'position' was wrong. The key is a hash of the maker's rule version, the text, the question, the kind and n (~/Projects/g9/transformer/src/blocks.js lines 17-26). n is the number in the block's label among blocks of its kind, not its place in the lesson. readyItems works out that key again and draws only a block that matches it (server.js lines 119-126). The QA incident (six old blocks played, three of them citing line numbers) is also evidence for #39.",
   "statement": "An item is good only for the text and the lesson question it was made from: key it on both, with its kind, its number among items of that kind and the version of the rules that made it, and draw only what is stored under today's key, whatever key a page sends.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/web/app.js",
     "lines": "38",
     "quote": "A short fingerprint of the source. A block is good only for the text and question it was made from.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/server.js",
     "lines": "119-120",
     "quote": "a native render or a playtest takes a block only if it is checked under today's rules: ready, and kept under the key this text, question, kind and number make now.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/blocks.js",
     "lines": "17",
     "quote": "Bumped when what a maker produces changes (prompts, checks), so an old block is made again, not served.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "193-194",
     "quote": "A block made before a rule changed is not drawn, whatever key a client sends. Before this fix, a playtest sent the saved link's first six blocks, all made before the line-number rule, and played them; three cited line numbers.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/server.test.mjs",
     "lines": "112",
     "quote": "made for another question: not played",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, but found_by's 'in both renders' is wrong: the animated pages send their own rubric with each answer. The rule holds in the engine's own view: test lines 47-48 (added) assert that no item, reasons, judge, code, checks or feedback reach the page. It also holds for the 3D render's feedback lines (threejs-render.js line 19). I restated it as the rule and narrowed it to what follows it; both exports are open exceptions.",
   "statement": "Send a student's page only what it shows and mark the answer on the server, so the item, its checks and its feedback lines never reach the page.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/server.test.mjs",
     "lines": "36",
     "quote": "blocks: made invisibly, cached, played; the page never sees the item or the checks",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/server.test.mjs",
     "lines": "47",
     "quote": "for (const k of [\"item\", \"reasons\", \"judge\", \"code\", \"checks\"]) assert.equal(k in b1, false, k);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/server.test.mjs",
     "lines": "48",
     "quote": "assert.equal(JSON.stringify(b1.view).includes(\"feedback\"), false);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "19",
     "quote": "with Jev, and replies only with the authored lines kept here in `marking`, which stays on the server.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "59",
     "quote": "the feedback lines are not shipped",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/server.js",
     "lines": "80",
     "quote": "Each keeps its marking (the authored lines, the text's key) beside its folder, never in it, so the",
     "verbatim": true
    }
   ],
   "against": "Neither export follows it. The animated pages carry the rubric (~/Projects/g9/transformer/src/glue/animated-judge.js line 1). They also carry each quick check's answer index and its wrong-option reasons (~/Projects/g9/transformer/src/glue/animated.js line 76, \"correct: it.answer, yes: say(it.feedback[it.answer], { final: true }) });\") and the evidence hunt's keyed lines (line 89). The 3D page's checkpoint table holds the expected answer (~/Projects/g9/transformer/test/threejs-render.test.mjs line 57, \"assert.deepEqual(check.expects, [qc.options[qc.answer]]);\").",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, but 'two renders never share progress' goes too far. The 3D progress key is exp.key, a hash of the lesson, its tables and its vocabulary (threejs-render.js line 275, added). A render's folder name also hashes the build's commit (~/Projects/g9/transformer/src/server.js line 90). So two renders of one lesson on different player commits share one progress store. Fixed to 'each version of a lesson'.",
   "statement": "Key a student's saved progress to the exact version of each question, so a remade question starts fresh, and give each version of a lesson its own progress store, apart from the player's own lessons.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "65",
     "quote": "a block made again kept the build's saved progress (its node ids now carry the block's key);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "71",
     "quote": "build keeps a student's progress by node id, and a block made again is a new question, not one already answered",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "365",
     "quote": "a progress of its own, apart from the build's and every other render",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "275",
     "quote": "const key = crypto.createHash(\"sha256\").update(JSON.stringify([lesson, tables, vocab])).digest(\"hex\").slice(0, 10);",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep",
   "reason": "The quotes are verbatim. In the 3D adapter the text's own wording appears only in the final reply (threejs-archivist.js line 52, added). The animated pages never give it (QA lines 74-75). This is a specific case of #14 and #49, kept as a rule of its own.",
   "statement": "When a quotation is nearly the text's words, say it is nearly right and ask which word is not the text's own, giving the exact wording only on the last try.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "74-75",
     "quote": "\"I follow him to serve my turn on him\" got \"Nearly. Which of your words is not the text's own?\" (the wording is never given), then the exact words were accepted.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
     "lines": "77",
     "quote": "nearly the text's words (the 3D build's matcher): say so, without giving the wording; the build checks the reply",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "144",
     "quote": "never the wording before the last try",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "52",
     "quote": "final ? ` The text has it as \"${strip(near[0].line)}\".` : ` Check the wording of \"${strip(near[0].wrote)}\" against the passage.`",
     "verbatim": true
    }
   ],
   "against": "None found. The 3D reply asks the student to check the wording of their quotation rather than asking which word is wrong.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim: both located() functions refuse a span under three words unless it is a whole line. 'Universal for quoted evidence' goes too far, because the 3D paragraph task counts two-word quotations and near ones (see against). I removed the threejs.js line 63 quote: it is about spotting near misses, not about what counts. Nothing records why the threshold is three.",
   "statement": "In an evidence hunt or a quotation criterion, a quotation counts only when it is at least three words of the text or a whole short line.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
     "lines": "33",
     "quote": "The units a quotation covers, if it is long enough to count: three words, or a whole short line.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "39",
     "quote": "The units a quotation covers, if it is long enough to count: three words, or a whole short line.",
     "verbatim": true
    }
   ],
   "against": "The 3D paragraph task counts shorter and inexact quotations: \"The quoted spans in a string, two words or more (its quotesIn: double, curly or single quotes).\" (~/Projects/g9/transformer/src/glue/threejs.js line 45); \"the text, exactly or nearly: the page puts its own wording note on a near one), the rest Jev; one sentence's job is a\" (~/Projects/g9/transformer/src/glue/threejs-archivist.js line 207).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, but the boundary rule belongs to the 3D build's matcher alone. The fallback, findQuote in src/text.js (added), searches spoken lines only and joins up to four of them whatever the speaker (lines 56-61). So it can match across a stage direction or across two speeches, and the marking adapters' located() uses it. I fixed the statement so the fallback promises only a plainer check, not the same guarantee. This refines #13.",
   "statement": "Match a quotation to the text with punctuation, case and apostrophes set aside, never across a stage direction or from one speech into another, and when that matcher is missing, fall back to a plainer check rather than pass the quotation.",
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
     "quote": "stage direction or two speeches. Without its tools, src/text.js findQuote, so a missing mirror never passes a quote",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/text.js",
     "lines": "52",
     "quote": "Find a quotation in the text. It may span consecutive lines. Returns the unit indices it covers, or null.",
     "verbatim": true
    }
   ],
   "against": "The fallback is looser. ~/Projects/g9/transformer/src/text.js line 56 (\"const ls = spoken(text);\") and lines 58-61 join up to four spoken lines whatever the speaker, so a match can run across a stage direction or from one speech into the next. The located() functions in ~/Projects/g9/transformer/src/glue/animated-judge.js and ~/Projects/g9/transformer/src/glue/threejs-archivist.js both use it.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep",
   "reason": "The quote is verbatim (lines 29-30 joined). It is one tested case, taken from the 3D build's own cases, so the general wording rests on the '!' example. It adds a needed exception to #32's rule against exclamation marks and is consistent with #13.",
   "statement": "Cleaning rules for the lines a student reads must leave words quoted from the text untouched: an exclamation mark inside a quoted line stays.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "29-30",
     "quote": "Tested on its own cases: praise and \"!\" removed, one question while a try remains, none on the final word, a quoted line's \"!\" kept.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep",
   "reason": "The quotes are verbatim. The test's judge is scripted to flag only words like 'grader' or 'mark this' (test line 21), so the drama case would pass whatever the guard says. What carries the rule is the guard's own question (~/Projects/g9/transformer/src/mechanics/util.js line 135, added). This refines #6 with an exception.",
   "statement": "A guard against answers aimed at the marker must not catch a command that the student quotes or retells from the text.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/animated-judge.test.mjs",
     "lines": "60",
     "quote": "an answer aimed at the marker meets nothing and is off task; a command quoted from the play is still an answer",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/animated-judge.test.mjs",
     "lines": "71",
     "quote": "the question says a command from the text does not count",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "135",
     "quote": "Words quoted or retold from the text, a character's commands among them, are part of an answer and do not count.",
     "verbatim": true
    }
   ],
   "against": "None found. The test's scripted judge (test line 21) cannot show that a real judge spares a quoted command.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. Both adapters call an answer off task only on a confident no with nothing met, and an answer aimed at the marker meets nothing (animated-judge.js line 97, added). The clause 'or left unsure' holds only in the animated adapter, so I cut it (see against).",
   "statement": "Call an answer off task only when the judge is sure it is, and never when any criterion was met.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/animated-judge.test.mjs",
     "lines": "53",
     "quote": "a criterion in meaning goes to Jev; off task only on a confident no, and never with a criterion met",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
     "lines": "105",
     "quote": "const offTask = !met.size && !unsure.length && results.find((r) => r.id === \"on-task\")?.verdict === \"fails\";",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
     "lines": "97",
     "quote": "if (results.find((r) => r.id === \"addresses-grader\")?.verdict === \"fails\") return { ok: true, assessment: { met: [], misreading: null, off_task: true",
     "verbatim": true
    }
   ],
   "against": "In the 3D adapter, an unsure criterion paired with a confident off-task no can still be called off. ~/Projects/g9/transformer/src/glue/threejs-archivist.js line 93 returns unsure only when on-task is not a confident no, and line 97 then calls the answer off. Line 158 does the same for other checkpoints.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. The model's lines and the guided screens' lines count as taken (threejs-render.js line 208). Up to three runs are offered, marked 'not locked' (lines 211-212), and the step is dropped when none is left (line 213). I made the statement plural to match.",
   "statement": "The quotations offered for a student's own paragraph never include one a worked model or guided screen has already used; when no other line can be offered, the paragraph task is left out.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "207",
     "quote": "the student's quote: lines the lesson's blocks found for the question, never the model's or a guided quote",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "213",
     "quote": "your paragraph: no other line of the text to offer as its quote (the model's own is never offered)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "186",
     "quote": "never the model's quote",
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
   "verdict": "keep",
   "reason": "The quotes are verbatim. The code takes the whole sentence a line is in, up to three lines of one speaker (lines 94-96), then single lines, and sorts the runs by position (line 106). It is a heuristic and has not been tested on readers.",
   "statement": "When offering quotations, prefer a whole clause (a line and the rest of its sentence, at most three lines of one speech) over a fragment, and show them in the text's order.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "85",
     "quote": "Up to n quotes from a ranked pool of units, the best first, shown in the text's order: whole clauses first (a line and",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "86",
     "quote": "the rest of its sentence, three lines of one speech at most), then single lines; never a line in `taken` or one the",
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
   "reason": "The quotes are verbatim. 'A few lines' is six units (line 60, added), and a tail of fewer than four spoken lines joins the last section (line 64). This is the same rule as #8 (ask right after the part that answers it). I kept it because it adds the cutting rules and their test (test lines 38-51).",
   "statement": "End each reading section just after the lines its question needs, run on to the end of that speech by a few lines at most but never into the lines the next question asks about, and fold a short leftover into the last section.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "45",
     "quote": "Cut the text so that each checkpoint comes right after the lines its answer is in (the build asks one checkpoint per",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "57",
     "quote": "a cut moves on to the end of its speech, a few lines at most, and never into the lines the next checkpoint asks about",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "62",
     "quote": "a short tail joins the last section rather than standing alone, a section with nothing to ask",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "60",
     "quote": "c.cut = Math.max(c.cut, Math.min(speechEnd(text, c.cut), c.cut + 6, next ? Math.min(next.cut, next.start) - 1 : last));",
     "verbatim": true
    }
   ],
   "against": "A check whose evidence needs the same final lines as an earlier check is dropped: \"the build asks one checkpoint per section, and no lines are left after its evidence for one more\" (~/Projects/g9/transformer/src/glue/threejs-render.js line 162).",
   "general": true,
   "duplicate_of": "8",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. The source applies this only to the engine's own plain lines ('Plain lines of ours') and gives no reason for it. Nothing rules out a preview a person writes, so the 'guided reading' scope went too far. I narrowed it to lines the lesson writes. It works as an application of #29.",
   "statement": "A line the lesson writes to introduce a section of the text names who speaks in it, never what happens in it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "114",
     "quote": "the build's own marker for the half it shows before a section). Plain lines of ours: who speaks, never the content.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "119",
     "quote": "return say(who ? `In this ${where}, ${who}.` : `In this ${where}, read slowly, with the question in mind.`);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "43",
     "quote": "the half before a section is the build's \"In this next section\"; the half after it is ours, never the content",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep",
   "reason": "The quotes are verbatim. The stand-in view marks the proving lines after a right quick-check pick (line 242). It also marks them whenever an open-check or claim-evidence-reasoning reply carries them (lines 362, 577). The rule comes from one player's reading page and has not been tested on readers.",
   "statement": "Once a question is answered, mark in the text the lines that prove the answer and bring them into view.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "167",
     "quote": "reveal.units: the build's margin line (.marked) on the lines that prove the answer, brought into view.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "242",
     "quote": "if (res.reveal?.units?.length) markLines(res.reveal.units);",
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
   "reason": "The quotes are verbatim. No such export incident is recorded; the reason is in the code. The checked gap is always the first word written (animated.js line 149), so authored order would put the answer first. key-words.js line 100 (added) applies the same rule to the engine's own deck. The comment on line 146 claims too much: alphabetical order only removes the authoring bias and does not stop the answer coming first. Related to #45, but a different method.",
   "statement": "Order cards and options by a neutral rule such as the alphabet, so the answer is not first just because it was written first.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "146",
     "quote": "in alphabetical order, so neither the first card nor the first option is the gap's word",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/animated.test.mjs",
     "lines": "94",
     "quote": "in alphabetical order: the first card is not the gap's word",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "100",
     "quote": "the study set in alphabetical order, and the gaps with their cues, so no gap lines up with its word",
     "verbatim": true
    }
   ],
   "against": "The comment's 'neither the first card nor the first option is the gap's word' holds only for the test's words: alphabetical order can still put the gap's word first.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 17,
   "verdict": "keep",
   "reason": "The quotes are verbatim. The guards are the animated build's own, and its lines are read live where its mirror exists; these are the fallback lines. The copied-line case is quote_only (animated.js line 253). Not a duplicate of #22 or #52.",
   "statement": "Even where answers are kept and never marked, refuse noise: gibberish, the question given back, or a copied line gets a plain request for an answer of the student's own.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "31",
     "quote": "lesson question for first thoughts: the build's guards refuse noise, and the answer is kept, not marked.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "252",
     "quote": "gibberish: \"That is not an answer yet. Write a sentence of your own.\", echo: \"That is the question. What is your answer to it?\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "61",
     "quote": "CER-1 refused \"asdf qwer zxcv\"",
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
   "verdict": "drop",
   "reason": "The quotes are verbatim, but the claim is contradicted in this repo (see against), and #34 puts a worked example before guided tries. The evidence shows something narrower: inside the claim-evidence-reasoning task, the model is shown after the attempt. The part that matters, no model of the same task before the first attempt, is already #29. Worth a look: the 3D export shows the claim-evidence-reasoning block's own model before 'your paragraph', which seems to conflict with #29.",
   "statement": "Show a model answer only after the student's own attempt is in.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "8",
     "quote": "build's guards pass (never marked), the evidence must be the text's own words; then a model answer",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "340",
     "quote": "Practice.tsx: the writing composer with its stem chip, the answer checked, then the model's sheet of rows",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "62",
     "quote": "accepted the exact quotation, kept the reasoning and showed a model answer.",
     "verbatim": true
    }
   ],
   "against": "When no worked model is on the strip, the 3D export shows the claim-evidence-reasoning block's own model as the worked model, before the student's paragraph (~/Projects/g9/transformer/src/glue/threejs-render.js lines 199-201). The worked-model block opens with \"Watch how I answer today's learning question: I find a quotation, unpick its words, then write my answer one move at a time.\" (~/Projects/g9/transformer/src/glue/animated.js line 226).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. A regex keeps questions that end in '?', have at most 26 words, do not open with a yes-or-no word and cite no line numbers (question.js line 12). The judge is asked whether each is answerable from the passage alone and worth a lesson (line 34). I added 'well formed' and 'worth a lesson' to the statement. Related to #4 and #33.",
   "statement": "When a lesson's driving question has to be generated, draft several, keep by rule the open, well-formed ones, and use the first a judge finds answerable from the text alone and worth a lesson.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/question.js",
     "lines": "1-3",
     "quote": "The writer drafts three; code keeps the open, well-formed ones; the judge keeps the first it finds answerable from the text alone and worth a lesson, on positive evidence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "90-91",
     "quote": "the writer drafts three, code keeps the open ones, Jev keeps the first answerable from the text",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/server.test.mjs",
     "lines": "87",
     "quote": "a text without a question is given one: open, well formed, answerable on the judge's word, the same next time",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/server.test.mjs",
     "lines": "94",
     "quote": "the yes-or-no draft is dropped",
     "verbatim": true
    }
   ],
   "against": "With no judge, the first well-formed draft is used unchecked and cached (~/Projects/g9/transformer/src/question.js lines 31 and 37).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep",
   "reason": "The quote is verbatim (lines 105-106 joined). It extends #31 (check the right option and each wrong one) with a check on every option's form, added after a draft was held.",
   "statement": "Check that every option is well formed, as well as checking that the key is right and the others are wrong.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "105-106",
     "quote": "that the keyed option is right, the others wrong, and that every option is well formed (added after a draft offered \"he is not what he am\")",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim (lines 139-140 joined). This is the same rule as #18 (give a judge exactly what the student sees). I kept it because it adds an incident in which the judge brought in outside knowledge, and restated it so the incident and the fix are explicit.",
   "statement": "Have a judge answer a give-away check from the question's own words only: one judge answered it from its general knowledge of the work.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "139-140",
     "quote": "its give-away question was answered from general knowledge of Othello (now: the question's own words only)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "18",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. I rewrote 'the writer' as 'the model that drafted it' so it cannot be read as a job. Lines 180 and 191 come from the video-essay notes, not from integration as found_by says. Not on record.",
   "statement": "When a check holds a draft, tell the model that drafted it which part fails and what would plainly hold, so its correction can act on it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "140",
     "quote": "the word web's hint check did not say which word to take out;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "180",
     "quote": "\"follow\" glossed as loyal: the writer now gets a correction it can act on, below.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "191",
     "quote": "it now asks for a version that plainly holds; before, it only said \"unclear\".",
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
   "verdict": "keep",
   "reason": "The quote is verbatim. A stored class is reused by block key, and only a class the judge was sure of is saved (server.js lines 111 and 115), so an unsure word is asked again. The code gives its purpose as identical exports and render reuse. Related to #21 and #51, not a duplicate.",
   "statement": "Store a judgment that shapes what students see, such as a word's class, once it is made, so the same lesson comes out the same each time.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/server.js",
     "lines": "108",
     "quote": "a word in focus keeps the class Jev gave it, so the same lesson exports the same files and its render is reused",
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
   "reason": "The quotes are verbatim. The patch replaces the player's 'two attempts, then secure' with a separate 'given' state that still completes the step (threejs-render.js lines 369-372). A test asserts that the old line is gone (~/Projects/g9/transformer/test/threejs-render.test.mjs line 106). It extends #49 and serves #42.",
   "statement": "When the answer is given after two misses, let the step finish but record and show it as given, never as accepted.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "366",
     "quote": "two tries, then the answer is given and the step completes, but a given answer is not shown as \"Accepted\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "373",
     "quote": "a checkpoint's answer given after two tries is not marked accepted",
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
   "reason": "The quotes are verbatim. This is wording only, with no result from readers. The 3D phrase is used for every checkpoint, factual ones too (~/Projects/g9/transformer/test/threejs-render.test.mjs line 127, 'Here is one way to see it: Roderigo.'), so the scope to open and written questions matters.",
   "statement": "Give a model or revealed answer as one way to see it, not as the only right answer.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "7",
     "quote": "two tries, then the answer is given (\"Here is one way to see it:\"),",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "174",
     "quote": "Here is one position you could defend:",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "713",
     "quote": "One strong answer",
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
   "verdict": "keep-with-fix",
   "reason": "The quotes and numbers are verbatim (6.6 s; 0.34, 0.48 and 0.26 s; 0.26 to 0.48 s). What was measured is speed, not the rule, so the kind is adopted rule. QA line 34 says the 6.6 s included the advisory check. The step is the first job the judge is sure is missing, in the order point, evidence, analysis, link (line 232). Only the analysis step uses the student's words (line 237). The switch to steps written in advance is evidence for #55 and is already recorded.",
   "statement": "Give feedback on a piece of writing as one next step chosen from steps written in advance: the first part the judge is sure is missing, using the student's own quotation where it can, and no step when the judge is unsure.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "208",
     "quote": "Secure only when all four hold; a job is called missing only on a confident no. One next step, ours.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "232",
     "quote": "const nextJob = verdict === \"developing\" ? NEED.find((j) => met[j] === false) ?? \"\" : \"\";",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "237",
     "quote": "analysis: span ? `Pick one word in \"${strip(span)}\" and say what it suggests.` : \"Pick one word in your quotation and say what it suggests.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "99-100",
     "quote": "It is now a Jev choice among four authored steps, filled with the student's own words, and shown only when Jev is sure.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/DECISIONS.md",
     "lines": "29-30",
     "quote": "the 3D build's paragraph coach (6.6 s through a second model) became a Jev choice of one next step (0.26 to 0.48 s live).",
     "verbatim": true
    }
   ],
   "against": "The two versions differ when every part holds. The 3D paragraph gives \"Zoom in on a second word from the quotation and say what it adds.\" (~/Projects/g9/transformer/src/glue/threejs-archivist.js line 240), while the claim-evidence-reasoning step gave none: \"a paragraph doing all three got no step (0.26 s)\" (~/Projects/g9/transformer/v02/QA.md line 102).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, but 'rather than forcing it onto a screen built for something else' is contradicted by the repo's own mappings. Direct the line sits on a key-term card (animated.js lines 15-16), and compare two answers and the evidence hunt sit on reading pages (QA line 80; animated.js line 5). What holds is this: native screens first, then the nearest screen adapted, and the rest listed with a reason and played in the stand-in view (QA line 122; README lines 22-23).",
   "statement": "When a lesson goes to another player, draw each part on that player's own screens, adapting the nearest one where it can carry the task, and list each part it cannot show, with the reason, so it plays in a stand-in view instead of vanishing.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "2",
     "quote": "Blocks map to its native nodes where one exists; the rest are listed, not forced.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "18",
     "quote": "The rest are listed, not forced.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "40-41",
     "quote": "The evidence hunt and the comparison were listed, not forced, as they have no screen of their own yet.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "15",
     "quote": "a key-term page used as a choice card (the line as the term, the lines before it under it), until",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "80",
     "quote": "a reading page of its own (the two answers as its text, the pick as its quick check);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "122",
     "quote": "compare, film, say it back and debate have no screen there yet and play in our view under the frame.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/README.md",
     "lines": "22-23",
     "quote": "A block a build cannot draw plays in the lesson view under it.",
     "verbatim": true
    }
   ],
   "against": "The adaptations themselves, for example \"a key-term page used as a choice card (the line as the term, the lines before it under it), until\" (~/Projects/g9/transformer/src/glue/animated.js line 15).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep",
   "reason": "The quotes are verbatim. This is the same rule as #17 (gate every check). I kept it because it adds an incident in a fallback view and that view's fix (lesson.js line 378).",
   "statement": "A stand-in view that plays a part another player cannot draw must keep the same gates: one played a film straight through with every question listed under it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "184-185",
     "quote": "That view now stops the same way; before, the film played straight through with every question listed under it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/web/app.js",
     "lines": "580",
     "quote": "draws the rest: blocks the chosen build has no screen for, blocks still being made, and everything while a render",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "378",
     "quote": "Films.tsx UnitFilm, plainly: the film stops at each of its questions, a seek past the next one comes back to it,",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": false,
   "duplicate_of": "17",
   "name_bearing_source": false
  },
  {
   "index": 29,
   "verdict": "keep",
   "reason": "The quotes are verbatim. They show three fixed labels from players built for one play: a speaker on the quote card (avoided by giving no reference), an act and scene, and a theme word on key-word cards. The big-idea label is handled the same way (threejs-render.js line 375). Not on record.",
   "statement": "Another player may wrap content in fixed labels of its own, such as a speaker, an act and scene, or a theme word; show each only where it is true of the lesson being shown.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "212",
     "quote": "the build's quote card names Iago beside any reference.",
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
     "lines": "261",
     "quote": "its key-word cards say \"Link to deceit\": our links go on them only when that is our centre too",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 30,
   "verdict": "keep",
   "reason": "The quotes and numbers are verbatim: 43 answers, 0 hard fails, 1 soft miss, 31 reached the judge, median 266 ms, slowest 437 ms. After the player moved from 71652b6 to e536ca1, the result was again 0 and 1, median 261 ms. Hard and soft come from the table's own must-pass flags (ops/judge-table.sh line 37, added). It builds on #35, #41 and #51. The table is the old marker's own test set, not students' answers.",
   "statement": "Test a marker that replaces another on the old marker's own labelled answers, run through the same page code students use; count must-pass misses apart from soft ones, and run the answers again when the player changes.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/ops/judge-table.sh",
     "lines": "2",
     "quote": "The animated build's own answer table (its scripts/judge-test.ts), run through its own page code",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "54",
     "quote": "43 answers, 0 hard fails, 1 soft miss. 31 reached the judge, median 266 ms, slowest 437 ms",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "77-78",
     "quote": "its answer table still gave 0 hard fails, 1 soft miss, median 261 ms.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/ops/judge-table.sh",
     "lines": "37",
     "quote": "if (c.must && bad) fails++; else if (bad) soft++;",
     "verbatim": true
    }
   ],
   "against": "The one soft miss came from a criterion that asked for one detail, 'in secret' (~/Projects/g9/transformer/v02/QA.md line 56).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, but the claim goes too far. ~/Projects/g9/transformer/ops/render-animated.sh runs no type-check, so the 0-error result is one six-block lesson checked once by hand, and the 3D build's own checks are not run on exports. The 3D edits fail only when an edit is found nowhere (threejs-render.js line 409, added), not when it is found a different number of times. I fixed the statement to what is done; a check on every export is the v08 plan.",
   "statement": "Check an exported lesson against the receiving player's own schema, and make the export stop, naming what an edit was for, when an edit it makes to that player no longer finds its target.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "41-42",
     "quote": "Type-checked against its own `src/contract.ts` with the TypeScript compiler: **0 errors in the exported lesson**.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "357",
     "quote": "Exact edits in the scratch copy, each found as many times as it says or the export fails, naming it (the build",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "409",
     "quote": "is not in it any more (${p.why})",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v08/README.md",
     "lines": "13",
     "quote": "**Exit criteria:** each export validates against its target's schema; an imported lesson round-trips.",
     "verbatim": true
    }
   ],
   "against": "\"a student's words, run its checks on exports, and a screen for compare two answers.\" (~/Projects/g9/transformer/v02/QA.md line 203, under 'Still to do'). ~/Projects/g9/transformer/ops/render-animated.sh builds without a type-check.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 32,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. 'Without putting them on the student's page' holds only for the players' own pages; the stand-in view tags every block (see against). Fixed. It fits #43, whose playtest line names each fault by block.",
   "statement": "Give every block a short label that is never renumbered or reused, name every automatic finding by that label, and where a player's page carries no labels, name the blocks on screen beside it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/web/app.js",
     "lines": "87",
     "quote": "the highest number ever given per code: numbers are never renumbered or reused",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/server.js",
     "lines": "234",
     "quote": "The composer shows the result as one line; an engine finding is named with its block's label",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/web/app.js",
     "lines": "639",
     "quote": "The block labels on the build's page now on screen, over the frame and on the strip (its pages carry none).",
     "verbatim": true
    }
   ],
   "against": "The stand-in view puts each block's label on the page (~/Projects/g9/transformer/web/lesson.js line 54, the tag span), as ~/Projects/g9/transformer/DECISIONS.md lines 12-13 ask for the reviewer's view.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 33,
   "verdict": "keep",
   "reason": "The quotes are verbatim. The rule holds for the animated export, whose lines are read live and laid over the fallback lines (animated.js line 67). The 3D export speaks in the engine's own plain lines (see against). Related to #32.",
   "statement": "A lesson shown in another player speaks in that player's own generic lines, read from that player, and falls back only to plain lines that never give the answer.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/sources.js",
     "lines": "50",
     "quote": "read live from its Lesson 1 so an exported lesson speaks in the build's own words.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "249",
     "quote": "Used only where the build's own lines cannot be read (no mirror): plain, and never the answer.",
     "verbatim": true
    }
   ],
   "against": "The 3D export does not read that player's generic lines. Its boxes and replies are the engine's own plain lines (~/Projects/g9/transformer/src/glue/threejs-render.js line 114), passed through the 3D build's cleaners.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 34,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. Evidence is settled in code (line 226, added), not by the judge, so I corrected 'each judged on its own'. The four jobs are the 3D build's, and a paragraph is secure only when all four hold (line 228).",
   "statement": "Mark an analytical paragraph on four jobs, each checked on its own (the quotation in code, the rest by the judge): a claim that answers the question, words quoted from the text, a quoted word examined for what it suggests, and a closing link back to the question.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "206",
     "quote": "The student's paragraph, the build's four jobs (point, evidence, analysis, link): evidence is code (words quoted from",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "201",
     "quote": "analysis: zooms in on a word or phrase from a quotation and says what it suggests or shows",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "202",
     "quote": "link: a closing sentence that ties the paragraph back to question",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "226",
     "quote": "evidence: exact.length > 0 || near.length > 0",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 35,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, but 'a vocabulary task' is too broad. The key-words recall requires the right spelling (key-words.js lines 3-4, added). The slip rule covers only words of five letters or more (threejs-archivist.js line 184, added). The animated rubric leaves spelling slips in any word to the judge. I narrowed it to the word web and folded in the rule for words just taught.",
   "statement": "In a word web, accept a one-letter slip of a word the lesson expects (five letters or more) and spell it back; a word just taught and typed back from memory must be spelled right, so a near spelling there gets a nudge.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "176",
     "quote": "count at once, a one-letter slip of them too (spelled right back); any other word goes to Jev, generously.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "184",
     "quote": "(w.length >= 5 ? known.find((x) => x.length >= 5 && slip(norm(x), w)) : undefined)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "151",
     "quote": "a slip is spelled back",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "3-4",
     "quote": "a near spelling gets a nudge, since a taught word is spelled right; the second miss gives the word.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "113",
     "quote": "One real English word or short phrase (spelling slips are fine)",
     "verbatim": true
    }
   ],
   "against": "The key-words recall does not accept a slip: \"a near spelling gets a nudge, since a taught word is spelled right\" (~/Projects/g9/transformer/src/mechanics/key-words.js lines 3-4).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 36,
   "verdict": "keep",
   "reason": "The quotes are verbatim, and both players ask the same question. They differ only on an unsure word (the 3D player treats it as its offline case; the animated player lets it in). That belongs to #50 and is recorded there as a counter.",
   "statement": "In a word web, count any word a reader could reasonably link to the centre word (a kind of it, a sign of it, a word for someone who shows it, or what it does to people), but not a random word or a name.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "187",
     "quote": "Could a Grade 9 reader reasonably link word to centre: a kind of it, a sign of it, a word for someone who shows it, or what it does to people? A random word, a name, or a word with no link does not count.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "86-87",
     "quote": "\"two-faced\", \"liar\", \"dissembling\" and \"hypocrite\" went in (Jev through `api/judge`, or a family form), \"football\" was struck through \"Not about duplicity\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
     "lines": "99",
     "quote": "an unsure criterion is never a pass and never a miss. The word web's own rule is to be generous, so there an unsure",
     "verbatim": true
    }
   ],
   "against": "The 3D player does not let an unsure word in: \"a confident no gets the page's own line; an unsure one is the build's offline case, never a miss\" (~/Projects/g9/transformer/src/glue/threejs-archivist.js line 190).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 37,
   "verdict": "keep",
   "reason": "The quotes are verbatim. The key-words mechanic (added, lines 1-4) is where the rule comes from: study first, then type each word from memory into its gap, cued by its meaning, with the word given on the second miss. A first miss gets a nudge: the first letter, a near-spelling note or a contrast of meanings (lines 119-121). The animated export asks only the first gap, as a choice (animated.js line 152).",
   "statement": "Teach key words by study first; then hide them and have each word typed back into its sentence from memory, cued by its meaning, with a nudge on the first miss and the word given on the second.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "514",
     "quote": "memory, cued by its meaning; a miss gets a nudge, the second gives the word",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "541",
     "quote": "Study each word and what it means. Then put them away, and put each back into its sentence from memory.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "12",
     "quote": "a key-words deck: study the set, then each word into its gap, cued by its meaning",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "1-2",
     "quote": "study a set, then recall each word into a gap. Each word comes back in a sentence about the text with a blank where it goes, cued by its meaning, and the student types it from memory.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "3-4",
     "quote": "a near spelling gets a nudge, since a taught word is spelled right; the second miss gives the word.",
     "verbatim": true
    }
   ],
   "against": "The animated export checks the deck with a single gap answered as a choice, not by typing from memory (~/Projects/g9/transformer/src/glue/animated.js line 152).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 38,
   "verdict": "keep",
   "reason": "The quotes are verbatim. In the 3D build the model is hidden while a sentence is rebuilt (line 331). It adds technique to #34's worked example.",
   "statement": "In a worked model, show the thinking beside each move, and have the student rebuild one of its sentences blank by blank, with a wrong pick staying out.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "583",
     "quote": "Practice.tsx Model, plainly: the quotation unpicked (GuidedScreens), the sentence rebuilt blank by blank (Rebuild:",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "584",
     "quote": "a wrong pick goes red and stays out), then the paragraph with the guide's thinking beside each move",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "331",
     "quote": "Now the model is hidden. Rebuild sentence",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 39,
   "verdict": "keep",
   "reason": "The quotes are verbatim. README line 51 (added) states the block's design. The animated export instead judges three criteria over two tries (see against), so 'without a grade' holds only in the engine's own view.",
   "statement": "In a debate, push back once on the side the student took, only when the judge is sure which side that is, then offer a position they could defend, without a grade.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "642",
     "quote": "Practice.tsx Evaluate: the question, a position and a reason; one push-back for the side taken, then a position",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "663",
     "quote": "a side Jev is sure of gets its push-back, which the next answer replies to",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "172",
     "quote": "Answers the other reading: says why someone could see it the other way, and answers them. One clause is enough.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/README.md",
     "lines": "51",
     "quote": "says where they stand and why, answers one push-back that cites the text; never marked",
     "verbatim": true
    }
   ],
   "against": "In the animated player the debate is judged on three criteria over two tries: \"You took a side, gave a reason from the text, and answered the other reading.\" (~/Projects/g9/transformer/src/glue/animated.js line 174).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 40,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. 'Any card built on that line' is contradicted by the engine's own word-in-focus rule: the slur itself may be glossed as the insult it is, on the judge's word (laws.test.mjs lines 153 and 173). It extends #28 from lines a student performs to context lines and cards. Corrected.",
   "statement": "Keep a line with a slur out of everything staged or voiced and out of the lines shown around a quotation; a word card may take the slur itself only to gloss it as the insult it is, on a judge's word.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "211",
     "quote": "line never staged is left out), the moment, the meaning and the words",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "183",
     "quote": "the 3D build never stages this line",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs.js",
     "lines": "79",
     "quote": "Without the mirror there is none, and the Jev question carries the guard.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/laws.test.mjs",
     "lines": "173",
     "quote": "word in focus: another word in that line is held; the slur itself, glossed as the insult it is, is left to the judge",
     "verbatim": true
    }
   ],
   "against": "The engine's own word in focus may gloss the slur: \"a word in focus may gloss the slur as an insult\" (~/Projects/g9/transformer/test/laws.test.mjs line 153). The 3D export is stricter and drops any word card on such a line (~/Projects/g9/transformer/src/glue/threejs-render.js line 183).",
   "general": false,
   "duplicate_of": "28",
   "name_bearing_source": false
  },
  {
   "index": 41,
   "verdict": "keep",
   "reason": "The quotes are verbatim. In the stand-in view the first answer is optional ('if you want one', lesson.js line 508), and the 3D export leaves out the return at the end. Related to #22 and #52. It does not claim the pair of answers measures learning (#3).",
   "statement": "Ask the lesson's question at the start for first thoughts, which are kept and never marked, and ask it again at the end, saving the second answer beside the first.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "468",
     "quote": "be kept, never marked; at the end of the lesson it is answered again, saved beside the first",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "141",
     "quote": "Saved, beside your first thoughts from the start of the lesson.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "508",
     "quote": "One sentence. There is no wrong answer yet.",
     "verbatim": true
    }
   ],
   "against": "The 3D export leaves out the return: \"the learning question's notes on its phrases; its return at the end of the lesson is a closing step, not exported\" (~/Projects/g9/transformer/src/glue/threejs-render.js line 234).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 42,
   "verdict": "keep",
   "reason": "The quotes are verbatim. A quick check is a choice in the animated build (~/Projects/g9/transformer/src/glue/animated.js line 3) and is asked open in the 3D build. An evidence hunt is a tap on a line in the stand-in view and a written quotation in both players. A fair open question, tied to #40 and #42.",
   "statement": "One block can become a different task in each player (a choice asked open, a tapped line asked as a written quotation), and whether results from different players can be compared item for item is not known.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "8",
     "quote": "a reading checkpoint: which words show the claim, quoted (settled on the quotation in code)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "260",
     "quote": "Tap the line in the text, on the left.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "7",
     "quote": "a reading checkpoint, asked open: the options go, the right one is what a secure answer shows",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 43,
   "verdict": "keep",
   "reason": "The quotes are verbatim. The animated export allows 3 tries by default, 2 for open checks and the debate, and 1 for a web word (animated.js lines 68, 113, 161 and 174). Earlier tries count in the animated adapter (~/Projects/g9/transformer/src/glue/animated-judge.js line 83) but not in the 3D one (threejs-archivist.js line 130). The against applies to some checks only.",
   "statement": "One lesson can follow different marking rules in different players (how many tries, whether earlier tries count, what an unsure judge does), and one rule set across players is not yet in place.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "68",
     "quote": "source, max_tries: 3, criteria, misreadings: [], lines:",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
     "lines": "130",
     "quote": "Taking answer on its own, does the student say this, in meaning? Any wording counts, and a short answer that says it is enough:",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "127-129",
     "quote": "in the 3D build it is its own offline case (not an attempt, the answer kept), in the animated build's pages the student is told it could not be checked (its generous word web takes the word), in our view it stays pending.",
     "verbatim": true
    }
   ],
   "against": "The written checks that the animated export adds do follow the 3D release rule: \"two tries, then the answer (the 3D build's release rule), for the written checks this file adds\" (~/Projects/g9/transformer/src/glue/animated.js line 42).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 44,
   "verdict": "keep",
   "reason": "The quotes are verbatim. Every rubric() call sets misreadings to [] (animated.js line 68), and the 3D adapter has no misreading check at all.",
   "statement": "A rubric can list a question's likely misreadings, each checked on its own and answered when nothing else is met, but no exported question lists any yet.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
     "lines": "87",
     "quote": "Does answer show this misreading:",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
     "lines": "104",
     "quote": "const misreading = met.size || unsure.length ? null :",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "68",
     "quote": "misreadings: [],",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 45,
   "verdict": "keep",
   "reason": "The quote is verbatim; it is a plan ('re-check only that step'). Related to #39.",
   "statement": "A step a person edits by hand should be checked again before it plays, just like a made step; the editor that does this is planned, not built.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v03/README.md",
     "lines": "8",
     "quote": "- Undo and redo; scene files saved and versioned; edit a baked step by hand and re-check only that step.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 46,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. 'More than one sample text' should be 'both samples', of which there are two (~/Projects/g9/transformer/README.md line 130). 'Count as ready ... or is held' garbled the exit criterion, which is ready or held. Corrected.",
   "statement": "A new kind of block is done only when it is ready on both sample texts or held with its reason, and every kind is shown made on the same text side by side; this is planned, not built.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v04/README.md",
     "lines": "17",
     "quote": "**Exit criteria:** every component is ready on both samples, or held with a reason; the gallery renders them all.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v04/README.md",
     "lines": "15",
     "quote": "A gallery shows every component baked on the same text.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v04/README.md",
     "lines": "14",
     "quote": "Each component carries: a data schema, editor hints, a writer prompt, code checks, judge checks, runtime behaviour",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 47,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. I cut the three-observation clause: it is #27, and its v05 line 5 evidence is already recorded. What remains fits #22.",
   "statement": "A student model that steers a lesson should read only recognition steps, never a student's own words; this is planned, not built.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v05/README.md",
     "lines": "10",
     "quote": "- Own words are never marked; the director reads only recognition steps.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 48,
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim. 'Fixed sequence' misread the plan, which adapts within its rules (v05 line 7, added). The personas clause is #43, and its v05 line 12 evidence is already recorded. Corrected.",
   "statement": "Reading lessons may follow sequences written as rulesets (first-read checks, close reading, analysis, writing), adapted at each action within those rules; this is planned, not built.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v05/README.md",
     "lines": "9",
     "quote": "reading sequences (first-read checks, close reading, analysis, writing)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v05/README.md",
     "lines": "7",
     "quote": "- Adaptive sequencing, hints and escalation, decided by Jev at each action within rules.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 49,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, but 'only comparing two answers exists as a block' missed the worked-model block (README line 47, added), which models an answer move by move. I restated it as the open question the plan raises.",
   "statement": "Whether full modelling, comparative judgement and faded non-examples, run as lesson procedures, help a reader is untested: they are planned as rulesets, a worked-model block and a compare-two-answers block exist, and no faded non-example does.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v05/README.md",
     "lines": "8",
     "quote": "Procedures as rulesets: full teacher modelling, comparative judgement and faded non-examples",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v04/README.md",
     "lines": "11",
     "quote": "- **Judge:** compare two answers ✓, faded non-example, rank the evidence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/README.md",
     "lines": "47",
     "quote": "follows a quotation unpicked, rebuilds one sentence, then reads the model paragraph",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 50,
   "verdict": "drop",
   "reason": "The quote is verbatim, but it adds nothing new: ranking glossary candidates by what they carry is #54, and noting the context the first lines need is #9. 'Planned, not built' is wrong for evidence maps: ~/Projects/g9/transformer/src/analyse.js line 1 already asks one bounded yes-or-no per line on whether it helps answer the lesson question, and blocks use the result as their focus.",
   "statement": "When a text is imported, map where each question's evidence lies, rank glossary candidates by the knowledge they carry, and note the context the first lines need; this is planned, not built.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v06/README.md",
     "lines": "5-6",
     "quote": "evidence maps per question; glossary candidates ranked by knowledge carried; context points (what the first lines need).",
     "verbatim": true
    }
   ],
   "against": "~/Projects/g9/transformer/src/analyse.js line 1 already finds the lines that matter for the lesson question, with one bounded yes-or-no per line.",
   "general": true,
   "duplicate_of": "54",
   "name_bearing_source": false
  },
  {
   "index": 51,
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim. I cut the reduced-motion clause: it is #38, and v07 lines 8-9 are recorded there. The plan keeps the whole text on screen, unlike #15's few words, so this stays an open question. No student has used a lesson (~/Projects/g9/transformer/README.md line 120).",
   "statement": "Read-aloud with each line of the text lit as it is heard, under one play-pause control fixed at the top, is planned, not built, and untested with readers.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v07/README.md",
     "lines": "5",
     "quote": "- Audio-synced reading: one play and pause control fixed at the top, text moving under it, each line lit as it is",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 52,
   "verdict": "keep",
   "reason": "The quote is verbatim. The hash-check part is #37. I kept it because it adds two things: the reading game engine already refuses changed bytes, and the bundle ties each file to the checks it passed.",
   "statement": "Bind every shipped file to the checks it passed, and refuse the file if its bytes change; this is planned for the web player.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v08/README.md",
     "lines": "5-6",
     "quote": "a standalone bundle with a manifest that binds the files to their checks (the engine's bundle rule: changed bytes are refused).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "37",
   "name_bearing_source": false
  },
  {
   "index": 53,
   "verdict": "keep",
   "reason": "The quotes are verbatim. Scoring on cases a person labelled is #35, and 'the seed sets measure nothing' is already recorded for it (QA line 136). I kept it for the new part: a measured precision shown beside every judged check.",
   "statement": "Every judged check should show its measured precision beside it, using labels people gave turned into test cases; today the seed sets measure nothing.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v09/README.md",
     "lines": "6",
     "quote": "- Calibration: reviewer labels become test cases; every judged check gets a measured precision and recall.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v09/README.md",
     "lines": "10",
     "quote": "**Exit criteria:** every judged check reports its measured precision beside it.",
     "verbatim": true
    }
   ],
   "against": "\"- Calibration has seed sets only: it proves the wiring and measures nothing until people label examples.\" (~/Projects/g9/transformer/README.md line 111).",
   "general": true,
   "duplicate_of": "35",
   "name_bearing_source": false
  },
  {
   "index": 54,
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim, but 'not built' missed the existing replay of kept decisions through a second judge (README line 71, added; QA lines 136-137). Corrected. Related to #39 and #51.",
   "statement": "Re-run saved lessons as a regression suite whenever a prompt or a model changes, with a report card per lesson; this is planned, and only a replay of kept decisions through a second judge exists.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v09/README.md",
     "lines": "7",
     "quote": "- Regression suites of saved scenes, re-run when a prompt or a model changes; a report card per lesson.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/README.md",
     "lines": "71",
     "quote": "re-judge kept decisions",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 55,
   "verdict": "keep",
   "reason": "The quote is verbatim. It is a plan line, framed as an open question, in line with ~/Projects/g9/transformer/README.md line 120 (no student has used a lesson). Relates to #30.",
   "statement": "It is not yet known whether any play signals (time to answer, hesitation, glossary taps, replays) say anything about a reader; they are planned but not collected.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v09/README.md",
     "lines": "8",
     "quote": "- Telemetry: time to answer, hesitation, glossary taps, replays.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 56,
   "verdict": "keep",
   "reason": "The quote is verbatim; it is a plan. It extends #21 (keep every judgment whole) to the decisions people make.",
   "statement": "Keep each decision a person makes on a lesson (approve, edit or hold) together with its reason, and keep versions and diffs for each lesson; this is planned, not built.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v10/README.md",
     "lines": "6",
     "quote": "- Versions and diffs per scene; an educator review queue (approve, edit or hold, with the reason kept).",
     "verbatim": true
    }
   ],
   "against": "\"- No lesson has been reviewed by a person or used by a student.\" (~/Projects/g9/transformer/README.md line 120).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 57,
   "verdict": "keep-with-fix",
   "reason": "The plan quote is verbatim, but the second clause mixed two scales. ~/Projects/g9/transformer/src/glue/animated.js line 101 is about one player keeping one word web per lesson, while the 3D export keeps several key-word decks (~/Projects/g9/transformer/src/glue/threejs-render.js line 229). So 'each lesson keeps one set' is not general, and neither point bears on a sweep across a unit. Cut.",
   "statement": "Sweep a whole unit for consistent terms, glossary priorities and key quotations; this is planned, not built.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v10/README.md",
     "lines": "7",
     "quote": "- Consistency sweeps across a unit: terms, glossary priorities, key quotations.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
   "lines": "6",
   "quote": "its reading sections, cut so that each checkpoint comes right after the lines it asks about",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "105",
   "quote": "question is answered by what has been said by its stop",
   "ok": true
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
   "lines": "182",
   "quote": "its word is not in its line as written",
   "ok": true
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/server.js",
   "lines": "211",
   "quote": "the text is kept by its hash, so the judge endpoint can settle quotations against it in code",
   "ok": true
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "136",
   "quote": "the build marks a phrase where the question has it, word for word",
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
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "138-139",
   "quote": "the open check's leak rule was stricter than the animated build's (a hint may quote the line to read);",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "182-183",
   "quote": "a seek past an open question is pulled back.",
   "ok": true
  },
  {
   "truth": 19,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "32",
   "quote": "Rubrics carry source \"transformer:<text key>\" so the judge endpoint (animated-judge.js) can find the text.",
   "ok": true
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
   "lines": "11",
   "quote": "Every decision is appended to runs/marking/<rubric id>.jsonl, for replay.",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "32-33",
   "quote": "Only that step is used, never its verdict, so the answer stays unmarked.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/README.md",
   "lines": "167",
   "quote": "a console of judgments, a profiler, for whoever builds the engine; never shown to reviewers",
   "ok": true
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
   "lines": "83",
   "quote": "Taking answer together with earlier_answers, does the student say this, in meaning (any wording counts):",
   "ok": true
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "56-57",
   "quote": "Its ladder runs on its authored lines, and a criterion met on an earlier try still counts.",
   "ok": true
  },
  {
   "truth": 25,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
   "lines": "130",
   "quote": "Taking answer on its own, does the student say this, in meaning? Any wording counts, and a short answer that says it is enough:",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "131-132",
   "quote": "a slur guard on lines a student is asked to perform (the 3D build's own list, read at run time; a Jev question);",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "29",
   "quote": "Nothing a student needs to work out is on screen before they answer: the key-term card's \"meaning\" holds the context.",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "63-64",
   "quote": "the word-in-focus card showed the meaning before the question; direct the line showed what the speaker wants before the pick;",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs.js",
   "lines": "4",
   "quote": "its house rules for every line a student reads (no praise, no \"!\", one question while the student still",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "66",
   "quote": "feedback opened with \"This is correct;\" under the build's own YES;",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/animated-judge.test.mjs",
   "lines": "95",
   "quote": "a reading check's reply is a question, as the build requires",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
   "lines": "31",
   "quote": "One batched Jev decision; per question id: the answer when it passes the support gates, else null (unsure).",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "193",
   "quote": "debate (the Grade 9 close: mimicry, then evaluation), then the learning question again",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v04/README.md",
   "lines": "12",
   "quote": "- **Transfer:** unseen lines, key quotations.",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "136",
   "quote": "Calibration harness and seed sets (test/calibration/, seed only: they prove the wiring, measure nothing);",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v07/README.md",
   "lines": "8-9",
   "quote": "reduced motion respected everywhere.",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "69-70",
   "quote": "saved blocks are shown at once and re-asked of the server, so a block an older maker made is made again (all six re-made, ready on the first or second try).",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/web/app.js",
   "lines": "832",
   "quote": "when nothing changed, and a block made by an older maker is made again",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/DECISIONS.md",
   "lines": "12-13",
   "quote": "A reviewer sees the lesson as a student meets it, with a short identifier on every block (`QC-1`, `EH-2`) to cite;",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "46-47",
   "quote": "speaker names only where a speech starts, fixed after the first render showed them on every line",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "173",
   "quote": "its evaluate node shows the last try's reply and not the reveal, so the model position is in that reply too",
   "ok": false
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/web/lesson.js",
   "lines": "4",
   "quote": "Class names and nesting follow the build's src/nodes (Reading, Practice, Opening) and src/components; no style of ours.",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/web/app.js",
   "lines": "626",
   "quote": "the 3D build's app takes its route in the hash; review=1 opens every step, so a chip can go straight to its block",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/web/app.js",
   "lines": "692",
   "quote": "Once the blocks settle, the four personas play the strip headless against an oracle built from each block's key (no",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v05/README.md",
   "lines": "12",
   "quote": "**Exit criteria:** sequencing measured with personas before any student sees it.",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "124-125",
   "quote": "Under the strip, one line: the four personas' playtest (\"Played by 4 personas: all finished · no faults\").",
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
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "35",
   "quote": "Tested offline with a stand-in model, including a slow or failed task, which adds nothing.",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/web/app.js",
   "lines": "544",
   "quote": "the number in the label tells the server which of its kind this is (QC-2 is told what QC-1 covers)",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "64-65",
   "quote": "QC-2 was a copy of QC-1;",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "42",
   "quote": "two tries, then the answer (the 3D build's release rule), for the written checks this file adds",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "140-141",
   "quote": "the two-tries release did not fire in sessions (the runtime now passes the attempt count); the hunt and debate now release after two tries;",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "68",
   "quote": "source, max_tries: 3, criteria, misreadings: [], lines:",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
   "lines": "9",
   "quote": "An unsure Jev is never a pass and never a miss: like no judge at all, it is the build's offline case",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
   "lines": "229",
   "quote": "developing only on a job Jev is sure is missing: unsure jobs alone are the offline case, so no revision is used up",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "141-142",
   "quote": "word classes are shown only where Jev confirmed them.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v06/README.md",
   "lines": "9",
   "quote": "Images through the TrueFoundry image route, shown only on positive evidence.",
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
   "truth": 52,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v04/README.md",
   "lines": "8",
   "quote": "paraphrase the line (saved, never marked)",
   "ok": true
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "64",
   "quote": "student text cited line numbers the build's reading does not show (\"in line 8\");",
   "ok": true
  },
  {
   "truth": 54,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
   "lines": "432",
   "quote": "The word class of each word in focus as it is used in its line, for its 3D card: one Jev choice per word, and \"\"",
   "ok": true
  },
  {
   "truth": 54,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "83-84",
   "quote": "The first draft's key words were hard words from the text (\"obsequious\", \"homage\", \"peculiar\") for \"resentment\", and Jev held it;",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
   "lines": "4",
   "quote": "evidence only, and writes no reply of its own: every word the student reads stays the rubric's.",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
   "lines": "5",
   "quote": "Jev only decides. Every reply is an authored line (the block's own feedback,",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/DECISIONS.md",
   "lines": "29-30",
   "quote": "the 3D build's paragraph coach (6.6 s through a second model) became a Jev choice of one next step (0.26 to 0.48 s live).",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated-judge.js",
   "lines": "9",
   "quote": "Beside the criteria Jev is asked whether the answer is aimed at whoever marks it (the Grade 3 engine's guard); a",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "130-131",
   "quote": "a guard on answers that address the grader in every play-time Jev decision over a student's words;",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/threejs-archivist.js",
   "lines": "102",
   "quote": "a real line outside those goes to Jev, which must find it clear evidence on its own.",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "60",
   "quote": "\"In following him, I follow but myself\", a fair line nobody keyed, on Jev's decision;",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/web/lesson.js",
   "lines": "684",
   "quote": "A line with each term made a hover word where it first appears, as the build's withGloss and Mimicry do.",
   "ok": true
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v06/README.md",
   "lines": "7-8",
   "quote": "each checked by a transcriber that has not seen the script and by a second recogniser before it ships.",
   "ok": true
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v07/README.md",
   "lines": "5",
   "quote": "one play and pause control fixed at the top, text moving under it, each line lit as it is",
   "ok": false
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v05/README.md",
   "lines": "5",
   "quote": "never adapt on fewer than three observations",
   "ok": true
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/web/lesson.js",
   "lines": "203",
   "quote": "reason under it and stays out; the right pick folds the options to that answer, with his Yes.",
   "ok": false
  }
 ]
}
```
