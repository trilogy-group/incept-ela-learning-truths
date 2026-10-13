# read:gap:draft-vs-remake-judge-logs

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  nono, analyse its ideas and fold them into the research results

## Result

```json
{
 "direction": "draft-vs-remake-judge-logs",
 "coverage": {
  "read": [
   "~/Projects/g9/transformer/runs/decisions/ (the 14 named logs, every entry: 0419fc2dc6f6bacf, 1ed330c52090f0fc, 963297774d627c12, 68d85cc9b79fb956, b5f74899349e1331, be97f27fc4c4a65a, 366b8d2c7104a608, 38cf6a0077428ec2, 815626dc60c1b455, 4397f06c124fdff7, 856ace1aed960671, c98cc9de312f4d43, a775ad50ec1c4070, b9cb3d0f3a8639c0), extracted to stdout with python3 -I: at, tag, samples, changed state fields with old and new values, and pass, value, top, margin, agreement, gate_reasons per question",
   "~/Projects/g9/transformer/runs/blocks/<same 14 keys>.json (status, tries, judgeCalls, reasons, code checks, judge results, item)",
   "~/Projects/g9/transformer/runs/blocks/*.json (all, scanned only for keyed-answer positions of quick-check, compare-paragraphs and film-check blocks)",
   "~/Projects/grade3-reading/engine/src/decide/client.js",
   "~/Projects/grade3-reading/engine/src/decide/questions.js (gates, aggregation, agreement, option rotation)",
   "~/Projects/grade3-reading/engine/src/decide/providers/jev.js (rotation lines only, via grep)",
   "~/Projects/g9/transformer/src/blocks.js",
   "~/Projects/g9/transformer/src/judge.js",
   "~/Projects/g9/transformer/src/transform.js",
   "~/Projects/g9/transformer/src/engine.js",
   "~/Projects/g9/transformer/src/films.js (pickFilm)",
   "~/Projects/g9/transformer/src/mechanics/film-check.js, evidence-hunt.js, compare-paragraphs.js, worked-model.js, quick-check.js, util.js (whole files); open-check.js lines 1-100; glossary.js and key-words.js (prompt, checks, judge, absorb)",
   "~/Projects/g9/transformer/src/quality/calibrate.js (header, line 61) and ~/Projects/g9/transformer/bin/transformer.mjs (sample defaults, via grep)",
   "~/Projects/g9/transformer/runs/calibration/*.json (check lists and summaries; the quick-check.answerable cases)",
   "~/Projects/g9/transformer/test/calibration/ (listing only)"
  ],
  "skipped": [
   "decisions d2d7d0787d6754d9, 34c293906aa945a2, 7e771d331c6b4135, 4370894c30725db3: film and video logs already read, per the brief",
   "decisions focus-*.json and the word-in-focus #0/#gain logs: two different checks, not remakes, per the brief",
   "the other 50 decision logs: not among the 14 remade blocks",
   "runs/lessons, playtest, sessions, marking, questions, texts, films, render, scenes: outside this direction",
   "transformer/DECISIONS.md, README.md, v01-v11 and the repo .agent/ orientation files: docs and operating notes outside this direction's scope",
   "no .env, key or credential files opened; nothing written"
  ],
  "notes": "Pairing (block status, tries, judgeCalls; current mechanic version from source; last reasons; what the log shows). 0419fc2dc6f6bacf film-check v3: failed, 2 tries, judgeCalls 1, last reason a code check (wrong-option feedback names the answer); log: 3 judgings, film fit 0.02 each time. 1ed330c52090f0fc key-words v2: ready, 2 tries; 2 judgings (second is a fresh try), first had one unsure gloss (0.59). 963297774d627c12 evidence-hunt v1: ready, 1 try; keyed half-line rejected 0.16, corrected. 68d85cc9b79fb956 worked-model v2: ready, 1 try; same-quotation option unsure 0.53, corrected. b5f74899349e1331 open-check v3: failed, 2 tries, last reason give-away (0.69, 0.71, 0.65). be97f27fc4c4a65a worked-model v2: failed, 2 tries, last reason the same-quotation option (0.24, 0.48, 0.31). 366b8d2c7104a608 glossary v1: ready, 2 tries; one unsure gloss 0.59, then a fresh try. 38cf6a0077428ec2 and 815626dc60c1b455 evidence-hunt v1: ready, 1 try each; keyed half-line rejected 0.35 both times, corrected. 4397f06c124fdff7 compare-paragraphs v1: ready, 1 try; weaker-honest 0.50, corrected. 856ace1aed960671 and c98cc9de312f4d43 quick-check v1: ready, 1 try each; key check 0.54 and 0.50, corrected to opposite keys. a775ad50ec1c4070 open-check (made under the older give-away wording): failed, 2 tries, give-away 0.56, 0.70, 0.62, 0.68. b9cb3d0f3a8639c0 worked-model: ready, 1 try; same-quotation option 0.51, corrected. Block files hold no version field: a version above 1 is folded into the key (blocks.js line 25), so versions given are today's source values. Correction passes and fresh tries were told apart from tries and judgeCalls (judgeCalls counts only the last try). All 33 judgings: model jev-1.13.0, prompt engine-bank-2026-09-22.1, samples 1, retried 0, agreement null on all 366 answers; 17 answers fell below the support gates (confidence 0.55, top 0.6, margin 0.15). In these logs 'pass' means an answer cleared those gates, not that the check held; a check expecting 'no' (give-away, known) holds when the value is below 0.5. 8 of the 14 first judged drafts were held for an unsure answer and 6 for a refutation; 8 of 13 correction passes cleared their failing check; 10 blocks ended ready, 4 failed. Beyond the 14 pairs: across all saved ready quick-check blocks the key sat at B in 10, A in 6, C in 1 (options are shown as written); compare-paragraphs stronger A 6, B 4; film-check answers 9/8/7 by position. The drift figure (39 same-content repeats) leaves out checks whose wording does not name every input they read (the quick-check set, give-away). JSON lines are quoted without their leading indentation."
 },
 "candidates": [
  {
   "statement": "Don't make a wrong option by swapping in another word from the same quotation: it often means the same thing, and in each remade worked model it was the one option the judge would not call wrong.",
   "kind": "measured",
   "found_by": "Each of the three remade worked-model blocks was first held because a wrong option for the word blank, another word from the same quotation, could not be confirmed as wrong. The scores were 0.53 (unsure) and 0.51 (unsure), and in the third block 0.24, 0.48 and 0.31 across three drafts that all kept that option. That block failed on it.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/be97f27fc4c4a65a.json",
     "lines": "54, 271",
     "quote": "\"sentence_0_1\": \"The phrase long remember presents spoken rhetoric as something fragile that will quickly fade from human memory.\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/68d85cc9b79fb956.json",
     "lines": "55, 288",
     "quote": "\"sentence_0_2\": \"The noun wrinkled lip implies that the king held his subjects in utter contempt and felt entirely superior to them.\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/b9cb3d0f3a8639c0.json",
     "lines": "55, 288",
     "quote": "\"sentence_0_2\": \"The phrase \\\"upon him\\\" reveals his purely opportunistic nature.\","
    }
   ],
   "against": "Some swaps from the same quotation were judged wrong, for example \"sentence_0_0\": \"The noun frown implies that the king held his subjects in utter contempt and felt entirely superior to them.\" at 0.78 (68d85cc9b79fb956.json lines 54, 271). One correction kept the same-quotation words but framed them as \"The verb phrase \\\"upon him\\\"\", and they then passed at 0.97 (b9cb3d0f3a8639c0.json lines 426, 643). So the swap fails only when the neighbouring word means the same.",
   "scope_note": "universal for choice blanks built from a quotation; seen in worked-model rebuild blanks",
   "adds_to_existing": [
    31
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Tell a correction exactly which part failed, keep the rest, and check in code that the failing part changed: told of one failing check, rewrites changed most of the item, and twice the failing part came back as it was.",
   "kind": "measured",
   "found_by": "Each of the 13 correction passes in the logs started from exactly one failing required check, and the correction prompt asks for the whole reply again. The rewrites changed 10 or 11 of 17 judged fields in the worked models, and both paragraphs of a comparison when only the weaker one was in doubt. In one open check, the correction for an unsure give-away judgment on the question changed the requirement, hint and reveal but left the question word for word; the give-away score then rose to 0.70 and failed. In one worked model, the correction kept the option that had failed (0.48 unsure, then 0.31). 8 of the 13 passes cleared their failing check.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "20",
     "quote": "YOUR PREVIOUS DRAFT FAILED THESE CHECKS. Fix every one and return the whole JSON again:"
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/a775ad50ec1c4070.json",
     "lines": "21, 111, 164, 254",
     "quote": "\"q\": \"According to Iago, what is his only reason for continuing to serve Othello?\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/be97f27fc4c4a65a.json",
     "lines": "423, 658, 796, 1017",
     "quote": "\"sentence_0_1\": \"The phrase long remember suggests that spoken dedications carry minimal lasting weight in human history.\","
    }
   ],
   "against": "8 of 13 corrections did clear their failing check. The narrowest one changed 1 of 2 fields and worked: \"claim\": \"The expression on the ruined statue shows that the ruler possessed a disdainful and harsh authority.\" (963297774d627c12.json line 160).",
   "scope_note": "universal for draft, check and correct loops",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Before writing questions on a film or other media, check that it is about the lesson's text and stop if it is not: a best-match picker always returns something, and rewriting the questions cannot fix a mismatch.",
   "kind": "measured",
   "found_by": "In the 12 October universality test, a poem lesson was given the unit film on a play. The picker returns whichever film shares the most words with the text, with no minimum. In all three judgings, the bounded fit question scored 0.02 while every question-level check passed. The writer rewrote the questions each time (draft one asked when the play was written), and the block failed.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/films.js",
     "lines": "55, 62",
     "quote": "/** The film whose narration shares most words with the text and the question; null if there is none. */"
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
     "lines": "60, 187, 794, 1401",
     "quote": "\"instructions\": \"Is film_narration about the same work as passage, so that it can open a lesson on it?\""
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
     "lines": "20, 23",
     "quote": "\"question_0\": \"When was the play written?\","
    }
   ],
   "against": "none found; the fit question caught the mismatch every time",
   "scope_note": "universal for any item built on media chosen automatically",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When an item fails, keep the reasons from every attempt, because the last attempt's reason can name a side fault and hide the cause.",
   "kind": "measured",
   "found_by": "The failed film-check block records one reason, from its last attempt, which was never judged: wrong-option feedback names the answer. It counts 2 tries and 1 judge call. Its log shows three judgings, and in each the judge found the film was not about the lesson's text (0.02).",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/0419fc2dc6f6bacf.json",
     "lines": "97",
     "quote": "\"Wrong-option feedback does not name the answer: question 2, option A: its feedback names the right answer; question 2, option C: its feedback names the right answer\""
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/0419fc2dc6f6bacf.json",
     "lines": "162-163",
     "quote": "\"judgeCalls\": 1,"
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
     "lines": "187, 794, 1401",
     "quote": "\"value\": 0.02,"
    }
   ],
   "against": "The full log of every attempt is kept beside the block (\"// every try's decide records, as decide made them, so the block can be re-judged through a second judge\", blocks.js line 93), so the cause can be recovered by reading it.",
   "scope_note": "universal",
   "adds_to_existing": [
    21
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When the evidence is a sentence that runs across lines, credit the whole sentence: judged one line at a time, one half of a two-line proof is rejected, so a reader who picks that half is not credited.",
   "kind": "measured",
   "found_by": "In all three remade evidence hunts, the first draft keyed two adjacent lines of one sentence. The judge, asked whether each line read on its own proves the claim, rejected one of them (0.16; 0.35; 0.35), and the correction keyed only the other. In the shipped poem block, the reveal explains the proof with the rejected line's word ('a frowning mouth') while only the other line is accepted.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/38cf6a0077428ec2.json",
     "lines": "22-23, 90",
     "quote": "\"L9\": \"L9 [IAGO] Heaven is my judge, not I for love and duty,\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/963297774d627c12.json",
     "lines": "22-23, 60",
     "quote": "\"L4\": \"L4 Half sunk a shattered visage lies, whose frown,\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/963297774d627c12.json",
     "lines": "13-16",
     "quote": "\"reveal\": \"The ruined face shows a frowning mouth with a cold expression, showing the ruler's harsh authority.\","
    }
   ],
   "against": "The rejected halves may really be weaker evidence on their own, and the same one-line-at-a-time questions are what let an unkeyed line be accepted elsewhere (38cf6a0077428ec2.json line 30, 0.89 at line 226).",
   "scope_note": "verse and drama; any task where evidence is picked by line",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Don't assume the writer's key is the best answer: judge every candidate, because a line nobody keyed can prove the point better than the keyed one.",
   "kind": "measured",
   "found_by": "One claim was judged four times: two separate makings, each a draft and its correction. Each time, a line the writer had not keyed scored 0.84 to 0.89 while the keyed line scored 0.75 to 0.78. The build accepted the unkeyed line as a further right answer.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/38cf6a0077428ec2.json",
     "lines": "30, 107, 226",
     "quote": "\"L3\": \"L3 [IAGO] I follow him to serve my turn upon him.\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/815626dc60c1b455.json",
     "lines": "339, 475",
     "quote": "\"value\": 0.87,"
    }
   ],
   "against": "One further accepted line sat exactly at the gate's floor on a single sample (\"p\": 0.6, 815626dc60c1b455 block line 82). The engine calls its gates \"conservative engineering thresholds, not calibrated correctness\" (questions.js line 105).",
   "scope_note": "universal for keyed-answer items that allow several defensible answers",
   "adds_to_existing": [
    7,
    33
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Ask the judge for the answer without showing it the key, then compare: asked only to confirm a key, it confirmed opposite keys to one ambiguous question.",
   "kind": "measured",
   "found_by": "Two makings of a quick check on the same poem began with the same ambiguous question (who speaks most of the poem), and the key check was unsure both times (0.54, 0.50). Each correction reworded the question. One keyed the narrator, confirmed at 0.90, with the traveller judged wrong at 0.69. The other keyed the traveller, confirmed at 0.73. Both passed every required check and shipped as ready.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/856ace1aed960671.json",
     "lines": "227, 230, 233, 296",
     "quote": "\"B\": \"The narrator who is repeating what a traveler told him\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/c98cc9de312f4d43.json",
     "lines": "227, 229, 233, 297",
     "quote": "\"A\": \"The traveler who visited the antique land\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/856ace1aed960671.json",
     "lines": "52, 259",
     "quote": "\"instructions\": \"Using only evidence_lines, is the option named by keyed_answer a correct answer to the question?\""
    }
   ],
   "against": "The first drafts' unsure answers did flag the ambiguity (\"value\": 0.54, 856ace1aed960671.json line 89; \"value\": 0.5, c98cc9de312f4d43.json line 89). A framed narrative may defensibly allow both readings. The fault is that rewording made the judge sure without making the text settle the answer.",
   "scope_note": "universal for choice items checked by a judge",
   "adds_to_existing": [
    11,
    5,
    31
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Hold a choice question whose wrong options would tempt no one, not only one with a wrong option that is right, because an option nobody picks tests nothing.",
   "kind": "measured",
   "found_by": "In the four judged drafts of the two remade quick checks, 7 of 8 judgments on whether a wrong option would tempt a skimmer said no (0.35 to 0.39) or were unsure (0.46, 0.48). That check is not required, so both questions shipped. The worked-model and film checks ask nothing about plausibility.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "74",
     "quote": "id: `tempting-${letters[i]}`, label: `Option ${letters[i]} would tempt a reader who skimmed`, required: false,"
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/c98cc9de312f4d43.json",
     "lines": "144, 161, 348, 365",
     "quote": "\"value\": 0.36,"
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/856ace1aed960671.json",
     "lines": "144, 161, 364",
     "quote": "\"value\": 0.39,"
    }
   ],
   "against": "The prompt already asks for tempting options (\"- Exactly three options. Exactly one is right given the text; the other two are tempting to a skimmer but the text\", quick-check.js line 23). The plausibility judgment has no labelled cases, so making it required could hold back good questions.",
   "scope_note": "universal for multiple-choice items",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When a judge is unsure of a gloss on a familiar word used in an older sense, send it to a person instead of dropping it, because those are the words a reader most needs explained.",
   "kind": "measured",
   "found_by": "In two remade blocks, the only unsure glosses were on familiar words used in an older sense: 'owe' glossed as own or possess (0.59), and 'mocked' glossed as copied or represented in art (0.59). Whether a reader knows 'owe' unaided was also unsure (0.44). Neither word reached the version that shipped, although the key-word prompt itself asks for older senses.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/366b8d2c7104a608.json",
     "lines": "47-49, 310, 482",
     "quote": "\"note_9\": \"own or possess\""
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/1ed330c52090f0fc.json",
     "lines": "37-38, 275",
     "quote": "\"meaning_2\": \"copied or represented something in an artistic work\","
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "49",
     "quote": "about it (a rank, an older sense, a word for what a character does or is), to study and then recall from memory."
    }
   ],
   "against": "Both later drafts were fresh tries, not corrections, so the words may have gone by chance. The second word's gloss gives only one of its two senses.",
   "scope_note": "older texts (early modern drama, Romantic verse); glossaries and key-word decks",
   "adds_to_existing": [
    54
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A check that fails every draft proves nothing until it passes an item known to be clean, so test a blocking check on good items as well as planted faults.",
   "kind": "measured",
   "found_by": "The open-check give-away check failed all seven judged drafts of two open questions, rewrites included: 0.56 unsure, then 0.70, 0.62 and 0.68; and 0.69, 0.71 and 0.65. It held both blocks back. One failing draft asked only for a character's purpose without stating it. There is no labelled calibration set for this check; test/calibration holds sets for five other checks.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/a775ad50ec1c4070.json",
     "lines": "444, 534",
     "quote": "\"q\": \"According to Iago, what is his purpose in continuing to serve Othello?\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/a775ad50ec1c4070.json",
     "lines": "37",
     "quote": "\"The question does not give its answer away: the judge found this does not hold\""
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/b5f74899349e1331.json",
     "lines": "39",
     "quote": "\"The question does not give its answer away: the judge found this does not hold\""
    }
   ],
   "against": "The three drafts on the speech did name both sides of the contrast they asked about (b5f74899349e1331.json line 21), so some of the seven may be real give-aways.",
   "scope_note": "universal for any judged check that can block an item",
   "adds_to_existing": [
    1,
    35
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge whether a question gives its answer away from its own words only, not from what anyone who knows a famous work would know.",
   "kind": "adopted rule",
   "found_by": "Between the 9 and 12 October runs, the give-away instruction was rewritten to judge only the question's wording, and the mechanic's version was raised so its blocks are remade. The code gives the reason: anyone who knows a famous work knows its answers.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "86-87",
     "quote": "// its own words only: a famous text's answer is known to anyone who knows the work, which is no give-away of the question's"
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/a775ad50ec1c4070.json",
     "lines": "48",
     "quote": "\"instructions\": \"Does the wording of q by itself give away what a good answer must say?\""
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/b5f74899349e1331.json",
     "lines": "48",
     "quote": "\"instructions\": \"Do the words of q themselves state, or nearly state, what a good answer must say? Judge only the wording of q, not what a reader may already know about the work.\""
    }
   ],
   "against": "After the change, all three drafts of a question on a famous speech still failed the check (\"value\": 0.65 at b5f74899349e1331.json line 437; 0.69 and 0.71 at lines 111 and 280).",
   "scope_note": "universal; matters most for famous texts",
   "adds_to_existing": [
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "How to ask an open question about a contrast the text states outright without giving it away: every draft that named the two things contrasted was judged a give-away.",
   "kind": "open question",
   "found_by": "All three judged drafts of one open question named both sides of the contrast the text states, and two also named what was being compared (durability, endurance). The give-away check said yes each time (0.69, 0.71, 0.65), and no wording that passes was produced.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/b5f74899349e1331.json",
     "lines": "21, 111",
     "quote": "\"q\": \"What difference does the speaker draw between the endurance of the ceremony and the impact of the fighting?\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/b5f74899349e1331.json",
     "lines": "161, 280",
     "quote": "\"q\": \"How does the speaker contrast the durability of what the soldiers did with the durability of the speech?\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/b5f74899349e1331.json",
     "lines": "347, 437",
     "quote": "\"q\": \"What difference does the speaker draw between the endurance of spoken words and the actions of the soldiers?\","
    }
   ],
   "against": "The give-away check has no labelled cases, so it is not settled that these questions do give the answer away.",
   "scope_note": "open reading questions on texts built around a stated contrast",
   "adds_to_existing": [
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Expect a judge to waver most where the question is arguable: settled questions barely moved between drafts, while one unchanged word-class call moved from 0.70 to 0.41.",
   "kind": "measured",
   "found_by": "I compared 39 pairs of judgments on questions whose named inputs were the same across drafts, all made at one sample. The median shift was 0.01. All five shifts of 0.10 or more were word-class calls: 0.70 to 0.41 and to 0.50; 0.82 to 0.65 and to 0.72; 0.75 to 0.91. Two of them fell below the support gate. The mechanic already treats word class as a judgment call that never holds a block.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/be97f27fc4c4a65a.json",
     "lines": "48-49, 416-417, 790-791",
     "quote": "\"word_0_class\": \"verb phrase\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/be97f27fc4c4a65a.json",
     "lines": "203, 571, 945",
     "quote": "\"value\": 0.41,"
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "112",
     "quote": "// a word class is a judgment call on Shakespeare, so it never holds the block, but one Jev did not confirm is not shown"
    }
   ],
   "against": "The rest of the batch changed between drafts, and checks whose wording does not name every input they read (the quick-check set and the give-away check) were left out of the comparison.",
   "scope_note": "universal for judges asked once per item",
   "adds_to_existing": [
    51,
    16
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check wrong-option feedback for the answer said in other words, not only for the right option's own words, because a word-match check misses a paraphrase.",
   "kind": "measured",
   "found_by": "In one remade film check, two feedback lines on wrong options said the keyed answer in other words: 'Othello is the general' and 'Othello served as Venice's trusted general', for the key 'A trusted North African or Black African general'. They passed the code check, which only fires on a run of the right option's own words as long as the option. The judge was asked only whether they were true (0.72, 0.95). A later draft that repeated the option's own words was caught.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "116",
     "quote": "const naming = checks.flatMap((c, k) => c.feedback.map((f, i) => ({ k, i, f })).filter(({ i, f }) => i !== c.answer && sharedRun(f, c.options[c.answer]) >= Math.max(3, words(c.options[c.answer]).length)));"
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
     "lines": "1249, 1251, 1263, 1641",
     "quote": "\"feedback_1_A\": \"Brabantio is identified as the senator, whereas Othello is the general.\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
     "lines": "1264, 1658",
     "quote": "\"feedback_1_B\": \"The Turks of the Ottoman Empire were the enemy, whilst Othello served as Venice's trusted general.\","
    }
   ],
   "against": "These lines never reached a student, because the block failed on its film.",
   "scope_note": "universal for choice items with feedback on each option",
   "adds_to_existing": [
    14
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Tell a retry why the last draft failed, or change its prompt, because a blind retry tends to write the same draft again.",
   "kind": "measured",
   "found_by": "A block's second try starts a fresh draft with no reasons from the first. In one open check, the fresh try wrote the failed question and its requirement again word for word and failed the same check (0.62). Two separate makings of a quick check began with the same question and the same unsure key check (0.54, 0.50). Two makings of an evidence hunt keyed the same two lines and got the same rejection (0.35).",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/a775ad50ec1c4070.json",
     "lines": "21, 304, 394",
     "quote": "\"q\": \"According to Iago, what is his only reason for continuing to serve Othello?\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/a775ad50ec1c4070.json",
     "lines": "26, 309",
     "quote": "\"requirement_0\": \"The student must state that Iago serves Othello to exploit him or use him for his own personal advantage.\","
    },
    {
     "path": "~/Projects/g9/transformer/src/blocks.js",
     "lines": "80",
     "quote": "const lesson = await transform({ text, question, track: [mechanic] }, { judge, writer, samples, log: mine, focus, avoid });"
    }
   ],
   "against": "Other fresh tries differed widely: the film check's three questions all changed between entries 1 and 2 of 0419fc2dc6f6bacf.json. So repetition is a tendency, not a rule.",
   "scope_note": "universal for generate-and-retry loops",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Calibrate a judged check at the number of samples it runs with, because votes that agree in calibration say nothing about a single draw in use.",
   "kind": "measured",
   "found_by": "The saved calibrations ran five samples per case, with agreement 1 on each case. All 33 build-time judgings in the remade blocks ran one sample. So agreement was never measured in use (null on all 366 answers), and the option-order rotation, which starts at the second sample, never ran.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/calibration/2026-10-09T12-25-25-449Z.json",
     "lines": "8",
     "quote": "\"samples\": 5,"
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
     "lines": "10, 617",
     "quote": "\"samples\": 1,"
    },
    {
     "path": "~/Projects/grade3-reading/engine/src/decide/questions.js",
     "lines": "118-120",
     "quote": "/** Deterministic option-order rotation per sample (option order shifts answers; rotate and average). */"
    }
   ],
   "against": "The calibrated cases sat far from the gates (0.92 and 0.08), where one draw may agree with five; the logged gate failures (0.50 to 0.59) were never in calibration.",
   "scope_note": "universal for sampled model judges",
   "adds_to_existing": [
    35,
    51,
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Put the hardest wrong answer in a check's labelled cases: a set of easy wrong keys can score perfectly while the check still confirms the confusable one in use.",
   "kind": "measured",
   "found_by": "The key-is-right check was calibrated on six seed cases, with precision and recall of 1 and scores of 0.92 or 0.08. Its wrong keys for the poem were the two obviously wrong figures; the narrator, the answer most easily confused with the right one, was not among them. In use, the same check confirmed the narrator as the key at 0.90 for a near-identical question. Its own labelled case reads the traveller as the one who tells what follows.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/calibration/2026-10-09T12-25-25-449Z.json",
     "lines": "453, 459",
     "quote": "\"why\": \"The speaker met a traveller, who said what follows.\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/calibration/2026-10-09T12-25-25-449Z.json",
     "lines": "92, 105, 114",
     "quote": "\"status\": \"calibrated\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/856ace1aed960671.json",
     "lines": "230, 296",
     "quote": "\"B\": \"The narrator who is repeating what a traveler told him\","
    }
   ],
   "against": "The project marks these sets as seeds and says so: \"Labels need a person: a model-made label measures nothing, and a seed set this small is diagnostic only.\" (calibrate.js line 6)",
   "scope_note": "universal for calibrating judged checks",
   "adds_to_existing": [
    35,
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Does a gap sentence that reuses its line's own words test the word, or only the finding of the line?",
   "kind": "open question",
   "found_by": "In the remade key-word deck, the shipped gap sentences rebuilt their lines' own wording around the blank. The judge's score for whether each gap points to its word rose to 0.98 and 0.99. Nothing checks whether a reader could fill the gap by finding the line rather than knowing the word.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/1ed330c52090f0fc.json",
     "lines": "454, 581",
     "quote": "\"gap_0\": \"A shattered ______ lies half sunk in the desert sand near the stone legs.\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/1ed330c52090f0fc.json",
     "lines": "459",
     "quote": "\"gap_1\": \"The sculptor read the ruler's ______ well and stamped them onto stone.\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/1ed330c52090f0fc.json",
     "lines": "20",
     "quote": "Half sunk a shattered visage lies, whose frown, / And wrinkled lip, and sneer of cold command, / Tell that its sculptor well those passions read"
    }
   ],
   "against": "Restating the line also made the sentences truer to the text: one rose from 0.81 to \"value\": 0.97 (1ed330c52090f0fc.json lines 241, 666). A meaning cue may still require knowing the word.",
   "scope_note": "vocabulary recall items set in sentences about the text",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Does a slur elsewhere in the passage lower a judge's confidence that a clean line is clean?",
   "kind": "open question",
   "found_by": "Asked whether a clean quotation was free of slurs, the judge answered 0.75 and 0.80 when the state also carried a passage with a slur in it (b9cb3d0f3a8639c0.json line 20). For quotations from texts without one, it answered 0.98 to 0.99. The question names only the quotation.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/b9cb3d0f3a8639c0.json",
     "lines": "20, 22, 360, 728",
     "quote": "\"quote\": \"I follow him to serve my turn upon him\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/68d85cc9b79fb956.json",
     "lines": "360, 728",
     "quote": "\"value\": 0.98,"
    }
   ],
   "against": "There are only two judgings of one quotation, and the quotation's own wording may read as hostile.",
   "scope_note": "slur and safety checks on lines from texts that contain slurs",
   "adds_to_existing": [
    18,
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep a claim to what its evidence shows: the same line proved an over-reaching claim less well than the claim narrowed to the line's own sense.",
   "kind": "measured",
   "found_by": "In the remade poem evidence hunt, the keyed line proved a claim of cruel dictatorship at 0.73. The correction narrowed the claim to disdainful, harsh authority, and the same line then proved it at 0.89.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/963297774d627c12.json",
     "lines": "20, 77",
     "quote": "\"claim\": \"The facial expression on the ruined statue shows that the monarch was a cruel and arrogant dictator.\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/963297774d627c12.json",
     "lines": "160, 200",
     "quote": "\"claim\": \"The expression on the ruined statue shows that the ruler possessed a disdainful and harsh authority.\","
    }
   ],
   "against": "This is one case. In the two other hunts, small rewordings moved the keyed line only from 0.75 or 0.76 to 0.78 (38cf6a0077428ec2.json lines 107, 339).",
   "scope_note": "evidence-finding tasks with a stated claim",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Name each judged part by what it is, not by its position, so its judgments can be compared across drafts.",
   "kind": "measured",
   "found_by": "In the remade glossary, the redraft inserted one term, so four unchanged glosses moved to new ids and two ids came to name different words. For example, the same gloss of one term was id 4 in one draft and id 5 in the next. Comparing judgments by id across the drafts compares different words.",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/366b8d2c7104a608.json",
     "lines": "32",
     "quote": "\"term_4\": \"ancient\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/366b8d2c7104a608.json",
     "lines": "529",
     "quote": "\"term_4\": \"toged consuls\","
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/366b8d2c7104a608.json",
     "lines": "532",
     "quote": "\"term_5\": \"ancient\","
    }
   ],
   "against": "Within one draft the ids are unambiguous, and the whole state is logged, so content can be matched again by hand.",
   "scope_note": "universal for judge logs and replay",
   "adds_to_existing": [
    21
   ],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
   "lines": "60, 187, 794, 1401",
   "quote": "\"instructions\": \"Is film_narration about the same work as passage, so that it can open a lesson on it?\""
  },
  {
   "truth": 3,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/runs/blocks/856ace1aed960671.json",
   "lines": "8, 14",
   "quote": "\"stem\": \"Who is the person actually speaking the words that describe the ruined statue and the surrounding desert?\","
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/856ace1aed960671.json",
   "lines": "230, 233, 296",
   "quote": "\"keyed_answer\": \"B\","
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/c98cc9de312f4d43.json",
   "lines": "229, 233, 297",
   "quote": "\"keyed_answer\": \"A\","
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/engine/src/decide/questions.js",
   "lines": "118",
   "quote": "/** Deterministic option-order rotation per sample (option order shifts answers; rotate and average). */"
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/38cf6a0077428ec2.json",
   "lines": "30, 226",
   "quote": "\"L3\": \"L3 [IAGO] I follow him to serve my turn upon him.\","
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/856ace1aed960671.json",
   "lines": "52, 259",
   "quote": "\"instructions\": \"Using only evidence_lines, is the option named by keyed_answer a correct answer to the question?\""
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
   "lines": "1264, 1658",
   "quote": "\"feedback_1_B\": \"The Turks of the Ottoman Empire were the enemy, whilst Othello served as Venice's trusted general.\","
  },
  {
   "truth": 16,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
   "lines": "112",
   "quote": "// a word class is a judgment call on Shakespeare, so it never holds the block, but one Jev did not confirm is not shown"
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/b9cb3d0f3a8639c0.json",
   "lines": "22, 360, 728",
   "quote": "\"quote\": \"I follow him to serve my turn upon him\","
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/blocks.js",
   "lines": "93",
   "quote": "// every try's decide records, as decide made them, so the block can be re-judged through a second judge"
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/b5f74899349e1331.json",
   "lines": "21, 111",
   "quote": "\"q\": \"What difference does the speaker draw between the endurance of the ceremony and the impact of the fighting?\","
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/68d85cc9b79fb956.json",
   "lines": "55, 288",
   "quote": "\"sentence_0_2\": \"The noun wrinkled lip implies that the king held his subjects in utter contempt and felt entirely superior to them.\","
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/38cf6a0077428ec2.json",
   "lines": "38",
   "quote": "\"instructions\": \"Does line L9 in lines, read on its own, give clear evidence for the claim?\""
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/engine/src/decide/questions.js",
   "lines": "105",
   "quote": "/** Support gates (conservative engineering thresholds, not calibrated correctness). */"
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/blocks/a775ad50ec1c4070.json",
   "lines": "37",
   "quote": "\"The question does not give its answer away: the judge found this does not hold\""
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/blocks.js",
   "lines": "17",
   "quote": "// Bumped when what a maker produces changes (prompts, checks), so an old block is made again, not served."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
   "lines": "83",
   "quote": "view(item) { return { kind: \"choice\", stem: item.stem, options: item.options }; },"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/transform.js",
   "lines": "78",
   "quote": "// an unsure judge is not a no: the correction asks for a version that plainly holds, not for its opposite"
  },
  {
   "truth": 50,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/runs/decisions/366b8d2c7104a608.json",
   "lines": "47-49, 310",
   "quote": "\"note_9\": \"own or possess\""
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/be97f27fc4c4a65a.json",
   "lines": "203, 571, 945",
   "quote": "\"value\": 0.41,"
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
   "lines": "10",
   "quote": "\"samples\": 1,"
  },
  {
   "truth": 54,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
   "lines": "49",
   "quote": "about it (a rank, an older sense, a word for what a character does or is), to study and then recall from memory."
  }
 ]
}
```
