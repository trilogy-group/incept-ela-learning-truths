# verify:artifacts-qa

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "artifacts-qa",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "All three quotes verbatim at the cited lines. Supported, but it is one unit's gate with one dated solver, so the statement now gives the counts instead of 'every time'. Adds to truth 5.",
   "statement": "Some question formats are far easier to make depend on the text than others: in one unit's blind-solve gate all 24 items that put text-specific fragments in order passed, while 19 of 24 plain choice and hot-text items leaked.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
     "lines": "20",
     "quote": "| fragment-sequence | 24 | 24 | 0 | 0 | 100% |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
     "lines": "22",
     "quote": "| choice-hottext | 24 | 4 | 19 | 1 | 17% |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
     "lines": "28",
     "quote": "Plain choice/hot-text confirms its high-leak prior (13/16 MCQ leaked).",
     "verbatim": true
    }
   ],
   "against": "Ordering items about well-known processes leaked heavily elsewhere: \"| sequence | 185 | **58.4%** | 3.0% | **~19×** | adjacent-pair order 85.2% |\" (alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md:17), so the format helps only when the order is fixed by the text; the gate's solver is marked historical provenance (items/02-gate-summary.md:5-6).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep",
   "reason": "Quotes verbatim (the second sits on line 32, not 31-32). Supported by a 480-item cross-family blind solve; added the report's own fix-path line, which states the remedy. Adds to truth 5.",
   "statement": "Items whose answer follows a well-known real-world order or category can be answered without reading; tie the key to an order, entity or category that only this text defines.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md",
     "lines": "17",
     "quote": "| sequence | 185 | **58.4%** | 3.0% | **~19×** | adjacent-pair order 85.2% |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md",
     "lines": "32",
     "quote": "real-world things have canonical categories — recoverable with zero reading.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md",
     "lines": "44",
     "quote": "items must hinge on passage-unique facts a general model can't recover",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md",
     "lines": "45-46",
     "quote": "invented entities/quantities/relations, story-specific event order rather than canonical process order, passage-defined categories rather than natural-kind categories",
     "verbatim": true
    }
   ],
   "against": "The probe used one solver family with forced guessing and no with-text control (same file:50-56).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep",
   "reason": "Quotes verbatim (the second on line 65). Gate results in one unit plus an independent audit of another bank; the source scopes its lessons to 'this unit, this grade', but the principle is general. Adds to truth 5.",
   "statement": "When world knowledge points to an answer the text contradicts, make that default a wrong option; keys that match the world-knowledge guess can be found without reading.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md",
     "lines": "62",
     "quote": "key is the blind solver's plurality narrative guess dies (8/11 cause leaks, incl.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md",
     "lines": "65",
     "quote": "a world-favorite decoy out-competes the key",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/RESULTS.md",
     "lines": "32",
     "quote": "GK default (d) \"walls keep out water\" is the trap; text says cold WINDS → blind solver actively misled to {a,d}; {a,b} text-locked",
     "verbatim": true
    }
   ],
   "against": "When the text itself rules out the obvious causes, the distractors become easy once read: \"The quality screen flagged this on **14 of 26** items\" (alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md:96).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 289/794 (36%) against a chance rate under 25% for four options supports the tendency; added the binding copy rule, which also bans a uniquely shortest key. Adds to truths 5 and 67.",
   "statement": "Generated multiple-choice items tend to make the right answer the longest option, so keep options to similar length, never let the key be uniquely longest or shortest, and check by counting.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/LLM_GENERATION_BOUNDARY.md",
     "lines": "34",
     "quote": "At course scale the tell is endemic: 289/794 keyed MCQs have the correct option strictly longest (~36%).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md",
     "lines": "16",
     "quote": "| Correct answer is the longest option | 28% | n/a | Length cue alone recovers the key |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/L5-REVIEW-GAPS-2026-09-17.md",
     "lines": "8",
     "quote": "the first wording made the correct option the single longest (95 vs 91) — validator caught it",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/BUILD-SPEC-batch.md",
     "lines": "6",
     "quote": "an mcq key is never the longest/shortest",
     "verbatim": true
    }
   ],
   "against": "In multi-select items the cue can be confounded: \"A test-taking strategy of \"pick the two longest\" yields opt[1]+opt[2], which is one right and one wrong\" (peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md:102).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep",
   "reason": "Quotes verbatim. The shares are of leaked items in a forensic sample; elimination by absolute words is the analysis's stated mechanism and a standard test-wiseness cue. Adds to truth 5.",
   "statement": "Wrong options containing absolute words (always, never, all, only) can be crossed off without reading.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md",
     "lines": "4",
     "quote": "**Based on:** Forensic analysis of 150 MCQ + 100 MSQ items (62.7% MCQ leak rate, 51.0% MSQ leak rate)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md",
     "lines": "15",
     "quote": "| Absolute language in wrong options | 27.3% | 34% | Students eliminate \"always/never/all/only\" without reading |",
     "verbatim": true
    }
   ],
   "against": "The shares are among leaked items only; no rate for clean items is given (same file:13-15).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep",
   "reason": "Quotes verbatim; three external-audit findings plus a later binding copy rule (added). Adds to truth 5.",
   "statement": "Write every option in the same grammatical shape; a key that is the only option with a different opener, article or clause pattern can be found by shape alone.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md",
     "lines": "8",
     "quote": "\"The answer is the only option not shaped like a question\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md",
     "lines": "10",
     "quote": "\"The correct sentence is the only one that does not use 'because'\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md",
     "lines": "9",
     "quote": "key is the only option without an article",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/BUILD-SPEC-batch.md",
     "lines": "6",
     "quote": "options open in parallel form (no odd article/opener)",
     "verbatim": true
    }
   ],
   "against": "Automated shape flags can be false positives: \"recorded so the raw score is not taken at face value\" (feedback-inceptbench-2026-09-18/REGISTER.md:14).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep",
   "reason": "Quotes verbatim; the repair kit's construction recipe and leak table plus an external audit. Adds to truths 5 and 6.",
   "statement": "Build wrong options as near-neighbours: a real detail of the text with one element changed; absurd, off-category or true-of-any-text options are eliminated without reading.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md",
     "lines": "184",
     "quote": "- Change ONE of: the subject, the cause, the effect, the relationship direction, or the scope.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md",
     "lines": "17",
     "quote": "| Generic topic-domain wrong option | 22% | 8% | \"Any passage on this topic\" option is trivially wrong |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md",
     "lines": "9",
     "quote": "\"One option is not a Darling child, so it is eliminable from the stem alone\"",
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
   "verdict": "keep",
   "reason": "Quotes verbatim. Two independent reviews of one item plus a proposed misconception catalogue; the elimination argument is a mechanism, not measured. Adds to truth 5.",
   "statement": "Each wrong option should carry a different misconception; when all wrong options share one tone or one misreading, the key wins by elimination.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "64",
     "quote": "All three distractors (friendly, gentle, caring) share the same \"nice\" valence, so the only unpleasant word (menacing) wins by elimination",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/L5-REVIEW-GAPS-2026-09-17.md",
     "lines": "8",
     "quote": "all three distractors were the same misconception (menacing used for something pleasant)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/KB_FURTHER_IMPROVEMENTS.md",
     "lines": "40",
     "quote": "author named misconception catalogue (M-REVERSE, M-EFFECT-AS-CAUSE, M-LAST-FIRST…), tag each distractor",
     "verbatim": true
    }
   ],
   "against": "A usage check may legitimately test one register violation: \"Downgraded to MINOR; criterion was designed for comprehension MCQs\" (peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-B-D5-D6-D11-D13.md:21).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep",
   "reason": "Quotes verbatim; supported by the select-all audit status and design rules. Adds to truths 5 and 6.",
   "statement": "In select-all items each option is judged on its own, so every option must be decidable only from the text, and knowing one right answer must not reveal another.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/MSQ_REGEN_GUIDE.md",
     "lines": "3",
     "quote": "**Status:** MSQ pool is 100% leaked (0 of 1,346 structural-pass items usable).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/MSQ_REGEN_GUIDE.md",
     "lines": "12",
     "quote": "In MSQ each option is judged true/false independently.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/MSQ_REGEN_GUIDE.md",
     "lines": "41",
     "quote": "**5. Knowing one correct answer must not help you find the other.**",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (line 96). 'Either turns a four-option item into a coin flip' overstated: a contradictory pair leaves 50/50, but one stem-ruled-out option removes one choice; the audited example needed two weak options to leave a coin flip. Statement corrected and the source's own line added. Adds to truth 5.",
   "statement": "No two wrong options may contradict each other, because a reader drops both and is left with a 50/50, and none may be ruled out by the stem alone; in one audited item an absolute-word option and a stem-ruled-out option left a choice between the key and one near-neighbour.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md",
     "lines": "96",
     "quote": "is left with a 50/50 — you have effectively built a 2-choice item.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md",
     "lines": "124",
     "quote": "Option C uses \"Both... agree\" on a question asking about a *difference* — eliminatable by reading the stem alone.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md",
     "lines": "125",
     "quote": "The problem is options B and C are too easy, so students only need to choose between A and D.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep",
   "reason": "Quotes verbatim (the second on line 70). A live-pool audit and the repair kit's main-idea rule both support same-scope options. Adds to truth 5.",
   "statement": "For a main-idea item all options must be the same scope: no broad truism among the wrong options and no key that is the only broad option.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FIX_LIST.md",
     "lines": "102",
     "quote": "`mainidea-earthworm-mcq-05` leaks instead via the \"pick the broadest option\" main-idea heuristic (its foils are all true narrow details).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md",
     "lines": "70",
     "quote": "main-idea status (a \"promoted supporting detail\" distractor).",
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
   "verdict": "keep",
   "reason": "Quotes verbatim: a 14-item leak pattern, a dropped false positive where keyword matching pointed away from the key, and an external audit. 'Learners match words' is inferred from blind solvers. Adds to truth 5.",
   "statement": "Put the question's distinctive words on a wrong option, not on the key; when the key repeats the stem's words or is the only option of its kind, learners match words or sentence types instead of reading.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FIX_LIST.md",
     "lines": "92",
     "quote": "Student discriminates by sentence-TYPE, not support-relationship. Hottext variants leak because the prompt reuses the key's distinctive content words.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FIX_LIST.md",
     "lines": "108",
     "quote": "The verbatim-keyword sentence (h9) is a DISTRACTOR; the key (h8) shares no prompt keywords — keyword-matching points AWAY from the key",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "79",
     "quote": "Key is the only option that repeats the stem's verb ('find'→'found')",
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
   "reason": "Quotes verbatim; a live mastery-form audit and the select-all stem rule. Adds to truth 5.",
   "statement": "Word stems so they point to the text (what the passage describes), never to how the world works, since a stem that invokes general knowledge invites answering without reading.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FIX_LIST.md",
     "lines": "75",
     "quote": "Prompt 'Match each cause to its correct effect based on how the water cycle works' explicitly invites world-knowledge, not the text.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/MSQ_REGEN_GUIDE.md",
     "lines": "39",
     "quote": "The stem must invoke a passage-specific standard",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Knowledge-building, read in full: the original wording ('fail the plain blind test') was inverted, and its headline case was later reclassified as plain-blind gameable under a newer solver, so a spine-only leak is not currently demonstrated; two capstone items were spine-only leaky under the same historical solver. Restated as a rule resting on the report's reasoning and disposition. Adds to truths 5 and 43.",
   "statement": "In a sequence that builds knowledge, an item on a new text can be answerable from what earlier lessons taught, which makes it no evidence the learner read the new text; test such items with the earlier lessons' content given to the solver, and write distractors consistent with the taught schema that only the new text decides between.",
   "kind": "adopted rule (from a dated measurement)",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/spine-gate/SPINE-GATE-REPORT.md",
     "lines": "81-82",
     "quote": "is a schema generalization the earlier lessons make derivable",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/spine-gate/SPINE-GATE-REPORT.md",
     "lines": "83",
     "quote": "exactly why the item cannot serve as evidence the student read text 4.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/spine-gate/SPINE-GATE-REPORT.md",
     "lines": "86-87",
     "quote": "re-author with distractors that are schema-consistent alternatives only text 4 disambiguates",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/gate-capstone-summary.json",
     "lines": "16",
     "quote": "\"spine_leaky\": 2,",
     "verbatim": true
    }
   ],
   "against": "The headline case no longer stands: \"calibrated Gemini 3.5 solves the target 3/3 without either passage or prior-course context.\" (demo-unit-2026-07-10/spine-gate/SPINE-GATE-REPORT.md:7), and the report records \"withdrawing the old claim that plain-blind screening could not detect this item\" (same file:111-112); the capstone counts come from the same historical solver.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep",
   "reason": "Quotes verbatim; a replay reversed the historical verdict, and the item gate summary itself demotes the old solver to provenance (added). Adds to truth 34.",
   "statement": "A blind-solve verdict belongs to the solver and version that produced it; rerun old verdicts with a pinned current model before relying on them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/spine-gate/SPINE-GATE-REPORT.md",
     "lines": "7",
     "quote": "calibrated Gemini 3.5 solves the target 3/3 without either passage or prior-course context.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/spine-gate/SPINE-GATE-REPORT.md",
     "lines": "113",
     "quote": "solver results drift and must be rerun with a pinned current model.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
     "lines": "5-6",
     "quote": "treat Gemini 2.5 as historical provenance, not current model selection or current cross-family certification",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep",
   "reason": "Quotes verbatim (the second on line 70). Measured flip rates across draws support the multi-draw ship standard and the exclusion ledger. Adds to truth 34.",
   "statement": "Treat text-dependence verdicts as stochastic: ship only items clean across several independent blind draws, and permanently exclude any item that ever leaked.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "68",
     "quote": "Measured: ~22% flipped on the 2nd draw, 11.1% on the 3rd unified draw — it asymptotes but",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "70",
     "quote": "permanently excludes any item that *ever* leaked, so a",
     "verbatim": true
    }
   ],
   "against": "A boundary score on few samples can be noise: an item at the 0.5 bar on 4 samples resolved at K=10 and was kept as practice, \"(the 0.5 was small-sample noise)\" (same file:107).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The source says errored blind attempts bias toward certification and errored controls toward a false defect; 'errored attempts bias toward passing' gave only half. Statement corrected. Adds to truth 9.",
   "statement": "Re-run only measurements that failed to complete, never re-roll unfavourable verdicts, and never certify on missing evidence: an errored blind attempt biases toward certifying an item, and an errored control toward a false defect.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
     "lines": "47",
     "quote": "attempts bias toward certification; errored controls toward false defect). Leaky verdicts",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
     "lines": "48",
     "quote": "were never re-rolled. The wave flipped 2 false certifications to leaky and 2 to",
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
   "reason": "Quotes verbatim (the second on line 36). Gate design plus four with-text control failures; the second report wanted the control to bound a leak claim rather than to check answerability, a related use. Adds to truths 5 and 6.",
   "statement": "Pair the blind test with a with-text control: an item must be answerable when the text is present as well as unanswerable without it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
     "lines": "9",
     "quote": "bar: plain-blind anti-leak (passage withheld) + with-passage answerability control",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
     "lines": "36",
     "quote": "genuinely ambiguous with the text",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md",
     "lines": "53",
     "quote": "**No passage-present control.**",
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
   "reason": "Quotes verbatim. In-loop 100%, independent audit 89% and a deterministic probe catching 5/15 tells both missed support independence; the intersection rule is the adopted bar. Adds to truths 43 and 66.",
   "statement": "Certify text-dependence with solvers from model families other than the generator and call an item clean only if every family fails; a generator's own grader passes items that independent and deterministic checks catch.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/LLM_GENERATION_BOUNDARY.md",
     "lines": "34",
     "quote": "In-loop grader passed at 100%; independent audit held ~89% (passed a half-leaky EBSR); a post-deploy structural probe then caught 5/15 longest-option tells *both* earlier graders missed.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "18",
     "quote": "**Intersection rule:** clean iff *every* family fails to recover (rate ≤ 0.5); leaky iff *any*",
     "verbatim": true
    }
   ],
   "against": "Independence needs enforcement, not just separate agents: \"mistaking two agents with shared write access for enforced independence\" (codex-qa/tool-reuse-assessment-2026-09-14.md:47); and the generator itself stayed one family: \"**Single generator family.**\" (COURSE_QUALITY_GATE_REPORT.md:124).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep",
   "reason": "Quotes verbatim (the second on line 66). Items a blind solver recovered still averaged 0.932 on the quality benchmark; the report calls the two orthogonal. Adds to truth 44.",
   "statement": "A high instructional-quality score says nothing about whether items need the text.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md",
     "lines": "60",
     "quote": "Stratified 90-item sample (30 per type) scored **mean 0.932**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md",
     "lines": "66",
     "quote": "compliance, NOT passage-dependence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/LLM_GENERATION_BOUNDARY.md",
     "lines": "19",
     "quote": "wrong construct; green-lights leaks at 1.0",
     "verbatim": true
    }
   ],
   "against": "It can still catch blatant mismatches: \"IB *can* catch a **blatant** passage mismatch and did here\" (alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md:254).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep",
   "reason": "Quotes verbatim. Near-duplicate of truth 34 (send each answer more than once); kept because it adds a quality benchmark's measured flip band, concentrated on formats it has no native evaluator for.",
   "statement": "Measure a quality judge's agreement with itself across independent draws before trusting it, especially on formats it has no native evaluator for.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "31",
     "quote": "grader self-agreement was measured first",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "40",
     "quote": "| **no** | **match** | 2 | **0/2** (1.00↔0.55, 1.00↔0.95) | **flip-band — IB NON-DIAGNOSTIC** |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "34",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "keep",
   "reason": "Quotes verbatim: a per-item gate passed a course whose 947 passages collapse to 136 and whose forms share stems; a later certifier confirmed disjoint forms. Adds to truth 68.",
   "statement": "Per-item checks cannot see course-level faults, so de-duplicate passages and stems across the whole set and keep parallel forms disjoint.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/LLM_GENERATION_BOUNDARY.md",
     "lines": "36",
     "quote": "947 passages collapse to 136 distinct (one reused 22×), 134 stems duplicated, MAP forms A/B share 3 stems. The compliance gate PASSED — it checks none of this.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "398",
     "quote": "4 parallel mastery forms fully **DISJOINT**: 114 distinct items, max pairwise overlap = 0.",
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
   "reason": "Quotes verbatim: a checklist row written from a shipped article error and a walkthrough finding of a quoted 'me' in an assembled sentence.",
   "statement": "A sentence frame with a blank must read correctly for every value the blank can take, including pronouns inside embedded quotes; check by substituting each value.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "49",
     "quote": "an article/agreement mismatch (\"has a enchanting\") is a defect, not a copy nit",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
     "lines": "17",
     "quote": "assembled you-do sentence carries Peter's \"me\" (\"Captain Hook 'hates me…'\")",
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
   "reason": "Quotes verbatim; a review-profile criterion applied in two lessons. A house rule, not a measured effect.",
   "statement": "Write item stems as full questions, not sentence-completion fragments.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/L4-REVIEW-GAPS-2026-09-16.md",
     "lines": "117",
     "quote": "Item stems are questions, not completion fragments (D5.11)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/L5-REVIEW-GAPS-2026-09-17.md",
     "lines": "7",
     "quote": "was a completion fragment (\"…staying here could mean ___\"), the only fragment stems in L5",
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
   "reason": "Quotes verbatim; a content review plus a blocking checklist gate.",
   "statement": "Never ask a question answerable yes or no or by a two-way pick: recast it as what or how, with at least four plausible options.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt",
     "lines": "25",
     "quote": "Even though the app says you can't just answer it yes or no, we should just avoid these questions altogether.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "50",
     "quote": "Every MCQ has ≥4 plausible options; zero two-option coin flips",
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
   "reason": "Quotes verbatim (the second also recurs at line 91). Measured answer-echo overlap plus an external audit of a check reusing the teaching card's example. Adds to truths 3 and 41.",
   "statement": "Don't key a follow-up to the exact words the learner just heard or to the example used to teach; that tests echo, not understanding.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/compare-2026-09-23/index.html",
     "lines": "68",
     "quote": "Measured across every branched cfu, ours were the outliers: L4 echoed its answer at",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/compare-2026-09-23/index.html",
     "lines": "77",
     "quote": "The right answer is the sentence Scout just said, word for word.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "63",
     "quote": "and it reuses the p2 card's own key concept (bared teeth)",
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
   "verdict": "keep",
   "reason": "Quotes verbatim; a curriculum audit and an external audit found earlier steps using up later steps' evidence. Distinct from truth 3: it spoils a later model or task, not only a first attempt. Adds to truths 3 and 41.",
   "statement": "An earlier step must not use up the evidence or answer a later step teaches or tests; an early check keyed to the model's own clue, or a 'where to look' step that names the evidence, empties the later task.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "112",
     "quote": "pre-spends the MM clue \"without a mother\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "94",
     "quote": "p13's key ('John grabbed a wooden sword and stood in front of his little brother.') is the exact line p14's I-do model later 'finds'",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "127",
     "quote": "The Search step's correct answer names two of the three Step-3 evidence lines directly",
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
   "verdict": "keep",
   "reason": "Quotes verbatim; added the register's own class rule from the same line. 'ela' in the folder name is an AI reviewer app, not a person. A first-lesson exception was ruled. Adds to truth 3.",
   "statement": "When an answer must use a taught word, print that word nowhere in the question, instructions or hints that demand it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-ela-chat-2026-09-24/REGISTER.md",
     "lines": "10",
     "quote": "don't take this as a general licence to put the taught word in the stem",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-ela-chat-2026-09-24/REGISTER.md",
     "lines": "10",
     "quote": "Class to encode: \"taught word demanded ⇒ not printed in the demanding node\" (L1 exempt by ruling)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md",
     "lines": "19",
     "quote": "you-do question gives away the magic word",
     "verbatim": true
    }
   ],
   "against": "An exception was ruled for the first lesson of a course: \"I judged the item purely on retrieval strength and missed that at the very start of a course the trade-off runs the other way.\" (feedback-ela-chat-2026-09-24/REGISTER.md:14).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep",
   "reason": "Quotes verbatim. Near-duplicate of truth 3 (nothing a student sees or hears gives the answer first); kept because it shows the leak sites were praise, nudges and instructions, not feedback, across four lessons.",
   "statement": "Answer leaks come from every learner-facing line, not only wrong-answer feedback, so check praise, nudges, instructions and the guide's own turn as well.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
     "lines": "15",
     "quote": "praise / nudges / instructions hand over the Step 3–4 answers",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/PR-BODY.md",
     "lines": "5",
     "quote": "Answers no longer handed over by nudges, praise, instructions or Scout's part",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "49",
     "quote": "before any miss is even required",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "3",
   "name_bearing_source": false
  },
  {
   "index": 29,
   "verdict": "keep",
   "reason": "Quotes verbatim; a lens method and a binding validator rule. Adds to truths 1 and 67.",
   "statement": "Check for leaks mechanically: no hint may contain an answer word from its own marking criterion, and no wrong-answer reply may contain a word only the key carries.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md",
     "lines": "174",
     "quote": "Methodology: collect exemplar/answer words (> 4 characters, meaningful) from each criterion's `requirement` field; check whether those words appear in the same criterion's `hint` or `second_hint` text.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/BUILD-SPEC-batch.md",
     "lines": "175",
     "quote": "fix = printed-only rewrite of the wrong reply so it names no word only the key carries",
     "verbatim": true
    }
   ],
   "against": "Over-strict leak checks can withhold useful hints: \"Withholding it was a false positive that left a child on their THIRD miss\" (peter-pan-standing-2026-09-11/readiness-2026-09-16/pr263-merge/RED-REGISTER.md:27).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 30,
   "verdict": "keep",
   "reason": "Quotes verbatim; an adjudicated merge showed the framing-word false positive withheld a needed hint. Adds to truths 1 and 38.",
   "statement": "Test leak detectors for false positives too: counting the marking criterion's own framing words as answer words withheld a hint a learner needed.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/pr263-merge/RED-REGISTER.md",
     "lines": "24",
     "quote": "ours' `leakedWords` flags `[\"reason\",\"any\"]` on that rung; staging's returns `[]`.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/pr263-merge/RED-REGISTER.md",
     "lines": "27",
     "quote": "Withholding it was a false positive that left a child on their THIRD miss",
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
   "reason": "Quotes verbatim; one probed case where regeneration introduced a misreading of the text. Reinforces truth 29's preference for lines written and checked in advance.",
   "statement": "When a generated reply fails a check, fall back to the authored text verbatim instead of regenerating, because a regeneration that avoided the flagged words introduced a factual error about the text.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
     "lines": "57",
     "quote": "The replacement introduced a factual error.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
     "lines": "63",
     "quote": "The backstop should fall back to the authored hint verbatim rather than regenerating on this path",
     "verbatim": true
    }
   ],
   "against": "Observed on one item in one run; an earlier run of the same input was safely vague: \"This run's feedback misread. The discrepancy confirms the issue is non-deterministic\" (same file:59).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 32,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Reworded from 'praise' to 'feedback' because truth 2 bars praise; the finding (crediting a detail the learner never said) stands. Adds to truth 11.",
   "statement": "Generated feedback must credit only what the learner actually said; crediting a story detail the answer never mentioned misleads the learner about what was right.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
     "lines": "81",
     "quote": "The praise attributes a correct story fact to the child that the child never said.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
     "lines": "85",
     "quote": "or directly reflect the child's stated idea",
     "verbatim": true
    }
   ],
   "against": "Intermittent, not systematic: \"This run's praise misread. Again non-deterministic.\" (same file:83).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 33,
   "verdict": "keep",
   "reason": "Quotes verbatim; 16 live calls, all bands right, two coaching-text misreads. Adds to truth 37.",
   "statement": "Evaluate a judge's feedback text separately from its verdict, since every score can be right while the coaching text misreads the source or the answer.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
     "lines": "37",
     "quote": "All 16 bands are correct. No held pass and no passed hold found. Two coaching-text issues found on p19, both in the `swyk-dialogue` node.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
     "lines": "97",
     "quote": "These findings are coaching-text quality failures, not scoring failures.",
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
   "reason": "Quotes verbatim. The four-variant probe was run; the longer list is a verification proposal and the negation case comes from a design spec, so the full set is a synthesis. Adds to truths 10 and 37.",
   "statement": "Probe every judged item with a fixed set of answers: a full pass, one criterion only, a plausible wrong answer, the hint echoed back, a misspelled right answer, keyword nonsense, a valid synonym, a fluent wrong answer and the answer's negation.",
   "kind": "adopted rule (partly proposed)",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
     "lines": "10",
     "quote": "Four variants per item: full-pass, one-criterion-only, plausible wrong, hint-echo.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/VERIFICATION-PROPOSALS.md",
     "lines": "8",
     "quote": "compare correct meaning with a typo, nonsense resembling a keyword, valid synonym, fluent wrong answer, partial answer and contradictory premise",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "68",
     "quote": "Never string-match. Matching on “broken” passes “trust can never be broken,” which is the opposite of the answer.",
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
   "reason": "Quotes verbatim; an external audit found disagreeing acceptance rules on blanks in two lessons. Adds to truth 67.",
   "statement": "Define one acceptance rule per answer; when the rubric, accepted forms, word bank and hints each define it separately, they drift apart.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "18",
     "quote": "The mood blank has three acceptance rules that disagree",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "56",
     "quote": "Four rules for the final blank disagree",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "57",
     "quote": "but the reading-notes Step-3 hunt's accept list omits \"evil\"",
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
   "reason": "Quotes verbatim; two external audits flagged the same class, which was left for a ruling, so 'confuses' is the auditors' judgment.",
   "statement": "Treat the same piece of evidence the same way everywhere in a course; a sentence accepted on one page and rejected on another confuses what counts.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md",
     "lines": "20",
     "quote": "one sentence accepted on one page, rejected on another (magician)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "67",
     "quote": "is rejected as evidence on p16",
     "verbatim": true
    }
   ],
   "against": "The class awaits a ruling: \"RULING (open)\" (feedback-inceptbench-2026-09-29/REGISTER.md:20).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 37,
   "verdict": "keep",
   "reason": "Quotes verbatim; an external audit and a walkthrough found untrue paraphrases in write-ups, feedback and keys. Extends truth 1's 'only what is true' and truth 59.",
   "statement": "Every claim a lesson makes about its source must be true to it, not just its quotes: model write-ups, feedback, stems and answer keys paraphrased the text wrongly.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "25",
     "quote": "\"The children could not sleep and lay wide awake\" is wrong — only John lies wide awake",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "120",
     "quote": "Five feedback/reveal lines contradict the story",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
     "lines": "10",
     "quote": "find-it key teaches a fact not in the story (London bedtime/rules/grown-ups)",
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
   "reason": "Quotes verbatim: a knowledge-base clue absent from the story and a design HTML line not in the story; the third shows a contested definition the governing design prescribed. Adds to truths 43 and 57.",
   "statement": "Source design documents and knowledge bases can be wrong about the text, so check every quote, model answer and definition they supply against the text before copying it verbatim.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "71",
     "quote": "The KB-listed 'fire burned low' clue is NOT used because the story does not contain that line",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "41",
     "quote": "the Modelling Moment HTML itself has \"because they are bored\" (not in the story)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "153",
     "quote": "is PRESCRIBED by the PP3 design DOCX",
     "verbatim": true
    }
   ],
   "against": "Where named designs govern, prescribed strings were kept pending a ruling: \"a design-prescribed string is NOT changed — say so in notes\" (feedback-live-walk-2026-09-30/BUILD-SPEC.md:4).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 39,
   "verdict": "keep",
   "reason": "Quotes verbatim: an external audit, a word-form error found by two reviewers, and a circularity criterion; the borrowed-detail case is disputed against the governing design. Adds to truth 18.",
   "statement": "A definition gives the word's general meaning in the word's own grammatical form, without using the word itself or borrowing details from the text where it appears.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "83",
     "quote": "'Furious' is defined wrongly on every visible passage ('very fast and full of anger')",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/PP-STANDING.md",
     "lines": "34",
     "quote": "is a word-form error",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md",
     "lines": "79",
     "quote": "| D4.17 | Distinct target words | PASS | Only 1 word; definition uses \"dangerous\" (different word); morph gloss uses \"menace/harm\" (different words). No circular definition. |",
     "verbatim": true
    }
   ],
   "against": "The flagged definition was prescribed by the governing design and reverted to it pending a ruling (feedback-inceptbench-2026-09-30/REGISTER.md:153).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 40,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 'Confused learners' overstated: the walkthrough was a content check, not learner data; 'summary' replaced with the checklist's end-of-lesson receipt. Adds to truth 18.",
   "statement": "Give each taught word and key idea one wording, used identically on the card, glossary, feedback, goal and end-of-lesson receipt; one walkthrough found three different trait rules and an invented detail within a single lesson.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "43",
     "quote": "One definition per word, verbatim everywhere",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
     "lines": "19",
     "quote": "three different trait rules; feelings keyed as traits; invented \"again and again\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/KB_FURTHER_IMPROVEMENTS.md",
     "lines": "46",
     "quote": "Canonical hinge proposition per weak skill** propagated verbatim teach→CFU→review",
     "verbatim": true
    }
   ],
   "against": "Verbatim reuse also spreads an error: \"'Furious' is defined wrongly on every visible passage ('very fast and full of anger')\" (feedback-inceptbench-2026-09-30/REGISTER.md:83).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 41,
   "verdict": "keep",
   "reason": "Quotes verbatim; a shipped unhuntable key word and a baseline count of vocabulary items about words absent from their passages.",
   "statement": "A word learners are asked to find in a text must actually occur in it, exactly or as a word-family form; otherwise the search becomes tapping highlighted lines.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "100",
     "quote": "A taught key word must actually occur in the passage or the hunt degrades into glowing-line tapping",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/SUMMARY_AGENT.qmd",
     "lines": "99",
     "quote": "~53 vocab-not-in-passage",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 42,
   "verdict": "keep",
   "reason": "Quotes verbatim (the third on line 266): 5 of 23 authored splits wrong, over-general affix glosses, and a calibration log ranking outside-authority content checks as the top human-only class. Adds to truth 44.",
   "statement": "Check word-part splits and affix meanings against a rule-based reference, never intuition; teach only real parts, and words that don't split as word families.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "224",
     "quote": "5 of 23 authored splits wrong",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/PP-STANDING.md",
     "lines": "37",
     "quote": "(\"-ing means it is happening right now\" for enchanting / menacing, whose definitions are descriptive)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/AUTOMATED-CHECKS-ROADMAP-2026-08-31.md",
     "lines": "266",
     "quote": "judgment across all 9 logged rounds (4 hits, the top-ranked residue class).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 43,
   "verdict": "keep",
   "reason": "Quotes verbatim: a review criterion, a rewritten spoiler example and a walkthrough finding of example words harder than the taught word (same-suffix examples). Adds to truth 18.",
   "statement": "Teach a new word with examples from outside the text being studied, easier than the word itself, that don't reveal what happens in the text.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md",
     "lines": "70",
     "quote": "| D4.6 | Examples beyond story | PASS |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21/index.html",
     "lines": "215",
     "quote": "The example no longer tells the ending",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
     "lines": "25",
     "quote": "same-ending examples harder than the word",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 44,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. A validator exempts words the learner must supply as the inference, and one lesson's taught word is deliberately absent from its passage, so 'must appear in its text' was too strong. Statement corrected. Adds to truth 18.",
   "statement": "A taught word should appear in its own text, recur in later lessons and be assessed by use, not only recognition; the exception is a word the learner must supply as the inference, which is deliberately left out of the text.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "12",
     "quote": "A taught word appears at least twice in its own passage and is met again in a later authored lesson",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md",
     "lines": "71",
     "quote": "| D4.7 | Use not recognition | PASS |",
     "verbatim": true
    }
   ],
   "against": "An inferred trait word is deliberately absent: \"Deliberate absence from the passage (confirmed: zero occurrences in passage text) forces the child to supply it as evidence of comprehension.\" (peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-C-D7-D8-D10-D12.md:29); and \"`validate-vocab-earned.mjs:198–220` explicitly exempts encapsulating words from own-passage/later-lesson recurrence rules\" (feedback-devfactory-2026-09-10/analysis-current-courses/G3-APPLICABILITY.md:24).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 45,
   "verdict": "keep",
   "reason": "Quotes verbatim. The transcript 'written with an eye' reads as a spoken letter (i/y) transcribed as a word, inferred from the clip's spelling explanation; added a second documented mishearing. Adds to truth 44.",
   "statement": "Machine transcription mishears letter names and word fragments, so have a person listen to word-part clips and print affixes with a hyphen so they don't read as words.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/listen-qa-l4-l7-2026-09-24/G3-U1-L6/p2-word.txt",
     "lines": "5",
     "quote": "Mercy, written with an eye,",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "291",
     "quote": "Whisper mis-hears short morphemes",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "132",
     "quote": "the morpheme gloss writes \"the suffix ant\" without a hyphen (reads as the insect to a grade-3 student)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21.md",
     "lines": "22",
     "quote": "whisper hears \"ant\" as \"and\"; does a child?",
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
   "verdict": "keep",
   "reason": "Quotes verbatim: rulings plus read-back checks of joined syllable clips. This is audio voice, not truth 2's writing voice. The chosen two-part split was disputed by an external audit.",
   "statement": "When a word is broken into parts for pronunciation, voice each part as it sounds inside the word, in the same voice as the whole word, and check the joined sequence reads back as the word.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21.md",
     "lines": "101",
     "quote": "\"pronounce the parts as parts of that word, not as individual parts\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21.md",
     "lines": "107",
     "quote": "the old three-piece set read back \"Manganese\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21.md",
     "lines": "123",
     "quote": "\"same voice for the pieces and the full word\"",
     "verbatim": true
    }
   ],
   "against": "An external audit disputed the resulting split: \"splits the word into two syllables instead of the correct three\" (feedback-inceptbench-2026-09-30/REGISTER.md:65); three words were left unchanged because in-word candidates read worse (HUMAN-REVIEW-2026-09-21.md:107-108).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 47,
   "verdict": "keep",
   "reason": "Quotes verbatim; replaced the truncated second quote with the full sentence across lines 95-96 and added the entry-knowledge heading. Knowledge-building, read in full: the inventory is a sandbox design input, not approved doctrine. Adds to truths 18 and 20.",
   "statement": "Inventory what each text assumes and adds, tied to the words that carry each item, and make sure every assumption is covered by an earlier text or stated entry knowledge, with no forward references.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-knowledge-inventory.md",
     "lines": "8",
     "quote": "Proposed adds / assumes per text, with carrying spans.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-knowledge-inventory.md",
     "lines": "20",
     "quote": "## Entry knowledge (theme assumes; no text teaches these)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-knowledge-inventory.md",
     "lines": "95-96",
     "quote": "Compounding check: every text's assumes are covered by earlier texts' adds or entry knowledge; no forward references.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-arc-continuity.md",
     "lines": "32",
     "quote": "### L5 characters and places — introduced before first use?",
     "verbatim": true
    }
   ],
   "against": "The file is input to placement, not doctrine: \"do not promote candidate IDs or the sandbox spine into approved curriculum doctrine.\" (demo-unit-2026-07-10/00-knowledge-inventory.md:5-6).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 48,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Knowledge-building, read in full: 'teaches nothing new' is true of the unseen capstone text, not of the transfer-rung teaching text, which adds four knowledge items; the statement now separates them and cites the capstone's role line. Adds to truths 40 and 48.",
   "statement": "Order a set of texts so each builds on the knowledge the earlier ones added, then assess on an unseen text that exercises the same schema on a new surface, avoids curriculum-staple examples and teaches nothing new.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md",
     "lines": "17",
     "quote": "Ladder note: the ramp is primer -> build -> deepen -> transfer-neighbor.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-knowledge-inventory.md",
     "lines": "83",
     "quote": "Adds (cluster 1, transfer rung -- reduced topical overlap, same schema):",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/passage.md",
     "lines": "8",
     "quote": "- role: capstone-unseen (assessment text; NOT a teaching text -- exercises the acquired schema, teaches no new KC)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/passage.md",
     "lines": "14",
     "quote": "P6 (an invented flood-plain farm town, not the curriculum-staple Nile/Mississippi delta)",
     "verbatim": true
    }
   ],
   "against": "A sandbox design, not approved doctrine (demo-unit-2026-07-10/00-knowledge-inventory.md:5-6).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 49,
   "verdict": "keep",
   "reason": "Quotes verbatim; added the scaffold disposition (pre-teach rather than swap). The measure is a heuristic FK estimate. Knowledge-building. Adds to truths 18 and 23.",
   "statement": "Readability formulas don't see conceptual load, so judge a text's difficulty also by the new knowledge it carries, and pre-teach the words that carry that knowledge rather than swapping them out to hit a number.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md",
     "lines": "18",
     "quote": "measures lexically simpler than the primer (FK 3.5) because its sentences are short; its",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md",
     "lines": "19",
     "quote": "step up is carried by conceptual load (five new knowledge ids, two taught terms) and by",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md",
     "lines": "44",
     "quote": "REVISE cannot swap payload words out",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md",
     "lines": "46",
     "quote": "FLAG -> SCAFFOLD: vocabulary_support pre-teach for \"erosion\" and \"gorge\" (pronunciation + meaning) before the reading dose",
     "verbatim": true
    }
   ],
   "against": "The measure is a heuristic: \"FK-to-band reading below is a judgment call, not a psychometric fact.\" (demo-unit-2026-07-10/00-difficulty-notes.md:15).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 50,
   "verdict": "keep",
   "reason": "Quotes verbatim; a factuality protocol written during authoring of four informational stories. The handoff itself is not completed QC. Knowledge-building. Adds to truths 59 and 61.",
   "statement": "In a story that carries real-world knowledge, list and check every world claim at the precision the grade needs, mark invented particulars as fiction, check invented numbers that embed real rates, and confirm characters' misconceptions are clearly refuted.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
     "lines": "18",
     "quote": "Verify each at that precision (short causal statements, qualitative magnitudes) -- not at",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
     "lines": "113",
     "quote": "Where an invented number embeds a real-world RATE or MAGNITUDE claim, it",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
     "lines": "115",
     "quote": "Character misconceptions are deliberately planted and refuted; verify the REFUTATION is clear,",
     "verbatim": true
    }
   ],
   "against": "The ledger is a handoff; the binding verdicts belong to a separate QC pass that this file does not record (same file:3-6, 11-13).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 51,
   "verdict": "keep",
   "reason": "Quote verbatim; the protocol's cross-cutting row asks the checker to sign the whole causal model. A protocol, not a finding of misteaching. Knowledge-building. Adds to truth 59.",
   "statement": "Check the knowledge model a sequence of texts builds as a whole, not only its separate claims, because individually true steps can still misteach in sequence.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
     "lines": "96",
     "quote": "QC should sign the MODEL, not only the atoms: confirm no step of the chain as sequenced across texts 01->04 misteaches the standard account.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 52,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The protocol allows a character's absolute claim as stance, not as a taught universal, and requires planted half-truths to be corrected, so banning a character's absolute statement outright contradicted the source. Statement corrected. Adds to truth 59.",
   "statement": "Check that no line a text presents as fact over-generalizes ('every', 'all', 'never') where only some cases hold; a character's absolute claim is fine as that character's stance, and a planted half-truth must be corrected by the text.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
     "lines": "72",
     "quote": "it does NOT overgeneralize to \"every river builds a delta.\" Verify no reader-facing overgeneralization.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
     "lines": "120",
     "quote": "Stance/rhetoric riding a character voice is not a taught universal",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md",
     "lines": "41",
     "quote": "Do not claim that all London had no cars or electricity.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 53,
   "verdict": "keep",
   "reason": "Quotes verbatim; the audit traced a later unit's transfer questions to two ideas the served lessons halved. Knowledge-building. Adds to truth 48.",
   "statement": "Keep a lesson's key idea whole as designed, because later lessons ask learners to transfer it and a halved idea leaves a later question pointing at something the learner never met.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "67",
     "quote": "Cross-course dependency: WITW L11 Use it (PR #613) asks \"Where else have you seen a setting set the rules and the mood? Think about Peter Pan.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "167",
     "quote": "WITW L11/L14 Form B now point at exactly the two ideas L4 and L7 fail to land",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "224",
     "quote": "Picking our four Name-it sentences without those two ideas leaves WITW pointing at content the child never met",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 54,
   "verdict": "keep",
   "reason": "Quote verbatim; the audit traced background knowledge supplied only by the film proposed for cutting. Adds to truth 20.",
   "statement": "Before removing a component, check what background knowledge only it supplied.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "73",
     "quote": "the child would meet no old-London context at all",
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
   "reason": "Quotes verbatim; a continuity lens found a place located differently in consecutive lessons.",
   "statement": "Check facts for consistency across the lessons of a sequence, not only within each lesson.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-arc-continuity.md",
     "lines": "67",
     "quote": "## MINOR-1 — Mermaid Lagoon geographical inconsistency",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-arc-continuity.md",
     "lines": "84",
     "quote": "This is a factual story-world inconsistency.",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Replaced the third quote with the spec's own sentence on recurrence across parts, which supports the last clause directly; the spec rates spaced retrieval well evidenced (line 156). Knowledge-building. Adds to truth 48.",
   "statement": "A lesson's key idea must come back in later lessons as something learners produce from memory, not something restated to them: the idea named in one part is asked for, unshown, at the start of the next.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "118",
     "quote": "recur as something the child is asked to produce, not something restated at them",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "118",
     "quote": "the sentence taught in Part 1 is the sentence asked for at the start of Part 2, and again in Part 3, without being shown",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "119",
     "quote": "If a threshold sentence appears once and never again, we have taught a slogan.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 57,
   "verdict": "keep",
   "reason": "Quotes verbatim; the spec's central rule, later encoded in a mutation-tested validator.",
   "statement": "Hide what learners must recall before they produce it, because producing it with the model still on screen is copying, not recall.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "54",
     "quote": "The sentence must not be visible when the child produces it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/REGISTER.md",
     "lines": "104",
     "quote": "sentence not printed",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 58,
   "verdict": "keep",
   "reason": "Quotes verbatim; a design spec adopted for every lesson's closing questions. Adds to truth 40.",
   "statement": "Close a lesson with three moves on one idea: name it, find where it works in this text (asking when, not what), then use it beyond the text, with support fading and never returning.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "17",
     "quote": "Name it · Find it here · Use it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "80",
     "quote": "The slots must ask when, not what.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "109",
     "quote": "Support fades and never returns. Maximum at Q1, a frame at Q2, nothing at Q3.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 59,
   "verdict": "keep",
   "reason": "Quote verbatim; a spec rule written against a transfer question asked before learners had texts to connect. Adds to truth 48.",
   "statement": "Ask learners to connect to another text only when a specific earlier text can be named in the question; otherwise ask for a prediction framed by the idea.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "102",
     "quote": "Rule of thumb: use Form B only when you can name the prior text inside the question. If you cannot name it, use Form A.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 60,
   "verdict": "keep",
   "reason": "Quote verbatim. Adds to truth 10.",
   "statement": "Mark a prediction on whether the learner used the idea, not on whether the prediction comes true.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "104",
     "quote": "Mark on whether the rule was used, not on whether the prediction turns out right.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 61,
   "verdict": "keep",
   "reason": "Quote verbatim; the same line says accept the answer, then push once (repeated at line 114). Adds to truth 18.",
   "statement": "Set a vocabulary floor: treat an answer in weaker words than the text supplies as unfinished and push once for the text's stronger word.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "83",
     "quote": "Do not accept an answer in weaker language than the text supplies.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 62,
   "verdict": "keep",
   "reason": "Quote verbatim; the spec cites high success in guided practice as well evidenced (lines 160-162). Actual success rates were not auditable from the artifacts.",
   "statement": "Set a target success rate for each question and read deviations as design faults: near everyone should name the idea, most should find it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "110",
     "quote": "Success gradient: about 100%, about 80%, no key. If children are failing Q1, it is built wrong. If nearly everyone aces Q2, it is too easy to be worth asking.",
     "verbatim": true
    }
   ],
   "against": "Outcome rates were not auditable: \"Target success rates (~100%/~80% in the Closing Questions spec) and whether children actually infer are unauditable from artifacts.\" (curriculum-adherence-2026-09-24/CRITIC.md:29).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 63,
   "verdict": "keep",
   "reason": "Quotes verbatim; the spec's evidence-status table separates well-evidenced findings, frameworks and weak practices.",
   "statement": "State the evidence behind each design principle honestly, separating well-evidenced findings from frameworks and from weakly supported practices.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "147",
     "quote": "So that nothing in this spec is defended on a stronger basis than it deserves.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "171",
     "quote": "There is no good evidence that saying something in unison builds durable knowledge.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 64,
   "verdict": "keep",
   "reason": "Quotes verbatim; the figures match the primary-source check (g=.66 vs .01; g=.54 vs .04). External research, knowledge-targeting.",
   "statement": "A question asked before reading improves learning of what it asks about but hardly anything else, so aim it at the lesson's most important goal.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
     "lines": "37",
     "quote": "The publisher confirms **g=.66 for prequestioned information and g=.01 for other information**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
     "lines": "43",
     "quote": "The **g=.54 targeted / .04 general** estimates are confirmed (k97/91).",
     "verbatim": true
    }
   ],
   "against": "\"Do not predict a .66 effect for Grade3, general transfer, or a particular tap-to-commit interface.\" (same file:39); the child-specific targeted estimate was .22 versus adults' .62 (same file:43).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 65,
   "verdict": "keep",
   "reason": "Quotes verbatim (.30 to .07 for Grade 4 untargeted recall). The study's readers could not look back while answering, so checks with the text in view may differ. A limit on truth 7.",
   "statement": "Frequent inferential questions during reading can cut young readers' recall of the rest of the story, so keep mid-reading questions sparse, at natural boundaries, and measure whole-story recall when changing them.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
     "lines": "29",
     "quote": "The quoted **.30 control → .07 during-reading** result is Grade4 recall of **untargeted information**, not overall comprehension.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
     "lines": "31",
     "quote": "**Design conclusion:** frequent unsupported interruptions can be costly for younger readers.",
     "verbatim": true
    }
   ],
   "against": "\"This does not establish a non-negotiable ban on every mid-text check\" (same file:31); after-reading questioning was also worse than control (.16 versus .30, same file:29); and \"Participants could not look back while answering\" (same file:27).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 66,
   "verdict": "keep",
   "reason": "Quotes verbatim. Swapped the drawing-study effect line for its design conclusion and added the reveal-style conclusion; studies used adults and non-reading tasks, and with font held constant the contrast was only a trend. Adds to truth 52.",
   "statement": "When text or a model answer is revealed progressively, reveal whole words or chunks with synchronized explanation rather than slow letter-by-letter tracing.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
     "lines": "13",
     "quote": "**Design conclusion:** progressive modelling with synchronized explanation is plausible.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
     "lines": "19",
     "quote": "Whole-word appearance beat tracing on recall in Study1, d=.97.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
     "lines": "21",
     "quote": "**Design conclusion:** avoid slow letter tracing that obstructs reading; chunked reveal is a reasonable prototype.",
     "verbatim": true
    }
   ],
   "against": "Studies used adults and non-reading tasks: \"The paper does not require a mascot paw or establish that text appearing without one fails.\" (same file:13); \"Holding typeface constant, whole-word versus tracing was d=.74 with corrected p=.077/.076: a trend, not a significant contrast.\" (same file:19).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 67,
   "verdict": "keep",
   "reason": "Quotes verbatim; a research-boundary review and an adversarial critique of an improvement dossier.",
   "statement": "Check a cited study's population, task and contrast before turning it into a design rule; literature effect sizes justify a direction, not a predicted effect for your own learners.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
     "lines": "5",
     "quote": "The review contains useful ideas, but its **mandatory visible paw**, **universal after-reading-only rule**, and **feedback timing/size claims** exceed the evidence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/V2_MONSTER_DOSSIER.md",
     "lines": "176",
     "quote": "justify DIRECTION not a v2 number",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 68,
   "verdict": "keep",
   "reason": "Quotes verbatim; a value analysis, a detector census and an external audit. Adds to truth 40.",
   "statement": "What the worked example models must match what learners then do: the same step names, frame, and number and kind of evidence across the model, the guided turn and independent work.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/L6-VALUE.md",
     "lines": "23",
     "quote": "so what is modeled matches what is asked.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAP-CLOSURE-PLAN-2026-09-15.md",
     "lines": "46",
     "quote": "The detector's census found one more SHIPPED defect of the class: L5 p16 `youdo-clue-hunt` \"Step 2: Find the clues\" vs the model's and the we-do's \"Look for clues\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "114",
     "quote": "The we-do write-up frame has only one quote blank, while the I-do models two pieces of evidence and the you-do (p16) asks for two",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 69,
   "verdict": "keep",
   "reason": "Quotes verbatim; found independently by an external audit and a walkthrough. Adds to truth 40.",
   "statement": "In a worked example each step must add something; a 'what I know' step that repeats the conclusion never demonstrates the move it teaches.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "24",
     "quote": "so the model never demonstrates the step it teaches",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
     "lines": "14",
     "quote": "model's \"I know\" repeats the conclusion",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 70,
   "verdict": "keep",
   "reason": "Quotes verbatim; two external audits. Adds to truth 40.",
   "statement": "A worked example must obey the lesson's own definitions, and its stated reasons must support its verdicts.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "53",
     "quote": "The lesson defines a trait as repeated action, not a passing feeling",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md",
     "lines": "21",
     "quote": "a rejected think-aloud candidate whose aside argues for it",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 71,
   "verdict": "keep",
   "reason": "Quotes verbatim; a review criterion and a content review of a reference lesson. Adds to truth 40.",
   "statement": "A worked example should weigh plausible wrong options aloud and say why each is rejected, say which evidence it keeps when it finds more than it uses, and vary how many pieces it uses.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md",
     "lines": "25",
     "quote": "| D1.10 | Model the hard part | PASS | States 4-7 show 4 plausible-but-wrong clues each weighed and rejected with genuine reasoning before the strongest is named |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-content-review-2026-09-20/REGISTER.md",
     "lines": "14",
     "quote": "Modeled answer must SHOW the choice when more clues are found than written",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-content-review-2026-09-20/REGISTER.md",
     "lines": "16",
     "quote": "Avoid modeling \"always exactly two\"",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 72,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; added the finding's heading. 'State how many to find' is design-dependent: one governing design shows a count tracker, and the audit faults counts where the design asks for an open hunt. Statement corrected. Adds to truth 40.",
   "statement": "In independent practice, don't pre-mark the candidate answers or name where to look, and don't announce how many to find when the design asks for an open hunt; each turns independent practice back into guided practice.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "45",
     "quote": "**3. Independent Find is assisted, not an open hunt (core; L5, L6, L7; supporting in L4).**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "47",
     "quote": "L6 p16/step3 hot_text, 8 glowing segments, \"Tap the three clues ... Not all the glowing clues are useful\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "135",
     "quote": "the Zoom MCQ pre-names the evidence region and undoes the open hunt",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/procedures/Example_Lesson_Components.txt",
     "lines": "31",
     "quote": "usually by clicking the evidence in the shown passage (click-to-highlight) rather than choosing from options",
     "verbatim": true
    }
   ],
   "against": "One governing design itself shows a count, tracker \"{n} of 2 found\" (curriculum-adherence-2026-09-24/REPORT.md:46); whether a hunt can run with no pre-glow was left to an engine ruling (same file:48).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 73,
   "verdict": "keep",
   "reason": "Quotes verbatim (the first on line 34). A gap register and value analysis found a judging task met cold. Adds to truth 40.",
   "statement": "Model every task type before learners do it alone.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
     "lines": "34",
     "quote": "child the six-statement judging task cold",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/L6-VALUE.md",
     "lines": "36",
     "quote": "Refine arrives unmodeled",
     "verbatim": true
    }
   ],
   "against": "Mitigated in that case because the task was objective with a retry ladder and a floor reveal (GAPS-2026-09-11.md:34-35).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 74,
   "verdict": "keep",
   "reason": "Quotes verbatim; a course-level screen disclosed the gap. Adds to truth 28.",
   "statement": "Every skill a gate tests must be practised before the gate.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/FEEDBACK_RESPONSE.md",
     "lines": "167",
     "quote": "layer has **zero main-idea (KCT1) drill and zero inference (KCT5) drill**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/FEEDBACK_RESPONSE.md",
     "lines": "168",
     "quote": "So a student practicing in this layer gets no repeated main-idea or",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 75,
   "verdict": "keep",
   "reason": "Quotes verbatim (the first on line 135); a recorded decision restructured one unit's gating. Conflicts with truth 28 and a blocking checklist row; flagged in against.",
   "statement": "Keep teaching checks separate from assessment: in-lesson checks give feedback but don't gate, and a later assessment carries the mastery gate.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
     "lines": "135",
     "quote": "conflated): l0-l3 are now non-gating formative",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/publish/README.md",
     "lines": "24",
     "quote": "Teaching checks are scored for immediate feedback but do not gate lesson progression; only the",
     "verbatim": true
    }
   ],
   "against": "Elsewhere every check gates: \"No trap (child can always proceed by doing the work) and no leak (cannot proceed without it)\" (AlphaRead-QC-Checklist-v2-2026-09-04.md:126).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 76,
   "verdict": "keep",
   "reason": "Quote verbatim; a narrowly scoped renderer ruling for the first check of a knowledge-building unit opener, recorded for one grade. A limit on truth 28.",
   "statement": "A first check that opens a new knowledge unit can activate prior knowledge without blocking progress.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "129",
     "quote": "that first check activates and does not gate",
     "verbatim": true
    }
   ],
   "against": "Scoped narrowly in the same row: every later check in the lesson still gates, and the rule applied to one grade only (same line).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 77,
   "verdict": "keep",
   "reason": "Quote verbatim. Near-duplicate of truth 41 (two blocks of one kind must test different things); kept for a visual comparison showing the same question on consecutive pages in four lessons.",
   "statement": "Don't ask the same question twice in a row on consecutive pages.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/compare-2026-09-24/FINDINGS.md",
     "lines": "24",
     "quote": "**The same question is asked twice in a row.**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "41",
   "name_bearing_source": false
  },
  {
   "index": 78,
   "verdict": "keep",
   "reason": "Quotes verbatim; a content review of a reference lesson encoded as criteria. Compatible with truth 7 (placement) since it concerns what is on screen while reading.",
   "statement": "While learners read, show only the text: questions come after the reading, the reading scaffold disappears when a question appears, and learners can move back freely.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "110",
     "quote": "Only the passage on screen during reading; the question appears after the timer/read-aloud ends and the child clicks next",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "111",
     "quote": "Scout's reading commentary is a scaffold for the TEXT; it disappears when a quick-check question is on screen",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt",
     "lines": "7",
     "quote": "Lack of free movement around the book is one of the major drawbacks of not having a physical book",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 79,
   "verdict": "keep",
   "reason": "Quotes verbatim; one content review, encoded as a criterion and audited on another lesson.",
   "statement": "Checks during reading should target cause and effect and the details the lesson builds on later, not low-leverage details.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "113",
     "quote": "Quick-checks mix cause-and-effect pickup with pointers at the key details the lesson focuses on later; no low-leverage detail questions",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt",
     "lines": "9",
     "quote": "They need to be a mix of ensuring students can pick up the cause and effect in the text",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 80,
   "verdict": "keep",
   "reason": "Quotes verbatim; a content review and two independent item reviews. Adds to truth 6.",
   "statement": "Check that each question's real demand matches the skill being practised; a locate question that needs inference, or a stem asking for the reason the text gives when it gives none, mis-tests the skill.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt",
     "lines": "28",
     "quote": "This involves inference.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "61",
     "quote": "but the story never states a reason",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md",
     "lines": "258",
     "quote": "Either way the correct answer should be statable with a single-sentence verbatim pointer.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 81,
   "verdict": "keep",
   "reason": "Quotes verbatim; a criterion and two external audits; one internal validator contradicts it, recorded for a ruling. Adds to truth 17.",
   "statement": "Keep what the text says apart from what the reader infers: inferences never sit in the evidence slot and never go inside quote marks.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "72",
     "quote": "Inferred mood words (gloomy, enchanting, etc.) live only in the 'I know' step, never inside 'The text says'",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md",
     "lines": "14",
     "quote": "quote marks around words the writer never wrote",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "113",
     "quote": "puts quotation marks around the model's own inferential words",
     "verbatim": true
    }
   ],
   "against": "A validator in the same system required quote marks around a model inference, recorded as \"is a CONTRADICTION, not a fix\" (feedback-inceptbench-2026-09-29/REGISTER.md:57).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 82,
   "verdict": "keep",
   "reason": "Quotes verbatim; a canonical component specification and the derived criterion.",
   "statement": "A summary cloze blanks the causal links of what was learned, not incidental detail or connective words, and uses distractors that were true earlier but not now to test whether learners tracked change.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/procedures/Example_Lesson_Components.txt",
     "lines": "20",
     "quote": "“true-earlier-but-not-now” distractors test that the child tracked how things changed",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "26",
     "quote": "exactly four blanks on the links of the mental model, bank of 6, answers text-true, no connective blank",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 83,
   "verdict": "keep",
   "reason": "Quotes verbatim (the second shortened to its rule clause). The first half rests on one content review; the second on a review criterion that was recorded as a design-level note, not acted on.",
   "statement": "Name strategy steps in words that work on any text, not app mechanics, and frame the strategy as the learner's own tool.",
   "kind": "adopted rule (second half: review criterion)",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt",
     "lines": "21",
     "quote": "because ‘find’ captures what they will need to do in any text (not just on this app)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md",
     "lines": "98",
     "quote": "Every strategy is explicitly framed as 'yours to use when the text gets hard'",
     "verbatim": true
    }
   ],
   "against": "The framing criterion was flagged on one lesson and left as a note: \"INFER never framed as the child's portable tool (D1.28)\" ... \"carry to the arc register, not a fix\" (peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/L5-REVIEW-GAPS-2026-09-17.md:12).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 84,
   "verdict": "keep",
   "reason": "Quote verbatim (line 21); a structural value argument, not measured.",
   "statement": "Ask for two different pieces of evidence to support a claim, since one quote only shows the learner can copy.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/L6-VALUE.md",
     "lines": "21",
     "quote": "child can copy; two different quotes prove the claim is supported",
     "verbatim": true
    }
   ],
   "against": "The second quote is partly transcription labour and adds minutes (same file:32-35).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 85,
   "verdict": "keep",
   "reason": "Quotes verbatim (the first on line 10); the source says the value is structural, not measured.",
   "statement": "Follow locating evidence with a task that builds the concept, such as judging statements some of which the text contradicts, because locating alone leaves the concept unbuilt.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/L6-VALUE.md",
     "lines": "10",
     "quote": "evidence located, concept",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/L6-VALUE.md",
     "lines": "12",
     "quote": "that is retrieval PLUS falsification",
     "verbatim": true
    }
   ],
   "against": "The value claim was structural, not measured: \"NOT measured learning.\" (same file:4).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 86,
   "verdict": "keep-with-fix",
   "reason": "Quote verbatim. The source rule covers a copied annotation pattern (one tap, one affirming clip at the end of independent work), not every scaffold; statement narrowed. Thin evidence (one plan line). Adds to truth 48.",
   "statement": "Keep guiding prompts and confirm-taps on practice pages; assessment items carry none.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/PARITY-PLAN-2026-09-14.md",
     "lines": "12",
     "quote": "practice pages only, never assessments, #488",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 87,
   "verdict": "keep",
   "reason": "Quotes verbatim; added the checklist row that keeps the passage visible when feedback says look back, which the second clause needed. Adds to truth 1.",
   "statement": "Show feedback right at the answer it responds to, and keep the source visible whenever feedback says to look back.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "103",
     "quote": "Wrong-answer reply renders directly under the tapped option, not below the list",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/VISUAL-QA-2026-09-11.md",
     "lines": "46",
     "quote": "The feedback is right; its position is not where the child's eyes are.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "72",
     "quote": "passage visible whenever feedback says look back",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 88,
   "verdict": "keep",
   "reason": "Quotes verbatim; the numbers match (40-word target, 60 cap). Adds to truth 1.",
   "statement": "Keep feedback short (about 40 words, 60 at most), at or below the learner's reading level, and keyed to the misconception behind each wrong option.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "71",
     "quote": "≤40 words target / 60 hard cap",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/publish/README.md",
     "lines": "55",
     "quote": "≤40-word misconception-keyed feedback",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 89,
   "verdict": "keep",
   "reason": "Quotes verbatim. Adds to truth 4.",
   "statement": "When learners are let through after the allowed tries, say they are moving on and never dress it up as success; an honestly labelled final example is different from a hint that hands over the answer.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "130",
     "quote": "Release after N tries is named as moving on, never dressed as a win",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/G3-APPLICABILITY.md",
     "lines": "23",
     "quote": "These are pre-reveal answer-supplying hints, distinct from an honestly labeled final example.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 90,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The checks were machine transcription and onset measurement, not listening, so 'listen' is replaced; counts added from the summary line (13 onset findings among 55 clips with zero transcript mismatches). Adds to truths 24 and 44.",
   "statement": "Check every generated audio take for dropped words and for a quiet first word: one take dropped a clause, and 13 of 55 clips whose transcripts all matched had a first word 25–74 dB below the clip's own mean.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/ROUND-RESULT.md",
     "lines": "21",
     "quote": "L6 p15 first take dropped \"then she would have to find another way\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-listen-qa.md",
     "lines": "19",
     "quote": "| Onset findings (WEAK ATTACK) | 13 |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-listen-qa.md",
     "lines": "218",
     "quote": "55 clips checked. 13 onset findings, all confirmed real by independent RMS measurement. 0 transcript mismatches",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-listen-qa.md",
     "lines": "220",
     "quote": "the first word's attack in the 60ms after that silence falls 25–74dB below the clip's own mean",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 91,
   "verdict": "keep",
   "reason": "Quotes verbatim; checklist gates and codebase rules. Audio-text match, not truth 2's writing voice.",
   "statement": "On-screen text and its narration should match word for word with nothing spoken that isn't printed, and a missing clip should mean silence plus captions, not a substitute voice.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "79",
     "quote": "audio\\_of \\= sha256 of the spoken text for every clip; zero mismatches",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "84",
     "quote": "Every measured voiceover mark must locate inside the prose displayed on the same page",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "85",
     "quote": "a missing clip means silence + captions, never browser TTS",
     "verbatim": true
    }
   ],
   "against": "A recap narration spoke unprinted sentences and was accepted by precedent: \"wrap-steps-heading voiceover speaks 3 sentences not printed on p21\" (peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-C-D7-D8-D10-D12.md:40).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 92,
   "verdict": "keep",
   "reason": "Quotes verbatim; checklist gates.",
   "statement": "Narration must not compete with the learner: don't auto-read a question before the learner has read it, and never play two audio sources at once.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "90",
     "quote": "Stem audio plays only on demand, never autoplayed before the child reads",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "87",
     "quote": "No overlapping playback anywhere",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 93,
   "verdict": "keep",
   "reason": "Quotes verbatim; three courses' sweeps and audits. Adds to truths 24 and 46.",
   "statement": "Sweep learner-facing text for leaked authoring markup and placeholders, such as heading tokens, formatting marks, HTML entities, draft metadata or codes standing in for a passage.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FIX_LIST.md",
     "lines": "114",
     "quote": "Both leak the literal authoring token `HEADING:` into student-visible body text.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/SUMMARY_AGENT.qmd",
     "lines": "138",
     "quote": "144 items rendered `&#x27;`/`&amp;#x27;`/`&quot;` literally in feedback.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "434",
     "quote": "passage text is literally the CCSS code string `RI.3.8`. No passage. Unanswerable.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 94,
   "verdict": "keep",
   "reason": "Quotes verbatim. About spoiling later content, not giving answers, so distinct from truth 3; teasers are allowed. Adds to truths 3 and 21.",
   "statement": "Nothing in a lesson may preview content the learner has not reached yet: not the text, feedback, checks, pictures or introductory media.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "47",
     "quote": "No text, feedback, or check previews content the child has not reached",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt",
     "lines": "6",
     "quote": "The image is a bad one for the start of the story as it’s a spoiler for what will happen but mostly because it does not match what happens in the text on screen.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "85",
     "quote": "the inference states 'Peter is wounded' before that happens in the story",
     "verbatim": true
    }
   ],
   "against": "Teasers are allowed: \"no spoilers of events but teasers\" (feedback-aladdin-2026-08-25/feedback-text.txt:4).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 95,
   "verdict": "keep",
   "reason": "Quotes verbatim; a content review encoded as a criterion and a film plan's production boundary. Adds to truth 21.",
   "statement": "Media about a text must be accurate about it, with no character labels or general claims the text doesn't support.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "109",
     "quote": "Videos must be factually accurate about the text; Aladdin, Peter Pan and Toad are NOT heroes and must not be called that",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md",
     "lines": "79",
     "quote": "No hero/villain labels. No children flying out, parental decision or ending. Do not narrate the assessed London/Neverland mood words or complete their inference for the learner.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 96,
   "verdict": "keep",
   "reason": "Quotes verbatim; a draft film plan checked against the installed film contract.",
   "statement": "Change a video and everything tied to it together, including its checks, captions and transcript, and keep checks in the lesson rather than burned into the video.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md",
     "lines": "58",
     "quote": "Replacing only its MP4 would leave that check and the five short transcript segments mismatched.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md",
     "lines": "53",
     "quote": "Pauses, response UI and feedback belong to the app, not burned into the MP4.",
     "verbatim": true
    }
   ],
   "against": "The plan is a draft: \"Original adaptation draft, pending reconciliation with the academics' reviewed ReadVenture Peter Pan script.\" (same file:7).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 97,
   "verdict": "keep",
   "reason": "Quotes verbatim; production rules drawn from comments on a reference film, in a draft plan. Adds to truths 21 and 26.",
   "statement": "In explanatory media show one main visual action at a time with the spoken concept and its referent together, add no decorative or invented on-screen text, and keep characters identical across shots.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md",
     "lines": "81",
     "quote": "One main visual action at a time. Spoken concepts and their referents appear together. Avoid eye-catching background motion during explanations.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md",
     "lines": "72",
     "quote": "No decorative lists, invented text or unspoken recap on notebook pages",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md",
     "lines": "69",
     "quote": "Lock cast sheets, scale, wardrobe, props and room geography",
     "verbatim": true
    }
   ],
   "against": "The plan is a draft pending reconciliation with a reviewed script (same file:7).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 98,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 'Learners who spot fake AI disengage' was a stated concern, not a measurement, and the flips came with tightened criteria between runs; statement corrected, and the discrimination result and reliability line added. Adds to truths 22 and 34.",
   "statement": "Generated pictures of people should not look machine-made (the stated concern: a student who calls a film 'fake AI' skips it); before trusting a check for this, show it separates such frames from drawn art, and take several independent reads on near-photoreal faces, because single reads flipped.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
     "lines": "4",
     "quote": "I never want a student to declare 'Fake AI video'",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
     "lines": "42",
     "quote": "Runs 1 and 2 disagreed on vf07 (FAIL → note), vf08 (note → FAIL) and vf10 (note → FAIL)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
     "lines": "44",
     "quote": "Single-read verdicts on near-photoreal humans are therefore not reliable",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
     "lines": "45",
     "quote": "now requires three independent reads with majority rule on film frames and near-photoreal humans.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
     "lines": "58-59",
     "quote": "The only FAIL is a film frame; every drawn-children image is a clean PASS on every read.",
     "verbatim": true
    }
   ],
   "against": "The two disagreeing runs used different criteria: \"the same images, criteria differing only by the tightening\" (same file:42-43); and \"its threshold is provisional\" pending a person's check (same file:72).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 99,
   "verdict": "keep",
   "reason": "Quotes verbatim (the second on line 70).",
   "statement": "Confirm any visual flag on the full-size, settled frame before filing it, because thumbnails, mid-animation frames and the checking tool's own scrolling produced false defects.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21.md",
     "lines": "48",
     "quote": "Not defects (each re-read at full size; do not re-raise):",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21.md",
     "lines": "70",
     "quote": "the background paragraph is there (thumbnail artifact)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/VISUAL-QA-2026-09-11.md",
     "lines": "93",
     "quote": "The jump was the harness's own scrolling.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 100,
   "verdict": "keep",
   "reason": "Quotes verbatim; a filing gate written after three false 'does nothing' claims.",
   "statement": "Before reporting that something does nothing, observe the whole page and wait out its designed timers.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "134",
     "quote": "three \"does nothing\" claims were feedback in the other column",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "13",
     "quote": "Wait out the designed timer",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 101,
   "verdict": "keep",
   "reason": "Quote verbatim; the checklist's filing gate.",
   "statement": "Before filing a defect, separate 'the specified step is wrong', which is a design question, from 'this instance is weak', which is a content defect.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "15",
     "quote": "a specified step is not a defect; keep \"the step is wrong\" apart from \"this instance is weak\"",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 102,
   "verdict": "keep",
   "reason": "Quotes verbatim (the second on line 30); three different checkers missed fields they never read. Adds to truth 38.",
   "statement": "A check covers only what it collects, so make every checker list what it read and treat anything outside its reach as unchecked.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "244",
     "quote": "MCQ-only collection missed narrated-text breaches twice",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/VISUAL-QA-2026-09-11.md",
     "lines": "30",
     "quote": "sees this because the path is derived at runtime, not authored (validate-audio-refs walks",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "139",
     "quote": "The audit script (audit.py) never reads think_aloud.states[].search / we_do.search fields at all",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 103,
   "verdict": "keep",
   "reason": "Quotes verbatim (the second also appears at line 407). Adds to truths 9 and 38.",
   "statement": "Confirm a cited check exists and actually ran before counting it; a check that was never built or never run is unverified, not passed.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "288",
     "quote": "claims \"the new verbatim-fidelity ratchet in course-renderer\" landed",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "525",
     "quote": "Do not ship \"v1 PASS\" on an unrun check.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 104,
   "verdict": "keep",
   "reason": "Quotes verbatim; three harness incidents. Adds to truth 9.",
   "statement": "Keep checking-tool failures apart from content failures; a missing judge, a crashed transcriber and a shared output folder each produced false content failures.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "230",
     "quote": "11 phantom FAILs cost a diagnosis round",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "84",
     "quote": "27 false positives cost a full pass to disprove",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
     "lines": "250",
     "quote": "a transcript finding and a dead process are no longer the same red",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 105,
   "verdict": "keep",
   "reason": "Quotes verbatim (the second on line 232). Adds to truths 24 and 46.",
   "statement": "Every check run must state which version and which learner-facing surface it checked.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
     "lines": "196",
     "quote": "Silence-by-design class (qa-must-converge): a check that cannot say what it",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
     "lines": "232",
     "quote": "this lane, baselines included, is therefore a read of the deprecated surface, not of the page the",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
     "lines": "86",
     "quote": "first capture run produced 30 near-byte-identical screenshots before this",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 106,
   "verdict": "keep",
   "reason": "Quotes verbatim.",
   "statement": "When the checking tool itself fails on the unchanged baseline, judge a change by the failures it adds over that baseline.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
     "lines": "135",
     "quote": "The L4 annotation slice adds ZERO failures over base (4 base-subset fails on the",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
     "lines": "60",
     "quote": "battery 10 fail vs staging 11 (strict subset)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 107,
   "verdict": "keep",
   "reason": "Quotes verbatim.",
   "statement": "A check that only compares counts invites rubber-stamping; make it list what was added or removed so people review names, not a number.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
     "lines": "81",
     "quote": "the assertion only asks \"does the count match\", never \"is the",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
     "lines": "84",
     "quote": "review is of names, not a number.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 108,
   "verdict": "keep",
   "reason": "Quotes verbatim. Adds to truth 63.",
   "statement": "Re-check every reported problem on the current version before fixing it, and apply feedback only to the course and lesson it was raised about.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "204",
     "quote": "2 ALREADY-FIXED, 2 NOT-REPRODUCIBLE on c056d3e",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-codex-visual-2026-09-07/REGISTER.md",
     "lines": "26",
     "quote": "Codex's reproductions ran before the chip-glue merge built.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "205",
     "quote": "a matching term found elsewhere (another course's accepted list, a sibling system) is DROPPED",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 109,
   "verdict": "keep",
   "reason": "Quotes verbatim; an audit's suggested distractor was a correct use, and a demanded spelling change was not supported by the dictionary.",
   "statement": "Check a suggested fix before applying it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md",
     "lines": "11",
     "quote": "NOT the report's own suggestion (a plant nursery is a CORRECT use of the word and cannot be a wrong option in \"uses the word correctly\")",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/L4-REVIEW-GAPS-2026-09-16.md",
     "lines": "98",
     "quote": "Merriam-Webster recognizes -ry as a form of -ery, so “must change to -ery” was unsupported.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 110,
   "verdict": "keep",
   "reason": "Quotes verbatim. Adds to truth 24.",
   "statement": "Re-derive every number in a report from its primary source at write time and state its denominator.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "211",
     "quote": "5 errors, all inherited; zero freshly-derived claims wrong",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "540",
     "quote": "The headline `/tmp/audit_compliance.json` is a `--limit` run (6 tests / 91 items), not the full course.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 111,
   "verdict": "keep",
   "reason": "Quotes verbatim; the second half overlaps truth 70, the first half (freeze one version per review) adds.",
   "statement": "Freeze one version for the length of a review, and hold everything else equal when comparing versions.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "200",
     "quote": "mid-flight main movement voided three internal rounds",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/compare-2026-09-22/ours-only.html",
     "lines": "31",
     "quote": "Both sides are the same staging commit 5d033ac1. The only difference is our work.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 112,
   "verdict": "keep",
   "reason": "Quotes verbatim. Adds to truth 34.",
   "statement": "Close a finding only by re-running the check that found it on the current version, and don't treat a later run that fails to reproduce a failure as a fix.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "213",
     "quote": "\"fixed in \\<commit\\>\" is not closure",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/book-driver/FINAL-CLAIM-AUDIT.md",
     "lines": "14",
     "quote": "trace04's natural 8.6-second end is nonreproduction, not a repair or acoustic acceptance",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/book-driver/ANNOTATION-AUDIO-DISPOSITION.md",
     "lines": "22",
     "quote": "No repeated run until green is justified.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 113,
   "verdict": "keep",
   "reason": "Quotes verbatim; swapped the roadmap quote for its mechanism line (the ledger half is a roadmap proposal). Adds to truth 38.",
   "statement": "Turn every defect a person finds into a class check that is shown to fire on the pre-fix content, sweep all content for that class, and keep a ledger of rejected lines so they cannot return.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "212",
     "quote": "Each human-found defect became a machine check the same cycle, born red",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md",
     "lines": "21",
     "quote": "L7 p3 vocab-form1 carried the same \", because …\" tell → fixed",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/AUTOMATED-CHECKS-ROADMAP-2026-08-31.md",
     "lines": "144-145",
     "quote": "fail if an exact or near-exact match reappears.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 114,
   "verdict": "keep",
   "reason": "Quotes verbatim (the second on line 56); 26 findings landed on green-gated lessons. Evidence for truths 44 and 46 but a distinct claim.",
   "statement": "A green gate is not a defect-free lesson; people found many issues on lessons whose gate was green, mostly ones visible only on the rendered page or in the language.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/AUTOMATED-CHECKS-ROADMAP-2026-08-31.md",
     "lines": "22",
     "quote": "**green at review time** (`ROUNDS.md` \"26 findings landed on lessons whose",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/AUTOMATED-CHECKS-ROADMAP-2026-08-31.md",
     "lines": "56",
     "quote": "JSON/JSX text**, and the findings that keep recurring are ones only visible",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 115,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (the first on line 160). 'Most defects appear only after a sequence of actions' overstated: 6 of 10 were sequence-only or non-visual. Statement corrected. Adds to truths 38 and 47.",
   "statement": "Many defects people report can't be judged from a static screenshot, because they need a sequence of actions or aren't visual (6 of 10 in one register); static captures can't certify a lesson, and a judge that passed a screen that never showed the defect proves nothing.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
     "lines": "160",
     "quote": "checkpoint-seeked capture this run did not take) and 6 are sequence-only or",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
     "lines": "181",
     "quote": "The judge passed a screen that never contained the defect's own UI, so this is NOT evidence the fix holds",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 116,
   "verdict": "keep",
   "reason": "Quotes verbatim; used the full sentence across lines 185-187. Near-duplicate of truth 37 (score a judged check on person-labelled cases); kept because it adds a by-hand stand-in that reported 3/3 against the real run's 0/3, and a fabrication stable across five calls (also truth 35).",
   "statement": "Measure a model judge by running it on known cases rather than estimating what it would say; its main failure was confident, repeatable fabrication.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
     "lines": "185-187",
     "quote": "This is the opposite of the first session's optimistic manual stand-in (which reported 3/3).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
     "lines": "180",
     "quote": "confirmed STABLE across 5 independent calls",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
     "lines": "311",
     "quote": "is not incompleteness, it is confident wrongness",
     "verbatim": true
    }
   ],
   "against": "It still surfaced new real findings: \"It DID surface two plausible genuine findings\" (same file:319).",
   "general": true,
   "duplicate_of": "37",
   "name_bearing_source": false
  },
  {
   "index": 117,
   "verdict": "keep",
   "reason": "Quotes verbatim (the second on line 218). Adds to truth 45.",
   "statement": "If a judged question fails most items because of a deliberate design, rewrite the question before using it as a gate.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
     "lines": "203",
     "quote": "**`task-dominance`: 24/30 pages fail**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
     "lines": "218",
     "quote": "layout choice has low information value as currently worded",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 118,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (10 of 18 missed; the run's result was 8 passed, 10 failed). Reworded to avoid naming a role. Adds to truths 37, 38 and 45.",
   "statement": "Have a check's test cases written independently of whoever built the check, with the expected outcomes fixed before the first measurement.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/experience-2026-09-14/RESULT.md",
     "lines": "29",
     "quote": "The original visibility implementation passed its 48 controls but missed 10 of 18 independently authored cases.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/experience-2026-09-14/independent-observer/REVIEW.md",
     "lines": "7",
     "quote": "Eighteen fixture expectations were fixed in the independent script and written into `run-01/INTENT.json` before the first measurement.",
     "verbatim": true
    }
   ],
   "against": "Independence was not enforced: \"These were independently authored withheld cases on a shared writable machine, not a security-enforced judge boundary.\" (codex-qa/experience-2026-09-14/independent-observer/REVIEW.md:9).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 119,
   "verdict": "keep",
   "reason": "Quotes verbatim (the first on line 10); added the duplicate-case and timeout tests the statement names. The tests prove the evidence accounting, not that observations are true. Adds to truth 9.",
   "statement": "Count only what a check actually observed: empty observations, duplicate cases and timeouts are incomplete rather than passes, and a verdict carries every unverified part with it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/harness-2026-09-14.txt",
     "lines": "10",
     "quote": "test_empty_observations_are_not_success",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/harness-2026-09-14.txt",
     "lines": "9",
     "quote": "test_duplicate_cases_are_not_coverage",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/harness-2026-09-14.txt",
     "lines": "21",
     "quote": "test_timeout_is_incomplete",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "44",
     "quote": "Therefore the verdict is **\"PASS-with-Caliper-unverified\"**, NEVER a bare \"PASS\".",
     "verbatim": true
    }
   ],
   "against": "The controls are synthetic: the gate checks case ids and nonblank evidence, not whether the evidence is a genuine measurement (codex-qa/tool-reuse-assessment-2026-09-14.md:103-104).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 120,
   "verdict": "keep",
   "reason": "Quotes verbatim. Adds to truths 43 and 66.",
   "statement": "Keep the judge, the acceptance cases and the evidence out of reach of whatever writes the fix; a second agent with write access to the same files is not independent.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/controller-2026-09-14/PLAN.md",
     "lines": "30",
     "quote": "Tier 1: independent acceptance files must be outside the worker's enforced writable boundary.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/tool-reuse-assessment-2026-09-14.md",
     "lines": "105",
     "quote": "Hashes are not protection against a writer who can alter both result and evidence consistently.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 121,
   "verdict": "keep",
   "reason": "Quotes verbatim. Adds to truth 70.",
   "statement": "Replace a checking method only after a trial on the same frozen cases shows no new misses or false alarms and a measured gain; being newer is not evidence.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/tool-reuse-assessment-2026-09-14.md",
     "lines": "42",
     "quote": "Tier 1: current requirements and immutable original evidence govern; timestamps and test totals cannot establish superiority.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/tool-reuse-assessment-2026-09-14.md",
     "lines": "95",
     "quote": "No additional misses or false alarms on protected cases, no lost obligations, and a measured benefit on the declared target are needed for replacement. Do not accept a faster probe that silently stops exercising hard cases.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 122,
   "verdict": "keep",
   "reason": "Quotes verbatim. Adds to truth 48.",
   "statement": "A problem's absence from a later review doesn't show it was fixed, because reviews with different builds and scope can't be compared.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/experience-2026-09-14/RESULT.md",
     "lines": "53",
     "quote": "Reported repeated classes trigger detector inspection, but absence from a later report cannot establish a fix or a declining rate.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/experience-2026-09-14/recurrence/CLASSIFICATION-REVIEW-v3.md",
     "lines": "233",
     "quote": "Round coverage is incomparable. Absence of a class is not resolved, retested or improved.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 123,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 'Developer-speak' names a job role and was replaced. The count holds: the procedure-language class recurs in four later sections, more than any other class in the table.",
   "statement": "Keep internal procedure names, app jargon and generic assistant phrasing out of learner-facing text, and check for them as their own class: across seven review records this was the complaint class raised again most often.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/experience-2026-09-14/recurrence/CLASSIFICATION-REVIEW-v3.md",
     "lines": "21",
     "quote": "| aladdin-followup | 2 | — | procedure_language |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/experience-2026-09-14/recurrence/CLASSIFICATION-REVIEW-v3.md",
     "lines": "34",
     "quote": "| eight-gaps | 5 | hint_disclosure | magic_word_use, morphology_accuracy, procedure_language |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "67",
     "quote": "Zero instances of generic-assistant phrasing that reads as \"every AI app\"",
     "verbatim": true
    }
   ],
   "against": "The gauge itself warns that sections are not comparable (CLASSIFICATION-REVIEW-v3.md:5).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 124,
   "verdict": "keep",
   "reason": "Quotes verbatim.",
   "statement": "Keep a recorded order of authority among design sources and log every divergence: a lesson-specific design over a generic one, a dated ruling over an undated principle, a later ruling over an earlier one.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "296",
     "quote": "a dated ruling beats an undated principle; a later ruling beats an earlier one",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "91",
     "quote": "promoted 2026-08-25 after L4 was built a tier too general",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 125,
   "verdict": "keep",
   "reason": "Quotes verbatim; added the baseline's own line on recency and confidence, which the second clause needed.",
   "statement": "Classify incoming feedback before acting on it as a demonstrated defect, a compatible refinement, a change of direction or insufficient evidence, and don't let recency or confidence alone override an earlier decision.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/DECISION-BASELINE.md",
     "lines": "17",
     "quote": "| Demonstrated defect | A factual/content error or observed malfunction with a clear expected behavior, consistent with the agreed approach.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/VERIFICATION-PROPOSALS.md",
     "lines": "24",
     "quote": "do not alternate between competing standards without recording which one governs",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/DECISION-BASELINE.md",
     "lines": "9",
     "quote": "Recency, reviewer confidence and the number of citations do not automatically supersede an earlier academic decision.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 126,
   "verdict": "keep",
   "reason": "Quotes verbatim.",
   "statement": "Record what people explicitly liked about a lesson as protected criteria so later changes don't remove it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "122",
     "quote": "The answer-becomes-dialogue-with-Scout pattern on wrong answers is explicitly liked — do not remove in any redesign",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-aladdin-2026-08-25/REGISTER.md",
     "lines": "72",
     "quote": "recorded so nobody \"fixes\" it away (no-churn)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 127,
   "verdict": "keep",
   "reason": "Quotes verbatim. Distinct from truth 48 (learning): this is design quality versus fidelity. Adds to truths 44 and 48.",
   "statement": "Fidelity checks show a lesson matches its design, not that the design teaches well.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/CONTRACT-v0-2026-08-31.md",
     "lines": "223",
     "quote": "A perfectly-transferred bad design passes every gate.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/PRIOR-curriculum-verification-2026-09-10.md",
     "lines": "3",
     "quote": "do not replace student text, regenerate media, or claim curricular approval from source equality or passing technical tests",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 128,
   "verdict": "keep",
   "reason": "Quotes verbatim. Adds to truth 44.",
   "statement": "Every audit should say what it did not check, because closed-world checks only check what they were told to.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/CONTRACT-v0-2026-08-31.md",
     "lines": "288",
     "quote": "six green audits failed a real review because none of them asked",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/CRITIC.md",
     "lines": "7",
     "quote": "Why: what the child sees ≠ what the file holds.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 129,
   "verdict": "keep",
   "reason": "Quotes verbatim.",
   "statement": "State how each claim was verified (walked by a person, full census, single probe, code test or still open) and never word it more strongly than that basis.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/RULES.md",
     "lines": "4",
     "quote": "**Confidence tags:** `[LIVE]` walked in the student app myself · `[CENSUS]` exhaustive",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "30",
     "quote": "state non-leakage as \"grep-verified per item,\" not \"machine-proven.\"",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 130,
   "verdict": "keep",
   "reason": "AP-related, checked deep. Quotes verbatim (the first spans 152-153). Added the harness's own search-yield line and the knowledge-base entry the facts sheet corrects, which states the '99%' and '28%' readings the same way. Adds to truth 65.",
   "statement": "Report generate-and-filter yields as the yield of a search, not as what the generator does in one try, and trace any headline score to its source before believing it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/GENERATOR.md",
     "lines": "152-153",
     "quote": "But it is **NOT a K=1 single-model claim.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/GENERATOR.md",
     "lines": "154",
     "quote": "they are the yield of a search-plus-filter loop.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "55",
     "quote": "the \"99%\" was **cache + best-of-N**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "56",
     "quote": "(not the model generating); the \"28%\" was **four harness bugs**.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "36",
     "quote": "- The **\"28%\" was four eval-harness bugs** — weeks burned on a measurement artifact, not a model failure.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 131,
   "verdict": "keep",
   "reason": "AP-related, checked deep. Quotes verbatim; the knowledge-base entry records the same refutation. The facts sheet also calls the '28%' figure a harness artifact (line 56), so the binding-grader number itself is shaky; the refutation rests on the jump existing only under the discredited judge. Adds to truths 35 and 44.",
   "statement": "Confirm an improvement with the grader of record, and watch for 'fixes' that only dodge the check, because a gain measured under one judge vanished under the binding grader.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "52",
     "quote": "aptraining's \"real passages = 0.29→0.95 lever\" is **REFUTED**: that jump existed only under a discredited",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "53",
     "quote": "Gemini judge; on the binding grader it collapsed to 28% (DBQ 0%, MCQ_SET 0%, \"Gemini-judge artifact\"). The",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "54",
     "quote": "actual MCQ fix was the OPPOSITE — *removing* the stimulus so the grader's leak-probe is skipped (grader-gaming).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "24-25",
     "quote": "That **0.29→0.95** jump existed only under a **discredited Gemini judge**. On the **binding grader** it **collapsed to ~28%** (DBQ 0%, MCQ_SET 0%) and was logged as a **\"Gemini-judge artifact.\"**",
     "verbatim": true
    }
   ],
   "against": "The underlying lever survived in a narrower form: \"anti-leak/answerability is a real, construct-general item-quality lever\" (same file:58).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 132,
   "verdict": "keep",
   "reason": "AP-related, checked deep. Quote verbatim; the knowledge-base entry adds the explicit consequence. Related to truth 35 but about cross-project replication, not a judge's samples.",
   "statement": "Agreement between two teams counts as replication only if they worked independently.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "57",
     "quote": "The \"two teams converged\" is **WEAK** — it's one author importing AP findings onto grade-3, not independent replication.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "30-31",
     "quote": "not two teams replicating independently. Treat it as a hypothesis-transfer, not a cross-validated law.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 133,
   "verdict": "keep",
   "reason": "Quotes verbatim. Adds to truth 63.",
   "statement": "Generators drift toward their usual grade and plausible-looking standard tags, so enforce the grade band and check each tag against the text and skill outside the generator.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/LLM_GENERATION_BOUNDARY.md",
     "lines": "38",
     "quote": "Told \"G5,\" generate-agents produced 17/20 items at RI.3.x (prior-pull)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "147",
     "quote": "(literary tag on a purely informational creature passage)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 134,
   "verdict": "keep",
   "reason": "Quotes verbatim (the second on line 45). Adds to truths 9 and 63.",
   "statement": "Tag content metadata only where the delivered content still matches the source, since tags copied from a stale snapshot are fabrication.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/SUMMARY_AGENT_G5.qmd",
     "lines": "39",
     "quote": "each Unit-2 item was tagged **only where the live passage still",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/SUMMARY_AGENT_G5.qmd",
     "lines": "45",
     "quote": "from the stale snapshot would be fabrication, so they stay uncoded and named.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 135,
   "verdict": "keep",
   "reason": "Quote verbatim; the same row supplies a cited norm table in place of the drifted anchors. Adds to truth 57.",
   "statement": "Take reference values such as test norms from a cited table, never from a model's memory.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/TI_COURSEPLANS_PR_PROPOSAL.md",
     "lines": "18",
     "quote": "RIT meaning free-floats on pre-training (wrong 200-210 / 208/214 anchors)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 136,
   "verdict": "keep",
   "reason": "Quotes verbatim. Adds to truth 48.",
   "statement": "A predicted learning outcome must carry its status as a prediction in the data itself, and a proxy test is never reported on the real test's scale.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/TI_COURSEPLANS_PR_PROPOSAL.md",
     "lines": "19",
     "quote": "is a **naked number** — no field carrying \"model PREDICTION, not measured outcome; no in-cohort pilot validated this; not proven growth\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/V2_MONSTER_DOSSIER.md",
     "lines": "107",
     "quote": "**A proxy stays a proxy.**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 137,
   "verdict": "keep",
   "reason": "Quotes verbatim. Adds to truths 51 and 70.",
   "statement": "Report completion gains only paired with the same learners' accuracy on unseen items, and take a baseline before changing anything.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/V2_MONSTER_DOSSIER.md",
     "lines": "109",
     "quote": "completion-up-while-construct-accuracy-flat is the named failure, not a win.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/V2_MONSTER_DOSSIER.md",
     "lines": "148",
     "quote": "Ranking the thing-being-measured above the measurement is the classic optimize-before-instrument error.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 138,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (the first on line 44). 'Expanding intervals' is not in the source, which faults a single static pass with no scheduler; statement corrected. Design rationale, not measured.",
   "statement": "Mix practice across skills so learners must choose which schema applies, and schedule spaced reviews instead of a single review pass.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/WHY_V2_WINS.md",
     "lines": "44",
     "quote": "so the student must *discriminate* schemas, not pattern-match one per lesson",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/KB_FURTHER_IMPROVEMENTS.md",
     "lines": "75",
     "quote": "kb-0027 names this as cramming, not distributed practice",
     "verbatim": true
    }
   ],
   "against": "The outcome effect is unmeasured: \"MAP **0/313** → no RIT, no \"proven growth.\"\" (alpha-read-packager/FACTS_SHEET.md:48).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 139,
   "verdict": "keep",
   "reason": "Quotes verbatim. Adds to truth 23.",
   "statement": "Present text excerpts in their original order, because reordering can make a line seem to belong to the wrong speaker or event.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "81",
     "quote": "Tap list is out of story order",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/BUILD-SPEC-batch.md",
     "lines": "180",
     "quote": "STORY-ORDER (validate-passage-refs.mjs)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 140,
   "verdict": "keep",
   "reason": "Quote verbatim. Adds to truth 16.",
   "statement": "Locate a quoted span by where the whole quote occurs, not by matching a fragment, because short fragments recur elsewhere in a text.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/VISUAL-QA-2026-09-11.md",
     "lines": "34",
     "quote": "so the candidate `\"So these are Peter Pan's precious friends,\" he said.` also lit the `he said.` fragment of the unrelated `\"Hook,\" he said.` a whole part earlier",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 141,
   "verdict": "keep",
   "reason": "Quotes verbatim. Adds to truth 46.",
   "statement": "Check content at its extremes (longest word, option and sentence, most options) on phone, tablet and desktop widths.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "113",
     "quote": "Longest word, longest option, longest sentence, max option count render clean at 1280 AND 390",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-codex-visual-2026-09-07/REGISTER.md",
     "lines": "14",
     "quote": "Class rule: battery is desktop-only; all three classes invisible to it",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 142,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Replaced 'reviewer switches' (a role) with review-mode switches. Adds to truths 28 and 46.",
   "statement": "Keep adult controls and metadata (timers, counters, build strings, skip or review-mode switches) off the learner's screen.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "181",
     "quote": "if it stays, every gate is one tap from skippable",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-argus-ui-2026-09-30/REGISTER.md",
     "lines": "11",
     "quote": "every gate opens (`nextLive = !locked \\|\\| reviewer`)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 143,
   "verdict": "keep",
   "reason": "Quotes verbatim (the second on line 369). Adds to truth 39.",
   "statement": "Log raw learner events rather than model-derived scores, and keep analysis separate, so the record doesn't change when a model does.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/TELEMETRY-SCHEMA-v0-2026-08-31.md",
     "lines": "365",
     "quote": "- **No inference fields computed and stored ahead of need**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/TELEMETRY-SCHEMA-v0-2026-08-31.md",
     "lines": "369",
     "quote": "disagree with itself the day the model changes",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 144,
   "verdict": "keep",
   "reason": "Quotes verbatim. Adds to truth 12.",
   "statement": "Test anti-copying guards against the answer you actually want, since an exact recall of a long target sentence was flagged as echoing; keep recall targets short.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/REGISTER.md",
     "lines": "128",
     "quote": "a Name-it/recall sentence longer than ~66 normalized chars is ≥0.70 of its own criterion line",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/REGISTER.md",
     "lines": "128",
     "quote": "an exact recall is demoted (\"page's own words\")",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 145,
   "verdict": "keep",
   "reason": "Quotes verbatim.",
   "statement": "When a change alters what learners are handed, judge whether it is better or worse for them before updating a test's expectation, and never edit an expected answer just to make a check pass.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/pr263-merge/RED-REGISTER.md",
     "lines": "13",
     "quote": "because each had to be adjudicated as better-or-worse before the test was retargeted",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/PLAN.md",
     "lines": "68",
     "quote": "do not edit an expected answer merely to produce green",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 146,
   "verdict": "keep-with-fix",
   "reason": "Quote verbatim. One observation, from an AI reviewer; restricted to reviewing agents because a marker of students' answers should see exactly what the student sees (truth 30).",
   "statement": "Give a reviewing agent the lesson's underlying data as well as the rendered page: one AI review withdrew two of its four findings once it had the data.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/REGISTER.md",
     "lines": "28",
     "quote": "It withdrew two of its four findings once it had the node data.",
     "verbatim": true
    }
   ],
   "against": "A single observation; for markers of student answers, truth 30 (give a judge exactly what the student sees) still governs.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 147,
   "verdict": "keep",
   "reason": "Quotes verbatim.",
   "statement": "Hold a lesson's load steady: count every moment that asks for a response against a budget and pair any addition with a deletion.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "57",
     "quote": "\\~31 is the proven target, \\~55 the documented breach",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "125",
     "quote": "Under the conservation rule an addition that stays pairs with a deletion",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/CRITIC.md",
     "lines": "11",
     "quote": "the audit found 11 added pages with no design basis in L4 alone, so the 25-min envelope is likely blown but unmeasured",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 148,
   "verdict": "keep",
   "reason": "Quote verbatim; a blocking checklist row whose verifier path is noted as unconfirmed.",
   "statement": "Write instructions and guide lines at an easier reading level than the text being taught.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "64",
     "quote": "instructional/Scout lines BELOW the passage band",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 149,
   "verdict": "keep",
   "reason": "Quote verbatim. A review-profile criterion; a blocking checklist row requires every passage slice inside the teaching band, so the two conflict and the rule stays contested.",
   "statement": "A text may sit above learners' independent reading level when it is read aloud to them.",
   "kind": "adopted rule (contested)",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-C-D7-D8-D10-D12.md",
     "lines": "31",
     "quote": "D8.20 permits above-band text at listening-comprehension level; all passages carry full voiceovers.",
     "verbatim": true
    }
   ],
   "against": "A checklist requires \"Every passage slice inside the teaching band\" (AlphaRead-QC-Checklist-v2-2026-09-04.md:64).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 150,
   "verdict": "keep",
   "reason": "Quotes verbatim; a ruling on an external audit's finding, which had criticised the literal-only checks. Adds to truth 40.",
   "statement": "Checks during the first read stay literal until the inference skill has been modelled, because independent inference before the model breaks the gradual release.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md",
     "lines": "26",
     "quote": "an independent inference item there would break the gradual-release order",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21.md",
     "lines": "27",
     "quote": "The retrieval-only reading checks (L4–L7 p6–p12)",
     "verbatim": true
    }
   ],
   "against": "An external audit criticised all-literal reading checks: \"\\\"Reasoning happens, but the method never lets go of the student's hand\\\"\" (feedback-inceptbench-2026-09-18/REGISTER.md:12); the rule was kept by a ruling.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 151,
   "verdict": "keep",
   "reason": "Quote verbatim; recorded as an open question awaiting a ruling. Adds to truth 18.",
   "statement": "Should a lesson's closing questions require learners to use the taught word, or only the concept language?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/REGISTER.md",
     "lines": "60",
     "quote": "does the closing sequence have to make the child USE THE TAUGHT WORD, or is the reading-goal concept language the only target?",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 152,
   "verdict": "keep",
   "reason": "Quotes verbatim; the policy is held pending a decision. Adds to truth 10.",
   "statement": "How should spelling count in comprehension answers, by task type and for typed versus spoken input?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/REGISTER.md",
     "lines": "17",
     "quote": "Misspelled answer marked correct (\"magician\")",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/VERIFICATION-PROPOSALS.md",
     "lines": "16",
     "quote": "The spelling policy: what earns comprehension credit, when spelling is separately corrected, and how typed versus transcribed answers differ.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 153,
   "verdict": "keep",
   "reason": "Quote verbatim; a routed recommendation with no mechanism yet.",
   "statement": "How can learners be made to commit to the model's reasoning before it is revealed without timers, locked buttons or yes/no gates?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/REGISTER.md",
     "lines": "29",
     "quote": "Explicit anti-patterns named: no timers, no disabled Next, no yes/no gates.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 154,
   "verdict": "keep",
   "reason": "Quote verbatim; a recorded push-back against a request for one storyline, so the question stays open. Knowledge-building.",
   "statement": "Is knowledge better built through one continuous storyline across lessons or through topic-coherent sets of texts?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "201",
     "quote": "Knowledge-first ≠ a single forced storyline; topic-coherent passage sets are the better unit",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 155,
   "verdict": "keep",
   "reason": "Quotes verbatim; added the line saying which goal makes the trade acceptable. The rebuilt form's background-knowledge risk is a flag, not a blind-solve result. Knowledge-building. Adds to truth 5.",
   "statement": "On a familiar topic, items that match their passage can still be answered from background knowledge, while making the text rule out the obvious answers weakens the distractors once read, so decide which goal each item serves.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "313",
     "quote": "items become **blind-solvable from background knowledge** — all 5 carry `blind_solvable_risk=HIGH`",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "314",
     "quote": "This is the coherence↔leak tension",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "96",
     "quote": "The quality screen flagged this on **14 of 26** items",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "99",
     "quote": "for MAP-style *ability discrimination* it is a noted limitation.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 156,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Knowledge-building, read in full: for a course meant to teach real knowledge, 'something a student cannot already know' must not mean false facts; added the blind-solve report's fix path and the unit's fiction-vehicle rule, which keep world claims true while items hinge on invented particulars. Adds to truth 5.",
   "statement": "To make items need the text on a familiar topic, change the passage rather than the distractors: give it particulars a student of the topic cannot already know, such as invented people, places, events and quantities that carry true world knowledge.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/PASSAGE_DESIGN_RULES.md",
     "lines": "5",
     "quote": "The fix is not to write harder distractors; it is to write passages that carry information the student cannot have encountered before opening this specific text.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/PASSAGE_DESIGN_RULES.md",
     "lines": "11",
     "quote": "> If the answer is YES for any item, the passage is leaking. Do not patch the item — fix the passage first.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md",
     "lines": "45-46",
     "quote": "invented entities/quantities/relations, story-specific event order rather than canonical process order, passage-defined categories rather than natural-kind categories",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
     "lines": "100-101",
     "quote": "It carries the true cargo; it asserts nothing about the real world.",
     "verbatim": true
    }
   ],
   "against": "Text-dependence is not truth: \"it does NOT mean the passage's own facts are sourced or true\" (alpha-read-packager/generator/GENERATOR.md:160); and blocking curriculum topics (\"**Blocked domains (curriculum — leak risk):**\", alpha-read-packager/generator/g5/PASSAGE_GENERATOR.md:23) conflicts with a knowledge-building course's topics.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 157,
   "verdict": "keep",
   "reason": "Quotes verbatim; passage specification headers in a sandbox unit.",
   "statement": "Write each text with explicit layers: what it states, what it implies with support, and plausible neighbours it does not support, kept for wrong options.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/passage.md",
     "lines": "18",
     "quote": "- unsupported-plausible neighbors (for distractors; NOT in the text):",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/passages/kingfisher-bend-01.md",
     "lines": "10",
     "quote": "- layers: stated = photo figure",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 158,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The rubric shows two worked responses (one meets, one falls short), not one per level, and is a draft; the capstone gate's zero certified items concern the separate selected-response set, so that quote moved to against. Statement corrected. Adds to truths 56 and 59.",
   "statement": "Define the mastery performance on an unseen text with worked example answers, including one that falls short and why, and a whole-performance rubric on which every row must meet the bar.",
   "kind": "adopted rule (draft)",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/exemplars-rubric.md",
     "lines": "8",
     "quote": "the mastery performance; defined by exemplars + rubric, NOT decomposed further",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/exemplars-rubric.md",
     "lines": "10",
     "quote": "SHOWING two worked responses and a rubric that",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/exemplars-rubric.md",
     "lines": "103",
     "quote": "Score each row 1-4. \"Meets the capstone\" = every row at 3 or higher",
     "verbatim": true
    }
   ],
   "against": "The rubric is a draft: \"they are NOT an academics-approved scoring key.\" (demo-unit-2026-07-10/phase-e/capstone/exemplars-rubric.md:14-15); the separate selected-response capstone items all failed the anti-leak gate (\"certified\": 0, phase-e/capstone/gate-capstone-summary.json:13) and no capstone was published.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 159,
   "verdict": "keep",
   "reason": "Quotes verbatim. About authored acceptance sets, distinct from truth 13's judge-sure rule. Adds to truths 6 and 13.",
   "statement": "Accept every answer the text defensibly supports, and check that reveals and hints don't steer toward only one of them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "116",
     "quote": "Only one of two defensible actions is accepted",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "97",
     "quote": "the reveal and second_hint steer only toward Hook",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 160,
   "verdict": "keep",
   "reason": "Quotes verbatim (the first on line 105); the report also calls for a single-link redesign of chain items (line 128). Adds to truth 6.",
   "statement": "A 'what causes this?' question over a causal chain has several defensible answers, so ask about one named link.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "105",
     "quote": "defensible, and anti-leak keying the *non-proximate* link worsens it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/BUNDLE_CONTENT_BUGS.md",
     "lines": "53",
     "quote": "The passage is one continuous transitive causal chain",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 161,
   "verdict": "keep",
   "reason": "Quotes verbatim.",
   "statement": "Every reference from one step to another must match what is actually there.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "57",
     "quote": "whose hint says \"Use one of the words you locked in at Step 3\", a step that does not exist",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "98",
     "quote": "but the text describes the Hook task, not the Lost Boys model",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "115",
     "quote": "use \"Zoom in\", the retired step-name",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 162,
   "verdict": "keep",
   "reason": "Quotes verbatim; the dead-data validator is recorded as unbuilt. Adds to truth 30.",
   "statement": "Check that every authored element actually reaches the learner, because content no surface shows is dead data and a marking proof built from it is invisible to the learner.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "92",
     "quote": "A validator must FAIL an authored block sitting on a node type whose renderer never reads it (the 477-line dead hunt; the teacher_recap near-miss)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAP-CLOSURE-PLAN-2026-09-15.md",
     "lines": "57",
     "quote": "so that quote blank's proof is invisible to the child",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 163,
   "verdict": "keep",
   "reason": "Quote verbatim; the source concerns generating new renderer components against the engine contract, but the rule is general. Adds to truth 57.",
   "statement": "Quote the exact specification into a generator's instructions instead of paraphrasing it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "223",
     "quote": "Generation without quoting the contract caused the 17-divergence parity round",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 164,
   "verdict": "keep",
   "reason": "Quote verbatim. Near-duplicate of truth 24 ('leave a value empty until it is measured'); kept only for a second domain (run-usage logging).",
   "statement": "Record a missing measurement as missing, never as zero.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/controller-2026-09-14/PLAN.md",
     "lines": "42",
     "quote": "Usage omissions remain explicit, never fabricated zeros.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "24",
   "name_bearing_source": false
  },
  {
   "index": 165,
   "verdict": "keep",
   "reason": "Quotes verbatim; a controller stop rule and a regeneration round where repeating the same remedy raised the leak rate, after which a design change worked. Adds to truths 65 and 70.",
   "statement": "Stop after two identical fixes that didn't work and review the process instead of repeating the remedy.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/controller-2026-09-14/PLAN.md",
     "lines": "76",
     "quote": "stop earlier after two identical ineffective remedies",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "59",
     "quote": "| Round 2 | 32 | 26 | 6 | 0.812 | re-author R1 leakers — leak rate *rose* (hard residue) |",
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
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "72",
   "quote": "\"Good try, let's look again\" is a defect; passage visible whenever feedback says look back",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md",
   "lines": "17",
   "quote": "23 wrong-answer feedbacks explain without pointing back to the text",
   "ok": false
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/BUILD-SPEC-batch.md",
   "lines": "6",
   "quote": "a wrong-answer reply never names or paraphrases the key and never quotes six words of the correct option (validate-feedback)",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
   "lines": "88",
   "quote": "Wrong-answer feedback for option D points directly at the condition that identifies the key",
   "ok": true
  },
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
   "lines": "80",
   "quote": "guard added after L4 shipped a 3-clip model split",
   "ok": false
  },
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "83",
   "quote": "A clip that is hash-correct (audio\\_of green) but voice-wrong still FAILS this row",
   "ok": false
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-arc-continuity.md",
   "lines": "147",
   "quote": "the goal before the passage already knows the answer (\"gentle\") before watching the model",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
   "lines": "27",
   "quote": "| LENS1-01 | Gradual-release leak: l0/l1 teaching articles pre-answered their certified release checks (must-fix)",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-arc-continuity.md",
   "lines": "160",
   "quote": "to notice (how they feel/sound), without naming the mood answer",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/ROUND-RESULT.md",
   "lines": "14",
   "quote": "PP2 P066 prescribes the sentence; observation only",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
   "lines": "69",
   "quote": "Two attempts, then Scout gives it and the lesson moves on.",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
   "lines": "24",
   "quote": "Generic doc mandates 'two attempts, then reveal' on pauses; R-Q-20 fails any mcq authoring reveal_after_tries",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md",
   "lines": "138",
   "quote": "plain MCQ items use unlimited retry until correct, matching L4 pattern",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md",
   "lines": "150",
   "quote": "**Outlier: tap-the-clue (p15) has reveal_after_tries=7 vs 3 for all other items.**",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
   "lines": "58",
   "quote": "anti-leak/answerability is a real, construct-general item-quality lever",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md",
   "lines": "38",
   "quote": "**But self-containment ≠ passage-dependence.**",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/exemplars-rubric.md",
   "lines": "97",
   "quote": "answerable from prior knowledge, so it fails Transfer and Evidence precision at the root.",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "102",
   "quote": "6 practice items dropped after the screen credibly showed a **multi-defensible key** (verified by reading",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md",
   "lines": "258",
   "quote": "Either way the correct answer should be statable with a single-sentence verbatim pointer.",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
   "lines": "25",
   "quote": "the answer is stated in the just-read sentence",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
   "lines": "29",
   "quote": "The quoted **.30 control → .07 during-reading** result is Grade4 recall of **untargeted information**, not overall comprehension.",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md",
   "lines": "47",
   "quote": "L4's first round had 72.5% on one position",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
   "lines": "29",
   "quote": "| LENS1-03 | Key-position imbalance, 12/19 A with a 5-run (must-fix)",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-29/census-pp-L4-L7.txt",
   "lines": "6",
   "quote": "every blank's answer sits at option 0: [0, 0, 0]",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
   "lines": "119",
   "quote": "The word bank lists answers in the same order as the blanks",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/KB_FURTHER_IMPROVEMENTS.md",
   "lines": "117",
   "quote": "The correct fix is *re-keying Form A's static options*, not shuffling.",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/cert-layer/CONTRACT-v0-2026-08-31.md",
   "lines": "285",
   "quote": "wiring) is marked UNVERIFIABLE, not PASS.",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "151",
   "quote": "flagged not flipped, to avoid a confident",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
   "lines": "38",
   "quote": "Never certified on missing evidence",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
   "lines": "68",
   "quote": "Never string-match. Matching on “broken” passes “trust can never be broken,” which is the opposite of the answer.",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-B-D5-D6-D11-D13.md",
   "lines": "58",
   "quote": "\"never mark down for grammar, spelling, or shortness\"",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/VERIFICATION-PROPOSALS.md",
   "lines": "8",
   "quote": "Correctness must not collapse to keyword presence.",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "156",
   "quote": "Accent or hesitation never fails a child; type path always offered",
   "ok": true
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "132",
   "quote": "A silent/no-speech dictation makes ZERO /api/speak-score calls",
   "ok": false
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
   "lines": "31",
   "quote": "overwrites a correct open answer that differs from the authored one",
   "ok": true
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
   "lines": "116",
   "quote": "Only one of two defensible actions is accepted",
   "ok": true
  },
  {
   "truth": 14,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/cert-layer/TELEMETRY-SCHEMA-v0-2026-08-31.md",
   "lines": "352",
   "quote": "- **No raw typed text for selected-response items**, only a hash",
   "ok": false
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/KB_FURTHER_IMPROVEMENTS.md",
   "lines": "50",
   "quote": "90% of 2 is impossible",
   "ok": false
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "107",
   "quote": "(the 0.5 was small-sample noise)",
   "ok": false
  },
  {
   "truth": 16,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/VISUAL-QA-2026-09-11.md",
   "lines": "34",
   "quote": "so the candidate `\"So these are Peter Pan's precious friends,\" he said.` also lit the `he said.` fragment of the unrelated `\"Hook,\" he said.` a whole part earlier",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "58",
   "quote": "Quoted spans verbatim in the passage",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
   "lines": "87",
   "quote": "Nudge quotes words not in the story",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md",
   "lines": "57",
   "quote": "is a CONTRADICTION, not a fix",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/procedures/Example_Lesson_Components.txt",
   "lines": "9",
   "quote": "Exactly one high-leverage word is taught — chosen to unlock this text and to feed the Phase 3 inference.",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md",
   "lines": "44",
   "quote": "REVISE cannot swap payload words out",
   "ok": true
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "70",
   "quote": "Hard words in passages carry glossary affordance at first occurrence",
   "ok": true
  },
  {
   "truth": 20,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/procedures/Example_Lesson_Components.txt",
   "lines": "7",
   "quote": "A short background-knowledge video plays first, building the knowledge the text takes for granted.",
   "ok": true
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt",
   "lines": "4",
   "quote": "but you must show the image as you say the word and ideally they would see the word on screen and hear what it means",
   "ok": true
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md",
   "lines": "81",
   "quote": "One main visual action at a time. Spoken concepts and their referents appear together. Avoid eye-catching background motion during explanations.",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "180",
   "quote": "the model adds the mother unprompted, and once drew five children from a four-child cast",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/L4-REVIEW-GAPS-2026-09-16.md",
   "lines": "116",
   "quote": "Peter on the chimney with THREE legs",
   "ok": true
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "171",
   "quote": "slice boundaries never orphan a sentence mid-thought",
   "ok": true
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
   "lines": "77",
   "quote": "Narrative sentences are never cut down to hit a length number (Lexile-driven editing forbidden)",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
   "lines": "86",
   "quote": "### B5. Deploy verification proves bytes, not behavior — SOLID",
   "ok": false
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/SUMMARY_AGENT.qmd",
   "lines": "15",
   "quote": "never an agent's self-report and never an HTTP 200 (a PUT can return 200 yet silently revert)",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "259",
   "quote": "but because **nothing re-ran IB (or the deterministic coherence gate) on the assembled live form**",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/SUMMARY_AGENT.qmd",
   "lines": "111",
   "quote": "silent-no-op feedback writes**",
   "ok": true
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "100",
   "quote": "Ask appears in exactly one surface; Scout frames, never restates",
   "ok": true
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-argus-ui-2026-09-30/REGISTER.md",
   "lines": "23",
   "quote": "right/wrong never rest on colour alone",
   "ok": true
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "91",
   "quote": "Every page completable with sound off",
   "ok": false
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "157",
   "quote": "nothing essential rides on an entrance animation",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "127",
   "quote": "Clicking forward with no answer records no progress and no XP (leaked live twice)",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/FEEDBACK_RESPONSE.md",
   "lines": "94",
   "quote": "real accuracy by clicking through — the gate did not actually require reading.",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
   "lines": "135",
   "quote": "conflated): l0-l3 are now non-gating formative",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "129",
   "quote": "that first check activates and does not gate",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
   "lines": "57",
   "quote": "The replacement introduced a factual error.",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAP-CLOSURE-PLAN-2026-09-15.md",
   "lines": "57",
   "quote": "so that quote blank's proof is invisible to the child",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
   "lines": "259",
   "quote": "with the blank's own ask → band full, score 1",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
   "lines": "42",
   "quote": "Runs 1 and 2 disagreed on vf07 (FAIL → note), vf08 (note → FAIL) and vf10 (note → FAIL)",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "68",
   "quote": "Measured: ~22% flipped on the 2nd draw, 11.1% on the 3rd unified draw — it asymptotes but",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
   "lines": "83",
   "quote": "This run's praise misread. Again non-deterministic.",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
   "lines": "180",
   "quote": "confirmed STABLE across 5 independent calls",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/codex-qa/tool-reuse-assessment-2026-09-14.md",
   "lines": "67",
   "quote": "Completeness and consistency do not prove the truth of observations.",
   "ok": true
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "131",
   "quote": "Infra-failure way-outs (StuckWayOut) hand back the authored reveal",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
   "lines": "152",
   "quote": "so a one-word answer would have been refused",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
   "lines": "185",
   "quote": "**Recall on the ground-truth set: 0/3 evaluable-as-designed (0%).** This is",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/audio/RESULT.md",
   "lines": "10",
   "quote": "The original read of stdout silently yielded NaN and skipped the attack check.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/audio/RESULT.md",
   "lines": "11",
   "quote": "including an actual temporary weak-onset tone that the original tool incorrectly accepted",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/cert-layer/CONTRACT-v0-2026-08-31.md",
   "lines": "267",
   "quote": "- **Red-control or it didn't happen.**",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
   "lines": "7",
   "quote": "Purpose: prove the new check DISCRIMINATES",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
   "lines": "44",
   "quote": "Independent recompute `verify_gate.py`: VERIFY PASS -- every verdict, blind score, floor,",
   "ok": true
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
   "lines": "28",
   "quote": "All 14 article stimuli rebuilt: Get ready > The text > Watch me think > Your turn > Say it with evidence > Our river map",
   "ok": true
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md",
   "lines": "26",
   "quote": "an independent inference item there would break the gradual-release order",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-pp-2026-08-27/REGISTER.md",
   "lines": "10",
   "quote": "Cracked both usage checks via \"baby\"+\"sleep\"",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/eval-suite/RANKING.md",
   "lines": "16",
   "quote": "two-forms-same-job defect",
   "ok": true
  },
  {
   "truth": 42,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/codex-qa/harness-2026-09-14.txt",
   "lines": "3",
   "quote": "test_changed_acceptance_contract_invalidates_old_pass",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/GENERATOR.md",
   "lines": "123",
   "quote": "**Generator and grader are separate roles/contexts.** The grader must never receive the",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
   "lines": "13",
   "quote": "Machine verification is exhaustive on shape and silent on doability by a Grade-3",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/compare-2026-09-23/index.html",
   "lines": "122",
   "quote": "133 clips machine-checked, zero human listens",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21.md",
   "lines": "22",
   "quote": "whisper hears \"ant\" as \"and\"; does a child?",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/codex-qa/experience-2026-09-14/independent-observer/REVIEW.md",
   "lines": "7",
   "quote": "Eighteen fixture expectations were fixed in the independent script and written into `run-01/INTENT.json` before the first measurement.",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/RULES.md",
   "lines": "42",
   "quote": "and \"AlphaBuild shows it Valid\" do **not** mean it renders in reading — only a live student-app walk proves",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
   "lines": "232",
   "quote": "this lane, baselines included, is therefore a read of the deprecated surface, not of the page the",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
   "lines": "94",
   "quote": "static grep proved dishonest twice on 2026-08-25",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-argus-ui-2026-09-30/REGISTER.md",
   "lines": "31",
   "quote": "any shell change gets a rendered look (screenshot or computed layout of the control) before the PR, not only a markup assertion",
   "ok": true
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/INTERNAL-REVIEW-MESSAGE.md",
   "lines": "28",
   "quote": "This is not one uninterrupted journey on the final source.",
   "ok": false
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/annotation-and-walk/C3-DOCUMENTATION-REVIEW.md",
   "lines": "14",
   "quote": "No source presence or page Next state alone proves every subtask.",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/WHY_V2_WINS.md",
   "lines": "14",
   "quote": "practiced certifies *familiarity*, not reading ability",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "188",
   "quote": "Receipt claims completion/practice, never mastery",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/cert-layer/CONTRACT-v0-2026-08-31.md",
   "lines": "53",
   "quote": "\"this lesson will not waste a child's time or lie to them,\" not",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
   "lines": "48",
   "quote": "\"Is it adding value\" cannot improve past \"the design says so and the shape is coherent\"",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/WHY_V2_WINS.md",
   "lines": "12",
   "quote": "**The weakness is text structure** — compare/contrast 39%, cause/effect 42%, sequence 48% (vs 83% blended).",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
   "lines": "33",
   "quote": "The cold/transfer passages are **MACHINE-AUTHORED** (`humanApproved:false`), **NOT real / primary-source**.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/KB_FURTHER_IMPROVEMENTS.md",
   "lines": "87",
   "quote": "flip humanApproved:true ONLY on individually-reviewed items, stamped with provenance",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/audio/VOICE-IDENTITY-2026-09-16.md",
   "lines": "16",
   "quote": "i.e. the stamp's voice label is wrong",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/VERIFICATION-PROPOSALS.md",
   "lines": "11",
   "quote": "“Looks more animated” alone is not evidence of better teaching.",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
   "lines": "59",
   "quote": "A visual preference alone cannot establish comprehension gains.",
   "ok": true
  },
  {
   "truth": 52,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
   "lines": "21",
   "quote": "**Design conclusion:** avoid slow letter tracing that obstructs reading; chunked reveal is a reasonable prototype.",
   "ok": true
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "150",
   "quote": "Every video carries a VTT; captions toggle works",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/exemplars-rubric.md",
   "lines": "8",
   "quote": "the mastery performance; defined by exemplars + rubric, NOT decomposed further",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "223",
   "quote": "Generation without quoting the contract caused the 17-divergence parity round",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/TI_COURSEPLANS_PR_PROPOSAL.md",
   "lines": "18",
   "quote": "RIT meaning free-floats on pre-training (wrong 200-210 / 208/214 anchors)",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "217",
   "quote": "the exact class meeting #10 calls \"passes item evaluations but fails the holistic course",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "230",
   "quote": "aggregate first returned a false all-clear",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
   "lines": "22",
   "quote": "child's science text is a kill, not a footnote.",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/exemplars-rubric.md",
   "lines": "103",
   "quote": "Score each row 1-4. \"Meets the capstone\" = every row at 3 or higher",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
   "lines": "47",
   "quote": "POLISH (recorded, not acted on unless a line is untrue to the story)",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "102",
   "quote": "6 practice items dropped after the screen credibly showed a **multi-defensible key** (verified by reading",
   "ok": true
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
   "lines": "12",
   "quote": "Author inner-loop verdicts are recorded per claim; the QC lane owns",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
   "lines": "87",
   "quote": "shipped L10 is Anansi (wrong unit, wrong story, wrong skill)",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "423",
   "quote": "Lesson \"Who Ruled the Republic?\" but passage is about aqueduct water engineering.",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/BUNDLE_CONTENT_BUGS.md",
   "lines": "15",
   "quote": "unanswerable-needs-visual | asks how a picture/diagram helps; image not rendered |",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "418",
   "quote": "\"Look at the labeled diagram to see where they are!\" — no image, no CDN URL, no inline labels.",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "534",
   "quote": "Flagging diegetic mentions risks crying wolf.",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "59",
   "quote": "| Round 2 | 32 | 26 | 6 | 0.812 | re-author R1 leakers — leak rate *rose* (hard residue) |",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/RESULTS.md",
   "lines": "47",
   "quote": "**Independent acceptance: 8/9 = 89% strict-hold; #7 is a self-grade-generous borderline",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/LLM_GENERATION_BOUNDARY.md",
   "lines": "12",
   "quote": "**Catch deterministic structural tells** (longest-option, key-validity, identity-order) — it estimates, doesn't count",
   "ok": true
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "216",
   "quote": "items are unanswerable as rendered.**",
   "ok": true
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
   "lines": "258",
   "quote": "same word, via /api/speak-score: \"angry\" with the frame prompt → band off, score 0",
   "ok": false
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/compare-2026-09-22/ours-only.html",
   "lines": "31",
   "quote": "Both sides are the same staging commit 5d033ac1. The only difference is our work.",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
   "lines": "59",
   "quote": "choose one variable",
   "ok": true
  }
 ]
}
```
