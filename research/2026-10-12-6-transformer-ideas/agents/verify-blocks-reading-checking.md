# verify:blocks-reading-checking

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  nono, analyse its ideas and fold them into the research results

## Result

```json
{
 "direction": "blocks-reading-checking",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "Recounted from runs/lessons. In the seven runs that have the temptation check (all except 082157), the quick check scored 2 holds, 6 fails and 6 unsure out of 14. Word in focus scored 0 holds, 10 fails and 4 unsure out of 14. All 14 blocks were ready, and the check is required: false. Every quote is verbatim. Fix: 'shipped' overstates, because no lesson has been used by a student (README.md line 120). The blocks were marked ready. The verdicts are the judge's own, and none has a labelled case.",
   "statement": "Every wrong option should tempt a reader who skimmed while the text rules it out; in seven live runs the judge found only 2 of 28 machine-written wrong options tempting, none of the 14 for word meanings, and every block was still marked ready because that check only advises.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "40-42",
     "quote": "A first live run on Othello showed two faults no check caught: a quick-check distractor no reader would choose (\"he hopes to eventually become the Moor\"), and \"L42\" written in a student paragraph.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "74",
     "quote": "id: `tempting-${letters[i]}`, label: `Option ${letters[i]} would tempt a reader who skimmed`, required: false,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/lessons/20261009-085057-why-does-iago-say-he-follows-oth.json",
     "lines": "879-881",
     "quote": "\"label\": \"Option A would tempt a reader who skimmed\", \"required\": false, \"verdict\": \"fails\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "20",
     "quote": "| othello-1-1 | `word-in-focus` | ready | 1 | 5/5 | 4/4 | 0/2 | 3.9 |",
     "verbatim": true
    }
   ],
   "against": "Judge precision has not been measured (\"their precision is not yet measured (v04)\", v01/QA.md lines 45-46). The temptation verdicts have no labelled cases, so the judge may be too strict. The word-meaning version asks about a reader who 'has not looked closely' (word-in-focus.js line 87), not one who skimmed.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep",
   "reason": "Quotes are verbatim (quick-check.js lines 23-24 and 55). The check counts option lengths in characters and holds the block when the longest option is more than 2.2 times the shortest. This is not on record. No test plants an unbalanced option, so the check has never been seen to fire.",
   "statement": "Keep a choice question's options close in length so the right one does not stand out; one rule holds any option more than 2.2 times as long as the shortest.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "23-24",
     "quote": "- Exactly three options. Exactly one is right given the text; the other two are tempting to a skimmer but the text rules them out. Keep the options a similar length.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "55",
     "quote": "check(\"length-balanced\", \"No option stands out by length\", Math.max(...lens) <= 2.2 * Math.min(...lens), \"one option is much longer than the others\"),",
     "verbatim": true
    }
   ],
   "against": "No test plants an unbalanced option. The word-meaning block also asks for three options but has no length rule or check (word-in-focus.js lines 33-34 and 50-60).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep",
   "reason": "Quotes are verbatim (quick-check.js lines 68 and 70; calibration line 5). The judge state gives the key question only evidence_lines and gives the wrong-option questions the whole text (quick-check.js lines 64-65 and 71). This refines record 31 by naming the evidence each check may use, so it is not a duplicate. The seed set only tests the wiring.",
   "statement": "Judge a choice question's key from the lines it cites alone and each wrong option against the whole text, so the key is proved by its own evidence and no wrong option turns out right somewhere else.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "68",
     "quote": "{ id: \"answerable\", label: \"The keyed answer is right, judged from the cited lines\", q: noul(\"answerable\", \"Using only evidence_lines, is the option named by keyed_answer a correct answer to the question?\"), expect: \"yes\" },",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "70",
     "quote": "id: `wrong-${letters[i]}`, label: `Option ${letters[i]} is wrong, judged from the whole text`,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/calibration/quick-check.answerable.json",
     "lines": "5",
     "quote": "A block's check, on both samples: is the keyed option right, judged only from the cited lines.",
     "verbatim": true
    }
   ],
   "against": "The seed set is \"Seed cases only: obvious ones\" (quick-check.answerable.json line 5), and it has only been run through a stand-in that \"proves the wiring, measures nothing\" (runs/calibration/2026-10-09T12-25-25-449Z.json line 6).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep",
   "reason": "Quotes are verbatim. Each respond() reveals only after a right answer: quick-check.js line 90 shows the evidence lines, evidence-hunt.js line 92 shows the tapped line with its reason, and word-in-focus.js line 100 shows the gloss. The prompts also ask for right-option feedback that quotes the line, and for a reveal that explains how the line proves the claim. This is not on record.",
   "statement": "After a right answer, show what settles it, the line that proves it or the word's meaning in its line, so the student sees why it is right and not only that it is.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "12",
     "quote": "student: \"Picks an option. A wrong pick sends them back to a line without naming the answer; the right pick shows the line that proves it.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "26",
     "quote": "- feedback[i] is shown after option i is picked. Right option: one sentence that confirms it and quotes the line.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
     "lines": "15",
     "quote": "student: \"Taps a line. A wrong line gets a hint; the right line is highlighted with the reason it proves the claim.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
     "lines": "29",
     "quote": "- reveal: one sentence that explains how the line proves the claim.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-in-focus.js",
     "lines": "18",
     "quote": "student: \"Sees the line with the word picked out, answers what it means here, then reads the gloss.\",",
     "verbatim": true
    }
   ],
   "against": "None found. Nothing measures whether students read the reveal.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. Fix: key-words.js line 26 is about the gap sentence the student fills, not about a hint (the deck's hints are fixed lines), so the recall case is now about the gap sentence. The find-the-line case is also enforced in code: evidence-hunt.js line 47 allows no four words in a row from the line. The over-strict hold is confirmed: runs/blocks/7bb3a47934432969.json lines 22 and 38 held a third hint whose only leak words sat inside a quotation of the line to reread. This is a corollary of record 14 (say where to look, never what to produce) and adds the quotation case. It is not a pure duplicate.",
   "statement": "Whether a hint may quote the text depends on what the student must produce: a hint for finding a line must not quote it, and a recall gap's sentence must not hold its word even inside a quotation, but when the task is to explain, the last hint may quote the words to reread.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "63-64",
     "quote": "// the animated build's own rule (its safeReply and build-content check): a hint may quote the text, even the line to read (its third rung), but it uses no leak word and copies no four-word run of the reveal outside a quotation",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
     "lines": "28",
     "quote": "- hint: one sentence that points to who speaks or what moment to look at, without quoting the line.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
     "lines": "47",
     "quote": "check(\"hint-no-quote\", \"The hint does not quote the line\", hintRun < 4, `the hint shares ${hintRun} consecutive words with a keyed line`),",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "26",
     "quote": "/** Does the sentence give its word away: the word or one of its forms, anywhere in it, quotations included. */",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/7bb3a47934432969.json",
     "lines": "22",
     "quote": "\"third_nudge\": \"Read the words \\\"I follow him to serve my turn upon him\\\" again. What does that phrase mean in your own words?\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "138-139",
     "quote": "the open check's leak rule was stricter than the animated build's (a hint may quote the line to read)",
     "verbatim": true
    }
   ],
   "against": "This repo's runtime never reaches the open check's third hint before it shows the answer (open-check.js line 117), so the allowance has never been tested in play.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim, and the planted test (mechanics.test.mjs lines 126-127) gives a hint a listed leak word. Fix: only hints are read with their quotations stripped (open-check.js lines 65-66). The question check matches a leak word anywhere in the question, quotations included (line 67). The hint check also holds four words in a row from the answer outside a quotation. Two of the five open-check records ended held on the hint check, one of them under the older rule that also counted quoted words.",
   "statement": "Have the writer list the words that would hand the answer over, then hold any question that uses one, and any hint that uses one or copies four words in a row of the answer outside a quotation.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "42-43",
     "quote": "\"third_nudge\": \"the words to read again, quoted exactly, still not the answer\", \"leak\": [\"the words that would hand the answer over\"]}. No nudge uses a leak word.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "66",
     "quote": "const leaky = item.criteria.flatMap((c) => nudges(c).filter((t) => c.leak.some((w) => has(unquoted(t), w)) || sharedRun(unquoted(t), item.reveal) >= 4));",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "67",
     "quote": "const told = item.criteria.flatMap((c) => c.leak).filter((w) => has(item.q, w));",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "70",
     "quote": "check(\"q-no-answer\", \"The question uses no word that hands the answer over\", !told.length, `the question uses: ${told.join(\", \")}`),",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "127",
     "quote": "assert.equal(oc.codeChecks(leaky, ctx).find((c) => c.id === \"nudges-no-leak\").ok, false);",
     "verbatim": true
    }
   ],
   "against": "Under the earlier rule, leak words that were the text's own words held a fair hint that only quoted them: \"No hint hands the answer over: a hint uses a word that hands the answer over, or the answer itself\" (runs/blocks/7bb3a47934432969.json line 38). The list also catches only the words the writer thought to list.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep",
   "reason": "Quotes are verbatim, and the code confirms it. On a first sure miss, resolve() gives the first hint of the first missing criterion, and on the next miss it gives the answer (open-check.js lines 107-117). The 3D export passes only the first hint (threejs-render.js line 158). Of the four held open checks, the two held on the hint check name only second or third hints (d872bc1dfbda65fb line 68; 7bb3a47934432969 line 38). The other two were held on the give-away question. The animated build gets all three hints with max_tries 2 (animated.js lines 160-161), but its ladder code is not in this repo, so the question stays open.",
   "statement": "Which hints can a student reach, and should only those be written and checked: one block drafts three hints for each point, its runtime shows only the first before the answer, and two of its four held drafts failed only on the second and third.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "117",
     "quote": "return missed(`${vs.includes(\"holds\") ? \"Part of it is there. \" : \"\"}${item.criteria[k].nudge}`);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/threejs-render.js",
     "lines": "158",
     "quote": "mark: { kind: \"oc\", id: b.id, q: it.q, criteria: it.criteria.map((c) => ({ requirement: c.requirement, accept: c.accept, nudge: c.nudge })), reveal: it.reveal } });",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/d872bc1dfbda65fb.json",
     "lines": "51",
     "quote": "\"second_nudge\": \"Examine the end of line five to see what kind of sneer is sculpted.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "161",
     "quote": "{ met: `Yes. ${say(it.reveal, { final: true })}` }, { reveal: say(it.reveal, { final: true }), max_tries: TRIES }) }] });",
     "verbatim": true
    }
   ],
   "against": "The animated build is sent all three hints (animated.js line 160), and its open-check page is described as \"a nudge per try, the answer on the second miss\" (animated.js lines 22-23). Its own hint-ladder code is not in this repo.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim, and the decision records confirm the narrowing. The older give-away question (runs/decisions/a775ad50ec1c4070.json line 471) held a question whose wording does not state the answer, which fits the QA note that it was answered from general knowledge. The current question (runs/decisions/b5f74899349e1331.json line 374) still held a question that named both sides of its contrast; the judge put 0.65 on yes, so p 0.35 for the expected no. Fix: the second clause turned one unlabelled judge verdict into a rule, so it now reports what happened. The narrowed check never asks whether readers of a well-known work know the answer already, which bears on record 4.",
   "statement": "Judge whether a question gives its answer away from its wording alone; what readers of a well-known work already know is a separate question, which the narrowed check leaves unasked. The older check, answered from general knowledge of a famous play, held a question whose wording did not state the answer; after the narrowing, the judge still held one that named both sides of the contrast it asked about.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "87",
     "quote": "Do the words of q themselves state, or nearly state, what a good answer must say? Judge only the wording of q, not what a reader may already know about the work.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "139-140",
     "quote": "its give-away question was answered from general knowledge of Othello (now: the question's own words only)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/a775ad50ec1c4070.json",
     "lines": "471",
     "quote": "\"instructions\": \"Does the wording of q by itself give away what a good answer must say?\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/a775ad50ec1c4070.json",
     "lines": "444",
     "quote": "\"q\": \"According to Iago, what is his purpose in continuing to serve Othello?\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/b5f74899349e1331.json",
     "lines": "8",
     "quote": "\"q\": \"What difference does the speaker draw between the endurance of spoken words and the actions of the soldiers?\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/b5f74899349e1331.json",
     "lines": "129-133",
     "quote": "\"id\": \"no-giveaway\", \"label\": \"The question does not give its answer away\", \"required\": true, \"verdict\": \"fails\", \"p\": 0.35,",
     "verbatim": true
    }
   ],
   "against": "Narrowing the check leaves a question whose answer is common knowledge unchecked: \"a famous text's answer is known to anyone who knows the work, which is no give-away of the question's\" (open-check.js line 86). The give-away verdicts have no labelled cases.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep-with-fix",
   "reason": "The tally is confirmed. Of the 5 open-check records, 4 failed after 2 tries and 1 was ready, while all 17 quick checks and all 8 word-in-focus blocks were ready on the first try. 4 of 5 is the highest held share of any block kind on record (debate 2 of 3, video essay 4 of 8). Fix: two of the four holds came under rules that were later changed. 7bb3a47934432969 was held under the leak rule that counted quoted words. a775ad50ec1c4070 was held under the older give-away question (runs/decisions/a775ad50ec1c4070.json line 471), and its question states no answer. So 'two for a question that nearly stated it' overstates. Under the current rules, one was held for leaking hints and one on the give-away question.",
   "statement": "Open questions with hints were the hardest blocks to make cleanly: four of the five on record were still held after the correction pass, the highest share of any block kind. Two of those holds came under rules since loosened; under the current rules one was held for hints that used the answer's own words and one for a question the judge found nearly stated its answer.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/b5f74899349e1331.json",
     "lines": "39",
     "quote": "\"The question does not give its answer away: the judge found this does not hold\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/d872bc1dfbda65fb.json",
     "lines": "68",
     "quote": "No hint hands the answer over: a hint uses a word that hands the answer over, or the answer itself",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/a775ad50ec1c4070.json",
     "lines": "37",
     "quote": "\"The question does not give its answer away: the judge found this does not hold\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/a775ad50ec1c4070.json",
     "lines": "471",
     "quote": "\"instructions\": \"Does the wording of q by itself give away what a good answer must say?\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/7bb3a47934432969.json",
     "lines": "38",
     "quote": "No hint hands the answer over: a hint uses a word that hands the answer over, or the answer itself",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "138-140",
     "quote": "the open check's leak rule was stricter than the animated build's (a hint may quote the line to read); its give-away question was answered from general knowledge of Othello (now: the question's own words only)",
     "verbatim": true
    }
   ],
   "against": "Each record keeps only a block's latest make, so earlier attempts are not counted. There are five records on three texts, and the judge's give-away verdicts have no labelled cases.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. Fix: the hint goes to the first criterion the judge is sure fails (vs.findIndex on 'fails'). The acknowledgement appears only when some other criterion surely holds, and an unsure criterion counts as neither. Unlike the animated build, our open check keeps no memory of points met on an earlier try.",
   "statement": "When an answer makes some of the required points, say that part of it is there and hint only at the first point the judge is sure is missing.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "116-117",
     "quote": "const k = vs.findIndex((x) => x === \"fails\"); return missed(`${vs.includes(\"holds\") ? \"Part of it is there. \" : \"\"}${item.criteria[k].nudge}`);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "68",
     "quote": "lines: { ...lines, partial: \"Part of it is there.\", ...own }",
     "verbatim": true
    }
   ],
   "against": "In the animated build's own answer table, a partly right answer came back not met: \"The soft miss: \"They argue about how Othello married Desdemona\" came back not met where the table wants partial; the criterion asks for \"in secret\".\" (v02/QA.md lines 55-56).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep",
   "reason": "Quotes are verbatim. The runtime test pins how the release line opens (runtime.test.mjs lines 104-105, with the try count supplied), and the debate frames its closing model position the same way (animated.js line 174). Closed answers, such as the hunt's 'Here it is' and the deck's 'Here is the word', are given plainly, which fits the scope. This is not on record.",
   "statement": "When an open question's answer is finally shown, offer it as one way to see it, not as the only right answer.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "108",
     "quote": "feedback: say(`Here is one way to see it: ${item.reveal}`, { final: true })",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/runtime.test.mjs",
     "lines": "105",
     "quote": "assert.equal(given.response.done, true); assert.match(given.response.feedback, /^Here is one way to see it:/);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "174",
     "quote": "before_reveal: say(`Here is one position you could defend: ${it.model_position}`, { final: true })",
     "verbatim": true
    }
   ],
   "against": "None found.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep",
   "reason": "Quotes are verbatim. normalize keeps one to three accepted answers for each criterion (open-check.js line 56), and the play-time question lists them as examples (line 100). This is related to record 25 (mark meaning), but it adds the sample answers shown to the marker. Nothing measures their effect.",
   "statement": "Write the marking points for a written answer as what a good answer must say in meaning, each with three short sample answers in varied wording that the marker is shown.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "39-40",
     "quote": "- criteria: 1 to 3 things a good answer must say, in meaning; a short answer that says them is enough. Each {\"requirement\": \"what the answer must say\", \"accept\": [\"three short answers that say it, in varied wording\"],",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "100",
     "quote": "Answers that say it look like: ${c.accept.map((a) => `\"${a}\"`).join(\"; \")}.",
     "verbatim": true
    }
   ],
   "against": "None found. No labelled cases measure whether the samples help the marker.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. Fix the noise definition. The pattern runs on the answer with spaces removed. It matches one character typed four or more times, or six or more characters with no a, e, i, o or u, and those characters can include digits and punctuation. An answer with no words is also thin (line 15). As a result, a real word with no vowel, such as 'rhythm', would be turned away. Related to record 25, but the pre-filter is new.",
   "statement": "Before a marker sees a written answer, turn away only noise (no words at all, one character typed four or more times, or six or more characters without a vowel, spaces aside) and let a short answer through.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "13",
     "quote": "const NOISE = /^(.)\\1{3,}$|^[^aeiou\\s]{6,}$/i;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "14",
     "quote": "// a short answer that says it is enough (the 3D build's marking rule), so only noise is turned away before Jev",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "15",
     "quote": "const thin = (t) => !wordCount(t) || NOISE.test(t.replace(/\\s+/g, \"\"));",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "98",
     "quote": "if (thin(text)) return null;",
     "verbatim": true
    }
   ],
   "against": "Another block asks for at least two words: \"const thin = (t) => wordCount(t) < 2 || NOISE.test(t.replace(/\\s+/g, \"\"));\" (learning-question.js line 10). The vowel rule also turns away a real word like 'rhythm'.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. wellFormed rejects a question that opens with one of 15 auxiliaries. Both the open check and the debate use it (debate.js line 69), and a planted closed question is caught (mechanics.test.mjs line 124). Fix: 'most closed ones' has not been measured. The pattern misses closed questions that open some other way ('According to the speaker, is ...') or with must, may or shall.",
   "statement": "An open question must not be answerable with yes or no, and code can hold a closed one that opens with an auxiliary verb such as is, does or can.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/question.js",
     "lines": "11",
     "quote": "const YES_NO = /^(is|are|does|do|did|can|could|would|will|was|were|has|have|had|should)\\b/i;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/question.js",
     "lines": "12",
     "quote": "export const wellFormed = (q) => typeof q === \"string\" && /\\?\\s*$/.test(q) && q.trim().split(/\\s+/).length <= 26 && !YES_NO.test(q.trim()) && !/\\b(?:L\\d+|lines?\\s+\\d+)/i.test(q);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "35",
     "quote": "answers in a sentence of their own after one careful reading. Not a yes or no question, and not a choice.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "124",
     "quote": "assert.equal(db.codeChecks(db.normalize({ ...FIX.debate, question: \"Can we sympathise with Iago?\" }, ctx), ctx).find((c) => c.id === \"question-open\").ok, false);",
     "verbatim": true
    }
   ],
   "against": "Reading the pattern shows that a closed question opening with another phrase or another modal verb passes it.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. Fix: not every activity is aimed at the question. Every prompt carries the question (util.js line 43), but only the quick check, open check and evidence hunt also get the relevant lines (focusNote). The quick check, key words, glossary and word in focus are defined by the text, not by the question. The relevant lines are only a preference (util.js line 41).",
   "statement": "Aim a lesson's reading tasks at its one question: give every writer the question, choose the claim to prove, the moment to check and the big idea because they bear on it, and point the checks at the lines the judge found help answer it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "43",
     "quote": "export const context = (ctx) => `LESSON QUESTION: ${ctx.question}\\n\\nTEXT (${ctx.text.kind}):\\n${unitsBlock(ctx.text)}`;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/analyse.js",
     "lines": "12",
     "quote": "Does line L${u.n} of text help a careful reader answer lesson_question?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
     "lines": "23",
     "quote": "TASK: write one claim about the text that helps answer the lesson question, for the reader to prove by finding the",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "34",
     "quote": "TASK: one open reading check on a key moment of the text that bears on the lesson question: a question a Grade 9 reader",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "35-36",
     "quote": "Choose the ONE word for the big idea that runs through this passage and bears on the lesson question",
     "verbatim": true
    }
   ],
   "against": "The relevant lines are a preference, not a rule: \"Prefer them, but use any line that fits the task.\" (util.js line 41). The glossary and key words are chosen for reading the text, not for the question.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep",
   "reason": "Quotes are verbatim (quick-check.js lines 1 and 20-21; v05/README.md line 9). The reading sequence is a v05 goal and has not been built yet. No case checks that drafted questions stay at the first-read level. This is not on record.",
   "statement": "A quick check of a first reading asks who speaks, what happens or how characters relate, not what it means, and a reader who has read the lines once can answer it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "1",
     "quote": "// Quick check: one first-read question (who, what, how characters relate), three options, exactly one defensible.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "20-21",
     "quote": "TASK: one quick multiple-choice question that checks a first reading: who is speaking, what is happening, or how two characters relate. Not interpretation. A Grade 9 reader who has read the lines once can answer it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v05/README.md",
     "lines": "9",
     "quote": "reading sequences (first-read checks, close reading, analysis, writing)",
     "verbatim": true
    }
   ],
   "against": "None found. The sequence it belongs to is planned, not built.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. The code holds a claim that has five or more words in a row from a keyed line, so a claim with four passes. The rationale is inferred from the task; the source does not state it. The second clause rests on one seed label (calibration line 15). Fix: the statement now gives the threshold.",
   "statement": "State a claim to be proved in other words than the line that proves it (no five words in a row from it), so the line cannot be found by matching words; a line that only shares the claim's words is not evidence.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
     "lines": "27",
     "quote": "- The claim must not copy five or more consecutive words from those lines.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
     "lines": "46",
     "quote": "check(\"claim-no-copy\", \"The claim does not copy the line\", run < 5, `the claim shares ${run} consecutive words with a keyed line`),",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/calibration/evidence-hunt.tapped-proves.json",
     "lines": "15",
     "quote": "Roderigo's line shares the words \\\"follow him\\\" but says nothing about Iago's purpose.",
     "verbatim": true
    }
   ],
   "against": "The seed label has never been scored against the judge (the seed sets measure nothing yet, README.md line 111).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 17,
   "verdict": "keep-with-fix",
   "reason": "Recounted from runs/lessons. On the drama sample, the keyed line grew to an accepted set of 3 to 5 lines in all five runs (+4, +3, +3, +3, +2), and in one run the writer keyed a line that the other runs had accepted only as an alternative. Fix: the search covers at most eight of the lines judged relevant, not every other line. On the poem, no line was added in three runs (two runs keyed three lines and one keyed one), so the statement now names that limit. This carries record 7 into build time and adds the measurement, so it is not a duplicate.",
   "statement": "Before a find-the-evidence item is used, ask the judge whether each of the other lines most relevant to the question proves the claim too, and accept every one it is sure of: in five runs on one drama text it accepted two to four more lines besides the keyed one, though on a short poem it added none in three runs.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
     "lines": "1-2",
     "quote": "The judge confirms every keyed line and also finds other lines that prove the claim just as well, so a fair answer is never marked wrong.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
     "lines": "65",
     "quote": "return { ...item, accepted: [...new Set([...item.evidence, ...also])] };",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "19",
     "quote": "| othello-1-1 | `evidence-hunt` | ready | 1 | 3/3 | 1/1 | 3/8 | 1.4 |",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/lessons/20261009-085057-why-does-iago-say-he-follows-oth.json",
     "lines": "982",
     "quote": "\"id\": \"also-L42\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v01/QA.md",
     "lines": "25",
     "quote": "| ozymandias | `evidence-hunt` | ready | 1 | 3/3 | 3/3 | 0/8 | 1.5 |",
     "verbatim": true
    }
   ],
   "against": "The search covers at most eight lines (evidence-hunt.js line 53), and the 'also' verdicts are advisory with no labelled cases.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep",
   "reason": "Quotes are verbatim: the GAIN scale (line 10), the summary (line 17) and the score question (line 67). Code takes the highest gain among the candidates the judge is sure are clean (lines 73-76). This duplicates record 54 (choose words by the knowledge they carry, not by rarity). It is kept for the evidence it adds: the five-step scale the judge scores each candidate on. The scale has no labelled cases.",
   "statement": "Choose the word to teach by how much knowing it helps a reader understand the passage, on steps from an everyday word, through an older sense or idiom and a rank, title or historical idea, to a word the scene cannot be understood without.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-in-focus.js",
     "lines": "10",
     "quote": "const GAIN = [\"almost none: an everyday word\", \"a little\", \"some: an older sense or an idiom\", \"a lot: a rank, a title or a historical idea\", \"essential: the scene cannot be understood without it\"];",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-in-focus.js",
     "lines": "17",
     "quote": "summary: \"The word that carries the most knowledge, glossed for this line and asked about. Chosen by knowledge carried, not by difficulty.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-in-focus.js",
     "lines": "67",
     "quote": "How much does knowing what \"${c.word}\" means in this passage (gloss: ${c.gloss}) help a Grade 9 reader understand it?",
     "verbatim": true
    }
   ],
   "against": "None found. The scale has no labelled cases.",
   "general": false,
   "duplicate_of": "54",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. The planted cases (laws.test.mjs lines 173-184) run only when the 3D build's mirror is on the machine (line 168). Fix the scope: the rule covers a line picked out to teach a word. Students still read lines with slurs in the text itself, and the glossary has no such rule. Its first draft in runs/decisions/366b8d2c7104a608.json (lines 47-49) glossed another word in a line that holds a racial epithet, and nothing checked that line. Not a duplicate of record 28, which is about performing a line.",
   "statement": "When a line is picked out to teach a word, choose a clean one: a line with a slur may be picked only to gloss the slur itself as the insult it is, and among candidates prefer those the judge is sure are clean.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-in-focus.js",
     "lines": "3-4",
     "quote": "The line shown must be clean: a slur in it is allowed only as the word in focus itself, glossed as the insult it is (as the animated build glosses it).",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-in-focus.js",
     "lines": "58",
     "quote": "check(\"not-never-staged\", \"No candidate's line is one the 3D build never stages, unless the word is that slur\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-in-focus.js",
     "lines": "73",
     "quote": "// the highest gain among the candidates the judge is sure are clean; with none, the highest, which the judge holds",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/laws.test.mjs",
     "lines": "173",
     "quote": "// word in focus: another word in that line is held; the slur itself, glossed as the insult it is, is left to the judge",
     "verbatim": true
    }
   ],
   "against": "The glossary block has no slur rule. Its first drafted glossary for the play glossed another word in a line with a racial epithet (runs/decisions/366b8d2c7104a608.json lines 47-49). The planted test is skipped when the mirror is absent.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep",
   "reason": "Quotes are verbatim (util.js lines 133-135). The guard is asked alongside the open-check, learning-question and word-web judgments. A seed control case plants a paragraph that quotes a character's commands and expects it to pass (test/calibration/cer-frame.addresses-grader.json lines 5 and 12), though the seed set measures nothing yet. This refines record 6 with the exception, so it is not a duplicate.",
   "statement": "A guard against answers aimed at the marker must count commands quoted or retold from the text as part of the answer, since characters in a play give orders.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "133-134",
     "quote": "Plays are full of commands, so a command quoted or retold from the text is said not to count.",
     "verbatim": true
    },
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
    }
   ],
   "against": "None found. No recorded false alarm, and the control case has not been scored against the judge.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "keep",
   "reason": "Quotes are verbatim (learning-question.js lines 1-2, 29-30 and 64). Code checks that each phrase appears in the question as written (line 53), and a planted stray phrase is caught (mechanics.test.mjs lines 120-121). This is not on record.",
   "statement": "Before students answer the lesson question, explain what two or three of its phrases ask of them, never what the answer is.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/learning-question.js",
     "lines": "1-2",
     "quote": "the lesson's question on its own, with two or three of its phrases explained (what each asks, never the answer)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/learning-question.js",
     "lines": "29-30",
     "quote": "Choose two or three short phrases of the lesson question that a Grade 9 reader should stop on, and say what each asks of them here, without answering the question.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/learning-question.js",
     "lines": "64",
     "quote": "Does note_${i} say what phrase_${i} asks or means in question, without answering question?",
     "verbatim": true
    }
   ],
   "against": "None found.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep",
   "reason": "Quotes are verbatim (lines 2-3, 96 and 99). respond() saves both answers and returns correct: null in every case (lines 90-99). Records 22 and 42 keep students' words and first attempts, but neither describes asking the same question at the start and at the end.",
   "statement": "Ask the lesson question at the start and again at the end, keep both answers side by side, and mark neither.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/learning-question.js",
     "lines": "2-3",
     "quote": "At the end of the lesson it is answered again, saved beside the first and never marked (the 3D build's bookends)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/learning-question.js",
     "lines": "96",
     "quote": "\"Kept. You will come back to it at the end of the lesson.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/learning-question.js",
     "lines": "99",
     "quote": "\"Saved, beside your first answer.\"",
     "verbatim": true
    }
   ],
   "against": "The first answer is optional: \"// Code only: both answers are saved, never marked; the first is optional.\" (learning-question.js line 89).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "keep",
   "reason": "Quotes are verbatim (lines 12, 71-72 and 77). resolve() adds a line only when the judge is sure of a choice other than D: in judge.js line 20, an unsure answer is 'unclear' and never 'fails'. It says nothing about words aimed at the marker (lines 84-85). This applies records 22 and 55 and adds the three kinds of growth. The choice is advisory and has no labelled cases.",
   "statement": "Say what a later answer adds to an earlier one only when the judge is sure, and only in one of three fixed ways: it now rests on the text's own words, makes a sharper claim, or weighs another reading.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/learning-question.js",
     "lines": "12",
     "quote": "const MOVED = { A: \"It now rests on the text's own words.\", B: \"It now makes a sharper claim than the first.\", C: \"It now weighs another reading.\" };",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/learning-question.js",
     "lines": "71-72",
     "quote": "one Jev choice on what it adds to the first, shown only when Jev is sure, and never as a mark. The line is ours and quotes neither answer.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/learning-question.js",
     "lines": "77",
     "quote": "D: \"nothing new: it says what first says\"",
     "verbatim": true
    }
   ],
   "against": "None found. The choice is advisory and has no labelled cases.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. The tenth note got a yes of 0.59 with gate reason top<0.6 (runs/decisions/366b8d2c7104a608.json lines 307-321). Fix: the second draft did not confirm that note. It dropped the word ('owe', glossed 'own or possess') and added two others, and the tenth note that passed at 0.92 was a different term (lines 544-546). The held note looks right, since it is an older sense of a common word. So this case shows what the gate costs as much as what it catches. A key-word draft lost an older-sense meaning the same way ('mocked', 0.59, runs/decisions/1ed330c52090f0fc.json).",
   "statement": "Where students only read and answer nothing, hold a drafted note until the judge confirms it fits its word as its line uses it, since a wrong gloss misleads quietly; in one ten-note draft the judge could not confirm one note, and the second draft passed by dropping that word.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "3-4",
     "quote": "Jev checks every note fits its word as the line uses it, each one required, since a wrong gloss on Shakespeare misleads quietly.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/366b8d2c7104a608.json",
     "lines": "307-310",
     "quote": "\"gloss_fits_9\": { \"id\": \"gloss_fits_9\", \"type\": \"noul\", \"value\": 0.59,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/366b8d2c7104a608.json",
     "lines": "319-321",
     "quote": "\"pass\": false, \"gate_reasons\": [ \"top<0.6\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/366b8d2c7104a608.json",
     "lines": "47",
     "quote": "\"term_9\": \"owe\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/366b8d2c7104a608.json",
     "lines": "544",
     "quote": "\"term_9\": \"peculiar end\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "125",
     "quote": "label: `The note fits \"${e.term}\" as its line uses it`, required: drafted,",
     "verbatim": true
    }
   ],
   "against": "Notes from an existing approved glossary are read but never hold the block: \"// the 3D build's own notes are its content: Jev's reading of them is kept, and never holds them\" (glossary.js line 121). In both drafts held on an unsure 0.59, the unconfirmed item looks right, and the writer replaced it instead of keeping it.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 25,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. The speech's glossary (runs/blocks/839053e70062cbb5.json) drafted ten terms. Two failed the known-unaided question (needed-2 at p 0.35, needed-3 at p 0.17) and were dropped, leaving eight, and three stayed unsure. All ten terms in the play's glossary (366b8d2c7104a608) were judged needed. Fix: 'ten-word' becomes ten-term, because several are phrases, and the scope note's 'modern prose' becomes a nineteenth-century speech. 'Never a name' is only asked in the prompt, and no check enforces it. Related to record 54, which is about knowledge carried, not familiarity.",
   "statement": "Gloss only what readers need: drop a term the judge is sure a typical reader knows unaided, never gloss a name, and never empty the list; in one ten-term draft for a nineteenth-century speech the judge was sure two terms were already known.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "85-86",
     "quote": "Not words a Grade 9 reader already knows, and never a name.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "130-131",
     "quote": "a drafted word Jev is sure a Grade 9 reader knows unaided is dropped, unless that would leave nothing",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "136",
     "quote": "return kept.length && kept.length < item.entries.length ? { ...item, entries: kept } : item;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/839053e70062cbb5.json",
     "lines": "352-354",
     "quote": "\"label\": \"A Grade 9 reader needs \\\"proposition\\\" explained\", \"required\": false, \"verdict\": \"fails\",",
     "verbatim": true
    }
   ],
   "against": "The check is advisory and has no labelled cases. In the same glossary, three words the judge was unsure of stayed in (needed-1, needed-8 and needed-9 are unclear in runs/blocks/839053e70062cbb5.json).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. Fix: 'check every gloss, meaning and cue' overstates. The word-in-focus gloss has no such check and no such prompt rule. Each check that does exist looks only for the word itself as a token, and the glossary looks only for a term's first word, so a definition that uses another form of the word passes. The three blocks that do check are the glossary's notes (line 115), the key-word meanings, which double as recall cues (line 78), and the word web's meanings (lines 68 and 71).",
   "statement": "Define a word without using the word or a form of it, and check that in code: three vocabulary blocks hold a definition that contains the word itself, but none of their checks catches another form of it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "87-88",
     "quote": "\"note\": \"what it means in this line, at most 15 words, without using the term\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "109",
     "quote": "const usesTerm = (e) => norm(e.note).split(\" \").includes(norm(e.term).split(\" \")[0]);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "78",
     "quote": "check(\"meanings-no-word\", \"No meaning uses its word\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "68",
     "quote": "check(\"meaning-no-word\", \"The meaning does not use the word\", !norm(item.meaning).split(\" \").includes(norm(item.centre)), \"the meaning uses the centre word\"),",
     "verbatim": true
    }
   ],
   "against": "The word-in-focus gloss is not checked for its word (word-in-focus.js lines 31 and 54-59). No test plants a definition that uses another form of its word.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep",
   "reason": "Quotes are verbatim (key-words.js lines 1-2 and 93; web/lesson.js line 541). The page removes the cards before the first gap appears (web/lesson.js line 540). This is a design adopted from another build, and nothing here measures recall. This is not on record.",
   "statement": "Teach a small set of words by study then recall: put the set away and have each word typed from memory into a true sentence about the text, cued by its meaning.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "1-2",
     "quote": "Key words: study a set, then recall each word into a gap. Each word comes back in a sentence about the text with a blank where it goes, cued by its meaning, and the student types it from memory.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "541",
     "quote": "Study each word and what it means. Then put them away, and put each back into its sentence from memory.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "93",
     "quote": "Is filled_${i} true to passage?",
     "verbatim": true
    }
   ],
   "against": "None found. Nothing measures recall.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim, and the planted test (mechanics.test.mjs lines 100-101) sets the accept list on the gap. Fix: the pointer applies only when the writer listed the other word as fitting, because key-words.js line 117 needs w.accept. Another deck word that was not listed gets a miss line giving both meanings (line 120).",
   "statement": "A recall gap must point to one word: check that its cue singles that word out from the rest of the set, and when the writer has listed another word of the set as also fitting the sentence, point the student to the cued meaning instead of marking a miss.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "92",
     "quote": "With meaning_${i} as its cue, does gap_${i} point to word_${i} rather than to any other word in deck?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "53",
     "quote": "\"accept\": [\"any OTHER word of this deck that would also fit the blank; usually none\"]}.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "117",
     "quote": "\"${other.word}\" fits the sentence too. But this meaning is ${w.meaning}. Which word is that?",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/mechanics.test.mjs",
     "lines": "101",
     "quote": "assert.equal(fits.correct, null, \"another deck word that fits the sentence is not a miss\");",
     "verbatim": true
    }
   ],
   "against": "An unlisted deck word that also fits is marked a miss (key-words.js line 120). The judge's points-to check has no labelled cases.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 29,
   "verdict": "keep",
   "reason": "Quotes are verbatim (key-words.js lines 118-121), and a near spelling means an edit distance of two or less. Tests plant a near spelling and a deck mix-up (mechanics.test.mjs lines 98-99) and the release (lines 102-103). The first-letter line gives away part of the answer, which runs against record 14.",
   "statement": "Fit a recall hint to the kind of miss: a near spelling is told it is nearly right, a mix-up with another taught word is shown both meanings, anything else gets the first letter, and the second miss gives the word.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "119",
     "quote": "const line = dist(plain(w.word), n) <= 2 ? \"Nearly. That is the word, but the spelling is not right yet.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "120",
     "quote": "\"${other.word}\" means ${other.meaning}. This one means ${w.meaning}.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "118",
     "quote": "Here is the word: \"${w.word}\" (${w.meaning}). Hold on to it: you will use it today.",
     "verbatim": true
    }
   ],
   "against": "The last hint gives away part of the answer: `The word you want begins with \"${w.word.charAt(0).toUpperCase()}\".` (key-words.js line 121).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 30,
   "verdict": "keep",
   "reason": "Quotes are verbatim. The generous play-time question does not mention spelling (word-web.js line 110). The spelling allowance comes from the seed label (word-web.linked.json line 13) and the animated rubric's wording ('spelling slips are fine', animated.js line 113), and neither has been measured. The deck marks an exact match and gives a nudge at an edit distance of two or less. Related to record 25, but this adds that strictness depends on the task.",
   "statement": "Match how strict marking is to the task: a word a student brings from memory counts if a reader could reasonably link it, spelling slips and all, while a word just taught must be typed exactly and a near spelling gets a nudge.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "3-4",
     "quote": "a near spelling gets a nudge, since a taught word is spelled right",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "110",
     "quote": "Could a Grade 9 reader reasonably link word to centre: a kind of it, a sign of it, a word for someone who shows it, or what it does to people? A random word, a name, or a word with no link does not count.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/calibration/word-web.linked.json",
     "lines": "13",
     "quote": "Deceive, misspelt: the link is plain, and the web does not mark spelling.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "113",
     "quote": "One real English word or short phrase (spelling slips are fine) connected to ${it.centre}",
     "verbatim": true
    }
   ],
   "against": "Whether the judge accepts misspellings has not been measured, and the seed case is a label only.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim, but the measure does not do what its comments claim. Alphabetical order leaves a word in its recall place whenever it happens to agree with the writer's order. In the three decks on record, two, one and two words kept their places. In runs/blocks/cd006e767ac5b219.json, the first gap's word is also first in the study order (lines 10 and 65), so the animated export, which uses the first gap and lists its options in deck order (animated.js lines 147-152), would make it the first card and the first option. The fix adds a code check, as record 45 does for answer positions.",
   "statement": "When students study a set and then recall it, put the set in an order unrelated to the recall order and check in code that no word keeps its place: alphabetical order, used for this, left at least one word in its recall place in each of the three decks made.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "100",
     "quote": "// the study set in alphabetical order, and the gaps with their cues, so no gap lines up with its word",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "146",
     "quote": "// in alphabetical order, so neither the first card nor the first option is the gap's word",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "149",
     "quote": "const g = it.words[0], at = g.gap.indexOf(BLANK);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/cd006e767ac5b219.json",
     "lines": "10",
     "quote": "\"word\": \"consecrate\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/cd006e767ac5b219.json",
     "lines": "65",
     "quote": "\"word\": \"consecrate\",",
     "verbatim": true
    }
   ],
   "against": "On the page the cards are removed before the gaps appear (web/lesson.js line 540), so a matching position is only a weak cue there. The multiple-choice export is where it matters.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 32,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. Fix: 'most play needs no judge' rests on one live session, where the judge decided 2 of 8 ticks (v02/QA.md lines 21-22), so that number replaces 'most'. 'Replays exactly' is not unique to code, because judged ticks also replay exactly from their recorded judgments (core/runtime.js line 4).",
   "statement": "Settle in code whatever code can settle, an exact word or a line already accepted, and send only the rest to the judge: in one live session the judge was needed on 2 of 8 ticks.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "4-5",
     "quote": "Play needs no judge and replays exactly.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
     "lines": "70",
     "quote": "// Play time: a line outside the accepted set is put to the judge, so a fair answer the author did not foresee counts.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "3-4",
     "quote": "A word the reader adds counts at once if it is a form of the centre or a key word; any other word is put to the judge, generously",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "21",
     "quote": "8 ticks in all: one wrong answer on the quick check, and one tap on a line nobody keyed in the evidence hunt.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "22",
     "quote": "Jev decided at play time on 2 ticks",
     "verbatim": true
    }
   ],
   "against": "Judged play replays exactly too: \"Given the same actions and the same recorded judgments a session replays exactly.\" (core/runtime.js line 4).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 33,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim, and the dropped synonym is tested (test/animated.test.mjs line 59). Fix: the forms that count at once are never checked one by one by the judge. Code keeps a form from the writer only if it shares its word's first four letters (lines 15 and 60), and that rule also admits a non-form that starts the same way. The older note in word-web.linked.json line 5 still says likely words skip the judge.",
   "statement": "Let code accept an answer on its own only if it was checked item by item beforehand, by the judge or by a code rule: in the word web, the centre and key words the judge checked, and their forms if they share the word's first four letters; a writer's list of likely answers, judged only as a whole, goes to the judge word by word.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "99-100",
     "quote": "code knows only the forms of the centre and the key words (Jev checked those); any other word, the writer's likely ones included, is the judge's to decide, so here it stays pending",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "86",
     "quote": "q: noul(\"likely_linked\", \"Are most of the words in likely clearly connected to centre?\"), expect: \"yes\" },",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "59",
     "quote": "// a form shares the start of its word (\"deceive\", \"deception\" for \"deceit\"); a synonym (\"lie\") is dropped",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "15",
     "quote": "const stemOf = (w) => norm(w).replace(/[^a-z]/g, \"\").slice(0, 4);",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/animated.test.mjs",
     "lines": "59",
     "quote": "assert.ok(web.families[0].words.includes(\"deception\") && !web.families[0].words.includes(\"lie\"), \"forms, not synonyms\");",
     "verbatim": true
    }
   ],
   "against": "An older note still says likely words skip the judge: \"A word that is not the centre, a key word, one of their forms or a likely word goes to the judge at play time.\" (test/calibration/word-web.linked.json line 5). The four-letter rule would admit an unrelated word with the same start.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 34,
   "verdict": "keep",
   "reason": "Quotes are verbatim (word-web.js lines 41-43; v02/QA.md lines 83-84). runs/blocks/9bce29e80207fd23.json line 90 shows one of the three key words that failed the link question after two tries. There is one draft before the prompt change and one after, and the link verdicts are the judge's own, with no labels. This is close to record 54's 'not the rarest ones', but it concerns words for writing about a theme and adds a measured case.",
   "statement": "Words taught for writing about a big idea must stand in a stated relation to it (a kind of it, a sign of it, a word for someone who shows it, or what it does to people), not be hard words from the text only loosely linked; one draft built on such words was held.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "41-43",
     "quote": "each clearly part of a web for the centre (a kind of it, a sign of it, a word for someone who shows it, or what it does to people), such as \"betrayal\" or \"duplicity\" for deceit. Not a hard word from the text that is only loosely linked.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/v02/QA.md",
     "lines": "83-84",
     "quote": "The first draft's key words were hard words from the text (\"obsequious\", \"homage\", \"peculiar\") for \"resentment\", and Jev held it;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/9bce29e80207fd23.json",
     "lines": "90",
     "quote": "belongs in a web for the centre: the judge found this does not hold",
     "verbatim": true
    }
   ],
   "against": "None found. It is one case, judged by the model and never by a person.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 35,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. The word web is first in the palette (index.js line 24) and first in the animated export's pages (animated.js line 194). Fix: nothing compares the key words with the student's web, so the block cannot show which key words are new to that student. It reveals the key words as the new ones (word-web.js line 94).",
   "statement": "Open with a web of words students already bring to the text's big idea, accepted generously, then turn over the lesson's key words for it as the new ones.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "1-2",
     "quote": "Word web: the big idea that runs through the text, as one word at the centre of a web the reader builds from memory; then the lesson's key words for it land face down, and each is said before it is turned.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "94",
     "quote": "Some of these words you brought with you, and some are new. The new ones are this lesson's key words for ${item.centre}.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/glue/animated.js",
     "lines": "108",
     "quote": "Before we read, show me what you already know. Build me a web for this one word.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/index.js",
     "lines": "24",
     "quote": "wordWeb, filmCheck, videoEssay, learningQuestion, keyWords,",
     "verbatim": true
    }
   ],
   "against": "The key-word deck is not yet linked to the web: \"Key words are not seeded from the word web's words.\" (README.md line 114).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 36,
   "verdict": "keep-with-fix",
   "reason": "The word-web case is confirmed. In runs/blocks/096b952e5ee95da5.json line 99, the hint used 'false', one of the likely words, and the reason did not name it (v02/QA.md line 140). Fix: the two 0.59 cases do not show the 'plainly holds' wording working. The glossary draft (2026-10-09T13:30Z) came before that wording, since records made at 14:18Z still say 'the judge found this unclear' (runs/blocks/0e36e4f6c770a7b1.json line 120). In both cases, the second draft replaced the unconfirmed word instead of rewriting it.",
   "statement": "When a check holds a draft, its reason must tell the writer what to change: name the offending words, and where the judge was unsure, ask for a version that plainly holds, because the writer gets one correction pass; one draft whose reason said only that its hint used a likely word, not which, was still held after it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/096b952e5ee95da5.json",
     "lines": "99",
     "quote": "\"The hint names none of the likely words: the hint names a likely word\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
     "lines": "74",
     "quote": "// the reason names the words, so the one correction pass can take them out",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "51",
     "quote": "for (let attempt = 1; attempt <= 2; attempt++) {",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "78",
     "quote": "// an unsure judge is not a no: the correction asks for a version that plainly holds, not for its opposite",
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
     "quote": "\"Beat 3: the first reading can be defended: the judge found this unclear\"",
     "verbatim": true
    }
   ],
   "against": "No record shows a named reason or the 'plainly holds' wording rescuing a draft. In both unsure cases, the writer swapped the item out.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 37,
   "verdict": "keep",
   "reason": "Quotes are verbatim. The held draft's hints say 'the fourth line', 'the fifth line' and 'line five' (runs/blocks/d872bc1dfbda65fb.json lines 22, 35, 36, 50 and 51), yet its no-line-numbers check is ok (lines 96-98). The pattern matches only forms like L12 or line 12 (util.js line 46), and so does the question check (question.js line 12). This adds a measured gap in the check behind record 53, so it is not a duplicate.",
   "statement": "A check for line references must catch numbers in words and ordinals, such as \"line five\" or \"the fifth line\", not only digits: one held draft's hints cited lines that way and passed it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/d872bc1dfbda65fb.json",
     "lines": "36",
     "quote": "\"second_nudge\": \"Examine the start of line five to see how the lip is described.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/d872bc1dfbda65fb.json",
     "lines": "35",
     "quote": "\"nudge\": \"Look at the fifth line for details about the mouth.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/d872bc1dfbda65fb.json",
     "lines": "96-98",
     "quote": "\"id\": \"no-line-numbers\", \"label\": \"No student text cites a line number\", \"ok\": true,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "46",
     "quote": "const LINE_NUMBER = /\\b(?:L\\d+|lines?\\s+\\d+)/i;",
     "verbatim": true
    }
   ],
   "against": "None found. The draft was held for another reason, so these hints did not ship.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 38,
   "verdict": "keep-with-fix",
   "reason": "I confirmed this by reading the code; I did not run it. When an action carries no try count, the runtime supplies the entity's attempt count (core/runtime.js line 60), and it counts a tick unless a required check was unsure (line 83). The key-word deck releases at tries of 1 or more (key-words.js line 118), so after one right gap, the first miss on the next gap gives the word. An open-check answer set aside as aimed at the marker also counts, and so does a thin answer, so the next sure miss shows the answer. The page counts only sure misses, gap by gap (web/lesson.js lines 522 and 531), while the scripted players drive the runtime (playtest.js line 102). The fix is for precision. The found_by overstates: runtime.test.mjs lines 104-105 test the release with the try count supplied, but no test covers the runtime's own count.",
   "statement": "How tries are counted decides when the answer appears: the lesson page counts sure misses gap by gap, while the session runtime counts every answer the judge did not leave unsure, across the whole block, so in a session the first miss on a later gap, or one after an answer set aside as aimed at the marker, shows the answer at once.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/core/runtime.js",
     "lines": "83",
     "quote": "if (!unsure.length || response.correct != null) es.attempts++;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/web/lesson.js",
     "lines": "531",
     "quote": "if (res.correct === false) tries++;",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "110",
     "quote": "// words aimed at whoever marks them are not an answer: no verdict, and no try (the Grade 3 engine's rule)",
     "verbatim": true
    }
   ],
   "against": "The runtime's own comment says the two agree: \"the runtime knows how many tries this entity has had, so a mechanic's release rule (two tries, then the answer) works in a session as it does in a page that counts its own\" (core/runtime.js lines 58-59). This has not been confirmed by a planted case.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 39,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. The threshold is the larger of 3 and the right option's word count, so a right option of one or two words can never be matched. The planted fault repeats a whole option of several words (test/video.test.mjs line 55), and the film stops use the same rule (util.js line 116). Fix: two-word answers are affected too.",
   "statement": "How to catch feedback that names a short answer: the choice question's rule flags a wrong option's feedback only when it repeats the whole right option and that option has three or more words, so it can never fire on a one- or two-word answer such as a name.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "53-54",
     "quote": "check(\"feedback-no-answer\", \"Wrong-option feedback does not name the answer\", item.feedback.every((f, i) => i === item.answer || sharedRun(f, right) < Math.max(3, right.split(/\\s+/).length)), \"a wrong option's feedback names the right answer\"),",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/video.test.mjs",
     "lines": "55",
     "quote": "(i === wrong ? `No: the answer is ${right}.` : f)",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "116",
     "quote": "const naming = checks.flatMap((c, k) => c.feedback.map((f, i) => ({ k, i, f })).filter(({ i, f }) => i !== c.answer && sharedRun(f, c.options[c.answer]) >= Math.max(3, words(c.options[c.answer]).length)));",
     "verbatim": true
    }
   ],
   "against": "None found.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 40,
   "verdict": "keep",
   "reason": "Quotes are verbatim. The block's code checks (word-in-focus.js lines 54-59) and judge questions (lines 84-88) cover the word, the gloss, the key, the wrong options, temptation and a clean line. They do not cover either give-away rule its prompt states, and the quick check enforces both (quick-check.js lines 52-54). This comes from reading code; there is no planted case.",
   "statement": "Whether a block's give-away rules hold when nothing checks them: one block's prompt forbids a question that contains the gloss and wrong-option feedback that names the answer, yet no code check or judge question tests either.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-in-focus.js",
     "lines": "32",
     "quote": "- stem: a question about what it means or does in this line, ending in \"?\", not containing the gloss.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-in-focus.js",
     "lines": "33-34",
     "quote": "feedback: one sentence per option (wrong ones send the reader back to the line without naming the answer).",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/word-in-focus.js",
     "lines": "55",
     "quote": "check(\"stem-question\", \"The question ends in a question mark\", item.candidates.every((x) => /\\?\\s*$/.test(x.stem)), \"a question does not end with a question mark\"),",
     "verbatim": true
    }
   ],
   "against": "None found.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/laws.test.mjs",
   "lines": "27",
   "quote": "// key shapes, each tried on a sample made here, so a law that could never fire fails too",
   "ok": true
  },
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/index.js",
   "lines": "2",
   "quote": "codeChecks (facts), judge (bounded questions with positive evidence), view (what the student sees; never a key)",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "context",
   "path": "~/Projects/g9/transformer/README.md",
   "lines": "120",
   "quote": "No lesson has been reviewed by a person or used by a student.",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "qualifies",
   "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
   "lines": "86",
   "quote": "// its own words only: a famous text's answer is known to anyone who knows the work, which is no give-away of the question's",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
   "lines": "110",
   "quote": "// words aimed at whoever marks them are not an answer: no verdict, and no try (the Grade 3 engine's rule)",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "59-60",
   "quote": "EH-1 refused a line that does not prove the claim with its hint, and accepted \"In following him, I follow but myself\", a fair line nobody keyed, on Jev's decision",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
   "lines": "83",
   "quote": "// the judge unsure or absent: the hint, no miss, and the line kept for review",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
   "lines": "1-2",
   "quote": "Glossary: dotted words in the text that open a short note, for the words a Grade 9 reader needs explained to follow it",
   "ok": true
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/util.js",
   "lines": "9-10",
   "quote": "Anything in quotation marks is the text's own words, copied exactly, in double quotes: never put a paraphrase in quotes.",
   "ok": true
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
   "lines": "27-28",
   "quote": "Wrong option: one sentence that sends the reader back to specific words (quote a few of them) without naming the right answer.",
   "ok": true
  },
  {
   "truth": 14,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
   "lines": "121",
   "quote": "`The word you want begins with \"${w.word.charAt(0).toUpperCase()}\".`",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports in part",
   "path": "~/Projects/g9/transformer/src/mechanics/learning-question.js",
   "lines": "99",
   "quote": "\"Saved, beside your first answer.\"",
   "ok": true
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
   "lines": "100",
   "quote": "Does student_text say requirement_${k}, in meaning? Any wording counts, and a short answer that says it is enough.",
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
   "truth": 28,
   "effect": "supports in part",
   "path": "~/Projects/g9/transformer/src/mechanics/word-in-focus.js",
   "lines": "73",
   "quote": "// the highest gain among the candidates the judge is sure are clean; with none, the highest, which the judge holds",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "63",
   "quote": "the word-in-focus card showed the meaning before the question",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/glue/animated.js",
   "lines": "29",
   "quote": "// Nothing a student needs to work out is on screen before they answer: the key-term card's \"meaning\" holds the context.",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/util.js",
   "lines": "6-7",
   "quote": "The tone is adult and precise: no games language, no exclamation marks, no \"Great job\", nothing that reads as written for young children.",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports in part",
   "path": "~/Projects/g9/transformer/src/mechanics/word-in-focus.js",
   "lines": "2-3",
   "quote": "The writer proposes candidates; the judge scores each for knowledge carried, and code takes the highest. One bounded question per candidate, never a wide choice.",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports in part",
   "path": "~/Projects/g9/transformer/src/mechanics/index.js",
   "lines": "22",
   "quote": "// the palette in the order a lesson runs: openers, the reading, practice, closers",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/calibration/2026-10-09T12-25-25-449Z.json",
   "lines": "6",
   "quote": "\"note\": \"answers from the labels themselves: proves the wiring, measures nothing\"",
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
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
   "lines": "22",
   "quote": "// bumped when its prompt or checks change, so its blocks are made again (blocks.js)",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "193-194",
   "quote": "Before this fix, a playtest sent the saved link's first six blocks, all made before the line-number rule, and played them; three cited line numbers.",
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
   "effect": "supports in part",
   "path": "~/Projects/g9/transformer/src/mechanics/learning-question.js",
   "lines": "2-3",
   "quote": "At the end of the lesson it is answered again, saved beside the first and never marked (the 3D build's bookends)",
   "ok": true
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/test/positive-evidence.test.mjs",
   "lines": "1-2",
   "quote": "with no judge, a judge that cannot be reached, or one that is unsure, no judged action of any mechanic is marked wrong or completes on the judge's word",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "64-65",
   "quote": "QC-2 was a copy of QC-1",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
   "lines": "13",
   "quote": "// what this block is about, so a second block of the same kind on the same text is told to differ",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/playtest/2026-10-09T12-18-55-414Z.json",
   "lines": "139",
   "quote": "\"detail\": \"stopped at tick 200 after 190 tries: no attempt ceiling and no reveal\",",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/v02/QA.md",
   "lines": "141",
   "quote": "the hunt and debate now release after two tries",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "qualifies",
   "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
   "lines": "90",
   "quote": "return { correct, feedback: item.feedback[i], reveal: correct ? { units: item.evidence } : null, done: correct };",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/evidence-hunt.js",
   "lines": "2-3",
   "quote": "At play time a line is a miss only when the judge is sure it is not evidence; unsure, the reader gets the hint with no verdict.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/word-web.js",
   "lines": "5",
   "quote": "// Only a confident no is \"Not about\" the centre; a word the judge was unsure of, or could not check, stays pending.",
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
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/playtest/2026-10-09T12-25-25-328Z.json",
   "lines": "248",
   "quote": "Review lines 7 and 8 to see who was recommending Iago for this permanent post.",
   "ok": true
  },
  {
   "truth": 53,
   "effect": "supports in part",
   "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
   "lines": "16",
   "quote": "/** The words of `term` as they are written in `text` (case, curly apostrophes, spacing), or null. */",
   "ok": true
  },
  {
   "truth": 54,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/word-in-focus.js",
   "lines": "17",
   "quote": "summary: \"The word that carries the most knowledge, glossed for this line and asked about. Chosen by knowledge carried, not by difficulty.\",",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/learning-question.js",
   "lines": "71-72",
   "quote": "one Jev choice on what it adds to the first, shown only when Jev is sure, and never as a mark. The line is ours and quotes neither answer.",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "supports in part",
   "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
   "lines": "4-5",
   "quote": "A section of the 3D build carries its own glossary: its terms and notes are passed through unchanged, each where its line mark puts it, and nothing is drafted.",
   "ok": true
  }
 ]
}
```
