# verify:gap:draft-vs-remake-judge-logs

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  nono, analyse its ideas and fold them into the research results

## Result

```json
{
 "direction": "draft-vs-remake-judge-logs",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "All three quotes are verbatim at the first cited line. The second cited line is the judge's value (0.24, 0.53 unsure, 0.51 unsure). In be97f27fc4c4a65a the 'long remember' swap for 'little note' stayed through three judged drafts (0.24, 0.48 unsure, 0.31), and the block failed on it (blocks file line 120). The original wording overstated the pattern. In every model, both wrong options on the word blank were words from the quotation, and one of each pair was confirmed wrong. The one not confirmed was the swap that carries the same reading: 'long remember', 'wrinkled lip', and 'upon him' (from the same phrase as 'serve my turn'). Narrowed to that. Not on record; it adds a construction rule beside 31.",
   "statement": "Don't build a wrong option by swapping in another word from the same quotation that carries the same reading: in each of three remade worked models, the one wrong option the judge would not confirm was such a swap, and one block failed on it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/be97f27fc4c4a65a.json",
     "lines": "54, 271",
     "quote": "\"sentence_0_1\": \"The phrase long remember presents spoken rhetoric as something fragile that will quickly fade from human memory.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/68d85cc9b79fb956.json",
     "lines": "55, 288",
     "quote": "\"sentence_0_2\": \"The noun wrinkled lip implies that the king held his subjects in utter contempt and felt entirely superior to them.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/b9cb3d0f3a8639c0.json",
     "lines": "55, 288",
     "quote": "\"sentence_0_2\": \"The phrase \\\"upon him\\\" reveals his purely opportunistic nature.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/be97f27fc4c4a65a.json",
     "lines": "120",
     "quote": "makes the rebuilt sentence wrong: the judge found this does not hold",
     "verbatim": true
    }
   ],
   "against": "In each model, the other wrong option on the same blank was also a word from the quotation, and it was confirmed wrong. 'frown' scored 0.78 (68d85cc9b79fb956.json lines 54, 271), 'never forget' 0.96 (be97f27fc4c4a65a.json lines 55, 288) and 'follow him' 0.85 (b9cb3d0f3a8639c0.json lines 54, 271). One correction kept 'upon him' but called it a verb phrase, and that option then passed at 0.97 (b9cb3d0f3a8639c0.json lines 426, 643). So the risk is a swap that says the same thing, not every swap.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep-with-fix",
   "reason": "Verified that each of the 13 judged corrections began from exactly one failing required check. The prompt asks for the whole JSON again (transform.js line 20). The worked-model corrections changed 11, 10 and 10 of 17 state fields. Two of those fields (passage, lesson_question) cannot be changed by the drafting model, so this is 10 or 11 of 15 drafted fields. The comparison rewrite changed both paragraphs, and 8 of 13 corrections cleared their check. 'Came back as it was' held only once: the open-check question came back word for word (a775ad50ec1c4070.json lines 21, 164; 0.56 unsure, then 0.70). The worked-model option came back reworded around the same swapped words (be97f27fc4c4a65a.json line 423 at 0.48, then line 796 at 0.31). A correction is already told the failing check's label, so the statement now asks for that part to be changed and the change to be checked in code.",
   "statement": "When a correction is told which check failed, ask it to change that part and keep the rest, and check in code that the part changed before judging again: asked for the whole reply again, rewrites changed 10 or 11 of 15 drafted fields in the worked models, and twice the failing part came back, once word for word.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/transform.js",
     "lines": "20",
     "quote": "YOUR PREVIOUS DRAFT FAILED THESE CHECKS. Fix every one and return the whole JSON again:",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/a775ad50ec1c4070.json",
     "lines": "21, 111, 164, 254",
     "quote": "\"q\": \"According to Iago, what is his only reason for continuing to serve Othello?\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/be97f27fc4c4a65a.json",
     "lines": "423, 658",
     "quote": "\"sentence_0_2\": \"The phrase \\\"long remember\\\" implies that official speeches leave almost no mark on history.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/be97f27fc4c4a65a.json",
     "lines": "796, 1017",
     "quote": "\"sentence_0_1\": \"The phrase long remember suggests that spoken dedications carry minimal lasting weight in human history.\",",
     "verbatim": true
    }
   ],
   "against": "8 of the 13 judged corrections cleared their failing check, and none brought in a new failing required check. The narrowest correction changed only the claim and cleared: \"claim\": \"The expression on the ruined statue shows that the ruler possessed a disdainful and harsh authority.\" (963297774d627c12.json line 160). Of the five that did not clear, three were on the give-away check, which has no labelled cases, and one was on a film that no rewrite could fix.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified. The fit instruction is at lines 60, 667 and 1274, and its 0.02 values at 187, 794 and 1401, so the quote's line numbers are corrected. pickFilm keeps the best overlap with no minimum (films.js line 62), and the block failed. Two details of the finding were overstated. In the third judging, one feedback line was unsure (feedback_0_C_true 0.59, line 1537), so not every question-level check passed. The correction also kept the third question, so only the fresh try rewrote all three. No 'universality test' label appears in the repo: this is the 12 October run that gave a poem lesson the play's film.",
   "statement": "Before writing questions on a film or other media, check that it is about the lesson's text and stop if it is not: a best-match picker always returns something, and rewriting the questions cannot fix a mismatch.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/films.js",
     "lines": "55",
     "quote": "/** The film whose narration shares most words with the text and the question; null if there is none. */",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/films.js",
     "lines": "62",
     "quote": "if (!best || shared > best.shared) best = { film: f, shared };",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
     "lines": "60, 667, 1274",
     "quote": "\"instructions\": \"Is film_narration about the same work as passage, so that it can open a lesson on it?\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
     "lines": "187, 794, 1401",
     "quote": "\"value\": 0.02,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
     "lines": "23",
     "quote": "\"question_0\": \"When was the play written?\",",
     "verbatim": true
    }
   ],
   "against": "Nothing found against the claim: the fit question caught the mismatch at 0.02 in all three judgings. The picker returns null only when no film is listed at all. With one film on the machine, it always returns that film.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep",
   "reason": "Verified. The block keeps one reason, from a final draft that failed a code check and was never judged ('judge' is empty at line 161; tries 2 and judgeCalls 1 at lines 162-163). All three judgings in its log scored the film's fit at 0.02. This is distinct from 21, which keeps the judgments themselves: the log has them, but the block's own record points at a side fault.",
   "statement": "When an item fails, keep the reasons from every attempt, because the last attempt's reason can name a side fault and hide the cause.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/blocks/0419fc2dc6f6bacf.json",
     "lines": "97",
     "quote": "\"Wrong-option feedback does not name the answer: question 2, option A: its feedback names the right answer; question 2, option C: its feedback names the right answer\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/0419fc2dc6f6bacf.json",
     "lines": "162-163",
     "quote": "\"judgeCalls\": 1,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
     "lines": "187, 794, 1401",
     "quote": "\"value\": 0.02,",
     "verbatim": true
    }
   ],
   "against": "The full log of every attempt is kept beside the block (\"// every try's decide records, as decide made them, so the block can be re-judged through a second judge\", blocks.js line 93), so the cause can be recovered by reading it.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified. L9 is at line 22, with 0.35 at line 90, in both Othello logs. L4 is at line 22, with 0.16 at line 60. The reveal is at line 13 of the block, whose accepted list is [4] (lines 14-16). The first drafts keyed L4 with L5 and L9 with L10, the two halves of one sentence, and each correction keyed only the other half. 'A reader who picks that half is not credited' was an inference. The rejected half is left out of the accepted lines, but a tap on it goes back to the judge at play time, and only a sure no marks a miss; no play logs were read. Narrowed to what was seen.",
   "statement": "When the evidence is a sentence that runs across lines, credit the whole sentence: judged one line at a time, one half of a two-line proof was rejected in all three remade evidence hunts and left out of the accepted lines.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/38cf6a0077428ec2.json",
     "lines": "22, 90",
     "quote": "\"L9\": \"L9 [IAGO] Heaven is my judge, not I for love and duty,\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/815626dc60c1b455.json",
     "lines": "22, 90",
     "quote": "\"L9\": \"L9 [IAGO] Heaven is my judge, not I for love and duty,\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/963297774d627c12.json",
     "lines": "22, 60",
     "quote": "\"L4\": \"L4 Half sunk a shattered visage lies, whose frown,\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/963297774d627c12.json",
     "lines": "13",
     "quote": "\"reveal\": \"The ruined face shows a frowning mouth with a cold expression, showing the ruler's harsh authority.\",",
     "verbatim": true
    }
   ],
   "against": "The rejected halves may be weaker evidence on their own: their corrections scored them 0.58 unsure, 0.33 and 0.24. At play time, a tap on a line outside the accepted set goes back to the judge, so it counts as a miss only on a sure no (evidence-hunt.js lines 71-84). The same one-line questions let an unkeyed line be accepted elsewhere (38cf6a0077428ec2.json line 30, 0.89 at line 226).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep-with-fix",
   "reason": "Verified across two makings and their corrections, which are four close wordings of the claim rather than one claim. The unkeyed L3 scored 0.89, 0.84, 0.89 and 0.87, and the keyed L10 scored 0.75, 0.78, 0.76 and 0.78. The first drafts also keyed L9, at 0.35. Both blocks accept L3. 'Prove the point better' read single-sample confidence as strength of proof, so the statement now says 'confirmed more surely'. This is 7 with new evidence; keep it only as evidence for 7.",
   "statement": "Don't treat the drafted key as the only right answer: ask about every candidate line, because a line nobody keyed can be confirmed more surely than the key.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/38cf6a0077428ec2.json",
     "lines": "30, 107, 226",
     "quote": "\"L3\": \"L3 [IAGO] I follow him to serve my turn upon him.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/815626dc60c1b455.json",
     "lines": "339, 475",
     "quote": "\"value\": 0.87,",
     "verbatim": true
    }
   ],
   "against": "One further accepted line sat exactly at the gate's floor on a single sample (\"p\": 0.6, 815626dc60c1b455 block line 82). The engine calls its gates \"conservative engineering thresholds, not calibrated correctness\" (questions.js line 105).",
   "general": true,
   "duplicate_of": "7",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep-with-fix",
   "reason": "Verified. Both makings began with the same question and an unsure key check (0.54 and 0.50 at line 89). One correction keyed the narrator (0.90, line 296), with the traveller judged wrong at 0.69 (line 313). The other keyed the traveller (0.73, line 297). Both shipped ready (answer 1 and answer 0 at line 14 of the two blocks). The two final questions are worded differently, so 'one ambiguous question' became 'two near-identical wordings'. This is 11 applied to keyed choices, with new evidence. It also shows the option-by-option checks of 31 passing while the text left the answer open.",
   "statement": "Ask the judge for the answer without showing it the key, then compare: asked only to confirm a key, it confirmed opposite answers to two near-identical wordings of one ambiguous question.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/856ace1aed960671.json",
     "lines": "230, 233, 296",
     "quote": "\"B\": \"The narrator who is repeating what a traveler told him\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/c98cc9de312f4d43.json",
     "lines": "229, 233, 297",
     "quote": "\"A\": \"The traveler who visited the antique land\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/856ace1aed960671.json",
     "lines": "52, 259",
     "quote": "\"instructions\": \"Using only evidence_lines, is the option named by keyed_answer a correct answer to the question?\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/856ace1aed960671.json",
     "lines": "14",
     "quote": "\"answer\": 1,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/c98cc9de312f4d43.json",
     "lines": "14",
     "quote": "\"answer\": 0,",
     "verbatim": true
    }
   ],
   "against": "The first drafts' unsure answers did flag the ambiguity (\"value\": 0.54, 856ace1aed960671.json line 89; \"value\": 0.5, c98cc9de312f4d43.json line 89). A framed narrative may defensibly allow both readings. The fault is that rewording made the judge sure without making the text settle the answer.",
   "general": true,
   "duplicate_of": "11",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep-with-fix",
   "reason": "Verified the tempting values: 0.39, 0.38, 0.66 and 0.46 (856ace1aed960671), and 0.37, 0.35, 0.36 and 0.48 (c98cc9de312f4d43). That is five no, two unsure and one yes. The check is required: false (quick-check.js line 74), and the film-check and worked-model judges ask nothing about plausibility. The original 'Hold a choice question whose wrong options would tempt no one' asked an uncalibrated judgment to block items, which 35 rules out. 'Would tempt no one' is also a model's opinion, not a count of what students pick. Reworded to a check that does not yet hold anything back.",
   "statement": "Check that every wrong option would tempt a skimming reader, because an option nobody picks tests nothing: in two remade quick checks the judge found 7 of 8 wrong options untempting or was unsure, and both questions shipped because that check is optional.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "74",
     "quote": "id: `tempting-${letters[i]}`, label: `Option ${letters[i]} would tempt a reader who skimmed`, required: false,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/c98cc9de312f4d43.json",
     "lines": "144, 161, 348, 365",
     "quote": "\"value\": 0.36,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/856ace1aed960671.json",
     "lines": "144, 161, 364",
     "quote": "\"value\": 0.39,",
     "verbatim": true
    }
   ],
   "against": "The prompt already asks for tempting options (\"- Exactly three options. Exactly one is right given the text; the other two are tempting to a skimmer but the text\", quick-check.js line 23). The plausibility judgment has no labelled cases, so it cannot yet hold a question back (35). A model's view of what tempts a skimmer is not a count of what students pick.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep-with-fix",
   "reason": "Verified. 'owe' glossed as 'own or possess' scored 0.59 (line 310), and 'known unaided' scored 0.44 (line 482). 'mocked' glossed as 'copied or represented something in an artistic work' scored 0.59 (line 275). These were the only unsure glosses in either block. Both blocks show tries 2 and judgeCalls 1, so the shipped drafts were fresh tries, and neither shipped item holds the word. Both prompts ask for older senses (key-words.js line 49, glossary.js line 85). 'Because those are the words a reader most needs explained' is not measured here and was cut. Refines 50 and 54; not a duplicate.",
   "statement": "When a judge is unsure of a gloss on a familiar word used in an older sense, have a person check it rather than let a redraft drop it: in two remade blocks the only unsure glosses were such words, and neither reached the shipped version.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/366b8d2c7104a608.json",
     "lines": "47-49, 310, 482",
     "quote": "\"note_9\": \"own or possess\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/1ed330c52090f0fc.json",
     "lines": "37-38, 275",
     "quote": "\"meaning_2\": \"copied or represented something in an artistic work\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
     "lines": "49",
     "quote": "about it (a rank, an older sense, a word for what a character does or is), to study and then recall from memory.",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/glossary.js",
     "lines": "85",
     "quote": "title, an older sense of a word, an idiom), four to ten of them, in the order they come.",
     "verbatim": true
    }
   ],
   "against": "Both later drafts were fresh tries, not corrections, so the words may have gone by chance. The line glossed for 'owe' also carries an epithet, which may itself have unsettled the judge. The gloss of 'mocked' gives only one of its two senses.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "reason": "Verified. The give-away check held all seven judged drafts: one unsure at 0.56 and six refuted (0.70, 0.62, 0.68; 0.69, 0.71, 0.65). Both blocks failed on it (block lines 37 and 39). The seven ran under two wordings of the check (line 48 of each log). test/calibration holds sets for five other checks and none for this one. All four saved calibration runs used a stand-in judge whose note reads 'proves the wiring, measures nothing', so no check here has been scored with the real judge. This is the mirror of 1 and a case of 35; not a duplicate.",
   "statement": "A check that fails every draft proves nothing until it passes an item known to be clean, so test a blocking check on good items as well as planted faults.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/a775ad50ec1c4070.json",
     "lines": "444, 534",
     "quote": "\"q\": \"According to Iago, what is his purpose in continuing to serve Othello?\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/a775ad50ec1c4070.json",
     "lines": "37",
     "quote": "\"The question does not give its answer away: the judge found this does not hold\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/b5f74899349e1331.json",
     "lines": "39",
     "quote": "\"The question does not give its answer away: the judge found this does not hold\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/calibration/2026-10-09T12-25-25-449Z.json",
     "lines": "6",
     "quote": "\"note\": \"answers from the labels themselves: proves the wiring, measures nothing\"",
     "verbatim": true
    }
   ],
   "against": "The three drafts on the speech did name both sides of the contrast they asked about (b5f74899349e1331.json line 21), so some of the seven may be real give-aways. The seven also fell under two different wordings of the check.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep",
   "reason": "Verified. The 9 October log uses the old wording (a775ad50ec1c4070.json line 48), the 12 October log uses the new one (b5f74899349e1331.json line 48), and open-check.js line 86 gives the reason. The mechanic is at version 3, but the repo holds a single commit for the file, so the version rise cannot be dated to this change. Not on record.",
   "statement": "Judge whether a question gives its answer away from its own words only, not from what anyone who knows a famous work would know.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/open-check.js",
     "lines": "86",
     "quote": "// its own words only: a famous text's answer is known to anyone who knows the work, which is no give-away of the question's",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/a775ad50ec1c4070.json",
     "lines": "48",
     "quote": "\"instructions\": \"Does the wording of q by itself give away what a good answer must say?\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/b5f74899349e1331.json",
     "lines": "48",
     "quote": "\"instructions\": \"Do the words of q themselves state, or nearly state, what a good answer must say? Judge only the wording of q, not what a reader may already know about the work.\"",
     "verbatim": true
    }
   ],
   "against": "After the change, all three drafts of a question on a famous speech still failed the check (\"value\": 0.65 at b5f74899349e1331.json line 437; 0.69 and 0.71 at lines 111 and 280).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep",
   "reason": "Verified. All three drafts (lines 21, 161, 347) named both sides of the contrast, and all three used a word for lasting (endurance or durability), not just two. The give-away scores were 0.69, 0.71 and 0.65 (lines 111, 280, 437), and the block failed. A fair open question; not on record.",
   "statement": "How to ask an open question about a contrast the text states outright without giving it away: every draft that named the two things contrasted was judged a give-away.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/b5f74899349e1331.json",
     "lines": "21, 111",
     "quote": "\"q\": \"What difference does the speaker draw between the endurance of the ceremony and the impact of the fighting?\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/b5f74899349e1331.json",
     "lines": "161, 280",
     "quote": "\"q\": \"How does the speaker contrast the durability of what the soldiers did with the durability of the speech?\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/b5f74899349e1331.json",
     "lines": "347, 437",
     "quote": "\"q\": \"What difference does the speaker draw between the endurance of spoken words and the actions of the soldiers?\",",
     "verbatim": true
    }
   ],
   "against": "The give-away check has no labelled cases, so it is not settled that these questions do give the answer away.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep-with-fix",
   "reason": "Verified the median of 0.01 and the five shifts of 0.10 or more. All five were word-class calls: in be97f27fc4c4a65a, 0.70 to 0.41 and to 0.50, and 0.82 to 0.65 and to 0.72; in b9cb3d0f3a8639c0, 0.75 to 0.91. Two of them fell below the gates. The pair count of 39 did not reproduce. Matching by question id gives 31 pairs once the quick-check and give-away checks are left out, and 38 if the glossary's shifted ids are matched by content; the median and the five large shifts hold either way. 'Unchanged' meant only the call's own inputs, since the rest of each batch changed. This refines 51 by showing where the wavering falls; not a duplicate.",
   "statement": "Expect a judge to waver most where the question is arguable: across drafts, judgments whose own inputs had not changed moved a median of 0.01, while one word-class call moved from 0.70 to 0.41.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/be97f27fc4c4a65a.json",
     "lines": "49, 417, 791",
     "quote": "\"word_0_class\": \"verb phrase\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/be97f27fc4c4a65a.json",
     "lines": "203, 571, 945",
     "quote": "\"value\": 0.41,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/b9cb3d0f3a8639c0.json",
     "lines": "203, 575",
     "quote": "\"value\": 0.91,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
     "lines": "112",
     "quote": "// a word class is a judgment call on Shakespeare, so it never holds the block, but one Jev did not confirm is not shown",
     "verbatim": true
    }
   ],
   "against": "The rest of each batch changed between drafts. Checks whose wording does not name every input they read (the quick-check set and the give-away check) were left out, and those moved too: give-away from 0.56 to 0.70, and one tempting call from 0.35 to 0.48.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "keep-with-fix",
   "reason": "Verified: key C at line 1249, the two feedback lines at 1263 and 1264, and truth scores of 0.72 and 0.95 at 1641 and 1658. The code check fires only on a shared run as long as the right option (util.js line 116; quick-check.js lines 53-54 use the same rule). The reader's 'never reached a student' is countered by a ready block. Quick-check block 856ace1aed960671 tells a reader who picks the traveller that 'the narrator is the speaker of the poem itself' (line 16). It tells one who picks the king that the description 'is spoken by the narrator repeating the traveler' (line 18). Both give the right answer in other words, against the block's own prompt (quick-check.js line 27), yet its code check passed (lines 56-58), and the quick-check judge asks nothing about feedback. Ready block c98cc9de312f4d43 does the same at line 18. This adds a check to 14.",
   "statement": "Check wrong-option feedback for the answer said in other words, not only for the right option's own words, because a word-match check misses a paraphrase.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/src/mechanics/util.js",
     "lines": "116",
     "quote": "const naming = checks.flatMap((c, k) => c.feedback.map((f, i) => ({ k, i, f })).filter(({ i, f }) => i !== c.answer && sharedRun(f, c.options[c.answer]) >= Math.max(3, words(c.options[c.answer]).length)));",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
     "lines": "1249, 1251, 1263, 1641",
     "quote": "\"feedback_1_A\": \"Brabantio is identified as the senator, whereas Othello is the general.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
     "lines": "1264, 1658",
     "quote": "\"feedback_1_B\": \"The Turks of the Ottoman Empire were the enemy, whilst Othello served as Venice's trusted general.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/856ace1aed960671.json",
     "lines": "16",
     "quote": "The traveler is the one who spoke the description to the narrator, but the narrator is the speaker of the poem itself",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/856ace1aed960671.json",
     "lines": "18",
     "quote": "whereas the description of the ruins is spoken by the narrator repeating the traveler",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/blocks/856ace1aed960671.json",
     "lines": "56-58",
     "quote": "\"id\": \"feedback-no-answer\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
     "lines": "27-28",
     "quote": "Wrong option: one sentence that sends the reader back to specific words (quote a few of them) without naming the",
     "verbatim": true
    }
   ],
   "against": "Whether a line names the answer in other words is itself a judgment, so a paraphrase check would need labelled cases before it holds a block (35). The film-check lines never reached a student, because that block failed on its film.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep-with-fix",
   "reason": "Verified. blocks.js line 80 calls transform with no reasons, so every try starts clean. The fresh try in a775ad50ec1c4070 (entry 2) repeated the question and the first draft's requirement word for word (lines 304, 309) and failed at 0.62 (line 394). The quick-check and evidence-hunt pairs are separate makings, not retries, but they show the same prompt giving the same first draft. 'Tends to' overstated a mixed record: two of six judged fresh tries brought the failing part back. The statement now says 'can'.",
   "statement": "Tell a retry why the last draft failed, or change its prompt: a retry with the same prompt and no reasons can write the failed draft again.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/a775ad50ec1c4070.json",
     "lines": "21, 304, 394",
     "quote": "\"q\": \"According to Iago, what is his only reason for continuing to serve Othello?\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/a775ad50ec1c4070.json",
     "lines": "26, 309",
     "quote": "\"requirement_0\": \"The student must state that Iago serves Othello to exploit him or use him for his own personal advantage.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/blocks.js",
     "lines": "80",
     "quote": "const lesson = await transform({ text, question, track: [mechanic] }, { judge, writer, samples, log: mine, focus, avoid });",
     "verbatim": true
    }
   ],
   "against": "Of six judged fresh tries, four changed the failing part. The film check's three questions all changed between entries 1 and 2 of 0419fc2dc6f6bacf.json (counting from 0).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "drop",
   "reason": "The calibration evidence was misread. All four saved calibration runs used a stand-in judge that answers from the labels (line 6 of each run: 'proves the wiring, measures nothing'; calibrate.js lines 111-122 return 0.92 or 0.08). So agreement 1 and the 0.92/0.08 scores are by construction, and one run used three samples, not five. No judge was calibrated at any sample count, so there is no contrast with the one-sample build to learn from. Option rotation applies only to choice questions (questions.js line 120), and only compare-paragraphs 'stronger' was one. What is real here (one sample, and agreement null on all 366 answers in 33 judgings) already bears on 51.",
   "statement": "Calibrate a judged check at the number of samples it runs with, because votes that agree in calibration say nothing about a single draw in use.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/calibration/2026-10-09T12-25-25-449Z.json",
     "lines": "8",
     "quote": "\"samples\": 5,",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/calibration/2026-10-09T12-25-25-449Z.json",
     "lines": "6",
     "quote": "\"note\": \"answers from the labels themselves: proves the wiring, measures nothing\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/src/quality/calibrate.js",
     "lines": "111",
     "quote": "/** A stand-in judge that answers every case from its own label. It proves the wiring (states, checks, votes, measures",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
     "lines": "10, 617",
     "quote": "\"samples\": 1,",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/engine/src/decide/questions.js",
     "lines": "118-120",
     "quote": "/** Deterministic option-order rotation per sample (option order shifts answers; rotate and average). */",
     "verbatim": true
    }
   ],
   "against": "The build's single samples are real: agreement was null on all 366 answers in 33 judgings. That bears on 51 rather than on calibration.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "drop",
   "reason": "The 'precision and recall of 1' and the 0.92/0.08 scores come from the stand-in label judge, which 'measures nothing', so they say nothing about easy or hard cases. The set itself says it holds obvious seed cases only (quick-check.answerable.json line 5). Its labelled stem asks who tells the speaker about the statue, which the traveller settles. The narrator key in use answered a differently worded, ambiguous question, so it is not a shown miss. The principle may hold, but it needs a calibration with the real judge that includes the confusable key. As it stands it overlaps 35.",
   "statement": "Put the hardest wrong answer in a check's labelled cases: a set of easy wrong keys can score perfectly while the check still confirms the confusable one in use.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/calibration/2026-10-09T12-25-25-449Z.json",
     "lines": "459",
     "quote": "\"why\": \"The speaker met a traveller, who said what follows.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/calibration/2026-10-09T12-25-25-449Z.json",
     "lines": "114",
     "quote": "\"status\": \"calibrated\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/calibration/2026-10-09T12-25-25-449Z.json",
     "lines": "6",
     "quote": "\"note\": \"answers from the labels themselves: proves the wiring, measures nothing\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/test/calibration/quick-check.answerable.json",
     "lines": "5",
     "quote": "Seed cases only: obvious ones",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/856ace1aed960671.json",
     "lines": "230, 296",
     "quote": "\"B\": \"The narrator who is repeating what a traveler told him\",",
     "verbatim": true
    }
   ],
   "against": "The project marks these sets as seeds and says so: \"Labels need a person: a model-made label measures nothing, and a seed set this small is diagnostic only.\" (calibrate.js line 6)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 17,
   "verdict": "keep",
   "reason": "Verified. The shipped gaps rebuild their lines' own words: 'A shattered ______ lies half sunk' comes from 'Half sunk a shattered visage lies', and 'The sculptor read the ruler's ______ well' from 'its sculptor well those passions read'. No code or judged check in key-words.js compares a gap with its line. The 'rose to 0.98 and 0.99' was a rise of 0.01 from 0.98 and 0.97, within single-sample movement, so it is no signal either way. A fair open question; not on record.",
   "statement": "Does a gap sentence that reuses its line's own words test the word, or only the finding of the line?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/1ed330c52090f0fc.json",
     "lines": "454, 581",
     "quote": "\"gap_0\": \"A shattered ______ lies half sunk in the desert sand near the stone legs.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/1ed330c52090f0fc.json",
     "lines": "459",
     "quote": "\"gap_1\": \"The sculptor read the ruler's ______ well and stamped them onto stone.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/1ed330c52090f0fc.json",
     "lines": "20",
     "quote": "Half sunk a shattered visage lies, whose frown, / And wrinkled lip, and sneer of cold command, / Tell that its sculptor well those passions read",
     "verbatim": true
    }
   ],
   "against": "Restating the line also made the sentences truer to the text: one rose from 0.81 to \"value\": 0.97 (1ed330c52090f0fc.json lines 241, 666). A meaning cue may still require knowing the word.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep",
   "reason": "Verified. clean_line on the same Othello quotation scored 0.75 and 0.80 (lines 360, 728), with an epithet in that state's passage. On the Ozymandias and Gettysburg quotations it scored 0.98 to 0.99 (68d85cc9b79fb956.json line 360 is 0.98, line 728 is 0.99). These are two judgings of one quotation, confounded by text, so it stays an open question. A possible further case: the one unsure gloss in the Othello glossary was on a line with an epithet (366b8d2c7104a608.json lines 47-49).",
   "statement": "Does a slur elsewhere in the passage lower a judge's confidence that a clean line is clean?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/b9cb3d0f3a8639c0.json",
     "lines": "20, 22, 360, 728",
     "quote": "\"quote\": \"I follow him to serve my turn upon him\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/68d85cc9b79fb956.json",
     "lines": "360",
     "quote": "\"value\": 0.98,",
     "verbatim": true
    }
   ],
   "against": "There are only two judgings of one quotation, and the quotation's own wording may read as hostile.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "drop",
   "reason": "Verified the rise from 0.73 to 0.89 (lines 77, 200), but it is one case on single samples. In these same logs, mid-range single-sample calls moved by up to 0.29 with their inputs unchanged, so the rise cannot be put down to the narrower claim. The other two hunts moved only from 0.75 and 0.76 to 0.78. It also reads judge confidence as strength of proof. Too thin for a measured learning.",
   "statement": "Keep a claim to what its evidence shows: the same line proved an over-reaching claim less well than the claim narrowed to the line's own sense.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/963297774d627c12.json",
     "lines": "20, 77",
     "quote": "\"claim\": \"The facial expression on the ruined statue shows that the monarch was a cruel and arrogant dictator.\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/963297774d627c12.json",
     "lines": "160, 200",
     "quote": "\"claim\": \"The expression on the ruined statue shows that the ruler possessed a disdainful and harsh authority.\",",
     "verbatim": true
    }
   ],
   "against": "This is one case. In the two other hunts, small rewordings moved the keyed line only from 0.75 or 0.76 to 0.78 (38cf6a0077428ec2.json lines 107, 339).",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified: term_4 'ancient' at line 32, 'toged consuls' at 529 and term_5 'ancient' at 532, with the same note at 34 and 534. The counts need correcting. The fresh try inserted one term at id 4, so every id from 4 to 9 named a different term in the two drafts, not two. Three glosses identical in term, line and note moved to new ids (ancient, old gradation, cashier'd), and a fourth term (affined) moved with a shortened note. This bears on 21 (replay) but is a separate point.",
   "statement": "Name each judged part by what it is, not by its position, so its judgments can be compared across drafts.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/g9/transformer/runs/decisions/366b8d2c7104a608.json",
     "lines": "32",
     "quote": "\"term_4\": \"ancient\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/366b8d2c7104a608.json",
     "lines": "529",
     "quote": "\"term_4\": \"toged consuls\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/366b8d2c7104a608.json",
     "lines": "532",
     "quote": "\"term_5\": \"ancient\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/366b8d2c7104a608.json",
     "lines": "34",
     "quote": "\"note_4\": \"a military rank equivalent to an ensign\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/g9/transformer/runs/decisions/366b8d2c7104a608.json",
     "lines": "534",
     "quote": "\"note_5\": \"a military rank equivalent to an ensign\",",
     "verbatim": true
    }
   ],
   "against": "Within one draft the ids are unambiguous, and the whole state is logged, so content can be matched again by hand.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
   "lines": "60, 187, 794, 1401",
   "quote": "\"instructions\": \"Is film_narration about the same work as passage, so that it can open a lesson on it?\"",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/runs/blocks/856ace1aed960671.json",
   "lines": "8, 14",
   "quote": "\"stem\": \"Who is the person actually speaking the words that describe the ruined statue and the surrounding desert?\",",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/856ace1aed960671.json",
   "lines": "230, 233, 296",
   "quote": "\"keyed_answer\": \"B\",",
   "ok": false
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/c98cc9de312f4d43.json",
   "lines": "229, 233, 297",
   "quote": "\"keyed_answer\": \"A\",",
   "ok": false
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/engine/src/decide/questions.js",
   "lines": "118",
   "quote": "/** Deterministic option-order rotation per sample (option order shifts answers; rotate and average). */",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/38cf6a0077428ec2.json",
   "lines": "30, 226",
   "quote": "\"L3\": \"L3 [IAGO] I follow him to serve my turn upon him.\",",
   "ok": true
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/856ace1aed960671.json",
   "lines": "52, 259",
   "quote": "\"instructions\": \"Using only evidence_lines, is the option named by keyed_answer a correct answer to the question?\"",
   "ok": true
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
   "lines": "1264, 1658",
   "quote": "\"feedback_1_B\": \"The Turks of the Ottoman Empire were the enemy, whilst Othello served as Venice's trusted general.\",",
   "ok": true
  },
  {
   "truth": 16,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/worked-model.js",
   "lines": "112",
   "quote": "// a word class is a judgment call on Shakespeare, so it never holds the block, but one Jev did not confirm is not shown",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/b9cb3d0f3a8639c0.json",
   "lines": "22, 360, 728",
   "quote": "\"quote\": \"I follow him to serve my turn upon him\",",
   "ok": false
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/blocks.js",
   "lines": "93",
   "quote": "// every try's decide records, as decide made them, so the block can be re-judged through a second judge",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/b5f74899349e1331.json",
   "lines": "21, 111",
   "quote": "\"q\": \"What difference does the speaker draw between the endurance of the ceremony and the impact of the fighting?\",",
   "ok": true
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/68d85cc9b79fb956.json",
   "lines": "55, 288",
   "quote": "\"sentence_0_2\": \"The noun wrinkled lip implies that the king held his subjects in utter contempt and felt entirely superior to them.\",",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/38cf6a0077428ec2.json",
   "lines": "38",
   "quote": "\"instructions\": \"Does line L9 in lines, read on its own, give clear evidence for the claim?\"",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/engine/src/decide/questions.js",
   "lines": "105",
   "quote": "/** Support gates (conservative engineering thresholds, not calibrated correctness). */",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/blocks/a775ad50ec1c4070.json",
   "lines": "37",
   "quote": "\"The question does not give its answer away: the judge found this does not hold\"",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/blocks.js",
   "lines": "17",
   "quote": "// Bumped when what a maker produces changes (prompts, checks), so an old block is made again, not served.",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/quick-check.js",
   "lines": "83",
   "quote": "view(item) { return { kind: \"choice\", stem: item.stem, options: item.options }; },",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/transform.js",
   "lines": "78",
   "quote": "// an unsure judge is not a no: the correction asks for a version that plainly holds, not for its opposite",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "counter",
   "path": "~/Projects/g9/transformer/runs/decisions/366b8d2c7104a608.json",
   "lines": "47-49, 310",
   "quote": "\"note_9\": \"own or possess\"",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/be97f27fc4c4a65a.json",
   "lines": "203, 571, 945",
   "quote": "\"value\": 0.41,",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/runs/decisions/0419fc2dc6f6bacf.json",
   "lines": "10",
   "quote": "\"samples\": 1,",
   "ok": false
  },
  {
   "truth": 54,
   "effect": "supports",
   "path": "~/Projects/g9/transformer/src/mechanics/key-words.js",
   "lines": "49",
   "quote": "about it (a rank, an older sense, a word for what a character does or is), to study and then recall from memory.",
   "ok": true
  }
 ]
}
```
