# verify:quality-standard-audit

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "quality-standard-audit",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "Both quotes are verbatim and the numbers match (1 of 16; 0/3 hidden vs 3/3 with prior lessons). The one measured catch did not hold up, though. A newer solver answered the same item 3/3 with no context at all (evaluator-spec 137-140, README 92), so no measurement is left showing that earlier lessons alone make a later question answerable. The spec still adopts the check as a guard against guessing, and the risk follows logically in knowledge-sequenced courses, so it is kept as an adopted precaution. 'Can let' is softened to 'may' and the kind is changed from measured.",
   "statement": "When later lessons deliberately reuse earlier knowledge, also run the hidden-text check with the solver given what earlier lessons taught but not the new text, since a later question may then be answerable from earlier lessons alone.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "106-108",
     "quote": "the solver receives all prior lesson content (on-ramp pre-teach, ledger state, prior passages) but not the new text; later items must fail.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "135-137",
     "quote": "the historical Gemini 2.5 run found **1 catch of 16**. `rivers-demo-choice-hottext-20` was **0/3 exact plain-blind but 3/3 exact + high confidence spine-conditioned.**",
     "verbatim": true
    }
   ],
   "against": "evaluator-spec.md 137-140: \"A calibrated 2026-07-13 Gemini 3.5 Flash replication was 3/3 in both conditions, so the same item is currently a direct plain-blind leak and the historical context-lift interpretation does not generalize across model versions.\" README.md 92: \"The old context-lift claim does not survive model drift; the item is directly gameable.\" practice-layer-spec.md 106: \"(measured on one theme, not universal)\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep",
   "reason": "Both quotes are verbatim at the cited lines. README 89-92 records that, after a with-passage calibration, the current solver got the item 3/3 without the text, where the older solver had 0/3. It is one item, but the statement says 'can', and that case supports it. It complements truth 5 and is not a duplicate.",
   "statement": "Re-run hidden-text checks with a current, capable solver before relying on an old pass, because a newer solver can answer without the text an item an older one could not.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/README.md",
     "lines": "90",
     "quote": "The required current-model check changed the verdict.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/README.md",
     "lines": "92",
     "quote": "The old context-lift claim does not survive model drift; the item is directly gameable.",
     "verbatim": true
    }
   ],
   "against": "README.md 93: \"This supports its existing removal from serving. It does not certify the rest of the course.\" README.md 87-88: \"That is a valid matched historical observation, not a timeless property of the item.\" (one item)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep",
   "reason": "Both quotes are verbatim. The assessor contract and the hardened certification protocol both require an item to fail without the text and pass with it, and README 89-90 shows the with-passage calibration run before a hidden-text verdict. This adds a positive control to truth 5; it is not a duplicate.",
   "statement": "Before trusting that a solver cannot answer an item without its text, confirm the same solver answers it correctly with the text, and certify only items that fail hidden and pass shown.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-assessor/SKILL.md",
     "lines": "29-30",
     "quote": "every item blind-probed (must fail without the passage, succeed with it)",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "233",
     "quote": "the solver family must differ from the generator's, blind-solve must fail AND with-passage must pass, and no certification is carried forward from a cached bundle.",
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
   "reason": "All three quotes are verbatim and the numbers match (1.0, all six, 6/6). I added the course-eval README line, which states the claim almost word for word: an item-quality pass 'must never be reported as an anti-leak result'. This is distinct from truths 5 and 44.",
   "statement": "A quality score or rubric judgment says nothing about whether an item can be answered without its text, so keep the hidden-text check as its own gate and never report a quality pass as protection against guessing.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "233",
     "quote": "InceptBench scored one gameable item **1.0** — so the gate is dual: an item ships only if a quality score clears **AND** a blind solver cannot answer it without the passage",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
     "lines": "51",
     "quote": "The rubric gate (item ≥0.85 + lesson-level >20% rule) passed all six of these items — so the rubric is demonstrably not a substitute for the empirical run.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D11-anti-gaming-claim-integrity.md",
     "lines": "6",
     "quote": "we've watched an LLM-judge pass items that a blind-solve cracked 6/6.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/README.md",
     "lines": "80-81",
     "quote": "IB scoring an item \"high quality\" says nothing about whether the item is gameable, and an IB pass must never be reported as an anti-leak result.",
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
   "reason": "All quotes are verbatim, and 60% vs 6%, 48.7% (738 of 1,516), ~94% and 78% match. 'Rather than by cloning question types' misread 'encyclopedic clones', a term these files never define. The course-formula note that a guess-resistant format pool still leaked ~78% means construction alone is not enough. The fix names the constructions the spec uses and keeps the per-item blind test.",
   "statement": "Build questions about a text from constructions that force use of it, such as ordering its fragments or attributing its statements, and still blind-test every one, because most raw generated questions can be answered without the text and even a guess-resistant format leaks.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "19",
     "quote": "construction-gated items: fragment-sequence, source-attribution, explicit-vs-inferred",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "21-23",
     "quote": "construction-first generation survived the anti-leak gate at 60% vs 6% for encyclopedic clones; one production campaign yielded 48.7% (738 certified of 1,516); raw generated banks leaked ~94% blind.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "59-60",
     "quote": "78% of raw machine-generated items failed the passage-dependence gate alone",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "233",
     "quote": "G5 proved format is necessary but not sufficient (the anti-leak-*format* pool still leaked ~78%)",
     "verbatim": true
    }
   ],
   "against": "practice-layer-spec.md 20: \"pricing and design evidence, not current readiness\" (historical G5 figures).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep",
   "reason": "All quotes are verbatim and 33% matches. The restatement leak recurred in two courses (measured in G3, found verbatim in a G4 sample), and the content-integrity rule states it for any two-part evidence item. The profile caveat concerns which format is riskiest, not the mechanism. Distinct from truth 68.",
   "statement": "In a two-part item the second part must not restate the first part's answer, because linked parts that echo each other let the item be solved without the material.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "134-135",
     "quote": "In the recorded G3 case, EBSR was gameable 33% of the time because Part B restated Part A",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
     "lines": "46",
     "quote": "Part B restates Part A — G3's measured root cause, verbatim present",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-content-integrity/SKILL.md",
     "lines": "158-159",
     "quote": "For EBSR, Part B needs one uniquely strongest evidence choice and must not reveal Part A.",
     "verbatim": true
    }
   ],
   "against": "course-red-team/SKILL.md 135: \"that is evidence for that profile, not a universal format rule.\" (about which format is riskiest)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep",
   "reason": "All quotes are verbatim (the remedy quote runs onto line 193). The core is the same as truth 5: the question must need the text. Kept because it adds evidence from two courses, names the two sources of the leak (world knowledge and genre logic), and gives the remedy (ask what only this text settles). Two of the three quotes come from the name-bearing archive; the local finding taxonomy (line 17) records the same G4 prior-knowledge class.",
   "statement": "When material teaches real-world knowledge or follows a familiar story pattern, check that its questions can't be answered from general knowledge or genre logic, and ask about what only this material settles, such as a detail, a sequence, a cause or a number.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
     "lines": "47",
     "quote": "Prior-knowledge answerability — the knowledge-expedition design makes items about real-world facts (pitch physics, Magellan, explorer funding) answerable by any knowledgeable solver with no passage.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-4/REDTEAM-R2-2026-08-06.md",
     "lines": "151",
     "quote": "\"Anansi is a spider, and spiders are tiny. That alone kills B, C and D.\"",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-4/REDTEAM-R2-2026-08-06.md",
     "lines": "192-193",
     "quote": "ask about something only this retelling decides (a detail, a sequence, a causal link, a number)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "5",
   "name_bearing_source": true
  },
  {
   "index": 7,
   "verdict": "keep",
   "reason": "Both quotes are verbatim; 12 of 19 and the 5-run match. This refines truth 8 and is kept because it adds the within-sequence check and evidence that a course-wide balance check averages runs away.",
   "statement": "Check where the right answer sits within each sequence a learner meets, not only across the whole bank, because a balanced total can hide a visible streak.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "151-152",
     "quote": "does not detect within-lesson position *runs* (a student-visible streak that a course-wide histogram averages away).",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "168",
     "quote": "**12 of 19 single-select keys at A, with a 5-run.**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "8",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep",
   "reason": "All quotes are verbatim; 79%, 12 v 11 and 61 v 62 match. No existing truth covers key length, and the item-construction criterion D5.8 (line 19) says the same.",
   "statement": "Keep the right answer from being the longest or most detailed option by putting the verdict in the option and the reasoning in the feedback, and check length in both words and characters.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "165-166",
     "quote": "**79% of correct answers sat at position A and the key was systematically the longest**",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "172",
     "quote": "key longest by word count 12 v 11 but not by characters 61 v 62",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "130-131",
     "quote": "**Length parity**: verdict in the option, mechanism in per-option feedback — the key is never systematically longest.",
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
   "reason": "All quotes are verbatim. I added two local sources, the item-construction criterion on grammar and absolute-word cues and the G4 note that shuffling does not mitigate the length cue, so the claim does not rest only on the name-bearing addendum. The grammatical odd-one-out and dash cases still come from that addendum.",
   "statement": "Check option sets for cues that need no knowledge — a key that is the only option of its grammatical kind or the only one with a dash or hedge, or distractors with absolute or absurd wording — since shuffling removes none of them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
     "lines": "48",
     "quote": "Distractor tells — wrong options use absolute/absurd language (\"no real hardships\", \"relocate their entire kingdoms\"); the correct option is consistently the longest and most detailed.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md",
     "lines": "23",
     "quote": "Key not eliminable by length/grammar/position/absolute-word cues without target knowledge",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
     "lines": "53",
     "quote": "the correct-is-longest cue in F1 is not mitigated by shuffling",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "214-216",
     "quote": "The key is the only option of its grammatical kind — a bare proper noun among three \"The …\" / \"He …\" options. Position shuffling does not remove this; a seeded shuffle already removed position information from these items and the cue survived intact.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "41",
     "quote": "U1-L1's read stops the *only* option carrying a dash was the key",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 10,
   "verdict": "keep",
   "reason": "All quotes are verbatim (the teacher-contract quote is at lines 59-60); 'across 2 units' and 'five rounds' match. The knowledge-check exemption is already in the statement. Record LENS1-01 in the labeled defect corpus, where teaching content pre-answered its own release checks, is a further instance.",
   "statement": "Keep the facts used while modelling or practising a skill apart from the facts the following skill questions test, and label each question as a check of taught knowledge (overlap allowed) or a use of the skill (overlap not allowed).",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "88",
     "quote": "a teaching dose models the exact proposition an item tests → the item checks recall of the modeled sentence, not the skill. Reproduced across 2 units.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/teacher-contract.md",
     "lines": "59-60",
     "quote": "Authoring a fresh unit (u03 respiratory) REPRODUCED the dose-item leak the hibernation unit took 5 rounds to eliminate",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "85-86",
     "quote": "Mis-classifying the item makes the same text both correct and defective — it took five adversarial rounds to isolate this.",
     "verbatim": true
    }
   ],
   "against": "teacher-contract.md 67-68: \"Knowledge-CFU items are exempt: they legitimately check taught knowledge; classify explicitly.\" (already built into the statement)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep",
   "reason": "Both quotes are verbatim; 72 and 1.000 match. This is the remedy for the order effect named in truth 35, not a restatement of it.",
   "statement": "Probe order-sensitive items under several shuffles and judge by the worst case, because certifying against a single shuffle lets guessable items through.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "20",
     "quote": "sequence items certified against one seeded shuffle; multi-shuffle re-probe decertified 72 incl. one exact 1.000",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-assessor/SKILL.md",
     "lines": "43-44",
     "quote": "(anonymized labels, seeded+multi shuffles, three blind votes incl. temp variation, leak = exact or partial ≥0.6, cross-family solver, no self-certification).",
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
   "reason": "All quotes are verbatim (the first runs to line 116); k/n and 1/C(n,k) match the source. The live probe found binary scoring with no partial credit.",
   "statement": "Work out each item's guessing floor from how it is actually scored where it is served, not from its format label, and never set a pass bar close to that floor.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "115-116",
     "quote": "Chance floors are stated **per item from its responseDeclaration under the actual serving scoring rule**",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "117-118",
     "quote": "a select-k interaction authored `cardinality=\"single\"` scores \"first token in correct set\" (floor k/n, not 1/C(n,k)), so the format label alone never determines the floor.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "119-120",
     "quote": "A bar within noise of its floor measures nothing.",
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
   "reason": "Both quotes are verbatim; 5–9 items, 90% and ceil(0.9n)=n for n≤9 match. The G4 red team gives the counter-case (a 22-item test tolerates two misses), which fits the statement.",
   "statement": "Work out what a percentage pass mark demands on each test's actual length, because on short tests 90% can mean a perfect score.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "14",
     "quote": "leak-purge shrank tests to 5–9 items → 90% gate = perfect-score-only (ceil(0.9n)=n for n≤9)",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "63-64",
     "quote": "**Arithmetic traps hide in small n.** ceil(0.9×n) = n for n ≤ 9: a 90% gate on a ≤9-item test demands a perfect score.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep",
   "reason": "All quotes are verbatim (the practice-layer quote is at lines 91-92); threshold 90 on all 5 resources matches. The eval-criteria line refers to the course-level declaration (curriculum or practice app); the resource-level version is practice-layer P6 and evaluator 6, which the statement follows.",
   "statement": "Declare each assessed resource's purpose — in-lesson check, interval assessment or benchmark — before judging it, and put pass thresholds only on assessments, since judging one by the other's rules misfires.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "230-231",
     "quote": "masteryThreshold=90 on all 5 lesson resources** -- the three teaching lessons and the transfer lesson behaved as 90% practice-test gates over their own formative checks.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "91-92",
     "quote": "judging one by the other's bar.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/timeback-course-eval/references/eval-criteria.md",
     "lines": "102",
     "quote": "The single most important criterion.",
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
   "reason": "Both quotes are verbatim (the second is at lines 273-275); 0/10, 8 and 2 match. The evaluator coverage map (evaluator-spec 294) also records an evaluator that 'treats a multi-skill bank as integrative', which the source calls a proof that declaration alone is insufficient.",
   "statement": "Include tasks that require combining taught skills and verify that each one really demands the combination, because passing every part separately does not show the whole and calling a task integrative does not make it so.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "246-247",
     "quote": "A gate of individually-good atomized checks licenses \"passed the parts,\" never \"acquired the theme.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "273-275",
     "quote": "the full gate certified **0/10** (8 plain-blind leaks, 2 spine-conditioned leaks; 0 integrative verified), so nothing was published.",
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
   "reason": "Both quotes are verbatim and the 24-hour figure matches. Refines truth 48: the later test must actually be later, and provably so. Not a duplicate.",
   "statement": "Call a check delayed only when the delay is enforced and the elapsed time is recorded, because same-day success shows short-term memory rather than learning.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/README.md",
     "lines": "116-117",
     "quote": "The platform does not enforce the intended 24-hour delay, and no elapsed-time evidence was captured, so this is not a verified delayed assessment.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "38-40",
     "quote": "release-day completion never qualifies (Practice BrainLift: same-day testing measures working memory, not learning).",
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
   "reason": "Both quotes are verbatim. The four-option minimum is a G3-profile rule. The universal standard says 'No fixed option count belongs in the universal standard' (STANDARD.qmd 770), and the same G3 criteria say 'drop to 3 rather than add a weak 4th' (D5 line 20), so the no-filler rule holds in general.",
   "statement": "Make every wrong option an error a learner would really make, and don't pad an item with filler options to reach a fixed count.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "160",
     "quote": "can you name what a student choosing each distractor is thinking? if not, it's filler (worse than 3 options)",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "773",
     "quote": "J16-ASS-001: Use only plausible, diagnostically useful response options; do not add filler to meet a count.",
     "verbatim": true
    }
   ],
   "against": "D5-assessment-item-construction.md 12: \"Every MCQ has ≥4 options; no 2-option / True-False item in the mastery pool (a yes/no is a 50/50 guess)\" is a scoped G3 minimum; the same file at line 20 says \"drop to 3 rather than add a weak 4th\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim. The clause 'true for every response routed to it' rested only on the name-bearing build rules (rule 4), and truth 1's 'only what is true' already covers it, so I removed it. The claim is now sourced from local criteria and the standard ('potent lures receive correction'; 'false lure left uncorrected').",
   "statement": "Give every plausible wrong option its own feedback that addresses the error it represents, because a strong lure left uncorrected can teach the error.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/labeled-defect-corpus.jsonl",
     "lines": "5",
     "quote": "Corrective feedback did not match the construct the distractor represents (feedback not misconception-keyed to the chosen option).",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "166",
     "quote": "strong misconception distractors + no feedback = teaching the error (negative suggestion effect)",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md",
     "lines": "17",
     "quote": "Every misconception distractor carries feedback addressing that misconception",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md",
     "lines": "18",
     "quote": "Any item with competitive/plausible distractors must provide feedback (guards the negative-suggestion effect)",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "768",
     "quote": "potent lures receive correction",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "769",
     "quote": "false lure left uncorrected",
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
   "reason": "The quote is verbatim. The G3 item criteria say the same (D5 line 26: 'Any \"application/analysis\" item presents novel stimulus; else tag it recall').",
   "statement": "A question claimed to need application or analysis must present material the learner has not seen, otherwise it is recall with a longer stem.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "163",
     "quote": "genuine higher-order needs a NOVEL stimulus (unseen passage/scenario); else retag recall",
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
   "reason": "Both quotes are verbatim; the D7 criterion is at line 32, not 33.",
   "statement": "Screen content questions for untaught vocabulary, hard syntax and idioms that make them test reading ability rather than the content.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D7-knowledge-first-curriculum.md",
     "lines": "32",
     "quote": "Autonomous items are screened for untaught Tier-2 vocab, grade-inappropriate syntax, and idioms that make them test reading, not content",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/curriculum-architecture.md",
     "lines": "99-100",
     "quote": "**linguistic-validity QC** (untaught Tier-2 vocab, syntax, idioms — required for teacherless delivery)",
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
   "reason": "Both quotes are verbatim. The reading exception narrows the rule rather than contradicting it, and criterion D5.18 (one KC per diagnostic item) says the same.",
   "statement": "Make each diagnostic item test one thing so a wrong answer can be interpreted, and don't make later parts of an item depend on earlier parts.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "165",
     "quote": "passage-parse + content + reasoning in one item → wrong answer uninterpretable",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md",
     "lines": "31",
     "quote": "No all-or-nothing multi-part item where (b) depends on (a); split into independent items",
     "verbatim": true
    }
   ],
   "against": "finding-taxonomy.md 165: \"(reading exception: OK when the stimulus IS the KC, then strip everything else)\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep",
   "reason": "Both quotes are verbatim; '<10 items' fits 'a handful'. Criterion D5.30 (anti-grind-through, line 41) asks for breadth across item families. Distinct from truths 15 and 48.",
   "statement": "Base a mastery decision on several different items and item families, because passing by retrying near-identical items or on a handful of items is practice, not mastery.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "168",
     "quote": "mastery evidence must span item families; a gate decision on <10 items is retrieval practice, not mastery",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md",
     "lines": "42",
     "quote": "No mastery decision rests on a single MCQ (≥25% guess); use item bundles",
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
   "reason": "Both quotes are verbatim.",
   "statement": "State the supports a result was earned with, because doing something with cues is not doing it unaided.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "169",
     "quote": "\"can do X with cues\" ≠ \"unaided\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md",
     "lines": "46",
     "quote": "The mastery claim states its support level (\"unaided\" vs \"with cues\"); high-stakes scores only the unaided check",
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
   "reason": "Both quotes are verbatim (the STANDARD line also recurs at 625); <5% fits 'almost nobody'. 'Replace predicted difficulty with live data' is a fair reading of 'a prior awaiting live calibration'.",
   "statement": "Watch items after use — revise options almost nobody chooses, flag items that discriminate the wrong way, and replace predicted difficulty with live data.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md",
     "lines": "47",
     "quote": "Distractor-level data reviewed; non-functioning distractors (<5%) revised; negative-discrimination items flagged",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "455",
     "quote": "J16-ASS-008: Treat predicted difficulty as a prior awaiting live calibration.",
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
   "reason": "Both quotes are verbatim. Criterion D5.38 (line 49) says the same: 'If the target is production, the format requires production'.",
   "statement": "If the goal is for learners to produce something — explain, write or say it — assess it with a production task, because selecting an answer can't show it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "132",
     "quote": "Production targets get production formats.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/opportunities-to-respond-brainlift.md",
     "lines": "30",
     "quote": "If a child never has to compose or explain an answer, the app cannot tell whether the child understood",
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
   "reason": "The quote is verbatim (lines 132-133). It rests only on the name-bearing archive; I found no local copy. It is general and not covered by truths 10 or 56, which concern what a marking rule should credit rather than testing a rule against its own model answer.",
   "statement": "Score every model answer against its own marking rule, because a rule that would mark down its own exemplar is broken.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "132-133",
     "quote": "U2-L6's SCR required the term \"sacrifice\"; its own model answer said \"gave up\". The exemplar the teacher reads aloud would have been marked down by the rule printed underneath it.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 27,
   "verdict": "keep",
   "reason": "Both quotes are verbatim (the first is at lines 141-142). They appear only in the name-bearing archive; no local copy found.",
   "statement": "Check that what one lesson marks correct agrees with what earlier lessons taught, because checks that read one lesson at a time can't see a learner marked wrong for learning an earlier lesson correctly.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "141-142",
     "quote": "A child who learned L5 **correctly** was marked wrong.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "144-145",
     "quote": "Invisible to five other gates because **every other gate reads one lesson at a time.**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 28,
   "verdict": "keep",
   "reason": "Both quotes are verbatim.",
   "statement": "Check that every item assesses the skill its lesson claims to teach, because retagging does not fix an item that demands a different operation.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "79-80",
     "quote": "A lesson's items must assess the KC the lesson claims to teach (construct coherence — a main-idea lesson serving inference items is a tagging *and* teaching defect).",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "84",
     "quote": "main-idea lesson served an inference item after a \"successful\" retag",
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
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim and 193 matches. The phrase 'can hide whole missing strands' had no cited support; it appears only in a name-bearing archive file. I replaced it with the local spec-to-KC coverage criterion (no orphan standards, no false alignment).",
   "statement": "Audit standard tags against what each item actually demands and report an error rate, and check that every standard the course claims has items behind it, because tag coverage is not a curriculum and tags can be wrong or missing.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "224",
     "quote": "G3 had systematic mistags (vocab-in-context wrongly on L.3.4; comprehension on the wrong strand); **193 items retagged** — audit tags and report an error rate",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "57-58",
     "quote": "Reading standards are skills, not knowledge — CASE-tag coverage is plumbing, never the curriculum claim.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D7-knowledge-first-curriculum.md",
     "lines": "27",
     "quote": "Every standard maps to ≥1 KC; no orphan standards/KCs; no false alignment (vocabulary matches the standard but the item's DOK is lower)",
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
   "reason": "Both quotes are verbatim. The counter line doubts that a valid comprehension-gap diagnostic exists; it does not contradict how one should be used if it does.",
   "statement": "Use diagnostics to route support under stated uncertainty, never as a grade or mastery label.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "99",
     "quote": "Product type, sampling limits, uncertainty, slips, guesses, unassessed knowledge, and routing behavior are explicit and tested.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "785",
     "quote": "Failure signals: Diagnostic score directly promotes, punishes, or labels mastery; uncertainty hidden.",
     "verbatim": true
    }
   ],
   "against": "D7-knowledge-first-curriculum.md 35 doubts any valid comprehension-gap diagnostic exists: a valid one does not exist — 'nailing jelly to the wall'.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep-with-fix",
   "reason": "The red-team quote is verbatim. It describes a predicted risk with no measured order effect, so 'open question' fits. I added the local assessor contract line showing that a counterbalanced linking design was adopted.",
   "statement": "When validating an assessment against an external test, make sure it doesn't act as practice for that test, for example by counterbalancing the order.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/map-proxy-assessment/red-team/RED_TEAM_FINDINGS.md",
     "lines": "21",
     "quote": "**Counterbalancing / order-effect design is not addressed anywhere in the CVP.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-assessor/SKILL.md",
     "lines": "46",
     "quote": "counterbalanced linking design",
     "verbatim": true
    }
   ],
   "against": "No measured order effect; the risk is a predicted reviewer objection.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 32,
   "verdict": "keep",
   "reason": "Both quotes are verbatim; 0.930, 0.928, ≥0.93, 4.12 and <4.0 match. They appear only in the name-bearing archive.",
   "statement": "Show every metric at its measured value in every summary, including the failing one, because rounding up to meet a bar or leaving out the failing metric is a false pass.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "9",
     "quote": "Summary tables reported reliability as \"0.930 ✅\" against a ≥0.93 benchmark the underlying reports state as 0.928, below",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "10",
     "quote": "The one failing metric (RMSE 4.12 vs <4.0 target) was omitted from every summary table",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 33,
   "verdict": "keep",
   "reason": "Both quotes are verbatim (the practice-layer quote is at lines 140-141).",
   "statement": "Don't reuse pass bars, yields or thresholds measured on one course or level for another; recalibrate them on a control set first.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "140-141",
     "quote": "All historical G5-derived bars and yields require a **G3 recalibration control set before any G3 gate or generation budget goes live** (blocking precondition)",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D6-practice-durable-mastery.md",
     "lines": "33",
     "quote": "Every G5-derived threshold/yield is recalibrated on a G3 control set before any G3 gate goes live",
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
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim (the SPOVs quote is at lines 106-109). I swapped the name-bearing feedback-ledger quote for the local red-team skill line that records gradual-release failure as a recurring rejection theme. The statement is unchanged.",
   "statement": "Make the model, guided and independent stages one and the same process at decreasing support, so that with the labels removed it still reads as one process fading.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-creation-spovs.md",
     "lines": "106-109",
     "quote": "round 2 found our gradual release **misapplied**: the I-do revealed answers instead of modelling the thought process, the we-do gave hints instead of walking the same steps with immediate corrective feedback, and the you-do switched skills.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "24-25",
     "quote": "strip the labels; a reviewer must still be able to say \"these three artifacts teach the same process at decreasing support.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "159-160",
     "quote": "the RECURRING rejection theme \"poor instructional decision making\"",
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
   "reason": "All quotes are verbatim (the red-team quote is at lines 163-164). This adds content to truth 40's 'worked example' and is not a duplicate.",
   "statement": "A worked example must show the reasoning on the material as it is spoken — where to look, the tempting wrong choice and why it is rejected — rather than just the finished answer.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "16-17",
     "quote": "Revealing the answer is not modelling.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "52",
     "quote": "Visible evidence, a plausible alternative, the reason it is rejected, and construction of the answer are synchronized and semantically sound.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "163-164",
     "quote": "the screen says \"watch\" but only shows the organizer filled with the finished right answer.",
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
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim. I added local criteria for the guided step (a partial answer the learner completes, with a blocking response at each step) and for release (independent work keeps the same demand). 'New material' and 'no more support than the guided step' still rest on the name-bearing archive.",
   "statement": "In guided practice hand the learner a partly finished answer to complete with feedback at each step, and in independent practice apply the same steps to new material with no more support than the guided step had.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "169-170",
     "quote": "\"I filled this row, now you answer\" with NO partial/seeded answer = the middle rung is missing",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D1-gradual-release-explicit-instruction.md",
     "lines": "14",
     "quote": "hands over a *partial answer the child completes*, with a blocking per-step response",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "51",
     "quote": "All stages reference one operation; scaffolds retire deliberately; independent work retains the cognitive demand and evidence structure.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-ENTRYPOINT-CLEAN-ROOM-G3-U4-L1-2026-08-06.qmd",
     "lines": "57-58",
     "quote": "You-do returns to the model's animal, evidence, and constructed answer instead of requiring the same operation on new evidence.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "332",
     "quote": "a you-do step may never be more scaffolded than the corresponding we-do step.",
     "verbatim": true
    }
   ],
   "against": "feedback-2026-08-06-addendum.md 340-344: the gradient rule was argued and overruled for one lesson, which shipped a default gap-fill at the independent step; the record calls it accepted-on-instruction, and the criterion still binds every other lesson.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 37,
   "verdict": "keep-with-fix",
   "reason": "Both quotes are verbatim (the first is at lines 31-32); 40, 60 and ~91 match. 'About 40 words at most' left out the 60-word hard cap and presented a grade-3 number as universal, and 'the task' was 'the passage' in the source.",
   "statement": "Give feedback a word budget that keeps it shorter than the material it refers to (the grade-3 reading standard set a 40-word target and a 60-word cap) and lint its mechanics, because generated feedback ran to a median of about 91 words, longer than the passage.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "31-32",
     "quote": "Target ≤ 40 words; hard cap 60. A grade-3 child will not read feedback longer than the passage (round-2 verified: our generator's median was ~91 words).",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "75",
     "quote": "G3 round-2: feedback longer than the passage, lowercase after full stops; G5 generator lineage measured at ~91-word median",
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
   "verdict": "drop",
   "reason": "Both quotes are verbatim and 64%→41% matches, but the number cannot carry the causal claim. Second-attempt accuracy is measured only on learners who missed the first attempt, so it is lower from selection alone, and the escalated item was harder by design. Neither source tests a same-difficulty retry, so 'because escalating difficulty lowered accuracy' overstates the evidence. What remains is close to truth 4 and to the protocol of correcting and then asking again.",
   "statement": "After a miss, reteach and retry at the same difficulty instead of escalating it, because escalating difficulty after a failure lowered second-attempt accuracy from 64% to 41%.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-1/timeback-pull/COURSE_BUNDLE_BRAINLIFT.md",
     "lines": "44",
     "quote": "Difficulty escalates after a miss; attempt-2 supporting-detail accuracy **drops from 64% to 41%**",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/generator-insights.md",
     "lines": "46",
     "quote": "retry that drops accuracy 64%→41%",
     "verbatim": true
    }
   ],
   "against": "Selection effect: second-attempt accuracy is computed only on the learners who missed the first attempt, and the escalated item was harder by design.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 39,
   "verdict": "keep",
   "reason": "Both quotes are verbatim. G3 criteria D1.24 and D6.5 say the same.",
   "statement": "After a failed checkpoint, reteach and retest once on new items after a delay, and send a second failure to a review of placement or sequence rather than an endless loop.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "72-74",
     "quote": "D15 failure routing: reteach via M7 → one delayed retest on new items → a second failure routes to placement/sequence review. No infinite retest loop",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-modes-spec.md",
     "lines": "36",
     "quote": "A second consecutive failed delayed retest routes to placement/sequence review — never an infinite loop.",
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
   "verdict": "keep",
   "reason": "The quote is verbatim. It is a single adopted rule (D6.12, the practice boundary rule) and it is general.",
   "statement": "If the correction a learner needs is longer or more complex than the original teaching, treat it as new teaching rather than practice feedback.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D6-practice-durable-mastery.md",
     "lines": "23",
     "quote": "If the corrective feedback needed exceeds the original instruction in length/complexity, it's new instruction, not practice",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 41,
   "verdict": "keep",
   "reason": "Both quotes are verbatim (the red-team quote is at lines 201-202). The underlying study is cited without a DOI.",
   "statement": "For an idea learners commonly get wrong, draw out their intuitive wrong belief once at the start and then resolve it, without repeating the wrong belief later.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/SKILL.md",
     "lines": "72",
     "quote": "A clear explanation that never engages the prior belief produces confident non-learning (Muller: clear-only exposition barely moved scores; misconception-first nearly doubled the gain).",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "201-202",
     "quote": "The wrong belief is voiced at most once, at the open, and never rehearsed/scolded in the body",
     "verbatim": true
    }
   ],
   "against": "none found; the cited study is a dissertation with no DOI or URL in these files",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 42,
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim. The original wording ('still teaches an unrelated objective unchanged') was garbled. I reworded it and added the rubric's alignment rule that the body must resolve the question the hook raises.",
   "statement": "Test an opening hook by deleting it: if the lesson body would teach exactly the same without it, the hook is detached; a hook should raise the question the body then resolves.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/video-red-team/references/rubric.md",
     "lines": "74-75",
     "quote": "If deleting the hook leaves the body teaching an unrelated objective unchanged, the hook is misaligned.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/video-red-team/references/rubric.md",
     "lines": "71-73",
     "quote": "They must be the same conceptual question, and the positive body must explicitly resolve the prediction raised at the open.",
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
   "reason": "All quotes are verbatim; 18/18 matches. G3 criteria D2.4 and D2.5 (lines 15-16) say the same. It overlaps open truth 55 only on the 'I don't know' branch.",
   "statement": "A reply that could have been written before the learner answered is not a response to them, so branch on what the learner actually produced and test that every branch, including 'I don't know', can fire.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "185",
     "quote": "the spoken answer never drives the branch",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "187",
     "quote": "branch authored + gated in 18/18 but **can never fire**",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/opportunities-to-respond-brainlift.md",
     "lines": "71",
     "quote": "A reply that would read the same no matter what the child answered is not a third turn.",
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
   "verdict": "keep",
   "reason": "Both quotes are verbatim; the recast sentence is at line 70, not 71. The DOI belongs to the Lyster and Saito (2010) meta-analysis in the reference list, and G3 criterion D2.6 (line 17) restates the rule. The second-language origin is noted under against.",
   "statement": "When a specific point must be learned exactly, prompt the learner to say it again in their own words rather than restating it for them, because learners often don't notice a restatement.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/opportunities-to-respond-brainlift.md",
     "lines": "70",
     "quote": "A recast keeps a conversation moving and grows how much a child says, but because children often do not notice a recast, it does not reliably teach one specific point (Lyster & Saito, 2010).",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/opportunities-to-respond-brainlift.md",
     "lines": "198",
     "quote": "https://doi.org/10.1017/S0272263109990520",
     "verbatim": true
    }
   ],
   "against": "opportunities-to-respond-brainlift.md 168: \"Drawn from second-language classrooms, so applied here by analogy to early oral language.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 45,
   "verdict": "keep",
   "reason": "All quotes are verbatim; 7–8, 2–3, ~2 and 5 of 7 match.",
   "statement": "When counting learner responses by type, check what each one is, because echo or say-back answers inflate production counts and a count that meets its target can still mislead about quality.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "183",
     "quote": "G3 iter-3 claimed \"7–8 generate/lesson, over-delivered\" — but 2–3 were trivial *say-backs* (repeat a word) and the real generative-comprehension production was ~2",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "83-85",
     "quote": "Iter-3's \"7–8 generate, over-delivered\" was true by count and misleading by quality (2–3 trivial say-backs; 5 of 7 spoken moments canned). Verify the number AND what it measures.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/opportunities-to-respond-brainlift.md",
     "lines": "23",
     "quote": "A high number of responses per minute is not evidence of quality if the app reached that number by asking only recognition questions.",
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
   "reason": "All quotes are verbatim. I swapped the name-bearing meeting note for the local standard, which requires consequential responses and lists 'Clicks counted as production' as a failure. The statement is unchanged.",
   "statement": "Don't let more than about a minute of passive content pass without a meaningful response from the learner, and don't count a decorative tap as one.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-modes-spec.md",
     "lines": "49",
     "quote": "a consequential check at least every 60s of passive content (Generic Instruction SS6)",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D10-delivery-ux-accessibility.md",
     "lines": "23",
     "quote": "No continuous passive segment beyond ~60s; a consequential check appears at least every 60s",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "349",
     "quote": "Passive content is interrupted by consequential identify, complete, generate, explain, or represent responses chosen for the target construct.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "350",
     "quote": "Clicks counted as production; authored prompts never render; long passive stretches; redundant low-value questions.",
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
   "reason": "Both quotes are verbatim (the addendum quote is at lines 310-311; the docx quote is line 11 of the textutil output). They appear only in the name-bearing archive.",
   "statement": "Reveal steps when the learner acts rather than on a timer, because a timer can't pace itself to a slow reader and turns the step into passive watching.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "310-311",
     "quote": "A timer also cannot pace itself to a slow reader. Tap-to-continue satisfies both.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/feedback/feedback5/Feedback 11.08.docx",
     "lines": "11 (textutil text)",
     "quote": "Otherwise, it will move too fast for some students.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 48,
   "verdict": "keep",
   "reason": "The quote is verbatim. It comes from one case, adopted as a process rule, and appears only in the name-bearing archive.",
   "statement": "Open each section with a link to what was just taught, because a section that is good on its own but disconnected in context passes every per-section check.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "305",
     "quote": "Cheap to author and invisible to every existing gate.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 49,
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim. The statement's 'check that support shrinks across the sequence' had no quote behind it. I added the addendum's rule that scaffold counts must not rise across the unit and the local scaffold-fading criterion (D6.23).",
   "statement": "Record how each scaffold fades as data — how many uses remain and what retires it — and check that support shrinks across the sequence, because a fade plan written only in prose never fades.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "238-239",
     "quote": "The reason it stays open is that \"states a condition\" is satisfiable by a sentence in a document nothing reads, so nothing ever fades.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "248-249",
     "quote": "**Counts are monotonically non-increasing across the unit.** A scaffold that reappears at greater volume in a later lesson is not fading.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D1-gradual-release-explicit-instruction.md",
     "lines": "24",
     "quote": "every scaffold states a fade/retirement condition",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D6-practice-durable-mastery.md",
     "lines": "34",
     "quote": "Scaffolds (frames, organizers, notes) are removed on an explicit schedule across a unit as a mastery check",
     "verbatim": true
    }
   ],
   "against": "feedback-2026-08-06-addendum.md 254: chunked reading existed on one lesson only, so there was nothing to fade yet; the rule is a template requirement.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 50,
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim (the third is at line 179). The original said both prompt types 'invert the task', but the source says copy-then-paraphrase prompts 'teach plagiarism', so the two reasons are now stated separately. I added the local G3 criterion D5.37.",
   "statement": "For evidence-based answers, have learners locate and mark the evidence first and then write in their own words, allowing evidence drawn from several places, because write-then-find inverts the task and copy-then-paraphrase prompts teach copying.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "81",
     "quote": "find+highlight FIRST, then write in own words",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "80",
     "quote": "often it's 2 ideas synthesized from different places",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "179",
     "quote": "copy-then-paraphrase writing prompts that teach plagiarism",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md",
     "lines": "48",
     "quote": "Evidence tasks: find-and-highlight the sentence first, then write in own words; the I-do models the finding",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 51,
   "verdict": "keep",
   "reason": "The quote is verbatim, and the count of 60 in the same table matches. It appears only in the name-bearing archive.",
   "statement": "Don't score learners on a form of answer the teaching never demonstrates.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "404-406",
     "quote": "the lesson grades the child on producing `The text says \"…\"` while the modelling omits the quote marks, so we grade a form we do not demonstrate.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 52,
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim; '0 mid-passage stops across 18 lessons' matches. I swapped the name-bearing meeting note for local G3 criteria: chunked, deepening rereads, and knowledge built through a set of texts 'not by rereading the same text start-to-finish every day'. The statement is unchanged.",
   "statement": "Plan rereading as passes with a stated, deepening purpose aimed at specific parts, because a single read followed by questions, and whole-text repetition by habit, both miss.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "204",
     "quote": "G3 iter-3: the passage is one block read ONCE, all questions after it (0 mid-passage stops across 18 lessons)",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D3-reading-architecture.md",
     "lines": "12",
     "quote": "The passage is chunked and reread with each pass going deeper",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D3-reading-architecture.md",
     "lines": "15",
     "quote": "not by rereading the same text start-to-finish every day",
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
   "reason": "Both quotes are verbatim (the first is at lines 38-39). G3 criteria D6.6 and D6.7 say the same. This extends truth 48 to when a skill may be interleaved.",
   "statement": "Keep practice of a new skill blocked until it passes a delayed retest on new items, then mix it into review with no two consecutive items on the same skill.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "38-39",
     "quote": "a delayed (≥24h) retest passed on *new* parallel items — release-day completion never qualifies",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "40-41",
     "quote": "Cumulative interleaved review keeps every cleared track alive, no two consecutive items on the same skill",
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
   "reason": "Both quotes are verbatim. Practice-layer P3 names the update task (explain, compare or place), and D6.11 says the same.",
   "statement": "Practise understanding by retrieving it and then transforming it — explaining, comparing or placing it — and keep bare recall for fixed facts.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "45-46",
     "quote": "Fixed retrieval is reserved for the anchor class; comprehension KCs never run as bare recall.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "66",
     "quote": "Classify KCs into **Fixed Retrieval**",
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
   "reason": "Both quotes are verbatim (the gauntlet quote is at line 34).",
   "statement": "Make most practice build knowledge and understanding rather than imitate the final test, keeping test-format and timed practice for late in the sequence.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/gauntlet-spec.md",
     "lines": "34",
     "quote": "test-format practice concentrated late, timed conditions last.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D7-knowledge-first-curriculum.md",
     "lines": "18",
     "quote": "Knowledge-building activity looks nothing like the paragraph-plus-questions test (marathon-training analogy)",
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
   "reason": "Both quotes are verbatim. The instruction-modes spec adds: 'Cold passages are never taught from — they are the practice layer's sealed benchmark.' (lines 68-69)",
   "statement": "Keep transfer benchmarks sealed: never teach from them or gate on them, and verify they share nothing with the taught material.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "71",
     "quote": "The cold benchmark is **never a mastery gate and never teaching material**",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-assessor/SKILL.md",
     "lines": "27-28",
     "quote": "passages with ZERO overlap with instruction (verified, the G4/G5 cold-finals property); parallel forms, disjoint.",
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
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim; 5.59 vs 2.63 and η²=.32 match. 'Incidental vocabulary' had no quote behind it, so I added the next fact in the brainlift (η²=.625). It is a single small study; see against.",
   "statement": "Sequence learning material so topic knowledge recurs and builds, keeping unrelated unfamiliar material for the test, because coherent sets build more knowledge and incidental vocabulary than unrelated pieces.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "130-131",
     "quote": "Coherent-set readers gained 5.59 vs 2.63 concept idea-units (η²=.32) over six texts in three days (Cervetti 2016, pp. 769–771).",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "132-133",
     "quote": "The largest Cervetti effect was *incidental* vocabulary: η²=.625, no meanings taught, target words recurring ~6× across the set (pp. 766–772).",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "166",
     "quote": "Cold plain text belongs at the *test*, not throughout learning; sequence passages so knowledge recurs and compounds",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/reading-science/sources.qmd",
     "lines": "18",
     "quote": "DOI: 10.1007/s11145-016-9628-x",
     "verbatim": true
    }
   ],
   "against": "SYNTHESIS.qmd 186-187: \"**Cervetti's limits** — N=59, one rural school, on-grade readers, 3-day intervention, null (unreliable) comprehension-questions measure\"; brainlift line 89 notes that knowledge transfer is near-domain at best.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 58,
   "verdict": "keep",
   "reason": "Both quotes are verbatim; ~10 vs ~50 sessions matches. The 'bounded value' caveat is consistent with 'briefly'.",
   "statement": "Teach general strategies briefly and explicitly and then spend the time on knowledge, because strategy instruction gives its benefit quickly and then stops adding.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "134-135",
     "quote": "Across eight quantitative reviews, ~10 strategy-instruction sessions produce the same comprehension benefit as ~50 — no dose-response (Willingham 2014, p. 2).",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D7-knowledge-first-curriculum.md",
     "lines": "15",
     "quote": "Strategies are a one-time \"bag of tricks,\" taught explicitly then stopped; no strategy-mastery gating (added practice confers no advantage)",
     "verbatim": true
    }
   ],
   "against": "SYNTHESIS.qmd 175-176: \"The claim is *bounded value*, not *no value*.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 59,
   "verdict": "keep-with-fix",
   "reason": "Both quotes are verbatim. The source restricts the finding to narrative subjects, so I added that qualifier.",
   "statement": "Plan the whole teaching episode — its throughline and persistent example — before breaking it into items, because generating item by item produced locally correct pieces that never cohered, at least on narrative subjects.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/academics-alignment-plan.md",
     "lines": "16-18",
     "quote": "Atomise-first on narrative subjects produces \"locally-correct micro-lessons that never cohere\" — the round-2 sequencing finding.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "97",
     "quote": "per-item generation with no throughline reasoning → \"locally-correct micro-lessons that never cohere\"",
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
   "reason": "Both quotes are verbatim (the eval-criteria quote is at lines 152-153).",
   "statement": "Make the knowledge sequence visible in the delivered material, because claimed links between lessons that can't be seen by working through it don't count.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "92",
     "quote": "\"3 compounding threads\" claimed; reviewer saw axolotl→shadows with no link, no pre-teach, no revisit",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/timeback-course-eval/references/eval-criteria.md",
     "lines": "152-153",
     "quote": "Claims that can't be seen by clicking through do not count.",
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
   "reason": "Both quotes are verbatim. In the negative fixture, per-lesson scoring passes both lessons while the cross-lesson check fails them.",
   "statement": "Let a lesson assume only what earlier lessons taught and the learner has shown on a later day, and check that chain in code, because each lesson can look fine on its own.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "103-104",
     "quote": "IB scores each of those two lessons as individually fine; only the cross-lesson invariant separates them.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-modes-spec.md",
     "lines": "62-64",
     "quote": "so an anchor first taught the same day never satisfies an `assumes` edge, and an anchor that is present-but-not-fluent is treated as not met.",
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
   "reason": "The quote is verbatim. Evaluator-spec 87-88 states the same requirement: 'as you saw last lesson' claims must be true against order.",
   "statement": "Make every reference to earlier material, such as 'as you saw last lesson', true in the order the learner actually meets it, and check it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/gauntlet-spec.md",
     "lines": "14",
     "quote": "Relational-reference truth check (\"last lesson\" must be factually last).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 63,
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim. 'Prerequisite structures are design choices rather than facts' contradicted the statement's own 'logical' label. The source limits the point to comprehension ('\"A before B\" is a design choice, not a logical necessity'), so I narrowed it.",
   "statement": "Label each prerequisite link as logical, evidence-based or merely conventional, and don't let a conventional link block a learner, because many orderings, especially in comprehension, are design choices rather than logical necessities.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-modes-spec.md",
     "lines": "123-125",
     "quote": "classify each edge logical / empirical / conventional (kc-graph change proposal, warrant field); a conventional edge may not block the on-ramp until upgraded by evidence",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "126",
     "quote": "a *conventional* (untested tradition) edge passed off as *logical* is the Engelmann trap (like/unlike-denominator)",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-modes-spec.md",
     "lines": "70-71",
     "quote": "ELA comprehension is a horizontal knowledge structure — \"A before B\" is a design choice, not a logical necessity",
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
   "reason": "Both quotes are verbatim. This is related to truth 29 but distinct.",
   "statement": "Have people set the sequencing policy and treat a model-generated sequence as a proposal to check against it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/curriculum-architecture.md",
     "lines": "31-33",
     "quote": "**You cannot outsource sequence judgment to the model** — the human supplies the policy (spine, entry assumptions, prereq strictness, priority order); the model generates an auditable proposal obeying it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-modes-spec.md",
     "lines": "75-77",
     "quote": "Any model-generated sequence is an auditable proposal reviewed against this policy, not against taste.",
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
   "reason": "All quotes are verbatim (the first is at line 129). The addendum says the rule that a concept keeps one definition everywhere is new, so no local copy exists. 'Four definitions in one lesson' matches its lines 125-129.",
   "statement": "Define each concept once and reuse that exact definition everywhere it is defined, and make the definition complete for the learner, since a true but partial definition teaches the wrong concept.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "129",
     "quote": "A child cannot resolve that.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "134-135",
     "quote": "the definition passes D4.4, D4.5, D4.17 and D4.24 and is still the wrong concept.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/feedback/feedback5/Feedback 11.08.docx",
     "lines": "4 (textutil text)",
     "quote": "This screen is still defining trickster in different language to the vocab screen for it.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 66,
   "verdict": "keep-with-fix",
   "reason": "Both quotes are verbatim. The source contrasts defining a character type by its method with defining it by a property. As a universal rule, 'define by what it does' would be wrong for concepts that are defined by their properties, so I reworded it as defining versus typical features, which is what the trickster case shows.",
   "statement": "Define a concept by its defining feature (for a character type, what it does) rather than by a property its typical examples happen to share, because making a typical property definitional invites over-generalisation.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "137-138",
     "quote": "Prefer a definition by **method** (what the character *does*) over one by **property** (what they *are*).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "140",
     "quote": "Property definitions are what generate the over-generalisation in A3.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 67,
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim; 53 of 58 matches, and the addendum's field note confirms the three-features-vary shape. I added the local criterion for the max-different example (D1.18). 'Say why the non-example fails' still rests on the archive.",
   "statement": "Teach a distinction with an example and a non-example that differ in one feature, say why the non-example fails by naming that feature, and then add a very different example that still fits.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "396",
     "quote": "| **S1** | Every vocab `non_example` states **why** it is not an example | 53 / 58 cards state no reason |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "158-159",
     "quote": "only the max-different example *kills the over-generalisation the pair invites*.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D1-gradual-release-explicit-instruction.md",
     "lines": "28",
     "quote": "Non-examples are minimally different from examples to mark the boundary",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D1-gradual-release-explicit-instruction.md",
     "lines": "29",
     "quote": "later juxtapose max-different examples that still fit",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 68,
   "verdict": "keep",
   "reason": "All quotes are verbatim; 12 of 46 and 16 of 19 match, and the 8× and 48× counts are at line 56 of the same failure-classes file. This refines truth 18 on timing and consistency.",
   "statement": "Teach a word no later than its first heavy use, make sure every taught word appears in the lesson's own material, and keep what learners are invited to use identical to what was taught.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "210",
     "quote": "iter-3: 12 of 46 taught words never occur in their own passage, so they can't be met in context or tapped there",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "71",
     "quote": "The rule is **first heavy use**, not peak use.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "401",
     "quote": "| **S6** | A declared set equals the set actually used (chips == taught words; scorer credits them) | chips wrong in **16 / 19** |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 69,
   "verdict": "keep",
   "reason": "Both quotes are verbatim (the second is at line 163); 39 of 46 and 6 match. They appear only in the name-bearing archive.",
   "statement": "Count something as already shown to a learner only if every path to that point shows it, because branches they may not take and skippable media establish nothing.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "152",
     "quote": "**\"Already seen\" must be an INTERSECTION over branch points, never a union.**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "163",
     "quote": "The intersection changed the finding from *\"39 of 46 clean\"* to **6 more real defects**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 70,
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim. 'Or names' had no quote behind it, so I added G3 criterion D10.11 (not 'matching gods' names'). The standard's failure signal at line 233, 'links based only on shared words', also applies.",
   "statement": "Give each unit one primary understanding and link units by ideas rather than by shared words or names.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "237",
     "quote": "J16-CUR-003: Give every unit one primary understanding.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "237",
     "quote": "J16-CUR-004: Use conceptual rather than surface cross-unit links.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D10-delivery-ux-accessibility.md",
     "lines": "22",
     "quote": "Cross-unit links are stated as the big idea, not as surface facts (not \"matching gods' names\")",
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
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim. 'Flag simplified models' had no quote behind it, so I added the taxonomy's class for a model shown without a simplification warning (line 147).",
   "statement": "Flag simplified models as simplifications and check wording for misconceptions it implies even without a banned phrase, because text that embeds a folk belief undoes correct teaching.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "145",
     "quote": "\"the plant grows by taking food from the soil\" implies plants-eat-soil without the literal phrase",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "802",
     "quote": "Simplification is acceptable only when it remains accurate and does not create a later-blocking misconception.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "147",
     "quote": "a food chain / atom / cell diagram presented as literal reality",
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
   "verdict": "keep",
   "reason": "Both quotes are verbatim. The same standard row also lists J16-SCI-006, 'Keep cross-domain terminology and mechanisms consistent.'",
   "statement": "Keep terms and explanations consistent with how other units and courses teach the same idea, reinforcing established framings rather than silently redefining them.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "805",
     "quote": "J16-SCI-003: Reinforce rather than silently redefine established domain knowledge.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "149",
     "quote": "reinforce-don't-redefine (consistent with the subject app's framing)",
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
   "reason": "The quote is verbatim. It is a single reviewer obligation in the standard, and it is general.",
   "statement": "Keep fact, interpretation, opinion and uncertainty distinct in what learners read.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "805",
     "quote": "J16-SOC-002: Preserve distinctions among fact, interpretation, opinion, and uncertainty.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 74,
   "verdict": "keep",
   "reason": "Both quotes are verbatim; ~22% vs ~40% matches. Eval-criteria C4 (line 115) says the same: 'complexity judged qualitatively, not by Lexile alone'.",
   "statement": "Choose material for purpose, genre balance and quality rather than by a single difficulty score.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "166",
     "quote": "G3 was flagged at **~22% literary vs ~40% target** because texts were picked on Lexile alone",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D8-text-quality.md",
     "lines": "22",
     "quote": "No rigid monotonic Lexile laddering is imposed, since prior knowledge can make a harder text accessible",
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
   "reason": "All quotes are verbatim (the first is at lines 34-35); 0.17 and the 3-sentence run match, and the clean sample scored 0.58.",
   "statement": "Screen every generated text for difficulty and cohesion, and let the automatic screen reject or flag but never approve, because generated texts tend to run too hard and cohere poorly.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/text-quality-lane.md",
     "lines": "34-35",
     "quote": "the screen independently flagged **cohesion density 0.17 with a 3-sentence static run**",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/text-quality-lane.md",
     "lines": "5-6",
     "quote": "the machine stage never approves, it only rejects and orders the queue.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D8-text-quality.md",
     "lines": "21",
     "quote": "AI-generated texts get human/expert QA because they run too hard in syntax and vocabulary and too weak on cohesion",
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
   "reason": "The quote is verbatim and 'grade 11 vs grade 3' matches. It is one case, but the check is cheap and general.",
   "statement": "Check a generator's target level before every batch.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "224",
     "quote": "the generator was calibrating passages at **grade 11, not grade 3**; verify the target grade before any batch",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 77,
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim; 58–217 words vs ~2,740 matches. 'Never builds the stamina' is a causal claim the source does not test, so I reworded it to what short pieces demonstrably cannot do: rehearse the target length.",
   "statement": "Ramp the length and demand of materials toward what the target task requires, because a course of short pieces never rehearses the stamina that task demands.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "224",
     "quote": "G3 passages were 58–217w when the test reality is multi-passage (~2,740w); ramp length toward test stamina",
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
   "verdict": "keep",
   "reason": "The quote is verbatim. It applies to any material tied to the exact wording of a source.",
   "statement": "Clear the rights to a source before writing material tied to its exact words, because material coupled to a withdrawn source is lost.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-modes-spec.md",
     "lines": "110-112",
     "quote": "copyright clears **passages before span-anchored authoring begins** — scripts and cite-items couple to exact text; a passage pulled after authoring loses the lesson's artifacts.",
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
   "verdict": "keep-with-fix",
   "reason": "Both quotes are verbatim. The cited risk is a prediction ('a good chance they'll all get rejected'), not an observed joint rejection. The blocking rule names lesson spines, difficulty and units, not length. I reworded the statement to match.",
   "statement": "When several courses for different levels come from the same guidance, require each to differ from its nearest sibling in more than its lesson list, difficulty and units, because near-copies share the same weaknesses and risk being rejected together.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/grade-band-profiles.md",
     "lines": "7",
     "quote": "rejected for the same underlying reasons. We're just failing in parallel.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "99-101",
     "quote": "**\"Sibling clone\" is a blocking red-team finding class**: a design whose only deltas from the nearest sibling are lesson spines/difficulty/units fails review before the academics ever see it.",
     "verbatim": true
    }
   ],
   "against": "The joint-rejection risk is a stated concern, not an observed outcome.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 80,
   "verdict": "keep",
   "reason": "The quote is verbatim (lines 354-355). It is one case, adopted as a rule, and appears only in the name-bearing archive.",
   "statement": "An in-text explanation works only if readers read it as one, so treat a misread gloss as failed and make it explicit.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "354-355",
     "quote": "When a reviewer misreads an in-text gloss, the gloss has failed by demonstration; make it explicit.",
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
   "reason": "All quotes are verbatim. It overlaps the evidence-status tagging candidate (index 103) but focuses on keeping readiness states apart, and goes further than truth 48.",
   "statement": "Word each claim only as strongly as the instrument that measured it, keeping 'built', 'checked', 'live', 'accepted' and 'works' as separate states.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/course-quality.qmd",
     "lines": "61",
     "quote": "A fully green build gate proves the course is well-built. It does not prove the course works.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "157",
     "quote": "Claims are licensed by instruments, nothing else",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "26",
     "quote": "Authored, mechanically validated, runtime verified, human accepted, production verified, and outcome validated remain distinct states.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 82,
   "verdict": "keep",
   "reason": "Both quotes are verbatim. The local counts disagree (1 of 18 in the skill file and in D1 line 47, 3 of 18 in the taxonomy), but either way the quality was missing from most lessons, and the statement avoids the number.",
   "statement": "Check every lesson rather than the polished one already shown, and record what was checked, unchecked and excluded, because a quality present in the showcase can be missing from most of the rest.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "77-78",
     "quote": "G3 iter-3's real \"reject-the-alternative\" modeling held in 1 of 18 lessons; the reviewed lesson (U2·L1) was that one.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "29",
     "quote": "A coverage manifest names every governed object, checked scope, unchecked scope, failures, and exclusions.",
     "verbatim": true
    }
   ],
   "against": "finding-taxonomy.md 191 gives a different count for the same audit: \"existed in **3 of 18** lessons — the reviewed lesson (U2·L1) plus two\"; course-red-team/SKILL.md 77-78 and D1-gradual-release-explicit-instruction.md 47 say 1 of 18.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 83,
   "verdict": "keep",
   "reason": "All quotes are verbatim and 191 matches. It overlaps truth 66 on independence but adds the ban on authors certifying their own work and the check of claimed independence against the build record.",
   "statement": "Don't let the maker of content certify it, and check any claimed independence of the checker against the record of who actually ran the check.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "22",
     "quote": "G5 R4: 191 choice items certified on a same-family lane while docs said \"every item blind-probed under a different model family\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-content-integrity/SKILL.md",
     "lines": "263-264",
     "quote": "Do not certify your own authored content. The author may fix findings; an independent reviewer must close them.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/evaluator-contracts/SEMANTIC-JUDGE.qmd",
     "lines": "8",
     "quote": "Use a model family independent of generation",
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
   "reason": "Both quotes are verbatim (the cached-bundle quote is at line 47). The same golden-checklist row applies the rule to 'content, renderer, rubric, model, policy, or dependency change'.",
   "statement": "Treat any relevant change to content, scoring rules, model or display as voiding the checks and certifications done on the old version, and re-run them instead of carrying results forward.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "35",
     "quote": "Evidence records carry artifact and dependency digests; relevant changes force the affected checks to be rerun.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "47",
     "quote": "never cache-as-truth (a cached bundle can certify content no longer deployed).",
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
   "verdict": "keep",
   "reason": "All quotes are verbatim. Six formats becoming five matches, and the same G5 finding records that all 20 two-part items were excluded.",
   "statement": "After fixing or filtering material, check what survived, because a purge of faulty items can silently remove a whole format or a strength that was working.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g5-reading-redteam-round1-2026-07-06.md",
     "lines": "27",
     "quote": "6-format MAP coverage quietly becomes 5-format on the certified core.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "183",
     "quote": "Visual alignment deletes reasoning; simpler flow removes access; old evidence reused after change.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "33",
     "quote": "Impact analysis names affected PRESERVE results; each guard is rerun on changed bytes and passes an equivalence-or-better test.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 86,
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim (the second is at line 65) and every count matches: 52/745/56 vs 47/713, 541/549/559, and 520 vs 650. I removed a job role ('reviewers') from the statement.",
   "statement": "Quote every count from one dated, re-runnable source and ship the data and tools to recompute it, because hand-typed figures drift between documents and undermine the review.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "262",
     "quote": "G3's email said 52/745/56 while the infographic said 47/713 (finding #11); G5 certified-count drifted **541 vs 549 vs 559** across docs; MAP-proxy summary tables summed to 520 while claiming 650.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "65",
     "quote": "**Prose drifts; data doesn't.** Hand-typed figures across ~15 artifacts WILL drift.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "263",
     "quote": "G4's package cited `course_bank.json`, `item_ledger_manifest.json`, `EVIDENCE_AND_CRITERIA.qmd` etc. but bundled **none** of them, so a reviewer without repo access takes every count on trust.",
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
   "reason": "Both quotes are verbatim; 206.4 / 72nd and 196.0 / 46th (n=915) match the archived audit table. It overlaps the threshold-reuse candidate (index 33) but concerns reported figures, not pass bars.",
   "statement": "Never borrow another group's numbers or a biased slice's baseline as your own; mark unmeasured figures as open and re-measure before claiming.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "262",
     "quote": "the MAP-proxy shipped a retired \"206.4 / 72nd percentile\" baseline that was a biased slice; the real figure was **196.0 / 46th pctile (n=915)**.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "29-30",
     "quote": "**Never invent a magnitude.** Do not carry another grade's/cohort's numbers as if they were this one's.",
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
   "reason": "Both quotes are verbatim and the 11-item count matches. Related to truths 46 and 47, but this one is about claims that a fix works.",
   "statement": "Treat a reported fix as unverified until it is shown working on the surface the review uses, with the same exploits, because most of one round's 'done and live' fixes failed review.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "101-102",
     "quote": "Round 2: most of an 11-item fix report failed live review, including the original kill exploit.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "91-93",
     "quote": "**No \"done & live\" without an independent student-seat walkthrough on the same surface the reviewer uses, running the reviewer's exact bypasses.** Two rounds of unverified fix reports is how trust dies.",
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
   "reason": "Both quotes are verbatim (the second starts at line 308). It overlaps truth 60 only on new failures.",
   "statement": "After a round of fixes, re-derive every earlier finding from the current material and look for new defects the fixes introduced, such as stale figures and contradictions.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "306",
     "quote": "Re-verify **every** prior finding by recomputation — not the disposition table.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "308",
     "quote": "Sweep for NEW issues introduced by the fix wave (fixes introduce contradictions:",
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
   "verdict": "keep",
   "reason": "All quotes are verbatim. Nine rules, five days, three rounds and 22 of 30 (build rules line 1044) match. They appear only in the name-bearing archive.",
   "statement": "A rule written into a document is not enforced until a check runs it, so before closing a review round check every previously adopted rule against the material by name.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "87",
     "quote": "The G3 2026-08-11 round re-reported NINE rules adopted five days earlier",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "89-90",
     "quote": "Three consecutive rounds, one unenforced rule. Prose in an addendum gets read, not run.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "1045-1046",
     "quote": "the standard was not missing them, this build shipped without running them.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 91,
   "verdict": "keep",
   "reason": "Both quotes are verbatim (the first is at lines 97-99); 2/151, 13/213 with 11 false, and 392/104/284 match. It overlaps truth 38 on catching a known fault, but adds the test that a check does not fire on everything and the raw/exempted/real way of reporting counts.",
   "statement": "Before relying on a new check, confirm it catches the example that prompted it and doesn't fire on nearly everything, and report its counts as raw, exempted and real with the exemption rule stated.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "97-99",
     "quote": "correct-is-longest and stem-overlap missed the seed entirely (the real cue was grammatical odd-one-out, 2/151), the first cut of that check fired 13/213 with 11 false",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "102-104",
     "quote": "An all-caps sweep read 392 raw; 104 were play-script speaker labels and a skill name; the real number was 284.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 92,
   "verdict": "keep",
   "reason": "All quotes are verbatim. The first half restates truth 38: a check proves nothing until it sees a known case. Kept for the added evidence (an analyzer that read the wrong field reported zero standards; a NUL byte blinded two searches) and for the point that two checks agreeing by the same blind method count as one.",
   "statement": "Before reporting something as missing, prove the instrument can see a case known to be there, because an empty result from a blind check is not evidence of absence and two checks using the same blind method agreeing count only once.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/timeback-course-eval/examples/reading-explorers-g3-allqtypes.md",
     "lines": "123",
     "quote": "the morning analyzer missed them because it only scanned `rawXml`; standards are in structured metadata, not inline XML",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "96-97",
     "quote": "**Two agents independently agreeing via the same blind method is one unverified claim counted twice, not corroboration**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "98-99",
     "quote": "For a claim of ABSENCE, prove your instrument can see a string you know is there before you trust the empty result.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "38",
   "name_bearing_source": true
  },
  {
   "index": 93,
   "verdict": "keep",
   "reason": "Both quotes are verbatim (the first is at lines 219-220) and 34/34 matches. Distinct from truth 38: here the check runs and passes, but on the wrong subject.",
   "statement": "Ask what a passing check would still pass on, because a check can be true about the wrong element or data stream and stay green while the real thing is broken.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "219-220",
     "quote": "**a gate that asserts something true about the wrong subject.**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "225-226",
     "quote": "a header-swap mutation passed 34/34 while the receipt showed teaching as −1 under \"Reading questions\"",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 94,
   "verdict": "keep",
   "reason": "Both quotes are verbatim. The source's rule is to print the rendered panel in DOM order and read it as prose. They appear only in the name-bearing archive.",
   "statement": "Read each rendered screen whole and in display order as the learner meets it, because parts that each pass their own check can add up to a contradictory screen.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "265",
     "quote": "Five patches to one panel each passed their own gate while the panel stayed incoherent.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "267-268",
     "quote": "the tick row showed three criteria while the rubric graded four, so the one criterion that decided the verdict was invisible.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 95,
   "verdict": "keep",
   "reason": "The quote is verbatim; ~29 gates and 1400×1000 match. It is an instance of truth 46 (review in the mode learners get), kept for its evidence.",
   "statement": "Run layout checks at the learners' real screen size, because checks run only at desktop size hid an overflow on every screen.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "280-281",
     "quote": "~29 gates all ran at 1400×1000, hiding a top-bar overflow on **every beat of every lesson**.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "46",
   "name_bearing_source": true
  },
  {
   "index": 96,
   "verdict": "keep",
   "reason": "All quotes are verbatim; 98% (53 of 54) and 'over 120 strings' match. They appear only in the name-bearing archive.",
   "statement": "Apply a check to every item type and every file that holds learner-facing content, and fail if that list comes out empty, because checks wired to part of the material leave whole types unguarded.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "120-121",
     "quote": "hook 69% A, we-do 53% A, **vocab 98% A** (53 of 54). A child tapping A scored nearly three quarters of the course's vocabulary.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "127",
     "quote": "**Enumerate every item type that carries a key**, then assert the enumeration",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "84-86",
     "quote": "Its corpus is `FILES` at line 110, five names, which omits `read_stops.json`, `story_pattern.json` and `skill.json`: over 120 strings carrying every stop MCQ and story-pattern row",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 97,
   "verdict": "keep",
   "reason": "All quotes are verbatim and 117 of 179 matches. They appear only in the name-bearing archive.",
   "statement": "When text that drives generated audio or other media changes, regenerate and verify that media in the same run with exact whole-string matching, because steps that can be run separately get run separately and leave silent gaps.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "61-62",
     "quote": "found **117 of 179 narrated strings orphaned** by the round's own rewrite",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "64-65",
     "quote": "two checks that *can* be run separately *will* be run separately.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "76-77",
     "quote": "**A drift check that tolerates prefixes silently exempts every string that was EXTENDED, and extension is the most common shape of a feedback edit**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 98,
   "verdict": "keep",
   "reason": "Both quotes are verbatim (the content-integrity quote is at lines 45-46). The first half has a local source; the second appears only in the archive.",
   "statement": "Fix a defect in the source specification or generator as well as in the delivered copy, because a downstream-only fix is undone by regeneration and an upstream-only fix never reaches material already built.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-content-integrity/SKILL.md",
     "lines": "45-46",
     "quote": "A rendered lesson that silently fixes a bad specification does not close the upstream defect because regeneration can reintroduce it.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "392-393",
     "quote": "A rule fixed in the generator prompt does not reach any lesson already on disk, and a fix applied on disk does not survive the next regen",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 99,
   "verdict": "keep",
   "reason": "Both quotes are verbatim (the first is at lines 46-47). It is a structural case of truth 3, kept for the design principle that a constraint the system cannot break beats a rule the model must remember.",
   "statement": "Where a model speaks before the learner has read the material, don't give it that material, so it cannot give away what comes next; a constraint the system can't break beats a rule the model must remember.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "46-47",
     "quote": "pre-passage moments send the scorer an **empty passage and empty vocab list**, so it *cannot* quote what the child hasn't read.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "47",
     "quote": "A rule you can't violate beats a rule you must remember.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 100,
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim; 5,396 and ~65 match, and the calibration line is at 87. The source describes calibration as a --calibrate run in which all 20 known-good strings must come back clean. Nothing says it runs every time or blocks the run, so I removed 'every run'.",
   "statement": "Prefilter in code so a model judges only the suspects, pin each verdict to a hash of the rules version and the exact content so re-runs can't flip it, and calibrate the judge on known-good cases that must all come back clean, so a broken judge is caught.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "84",
     "quote": "**Regex prefilter** cuts 5,396 strings to ~65 suspects, so the LLM judges 1% of the corpus.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "85-86",
     "quote": "**Verdicts pinned** by `sha256(RULES_VERSION + string)` — a model that flips its mind can't flap the gate.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "87",
     "quote": "feeds 20 known-good strings; all must come back clean, or the judge is broken.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 101,
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim. I added the semantic-judge contract (independent model family, quoted evidence, advisory until qualified) and replaced 'expert-labelled' with 'human-labelled' to keep job roles out. It goes further than truth 37.",
   "statement": "Have a model judge quote the evidence it relies on and use a family independent of the generator, keeping its verdict advisory until it is calibrated on human-labelled examples.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D1-gradual-release-explicit-instruction.md",
     "lines": "45",
     "quote": "scored on a model family ≠ the generator, with evidence quotes, against academics-labeled anchor lessons.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/evaluator-contracts/SEMANTIC-JUDGE.qmd",
     "lines": "8-10",
     "quote": "Use a model family independent of generation, pin its identity, require calibration anchors and human qualification, and retain quoted/source-pinned evidence. Until qualified, semantic results are advisory and cannot emit `PRESERVE` or replace human sign-off.",
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
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim. The source says to re-ask once and then mark the check RED; the statement now says what happens after the re-ask. Related to truth 9 but distinct.",
   "statement": "Treat a judge that returns the same verdict for every case as having given no answer: re-ask once, then count the check as failed, never as passed.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/video-red-team/references/finding-taxonomy.md",
     "lines": "93-94",
     "quote": "**Flat score row** — the judge returns identical/undiscriminating statuses; treat as a non-answer (re-ask once, then RED), never as a pass.",
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
   "reason": "Both quotes are verbatim.",
   "statement": "Tag every claim and threshold with its evidence status — measured, asserted, open or working heuristic — and never quietly promote it to a stronger status.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "35-37",
     "quote": "**Epistemic tags on shipped claims.** Verified (recomputed/measured) · Asserted (stated in a design, checkable only in delivery) · Open (needs data that doesn't exist yet). Never silently promote Asserted→Verified or Open→Asserted.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/video-red-team/references/rubric.md",
     "lines": "8",
     "quote": "An [OH] is never cited as a proven learning threshold.",
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
   "reason": "Both quotes are verbatim. The local gauntlet spec lists the same probe among its permanent regression probes; the evidence that it caught its own regression appears only in the archive.",
   "statement": "Turn every defect found in review into a permanent test before the fix ships, so the test catches the defect if it ever returns.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/SKILL.md",
     "lines": "67-68",
     "quote": "**Every externally demonstrated defect becomes a permanent gauntlet probe before any fix ships** (the strongest guarantee in the system: the test outlives the fix).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-1/teacher-skill/gauntlet/CONVERGENCE-REPORT.md",
     "lines": "20-21",
     "quote": "is now a permanent gauntlet probe that earned its keep in round 2 by catching its own regression.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 105,
   "verdict": "keep",
   "reason": "The quote is verbatim. An archived layer-5 result applies the same rule ('a confirming round is still required').",
   "statement": "Stop reviewing a layer only after two consecutive rounds find nothing new.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/gauntlet-spec.md",
     "lines": "3-4",
     "quote": "each layer must go **dry** (two consecutive rounds, zero new findings) before the next.",
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
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim. I reworded 'judges the builder never used' and 'experts' to keep job roles out. The gauntlet spec's anti-Goodhart rules (lines 91-95) say the same.",
   "statement": "Keep checks from becoming the target: rotate probes, hold some back, use judges from model families never used to build the material, periodically re-anchor them to human judgment, and audit the checks themselves.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/SKILL.md",
     "lines": "116-119",
     "quote": "Rotate probe seeds and personas every round; hold out one probe family per promotion; judges from unseen model families; periodic expert re-anchoring; and red-team the gauntlet itself with `course-red-team` (our own single-shuffle gate bug is the standing reminder that the gate can be the bug).",
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
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim. I replaced 'reviewers', a job role, with 'feedback'.",
   "statement": "Record conflicts between sources, feedback or rules as named open questions for a decision, and never average them or quietly pick one.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/SKILL.md",
     "lines": "47-48",
     "quote": "Conflicts are recorded in `tensions.md`, never averaged.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/crosswalk/CONFLICT-LEDGER.qmd",
     "lines": "8",
     "quote": "open decisions and fixes are explicit; no conflict was flattened.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "191",
     "quote": "a domain scoring high on frequency but low on load-bearing (present the tension, don't average it away).",
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
   "reason": "All quotes are verbatim. The standard's learner outcome reads: 'Nothing material is lost behind a bulk statement that feedback was addressed.'",
   "statement": "Map every point of feedback individually to a decision and evidence, neither dropping it nor silently turning it into a universal rule, because bulk 'addressed' statements lose points.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "25",
     "quote": "Each source point has a disposition and links to one or more requirements, exact evidence, an owner when open, and a closed or unresolved state.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/profiles/base/RED_TEAM_BASE.source.json",
     "lines": "1410",
     "quote": "Feedback is neither dropped nor silently promoted into universal policy.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "54",
     "quote": "Bulk addressed claims; missing source points; evidence with no feedback link.",
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
   "verdict": "keep-with-fix",
   "reason": "Both quotes are verbatim (the authority quote is at line 31). The rationale 'grouping or indexing a rule does not make it universal' was not in any cited file, so I replaced it with what the authority file says and added an example from the universal standard.",
   "statement": "Keep a rule scoped to the level, subject or source it came from until a recorded decision extends it; a scoped rule must never silently become universal.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/AUTHORITY.qmd",
     "lines": "31",
     "quote": "A scoped overlay never silently becomes universal; a runtime or context asset never silently becomes",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "231-233",
     "quote": "The current G3 profile requires at least four options on every MCQ, prohibits mastery True/False, and prohibits EBSR; do not generalize those thresholds to another profile.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "770",
     "quote": "No fixed option count belongs in the universal standard.",
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
   "reason": "The quote is verbatim; 269 transcripts were reviewed in nine independent batches. It is a general method for synthesising outside sources.",
   "statement": "In a review of outside sources, treat a technique seen once as a candidate and promote it to a rule only when it recurs across independent batches.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/IES-CORPUS-REVIEW-2026-08-05.md",
     "lines": "17-18",
     "quote": "Findings that recurred across *independent* batches were treated as high-confidence; a technique seen once was treated as a candidate, not a rule.",
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
   "reason": "The quote is verbatim, and the rule is general.",
   "statement": "Research that supports a design is not evidence that your implementation of it works, so never cite it as an outcome.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/reading-science/PRIORITIES.qmd",
     "lines": "82-83",
     "quote": "corpus grounds DESIGN, it does not prove OUR implementation works. Never cite it as evidence about our courses' outcomes.",
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
   "reason": "All quotes are verbatim (the 'never re-typed' line is 50). The pipeline applied all three rules and verified 230 of 230 quotes. General for any knowledge base.",
   "statement": "When turning source documents into a knowledge base, check each extraction reaches the document's true end, never ingest an empty extraction, and copy source text by file rather than having a model retype it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/reading-science/EXTRACTION_EVIDENCE.qmd",
     "lines": "39",
     "quote": "(does each extraction reach the document's true end?)",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/reading-science/EXTRACTION_EVIDENCE.qmd",
     "lines": "50",
     "quote": "the full texts here were never re-typed through a model.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/knowledge-ingest/SKILL.md",
     "lines": "41-42",
     "quote": "a scanned PDF yielding whitespace is `skipped: needs-manual-export`, never ingested empty.",
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
   "reason": "Both quotes are verbatim; ~67% and r≈0.72–0.79 match. The train-teacher skill (lines 119-120) says the same.",
   "statement": "Label results from simulated learners as predictions, never outcomes, and calibrate them against real learners when that data exists.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/gauntlet-spec.md",
     "lines": "50-51",
     "quote": "**All results labeled SIMULATED**; calibrate against real-student data as pilots run.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/generator-insights.md",
     "lines": "123-124",
     "quote": "LLM student role-play is structurally flawed and caps ~67% accuracy; teacher-as-predictor reaches r≈0.72–0.79 population-level",
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
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim; 772/772 and 957/957 match. 'Far better than none' overstated the source, which says a sampled review of about 60 items converts '0 human-reviewed' into 'sampled + attested'. I reworded it to that.",
   "statement": "Put nothing in front of learners that no person has read; even a sampled human review turns 'no one has read this' into 'sampled and attested'.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "263",
     "quote": "`humanApproved:false` on 772/772 (G5) / 957/957 (G4) submitted to educators means \"no human has read what you'd put in front of ten-year-olds\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "263",
     "quote": "even a sampled ~60-item review converts \"0 human-reviewed\" into \"sampled + attested\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "101",
     "quote": "Human edit pass before ship — \"several read as unedited AI output\" must never recur.",
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
   "verdict": "keep",
   "reason": "Both quotes are verbatim and 231/772 (30%) matches. Distinct from truth 59.",
   "statement": "Remove items known to be faulty from what learners see, not just from scoring, because a guessable item still rewards skipping the work.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "233",
     "quote": "G5 shipped with **231/772 (30%) classified known_leaky still live** (excluded from gates but in front of children)",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g5-reading-redteam-round1-2026-07-06.md",
     "lines": "17",
     "quote": "A leaky item awards progress for non-reading",
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
   "verdict": "keep-with-fix",
   "reason": "Both quotes are verbatim and 4 of 11 matches. 'Keep its controls out of learners' reach' had no quote behind it, so I added the archived finding that a previewer chip tappable in student mode defeated every gate, plus the local modes-spec line on an unlocked mode that mints no mastery evidence.",
   "statement": "Provide an unlocked path through every lesson for review, but keep its controls out of learners' reach and stop it creating learner records.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "105-106",
     "quote": "Locked lesson progression blocked half the round-2 review — 4 of 11 items came back \"unable to verify\".",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "34",
     "quote": "Free navigation, answer reveal, reset, and reviewer-only controls leave mastery, reward, completion, and unlock records unchanged.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-modes-spec.md",
     "lines": "114-115",
     "quote": "a reviewer mode that unlocks lessons **without minting mastery evidence**",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-4/REDTEAM-U1L1-2026-08-05.md",
     "lines": "41",
     "quote": "The 🎒 Student/👁 Previewer chip is visible and tappable in student mode — **one child tap defeats every gate in the lesson** (live-proven)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 117,
   "verdict": "keep",
   "reason": "All quotes are verbatim; 525/772 and 406/1,005 (40%) match.",
   "statement": "Formats chosen to resist guessing are often the least accessible, so prove keyboard and assistive-technology operation for every interaction type and don't let anti-guessing controls block legitimate access.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g5-reading-redteam-round1-2026-07-06.md",
     "lines": "15",
     "quote": "the anti-leak thesis deliberately concentrates items in the TEI formats (hot-text/sequence/match = 525/772) that are precisely the accessibility-risk types.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
     "lines": "63",
     "quote": "Accessibility: 406/1,005 (40%) not keyboard/AT-operable",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "535",
     "quote": "Anti-gaming controls must not block legitimate accessibility paths.",
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
   "verdict": "keep",
   "reason": "Both quotes are verbatim (the brainlift quote is at lines 58-60). This is the reasoning behind truth 28, kept for its evidence and for the reframing: a bypass places learners past what they know and poisons the data used to improve the material.",
   "statement": "Treat a bypassable gate as a teaching failure, not just a security gap, because it moves learners past what they know and corrupts the data used to improve the material.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/timeback-course-eval/references/eval-criteria.md",
     "lines": "135",
     "quote": "produces a *poisoned feedback signal* — kid-outcome data from a gameable course can't improve",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "58-60",
     "quote": "A gate a child can bypass doesn't just corrupt the data; it places the child outside their zone of proximal development *by construction*",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "28",
   "name_bearing_source": false
  },
  {
   "index": 119,
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim. I swapped the two name-bearing archive quotes (prompts authored in all 18 lessons and never rendered; rationale in the data that the screen never performed) for the local standard's failure signal and the golden checklist's 'demonstrated as behavior, not inferred from source files'. The kind changes to adopted rule accordingly; the measured cases remain in the archive.",
   "statement": "Count content that is authored but never shown as missing, and check the delivered surface rather than the data.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "350",
     "quote": "Clicks counted as production; authored prompts never render",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "27",
     "quote": "The intended experience is demonstrated as behavior, not inferred from source files or screenshots.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 120,
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim. I swapped the name-bearing guess-through quote for the local standard (guessing or interface tricks cannot manufacture success; repeated submission must not duplicate credit). The statement is unchanged.",
   "statement": "Give progress and rewards only for verified learning, so unmastered work, guessed-through retries and replays earn nothing.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "73",
     "quote": "One reward unit has a published meaning; full reward follows verified mastery; non-mastered work earns zero; nothing below eighty percent earns reward; replay cannot duplicate it; ledger and display agree.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/timeback-course-eval/examples/reading-explorers-g3-allqtypes.md",
     "lines": "187",
     "quote": "Team found the broker fabricates quiz XP with **no 80% floor**",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "532",
     "quote": "Learner outcome: Skipping, guessing, or interface tricks cannot manufacture success.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "534",
     "quote": "Failure signals: Skip-to-pass; inactive time rewarded; revealed answer counted; repeated submission duplicates credit.",
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
   "reason": "The quote is verbatim (RAND, App. A pp. 108-109, as given in the synthesis). The G3 practice criteria (D6.14) schedule on accuracy and latency, not self-report.",
   "statement": "Don't rely on learners' own sense of whether they understood, because people judge their own comprehension poorly; check with a task.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/reading-science/SYNTHESIS.qmd",
     "lines": "180-181",
     "quote": "\"most child and adult readers have a poor ability to calibrate the success of their comprehension\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D6-practice-durable-mastery.md",
     "lines": "25",
     "quote": "schedule on accuracy+latency, not self-report",
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
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim. The source says such assessments 'may inadvertently limit' the curriculum, so I softened 'tend to shrink' to 'can narrow'.",
   "statement": "Assess more than a few task types, because assessments that focus on only a few tasks can narrow teaching to preparation for those tasks.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/reading-science/SYNTHESIS.qmd",
     "lines": "127-129",
     "quote": "\"assessments that are widely used today focus heavily on only a few tasks and thus may inadvertently limit the reading curriculum to preparation for those few tasks.\"",
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
   "reason": "All quotes are verbatim, but the digest file's path contains an author's surname. I re-sourced the claim to the local brainlift (knowing-that and generating-aligned are different capabilities), the evaluator spec (which cites the paper's own limitation) and the requirements note (a generator that 'knows' gradual release still emitted answer-reveals). The external paper is DOI 10.3389/frai.2026.1851993. Kind changed to adopted rule.",
   "statement": "A model's score on questions about teaching does not show it can produce good teaching material, so judge the material it generates.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "79-81",
     "quote": "Knowing-that (answering pedagogy questions) and generating-aligned (producing content that embodies the pedagogy) are different capabilities; the gap must be measured at the artifact level rather than inferred from benchmark scores.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "304-305",
     "quote": "knowing-that != generating-aligned (kb-0121 SPOV2, kb-0124 EduQwen authors' own limitation)",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/train-teacher-requirements.md",
     "lines": "19-20",
     "quote": "a generator can \"know\" gradual release and still emit answer-reveals.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 124,
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim. The contract keeps cold topics out of training data only; prompts are held identical across arms, so 'and prompts' was wrong. The baseline is specifically the untrained base model.",
   "statement": "Evaluate a trained content generator on topics kept out of its training data, against the untrained base model given identical inputs, and replicate before claiming a gain.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "68-69",
     "quote": "**Contamination ledger applies to TRAINING DATA:** cold topics excluded from every training pair.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "71-72",
     "quote": "A model trained on a cold topic cannot be evaluated on it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "53",
     "quote": "**Arm B (base): the untrained base model + the SAME prompts and briefs.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "53-54",
     "quote": "Isolates what training added; run it or the result is uninterpretable.",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "65",
     "quote": "**Same inputs to every arm:** one pinned brief set",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "75-76",
     "quote": "any bar-hit claim needs 2 independent generation runs; a single run is a single-point estimate.",
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
   "reason": "Both quotes are verbatim, and 80%, 74% and 1 in 5 match the brainlift summary. The underlying review of nine quiz builders is not identified in these files, so treat the numbers as second-hand.",
   "statement": "Prefer assembling and adapting vetted material over generating items from scratch, and treat anything generated as a candidate until a separate check passes it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/generator-insights.md",
     "lines": "56-57",
     "quote": "But of 9 Gen-AI quiz builders studied, **80% of items violated ≥1 best-practice guideline and 74% had major flaws — only 1 in 5 usable**",
     "verbatim": true
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/generator-insights.md",
     "lines": "59-60",
     "quote": "**Design generators that assemble + transform vetted material and tag to standards — not ones that invent items from scratch.**",
     "verbatim": true
    }
   ],
   "against": "practice-layer-spec.md 22: construction-first generation still certified \"48.7% (738 certified of 1,516)\" under gates; the cited review of nine quiz builders has no DOI or URL in these files.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
   "lines": "114",
   "quote": "On a miss: **Correct** (answer + brief why) → **Test** (re-ask immediately) →",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D1-gradual-release-explicit-instruction.md",
   "lines": "36",
   "quote": "wrong answers corrected immediately with the correct answer + brief why",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g5-reading/approval-package/D9-GATE-WALKTHROUGH.md",
   "lines": "30",
   "quote": "**The correct answer is shown after a miss** (auto-highlighted)",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
   "lines": "50",
   "quote": "a wrong answer returns only \"Good try, let's look again,\" with no explanation and no correct answer shown.",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D2-opportunities-to-respond.md",
   "lines": "25",
   "quote": "The app never restates the correct answer for the child; it prompts the child to complete/say it",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "399",
   "quote": "Immediate answer reveal; identical retry; endless loop; supported retry counted as first independent success.",
   "ok": true
  },
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/video-red-team/references/rubric.md",
   "lines": "88",
   "quote": "One calm, grade-appropriate voice, conversational 2nd person (r15).",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/labeled-defect-corpus.jsonl",
   "lines": "2",
   "quote": "teaching content leaking the answer to the check it precedes.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "883",
   "quote": "Vocabulary support must not pre-answer the target question.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "43",
   "quote": "The durable rule is attempt first, then targeted help.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
   "lines": "226-227",
   "quote": "RT-10 found the video-2 check answerable from the title alone.",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "43",
   "quote": "offered three consecutive errors as a possible backend trigger",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-4/REDTEAM-R2-2026-08-06.md",
   "lines": "159-160",
   "quote": "`buildMCQ` has no lockout and never withholds the key, so every stop released on or before the 4th tap.",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
   "lines": "43",
   "quote": "6/6 were solvable without the passage:",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
   "lines": "233",
   "quote": "a course-wide audit found **~half of ~700 items gameable**",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-4/REDTEAM-R2-2026-08-06.md",
   "lines": "88-89",
   "quote": "A clean-room blind-solver with no passage got **4/4** and reported that not one item required reading.",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-content-integrity/SKILL.md",
   "lines": "155-156",
   "quote": "\"The intended answer is stronger\" does not repair a hard-scored item when another option also answers the question.",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-ENTRYPOINT-CLEAN-ROOM-G3-U4-L1-2026-08-06.qmd",
   "lines": "59-60",
   "quote": "One hot-text prompt can reasonably be answered by either winter or spring camouflage, while only the winter sentence is keyed.",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "205",
   "quote": "stop at key points INSIDE the text and ask right there (REL West), not only at the end",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
   "lines": "225",
   "quote": "the G4 pull found **79% of MCQ correct answers at Choice A**",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
   "lines": "255",
   "quote": "`shuffle=\"true\"` in the authored XML neutralizes an answer-position skew ONLY if each renderer honors it.",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-content-integrity/SKILL.md",
   "lines": "24-25",
   "quote": "`NEEDS_HUMAN`: evidence is missing, conflicting, inaccessible, malformed, or specialist judgment is genuinely required.",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/course-quality.qmd",
   "lines": "77",
   "quote": "A surface may have emission code but an unreadable or under-scoped token (a reachability gap), or may not emit at all (a coding gap). The first is `UNVERIFIED` pending a scoped read; the second is `FAIL`.",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "655",
   "quote": "Keyword or word-count pass called comprehension",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-LIBRARY-USABILITY-CLEAN-ROOM-2026-08-07.qmd",
   "lines": "64",
   "quote": "Written-response completion can accept a fluent but false response through length and selection counts.",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md",
   "lines": "32",
   "quote": "Short-text items use a small 0/1/2 micro-rubric, not an ever-growing exact-match list",
   "ok": true
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/grade-band-profiles.md",
   "lines": "44",
   "quote": "child-ASR ~13% error blocks production mastery",
   "ok": true
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "705",
   "quote": "Speech can support practice without becoming protected evidence unless its scoring is validated.",
   "ok": true
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/PROJECTION.qmd",
   "lines": "50-51",
   "quote": "a prompt-like unknown field also fails the closed input contract and is never treated as an instruction.",
   "ok": false
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "400",
   "quote": "Repair evidence remains distinct from first-try evidence.",
   "ok": true
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md",
   "lines": "42",
   "quote": "No mastery decision rests on a single MCQ (≥25% guess); use item bundles",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/IES-CORPUS-REVIEW-2026-08-05.md",
   "lines": "121",
   "quote": "116 of 116 confirmed as real substrings, zero invented.",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/reading-science/EXTRACTION_EVIDENCE.qmd",
   "lines": "32",
   "quote": "230/230 extracted quotes verified verbatim at extraction time",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-1/teacher-skill/gauntlet/layer5/RESULT.md",
   "lines": "39",
   "quote": "**Fabricated evidence**: Q16 Part B quotes a sentence not in the text.",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "210",
   "quote": "iter-3: 12 of 46 taught words never occur in their own passage, so they can't be met in context or tapped there",
   "ok": true
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/video-red-team/references/rubric.md",
   "lines": "13",
   "quote": "Audio is the master clock; a reveal MUST NOT complete before its term is spoken (r4).",
   "ok": true
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/feedback/feedback5/Feedback 11.08.docx",
   "lines": "14 (textutil text)",
   "quote": "The things being done to the text must happen immediately after they are spoken about.",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/video-red-team/references/finding-taxonomy.md",
   "lines": "24",
   "quote": "image-model text corruption",
   "ok": true
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/source-course-refinement.qmd",
   "lines": "102",
   "quote": "If an additive layer changes source content, split the change and re-run no-cut.",
   "ok": true
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/source-course-refinement.qmd",
   "lines": "47",
   "quote": "| No silent cuts | Missing source ids fail the build. |",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "91",
   "quote": "Unit-2: a fix-note said \"11w\" while the delivered option was 10w",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "176",
   "quote": "Measured: informational passages were **312–333** while",
   "ok": true
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D10-delivery-ux-accessibility.md",
   "lines": "18",
   "quote": "No on-screen text that merely duplicates speech",
   "ok": true
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "83",
   "quote": "too much on screen",
   "ok": true
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
   "lines": "88",
   "quote": "**Automated WCAG contrast checks** in render QA (round-2 found black-on-black).",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
   "lines": "84",
   "quote": "**Attention/read gates must block.** Any nudge skippable by an extra click is a",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-LIBRARY-USABILITY-CLEAN-ROOM-2026-08-07.qmd",
   "lines": "65",
   "quote": "One incorrect comprehension response unlocks `Next` while the feedback still says `Pick again`.",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-4/REDTEAM-U1L1-2026-08-05.md",
   "lines": "41",
   "quote": "**one child tap defeats every gate in the lesson** (live-proven)",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-modes-spec.md",
   "lines": "34",
   "quote": "Deterministic span-acceptance rules first; LLM grading only after a calibration pass — until then this step never blocks progression.",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/gauntlet-spec.md",
   "lines": "86-87",
   "quote": "so author annotations (\"possibly removed\") register as false positives.",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "counter",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/gauntlet-spec.md",
   "lines": "38-39",
   "quote": "adversarial framing (\"try to refute that this teaches\")",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
   "lines": "231",
   "quote": "IB quality scores are the MEDIAN of 3 runs (non-determinism precedent: 0.95/0.92/0.98 on identical content).",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
   "lines": "34",
   "quote": "now \"internal cross-bank consistency (synthetic),\" explicitly not MAP agreement",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "20",
   "quote": "sequence items certified against one seeded shuffle; multi-shuffle re-probe decertified 72 incl. one exact 1.000",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/SKILL.md",
   "lines": "110",
   "quote": "advisory until calibrated on academics-labeled anchor lessons",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
   "lines": "102-103",
   "quote": "No auto-score gates progress until the rubric-calibration harness proves LLM-vs-SME agreement",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "208",
   "quote": "`UNIT=2` instead of `U2` matched no lessons — judged 6% of the corpus, printed ALL PASS",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
   "lines": "75",
   "quote": "8 failing fixtures + 1 passing unit, one failing",
   "ok": true
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "77",
   "quote": "camouflage lesson modeled BEFORE the child read the text and set no reading purpose",
   "ok": true
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "643",
   "quote": "J16-LES-002: Provide a complete first encounter before close analysis.",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
   "lines": "208-209",
   "quote": "Two independent instruments landing on one item is the strongest signal in the document, and it is the argument for running both.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
   "lines": "69",
   "quote": "Structurally-verified ≠ instructionally-sound.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "57",
   "quote": "A clean automated report is useful pre-review evidence, never a substitute for reviewer judgment.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/feedback/feedback5/Feedback 11.08.docx",
   "lines": "4 (textutil text)",
   "quote": "no one has managed to come up with a perfect set of rules to get an LLM to generate these without human review yet.",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
   "lines": "5-7",
   "quote": "primary metric, test set, baselines, ceiling, and gates are fixed now; any later change is an appended methodology-correction note, never a rewrite.",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
   "lines": "207",
   "quote": "A gate proven on one surface proves nothing about another.",
   "ok": true
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
   "lines": "86-87",
   "quote": "**Wrong answers must not pass.** Re-run the reviewer's exploit — all-wrong answers through a full lesson — on every delivery surface before any gate claim.",
   "ok": true
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/feedback/feedback1/Reading_Explorers_v2_Feedback (1).docx",
   "lines": "61 (textutil text)",
   "quote": "in a main-idea task we earned the pass while answering every question incorrectly.",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/course-quality.qmd",
   "lines": "61",
   "quote": "A fully green build gate proves the course is well-built. It does not prove the course works.",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
   "lines": "120",
   "quote": "Durable mastery requires a **delayed",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "284-285",
   "quote": "Twice I reported results from a file that moved mid-run.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
   "lines": "24",
   "quote": "Source commit, source digest, release digest, live digest, route, and evidence identify the same immutable artifact.",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/generator-insights.md",
   "lines": "143",
   "quote": "A generator optimizing for pass-rates or engagement will quietly lower rigor",
   "ok": true
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/video-red-team/references/rubric.md",
   "lines": "99-100",
   "quote": "suppressed when a text card shows the same words (r18).",
   "ok": true
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/feedback/feedback5/Feedback 11.08.docx",
   "lines": "10 (textutil text)",
   "quote": "not everything Scout says needs to appear on screen",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D2-opportunities-to-respond.md",
   "lines": "18",
   "quote": "is actually reachable for the child who freezes or says \"I don't know\"",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/generator-insights.md",
   "lines": "71",
   "quote": "**Ungrounded generation is where the 74%-flaw rate lives.**",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
   "lines": "10",
   "quote": "Facts: ONLY this lesson's `lesson.json` passage.",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "168",
   "quote": "Human override cannot erase factual, safety, or integrity failures.",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
   "lines": "308",
   "quote": "Sweep for NEW issues introduced by the fix wave (fixes introduce contradictions:",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/README.md",
   "lines": "132",
   "quote": "scope mismatch, two schema/policy misses, one metadata-confirmed conflict",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D8-text-quality.md",
   "lines": "32",
   "quote": "Reject passages whose graphics decorate rather than carry meaning",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/video-red-team/references/finding-taxonomy.md",
   "lines": "36",
   "quote": "| Decorative filler | b-roll/motion with no fact_id |",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
   "lines": "218",
   "quote": "systematic defect patterns (same defect class across a whole batch = generator prompt bug, not per-item fixes).",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "21",
   "quote": "G5: deploying lane certified its own items until the protocol banned it",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
   "lines": "69-70",
   "quote": "op-lint's deterministic layer catches **6 of the 10 round-2 academics failure shapes**",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "277",
   "quote": "That's a 7,000× difference.",
   "ok": false
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
   "lines": "224-225",
   "quote": "a token which uniquely identifies one item's key must not appear in another item's stem, options, or feedback anywhere in the same lesson",
   "ok": true
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "79",
   "quote": "is the comprehension question bespoke to THIS text, or a generic template?",
   "ok": false
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-1/teacher-skill/gauntlet/layer5/RESULT.md",
   "lines": "34",
   "quote": "**Generic identical feedback on all 16 items**",
   "ok": false
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/plain-english-explainer.md",
   "lines": "40",
   "quote": "Two of those five things actually helped. Three made it worse.",
   "ok": false
  }
 ]
}
```
