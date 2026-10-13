# read:kb-course-builds

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "kb-course-builds",
 "coverage": {
  "read": [
   "~/Projects/grade3-reading/knowledge_bot/INDEX.md (tags/keywords parsed to find scope entries)",
   "~/Projects/grade3-reading/knowledge_bot/knowledge/ in-scope entries read in full: kb-0003, 0004, 0006, 0007, 0008, 0009, 0010, 0011, 0012, 0013, 0014, 0015, 0022, 0023, 0056, 0057, 0058, 0059, 0060, 0062, 0064, 0066, 0067, 0068, 0073, 0074, 0075, 0076, 0078, 0079, 0081, 0082, 0083, 0084, 0085, 0086, 0089, 0090, 0091, 0092, 0096, 0097, 0098, 0099, 0100, 0120, 0122, 0123, 0125, 0126, 0127, 0129, 0130, 0134, 0135, 0136, 0149 (prose plus sampled rows), 0164, 0167, 0169, 0172, 0174, 0176, 0177, 0178, 0179, 0180, 0186, 0188, 0193, 0198, 0202, 0203, 0204, 0205, 0210, 0211, 0212, 0213, 0214, 0215, 0216, 0217, 0218, 0219, 0220, 0221, 0222, 0223, 0224, 0225, 0226, 0227, 0228, 0229, 0230, 0231, 0232, 0233, 0234, 0235, 0236, 0237, 0238, 0241, 0242, 0243, 0244, 0245, 0246, 0247, 0248, 0249, 0250, 0251",
   "Extra, because of the AP emphasis: kb-0063 (AP training history, read to check kb-0064's AP claims), kb-0170 and kb-0171 (APUSH course-build records, read in full), kb-0175 (short, no candidates), kb-0132 (tag 'grade-3-reading', near-variant; skimmed with targeted reads)"
  ],
  "skipped": [
   "Entries with no scope tag or keyword (other subjects, infrastructure, vendor and model-training notes, e.g. kb-0121, 0124, 0128, 0131, 0133, 0137-0139, 0173): outside this direction",
   "Closeout-only entries kb-0181-0185, 0187, 0189-0192, 0194-0197, 0199-0201 and memory digests kb-0206-0209: no scope tag or keyword",
   "~/Projects/grade3-reading/knowledge_bot/.env: never opened, as the rules say",
   "Raw data files referenced inside entries (jsonl, csv, zip): not opened"
  ],
  "notes": "Read-only throughout; nothing written. Names appear inside many file bodies; quotes were chosen as name-free substrings where possible. Paths that contain a person's name: kb-0073, 0079, 0100, 0177, 0178, 0212, 0214, 0246, 0247, 0250. Only two candidates rely on kb-0250 and they are marked name_bearing_source true. Multi-line quotes are joined with one space. Line numbers were checked again this session. For external research, the DOI or URL is given in found_by because kind is an enum."
 },
 "candidates": [
  {
   "statement": "A high general quality score does not show that an item needs its text; run leak, structure and fit checks separately and let each block on its own.",
   "kind": "measured",
   "found_by": "Answer-leaking items scored 1.0 on the general item judge; a 100% blind-solvable item scored 1.0; a course whose items all scored 1.0 was 90% blind-solvable.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
     "lines": "47",
     "quote": "**MAP-likeness review (separate from InceptBench, which graded answer-leaking items 1.0):**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "103-105",
     "quote": "a course where every item scores IB 1.0 but 90% is blind-solvable is a failed course (proof: DAPO epoch 0 emitted \"What is the primary function of chlorophyll?\" from a photosynthesis passage — IB 1.0, blind-solve 100%)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "68-69",
     "quote": "InceptBench grades *instructional* quality, **not** test-security — so it won't catch a leaky-stimulus gap; anti-leak must be enforced upstream."
    }
   ],
   "against": "Limit, kb-0234 lines 30-31: \"a **CRITICAL veto** caps the score at 0.84 if any CRITICAL metric is 0\". The judge does veto on its own critical metrics; leak is just not one of them.",
   "adds_to_existing": [
    5,
    44,
    58,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge the whole set as well as each item: repeats, cross-item clues and answer patterns only show at set level, and items that pass one by one can fail together.",
   "kind": "measured",
   "found_by": "65 of 76 lesson bundles scored 0 on non-repetitiveness; a course passed item-level evaluation but failed the course-level one; one word pair cracked two separate checks.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0083-clone-lessons-inceptbench-results-2026-07-02-eval-summary.qmd",
     "lines": "64",
     "quote": "Non-repetitiveness is by far the weakest dimension: **avg 0.14; 65 of 76 bundles scored exactly 0** on it."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0076-coe-catchup-2026-06-30.qmd",
     "lines": "33",
     "quote": "G3 passed **individual item** evals but **NOT** the holistic **course-level** eval"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0211-peter-pan-reviewer-round-2708.qmd",
     "lines": "24",
     "quote": "Both usage checks were crackable via the single pair \"baby\"+\"sleep\""
    }
   ],
   "against": "kb-0083 line 94: \"the 0.0s on multi-passage bundles say more about eval packaging than content.\"",
   "adds_to_existing": [
    8,
    41,
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A solve check with the text hidden is only as good as its solver: calibrate the solver on known leaky and known clean items, because a weak solver passes leaky items and a bluffing solver flags clean ones.",
   "kind": "measured",
   "found_by": "With a stronger solver, only 20 of 95 previously clean items survived; an over-eager solver gamed option-length tells and scored 1.0 blind on items that needed the passage.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "68-69",
     "quote": "of v1's 95 re-gated \"clean\" items, only **20 (21%) survived**; **75 leaked** under the strong solver."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd",
     "lines": "31",
     "quote": "it returned blind accuracy of `1.0` on items that genuinely needed the passage."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd",
     "lines": "70",
     "quote": "2. A solver that can bluff its way through without the passage will inflate leak rates."
    }
   ],
   "against": "Limit, kb-0092 lines 25-27: real users include \"test-wise students, and students willing to click through or guess.\" A solver that never guesses can understate the risk.",
   "adds_to_existing": [
    5,
    37,
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Never let the process that made items certify them; a separate check, ideally from a different model family, must pass them, and the maker's own report of success counts for nothing.",
   "kind": "adopted rule",
   "found_by": "A generation retrospective credited quality to distrusting the generator; plan traces banked that self-report is not evidence.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "26",
     "quote": "The questions were good because the generator was not trusted."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0090-fable5-plan-traces-2026-07-09.qmd",
     "lines": "129-131",
     "quote": "- a lane cannot certify its own items;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "231",
     "quote": "3. Use a different family for the gate than for the author. Never same-family certify."
    }
   ],
   "against": "kb-0127 lines 85-86: \"Three-family judging was proposed, not approved, and no evidence was presented that it reduces evaluator flakiness.\"",
   "adds_to_existing": [
    44,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A pass belongs to the exact content, rules and checker that produced it; after any change to any of them the earlier result is void until the checks run again.",
   "kind": "measured",
   "found_by": "An item clean under an older solver leaked 3/3 under the current one; model snapshots were withdrawn after source changes.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "52-53",
     "quote": "its later invalidation by a stronger current plain-blind solver; stale solver results are not certification."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0134-g5-reading-v2-local-design-package.qmd",
     "lines": "168-170",
     "quote": "Any canonical, source, model-policy, renderer, validator, or package-contract change invalidates the relevant downstream evidence and requires a fresh rebuild."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
     "lines": "24",
     "quote": "All 550 forms remain candidates and the historical model snapshots are withdrawn after source changes."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    42,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count repeated exact recoveries made with the text hidden as a leak even when the solver says it was guessing; low stated confidence must not cancel a correct blind answer.",
   "kind": "measured",
   "found_by": "A sealed rule ignored an item recovered exactly in 3 of 8 shuffles because the solver reported low confidence; an objective recount reversed the promotion.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "43-45",
     "quote": "Promotion review found `r3-09` at 3/8 exact plain-blind recovery and 0.71875 mean partial accuracy; the sealed rule had ignored those hits because the solver reported low confidence."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0126-claude-takeover-audit-2026-07-13.qmd",
     "lines": "29-30",
     "quote": "`r3-09` was exactly solved blind in 3/8 shuffles and that low solver confidence had hidden those hits."
    }
   ],
   "against": "Limit, kb-0089 lines 286-287: \"sounder leak signal became pair-mean over many shuffles above a higher margin or exact-match rate above the chance floor.\" Recoveries count only above chance.",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Set each pass or fail threshold against the chance score of that exact item as it is actually scored, not against its format name.",
   "kind": "measured",
   "found_by": "A 0.60 threshold on an ordering score with a chance floor near 0.50 flagged noise.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd",
     "lines": "284-285",
     "quote": "a 0.60 pair-accuracy threshold was too close to chance and flagged noise."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "40-41",
     "quote": "PASS if with-passage correct-rate >= 0.80 AND without-passage correct-rate <= chance-rate + 0.15 margin"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Choose the number of options on purpose: two invite coin-flip guessing, a dozen overload the student, and filler options must never be added to reach a count.",
   "kind": "adopted rule",
   "found_by": "Reviews rejected a two-option item as a 50/50 guess and a twelve-option item as too heavy a load; a routing note banned settling the three-or-four dispute with filler.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "112",
     "quote": "MCQs need at least four options. A two-option yes/no item permits a 50/50 guess."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "128",
     "quote": "one hot-text item offered twelve selectable options, an excessive motor and cognitive load for an eight-year-old."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "104",
     "quote": "An agent must not resolve this by adding filler"
    }
   ],
   "against": "kb-0164 lines 102-104: \"the MCQ BrainLift reports a research consensus favoring three and recommends four as Alpha's default only when all distractors remain plausible and diagnostically useful.\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "The right answer must not stand out by length, form or a distinctive word it shares with the question, and this should be checked in code when items are written.",
   "kind": "measured",
   "found_by": "A deterministic grader found 626 longest-option tells in one dataset; a key-integrity check now bans stem words that appear only in the key.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0068-g5-static-dataset-intake-2026-06-23.qmd",
     "lines": "117",
     "quote": "longest-option-tell: 626"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "91-92",
     "quote": "STEM-LEAK (no distinctive content word may sit in both the stem and only the correct option)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "133",
     "quote": "Closed-response items must require the target reasoning and must not be answerable by surface cues, keyword matching, option length, or test-wise elimination."
    }
   ],
   "against": "Limit, kb-0096 lines 49-50: \"The audit says 10 MCQs were over-flagged under the old blind-solver and correctly certified after the re-baseline.\"",
   "adds_to_existing": [
    8,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In matching tasks give more targets than prompts and do not announce which one is spare, so the last pairing cannot be won by elimination.",
   "kind": "adopted rule",
   "found_by": "Intake required an unused target in every match item; a 3x3 match was admitted as an elimination cue; a scan found 192 items announcing their decoy.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0067-g5-generator-pilot-intake-and-team-async-2026-06-23.qmd",
     "lines": "314",
     "quote": "- add at least one unused/decoy right bucket to match items"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
     "lines": "66",
     "quote": "`match` is 3×3 (minor elimination cue)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "133",
     "quote": "192 match items announcing a decoy bucket"
    }
   ],
   "against": "kb-0068 line 116 lists \"unused-right-bucket-exists: 638\" as a failure reason. One local grader treated a spare target as a defect.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Build the need for the text into how items are constructed; raw generated items mostly leak, and recall or 'textbook-correct' items leak through general knowledge whatever their format.",
   "kind": "measured",
   "found_by": "A raw candidate sample leaked 94% under a strict cross-family solve; MCQs leaked through ordinary school knowledge.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd",
     "lines": "276",
     "quote": "85/90 exact blind-recovered = 94% leak under the strict sample."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd",
     "lines": "271",
     "quote": "- construction is the lever, not format alone."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "208",
     "quote": "- MCQ leaked through ordinary school knowledge, vocabulary, or a \"textbook correct\" option;"
    }
   ],
   "against": "kb-0091 lines 127-128: \"Lesson: anti-leak success alone is insufficient. Some items became mechanical ordering tasks or failed standard fit even after passing the blind gate.\"",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When most items on a text leak, change the text instead of repairing items; texts that restate widely known facts cannot carry questions that need the text.",
   "kind": "measured",
   "found_by": "Regeneration was abandoned once leaks were traced to encyclopedic passages; one item stayed cold-solvable at about 0.8 because its facts are world-famous.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "37-38",
     "quote": "regeneration was abandoned — the root cause is passage design (encyclopedic passages), not item quality."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
     "lines": "119-120",
     "quote": "cold-solvable ~0.8 because camel adaptations are world-famous general knowledge; distractor surgery can't close it, needs full content replacement"
    }
   ],
   "against": "Limit, kb-0074 lines 42-43: \"**Reconciliation = role-separation: cold at the gate/test, topic-coherent during learning.**\" The rule holds for test texts.",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep learning texts and test texts apart: sequence learning texts so knowledge recurs and builds, keep unseen texts for tests, and keep what is scored separate from what was taught.",
   "kind": "adopted rule",
   "found_by": "A course of disconnected passages chosen so that knowledge could not help was judged not to be a curriculum.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "70",
     "quote": "Sequence the learning texts so taught knowledge recurs and compounds, and reserve cold, non-overlapping passages for the test only, where that property belongs."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0074-g3-reviewer-feedback-distilled-for-g5-2026-06-30.qmd",
     "lines": "79-80",
     "quote": "The **scored `item_bank`/independent claims stay disjoint from that on-ramp and from every teaching claim**"
    }
   ],
   "against": "kb-0098 lines 38-39: \"knowledge-building can be gamed if later questions become answerable from earlier lessons without proving true comprehension.\"",
   "adds_to_existing": [
    18,
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A bank of good items is not a course; items count only inside a taught sequence that students can actually move through.",
   "kind": "adopted rule",
   "found_by": "A well-built practice engine was refused approval as a curriculum.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "118",
     "quote": "- Build a real curriculum, not a library of components or a standards-aligned item bank."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd",
     "lines": "70",
     "quote": "Strong questions do not become a course unless they sit inside this flow and the actual app proves students can experience it."
    }
   ],
   "against": "kb-0076 line 20: \"The reviewer **praised** the MAPS focus; it only \"fell short as a standalone teaching course.\"\"",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In gradual release, the model shows the thinking rather than revealing the answer, the shared step leaves part of the answer for the student, and all three stages practise the same skill.",
   "kind": "adopted rule",
   "found_by": "Reviewers found the model revealing answers, the shared step reduced to a hint, and independent work switching skill.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "60",
     "quote": "I-do reveals the answer instead of modeling thought; we-do is only a hint; you-do sometimes switches to a different skill."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "34-36",
     "quote": "the we-do gives a *partial* answer the child completes (a hint is not a we-do, a fresh question is not a we-do); I-do, we-do and you-do must run the *same skill*, never switch mid-lesson."
    }
   ],
   "against": "Limit, kb-0204 line 326: \"A quick check at the start of guided practice lets confident students move straight on.\"",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Fade support by the number of successful uses, not the calendar, and let students who show they already know a skill skip the full model.",
   "kind": "adopted rule",
   "found_by": "Rulings set an exposure-based fade; the design specification cites the expertise reversal effect.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd",
     "lines": "72-73",
     "quote": "exposure-based fade progression per skill (heavy model 5/2/1 → shift 3/2/3 → hand-over 1/2/5)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "41",
     "quote": "scaffolds fade across a unit (a procedure \"collapses into a two-step option after five successful uses,\""
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "284",
     "quote": "The expertise reversal effect (Kalyuga et al.): heavy guidance helps novices but slows down learners who already know the material."
    }
   ],
   "against": "kb-0204 line 306: \"In review lessons (Profile D), guided practice grows again but changes form: worked examples and comparative judgement, rather than first-time modeling.\"",
   "adds_to_existing": [
    15
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every screen should ask for a response that matters to the teaching move, preferably one the student produces rather than clicks; passive or decorative-tap screens invite click-through.",
   "kind": "adopted rule",
   "found_by": "A ruling on active engagement made every screen require a specific interaction.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "27",
     "quote": "passive listening or text-only screens invite click-through rather than attention. The interaction must be substantive to the teaching move; a decorative tap control does not satisfy the concern."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "86-87",
     "quote": "match the task family to the knowledge: recognition is not enough for productive, representational, justificatory, or integrative constructs;"
    }
   ],
   "against": "Limit, kb-0081 line 108: \"Covering varied technology-enhanced item types is a real benefit and the clearest advantage over the incumbent\"",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Try to beat every mastery gate yourself before claiming it works: click through without reading, answer everything wrong, and try to reach the end with no answers.",
   "kind": "measured",
   "found_by": "Walkthroughs passed gates at about 20% accuracy, with every answer wrong, and with zero answers given.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "120",
     "quote": "earned a stamp on \"The Amazing Axolotl\" at about 20 percent accuracy by clicking through without reading, then advanced with the passage hidden from view."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "101",
     "quote": "In a main-idea task, reviewers earned the pass while answering every question incorrectly."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0215-g5-media-recovery-plan-and-edullm-entrypoint-test.qmd",
     "lines": "85-87",
     "quote": "a real browser reached \"Great Work!\" across all 18 of U1·L3's scenes with **zero answers given**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    28,
    38,
    47
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A rule declared in metadata or documents is not enforced until the running product is shown to block on it.",
   "kind": "measured",
   "found_by": "A declared 90% threshold was null or unenforced live; a documented 24-hour delay was not enforced by the platform.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "92-93",
     "quote": "`masteryThreshold` was `null` on both live courses (the 90% gate didn't actually block)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "64-65",
     "quote": "The D15 24-hour delay is documented but not platform-enforced."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24,
    28,
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A percentage gate needs enough items to mean anything; with four or five items a 90% bar cannot be applied.",
   "kind": "measured",
   "found_by": "An evaluation scored a course's mastery truthfulness 1/5 partly because 4-5 item tests cannot be gated.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd",
     "lines": "37",
     "quote": "two 4-5 item tests are un-gateable (no \"90% of 4\")"
    }
   ],
   "against": "kb-0164 line 88: \"define mastery through controlled evidence and downstream risk, not a global raw `90%`;\"",
   "adds_to_existing": [
    15
   ],
   "name_bearing_source": false
  },
  {
   "statement": "After a failed mastery attempt, reteach and retest later on new items from a parallel form, which needs a bank deep enough for separate forms.",
   "kind": "adopted rule",
   "found_by": "Course rules and an independent audit required a reteach-then-different-evidence retry; a certified bank was too thin for separate forms.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "141",
     "quote": "- Require 90% to advance; if not met, give intensive instruction and a delayed test with new items."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "67-68",
     "quote": "Rebuild every assessment and writing criterion as failed function -> relevant taught check -> different-evidence retry."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "76",
     "quote": "97/172 items can't populate disjoint parallel forms without overlap."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Measure whether students finish before tuning accuracy; low completion was the main measured failure, and the design should answer that number.",
   "kind": "measured",
   "found_by": "Incumbent data showed 12.5% median completion.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "37-38",
     "quote": "the incumbent's real failure is 12.5% median completion, ~30% of intended work done"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0244-g3-proposal-bakeoff-seven-proposals-2026-06-15.qmd",
     "lines": "110-111",
     "quote": "the dosage crisis (7.5/25 XP, 12.5% median completion, ~0 acceleration) is the real #1 problem"
    }
   ],
   "against": "kb-0244 lines 111-112: proposals differed, as \"A/D treat it as an input and F underweights it structurally.\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Report results by student group and check the tails; an overall average can hide a group doing worse than expected.",
   "kind": "measured",
   "found_by": "A data pull found at-grade students performing worse than below-grade students.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0244-g3-proposal-bakeoff-seven-proposals-2026-06-15.qmd",
     "lines": "78-79",
     "quote": "Discovered the **grade-band inversion** (at-grade students are the WORST performers, 73.0%/16.6% XP, vs below-grade 83.2%/44.8%)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0092-student-ready-criticism-framework-2026-07-09.qmd",
     "lines": "25-27",
     "quote": "Include below-grade readers, English learners, keyboard-only users, screen-reader users, frustrated students, test-wise students, and students willing to click through or guess."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    49,
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat thresholds, cut scores and predicted difficulty as stated priors to be replaced with live response data, not as calibrated facts.",
   "kind": "adopted rule",
   "found_by": "Course repos and the assessment rules labelled cut scores and difficulty as defaults until real attempt data exists.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0008-alpha-courses-repo.qmd",
     "lines": "153-154",
     "quote": "cut-scores, mastery gates, WCPM targets are reasoned pilot defaults, to be tuned against real attempt data."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "97-98",
     "quote": "predicted difficulty is a prior with method, population, provenance, and uncertainty; live data must eventually replace it;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "36",
     "quote": "launch on Lexile priors, set `p_m_observed` after ~150-250 live responses"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make no claim that a course or test predicts an external score until a linking study with real students has been run.",
   "kind": "adopted rule",
   "found_by": "A test design kept its score-mapping claim pending a pilot; the engine refuses to output a predicted score until linked to real scores.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
     "lines": "64-65",
     "quote": "the 200-210 claim is by-design **pre-pilot** and confirms only after a linking study"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "40",
     "quote": "no RIT output; engine physically will not emit RIT until linked to real MAP scores."
    }
   ],
   "against": "Limit, kb-0086 line 39: simulation stats look strong (\"ability recovery r = 0.967 ... reliability 0.931\") but are self-reported simulation, not linking.",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Simulated students mostly echo the assumptions built into them; use them to stress-test a design, not to predict outcomes or effect sizes.",
   "kind": "measured",
   "found_by": "An engine's predicted fixes: 2 of 5 worked and 3 backfired; a literature summary found large simulations add no new information.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0010-amalgamation-v2-engine-results.qmd",
     "lines": "110",
     "quote": "2 of 5 recs delivered as predicted, 3 backfired — engine flagged why"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd",
     "lines": "74",
     "quote": "Running 100K simulated students yields **zero new information** — outputs are determined by the imposed math models + pre-training."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd",
     "lines": "23",
     "quote": "This is a deterministic design stress test and reproduction packet."
    }
   ],
   "against": "kb-0007 line 75: \"Teacher-as-predictor instead reaches r ≈ 0.72–0.79 population-level prediction across three independent research groups\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Confirm a score jump on the binding judge before believing it, and check whether part of the check simply stopped running.",
   "kind": "measured",
   "found_by": "An AP training jump from 0.29 to 0.95 existed only under a discredited judge; the fix behind it removed the stimulus so the leak probe was skipped.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "24-25",
     "quote": "On the **binding grader** it **collapsed to ~28%** (DBQ 0%, MCQ_SET 0%) and was logged as a **\"Gemini-judge artifact.\"**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "26-27",
     "quote": "it was **REMOVING the stimulus** so the grader's leak-probe is skipped. That's **grader-gaming**, not a provenance win."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "186-188",
     "quote": "reward inversion/Goodhart (a reworded canonical leak scored higher than a genuine requires-reading item under the shipped code)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Report quality from one clean attempt per item; numbers that include retries, best-of-several picks, repair or cached answers measure the process, not the maker.",
   "kind": "measured",
   "found_by": "An AP headline of 99% came from cache plus best-of-N; the later APUSH contract defined raw quality as one attempt.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "34-35",
     "quote": "The headline **\"99%\" was cache + best-of-N** — its own scoreboard flagged it as **\"NOT the model generating\" / \"not a verified 99%.\"**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "58-59",
     "quote": "Raw generator quality is `raw_k1`: one candidate, one attempt, no retry, reranking, repair, cache substitution, rejection sampling, best-of-N, or hidden human selection."
    }
   ],
   "against": "Limit, kb-0091 line 36: the delivered bank's quality came from \"discarding large volumes of plausible-looking output.\" Selection is legitimate for the bank, just not as maker quality.",
   "adds_to_existing": [
    65
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Validate the measuring tool before believing its numbers; harness bugs, missing keys and hardcoded constants have passed for content failures.",
   "kind": "measured",
   "found_by": "Weeks stuck at '28%' were four harness bugs; an auditor's 81/81 FAIL came from an arbitrary constant; most listen findings in one day came from the probe itself.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "36",
     "quote": "The **\"28%\" was four eval-harness bugs** — weeks burned on a measurement artifact, not a model failure."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "136-137",
     "quote": "the auditor's `thin_banks`/`enforcement_broken` FAIL (81/81) traced to an arbitrary `>=15` bank-depth constant hardcoded in `audit_compliance.py` itself"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "141-142",
     "quote": "the probe is often the bug (4 of 5 listen findings that day were probe-classes, not real defects)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    36,
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Do not let an automated judge block content until it catches every known failure, raises no false flags on clean controls, and is not confidently wrong.",
   "kind": "measured",
   "found_by": "A semantic-lint calibration missed cases and false-flagged controls (NO-GO); a vision judge hallucinated a confident fail; a structural rule was left unwired because it flagged approved content.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "64-65",
     "quote": "GO requires every in-scope case caught, zero false flags on controls, agreement >= 0.8. **NO-GO stands; semantic lints remain advisory.**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd",
     "lines": "76-77",
     "quote": "**the failure mode is confident wrongness, not incompleteness**, which is worse for an automated gate than an honest \"cannot tell.\""
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "83-85",
     "quote": "the function is retained unwired as evidence because both candidate forms flagged approved, reviewed content."
    }
   ],
   "against": "kb-0245 lines 77-79: \"It DID surface two plausible genuine findings no prior human round had filed ... real value, just not gate-strength yet.\"",
   "adds_to_existing": [
    9,
    37,
    38,
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Test every answer judge on empty, off-topic, keyword-stuffed and word-perfect answers before use.",
   "kind": "measured",
   "found_by": "Judges accepted empty answers, one fallback graded by keyword overlap, and an echo guard rejected a word-perfect recall.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "63",
     "quote": "oral/typed judges accept empty or content-blind answers."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "72",
     "quote": "The local evaluation fallback grades free responses by keyword overlap, and a porting note propagates that defect."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0229-closing-questions-build-2026-09-25.qmd",
     "lines": "78-79",
     "quote": "the gate was punishing the child for saying the taught sentence exactly."
    }
   ],
   "against": "Limit, kb-0229 line 96: \"117 judge cases authored, 114 OK/3 WRONG pre-fix (all three the echo class)\"",
   "adds_to_existing": [
    10,
    36,
    37
   ],
   "name_bearing_source": false
  },
  {
   "statement": "The same answer must get the same verdict every time; pin the judge to its most deterministic setting and reuse the verdict for identical resubmissions.",
   "kind": "measured",
   "found_by": "An identical typed answer got a different verdict on resubmit.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0238-l4-baseline-submission-and-signoff-packet-2026-08-31.qmd",
     "lines": "37-40",
     "quote": "fixed by running the first judging attempt at the most deterministic model setting and caching identical resubmits to return the same verdict instantly."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "After rebuilding items, run a behavioural sweep that submits right and wrong answers to the live scorer; checking that the file landed does not catch scoring bugs.",
   "kind": "measured",
   "found_by": "41 rebuilt items paid 0 for every answer; one match item would have accepted an incomplete response.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd",
     "lines": "235-236",
     "quote": "A behavioral sweep found 41 Unit-2 MCQs paying 0 for every answer because response processing compared `RESPONSE` against stale literal option text instead of the key id."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd",
     "lines": "180",
     "quote": "PUT/read-back catches XML landing, but behavioral scoring sweeps are needed for response-processing bugs."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
     "lines": "99-100",
     "quote": "right buckets keyed 2x with `match-max=1`, which would have let a spec-conformant renderer accept an incomplete response"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24,
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check narration against the printed words by machine transcript and by ear, with a person deciding on flagged clips, and bind each clip to its text so an edit marks it stale.",
   "kind": "measured",
   "found_by": "Clips without a text hash went silently stale after edits; machine transcripts mis-heard lines.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
     "lines": "29-31",
     "quote": "a text edit (e.g. a definition rewording) leaves the clip silently stale with nothing in the validator suite able to detect it"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0188-feedback-round-pipeline-end-to-end.qmd",
     "lines": "124-125",
     "quote": "written only if the transcript matches the printed line word-for-word"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0228-g3-listen-qa-transcript-receipts-2026-09-24.qmd",
     "lines": "43-44",
     "quote": "machine transcripts needing human disposition before any claim about audio quality is made from them"
    }
   ],
   "against": "kb-0217 lines 72-73: \"half of 'audio defects' were defective checks\". Checks can be wrong too.",
   "adds_to_existing": [
    21,
    24,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "What the voice says must match the printed words, except for deliberate differences that are recorded as such.",
   "kind": "adopted rule",
   "found_by": "A contract gate made spoken=printed a check; a probe falsely flagged a deliberate printed/spoken split.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "64",
     "quote": "audio truth (spoken=printed, clip-hash match, no \"Name:\" opener — speaker-label trap)"
    }
   ],
   "against": "kb-0213 lines 113-114: \"a deliberate printed/spoken split (printed \"ry,\" spoken \"ree\") was being flagged as a missing part-read\"",
   "adds_to_existing": [
    21,
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Everything a lesson tells students the text says, quoted or paraphrased, must be in the text; unquoted 'the text says' claims hide the worst errors.",
   "kind": "measured",
   "found_by": "An audit's one surviving CRITICAL was a printed recap inventing a cause the text never states.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
     "lines": "45-46",
     "quote": "\"Bored\" occurs exactly once in the whole lesson (this string) and zero times in any passage node."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "78-79",
     "quote": "ATTRIBUTED spans (no quotes, introduced by \"the story says\"/\"it says\" phrasing — the shape that hides the worst defects, since unquoted claims look like nothing)."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0205-g9-othello-1-1-kb-lesson-view.qmd",
     "lines": "45-46",
     "quote": "In the quote, Iago does follow Othello, only \"to serve my turn upon him\", so \"refusal\" may misstate the line."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    6,
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Turn each confirmed review finding into a reusable check for its whole class and sweep sibling content, so the same kind of defect is never found by hand twice.",
   "kind": "adopted rule",
   "found_by": "Reviewer-round discipline encoded classes as validators; one visual audit's four classes became a red-controlled walk.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0179-g3-peter-pan-close-out-state-and-reusable-process.qmd",
     "lines": "84-85",
     "quote": "encode the finding's CLASS as a reusable census/validator so the same shape of defect is never re-found by hand twice."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0216-codex-visual-audit-2026-09-07.qmd",
     "lines": "72-73",
     "quote": "so none of these four visual classes can regress silently again"
    }
   ],
   "against": "kb-0234 lines 83-85: a class rule \"was specified but is explicitly NOT shipped/wired\" because it flagged approved content.",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Verify audit findings before acting on them; about one in ten were false, many serious ones were refuted, and some fix lists were already stale.",
   "kind": "measured",
   "found_by": "Audit false-positive rate measured at 9%; 9 of 12 serious findings were refuted; 5 of 7 'not applied' fixes were already live.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "100-101",
     "quote": "audit false-positive rate **6/65 = 9%**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
     "lines": "9",
     "quote": "9 of 12 serious findings were refuted with evidence"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
     "lines": "90-91",
     "quote": "5 of 7 were already fixed live before this session (the FIX_LIST's \"not applied\" status was stale)"
    }
   ],
   "against": "kb-0245 lines 35-36: \"these are not rushed-tree findings, they are findings the team's OWN passing gate missed.\"",
   "adds_to_existing": [
    44,
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When guidance conflicts, build from the most specific named design for that lesson, cited exactly, rather than from general rules or a sibling lesson.",
   "kind": "adopted rule",
   "found_by": "Content disputes were settled by named design documents; a lesson built from general sources missed three designed components.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0179-g3-peter-pan-close-out-state-and-reusable-process.qmd",
     "lines": "67-69",
     "quote": "a named source-of-truth document per lesson-design decision, cited by paragraph number, beats \"mirror a sibling lesson\" or \"the portal's own text\" every time a content dispute comes up."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0210-aladdin-2508-feedback-and-pr27-safety-snapshots.qmd",
     "lines": "119-120",
     "quote": "both of those are real authorities but one tier too general."
    }
   ],
   "against": "kb-0218 line 70: \"recency/confidence/citation-count do not supersede an earlier academic decision\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Audit each built lesson against its design part by part; builds silently drop or adapt designed parts even when the text itself matches.",
   "kind": "measured",
   "found_by": "Closure audits found adapted rows outnumbering designed ones, missing components, and a never-authored lesson slot.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0226-g3-pre-submission-closure-audit-2026-09-24.qmd",
     "lines": "30-31",
     "quote": "adapted rows outnumber as-designed rows in every lesson"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0210-aladdin-2508-feedback-and-pr27-safety-snapshots.qmd",
     "lines": "120-121",
     "quote": "L4 as authored/reviewed/deployed was missing three components the design doc mandated"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0233-aug31-sweeps-prose-and-slotmap.qmd",
     "lines": "80-81",
     "quote": "**Slot 3, Aladdin Part 3, is MISSING outright** — spec slot real, design doc exists on disk, but no lessonId was ever authored/shipped for it."
    }
   ],
   "against": "kb-0218 lines 88-89: a programme-level gap was ruled \"an open scope question, not a defect.\"",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Name each concept, step and frame one way everywhere, and make a frame's wording match the thinking move it claims to teach.",
   "kind": "measured",
   "found_by": "Audits found step labels renamed between stages, words with two respellings, and frames whose wording did not match their declared procedure.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
     "lines": "55",
     "quote": "**MAJOR — we-do renames three of the four I-do step labels (R-KC-11).**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "104-106",
     "quote": "A lesson's frame wording must match its *declared* procedure — a FIND question dressed as INFER (or the reverse) is a defect, not style"
    }
   ],
   "against": "kb-0233 line 70: an aside-phrase family \"is legitimately varied, not robotic.\"",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A word taught for a text must appear in that text and recur later; target words should not overlap in meaning, and other hard words need support too.",
   "kind": "measured",
   "found_by": "A taught word never appeared in its passage; 7 of 9 taught words appeared only once; overlapping target words were rejected.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "74-76",
     "quote": "**Taught word \"betrayal\" never appears in the L1 passage**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "65-66",
     "quote": "vocab-earned (taught word recurs in-passage + later unit, from 7/9 taught words appearing only once)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "106",
     "quote": "Handle difficult words beyond the three designated vocabulary words."
    }
   ],
   "against": "kb-0224 lines 89-90: \"a taught word absent from the passage carries an `encapsulating {reason, authority}` exemption\"",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep the text, the live question and the steps visible while students work on them.",
   "kind": "adopted rule",
   "found_by": "Reviews found the passage hidden when students had to cite it and the steps scrolling away.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "86",
     "quote": "Prompts ask for textual evidence, but the passage is hidden when the student needs to cite it."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "84",
     "quote": "The steps and live question must remain visible, and the model should surface one thing at a time; the current screen contains too much at once."
    }
   ],
   "against": "Limit, kb-0180 lines 61-62: a passage page offers back \"every *earlier* part of the story only\"; later parts stay hidden.",
   "adds_to_existing": [
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Show students strong model responses, ideally at more than one level, before asking them to write their own, but never one that answers their own task.",
   "kind": "adopted rule",
   "found_by": "A review found no model of a strong response; a later knowledge base added three exemplars at different levels.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "87",
     "quote": "No model of a strong response is shown."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0203-g9-ela-cnu-academics-meeting-2026-10-01.qmd",
     "lines": "86-87",
     "quote": "**three exemplar responses** at different levels."
    }
   ],
   "against": "Limit, kb-0167 line 64: \"Replace independent tasks that reuse answer-bearing modeled evidence\"",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Model every step except the final thinking move and leave that to the student, and name steps by what a reader thinks or does, not by a gesture.",
   "kind": "adopted rule",
   "found_by": "Rulings fixed the modelling split and retired gesture-based step names.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "83-84",
     "quote": "the teacher models every step up to but not including the final substantive thinking move; the child does that move"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "96",
     "quote": "\"reread and tap\" -> \"reread and find\" (\"find\" names what a reader does, not what a finger does)."
    }
   ],
   "against": "kb-0226 lines 38-39: \"FIND I-do State hands the conclusion to the child ... instead of a complete modeled sentence\" was flagged as a gap.",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Do not teach shortcut rules that are false for many texts, and write questions specific to the text instead.",
   "kind": "adopted rule",
   "found_by": "Reviews rejected 'check against the title' and 'one sentence holds the answer'; a keyword-hunting step was retired.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "73",
     "quote": "Titles frequently do not state the main idea, so checking against the title is not a dependable rule."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "80",
     "quote": "The lesson may also embed the misconception that text evidence always points to one sentence."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "95",
     "quote": "retiring \"hunt for keywords\" (many texts have no clean keyword)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Close lessons with one idea used several times: state it, find it in the text, apply it to new text or a judgement, then recall it next lesson, with support fading and never returning.",
   "kind": "adopted rule",
   "found_by": "A closing-questions pattern was adopted for every lesson; the older-grade spec uses mimicry, application, evaluation.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "133-134",
     "quote": "The pattern, novice-to-expert on one idea moved three times, production only, no MCQ / word bank / tap-to-fill anywhere in the closing three:"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "268",
     "quote": "moving from mimicry, to application to the text, to evaluation at the end."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0225-g3-closing-questions-adoption-2026-09-24.qmd",
     "lines": "35",
     "quote": "support fades and never returns (max→frame→none)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40,
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before interpreting any assessment, declare its purpose and its full specification: knowledge, evidence, task conditions and scoring rule.",
   "kind": "adopted rule",
   "found_by": "Assessment-literature rules were routed into the course controls.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "84-85",
     "quote": "no KC, claim, evidence indicators, task conditions, outcome space, and scoring rule means no assessment;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "89-90",
     "quote": "declare whether a resource is formative, mastery, diagnostic, summative, or cold measurement before interpreting its result;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "132",
     "quote": "do not teach one cognitive operation and assess another."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write wrong options as plausible near-misses drawn from real errors, check that none is also right, and correct misconception lures afterwards because they can plant false knowledge.",
   "kind": "adopted rule",
   "found_by": "Filler distractors were flagged as a major defect; one repair produced a competing defensible answer.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "95-96",
     "quote": "potent misconception-based distractors require product-appropriate corrective feedback or post-test correction because plausible lures can seed false knowledge;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "69",
     "quote": "Chunk-stop distractors are self-declared filler, not real near-neighbour traps."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0134-g5-reading-v2-local-design-package.qmd",
     "lines": "104",
     "quote": "Independent review found an initial competing S07 plus S09 interpretation."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1,
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every interaction must work by keyboard and assistive technology and be readable; an item type that cannot be made accessible is also an unfaithful rehearsal of the real test.",
   "kind": "adopted rule",
   "found_by": "Drag and match items were not keyboard-operable; one item rendered black on black; accessibility was treated as a hard approval blocker.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "128",
     "quote": "An item type that cannot be made accessible is also not a faithful rehearsal of the test."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "105",
     "quote": "The Axolotl lesson's opening selection item rendered black text on a black background, legible only on hover."
    }
   ],
   "against": "Limit, kb-0076 line 21: the real test uses these formats too: \"MAP uses these for G3 — check MAP's implementation\"",
   "adds_to_existing": [
    27
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check what each filtering rule removes and what it concentrates; a leak filter removed recall items by design and pushed most survivors into the least accessible formats.",
   "kind": "measured",
   "found_by": "Domain-recall coverage fell to about 0; 525 of 772 kept items were technology-enhanced formats with no accessibility attestation.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "73-74",
     "quote": "KCT1 (domain-knowledge recall) is ~0 **by design** — passage-independent items are exactly what the anti-leak filter removes"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0085-g5-red-team-findings-2026-07-06.qmd",
     "lines": "25-26",
     "quote": "anti-leak concentrates items into TEI formats (525/772), no attestation."
    }
   ],
   "against": "kb-0089 line 182: a later lane \"disproved \"selected response is inherently leaky\"\"",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Optimise the course, not a tool's score; never reorder or reshape lessons to satisfy an aggregate metric.",
   "kind": "adopted rule",
   "found_by": "A ruling kept early checks as retrieval despite a reviewing tool's inference-share metric; a generator directive put course over item.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "122-123",
     "quote": "never move a check earlier to satisfy an aggregate percentage from a reviewing tool."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "102-103",
     "quote": "the correction is \"optimize the course, not the item\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Standards bound what to cover but give no teaching order; state each unit's key understanding in one plain sentence, link units by big ideas, and record why each prerequisite holds.",
   "kind": "adopted rule",
   "found_by": "Curriculum BrainLift rules and course-graph review.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "119",
     "quote": "- Standards constrain scope but do not provide a teachable sequence."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "52",
     "quote": "Make cross-unit links about big ideas rather than surface facts."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0122-g3-reading-course-graph.qmd",
     "lines": "28",
     "quote": "**Warrant tags:** logical (domain-intrinsic) / empirical (evidence-grounded) / conventional (designed/traditional)"
    }
   ],
   "against": "kb-0097 line 30: \"is \"lock one topic across many lessons\" the actual ask, or a misread?\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Choose topics with a visible scoring formula people can challenge, and record a reason whenever a person overrides the score.",
   "kind": "adopted rule",
   "found_by": "Topic scoring was the most praised feature because it can be tested.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "17",
     "quote": "They can challenge the weightings, inspect what falls out, and push on a decision they disagree with."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "18",
     "quote": "A person overrode the score and gave a reason rather than allowing the number to decide."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Screen every text that touches another subject against that subject's known misconceptions, and never present diagrams or models as literal reality.",
   "kind": "adopted rule",
   "found_by": "Misconception lists were routed into text review; a screen found 22 misconception hits across 8 lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "48",
     "quote": "apply the misconception-check process to every science-bearing Read/Write text;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "66",
     "quote": "- diagrams or models presented as literal reality;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0215-g5-media-recovery-plan-and-edullm-entrypoint-test.qmd",
     "lines": "84-85",
     "quote": "22 Tier-1 misconception hits across 8 lessons"
    }
   ],
   "against": "kb-0149 lines 34-35: no \"settled consensus science curriculum\" exists yet to check against.",
   "adds_to_existing": [
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a text overlaps a topic taught elsewhere in the same year, make it work in either order and take a fresh angle instead of duplicating it.",
   "kind": "adopted rule",
   "found_by": "Rules for re-encountering another subject's topics.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0149-draft-grade-5-science-ledger.qmd",
     "lines": "37-39",
     "quote": "a same-grade reading treatment must work whether the science lesson happened before or after it and should use a fresh angle rather than duplicate the proposed science treatment."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "45",
     "quote": "use prior-grade or sequencing-safe fresh-angle re-encounters;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A modelled inference may use only what the text shows plus knowledge students can be assumed to have; give only the background the text itself needs.",
   "kind": "adopted rule",
   "found_by": "A ruling struck a worked example that relied on outside cultural knowledge.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "81-82",
     "quote": "an inference may only use what the passage's own words show; extension deepens the mood from remaining text clues, never a civic/cultural fact the passage never gave."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "139",
     "quote": "Only context students will need in Act 1, not general history."
    }
   ],
   "against": "Limit, kb-0180 line 76: inference is defined as \"combine text clues with what you know\"",
   "adds_to_existing": [
    20
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Opening media and setup screens must not spoil or signal what is coming; test each line for whether it would still be true if the student never read the text.",
   "kind": "adopted rule",
   "found_by": "An opening image showed a character before the text introduced him; an intro-video review applied three tests to every line.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "69-70",
     "quote": "**L1 p8 opening image is a spoiler** (shows the stranger who doesn't enter the text until p10)."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0220-peter-pan-video-brief-and-screen-narratives.qmd",
     "lines": "27-28",
     "quote": "Removal test (would it still be true if the child never read the passage)."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0220-peter-pan-video-brief-and-screen-narratives.qmd",
     "lines": "23-24",
     "quote": "no question after the film may ask what happens next, because choosing what to repeat leaks which threads matter"
    }
   ],
   "against": "kb-0220 lines 45-47: the reviewers later \"agreed to reveal the plot and characters\"",
   "adds_to_existing": [
    3,
    21
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep instructional videos short and put required checks inside them; embedded questions reduce mind-wandering and improve recall.",
   "kind": "external research",
   "found_by": "Szpunar, Khan & Schacter 2013 PNAS https://www.pnas.org/doi/pdf/10.1073/pnas.1221764110; Guo, Kim & Rubin 2014 https://dl.acm.org/doi/10.1145/2556325.2566239",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd",
     "lines": "211-212",
     "quote": "Interpolated memory tests inserted into recorded lectures cut mind-wandering by roughly a third and improved recall versus uninterrupted video."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd",
     "lines": "144-145",
     "quote": "engagement drops sharply with length (students rarely watched past 9 min; recommend **≤6 min segments**)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "31",
     "quote": "If video carries essential context, interrupt it with mandatory quick checks so the learner does not watch a long unexamined clip."
    }
   ],
   "against": "kb-0248 lines 218-219: the check dosage \"is a reasonable extrapolation, not a directly tested parameter.\"",
   "adds_to_existing": [
    7,
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Whether comprehension checks should interrupt reading or come after it is unsettled: embedded tests helped recall in video, but inferential questions during reading cut recall in one study.",
   "kind": "open question",
   "found_by": "A design review flagged a reading study against the mid-passage checks in use.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
     "lines": "42-44",
     "quote": "interpolated inferential questions cut grade-4 recall .30->.07; her rule is ask AFTER not DURING reading"
    }
   ],
   "against": "kb-0248 lines 211-212: interpolated tests \"improved recall versus uninterrupted video.\"",
   "adds_to_existing": [
    7
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Avoid moving, speaking near-photoreal synthetic presenters: mismatched face, voice and motion read as fake and cut engagement while learning stays about the same; the guide's role matters more than how realistic it looks.",
   "kind": "external research",
   "found_by": "Video research files: IRRODL https://www.irrodl.org/index.php/irrodl/article/view/7815; Baylor & Kim https://doi.org/10.3233/irg-2005-15(2)02; Castro-Alonso et al. https://link.springer.com/article/10.1007/s10648-020-09587-1",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0202-g9-othello-video-research-fake-ai-attention.qmd",
     "lines": "36-37",
     "quote": "**Moving, speaking synthetic humans still read as fake.** The trigger is a mismatch between face, voice and motion, more than the level of realism"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0202-g9-othello-video-research-fake-ai-attention.qmd",
     "lines": "39",
     "quote": "**AI presenters show no reliable learning loss, but a real engagement and comfort loss**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd",
     "lines": "187-188",
     "quote": "Presence and role matter; realism of rendering does not."
    }
   ],
   "against": "kb-0248 line 37: participants rated \"the **realistic avatar as significantly more trustworthy**\"; lines 203-204: \"**cartoon-like scored worst**\"",
   "adds_to_existing": [
    22,
    52
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Turn full read-aloud off by default for fluent readers and show key terms instead of verbatim captions; keep read-aloud as an opt-in for weaker readers.",
   "kind": "external research",
   "found_by": "Adesope & Nesbit 2012 meta-analysis https://doi.org/10.1037/a0026147",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0250-g9-[name]-design-pr700-marisol-prototype.qmd",
     "lines": "578",
     "quote": "Showing extracted key terms beat verbatim spoken-plus-written."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
     "lines": "492-493",
     "quote": "visuals + spoken words beat visuals + printed words"
    }
   ],
   "against": "kb-0174 line 65: \"captions for Scout (headphones cannot be assumed)\"; kb-0136 line 107: make hard words readable aloud \"for students who cannot yet decode them.\"",
   "adds_to_existing": [
    53,
    54
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Open critical feedback with high standards and confidence the student can meet them, use autonomy-supporting language instead of directives, and offer a few meaningful choices.",
   "kind": "external research",
   "found_by": "Yeager et al. 2014 https://www.columbia.edu/cu/psychology/vpvaughns/assets/pdfs/Yeager_Breaking_the_Cycle_2013.pdf; Reeve & Jang 2006 https://selfdeterminationtheory.org/SDT/documents/2006_ReeveJang_JEP.pdf; Patall et al. 2008 https://doi.org/10.1037/0033-2909.134.2.270",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0250-g9-[name]-design-pr700-marisol-prototype.qmd",
     "lines": "514",
     "quote": "**1.3 \"Wise feedback\" (high standards plus \"I believe you can meet them\") makes students more likely to revise.**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0250-g9-[name]-design-pr700-marisol-prototype.qmd",
     "lines": "530",
     "quote": "Six predicted lower autonomy: holding onto the materials, showing or saying the answers, directives, \"should / got to\" statements, and controlling questions."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0250-g9-[name]-design-pr700-marisol-prototype.qmd",
     "lines": "601",
     "quote": "The effect was strongest with 2–4 successive choices and weaker for adults than for children."
    }
   ],
   "against": "kb-0250 line 532: \"Limits: lab study, preservice-teacher pairs, a 10-minute one-on-one session.\"",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Rewrite voice, register and feedback style for the students' age; mechanisms carry over between age groups, register does not.",
   "kind": "adopted rule",
   "found_by": "A build nearly shipped a young child's storytime voice for older content; a checklist separated register from mechanism.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0193-g3-book-grade-agnostic-vs-specific-g9-checklist.qmd",
     "lines": "122",
     "quote": "**Register/content differences are separate from mechanism differences.**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
     "lines": "959-961",
     "quote": "almost shipping a 10-year-old's storytime voice for salinity-gradient content — is the exact failure mode to avoid repeating at a larger age gap"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    2
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Whether a teaching approach built for younger students holds for older ones is untested; one older-grade trial is a probe, not proof.",
   "kind": "open question",
   "found_by": "Service meeting record; high-school reading was called a complete unknown.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0130-incept-service-coe-catchup-2026-07-15.qmd",
     "lines": "177",
     "quote": "Do not describe this pedagogy or the trained model as grade-agnostic. Grade 6 is a probe, not proof."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Never tell students something untrue about the interaction: no pretend listening, no receipts for actions they did not take, and help-assisted completion is never shown as solo success.",
   "kind": "adopted rule",
   "found_by": "A build audit found a welcome that faked listening and a receipt claiming events that never happened.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "70",
     "quote": "The welcome beat overclaims contingent listening while still issuing a static, answer-independent recast"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "71",
     "quote": "The receipt screen asserts out-loud/self-done events that did not actually happen on the typed/floor interaction paths."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "99",
     "quote": "framed as help, never \"solo pass\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    14
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Independent work must use different evidence from the modelled example; reusing the model's evidence turns it into copying.",
   "kind": "adopted rule",
   "found_by": "An independent audit blocked tasks reusing modelled evidence; a design locks students out of the guided quote.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "64",
     "quote": "Replace independent tasks that reuse answer-bearing modeled evidence in Lessons 1, 3, and 6."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0205-g9-othello-1-1-kb-lesson-view.qmd",
     "lines": "32",
     "quote": "**\"students are locked out of writing about the guided practice quote\"**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    3,
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Send the student's device only student material; answer keys and scoring stay on the server.",
   "kind": "adopted rule",
   "found_by": "App compliance rules and an APUSH audit's student-only projection.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0060-incept-read-app-field-notebook.qmd",
     "lines": "39-40",
     "quote": "The client must **never** extract the answer key, compute score/mastery/XP/accuracy/advancement"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "71-72",
     "quote": "Define a student-only source projection containing `student_material` plus approved citation metadata, excluding teacher-only answer-bearing fields."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Review the student view through a dedicated test-student account, never by impersonating a real child.",
   "kind": "adopted rule",
   "found_by": "The only route to the real render listed real student accounts; that line was not crossed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0241-alpha-read-contract-investigation-and-packager-build-2026-06.qmd",
     "lines": "123-124",
     "quote": "provision a dedicated sandbox test-student account and impersonate that, never a real child."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Clear rights for every text, clip and image before building on it; a licence to view is not a licence to excerpt or embed, and open licences carry conditions.",
   "kind": "adopted rule",
   "found_by": "Licensing research for productions and the source text.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0202-g9-othello-video-research-fake-ai-attention.qmd",
     "lines": "56",
     "quote": "every published licence found grants platform viewing, **not clip extraction or embedding in another app**."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "65",
     "quote": "Confirm receipt, rights, and permitted use before placing any material in a training corpus."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Pin one edition of a source text and check every quote, line reference and stated fact against it, not against memory.",
   "kind": "measured",
   "found_by": "A line cited as 45 is 43 in another edition and unnumbered in others; a script fact was overstated.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
     "lines": "38-39",
     "quote": "Open Source Shakespeare numbers it 43, and Gutenberg and MIT have no numbers. Pin the edition to Folger."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "393",
     "quote": "All quotes need checking against the chosen edition."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    16,
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Prefer authentic, well-written texts for literature over machine-written stories, and never label machine-written texts as real sources.",
   "kind": "adopted rule",
   "found_by": "A ruling put real texts first; an insight note warned against relabelling machine-authored passages.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0198-meetings-decisions-timeline-0819-1001.qmd",
     "lines": "29-30",
     "quote": "LLM-generated fiction \"is never going to be great\"; real, split-into-parts texts are the priority"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "44-45",
     "quote": "don't relabel machine-authored cold passages as \"real.\""
    }
   ],
   "against": "kb-0064 lines 41-42: machine-authored unseen passages still served as cold tests.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Build and fully review one or two lessons by hand first and make them the template; expect the procedure to change once it is actually run.",
   "kind": "adopted rule",
   "found_by": "An agreed handcraft-first decision and a template-lesson rule.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0076-coe-catchup-2026-06-30.qmd",
     "lines": "16",
     "quote": "**Handcraft first, automate later** — manually craft the first 1–2 courses to set the quality bars/guardrails before the full automated pipeline."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
     "lines": "596-597",
     "quote": "the template lesson is not a planning document — it is the first fully-built, fully-reviewed lesson"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    47
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Calibrate production estimates on a representative unit, not the easiest, and when a quality gate is missed move the date, not the gate.",
   "kind": "adopted rule",
   "found_by": "A delivery calibration plan.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0129-g5-delivery-sequence-and-eta-calibration.qmd",
     "lines": "126-127",
     "quote": "Choose a representative unit, not the easiest one."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0129-g5-delivery-sequence-and-eta-calibration.qmd",
     "lines": "47",
     "quote": "A missed gate changes the date, never the gate."
    }
   ],
   "against": "kb-0063 line 22: an AP bar was \"**Softened 04-27 → 04-28**\".",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Take every count in every document from one dated pull and recheck after each fix; a green consistency linter still misses stale numbers.",
   "kind": "measured",
   "found_by": "A course's own documents disagreed on lesson and item counts; stragglers survived green linter runs.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "136",
     "quote": "The course's own materials disagree with each other."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
     "lines": "46-47",
     "quote": "Every count in every doc must trace to one named pull with a date"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd",
     "lines": "260",
     "quote": "A green linter is necessary, not sufficient."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "State each result with its verification level and named gaps, never as a bare pass, and never average separate readiness gates into one score.",
   "kind": "adopted rule",
   "found_by": "Honesty rules in submission packs; an APUSH completion ledger with separate gates.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
     "lines": "63",
     "quote": "verdicts are PASS-with-named-gaps, never bare PASS."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0171-apush-full-course-local-authoring-review-hub-archive.qmd",
     "lines": "50",
     "quote": "Do not average the independent readiness gates into a fake single quality score."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0009-timeback-alpha-read-packager.qmd",
     "lines": "107-108",
     "quote": "`[OPEN]` not yet verified."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44,
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before counting two findings as independent confirmation, check that they did not come from the same source or the same model.",
   "kind": "adopted rule",
   "found_by": "A claimed two-project convergence was one author importing AP findings; resample agreement was self-consistency.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "29-30",
     "quote": "it's **one author importing AP findings onto grade-3**, not two teams replicating independently."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0221-early-planning-history-and-sep22-snapshots.qmd",
     "lines": "55-56",
     "quote": "re-label the anti-leak engine MEASURED-in-history/UNTESTED-in-reading"
    }
   ],
   "against": "kb-0242 lines 32-34: duplicates were \"KEPT, not deduped, because repetition across sources is evidence of cross-authority consensus\"",
   "adds_to_existing": [
    35,
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "What counts as a leak depends on the skill: if finding information in the text is the skill, an answer stated in the text is not a leak, but a question meant to need inference must not have its conclusion stated outright.",
   "kind": "measured",
   "found_by": "The reading leak control deliberately skipped the history-style source check; an inference-integrity probe found 1 of 18 conclusions stated outright.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "26-27",
     "quote": "in reading, finding the answer in the passage IS the skill, so the usual history-style \"answer is in the source\" leak check is deliberately skipped."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0231-pp-depth-6h-doc-diffs.qmd",
     "lines": "75-76",
     "quote": "stating the trait/conclusion itself is a disguised-FIND violation)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Aim checks at the detail the lesson's idea turns on, not an incidental detail.",
   "kind": "adopted rule",
   "found_by": "A check asked about a coin instead of the detail the theme depends on; a spot-check found two incidental checks.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
     "lines": "58-59",
     "quote": "are our part-checks about the thematic hinge, not an incidental detail?"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
     "lines": "448",
     "quote": "It keeps the learning question anchored to one small, specific quotation rather than the whole scene"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    7,
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check cross-references in both directions: a question must not depend on anything not yet read, and a later lesson must not point back to content students never met.",
   "kind": "adopted rule",
   "found_by": "A forward-reference check and a cross-lesson dependency found in closing questions.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "86-87",
     "quote": "a question/option/hint on page N must not depend on a concrete story noun the child has not read yet"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0225-g3-closing-questions-adoption-2026-09-24.qmd",
     "lines": "60",
     "quote": "or WITW points at content the child never met."
    }
   ],
   "against": "kb-0234 lines 88-89: the check \"explicitly excludes taught vocabulary and invented practice scenarios from false-positiving.\"",
   "adds_to_existing": [
    7
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Fill-in frames must stay grammatical for every word a student might put in; check frames with substitutions.",
   "kind": "measured",
   "found_by": "A frame turned ungrammatical with the student's word, and no validator checked fit under substitution.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0238-l4-baseline-submission-and-signoff-packet-2026-08-31.qmd",
     "lines": "35-36",
     "quote": "which stays grammatical regardless of the filling word."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd",
     "lines": "38-40",
     "quote": "no validator in `validate-contracts.mjs` checks a lead's grammatical fit under substitution"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Proofread every student-facing string, especially model answers students imitate; validators missed grammar slips, repeated stock openers and other machine-writing tells.",
   "kind": "measured",
   "found_by": "Sweeps found a grammar error repeated at 5 paths in a model answer and 11 identical openers; none was caught by validators.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0233-aug31-sweeps-prose-and-slotmap.qmd",
     "lines": "63-64",
     "quote": "**F4 (structural AI-tell):** every U1 lesson's think-aloud opens with the identical clause \"I am hunting for...\" (7x)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0233-aug31-sweeps-prose-and-slotmap.qmd",
     "lines": "10",
     "quote": "none of which any current validator catches"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "88",
     "quote": "Some word-bank prompts misuse vocabulary and read as unedited AI output."
    }
   ],
   "against": "kb-0233 lines 68-69: \"18 a/an \"violations\" all false positives\"",
   "adds_to_existing": [
    2,
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "For generated pictures, fix characters and recurring places with references, state exact object counts, and settle borderline cases with several independent reads and a majority.",
   "kind": "measured",
   "found_by": "Art QA found the model cannot count objects and places drift; single reads of near-photoreal faces flipped.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "137-138",
     "quote": "the model cannot count objects in generated art (needs EXACTLY-N enumerated in the scene line)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "140-141",
     "quote": "pin recurring locations/mediums or they drift"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0219-watch-48h-and-art-qa-redcontrol.qmd",
     "lines": "91-92",
     "quote": "any near-photoreal human face now requires three independent reads with majority rule, not a single pass."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    22,
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Media must fail closed: a missing clip plays as silence with captions, never an automatic synthetic substitute, and packaging rejects absent or mismatched files.",
   "kind": "adopted rule",
   "found_by": "A media recovery plan and a quota outage set fail-closed rules; one generator silently fell back to the wrong voice.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0215-g5-media-recovery-plan-and-edullm-entrypoint-test.qmd",
     "lines": "31-33",
     "quote": "rejects absent/duplicate/digest-mismatched clips, no browser-TTS fallback in the renderer"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "126-127",
     "quote": "a missing clip renders as silence + captions, never browser TTS or synthetic voice."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0227-g3-branch-hygiene-pr634-prep-2026-09-24.qmd",
     "lines": "68-69",
     "quote": "so the generator fell through to the narrator"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    36,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Teach new material in blocks and mix it with other material only once it is held; teach easily confused pairs explicitly and mix them after both are learned.",
   "kind": "adopted rule",
   "found_by": "Practice BrainLift rules and the course graph.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "160",
     "quote": "- Interleaving is only appropriate after the skill is ready; massed/blocked first, interleaved later."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0122-g3-reading-course-graph.qmd",
     "lines": "53",
     "quote": "**Gateway discriminations** (taught explicitly, interleaved after both learned)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Correct errors immediately and briefly, retest after other items, and give less feedback as proficiency grows.",
   "kind": "adopted rule",
   "found_by": "Direct-instruction and practice rules.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "143",
     "quote": "- Error correction should be immediate and brief: correct, test, give intervening items, then retest later."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "161",
     "quote": "- Too much feedback can reduce active processing; feedback timing should shift as proficiency improves."
    }
   ],
   "against": "kb-0172 line 43: \"an immediately available hint lowers desirable difficulty. The durable rule is attempt first, then targeted help.\"",
   "adds_to_existing": [
    1,
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep several strands running, only one introducing new material while the rest review (around nine parts review to one part new).",
   "kind": "adopted rule",
   "found_by": "Direct-instruction rules and a course-building skill.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "145",
     "quote": "- Keep multiple tracks alive over time; only one track should introduce new material while the rest is review."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd",
     "lines": "43",
     "quote": "lesson composition as interleaved tracks at ~90:10 review:new"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Teach concepts with clear examples and non-examples that differ in one feature, and stretch strong answers by asking for an original example.",
   "kind": "adopted rule",
   "found_by": "Direct-instruction rules and a spoken vocabulary routine.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "144",
     "quote": "- Start with clear examples/non-examples and systematically vary examples using set-up/difference/sameness principles."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "47",
     "quote": "imprecise oral definitions receive concrete examples and non-examples; strong answers are extended by asking for an original example."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give every activity and screen a short written rationale: the knowledge type and target performance, the failure it guards against, and when its scaffold is withdrawn.",
   "kind": "adopted rule",
   "found_by": "Generic-instruction rules; screen narratives replaced pass/fail checklists for review.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "134",
     "quote": "- Any activity needs a rationale: target knowledge type, performance, failure mode it protects against, why this activity, and scaffold retirement condition."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0220-peter-pan-video-brief-and-screen-narratives.qmd",
     "lines": "61-62",
     "quote": "every submitted screen should carry a short why-built-this-way narrative instead of a pass/fail checklist"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Include tasks that make students select, combine and justify what they learned, and define the final performance by exemplars and a rubric instead of splitting it into ever smaller parts.",
   "kind": "adopted rule",
   "found_by": "Curriculum rules and the course graph's capstone; a build had no check requiring both sources.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "123",
     "quote": "- Integrative lessons matter: students can master parts and still fail when asked to select, combine, or justify them in context."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0122-g3-reading-course-graph.qmd",
     "lines": "76",
     "quote": "defined by exemplars+rubric, NOT decomposed further"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    41,
    56
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Engagement features may shape framing, tone and setting but must never weaken what a scored item measures.",
   "kind": "adopted rule",
   "found_by": "A proposal bake-off named this as an invariant.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0244-g3-proposal-bakeoff-seven-proposals-2026-06-15.qmd",
     "lines": "98-99",
     "quote": "hooks may shape stimulus/framing/tone but may never weaken a scored item's construct."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    51
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Sort review feedback into proven defects, compatible refinements, conflicts of direction and insufficient evidence, and log contradictions found in the rules themselves.",
   "kind": "adopted rule",
   "found_by": "A change-control baseline; an audit found a live contradiction between a rule and its validator.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
     "lines": "70-74",
     "quote": "**insufficient evidence** (stays explicitly unresolved)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
     "lines": "103-105",
     "quote": "*requires* the \"Step N: ...\" numbered format and fails any node without it"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Compare against a baseline measured on items as hard as the target; a baseline from easy-distractor items overstates performance.",
   "kind": "measured",
   "found_by": "An 83% baseline was corrected as measured with the wrong instrument.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0221-early-planning-history-and-sep22-snapshots.qmd",
     "lines": "74-75",
     "quote": "re-measure the 83% baseline on hard/near-neighbour items, not the incumbent's easy-distractor items;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "41",
     "quote": "the wrong-instrument correction of the 83% baseline."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Screen generated texts for age-appropriateness and reading level, and check the generator's own settings.",
   "kind": "measured",
   "found_by": "A generator was set for a much older grade; passages leaked advanced vocabulary; 43 of 48 passages failed a text screen.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0221-early-planning-history-and-sep22-snapshots.qmd",
     "lines": "76-77",
     "quote": "add an age-appropriateness check to the team rubric, fix a grade-11-to-grade-3 setting found in the code;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0008-alpha-courses-repo.qmd",
     "lines": "147",
     "quote": "fluency passages regenerated after a first pass leaked Tier-3 vocabulary"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Choose texts for purpose, genre and quality as well as a difficulty number; difficulty formulas mishandle poetry and narrative and cannot tell whether a text is worth reading.",
   "kind": "adopted rule",
   "found_by": "A course whose texts were selected by readability number alone.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "76",
     "quote": "Lexile alone also mishandles poetry and narrative and cannot tell you whether a text is worth reading."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Practise at the length and demands of the real task; short passages alone never build the stamina that long and paired texts need.",
   "kind": "adopted rule",
   "found_by": "Course passages averaged about 166 words against test sets of thousands.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "94",
     "quote": "Practising only on very short texts does not build that stamina."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Set a purpose before reading, let students read the whole text first, then model beside the text, and never model the thinking as if it were easy.",
   "kind": "adopted rule",
   "found_by": "A review of showcase lessons; the rulings that followed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "61",
     "quote": "Children need a reason to read before they start"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "28-29",
     "quote": "the child reads the *whole* passage before anything is modelled, and the modelling moment happens *beside* the passage"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "64",
     "quote": "The model should show that selecting the relevant animal and adaptation is genuinely difficult."
    }
   ],
   "against": "kb-0172 line 39: \"do not make whole-text repetition a universal ritual.\"",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Use comparison and error-spotting as guided practice: pick the better of two responses and say why, or stop a model answer at a deliberately planted error and fix it.",
   "kind": "external research",
   "found_by": "McLaren, Adams & Mayer 2015, DOI 10.1007/s40593-015-0064-x; Pollitt 2012 https://doi.org/10.1080/0969594X.2012.665354",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "250",
     "quote": "Students see two responses side by side, pick the one that better answers the learning question, and explain why."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
     "lines": "305",
     "quote": "confirms the delayed-test advantage of erroneous examples."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "391",
     "quote": "So that errors are designed on purpose, not improvised."
    }
   ],
   "against": "kb-0204 line 392: \"In the research, \"faded examples\" usually means steps removed for the learner to complete.\"",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Structure discussion: give thinking or writing time before calling on anyone, track who has spoken, prefer scripted argue-both-sides sequences to open debate, and make students produce the final synthesis alone.",
   "kind": "external research",
   "found_by": "Dallimore et al. 2013 https://journals.sagepub.com/doi/abs/10.1177/1052562912446067; Johnson & Johnson 2009 https://doi.org/10.3102/0013189x08330540",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
     "lines": "124-125",
     "quote": "(1) think/write time before calling on anyone; (2) track who's been called against the roster"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
     "lines": "263",
     "quote": "**4. Structured, scripted argument beats open debate; open debate beats none.**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
     "lines": "324-325",
     "quote": "both argue for a mandatory \"you-do\" synthesis turn the student alone produces."
    }
   ],
   "against": "kb-0249 lines 126-127: \"**Quasi-experimental, peer-reviewed** for the core effect (adult sample, not remote)\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Whether an AI tutor or critic voice abandons a correct position under pressure from a student is untested; sycophancy is a known risk.",
   "kind": "open question",
   "found_by": "Research file; simulated-tutoring study https://arxiv.org/abs/2506.10297",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
     "lines": "328-329",
     "quote": "Untested anywhere found: whether a \"critic\" voice in a multi-agent panel softens its disagreement under social pressure from the student — flag as an open risk."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Scores on pedagogy-knowledge benchmarks do not show teaching quality or learning; whether they predict either is untested.",
   "kind": "open question",
   "found_by": "Corrections in two service meeting records.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0127-incept-service-coe-catchup-2026-07-14.qmd",
     "lines": "94",
     "quote": "pedagogical-knowledge benchmark performance is not proof of teaching quality."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0130-incept-service-coe-catchup-2026-07-15.qmd",
     "lines": "136-137",
     "quote": "Neither dataset size nor CDPK performance establishes effective generated instruction or student learning."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Whether to label media as machine-made is unresolved: most teens want labels, but labels tend to lower trust in instructional content.",
   "kind": "open question",
   "found_by": "Video research surveys and disclosure experiments.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd",
     "lines": "224-225",
     "quote": "**73% of teens want AI-generated content clearly labeled or watermarked**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd",
     "lines": "71-72",
     "quote": "disclosure/labeling is not a free action."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Avoid a live self-view camera during learning; seeing oneself raised appearance anxiety, which lowered recall.",
   "kind": "external research",
   "found_by": "Tien, Imundo & Bjork 2023 (secondary report https://www.psypost.org/having-camera-on-during-online-classes-increases-social-appearance-anxiety-which-decreases-learning-of-students/)",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
     "lines": "96-97",
     "quote": "that anxiety, not camera status itself, mediated lower lecture recall."
    }
   ],
   "against": "kb-0249 line 98: \"(university sample; generalization to 14–15s is inferential)\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "How students are placed into levels (assigned, diagnosed or self-chosen) must be settled before level-specific content is built; the best method is unresolved.",
   "kind": "open question",
   "found_by": "Listed as a decision needed before build.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "385",
     "quote": "Needed before build, because it drives the learning question screen."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Rewards should follow focused time or verified mastery, never raw answer counts.",
   "kind": "adopted rule",
   "found_by": "An app was found fabricating points per correct answer; the later contract removed per-answer points.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0060-incept-read-app-field-notebook.qmd",
     "lines": "52-53",
     "quote": "The broker previously **fabricated** quiz XP (`correct × 3`, no 80% floor, not time-based"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd",
     "lines": "31-32",
     "quote": "no per-answer XP; preview XP once at finish; 1 XP per whole focused minute; 90% checkpoint"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When comparing versions, score them blind to which version or maker produced each, and keep tuning and calibration examples out of the final evaluation.",
   "kind": "adopted rule",
   "found_by": "A preregistered pedagogy-policy experiment protocol.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0132-eppc-bias-experiment-execution-handover.qmd",
     "lines": "568-569",
     "quote": "Scorers never see arm, model, prompt, cost, or other scorer labels."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0132-eppc-bias-experiment-execution-handover.qmd",
     "lines": "566",
     "quote": "calibration items never enter pilot/final."
    }
   ],
   "against": "kb-0132 line 12: \"The handover is ready; the experiment has not run.\"",
   "adds_to_existing": [
    43,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count an item bank by exact-unique items that passed independent checks; gross generated rows overstate it, and generated items stay candidates until they pass.",
   "kind": "measured",
   "found_by": "An APUSH corpus of 143,026 rows held 49,571 unique and 0 certified items; 28% of one pool was duplicate copies.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "78",
     "quote": "The 100,000 unique/usable-sample claim is therefore rejected."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "48-49",
     "quote": "340 stem clusters duplicated (2,233 excess copies, 28% of pool)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "87-89",
     "quote": "None bypasses source identity, current-format, factuality, answerability, independence, or human review gates."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check claimed external requirements against the official text before building on them.",
   "kind": "measured",
   "found_by": "A spec called a text mandatory; the official rule names other texts.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
     "lines": "36-37",
     "quote": "The spec's \"TEA mandatory literary works list\" wording overstates it; Othello is the course's own choice."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
   "lines": "94-95",
   "quote": "all 13 MCQs carry exactly 4 options with index-aligned feedback and no wrong-answer feedback names the key"
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
   "lines": "263",
   "quote": "Show students where to look in the text, and revisit previous knowledge to spark connections."
  },
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
   "lines": "52",
   "quote": "replace the binary feedback with corrective feedback that explains why an answer is right or wrong."
  },
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
   "lines": "524-525",
   "quote": "one stable voice per \"expert\" across the whole exchange; tune for register-matched, moderate prosody, not maximum expressiveness"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0224-g3-dialogue-branches-pace-gate-roll-forward-2026-09-22-23.qmd",
   "lines": "57",
   "quote": "our L4 silent branch was at **1.00** overlap (verbatim echo)"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0225-g3-closing-questions-adoption-2026-09-24.qmd",
   "lines": "95-96",
   "quote": "every node whose gate/rubric/magic-word demands the taught word prints it nowhere in its stem/instruction/hints."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "68",
   "quote": "The \"Dashed Line\" beat pre-teaches its own check on the same screen."
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0225-g3-closing-questions-adoption-2026-09-24.qmd",
   "lines": "37",
   "quote": "failure is cheap (two attempts, warm reveal, never loop)"
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0224-g3-dialogue-branches-pace-gate-roll-forward-2026-09-22-23.qmd",
   "lines": "86-88",
   "quote": "single-select mcq never reveals the answer (R-Q-24, logged as a contradiction awaiting the author's ruling since it departs from \"two attempts then reveal\")"
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
   "lines": "614-615",
   "quote": "every free-text written answer except the closing questions gets ten [tries]"
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0220-peter-pan-video-brief-and-screen-narratives.qmd",
   "lines": "91-92",
   "quote": "every other open-response node across all four lessons caps at 3 tries"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
   "lines": "172-173",
   "quote": "Measured lesson: control-pass rate did not predict blind certifiability."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
   "lines": "30-31",
   "quote": "`novelty:\"unseen\"` guarantees the passage is new; it does NOT guarantee passage-dependence"
  },
  {
   "truth": 5,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0221-early-planning-history-and-sep22-snapshots.qmd",
   "lines": "78",
   "quote": "(5) treat anti-leak as a build-time lint for reading, not a deep guarantee."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
   "lines": "146-147",
   "quote": "The 417 with-passage control failures were often ambiguity or broad `Both` keying, not necessarily blind leakage."
  },
  {
   "truth": 7,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
   "lines": "42-44",
   "quote": "interpolated inferential questions cut grade-4 recall .30->.07; her rule is ask AFTER not DURING reading"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
   "lines": "50-51",
   "quote": "**answer-position bias fixed** (correct answers were ~75% option \"A\" → shuffled ~even A/B/C/D)"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
   "lines": "56",
   "quote": "Key-position/length balance needs an authoring-time check (12/19 A-keys shipped before the lens)."
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0215-g5-media-recovery-plan-and-edullm-entrypoint-test.qmd",
   "lines": "101-102",
   "quote": "correctly routes missing evidence to `NOT_EVALUABLE` instead of guessing"
  },
  {
   "truth": 9,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
   "lines": "44-45",
   "quote": "the sealed rule had ignored those hits because the solver reported low confidence."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0225-g3-closing-questions-adoption-2026-09-24.qmd",
   "lines": "36",
   "quote": "no string matching (judge on rubric meaning)"
  },
  {
   "truth": 10,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
   "lines": "25",
   "quote": "Misspelled \"magician\" marked correct; decide a comprehension spelling policy"
  },
  {
   "truth": 16,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
   "lines": "38-39",
   "quote": "Open Source Shakespeare numbers it 43, and Gutenberg and MIT have no numbers."
  },
  {
   "truth": 16,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
   "lines": "60-61",
   "quote": "never a position (`?page=n` rotted once already when a lesson grew a page)"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd",
   "lines": "70",
   "quote": "exact-quote grading must fail closed (a botched quote was accepted)"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
   "lines": "330-331",
   "quote": "roughly two-thirds of ChatGPT-generated bibliographic citations invented or wrong"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0067-g5-generator-pilot-intake-and-team-async-2026-06-23.qmd",
   "lines": "275",
   "quote": "The adapter only marks Part B as evidence if the option text resolves against the stimulus text."
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "59",
   "quote": "\"producer\"/\"habitat\" are deep-taught as if they were blocking vocabulary (they aren't)."
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0220-peter-pan-video-brief-and-screen-narratives.qmd",
   "lines": "19-20",
   "quote": "three-channel word stamping (`nursery`, `revenge`, `cutlass`, `hull`, `rigging` — heard, on-screen text, and pictured together)"
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
   "lines": "532-533",
   "quote": "**The specific comics failure is cross-panel drift, not single-panel flaws.**"
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
   "lines": "110-111",
   "quote": "each split into single-question pages/cases, all verbatim quoted options preserved"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
   "lines": "95-96",
   "quote": "`validate-assets`, voice-provenance and voiceover-sync were all green because none of them opens the file."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0176-g3-peter-pan-pr-timeline.qmd",
   "lines": "53",
   "quote": "Every deploy was proven by **hashing the served file**, never by a 200 response"
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
   "lines": "39",
   "quote": "\"remove Scout's interjections at the top of each page. They take away from the reading flow.\""
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd",
   "lines": "62-63",
   "quote": "one attention target at a time; only the current sentence highlighted."
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "67",
   "quote": "The diagram is not element-addressable and has no accessible table equivalent."
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
   "lines": "19-20",
   "quote": "the closing comprehension check was silently optional while every sibling page gates."
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
   "lines": "130",
   "quote": "skippable \"pause and think\" is not a check."
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd",
   "lines": "69-70",
   "quote": "the judged screenshot never contained the defect's gated UI node at all -- a pass that proves nothing"
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0219-watch-48h-and-art-qa-redcontrol.qmd",
   "lines": "83-84",
   "quote": "confirming single-read verdicts on near-photoreal humans are unstable."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
   "lines": "83-84",
   "quote": "same-model resamples (agreement = self-consistency, not cross-family agreement)"
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0186-scope-lane-and-model-routing-rules.qmd",
   "lines": "82-84",
   "quote": "a probe route was found to return 200 with `{\"ok\":false}` when the key was missing, serving keyless for roughly 11 hours undetected"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0229-closing-questions-build-2026-09-25.qmd",
   "lines": "96",
   "quote": "117 judge cases authored, 114 OK/3 WRONG pre-fix (all three the echo class)"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
   "lines": "97-98",
   "quote": "invariant (ID3 tag or frame sync in the first bytes), red-controlled 11→0."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0219-watch-48h-and-art-qa-redcontrol.qmd",
   "lines": "74-75",
   "quote": "prove the new check discriminates (fires on AI-generated film-frame humans, stays quiet on drawn children) *before* judging"
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd",
   "lines": "67",
   "quote": "Prepare knowledge -> encounter text -> model thinking -> guided same-process practice -> student articulation -> evidence check -> delayed/varied transfer"
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0083-clone-lessons-inceptbench-results-2026-07-02-eval-summary.qmd",
   "lines": "64",
   "quote": "Q4, Q9, Q12, and Q13 all ask why ice floats."
  },
  {
   "truth": 42,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0089-parent-claude-sessions-worklog-2026-07-09.qmd",
   "lines": "256",
   "quote": "- rule that downstream invariants must be recomputed after any fix wave."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
   "lines": "23",
   "quote": "machine checks do not approve content."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
   "lines": "55-56",
   "quote": "That green state is not the semantic verdict."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
   "lines": "149-151",
   "quote": "is not the same as truly ready"
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
   "lines": "18",
   "quote": "## What's REQUIRED (the bar — and it moved)"
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
   "lines": "54-55",
   "quote": "the live-rendered surface must be reviewed, not just source artifacts."
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0009-timeback-alpha-read-packager.qmd",
   "lines": "116-117",
   "quote": "They push fine (201, valid QTI, GET 200) but the quiz body is empty"
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0216-codex-visual-audit-2026-09-07.qmd",
   "lines": "44-45",
   "quote": "the content-check battery is desktop-only, so all three classes were invisible to it"
  },
  {
   "truth": 47,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0219-watch-48h-and-art-qa-redcontrol.qmd",
   "lines": "37-38",
   "quote": "exit codes showed 0 but masked real FAIL counts (L4 14, L5 16, L6 6, L7 4)"
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
   "lines": "149",
   "quote": "A same-day lesson gate proves at most \"I can do it now,\" not \"I can still do it later under changed conditions.\""
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0244-g3-proposal-bakeoff-seven-proposals-2026-06-15.qmd",
   "lines": "80-81",
   "quote": "inference was 5x undercounted by the live heuristic (actually 9.7%, not the 2% other proposals cited)"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
   "lines": "146-147",
   "quote": "clip basenames repeat across lessons so hash edits must match the full lesson path, never the bare basename."
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd",
   "lines": "45",
   "quote": "**No significant difference in academic performance** between AI and human instructor conditions. **Video engagement was higher with the human instructor.**"
  },
  {
   "truth": 52,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
   "lines": "508-509",
   "quote": "switching static images as defensible, not proven-superior**, to video on learning grounds alone."
  },
  {
   "truth": 53,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd",
   "lines": "65",
   "quote": "captions for Scout (headphones cannot be assumed)"
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
   "lines": "651-652",
   "quote": "after 4 wrong taps, Scout (the guide) offers to find the remaining clues"
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
   "lines": "335-336",
   "quote": "**This is the single highest-confidence risk in this file** — a general, high-base-rate LLM property, not a possibility."
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
   "lines": "38-40",
   "quote": "water-cycle items were bound to an unrelated pistol-shrimp passage"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
   "lines": "30-31",
   "quote": "a **CRITICAL veto** caps the score at 0.84 if any CRITICAL metric is 0"
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0083-clone-lessons-inceptbench-results-2026-07-02-eval-summary.qmd",
   "lines": "64",
   "quote": "the flags live in the prose reasoning, not the ID list."
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd",
   "lines": "51",
   "quote": "trust the recompute, not the annotation"
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
   "lines": "174-175",
   "quote": "the agent that proposed the redesign reported the shadowed, non-shipped number."
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
   "lines": "92",
   "quote": "Example found: a main-idea lesson served an inference/evidence item."
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0249-g9-idea-research-full-files.qmd",
   "lines": "500-502",
   "quote": "panels must switch on content (new speaker/beat/clue), never for variety alone — that is the seductive-details pattern."
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
   "lines": "182-184",
   "quote": "cross-family blind-solve on a held-out 50-item probe as the real ground truth and checkpoint-selection signal, not the per-rollout reward)."
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
   "lines": "29",
   "quote": "(`reading_level_match`, `answer_balance`) are deterministic, not LLM-judged."
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0211-peter-pan-reviewer-round-2708.qmd",
   "lines": "24",
   "quote": "Both usage checks were crackable via the single pair \"baby\"+\"sleep\""
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
   "lines": "73-74",
   "quote": "the seven `unsupported-detail` family routes were replaced with diagnosed, evidence-bound distractor semantics."
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0219-watch-48h-and-art-qa-redcontrol.qmd",
   "lines": "82-84",
   "quote": "same images, criteria differing only by the tightening"
  }
 ]
}
```
