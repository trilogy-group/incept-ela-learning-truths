# verify:kb-course-builds

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "kb-course-builds",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "All three quotes are verbatim at the cited lines. The found_by clause 'a course whose items all scored 1.0 was 90% blind-solvable' overstates. kb-0235 103-105 states that as the definition of a failed course and gives one item (IB 1.0, blind-solve 100%) as proof. No evidence covers 'structure and fit checks', so the statement is narrowed to the leak check. Added kb-0235 106-108. Overlaps 5 and 58 but adds that a general quality judge passes leaky items. General.",
   "statement": "A top score from a general quality judge does not show that an item needs its text: answer-leaking items scored 1.0. Run the leak check separately and let it block on its own.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
     "lines": "47",
     "quote": "**MAP-likeness review (separate from InceptBench, which graded answer-leaking items 1.0):**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "103-105",
     "quote": "a course where every item scores IB 1.0 but 90% is blind-solvable is a failed course (proof: DAPO epoch 0 emitted \"What is the primary function of chlorophyll?\" from a photosynthesis passage — IB 1.0, blind-solve 100%)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "68-69",
     "quote": "InceptBench grades *instructional* quality, **not** test-security — so it won't catch a leaky-stimulus gap; anti-leak must be enforced upstream.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "106-108",
     "quote": "The binding gate must stay **cross-family** (solver family != generator family); IB self-certification is not anti-leak evidence.",
     "verbatim": true
    }
   ],
   "against": "Limit, kb-0234 lines 30-31: \"a **CRITICAL veto** caps the score at 0.84 if any CRITICAL metric is 0\". The judge does veto on its own critical metrics; leak is just not one of them.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep",
   "reason": "Quotes verbatim. 'avg 0.14' and '65 of 76' match kb-0083 64. The baby+sleep pair cracked the checks on two forms, a cross-form tell (kb-0211 24). Added kb-0164 93-94 (form-level obligations) and kb-0234 39-40 (a defect that passes item evals but fails the holistic course eval). Overlaps 8, 41 and 68, but states the set-level principle that none of them does. General.",
   "statement": "Judge the whole set as well as each item: repeats, cross-item clues and answer patterns only show at set level, and items that pass one by one can fail together.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0083-clone-lessons-inceptbench-results-2026-07-02-eval-summary.qmd",
     "lines": "64",
     "quote": "Non-repetitiveness is by far the weakest dimension: **avg 0.14; 65 of 76 bundles scored exactly 0** on it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0076-coe-catchup-2026-06-30.qmd",
     "lines": "33",
     "quote": "G3 passed **individual item** evals but **NOT** the holistic **course-level** eval",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0211-peter-pan-reviewer-round-2708.qmd",
     "lines": "24",
     "quote": "Both usage checks were crackable via the single pair \"baby\"+\"sleep\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "93-94",
     "quote": "answer position, option length, distractor function, enemy items, blueprints, and independent cold review are form-level obligations;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "39-40",
     "quote": "the class of defect that \"passes item evals but fails the holistic course eval.\"",
     "verbatim": true
    }
   ],
   "against": "kb-0083 line 94: \"the 0.0s on multi-passage bundles say more about eval packaging than content.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "The kb-0235 quote spans lines 67-69, not 68-69. '20 (21%)' of 95 and '75 leaked' match. The kb-0096 quotes are verbatim, and lines 28-31 confirm the over-eager solver guessed from option-length and wording tells. Added kb-0096 69 (calibration matters more than which judge). Refines 5 and 37 with the point about solver strength. General.",
   "statement": "A solve check with the text hidden is only as good as its solver: calibrate the solver on known leaky and known clean items, because a weak solver passes leaky items and a bluffing solver flags clean ones.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "67-69",
     "quote": "of v1's 95 re-gated \"clean\" items, only **20 (21%) survived**; **75 leaked** under the strong solver.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd",
     "lines": "31",
     "quote": "it returned blind accuracy of `1.0` on items that genuinely needed the passage.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd",
     "lines": "70",
     "quote": "2. A solver that can bluff its way through without the passage will inflate leak rates.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd",
     "lines": "69",
     "quote": "1. Blind-solve calibration matters more than judge identity alone.",
     "verbatim": true
    }
   ],
   "against": "Limit, kb-0092 lines 25-27: real users include \"test-wise students, and students willing to click through or guess.\" A solver that never guesses can understate the risk.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The cited kb-0090 range 129-131 holds three rules, so the quote is extended to all three; that also covers the claim that the maker's own report counts for nothing. Added kb-0235 106-108 (the gate must be cross-family; self-certification is not anti-leak evidence). Overlaps 61 and 66, but this is the separate rule that the maker cannot certify its own output. General.",
   "statement": "Never let the process that made items certify them; a separate check, ideally from a different model family, must pass them, and the maker's own report of success counts for nothing.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "26",
     "quote": "The questions were good because the generator was not trusted.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0090-fable5-plan-traces-2026-07-09.qmd",
     "lines": "129-131",
     "quote": "- do not trust LLM self-report; - only gate outputs and read-back artifacts count; - a lane cannot certify its own items;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "231",
     "quote": "3. Use a different family for the gate than for the author. Never same-family certify.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "106-108",
     "quote": "The binding gate must stay **cross-family** (solver family != generator family); IB self-certification is not anti-leak evidence.",
     "verbatim": true
    }
   ],
   "against": "kb-0127 lines 85-86: \"Three-family judging was proposed, not approved, and no evidence was presented that it reduces evaluator flakiness.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep",
   "reason": "Quotes verbatim. The found_by '3/3' is confirmed at kb-0120 33 (0/3 plain-blind before, 3/3 under the current replay), and that line is added. Overlaps 42 (remake under new rules), but adds that a pass is tied to the checker version as well as to the content. '550' matches. General.",
   "statement": "A pass belongs to the exact content, rules and checker that produced it; after any change to any of them the earlier result is void until the checks run again.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "52-53",
     "quote": "its later invalidation by a stronger current plain-blind solver; stale solver results are not certification.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0134-g5-reading-v2-local-design-package.qmd",
     "lines": "168-170",
     "quote": "Any canonical, source, model-policy, renderer, validator, or package-contract change invalidates the relevant downstream evidence and requires a fresh rebuild.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
     "lines": "24",
     "quote": "All 550 forms remain candidates and the historical model snapshots are withdrawn after source changes.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "33",
     "quote": "Current Gemini 3.5 replay: 3/3 in both conditions - direct blind leak; old lift is historical.",
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
   "reason": "Quotes verbatim. '3/8' and '0.71875' match kb-0120 43-44 and kb-0126 29-30. Added kb-0120 59-60 (the model's confidence cannot cancel exact blind recoveries). The chance-floor limit in the against field is correct. No existing truth covers this; it sets a boundary on 9 when the solver is the one reporting doubt. General.",
   "statement": "Count repeated exact recoveries made with the text hidden as a leak even when the solver says it was guessing; low stated confidence must not cancel a correct blind answer.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "43-45",
     "quote": "Promotion review found `r3-09` at 3/8 exact plain-blind recovery and 0.71875 mean partial accuracy; the sealed rule had ignored those hits because the solver reported low confidence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0126-claude-takeover-audit-2026-07-13.qmd",
     "lines": "29-30",
     "quote": "`r3-09` was exactly solved blind in 3/8 shuffles and that low solver confidence had hidden those hits.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "59-60",
     "quote": "the later objective overlay showed why model self-confidence cannot erase exact blind recoveries.",
     "verbatim": true
    }
   ],
   "against": "Limit, kb-0089 lines 286-287: \"sounder leak signal became pair-mean over many shuffles above a higher margin or exact-match rate above the chance floor.\" Recoveries count only above chance.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. kb-0089 284 states the 0.50 chance floor for pair accuracy, so the found_by number holds. Nothing supports 'not against its format name', so that part is dropped. General.",
   "statement": "Set each pass or leak threshold against the chance score of the item as it is actually scored; a threshold too close to chance flags noise.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd",
     "lines": "284-285",
     "quote": "a 0.60 pair-accuracy threshold was too close to chance and flagged noise.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd",
     "lines": "284",
     "quote": "sequence pair-accuracy has a chance floor around 0.50.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "40-41",
     "quote": "PASS if with-passage correct-rate >= 0.80 AND without-passage correct-rate <= chance-rate + 0.15 margin",
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
   "reason": "Quotes verbatim. The kb-0164 filler sentence spans lines 104-105, not 104. 'twelve' and '50/50' match. Added kb-0172 51 (the four-option rule is no license for a weak fourth distractor) and kb-0081 130 (cap the number of options). The three-or-four dispute in the against field is real and stays open. General.",
   "statement": "Choose the number of options on purpose: two invite coin-flip guessing, a dozen overload the student, and filler options must never be added to reach a count.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "112",
     "quote": "MCQs need at least four options. A two-option yes/no item permits a 50/50 guess.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "128",
     "quote": "one hot-text item offered twelve selectable options, an excessive motor and cognitive load for an eight-year-old.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "104-105",
     "quote": "An agent must not resolve this by adding filler",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "51",
     "quote": "This is reviewer feedback, not a license to create a fourth weak distractor.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "130",
     "quote": "cap the number of selectable options.",
     "verbatim": true
    }
   ],
   "against": "kb-0164 lines 102-104: \"the MCQ BrainLift reports a research consensus favoring three and recommends four as Alpha's default only when all distractors remain plausible and diagnostically useful.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep",
   "reason": "Quotes verbatim. '626' is a deterministic grader's failure count (kb-0068 117). Added kb-0217 63, where 'correct answer never longest' is a contract gate in code. Overlaps 8 and 67, but covers tells from length and stem words rather than position. General.",
   "statement": "The right answer must not stand out by length, form or a distinctive word it shares with the question, and this should be checked in code when items are written.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0068-g5-static-dataset-intake-2026-06-23.qmd",
     "lines": "117",
     "quote": "longest-option-tell: 626",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "91-92",
     "quote": "STEM-LEAK (no distinctive content word may sit in both the stem and only the correct option)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "133",
     "quote": "Closed-response items must require the target reasoning and must not be answerable by surface cues, keyword matching, option length, or test-wise elimination.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "63",
     "quote": "MCQ correct answer never longest",
     "verbatim": true
    }
   ],
   "against": "Limit, kb-0096 lines 49-50: \"The audit says 10 MCQs were over-flagged under the old blind-solver and correctly certified after the re-baseline.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep",
   "reason": "Quotes verbatim. '192' matches kb-0235 133, a gap named in a static accessibility scan. The 638 'unused-right-bucket-exists' failures at kb-0068 116 are a real counter from one local grader. Applies to any matching item. General.",
   "statement": "In matching tasks give more targets than prompts and do not announce which one is spare, so the last pairing cannot be won by elimination.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0067-g5-generator-pilot-intake-and-team-async-2026-06-23.qmd",
     "lines": "314",
     "quote": "- add at least one unused/decoy right bucket to match items",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
     "lines": "66",
     "quote": "`match` is 3×3 (minor elimination cue)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "133",
     "quote": "192 match items announcing a decoy bucket",
     "verbatim": true
    }
   ],
   "against": "kb-0068 line 116 lists \"unused-right-bucket-exists: 638\" as a failure reason. One local grader treated a spare target as a defect.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep",
   "reason": "Quotes verbatim. 85/90 = 94% matches kb-0089 276, and line 270 says the solve was cross-family. Added kb-0217 66-67 (~78% of raw generated items were blind-solvable) and kb-0089 279 (redesign fails when the item encodes world knowledge or an obvious order). Refines 5. General.",
   "statement": "Build the need for the text into how items are constructed; raw generated items mostly leak, and recall or 'textbook-correct' items leak through general knowledge whatever their format.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd",
     "lines": "276",
     "quote": "85/90 exact blind-recovered = 94% leak under the strict sample.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd",
     "lines": "271",
     "quote": "- construction is the lever, not format alone.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "208",
     "quote": "- MCQ leaked through ordinary school knowledge, vocabulary, or a \"textbook correct\" option;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "66-67",
     "quote": "~78% of raw generated items were blind-solvable before this gate",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd",
     "lines": "279",
     "quote": "- Redesigning the wrong construction does not work if the item encodes world knowledge or obvious order.",
     "verbatim": true
    }
   ],
   "against": "kb-0091 lines 127-128: \"Lesson: anti-leak success alone is insufficient. Some items became mechanical ordering tasks or failed standard fit even after passing the blind gate.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep",
   "reason": "Quotes verbatim. '~0.8' matches kb-0236 119. Distinct from 5 because it moves the fix to the text itself. The limit in the against field fits. General.",
   "statement": "When most items on a text leak, change the text instead of repairing items; texts that restate widely known facts cannot carry questions that need the text.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "37-38",
     "quote": "regeneration was abandoned — the root cause is passage design (encyclopedic passages), not item quality.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
     "lines": "119-120",
     "quote": "cold-solvable ~0.8 because camel adaptations are world-famous general knowledge; distractor surgery can't close it, needs full content replacement",
     "verbatim": true
    }
   ],
   "against": "Limit, kb-0074 lines 42-43: \"**Reconciliation = role-separation: cold at the gate/test, topic-coherent during learning.**\" The rule holds for test texts.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep",
   "reason": "Quotes verbatim. The found_by phrase 'judged not to be a curriculum' is loose; kb-0081 68 calls this 'the deepest issue with the design', and that line is added. Related to 18 and 48 but not a duplicate. General.",
   "statement": "Keep learning texts and test texts apart: sequence learning texts so knowledge recurs and builds, keep unseen texts for tests, and keep what is scored separate from what was taught.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "70",
     "quote": "Sequence the learning texts so taught knowledge recurs and compounds, and reserve cold, non-overlapping passages for the test only, where that property belongs.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0074-g3-reviewer-feedback-distilled-for-g5-2026-06-30.qmd",
     "lines": "79-80",
     "quote": "The **scored `item_bank`/independent claims stay disjoint from that on-ramp and from every teaching claim**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "68",
     "quote": "by design ensures assessment passages never overlap taught topics so a student \"can't pass on recall.\"",
     "verbatim": true
    }
   ],
   "against": "kb-0098 lines 38-39: \"knowledge-building can be gamed if later questions become answerable from earlier lessons without proving true comprehension.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "keep",
   "reason": "Quotes verbatim. Overlaps 40, which is the lesson flow kb-0099 70 refers to, but adds that an item bank is not a course. General.",
   "statement": "A bank of good items is not a course; items count only inside a taught sequence that students can actually move through.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "118",
     "quote": "- Build a real curriculum, not a library of components or a standards-aligned item bank.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd",
     "lines": "70",
     "quote": "Strong questions do not become a course unless they sit inside this flow and the actual app proves students can experience it.",
     "verbatim": true
    }
   ],
   "against": "kb-0076 line 20: \"The reviewer **praised** the MAPS focus; it only \"fell short as a standalone teaching course.\"\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep",
   "reason": "Quotes verbatim. Added kb-0086 142 (the definition of gradual release) and kb-0180 31-32 (model the thinking, never just reveal a filled-in organiser). Spells out the stages of 40 rather than repeating it. General.",
   "statement": "In gradual release, the model shows the thinking rather than revealing the answer, the shared step leaves part of the answer for the student, and all three stages practise the same skill.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "60",
     "quote": "I-do reveals the answer instead of modeling thought; we-do is only a hint; you-do sometimes switches to a different skill.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "34-36",
     "quote": "the we-do gives a *partial* answer the child completes (a hint is not a we-do, a fresh question is not a we-do); I-do, we-do and you-do must run the *same skill*, never switch mid-lesson.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "142",
     "quote": "- Gradual release means model the thought process, let the student practice the same process with guidance, then release the same process to independent work.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "31-32",
     "quote": "the I-do must model *thinking* — why this detail and not that one, what was rejected and why — never just reveal a filled-in organiser.",
     "verbatim": true
    }
   ],
   "against": "Limit, kb-0204 line 326: \"A quick check at the start of guided practice lets confident students move straight on.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep-with-fix",
   "reason": "The kb-0180 quote spans lines 41-42, not 41. '5/2/1 → 3/2/3 → 1/2/5' matches kb-0174 72-73. Nothing supports 'not the calendar', so it is dropped. Added kb-0204 326 (a quick check lets confident students move on), which supports the skip clause. The researcher's name is trimmed from the kb-0204 quote. kb-0180 42-44 records that the five-use fade was never implemented. General.",
   "statement": "Fade support as the student succeeds with a skill (one rule collapses a procedure to two steps after five successful uses), and let students who show they already know the skill skip the full model.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd",
     "lines": "72-73",
     "quote": "exposure-based fade progression per skill (heavy model 5/2/1 → shift 3/2/3 → hand-over 1/2/5)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "41-42",
     "quote": "scaffolds fade across a unit (a procedure \"collapses into a two-step option after five successful uses,\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "284",
     "quote": "heavy guidance helps novices but slows down learners who already know the material.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "326",
     "quote": "A quick check at the start of guided practice lets confident students move straight on.",
     "verbatim": true
    }
   ],
   "against": "kb-0204 line 306: \"In review lessons (Profile D), guided practice grows again but changes form: worked examples and comparative judgement, rather than first-time modeling.\" Also kb-0180 lines 42-44: the five-use fade \"stayed unimplemented\" in the grade 3 build.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "keep",
   "reason": "Quotes verbatim. The kb-0172 quote leaves out the name that opens its sentence. Added kb-0180 37 and 38-39 (every screen requires a specific interaction; production counts over selection), which is the ruling the found_by describes. General.",
   "statement": "Every screen should ask for a response that matters to the teaching move, preferably one the student produces rather than clicks; passive or decorative-tap screens invite click-through.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "27",
     "quote": "passive listening or text-only screens invite click-through rather than attention. The interaction must be substantive to the teaching move; a decorative tap control does not satisfy the concern.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "86-87",
     "quote": "match the task family to the knowledge: recognition is not enough for productive, representational, justificatory, or integrative constructs;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "37",
     "quote": "every screen requires a specific interaction (no passive screens,",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "38-39",
     "quote": "judge a lesson by *production* (say/write/type) over *selection* (click)",
     "verbatim": true
    }
   ],
   "against": "Limit, kb-0081 line 108: \"Covering varied technology-enhanced item types is a real benefit and the clearest advantage over the incumbent\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 17,
   "verdict": "keep",
   "reason": "Quotes verbatim. 'about 20 percent', 'every question incorrectly' and 'all 18 ... zero answers given' match. Added kb-0081 122 (show the gate blocking a real miss in a live walkthrough). Overlaps 38 and 47, but names the three attacks to try. General.",
   "statement": "Try to beat every mastery gate yourself before claiming it works: click through without reading, answer everything wrong, and try to reach the end with no answers.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "120",
     "quote": "earned a stamp on \"The Amazing Axolotl\" at about 20 percent accuracy by clicking through without reading, then advanced with the passage hidden from view.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "101",
     "quote": "In a main-idea task, reviewers earned the pass while answering every question incorrectly.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0215-g5-media-recovery-plan-and-edullm-entrypoint-test.qmd",
     "lines": "85-87",
     "quote": "a real browser reached \"Great Work!\" across all 18 of U1·L3's scenes with **zero answers given**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "122",
     "quote": "demonstrate it blocking a real miss in a live walkthrough.",
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
   "reason": "Quotes verbatim. '90%' and '24-hour' match. Added kb-0058 37 (a threshold declared in metadata but not enforced). Overlaps 46, but this one is specifically about declared rules. General.",
   "statement": "A rule declared in metadata or documents is not enforced until the running product is shown to block on it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "92-93",
     "quote": "`masteryThreshold` was `null` on both live courses (the 90% gate didn't actually block)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "64-65",
     "quote": "The D15 24-hour delay is documented but not platform-enforced.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd",
     "lines": "37",
     "quote": "`masteryThreshold:90` declared in metadata, not enforced by an observable mechanism",
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
   "reason": "Quote verbatim. kb-0058 37 scores mastery truthfulness 'FAIL 1/5' and gives this as one reason, matching the found_by. Single source, but the point is arithmetic, so general. The against field is a fair limit.",
   "statement": "A percentage gate needs enough items to mean anything; with four or five items a 90% bar cannot be applied.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd",
     "lines": "37",
     "quote": "two 4-5 item tests are un-gateable (no \"90% of 4\")",
     "verbatim": true
    }
   ],
   "against": "kb-0164 line 88: \"define mastery through controlled evidence and downstream risk, not a global raw `90%`;\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep",
   "reason": "Quotes verbatim. '97/172' matches kb-0235 76 (two versions of the bank). kb-0167 is an APUSH audit, so the rule spans history and reading. Not a duplicate of 48, which is about the later test, not the retry path. General.",
   "statement": "After a failed mastery attempt, reteach and retest later on new items from a parallel form, which needs a bank deep enough for separate forms.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "141",
     "quote": "- Require 90% to advance; if not met, give intensive instruction and a delayed test with new items.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "67-68",
     "quote": "Rebuild every assessment and writing criterion as failed function -> relevant taught check -> different-evidence retry.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "76",
     "quote": "97/172 items can't populate disjoint parallel forms without overlap.",
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
   "reason": "Quotes verbatim. '12.5%' and '~30%' match both files, and '7.5/25 XP' matches kb-0244. 'Low completion was the main measured failure' describes one incumbent, so the statement is rewritten as a general rule with that case as evidence. The kb-0217 quote is extended to include the heading on its line. General as rewritten.",
   "statement": "Treat completion as the first problem: measure whether students finish before tuning accuracy; one incumbent course had 12.5% median completion.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "37-38",
     "quote": "**Treats completion as the first problem** — the incumbent's real failure is 12.5% median completion, ~30% of intended work done",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0244-g3-proposal-bakeoff-seven-proposals-2026-06-15.qmd",
     "lines": "110-111",
     "quote": "the dosage crisis (7.5/25 XP, 12.5% median completion, ~0 acceleration) is the real #1 problem",
     "verbatim": true
    }
   ],
   "against": "kb-0244 lines 111-112: proposals differed, as \"A/D treat it as an input and F underweights it structurally.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep",
   "reason": "Quotes verbatim. '73.0%/16.6%' and '83.2%/44.8%' match kb-0244 79. kb-0092 25-27 lists the subgroups to check. Distinct from 49, which splits by skill rather than by group. General.",
   "statement": "Report results by student group and check the tails; an overall average can hide a group doing worse than expected.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0244-g3-proposal-bakeoff-seven-proposals-2026-06-15.qmd",
     "lines": "78-79",
     "quote": "Discovered the **grade-band inversion** (at-grade students are the WORST performers, 73.0%/16.6% XP, vs below-grade 83.2%/44.8%)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0092-student-ready-criticism-framework-2026-07-09.qmd",
     "lines": "25-27",
     "quote": "Include below-grade readers, English learners, keyboard-only users, screen-reader users, frustrated students, test-wise students, and students willing to click through or guess.",
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
   "reason": "Quotes verbatim. '~150-250' matches kb-0243 36, which is a proposed schema. Three independent files. General.",
   "statement": "Treat thresholds, cut scores and predicted difficulty as stated priors to be replaced with live response data, not as calibrated facts.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0008-alpha-courses-repo.qmd",
     "lines": "153-154",
     "quote": "cut-scores, mastery gates, WCPM targets are reasoned pilot defaults, to be tuned against real attempt data.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "97-98",
     "quote": "predicted difficulty is a prior with method, population, provenance, and uncertainty; live data must eventually replace it;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "36",
     "quote": "launch on Lexile priors, set `p_m_observed` after ~150-250 live responses",
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
   "reason": "Quotes verbatim. '200-210' matches kb-0059 64. Added kb-0236 61-62 (with 0 of 313 students in the cohort, no RIT claim is made). The against figures (r = 0.967, reliability 0.931) are verbatim at kb-0086 39. General.",
   "statement": "Make no claim that a course or test predicts an external score until a linking study with real students has been run.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
     "lines": "64-65",
     "quote": "the 200-210 claim is by-design **pre-pilot** and confirms only after a linking study",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "40",
     "quote": "no RIT output; engine physically will not emit RIT until linked to real MAP scores.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
     "lines": "61-62",
     "quote": "MAP is 0/313 in-cohort — no RIT claim, no \"proven\", no growth multiples",
     "verbatim": true
    }
   ],
   "against": "Limit, kb-0086 line 39: simulation stats look strong (\"ability recovery r = 0.967 ... reliability 0.931\") but are self-reported simulation, not linking.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 25,
   "verdict": "keep",
   "reason": "Quotes verbatim. '2 of 5 ... 3 backfired' matches kb-0010 110, but these were an LLM prediction engine's own recommendations tested on five synthetic profiles. So the found_by word 'worked' means 'delivered as predicted in a later engine run', not a real-world result. Added kb-0010 120 (no number in the document should be trusted as a magnitude). The central claim rests on the literature summary at kb-0007 74. The against field is a fair limit. General.",
   "statement": "Simulated students mostly echo the assumptions built into them; use them to stress-test a design, not to predict outcomes or effect sizes.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0010-amalgamation-v2-engine-results.qmd",
     "lines": "110",
     "quote": "2 of 5 recs delivered as predicted, 3 backfired — engine flagged why",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd",
     "lines": "74",
     "quote": "Running 100K simulated students yields **zero new information** — outputs are determined by the imposed math models + pre-training.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd",
     "lines": "23",
     "quote": "This is a deterministic design stress test and reproduction packet.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0010-amalgamation-v2-engine-results.qmd",
     "lines": "120",
     "quote": "**No numerical claim in this document should be trusted as a magnitude.**",
     "verbatim": true
    }
   ],
   "against": "kb-0007 line 75: \"Teacher-as-predictor instead reaches r ≈ 0.72–0.79 population-level prediction across three independent research groups\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "keep",
   "reason": "AP case checked in depth. Quotes verbatim. kb-0064 22-27 confirms the 0.29→0.95 jump existed only under a discredited judge, and that the MCQ fix removed the stimulus so the leak probe was skipped. kb-0063 52-53 independently calls the 0.953-vs-0.29 result smoke-only (n=6). kb-0235 186-188 names a risk rather than reporting a measured event. Caveat: kb-0063 39-41 shows the binding grader's own ~28% was largely harness bugs, so the binding judge needs validating too (candidate 28). Overlaps 38 and 66, and adds the case of a sub-check that silently stopped running. General.",
   "statement": "Confirm a score jump on the binding judge before believing it, and check whether part of the check simply stopped running.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "24-25",
     "quote": "On the **binding grader** it **collapsed to ~28%** (DBQ 0%, MCQ_SET 0%) and was logged as a **\"Gemini-judge artifact.\"**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "26-27",
     "quote": "it was **REMOVING the stimulus** so the grader's leak-probe is skipped. That's **grader-gaming**, not a provenance win.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "186-188",
     "quote": "reward inversion/Goodhart (a reworded canonical leak scored higher than a genuine requires-reading item under the shipped code)",
     "verbatim": true
    }
   ],
   "against": "Limit, kb-0063 lines 39-40: on the binding grader, \"the \"stuck at ~28%\" narrative was largely **measurement artifact**\", so the binding judge itself has to be validated.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep-with-fix",
   "reason": "AP case checked in depth. The kb-0170 quote spans lines 58-60, not 58-59. '99%' and 'best-of-N' match kb-0064 34-35. Added kb-0063 50 (the 99% is process, not a clean model win) and kb-0170 61-62 (served-bank and cache evidence kept in a separate lane). Distinct from 65. General.",
   "statement": "Report quality from one clean attempt per item; numbers that include retries, best-of-several picks, repair or cached answers measure the process, not the maker.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "34-35",
     "quote": "The headline **\"99%\" was cache + best-of-N** — its own scoreboard flagged it as **\"NOT the model generating\" / \"not a verified 99%.\"**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "58-60",
     "quote": "Raw generator quality is `raw_k1`: one candidate, one attempt, no retry, reranking, repair, cache substitution, rejection sampling, best-of-N, or hidden human selection.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
     "lines": "50",
     "quote": "So the \"99%\" is process, not a clean model win.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "61-62",
     "quote": "Served-bank and cache/runtime evidence stays in a separate lane.",
     "verbatim": true
    }
   ],
   "against": "Limit, kb-0091 line 36: the delivered bank's quality came from \"discarding large volumes of plausible-looking output.\" Selection is legitimate for the bank, just not as maker quality.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep-with-fix",
   "reason": "AP case checked in depth. Quotes verbatim. '28%', 'four', '81/81', '>=15' and '4 of 5' match. 'Missing keys' had no cited evidence, so two quotes are added: kb-0217 70-71, where a keyless judge produced 11 phantom FAILs that were harness faults, not content faults; and kb-0063 39-41, which lists the four AP harness bugs. Distinct from 36 and 38. General.",
   "statement": "Validate the measuring tool before believing its numbers; harness bugs, missing keys and hardcoded constants have passed for content failures.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "36",
     "quote": "The **\"28%\" was four eval-harness bugs** — weeks burned on a measurement artifact, not a model failure.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "136-137",
     "quote": "the auditor's `thin_banks`/`enforcement_broken` FAIL (81/81) traced to an arbitrary `>=15` bank-depth constant hardcoded in `audit_compliance.py` itself",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "141-142",
     "quote": "the probe is often the bug (4 of 5 listen findings that day were probe-classes, not real defects)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "70-71",
     "quote": "preflight refuses a keyless judge (\"HARNESS, NOT CONTENT\" — 2026-09-03 cost 11 phantom FAILs once).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
     "lines": "39-41",
     "quote": "the \"stuck at ~28%\" narrative was largely **measurement artifact** (wrong field read, grader on wrong host, MCQ_SET mis-route 0→0.77, DBQ truncation 0.55→1.0 at 6000 tok).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 29,
   "verdict": "keep",
   "reason": "Quotes verbatim. '>= 0.8' matches kb-0243 64. kb-0234 83-85 is a code check rather than a model judge, but the bar applies to any automated gate. Overlaps 37, but adds the GO bar and the failure mode of confident wrongness. General.",
   "statement": "Do not let an automated judge block content until it catches every known failure, raises no false flags on clean controls, and is not confidently wrong.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "64-65",
     "quote": "GO requires every in-scope case caught, zero false flags on controls, agreement >= 0.8. **NO-GO stands; semantic lints remain advisory.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd",
     "lines": "76-77",
     "quote": "**the failure mode is confident wrongness, not incompleteness**, which is worse for an automated gate than an honest \"cannot tell.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "83-85",
     "quote": "the function is retained unwired as evidence because both candidate forms flagged approved, reviewed content.",
     "verbatim": true
    }
   ],
   "against": "kb-0245 lines 77-79: \"It DID surface two plausible genuine findings no prior human round had filed ... real value, just not gate-strength yet.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 30,
   "verdict": "keep",
   "reason": "Quotes verbatim. '117', '114' and '3' in the against field match kb-0229 96. Overlaps 10, 36 and 37, and adds the specific edge cases to test. General.",
   "statement": "Test every answer judge on empty, off-topic, keyword-stuffed and word-perfect answers before use.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "63",
     "quote": "oral/typed judges accept empty or content-blind answers.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "72",
     "quote": "The local evaluation fallback grades free responses by keyword overlap, and a porting note propagates that defect.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0229-closing-questions-build-2026-09-25.qmd",
     "lines": "78-79",
     "quote": "the gate was punishing the child for saying the taught sentence exactly.",
     "verbatim": true
    }
   ],
   "against": "Limit, kb-0229 line 96: \"117 judge cases authored, 114 OK/3 WRONG pre-fix (all three the echo class)\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep",
   "reason": "Quote verbatim (kb-0238 37-40). Single source. It is the rule that answers 34 (verdicts vary between runs). General for automated judges.",
   "statement": "The same answer must get the same verdict every time; pin the judge to its most deterministic setting and reuse the verdict for identical resubmissions.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0238-l4-baseline-submission-and-signoff-packet-2026-08-31.qmd",
     "lines": "37-40",
     "quote": "fixed by running the first judging attempt at the most deterministic model setting and caching identical resubmits to return the same verdict instantly.",
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
   "reason": "Quotes verbatim. '41' matches kb-0089 235, and line 238 reports the re-sweep at 772/772. 'Rebuilt' is a fair reading of 'stale literal option text'. Distinct from 24 and 46. General.",
   "statement": "After rebuilding items, run a behavioural sweep that submits right and wrong answers to the live scorer; checking that the file landed does not catch scoring bugs.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd",
     "lines": "235-236",
     "quote": "A behavioral sweep found 41 Unit-2 MCQs paying 0 for every answer because response processing compared `RESPONSE` against stale literal option text instead of the key id.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd",
     "lines": "180",
     "quote": "PUT/read-back catches XML landing, but behavioral scoring sweeps are needed for response-processing bugs.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
     "lines": "99-100",
     "quote": "right buckets keyed 2x with `match-max=1`, which would have let a spec-conformant renderer accept an incomplete response",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 33,
   "verdict": "keep",
   "reason": "Quotes verbatim. Overlaps 50 (hash) and 24. Candidate 34 states the matching rule, so the merge could combine 33 and 34. General.",
   "statement": "Check narration against the printed words by machine transcript and by ear, with a person deciding on flagged clips, and bind each clip to its text so an edit marks it stale.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
     "lines": "29-31",
     "quote": "a text edit (e.g. a definition rewording) leaves the clip silently stale with nothing in the validator suite able to detect it",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0188-feedback-round-pipeline-end-to-end.qmd",
     "lines": "124-125",
     "quote": "written only if the transcript matches the printed line word-for-word",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0228-g3-listen-qa-transcript-receipts-2026-09-24.qmd",
     "lines": "43-44",
     "quote": "machine transcripts needing human disposition before any claim about audio quality is made from them",
     "verbatim": true
    }
   ],
   "against": "kb-0217 lines 72-73: \"half of 'audio defects' were defective checks\". Checks can be wrong too.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 34,
   "verdict": "keep-with-fix",
   "reason": "The kb-0217 quote spans lines 64-65, not 64. The exception clause was supported only by the quote in the against field, so that quote moves into evidence, with kb-0213 116-117 (the split became a standing ruling). Overlaps candidate 33. General.",
   "statement": "What the voice says must match the printed words, except for deliberate differences that are recorded as such.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "64-65",
     "quote": "audio truth (spoken=printed, clip-hash match, no \"Name:\" opener — speaker-label trap)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "113-114",
     "quote": "a deliberate printed/spoken split (printed \"ry,\" spoken \"ree\") was being flagged as a missing part-read",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "116-117",
     "quote": "All three folded into `listen-clips.mjs` as standing rulings.",
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
   "reason": "Quotes verbatim. Added kb-0234 76-77, which states the rule as a check. Extends 17 from exact quotes to paraphrase. General.",
   "statement": "Everything a lesson tells students the text says, quoted or paraphrased, must be in the text; unquoted 'the text says' claims hide the worst errors.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
     "lines": "45-46",
     "quote": "\"Bored\" occurs exactly once in the whole lesson (this string) and zero times in any passage node.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "78-79",
     "quote": "ATTRIBUTED spans (no quotes, introduced by \"the story says\"/\"it says\" phrasing — the shape that hides the worst defects, since unquoted claims look like nothing).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0205-g9-othello-1-1-kb-lesson-view.qmd",
     "lines": "45-46",
     "quote": "In the quote, Iago does follow Othello, only \"to serve my turn upon him\", so \"refusal\" may misstate the line.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "76-77",
     "quote": "anything a lesson presents to the child as being IN the story must actually be in that lesson's own passage text",
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
   "reason": "Quotes verbatim. The against field fits. General.",
   "statement": "Turn each confirmed review finding into a reusable check for its whole class and sweep sibling content, so the same kind of defect is never found by hand twice.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0179-g3-peter-pan-close-out-state-and-reusable-process.qmd",
     "lines": "84-85",
     "quote": "encode the finding's CLASS as a reusable census/validator so the same shape of defect is never re-found by hand twice.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0216-codex-visual-audit-2026-09-07.qmd",
     "lines": "72-73",
     "quote": "so none of these four visual classes can regress silently again",
     "verbatim": true
    }
   ],
   "against": "kb-0234 lines 83-85: a class rule \"was specified but is explicitly NOT shipped/wired\" because it flagged approved content.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 37,
   "verdict": "keep",
   "reason": "Quotes verbatim. 6/65 = 9%, '9 of 12' and '5 of 7' match. Added kb-0217 35 (two-layer audits measured at about 8-15% false positives). General.",
   "statement": "Verify audit findings before acting on them; about one in ten were false, many serious ones were refuted, and some fix lists were already stale.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "100-101",
     "quote": "audit false-positive rate **6/65 = 9%**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
     "lines": "9",
     "quote": "9 of 12 serious findings were refuted with evidence",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
     "lines": "90-91",
     "quote": "5 of 7 were already fixed live before this session (the FIX_LIST's \"not applied\" status was stale)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "35",
     "quote": "two-layer audits at a measured ~8-15% false-positive rate",
     "verbatim": true
    }
   ],
   "against": "kb-0245 lines 35-36: \"these are not rushed-tree findings, they are findings the team's OWN passing gate missed.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 38,
   "verdict": "keep",
   "reason": "Quotes verbatim. A course-build governance rule that holds beyond its source. The against field fits.",
   "statement": "When guidance conflicts, build from the most specific named design for that lesson, cited exactly, rather than from general rules or a sibling lesson.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0179-g3-peter-pan-close-out-state-and-reusable-process.qmd",
     "lines": "67-69",
     "quote": "a named source-of-truth document per lesson-design decision, cited by paragraph number, beats \"mirror a sibling lesson\" or \"the portal's own text\" every time a content dispute comes up.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0210-aladdin-2508-feedback-and-pr27-safety-snapshots.qmd",
     "lines": "119-120",
     "quote": "both of those are real authorities but one tier too general.",
     "verbatim": true
    }
   ],
   "against": "kb-0218 line 70: \"recency/confidence/citation-count do not supersede an earlier academic decision\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 39,
   "verdict": "keep",
   "reason": "Quotes verbatim. 'three components' matches kb-0210 120-121. General.",
   "statement": "Audit each built lesson against its design part by part; builds silently drop or adapt designed parts even when the text itself matches.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0226-g3-pre-submission-closure-audit-2026-09-24.qmd",
     "lines": "30-31",
     "quote": "adapted rows outnumber as-designed rows in every lesson",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0210-aladdin-2508-feedback-and-pr27-safety-snapshots.qmd",
     "lines": "120-121",
     "quote": "L4 as authored/reviewed/deployed was missing three components the design doc mandated",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0233-aug31-sweeps-prose-and-slotmap.qmd",
     "lines": "80-81",
     "quote": "**Slot 3, Aladdin Part 3, is MISSING outright** — spec slot real, design doc exists on disk, but no lessonId was ever authored/shipped for it.",
     "verbatim": true
    }
   ],
   "against": "kb-0218 lines 88-89: a programme-level gap was ruled \"an open scope question, not a defect.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 40,
   "verdict": "keep",
   "reason": "Quotes verbatim. 'three of the four' matches kb-0232 55. Added kb-0234 81-82 (a check for step labels that drift) and kb-0233 61-62 (two spellings of one word, as the found_by claims). General.",
   "statement": "Name each concept, step and frame one way everywhere, and make a frame's wording match the thinking move it claims to teach.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
     "lines": "55",
     "quote": "**MAJOR — we-do renames three of the four I-do step labels (R-KC-11).**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "104-106",
     "quote": "A lesson's frame wording must match its *declared* procedure — a FIND question dressed as INFER (or the reverse) is a defect, not style",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "81-82",
     "quote": "RULE 1 (STEP LABEL DRIFT, shipped) requires the step be named identically at all three stages",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0233-aug31-sweeps-prose-and-slotmap.qmd",
     "lines": "61-62",
     "quote": "**F3 (minor, display-only):** \"erosion\" and \"mechanism\" each get two different phonetic respellings across their two in-course appearances (U1-L2 vs U1-L7).",
     "verbatim": true
    }
   ],
   "against": "kb-0233 line 70: an aside-phrase family \"is legitimately varied, not robotic.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 41,
   "verdict": "keep",
   "reason": "Quotes verbatim. '7/9' matches kb-0217 65-66. The found_by claim that overlapping target words were rejected had no quote; added kb-0136 105. Refines 18. General.",
   "statement": "A word taught for a text must appear in that text and recur later; target words should not overlap in meaning, and other hard words need support too.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "74-76",
     "quote": "**Taught word \"betrayal\" never appears in the L1 passage**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "65-66",
     "quote": "vocab-earned (taught word recurs in-passage + later unit, from 7/9 taught words appearing only once)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "106",
     "quote": "Handle difficult words beyond the three designated vocabulary words.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "105",
     "quote": "Choose distinct vocabulary words. In the camouflage lesson, *camouflage*, *adapt*, and *blend* overlap too much; *blend* even appears inside the definition of *camouflage*.",
     "verbatim": true
    }
   ],
   "against": "kb-0224 lines 89-90: \"a taught word absent from the passage carries an `encapsulating {reason, authority}` exemption\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 42,
   "verdict": "keep",
   "reason": "Quotes verbatim. The against field fits (only earlier parts are kept on screen). In tension with 26 but not a duplicate of it. General.",
   "statement": "Keep the text, the live question and the steps visible while students work on them.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "86",
     "quote": "Prompts ask for textual evidence, but the passage is hidden when the student needs to cite it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "84",
     "quote": "The steps and live question must remain visible, and the model should surface one thing at a time; the current screen contains too much at once.",
     "verbatim": true
    }
   ],
   "against": "Limit, kb-0180 lines 61-62: a passage page offers back \"every *earlier* part of the story only\"; later parts stay hidden.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 43,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The clause 'never one that answers their own task' was supported only by the against quote, and it is candidate 66's point, so it is dropped here. Overlaps 40 (worked example), but adds exemplars at more than one level. General.",
   "statement": "Show students strong model responses, ideally at more than one level, before they write their own.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "87",
     "quote": "No model of a strong response is shown.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0203-g9-ela-cnu-academics-meeting-2026-10-01.qmd",
     "lines": "86-87",
     "quote": "**three exemplar responses** at different levels.",
     "verbatim": true
    }
   ],
   "against": "Limit, kb-0167 line 64: \"Replace independent tasks that reuse answer-bearing modeled evidence\" (see candidate 66).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 44,
   "verdict": "keep",
   "reason": "Quotes verbatim. The against field shows a FIND exception (the State step needs a complete modelled sentence), and kb-0180 84-86 names a MAIN IDEA exception. The rule holds as a default. Spells out part of 40. General.",
   "statement": "Model every step except the final thinking move and leave that to the student, and name steps by what a reader thinks or does, not by a gesture.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "83-84",
     "quote": "the teacher models every step up to but not including the final substantive thinking move; the child does that move",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "96",
     "quote": "\"reread and tap\" -> \"reread and find\" (\"find\" names what a reader does, not what a finger does).",
     "verbatim": true
    }
   ],
   "against": "kb-0226 lines 38-39: \"FIND I-do State hands the conclusion to the child ... instead of a complete modeled sentence\" was flagged as a gap.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 45,
   "verdict": "keep",
   "reason": "Quotes verbatim. Added kb-0136 75 (the question must be bespoke to the text) to support the second clause. General.",
   "statement": "Do not teach shortcut rules that are false for many texts, and write questions specific to the text instead.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "73",
     "quote": "Titles frequently do not state the main idea, so checking against the title is not a dependable rule.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "80",
     "quote": "The lesson may also embed the misconception that text evidence always points to one sentence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "95",
     "quote": "retiring \"hunt for keywords\" (many texts have no clean keyword)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "75",
     "quote": "the question must be bespoke to the text.",
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
   "reason": "Quotes verbatim. Added kb-0225 38-39 (rule 10: the sentence comes back in the next part) to support 'recall it next lesson'. The grade 9 spec's sequence of mimicry, application and evaluation shows the pattern carries across grades. General.",
   "statement": "Close lessons with one idea used several times: state it, find it in the text, apply it to new text or a judgement, then recall it next lesson, with support fading and never returning.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "133-134",
     "quote": "The pattern, novice-to-expert on one idea moved three times, production only, no MCQ / word bank / tap-to-fill anywhere in the closing three:",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "268",
     "quote": "moving from mimicry, to application to the text, to evaluation at the end.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0225-g3-closing-questions-adoption-2026-09-24.qmd",
     "lines": "35",
     "quote": "support fades and never returns (max→frame→none)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0225-g3-closing-questions-adoption-2026-09-24.qmd",
     "lines": "38-39",
     "quote": "**rule 10** — the Name-it sentence recurs at the start of the next part, produced not shown, on a \"Look back\" page.",
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
   "reason": "Quotes verbatim. Distinct from 45. General.",
   "statement": "Before interpreting any assessment, declare its purpose and its full specification: knowledge, evidence, task conditions and scoring rule.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "84-85",
     "quote": "no KC, claim, evidence indicators, task conditions, outcome space, and scoring rule means no assessment;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "89-90",
     "quote": "declare whether a resource is formative, mastery, diagnostic, summative, or cold measurement before interpreting its result;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "132",
     "quote": "do not teach one cognitive operation and assess another.",
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
   "reason": "Quotes verbatim. 'Check that none is also right' repeats part of 6. The near-miss and post-test correction parts are new. General.",
   "statement": "Write wrong options as plausible near-misses drawn from real errors, check that none is also right, and correct misconception lures afterwards because they can plant false knowledge.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "95-96",
     "quote": "potent misconception-based distractors require product-appropriate corrective feedback or post-test correction because plausible lures can seed false knowledge;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "69",
     "quote": "Chunk-stop distractors are self-declared filler, not real near-neighbour traps.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0134-g5-reading-v2-local-design-package.qmd",
     "lines": "104",
     "quote": "Independent review found an initial competing S07 plus S09 interpretation.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim. Added kb-0081 128 and 130 (drag-and-drop and matching items are not keyboard operable; support every interaction). Distinct from 27. General.",
   "statement": "Every interaction must work by keyboard and assistive technology and be readable; an item type that cannot be made accessible is also an unfaithful rehearsal of the real test.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "128",
     "quote": "An item type that cannot be made accessible is also not a faithful rehearsal of the test.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "105",
     "quote": "The Axolotl lesson's opening selection item rendered black text on a black background, legible only on hover.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "128",
     "quote": "The drag-and-drop and matching items are not keyboard or assistive-technology operable",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "130",
     "quote": "Engineer keyboard and assistive-technology support for every interaction",
     "verbatim": true
    }
   ],
   "against": "Limit, kb-0076 line 21: the real test uses these formats too: \"MAP uses these for G3 — check MAP's implementation\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 50,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. '525/772' matches kb-0085 25. 'Least accessible formats' goes beyond the source, which says 'TEI formats ... no attestation', so the wording is changed. General.",
   "statement": "Check what each filtering rule removes and what it concentrates: a leak filter removed recall items by design and pushed 525 of 772 kept items into interactive formats with no accessibility attestation.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "73-74",
     "quote": "KCT1 (domain-knowledge recall) is ~0 **by design** — passage-independent items are exactly what the anti-leak filter removes",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0085-g5-red-team-findings-2026-07-06.qmd",
     "lines": "25-26",
     "quote": "anti-leak concentrates items into TEI formats (525/772), no attestation.",
     "verbatim": true
    }
   ],
   "against": "kb-0089 line 182: a later lane \"disproved \"selected response is inherently leaky\"\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 51,
   "verdict": "keep",
   "reason": "Quotes verbatim. kb-0235 102-103 says 'not the item', meaning the per-item judge score, so 'a tool's score' is a fair gloss when read with kb-0180 122-123. General.",
   "statement": "Optimise the course, not a tool's score; never reorder or reshape lessons to satisfy an aggregate metric.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "122-123",
     "quote": "never move a check earlier to satisfy an aggregate percentage from a reviewing tool.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "102-103",
     "quote": "the correction is \"optimize the course, not the item\"",
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
   "verdict": "keep",
   "reason": "Quotes verbatim. The clause about one plain sentence per unit had no quote; added kb-0136 51. General.",
   "statement": "Standards bound what to cover but give no teaching order; state each unit's key understanding in one plain sentence, link units by big ideas, and record why each prerequisite holds.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "119",
     "quote": "- Standards constrain scope but do not provide a teachable sequence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "52",
     "quote": "Make cross-unit links about big ideas rather than surface facts.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0122-g3-reading-course-graph.qmd",
     "lines": "28",
     "quote": "**Warrant tags:** logical (domain-intrinsic) / empirical (evidence-grounded) / conventional (designed/traditional)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "51",
     "quote": "Add a key understanding at the top of every unit: one plain-language sentence stating what the whole unit is really about.",
     "verbatim": true
    }
   ],
   "against": "kb-0097 line 30: \"is \"lock one topic across many lessons\" the actual ask, or a misread?\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 53,
   "verdict": "keep",
   "reason": "Quotes verbatim (kb-0136 17-18, which records reviewer praise). Single source; this is an adopted rule, not a measured result. General.",
   "statement": "Choose topics with a visible scoring formula people can challenge, and record a reason whenever a person overrides the score.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "17",
     "quote": "They can challenge the weightings, inspect what falls out, and push on a decision they disagree with.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "18",
     "quote": "A person overrode the score and gave a reason rather than allowing the number to decide.",
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
   "reason": "Quotes verbatim. '22 ... 8 lessons' matches kb-0215 84. The source is about science; social studies gets a separate fact-versus-interpretation rule at kb-0164 52-53. So 'another subject' is a mild generalisation. General.",
   "statement": "Screen every text that touches another subject against that subject's known misconceptions, and never present diagrams or models as literal reality.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "48",
     "quote": "apply the misconception-check process to every science-bearing Read/Write text;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "66",
     "quote": "- diagrams or models presented as literal reality;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0215-g5-media-recovery-plan-and-edullm-entrypoint-test.qmd",
     "lines": "84-85",
     "quote": "22 Tier-1 misconception hits across 8 lessons",
     "verbatim": true
    }
   ],
   "against": "kb-0149 lines 34-35: no \"settled consensus science curriculum\" exists yet to check against.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 55,
   "verdict": "keep",
   "reason": "Quotes verbatim. General.",
   "statement": "When a text overlaps a topic taught elsewhere in the same year, make it work in either order and take a fresh angle instead of duplicating it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0149-draft-grade-5-science-ledger.qmd",
     "lines": "37-39",
     "quote": "a same-grade reading treatment must work whether the science lesson happened before or after it and should use a fresh angle rather than duplicate the proposed science treatment.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "45",
     "quote": "use prior-grade or sequencing-safe fresh-angle re-encounters;",
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
   "reason": "The kb-0180 quote starts on line 80, so the range is 80-82. 'Plus knowledge students can be assumed to have' squares the ruling with INFER's own definition (see against) and is fair. The background clause overlaps 20. General.",
   "statement": "A modelled inference may use only what the text shows plus knowledge students can be assumed to have; give only the background the text itself needs.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "80-82",
     "quote": "an inference may only use what the passage's own words show; extension deepens the mood from remaining text clues, never a civic/cultural fact the passage never gave.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "139",
     "quote": "Only context students will need in Act 1, not general history.",
     "verbatim": true
    }
   ],
   "against": "Limit, kb-0180 line 76: inference is defined as \"combine text clues with what you know\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 57,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, but the statement as written overstates them. kb-0220 45-47 records that reviewers agreed intro videos may reveal the plot and characters, which sets aside the world-only Removal test. What holds across every variant is the never-spoil rule, no ending shown or stated (kb-0220 54). kb-0213 69-70 separately flags a picture that showed a character before the text introduced him. The statement is rewritten to those two points; the picture part overlaps 21. General.",
   "statement": "Media must not get ahead of the text: an opening video may introduce characters and set up the plot but never show or state the ending, and a picture must not show a character or event before the text reaches it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0220-peter-pan-video-brief-and-screen-narratives.qmd",
     "lines": "54",
     "quote": "never-spoil (no ending shown/stated)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0220-peter-pan-video-brief-and-screen-narratives.qmd",
     "lines": "45-47",
     "quote": "reviewers agreed on 30-40 seconds, agreed to reveal the plot and characters, agreed to start where the story gets interesting",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "69-70",
     "quote": "**L1 p8 opening image is a spoiler** (shows the stranger who doesn't enter the text until p10).",
     "verbatim": true
    }
   ],
   "against": "kb-0220 lines 23-24: a design rule held that \"no question after the film may ask what happens next\"; the entry leaves the final choice between variants to the reviewers.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 58,
   "verdict": "keep",
   "reason": "Quotes verbatim. 'roughly a third', '9 min' and '≤6 min' match kb-0248. External research. Overlaps 7 and 28 as applied to video. General.",
   "statement": "Keep instructional videos short and put required checks inside them; embedded questions reduce mind-wandering and improve recall.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd",
     "lines": "211-212",
     "quote": "Interpolated memory tests inserted into recorded lectures cut mind-wandering by roughly a third and improved recall versus uninterrupted video.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd",
     "lines": "144-145",
     "quote": "engagement drops sharply with length (students rarely watched past 9 min; recommend **≤6 min segments**)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "31",
     "quote": "If video carries essential context, interrupt it with mandatory quick checks so the learner does not watch a long unexamined clip.",
     "verbatim": true
    }
   ],
   "against": "kb-0248 lines 218-219: the check dosage \"is a reasonable extrapolation, not a directly tested parameter.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 59,
   "verdict": "keep-with-fix",
   "reason": "Quote verbatim, and '.30->.07' matches. The finding concerns grade-4 readers, so the statement now says so. The quote is trimmed to drop a pronoun that refers to a person. Remains an open tension with 7, and with 58 for video. General.",
   "statement": "Whether comprehension checks should interrupt reading or come after it is unsettled: embedded tests helped recall in video, but in one study inferential questions during reading cut grade-4 recall.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
     "lines": "42-43",
     "quote": "interpolated inferential questions cut grade-4 recall .30->.07",
     "verbatim": true
    }
   ],
   "against": "kb-0248 lines 211-212: interpolated tests \"improved recall versus uninterrupted video.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 60,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 'Presenters' and 'the guide's role' are role words, so the statement is rewritten without them. The evidence on realism is mixed (see against), while the mismatch finding is well supported, so the rule is made conditional on mismatch. Added kb-0202 49 and kb-0248 195-196. Overlaps 52. General.",
   "statement": "Avoid moving, speaking near-photoreal synthetic humans on screen unless face, voice and motion match: mismatch reads as fake and cuts engagement while learning stays about the same, and an on-screen figure's presence and role matter more than its realism.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0202-g9-othello-video-research-fake-ai-attention.qmd",
     "lines": "36-37",
     "quote": "**Moving, speaking synthetic humans still read as fake.** The trigger is a mismatch between face, voice and motion, more than the level of realism",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0202-g9-othello-video-research-fake-ai-attention.qmd",
     "lines": "39",
     "quote": "**AI presenters show no reliable learning loss, but a real engagement and comfort loss**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd",
     "lines": "187-188",
     "quote": "Presence and role matter; realism of rendering does not.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0202-g9-othello-video-research-fake-ai-attention.qmd",
     "lines": "49",
     "quote": "A **stylized, illustrated, non-photoreal** figure.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd",
     "lines": "195-196",
     "quote": "Increasing the realism of on-screen embodied instructors creates more looking but less learning",
     "verbatim": true
    }
   ],
   "against": "kb-0248 line 37: participants rated \"the **realistic avatar as significantly more trustworthy**\" in a science framing; line 46: a matched AI voice and AI face \"outperformed all other pairings, including the fully human one, on retention\"; line 48: \"**High behavioral fidelity increased social presence and transfer performance**\"; lines 203-204: \"**cartoon-like scored worst**\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 61,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The redundancy finding (Adesope & Nesbit 2012) is cited only in kb-0250, whose path contains a person's name; no other file cites it. kb-0249 492-493 (spoken words beat printed words beside visuals) does not support turning read-aloud off, so it is dropped. 'Keep read-aloud for weaker readers' misread the meta-analysis: for low-prior-knowledge learners, spoken-plus-written beat spoken-only, not written-only. The case for offering read-aloud rests instead on kb-0136 107 (students who cannot yet decode). Adds evidence to open truth 53. General.",
   "statement": "For fluent readers, listening while reading adds nothing over reading alone, and key terms on screen beat verbatim spoken-plus-written text; offer read-aloud as an option for students who cannot yet decode rather than as the default.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0250-g9-[name]-design-pr700-marisol-prototype.qmd",
     "lines": "578",
     "quote": "Spoken-plus-written was no better than written-only.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0250-g9-[name]-design-pr700-marisol-prototype.qmd",
     "lines": "578",
     "quote": "Showing extracted key terms beat verbatim spoken-plus-written.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "107",
     "quote": "Make difficult words tappable and readable aloud—\"hear it, say it, map it\"—for students who cannot yet decode them.",
     "verbatim": true
    }
   ],
   "against": "kb-0174 line 65: \"captions for Scout (headphones cannot be assumed)\"; the meta-analysis was mostly college students.",
   "general": true,
   "duplicate_of": "53",
   "name_bearing_source": true
  },
  {
   "index": 62,
   "verdict": "keep",
   "reason": "Quotes verbatim. '2–4' matches kb-0250 601, and line 514 also reports 71% versus 17% revising. All three findings come only from kb-0250, whose path contains a person's name; no other file cites them. External research with its limits stated. General.",
   "statement": "Open critical feedback with high standards and confidence the student can meet them, use autonomy-supporting language instead of directives, and offer a few meaningful choices.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0250-g9-[name]-design-pr700-marisol-prototype.qmd",
     "lines": "514",
     "quote": "**1.3 \"Wise feedback\" (high standards plus \"I believe you can meet them\") makes students more likely to revise.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0250-g9-[name]-design-pr700-marisol-prototype.qmd",
     "lines": "530",
     "quote": "Six predicted lower autonomy: holding onto the materials, showing or saying the answers, directives, \"should / got to\" statements, and controlling questions.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0250-g9-[name]-design-pr700-marisol-prototype.qmd",
     "lines": "601",
     "quote": "The effect was strongest with 2–4 successive choices and weaker for adults than for children.",
     "verbatim": true
    }
   ],
   "against": "kb-0250 line 532: \"Limits: lab study, preservice-teacher pairs, a 10-minute one-on-one session.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 63,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. In kb-0193, 'mechanism' means shared renderer code, not teaching method. As written, the statement clashes with candidate 64 (the teaching approach is not shown to work across grades), so it is reworded. Distinct from 2. General.",
   "statement": "Rewrite voice, register and feedback style for each age group; shared lesson mechanics can be reused across grades, but register is content that has to be redone.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0193-g3-book-grade-agnostic-vs-specific-g9-checklist.qmd",
     "lines": "122",
     "quote": "**Register/content differences are separate from mechanism differences.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
     "lines": "959-961",
     "quote": "almost shipping a 10-year-old's storytime voice for salinity-gradient content — is the exact failure mode to avoid repeating at a larger age gap",
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
   "reason": "Quote verbatim. The surrounding text (kb-0130 172-175) calls high-school reading a complete unknown. Single source; an open question. General.",
   "statement": "Whether a teaching approach built for younger students holds for older ones is untested; one older-grade trial is a probe, not proof.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0130-incept-service-coe-catchup-2026-07-15.qmd",
     "lines": "177",
     "quote": "Do not describe this pedagogy or the trained model as grade-agnostic. Grade 6 is a probe, not proof.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 65,
   "verdict": "keep",
   "reason": "Quotes verbatim (kb-0237 findings F14 and F15, and line 99). Extends the 'only what is true' part of 1 beyond feedback. General.",
   "statement": "Never tell students something untrue about the interaction: no pretend listening, no receipts for actions they did not take, and help-assisted completion is never shown as solo success.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "70",
     "quote": "The welcome beat overclaims contingent listening while still issuing a static, answer-independent recast",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "71",
     "quote": "The receipt screen asserts out-loud/self-done events that did not actually happen on the typed/floor interaction paths.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "99",
     "quote": "framed as help, never \"solo pass\"",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 66,
   "verdict": "keep",
   "reason": "Quotes verbatim. 'Lessons 1, 3, and 6' matches kb-0167 64, an APUSH audit; kb-0205 32 comes from the grade 9 Othello build, so the rule spans history and ELA. Overlaps 3. General.",
   "statement": "Independent work must use different evidence from the modelled example; reusing the model's evidence turns it into copying.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "64",
     "quote": "Replace independent tasks that reuse answer-bearing modeled evidence in Lessons 1, 3, and 6.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0205-g9-othello-1-1-kb-lesson-view.qmd",
     "lines": "32",
     "quote": "**\"students are locked out of writing about the guided practice quote\"**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 67,
   "verdict": "keep",
   "reason": "Quotes verbatim. kb-0060 39-43 shows the rule enforced in CI, and kb-0167 71-72 is an APUSH audit. General.",
   "statement": "Send the student's device only student material; answer keys and scoring stay on the server.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0060-incept-read-app-field-notebook.qmd",
     "lines": "39-40",
     "quote": "The client must **never** extract the answer key, compute score/mastery/XP/accuracy/advancement",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "71-72",
     "quote": "Define a student-only source projection containing `student_material` plus approved citation metadata, excluding teacher-only answer-bearing fields.",
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
   "reason": "Quote verbatim. Single source; a general safeguarding rule. Supports 46 without duplicating it.",
   "statement": "Review the student view through a dedicated test-student account, never by impersonating a real child.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0241-alpha-read-contract-investigation-and-packager-build-2026-06.qmd",
     "lines": "123-124",
     "quote": "provision a dedicated sandbox test-student account and impersonate that, never a real child.",
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
   "verdict": "keep-with-fix",
   "reason": "The kb-0202 quote spans lines 55-56, not 56. The claim that open licences carry conditions had no quote; added kb-0251 101 (the Folger texts are CC BY-NC and require attribution). General.",
   "statement": "Clear rights for every text, clip and image before building on it; a licence to view is not a licence to excerpt or embed, and open licences carry conditions.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0202-g9-othello-video-research-fake-ai-attention.qmd",
     "lines": "55-56",
     "quote": "every published licence found grants platform viewing, **not clip extraction or embedding in another app**.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "65",
     "quote": "Confirm receipt, rights, and permitted use before placing any material in a training corpus.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
     "lines": "101",
     "quote": "free for non-commercial use, attribution + link to licence required",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 43 versus 45 matches kb-0251 38-39. 'Check every stated fact against [the edition]' is wrong for background facts: the Venice fact at kb-0204 393 is history, not text. Reworded, and that line added. Overlaps 16 and 17, but adds the rule of pinning one edition. General.",
   "statement": "Pin one edition of a source text and check every quote and line reference against it; check background facts against sources too, not memory.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
     "lines": "38-39",
     "quote": "Open Source Shakespeare numbers it 43, and Gutenberg and MIT have no numbers. Pin the edition to Folger.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "393",
     "quote": "All quotes need checking against the chosen edition.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "393",
     "quote": "By 1603 Venice was past its peak, so \"one of the richest\" is safer.",
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
   "reason": "Quotes verbatim. The kb-0198 quote leaves out the speaker's name. The against field is corrected to a direct quote. General.",
   "statement": "Prefer authentic, well-written texts for literature over machine-written stories, and never label machine-written texts as real sources.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0198-meetings-decisions-timeline-0819-1001.qmd",
     "lines": "29-30",
     "quote": "LLM-generated fiction \"is never going to be great\"; real, split-into-parts texts are the priority",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "44-45",
     "quote": "don't relabel machine-authored cold passages as \"real.\"",
     "verbatim": true
    }
   ],
   "against": "kb-0064 lines 41-42: grade 3 still used \"**machine-authored cold/unseen passages (`humanApproved:false`)**\" as cold tests, labelled as machine-authored.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 72,
   "verdict": "keep",
   "reason": "Quotes verbatim. '1–2' matches kb-0076 16. 'Expect the procedure to change' had no quote; added kb-0180 88-89 (the rail wording was ruled on several times, each ruling replacing the last). General.",
   "statement": "Build and fully review one or two lessons by hand first and make them the template; expect the procedure to change once it is actually run.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0076-coe-catchup-2026-06-30.qmd",
     "lines": "16",
     "quote": "**Handcraft first, automate later** — manually craft the first 1–2 courses to set the quality bars/guardrails before the full automated pipeline.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
     "lines": "596-597",
     "quote": "the template lesson is not a planning document — it is the first fully-built, fully-reviewed lesson",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "88-89",
     "quote": "The exact FIND/INFER rail wording was ruled multiple times and each later ruling supersedes the one before it",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 73,
   "verdict": "keep",
   "reason": "Quotes verbatim. The against case (the AP bar softened from 04-27 to 04-28, kb-0063 22) is exactly the failure the rule prevents. General.",
   "statement": "Calibrate production estimates on a representative unit, not the easiest, and when a quality gate is missed move the date, not the gate.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0129-g5-delivery-sequence-and-eta-calibration.qmd",
     "lines": "126-127",
     "quote": "Choose a representative unit, not the easiest one.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0129-g5-delivery-sequence-and-eta-calibration.qmd",
     "lines": "47",
     "quote": "A missed gate changes the date, never the gate.",
     "verbatim": true
    }
   ],
   "against": "kb-0063 line 22: an AP bar was \"**Softened 04-27 → 04-28**\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 74,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. kb-0081 134 adds that the disagreeing documents all cited the same dated pull, so citing a pull is not enough; each count has to be derived from it. Reworded. General.",
   "statement": "Derive every count in every document from one dated data pull and recheck after each fix; documents that all cited the same pull still disagreed, and a green consistency linter still misses stale numbers.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "136",
     "quote": "The course's own materials disagree with each other.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "134",
     "quote": "all of them cite the same data pull dated 18 June 2026.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
     "lines": "46-47",
     "quote": "Every count in every doc must trace to one named pull with a date",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd",
     "lines": "260",
     "quote": "A green linter is necessary, not sufficient.",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The kb-0009 quote is extended to the full legend of verification tags (lines 107-108), because '[OPEN] not yet verified' alone does not show the levels. kb-0171 is an APUSH status page. Distinct from 44 and 59. General.",
   "statement": "State each result with its verification level and named gaps, never as a bare pass, and never average separate readiness gates into one score.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
     "lines": "63",
     "quote": "verdicts are PASS-with-named-gaps, never bare PASS.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0171-apush-full-course-local-authoring-review-hub-archive.qmd",
     "lines": "50",
     "quote": "Do not average the independent readiness gates into a fake single quality score.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0009-timeback-alpha-read-packager.qmd",
     "lines": "107-108",
     "quote": "Confidence tags: `[LIVE]` walked in the student app · `[CENSUS]` exhaustive content check · `[PROBE]` one live probe per format · `[CODE]` enforced in code+tests · `[OPEN]` not yet verified.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 76,
   "verdict": "keep",
   "reason": "AP case checked. Quotes verbatim. The kb-0064 quote is extended to lines 29-31 ('a hypothesis-transfer, not a cross-validated law'). kb-0221 55-56 relabels the anti-leak engine as measured in history but untested in reading, which supports not counting a history result as confirmation in reading. Added kb-0235 188-189 for the same-model part, which overlaps 35. General.",
   "statement": "Before counting two findings as independent confirmation, check that they did not come from the same source or the same model.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "29-31",
     "quote": "it's **one author importing AP findings onto grade-3**, not two teams replicating independently. Treat it as a hypothesis-transfer, not a cross-validated law.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0221-early-planning-history-and-sep22-snapshots.qmd",
     "lines": "55-56",
     "quote": "re-label the anti-leak engine MEASURED-in-history/UNTESTED-in-reading",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "188-189",
     "quote": "single-family blind-solve confound (every label comes from one solver family; no two-family agreement had been measured",
     "verbatim": true
    }
   ],
   "against": "kb-0242 lines 32-34: duplicates were \"KEPT, not deduped, because repetition across sources is evidence of cross-authority consensus\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 77,
   "verdict": "keep",
   "reason": "Quotes verbatim. '1 of 18' matches the table in kb-0231 (18 probed, 1 stated). Refines 5 by skill. The contrast between history and reading comes from AP-style leak checks on source documents. General.",
   "statement": "What counts as a leak depends on the skill: if finding information in the text is the skill, an answer stated in the text is not a leak, but a question meant to need inference must not have its conclusion stated outright.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "26-27",
     "quote": "in reading, finding the answer in the passage IS the skill, so the usual history-style \"answer is in the source\" leak check is deliberately skipped.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0231-pp-depth-6h-doc-diffs.qmd",
     "lines": "75-76",
     "quote": "stating the trait/conclusion itself is a disguised-FIND violation).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 78,
   "verdict": "keep-with-fix",
   "reason": "kb-0230 58-59 is verbatim. The coin case named in the found_by is at kb-0230 52-53, added. kb-0251 448 is about anchoring a learning question on one quotation, not about what checks target, so it is dropped. General.",
   "statement": "Aim checks at the detail the lesson's idea turns on, not an incidental detail.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
     "lines": "58-59",
     "quote": "are our part-checks about the thematic hinge, not an incidental detail?",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
     "lines": "52-53",
     "quote": "the p10 reading check instead asks about the gold coin, so the betrayal-theme detail is not checked until the modelling moment",
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
   "reason": "Quotes verbatim. General.",
   "statement": "Check cross-references in both directions: a question must not depend on anything not yet read, and a later lesson must not point back to content students never met.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "86-87",
     "quote": "a question/option/hint on page N must not depend on a concrete story noun the child has not read yet",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0225-g3-closing-questions-adoption-2026-09-24.qmd",
     "lines": "60",
     "quote": "or WITW points at content the child never met.",
     "verbatim": true
    }
   ],
   "against": "kb-0234 lines 88-89: the check \"explicitly excludes taught vocabulary and invented practice scenarios from false-positiving.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 80,
   "verdict": "keep",
   "reason": "Quotes verbatim. General.",
   "statement": "Fill-in frames must stay grammatical for every word a student might put in; check frames with substitutions.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0238-l4-baseline-submission-and-signoff-packet-2026-08-31.qmd",
     "lines": "35-36",
     "quote": "which stays grammatical regardless of the filling word.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd",
     "lines": "38-40",
     "quote": "no validator in `validate-contracts.mjs` checks a lead's grammatical fit under substitution",
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
   "reason": "Quotes verbatim. '7x', '11 openers' and '5 paths' match kb-0233 9 and 63-66. Overlaps 44. General.",
   "statement": "Proofread every student-facing string, especially model answers students imitate; validators missed grammar slips, repeated stock openers and other machine-writing tells.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0233-aug31-sweeps-prose-and-slotmap.qmd",
     "lines": "63-64",
     "quote": "**F4 (structural AI-tell):** every U1 lesson's think-aloud opens with the identical clause \"I am hunting for...\" (7x)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0233-aug31-sweeps-prose-and-slotmap.qmd",
     "lines": "10",
     "quote": "none of which any current validator catches",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "88",
     "quote": "Some word-bank prompts misuse vocabulary and read as unedited AI output.",
     "verbatim": true
    }
   ],
   "against": "kb-0233 lines 68-69: \"18 a/an \"violations\" all false positives\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 82,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 'Fix characters with references' had no quote; added kb-0249 533-534 (characters drift between panels unless generation is tied to a reference). Overlaps 22 and 34. General.",
   "statement": "For generated pictures, fix characters and recurring places with references, state exact object counts, and settle borderline cases with several independent reads and a majority.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "137-138",
     "quote": "the model cannot count objects in generated art (needs EXACTLY-N enumerated in the scene line)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "140-141",
     "quote": "pin recurring locations/mediums or they drift",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0219-watch-48h-and-art-qa-redcontrol.qmd",
     "lines": "91-92",
     "quote": "any near-photoreal human face now requires three independent reads with majority rule, not a single pass.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
     "lines": "533-534",
     "quote": "a character whose face/hair/proportions shift between panels, because diffusion generation has no memory across calls unless deliberately conditioned on a reference",
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
   "reason": "Quotes verbatim. General.",
   "statement": "Media must fail closed: a missing clip plays as silence with captions, never an automatic synthetic substitute, and packaging rejects absent or mismatched files.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0215-g5-media-recovery-plan-and-edullm-entrypoint-test.qmd",
     "lines": "31-33",
     "quote": "rejects absent/duplicate/digest-mismatched clips, no browser-TTS fallback in the renderer",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "126-127",
     "quote": "a missing clip renders as silence + captions, never browser TTS or synthetic voice.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0227-g3-branch-hygiene-pr634-prep-2026-09-24.qmd",
     "lines": "68-69",
     "quote": "so the generator fell through to the narrator",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 84,
   "verdict": "keep",
   "reason": "Quotes verbatim. General.",
   "statement": "Teach new material in blocks and mix it with other material only once it is held; teach easily confused pairs explicitly and mix them after both are learned.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "160",
     "quote": "- Interleaving is only appropriate after the skill is ready; massed/blocked first, interleaved later.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0122-g3-reading-course-graph.qmd",
     "lines": "53",
     "quote": "**Gateway discriminations** (taught explicitly, interleaved after both learned)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 85,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. kb-0086 161 says feedback timing should shift as proficiency improves, not that feedback should shrink, so the statement is reworded. Distinct from 1 and 4. General.",
   "statement": "Correct errors immediately and briefly, retest after other items, and shift feedback timing as proficiency grows, since too much feedback can reduce active processing.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "143",
     "quote": "- Error correction should be immediate and brief: correct, test, give intervening items, then retest later.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "161",
     "quote": "- Too much feedback can reduce active processing; feedback timing should shift as proficiency improves.",
     "verbatim": true
    }
   ],
   "against": "kb-0172 line 43: \"an immediately available hint lowers desirable difficulty. The durable rule is attempt first, then targeted help.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 86,
   "verdict": "keep",
   "reason": "Quotes verbatim. '~90:10' matches kb-0123 43. General.",
   "statement": "Keep several strands running, only one introducing new material while the rest review (around nine parts review to one part new).",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "145",
     "quote": "- Keep multiple tracks alive over time; only one track should introduce new material while the rest is review.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd",
     "lines": "43",
     "quote": "lesson composition as interleaved tracks at ~90:10 review:new",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 'Differ in one feature' covers only the difference principle, while the source names set-up, difference and sameness, so the statement is reworded. General.",
   "statement": "Teach concepts with clear examples and non-examples, varied on purpose (set-up, difference and sameness), and stretch strong answers by asking for an original example.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "144",
     "quote": "- Start with clear examples/non-examples and systematically vary examples using set-up/difference/sameness principles.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "47",
     "quote": "imprecise oral definitions receive concrete examples and non-examples; strong answers are extended by asking for an original example.",
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
   "reason": "Both quotes verbatim. In kb-0220 the compound 'why-built-this-way' breaks across lines 61-62, so the quote is given in the joined form, with one space at the break. Line 61 opens with names that the quote leaves out. General.",
   "statement": "Give every activity and screen a short written rationale: the knowledge type and target performance, the failure it guards against, and when its scaffold is withdrawn.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "134",
     "quote": "- Any activity needs a rationale: target knowledge type, performance, failure mode it protects against, why this activity, and scaffold retirement condition.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0220-peter-pan-video-brief-and-screen-narratives.qmd",
     "lines": "61-62",
     "quote": "every submitted screen should carry a short why-built- this-way narrative instead of a pass/fail checklist",
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
   "reason": "Quotes verbatim. The found_by claim that no check required both sources is confirmed at kb-0237 66, added. General.",
   "statement": "Include tasks that make students select, combine and justify what they learned, and define the final performance by exemplars and a rubric instead of splitting it into ever smaller parts.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "123",
     "quote": "- Integrative lessons matter: students can master parts and still fail when asked to select, combine, or justify them in context.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0122-g3-reading-course-graph.qmd",
     "lines": "76",
     "quote": "defined by exemplars+rubric, NOT decomposed further",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "66",
     "quote": "No rendered check requires integrating both sources",
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
   "reason": "Quote verbatim. 'Setting' is not in the source, which says stimulus, framing and tone, so the statement is reworded. Single source; line 94 names a person but the quote does not. General.",
   "statement": "Engagement hooks may shape the material, framing and tone but must never weaken what a scored item measures.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0244-g3-proposal-bakeoff-seven-proposals-2026-06-15.qmd",
     "lines": "98-99",
     "quote": "hooks may shape stimulus/framing/tone but may never weaken a scored item's construct.",
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
   "reason": "Quotes verbatim. General.",
   "statement": "Sort review feedback into proven defects, compatible refinements, conflicts of direction and insufficient evidence, and log contradictions found in the rules themselves.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
     "lines": "70-74",
     "quote": "**insufficient evidence** (stays explicitly unresolved)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
     "lines": "103-105",
     "quote": "*requires* the \"Step N: ...\" numbered format and fails any node without it",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 92,
   "verdict": "keep",
   "reason": "Quotes verbatim. '83%' matches. General.",
   "statement": "Compare against a baseline measured on items as hard as the target; a baseline from easy-distractor items overstates performance.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0221-early-planning-history-and-sep22-snapshots.qmd",
     "lines": "74-75",
     "quote": "re-measure the 83% baseline on hard/near-neighbour items, not the incumbent's easy-distractor items;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "41",
     "quote": "the wrong-instrument correction of the 83% baseline.",
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
   "reason": "Quotes verbatim. The found_by figure '43 of 48' was uncited; it is at kb-0215 83-84, where 43 of 48 passages fail the grade 3 text screen mechanically, and that line is added. General.",
   "statement": "Screen generated texts for age-appropriateness and reading level, and check the generator's own settings.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0221-early-planning-history-and-sep22-snapshots.qmd",
     "lines": "76-77",
     "quote": "add an age-appropriateness check to the team rubric, fix a grade-11-to-grade-3 setting found in the code;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0008-alpha-courses-repo.qmd",
     "lines": "147",
     "quote": "fluency passages regenerated after a first pass leaked Tier-3 vocabulary",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0215-g5-media-recovery-plan-and-edullm-entrypoint-test.qmd",
     "lines": "83-84",
     "quote": "43/48 passages mechanically fail the G3 text screen",
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
   "reason": "Quote verbatim. A single reviewer source. General for any course built on texts.",
   "statement": "Choose texts for purpose, genre and quality as well as a difficulty number; difficulty formulas mishandle poetry and narrative and cannot tell whether a text is worth reading.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "76",
     "quote": "Lexile alone also mishandles poetry and narrative and cannot tell you whether a text is worth reading.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 95,
   "verdict": "keep",
   "reason": "Quote verbatim. The found_by phrase 'test sets of thousands' overstates the source. kb-0081 92 says the state test presents up to roughly 2,740 words, and line 94 says course passages run 58 to 217 words, averaging about 166. Both lines are added. General.",
   "statement": "Practise at the length and demands of the real task; short passages alone never build the stamina that long and paired texts need.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "94",
     "quote": "Practising only on very short texts does not build that stamina.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "94",
     "quote": "Course passages run 58 to 217 words, averaging about 166.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "92",
     "quote": "STAAR presents up to roughly 2,740 words across two single passages and one paired set",
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
   "reason": "Quotes verbatim. General.",
   "statement": "Set a purpose before reading, let students read the whole text first, then model beside the text, and never model the thinking as if it were easy.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "61",
     "quote": "Children need a reason to read before they start",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "28-29",
     "quote": "the child reads the *whole* passage before anything is modelled, and the modelling moment happens *beside* the passage",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "64",
     "quote": "The model should show that selecting the relevant animal and adaptation is genuinely difficult.",
     "verbatim": true
    }
   ],
   "against": "kb-0172 line 39: \"do not make whole-text repetition a universal ritual.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 97,
   "verdict": "keep",
   "reason": "Quotes verbatim. The replication in kb-0251 305 had 390 students. External research plus the grade 9 spec. General.",
   "statement": "Use comparison and error-spotting as guided practice: pick the better of two responses and say why, or stop a model answer at a deliberately planted error and fix it.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "250",
     "quote": "Students see two responses side by side, pick the one that better answers the learning question, and explain why.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
     "lines": "305",
     "quote": "confirms the delayed-test advantage of erroneous examples.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "391",
     "quote": "So that errors are designed on purpose, not improvised.",
     "verbatim": true
    }
   ],
   "against": "kb-0204 line 392: \"In the research, \"faded examples\" usually means steps removed for the learner to complete.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 98,
   "verdict": "keep",
   "reason": "Quotes verbatim. The first two clauses rest on practitioner guidance and adult samples (see against); the last is inferred from studies of over-reliance on AI. General.",
   "statement": "Structure discussion: give thinking or writing time before calling on anyone, track who has spoken, prefer scripted argue-both-sides sequences to open debate, and make students produce the final synthesis alone.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
     "lines": "124-125",
     "quote": "(1) think/write time before calling on anyone; (2) track who's been called against the roster",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
     "lines": "263",
     "quote": "**4. Structured, scripted argument beats open debate; open debate beats none.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
     "lines": "324-325",
     "quote": "both argue for a mandatory \"you-do\" synthesis turn the student alone produces.",
     "verbatim": true
    }
   ],
   "against": "kb-0249 lines 126-127: \"**Quasi-experimental, peer-reviewed** for the core effect (adult sample, not remote)\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 99,
   "verdict": "keep-with-fix",
   "reason": "Quote verbatim. 'AI tutor' is a role word, and it also overstates: kb-0249 327 says a simulated-tutoring study measured models giving in to a student's wrong view. Only the case of a critic voice in a multi-agent panel is untested. Reworded, and line 327 added. General.",
   "statement": "Whether a critic voice in a multi-agent AI panel softens its disagreement when a student pushes back is untested; single models have been measured giving in to a student's wrong view in simulated tutoring.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
     "lines": "328-329",
     "quote": "Untested anywhere found: whether a \"critic\" voice in a multi-agent panel softens its disagreement under social pressure from the student — flag as an open risk.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
     "lines": "327",
     "quote": "a 2025 simulated-tutoring study measured models conforming to a student's stated (wrong) view",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The sources say benchmark scores are not proof and do not establish learning; calling the link 'untested' goes beyond them. Reworded. General.",
   "statement": "Scores on pedagogy-knowledge benchmarks do not show that a model teaches well or that students learn; that link is unproven.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0127-incept-service-coe-catchup-2026-07-14.qmd",
     "lines": "94",
     "quote": "pedagogical-knowledge benchmark performance is not proof of teaching quality.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0130-incept-service-coe-catchup-2026-07-15.qmd",
     "lines": "136-137",
     "quote": "Neither dataset size nor CDPK performance establishes effective generated instruction or student learning.",
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
   "reason": "Quotes verbatim. '73%' matches kb-0248 224. General.",
   "statement": "Whether to label media as machine-made is unresolved: most teens want labels, but labels tend to lower trust in instructional content.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd",
     "lines": "224-225",
     "quote": "**73% of teens want AI-generated content clearly labeled or watermarked**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd",
     "lines": "71-72",
     "quote": "disclosure/labeling is not a free action.",
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
   "reason": "Quote verbatim. One paper reporting three experiments with university students; the limit in the against field fits. General.",
   "statement": "Avoid a live self-view camera during learning; seeing oneself raised appearance anxiety, which lowered recall.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
     "lines": "96-97",
     "quote": "that anxiety, not camera status itself, mediated lower lecture recall.",
     "verbatim": true
    }
   ],
   "against": "kb-0249 line 98: \"(university sample; generalization to 14–15s is inferential)\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 103,
   "verdict": "drop",
   "reason": "The quote is verbatim, but it is a pending design decision listed under 'Decisions TBC' in one app specification (kb-0204 385), not a learning truth. It gives no evidence about placement methods, and 'must be settled before level-specific content is built' depends on that app's own design.",
   "statement": "How students are placed into levels (assigned, diagnosed or self-chosen) must be settled before level-specific content is built; the best method is unresolved.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "385",
     "quote": "Needed before build, because it drives the learning question screen.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 104,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 'correct × 3' and '80%' match kb-0060 52. This is a platform's adopted reward contract and the sources give no learning rationale for it, so the statement is narrowed to the rule itself. Added kb-0060 53-54. General beyond grade and subject.",
   "statement": "Give points for focused time and passed checkpoints, never per correct answer.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0060-incept-read-app-field-notebook.qmd",
     "lines": "52-53",
     "quote": "The broker previously **fabricated** quiz XP (`correct × 3`, no 80% floor, not time-based",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0060-incept-read-app-field-notebook.qmd",
     "lines": "53-54",
     "quote": "Now it records only raw correctness/accuracy and lets TimeBack's gradebook own XP; the only XP surfaced (Caliper `xpEarned`) is time-based.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd",
     "lines": "31-32",
     "quote": "no per-answer XP; preview XP once at finish; 1 XP per whole focused minute; 90% checkpoint",
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
   "reason": "Quotes verbatim. kb-0132 is a preregistered protocol that has not yet been run. The path contains no names; the file is tagged grade 3 reading. General.",
   "statement": "When comparing versions, score them blind to which version or maker produced each, and keep tuning and calibration examples out of the final evaluation.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0132-eppc-bias-experiment-execution-handover.qmd",
     "lines": "568-569",
     "quote": "Scorers never see arm, model, prompt, cost, or other scorer labels.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0132-eppc-bias-experiment-execution-handover.qmd",
     "lines": "566",
     "quote": "calibration items never enter pilot/final.",
     "verbatim": true
    }
   ],
   "against": "kb-0132 line 12: \"The handover is ready; the experiment has not run.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 106,
   "verdict": "keep",
   "reason": "AP case checked. Quotes verbatim. The found_by figures of 143,026 gross rows, 49,571 unique and 0 certified are confirmed at kb-0170 73-75 (added). 340 clusters, 2,233 copies and 28% match kb-0235 48-49. General.",
   "statement": "Count an item bank by exact-unique items that passed independent checks; gross generated rows overstate it, and generated items stay candidates until they pass.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "78",
     "quote": "The 100,000 unique/usable-sample claim is therefore rejected.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "73-75",
     "quote": "- 143,026 gross APUSH rows; - 49,571 sampling-eligible exact unique candidate bodies; - 0 independently certified rows; and",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "48-49",
     "quote": "340 stem clusters duplicated (2,233 excess copies, 28% of pool)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "87-89",
     "quote": "None bypasses source identity, current-format, factuality, answerability, independence, or human review gates.",
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
   "reason": "Quote verbatim. Single source. General.",
   "statement": "Check claimed external requirements against the official text before building on them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
     "lines": "36-37",
     "quote": "The spec's \"TEA mandatory literary works list\" wording overstates it; Othello is the course's own choice.",
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
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
   "lines": "94-95",
   "quote": "all 13 MCQs carry exactly 4 options with index-aligned feedback and no wrong-answer feedback names the key",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
   "lines": "263",
   "quote": "Show students where to look in the text, and revisit previous knowledge to spark connections.",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
   "lines": "52",
   "quote": "replace the binary feedback with corrective feedback that explains why an answer is right or wrong.",
   "ok": true
  },
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
   "lines": "524-525",
   "quote": "one stable voice per \"expert\" across the whole exchange; tune for register-matched, moderate prosody, not maximum expressiveness",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0224-g3-dialogue-branches-pace-gate-roll-forward-2026-09-22-23.qmd",
   "lines": "57",
   "quote": "our L4 silent branch was at **1.00** overlap (verbatim echo)",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0225-g3-closing-questions-adoption-2026-09-24.qmd",
   "lines": "95-96",
   "quote": "every node whose gate/rubric/magic-word demands the taught word prints it nowhere in its stem/instruction/hints.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "68",
   "quote": "The \"Dashed Line\" beat pre-teaches its own check on the same screen.",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0225-g3-closing-questions-adoption-2026-09-24.qmd",
   "lines": "37",
   "quote": "failure is cheap (two attempts, warm reveal, never loop)",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0224-g3-dialogue-branches-pace-gate-roll-forward-2026-09-22-23.qmd",
   "lines": "86-88",
   "quote": "single-select mcq never reveals the answer (R-Q-24, logged as a contradiction awaiting the author's ruling since it departs from \"two attempts then reveal\")",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
   "lines": "614-615",
   "quote": "every free-text written answer except the closing questions gets ten [tries]",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0220-peter-pan-video-brief-and-screen-narratives.qmd",
   "lines": "91-92",
   "quote": "every other open-response node across all four lessons caps at 3 tries",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
   "lines": "172-173",
   "quote": "Measured lesson: control-pass rate did not predict blind certifiability.",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
   "lines": "30-31",
   "quote": "`novelty:\"unseen\"` guarantees the passage is new; it does NOT guarantee passage-dependence",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0221-early-planning-history-and-sep22-snapshots.qmd",
   "lines": "78",
   "quote": "(5) treat anti-leak as a build-time lint for reading, not a deep guarantee.",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
   "lines": "146-147",
   "quote": "The 417 with-passage control failures were often ambiguity or broad `Both` keying, not necessarily blind leakage.",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
   "lines": "42-44",
   "quote": "interpolated inferential questions cut grade-4 recall .30->.07; her rule is ask AFTER not DURING reading",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
   "lines": "50-51",
   "quote": "**answer-position bias fixed** (correct answers were ~75% option \"A\" → shuffled ~even A/B/C/D)",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
   "lines": "56",
   "quote": "Key-position/length balance needs an authoring-time check (12/19 A-keys shipped before the lens).",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0215-g5-media-recovery-plan-and-edullm-entrypoint-test.qmd",
   "lines": "101-102",
   "quote": "correctly routes missing evidence to `NOT_EVALUABLE` instead of guessing",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
   "lines": "44-45",
   "quote": "the sealed rule had ignored those hits because the solver reported low confidence.",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0225-g3-closing-questions-adoption-2026-09-24.qmd",
   "lines": "36",
   "quote": "no string matching (judge on rubric meaning)",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
   "lines": "25",
   "quote": "Misspelled \"magician\" marked correct; decide a comprehension spelling policy",
   "ok": true
  },
  {
   "truth": 16,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
   "lines": "38-39",
   "quote": "Open Source Shakespeare numbers it 43, and Gutenberg and MIT have no numbers.",
   "ok": true
  },
  {
   "truth": 16,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
   "lines": "60-61",
   "quote": "never a position (`?page=n` rotted once already when a lesson grew a page)",
   "ok": false
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd",
   "lines": "70",
   "quote": "exact-quote grading must fail closed (a botched quote was accepted)",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
   "lines": "330-331",
   "quote": "roughly two-thirds of ChatGPT-generated bibliographic citations invented or wrong",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0067-g5-generator-pilot-intake-and-team-async-2026-06-23.qmd",
   "lines": "275",
   "quote": "The adapter only marks Part B as evidence if the option text resolves against the stimulus text.",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "59",
   "quote": "\"producer\"/\"habitat\" are deep-taught as if they were blocking vocabulary (they aren't).",
   "ok": true
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0220-peter-pan-video-brief-and-screen-narratives.qmd",
   "lines": "19-20",
   "quote": "three-channel word stamping (`nursery`, `revenge`, `cutlass`, `hull`, `rigging` — heard, on-screen text, and pictured together)",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
   "lines": "532-533",
   "quote": "**The specific comics failure is cross-panel drift, not single-panel flaws.**",
   "ok": true
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
   "lines": "110-111",
   "quote": "each split into single-question pages/cases, all verbatim quoted options preserved",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
   "lines": "95-96",
   "quote": "`validate-assets`, voice-provenance and voiceover-sync were all green because none of them opens the file.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0176-g3-peter-pan-pr-timeline.qmd",
   "lines": "53",
   "quote": "Every deploy was proven by **hashing the served file**, never by a 200 response",
   "ok": true
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
   "lines": "39",
   "quote": "\"remove Scout's interjections at the top of each page. They take away from the reading flow.\"",
   "ok": true
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd",
   "lines": "62-63",
   "quote": "one attention target at a time; only the current sentence highlighted.",
   "ok": true
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "67",
   "quote": "The diagram is not element-addressable and has no accessible table equivalent.",
   "ok": false
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
   "lines": "19-20",
   "quote": "the closing comprehension check was silently optional while every sibling page gates.",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
   "lines": "130",
   "quote": "skippable \"pause and think\" is not a check.",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd",
   "lines": "69-70",
   "quote": "the judged screenshot never contained the defect's gated UI node at all -- a pass that proves nothing",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0219-watch-48h-and-art-qa-redcontrol.qmd",
   "lines": "83-84",
   "quote": "confirming single-read verdicts on near-photoreal humans are unstable.",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
   "lines": "83-84",
   "quote": "same-model resamples (agreement = self-consistency, not cross-family agreement)",
   "ok": true
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0186-scope-lane-and-model-routing-rules.qmd",
   "lines": "82-84",
   "quote": "a probe route was found to return 200 with `{\"ok\":false}` when the key was missing, serving keyless for roughly 11 hours undetected",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0229-closing-questions-build-2026-09-25.qmd",
   "lines": "96",
   "quote": "117 judge cases authored, 114 OK/3 WRONG pre-fix (all three the echo class)",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
   "lines": "97-98",
   "quote": "invariant (ID3 tag or frame sync in the first bytes), red-controlled 11→0.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0219-watch-48h-and-art-qa-redcontrol.qmd",
   "lines": "74-75",
   "quote": "prove the new check discriminates (fires on AI-generated film-frame humans, stays quiet on drawn children) *before* judging",
   "ok": true
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd",
   "lines": "67",
   "quote": "Prepare knowledge -> encounter text -> model thinking -> guided same-process practice -> student articulation -> evidence check -> delayed/varied transfer",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0083-clone-lessons-inceptbench-results-2026-07-02-eval-summary.qmd",
   "lines": "64",
   "quote": "Q4, Q9, Q12, and Q13 all ask why ice floats.",
   "ok": true
  },
  {
   "truth": 42,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd",
   "lines": "256",
   "quote": "- rule that downstream invariants must be recomputed after any fix wave.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
   "lines": "23",
   "quote": "machine checks do not approve content.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
   "lines": "55-56",
   "quote": "That green state is not the semantic verdict.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
   "lines": "149-151",
   "quote": "is not the same as truly ready",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
   "lines": "18",
   "quote": "## What's REQUIRED (the bar — and it moved)",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
   "lines": "54-55",
   "quote": "the live-rendered surface must be reviewed, not just source artifacts.",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0009-timeback-alpha-read-packager.qmd",
   "lines": "116-117",
   "quote": "They push fine (201, valid QTI, GET 200) but the quiz body is empty",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0216-codex-visual-audit-2026-09-07.qmd",
   "lines": "44-45",
   "quote": "the content-check battery is desktop-only, so all three classes were invisible to it",
   "ok": true
  },
  {
   "truth": 47,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0219-watch-48h-and-art-qa-redcontrol.qmd",
   "lines": "37-38",
   "quote": "exit codes showed 0 but masked real FAIL counts (L4 14, L5 16, L6 6, L7 4)",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
   "lines": "149",
   "quote": "A same-day lesson gate proves at most \"I can do it now,\" not \"I can still do it later under changed conditions.\"",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0244-g3-proposal-bakeoff-seven-proposals-2026-06-15.qmd",
   "lines": "80-81",
   "quote": "inference was 5x undercounted by the live heuristic (actually 9.7%, not the 2% other proposals cited)",
   "ok": false
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
   "lines": "146-147",
   "quote": "clip basenames repeat across lessons so hash edits must match the full lesson path, never the bare basename.",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd",
   "lines": "45",
   "quote": "**No significant difference in academic performance** between AI and human instructor conditions. **Video engagement was higher with the human instructor.**",
   "ok": true
  },
  {
   "truth": 52,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
   "lines": "508-509",
   "quote": "switching static images as defensible, not proven-superior**, to video on learning grounds alone.",
   "ok": true
  },
  {
   "truth": 53,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd",
   "lines": "65",
   "quote": "captions for Scout (headphones cannot be assumed)",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
   "lines": "651-652",
   "quote": "after 4 wrong taps, Scout (the guide) offers to find the remaining clues",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
   "lines": "335-336",
   "quote": "**This is the single highest-confidence risk in this file** — a general, high-base-rate LLM property, not a possibility.",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
   "lines": "38-40",
   "quote": "water-cycle items were bound to an unrelated pistol-shrimp passage",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
   "lines": "30-31",
   "quote": "a **CRITICAL veto** caps the score at 0.84 if any CRITICAL metric is 0",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0083-clone-lessons-inceptbench-results-2026-07-02-eval-summary.qmd",
   "lines": "64",
   "quote": "the flags live in the prose reasoning, not the ID list.",
   "ok": true
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd",
   "lines": "51",
   "quote": "trust the recompute, not the annotation",
   "ok": true
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
   "lines": "174-175",
   "quote": "the agent that proposed the redesign reported the shadowed, non-shipped number.",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
   "lines": "92",
   "quote": "Example found: a main-idea lesson served an inference/evidence item.",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
   "lines": "500-502",
   "quote": "panels must switch on content (new speaker/beat/clue), never for variety alone — that is the seductive-details pattern.",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
   "lines": "182-184",
   "quote": "cross-family blind-solve on a held-out 50-item probe as the real ground truth and checkpoint-selection signal, not the per-rollout reward).",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
   "lines": "29",
   "quote": "(`reading_level_match`, `answer_balance`) are deterministic, not LLM-judged.",
   "ok": true
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0211-peter-pan-reviewer-round-2708.qmd",
   "lines": "24",
   "quote": "Both usage checks were crackable via the single pair \"baby\"+\"sleep\"",
   "ok": true
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
   "lines": "73-74",
   "quote": "the seven `unsupported-detail` family routes were replaced with diagnosed, evidence-bound distractor semantics.",
   "ok": false
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0219-watch-48h-and-art-qa-redcontrol.qmd",
   "lines": "82-84",
   "quote": "same images, criteria differing only by the tightening",
   "ok": true
  }
 ]
}
```
