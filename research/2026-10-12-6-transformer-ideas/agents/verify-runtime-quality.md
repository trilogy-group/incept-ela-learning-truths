# verify:runtime-quality

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  nono, analyse its ideas and fold them into the research results

## Result

```json
{
 "direction": "runtime-quality",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "All three quotes are verbatim at the cited lines. The eight recorded playtests bear out the found_by: the reader that plays the key had 0 wrong and 0 refused in each. Fixed: the source puts a stall down to the engine ('a stall is the engine's'). Only a 'wrong' is 'the mechanic and its item disagreeing' (personas.js 116-117), so the statement no longer says all three cases mean the item and its marking disagree. Refines #43 (the reader who knows) by saying how to read its run.",
   "statement": "Play every item with its own key before anyone sees the lesson: if the key's answer is marked wrong, the item and its marking disagree, and if it is refused or stalls, the fault is the lesson's or its runtime's.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/quality/personas.js",
     "lines": "116",
     "quote": "completes: it plays the key, so a stall is the engine's.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/playtest.js",
     "lines": "83",
     "quote": "the key's own answer was marked wrong",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/quality.test.mjs",
     "lines": "26",
     "quote": "strong plays every entity to the end, is never refused or told it is wrong, and leaves no finding",
     "verbatim": true
    }
   ],
   "against": "A clean run shows that the key and the marking agree, not that the key is right. Of the offline judge playtests use, ~/Projects/g9/transformer/src/quality/playtest.js line 26 says: \"It proves plumbing, never the quality of judgment.\" Line 44 adds: \"the writer's likely words stand in for a reader's here\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (playtest.js 8 and 9; ops/playtest.mjs 8). The against checks out: 'stopped at tick 200 after 190 tries' is line 139 of that report, with severity gap. Fixed: the engine class covers 'the scene or the runtime broke a rule' (playtest.js 4), so the faults are the lesson's or its runtime's. The statement now also gives the reason for the split: a reader's limit 'says nothing about the engine'. Refines #43.",
   "statement": "Sort what scripted readers find into faults of the lesson or its runtime, things the runtime cannot do yet, and limits of the scripted reader, so a reader's limits never count against a lesson, and gate serving on the faults.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/quality/playtest.js",
     "lines": "9",
     "quote": "the persona cannot play this: it says nothing about the engine",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/playtest.js",
     "lines": "8",
     "quote": "what the runtime does not do yet (the v05 director): no way out for a guesser, no answer to an idle",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/ops/playtest.mjs",
     "lines": "8",
     "quote": "Exit 1 on an engine finding, so it can stand as a gate before a scene is served.",
     "verbatim": true
    }
   ],
   "against": "Gaps never fail the gate, even when a reader cannot finish. A guesser was \"stopped at tick 200 after 190 tries: no attempt ceiling and no reveal\" (~/Projects/g9/transformer/runs/playtest/2026-10-09T12-25-25-174Z.json line 139), and that run was graded a gap. The fix went into the runtime, not the gate: \"the hunt and debate now release after two tries;\" (~/Projects/g9/transformer/v02/QA.md line 141).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "Both quotes are verbatim; the first runs over lines 1-2 with its newline and comment marker. 'The judge is the only thing under test' went past the source: the same runs also check the runtime's own rules (playtest.js 4-7: a crash, a key in a view, two judge requests in a tick). The statement now says a run tests the lesson and its judge rather than the reader. A limit is added to against. Refines #43.",
   "statement": "Make scripted readers plain, seeded code that never calls a model, so a run tests the lesson and its judge rather than the reader, and no model grades a pick it made.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/quality/personas.js",
     "lines": "1-2",
     "quote": "Deterministic: they never call a model, so the judge is what is\n// under test (and Jev never grades a pick Jev made).",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/personas.js",
     "lines": "29",
     "quote": "reads only what the student sees; inject(item, history) puts the adversarial line where the student writes.",
     "verbatim": true
    }
   ],
   "against": "The readers write template prose, not student writing: the guesser's paragraph is \"half the time too thin, half the time a line copied whole\" (~/Projects/g9/transformer/src/quality/personas.js line 63).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep",
   "reason": "Both quotes are verbatim; the first runs over lines 150-151 with its newline and comment marker. The number re-computes from the generator at personas.js line 10: the first draw is 1025555898/2^32 = 0.2388 for seed 7 and 1027220423/2^32 = 0.2392 for seed 8, both 0.239. Narrow, as its scope note says: it bears on whether playtest runs count as separate samples.",
   "statement": "Repeated runs of a random scripted reader count as separate samples only if their draws differ: neighbouring seeds gave the same first draw, so seeds are set far apart.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/quality/personas.js",
     "lines": "150-151",
     "quote": "The guesser's seeds are far apart: the generator's first draw barely\n *  moves between neighbouring seeds (0.239 for 7 and for 8).",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/personas.js",
     "lines": "152",
     "quote": "guesser: (run = 0) => guesser(7 + run * 104729)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (runtime.js 5; positive-evidence.test.mjs 84; quality.test.mjs 39). The four judges in the found_by are the test's own (positive-evidence.test.mjs 36-46). The opening clause overstated: the runtime also counts a settled tick that marks nothing, such as a saved paragraph. Per runtime.js 83, a try is counted unless a required check was unsure and nothing was marked. 'Only when the answer was actually marked' is cut. Refines #50 and #49: the two-tries release reads this count.",
   "statement": "An idle, a refused action or an answer the judge could not settle uses up none of a student's tries.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/core/runtime.js",
     "lines": "5",
     "quote": "unsure or absent judge is never a verdict: such a tick is neutral, put up for review, and not counted as an attempt.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/positive-evidence.test.mjs",
     "lines": "84",
     "quote": "assert.equal(s.state.entities[e.id].attempts, 0, `${where}: not an attempt`);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/quality.test.mjs",
     "lines": "39",
     "quote": "idles are not tries",
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
   "verdict": "keep-with-fix",
   "reason": "The test quote is verbatim at line 106. That test shows only that the answer is not marked accepted, so 'record it as given' rested on the found_by alone. The patch the test checks is added as evidence: threejs-render.js 369-370 replaces the second-try rule with a 'given' flag and stores that turn's verdict as 'given'. Refines #49.",
   "statement": "When the answer is given after the last try, record it as given, never as the student's success.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "106",
     "quote": "assert.ok(!files[\"src/steps/Reading.tsx\"].includes(\"attempt >= 2) v = 'secure'\"), \"an answer given after two tries is not marked accepted\");",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "369",
     "quote": "two attempts, then the answer is given: the step completes, never marked Accepted",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "370",
     "quote": "v: given ? ('given' as Verdict) : v",
     "verbatim": true
    }
   ],
   "against": "The test runs only where the 3D build's mirror is present. Otherwise it is skipped with \"no 3D build mirror\" (~/Projects/g9/transformer/test/threejs-render.test.mjs line 91).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep",
   "reason": "Both quotes verbatim (v02/QA.md 65; animated.test.mjs 41). The test (lines 41-49) checks that two keys give two node ids while the page id stays the label. A fault found and fixed. Distinct from #39, which is about remaking under a new rule, not about the remade item's identity.",
   "statement": "A remade question is a new question: give it a new identity, so progress saved against the old version does not carry over.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "65",
     "quote": "a block made again kept the build's saved progress (its node ids now carry the block's key);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/animated.test.mjs",
     "lines": "41",
     "quote": "a block made again is a new question in the build: its node id carries the block's key, its page id the label",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep-with-fix",
   "reason": "All three quotes are verbatim (v01/QA.md 41-42, joined over the line break; the lesson file line 807; mechanics.test.mjs 63). The times check: the lesson's createdAt is 2026-10-09T08:50:57.872Z (its line 3), and the v01 proof run is at 08:42:12.637Z (proof-2026-10-09.json line 3). The lesson's student text says 'in line 42' and 'Review lines 34 to 36' (lines 806-807). Playtest 2026-10-09T12-25-25-328Z.json logged 20 line-number findings on it, all of severity engine. The QA doc does not date the prompt change, so its coming before 08:50:57Z is inferred from the doc's account of the earlier runs. 'Does not hold' is softened to 'is not enough': the writer avoided the form it was told to avoid and used another.",
   "statement": "A ban written only into the writer's prompt is not enough: after the prompt forbade one form of line number, a later lesson used another, so check every form of a banned pattern in code.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "41-42",
     "quote": "and \"L42\" written in a student paragraph. The house prompt now forbids L numbers in student-facing text",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/lessons/20261009-085057-why-does-iago-say-he-follows-oth.json",
     "lines": "807",
     "quote": "Correct; in line 42, Iago explicitly states,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "63",
     "quote": "no text a student reads cites a line number; quoting the words passes",
     "verbatim": true
    }
   ],
   "against": "The project's pattern checks are heuristics. Of its laws it says: \"They are heuristics: they catch the plain ways of breaking a rule, not every way.\" (~/Projects/g9/transformer/test/laws.test.mjs line 2).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (glue.test.mjs 8; mechanics.test.mjs 70; playtest.js 22). 'Dashes' was broader than the rule, which removes only a dash standing in for a comma ('no semicolon or dash for a comma'). mechanics.test.mjs 75 turns 'two-faced — a liar' into 'two-faced, a liar' and keeps the hyphen, so the statement now says so. Connects #32's plain voice with #13's exact quotation.",
   "statement": "Style rules stop at quotation marks: the lesson's own words lose exclamation marks, opening verdicts and dashes standing in for commas, but a quoted line keeps its punctuation exactly.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/glue.test.mjs",
     "lines": "8",
     "quote": "a quoted line keeps its !",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "70",
     "quote": "student text in both builds' house style: no opening verdict, no semicolon or dash for a comma, quotations untouched",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/playtest.js",
     "lines": "22",
     "quote": "What a student reads after a tick, outside quotations: no line number (src/mechanics/util.js) and no exclamation mark.",
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
   "reason": "Quotes verbatim (server.test.mjs 36; threejs-render.test.mjs 59; playtest.js 16). The found_by's field list matches FORBIDDEN in test/mechanics.test.mjs line 10. The against is right and verbatim: the animated build's export still sends the keyed index to its page (animated.test.mjs 18). Distinct from #29, which is about what is shown before an attempt, not what is sent to the page.",
   "statement": "Send a student's page only what the student sees: the key, the feedback lines, the evidence and the checks stay on the server.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/server.test.mjs",
     "lines": "36",
     "quote": "blocks: made invisibly, cached, played; the page never sees the item or the checks",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "59",
     "quote": "the feedback lines are not shipped",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/playtest.js",
     "lines": "16",
     "quote": "The student view never carries a key, feedback, evidence or a model answer (the list in test/mechanics.test.mjs).",
     "verbatim": true
    }
   ],
   "against": "The animated build's own lesson contract still carries the key to the page. The export test asserts \"assert.equal(reading.mcqs[0].correct, 0);\" (~/Projects/g9/transformer/test/animated.test.mjs line 18).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep",
   "reason": "All three quotes are verbatim. One number in the found_by is wrong: the four calibration runs had 26, 9, 31 and 31 cases, not '26 to 31 cases each'. runs/calibration/2026-10-09T12-19-39-986Z.json is a single check, word-web.linked, with 9 cases. All four used the label oracle and gave precision 1 and recall 1 on every check, and all eight playtest reports used the oracle judge. Distinct from #35 (who labels the cases) and #1 (planted faults).",
   "statement": "A perfect score from a stand-in judge that answers from the key or the labels proves only the wiring, and must never be reported as accuracy.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/ops/calibrate.mjs",
     "lines": "6",
     "quote": "answers from the labels themselves and so proves the wiring and measures nothing.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/calibration/2026-10-09T12-25-25-449Z.json",
     "lines": "6",
     "quote": "answers from the labels themselves: proves the wiring, measures nothing",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/playtest.js",
     "lines": "26",
     "quote": "the offline judge: answers from each entity's own key. It proves plumbing, never the quality of judgment.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The first item, 'The real state and check for one case.', is only a docstring heading. It is replaced with the file header that states the method (calibrate.js 4-6): each case's state is built by the mechanic itself and asked through runChecks, as a block or a play asks it. The two test quotes (quality.test.mjs 105 and 147) stand.",
   "statement": "Measure a judged check on exactly the state the lesson would send it, built by the same code a block or a play uses.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
     "lines": "4-6",
     "quote": "Each case's state is built by the mechanic\n// itself (judge for a block's checks, judgeAction for a play-time answer) and asked through runChecks, as a block or a\n// play asks it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/quality.test.mjs",
     "lines": "105",
     "quote": "the seed cases: one file per check, sorted as the 3D build sorts its answers, each labelled and built by its mechanic",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/quality.test.mjs",
     "lines": "147",
     "quote": "a case that cannot be built is an error that fails the run, including an answer code settles first",
     "verbatim": true
    }
   ],
   "against": "The seed sets are small: \"a seed set this small is diagnostic only.\" (~/Projects/g9/transformer/src/quality/calibrate.js line 6).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep",
   "reason": "Quotes verbatim (calibrate.js 4 and 90; ops/calibrate.mjs 4). The threshold is set where the code says: halfway between the lowest p that holds and the highest p that fails, when the two groups separate (calibrate.js 94). Refines #35 by naming the measures to report. No live judge has been scored this way yet.",
   "statement": "Score a judged check by the precision of its passes, the recall of its fails, the good cases it would wrongly hold back, and the gap between the two groups' probabilities, which sets its threshold.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
     "lines": "4",
     "quote": "recall of fails, and false holds (good cases the check would hold back).",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
     "lines": "90",
     "quote": "the gap between the groups: the lowest p among cases that hold and the highest among cases that fail",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/ops/calibrate.mjs",
     "lines": "4",
     "quote": "Each case goes through runChecks with several votes; per check it reports precision, recall, false holds and the gap",
     "verbatim": true
    }
   ],
   "against": "\"a seed set this small is diagnostic only.\" (~/Projects/g9/transformer/src/quality/calibrate.js line 6)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (quality.test.mjs 142 and 137; ops/calibrate.mjs 7), and 0.667 re-computes: with never-tell-me flipped, the evidence-hunt set's 2 good holds plus 1 wrong hold give 2/3. 'Advisory' means two things in this code: a check that is not required, and a calibration status. Candidate 14 uses the second sense, so this statement says 'a check that never holds a lesson back'. The run-level rule is also stated in calibrate.js 79-80.",
   "statement": "One labelled case judged the wrong way fails a check's calibration, even for a check that never holds a lesson back, because such a check still changes what a student is told.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/quality.test.mjs",
     "lines": "142",
     "quote": "an advisory check still changes what a student is told",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/quality.test.mjs",
     "lines": "137",
     "quote": "assert.equal(wrong.checks[0].status, \"failing\"); assert.equal(wrong.checks[0].wrong, 1); assert.equal(wrong.checks[0].precision, 0.667);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/ops/calibrate.mjs",
     "lines": "7",
     "quote": "Exit 1 on any wrong case or a case that cannot be built (the closing-questions judge's rule).",
     "verbatim": true
    }
   ],
   "against": "Nothing acts on the result yet. Outside src/quality/calibrate.js, only ops/calibrate.mjs and bin/transformer.mjs mention calibration (src/, bin/ and ops/ searched), so no lesson step is held back or let through because of a check's calibration.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (calibrate.js 70 and 105; quality.test.mjs 144). Five votes is the default (calibrate.js 61; ops/calibrate.mjs 21). Reworded so that 'advisory' is not confused with candidate 13's checks that are not required: the status here means 'not calibrated' (calibrate.js 106 sets advisory for any status other than calibrated). Refines #51.",
   "statement": "A check whose votes split on even one labelled case is not calibrated: it should not hold a lesson back or decide what a student is told.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
     "lines": "70",
     "quote": "the share of votes that agree with the verdict: a split vote on a labelled case is a control that flips",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
     "lines": "105",
     "quote": "a check whose controls go wrong or flip should not hold a block or decide what a student is told",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/quality.test.mjs",
     "lines": "144",
     "quote": "assert.equal(split.checks[0].status, \"advisory\"); assert.equal(split.checks[0].flips, 1); assert.equal(split.checks[0].wrong, 0);",
     "verbatim": true
    }
   ],
   "against": "Nothing acts on the status yet. Outside src/quality/calibrate.js, only ops/calibrate.mjs and bin/transformer.mjs mention calibration (src/, bin/ and ops/ searched), so required checks still hold blocks without it.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (calibrate.js 18 and 97; quality.test.mjs 111). The statement overstated. ORDER is the order cases are sorted in (calibrate.js 17), not a spread every set must cover, and no seed set covers every kind: none has a near quotation, and the paragraph's set leaves out what code stops first. What the code enforces is that every case has a kind and every set has both groups; a set without both is 'unmeasured'. Rewritten to say that.",
   "statement": "Give each of a marker's test cases a kind from one fixed list (short and right, misspelt but right, vague, nonsense, literal, near quotation, aimed at the marker), and include cases that should pass and cases that should fail: a set without both is unmeasured.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
     "lines": "18",
     "quote": "export const ORDER = [\"short-right\", \"misspelt-right\", \"vague\", \"nonsense\", \"literal\", \"near-quote\", \"injection\"];",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/quality.test.mjs",
     "lines": "111",
     "quote": "needs both groups",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
     "lines": "97",
     "quote": "const status = asked.length < rows.length ? \"broken\" : wrong ? \"failing\" : !good.length || !bad.length ? \"unmeasured\" : unsure || flips ? \"advisory\" : \"calibrated\";",
     "verbatim": true
    }
   ],
   "against": "The list fits markers of answers, not every check. The answer-key check uses its own kinds (keyed-right, keyed-wrong), and \"other kinds sort after these.\" (~/Projects/g9/transformer/src/quality/calibrate.js line 17). No seed set in test/calibration/ covers every kind, and none has a near quotation. The paragraph's set leaves out nonsense and thin answers because code stops them first (~/Projects/g9/transformer/test/calibration/cer-frame.next-step.json line 5).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "keep-with-fix",
   "reason": "The two calibration quotes are verbatim: tapped-proves.json 15, quoted as the raw file has it, with escaped quotation marks, and next-step.json 13. The third quote, 'shared run of words measures copying' (text.test.mjs 34), is about a word-overlap measure. The code uses it for leaks and give-aways (open-check.js 66; util.js 116), not for test cases, so it is dropped. Overlaps candidate 15's 'literal' kind.",
   "statement": "Among a judge's test cases, include wrong answers that share the right answer's words, so matching words is never taken for meaning.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/calibration/evidence-hunt.tapped-proves.json",
     "lines": "15",
     "quote": "Roderigo's line shares the words \\\"follow him\\\" but says nothing about Iago's purpose.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/calibration/cer-frame.next-step.json",
     "lines": "13",
     "quote": "The reasoning repeats the quotation and explains no word in it.",
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
   "reason": "Both quotes verbatim (quick-check.answerable.json 5 and 11). The set re-keys the question to each wrong option on two texts (lines 11-12 and 14-15). Applies #1 to the answer-key check and goes with #31's option-by-option checking.",
   "statement": "To test a check of the answer key, key the same question to each wrong option in turn: the check must pass the real key and fail every false one.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/calibration/quick-check.answerable.json",
     "lines": "5",
     "quote": "A case keys a different option of the same question.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/calibration/quick-check.answerable.json",
     "lines": "11",
     "quote": "\"kind\": \"keyed-wrong\", \"item\": { \"answer\": 1 }, \"expect\": \"fails\"",
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
   "reason": "Quotes verbatim (cer-frame.next-step.json 5; calibrate.js 53; v02/QA.md 54), and the numbers match: 43 answers, 0 hard fails, 1 soft miss, 31 reached the judge. The test at quality.test.mjs 147-153 makes a case that code settles first fail the run as 'not asked'.",
   "statement": "Settle in code whatever code can settle (nonsense, an answer too thin, a quotation not in the text) before an answer reaches the judge, and calibrate the judge only on what gets past the code.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/calibration/cer-frame.next-step.json",
     "lines": "5",
     "quote": "Only a saved answer reaches the judge: nonsense, a box too thin and a quotation that is not the text's exact words are stopped by code first (cer-frame respond), so they have no cases here.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
     "lines": "53",
     "quote": "not asked: code settles this answer before the judge sees it",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "54",
     "quote": "43 answers, 0 hard fails, 1 soft miss. 31 reached the judge",
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
   "verdict": "keep",
   "reason": "Quotes verbatim (addresses-grader.json 5; animated-judge.test.mjs 60 and 71). The set's quotes-commands case is the control (line 12). Refines #6.",
   "statement": "A guard against answers aimed at the marker must spare commands quoted or retold from the text, and keep such an answer among its cases as a control.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/calibration/cer-frame.addresses-grader.json",
     "lines": "5",
     "quote": "Drama invites false alarms: a paragraph that quotes a character's commands is an answer, and is kept here as a control.",
     "verbatim": true
    },
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
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep",
   "reason": "Quotes verbatim (positive-evidence.test.mjs 131 and 148; quotes.test.mjs 59). transform.test.mjs 36-41 adds the lesson-level case: no judge means 'unjudged, never ready'.",
   "statement": "A step is ready only when its checks actually ran: one made with no judge, or saved as ready with no judge call, is unchecked and remade once a judge is present, and a check whose tool is missing falls back instead of passing.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/positive-evidence.test.mjs",
     "lines": "131",
     "quote": "a block made with no judge is unchecked: never ready, never served as ready, made again once a judge is present",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/positive-evidence.test.mjs",
     "lines": "148",
     "quote": "a block saved as ready before 'unchecked' existed, with no judge call, is unchecked and made again",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/quotes.test.mjs",
     "lines": "59",
     "quote": "without the 3D build's mirror the quotation check still runs, on src/text.js findQuote, and never passes for lack of it",
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
   "verdict": "keep",
   "reason": "Quotes verbatim (scene.js 2; animated.test.mjs 8; threejs-render.test.mjs 197). The exports' skipped lists give reasons (threejs-render.test.mjs 195-197).",
   "statement": "Leave out what does not fit rather than force it, and list each part left out with its reason, whether it failed its checks or has no screen in that player.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/core/scene.js",
     "lines": "2",
     "quote": "Only steps that passed their checks ship; the rest are listed as excluded, with their reasons.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/animated.test.mjs",
     "lines": "8",
     "quote": "blocks export to the animated build's lesson shape: reading checks, key terms, apply; the rest listed, not forced",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "197",
     "quote": "a changed item is listed, never forced",
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
   "reason": "Quotes verbatim (v02/QA.md 94-96, joined over the line breaks; positive-evidence.test.mjs 184 and 190). 15 s matches.",
   "statement": "A judge or a read that failed is not an empty answer: never cache or save its silence as the result.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "94-96",
     "quote": "a reload while the server restarted lost the strip (the block list failed to load, every saved block was dropped as unknown, and the empty strip was saved); the page now asks again for up to 15 s and never saves a lesson it could not read.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/positive-evidence.test.mjs",
     "lines": "184",
     "quote": "a judge that answered nothing leaves no focus behind: the text is read again once the judge answers",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/positive-evidence.test.mjs",
     "lines": "190",
     "quote": "no empty focus is cached as the text's",
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
   "reason": "Quotes verbatim (v02/QA.md 140-141 and 184-185; runtime.js 58). Close to #41, which says to review in the mode students get. This extends it from one player's modes to the several players a lesson runs in, with two new failures: a release that fired in pages but not in sessions, and a view that played a film straight through. Kept for that evidence.",
   "statement": "Play a lesson in every player students will use, because a rule that holds in one can silently fail in another.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "140-141",
     "quote": "the two-tries release did not fire in sessions (the runtime now passes the attempt count)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "184-185",
     "quote": "That view now stops the same way; before, the film played straight through with every question listed under it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/core/runtime.js",
     "lines": "58",
     "quote": "the runtime knows how many tries this entity has had, so a mechanic's release rule (two tries, then the answer)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "41",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep",
   "reason": "Quotes verbatim (playtest.js 158 and 160; v02/QA.md 24), and the live replay numbers match: 8 ticks, 0 differences. The probe is unsureAnswer, an answer below the gates (playtest.js 29-35), so a replay that asked it would change outcomes. Refines #21 with a way to prove that a replay used only the recorded verdicts.",
   "statement": "Replay a student's session from its recorded verdicts without asking the judge again, and prove it with a stand-in judge that would answer differently: any call or changed outcome is a fault.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/quality/playtest.js",
     "lines": "158",
     "quote": "the run, rebuilt from its own log with the recorded verdicts: it must match tick for tick and never ask the judge",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/playtest.js",
     "lines": "160",
     "quote": "const probe = createFakeProvider(unsureAnswer, { name: \"replay-probe\" });",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "24",
     "quote": "Replaying the session from its log: 8 ticks, 0 differences.",
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
   "reason": "Quotes verbatim (v02/QA.md 191, 140 and 180). The transformer's correction text matches: after an unsure judge, the reason asks the writer to 'rewrite it so that it plainly holds' (src/transform.js 78-79). The against is verbatim (transform.test.mjs 18).",
   "statement": "When a check holds a draft, tell the writer exactly what to change, such as the text's own wording, the word to take out or a version that plainly holds; a bare 'unclear' gives it nothing to act on.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "191",
     "quote": "it now asks for a version that plainly holds; before, it only said \"unclear\".",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "140",
     "quote": "the word web's hint check did not say which word to take out",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "180",
     "quote": "\"follow\" glossed as loyal: the writer now gets a correction it can act on, below.",
     "verbatim": true
    }
   ],
   "against": "A draft gets only one correction: \"a failing required check gets one correction pass with the reason, then the step is held\" (~/Projects/g9/transformer/test/transform.test.mjs line 18).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (v02/QA.md 90-91; server.test.mjs 94; mechanics.test.mjs 112). The evidence covers the lesson's guiding question, where suggest-question keeps only open drafts, and the debate question, which the question-open check holds (mechanics.test.mjs 124). It does not cover choice questions, so the statement is scoped to those two.",
   "statement": "Make a lesson's guiding question and any debate question open, never yes-or-no: a yes-or-no draft is dropped or held.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "90-91",
     "quote": "the writer drafts three, code keeps the open ones, Jev keeps the first answerable from the text",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/server.test.mjs",
     "lines": "94",
     "quote": "the yes-or-no draft is dropped",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "112",
     "quote": "code checks hold a gap that gives its word away, a rebuild that does not make its sentence, a phrase not in the question, a yes-or-no debate and a hint that leaks",
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
   "reason": "Quotes verbatim (threejs-render.test.mjs 54, 63 and 64). The project does not hold such stems everywhere: one player asks quick checks open and skips a stem that needs its options. The statement now says where the rule comes from.",
   "statement": "Write a choice question's stem so it can be answered with the options covered: one player asks such checks open, and skips a stem like 'Which of these is true?' that only makes sense beside its options.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "54",
     "quote": "a quick check is asked open, an evidence hunt asks for the words; their lines stay on the server",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "63",
     "quote": "stem: \"Which of these is true?\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "64",
     "quote": "assert.match(skip.skipped[0].reason, /beside its options/);",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep-with-fix",
   "reason": "Both test quotes are verbatim (threejs-render.test.mjs 79 and 186). 'So copying the example cannot complete it' went past the source. The options are offered 'not locked' (threejs-render.js 212), so a student may still use the model's line; the code only never offers it. Statement fixed, and the code comment added as evidence (threejs-render.js 207).",
   "statement": "In the student's own task, offer evidence other than the worked model's and the guided screens', so the task is not the example again.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "79",
     "quote": "never the model's quote or a guided one",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
     "lines": "186",
     "quote": "never the model's quote",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "207",
     "quote": "the student's quote: lines the lesson's blocks found for the question, never the model's or a guided quote",
     "verbatim": true
    }
   ],
   "against": "The options are only suggestions: the page lists \"Quote options (not locked)\" (~/Projects/g9/transformer/src/glue/threejs-render.js line 212), so a student may still quote the model's line.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 29,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (animated.test.mjs 74 and 85; v02/README.md 46). The README line is about a reading page with no quick check, not about the lesson's question at both ends. It is replaced with the learning-question mechanic's own rule: both answers are saved and never marked, and the first is optional (learning-question.js 89).",
   "statement": "Ask the lesson's question at the start and again before the end, keeping both answers and marking neither.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/animated.test.mjs",
     "lines": "74",
     "quote": "the learning question opens the lesson after the openers, its phrases noted where the question has them, and is asked again, unmarked, before the end",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/learning-question.js",
     "lines": "89",
     "quote": "Code only: both answers are saved, never marked; the first is optional.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/animated.test.mjs",
     "lines": "85",
     "quote": "saved, never marked: the build's guards only",
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
   "verdict": "keep",
   "reason": "Quotes verbatim (next-step.json 5; glue.test.mjs 26; v02/QA.md 102), and 0.26 s matches. Refines #55: one of the authored choices means no step.",
   "statement": "A feedback picker needs a 'none of these' choice, so an answer that already does what was asked gets no invented next step.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/calibration/cer-frame.next-step.json",
     "lines": "5",
     "quote": "The one change that would most improve a saved paragraph: the check holds on D (none of these), and a case that fails names the change it expects in choice.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/glue.test.mjs",
     "lines": "26",
     "quote": "a paragraph that does all three gets no step",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "102",
     "quote": "a paragraph doing all three got no step (0.26 s).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep",
   "reason": "Quote verbatim (v02/QA.md 106). It comes from the film-with-checks block's batched judge check (lines 103-106). Adds a test that #31 lacks.",
   "statement": "Check that every option is well formed, not only that the key is right and the others wrong: a draft offered an ungrammatical garble of a quoted line as an option.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "106",
     "quote": "every option is well formed (added after a draft offered \"he is not what he am\")",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 32,
   "verdict": "keep",
   "reason": "Quotes verbatim (v01/QA.md 41 and 42-43), and 'two distractors' matches. The against is right: the check is advisory, and a quick check marked ready in the v01 proof has tempting-B failing at p 0.37 (proof-2026-10-09.json 53-56).",
   "statement": "Each wrong option should tempt a reader who skimmed: a live draft offered one no reader would choose, and no check caught it until a question about it was added.",
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
     "lines": "42-43",
     "quote": "an advisory check asks whether each wrong option would tempt a reader who skimmed; on Ozymandias it flagged two distractors as not tempting.",
     "verbatim": true
    }
   ],
   "against": "The tempting check is advisory, so an untempting option still ships. A quick check marked ready in the v01 proof carries \"id\": \"tempting-B\", \"required\": false, \"verdict\": \"fails\", \"p\": 0.37 (~/Projects/g9/transformer/v01/proof-2026-10-09.json lines 53-56). The judge's \"precision is not yet measured (v04).\" (~/Projects/g9/transformer/v01/QA.md line 46).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 33,
   "verdict": "keep",
   "reason": "Quotes verbatim (v01/QA.md 38-39; v02/QA.md 138-139). Both over-strict checks were loosened. The complement of #1: a check must also let through what is fine.",
   "statement": "Test every check on valid edge cases as well as on faults, because a check can be too strict and hold good material.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "38-39",
     "quote": "one paragraph quoted the single word \"boundless\", and the exact-quotation check only accepted quotations of two or more words.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "138-139",
     "quote": "the open check's leak rule was stricter than the animated build's (a hint may quote the line to read)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 34,
   "verdict": "keep",
   "reason": "Quotes verbatim (v02/QA.md 139-140; quick-check.answerable.json 5). Distinct from #18, which is about what the judge is given, not what it may draw on.",
   "statement": "Tell a judge to answer only from the words it is given: a give-away check answered from general knowledge of the work until it was limited to the question's own words.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "139-140",
     "quote": "its give-away question was answered from general knowledge of Othello (now: the question's own words only)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/calibration/quick-check.answerable.json",
     "lines": "5",
     "quote": "A block's check, on both samples: is the keyed option right, judged only from the cited lines.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 35,
   "verdict": "keep",
   "reason": "Quote verbatim (v02/QA.md 177). One held draft and the bar it led to; scoped to interpretation.",
   "statement": "Judge an interpretive claim by whether the text goes against it, not by whether it is 'true'.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "177",
     "quote": "an argument beat's narration that was not \"true\": it now has only to say nothing the text goes against;",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 36,
   "verdict": "keep",
   "reason": "Quote verbatim (v02/QA.md 178). One held draft and the prompt change it led to; scoped to literary reading.",
   "statement": "Keep each reading of a text close to its lines' own words, so it can be defended from them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "178",
     "quote": "a reading Jev could not defend from the lines: points now keep close to the lines' own words;",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 37,
   "verdict": "keep",
   "reason": "Quotes verbatim (v02/QA.md 179 and 187; video.test.mjs 49). The code check is 'viewer-words' (video.test.mjs 53 and 57).",
   "statement": "Never let production words reach a learner: feedback that mentions beats, cues, captions or frames is held.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "179",
     "quote": "an untrue feedback line, \"the second frame\", and wrong-option feedback that named the answer: new checks, below;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "187",
     "quote": "code: no \"beat\", \"cue\", \"caption\" or \"frame\", and no wrong-option feedback that names the answer;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/video.test.mjs",
     "lines": "49",
     "quote": "what a viewer reads at a stop: no making words, and a wrong option's feedback does not name the answer",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 38,
   "verdict": "keep",
   "reason": "Quotes verbatim (v02/QA.md 163 and 169; video.test.mjs 76).",
   "statement": "Make a film only after its plan passes every check, and once per version of its content.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "163",
     "quote": "is made only after the block passes, and once per key",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "169",
     "quote": "The key covers the title, the beats, what is drawn, the stops, the pinned modules and the voice.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/video.test.mjs",
     "lines": "76",
     "quote": "made once: the second call speaks nothing",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 39,
   "verdict": "keep",
   "reason": "Quotes verbatim (video.test.mjs 42; v02/QA.md 154). The code's rule is 'The checks follow different beats, not one after the other' (video-essay.js 105: successive checks at least two beats apart).",
   "statement": "Space a film's pause-to-check questions apart: two checks only one beat apart are held.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/video.test.mjs",
     "lines": "42",
     "quote": "two checks one beat apart",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "154",
     "quote": "narration length, and the spacing of the questions.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 40,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (laws.test.mjs 153 and 173), and the against (line 168) too. 'May be studied only by naming the slur' overstated. The guards cover a line a student performs and a word in focus, not every use of such a line: they sit in five mechanics, and an evidence hunt or quick check has none. Rewritten to the word-in-focus rule. Extends #28.",
   "statement": "When a lesson focuses on one word of a line that holds a slur, the word must be the slur itself, glossed as the insult it is: another word from that line is held.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/laws.test.mjs",
     "lines": "153",
     "quote": "a line never staged holds a direct-the-line block, in code and on the judge's word; a word in focus may gloss the slur as an insult",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/laws.test.mjs",
     "lines": "173",
     "quote": "word in focus: another word in that line is held; the slur itself, glossed as the insult it is, is left to the judge",
     "verbatim": true
    }
   ],
   "against": "Without the list, only the judge guards: \"the 3D build's mirror is not on this machine: the judge's question carries the guard\" (~/Projects/g9/transformer/test/laws.test.mjs line 168). The slur guards sit in five mechanics: direct the line, word in focus, worked model, key words and debate (src/mechanics/, searched for neverStaged and no-slur). Other blocks may still quote such a line.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 41,
   "verdict": "keep",
   "reason": "Quotes verbatim (word-web.linked.json 5 and 17; animated-judge.test.mjs 107). The misspelt case 'decieve' is expected to hold (line 13). The against is right: this runtime keeps an unchecked word pending rather than taking it (positive-evidence.test.mjs 108).",
   "statement": "In a word-association task, accept any word a reader could reasonably link, don't mark its spelling, and don't count a name taken from the text.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/calibration/word-web.linked.json",
     "lines": "5",
     "quote": "The check is generous by design: a word a reader could reasonably link counts, spelling is not what it checks, and a name does not count.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/calibration/word-web.linked.json",
     "lines": "17",
     "quote": "A name taken from the text: the check says a name does not count.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/animated-judge.test.mjs",
     "lines": "107",
     "quote": "the web's own rule is to be generous",
     "verbatim": true
    }
   ],
   "against": "This runtime is not generous when the judge is unsure: \"the word web: a word the judge did not check stays pending, never 'Not about'; only a confident no is\" (~/Projects/g9/transformer/test/positive-evidence.test.mjs line 108).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 42,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (mechanics.test.mjs 88 and 101; threejs-render.test.mjs 151). 'Rather than count a miss' is contradicted for key words. There a near spelling gets 'Nearly. That is the word, but the spelling is not right yet.' and is still marked wrong, since 'a taught word is spelled right' (key-words.js 3-4 and 119-122). Only say it back names a slip without counting it (say-it-back.js 3). The third quote is about a word web, an association task, so it is replaced with the key-words line. The statement now keeps what both recall tasks share.",
   "statement": "In a recall task, tell the student when an answer is the right word misspelt rather than marking it simply wrong, and don't count another taught word that also fits the gap as a miss.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "88",
     "quote": "say it back, key words and the worked model mark in code: a slip is named, and the second miss gives the answer",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "119",
     "quote": "Nearly. That is the word, but the spelling is not right yet.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "101",
     "quote": "another deck word that fits the sentence is not a miss",
     "verbatim": true
    }
   ],
   "against": "Whether a slip still counts differs by task. In say it back, \"a near spelling of a long word is named but not counted as a miss\" (~/Projects/g9/transformer/src/mechanics/say-it-back.js line 3). In key words, a near spelling \"gets a nudge, since a taught word is spelled right\" (~/Projects/g9/transformer/src/mechanics/key-words.js line 4) and comes back marked wrong (line 122).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 43,
   "verdict": "keep-with-fix",
   "reason": "Both quotes verbatim (quotes.test.mjs 48 and 42), and the against (line 43) too. 'Never against the item's own strings' went too far: a feedback line may quote one of the item's options and pass (quotes.test.mjs 28). Per util.js 74, quotations in the item's own wording are checked only against the text and the declared sources; other strings may also match the item's own wording. Rewritten to the quotation inside the question's own wording. Refines #13.",
   "statement": "Check a quotation in a question's own wording against the text and the sources the lesson declares, never against the question itself, or an invented quotation in a stem vouches for itself.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/quotes.test.mjs",
     "lines": "48",
     "quote": "an item's own string is checked against the text, and cannot pass its own quotation",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/quotes.test.mjs",
     "lines": "42",
     "quote": "a source the mechanic declares (a film's narration)",
     "verbatim": true
    }
   ],
   "against": "Short quoted spans are not checked at all: \"two words are too few to call a quotation\" (~/Projects/g9/transformer/test/quotes.test.mjs line 43). Feedback may still quote the question's own options: \"quoting one of its options passes\" (same file, line 28).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 44,
   "verdict": "keep",
   "reason": "Quotes verbatim (v02/QA.md 46-47; animated.test.mjs 21). The test checks the speakers of the first four lines (RODERIGO, none, none, IAGO). Found on the first render.",
   "statement": "In a play's text, show a speaker's name only where a speech starts, as a script does.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "46-47",
     "quote": "(speaker names only where a speech starts, fixed after the first render showed them on every line)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/animated.test.mjs",
     "lines": "21",
     "quote": "a name only where a speech starts",
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
   "reason": "Quotes verbatim (mechanics.test.mjs 130 and 144). The test also checks every term passed through against the other build's own glossary (lines 138-142). It runs only where that build's mirror is present (the skip at line 130).",
   "statement": "Where a text comes with authored glosses, use them unchanged and where their marks place them, draft only for texts without them, and let a judge read authored notes but never hold them back.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "130",
     "quote": "a section of the 3D build brings its own glossary, unchanged and placed by its line marks; any other text is drafted",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "144",
     "quote": "Jev reads the 3D build's notes, and never holds them",
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
   "reason": "Both quotes verbatim (mechanics.test.mjs 36 and 37). As written, it was a schema constraint with no reason or failure behind it. What the code enforces is an order: the shape is checked when the reply is read, before the code checks and the judge (src/transform.js 58-73). A reply that fails goes back with 'the reply could not be used' for one correction (line 63). Rewritten to that rule, with the test's heading as evidence.",
   "statement": "Check a draft's shape in code before any judge sees it, and send a wrong shape back to the writer with the reason, as when a three-option question comes back with two options or keys lines the text does not have.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "35",
     "quote": "normalize rejects a reply of the wrong shape",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "36",
     "quote": "assert.throws(() => getMechanic(\"quick-check\").normalize({ stem: \"Who?\", options: [\"a\", \"b\"], answer: 0, feedback: [], evidence: [1] }, ctx), /exactly 3/);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "63",
     "quote": "the reply could not be used",
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
   "verdict": "keep",
   "reason": "Quote verbatim (v02/QA.md 198-199). Seen in the film frames and listed for the module lane; not yet fixed in this repo.",
   "statement": "Set a quotation card without a one-word last line, and start a marked word's underline on the word, not the space before it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "198-199",
     "quote": "the quote card leaves a one-word last line, and its underline starts on the space before a marked word.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim (v02/QA.md 100-101; glue.test.mjs 11), and 0.34 s matches. Refines #55: the authored step is filled with the student's own words.",
   "statement": "Fill a pre-written next step with the student's own words, such as the quotation they chose, so it points at their answer.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "100-101",
     "quote": "a paragraph that explains no word got \"pick one word in \"I follow him to serve my turn upon him\" and say what it suggests\" (0.34 s)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/glue.test.mjs",
     "lines": "11",
     "quote": "a saved claim-evidence-reasoning answer gets one next step from a Jev choice, filled with the student's words; none when Jev is unsure, or sure the words address the marker",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 49,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (animated.test.mjs 128; mechanics.test.mjs 127; othello-items.json 13). The hint ladder is authored, but as the against shows, two tries reach only the first hint (animated.test.mjs 124; runtime.test.mjs 96; threejs-render.test.mjs 206-208). The ladder is dropped from the statement. The accepted answers, the leak list and its code check stand.",
   "statement": "Give each criterion of an open answer several accepted answers and a list of words no hint may use, and hold any hint that uses one.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/test/animated.test.mjs",
     "lines": "128",
     "quote": "assert.ok(c.nudge && c.second_nudge && c.third_nudge && c.accept.length === 3);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "127",
     "quote": "assert.equal(oc.codeChecks(leaky, ctx).find((c) => c.id === \"nudges-no-leak\").ok, false);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/fixtures/othello-items.json",
     "lines": "13",
     "quote": "\"leak\": [\"lieutenant\", \"promotion\", \"promoted\"]",
     "verbatim": true
    }
   ],
   "against": "With two tries, only the first hint is ever reached. The export sets \"assert.equal(oc.rubric.max_tries, 2);\" (~/Projects/g9/transformer/test/animated.test.mjs line 124), and in the runtime \"a sure miss gets its hint, the second miss the answer\" (~/Projects/g9/transformer/test/runtime.test.mjs line 96). Each criterion's second and third nudges are written but never shown.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 50,
   "verdict": "keep",
   "reason": "Quotes verbatim (v02/QA.md 55-56 and 54), and the numbers match. A real open question: the answer table wants a partial verdict, and a yes-or-no criterion cannot give one. It is also on record as a limit of #33.",
   "statement": "How to give partial credit when each criterion is judged yes or no: an answer a scoring table rated partial came back not met because it lacked one detail the criterion named.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "55-56",
     "quote": "The soft miss: \"They argue about how Othello married Desdemona\" came back not met where the table wants partial; the criterion asks for \"in secret\".",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "54",
     "quote": "43 answers, 0 hard fails, 1 soft miss.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/quality.test.mjs",
   "lines": "50",
   "quote": "the line reached the judge",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/quality/personas.js",
   "lines": "66",
   "quote": "the exact quotation, so the answer is saved and reaches the judge",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/laws.test.mjs",
   "lines": "27",
   "quote": "key shapes, each tried on a sample made here, so a law that could never fire fails too",
   "ok": true
  },
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v01/QA.md",
   "lines": "45-46",
   "quote": "Judge checks are bounded questions with the evidence supplied; their precision is not yet measured (v04).",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/v01/QA.md",
   "lines": "40-41",
   "quote": "A first live run on Othello showed two faults no check caught",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
   "lines": "70",
   "quote": "the share of votes that agree with the verdict: a split vote on a labelled case is a control that flips",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "130-131",
   "quote": "a guard on answers that address the grader in every play-time Jev decision over a student's words",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/animated-judge.test.mjs",
   "lines": "70",
   "quote": "the guard rides in the same batch as the criteria",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/positive-evidence.test.mjs",
   "lines": "118",
   "quote": "words aimed at the marker are no answer, and no verdict",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/quality/playtest.js",
   "lines": "91",
   "quote": "the grader line must never be credited, and no judged check may hold on it (addresses-grader holding means unseen)",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "11-12",
   "quote": "At play time, a tapped line nobody keyed goes to the judge in one request. It is accepted only on positive evidence, and logged for review.",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "59-60",
   "quote": "accepted \"In following him, I follow but myself\", a fair line nobody keyed, on Jev's decision",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/calibration/evidence-hunt.tapped-proves.json",
   "lines": "11",
   "quote": "The line the claim was written from, tapped while another line is keyed: it must still count.",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
   "lines": "30",
   "quote": "the text becomes the build's reading sections, cut so each checkpoint follows the lines it asks about",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/video.test.mjs",
   "lines": "72",
   "quote": "each stop right after its beat's narration",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/animated.test.mjs",
   "lines": "104",
   "quote": "a glossary exports as lesson.glossary: each term at its script line, matched as the line has it; one per lesson",
   "ok": true
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/quotes.test.mjs",
   "lines": "48",
   "quote": "an item's own string is checked against the text, and cannot pass its own quotation",
   "ok": true
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "196",
   "quote": "annotated-asset: its arrows need positions read from the picture;",
   "ok": true
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "66",
   "quote": "the guide's portrait was a broken image",
   "ok": true
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/quotes.test.mjs",
   "lines": "28",
   "quote": "an invented quotation holds a quick check; an exact one passes; quoting one of its options passes",
   "ok": true
  },
  {
   "truth": 13,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/test/quotes.test.mjs",
   "lines": "43",
   "quote": "two words are too few to call a quotation",
   "ok": true
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/runtime.test.mjs",
   "lines": "103",
   "quote": "a hint, never the answer",
   "ok": true
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
   "lines": "144",
   "quote": "never the wording before the last try",
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
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "182-183",
   "quote": "a seek past an open question is pulled back.",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "184-185",
   "quote": "That view now stops the same way; before, the film played straight through with every question listed under it.",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/video.test.mjs",
   "lines": "46",
   "quote": "held to what the film has shown and said by its stop",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/runtime.test.mjs",
   "lines": "96",
   "quote": "play time: an open check is Jev's, one question per criterion; a sure miss gets its hint, the second miss the answer, an unsure judge no verdict",
   "ok": true
  },
  {
   "truth": 19,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/animated-judge.test.mjs",
   "lines": "34",
   "quote": "a quote criterion is settled in code: the text's own words count, words not in the text do not, no judge needed",
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
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "24",
   "quote": "Replaying the session from its log: 8 ticks, 0 differences.",
   "ok": true
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/core/runtime.js",
   "lines": "37",
   "quote": "the whole decide record (state, questions, answers) stays in the tick log, so any tick can be re-judged through a",
   "ok": true
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/quality.test.mjs",
   "lines": "57",
   "quote": "each judged tick keeps its decide record, for a second judge",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "13",
   "quote": "Own words are never marked. The claim-evidence-reasoning entity saves the answer, and the judge only shapes a note.",
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
   "truth": 22,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/quality/playtest.js",
   "lines": "20-21",
   "quote": "// Actions that carry the student's own words: saved and shown back, never marked.\nconst OWN_WORDS = new Set([\"cer\"]);",
   "ok": true
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "57",
   "quote": "a criterion met on an earlier try still counts.",
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
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/video.test.mjs",
   "lines": "70",
   "quote": "film ${probe.format.duration} s, manifest ${m.duration} s",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/laws.test.mjs",
   "lines": "162",
   "quote": "the judge's guard: the line is in the state, and the block ships only when the judge is sure it is clean",
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
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/animated.test.mjs",
   "lines": "26",
   "quote": "nothing a student works out is on the card before they answer: the gloss and the speaker's aim come after",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
   "lines": "112",
   "quote": "code checks hold a gap that gives its word away, a rebuild that does not make its sentence, a phrase not in the question, a yes-or-no debate and a hint that leaks",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/quality/playtest.js",
   "lines": "156",
   "quote": "the runtime has no idle or timer action, so nothing nudges a reader who is stuck",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "135",
   "quote": "the one finding left is a gap (no idle nudge, v05).",
   "ok": true
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "105",
   "quote": "that the keyed option is right, the others wrong",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/glue.test.mjs",
   "lines": "6",
   "quote": "assert.equal(houseRules(\"Great job! You found the line. Which word matters? And why?\"), \"You found the line. Which word matters?\");",
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
   "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
   "lines": "120",
   "quote": "a closing reply asks nothing",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "90-91",
   "quote": "the writer drafts three, code keeps the open ones, Jev keeps the first answerable from the text",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/transform.test.mjs",
   "lines": "44",
   "quote": "word in focus takes the candidate the judge scores highest",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "55-56",
   "quote": "The soft miss: \"They argue about how Othello married Desdemona\" came back not met where the table wants partial; the criterion asks for \"in secret\".",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "116-117",
   "quote": "The palette runs in lesson order: WW FM LQ KW | GL QC OC EH WF DL | WM CER CA | SB DB.",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
   "lines": "182",
   "quote": "the worked model is the model; CER is the student's paragraph",
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
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "136",
   "quote": "Calibration harness and seed sets (test/calibration/, seed only: they prove the wiring, measure nothing)",
   "ok": true
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "156",
   "quote": "the narration against the text, and each frame against its narration;",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "167",
   "quote": "WebVTT captions, a poster, and a manifest of module digests, narrator, renderer versions and file hashes.",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "193-194",
   "quote": "A block made before a rule changed is not drawn, whatever key a client sends. Before this fix, a playtest sent the saved link's first six blocks, all made before the line-number rule, and played them; three cited line numbers.",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/server.test.mjs",
   "lines": "100",
   "quote": "a render or a playtest takes a block only if today's rules made it: one kept under an older key is not drawn",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "69-70",
   "quote": "so a block an older maker made is made again (all six re-made, ready on the first or second try).",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "140-141",
   "quote": "the two-tries release did not fire in sessions (the runtime now passes the attempt count)",
   "ok": true
  },
  {
   "truth": 42,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/core/runtime.js",
   "lines": "94",
   "quote": "Telemetry and log: everything needed to replay this tick exactly.",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "134-135",
   "quote": "its four scripted personas (strong, guesser, stuck, adversarial) play every scene headless; all four finish a 15-block Othello lesson; replay gives 0 differences;",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/ops/playtest.mjs",
   "lines": "2",
   "quote": "Play a baked scene headless with the scripted personas, before anyone sees it:",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/animated.test.mjs",
   "lines": "94",
   "quote": "in alphabetical order: the first card is not the gap's word",
   "ok": true
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/positive-evidence.test.mjs",
   "lines": "71",
   "quote": "no judged action is marked wrong, or completes on the judge's word; each is put up for review",
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
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/animated-judge.test.mjs",
   "lines": "74",
   "quote": "a judge that answers nothing is no verdict: judge_unavailable, never nothing met",
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
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/server.test.mjs",
   "lines": "75",
   "quote": "QC-2's writer is told what QC-1 asks",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/playtest/2026-10-09T12-25-25-174Z.json",
   "lines": "139",
   "quote": "stopped at tick 200 after 190 tries: no attempt ceiling and no reveal",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "141",
   "quote": "the hunt and debate now release after two tries;",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
   "lines": "127",
   "quote": "two tries, then the answer",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "126-127",
   "quote": "an unsure Jev is never a pass and never a miss",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/positive-evidence.test.mjs",
   "lines": "121",
   "quote": "the hunt: an unsure judge gives the hint with no miss; a confident no is a miss",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/core/runtime.js",
   "lines": "35",
   "quote": "each verdict keeps its pass, probabilities and band, so unsure is told apart from refuted",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/judge.js",
   "lines": "30",
   "quote": "That one could not be checked yet. It is kept, with no mark.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/test/animated-judge.test.mjs",
   "lines": "99",
   "quote": "an unsure criterion is never a miss: the student is told it could not be checked; the word web, generous, takes the word",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "77-78",
   "quote": "and its answer table still gave 0 hard fails, 1 soft miss, median 261 ms.",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v01/QA.md",
   "lines": "45",
   "quote": "**Limits.** One sample per judge question.",
   "ok": true
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "64",
   "quote": "student text cited line numbers the build's reading does not show (\"in line 8\")",
   "ok": true
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/calibration/evidence-hunt.tapped-proves.json",
   "lines": "5",
   "quote": "Lines are named by their words, never by number.",
   "ok": true
  },
  {
   "truth": 54,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "83-85",
   "quote": "The first draft's key words were hard words from the text (\"obsequious\", \"homage\", \"peculiar\") for \"resentment\", and Jev held it; with the prompt sharpened, the block was ready on the first try",
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
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "99-100",
   "quote": "It is now a Jev choice among four authored steps, filled with the student's own words, and shown only when Jev is sure.",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/threejs-render.test.mjs",
   "lines": "116",
   "quote": "the archivist: a checkpoint from a quick check, judged by Jev, replied with its own authored lines",
   "ok": true
  }
 ]
}
```
